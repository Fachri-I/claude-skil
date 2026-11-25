#!/usr/bin/env python3
"""Periksa DESIGN.md terhadap spesifikasi resmi Stitch (google-labs-code/design.md, versi alpha), tanpa jaringan.

Pemakaian: python lint_design.py <path/ke/DESIGN.md>

Keluaran: ERROR (harus diperbaiki) dan WARN (sebaiknya diperbaiki). Exit code 1 bila ada ERROR.
Ini pemeriksaan pendamping yang meniru aturan utama spesifikasi, bukan pengganti linter resmi.
Bila linter resmi tersedia, jalankan juga.
"""
import difflib
import pathlib
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

SECTIONS = [
    ("Overview", ["Brand & Style"]),
    ("Colors", []),
    ("Typography", []),
    ("Layout", ["Layout & Spacing"]),
    ("Elevation & Depth", ["Elevation"]),
    ("Shapes", []),
    ("Motion & Micro-interaction", ["Motion & Micro-interactions", "Motion"]),
    ("Voice & Content Strategy", []),
    ("Components", []),
    ("Do's and Don'ts", []),
]
TOKEN_SECTION = {
    "colors": "Colors", "typography": "Typography", "spacing": "Layout",
    "rounded": "Shapes", "motion": "Motion & Micro-interaction", "components": "Components",
}
TYPO_PROPS = {"fontFamily", "fontSize", "fontWeight", "lineHeight", "letterSpacing", "fontFeature", "fontVariation"}
TYPO_WRONG = {"size": "fontSize", "weight": "fontWeight", "family": "fontFamily", "font": "fontFamily",
              "font-size": "fontSize", "font-weight": "fontWeight", "line-height": "lineHeight",
              "letter-spacing": "letterSpacing"}
COMP_PROPS = {"backgroundColor", "textColor", "typography", "rounded", "padding", "size", "height", "width"}
MOTION_PROPS = {"duration", "delay", "timingFunction"}

HEX = re.compile(r"^#([0-9A-Fa-f]{3,4}|[0-9A-Fa-f]{6}|[0-9A-Fa-f]{8})$")
FUNC = re.compile(r"^(rgb|rgba|hsl|hsla|hwb|oklch|oklab|lch|lab|color-mix)\(", re.I)
DIM = re.compile(r"^-?\d+(\.\d+)?(px|em|rem)$")
DUR = re.compile(r"^\d+(\.\d+)?ms$")
REF = re.compile(r"^\{([^{}]+)\}$")


def norm(s):
    return s.replace("\u2019", "'").strip().lower()


LOOKUP = {}
for i, (canon, aliases) in enumerate(SECTIONS):
    for n in [canon] + aliases:
        LOOKUP[norm(n)] = i


def lum(hexv):
    h = hexv.lstrip("#")
    if len(h) in (3, 4):
        h = "".join(c * 2 for c in h[:3])
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def ratio(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def is_group(node, props):
    """Grup token: dict yang semua isinya dict dan tidak memuat properti token."""
    return isinstance(node, dict) and node and not (set(node) & props) and all(isinstance(v, dict) for v in node.values())


def flatten(node, props, prefix, out):
    for k, v in node.items():
        path = f"{prefix}.{k}"
        if is_group(v, props):
            flatten(v, props, path, out)
        else:
            out[path] = v


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    text = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8").replace("\r\n", "\n")
    res = []  # (level, message)
    E = lambda m: res.append(("ERROR", m))
    W = lambda m: res.append(("WARN", m))

    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    front, body = (m.group(1), text[m.end():]) if m else (None, text)
    blocks = []
    if front is None:
        W("front matter YAML tidak ada di awal berkas (opsional menurut spesifikasi, tetapi token mesin dianjurkan)")
    else:
        blocks.append(front)
    blocks += re.findall(r"```ya?ml\n(.*?)\n```", body, re.S)

    # kunci tingkat atas ganda
    seen = {}
    for b in blocks:
        for k in re.findall(r"^([A-Za-z][\w-]*):", b, re.M):
            seen[k] = seen.get(k, 0) + 1
    for k, n in seen.items():
        if n > 1:
            E(f"kunci YAML tingkat atas '{k}' didefinisikan {n} kali (maksimal satu kali)")

    tokens = {}
    if blocks and yaml is None:
        W("PyYAML tidak tersedia: pemeriksaan token dilewati")
    elif blocks:
        for b in blocks:
            try:
                data = yaml.safe_load(b) or {}
            except yaml.YAMLError as e:
                E(f"YAML tidak valid: {str(e).splitlines()[0]}")
                data = {}
            if isinstance(data, dict):
                for k, v in data.items():
                    tokens.setdefault(k, v)

    if tokens:
        if not tokens.get("name"):
            E("front matter tidak memuat 'name'")
        ver = str(tokens.get("version", ""))
        if ver and ver != "alpha":
            W(f"version '{ver}' tidak dikenal; versi spesifikasi saat ini 'alpha' (keterangan taruh di 'description')")

        prims = {}   # path -> nilai primitif
        comps = {}   # path -> token komposit (typography, motion, components)

        # colors
        colors = tokens.get("colors") or {}
        flat = {}
        if isinstance(colors, dict):
            flatten(colors, set(), "colors", flat)
        for p, v in flat.items():
            if not isinstance(v, str) or not (HEX.match(v) or FUNC.match(v) or re.fullmatch(r"[A-Za-z]+", v)):
                E(f"{p}: nilai warna tidak valid ({v!r})")
            else:
                prims[p] = v
        if "colors" in tokens and not any(p.split(".")[-1] == "primary" or ".primary" in p or p.split(".")[-1].startswith("primary-") for p in flat):
            E("colors: palet 'primary' wajib ada")

        # typography
        typo = tokens.get("typography") or {}
        tflat = {}
        if isinstance(typo, dict):
            flatten(typo, TYPO_PROPS, "typography", tflat)
        for p, v in tflat.items():
            if not isinstance(v, dict):
                E(f"{p}: harus berupa token berisi properti (fontFamily, fontSize, ...), bukan nilai tunggal {v!r}")
                continue
            comps[p] = v
            for k, val in v.items():
                if k in TYPO_WRONG:
                    E(f"{p}.{k}: nama properti salah, pakai '{TYPO_WRONG[k]}'")
                elif k not in TYPO_PROPS:
                    W(f"{p}.{k}: properti tidak dikenal")
                elif k in ("fontSize", "letterSpacing") and not DIM.match(str(val)):
                    E(f"{p}.{k}: dimensi harus memakai satuan px, em, atau rem ({val!r})")
                elif k == "lineHeight" and not (DIM.match(str(val)) or isinstance(val, (int, float))):
                    E(f"{p}.lineHeight: dimensi atau angka tanpa satuan ({val!r})")
                elif k == "fontWeight" and not str(val).isdigit():
                    E(f"{p}.fontWeight: harus angka ({val!r})")
            for need in ("fontFamily", "fontSize"):
                if need not in v and not any(w in v for w in TYPO_WRONG):
                    W(f"{p}: tidak punya '{need}'")

        # rounded dan spacing
        for key in ("rounded", "spacing"):
            sect = tokens.get(key) or {}
            if not isinstance(sect, dict):
                E(f"{key}: harus berupa map")
                continue
            sflat = {}
            flatten(sect, set(), key, sflat)
            for p, v in sflat.items():
                if isinstance(v, (list, tuple)):
                    E(f"{p}: array tidak didukung; ubah menjadi map nama ke dimensi (xs: 4px, sm: 8px, ...)")
                elif isinstance(v, bool) or v is None or isinstance(v, dict):
                    E(f"{p}: nilai tidak valid ({v!r})")
                elif key == "rounded" and not DIM.match(str(v)):
                    E(f"{p}: dimensi harus memakai satuan px, em, atau rem ({v!r})")
                elif key == "spacing" and not (isinstance(v, (int, float)) or DIM.match(str(v))):
                    W(f"{p}: bukan dimensi atau angka ({v!r}); akan disimpan sebagai teks")
                else:
                    prims[p] = v

        # motion
        motion = tokens.get("motion") or {}
        if isinstance(motion, dict):
            for name, v in motion.items():
                p = f"motion.{name}"
                if not isinstance(v, dict):
                    E(f"{p}: harus berisi duration, delay, timingFunction")
                    continue
                comps[p] = v
                for k, val in v.items():
                    if k not in MOTION_PROPS:
                        W(f"{p}.{k}: properti tidak dikenal")
                    elif k in ("duration", "delay") and not DUR.match(str(val)):
                        E(f"{p}.{k}: durasi harus berakhiran ms ({val!r})")

        # components
        cmp_ = tokens.get("components") or {}
        if isinstance(cmp_, dict):
            for name, v in cmp_.items():
                p = f"components.{name}"
                if not isinstance(v, dict):
                    E(f"{p}: harus berupa map properti")
                    continue
                comps[p] = v
                for k in v:
                    if k not in COMP_PROPS:
                        W(f"{p}.{k}: properti komponen tidak dikenal")

        # referensi
        def resolve(val, where, allow_comp):
            mm = REF.match(val) if isinstance(val, str) else None
            if not mm:
                return val
            path = mm.group(1).strip()
            if path in prims:
                return prims[path]
            if path in comps:
                if not allow_comp:
                    E(f"{where}: referensi {{{path}}} menunjuk token komposit; hanya boleh di dalam components")
                return None
            E(f"{where}: referensi {{{path}}} tidak ditemukan")
            return None

        for sect in ("colors", "rounded", "spacing"):
            s = tokens.get(sect)
            if isinstance(s, dict):
                f2 = {}
                flatten(s, set(), sect, f2)
                for p, v in f2.items():
                    if isinstance(v, str) and REF.match(v):
                        resolve(v, p, False)
        for p, v in comps.items():
            if not p.startswith("components."):
                continue
            for k, val in v.items():
                if isinstance(val, str) and REF.match(val):
                    resolve(val, f"{p}.{k}", True)

        # kontras pasangan teks dan latar pada komponen
        for p, v in comps.items():
            if not p.startswith("components."):
                continue
            bg = resolve(v.get("backgroundColor"), p, True) if v.get("backgroundColor") else None
            fg = resolve(v.get("textColor"), p, True) if v.get("textColor") else None
            if isinstance(bg, str) and isinstance(fg, str) and HEX.match(bg) and HEX.match(fg):
                r = ratio(bg, fg)
                if r < 4.5:
                    E(f"{p}: kontras teks/latar {r:.2f}:1 di bawah 4,5:1")

    # bagian markdown
    titles, in_fence = [], False
    for line in body.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
        elif not in_fence:
            mh = re.match(r"^## (.+?)\s*$", line)
            if mh:
                titles.append(mh.group(1))
    names_seen, order = {}, []
    for t in titles:
        stripped = re.sub(r"^\d+[.)]\s+", "", t)
        if stripped != t:
            W(f"judul '{t}' diberi nomor; hapus nomor agar dikenali sebagai bagian baku")
        n = norm(stripped)
        names_seen[n] = names_seen.get(n, 0) + 1
        if n in LOOKUP:
            order.append((LOOKUP[n], stripped))
        else:
            close = difflib.get_close_matches(n, list(LOOKUP), n=1, cutoff=0.6)
            if "&" in stripped and any(w in n for w in ("shape", "elevation")):
                W(f"judul '{stripped}' bukan nama baku; pisah menjadi 'Elevation & Depth' dan 'Shapes'")
            elif close:
                W(f"judul '{stripped}' bukan nama baku; mirip '{SECTIONS[LOOKUP[close[0]]][0]}'")
    for n, c in names_seen.items():
        if c > 1:
            E(f"judul bagian '{n}' muncul {c} kali")
    idx = [i for i, _ in order]
    if idx != sorted(idx):
        E("urutan bagian baku salah: " + " > ".join(s for _, s in order) + "; urutan seharusnya " + " > ".join(c for c, _ in SECTIONS))
    present = {SECTIONS[i][0] for i in idx}
    for key, sect in TOKEN_SECTION.items():
        if tokens and key in tokens and sect not in present:
            W(f"token '{key}' ada tetapi bagian '{sect}' tidak ada atau tidak dikenali")

    errs = sum(1 for lv, _ in res if lv == "ERROR")
    for lv, msg in res:
        print(f"{lv:5} {msg}")
    print("OK" if not errs else f"{errs} error(s)")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()

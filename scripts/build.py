#!/usr/bin/env python3
"""Validasi dan kemas skill menjadi zip siap unggah ke Claude.

Pemakaian:
  python scripts/build.py --all
  python scripts/build.py prd-builder techstack-recommender

Hasil: dist/<nama-skill>.zip (folder <nama-skill>/ berada di akar zip).
Skrip ini hanya memakai pustaka standar Python, jadi jalan di Windows/macOS/Linux.
"""
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
DIST = ROOT / "dist"

ALLOWED_KEYS = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
EXCLUDE_FILES = {"CHANGELOG.md", ".DS_Store"}
EXCLUDE_DIRS = {"__pycache__", ".git"}


def read_frontmatter(skill_md: Path) -> dict:
    text = skill_md.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        raise ValueError("frontmatter YAML tidak ditemukan di awal SKILL.md")
    fm = {}
    for line in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)  # hanya key tingkat atas
        if km:
            fm[km.group(1)] = km.group(2).strip().strip('"').strip("'")
    return fm


def changelog_version(changelog: Path):
    if not changelog.exists():
        return None
    m = re.search(r"^## \[(\d+\.\d+\.\d+)\]", changelog.read_text(encoding="utf-8"), re.M)
    return m.group(1) if m else None


def validate(name: str):
    errors = []
    folder = SKILLS / name
    skill_md = folder / "SKILL.md"
    if not folder.is_dir():
        return [f"folder skills/{name} tidak ada"], None
    if not skill_md.is_file():
        return [f"skills/{name}/SKILL.md tidak ada (nama harus persis SKILL.md)"], None
    try:
        fm = read_frontmatter(skill_md)
    except ValueError as e:
        return [str(e)], None

    unexpected = set(fm) - ALLOWED_KEYS
    if unexpected:
        errors.append(f"key frontmatter tidak diizinkan: {', '.join(sorted(unexpected))}")
    if fm.get("name") != name:
        errors.append(f"frontmatter name '{fm.get('name')}' tidak sama dengan nama folder '{name}'")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
        errors.append("nama folder harus kebab-case (huruf kecil, angka, tanda hubung), maks 64 karakter")
    desc = fm.get("description", "")
    if not desc:
        errors.append("description kosong")
    if len(desc) > 1024:
        errors.append(f"description terlalu panjang ({len(desc)} > 1024)")
    if "<" in desc or ">" in desc:
        errors.append("description tidak boleh mengandung tanda < atau >")

    version = changelog_version(folder / "CHANGELOG.md")
    if version is None:
        errors.append("CHANGELOG.md tidak ada atau tidak punya entri '## [X.Y.Z]'")
    return errors, version


def build(name: str) -> Path:
    folder = SKILLS / name
    DIST.mkdir(exist_ok=True)
    out = DIST / f"{name}.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(folder.rglob("*")):
            rel = path.relative_to(folder)
            if path.is_dir():
                continue
            if path.name in EXCLUDE_FILES or any(p in EXCLUDE_DIRS for p in rel.parts):
                continue
            zf.write(path, arcname=f"{name}/{rel.as_posix()}")
    return out


def main(argv):
    if not SKILLS.is_dir():
        print("folder skills/ tidak ditemukan", file=sys.stderr)
        return 2
    if not argv:
        print(__doc__)
        return 2
    if argv == ["--all"]:
        names = sorted(p.name for p in SKILLS.iterdir() if p.is_dir())
    else:
        names = argv

    failed = False
    for name in names:
        errors, version = validate(name)
        if errors:
            failed = True
            print(f"[GAGAL] {name}")
            for e in errors:
                print(f"        - {e}")
            continue
        out = build(name)
        print(f"[OK]    {name} v{version} -> {out.relative_to(ROOT).as_posix()}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

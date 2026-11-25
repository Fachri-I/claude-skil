# Panduan: 00-konsistensi-aset-style.md dan blok identik

Tujuan: hasil Stitch seragam di semua layar dan semua peran, dimulai dari aset yang dikunci sampai gaya visual. Semua nilai `<...>` diambil dari DESIGN.md (yang berasal dari audit); jangan menambah nilai baru di sini.

## Blok yang disimpan di `src/blocks/` (dipakai lewat placeholder)

| File blok | Placeholder | Isi |
|---|---|---|
| `global.txt` | `{{GLOBAL}}` | Global Prompt (template di bawah) |
| `reminder.txt` | `{{REMINDER}}` | Prompt Pengingat, versi singkat Global Prompt |
| `guard.txt` | `{{GUARD}}` | Kalimat penjaga konten |
| `ds.txt` | `{{DS}}` | `Use the global design system.` |
| `refine.txt` | `{{REFINE}}` | Set refinement umum R1-R12 (template di bawah) |

Kalimat penjaga (`guard.txt`): `Use ONLY the content listed here. Do not add or invent sections, copy, badges, statistics, logos, testimonials, pricing or claims; omit any detail not specified.`

## Struktur file 00

```markdown
# Prompt Konsistensi Aset dan Style: <Project>
> Tujuan, prinsip (aset dikunci, design system sekali, papan komponen, jangkar, lalu layar lain).
## 1. Kunci aset              <- tabel: aset | pilihan terkunci | catatan
## 2. Urutan kerja            <- 8 langkah
## 3. Global Prompt           <- {{GLOBAL}} (salinan induk)
## 4. Design System Board     <- prompt papan komponen
## 5. Kunci jangkar           <- satu prompt per peran
## 6. Awalan jangkar          <- awalan untuk tiap prompt layar baru
## 7. Audit konsistensi       <- prompt audit
## 8. Checklist manual        <- 10 poin
## 9. Bila Stitch tetap menyimpang  <- tabel gejala dan tindakan
```

### 1. Kunci aset (baris wajib)

Font; set ikon (nama, gaya, stroke, ukuran, larangan terisi dan emoji); logo (bentuk, warna, wordmark; beri label **Asumsi** bila tidak ada di sumber); poster atau gambar (gradien kategori, tanpa foto/stok/ilustrasi); avatar; QR atau elemen khusus produk; empty state; panel merek auth; aturan data contoh (label sample, tanggal dan hari benar, zona waktu, tanpa statistik fiktif); bahasa dan mode (gelap atau terang).

### 2. Urutan kerja (tetap)

1. Buat project Stitch, unggah `DESIGN.md`. 2. Tempel Global Prompt. 3. Buat Design System Board, perbaiki dengan R1-R5. 4. Buat layar jangkar, setujui, tempel Kunci jangkar. 5. Buat layar lain dalam batch maksimal 5, awali dengan Awalan jangkar. 6. Audit konsistensi pada satu layar acak tiap batch. 7. Perbaiki satu aspek per prompt. 8. Bila beberapa layar berturut-turut menyimpang, tempel Prompt Pengingat lalu ulangi layar itu.

## Template Global Prompt

Susun dari DESIGN.md; urutan bagian tetap.

```
Design a responsive web interface (desktop 1440px, tablet 768px, mobile 375px) for "<Product>", <one-line product and roles>. All UI text is in <UI language>. Treat this message as the permanent design system; every later screen must follow it exactly.
Style: <3-5 adjectives>. <Light/dark mode statement>.

COLORS (exact hex values, no others):
- Brand: primary <hex> (hover <hex>), primary-soft <hex>, link and active text <hex>, text on primary <hex>
- Neutrals: canvas, surface, border, input border, text, muted text, subtle text (with where it may be used)
- Status (text / background / border): success, warning, danger (solid hover), info
- Categories (label text / label bg / poster gradient from to): <one per category>
- Disabled controls: background <hex>, text <hex>

TYPOGRAPHY: <font> only. <full scale as size/line-height weight>. <Where monospace is allowed>.
SHAPE AND SPACING: <radii per component>, <shadow values>, <border>, <spacing scale, max width, page margins>.
NAVIGATION: <header height>; <desktop sidebar width and active style>; <tablet rail>; <mobile bottom bar>. Sidebar items per role: <role = items; ...>. <Public header; auth split layout and brand panel>.
LOCKED ASSETS: <logo>; <icon set, stroke, sizes, bans>; <poster policy>; <avatar>; <product-specific assets>; <empty state>.
COMPONENTS: <button variants and size; one primary per area>; <input>; <badge>; <quota or progress>; <dialog>; <toast>; <dropzone>; <table behavior on mobile>.
STATUS LABELS (never show raw enum names): <per entity: label (color family)>.
DATA: <time and number format; sample data policy>.
AVOID: <dark mode, extra gradients, stock photos, emoji, glows, new accent hues, fictional statistics, logos, testimonials, pricing, claims>. Never add content that a screen prompt does not list.
Acknowledge in one line, then wait: I will request screens one by one.
```

Aturan: setiap hex di DESIGN.md harus muncul di sini dan sebaliknya; tidak ada hex lain.

## Template Prompt Pengingat (`reminder.txt`, sekitar 80 kata)

`Reminder of the <Product> design system, apply it unchanged: <font>; <primary and hover>, soft, canvas, surface, border, input border, text, muted, subtle; status triplets ...; radius ...; 44px controls; <icon set> only; category gradients for posters, no photos; one primary button per area; status always as a text pill; <UI language> copy; nothing added beyond the listed content.`

## Template Design System Board

Satu layar referensi, bukan halaman produk, lebar 1440px di atas warna canvas. Bagian atas ke bawah: 1) swatch warna dengan nama dan hex, dikelompokkan Brand, Neutrals, Status, Categories; 2) tipografi satu baris per gaya; 3) tombol semua varian dan state (default, hover, fokus, nonaktif, loading); 4) input (default, fokus, error, nonaktif, select, textarea, checkbox, toggle, dropzone); 5) badge dan pill; 6) alert dan toast; 7) navigasi (sidebar aktif dan tidak aktif, tab bawah, tab pill dengan hitungan, stepper); 8) blok konten (kartu utama produk, header tabel dan satu baris, empty state, satu dialog); 9) aset (logo, avatar, enam ikon yang dipakai produk). Akhiri dengan `Use the global design system. {{GUARD}}`. Target kurang dari 270 kata.

## Template Kunci jangkar (satu per peran)

`Keep everything else unchanged. Treat this screen as the style anchor for the <Product> <role> screens: from now on reuse its <komponen kunci peran itu> exactly, and do not restyle them on later screens.`

## Template Awalan jangkar

`Use the existing anchor screen as the visual reference: copy its header, sidebar or bottom navigation, cards, buttons, badges, tables and spacing exactly. The content and layout of this new screen follow the description below, and the global design system still applies.`

## Template Audit konsistensi

`Audit this screen against the <Product> design system and fix every deviation, keeping the layout and copy unchanged. Check and correct: (1) only the listed hex colors are used; (2) <font> and the type scale; (3) control heights and radii; (4) at most one solid primary button per area; (5) every status is a text pill with the exact status triplet; (6) <icon set> only, no emoji, no photos, no illustrations; (7) the correct navigation items for this role, active item styled correctly; (8) quota or data format and time zones; (9) subtle text never on the border-colored background; (10) no content, statistics, logos or claims that were not requested. {{GUARD}}`

## Set refinement umum (`refine.txt`, R1-R12)

Tiap item: `- [ ] **R<n> <nama>**` + blok kode yang diawali `Keep everything else unchanged.` dan diakhiri `{{GUARD}}`.
R1 palet (sebut hex token inti, ganti warna lain ke token terdekat); R2 warna status (tiga hex per status); R3 tipografi (font dan skala); R4 bentuk dan tinggi kontrol (radius, tinggi, shadow kartu); R5 ikon dan aset (set ikon, hapus terisi dan emoji, ganti foto dengan gradien kategori, logo tetap); R6 satu tombol primer per area; R7 tombol nonaktif; R8 teks subtle tidak di atas warna border; R9 hapus konten tambahan; R10 label kuota/data dan zona waktu; R11 cincin fokus dan target 44px; R12 varian mobile (tumpuk kolom, tabel jadi kartu, sidebar jadi tab bawah, tombol utama penuh lebar).

## Checklist manual (10 poin)

Hex hanya dari DESIGN.md; font dan skala; tinggi dan radius kontrol; satu tombol primer per area; status berupa pill bertulisan; set ikon dan tanpa foto; navigasi sesuai peran; bahasa, zona waktu, format angka; tanpa konten tambahan; tampilan 375px tanpa scroll horizontal.

## Tabel troubleshooting (gejala, tindakan)

Ikon salah gaya: R5 lalu Pengingat. Warna berbeda: R1 lalu R2. Foto atau ilustrasi muncul: R5 dan R9. Dua tombol primer: R6. Layar baru berbeda: Awalan jangkar lalu ulangi. Teks tambahan: R9. Beberapa perbaikan saling menimpa: satu prompt per perbaikan.

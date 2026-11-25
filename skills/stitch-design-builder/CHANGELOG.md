# Changelog — stitch-design-builder

Versi mengikuti SemVer (MAJOR.MINOR.PATCH). Entri terbaru ada di paling atas.

## [2.0.0] - 2026-11-25

### Changed
- `DESIGN.md` kini mengikuti spesifikasi resmi Stitch (alpha): front matter YAML dengan token `colors`, `typography`, `rounded`, `spacing`, `motion`, `components`; bagian baku berurutan (Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Motion & Micro-interaction, Voice & Content Strategy, Components, Do's and Don'ts); bagian tambahan (Iconography & Imagery, Accessibility) dipertahankan.
- Properti token typography memakai `fontFamily`, `fontSize`, `fontWeight`, `lineHeight`, `letterSpacing` (sebelumnya `size`/`weight` dan `fontFamily` tunggal). `spacing` berupa map nama ke dimensi (sebelumnya array `scale`). Judul bagian tanpa nomor dan memakai nama baku.
- Langkah 1 menambah aturan untuk DESIGN.md yang sudah ada di input: format resmi dipertahankan utuh (termasuk data dari skill Design Direction seperti `Dial:`), format lama dikonversi tanpa mengubah nilai.

### Added
- `scripts/lint_design.py`: pemeriksa offline DESIGN.md terhadap spesifikasi resmi (nama properti, satuan dimensi, rujukan token, urutan dan nama bagian, kontras pasangan komponen). Dijalankan di Langkah 5 setelah `check.py`.
- Token `components` dan `motion` di DESIGN.md, dan bagian Voice & Content Strategy.

## [1.0.0] - 2026-11-24

### Added
- Impor awal ke repositori. Isi sama dengan versi yang terpasang di akun Claude saat ini.

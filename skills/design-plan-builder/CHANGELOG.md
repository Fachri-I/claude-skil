# Changelog — design-plan-builder

Versi mengikuti SemVer (MAJOR.MINOR.PATCH). Entri terbaru ada di paling atas.

## [1.1.0] - 2026-11-26

### Added
- Mockup kini dibuat dalam dua tahap. Tahap 1: pratinjau selalu ditampilkan lebih dulu sebagai artifact di chat (satu halaman mandiri dengan CSS di dalamnya, navigasi antar halaman, revisi pada artifact yang sama). Tahap 2: setelah user menyetujui, artifact diubah menjadi berkas HTML untuk setiap halaman lengkap dengan `styles.css` bersama dan `index.html`.
- Aturan persetujuan eksplisit sebelum Tahap 2, batas cakupan pratinjau (maksimal enam halaman kunci bila halaman banyak), pemeriksaan sebelum menyerahkan, dan dua butir baru di daftar periksa.

### Changed
- Tokens dikunci ke Shared Contract setelah mockup disetujui (sebelumnya setelah tokens disetujui). Revisi mockup yang mengubah token atau halaman disinkronkan ke `UIUX_<project>.md`.
- Aturan mockup HTML dipecah menjadi Tahap 1, Tahap 2, dan aturan yang berlaku untuk kedua tahap.

## [1.0.0] - 2026-11-24

### Added
- Impor awal ke repositori. Isi sama dengan versi yang terpasang di akun Claude saat ini.

# Changelog — design-plan-builder

Versi mengikuti SemVer (MAJOR.MINOR.PATCH). Entri terbaru ada di paling atas.

## [1.2.0] - 2026-11-26

### Added
- Spesifikasi gerak dan interaksi di `UIUX_<project>.md` (item 9): tingkat gerak dan alasannya, token gerak, tabel efek per halaman (pemicu, efek, token, library, fallback `prefers-reduced-motion`), dan kebijakan smooth scroll.
- Bagian "Animasi dan gerak" di `FRONTEND_<project>.md` (item 11): library terpilih, impor modular, konstanta token gerak, pembungkus, pembersihan, lazy loading, reduced-motion terpusat, dan anggaran kinerja.
- Referensi baru `references/motion.md`: tingkat gerak 1 sampai 3, pemilihan CSS, Motion, GSAP, dan Lenis, aturan kinerja dan aksesibilitas, serta format spesifikasi.
- Pertanyaan tingkat gerak bila tidak ada `DESIGN.md`; `DESIGN.md` dari design-direction-builder dibaca sebagai input opsional di Fase 0.
- Pemeriksaan konsistensi Fase 6 dan satu butir daftar periksa: library gerak harus tercantum di `techstack.md`, setiap efek punya fallback reduced-motion, token gerak identik antar file.
- Aturan mockup: gerak hanya didekati dengan CSS, tanpa memuat library gerak.

### Changed
- Design tokens di UI/UX kini mencakup token gerak (durasi dan easing) dan ikut dikunci ke Shared Contract.
- Item "Konvensi kode, linting, dan testing" di `FRONTEND_<project>.md` bergeser dari nomor 11 ke 12.

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

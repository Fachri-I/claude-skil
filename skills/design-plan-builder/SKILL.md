---
name: "design-plan-builder"
description: Membuat rancangan kerja pembangunan website (UI/UX, Frontend, Backend) dalam file .md plus mockup HTML statis, dari PRD, techstack, dan file pendukung, agar fitur, tampilan, API, dan database konsisten. Gunakan skill ini setiap kali user ingin membuat rancangan kerja, design plan, blueprint, atau rancangan teknis website/web app dari PRD, ingin menyelaraskan UI/UX dengan frontend dan backend, ingin membuat task.md atau security.md, atau menyebut PRD_nama-project.md dan techstack.md, walaupun user tidak menyebut kata "skill". Also use when the user asks for a UI/UX, frontend, and backend plan for a website from a PRD. Skill ini melanjutkan hasil skill PRD Builder.
---

# Design Plan Builder

Skill ini mengubah PRD, techstack, dan file pendukung menjadi satu paket rancangan kerja yang konsisten dari fitur sampai tampilan, untuk tiga role: **UI/UX, Frontend, Backend**. Hasilnya berupa file `.md` dan mockup HTML statis.

Konsistensi adalah tujuan utama. Semua keputusan penting (fitur, nama, warna, halaman, endpoint, tabel) ditulis **sekali** di Shared Contract, lalu dirujuk oleh ketiga role. Jangan menduplikasi atau menamai ulang hal yang sama di file lain.

## Aturan umum

- **Bahasa:** default Bahasa Indonesia untuk semua file hasil dan percakapan. Jika input user berbahasa Inggris, ikuti bahasa user. Istilah teknis, nama kode, route, dan field tetap dalam bahasa Inggris.
- **Sesuaikan dengan techstack.** Semua kode, struktur folder, library, dan konvensi mengikuti `techstack.md`. Jangan memakai stack lain. Jika techstack tidak lengkap (misalnya belum ada ORM atau library UI), tanyakan dulu.
- **Jangan mengarang.** Jika informasi di PRD tidak cukup untuk memutuskan sesuatu, tanyakan ke user atau tandai `[PERLU KONFIRMASI]`. Jangan diam-diam membuat asumsi besar.
- **Kedalaman:** sampai detail teknis. Struktur folder, skema tabel, kontrak API lengkap, props komponen, contoh kode kunci, dan aturan keamanan.
- **Tanya satu topik per giliran.** Jangan membanjiri user dengan pertanyaan. Kelompokkan maksimal 3 pertanyaan terkait.

## Alur kerja

Jalankan fase berurutan. Setelah tiap fase selesai, beri ringkasan singkat dan minta persetujuan user sebelum lanjut, kecuali user meminta langsung selesai.

### Fase 0: Pengecekan input

Minta user menyerahkan file perancangan. Periksa apa yang ada:

| File | Status | Isi minimum yang dicari |
|---|---|---|
| `PRD_<project>.md` | Wajib | tujuan, target user, daftar fitur, alur utama, batasan |
| `techstack.md` | Wajib | frontend, backend, database, auth, hosting, library UI |
| File pendukung | Opsional | `user-flow.md`, skema DB awal, brand guideline, `DESIGN.md` (dari design-direction-builder), aturan bisnis, `task.md`/`security.md` yang sudah ada |

Aturan:
- Jika PRD atau techstack belum ada, hentikan dan beri tahu user. Sarankan membuatnya dengan skill PRD Builder.
- Jika ada, baca semuanya, lalu laporkan: apa yang sudah cukup, apa yang kurang, dan apa yang belum bisa dirancang karena itu.
- Jika `task.md` atau `security.md` sudah ada, gunakan sebagai dasar dan perbarui (lihat Fase 5), jangan menimpa.

### Fase 1: Shared Contract

Ekstrak dari input lalu susun kamus konsistensi. Simpan di bagian awal `DESIGN_PLAN_<project>.md`:

1. **Daftar fitur dengan ID** (`F-01`, `F-02`, ...): nama, deskripsi singkat, prioritas (Must/Should/Could), role pengguna yang terlibat.
2. **Glosarium & penamaan:** nama entitas, istilah bisnis, dan konvensi penamaan (file, komponen, route, tabel, field, endpoint). Satu istilah, satu nama.
3. **Peta halaman:** ID halaman (`P-01`, ...), nama, route, fitur yang dilayani.
4. **Design tokens:** diisi setelah Fase 2, lalu dikunci.
5. **Kontrak API:** diisi di Fase 3.
6. **Matriks keterlacakan:** diisi bertahap, diselesaikan di Fase 6.

Minta persetujuan user atas daftar fitur dan peta halaman sebelum lanjut, karena semua fase berikutnya bergantung padanya.

### Fase 2: UI/UX

**Langkah wajib pertama: tanya referensi desain.** Tanyakan:

> "Apakah Anda punya referensi desain (gambar, link, screenshot, brand guideline), atau pernah membuat desain dari PRD ini sebelumnya (misalnya dari Figma, mockup lama, atau hasil AI lain)?"

- **Jika ada referensi:** analisis dulu (warna, tipografi, spacing, radius, gaya komponen, pola layout, nuansa). Jadikan sumber design tokens. Halaman yang tidak tercakup referensi **disesuaikan** dengan gaya yang sama, bukan didesain ulang dari nol. Catat di `UIUX_<project>.md` bagian "Sumber & adaptasi": mana yang berasal dari referensi dan mana yang diturunkan.
- **Jika tidak ada:** rancang sendiri. Tanyakan dulu preferensi singkat bila belum ada di PRD (nuansa/brand, warna utama, mode gelap perlu atau tidak). Lalu pilih arah visual yang sesuai tujuan dan target user di PRD, dan jelaskan alasannya dalam satu-dua kalimat. Hindari tampilan generik; buat pilihan tipografi dan warna yang disengaja.

Isi `UIUX_<project>.md`:

1. Sumber & adaptasi desain
2. Prinsip desain dan nuansa
3. **Design tokens** (warna dengan nama semantik, tipografi, skala spacing, radius, shadow, token gerak berupa durasi dan easing, breakpoint, mode terang/gelap bila perlu), ditulis sebagai tabel **dan** blok CSS variables
4. Pola komponen (button, input, card, modal, tabel, navigasi, notifikasi) dengan varian dan state: default, hover, focus, disabled, loading, error
5. **Per halaman (P-xx):** tujuan, fitur terkait (F-xx), struktur layout (wireframe teks), komponen yang dipakai, state (kosong, loading, error, sukses), perilaku responsif
6. Alur pengguna (user flow) antar halaman
7. Aksesibilitas: kontras, fokus keyboard, label, ukuran target sentuh
8. Microcopy utama (judul, tombol, pesan error) bila relevan
9. **Spesifikasi gerak & interaksi** (format dan panduan di `references/motion.md`): tingkat gerak beserta alasannya, tabel efek per halaman (pemicu, efek, token, library, fallback `prefers-reduced-motion`), dan kebijakan smooth scroll. Library gerak hanya boleh dari `techstack.md`; bila belum tercantum, tandai `[PERLU KONFIRMASI]` dan tanyakan, jangan menambahkannya sendiri.

**Gerak:** tujuannya agar website terasa hidup tanpa menjadi berat. Bila ada `DESIGN.md` dengan baris `Dial:`, ikuti nilai MOTION-nya. Bila tidak ada, tanyakan satu pertanyaan pilihan (minimal, seimbang, atau ekspresif; jelaskan tiap pilihan dalam satu kalimat), lalu catat jawaban dan alasannya di spesifikasi gerak.

**Mockup dalam dua tahap** (wajib, aturan lengkap di bagian "Aturan mockup HTML"):

1. **Pratinjau sebagai artifact.** Pertama kali mockup selalu ditampilkan sebagai artifact di chat, bukan langsung sebagai berkas. Revisi dikerjakan pada artifact yang sama.
2. **Berkas HTML per halaman.** Hanya setelah user menyatakan mockup disetujui, ubah menjadi berkas HTML untuk setiap halaman lengkap dengan CSS.

Setelah mockup disetujui, **kunci** tokens (termasuk token gerak) ke Shared Contract. Frontend wajib memakai nama token yang sama. Bila revisi mockup mengubah token, halaman, atau komponen, perbarui `UIUX_<project>.md` agar tetap sama dengan artifact sebelum meminta persetujuan.

### Fase 3: Kontrak API

Dari fitur (F-xx) dan halaman (P-xx), turunkan kontrak API. Untuk tiap endpoint tulis: method, path, deskripsi, auth/role yang boleh, parameter, body request, body response sukses (contoh JSON), daftar error (kode + pesan), dan fitur/halaman yang memakainya. Tetapkan format respons dan error yang seragam di seluruh API. Bila techstack bukan REST (GraphQL, tRPC, server actions), sesuaikan bentuk kontraknya.

Kontrak ini disimpan di Shared Contract dan menjadi sumber tunggal bagi Frontend dan Backend.

### Fase 4: Frontend dan Backend

Kerjakan setelah UI/UX dan kontrak API terkunci. Keduanya mengacu pada Shared Contract.

**`FRONTEND_<project>.md`** memuat:
1. Ringkasan stack dan alasan pilihan library (sesuai techstack)
2. Struktur folder lengkap
3. Routing: tabel route ↔ halaman (P-xx) ↔ guard/akses
4. Implementasi design tokens (file konfigurasi tema/CSS variables, nama sama dengan UI/UX)
5. Daftar komponen: nama, props (tipe), state, event, dan halaman pemakainya; contoh kode untuk komponen kunci
6. State management dan data fetching (cache, invalidasi, loading/error handling)
7. Integrasi API: client, penanganan error, pemetaan endpoint ↔ komponen/halaman
8. Form dan validasi (skema validasi selaras dengan Backend)
9. Auth di sisi klien (penyimpanan sesi/token, route guard)
10. Performa, SEO, dan aksesibilitas yang relevan
11. Animasi dan gerak (panduan di `references/motion.md`): library dan impor modular, konstanta token gerak (nama sama dengan UI/UX), komponen atau hook pembungkus, pola cleanup, lazy loading, penanganan `prefers-reduced-motion` terpusat, dan anggaran kinerja. Bila gerak hanya memakai CSS, cukup token dan aturan reduced-motion.
12. Konvensi kode, linting, dan testing

**`BACKEND_<project>.md`** memuat:
1. Ringkasan stack dan arsitektur (layering, modul)
2. Struktur folder lengkap
3. **Skema database:** tabel, kolom, tipe, constraint, relasi, index, dan diagram ERD (Mermaid). Penamaan mengikuti glosarium.
4. Migrasi dan seed data
5. Implementasi kontrak API per endpoint: handler/service/repository, validasi, aturan bisnis; contoh kode untuk alur kunci
6. Autentikasi dan otorisasi (role/permission, matriks akses per endpoint)
7. Penanganan error dan format respons seragam
8. Logging, monitoring, dan konfigurasi environment (daftar variabel, tanpa nilai rahasia)
9. Background job, upload file, integrasi pihak ketiga bila ada di PRD
10. Testing dan strategi deployment sesuai techstack

### Fase 5: File pendukung

**`security.md`:** aturan keamanan website yang disesuaikan dengan techstack dan fitur. Minimal mencakup:
- autentikasi, manajemen sesi/token, kebijakan password, dan rate limiting
- otorisasi (RBAC) dan pencegahan IDOR
- validasi dan sanitasi input; pencegahan injeksi (SQL/NoSQL), XSS, CSRF
- header keamanan, CORS, HTTPS, cookie flags
- upload file (tipe, ukuran, penyimpanan aman)
- pengelolaan secret dan environment variable
- perlindungan data pribadi, enkripsi, dan backup
- logging keamanan, penanganan error tanpa membocorkan detail
- keamanan dependensi dan checklist sebelum rilis

Beri ID aturan (`S-01`, ...) dan petakan tiap aturan ke endpoint/halaman yang terkena bila relevan.

**`task.md`:** pelacak pekerjaan untuk project yang dikerjakan bersama. Format:

```
| ID Tugas | Fitur | Role (UI/UX/FE/BE) | Deskripsi | Status | Penanggung jawab | Catatan |
```

Status: `Belum` / `Sedang dikerjakan` / `Review` / `Selesai` / `Terblokir`. Pecah tiap fitur (F-xx) menjadi tugas per role, urut sesuai ketergantungan (UI/UX → kontrak API → FE & BE paralel → integrasi → testing). Tambahkan bagian "Riwayat perubahan" berisi tanggal dan ringkasan.

**Mode pembaruan:** jika `task.md` sudah ada saat skill dipakai lagi, jangan buat ulang. Pertahankan status yang sudah ada, tambahkan tugas baru, perbarui status sesuai info dari user, dan catat di riwayat. Perlakuan yang sama berlaku untuk `security.md` yang sudah ada: tambahkan atau revisi, jangan timpa tanpa persetujuan.

### Fase 6: Pengecekan konsistensi dan penutup

1. Lengkapi **matriks keterlacakan**:

```
| Fitur | Halaman | Komponen | Endpoint | Tabel DB | Aturan keamanan |
```

2. Periksa dan laporkan temuan:
   - fitur tanpa halaman, endpoint, atau tabel
   - endpoint atau tabel yang tidak dipakai fitur mana pun
   - perbedaan nama (entitas, field, token) antar file
   - halaman di UI/UX yang tidak punya route di Frontend, atau sebaliknya
   - field di form yang tidak ada di request API atau skema database
   - endpoint yang tidak punya aturan akses di `security.md`
   - library gerak di spesifikasi gerak atau `FRONTEND_<project>.md` yang tidak tercantum di `techstack.md`
   - efek gerak tanpa fallback `prefers-reduced-motion`, atau token gerak yang namanya berbeda antar file
3. Perbaiki temuan, atau tanyakan ke user bila perlu keputusan. Catat hasilnya di bagian "Hasil pengecekan konsistensi" pada file induk.
4. Serahkan semua file dan ringkas apa yang dihasilkan serta apa yang masih `[PERLU KONFIRMASI]`.

## Struktur output

```
<project>-design-plan/
├── DESIGN_PLAN_<project>.md     (induk: ringkasan, Shared Contract, matriks, hasil pengecekan)
├── UIUX_<project>.md
├── FRONTEND_<project>.md
├── BACKEND_<project>.md
├── task.md
├── security.md
└── mockups/
    ├── index.html               (daftar halaman + tautan)
    ├── styles.css               (design tokens + gaya bersama)
    └── <route-atau-nama-halaman>.html   (satu file per halaman P-xx)
```

`DESIGN_PLAN_<project>.md` berisi: ringkasan proyek, daftar file dan fungsinya, urutan kerja, Shared Contract lengkap, matriks keterlacakan, dan hasil pengecekan konsistensi.

## Aturan mockup HTML

Mockup adalah gambaran visual yang bisa dibuka langsung di browser tanpa server atau build. Ia dibuat dalam dua tahap yang berurutan: pratinjau artifact, lalu berkas HTML per halaman.

### Tahap 1: Pratinjau sebagai artifact

- **Selalu artifact dulu.** Jangan menulis folder `mockups/` sebelum user menyetujui pratinjau, kecuali user meminta langsung berkas.
- **Cara menampilkan:** gunakan alat artifact bila tersedia. Jika ada jenis artifact untuk mockup atau desain, pakai itu; jika tidak, satu halaman HTML mandiri yang dipublikasikan sebagai artifact. Bila alat artifact tidak tersedia, tulis satu berkas HTML mandiri ke `/mnt/user-data/outputs/` lalu tampilkan dengan `present_files`.
- **Satu artifact mandiri:** semua CSS di dalam `<style>` (tanpa `styles.css` terpisah), tanpa framework, tanpa gambar atau skrip dari host lain (font boleh dengan fallback). Semua halaman ada di artifact yang sama dan bisa dipindah lewat bilah navigasi kecil yang jelas bukan bagian produk (tautan `#P-01` atau tab; JavaScript secukupnya).
- **Cakupan:** semua halaman P-xx bila jumlahnya enam atau kurang. Bila lebih, pratinjau memuat halaman kunci (maksimal enam: yang paling sering dilihat dan yang mewakili tiap pola layout), dan beri tahu halaman mana yang belum tampil serta bahwa halaman itu akan dibuat dengan pola yang sama setelah persetujuan. Tampilkan state penting (kosong, error, loading, sukses) pada halaman yang relevan.
- **Token dan struktur** sudah identik dengan `UIUX_<project>.md`: CSS variables di `:root`, nama kelas yang konsisten untuk komponen bersama, dan atribut `data-page`/`data-feature` pada tiap halaman. Dengan begitu konversi di Tahap 2 hanya memindahkan, bukan merancang ulang.
- **Revisi:** terapkan masukan user pada artifact yang sama (perbarui artifact yang ada, bukan membuat artifact baru), lalu sinkronkan `UIUX_<project>.md`. Setelah tiap putaran, ringkas apa yang berubah dan tanya apakah sudah disetujui.
- **Persetujuan:** minta persetujuan eksplisit sebelum Tahap 2 ("sudah disetujui, ubah jadi HTML per halaman?"). Jawaban seperti "lanjut" atau "setuju" dihitung. Tanpa persetujuan, tetap di Tahap 1.

### Tahap 2: Berkas HTML per halaman (setelah disetujui)

Ubah artifact yang disetujui menjadi berkas yang bisa dibuka di browser tanpa server:

- **Satu file per halaman (P-xx)** dengan CSS dari `styles.css` bersama: `<link rel="stylesheet" href="styles.css">` di setiap halaman. Pindahkan semua CSS artifact ke `styles.css` (token `:root` di bagian atas, lalu gaya bersama, lalu gaya khusus halaman dengan komentar penanda); tidak ada CSS inline selain nilai dinamis yang memang perlu.
- **`index.html`** sebagai daftar isi, memuat nama halaman, ID P-xx, fitur terkait, dan tautan.
- **Navigasi** antar halaman memakai tautan relatif ke berkas, bukan lagi `#P-01` atau JavaScript pengalih. Bilah navigasi artifact yang bukan bagian produk dihapus.
- **Tampilan identik dengan artifact yang disetujui.** Jangan mendesain ulang, mengganti token, atau mengubah teks tanpa persetujuan. Halaman yang tidak ada di pratinjau dibuat dengan pola, komponen, dan kelas yang sama dengan halaman yang disetujui.
- **Pemeriksaan sebelum menyerahkan:** setiap berkas terbuka dan semua tautan relatif menuju berkas yang ada; setiap halaman P-xx di peta halaman punya satu berkas; nilai token di `styles.css` sama dengan `UIUX_<project>.md`; tidak ada placeholder yang tersisa.
- **Menyerahkan:** simpan di `<project>-design-plan/mockups/` lalu `present_files` dengan `index.html` di depan, diikuti `styles.css` dan semua halaman. Bila berkasnya lebih dari delapan, sertakan juga `mockups.zip`.

### Aturan berlaku untuk kedua tahap

- **Statis dan mandiri:** HTML + CSS. Tanpa framework dan tanpa JavaScript, kecuali sedikit untuk interaksi dasar yang memperjelas desain (menu, tab, modal). Tanpa permintaan jaringan selain font; beri fallback font.
- **Pakai design tokens yang sama persis** dengan `UIUX_<project>.md` lewat CSS variables (`--color-primary`, dan seterusnya), di `<style>` pada artifact dan di `styles.css` pada berkas final, sehingga Frontend bisa memindahkannya apa adanya.
- **Alur pengguna bisa diklik:** tautan antar halaman berfungsi, lewat navigasi artifact di Tahap 1 dan path relatif antar berkas di Tahap 2.
- **Tandai keterlacakan:** beri atribut `data-page="P-xx"` pada `<body>` dan `data-feature="F-xx"` pada blok fitur utama.
- **Tampilkan state penting** (kosong, error, loading, sukses) sebagai bagian atau varian di halaman yang relevan, misalnya lewat tab atau bagian berlabel "State: ...".
- **Responsif:** tampil baik di mobile dan desktop sesuai breakpoint di tokens.
- **Gerak di mockup hanya didekati dengan CSS:** satu atau dua efek kunci (hover, reveal sederhana) lewat `transition` atau `@keyframes` memakai token gerak, lengkap dengan blok `@media (prefers-reduced-motion: reduce)`. Jangan memuat library gerak di mockup; gerak final ada di spesifikasi gerak di `UIUX_<project>.md`.
- **Aksesibilitas dasar:** HTML semantik, label form, kontras sesuai tokens, fokus terlihat.
- **Konten realistis:** gunakan data contoh yang masuk akal sesuai domain project, bukan lorem ipsum.
- Jika berasal dari referensi desain, mockup harus terlihat satu keluarga dengan referensi, termasuk pada halaman yang tidak ada di referensi.

## Daftar periksa sebelum menyerahkan

- [ ] PRD dan techstack sudah dibaca; kekurangan sudah ditanyakan
- [ ] Referensi desain sudah ditanyakan dan keputusan dicatat
- [ ] Setiap fitur punya ID dan tercantum di matriks keterlacakan
- [ ] Mockup ditampilkan sebagai artifact lebih dulu dan sudah disetujui user sebelum berkas HTML dibuat
- [ ] Berkas HTML per halaman + `styles.css` identik secara visual dengan artifact yang disetujui
- [ ] Design tokens identik di `UIUX`, `styles.css`, dan `FRONTEND`
- [ ] Spesifikasi gerak ada di `UIUX`, library gerak tercantum di `techstack.md`, setiap efek punya fallback `prefers-reduced-motion`, dan token gerak identik di `UIUX`, `FRONTEND`, serta `DESIGN.md` bila ada
- [ ] Kontrak API identik di Shared Contract, `FRONTEND`, dan `BACKEND`
- [ ] Skema database memakai istilah dari glosarium
- [ ] Semua kode dan struktur sesuai techstack
- [ ] `task.md` dan `security.md` dibuat atau diperbarui, bukan ditimpa
- [ ] Bahasa file sesuai bahasa user
- [ ] Semua `[PERLU KONFIRMASI]` dilaporkan di akhir

## Referensi

| File | Dibaca saat |
|---|---|
| `references/motion.md` | Fase 2 (menyusun spesifikasi gerak) dan Fase 4 (bagian Animasi dan gerak di `FRONTEND_<project>.md`) |

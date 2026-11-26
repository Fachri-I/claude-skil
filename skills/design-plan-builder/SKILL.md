---
name: "design-plan-builder"
description: Membuat rancangan kerja pembangunan website (UI/UX, Frontend, Backend) dalam file .md plus mockup HTML statis, dari PRD, techstack, dan file pendukung, agar fitur, tampilan, API, dan database konsisten. Gunakan skill ini setiap kali user ingin membuat rancangan kerja, design plan, blueprint, atau rancangan teknis website/web app dari PRD, ingin menyelaraskan UI/UX dengan frontend dan backend, ingin membuat task.md atau security.md, atau menyebut PRD_nama-project.md dan techstack.md, walaupun user tidak menyebut kata "skill". Also use when the user asks for a UI/UX, frontend, and backend plan for a website from a PRD. Skill ini melanjutkan hasil skill PRD Builder. Hasilkan juga AGENTS.md dan task.md berformat eksekusi setia desain (sumber desain per tugas, checklist kesesuaian, database-first) agar agen coding patuh pada desain.
---

# Design Plan Builder

Skill ini mengubah PRD, techstack, dan file pendukung menjadi satu paket rancangan kerja yang konsisten dari fitur sampai tampilan, untuk tiga role: **UI/UX, Frontend, Backend**. Hasilnya berupa file `.md` dan mockup HTML statis.

Konsistensi adalah tujuan utama. Semua keputusan penting (fitur, nama, warna, halaman, endpoint, tabel) ditulis **sekali** di Shared Contract, lalu dirujuk oleh ketiga role. Jangan menduplikasi atau menamai ulang hal yang sama di file lain.

Tujuan kedua: **agen coding yang membangun website harus patuh pada desain dan rancangan tanpa perlu diingatkan berulang.** Karena itu paket ini selalu menyertakan `AGENTS.md` dan `task.md` yang menunjuk file desain sumber, skema database terkunci, dan checklist kesesuaian (lihat Fase 5).

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
| Folder desain | Wajib jika desain UI sudah ada | path folder (default `docs/Stitch-design/`) berisi HTML per halaman dan `DESIGN.md` |
| `database.md` | Opsional | skema database dari skill database; bila ada, jadi sumber kebenaran skema |
| File pendukung | Opsional | `user-flow.md`, skema DB awal, brand guideline, `DESIGN.md` (dari design-direction-builder), aturan bisnis, `task.md`/`security.md` yang sudah ada |

Aturan:
- Jika PRD atau techstack belum ada, hentikan dan beri tahu user. Sarankan membuatnya dengan skill PRD Builder.
- Jika ada, baca semuanya, lalu laporkan: apa yang sudah cukup, apa yang kurang, dan apa yang belum bisa dirancang karena itu.
- Jika `task.md` atau `security.md` sudah ada, gunakan sebagai dasar dan perbarui (lihat Fase 5), jangan menimpa.
- Tanyakan lokasi folder desain bila belum disebut, lalu catat path-nya di Shared Contract.
- Buat **Peta Desain**: pasangkan tiap halaman P-xx dengan satu file HTML sumber. Halaman tanpa file sumber ditandai `TANPA SUMBER: turunkan dari DESIGN.md` dan dilaporkan ke user.

### Fase 1: Shared Contract

Ekstrak dari input lalu susun kamus konsistensi. Simpan di bagian awal `DESIGN_PLAN_<project>.md`:

1. **Daftar fitur dengan ID** (`F-01`, `F-02`, ...): nama, deskripsi singkat, prioritas (Must/Should/Could), role pengguna yang terlibat.
2. **Glosarium & penamaan:** nama entitas, istilah bisnis, dan konvensi penamaan (file, komponen, route, tabel, field, endpoint). Satu istilah, satu nama.
3. **Peta halaman:** tabel dengan kolom `ID | Nama | Route | Fitur (F-xx) | File desain sumber`. ID halaman (`P-01`, ...). Kolom file desain sumber diisi path relatif dari root proyek, contoh `docs/Stitch-design/login.html`.
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

Jika user sudah punya desain final di folder desain (misalnya hasil Stitch), tahap mockup hanya untuk halaman yang belum punya file sumber. Halaman yang sudah punya file sumber tidak didesain ulang.

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
3. **Skema database:** jika `database.md` ada, BACKEND **merujuknya dan tidak mendefinisikan ulang** (tulis "Skema: lihat `database.md`, status TERKUNCI"). Jika tidak ada, definisikan di sini: tabel, kolom, tipe, constraint, relasi, index, dan diagram ERD (Mermaid), dengan penamaan mengikuti glosarium. Setelah disetujui, skema dikunci: perubahan hanya lewat persetujuan user.
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

**`task.md`:** pelacak pekerjaan yang juga menjadi perintah kerja bagi agen coding. Format tabel satu baris per tugas tidak cukup karena tidak bisa memuat aturan per tugas. Pakai **tabel ringkasan + blok detail per tugas**.

*Urutan fase tugas (wajib):*

1. **A. Fondasi:** setup proyek, design tokens dari `DESIGN.md`, struktur folder
2. **B. Database:** migrasi dan seed dari `database.md`
3. **C. Backend/API:** endpoint sesuai kontrak API
4. **D. UI per halaman:** satu tugas per halaman P-xx
5. **E. Integrasi:** sambungkan UI ke API
6. **F. Testing dan keamanan:** sesuai `security.md`

*Bagian atas `task.md` (ringkasan):*

```
| ID | Fase | Tugas | Role | Status | Bergantung pada |
```

Status: `Belum` / `Sedang dikerjakan` / `Review` / `Selesai` / `Terblokir`.

*Blok detail tugas UI (wajib persis format ini):*

```
### T-xx: [UI] Halaman <nama> (P-xx)
- Fitur: F-xx
- SUMBER DESAIN (wajib dibaca sebelum menulis kode): <folder-desain>/<file>.html
- Metode: PORT, bukan desain ulang. Salin struktur HTML, class, warna, spasi,
  font, dan urutan section dari file sumber ke komponen. Setelah itu baru
  ganti data statis dengan data dinamis. Dilarang menambah, menghapus, atau
  mengubah elemen visual.
- Gerak: ikuti baris halaman ini di spesifikasi gerak (UIUX_<project>.md, bagian 9),
  lengkap dengan fallback prefers-reduced-motion. Library hanya dari techstack.md.
- Data/API: <endpoint dari kontrak API>
- Checklist kesesuaian (isi sebelum status diubah ke Review):
  - [ ] Semua section di file sumber ada, urutannya sama
  - [ ] Warna, font, radius, dan spasi memakai token DESIGN.md (tanpa nilai hardcode baru)
  - [ ] Tidak ada elemen tambahan yang tidak ada di sumber
  - [ ] State penting (kosong/loading/error) mengikuti sumber atau DESIGN.md
  - [ ] Tampil benar di mobile dan desktop seperti sumber
- Bukti selesai: ringkasan perbedaan yang tersisa (atau "tidak ada")
```

*Blok detail tugas Database:*

```
### T-xx: [DB] <nama migrasi/tabel>
- Sumber skema (TERKUNCI): database.md, bagian <tabel>
- Aturan: ikuti nama tabel, kolom, tipe, dan relasi persis seperti sumber.
  Dilarang mengubah skema. Jika butuh perubahan, BERHENTI dan tanyakan ke user.
- Bukti selesai: migrasi berhasil dijalankan, seed terisi
```

*Blok detail tugas Backend:*

```
### T-xx: [BE] <METHOD /path>
- Sumber kontrak: DESIGN_PLAN_<project>.md, bagian Kontrak API
- Aturan: request, response, dan kode error persis seperti kontrak.
  Aturan akses mengikuti security.md (S-xx).
- Bukti selesai: endpoint diuji dengan contoh request/response dari kontrak
```

*Aturan tambahan:*
- Satu tugas = satu halaman atau satu modul kecil, agar konteks agen tidak membengkak.
- Tugas UI bergantung pada tugas Fondasi (tokens) dan tidak boleh mendahului tugas Database/Backend yang diperlukan datanya, **kecuali** dikerjakan dengan data statis dulu lalu dihubungkan di fase E (tulis ini di "Bergantung pada").
- Sertakan bagian "Riwayat perubahan" berisi tanggal dan ringkasan.

**Mode pembaruan:** jika `task.md` sudah ada saat skill dipakai lagi, jangan buat ulang. Pertahankan status yang sudah ada, tambahkan tugas baru, perbarui status sesuai info dari user, dan catat di riwayat. Perlakuan yang sama berlaku untuk `security.md` yang sudah ada: tambahkan atau revisi, jangan timpa tanpa persetujuan.

**`AGENTS.md`:** aturan wajib untuk agen coding. Agen seperti opencode membacanya otomatis di setiap sesi, sehingga aturan tidak hilang saat konteks panjang atau model diganti. Dibuat di root proyek bersama `task.md`. Gunakan template berikut dan sesuaikan path serta nama proyek:

````markdown
# AGENTS.md: Aturan Wajib untuk Agen Coding

Proyek: <nama proyek>

## Sumber kebenaran (urutan prioritas)
1. `<folder-desain>/*.html`: tampilan setiap halaman. Ini hukum, bukan inspirasi.
2. `<folder-desain>/DESIGN.md`: design tokens (warna, font, spasi, radius, gerak).
3. `database.md`: skema database (TERKUNCI).
4. `DESIGN_PLAN_<project>.md`: kontrak API, peta halaman, glosarium.
5. `task.md`: daftar tugas dan urutan kerja.
6. `security.md`: aturan keamanan.

Jika dua sumber bertentangan, ikuti urutan di atas dan laporkan pertentangannya.

## Cara kerja per tugas
1. Buka `task.md`, ambil **satu** tugas dengan status Belum yang dependensinya sudah Selesai.
2. Ubah statusnya menjadi Sedang dikerjakan.
3. Baca semua "Sumber" yang tertulis di tugas itu **sebelum menulis kode**.
4. Kerjakan hanya tugas itu. Jangan menyentuh halaman/modul lain.
5. Isi checklist tugas. Jika ada yang tidak terpenuhi, perbaiki dulu.
6. Ubah status menjadi Review, tulis ringkasan singkat di Riwayat perubahan, lalu berhenti dan lapor.

## Aturan UI (paling sering dilanggar)
- **PORT, bukan desain ulang.** Sebelum menulis kode halaman, tulis daftar section dari file HTML sumber (urutan dan nama). Lalu salin struktur, class, dan gaya dari file itu.
- Dilarang mengarang layout, mengganti warna, menambah section, atau "memperbaiki" desain.
- Dilarang memakai nilai warna/font/spasi yang tidak ada di `DESIGN.md`.
- Gerak mengikuti spesifikasi gerak di `UIUX_<project>.md`. Dilarang menambah library gerak di luar `techstack.md`, dan setiap efek wajib punya fallback `prefers-reduced-motion`.
- Bila ada konflik antara kemudahan teknis dan kesesuaian desain, pilih kesesuaian desain, atau berhenti dan tanyakan.

## Aturan Database
- Skema mengikuti `database.md` persis. Dilarang menambah/menghapus/mengubah tabel, kolom, atau relasi sendiri.
- Perlu perubahan skema? Berhenti, jelaskan alasannya, tunggu persetujuan user.

## Aturan umum
- Jangan menebak untuk hal yang bisa dibaca dari file. Jika informasi benar-benar tidak ada, tanyakan.
- Jangan mengerjakan tugas di luar `task.md`.
- Jangan menandai tugas Selesai sebelum checklist terpenuhi. Hanya user yang mengubah Review menjadi Selesai.
````

Jika proyek tidak punya `database.md`, ganti butir 3 dengan rujukan ke bagian skema di `BACKEND_<project>.md`. Jika `AGENTS.md` sudah ada di proyek, gabungkan: tambahkan bagian yang belum ada, jangan timpa.

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
   - halaman P-xx yang punya UI tetapi tugasnya tidak punya `SUMBER DESAIN`, atau path file desainnya tidak ada
   - tugas UI tanpa checklist kesesuaian
   - tugas DB/BE yang tidak merujuk `database.md` atau kontrak API
   - urutan tugas yang melanggar database-first
   - `AGENTS.md` tidak ada, atau path di dalamnya tidak cocok dengan struktur proyek
3. Perbaiki temuan, atau tanyakan ke user bila perlu keputusan. Catat hasilnya di bagian "Hasil pengecekan konsistensi" pada file induk.
4. Serahkan semua file dan ringkas apa yang dihasilkan serta apa yang masih `[PERLU KONFIRMASI]`.

## Struktur output

```
<project>-design-plan/
├── DESIGN_PLAN_<project>.md     (induk: ringkasan, Shared Contract, matriks, hasil pengecekan)
├── UIUX_<project>.md
├── FRONTEND_<project>.md
├── BACKEND_<project>.md
├── AGENTS.md                    (aturan wajib agen coding; pindahkan ke root proyek saat membangun)
├── task.md                      (ringkasan + blok detail per tugas; pindahkan ke root proyek)
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
- [ ] Setiap halaman UI punya file desain sumber di Peta Desain (atau ditandai TANPA SUMBER dan dilaporkan)
- [ ] Mockup ditampilkan sebagai artifact lebih dulu dan sudah disetujui user sebelum berkas HTML dibuat
- [ ] Berkas HTML per halaman + `styles.css` identik secara visual dengan artifact yang disetujui
- [ ] Design tokens identik di `UIUX`, `styles.css`, dan `FRONTEND`
- [ ] Spesifikasi gerak ada di `UIUX`, library gerak tercantum di `techstack.md`, setiap efek punya fallback `prefers-reduced-motion`, dan token gerak identik di `UIUX`, `FRONTEND`, serta `DESIGN.md` bila ada
- [ ] Kontrak API identik di Shared Contract, `FRONTEND`, dan `BACKEND`
- [ ] Skema database memakai istilah dari glosarium, dan dirujuk dari `database.md` bila ada (tidak didefinisikan ulang)
- [ ] Semua kode dan struktur sesuai techstack
- [ ] `task.md` memakai format baru: tiap tugas UI memuat SUMBER DESAIN, metode PORT, dan checklist kesesuaian; urutan fase Fondasi → Database → Backend → UI → Integrasi → Testing
- [ ] `AGENTS.md` dibuat dan path di dalamnya sudah benar
- [ ] `task.md` dan `security.md` dibuat atau diperbarui, bukan ditimpa
- [ ] Bahasa file sesuai bahasa user
- [ ] Semua `[PERLU KONFIRMASI]` dilaporkan di akhir

## Referensi

| File | Dibaca saat |
|---|---|
| `references/motion.md` | Fase 2 (menyusun spesifikasi gerak) dan Fase 4 (bagian Animasi dan gerak di `FRONTEND_<project>.md`) |

# Hubungan dengan antislop

Sumber dan lisensi: https://github.com/miqdadbadjuber/anti-slop (MIT). Bagian ringkas di bawah adalah prinsip yang diadaptasi dengan atribusi ini. Salinan penuh antislop tidak disertakan di skill ini.

## 1. Dua fase, dua peran

| | Fase perancangan (Claude chat atau Project) | Fase implementasi (OpenCode atau agen lain) |
|---|---|---|
| Skill | Design Direction Builder, lalu Design Plan Builder dan Stitch Design Builder | agen menulis kode dari hasil perancangan |
| Peran antislop | **hanya prinsipnya** (bagian 2 dan 3) | **antislop penuh terpasang** sebagai skill di proyek |
| Penegak | `critique-rubric.md` | Delivery Gate penuh pada aplikasi yang benar-benar dibangun dan dijalankan |

antislop adalah **filter, bukan sumber arah**: ia menolak teknik tanpa tujuan dan menuntut kehidupan visual, tetapi tidak memilih warna, font, atau tata letak. Skill ini yang menyusun arah. Jembatan antar fase adalah **`DESIGN.md`**, karena antislop memakainya sebagai sumber arah dan menganggap dirinya filter di atasnya.

Tanpa arah, hasil antislop bersih tetapi steril. Dengan arah tetapi tanpa filter, slop tetap muncul. Keduanya diperlukan.

## 2. Prinsip yang dipakai di chat

1. **Teknik harus punya tujuan.** Tiap keputusan besar (warna, tata letak, tipografi, jarak, kartu, ikon atau ilustrasi) diberi alasan satu baris. Alasan "ini default" atau "terlihat aman" berarti keputusan dibuang atau dikerjakan ulang.
2. **Pengguna adalah penulis arah.** Arah yang dikarang agen cenderung ke selera default AI. Agen menyusun dan memformat masukan user, tidak mengarang selera.
3. **Kehidupan harus ditambahkan, bukan hanya slop dihapus.**
4. **Design Read satu baris** sebelum membuat mockup (format ada di `SKILL.md`).
5. **Tiga dial**, skala 1 sampai 3, dipegang konsisten dari bagian pertama sampai terakhir:

| Dial | 1 (tenang) | 2 (seimbang) | 3 (berani) |
|---|---|---|---|
| ENERGY | tegas dan tenang | sedang | menonjol, eksperimental |
| RHYTHM | grid seragam | konsisten dengan beberapa jeda | asimetris, komposisi campuran |
| MOTION | hanya status hover | transisi dan scroll-reveal | koreografi, parallax |

6. **Tuas kehidupan visual** per arah: satu titik fokus per layar; kontras hierarki yang disengaja; whitespace sebagai struktur; **satu aksen sengaja** (nol aksen steril, aksen di mana-mana slop); satu motif identitas yang spesifik dan berulang.
7. **Uji penukaran:** bila logo dan nama produk ditukar, apakah desain masih terasa unik? Bila tidak, ulangi.
8. **Tiga arah berbeda secara struktur**, bukan hanya warna. Satu arah aman (dial rendah), satu seimbang, satu berani. Referensi dipakai sebagai inspirasi, tidak ditiru menyeluruh.

## 3. Aturan isi mockup (ringkas)

- Konten hanya dari PRD; tanpa statistik, delta, testimoni, nama, fitur, atau klaim karangan. Placeholder jujur (`[DATA ASLI]`, "Segera hadir").
- Logo berupa teks atau `[LOGO]`; avatar inisial atau bentuk geometris; field formulir kosong atau placeholder jujur.
- Navigasi dan tombol menuju layar yang ada atau berlabel "Segera hadir" atau "mockup".
- CTA spesifik, tanpa kata pemasaran klise, tanpa em dash di teks antarmuka.
- Palet 2-3 inti + 1 aksen; tema gelap hanya dengan alasan.
- Glass dan glow maksimal 1-2 elemen; bayangan hanya penanda elevasi; latar bergrid hanya dengan alasan identitas; ikon dengan relevansi tertulis.
- Tata letak dari kebutuhan konten, bukan template.
- Dasar teknis: tanpa overflow horizontal di 375px, kontras minimal 4,5:1 yang diukur, status fokus dan hover terlihat, `prefers-reduced-motion` dihormati.

Detail lengkap ada di `mockup-guidelines.md`; rubrik penilaian di `critique-rubric.md`.

## 4. Serah terima ke fase implementasi

Keluaran untuk agen: **`DESIGN.md`** (format resmi Stitch, memuat baris `Dial: ENERGY x / RHYTHM y / MOTION z`, Design Read, motif identitas, aksen, dan alasan per keputusan). Berkas ini hanya berisi data desain, bukan perintah untuk agen; antislop memperlakukan berkas arah sebagai data yang diterapkan.

Catatan pemasangan untuk user (dijalankan di proyek implementasi, bukan di chat):

1. Jalankan `npx antislop-ai` di folder proyek, pilih agen (OpenCode didukung), lalu pilih skill (All, atau minimal `antislop-ui`). Penginstal memasang folder skill dan menulis blok pointer ke `AGENTS.md` sendiri; jangan menulisnya manual dan jangan menggandakannya.
2. Letakkan `DESIGN.md` di akar proyek.
3. Mode during atau after dijawab di sana (agen yang menanyakannya); skill ini tidak menanyakan mode.
4. Di sana antislop dijalankan penuh: aplikasi dibangun dan dijalankan, setiap kontrol diklik, dan Delivery Gate menghasilkan laporan PASS atau FAIL dengan bukti.

Jalur alternatif menurut README antislop: `npx skills add miqdadbadjuber/anti-slop --all`. Bila agen tidak didukung penginstal, folder skill mengikuti standar Agent Skills (`<nama>/SKILL.md`) dan dapat disalin ke folder skill agen tersebut; antislop juga tersedia sebagai satu berkas `antislop.md`.

## 5. Dampak ke skill lain di rantai

- **Design Plan Builder:** memakai `DESIGN.md` sebagai sumber gaya dan tidak menaruh data karangan di wireframe atau mockup.
- **Stitch Design Builder (v2.0.0 ke atas):** memakai `DESIGN.md` ini dan melengkapi bagian yang kosong tanpa menimpa data arah.
- Rancangan layar aplikasi sebaiknya menyatakan keputusan yang diambil pengguna di tiap layar, karena `antislop-ui` menganggap susunan dashboard bawaan sebagai pola slop.

## 6. Pemeliharaan

Tidak ada salinan antislop yang perlu dirawat di skill ini. Ringkasan bagian 2 dan 3 bersifat prinsip dan jarang berubah; bila antislop mengubah prinsipnya, perbarui bagian itu secara manual. Dasar verifikasi: `antislop.md` (746 baris) dan `antislop-ui/SKILL.md` (351 baris) yang dibaca pada 25 November 2026.

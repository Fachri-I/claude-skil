---
name: techstack-recommender
description: Membaca file PRD (PRD_nama-proyek.md) lalu merekomendasikan tech stack yang cocok dengan kebutuhan proyek, dan menghasilkan file techstack.md berisi pilihan utama, alternatif, alasan dalam bahasa awam, serta trade-off. Gunakan skill ini setiap kali pengguna melampirkan atau menyebut file PRD dan ingin tahu tech stack apa yang cocok, ingin memilih frontend/backend/database/hosting, bingung memilih teknologi, ingin membuat techstack.md, atau berkata "rekomendasi tech stack", "pakai teknologi apa", "stack yang bagus untuk proyek ini", "pilih framework", "pilih starter/template", walaupun pengguna tidak menyebut kata "skill". Skill ini melanjutkan hasil skill PRD Builder dan ramah untuk pengguna yang masih awam soal tech stack.
---

# Techstack Recommender

Skill ini membaca sebuah PRD, mencari tahu kebutuhan teknis yang tersirat di dalamnya, lalu menghasilkan `techstack.md`: rekomendasi teknologi yang dijelaskan dengan bahasa awam dan dihubungkan langsung ke kebutuhan PRD.

Pengguna skill ini sering **belum paham tech stack**. Jadi tugas utamanya bukan hanya menyebut nama teknologi, tetapi menjelaskan *kenapa* teknologi itu cocok, dengan istilah yang mudah dimengerti.

## Bahasa

Gunakan Bahasa Indonesia. Istilah teknis boleh tetap dalam bahasa Inggris, tetapi **setiap istilah teknis yang muncul pertama kali diberi penjelasan satu kalimat** (contoh: "*database* — tempat menyimpan data aplikasi secara permanen").

## Alur kerja

```
Baca PRD → Ekstrak kebutuhan → Tanya hanya yang kurang → Rekomendasi → Konfirmasi → Tulis techstack.md
```

### Langkah 1 — Baca PRD

Cari file PRD di `/mnt/user-data/uploads/` (biasanya `PRD_<nama-proyek>.md`). Jika file tidak ada, minta pengguna melampirkannya. Jika pengguna hanya menempelkan teks PRD di chat, gunakan teks itu.

Jika PRD sudah memuat bagian tech stack (misalnya dari Fase 6 PRD Builder), perlakukan sebagai **keputusan awal pengguna**: validasi, jangan ganti begitu saja. Bila ada yang kurang cocok dengan kebutuhan, jelaskan alasannya dan tawarkan alternatif.

### Langkah 2 — Ekstrak kebutuhan

Dari PRD, catat sinyal berikut. Tandai tiap item sebagai **jelas**, **tersirat**, atau **tidak ada**.

| Sinyal | Dicari di PRD | Pengaruh pada stack |
|---|---|---|
| Platform | web, HP (Android/iOS), keduanya, API saja | Menentukan frontend dan apakah perlu framework mobile |
| Jenis data | relasional (pesanan, user, relasi antartabel) atau fleksibel | Menentukan database |
| Fitur khusus | login, pembayaran, upload file, notifikasi, real-time/chat, pencarian, laporan, AI | Menambah komponen (auth, storage, WebSocket, dll.) |
| Skala | jumlah pengguna, lonjakan trafik | Menentukan arsitektur dan hosting |
| SEO | perlu muncul di Google? | Mendorong framework dengan server rendering |
| Keamanan/regulasi | data sensitif, kepatuhan | Menentukan auth, enkripsi, lokasi hosting |
| Tim & timeline | jumlah orang, pengalaman, tenggat | Menentukan kompleksitas yang masih realistis |
| Budget | biaya bulanan yang sanggup | Menentukan hosting dan layanan berbayar |

### Langkah 3 — Tanya hanya yang kurang

Ajukan pertanyaan **hanya untuk sinyal yang "tidak ada" atau samar** di PRD. Jangan menanyakan ulang yang sudah tertulis.

Aturan bertanya:

- Maksimal 3–5 pertanyaan per giliran.
- Pakai bahasa awam, bukan istilah teknis mentah. Beri pilihan jawaban; jika tool `ask_user_input_v0` tersedia, gunakan tombol pilihan.
- Selalu sediakan opsi **"belum tahu / sarankan saja"**. Jika dipilih, buat asumsi yang aman dan tandai sebagai asumsi di `techstack.md`.
- Tuliskan tebakan sendiri bila keyakinan tinggi dan minta pengguna cukup menjawab "ya". Jangan menebak diam-diam bila keyakinan rendah; tanyakan.

Pertanyaan yang perlu ditanyakan **jika belum ada di PRD**:

1. **Platform** — "Aplikasi ini dipakai lewat apa?" (browser web / aplikasi HP / keduanya)
2. **Perkiraan pengguna** — "Berapa orang yang kira-kira memakai dalam 6–12 bulan pertama?" (puluhan / ratusan / ribuan / puluhan ribu+)
3. **Hosting gratis atau berbayar** — "Aplikasi ini akan ditaruh di hosting gratis, atau ada budget bulanan?" (gratis saja / sampai kisaran tertentu per bulan / fleksibel). Jawaban ini **wajib dicari tahu** karena memengaruhi hampir semua pilihan; lihat bagian "Mode hosting" di bawah.
4. **Pengalaman coding** — "Siapa yang akan membangun, dan seberapa terbiasa dengan coding?" (pemula / menengah / mahir; sendiri / tim). Jika pembangunan dibantu AI, catat itu.
5. **Fitur khusus** — "Apakah butuh fitur real-time (chat/notifikasi langsung), pembayaran online, upload file, atau fitur AI?"
6. **Bahasa/teknologi yang sudah dikuasai** — bila ada, jadikan prioritas agar kurva belajar rendah.

Tambahkan pertanyaan lain hanya jika PRD menunjukkan kebutuhan khusus (misalnya SEO, data sensitif, integrasi pihak ketiga tertentu).

### Langkah 4 — Susun rekomendasi

Untuk **setiap komponen** yang relevan, beri **satu pilihan utama + satu alternatif**:

- Frontend (tampilan)
- Backend (logika di server) / API
- Database
- Autentikasi (login)
- Penyimpanan file (bila perlu)
- Hosting & deployment
- Layanan tambahan sesuai fitur (pembayaran, email, notifikasi, real-time, AI, dll.)
- Tools pendukung (version control, testing, CI/CD) secara singkat

Untuk tiap komponen tulis:

- **Pilihan utama** dan alasan yang **dikaitkan ke kebutuhan PRD** (kutip fitur/kebutuhan terkait, bukan alasan generik).
- **Alternatif** dan kapan lebih baik memilihnya.
- **Trade-off** jujur (kelebihan dan kekurangan).

Prinsip memilih:

1. **Sederhana dulu.** Pilih stack paling sederhana yang memenuhi kebutuhan PRD. Jangan merekomendasikan arsitektur rumit (misalnya microservices) untuk proyek kecil.
2. **Konsisten.** Komponen harus cocok satu sama lain. Jangan merekomendasikan kombinasi yang jarang dipakai bersama tanpa alasan kuat.
3. **Matang dan punya komunitas besar.** Utamakan teknologi yang dokumentasi dan tutorialnya melimpah, terutama bagi pemula.
4. **Hormati preferensi pengguna.** Jika pengguna sudah menguasai atau memilih teknologi tertentu, pakai itu kecuali tidak memenuhi kebutuhan.
5. **Jujur soal ketidakpastian.** Versi, harga, dan batas gratis layanan berubah. Bila web search tersedia, cek informasi terbaru untuk harga/kuota/versi sebelum menulisnya; bila tidak, tulis bahwa angka itu perlu diverifikasi.

### Mode hosting

Jawaban "gratis atau berbayar" mengubah rekomendasi:

- **Gratis saja:** utamakan layanan dengan *free tier* (paket gratis) yang memadai untuk proyek kecil. Jelaskan batasan yang perlu diketahui, misalnya server yang "tertidur" saat sepi, kuota database, atau batas penyimpanan, dan dampaknya pada pengguna. Hindari komponen yang tidak punya opsi gratis.
- **Berbayar dengan budget terbatas:** rekomendasikan opsi hemat yang bisa dinaikkan nanti (*scale up*). Beri perkiraan kisaran biaya bulanan per komponen bila datanya tersedia.
- **Fleksibel:** pilih berdasarkan kecocokan teknis, lalu sebutkan kisaran biayanya.

Selalu tulis di `techstack.md` apa yang terjadi jika proyek tumbuh dan melewati batas gratis ("jalur upgrade").

### Menjelaskan starter template

Pengguna kadang membawa daftar *starter template* (kerangka proyek siap pakai) sebagai referensi, dan sering belum paham fungsinya. Jika pengguna menyebut atau melampirkan starter:

1. Jelaskan dulu dengan analogi: starter adalah "rumah setengah jadi" yang sudah berisi pondasi (struktur folder, login contoh, koneksi database, konfigurasi), sehingga tinggal menambah fitur.
2. Petakan starter ke kebutuhan PRD: rekomendasikan starter **hanya bila cocok** dengan stack yang dipilih, dan sebutkan alasannya. Jika tidak ada starter yang cocok, katakan jujur dan rekomendasikan membangun dari nol atau memakai starter resmi dari framework terkait.
3. Panduan kasar memetakan jenis starter (jangan dipakai buta; sesuaikan dengan isi starter yang sebenarnya):

| Jenis starter | Cocok bila | Kurang cocok bila |
|---|---|---|
| Aplikasi HP (mis. React Native/Expo + API) | Butuh aplikasi di Android/iOS | Hanya butuh situs web |
| Fullstack web satu kode (mis. Next.js) | Web dengan frontend dan backend sederhana dalam satu proyek, perlu SEO | Backend sangat besar atau dipakai banyak klien berbeda |
| Fullstack web alternatif (mis. TanStack Start) | Web interaktif dengan tipe data yang ketat, tim nyaman dengan ekosistem React modern | Pemula yang butuh banyak tutorial |
| Monorepo (frontend dan backend terpisah dalam satu repositori) | Ada API sendiri yang dipakai beberapa klien (web, HP), atau tim yang membagi tugas | Proyek kecil dikerjakan sendiri; terlalu rumit |

4. Jika isi starter tidak jelas, **tanyakan** (atau minta pengguna menempelkan deskripsinya) daripada menebak.

### Langkah 5 — Ringkasan & konfirmasi

Sebelum menulis file, tampilkan **ringkasan satu layar**: tabel komponen → pilihan utama → alternatif, plus daftar asumsi. Tanyakan apakah ada yang ingin diubah. Jika pengguna ingin langsung dibuatkan file, lewati konfirmasi dan tulis dengan asumsi yang ditandai jelas.

### Langkah 6 — Tulis `techstack.md`

Simpan ke `/mnt/user-data/outputs/techstack.md`, lalu bagikan dengan `present_files`. Setelah itu beri ringkasan 2–3 kalimat saja.

Struktur file:

```markdown
# Tech Stack — <Nama Proyek>

> Berdasarkan: PRD_<nama-proyek>.md · Tanggal: <tanggal>

## 1. Ringkasan
Satu paragraf: stack yang direkomendasikan dan alasan utamanya.

## 2. Kebutuhan dari PRD
Tabel: kebutuhan → sumber di PRD (bagian/fitur) → dampak pada stack.

## 3. Profil proyek
Platform, skala, mode hosting (gratis/berbayar), pengalaman tim, fitur khusus.
Tandai yang berasal dari PRD, dari jawaban pengguna, atau **asumsi**.

## 4. Rekomendasi per komponen
Untuk tiap komponen:
### <Komponen>
- **Pilihan utama:** ...
- **Kenapa cocok:** (dikaitkan ke kebutuhan PRD)
- **Alternatif:** ... (pilih ini bila ...)
- **Trade-off:** ...

## 5. Tabel ringkas
Komponen | Pilihan utama | Alternatif | Biaya (gratis/berbayar)

## 6. Starter template (bila relevan)
Starter yang cocok, alasan, dan cara memakainya; atau catatan bahwa tidak ada yang cocok.

## 7. Hosting & biaya
Opsi gratis, batasan free tier, perkiraan biaya bila tumbuh, dan jalur upgrade.

## 8. Risiko & hal yang perlu diverifikasi
Batas gratis yang bisa berubah, kurva belajar, ketergantungan pada vendor tertentu.

## 9. Asumsi & pertanyaan terbuka
Semua hal yang diputuskan tanpa konfirmasi pengguna.

## 10. Langkah berikutnya
Urutan setup awal (instalasi, membuat repositori, menjalankan starter), dan tautan ke dokumen pendukung bila ada (ARCHITECTURE.md, TASKS.md).

## Glosarium
Istilah teknis yang dipakai beserta arti satu kalimat.
```

Ukuran file proporsional: proyek kecil cukup ringkas; proyek besar lebih rinci pada keamanan dan skala.

## Prinsip kualitas

- **Berbasis PRD.** Setiap rekomendasi harus bisa ditelusuri ke kebutuhan di PRD atau ke jawaban pengguna. Tidak ada pilihan "karena populer".
- **Bahasa awam.** Pengguna harus bisa menjelaskan ulang pilihannya setelah membaca.
- **Konsisten dengan dokumen lain.** Nama teknologi dan versi harus identik dengan PRD dan dokumen pendukung. Jika `techstack.md` mengubah keputusan di PRD, sebutkan dan tawarkan memperbarui PRD.
- **Jujur.** Tandai asumsi, sebutkan kekurangan pilihan, dan jangan mengarang angka harga atau kuota.
- **Tidak berlebihan.** Jangan merekomendasikan lebih banyak komponen daripada yang dibutuhkan PRD.

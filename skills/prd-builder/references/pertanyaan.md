# Bank Pertanyaan Wawancara PRD

Pilih 3–5 pertanyaan paling relevan per fase. Lewati yang sudah terjawab. Sesuaikan bahasa dengan pengguna.

## Daftar isi
- Fase 1: Gambaran umum
- Fase 2: Masalah & pengguna
- Fase 3: Fitur & scope
- Fase 4: Alur & data
- Fase 5: Non-fungsional
- Fase 6: Tech stack
- Fase 7: Eksekusi

---

## Fase 1 — Gambaran umum

1. Apa nama proyeknya (boleh nama sementara)?
2. Jelaskan proyek ini dalam satu kalimat. (Contoh: "Aplikasi kasir untuk warung kecil yang bisa jalan offline.")
3. Apa tujuan utamanya? (komersial, internal perusahaan, tugas kuliah, portofolio, open source, eksperimen)
4. Jenis produknya apa? (web app, mobile app, API/backend saja, desktop, bot, landing page, lainnya)
5. Apakah ini proyek baru atau pengembangan dari sistem yang sudah ada?

## Fase 2 — Masalah & pengguna

1. Masalah apa yang ingin diselesaikan? Bagaimana orang mengatasinya sekarang?
2. Siapa pengguna utamanya? (peran, usia/latar belakang, tingkat melek teknologi)
3. Adakah lebih dari satu jenis pengguna (misalnya admin, staf, pelanggan)? Apa beda hak aksesnya?
4. Apa yang membuat solusi ini lebih baik dari alternatif yang ada?
5. Bagaimana Anda tahu masalah ini nyata? (wawancara, pengalaman pribadi, data)

## Fase 3 — Fitur & scope

1. Sebutkan fitur-fitur yang terpikir, urutan acak pun tidak apa-apa.
2. Jika hanya boleh merilis 3 fitur di versi pertama, mana yang dipilih? (ini menentukan MVP)
3. Fitur apa yang **sengaja tidak** dibangun dulu?
4. Apakah ada fitur yang wajib karena aturan, kontrak, atau permintaan klien?
5. Apakah ada produk pembanding/referensi yang ingin ditiru atau dihindari?

Setelah daftar fitur terkumpul, bantu pengguna memprioritaskan: **Must have / Should have / Could have / Won't have (sekarang)**.

## Fase 4 — Alur & data

1. Ceritakan alur utama pengguna dari awal sampai selesai (misalnya: daftar → login → buat pesanan → bayar → terima notifikasi).
2. Data utama apa yang disimpan? (misalnya pengguna, produk, pesanan, pembayaran)
3. Apakah butuh integrasi pihak ketiga? (pembayaran, email/WhatsApp, peta, login Google, analitik, ERP)
4. Apakah ada data yang sudah ada dan perlu diimpor/dimigrasi?
5. Apakah ada kebutuhan laporan, ekspor (PDF/Excel), atau dashboard?

## Fase 5 — Non-fungsional

1. Perkiraan jumlah pengguna saat peluncuran dan 1 tahun ke depan?
2. Seberapa sensitif datanya? (data pribadi, keuangan, kesehatan) Ada aturan yang harus dipatuhi? (misalnya UU PDP, standar industri)
3. Perlu berjalan offline atau di jaringan lambat?
4. Perangkat/peramban apa yang harus didukung? Perlu multi-bahasa?
5. Target ketersediaan dan performa? (misalnya uptime 99,5%, halaman < 2 detik)
6. Ada kebutuhan aksesibilitas khusus?

## Fase 6 — Tech stack

Tanyakan dulu preferensi dan batasan, lalu **rekomendasikan 2–3 opsi** dengan trade-off.

1. Teknologi apa yang sudah dikuasai tim/Anda? Adakah yang wajib atau dilarang?
2. Frontend: framework apa yang diinginkan? Perlu SSR/SEO?
3. Backend: bahasa/framework? Gaya API (REST, GraphQL, RPC)?
4. Database: relasional atau NoSQL? Perlu cache, pencarian, atau antrean (queue)?
5. Autentikasi: sendiri atau layanan (Auth0, Firebase, Keycloak, dll)?
6. Hosting & deployment: cloud mana, VPS, atau serverless? Perlu Docker/CI-CD?
7. Batasan biaya infrastruktur per bulan?

Panduan rekomendasi: pilih stack yang paling sederhana yang memenuhi kebutuhan Fase 1–5 dan sesuai keahlian pengguna. Jelaskan alasan dalam 1–2 kalimat per opsi. Hindari teknologi berlebihan untuk skala kecil (misalnya microservices untuk MVP).

## Fase 7 — Eksekusi

1. Siapa saja yang mengerjakan? (jumlah orang dan perannya)
2. Target waktu: kapan prototipe, MVP, dan rilis penuh?
3. Berapa anggaran atau batas sumber daya?
4. Bagaimana mengukur keberhasilan? (jumlah pengguna, transaksi, waktu hemat, kepuasan)
5. Apa risiko terbesar yang Anda khawatirkan? (teknis, waktu, biaya, adopsi pengguna)
6. Adakah deadline atau dependensi eksternal yang tidak bisa digeser?

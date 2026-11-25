---
name: prd-builder
description: Merancang PRD (Product Requirements Document) dari nol lewat sesi wawancara bertahap — mulai dari gambaran umum proyek, masalah, pengguna, fitur, kebutuhan non-fungsional, sampai pemilihan tech stack — lalu menghasilkan file PRD_nama-proyek.md lengkap dengan workflow pembangunan proyek, serta saran file .md pendukung (techstack.md, ARCHITECTURE.md, TASKS.md, dll). Gunakan skill ini setiap kali pengguna ingin membuat PRD, merencanakan proyek/aplikasi/produk baru, menyusun spesifikasi atau kebutuhan produk, menentukan scope MVP, memilih tech stack, atau berkata "buatkan PRD", "saya punya ide aplikasi", "bantu rancang proyek", "product requirements", "project brief", walaupun pengguna tidak menyebut kata "PRD" secara eksplisit.
---

# PRD Builder

Skill ini memandu pengguna merancang PRD dari nol dengan **wawancara terstruktur**, lalu merangkum jawabannya menjadi dokumen `PRD_<nama-proyek>.md` yang bisa langsung dipakai untuk membangun proyek.

Alasan wawancara (bukan langsung menulis): PRD yang baik lahir dari keputusan pengguna, bukan tebakan Claude. Pengguna sering baru punya ide kasar; pertanyaan yang tepat membantu mereka menemukan scope, prioritas, dan batasan yang belum terpikirkan.

## Bahasa

Gunakan bahasa yang dipakai pengguna (default: Bahasa Indonesia). Istilah teknis boleh tetap dalam bahasa Inggris (misalnya *user story*, *endpoint*, *MVP*). Nama file mengikuti format `PRD_<nama-proyek>.md`.

## Alur kerja

```
Fase 0 Pembuka → Fase 1–7 Wawancara → Ringkasan & Konfirmasi → Tulis PRD + Workflow → Saran file pendukung
```

### Fase 0 — Pembuka

Sapa singkat, jelaskan bahwa akan ada beberapa putaran pertanyaan pendek (sekitar 7 fase), dan bahwa jawaban "belum tahu" atau "sarankan saja" selalu boleh. Langsung mulai Fase 1; jangan menunggu persetujuan.

Jika pengguna sudah memberi deskripsi proyek di pesan awal, **ekstrak dulu semua yang sudah terjawab** dan lewati pertanyaan yang jawabannya sudah jelas. Jangan menanyakan ulang hal yang sudah dikatakan.

### Fase 1–7 — Wawancara

Tanyakan **satu fase per giliran**, maksimal 3–5 pertanyaan per giliran, supaya pengguna tidak kewalahan. Bank pertanyaan lengkap ada di `references/pertanyaan.md` — baca file itu sebelum mulai wawancara.

| Fase | Topik | Tujuan |
|------|-------|--------|
| 1 | Gambaran umum | Nama, deskripsi satu kalimat, tujuan, jenis proyek (web/mobile/API/dll) |
| 2 | Masalah & pengguna | Masalah yang diselesaikan, target pengguna, persona, solusi yang sudah ada |
| 3 | Fitur & scope | Fitur inti, prioritas (must/should/could), apa yang **tidak** dibangun |
| 4 | Alur & data | Alur pengguna utama, entitas data utama, integrasi pihak ketiga |
| 5 | Non-fungsional | Performa, keamanan, skala, aksesibilitas, kepatuhan/regulasi |
| 6 | Tech stack | Frontend, backend, database, hosting, tools, preferensi & batasan tim |
| 7 | Eksekusi | Tim, timeline, budget, metrik sukses, risiko |

Cara bertanya yang baik:

- Jika tool `ask_user_input_v0` tersedia dan pertanyaannya punya pilihan yang jelas (misalnya jenis platform, skala pengguna), gunakan tombol pilihan agar mudah dijawab di ponsel. Untuk pertanyaan terbuka (misalnya "ceritakan masalahnya"), tanyakan dengan teks biasa.
- Beri contoh singkat pada pertanyaan yang abstrak, supaya pengguna tahu level detail yang diharapkan.
- Jika jawaban pengguna samar, ajukan satu pertanyaan lanjutan yang spesifik — jangan menebak diam-diam.
- Pada Fase 6, **berikan rekomendasi beralasan** (2–3 opsi dengan trade-off singkat) berdasarkan jawaban Fase 1–5, bukan hanya menanyakan "pakai teknologi apa?". Hormati preferensi atau keahlian yang disebut pengguna; jika pengguna tidak punya preferensi, rekomendasikan stack paling sederhana yang memenuhi kebutuhan.
- Jika pengguna menjawab "terserah/sarankan saja", buat keputusan sementara, tandai sebagai **asumsi** di PRD, dan lanjut.
- Satu kalimat konfirmasi singkat di akhir tiap fase ("Oke, dicatat: ...") sudah cukup — jangan mengulang seluruh jawaban.

### Ringkasan & konfirmasi

Setelah Fase 7 selesai, tampilkan **ringkasan satu layar** (nama, tujuan, pengguna, fitur MVP, tech stack, asumsi yang dibuat). Tanyakan apakah ada yang perlu diubah sebelum PRD ditulis. Ini murah dilakukan dan mencegah penulisan ulang dokumen panjang.

### Menulis PRD + Workflow

Setelah pengguna setuju:

1. Baca `references/template-prd.md` dan ikuti strukturnya.
2. Isi semua bagian dengan jawaban pengguna. Bagian yang tidak dijawab ditulis sebagai asumsi eksplisit (`> **Asumsi:** ...`) atau pertanyaan terbuka di bagian "Open Questions" — jangan dikarang seolah-olah pengguna yang memutuskan.
3. Tulis **Workflow Pembangunan** sebagai bagian dari PRD: fase-fase kerja berurutan (setup → fondasi → fitur inti → integrasi → testing → deploy → pasca-rilis), tiap fase berisi tujuan, deliverable, checklist tugas, dan kriteria selesai (*definition of done*). Urutan harus mengikuti ketergantungan teknis nyata dari stack dan fitur yang dipilih, bukan template generik.
4. Simpan ke `/mnt/user-data/outputs/PRD_<nama-proyek>.md`. Normalisasi nama proyek: huruf kecil atau kapital konsisten, spasi diganti `-`, tanpa karakter khusus (contoh: "Toko Kopi Kita" → `PRD_toko-kopi-kita.md`).
5. Bagikan file dengan `present_files`. Setelah itu cukup beri ringkasan 2–3 kalimat; pengguna bisa membuka dokumennya langsung.

### Saran file .md pendukung

Setelah PRD dibagikan, tawarkan file pendukung yang relevan. Baca `references/dokumen-pendukung.md` untuk daftar lengkap dan kapan masing-masing berguna. Pilih hanya yang relevan dengan proyek ini (proyek kecil tidak butuh sepuluh dokumen), tampilkan sebagai daftar singkat berisi nama file + fungsinya dalam satu baris, lalu tanyakan mana yang ingin dibuatkan. Jika pengguna memilih, buatkan file-nya dengan isi konsisten dengan PRD (stack, nama entitas, dan keputusan harus sama persis).

## Prinsip kualitas

- **Spesifik dan dapat diuji.** Kebutuhan seperti "aplikasi harus cepat" diubah menjadi angka ("halaman utama termuat < 2 detik pada 4G"). Fitur ditulis sebagai *user story* dengan *acceptance criteria*.
- **Scope eksplisit.** Selalu ada bagian "Di luar scope" supaya MVP tidak melebar.
- **Konsisten.** Nama fitur, entitas, dan teknologi harus identik di seluruh dokumen.
- **Jujur soal ketidakpastian.** Asumsi dan pertanyaan terbuka ditandai jelas.
- **Proporsional.** Proyek kecil → PRD ringkas. Proyek enterprise → lebih rinci pada keamanan, skala, dan kepatuhan.
- **Jangan menunda output.** Jika pengguna ingin berhenti bertanya dan langsung dibuatkan PRD, tulis PRD dengan informasi yang ada dan tandai semua celah sebagai asumsi.

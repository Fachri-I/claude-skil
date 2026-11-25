# Saran Dokumen Pendukung (.md)

Tawarkan hanya yang relevan. Proyek kecil/MVP cukup 3–4 file inti; proyek enterprise bisa memakai hampir semuanya. Semua isi harus konsisten dengan PRD (nama stack, entitas, fitur).

## Daftar isi
- Inti (hampir selalu berguna)
- Teknis
- Kualitas & operasional
- Untuk pengembangan dengan AI
- Rekomendasi per ukuran proyek

---

## Inti (hampir selalu berguna)

| File | Fungsi | Isi utama |
|------|--------|-----------|
| `techstack.md` | Keputusan teknologi dan alasannya | Daftar teknologi + versi, alasan pemilihan, alternatif yang ditolak, batasan |
| `README.md` | Pintu masuk proyek | Deskripsi, cara instal & menjalankan, struktur folder, perintah penting |
| `TASKS.md` | Papan tugas turunan dari workflow PRD | Checklist per fase, status, prioritas, penanggung jawab |
| `ARCHITECTURE.md` | Gambaran arsitektur | Komponen, alur data, diagram, keputusan desain utama |

## Teknis

| File | Fungsi | Isi utama |
|------|--------|-----------|
| `DATABASE.md` | Rancangan basis data | ERD, tabel/kolom, relasi, indeks, strategi migrasi, data seed |
| `API.md` | Kontrak API | Endpoint, method, request/response, kode error, autentikasi |
| `UI-UX.md` | Panduan antarmuka | Daftar halaman, wireframe/alur, komponen, palet warna, tipografi |
| `FOLDER-STRUCTURE.md` | Struktur kode | Pohon folder, aturan penamaan, tempat menaruh tiap jenis file |
| `CONVENTIONS.md` | Standar koding | Gaya kode, penamaan, format commit, strategi branch, aturan code review |
| `ENV.md` / `.env.example` | Konfigurasi | Daftar variabel lingkungan, fungsinya, contoh nilai (tanpa rahasia) |

## Kualitas & operasional

| File | Fungsi | Isi utama |
|------|--------|-----------|
| `SECURITY.md` | Kebijakan keamanan | Model ancaman, autentikasi/otorisasi, penanganan data sensitif, checklist OWASP |
| `TESTING.md` | Strategi pengujian | Jenis test, cakupan target, tools, skenario kritis, data uji |
| `DEPLOYMENT.md` | Panduan rilis | Environment (dev/staging/prod), pipeline CI/CD, rollback, monitoring, backup |
| `CHANGELOG.md` | Riwayat perubahan | Perubahan per versi (format Keep a Changelog) |
| `CONTRIBUTING.md` | Panduan kontributor | Cara berkontribusi, alur PR, aturan komunikasi (untuk tim atau open source) |
| `GLOSSARY.md` | Kamus istilah domain | Istilah bisnis dan teknis agar tim punya bahasa yang sama |
| `DECISIONS.md` | Catatan keputusan (ADR) | Keputusan penting: konteks, pilihan, konsekuensi, tanggal |

## Untuk pengembangan dengan AI

| File | Fungsi | Isi utama |
|------|--------|-----------|
| `CLAUDE.md` / `AGENTS.md` | Instruksi tetap untuk asisten AI di repo | Ringkasan proyek, stack, perintah build/test, konvensi, hal yang dilarang |
| `PROMPTS.md` | Kumpulan prompt kerja | Prompt siap pakai per fase workflow (membuat fitur, review, debugging) |

## Rekomendasi per ukuran proyek

- **Prototipe / tugas kuliah / MVP kecil:** `techstack.md`, `README.md`, `TASKS.md`, (opsional `DATABASE.md`)
- **Produk startup / aplikasi bisnis:** tambahkan `ARCHITECTURE.md`, `DATABASE.md`, `API.md`, `UI-UX.md`, `TESTING.md`, `DEPLOYMENT.md`
- **Enterprise / data sensitif:** tambahkan `SECURITY.md`, `DECISIONS.md`, `CONVENTIONS.md`, `GLOSSARY.md`, `CONTRIBUTING.md`
- **Dikerjakan bersama asisten AI (Claude Code, dll):** tambahkan `CLAUDE.md`/`AGENTS.md` dan `PROMPTS.md`

## Cara menawarkan

Tampilkan 4–8 file yang paling relevan sebagai daftar singkat (nama + fungsi satu baris), beri tanda yang direkomendasikan untuk dibuat lebih dulu, lalu tanyakan mana yang ingin dibuatkan. Jika pengguna memilih, buat file satu per satu atau sekaligus dan bagikan dengan `present_files`.

---
name: stitch-design-builder
description: Mengubah design plan UI/UX (file .md), kumpulan prompt/DESIGN.md lama, atau gambar referensi menjadi paket siap pakai untuk Google Stitch yang konsisten, yaitu (1) file konsistensi aset dan style, (2) Design Audit & Technical Breakdown, (3) Stitch Prompt dipisah per peran pengguna (satu file per peran), (4) satu DESIGN.md untuk seluruh peran, dan (5) HTML statis Tailwind bila diminta. Gunakan skill ini setiap kali user melampirkan design plan, wireframe, screenshot, mockup, prompt Stitch lama, atau DESIGN.md dan ingin merealisasikan, merapikan, memisahkan per peran, atau menyeragamkannya di Google Stitch; juga untuk permintaan "prompt Stitch", "DESIGN.md", "audit desain", "prompt konsistensi", "pisah prompt per user/peran", atau "HTML Tailwind dari desain ini", walaupun user tidak menyebut kata "skill". Also use when the user wants a consistent, role-split Stitch-ready design package.
---

# Stitch Design Builder

Skill ini menjembatani **design plan UI/UX, prompt lama, atau gambar referensi** dengan **Google Stitch**. Tujuannya: desain bisa direalisasikan di Stitch dengan hasil yang **seragam di semua layar dan semua peran**, tanpa user menulis prompt dan design system dari nol.

Kunci konsistensi ada pada empat hal: satu sumber token (audit lalu DESIGN.md), aset yang dikunci sejak awal, blok teks yang identik di semua file (dibangun lewat placeholder, bukan diketik ulang), dan pemeriksaan otomatis sebelum menyerahkan hasil.

## Output

| # | Output | Bahasa | File |
|---|--------|--------|------|
| 0 | Konsistensi Aset & Style | Catatan Indonesia, prompt English | `00-konsistensi-aset-style.md` |
| 1 | Design Audit & Technical Breakdown | Indonesia | `01-design-audit.md` |
| 2 | Stitch Prompt, **satu file per peran** | Catatan Indonesia, prompt English | `02-stitch-prompt-<peran>.md` |
| 3 | DESIGN.md resmi Stitch (alpha), **satu untuk semua peran** | English | `DESIGN.md` |
| 4 | HTML statis + Tailwind, satu file per halaman | Kode English, teks UI mengikuti desain | `html/<halaman>.html` (hanya bila diminta atau dijanjikan di ringkasan) |
| 5 | Restore point | Indonesia | `RESTORE_POINT.md` (hanya bila user atau proyek menghendaki) |

Bila hanya ada satu peran, hasilnya satu file `02-stitch-prompt.md`. Penjelasan dan ringkasan kepada user memakai bahasa Indonesia; isi prompt dan DESIGN.md memakai English; teks UI mengikuti bahasa produk (biasanya Indonesia).

## Alur kerja

### Langkah 1: Cek input dan tentukan sumber kebenaran

- Baca **semua** file yang dilampirkan sebelum menulis apa pun. Jangan menebak isi dari nama file. Jika tidak ada lampiran atau file tidak terbaca, minta user melampirkan; itu satu-satunya kondisi untuk berhenti bertanya.
- Bila input tidak lengkap (tanpa warna, font, platform), jangan berhenti bertanya. Ambil asumsi yang masuk akal dan tulis di bagian Asumsi audit.
- Bila ada **beberapa versi** (DESIGN.md v1 dan v2, prompt lama dan baru, desain admin dari proyek lain), buat tabel peran file di audit: yang terbaru dan selaras dengan plan menjadi sumber utama; yang lama hanya pembanding atau bahan perluasan. Plan teks menang untuk keputusan eksplisit (nama, konten, perilaku); gambar menang untuk gaya visual. Catat tiap pertentangan.
- **Centang lama diabaikan** bila user berkata semua prompt dianggap belum dikerjakan; reset semua kotak menjadi `[ ]`. Bila user menyebut sebagian sudah dikerjakan, pertahankan hanya yang ia sebut. Catatan tangan user pada item lama (misalnya "belum butuh") dipertahankan sebagai penanda opsional, bukan dibuang diam-diam.
- **DESIGN.md yang sudah ada di input**: bila sudah berformat resmi dan memuat data dari skill lain (baris `Dial:`, motif identitas, alasan per keputusan, bagian tambahan), pertahankan semuanya dan lengkapi hanya yang kosong. Bila formatnya lama (properti `size`/`weight`, array `scale`, judul bernomor), konversi ke format resmi tanpa mengubah nilai dan catat di audit. Aturan lengkap ada di `references/design-md-template.md`.
- Cek yang bisa dihitung, jangan ditebak: jalankan `scripts/contrast.py` untuk kontras dan hari-dalam-pekan pada tanggal contoh.

### Langkah 2: Tentukan peran dan bagi layar

Aturan pembagian ada di `references/stitch-prompt-guide.md` (bagian Pembagian per peran). Ringkasnya: layar publik atau bersama masuk ke file peran utama (biasanya pengguna akhir); file peran lain hanya berisi layar dan varian khususnya; tiap file berdiri sendiri karena memuat Global Prompt yang identik.

### Langkah 3: Susun audit dulu (sumber kebenaran)

Semua token diputuskan **di audit**, lalu dipakai apa adanya di output lain. Format lengkap di `references/audit-template.md`; baca sebelum menulis. Wajib ada: peran tiap file input, asumsi, inventaris layar dengan nomor tetap, kontras terhitung, dan daftar temuan (konflik, gap, risiko) beserta keputusan yang diambil.

### Langkah 4: Turunkan output lain dari audit

Urutan: DESIGN.md, lalu file konsistensi dan Global Prompt, lalu prompt per peran, lalu HTML bila diminta.

- **DESIGN.md**: `references/design-md-template.md`. Satu file berformat resmi Stitch (alpha): front matter YAML dengan token `colors`, `typography`, `rounded`, `spacing`, `motion`, `components`, diikuti bagian baku berurutan (Overview sampai Do's and Don'ts) dan bagian tambahan bila perlu. Nama token langsung bisa menjadi kunci `tailwind.config`.
- **File konsistensi**: `references/consistency-guide.md`. Berisi kunci aset, urutan kerja, Global Prompt induk, Design System Board, kunci dan awalan jangkar, prompt audit konsistensi, checklist, dan tabel troubleshooting.
- **Prompt per peran**: `references/stitch-prompt-guide.md`.
- **HTML**: `references/html-guidelines.md`.
- **Contoh nyata**: `references/example-blocks/` berisi lima blok (Global Prompt, Prompt Pengingat, penjaga, `ds`, refinement) dari proyek Ruang Tumbuh. Pakai sebagai gambaran kedalaman dan format; nilai selalu diganti dengan token proyek yang sedang dikerjakan.

### Langkah 5: Bangun lewat placeholder, lalu periksa

Tulis sumber file dengan placeholder (`{{GLOBAL}}`, `{{REMINDER}}`, `{{GUARD}}`, `{{DS}}`, `{{REFINE}}`) agar blok yang harus identik tidak pernah diketik ulang. Taruh blok di `src/blocks/*.txt`, lalu:

```
python scripts/build.py <src_dir> <out_dir>
python scripts/check.py <out_dir>
python scripts/lint_design.py <out_dir>/DESIGN.md
```

`lint_design.py` memeriksa DESIGN.md terhadap spesifikasi resmi (nama properti token, satuan dimensi, tanpa array di `spacing`, rujukan token, urutan dan nama bagian, kontras pasangan komponen). Perbaiki semua ERROR sampai `OK`; bila linter resmi Stitch tersedia di lingkungan, jalankan juga.

`check.py` memastikan: setiap hex di prompt ada di DESIGN.md; setiap hex DESIGN.md ada di Global Prompt; Global Prompt identik di semua file; tidak ada placeholder tersisa; semua kotak `[ ]` bila diminta direset; tidak ada prompt layar di atas 250 kata. Perbaiki sampai bersih. Cek manual tambahan:

1. Setiap layar di inventaris punya prompt desktop dan varian mobile; state dan dialog ada bila disebut plan.
2. Kontras teks utama minimal 4,5:1 (teks besar 3:1). Jika sumber melanggar, tandai di audit dan tawarkan koreksi; jangan diam-diam mengubah nilai.
3. Tidak ada gambar remote, foto, atau ilustrasi; poster memakai gradien kategori.
4. Konten contoh ditandai `(sample copy)`; hari dan tanggal contoh cocok.

### Langkah 6: Simpan dan sampaikan

Simpan di `/mnt/user-data/outputs/<project-slug>/`:

```
<project-slug>/
├── 00-konsistensi-aset-style.md
├── 01-design-audit.md
├── 02-stitch-prompt-<peran>.md   (satu per peran)
├── DESIGN.md
├── RESTORE_POINT.md              (bila diminta)
└── html/                         (bila diminta)
```

Panggil `present_files` dengan `00-konsistensi-aset-style.md` atau `01-design-audit.md` di depan. Balasan singkat, bahasa Indonesia: (1) satu kalimat isi paket (jumlah peran, layar, prompt); (2) tiga asumsi atau keputusan terpenting yang perlu dikonfirmasi; (3) cara pakai: unggah DESIGN.md, tempel Global Prompt, buat Design System Board, setujui layar jangkar, kerjakan layar per batch, audit tiap batch. Jangan mengulang isi file.

## Prinsip yang menjaga kualitas

- **Satu sumber token.** Ubah di audit, lalu sebarkan ke semua output lewat build, bukan edit tangan per file.
- **DESIGN.md mengikuti spesifikasi resmi Stitch.** Format yang valid membuat Stitch dan tool coding membaca token dengan benar; nama properti, satuan, dan urutan bagian dijaga oleh `lint_design.py`.
- **Kunci aset sebelum gaya.** Font, set ikon, logo, gaya poster, avatar, QR, empty state, dan panel merek auth diputuskan dan ditulis di Global Prompt. Aset yang tidak ada di sumber diberi label asumsi.
- **Jangan mengarang konten tersembunyi.** Tiap prompt layar berakhir dengan kalimat penjaga (`{{GUARD}}`). Buang statistik, klaim, logo mitra, testimoni, dan contoh kredensial dari desain lama. Detail infrastruktur spesifik vendor yang tidak ada di tech stack digeneralisasi atau dibuang.
- **Hormati larangan di plan.** Fitur yang dilarang plan (misalnya "tanpa aksi massal", "tanpa pencarian") tidak boleh muncul lewat desain lama. Bila desain lama membawa fitur di luar plan, pindahkan ke Bagian B "perluasan, menunggu persetujuan", disesuaikan ke design system bersama.
- **Satu aspek per perbaikan.** Prompt refinement memperbaiki satu hal dan diawali "Keep everything else unchanged."
- **Spesifik mengalahkan estetis.** Angka dan hex lebih berguna bagi Stitch daripada kata suasana.
- **Untuk gambar referensi, nilai perkiraan diberi label `(estimated)`.**
- **Jaga ukuran.** Prompt layar di bawah sekitar 250 kata; pecah bila lebih. Satu layar, satu tujuan; varian state boleh sebagai frame tambahan, tetapi pecah menjadi prompt terpisah bila hasil tidak seragam.
- **Lengkap sejak awal.** Beri varian mobile untuk setiap layar, termasuk layar yang dilewatkan plan lama (profil, dasbor, auth, halaman sistem).
- **Label status bukan enum mentah.** Petakan enum ke label teks dan pasangkan dengan pill bertulisan, bukan warna saja.
- **Tahan keputusan yang belum disetujui.** Item yang menunggu keputusan ditaruh di bagian "Menunggu keputusan" dan tidak dikerjakan sebelum disetujui.

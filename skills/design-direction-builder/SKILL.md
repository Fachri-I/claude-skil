---
name: design-direction-builder
description: Menyusun arah desain visual dari nol untuk produk yang sudah punya PRD dan tech stack tetapi belum punya referensi desain. Membaca PRD dan techstack, mewawancarai selera singkat (tema, warna, anti-referensi), merumuskan tiga arah desain yang berbeda secara struktur, membuat mockup HTML statis dua layar kunci per arah, menilainya dengan rubrik anti-generik, lalu mengunci arah pilihan menjadi DESIGN.md berformat resmi Stitch (token, dial, motif identitas) untuk skill design-plan-builder, stitch-design-builder, dan agen coding. Gunakan skill ini setiap kali user bingung menentukan desain, ingin beberapa referensi atau mockup, moodboard, pilihan tampilan, tema dan palet, atau berkata "arah desain", "referensi desain", "desainnya seperti apa", "visual terlihat datar atau generik", walaupun tidak menyebut kata skill. Also use when the user needs several design direction options before UI/UX planning or Stitch.
---

# Design Direction Builder

Skill ini menjawab satu pertanyaan: **"Tampilan produk ini sebaiknya seperti apa?"** Ia mengubah PRD dan tech stack yang sudah selesai menjadi beberapa arah desain yang bisa dilihat, dibandingkan, dan dipilih, lalu mengunci pilihannya sebagai `DESIGN.md`. Ia tidak membuat desain lengkap: hanya keputusan visual dan bukti visual berupa mockup beberapa layar kunci.

Posisi dalam rantai: PRD Builder, Techstack Recommender, **Design Direction Builder**, Design Plan Builder, Stitch Design Builder. Hasil skill ini menjadi sumber gaya bagi dua skill terakhir dan bagi agen coding (OpenCode dan sejenisnya) yang mengimplementasikan desain.

## Output

| # | Output | Bahasa | File |
|---|--------|--------|------|
| 1 | Dokumen kerja: ringkasan PRD, jawaban wawancara, Design Read, tiga arah, perbandingan, rekomendasi, hasil rubrik, keputusan | Indonesia | `design-direction.md` |
| 2 | Mockup statis, satu file per arah, dua layar kunci | Kode English, teks UI mengikuti bahasa produk | `mockup-arah-a.html`, `mockup-arah-b.html`, `mockup-arah-c.html` |
| 3 | Hasil kunci arah terpilih, format resmi Stitch | English | `DESIGN.md` (dibuat hanya setelah user memilih arah) |
| 4 | Restore point | Indonesia | `RESTORE_POINT.md` (hanya bila user atau proyek menghendaki) |

Penjelasan dan ringkasan kepada user memakai bahasa Indonesia.

## Prinsip yang menjaga kualitas

- **Pengguna adalah penulis arah.** Agen menyusun, memformat, dan memperluas masukan user; ia tidak mengarang selera. Arah yang dikarang agen sendiri cenderung terasa generik dan seragam antar proyek, jadi wawancara bukan formalitas.
- **Tiga arah harus berbeda secara struktur** (dial, bahasa visual, motif identitas, tata letak), bukan hanya beda warna.
- **Setiap keputusan besar punya alasan satu baris.** Bila alasannya hanya "ini default" atau "terlihat aman", keputusan dibuang atau dikerjakan ulang.
- **Hindari datar dan hindari slop sekaligus.** Menghapus pola generik saja menghasilkan desain steril; kehidupan visual harus ditambahkan lewat titik fokus, satu aksen sengaja, dan satu motif identitas.
- **Satu tempat berani.** Biarkan satu elemen menjadi hal yang diingat, jaga sisanya tenang dan disiplin. Potong dekorasi yang tidak melayani brief.
- **Konten mockup berasal dari PRD.** Dilarang mengarang statistik, testimoni, nama orang, fitur, atau klaim. Pakai placeholder jujur.
- **Spesifik mengalahkan estetis.** Hex, ukuran, dan nama font lebih berguna daripada kata suasana.
- **Jujur tentang batas.** Angka yang tidak diukur ditulis "tidak diukur". Asumsi ditulis sebagai asumsi.

## Alur kerja

### Langkah 1: Baca input

Baca **semua** file yang dilampirkan sebelum menulis apa pun: `PRD_<proyek>.md`, `techstack.md`, dan bila ada referensi visual, DESIGN.md lama, atau tautan situs. Jangan menebak isi dari nama file. Jika PRD atau techstack tidak ada atau tidak terbaca, minta user melampirkannya; itu satu-satunya alasan berhenti dan bertanya sebelum Langkah 2. Jika sudah ada DESIGN.md yang punya arah jelas, jangan membuat arah baru: tawarkan melengkapinya (lihat `references/design-md-template.md`, bagian "Bila sudah ada DESIGN.md").

Ekstrak dan tulis ringkasan 5-8 baris: jenis produk, pengguna dan konteks pakainya, tugas utama tiap peran, fitur utama, batasan teknis dari techstack (library UI, Tailwind, platform, mobile atau web), bahasa antarmuka, dan kata sifat yang tersirat. Tunjukkan ringkasan itu kepada user.

### Langkah 2: Wawancara selera

Ikuti `references/interview.md`. Ringkasnya: empat sampai lima pertanyaan pilihan ganda (gunakan alat pertanyaan bertombol bila tersedia, jika tidak, daftar bernomor), mencakup kesan utama, kepadatan, tema terang atau gelap, warna wajib atau terlarang, **anti-referensi** (tampilan yang dianggap membosankan), tiga kata sifat, dan satu produk yang tampilannya disukai sebagai inspirasi prinsip, bukan untuk ditiru. Tanyakan juga dua layar kunci mana yang akan dibuatkan mockup; bila user tidak peduli, pilih dari PRD (layar yang paling sering dilihat dan layar fitur inti) dan sebut pilihannya.

Bila user menjawab "terserah" atau tidak memberi masukan: katakan terus terang bahwa arah yang disusun agen berisiko terasa generik, tetap minta ringkasan minimal (produk, audiens, suasana), dan tandai seluruh hasil sebagai **draf**.

### Langkah 3: Rumuskan tiga arah (rencana dulu, sebelum membangun)

Tulis satu baris **Design Read**: `Membaca ini sebagai: <jenis halaman> untuk <audiens>, bergaya <bahasa visual>, dial <ENERGY/RHYTHM/MOTION>.` Lalu susun tiga arah dengan `references/antislop-integration.md` (dial, tuas kehidupan visual) dan format di `references/direction-template.md`. Setiap arah memuat nama dan konsep satu kalimat, mengapa cocok dengan PRD, dial, bahasa visual, motif identitas, satu aksen, palet (2-3 warna inti + 1 aksen, hex), tipografi (satu atau dua keluarga Google Fonts dengan peran jelas), arketipe tata letak, cara membangun kedalaman, aset yang dibuat (SVG, dengan alasan), alasan satu baris per keputusan, dan risiko.

Susun satu arah aman (dial rendah), satu seimbang, satu berani. Lalu **tinjau rencana terhadap brief** sebelum membangun: bila ada bagian yang terbaca seperti default untuk produk sejenis, ganti, dan catat apa yang diubah dan alasannya. Jika skill `frontend-design` tersedia di lingkungan, baca dulu; daftar ciri generik di dalamnya berlaku sebagai bahan tinjauan (misalnya latar krem dengan serif dan aksen terakota, atau kartu identik dengan bayangan abu yang sama).

### Langkah 4: Bangun mockup

Satu file HTML per arah, dua layar kunci per file, konten dari PRD. Aturan teknis dan konten ada di `references/mockup-guidelines.md`; baca sebelum menulis. Tulis satu arah dalam satu kali pembuatan file, jangan ditambal berulang. Jalankan `python scripts/contrast.py '#FG' '#BG' ...` untuk pasangan warna teks dan latar utama setiap arah, dan simpan hasilnya sebagai bukti.

### Langkah 5: Nilai dengan rubrik

Jalankan `references/critique-rubric.md` pada setiap arah. Tulis PASS atau FAIL dengan bukti konkret. Perbaiki FAIL dan ulangi sampai bersih sebelum menyerahkan; sebutkan apa yang diperbaiki.

### Langkah 6: Rekomendasi dan keputusan

Tulis `design-direction.md` dengan tabel perbandingan tiga arah (kesan, kekuatan, risiko, cocok bila), satu arah yang direkomendasikan beserta alasan dan risikonya, dan hasil rubrik. Sampaikan mockup ke user. User boleh memilih satu arah, menggabungkan elemen dari beberapa arah, atau meminta revisi. Batasi **dua putaran revisi**; sesudahnya, tawarkan mengunci arah terbaik saat itu dan menunda penyempurnaan ke tahap Design Plan.

### Langkah 7: Kunci arah menjadi DESIGN.md

Setelah user memilih, tulis `DESIGN.md` mengikuti `references/design-md-template.md`: format resmi Stitch (token YAML plus bagian baku berurutan), ditambah data arah di Overview (Design Read, baris `Dial:`, motif identitas, aksen, alasan satu baris per keputusan). Nilai hanya dari arah terpilih dan hasil wawancara; jangan menambah nilai baru. Jalankan `python scripts/lint_design.py DESIGN.md` sampai `OK`. DESIGN.md hanya memuat data desain, bukan perintah untuk agen.

### Langkah 8: Simpan dan sampaikan

Simpan di `/mnt/user-data/outputs/<project-slug>/` dan panggil `present_files` dengan `design-direction.md` di depan, lalu mockup dan `DESIGN.md`. Balasan singkat, bahasa Indonesia: (1) satu kalimat isi paket; (2) arah yang direkomendasikan dan satu risikonya; (3) tiga asumsi atau keputusan yang perlu dikonfirmasi; (4) langkah berikutnya: berikan `DESIGN.md` ke skill design-plan-builder dan stitch-design-builder, dan di proyek implementasi letakkan `DESIGN.md` di akar proyek lalu pasang antislop (`references/antislop-integration.md`, bagian serah terima). Jangan mengulang isi file.

## Batas skill

Skill ini tidak membuat semua halaman (itu tugas design-plan-builder), tidak membuat logo atau aset gambar final, tidak membuat kode frontend produksi, dan mockupnya statis tanpa fungsi atau backend.

## Referensi

| File | Dibaca saat |
|---|---|
| `references/interview.md` | Langkah 2 |
| `references/antislop-integration.md` | Langkah 3 dan serah terima |
| `references/direction-template.md` | Langkah 3 dan 6 |
| `references/mockup-guidelines.md` | Langkah 4 |
| `references/critique-rubric.md` | Langkah 5 |
| `references/design-md-template.md` | Langkah 7 |

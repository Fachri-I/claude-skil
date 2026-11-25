# Panduan mockup HTML

Satu file per arah (`mockup-arah-a.html`, `-b`, `-c`), dua layar kunci per file. Tujuannya membandingkan arah secara visual, bukan membangun halaman produksi. Semua arah memakai **konten yang sama** (dari PRD) agar yang dibandingkan murni tampilannya.

## Rencana sebelum menulis kode

Untuk tiap arah, jawab dalam beberapa baris: palet (hex), font dan perannya, arketipe tata letak, titik fokus tiap layar, motif identitas, dan satu hal yang berani. Bandingkan dengan tiga arah lain: bila dua arah terbaca seperti variasi satu gaya, ubah salah satunya sebelum menulis kode.

## Struktur file

- Satu berkas HTML mandiri: CSS dan JS (bila ada) di dalam berkas. Tanpa gambar remote. Font dari Google Fonts boleh lewat tag `<link>` dengan susunan fallback yang nyata; stylesheet atau skrip dari host lain tidak.
- Warna, ukuran, jarak, dan radius sebagai CSS custom properties di `:root` yang nilainya sama dengan token yang akan masuk ke `DESIGN.md`.
- Dua layar sebagai dua `<section>`, masing-masing diberi pita label kecil dan netral (`Arah A, Layar 1: <nama>`) yang jelas bukan bagian produk. Tambahkan catatan "mockup statis" yang terlihat.
- Lebar rancangan desktop 1440px dan mobile 375px; layar harus responsif di antaranya dan tidak overflow horizontal di 375px.
- Elemen semantik (`header`, `nav`, `main`, `button`, `a`, `label`), satu `h1` per layar, urutan heading benar.

## Isi dan konten

- **Hanya dari PRD**: nama fitur, alur, istilah, label status. Dilarang mengarang statistik, delta, testimoni, nama orang, fitur, klaim keamanan atau kinerja. Gantikan dengan placeholder jujur seperti `[DATA ASLI]` atau "Segera hadir"; bagian kosong lebih baik daripada bagian palsu.
- **Aset**: logo berupa nama produk dalam teks (atau `[LOGO]` bila nama sementara); avatar berupa inisial atau bentuk geometris; field formulir kosong atau placeholder jujur. Ilustrasi dibuat sebagai SVG inline dan harus berhubungan dengan produk, bukan dekorasi acak.
- **Navigasi dan tombol**: setiap item menuju layar yang ada atau diberi label "Segera hadir" yang terlihat. Tombol tanpa perilaku diberi penanda bahwa ini mockup.
- **Teks**: CTA spesifik pada aksinya (bukan "Get Started", "Learn More", "Try Now"), tanpa kata pemasaran klise, tanpa em dash di teks antarmuka. Bahasa antarmuka sama dengan produk.

## Visual

- **Hero atau layar utama** dimulai dari hal paling khas di dunia produk (headline, tampilan produk, momen interaktif), bukan formula angka besar + label kecil + gradien aksen.
- **Layar aplikasi** dibangun di sekitar keputusan yang diambil pengguna di layar itu. Hindari susunan bawaan sidebar + baris kartu statistik + grafik + tabel.
- **Tata letak** dari kebutuhan konten, bukan template: hindari bento mosaik, kartu identik, "How It Works" selalu tiga langkah, bar logo "Trusted By", tiga kolom harga, footer empat kolom seragam, jendela terminal palsu.
- **Palet**: 2-3 warna inti + 1 aksen (netral tidak dihitung). Aksen hanya untuk hal terpenting. Tema gelap hanya dengan alasan tertulis.
- **Tipografi**: satu atau dua keluarga, jelas berbeda bila dua. Skala dengan kontras tegas (judul bisa 4 sampai 8 kali teks isi) dan variasi berat yang nyata. Panjang baris di bawah 80 karakter. Hindari pola umum: satu kata di headline diberi warna atau miring berbeda, label HURUF KAPITAL di atas setiap judul, penomoran 01/02/03 pada konten yang bukan urutan.
- **Kedalaman**: utamakan lapisan tonal, border, dan skala. Glass dan glow maksimal 1-2 elemen; bayangan hanya sebagai penanda elevasi dengan alasan. Latar bergrid, titik, atau blueprint hanya bila punya alasan identitas tertulis.
- **Ikon**: satu set, dengan alasan relevansi; tanpa emoji dekoratif dan tanpa ikon AI generik (kilat, bintang, robot, orb).
- **Gerak**: hover, fokus, dan aktif untuk semua elemen interaktif. Gerak yang tidak dipicu user dipakai hemat, paling banyak satu urutan pemuatan. `prefers-reduced-motion` dihormati.
- **Satu tempat berani**: satu elemen yang diingat; sisanya tenang.

## Dasar teknis dan aksesibilitas

- Kontras teks minimal 4,5:1 (teks besar 3:1), diukur dengan `python scripts/contrast.py '#FG' '#BG' ...` dan hasilnya dicatat di `design-direction.md`. Pasangan yang tidak diukur ditulis "tidak diukur".
- Status fokus terlihat; target sentuh minimal 44px; status tidak hanya dengan warna (pasangkan dengan teks atau ikon).
- Elemen interaktif memakai elemen native; kursor pointer pada yang bisa diklik.
- Tanpa pustaka eksternal bila CSS biasa cukup.

## Pemeriksaan sebelum menyerahkan

Buka kembali berkas yang ditulis: pastikan tag tertutup, tidak ada placeholder `{{...}}` yang tersisa, dan kedua layar terbaca. Bila lingkungan mendukung tangkapan layar, ambil satu di lebar 1440px dan satu di 375px untuk melihat hasilnya sebelum dinilai dengan rubrik; bila tidak, nyatakan bahwa tampilan tidak dirender.

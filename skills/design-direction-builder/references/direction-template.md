# Template: design-direction.md

Bahasa: Indonesia (istilah desain seperti token, dial, hero boleh tetap English). Dokumen kerja yang menjadi satu-satunya tempat membandingkan arah. Hasil kunci ada di `DESIGN.md`, bukan di sini.

Gunakan struktur persis di bawah ini.

````markdown
# Design Direction: <Nama Proyek>

## 1. Ringkasan Input
- File yang dibaca: <daftar>
- Produk, audiens, konteks pakai, bahasa antarmuka, batasan teknis dari techstack
- Layar kunci yang dibuatkan mockup: <dua layar> (dipilih user / dipilih dari PRD)
- Status: draf / berarah (jika wawancara dijawab penuh)

## 2. Masukan User
Kesan utama, tiga kata sifat, anti-referensi (kata user), produk yang disukai dan alasannya, kepadatan, tema, warna wajib atau terlarang. Tulis "tidak dijawab" bila kosong.

## 3. Asumsi
Tabel: | Hal | Asumsi | Alasan | Perlu konfirmasi? |
Wajib memuat: nama produk bila sementara, aset yang tidak ada (logo), pilihan layar kunci bila dipilih agen, dan keputusan atas konflik antar file input.

## 4. Design Read
`Membaca ini sebagai: <jenis halaman> untuk <audiens>, bergaya <bahasa visual>, dial <ENERGY/RHYTHM/MOTION>.`

## 5. Tiga Arah
Untuk setiap arah (A aman, B seimbang, C berani) tulis:
- **Nama dan konsep** (satu kalimat)
- **Mengapa cocok** dengan PRD dan masukan user
- **Dial**: ENERGY x / RHYTHM y / MOTION z
- **Bahasa visual dan motif identitas** (spesifik dan berulang), **satu aksen sengaja**
- **Palet**: 2-3 warna inti + 1 aksen, dengan hex, peran, dan pasangan kontras yang diukur
- **Tipografi**: keluarga font, peran, skala utama
- **Tata letak**: arketipe dan alasannya; di mana ia sengaja keluar dari grid
- **Kedalaman dan aset**: bagaimana hierarki dibangun, aset SVG apa dan mengapa
- **Alasan satu baris** untuk tiap keputusan besar (warna, tata letak, tipografi, jarak, kartu, ikon atau ilustrasi)
- **Hindari**: turunan dari anti-referensi
- **Risiko dan trade-off**
- **Mockup**: `mockup-arah-a.html` (dua layar)

## 6. Perbandingan
Tabel: | | Arah A | Arah B | Arah C |  dengan baris Kesan, Dial, Kekuatan, Risiko, Cocok bila, Biaya implementasi (rendah, sedang, tinggi).

## 7. Rekomendasi
Satu arah yang direkomendasikan, alasan, risiko, dan apa yang perlu diuji. Sebut jika menggabungkan elemen arah lain masuk akal.

## 8. Hasil Rubrik
Tabel PASS/FAIL per arah dengan bukti (lihat `critique-rubric.md`), dan catatan apa yang diperbaiki.

## 9. Keputusan
Arah terpilih, elemen gabungan (bila ada), putaran revisi ke-<n> dari maksimal 2, dan status `DESIGN.md` (belum dibuat / dibuat / lolos lint).
````

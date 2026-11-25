# Rubrik penilaian arah

Jalankan pada **setiap arah** sebelum menyerahkan. Tulis PASS atau FAIL dengan bukti konkret (bukan ringkasan umum). Bila ada FAIL, perbaiki lalu ulangi, dan sebut apa yang diperbaiki. Angka yang tidak diukur ditulis "tidak diukur", bukan diperkirakan.

| # | Pertanyaan | Lulus bila | Bukti |
|---|---|---|---|
| 1 | Design Read dan tiga dial dinyatakan, dan mockup konsisten dengannya? | ya (RHYTHM 3 dengan section seragam = FAIL) | kutip dial dan sebut contoh bagian |
| 2 | Ada satu titik fokus per layar, satu aksen sengaja, dan satu motif identitas yang berulang? | ya | sebut elemennya di tiap layar |
| 3 | Uji penukaran: jika logo dan nama produk ditukar, apakah desain masih terasa unik? | ya | satu kalimat alasan |
| 4 | Tiga arah berbeda secara struktur (dial, bahasa visual, motif, tata letak)? | ya | tabel perbedaan singkat |
| 5 | Setiap keputusan besar punya alasan satu baris? | ya | daftar keputusan tanpa alasan (harus kosong) |
| 6 | Ada konten karangan (statistik, testimoni, nama, klaim, fitur di luar PRD)? | tidak | hasil pencarian di berkas |
| 7 | Ada pola template (bento mosaik, kartu identik, tiga langkah, bar logo, tiga kolom harga, footer empat kolom seragam, susunan dashboard bawaan)? | tidak | sebut bagian yang diperiksa |
| 8 | Glass, glow, atau bayangan melewati batas dosis, atau latar bergrid tanpa alasan? | tidak | hitung elemen |
| 9 | Palet melewati 2-3 inti + 1 aksen? | tidak | daftar hex inti dan aksen |
| 10 | Ada teks di bawah kontras standar, atau overflow horizontal di 375px? | tidak | keluaran `scripts/contrast.py`; hasil pemeriksaan lebar |
| 11 | Ada tombol atau navigasi tanpa tujuan dan tanpa label "mockup" atau "Segera hadir"? Ada kemiripan jelas dengan produk populer tertentu? | tidak | daftar elemen |

## Tambahan: ciri generik yang sering lolos

Periksa juga apakah arah jatuh ke salah satu default berikut tanpa alasan dari brief: latar krem dengan serif tinggi kontras dan aksen terakota; latar hitam pekat dengan satu aksen hijau atau jingga menyala; tata letak koran dengan garis rambut dan sudut tanpa radius; satu radius dan satu bayangan abu yang sama di semua kartu; label huruf kapital di atas setiap judul; gradien ungu-biru bawaan; font bawaan sistem untuk judul tanpa alasan. Default boleh dipakai bila brief menuntutnya, tetapi harus tertulis sebagai pilihan dengan alasan.

## Pelaporan

Satu tabel per arah di `design-direction.md` bagian "Hasil Rubrik". Setelah perbaikan, laporkan hasil akhir dan daftar perbaikan, bukan semua iterasi.

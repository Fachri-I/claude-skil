# Panduan gerak dan interaksi (motion)

Dibaca saat menyusun spesifikasi gerak di `UIUX_<project>.md` (Fase 2) dan bagian "Animasi dan gerak" di `FRONTEND_<project>.md` (Fase 4). Tujuannya: website terasa hidup dan tidak kaku, tanpa menjadi berat atau mengganggu.

## 1. Prinsip

- Gerak melayani tujuan: memberi orientasi, umpan balik, hierarki, atau identitas. Tiap efek punya alasan satu baris. Alasan "supaya keren" atau "biar tidak kosong" berarti efek dibuang.
- Gerak mengikuti karakter visual. Tingkat gerak harus selaras dengan dial MOTION di `DESIGN.md` bila ada.
- Satu momen yang diingat per halaman cukup. Elemen lain bergerak tenang dan konsisten. Hindari semua elemen memakai fade-up yang sama.
- Library gerak hanya boleh dari `techstack.md`. Bila belum tercantum, tandai `[PERLU KONFIRMASI]`, tawarkan opsi dengan trade-off, dan tetap rancang versi CSS murni sebagai cadangan.

## 2. Tingkat gerak

Selaraskan dengan dial MOTION di `DESIGN.md` (1, 2, atau 3). Bila tidak ada `DESIGN.md`, tanyakan ke user.

| Tingkat | Karakter | Cakupan | Alat yang wajar |
|---|---|---|---|
| 1, minimal | tenang, cepat | hover, focus, transisi status, buka-tutup menu | CSS `transition` dan `@keyframes`, tanpa library |
| 2, seimbang | halus, terarah | transisi komponen, masuk-keluar elemen, scroll-reveal ringan, transisi halaman | CSS, ditambah Motion (stack React) atau GSAP dengan ScrollTrigger; Lenis opsional |
| 3, ekspresif | sinematik, bercerita | koreografi urutan, parallax, bagian yang ditahan (pin) atau digerakkan scroll (scrub), teks yang dipecah | GSAP dengan ScrollTrigger, Lenis bila perlu; Motion bila stack React dan alurnya sederhana |

## 3. Memilih library

| Alat | Cocok untuk | Catatan |
|---|---|---|
| CSS saja | hover, focus, transisi sederhana, `@keyframes` | paling ringan; mulai dari sini, naik hanya bila perlu |
| Motion (paket `motion`) | stack React (juga tersedia untuk JavaScript biasa dan Vue); animasi deklaratif, masuk-keluar komponen, animasi layout, gesture, spring | bila ukuran penting, pakai `LazyMotion` agar fitur berat dimuat saat dibutuhkan |
| GSAP | timeline kompleks, animasi berbasis scroll (ScrollTrigger), SVG, canvas atau WebGL, framework apa pun | di React pakai hook `useGSAP` agar pembersihan benar; impor hanya plugin yang dipakai |
| Lenis | smooth scroll untuk halaman konten atau pemasaran | tambahan, bukan library animasi; bila dipakai bersama ScrollTrigger, sinkronkan sesuai dokumentasi Lenis; hindari di aplikasi padat form atau dashboard |

Aturan pemilihan:
- Satu library utama per jenis pekerjaan. Jangan memakai GSAP dan Motion untuk hal yang sama.
- Lenis hanya bila tingkat gerak 2 atau 3 dan halaman bersifat konten atau pemasaran. Tulis alasannya.
- Sebelum menetapkan, periksa lisensi dan versi terbaru di dokumentasi resmi masing-masing library; keduanya dapat berubah. Catat versi yang dipilih di `FRONTEND_<project>.md`, bukan angka dari ingatan.
- Ukuran library bukan masalah utama. Yang lebih sering membuat berat adalah jumlah elemen beranimasi, properti yang dianimasikan, dan gambar yang tidak dioptimasi.

## 4. Aturan kinerja dan aksesibilitas (wajib)

- Animasikan hanya `transform` dan `opacity`. Hindari `width`, `height`, `top`, `left`, dan `box-shadow` karena memicu reflow.
- **Hormati `prefers-reduced-motion: reduce`.** Matikan parallax, scrub, smooth scroll, dan putar otomatis; ganti dengan fade singkat atau tanpa gerak. Setiap efek di spesifikasi punya satu baris fallback.
- Konten di atas lipatan (hero, elemen LCP) tidak boleh tersembunyi sambil menunggu JavaScript. Jangan mulai dari `opacity: 0` tanpa fallback; bila ragu, jangan animasikan elemen LCP.
- Muat library secara lazy untuk bagian di bawah lipatan atau halaman yang membutuhkannya. Impor modular.
- Batasi jumlah elemen yang bergerak bersamaan dalam satu viewport. Hindari animasi tanpa akhir yang menyala terus.
- Di perangkat sentuh dan kelas menengah ke bawah, sederhanakan: matikan smooth scroll kustom dan kurangi parallax.
- Fokus dan operasi keyboard tidak boleh bergantung pada gerak. Tidak ada kilatan lebih dari tiga kali per detik.
- Uji di HP kelas menengah dan ukur dengan Lighthouse. Catat sebagai tugas di `task.md`.

## 5. Format di `UIUX_<project>.md`

1. **Tingkat gerak dan alasan:** tingkat yang dipilih, sumbernya (dial MOTION atau jawaban user), dan alasan satu baris.
2. **Token gerak** (tabel dan CSS variables, nama sama dengan `motion` di `DESIGN.md` bila ada): durasi (cepat, dasar, lambat), easing (standar, masuk, keluar), jarak geser reveal, jeda antar elemen (stagger). Patokan awal: umpan balik UI 150 sampai 300 ms, reveal 400 sampai 700 ms; ubah bila arah desain menuntut.
3. **Tabel efek per halaman:**

```
| Halaman (P-xx) | Elemen | Pemicu (load/scroll/hover/klik) | Efek | Token | Library | Fallback reduced-motion | Fitur (F-xx) |
```

4. **Transisi antarhalaman** bila ada, dan alasannya.
5. **Kebijakan global:** smooth scroll dipakai atau tidak, di halaman mana, dan kapan dimatikan; batas jumlah elemen beranimasi.

## 6. Format di `FRONTEND_<project>.md`

Bagian "Animasi dan gerak" memuat: library dan versi terpilih beserta cara impor modular; lokasi file dan struktur folder untuk gerak; konstanta token gerak sebagai sumber tunggal (nama sama dengan UI/UX); komponen atau hook pembungkus untuk pola berulang (misalnya reveal saat masuk viewport); pola pembersihan (`useGSAP` atau `AnimatePresence` sesuai library); strategi lazy loading; satu utilitas terpusat untuk `prefers-reduced-motion`; anggaran kinerja dan cara mengujinya; contoh kode kunci sesuai techstack.

## 7. Pola yang dihindari

- Parallax tanpa tujuan, atau efek yang sama dipakai di semua section.
- Durasi UI di atas 400 ms untuk umpan balik, atau animasi memantul pada form dan tombol aksi.
- Smooth scroll di aplikasi yang dipakai untuk bekerja (dashboard, formulir panjang).
- Menyembunyikan konten penting sampai animasi selesai.
- Mengandalkan gerak sebagai satu-satunya penanda status.

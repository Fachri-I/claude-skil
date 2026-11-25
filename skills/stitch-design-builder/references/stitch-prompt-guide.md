# Panduan: 02-stitch-prompt-<peran>.md

Bahasa isi prompt: English. Catatan pembuka dan judul bagian: Indonesia. Teks UI di dalam prompt mengikuti bahasa produk.

Prinsip: Stitch lebih terkontrol bila konteks dan design system diberikan sekali di awal, layar diminta satu per satu, lalu diperhalus bertahap. Karena itu setiap file peran berisi satu Global Prompt, prompt per layar, dan refinement. Konsistensi antarfile dijaga dengan blok yang identik (placeholder).

## Pembagian per peran

1. Daftar peran dari plan (misalnya mahasiswa, penyelenggara, admin). Satu peran berarti satu file `02-stitch-prompt.md`.
2. **Layar publik atau bersama** (katalog, detail, login, daftar, verifikasi email, lupa dan reset kata sandi, halaman sistem) masuk ke file peran utama (pengguna akhir). File peran lain tidak mengulangnya; hanya memuat varian khusus (misalnya tab "penyelenggara" pada Daftar akun).
3. Layar yang hanya dipakai satu peran masuk ke file peran itu. Layar login terpisah (misalnya host admin) masuk ke file perannya.
4. Pertahankan nomor layar dari plan (P-01, P-02, ...) supaya mudah dilacak lintas dokumen. Perluasan di luar plan memakai nomor X-01, X-02.
5. Tiap file wajib berdiri sendiri: memuat Global Prompt yang identik, Prompt Pengingat, refinement umum, dan navigasi peran itu.
6. Tiap file menetapkan satu **layar jangkar** (layar tipikal paling kaya komponen untuk peran itu).

## Struktur file

```markdown
# Stitch Prompts: <Project> — <Peran>

> Cakupan (layar apa saja, apa yang ada di file lain). Cara pakai 5-6 langkah (Indonesia).

## Daftar kerja        <- satu baris per layar, semua [ ] bila direset
## 0. Persiapan        <- 0.1 Global Prompt ({{GLOBAL}}), 0.2 Design System Board, 0.3 layar jangkar
## P-01 <Layar>        <- P-01.1 Desktop, P-01.2 State, P-01.3 Dialog, P-01.4 Mobile 375px
...
## G Menunggu keputusan (jangan dikerjakan sebelum disetujui)
## B (opsional) Perluasan di luar plan, menunggu persetujuan
## R Refinement         <- R0 navigasi peran, lalu {{REFINE}}
## Prompt Pengingat     <- {{REMINDER}}
```

Setiap prompt memakai kotak `- [ ] **<id> <nama>**` diikuti blok kode. Item opsional atau yang membawa catatan user ditulis di judul item.

## Prompt layar (desktop), target kurang dari 250 kata

```
Screen: <nama> (<peran>). Purpose: <satu baris>.
Layout: <sidebar/header/kolom/grid, dengan lebar bila perlu>.
Sections, top to bottom:
1. <Bagian>: <komponen dan copy persis>
2. ...
{{DS}} {{GUARD}}
```

Aturan:
- Tulis copy nyata dari plan. Bila plan tidak punya, buat contoh masuk akal dan tandai `(sample copy)`. Tanggal contoh harus benar harinya (cek dengan `scripts/contrast.py --date`).
- Sebut item navigasi persis seperti di Global Prompt dan tandai item aktif.
- Pakai nama komponen yang sama dengan DESIGN.md.
- Kutip label status final (bukan enum), misalnya "Menunggu tinjauan".
- Hanya satu tombol primer per area; bila dua kondisi (misalnya tanpa seleksi dan dengan seleksi), buat varian terpisah.
- Auth: jelaskan panel merek sekali di Global Prompt; prompt layar cukup menyebut "same brand panel".

## Prompt patch (state, dialog, mobile)

Ditempel pada layar yang sudah ada, selalu diawali `Keep everything else unchanged.` dan diakhiri `{{GUARD}}`.

- **State**: "Add N small variant frames labeled ...", satu kalimat per varian.
- **Dialog**: `Screen: dialog on "<layar>" over the dimmed page. Title ..., sentence ..., buttons "Kembali" (left) and <aksi utama> (right).` Dialog destruktif memakai tombol danger.
- **Mobile**: `Create the 375px variant of <layar>: ...` sebut apa yang bertumpuk, tab bawah dengan item peran itu, tombol utama penuh lebar 44px.
- Prompt auth boleh digabung menjadi satu prompt mobile untuk semua layar auth yang berbagi tata letak.

## Bagian "Menunggu keputusan" dan "Perluasan"

- Item yang bergantung pada keputusan terbuka dipindah ke bagian G dengan label keputusan (misalnya D-21) dan teks akhir ditandai pending.
- Fitur dari desain lama yang tidak ada di plan (laporan, pengaturan, aksi massal) tidak dibuang diam-diam: bila masuk akal, ubah ke design system bersama, taruh di Bagian B, beri navigasi tambahan sebagai prompt patch tersendiri (X-00), dan jelaskan di audit apa yang dibuang dan mengapa.

## Refinement

`{{REFINE}}` berisi set umum yang identik di semua file (ganti nilai dengan token proyek):
R1 palet, R2 warna status, R3 tipografi, R4 bentuk dan tinggi kontrol, R5 ikon dan aset, R6 satu tombol primer per area, R7 tombol nonaktif, R8 teks subtle, R9 hapus konten tambahan, R10 label kuota/data dan zona waktu, R11 cincin fokus, R12 varian mobile. Tambahkan di tiap file R0 (navigasi peran) dan perbaikan khusus peran. Tiap refinement hanya mengubah satu aspek.

## Kesalahan yang dihindari

- Hex berbeda antara prompt, Global Prompt, dan DESIGN.md.
- Mengetik ulang blok identik secara manual (gunakan placeholder dan build).
- Prompt hanya berisi kata suasana tanpa angka.
- Menggabungkan beberapa layar dalam satu prompt.
- Menjanjikan hal yang sulit dihasilkan Stitch (animasi kompleks, ilustrasi custom); pindahkan ke "Catatan Realisasi di Stitch" pada audit.
- Membawa klaim, statistik, atau contoh kredensial dari desain lama.
- Melewatkan varian mobile untuk layar yang tidak disebut plan lama.

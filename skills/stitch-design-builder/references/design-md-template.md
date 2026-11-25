# Template: DESIGN.md (format resmi Stitch, versi alpha)

Bahasa: English untuk isi berkas, penjelasan di sini Indonesia. **Satu DESIGN.md untuk seluruh peran dan seluruh layar.** Dokumen ini adalah design system tertulis yang dibaca manusia, Stitch, dan tool coding. Nilainya diambil dari bagian Design Tokens dan Komponen & State pada audit; jangan menambah nilai baru di sini.

Format mengikuti spesifikasi DESIGN.md dari Google Stitch (repositori `google-labs-code/design.md`, versi `alpha`): front matter YAML berisi token mesin (nilai normatif), lalu bagian markdown berisi alasan dan panduan penerapan. Spesifikasi masih berkembang; bila bisa diakses, periksa versi terbarunya dan ikuti bila berbeda dari ringkasan ini.

## Kerangka

````markdown
---
version: alpha
name: <Project Name>
description: <one or two sentences: product, roles, one design system for all roles>
colors:
  primary: '#...'
  primary-hover: '#...'
  primary-soft: '#...'
  on-primary: '#FFFFFF'
  canvas: '#...'
  surface: '#...'
  border: '#...'
  text: '#...'
  text-muted: '#...'
  # status, kategori, dst: satu kunci per baris, nama bebas (success-ink, success-bg, danger, cat-<kategori>-ink ...)
typography:
  display:
    fontFamily: <Font>
    fontSize: 36px
    fontWeight: 800
    lineHeight: 44px
    letterSpacing: -0.02em
  body:
    fontFamily: <Font>
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px
  # h1 ... micro dengan pola yang sama; override mobile di grup sm (lihat aturan)
rounded:
  sm: 4px
  md: 8px
  lg: 12px
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  content-max: 1200px
  page-margin-mobile: 16px
motion:
  state-change:
    duration: 150ms
    delay: 0ms
    timingFunction: ease-out
components:
  button-primary:
    backgroundColor: '{colors.primary}'
    textColor: '{colors.on-primary}'
    rounded: '{rounded.md}'
    height: 44px
  button-primary-hover:
    backgroundColor: '{colors.primary-hover}'
  badge-success:
    backgroundColor: '{colors.success-bg}'
    textColor: '{colors.success-ink}'
    typography: '{typography.label}'
    rounded: '{rounded.full}'
---

# DESIGN.md: <Project Name>

## Overview
## Colors
## Typography
## Layout
## Elevation & Depth
## Shapes
## Motion & Micro-interaction
## Voice & Content Strategy
## Components
<bagian tambahan di luar baku: Iconography & Imagery, Accessibility, dan sejenisnya>
## Do's and Don'ts
````

## Isi tiap bagian

Tulis prosa yang menjelaskan **mengapa** dan **di mana** token dipakai, merujuk nama token. Bagian yang tidak relevan boleh dihilangkan, tetapi yang ada harus berurutan seperti di atas.

- **Overview** (alias Brand & Style): tujuan produk, semua peran, kepribadian visual dalam hal konkret, 4-5 prinsip.
- **Colors**: tabel `Token | Hex | Role | Usage notes`; aturan warna mana boleh bersama, satu tombol primer per area, status selalu dengan teks, warna nonaktif, warna grafik, tanpa hue baru. Palet `primary` wajib ada.
- **Typography**: font (Google Fonts) dan fallback; tabel `Style | Size | Weight | Line height | Letter spacing | Use`; kapan monospace dipakai.
- **Layout** (alias Layout & Spacing): unit dasar dan skala, lebar maksimum, margin, breakpoint dan lebar rancangan, navigasi per breakpoint (sidebar, rail, tab bawah, tinggi header), **item sidebar per peran**, header publik, tata letak auth dan panel merek.
- **Elevation & Depth**: tingkat shadow dengan CSS persis, aturan border; bila desain datar, jelaskan cara lain membangun hierarki (border, kontras warna). Tanpa glow kecuali sumber menyebut.
- **Shapes**: radius per komponen; catatan Tailwind bila nama radius berbeda dari bawaan.
- **Motion & Micro-interaction** (alias Motion): apa yang bergerak, durasi, easing, aturan `prefers-reduced-motion`. Tulis "minimal" bila sumber tidak menyebut apa pun.
- **Voice & Content Strategy**: bahasa antarmuka, format angka, uang, tanggal dan zona waktu, tata bahasa label tombol, istilah baku, isi empty/loading/error state, dan **peta label status** (enum ke label terlihat dan keluarga warna). Prosa saja, tanpa token. Isi hanya dari sumber atau audit.
- **Components**: satu butir per komponen dengan resep kelas Tailwind, varian, ukuran, state: Button, Input, Select/Textarea, Checkbox/Toggle, kartu konten utama, Badge, Alert, Filter tab, Segmented control, Responsive table, Dialog, Stepper, Progress/Quota, Dropzone, Toast, App navigation, Empty/Skeleton, plus komponen khas produk. Tandai komponen yang hanya milik perluasan di luar plan.
- **Bagian tambahan** (bagian di luar nama baku dipertahankan oleh Stitch dan tidak menjadi galat), diletakkan setelah Components dan sebelum Do's and Don'ts:
  - **Iconography & Imagery** (kunci aset): set ikon, stroke, ukuran, larangan; spesifikasi logo; kebijakan poster/gambar; avatar; elemen khusus (QR dan sejenisnya); tanpa gambar remote di prototipe.
  - **Accessibility**: target kontras dengan pasangan terverifikasi dan pasangan lulus terendah; cincin fokus; target 44px; urutan heading; skip link; alternatif grafik; zona waktu. Daftar **open issue** (misalnya warna border yang gagal 3:1 non-teks) dengan saran perbaikan, tetapi nilai sumber dipertahankan sampai user setuju.
- **Do's and Don'ts**: enam sampai delapan pasangan konkret.

## Aturan token (diperiksa `scripts/lint_design.py`)

- `version: alpha`. Keterangan seperti "satu design system untuk semua peran" ditaruh di `description`, bukan di `version`.
- `colors`: nilai hex `#RRGGBB` dalam tanda kutip; minimal ada `primary`. Nama token bebas dan langsung bisa menjadi kunci `tailwind.config` (`primary`, `primary-hover`, `surface`, `text-muted`).
- `typography`: setiap token adalah **objek** berisi `fontFamily`, `fontSize`, `fontWeight`, `lineHeight`, `letterSpacing` (opsional). Nama properti harus persis itu, bukan `size` atau `weight`. `fontFamily` diulang di tiap token; jangan menaruhnya sebagai teks tunggal di level `typography`. Satuan dimensi hanya `px`, `em`, `rem`. `lineHeight` boleh dimensi atau angka tanpa satuan. Override mobile ditaruh di grup `sm` (`typography.sm.h1`), yang hanya memuat token yang berubah.
- `rounded` dan `spacing`: map nama ke dimensi. **Dilarang array** (`scale: [4, 8, 12]`); ubah menjadi `xs: 4px`, `sm: 8px`, dan seterusnya. Jangan memakai nama skala (`sm`, `md`, `lg`) sekaligus sebagai nama grup breakpoint di `spacing`; margin per breakpoint ditulis `page-margin-mobile`, `page-margin-tablet`, `page-margin-desktop`.
- `motion`: nama sesuai tujuan (`state-change`, `surface-enter`), tiap token punya `duration`, `delay` (akhiran `ms`) dan `timingFunction`.
- `components`: token per komponen dengan properti `backgroundColor`, `textColor`, `typography`, `rounded`, `padding`, `size`, `height`, `width`. Nilai boleh literal atau rujukan `{colors.primary}`, `{rounded.md}`, `{typography.label}`. Varian ditulis sebagai kunci terpisah (`button-primary`, `button-primary-hover`). Hanya tulis properti yang ada di sumber; jangan mengarang. Pasangan `backgroundColor` dan `textColor` pada satu komponen harus berkontras minimal 4,5:1. Komponen nonaktif (disabled) cukup dijelaskan di prosa bila pasangannya sengaja di bawah 4,5:1.
- Setiap rujukan `{path}` harus menunjuk token yang ada. Rujukan ke token komposit (typography, motion, komponen) hanya boleh di dalam `components`.
- Setiap kunci YAML tingkat atas hanya sekali. Tidak ada judul bagian ganda.
- Judul bagian memakai `##` dan **nama baku tanpa nomor**: Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Motion & Micro-interaction, Voice & Content Strategy, Components, Do's and Don'ts (alias yang diterima: Brand & Style, Layout & Spacing, Elevation, Motion). "Shape & Elevation" dipisah menjadi dua bagian.
- Dua gaya penulisan token diperbolehkan (front matter, atau blok ```yaml di dalam bagian terkait), tetapi satu kunci tingkat atas tidak boleh didefinisikan di dua tempat. Skill ini memakai front matter.

## Bila sudah ada DESIGN.md di input

- Bila inputnya sudah berformat resmi (misalnya dari skill Design Direction), **pertahankan semuanya**: baris `Dial:`, Design Read, motif identitas, aksen, alasan satu baris per keputusan, bagian tambahan, dan urutan. Lengkapi hanya bagian yang kosong (token `components` dan `motion`, Voice & Content Strategy). Jangan menimpa nilai dan jangan menambah perintah untuk agen di dalam berkas; DESIGN.md hanya memuat data desain.
- Bila formatnya lama (properti `size`/`weight`, array `scale`, judul bernomor), konversi ke format resmi tanpa mengubah satu pun nilai hex atau angka, dan catat konversinya di audit.

## Aturan umum

- Semua nilai konkret (hex, px). Hindari kata samar tanpa angka.
- Setiap hex di DESIGN.md harus muncul di Global Prompt dan sebaliknya (diperiksa `scripts/check.py`). Hex hanya `#RRGGBB`.
- Panjang target 200-330 baris termasuk front matter. Padat lebih berguna daripada panjang dan generik.
- Satu file untuk semua peran: beda peran hanya tampil di navigasi (Layout) dan di komponen khusus (Components).
- Setelah menulis, jalankan `python scripts/lint_design.py <out_dir>/DESIGN.md` sampai `OK`. Bila linter resmi Stitch tersedia di lingkungan, jalankan juga.
- Bila Stitch tetap menolak front matter, hapus front matter lalu pindahkan token penting ke prosa; front matter bersifat opsional menurut spesifikasi.

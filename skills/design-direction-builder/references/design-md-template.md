# Template: DESIGN.md (format resmi Stitch, versi alpha, plus data arah)

Bahasa: English untuk isi berkas, penjelasan di sini Indonesia. Satu `DESIGN.md` untuk arah terpilih. Dokumen ini adalah design system tertulis yang dibaca manusia, Stitch, dan agen coding. Nilai hanya dari arah terpilih dan masukan user; jangan menambah nilai baru.

Format mengikuti spesifikasi DESIGN.md dari Google Stitch (repositori `google-labs-code/design.md`, versi `alpha`): front matter YAML berisi token mesin (nilai normatif), lalu bagian markdown berisi alasan dan panduan penerapan. Spesifikasi masih berkembang; bila bisa diakses, ikuti versi terbarunya bila berbeda dari ringkasan ini.

## Kerangka

````markdown
---
version: alpha
name: <Project Name>
description: <one or two sentences: product, audience, the chosen direction in a phrase>
colors:
  primary: '#...'
  on-primary: '#FFFFFF'
  canvas: '#...'
  surface: '#...'
  border: '#...'
  text: '#...'
  text-muted: '#...'
  accent: '#...'
typography:
  display:
    fontFamily: <Font>
    fontSize: 48px
    fontWeight: 700
    lineHeight: 52px
    letterSpacing: -0.02em
  body:
    fontFamily: <Font>
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
rounded:
  sm: 4px
  md: 8px
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  content-max: 1200px
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
    backgroundColor: '{colors.accent}'
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
<bagian tambahan di luar baku bila perlu: Iconography & Imagery, Accessibility>
## Do's and Don'ts
````

## Data arah di dalam DESIGN.md

Taruh di **Overview** (antislop membaca arah dari berkas ini dan mengenali baris `Dial:`):

```
Design Read: Reading this as: <page type> for <audience>, <visual language>, dial <ENERGY/RHYTHM/MOTION>.
Dial: ENERGY 2 / RHYTHM 3 / MOTION 1
Identity motif: <one specific, repeated visual idea>. Why: <one line>.
Accent: <hex and where it is used>. Why: <one line>.
```

Setiap bagian lain diakhiri baris `Why:` untuk keputusan utamanya (palet, tipografi, tata letak, kedalaman, ikon atau ilustrasi, gerak). Jangan memasukkan instruksi untuk agen; DESIGN.md hanya memuat data desain. Pilihan user (tiga kata sifat, anti-referensi) menjadi personality di Overview dan daftar Don't di Do's and Don'ts.

## Isi tiap bagian

Prosa menjelaskan **mengapa** dan **di mana** token dipakai, merujuk nama token. Bagian yang tidak relevan boleh dihilangkan, tetapi yang ada harus berurutan seperti kerangka.

- **Overview** (alias Brand & Style): tujuan, audiens, personality dalam hal konkret, Design Read, Dial, motif identitas, aksen, 4-5 prinsip.
- **Colors**: tabel `Token | Hex | Role | Usage notes`; 2-3 warna inti + 1 aksen; aturan pasangan warna; pasangan kontras terukur. Palet `primary` wajib ada.
- **Typography**: font (Google Fonts) dan fallback; tabel `Style | Size | Weight | Line height | Letter spacing | Use`.
- **Layout** (alias Layout & Spacing): unit dasar, skala, lebar maksimum, margin, breakpoint, arketipe tata letak dan di mana ia sengaja keluar dari grid.
- **Elevation & Depth**: cara membangun hierarki (lapisan tonal, border, bayangan dengan CSS persis bila dipakai).
- **Shapes**: radius per komponen.
- **Motion & Micro-interaction**: apa yang bergerak, durasi, easing, `prefers-reduced-motion`; tulis "minimal" bila arah menuntutnya.
- **Voice & Content Strategy**: nada, kapitalisasi, istilah baku, tata bahasa label tombol (verba yang menamai hasil, bukan "OK" atau "Submit"), empty, loading, dan error state, format angka dan tanggal. Prosa saja. Isi dari PRD dan masukan user.
- **Components**: butir per komponen dengan resep kelas Tailwind (bila techstack memakai Tailwind), varian, state.
- **Bagian tambahan**: Iconography & Imagery (set ikon, logo, kebijakan gambar), Accessibility (kontras terukur dan pasangan lulus terendah, fokus, target 44px). Bagian di luar nama baku dipertahankan oleh Stitch; letakkan setelah Components dan sebelum Do's and Don'ts.
- **Do's and Don'ts**: enam sampai delapan pasangan konkret, termasuk turunan dari anti-referensi user.

## Aturan token (diperiksa `scripts/lint_design.py`)

- `version: alpha`; keterangan ditaruh di `description`.
- `colors`: hex `#RRGGBB` dalam tanda kutip; minimal ada `primary`; nama token bebas dan langsung bisa menjadi kunci `tailwind.config`.
- `typography`: setiap token adalah **objek** berisi `fontFamily`, `fontSize`, `fontWeight`, `lineHeight`, `letterSpacing` (opsional). Bukan `size` atau `weight`. `fontFamily` diulang di tiap token, tidak sebagai teks tunggal di level `typography`. Satuan dimensi hanya `px`, `em`, `rem`. Override mobile di grup `sm` (`typography.sm.h1`).
- `rounded` dan `spacing`: map nama ke dimensi. **Dilarang array.** Jangan memakai nama skala (`sm`, `md`, `lg`) sekaligus sebagai nama grup breakpoint di `spacing`.
- `motion`: nama sesuai tujuan; tiap token punya `duration`, `delay` (akhiran `ms`), `timingFunction`.
- `components`: properti `backgroundColor`, `textColor`, `typography`, `rounded`, `padding`, `size`, `height`, `width`; nilai literal atau rujukan `{colors.primary}`. Varian sebagai kunci terpisah (`button-primary-hover`). Tulis hanya properti yang ada di arah terpilih. Pasangan teks dan latar harus berkontras minimal 4,5:1.
- Setiap rujukan `{path}` menunjuk token yang ada. Rujukan ke token komposit hanya boleh di dalam `components`.
- Setiap kunci YAML tingkat atas hanya sekali; tidak ada judul bagian ganda.
- Judul bagian memakai `##` dan **nama baku tanpa nomor**: Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Motion & Micro-interaction, Voice & Content Strategy, Components, Do's and Don'ts (alias yang diterima: Brand & Style, Layout & Spacing, Elevation, Motion).

## Bila sudah ada DESIGN.md di input

- Bila sudah berformat resmi dan berarah jelas, **pertahankan semuanya** (dial, motif, aksen, alasan, bagian tambahan, urutan). Lengkapi hanya yang kosong (`components`, `motion`, Voice & Content Strategy). Jangan menimpa nilai.
- Bila formatnya lama (properti `size` atau `weight`, array `scale`, judul bernomor), konversi ke format resmi tanpa mengubah nilai hex atau angka, dan catat konversinya di `design-direction.md`.

## Pemeriksaan

Setelah menulis, jalankan `python scripts/lint_design.py DESIGN.md` sampai `OK`. Bila linter resmi Stitch tersedia di lingkungan, jalankan juga. Bila Stitch menolak front matter, hapus front matter dan pindahkan token penting ke prosa; front matter bersifat opsional menurut spesifikasi.

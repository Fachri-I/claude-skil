# Panduan: html/<halaman>.html (statis, Tailwind)

Satu file HTML per layar di inventaris audit. Tujuannya pratinjau statis yang setia pada design system, berguna sebagai pembanding hasil Stitch dan titik awal implementasi.

## Aturan teknis

- Satu file mandiri per halaman, dapat dibuka langsung di browser.
- Tailwind lewat CDN: `<script src="https://cdn.tailwindcss.com"></script>`. CDN ini untuk prototipe; jelaskan di komentar bahwa produksi memakai build Tailwind.
- Pasang font lewat satu `<link>` Google Fonts, dengan fallback `sans-serif`/`serif` pada config.
- Semua token dari DESIGN.md masuk ke `tailwind.config` di dalam `<script>` sebelum konten. Jangan menulis hex langsung di class (`bg-[#2563EB]`); pakai token (`bg-primary`).
- HTML semantik: `header`, `nav`, `main`, `section`, `footer`, satu `h1` per halaman, urutan heading benar.
- Responsif mobile-first dengan prefix `sm: md: lg:`. Sesuaikan breakpoint dengan audit.
- Tanpa framework JS. Vanilla JS hanya bila perlu (toggle menu mobile, tab sederhana), taruh di akhir `body`.
- Tanpa gambar remote. Placeholder: blok berwarna token `surface`, gradien, atau SVG inline. Beri `aria-label` atau teks alternatif.
- Aksesibilitas: `lang` pada `html`, label untuk input, `focus-visible:ring`, target sentuh minimal 44px, kontras sesuai audit.
- Tautan navigasi antarhalaman memakai nama file relatif (`index.html`, `pricing.html`), memakai slug dari inventaris audit.
- Perilaku dinamis (data, auth, form submit) tidak diimplementasikan; tampilkan state statis yang disebut plan (misalnya satu contoh error).

## Kerangka dasar

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title><Page> | <Project></title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link href="https://fonts.googleapis.com/css2?family=<Font>:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: { primary: { DEFAULT: '#...', 700: '#...' }, surface: '#...', 'text-muted': '#...' },
          fontFamily: { heading: ['<Heading Font>', 'sans-serif'], body: ['<Body Font>', 'sans-serif'] },
          borderRadius: { card: '12px' },
          boxShadow: { soft: '0 4px 16px rgba(0,0,0,0.08)' }
        }
      }
    }
  </script>
</head>
<body class="bg-background font-body text-text">
  <!-- header / main / footer -->
</body>
</html>
```

`tailwind.config` harus identik di semua halaman. Susun sekali, salin ke setiap file.

## Isi halaman

- Ikuti urutan bagian dari prompt layar yang sesuai, atas ke bawah.
- Pakai copy dari plan. Bila tidak ada, pakai contoh realistis yang sama dengan `(sample copy)` di prompt.
- Komponen berulang (kartu, tombol) memakai class recipe yang tertulis di DESIGN.md bagian Components supaya konsisten.

## Cek akhir per file

1. Dibuka di browser tanpa error konsol.
2. Tidak ada hex literal di class.
3. Satu `h1`, heading berurutan.
4. Tampilan mobile (sekitar 390px) dan desktop sama-sama rapi, tanpa scroll horizontal.
5. Semua tautan antarhalaman menunjuk ke file yang ada.

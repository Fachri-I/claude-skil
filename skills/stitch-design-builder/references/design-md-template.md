# Template: DESIGN.md

Bahasa: English. **Satu DESIGN.md untuk seluruh peran dan seluruh layar.** Dokumen ini adalah design system tertulis yang dibaca manusia, Stitch, dan tool coding. Isi seluruhnya diambil dari bagian Design Tokens pada audit; jangan menambah nilai baru di sini.

Struktur: front matter YAML (token mesin, gaya DESIGN.md hasil Stitch) diikuti 10 bagian. Bila user menyebut skema resmi dari Stitch atau timnya, ikuti skema itu dan petakan token audit ke dalamnya.

````markdown
---
name: <Project Name>
version: <n> (one design system for <roles>)
colors:
  primary: '#...'
  primary-hover: '#...'
  primary-soft: '#...'
  primary-ink: '#...'
  on-primary: '#FFFFFF'
  canvas: '#...'
  surface: '#...'
  border: '#...'
  border-strong: '#...'
  text: '#...'
  text-muted: '#...'
  text-subtle: '#...'
  success-ink: ...   success-bg: ...   success-border: ...   # one key per line in the real file
  warning-*, danger, danger-hover, danger-bg, danger-border, info-*, cat-<kategori>-ink/bg/from/to
typography:
  fontFamily: <Font>
  display: {size: 36px, weight: '800', lineHeight: 44px, letterSpacing: -0.02em}
  h1 ... micro
rounded: {sm: 4px, md: 8px, lg: 12px, xl: 16px, full: 9999px}
spacing: {unit: 4px, scale: [4, 8, 12, 16, 24, 32, 48]}
---

# DESIGN.md: <Project Name>

## 1. Overview
Purpose, audiences (all roles), visual personality in concrete terms; 4-5 principles.

## 2. Color
| Token | Hex | Role | Usage notes |
Rules: which colors may appear together, one primary button per area, status always paired with text, disabled colors, chart colors (second series dashed), no new hues.

## 3. Typography
Font (Google Fonts) and fallback; table: Style | Size | Weight | Line height | Letter spacing | Use. Number and time format rules.

## 4. Layout & Spacing
Base unit and scale; max width and margins; breakpoints and design widths; navigation by breakpoint (sidebar, rail, bottom bar, header height); **sidebar items per role**; public header; auth split layout and brand panel.

## 5. Shape & Elevation
Radius per component; Tailwind note if radius names differ from defaults (override `lg`, `xl`); shadow levels with exact CSS; border rules; no glows.

## 6. Components
One bullet per component with a Tailwind class recipe, variants, sizes, states: Button, Input, Select/Textarea, Checkbox/Toggle, main content card, Badge, Alert, Filter tab, Segmented control, Responsive table, Dialog, Stepper, Progress/Quota, Dropzone, Toast, App navigation, Empty/Skeleton, plus product-specific ones. Include **status label maps** (enum to visible label and color family). Mark components that belong only to out-of-plan extensions.

## 7. Iconography & Imagery  (assets lock)
Icon set, stroke, sizes, bans; logo spec; poster/image policy; avatars; special elements (QR etc.); no remote images in prototypes.

## 8. Motion
Durations, easing, which elements animate. "Minimal" if the source says nothing; reduced-motion rule.

## 9. Accessibility
Contrast targets with the verified pairs and the lowest passing one; focus ring; 44px targets; heading order; skip link; chart alternatives; time zones. List **open issues** (for example a border color that fails non-text 3:1) with the proposed fix, keeping the source value until the user agrees.

## 10. Do and Don't
Six to eight concrete pairs.
````

## Aturan

- Token memakai nama yang langsung bisa menjadi kunci `tailwind.config` (`primary`, `primary-hover`, `surface`, `text-muted`).
- Semua nilai konkret (hex, px). Hindari kata samar tanpa angka.
- Setiap hex di DESIGN.md harus muncul di Global Prompt dan sebaliknya (diperiksa `scripts/check.py`).
- Front matter harus YAML valid; di file nyata tulis satu kunci per baris.
- Panjang target 150-250 baris termasuk front matter. Padat lebih berguna daripada panjang dan generik.
- Satu file untuk semua peran: beda peran hanya tampil di navigasi (bagian 4) dan di komponen khusus (bagian 6).

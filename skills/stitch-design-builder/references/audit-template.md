# Template: 01-design-audit.md

Bahasa: Indonesia (istilah teknis seperti token, grid, breakpoint boleh tetap English).
Tujuan: satu dokumen yang menjadi sumber kebenaran untuk semua output lain. Bagian 9 (temuan) adalah tempat semua konflik dan keputusan dicatat.

Gunakan struktur persis di bawah ini.

```markdown
# Design Audit & Technical Breakdown: <Nama Proyek>

## 1. Ringkasan Input
- Jenis input: design plan .md / prompt dan DESIGN.md lama / gambar referensi / kombinasi
- Tabel peran file: | File | Isi | Peran dalam paket ini | (sumber utama, pembanding, bahan perluasan)
- Platform: Web desktop / Mobile / Responsif (alasan singkat) dan lebar rancangan
- Tujuan produk satu kalimat; pengguna utama (daftar peran)
- Permintaan khusus putaran ini (misalnya prompt dianggap belum dikerjakan, dipisah per peran, satu DESIGN.md)

## 2. Asumsi
Tabel: | Hal | Asumsi yang diambil | Alasan | Perlu konfirmasi? |
Wajib memuat: sumber token yang dipilih, keputusan atas konflik antarfile, aset yang tidak ada di sumber (logo, panel merek, avatar), label turunan, penempatan layar bersama, tanggal contoh, apakah HTML dibuat.

## 3. Inventaris Layar
Tabel: | # | Nama layar | Slug (untuk HTML) | Tujuan | Komponen utama | File peran | Sumber |
Nomor tetap dari plan (P-01, ...); perluasan memakai X-01. Nomor ini dipakai ulang di prompt dan nama file HTML.

## 4. Design Tokens
Warna: | Token | Hex | Peran | Kontras terhitung | (hasil `scripts/contrast.py`, bukan tebakan)
Tipografi, spacing, radius, shadow: ringkas, rujuk DESIGN.md sebagai satu sumber.

## 5. Layout & Grid
Lebar maksimum, margin, breakpoint, navigasi per breakpoint, auth, perilaku tabel dan kartu.

## 6. Komponen & State
Tabel: | Komponen | Varian | State | Dipakai di layar |

## 7. Interaksi & Motion
Transisi, navigasi antarlayar. Tulis "tidak disebut" bila tidak ada; jangan mengarang.

## 8. Aksesibilitas
Hasil cek kontras (pasangan terendah disebut), target sentuh, fokus, heading, status tidak mengandalkan warna.

## 9. Temuan: Gap, Konflik, Risiko
Daftar bernomor: masalah, lokasi, dampak, saran dan keputusan yang diambil (nilai asli dipertahankan sampai user setuju bila menyangkut desain sumber).
Kategori yang selalu diperiksa:
- Konflik token antarfile (warna, ikon, radius) dan keputusan pemenang.
- Konflik navigasi atau jumlah menu antarperan.
- Taksonomi atau label berbeda antarfile (kategori, status); pilih satu dan catat.
- Fitur di desain lama yang bertentangan dengan plan (aksi massal, kolom yang masih keputusan terbuka); apa yang dibuang atau dipindah ke Bagian B.
- Klaim, statistik, detail infrastruktur vendor, atau contoh kredensial di desain lama yang dibuang.
- Kontras: pasangan yang gagal atau tipis; batas input (non-teks 3:1).
- Tanggal contoh yang salah hari.
- Layar atau varian mobile yang tidak ada di plan lama dan ditambahkan.
- Item yang menunggu keputusan (ditahan) dan catatan tangan user yang dipertahankan.

## 10. Catatan Realisasi di Stitch
Hal yang mungkin sulit bagi Stitch (set ikon bawaan, grafik dua garis, drag handle, QR, banyak frame varian dalam satu prompt) dan cara menyiasatinya (refinement, memecah prompt, aset manual). Sebut bahwa front matter YAML DESIGN.md boleh dihapus bila Stitch menolak.
```

## Cara mengisi dari sumber berbeda

**Dari file .md:** ekstrak apa adanya. Warna bernama dikonversi ke hex dan dicatat di Asumsi.

**Dari prompt dan DESIGN.md lama:** ambil token dari versi terbaru, salin copy UI persis, gabungkan patch (perbaikan, state, dialog, mobile) ke dalam prompt layar yang lengkap, dan petakan item lama ke nomor layar.

**Dari gambar:** perkirakan hex dari area warna dominan, tandai `(estimated)`. Identifikasi font; bila tidak yakin, sebut kandidat Google Fonts terdekat sebagai asumsi.

**Dari keduanya:** teks plan menang untuk keputusan eksplisit, gambar menang untuk gaya visual; catat pertentangannya.

## Menghitung kontras dan tanggal

Jalankan `python scripts/contrast.py '#FFFFFF' '#2563EB' '#64748B' '#FFFFFF' --date 2026-12-12`. Pasangan diberikan berurutan (latar depan, latar belakang). Hasilnya rasio WCAG dan nama hari.

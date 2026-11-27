---
name: architecture-diagram-builder
description: Menyiapkan data dan prompt untuk skill Archify agar arsitektur website atau app (dari PRD, techstack.md, database.md, dan rancangan kerja) bisa dibaca manusia sebagai diagram interaktif, lalu menjalankan Archify bila tersedia. Hasil berupa file ARCHITECTURE_nama-proyek.md (spesifikasi yang bersumber jelas), prompt Archify siap pakai, dan file HTML diagram. Gunakan skill ini setiap kali user ingin diagram arsitektur, peta sistem, alur data, sequence diagram, alur proses, lifecycle status, atau ingin "menggambarkan arsitektur proyek ini" untuk presentasi, dokumentasi, dosen, klien, atau tim, atau menyebut Archify, walaupun user tidak menyebut kata "skill". Diagram ini HANYA untuk dibaca manusia; agen coding tidak memakainya, acuan agen tetap task.md. Skill ini melanjutkan hasil PRD Builder, techstack-recommender, skill database, dan design-plan-builder.
---

# Architecture Diagram Builder

Skill ini mengubah dokumen perancangan yang sudah ada menjadi diagram arsitektur yang mudah dibaca manusia, dengan **Archify** sebagai satu-satunya alat penggambar. Skill ini tidak menggambar sendiri dan tidak memakai alat diagram lain.

Tujuannya hanya satu: **pembaca manusia** (user, dosen, klien, anggota tim) cepat paham bagaimana website atau app tersusun. Agen coding tidak membutuhkan diagram ini karena sudah punya `task.md`. Karena itu:
- Jangan menambahkan diagram atau `ARCHITECTURE_<project>.md` sebagai acuan wajib di `AGENTS.md` atau `task.md`.
- Jangan mengubah file perancangan lain. Skill ini hanya membaca.

## Aturan umum

- **Bahasa:** ikuti bahasa user (default Bahasa Indonesia). Nama kode, route, tabel, dan field tetap dalam bahasa Inggris.
- **Jangan mengarang.** Setiap komponen dan garis di diagram harus punya sumber di dokumen (atau di kode yang user serahkan). Tanpa sumber, tandai `[PERLU KONFIRMASI]` dan tanyakan, jangan digambar.
- **Satu istilah, satu nama.** Pakai nama dari glosarium Shared Contract bila ada.
- **Tanya seperlunya:** maksimal 3 pertanyaan terkait per giliran. Jika keyakinan tinggi, putuskan sendiri dan sebutkan asumsinya, jangan menanyakan hal sepele.

## Alur kerja

### Fase 0: Pengecekan input

Minta user menyerahkan file, lalu periksa:

| File | Status | Dipakai untuk |
|---|---|---|
| `PRD_<project>.md` | Wajib | peran pengguna, fitur, alur utama |
| `techstack.md` | Wajib | frontend, backend, database, hosting, layanan pihak ketiga |
| `database.md` atau skema tabel | Wajib untuk diagram data flow dan lifecycle | tabel, relasi, kolom status |
| `BACKEND_<project>.md` / `DESIGN_PLAN_<project>.md` | Disarankan | modul backend, endpoint, auth, kontrak API |
| `security.md` | Opsional | batas kepercayaan, peran, lapisan keamanan |

Aturan:
- Jika PRD atau techstack belum ada, hentikan dan sarankan membuatnya dengan skill PRD Builder dan techstack-recommender.
- Proyek yang sudah berjalan tanpa dokumen perancangan: boleh membaca README, struktur folder, atau file kode yang user serahkan. Tandai sumbernya `dari kode`.
- Laporkan singkat apa yang cukup, apa yang kurang, dan diagram mana yang belum bisa dibuat karenanya.

### Fase 1: Pilih diagram

Tanyakan (gabungkan dalam satu giliran):
1. **Jenis diagram.** Default: **arsitektur** + **lifecycle status**. Pilihan lain: data flow, sequence, workflow.
2. **Siapa pembacanya**, karena menentukan tingkat detail: awam (hanya blok besar, tanpa istilah teknis), dosen/klien (blok + teknologi), atau tim developer (lengkap dengan protokol dan modul).
3. Jika memilih sequence: **skenario kunci** apa (misalnya checkout atau pencairan dana).

Data yang dibutuhkan tiap jenis dan cara menyusunnya ada di `references/archify-prompts.md`.

### Fase 2: Spesifikasi `ARCHITECTURE_<project>.md`

Susun satu file `.md` berisi, per diagram:

1. **Tujuan dan pembaca** (satu kalimat).
2. **Komponen:** tabel `ID | Nama | Peran (satu kalimat) | Teknologi | Lapisan | Sumber`. Lapisan umum: Klien, Backend, Data, Layanan eksternal.
3. **Koneksi:** tabel `Dari | Ke | Label | Data/protokol | Sumber`.
4. Khusus lifecycle: tabel status dan transisi `Dari | Ke | Pemicu | Aktor | Sumber`.
5. Khusus sequence dan workflow: langkah berurutan dengan aktor.
6. **Catatan** dan daftar `[PERLU KONFIRMASI]`.

Kolom Sumber berisi nama file dan bagian, misalnya `techstack.md > Backend`.

**Batas keterbacaan:** diagram arsitektur maksimal sekitar 12 sampai 15 komponen. Jika lebih, kelompokkan komponen sejenis (misalnya "Modul Auth, Order, Pembayaran" menjadi satu blok per lapisan) atau pecah menjadi beberapa diagram. Diagram yang padat justru melanggar tujuan skill ini.

Minta persetujuan user atas spesifikasi sebelum lanjut, karena Fase 3 bergantung padanya.

### Fase 3: Archify

1. Periksa apakah skill Archify tersedia di lingkungan ini (cari folder `archify` di `/mnt/skills/`).
2. **Jika tersedia:** baca `SKILL.md`-nya, lalu buat diagram sesuai instruksinya dengan memakai spesifikasi dari Fase 2 sebagai satu-satunya isi. Simpan HTML hasilnya.
3. **Jika tidak tersedia:** jangan menggambar dengan alat lain dan jangan berpura-pura sudah menjalankan Archify. Tulis `archify-prompts.md` berisi prompt siap tempel per diagram (format di `references/archify-prompts.md`), lalu beri tahu user di mana Archify bisa dipasang:
   - opencode atau Claude Code: pasang lewat `npx skills add tt-a1i/archify --skill archify` lalu tempel prompt.
   - Claude.ai: unggah `archify.zip` di Settings > Capabilities > Skills (butuh paket berbayar), atau unggah ke Project Knowledge.
4. Revisi diagram dilakukan lewat bahasa biasa ("geser Redis ke kiri", "tambahkan Kafka"). Setiap revisi yang mengubah isi (bukan hanya tata letak) harus disalin kembali ke `ARCHITECTURE_<project>.md` agar tetap sinkron.

### Fase 4: Pengecekan dan serah terima

Sebelum menyerahkan:
- [ ] Setiap komponen dan garis punya sumber; tidak ada yang dikarang
- [ ] Nama komponen sama dengan glosarium, techstack.md, dan database.md
- [ ] Jumlah komponen per diagram masih terbaca (lihat batas di Fase 2)
- [ ] Tingkat detail sesuai pembaca yang dipilih
- [ ] Semua `[PERLU KONFIRMASI]` dilaporkan
- [ ] Tidak ada perubahan pada `AGENTS.md`, `task.md`, atau file perancangan lain

Serahkan semua file dengan `present_files`, urut: `ARCHITECTURE_<project>.md`, lalu `archify-prompts.md` atau file HTML diagram. Ringkas dalam beberapa kalimat apa yang dihasilkan dan apa yang masih perlu dikonfirmasi.

Ingatkan user bahwa diagram perlu dibuat ulang bila stack, database, atau alur bisnis berubah.

## Struktur output

```
<project>-architecture/
├── ARCHITECTURE_<project>.md     (spesifikasi bersumber, sumber kebenaran diagram)
├── archify-prompts.md            (bila Archify belum tersedia di lingkungan ini)
└── diagrams/
    └── <jenis>-<project>.html    (hasil Archify, bila dijalankan)
```

## Referensi

| File | Dibaca saat |
|---|---|
| `references/archify-prompts.md` | Fase 1 (data per jenis diagram) dan Fase 3 (format prompt Archify) |

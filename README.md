# Claude Skills

Kumpulan skill kustom (Agent Skills) untuk Claude. Repositori ini adalah **sumber utama**: semua perubahan dibuat di sini, lalu zip-nya diunggah ke tiap akun Claude.

Aturan lengkap untuk mengubah repositori ini ada di [AGENTS.md](AGENTS.md).

## Daftar skill

| Skill | Versi | Status | Fungsi singkat |
|---|---|---|---|
| [prd-builder](skills/prd-builder/) | 1.0.0 | aktif | Menyusun PRD dari nol lewat wawancara, output `PRD_<proyek>.md` + file pendukung |
| [techstack-recommender](skills/techstack-recommender/) | 1.0.0 | aktif | Membaca PRD lalu merekomendasikan tech stack, output `techstack.md` |
| [design-direction-builder](skills/design-direction-builder/) | 1.0.0 | aktif | Menyusun tiga arah desain dari PRD dan techstack, mockup HTML, dan mengunci pilihan menjadi `DESIGN.md` resmi Stitch |
| [design-plan-builder](skills/design-plan-builder/) | 1.0.0 | aktif | Rancangan kerja website (UI/UX, Frontend, Backend) + mockup HTML statis |
| [stitch-design-builder](skills/stitch-design-builder/) | 2.0.0 | aktif | Mengubah design plan atau gambar referensi menjadi paket siap pakai untuk Google Stitch |

> Kolom **Versi** harus selalu sama dengan entri teratas `CHANGELOG.md` milik skill tersebut.

## Menunggu file SKILL.md

Skill berikut sudah dibuat pemiliknya tetapi isi `SKILL.md`-nya belum diserahkan, jadi belum ada foldernya di `skills/`. Tambahkan foldernya saat filenya tersedia, lalu pindahkan barisnya ke tabel di atas.

| Skill | Gambaran |
|---|---|
| instruktur-bahasa-inggris | Instruktur bahasa Inggris: persiapan TOEFL (Grammar dan Reading), transisi ke Academic English |
| instruktur-database | Instruktur database: perancangan DBMS, ERD, CDM/PDM, skrip SQL (DDL/DML) |
| senior-fullstack-mvp | Senior Full Stack Developer untuk MVP web cepat |
| senior-fullstack-secure | Senior Full Stack Developer dengan arsitektur aman kelas enterprise |

## Rencana (belum dibuat)

| Gagasan | Gambaran |
|---|---|
| database-skill | Skill `database.md` pelengkap prd-builder untuk perancangan database |

## Cara memakai skill di akun Claude

```bash
python scripts/build.py --all
```

Hasilnya ada di `dist/<nama-skill>.zip`. Unggah zip itu lewat pengaturan Skills di claude.ai pada tiap akun (letak menunya bisa berubah). Setelah skill diperbarui, unggah zip baru ke tiap akun; bila Claude tidak menimpa versi lama otomatis, hapus dulu versi lama di akun tersebut.

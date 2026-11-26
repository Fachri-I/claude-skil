# Claude Skills

Kumpulan skill kustom (Agent Skills) untuk Claude. Repositori ini adalah **sumber utama**: semua perubahan dibuat di sini, lalu zip-nya diunggah ke tiap akun Claude.

Aturan lengkap untuk mengubah repositori ini ada di [AGENTS.md](AGENTS.md).

## Daftar skill

| Skill                                                        | Versi | Status | Fungsi singkat                                                                                                       |
| ------------------------------------------------------------ | ----- | ------ | -------------------------------------------------------------------------------------------------------------------- |
| [prd-builder](skills/prd-builder/)                           | 1.0.0 | aktif  | Menyusun PRD dari nol lewat wawancara, output `PRD_<proyek>.md` + file pendukung                                     |
| [techstack-recommender](skills/techstack-recommender/)       | 1.0.0 | aktif  | Membaca PRD lalu merekomendasikan tech stack, output `techstack.md`                                                  |
| [design-direction-builder](skills/design-direction-builder/) | 1.1.0 | aktif  | Menyusun tiga arah desain dari PRD dan techstack, mockup HTML, dan mengunci pilihan menjadi `DESIGN.md` resmi Stitch |
| [design-plan-builder](skills/design-plan-builder/)           | 1.0.0 | aktif  | Rancangan kerja website (UI/UX, Frontend, Backend) + mockup HTML statis                                              |
| [stitch-design-builder](skills/stitch-design-builder/)       | 2.0.0 | aktif  | Mengubah design plan atau gambar referensi menjadi paket siap pakai untuk Google Stitch                              |

> Kolom **Versi** harus selalu sama dengan entri teratas `CHANGELOG.md` milik skill tersebut.

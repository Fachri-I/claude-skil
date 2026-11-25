# AGENTS.md — Aturan repositori Claude Skills

Dokumen ini dibaca oleh AI coding agent (OpenCode) setiap kali bekerja di repositori ini. Ikuti seluruhnya. Bila ada yang tidak jelas atau bertentangan dengan permintaan pengguna, **tanyakan dulu**, jangan menebak.

## 1. Tujuan

Repositori ini menyimpan skill kustom Claude beserta riwayat versinya. Skill dirancang dan diperbarui oleh pengguna bersama Claude di chat. Tugas agent: menaruh file hasilnya di tempat yang benar, mencatat versi, commit, tag, dan push.

## 2. Struktur wajib

```
claude-skills/
├── README.md                  # daftar skill + versi + status
├── AGENTS.md                  # file ini
├── .gitignore
├── scripts/
│   └── build.py               # validasi + kemas zip
├── skills/
│   └── <nama-skill>/          # satu folder per skill
│       ├── SKILL.md           # wajib, nama file persis SKILL.md
│       ├── CHANGELOG.md       # wajib, riwayat versi skill ini
│       ├── references/        # opsional: dokumen yang dibaca sesuai kebutuhan
│       └── scripts/           # opsional: skrip pendukung skill
└── dist/                      # hasil build (zip), TIDAK di-commit
```

Aturan penamaan:

- Nama folder skill memakai kebab-case (huruf kecil, angka, tanda hubung), maksimal 64 karakter, contoh `prd-builder`.
- Nilai `name` di frontmatter `SKILL.md` harus **sama persis** dengan nama folder.
- Frontmatter hanya boleh berisi key: `name`, `description`, `license`, `allowed-tools`, `metadata`, `compatibility`. Jangan menambah key `version`. Versi dicatat di `CHANGELOG.md` dan tag Git.
- `description` maksimal 1024 karakter dan tidak boleh memuat tanda `<` atau `>`.
- Satu skill = satu folder mandiri. Jangan membuat file yang dipakai bersama antar skill; salin saja ke masing-masing skill.

## 3. Versi (SemVer per skill)

Setiap skill punya versi sendiri, `MAJOR.MINOR.PATCH`:

- **MAJOR**: alur kerja atau format output berubah sehingga hasilnya tidak sebanding dengan versi sebelumnya.
- **MINOR**: menambah langkah, fitur, pertanyaan, atau file referensi baru.
- **PATCH**: perbaikan kalimat, typo, kejelasan, atau penyesuaian kecil.

Sumber kebenaran versi saat ini adalah entri teratas `skills/<nama>/CHANGELOG.md` dengan format `## [X.Y.Z] - YYYY-MM-DD`. Isi entri dikelompokkan di bawah `### Added`, `### Changed`, `### Fixed`, atau `### Removed`.

## 4. Langkah setiap kali satu skill diperbarui

1. Taruh file baru dari pengguna di `skills/<nama>/` persis sesuai isi yang diberikan. Jangan mengubah isi di luar yang diminta.
2. Tambahkan entri baru di **paling atas** `CHANGELOG.md` skill itu (versi baru, tanggal hari ini, ringkasan perubahan). Bila pengguna menyertakan ringkasan dari chat, pakai itu.
3. Perbarui kolom **Versi** skill tersebut di tabel `README.md`.
4. Jalankan `python scripts/build.py <nama>`. Harus `[OK]`. Jika `[GAGAL]`, perbaiki masalahnya atau tanyakan ke pengguna.
5. Commit (lihat bagian 5).
6. Beri tag `<nama>-vX.Y.Z` (lihat bagian 5), lalu push.

Menambah skill baru: buat folder `skills/<nama>/` dengan `SKILL.md` dan `CHANGELOG.md` (entri `1.0.0`), tambahkan baris di tabel `README.md`, lalu ikuti langkah 4 sampai 6. Jika skill itu sebelumnya tercantum di bagian "Menunggu file SKILL.md" atau "Rencana", pindahkan barisnya ke tabel utama.

## 5. Commit, tag, dan push

- Satu commit per skill. Jangan menggabungkan perubahan beberapa skill dalam satu commit.
- Format pesan commit: `<tipe>(<skill>): <ringkasan singkat, huruf kecil>`.
  - Tipe: `feat` (fitur/langkah baru), `fix` (perbaikan), `docs` (hanya teks/penjelasan), `refactor` (susunan ulang tanpa ubah perilaku), `chore` (perawatan repo).
  - Contoh: `feat(prd-builder): tambah pertanyaan tentang anggaran`, `fix(techstack-recommender): perbaiki format tabel alternatif`.
  - Perubahan yang bukan milik satu skill: `chore: perbarui README` atau `chore(repo): ...`.
- Tag anotasi per rilis skill: `git tag -a <skill>-vX.Y.Z -m "<skill> vX.Y.Z: <ringkasan>"`, contoh `prd-builder-v1.1.0`.
- Cabang kerja: `main` saja (repositori pribadi). Boleh membuat cabang untuk perubahan besar, tetapi gabungkan ke `main` sebelum tag.
- Push: `git push origin main` lalu `git push origin --tags`.

## 6. Larangan

- Jangan `git push --force`, jangan menghapus atau memindahkan tag yang sudah dipush.
- Jangan commit folder `dist/`, file `.zip`, token, kunci API, atau file rahasia apa pun.
- Jangan mengubah isi `SKILL.md` atau file referensi di luar permintaan pengguna. Perubahan format/rapi-rapi tanpa diminta juga dilarang.
- Jangan membuat skill atau mengarang isi file skill yang belum diberikan pengguna.
- Jangan menebak URL remote GitHub atau nama repositori. Tanyakan.

## 7. Memakai skill di akun Claude

`python scripts/build.py --all` menghasilkan `dist/<nama>.zip` untuk tiap skill. Pengguna sendiri yang mengunggahnya ke tiap akun Claude. Agent cukup memastikan zip berhasil dibuat dan melaporkan nama skill beserta versinya.

# Referensi: data per diagram dan template prompt Archify

## Daftar isi
1. Data yang dibutuhkan per jenis diagram
2. Tingkat detail per pembaca
3. Template prompt Archify
4. Contoh singkat (lifecycle pesanan)

## 1. Data yang dibutuhkan per jenis diagram

| Jenis | Data minimum | Sumber utama |
|---|---|---|
| Arsitektur | frontend, backend, database, hosting, layanan eksternal (pembayaran, storage, email); modul backend utama; peran pengguna; cara autentikasi | techstack.md, BACKEND_*.md, security.md |
| Data flow | data apa yang masuk dari siapa, disimpan di tabel mana, keluar ke mana | database.md, BACKEND_*.md |
| Sequence | satu skenario, daftar aktor (pengguna, frontend, API, database, layanan eksternal), urutan panggilan | PRD (alur utama), BACKEND_*.md (endpoint) |
| Workflow | langkah proses bisnis per peran, titik keputusan | PRD |
| Lifecycle | entitas yang punya status, daftar status, transisi, pemicu, aktor yang boleh memicu | PRD (aturan bisnis), database.md (kolom status) |

Jika satu data minimum tidak ditemukan di sumbernya, tandai `[PERLU KONFIRMASI]` dan tanyakan. Jangan mengisi dari kebiasaan umum.

## 2. Tingkat detail per pembaca

| Pembaca | Isi diagram | Hindari |
|---|---|---|
| Awam / klien non-teknis | blok besar dengan nama fungsi ("Pembayaran", "Pesanan"), panah bermakna bisnis | nama library, protokol, nama tabel |
| Dosen / klien teknis | blok + teknologi di bawah nama, lapisan jelas | detail endpoint |
| Tim developer | modul, protokol (REST, WebSocket), arah data, batas keamanan | hal yang tidak ada di dokumen |

## 3. Template prompt Archify

Tempel sebagai satu blok per diagram. Isi dari `ARCHITECTURE_<project>.md`, jangan menambah elemen baru.

```
Gunakan skill archify untuk membuat diagram {JENIS} dari deskripsi berikut.

Pembaca: {awam | dosen/klien | tim developer}
Bahasa label: {Indonesia | Inggris}
Tema: {terang | gelap | keduanya}

Lapisan dan komponen:
- {Lapisan 1}: {Komponen A (teknologi)}, {Komponen B (teknologi)}
- {Lapisan 2}: ...

Koneksi:
- {Komponen A} -> {Komponen B}: {label singkat}
- ...

Catatan tata letak: {misalnya "klien di kiri, data di kanan"}.
Hanya gambar elemen yang disebut di atas. Jangan menambah komponen.
```

Untuk lifecycle, ganti "Lapisan dan komponen" dengan "Status" dan "Transisi" (`Status A -> Status B: pemicu oleh aktor`). Untuk sequence, ganti dengan "Aktor" dan "Langkah berurutan" bernomor.

## 4. Contoh singkat (lifecycle pesanan, ilustrasi format)

```
Gunakan skill archify untuk membuat diagram lifecycle dari deskripsi berikut.

Pembaca: dosen/klien
Bahasa label: Indonesia
Tema: keduanya

Status: Dibuat, Dibayar, Ditahan Admin, Selesai, Dispute, Dibatalkan

Transisi:
- Dibuat -> Dibayar: pembeli membayar
- Dibayar -> Ditahan Admin: dana diterima admin
- Ditahan Admin -> Selesai: pembeli konfirmasi, dana diteruskan
- Ditahan Admin -> Dispute: pembeli melaporkan masalah
- Dibuat -> Dibatalkan: pembeli membatalkan

Hanya gambar status dan transisi di atas. Jangan menambah status.
```

Contoh ini hanya ilustrasi format, bukan data proyek. Data nyata harus berasal dari PRD dan database.md.

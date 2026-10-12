> 🇬🇧 [English](README.md) | 🇮🇩 [Bahasa Indonesia](README.id.md)

# 5_verify_references/ - Verifikasi Referensi

Folder ini memverifikasi keberadaan referensi pendukung dengan mencocokkan
judulnya ke Crossref dan menampilkan DOI hasil pencarian.

## Alur (order of execution)

```
verify_refs.py   ->   (cetak ke layar / stdout)
```

Tidak ada ketergantungan antar-file di folder ini.

## File

### `verify_refs.py`
- **Tujuan:** Mencari tiap judul referensi (daftar `refs` yang tertanam di skrip) di Crossref dan menampilkan tahun, jurnal, judul, serta DOI hasil pencarian (2 kandidat teratas per judul).
- **INPUT:** tidak ada file (daftar judul tertanam di skrip); sumber jaringan `https://api.crossref.org/works`.
- **OUTPUT:** hanya cetak ke stdout (tidak menulis file).
- **Menjalankan:** `python3 verify_refs.py`

> **NOTE:** Skrip ini tidak memakai path file, jadi tidak ada path absolut yang
> perlu diubah. Skrip lain di pipeline memakai path absolut
> (mis. `BASE="/tmp/opencode/slr"`) yang harus kamu sesuaikan sendiri.

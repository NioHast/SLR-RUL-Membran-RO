> 🇬🇧 [English](README.md) | 🇮🇩 [Bahasa Indonesia](README.id.md)

# 3_journal_classification/ - Klasifikasi Jurnal (Kuartil Scopus)

Folder ini menetapkan kuartil Scopus tiap jurnal korpus berdasarkan dataset mirror
SCImago (turunan Scopus), dan menyediakan verifikasi independen.

## Alur (order of execution)

```
download_mirrors.py  ->  issn.py  ->  classify_scopus.py  ->  verify_scopus.py
        |                   |                 |                     |
 ../mirror_data/*     issn_map.json    corpus_*.json        scopus_check.json
                                        (kolom klasifikasi)

check_open_access.py  (mandiri: cek status OA + lisensi)
        |
 open_access_status.json
```

1. `download_mirrors.py` - unduh mirror SCImago.
2. `issn.py` - petakan DOI -> ISSN/venue.
3. `classify_scopus.py` - tetapkan kuartil Scopus per artikel.
4. `verify_scopus.py` - verifikasi silang cakupan Scopus.
5. `check_open_access.py` - (mandiri) cek OA + lisensi.

## File

### `download_mirrors.py`
- **Tujuan:** Mengunduh semua dataset mirror publik (SCImago SJR Best Quartile, SJR panel 1999-2025, daftar judul Scopus).
- **INPUT:** tidak ada (unduh dari internet).
- **OUTPUT:** `../mirror_data/sjr_quart.csv`, `../mirror_data/sjr_all.csv`, `../mirror_data/scopus_titles.tsv`.
- **Menjalankan:** `python3 download_mirrors.py`

### `issn.py`
- **Tujuan:** Mengambil ISSN-L, daftar ISSN, nama jurnal, dan status DOAJ untuk tiap DOI dari OpenAlex.
- **INPUT:** `corpus_*.json`.
- **OUTPUT:** `issn_map.json`.
- **Menjalankan:** `python3 issn.py`

### `classify_scopus.py`
- **Tujuan:** Menetapkan field `klasifikasi` tiap artikel: `SJR Best Quartile` (resmi, ed. 2022) -> fallback SJR 2024 (kuartil diturunkan) -> "Belum terverifikasi".
- **INPUT:** `data/issn_map.json`, `../mirror_data/sjr_quart.csv`, `../mirror_data/sjr_all.csv`.
- **OUTPUT:** `data/corpus_*.json` (ditulis ulang dengan kolom `klasifikasi`).
- **Menjalankan:** `python3 classify_scopus.py`

### `verify_scopus.py`
- **Tujuan:** Menghitung ulang secara independen berapa jurnal korpus yang benar-benar terindeks Scopus + kuartilnya (verifikasi silang klasifikasi).
- **INPUT:** `issn_map.json`, `sjr_all.csv` (salin dari `../mirror_data/` ke folder ini dulu).
- **OUTPUT:** `scopus_check.json`.
- **Menjalankan:** `python3 verify_scopus.py`

### `check_open_access.py`
- **Tujuan:** Mengecek status Open Access + lisensi tiap artikel via Unpaywall untuk menentukan mana yang aman/legal disertakan full-text-nya (OA + lisensi CC).
- **INPUT:** `../../metadata/corpus_a.json` (fallback: `../../source_code/data/corpus_a.json`).
- **OUTPUT:** `open_access_status.json` (di folder yang sama).
- **Menjalankan:** `python3 check_open_access.py` (butuh internet).

> **NOTE:** Sebagian skrip di folder ini memakai path relatif terhadap lokasi file
> (`HERE/data`, `HERE/../mirror_data`), sebagian lagi memakai working directory.
> Skrip lain di pipeline memakai path absolut (mis. `BASE="/tmp/opencode/slr"`)
> yang harus kamu sesuaikan sendiri.

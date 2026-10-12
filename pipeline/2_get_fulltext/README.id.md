> 🇬🇧 [English](README.md) | 🇮🇩 [Bahasa Indonesia](README.id.md)

# 2_get_fulltext/ - Pengambilan Full-Text

Folder ini mengunduh PDF **Open Access** secara otomatis, lalu memakai Playwright
sebagai fallback untuk artikel yang masih berstatus *closed* tetapi ternyata PDF-nya
tersedia publik.

## Alur (order of execution)

```
download_fulltext.py  ->  download_closed_playwright.py
        |                            |
  ../full_text/*.pdf          ../full_text/*.pdf
  fulltext_report.json        closed_playwright_report.json
```

1. `download_fulltext.py` - unduh semua PDF OA (OpenAlex + Unpaywall).
2. `download_closed_playwright.py` - (fallback) coba artikel berstatus `closed` via browser.

## File

### `download_fulltext.py`
- **Tujuan:** Mengunduh full-text PDF Open Access untuk seluruh korpus dari semua lokasi OA yang diketahui (OpenAlex `best_oa_location` + `locations`, dan Unpaywall `best_oa_location` + `oa_locations`).
- **INPUT:** `data/corpus_*.json`.
- **OUTPUT:** `../full_text/00X_*.pdf` dan `../full_text/fulltext_report.json` (status ok/skip/closed).
- **Menjalankan:** `python3 download_fulltext.py` (aman diulang; file yang sudah ada dilewati).

### `download_closed_playwright.py`
- **Tujuan:** Untuk tiap artikel berstatus `closed`, membuka halaman DOI dengan Playwright (Chrome), mencari link/tombol PDF, dan mengunduh hanya bila benar-benar PDF publik; melewati yang butuh login.
- **INPUT:** `data/corpus_*.json` + `../full_text/fulltext_report.json`.
- **OUTPUT:** `../full_text/00X_*.pdf` dan `../full_text/closed_playwright_report.json`.
- **Menjalankan:** `python3 download_closed_playwright.py` (butuh Playwright + Chrome).

> **NOTE:** Path dihitung relatif terhadap lokasi file (`HERE/data` -> `../full_text`),
> jadi struktur folder harus dijaga. Skrip lain di pipeline memakai path absolut
> (mis. `BASE="/tmp/opencode/slr"`) yang harus kamu sesuaikan sendiri.

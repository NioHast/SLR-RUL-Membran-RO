> 🇬🇧 [English](RUNBOOK.md) | 🇮🇩 [Bahasa Indonesia](RUNBOOK.id.md)

# RUNBOOK - Alur End-to-End

Panduan menjalankan ulang SELURUH pipeline SLR dari nol. Menjelaskan urutan langkah dan
**keterkaitan antar folder** (`pipeline/`, `metadata/`, `mirror_data/`, `papers_analysis/`, `docs/`).

## Diagram Keterkaitan
```
  pipeline/1_search_and_select/  --->  metadata/  (pool, ranked, selected, corpus)
            |
  pipeline/3_journal_classification/  <-- mirror_data/ (SJR/Scopus)  --->  metadata/ (issn, kuartil)
            |
  pipeline/2_get_fulltext/  +  pipeline/6_fulltext_extraction_kaggle/  --->  papers_analysis/ (full_text.md/pdf, figures)
            |
  (analisis per paper: extraction.json, analysis.txt)  --->  metadata/corpus_a.json
            |
  pipeline/4_build_deliverables/  -------------------------------------->  docs/ (xlsx, docx, pdf, html)
            |
  pipeline/5_verify_references/  (verifikasi DOI referensi)
```

## Prasyarat
- **Python 3** + paket: `openpyxl`, `python-docx`, `beautifulsoup4`, `lxml`, `pdfplumber`, `PyMuPDF`, `camelot-py`, `kaggle`.
  ```
  pip install --break-system-packages openpyxl python-docx beautifulsoup4 lxml pdfplumber PyMuPDF "camelot-py[cv]" kaggle
  ```
- **LibreOffice** (headless) untuk konversi DOCX -> PDF.
- **Akun Kaggle + API token** (untuk tahap 6): simpan di `~/.kaggle/access_token` dan set `export KAGGLE_API_TOKEN=$(cat ~/.kaggle/access_token)`. **Token tidak disimpan di repo ini.**
- **Catatan penting:** sebagian skrip memakai **path absolut** (mis. `BASE="/tmp/opencode/slr"`). Ubah ke lokasi kerjamu sendiri. Jalankan sesuai README di tiap subfolder.

## Langkah
1. **Pencarian & seleksi korpus** - `pipeline/1_search_and_select/`
   Panen metadata (OpenAlex/Crossref), ranking relevansi, seleksi korpus -> `metadata/pool.json`, `ranked.json`, `selected*.json`.
2. **Klasifikasi jurnal** - `pipeline/3_journal_classification/` (+ `mirror_data/`)
   Unduh mirror SJR (`download_mirrors.py`), petakan ISSN (`issn.py`), tetapkan kuartil (`classify_scopus.py`) -> `metadata/issn_map.json`, `scopus_official.json`. Cek OA/lisensi: `check_open_access.py` -> `metadata/open_access_status.json`.
3. **Perolehan & ekstraksi full-text** - `pipeline/2_get_fulltext/` + `pipeline/6_fulltext_extraction_kaggle/`
   Unduh OA (`download_fulltext.py`/Playwright) lalu ekstraksi penuh dengan **Marker** di Kaggle GPU (kernel + merge) -> `papers_analysis/<folder>/full_text.md`, `figures/`, `meta.json`.
4. **Analisis per paper (Phase 5)** - hasilkan `papers_analysis/<folder>/extraction.json` + `analysis.txt` -> digabung ke `metadata/corpus_a.json`.
5. **Bangun deliverables** - `pipeline/4_build_deliverables/`
   `fill_report.py` -> `build_xlsx.py` -> `build_docx.py` -> `build_article_docx.py` -> (LibreOffice) PDF -> `docs/`.
6. **Verifikasi referensi** - `pipeline/5_verify_references/` (`verify_refs.py`).

## Ringkas Peran Folder
| Folder | Peran | Jenis |
|---|---|---|
| `pipeline/` (1-6) | Kode sumber seluruh tahap | KODE |
| `metadata/` | Data antara & korpus (JSON) | DATA |
| `mirror_data/` | Dataset SJR/Scopus (SCImago) | DATA |
| `papers_analysis/` | Hasil analisis + (OA) full-text & figur | OUTPUT |
| `docs/` | Deliverables akhir (xlsx/docx/pdf/html) | OUTPUT |

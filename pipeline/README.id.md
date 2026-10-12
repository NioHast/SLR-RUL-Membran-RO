> 🇬🇧 [English](README.md) | 🇮🇩 [Bahasa Indonesia](README.id.md)

# pipeline/ - Kode Sumber (reproducible)

Kode untuk menjalankan ulang SLR dari awal. Dikelompokkan berurutan:

| Folder | Fungsi | Detail |
|---|---|---|
| `1_search_and_select/` | Panen metadata (OpenAlex/Crossref), ranking relevansi, seleksi korpus (`harvest.py`, `rank.py`, `select.py`, `supp.py`). | Detail tiap file: lihat [`README.md`](1_search_and_select/README.md) |
| `2_get_fulltext/` | Memperoleh full-text Open Access (`download_fulltext.py`) + fallback Playwright (`download_closed_playwright.py`). | Detail tiap file: lihat [`README.md`](2_get_fulltext/README.md) |
| `3_journal_classification/` | Unduh mirror SJR (`download_mirrors.py`), ambil ISSN (`issn.py`), klasifikasi kuartil Scopus (`classify_scopus.py`, `verify_scopus.py`). | Detail tiap file: lihat [`README.md`](3_journal_classification/README.md) |
| `4_build_deliverables/` | Bangun hasil: `fill_report.py`, `build_xlsx.py`, `build_docx.py`, `build_article_docx.py` + sumber teks (`report.md`, `synthesis.json`, `article.md`, `presentation_brief.md`) + `assets/` (reveal.js). | Detail tiap file: lihat [`README.md`](4_build_deliverables/README.md) |
| `5_verify_references/` | Verifikasi DOI referensi via Crossref (`verify_refs.py`). |
| `6_fulltext_extraction_kaggle/` | Kernel/notebook Kaggle untuk ekstraksi full-text dengan Marker (GPU). Lihat README di subfolder. |

Detail tiap file: lihat `README.md` di masing-masing subfolder. Detail tiap file: lihat [`README.md`](5_verify_references/README.md) |

## Catatan
- Skrip memakai **path absolut** (mis. `BASE=/tmp/opencode/slr`); sesuaikan ke lokasi kerjamu.
- Data masukan/keluaran (JSON) ada di `../metadata/`; mirror SJR di `../mirror_data/`.
- Dependensi Python: `openpyxl`, `python-docx`, `beautifulsoup4`, `lxml`, `pdfplumber`, `PyMuPDF`, `camelot`.
- Konversi PDF memakai LibreOffice (headless).

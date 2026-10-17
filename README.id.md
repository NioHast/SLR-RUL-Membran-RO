> 🇬🇧 [English](README.md) | 🇮🇩 [Bahasa Indonesia](README.id.md)

# SLR: Prediksi Remaining Useful Life (RUL) Membran Reverse Osmosis dengan Survival Analysis & Deep Learning

Systematic Literature Review (SLR) atas **101 record yang dinilai (79 included)** tentang prediksi RUL membran
reverse osmosis (RO)/desalinasi, dengan penekanan pada **data tersensor (right-censored)**
dan **skala data kecil**, sebagai dasar penelitian tesis di bidang Sistem Informasi.

**Penulis:** Muhammad Nio Hastungkoro (NIM 30000226410017) - Magister Sistem Informasi,
Sekolah Pascasarjana, Universitas Diponegoro. Kontak: mnioh@students.undip.ac.id

## Struktur Repositori
| Folder | Isi |
|---|---|
| `docs/` | Deliverables utama: protokol SLR, korpus (Excel), laporan, artikel jurnal, presentasi, log keputusan, diagram (`figures/`). |
| `papers_analysis/` | Hasil analisis per paper (`extraction.json` + `analysis.txt`) untuk korpus included. |
| `pipeline/` | Kode sumber pipeline (pencarian, klasifikasi jurnal, pembangunan dokumen, verifikasi referensi). |
| `metadata/` | Data antara/JSON: korpus master, pemetaan ISSN & kuartil jurnal, statistik pencarian. |
| `pipeline/6_fulltext_extraction_kaggle/` | Kode kernel Kaggle (ekstraksi full-text dengan Marker di GPU). |
| `mirror_data/` | Data SJR/Scopus (SCImago) yang dipakai untuk klasifikasi kuartil (sumber: README.md). |
| `AGENTS.md` | Konvensi untuk agen koding AI. Keterbukaan penggunaan AI: [`docs/AI_USAGE.id.md`](docs/AI_USAGE.id.md). |

## Metode (ringkas)
Kitchenham & Charters (prosedur) + PRISMA 2020 (pelaporan) + Webster & Watson (matriks konsep)
+ Wohlin (snowballing). Pencarian hybrid; klasifikasi kuartil via SCImago/SJR (turunan Scopus).
Ekstraksi full-text memakai **Marker** (di Kaggle GPU T4); analisis per paper memakai rubrik
kualitas Q1-Q8, dimensi ketentuan ketat (D1-D8), dan tingkat relevansi (Inti-Metode / Inti-Domain /
Inti-Metode+Domain / Pendukung / Konteks).

## Temuan Kunci
- Korpus: **101 dinilai, 79 included** (Q1/Q2/Q3). Censoring (D3) dibahas 28 artikel included; domain RO (D7) 2 artikel, dengan **irisan 0**.
- **Irisan metode x domain (Inti-Metode+Domain) hanya 2 artikel** -> gap penelitian nyata.

## Penggunaan AI
AI generatif (LLM) membantu pada **tahap tertentu yang terdokumentasi** (ekstraksi full-text, sintesis
tematik, penulisan draf, dokumen). Semua keputusan seleksi studi & isi akhir dibuat oleh penulis.
Template prompt: [`pipeline/prompts/`](pipeline/prompts/README.id.md); keterbukaan: [`docs/AI_USAGE.id.md`](docs/AI_USAGE.id.md).

## Prasyarat
- **Python 3.12+** (paket dipatok di `requirements.txt`; versi di `.python-version`).
- Pasang paket Python: `pip install -r requirements.txt`.
- **Dependensi sistem (bukan pip):** LibreOffice (`soffice`, DOCX->PDF), Pandoc, Ghostscript (`gs`, untuk Camelot).
- **Kaggle CLI + API token** untuk tahap ekstraksi full-text (token tidak disimpan di repo ini).

## Cara Menjalankan Ulang (reproducible)
1. `pipeline/1_search_and_select/`: panen metadata (OpenAlex/Crossref) -> `metadata/`.
2. `pipeline/3_journal_classification/`: klasifikasi kuartil (SCImago) + `mirror_data/`.
3. `pipeline/2_get_fulltext/` + `pipeline/6_fulltext_extraction_kaggle/`: peroleh & ekstrak full-text (Marker via Kaggle GPU).
4. `pipeline/4_build_deliverables/`: bangun `docs/` (Excel, Word, PDF, presentasi).
5. `docs/figures/src/build_figures.sh`: bangun ulang diagram (Mermaid + matplotlib).
6. `pipeline/4_build_deliverables/build_presentation.py`: validasi deck dan bangun PDF-nya.
(Lihat README di tiap folder. Skrip relatif terhadap repo; sesuaikan path keluaran bila perlu.)

## Catatan Hak Cipta (PENTING)
- **Full-text OA + CC untuk 61 dari 79 included (77 dari 101 yang dinilai)** -> `full_text.pdf`
  **disertakan** karena lisensinya mengizinkan redistribusi (dengan **atribusi**; lihat `SOURCE.txt` tiap folder).
- **Sisanya (24 artikel: closed / bronze / tanpa lisensi jelas)** -> **hanya hasil analisis**
  (`extraction.json`, `analysis.txt`) + **DOI**, karena tidak ada izin redistribusi.
- Status OA/lisensi dicek otomatis: `pipeline/3_journal_classification/check_open_access.py`
  (API Unpaywall) -> hasil di `metadata/open_access_status.json`.
- Kode memperoleh & mengekstrak full-text disertakan (`pipeline/`, termasuk `pipeline/6_fulltext_extraction_kaggle/`) agar **reproducible**.

## Atribusi Data
Kuartil/klasifikasi jurnal bersumber dari **SCImago (SJR)** - https://www.scimagojr.com (turunan Scopus).
Mirror data: lihat `mirror_data/README.md`.

## Lisensi / License
- **Kode (buatan penulis): MIT-0** - bebas dipakai, **tanpa atribusi** (lihat `LICENSE`).
- **Konten buatan penulis (dokumen, hasil analisis, metadata): CC0 1.0** - public domain, **tanpa atribusi** (lihat `LICENSE-CONTENT`).
- **Data/artikel pihak ketiga: tetap lisensinya** (SCImago = CC BY-NC; artikel OA sesuai lisensinya) - lihat `NOTICE`.
- Ringkas: *Kode & konten saya: MIT-0/CC0 (tanpa atribusi). Data pihak ketiga (SCImago, artikel OA) tetap lisensinya.*

> Ini adalah artefak penelitian. Issues/PRs mungkin tidak dipantau secara berkala.

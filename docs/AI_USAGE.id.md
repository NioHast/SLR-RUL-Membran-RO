> 🇬🇧 [English](AI_USAGE.md) | 🇮🇩 [Bahasa Indonesia](AI_USAGE.id.md)

# Keterbukaan Penggunaan AI

Repositori ini adalah artefak penelitian Systematic Literature Review (SLR). Alat AI generatif
(LLM) membantu pada **tahap tertentu yang terdokumentasi**; **seluruh keputusan seleksi studi,
penilaian kualitas, dan isi akhir dibuat serta ditinjau oleh penulis (manusia)**. Template prompt
berversi ada di [`pipeline/prompts/`](../pipeline/prompts/README.id.md).

## AI dipakai untuk apa
| Tahap | Peran AI | Alat / model | Pemeriksaan manusia |
|---|---|---|---|
| Phase 5 - ekstraksi per paper | Membaca isi penuh tiap paper (`text.md` dari Marker) + figur terpilih; menulis `extraction.json` + `analysis.txt` (ringkasan, temuan kunci, tag dimensi + bukti, kualitas Q1-Q8, tier) | Subagen LLM (`deep-low`) dalam wave paralel | Pilot rubrik 5 paper + ekstraksi ganda pada sampel + review penulis |
| Sintesis agregat | Sintesis tematik (D1-D8), research gap, peta teori/konsep | Subagen LLM | Review penulis; angka dicek silang ke korpus |
| Deliverable naratif | Penyusunan narasi laporan / artikel jurnal | Berbantuan LLM | Review penulis |
| Presentasi | Membangun deck reveal.js dari `pipeline/prompts/presentation.md` | Subagen LLM | Review penulis |
| Perawatan repo | README, dokumen, format, pesan commit | Agen koding LLM | Review penulis |

## Yang TIDAK dilakukan AI (kode deterministik atau manusia)
- Pencarian & seleksi record (`pipeline/1_search_and_select/`), klasifikasi jurnal/kuartil
  (`pipeline/3_journal_classification/`), verifikasi referensi (`pipeline/5_verify_references/`).
- Konversi full-text: **Marker** (`marker-pdf==1.10.2`) - pipeline PDF-ke-Markdown berbasis
  machine learning (model layout/OCR), bukan LLM generatif; dipanggil secara deterministik.
- Pembangunan deliverable: `build_xlsx.py`, `build_docx.py`, `build_article_docx.py`, `fill_report.py`.
- Korpus final 101 artikel, kebijakan kuartil, dan setiap keputusan inklusi/eksklusi.
- Heuristik dimensi berbasis kata kunci di `phase2_assemble.py` **dibatalkan** (terlalu longgar);
  dimensi resmi berasal dari review Phase 5.

## Model & lingkungan
- Tahap AI dijalankan sebagai **subagen LLM (OpenCode, kategori task `deep-low`)** dalam wave
  paralel bertanggal pada **2026-10-11/12**.
- Nama/versi LLM pendukung **tidak terekam** di repo ini. `[ISI bila diketahui]`
- Ekstraksi full-text: `marker-pdf==1.10.2` pada GPU Kaggle (NVIDIA T4).
- Tidak ada API key/token yang disimpan di repositori ini.

## Batasan & tanggung jawab
- Output LLM bersifat **non-deterministik**: prompt mendokumentasikan maksud, bukan jaminan reproduksi.
- Field hasil AI di-spot-check; sisa kesalahan tetap tanggung jawab penulis.
- Tiap prompt mencatat model/versi/tanggal/parameter di headernya.

## Pernyataan keterbukaan (siap tempel)
> Alat AI generatif (LLM) digunakan untuk membantu ekstraksi data full-text, sintesis tematik,
> penulisan draf, dan dokumentasi repositori. Seluruh keputusan seleksi studi, penilaian kualitas,
> dan isi akhir ditinjau serta disetujui oleh penulis, yang bertanggung jawab penuh atas karya ini.

Sitasi: Hastungkoro, M. N. (2026). *SLR: Prediksi RUL Membran Reverse Osmosis* (v1.0.0).
GitHub. https://github.com/NioHast/SLR-RUL-Membran-RO - lihat `docs/AI_USAGE.id.md`.

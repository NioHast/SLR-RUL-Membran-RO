> 🇬🇧 [English](README.md) | 🇮🇩 [Bahasa Indonesia](README.id.md)

# prompts/ - Template Prompt AI (berversi)

Template prompt yang dipakai untuk menghasilkan analisis dan deliverable. File ini
mendokumentasikan **maksud** prompt, bukan jaminan reproduksi (output LLM non-deterministik).
Lihat [`docs/AI_USAGE.id.md`](../../docs/AI_USAGE.id.md) untuk penjelasan AI dipakai di mana.

| File | Tahap | Keluaran | Model / tanggal |
|---|---|---|---|
| `extraction.md` | Phase 5 - ekstraksi full-text per paper | `papers_analysis/*/extraction.json` + `analysis.txt` | Subagen LLM (`deep-low`), 2026-10-11/12 |
| `synthesis.md` | Sintesis tematik agregat | `pipeline/4_build_deliverables/synthesis.json` | Subagen LLM, 2026-10-12 |
| `presentation.md` | Deck presentasi | `SLR_Presentasi.html` (+ PDF) | Subagen LLM, 2026-10-12 |
| `deliverable_style.md` | (lintas-tahap) | kontrak gaya untuk docx/xlsx/deck | rujukan (bukan prompt tugas) |

## Cara pakai
- Isi placeholder (mis. `{PAPER_TEXT}`) dengan masukan Anda.
- Catat **model / versi / tanggal / parameter** di header sebelum menjalankan.
- Skrip build deterministik (`pipeline/4_build_deliverables/*.py`) tetap **sumber kebenaran** format;
  jaga `deliverable_style.md` tetap sinkron (jangan drift).
- Prosa deliverable = Bahasa Indonesia + istilah teknis Inggris; **tanpa em dash** (`—`).

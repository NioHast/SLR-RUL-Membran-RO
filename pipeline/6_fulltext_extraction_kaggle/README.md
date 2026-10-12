> 🇬🇧 [English](README.md) | 🇮🇩 [Bahasa Indonesia](README.id.md)

# kaggle/ - Full-Text Extraction Pipeline on Kaggle

Code to extract article full-text using **Marker** (marker-pdf) on a **Kaggle GPU (NVIDIA T4)**,
run automatically from WSL via the Kaggle CLI.

## Contents
- `make_kernel.py` - creates the kernel notebook (pilot).
- `phase0_pilot_kernel/` - initial test kernel (3 papers).
- `phase1_full_kernel/` - full-corpus kernel (101 papers) + metadata.
- `fix3_kernel/` - repair kernel for 3 papers (PDF mismatch).
- `phase2_assemble.py`, `phase2_finalize.py` - assemble the per-paper folders.
- `phase5_merge.py` - merge the analysis results into the corpus.
- `phase5_run_waves.md` - notes on subagent wave execution.

## Output on Kaggle (not in the repo)
- Dataset (PDF): `muhammadnioh/slr-corpus-pdfs`, `muhammadnioh/slr-pilot-pdfs`, `muhammadnioh/slr-fix3-pdfs`.
- Kernel: `muhammadnioh/slr-corpus-marker`, `muhammadnioh/slr-pilot-marker`, `muhammadnioh/slr-fix3-marker`.

**Why are the Kaggle datasets & outputs (PDF/markdown/images) NOT committed here?**
Because their contents (article PDFs & images) may violate **copyright** and are large.
Only the **code + kernel metadata** are included, so that others can re-run the pipeline
(if they have access rights to the articles). The Kaggle API token is **not** stored in this repo;
the script reads the token from `~/.kaggle/access_token` (the `KAGGLE_API_TOKEN` variable).

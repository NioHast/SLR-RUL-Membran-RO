> 🇬🇧 [English](README.md) | 🇮🇩 [Bahasa Indonesia](README.id.md)

# kaggle/ - Pipeline Ekstraksi Full-Text di Kaggle

Kode untuk mengekstrak full-text artikel memakai **Marker** (marker-pdf) di **Kaggle GPU (NVIDIA T4)**,
dijalankan otomatis dari WSL via Kaggle CLI.

## Isi
- `make_kernel.py` - membuat notebook kernel (pilot).
- `phase0_pilot_kernel/` - kernel uji awal (3 paper).
- `phase1_full_kernel/` - kernel korpus penuh (101 paper) + metadata.
- `fix3_kernel/` - kernel perbaikan 3 paper (mismatch PDF).
- `phase2_assemble.py`, `phase2_finalize.py` - merakit folder per paper.
- `phase5_merge.py` - menggabungkan hasil analisis ke korpus.
- `phase5_run_waves.md` - catatan eksekusi gelombang (wave) subagen.

## Output di Kaggle (tidak di repo)
- Dataset (PDF): `muhammadnioh/slr-corpus-pdfs`, `muhammadnioh/slr-pilot-pdfs`, `muhammadnioh/slr-fix3-pdfs`.
- Kernel: `muhammadnioh/slr-corpus-marker`, `muhammadnioh/slr-pilot-marker`, `muhammadnioh/slr-fix3-marker`.

**Mengapa dataset & output Kaggle (PDF/markdown/gambar) TIDAK di-commit di sini?**
Karena isinya (PDF & gambar artikel) berpotensi melanggar **hak cipta** dan berukuran besar.
Yang disertakan cukup **kode + metadata kernel** agar orang lain dapat menjalankan ulang pipeline
(bila memiliki hak akses ke artikel). API token Kaggle **tidak** disimpan di repo ini;
skrip membaca token dari `~/.kaggle/access_token` (variabel `KAGGLE_API_TOKEN`).

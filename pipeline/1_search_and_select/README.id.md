> 🇬🇧 [English](README.md) | 🇮🇩 [Bahasa Indonesia](README.id.md)

# 1_search_and_select/ - Pencarian & Seleksi Korpus

Folder ini melakukan **panen metadata** dari OpenAlex dan menyeleksi korpus inti
SLR (ranking relevansi + pemetaan pilar konsep A-G).

## Alur (order of execution)

```
harvest.py  ->  supp.py (opsional)  ->  rank.py  ->  select.py
   |                  |                   |             |
 pool.json        pool.json           ranked.json   selected.json
 pool.csv         (diperluas)         (skor)        (korpus inti)
```

1. `harvest.py` - panen awal 16 query.
2. `supp.py` - (opsional) tambah artikel dari 8 query pelengkap.
3. `rank.py` - beri skor relevansi tiap artikel.
4. `select.py` - pilih korpus inti + tandai pilar.

## File

### `harvest.py`
- **Tujuan:** Mengirim 16 query pencarian ke OpenAlex API dan menggabungkan hasil menjadi satu kumpulan artikel unik (dedup berdasarkan ID OpenAlex).
- **INPUT:** tidak ada file (query tertanam di skrip); sumber jaringan `https://api.openalex.org/works`.
- **OUTPUT:** `pool.json` (seluruh artikel unik), `pool.csv` (ringkasan cepat).
- **Menjalankan:** `python3 harvest.py`

### `supp.py`
- **Tujuan:** Menjalankan 8 query tambahan (keterbatasan data, few-shot prognostik, konteks Indonesia) lalu menambahkan hasil **baru** ke `pool.json` tanpa menimpa record lama.
- **INPUT:** `pool.json`.
- **OUTPUT:** `pool.json` (diperluas).
- **Menjalankan:** `python3 supp.py`

### `rank.py`
- **Tujuan:** Memberi skor tiap artikel berdasarkan kata kunci pilar (RUL/censoring/DL/domain RO), bonus kata kunci di judul, dan bobot logaritmik sitasi.
- **INPUT:** `pool.json`.
- **OUTPUT:** `ranked.json` (tiap artikel diberi field `_score`, sudah urut).
- **Menjalankan:** `python3 rank.py`

### `select.py`
- **Tujuan:** Membuang artikel bertopik medis/tanpa abstrak, menandai pilar A-G, lalu memilih korpus inti (prioritas 4 artikel acuan, kuota 72 artikel).
- **INPUT:** `ranked.json`.
- **OUTPUT:** `selected.json` (korpus inti; tiap artikel punya `pillars`).
- **Menjalankan:** `python3 select.py`

> **NOTE:** Skrip di folder ini membaca/menulis file di **working directory** saat ini
> (bukan path absolut). Jalankan dari folder yang benar, atau sesuaikan path-nya.

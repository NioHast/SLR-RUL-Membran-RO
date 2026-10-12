# Spesifikasi Presentasi reveal.js: SLR RUL Membran RO

Tujuan: mempresentasikan SELURUH hasil SLR secara akademik dan meyakinkan.
Sumber data: /tmp/opencode/slr/report_filled.md dan /home/nioha/Downloads/SLR_Korpus.xlsx (sheet "Ringkasan & Status", "SLR - Korpus Jurnal").
Keluaran: satu file HTML mandiri /home/nioha/Downloads/SLR_Presentasi.html memakai reveal.js dari CDN.

## Aturan teknis
- reveal.js via CDN (unpkg/jsdelivr, versi 5.x). Tema kustom (jangan default polos).
- 16:9, navigasi keyboard, progress bar, nomor slide, transisi halus.
- Bahasa Indonesia; istilah teknis boleh Inggris.
- Aman dibuka offline (CDN boleh; tidak ada build step).
- Grafik sederhana diizinkan (Chart.js via CDN atau bar berbasis CSS). Tidak ada gambar eksternal yang bisa gagal.
- Palet akademik: biru tua (#1F4E78), abu, aksen oranye. Font sans-serif (mis. Inter/Arial).

## Struktur slide (isi wajib)
1. **Judul**: judul SLR, nama mahasiswa, NIM, Program Studi Sistem Informasi, tahun.
2. **Agenda**: daftar bagian presentasi.
3. **Latar belakang & urgensi**: mengapa SLR ini perlu (3 poin).
4. **Tujuan & Research Questions**: RQ1–RQ4.
5. **Metode (ringkas)**: Kitchenham + PRISMA 2020 + Webster & Watson + snowballing Wohlin.
6. **Strategi pencarian**: basis data + contoh search string + PICOC (ringkas).
7. **Alur PRISMA**: angka: identifikasi → screening → layak → termasuk (ambil dari report/dataset).
8. **Hasil: sebaran pilar A–G**: grafik batang + penjelasan singkat.
9. **Hasil: matriks konsep D1–D8**: bar jumlah artikel per dimensi.
10. **Sintesis per dimensi**: temuan utama (D1–D8 ringkas).
11. **Research Gap**: nyatakan celah utama (kutip dari "Sintesis & Gap Final").
12. **Kontribusi & implikasi**: apa yang ditawarkan tesis.
13. **Kesimpulan**: 3–4 poin.
14. **Referensi kunci**: 5–8 referensi utama (dengan DOI singkat).
15. **Penutup**: Terima kasih / tanya jawab + kontak.

## Gaya
- Padat, tidak bertele-tele; tiap slide ≤ 6 poin.
- Gunakan angka nyata dari korpus (jangan hardcode 72; ambil jumlah final).
- Sertakan catatan pembicara (speaker notes) singkat di tiap slide (pakai elemen <aside class="notes">).

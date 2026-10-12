# Systematic Literature Review (SLR): Prediksi Remaining Useful Life (RUL) Berbasis Survival Analysis dan Deep Learning untuk Membran Reverse Osmosis

## Abstrak

Tinjauan literatur sistematis ini memetakan metode prediksi sisa usia pakai (Remaining Useful Life, RUL) berbasis survival analysis dan deep learning, dengan perhatian khusus pada penanganan data tersensor (right-censored) dan keterbatasan data (small-data), serta penerapannya pada domain membran reverse osmosis (RO) dan desalinasi. Kajian ini dijalankan mengikuti panduan Kitchenham & Charters (2007), pelaporan PRISMA 2020 (Page dkk., 2021), dan sintesis concept-centric Webster & Watson (2002). Pencarian hybrid (basis data + snowballing Wohlin, 2014) pada repositori terindeks menghasilkan korpus inti puluhan artikel internasional. Hasil menunjukkan bahwa penanganan censoring dan kuantifikasi ketidakpastian masih jarang diterapkan pada domain membran, dan belum ada studi yang secara simultan menggabungkan RUL membran RO, data tanpa kegagalan, skala data kecil, serta integrasi ke sistem pendukung keputusan perawatan. Celah inilah yang menjadi dasar penelitian tesis.

## 1. Pendahuluan

### 1.1 Motivasi dan urgensi ilmiah
Membran reverse osmosis (RO) merupakan komponen inti pada instalasi desalinasi air payau maupun air laut. Kinerjanya menurun seiring waktu karena fouling, scaling, dan degradasi kimia, sehingga memerlukan perawatan berkala (Clean-in-Place, CIP) atau penggantian. Karena perawatan selalu dilakukan secara preventif, sebelum kerusakan fisik total, log pemantauan lapangan didominasi data tersensor kanan (right-censored data): pengamatan berhenti tanpa pernah merekam waktu kegagalan yang sebenarnya. Metode prediksi RUL konvensional yang hanya belajar dari data run-to-failure membuang data tersensor ini, sehingga prediksinya bias (Gao dkk., 2025).

Urgensi SLR ini muncul dari tiga tegangan: (1) metode survival analysis dan deep learning sudah mapan untuk mesin berarmada besar (turbin, bearing, baterai), tetapi belum banyak dipakai untuk membran RO; (2) di lapangan, data membran justru kecil dan tanpa kegagalan teramati, kondisi yang belum banyak diuji; dan (3) manfaat prediksi bagi keputusan perawatan (Sistem Pendukung Keputusan) belum menjadi fokus. SLR ini memetakan bukti untuk memastikan bahwa celah tersebut nyata dan layak diteliti.

### 1.2 Kontribusi SLR
SLR ini menyediakan (a) peta taksonomi metode prediksi RUL dengan fokus censoring dan data kecil; (b) matriks konsep yang menunjukkan sebaran dimensi riset; dan (c) perumusan research gap yang menjadi dasar tesis.

## 2. Metode Tinjauan

### 2.1 Pertanyaan Riset
- RQ1: Bagaimana metode survival analysis menangani data tersensor pada prediksi RUL?
- RQ2: Bagaimana deep learning (LSTM/Transformer/Bayesian) meningkatkan prediksi RUL dan kuantifikasi ketidakpastian?
- RQ3: Kendala apa yang muncul pada kondisi data kecil (small-data) / tanpa kegagalan (all-censored), dan bagaimana solusinya?
- RQ4: Bagaimana hasil prediksi RUL digunakan dalam sistem pendukung keputusan perawatan (DSS/CMMS)?

### 2.2 Strategi Pencarian
Pencarian hybrid memadukan pencarian basis data dan snowballing (Wohlin, 2014). Basis data utama: Scopus, IEEE Xplore, ScienceDirect, ACM Digital Library, AIS eLibrary, dan Web of Science; pelengkap nasional: Garuda dan SINTA. Pencarian awal dilakukan pada repositori terbuka (OpenAlex/Crossref) memakai kombinasi kata kunci berikut (contoh, gaya Scopus):

```
TITLE-ABS-KEY(
  ("remaining useful life" OR RUL OR prognos* OR "predictive maintenance" OR "failure prediction")
  AND (censored OR censoring OR "survival analysis" OR Weibull OR "time-to-event")
  AND ("deep learning" OR LSTM OR transformer OR "neural network" OR Bayesian)
)
TITLE-ABS-KEY(
  ("reverse osmosis" OR membrane* OR desalination OR "water treatment")
  AND ("remaining useful life" OR RUL OR fouling OR "predictive maintenance" OR "health index")
)
```
Snowballing (backward dan forward) diterapkan dari artikel kunci untuk menambah cakupan. Batas: artikel jurnal (article), berbahasa Inggris, terbit 2015–2026 (karya landamark pra-2015 dapat masuk melalui snowballing).

### 2.3 Kriteria Inklusi dan Eksklusi
Inklusi: studi peer-review yang membahas RUL/prognostics/survival analysis atau predictive maintenance membran/air; mendefinisikan target RUL/kegagalan; atau berkontribusi pada metode sadar-censoring, deep learning RUL, ketidakpastian, atau skala data. Eksklusi: studi medis/klinis (membran biologis), makalah tanpa abstrak, dan studi tanpa relevansi metodologis.

### 2.4 Penyaringan dan PRISMA 2020
Proses mengikuti alur PRISMA 2020 (identifikasi → penyaringan → kelayakan → disertakan). Angka lengkap disajikan pada Bagian 3.1.

### 2.5 Penilaian Kualitas
Setiap studi dinilai dengan checklist 10 butir (kejelasan RQ, validitas data, reproduksibilitas metode, kecukupan evaluasi, penanganan censoring, pelaporan ketidakpastian, keterkaitan keputusan, dll.), skala Ya/Sebagian/Tidak.

### 2.6 Ekstraksi Data dan Sintesis
Ekstraksi mengikuti form: No, Pilar/Tema, Judul, Penulis, Tahun, Jurnal, Klasifikasi, Link/DOI, Ringkasan Temuan, Kontribusi terhadap Research Gap. Sintesis dilakukan secara concept-centric memakai matriks konsep Webster & Watson (2002) dengan tujuh pilar (A–G) dan delapan dimensi konsep (D1–D8).

## 3. Hasil

### 3.1 Alur PRISMA
<!-- PRISMA -->

### 3.2 Sebaran Pilar
<!-- PILAR -->

### 3.3 Matriks Konsep (sebaran dimensi)
<!-- DIMENSI -->

<!-- TABLES -->

## 4. Sintesis dan Research Gap

### 4.1 Sintesis per Dimensi
<!-- SINTESIS -->

### 4.2 Research Gap
<!-- GAP -->

## 5. Diskusi

### 5.1 Implikasi
Peta literatur menunjukkan bahwa metode sadar-censoring untuk RUL sudah tersedia, tetapi aplikasinya pada membran RO sangat terbatas, dan asumsi armada besar (banyak kegagalan teramati) tidak selalu berlaku di plant pilot kecil. Oleh karena itu, kontribusi yang paling dapat dipertahankan bukan sekadar "menerapkan metode X ke domain Y", melainkan menangani rezim data yang justru dihindari literatur: censoring mendominasi dan jumlah kegagalan mendekati nol.

### 5.2 Agenda Riset
Agenda riset ke depan mencakup: (1) definisi endpoint proxy (soft failure) yang standar untuk membran RO; (2) metode identifikasi parameter survival yang jujur pada data all-censored (prior informatif, shape dikunci); (3) integrasi hasil RUL ke DSS perawatan berbasis biaya; dan (4) validasi lintas-plant pada armada replikasi.

### 5.3 Ancaman Validitas
Sebagian besar metode dievaluasi pada dataset benchmark mesin (C-MAPSS/bearing) dengan censoring disimulasi; transfer ke membran nyata belum teruji. Klasifikasi indeks Scopus pada korpus perlu diverifikasi pada laman resmi. Abstrak sebagai dasar ringkasan menimbulkan keterbatasan detail.

## 6. Kesimpulan
SLR ini menegaskan adanya celah nyata: belum ada studi yang menggabungkan prediksi RUL membran RO berbasis survival analysis sadar-censoring, kondisi data tanpa kegagalan, skala data kecil, dan integrasi DSS perawatan. Celah ini menjadi dasar penelitian tesis yang diusulkan.

## Daftar Pustaka (terpilih)
1. Gao, Y., Li, S., Wang, D., Mao, J., & Ouyang, L. (2025). A Neural Network-Based Survival Analysis Model Considering Censored Data for Failure Prediction. IEEE Transactions on Automation Science and Engineering. DOI 10.1109/TASE.2025.3640217.
2. Alshraideh, H., Al Ali, F., Awad, M., & Al-Othman, A. (2026). AI-based remaining useful life prediction of seawater desalination membranes. Chemical Engineering Journal Advances, 26, 101217. DOI 10.1016/j.ceja.2026.101217.
3. Noot, J.-P., Martin, M., & Birmelé, E. (2025). LSTM and Transformers based methods for Remaining Useful Life Prediction considering Censored Data. International Journal of Prognostics and Health Management, 16(2). DOI 10.36001/ijphm.2025.v16i2.4260.
4. Si, X.-S., Wang, W., Hu, C.-H., & Zhou, D.-H. (2011). Remaining Useful Life Estimation - A Review on the Statistical Data Driven Approaches. European Journal of Operational Research, 213(1), 1-14.
5. Kitchenham, B., & Charters, S. (2007). Guidelines for Performing Systematic Literature Reviews in Software Engineering. EBSE Technical Report.
6. Page, M. J., dkk. (2021). The PRISMA 2020 statement. BMJ, 372, n71.
7. Webster, J., & Watson, R. T. (2002). Analyzing the Past to Prepare for the Future: Writing a Literature Review. MIS Quarterly, 26(2), xiii-xxiii.
8. Wohlin, C. (2014). Guidelines for Snowballing in Systematic Literature Studies. EASE '14.
9. Drent, C., Kapodistria, S., & Boxma, O. J. (2020). Censored lifetime learning: Optimal Bayesian age-replacement policies. Operations Research Letters, 48(6), 827-834.
10. Li, C.-S., Taylor, J. M. G., & Sy, J. P. (2001). Identifiability of cure models. Statistics & Probability Letters, 54(4), 389-395.

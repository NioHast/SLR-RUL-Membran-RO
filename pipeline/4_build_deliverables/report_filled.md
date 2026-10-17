# Systematic Literature Review (SLR): Prediksi Remaining Useful Life (RUL) Membran Reverse Osmosis Berbasis Survival Analysis dan Deep Learning

## Abstrak

Tinjauan literatur sistematis ini memetakan metode prediksi sisa usia pakai (Remaining Useful Life, RUL) berbasis survival analysis dan deep learning, dengan perhatian khusus pada penanganan data tersensor (right-censored) dan keterbatasan data (small-data), serta penerapannya pada domain membran reverse osmosis (RO). Kajian mengikuti panduan Kitchenham dan Charters, pelaporan PRISMA 2020, sintesis concept-centric Webster dan Watson, serta snowballing Wohlin. Pencarian pada OpenAlex (16 query) mengidentifikasi 694 rekaman, yang setelah penyaringan menghasilkan 101 artikel yang dinilai kelayakannya, dengan 79 artikel lolos sebagai korpus sintesis. Dari korpus tersebut, 46 artikel tergolong Inti (31 Inti-Metode, 13 Inti-Domain, 2 Inti-Metode+Domain) dan 19 artikel ditetapkan sebagai core paper. Temuan utama: dimensi censoring (D3) dibahas 28 artikel, domain RO (D7) hanya 2 artikel, tetapi irisan keduanya nol artikel. Artinya, belum ada studi yang menangani data tersensor pada domain membran RO. Celah inilah yang menjadi dasar penelitian tesis.

## 1. Pendahuluan

### 1.1 Latar belakang dan urgensi

Membran reverse osmosis (RO) merupakan komponen inti pada instalasi desalinasi air payau maupun air laut. Kinerjanya menurun seiring waktu karena fouling, scaling, dan degradasi kimia, sehingga memerlukan perawatan berkala berupa Clean-in-Place (CIP) atau penggantian elemen membran. Keputusan yang terlambat menimbulkan penurunan kualitas permeat dan konsumsi energi yang membengkak, sedangkan penggantian yang terlalu dini membuang sisa umur pakai yang masih tersedia. Karena itu, prediksi RUL yang akurat memiliki nilai ekonomi dan operasional yang tinggi.

Persoalan mendasar muncul dari sifat data lapangan. Perawatan membran hampir selalu dilakukan secara preventif, yaitu sebelum terjadi kegagalan fisik total. Akibatnya, basis data pemantauan didominasi data tersensor kanan (right-censored): pengamatan berhenti karena penggantian preventif atau berakhirnya periode studi, tanpa pernah merekam waktu kegagalan sebenarnya. Metode prediksi RUL konvensional yang hanya belajar dari data run-to-failure membuang observasi tersensor ini dan karenanya menghasilkan estimasi yang bias (Gao dkk., 2025). Survival analysis menawarkan kerangka waktu-ke-kejadian yang secara eksplisit memanfaatkan data tersensor, sedangkan deep learning menawarkan kapasitas menangkap pola multi-sensor yang kompleks (Si dkk., 2011; Noot dkk., 2025).

Urgensi tinjauan ini muncul dari tiga ketegangan. Pertama, metode survival analysis dan deep learning sudah mapan untuk mesin berarmada besar seperti turbin, bearing, dan baterai, tetapi belum banyak diadopsi untuk membran RO. Kedua, di lapangan data membran justru berukuran kecil dan hampir tanpa kegagalan teramati, kondisi yang belum banyak diuji literatur. Ketiga, pemanfaatan hasil prediksi RUL untuk keputusan perawatan berbasis Sistem Pendukung Keputusan (DSS) belum menjadi fokus utama.

### 1.2 Rumusan masalah dan pertanyaan riset

Berdasarkan latar belakang tersebut, permasalahan penelitian dirumuskan sebagai berikut.

- RQ1: Bagaimana metode survival analysis menangani data tersensor pada prediksi RUL?
- RQ2: Bagaimana deep learning (LSTM, Transformer, Bayesian) meningkatkan prediksi RUL dan kuantifikasi ketidakpastian?
- RQ3: Kendala apa yang muncul pada kondisi data kecil (small-data) maupun tanpa kegagalan (all-censored), dan bagaimana solusinya?
- RQ4: Bagaimana hasil prediksi RUL digunakan dalam sistem pendukung keputusan perawatan (DSS/CMMS)?

### 1.3 Tujuan dan manfaat

Tujuan tinjauan ini adalah memetakan bukti metode RUL sadar-censoring, menilai kesiapan metode tersebut untuk domain membran RO, dan merumuskan celah penelitian yang dapat dipertanggungjawabkan. Manfaatnya: secara teoretis menyediakan peta taksonomi dan matriks konsep; secara praktis menjadi dasar perancangan model prediksi RUL membran; secara metodologis memberikan prosedur pemilihan paper inti yang transparan dan dapat direproduksi.

### 1.4 Kontribusi

Kontribusi tinjauan ini ada tiga. Pertama, peta taksonomi metode prediksi RUL dengan fokus censoring dan keterbatasan data. Kedua, matriks konsep yang menunjukkan sebaran dimensi riset pada korpus. Ketiga, perumusan research gap yang menjadi dasar usulan penelitian tesis, yaitu prediksi RUL membran RO berbasis survival analysis sadar-censoring pada rezim data kecil.

### 1.5 Ruang lingkup dan batasan

Tinjauan mencakup artikel jurnal dan prosiding berbahasa Inggris pada rentang 2015 sampai 2026, dengan karya landamark pra-2015 dapat masuk melalui snowballing. Domain utama adalah RUL, prognostik, survival analysis, dan predictive maintenance, dengan penekanan pada keterkaitannya dengan membran RO dan desalinasi. Tinjauan tidak mencakup studi medis/klinis (membran biologis) dan tidak melakukan meta-analisis kuantitatif karena heterogenitas studi.

## 2. Metode Tinjauan

### 2.1 Protokol dan pedoman

Protokol disusun sebelum pencarian agar proses dapat diaudit dan direproduksi. Prosedur mengikuti Kitchenham dan Charters (2007), pelaporan alur seleksi mengikuti PRISMA 2020 (Page dkk., 2021), sintesis concept-centric mengikuti Webster dan Watson (2002), dan penelusuran lanjutan mengikuti Wohlin (2014).

{{FIG:fig02_slr_process.png|Alur metode SLR: protokol, pencarian, penyaringan, ekstraksi, sintesis, dan pelaporan|15}}

### 2.2 PICOC

- Population: sistem membran RO dan mesin industri yang menyelenggarakan prognostik.
- Intervention: metode survival analysis dan deep learning untuk RUL.
- Comparison: metode RUL konvensional berbasis regresi dan data run-to-failure.
- Outcome: akurasi RUL, kualitas kuantifikasi ketidakpastian, dan kelayakan keputusan perawatan.
- Context: plant industri maupun pilot, dengan perhatian pada rezim data tersensor dan skala data kecil.

### 2.3 Strategi pencarian

Pencarian hybrid memadukan pencarian basis data dan snowballing (Wohlin, 2014). Eksekusi korpus ini menggunakan OpenAlex (metadata Crossref) dengan 16 query title+abstract, filter type=article dan has_doi=true, diambil 50 hasil teratas per query. Snowballing backward dan forward diterapkan dari artikel inti. Protokol juga memuat string Scopus untuk replikasi (Lampiran B). Batas recall yang disadari: tanpa paginasi dan tanpa filter tahun di API, sehingga penyaringan tahun dilakukan pada tahap screening.

### 2.4 Kriteria inklusi dan eksklusi

Studi diinklusikan bila merupakan publikasi peer-review yang membahas RUL, prognostik, survival analysis, atau predictive maintenance pada domain membran/air; mendefinisikan target RUL atau kegagalan; atau berkontribusi pada metode sadar-censoring, deep learning RUL, kuantifikasi ketidakpastian, maupun skala data. Studi dieksklusi bila bersifat medis/klinis, tidak memiliki abstrak, tidak relevan secara metodologis, atau berada di luar rentang tahun tanpa alasan snowballing.

### 2.5 Seleksi dan PRISMA

Proses seleksi mengikuti alur identifikasi, penyaringan judul/abstrak, penilaian kelayakan full-record, dan penyertaan akhir. Angka final disajikan pada Bagian 3.1. Seluruh eksklusi dan substitusi dicatat pada lampiran log agar dapat diaudit.

### 2.6 Ekstraksi data

Ekstraksi mengikuti formulir terstruktur: nomor, pilar/tema, judul, penulis, tahun, jurnal, klasifikasi, tautan/DOI, ringkasan temuan, dan kontribusi terhadap research gap. Setiap artikel juga diberi penanda dimensi D1 sampai D8 beserta bukti pendukungnya.

### 2.7 Penilaian kualitas

Setiap studi dinilai dengan checklist sepuluh butir (kejelasan RQ, validitas data, reproduksibilitas metode, kecukupan evaluasi, penanganan censoring, pelaporan ketidakpastian, keterkaitan keputusan, dan seterusnya) dengan skala Ya/Sebagian/Tidak. Skor akhir dinormalisasi ke skala 0 sampai 10.

### 2.8 Sintesis

Sintesis dilakukan secara concept-centric menggunakan matriks konsep Webster dan Watson dengan tujuh pilar (A sampai G) dan delapan dimensi konsep (D1 sampai D8). Karena studi heterogen, sintesis bersifat naratif (SWiM-like) dan tidak melakukan pooling efek kuantitatif.

### 2.9 Ancaman validitas

Tiga ancaman validitas dicatat. Pertama, validitas internal: sebagian besar metode dievaluasi pada benchmark mesin dengan censoring disimulasikan, sehingga transfer ke membran nyata belum tentu berlaku. Kedua, validitas konstruk: penentuan pilar dan dimensi bergantung pada penilaian peneliti. Ketiga, validitas eksternal: sebagian ringkasan bersumber dari abstrak, sehingga detail metodologis halus berpotensi tidak tertangkap.

## 3. Hasil

### 3.1 Alur PRISMA dan korpus final

Pencarian mengidentifikasi 694 rekaman unik. Sebanyak 209 rekaman tanpa abstrak atau metadata tidak lengkap dikeluarkan sebelum penyaringan, menyisakan 485 rekaman yang disaring pada judul dan abstrak. Dari tahap ini diperoleh 72 artikel yang layak, lalu ditambah 29 artikel dari snowballing dan penggantian Open Access. Seluruh 101 artikel dinilai kelayakannya; 22 artikel dikeluarkan pada tahap eligibilitas (15 topik di luar RUL/prognostik, 6 review, 1 domain) sehingga 79 artikel menjadi korpus sintesis.

{{FIG:fig01_prisma_flow.png|Alur PRISMA 2020 dan komposisi korpus final (n = 79 included)|13}}

| Tahap | Jumlah |
| --- | --- |
| Identifikasi (record unik) | 694 |
| Dihapus sebelum penyaringan (tanpa abstrak/metadata) | 209 |
| Disaring judul/abstrak | 485 |
| Dikeluarkan pada judul/abstrak | 413 |
| Layak dari pencarian basis data | 72 |
| Ditambah: snowballing + pengganti OA | 29 |
| Dinilai pada full-text | 101 |
| Dikeluarkan pada full-text | 0 |
| Termasuk dalam sintesis | 79 |
| Core paper (skor >= 5.5 atau gap) | 19 |

### 3.2 Sebaran pilar

Korpus terbagi ke dalam tujuh pilar tematik. Pilar survival analysis dan censored data (A) serta deep learning RUL (B) masing-masing mencakup 24 artikel, diikuti Bayesian/uncertainty (C) dengan 15 artikel dan small-data/transfer (D) 9 artikel. Pilar DSS/predictive maintenance (F) mencakup 6 artikel, sedangkan domain membran/RO (E) hanya 1 artikel karena studi domain yang murni fouling/performance dikeluarkan pada gate topik; konteks Indonesia (G) tidak tersisa pada korpus sintesis.

{{FIG:fig07_pillar_distribution.png|Sebaran artikel per pilar A sampai G (n = 79 included)|14}}

| Pilar/Tema | Jumlah Artikel |
| --- | --- |
| A. Survival Analysis & Censored Data | 24 |
| B. Deep Learning RUL | 24 |
| C. Bayesian & Uncertainty | 15 |
| D. Small-data/Transfer/Hierarchical | 9 |
| E. Membrane/RO/Desalination | 1 |
| F. DSS & Predictive Maintenance (IS) | 6 |

### 3.3 Matriks konsep dan sebaran dimensi

Matriks konsep menunjukkan sebaran yang tidak merata. Dimensi target/kegagalan (D2) dibahas 79 artikel, arsitektur model (D4) 76 artikel, dan data/sensor (D1) 73 artikel. Dimensi ketidakpastian (D5) dibahas 43 artikel, skala data (D8) 31 artikel, censoring (D3) 28 artikel, keputusan/DSS (D6) 21 artikel, dan domain RO (D7) hanya 2 artikel. Meskipun D3 bukan dimensi paling tipis secara absolut, D3 justru paling kritis karena merupakan inti persoalan data membran.

{{FIG:fig08_dimension_coverage.png|Cakupan dimensi konsep D1 sampai D8 (n = 79 included)|14}}

| Dimensi Konsep | Jumlah Artikel | / Total |
| --- | --- | --- |
| D1 Data/Sensor | 73 | /79 |
| D2 Target/Failure | 79 | /79 |
| D3 Censoring | 28 | /79 |
| D4 Arsitektur Model | 76 | /79 |
| D5 Ketidakpastian | 43 | /79 |
| D6 Keputusan/DSS | 21 | /79 |
| D7 Domain RO/Membran | 2 | /79 |
| D8 Skala Data | 31 | /79 |

{{FIG:fig10_pillar_dimension_heatmap.png|Matriks konsep Webster-Watson: irisan pilar dan dimensi (jumlah artikel)|15}}

### 3.4 Penentuan paper inti dan core paper

Untuk menjawab kebutuhan praktis tesis, korpus 79 artikel dipilah menjadi basis bukti bertingkat. Sebanyak 46 artikel tergolong Inti (31 Inti-Metode, 13 Inti-Domain, 2 Inti-Metode+Domain), 31 Pendukung, dan 2 Konteks. Dengan rubrik skor 0 sampai 6 (relevansi RQ, kedekatan metodologis, kualitas), ditetapkan 19 core paper yang menjadi sumber utama model.

{{FIG:fig09_tier_funnel.png|Penyaringan korpus dan penentuan 19 core paper|13}}

| No | Tahun | Jurnal | Judul | Tier | Skor |
| --- | --- | --- | --- | --- | --- |
| 11 | 2025 | IEEE Transactions on Automation Science  | A Neural Network-Based Survival Analysis Model Considering Censored Data for Fai | Inti-Metode | 6.0 |
| 12 | 2025 | International Journal of Prognostics and | LSTM and Transformers based methods for Remaining Useful Life Prediction conside | Inti-Metode | 6.0 |
| 13 | 2026 | Sensors | Survival Models for Predictive Maintenance and Remaining Useful Life in Sensor-E | Inti-Metode | 6.0 |
| 48 | 2019 | International Journal of Prognostics and | Data-driven Prognostics with Predictive Uncertainty Estimation using Ensemble of | Inti-Metode | 6.0 |
| 64 | 2020 | Shock and Vibration | General Log-Linear Weibull Model Combining Vibration and Temperature Characteris | Inti-Metode | 6.0 |
| 4 | 2016 | Reliability Engineering & System Safety | Remaining useful life estimation in heterogeneous fleets working under variable  | Inti-Metode | 5.6 |
| 17 | 2026 | IEEE Sensors Letters | A Multisensor Cross-Modal Attention Framework for Weibull-Driven RUL Estimation  | Inti-Metode | 5.6 |
| 19 | 2022 | Neural Computing and Applications | Weibull recurrent neural networks for failure prognosis using histogram data | Inti-Metode | 5.6 |
| 9 | 2026 | Scientific Reports | Survival-analysis-guided machine learning for failure and remaining-useful-life  | Inti-Metode | 5.5 |
| 35 | 2022 | IEEE Transactions on Instrumentation and | Domain Adaptive Remaining Useful Life Prediction With Transformer | Inti-Domain | 5.5 |
| 54 | 2025 | Data & Metadata | Reliable prediction of industrial components Remaining Useful Life using Cox and | Inti-Metode | 5.5 |
| 75 | 2019 | Decision Support Systems | Forecasting remaining useful life: Interpretable deep learning approach via vari | Inti-Metode | 5.5 |
| 76 | 2025 | Journal of Advanced Mechanical Design Sy | A physical knowledge-guided and data-driven framework for remaining useful life  | Inti-Metode | 5.5 |
| 78 | 2025 | Green Energy and Intelligent Transportat | A physics-informed neural network-based method for predicting degradation trajec | Inti-Domain | 5.5 |
| 89 | 2026 | Quality and Reliability Engineering Inte | Weibull Variational Autoencoder for Remaining Useful Life Prediction | Inti-Metode | 5.5 |
| 92 | 2020 | Wireless Communications and Mobile Compu | Developing Deep Survival Model for Remaining Useful Life Estimation Based on Con | Inti-Metode | 5.5 |
| 99 | 2023 | Machines (MDPI), 11(2):163, ISSN 2075-17 | Explainable Data-Driven Method Combined with Bayesian Filtering for Remaining Us | Inti-Domain | 5.5 |
| 68 | 2026 | IEEE Transactions on Instrumentation and | Multisensor Time Series Forecasting-Based Augmentation Framework for Remaining U | Inti-Metode+Domain | 4.2 |
| 81 | 2022 | IEEE Transactions on Industry Applicatio | Probabilistic Modeling of Li-Ion Battery Remaining Useful Life | Inti-Metode+Domain | 3.8 |

### 3.5 Kualitas studi

Skor kualitas studi berkisar 4 sampai 9 dari 10, dengan mayoritas berada pada rentang 6 sampai 8. Sebaran ini menunjukkan bahwa korpus cukup matang secara metodologis, tetapi belum merata pada aspek pelaporan ketidakpastian dan penanganan censoring.

{{FIG:fig12_quality_distribution.png|Sebaran skor kualitas studi (n = 79 included)|12}}

### 3.6 Tren publikasi

Publikasi meningkat setelah 2018 seiring meluasnya deep learning untuk prognostik, dengan puncak pada beberapa tahun terakhir. Tren ini menegaskan bahwa bidangnya aktif, tetapi belum terkonsentrasi pada domain membran.

{{FIG:fig11_year_trend.png|Tren publikasi korpus 2015 sampai 2026|14}}

## 4. Sintesis dan Research Gap

### 4.1 Sintesis per dimensi

- **D1 Data/Sensor**: Literatur RUL umumnya memakai data multi-sensor deret waktu (vibrasi, suhu, tekanan, arus). Pada domain membran/RO, sinyal kunci adalah beda tekanan transmembran (TMP/delta-P), laju alir permeate, konduktivitas/TDS, suhu umpan, dan pH. Artinya, sensor yang dibutuhkan tesis ini sudah mapan di literatur. (73/79 artikel)
- **D2 Target/Failure**: Definisi target terbelah dua: (a) sebagian studi memakai kegagalan fisik (data run-to-failure seperti C-MAPSS/bearing), (b) sebagian mendefinisikan target sebagai ambang performa/health index (soft failure). Untuk membran yang jarang dibiarkan rusak total, pendekatan (b) lebih relevan dan lebih realistis. (79/79 artikel)
- **D3 Censoring**: Kelompok survival analysis dan sejumlah metode deep learning modern secara eksplisit menangani data tersensor. Namun mayoritas metode DL untuk RUL masih mengabaikan censoring dan dilatih hanya pada data lengkap, sehingga bias. Ini celah metodologis utama. (28/79 artikel)
- **D4 Arsitektur Model**: Arsitektur didominasi LSTM, CNN-LSTM, dan Transformer untuk deret waktu, serta Bayesian Neural Network untuk probabilistik; pendekatan survival klasik (Cox, Weibull/AFT) tetap dipakai untuk pemodelan waktu-ke-kejadian. (76/79 artikel)
- **D5 Ketidakpastian**: Model probabilistik/Bayesian menyediakan kuantifikasi ketidakpastian (interval prediksi), sedangkan model deterministik umumnya hanya mengeluarkan satu angka RUL. Untuk keputusan perawatan, ketidakpastian penting. (43/79 artikel)
- **D6 Keputusan/DSS**: Hanya sebagian kecil studi menghubungkan prediksi RUL ke keputusan perawatan (penjadwalan, biaya). Justru di sinilah kontribusi Sistem Informasi (DSS/CMMS) berada. (21/79 artikel)
- **D7 Domain RO/Membran**: Domain membran/RO/desalinasi jauh lebih sedikit dibanding mesin/bearing/baterai. Prediksi RUL membran masih tipis; sebagian besar berupa prediksi fouling atau performa, bukan RUL dengan survival analysis. (2/79 artikel)
- **D8 Skala Data**: Sangat sedikit studi yang secara khusus menangani data kecil (small-data), few-shot, transfer learning, atau kondisi tanpa kegagalan; mayoritas berasumsi armada besar dengan banyak kegagalan teramati. (31/79 artikel)

### 4.2 Research gap

Dari 101 artikel yang diekstraksi, tidak satu pun secara simultan menggabungkan: (1) prediksi RUL membran reverse osmosis dengan survival analysis yang sadar-censoring; (2) kondisi data tanpa kegagalan (penggantian preventif sebelum rusak) sehingga censoring mendominasi; (3) skala data kecil pada satu plant pilot; dan (4) integrasi hasilnya ke dalam sistem pendukung keputusan perawatan. Kombinasi inilah yang menjadi kontribusi tesis.

Catatan kuantitatif: D3 dibahas 28 artikel dan D7 dibahas 2 artikel, tetapi irisan D3 dan D7 berjumlah 0 artikel.

Temuan kunci yang memperkuat gap: dari 79 artikel included, 28 artikel membahas censoring (D3) dan 2 artikel membahas domain RO (D7), tetapi tidak ada satu pun artikel yang membahas keduanya secara bersamaan. Dengan kata lain, irisan D3 dan D7 berjumlah nol. Ini berarti rezim data yang paling relevan di lapangan, yaitu data tersensor pada membran RO, justru belum pernah diteliti secara langsung.

## 5. Diskusi

### 5.1 Implikasi

Peta literatur menunjukkan bahwa metode sadar-censoring untuk RUL sudah tersedia, tetapi aplikasinya pada membran RO sangat terbatas, dan asumsi armada besar tidak selalu berlaku di plant pilot kecil. Kontribusi yang paling dapat dipertahankan bukan sekadar menerapkan metode tertentu ke domain tertentu, melainkan menangani rezim data yang justru dihindari literatur: censoring mendominasi dan jumlah kegagalan mendekati nol.

### 5.2 Agenda riset

Agenda riset ke depan mencakup: definisi endpoint proxy (soft failure) yang standar untuk membran RO; metode identifikasi parameter survival yang jujur pada data all-censored (prior informatif, bentuk dikunci); integrasi hasil RUL ke DSS perawatan berbasis biaya; dan validasi lintas-plant pada armada replikasi.

### 5.3 Keterbatasan tinjauan

Tinjauan ini menggunakan OpenAlex sebagai sumber utama, sehingga artikel yang hanya terindeks di Scopus atau WoS berpotensi tidak tertangkap. Pengambilan 50 hasil teratas per query juga membatasi recall. Selain itu, sebagian ringkasan bersumber dari abstrak. Keterbatasan ini dicatat sebagai ancaman validitas dan menjadi dasar replikasi pada basis data berlangganan.

## 6. Kesimpulan

SLR ini menegaskan adanya celah penelitian yang nyata. Kerangka survival analysis untuk data tersensor dan kapasitas deep learning untuk pemodelan deret waktu telah matang, tetapi konvergensinya pada domain membran reverse osmosis masih sangat terbatas. Dimensi censoring dibahas 28 artikel dan domain RO hanya 2 artikel, namun irisan keduanya nol. Belum ada studi yang secara simultan menggabungkan prediksi RUL membran RO sadar-censoring, kondisi data tanpa kegagalan, skala data kecil, dan integrasi DSS perawatan. Celah inilah yang menjadi dasar penelitian tesis yang diusulkan.

## Daftar Pustaka

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

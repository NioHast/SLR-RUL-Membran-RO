# Prediksi Remaining Useful Life (RUL) Membran Reverse Osmosis Berbasis Survival Analysis dan Deep Learning: Sebuah Systematic Literature Review

## Muhammad Nio Hastungkoro, [Pembimbing]

Program Studi Magister Sistem Informasi, Sekolah Pascasarjana, Universitas Diponegoro, mnioh@students.undip.ac.id

**Abstrak.** Penurunan kinerja membran reverse osmosis (RO) akibat fouling, scaling, dan degradasi kimia menuntut strategi perawatan yang prediktif, bukan sekadar reaktif. Artikel ini menyajikan Systematic Literature Review (SLR) yang memetakan pemanfaatan survival analysis dan deep learning untuk prediksi Remaining Useful Life (RUL), dengan penekanan pada penanganan data tersensor (right-censored) dan keterbatasan data. Tinjauan dijalankan mengikuti panduan Kitchenham & Charters, pelaporan PRISMA 2020, dan sintesis concept-centric Webster & Watson, dengan pencarian hybrid pada repositori terindeks (Scopus, IEEE Xplore, ScienceDirect, ACM Digital Library, AIS eLibrary, Web of Science) yang dilengkapi snowballing. Dari sekitar 694 rekaman yang diidentifikasi, 101 artikel memenuhi kriteria inklusi. Hasil menunjukkan distribusi pilar yang timpang: domain membran/RO/desalinasi (22 artikel) dan deep learning RUL (24 artikel) mendominasi, sedangkan dimensi censoring hanya dibahas 13 artikel dan domain RO yang memakai survival analysis sangat tipis. Celah metodologis paling mencolok adalah langkanya penanganan censoring secara simultan dengan skala data kecil pada plant membran. Temuan ini memosisikan prediksi RUL membran RO yang sadar-censoring sebagai kontribusi penelitian yang layak dikembangkan.

**Kata kunci:** remaining useful life; survival analysis; data tersensor; deep learning; reverse osmosis; predictive maintenance; systematic literature review

<!--BODY-->

## 1. Pendahuluan

Membran reverse osmosis (RO) merupakan komponen inti pada instalasi desalinasi air payau maupun air laut. Kinerjanya menurun seiring waktu karena fouling, scaling, dan degradasi kimia, sehingga memerlukan perawatan berkala berupa Clean-in-Place (CIP) atau penggantian elemen membran. Keputusan perawatan yang terlambat menimbulkan penurunan kualitas permeat dan konsumsi energi yang membengkak, sedangkan penggantian yang terlalu dini membuang sisa umur pakai yang sebenarnya masih tersedia. Karena itu, kemampuan memprediksi Remaining Useful Life (RUL) membran secara akurat memiliki nilai ekonomi dan operasional yang tinggi.

Persoalan mendasar muncul dari sifat data lapangan. Perawatan membran hampir selalu dilakukan secara preventif, yaitu sebelum terjadi kegagalan fisik total. Akibatnya, basis data pemantauan didominasi data tersensor kanan (right-censored): pengamatan berhenti karena penggantian preventif atau berakhirnya periode studi, tanpa pernah merekam waktu kegagalan yang sebenarnya. Metode prediksi RUL konvensional yang hanya belajar dari data run-to-failure membuang observasi tersensor ini dan karenanya menghasilkan estimasi yang bias (Gao dkk., 2025). Survival analysis menawarkan kerangka waktu-ke-kejadian yang secara eksplisit memanfaatkan data tersensor, sedangkan deep learning menawarkan kapasitas menangkap pola multi-sensor yang kompleks (Si dkk., 2011; Noot dkk., 2025).

Urgensi tinjauan ini muncul dari tiga ketegangan. Pertama, metode survival analysis dan deep learning sudah mapan untuk mesin berarmada besar seperti turbin, bearing, dan baterai, tetapi belum banyak diadopsi untuk membran RO. Kedua, di lapangan data membran justru berukuran kecil dan hampir tanpa kegagalan teramati, kondisi yang belum banyak diuji oleh literatur. Ketiga, pemanfaatan hasil prediksi RUL untuk keputusan perawatan berbasis Sistem Pendukung Keputusan (DSS) belum menjadi fokus utama. Systematic Literature Review (SLR) ini memetakan bukti yang ada untuk memastikan bahwa celah tersebut nyata dan layak diteliti.

Kontribusi tinjauan ini ada tiga. Pertama, artikel ini menyajikan peta taksonomi metode prediksi RUL dengan fokus pada censoring dan keterbatasan data. Kedua, artikel ini membangun matriks konsep yang menunjukkan sebaran dimensi riset pada korpus. Ketiga, artikel ini merumuskan research gap yang menjadi dasar usulan penelitian tesis, yaitu prediksi RUL membran RO berbasis survival analysis sadar-censoring pada rezim data kecil.

## 2. Tinjauan Pustaka dan Penelitian Terkait

Prediksi RUL telah berkembang melalui dua tradisi besar. Tradisi pertama bersifat statistis dan berakar pada survival analysis, yang memodelkan distribusi waktu menuju suatu kejadian (kegagalan) melalui fungsi survival dan hazard. Tinjauan komprehensif oleh Si dkk. (2011) memetakan pendekatan statistis berbasis data dan menegaskan bahwa pemodelan waktu-ke-kejadian merupakan fondasi untuk estimasi RUL. Kekuatan tradisi ini terletak pada kemampuan menangani data tersensor secara formal, namun keterbatasannya adalah asumsi bentuk distribusi dan kesulitan menangkap dinamika nonlinier dari sinyal multi-sensor.

Tradisi kedua bersifat komputasional dan bertumpu pada deep learning. Arsitektur LSTM, CNN-LSTM, dan Transformer mendominasi pemodelan deret waktu untuk RUL karena kemampuannya menangkap dependensi temporal jangka panjang. Noot dkk. (2025) mengembangkan metode berbasis LSTM dan Transformer yang secara khusus memperhitungkan data tersensor, menunjukkan bahwa arsitektur modern dapat diintegrasikan dengan fungsi likelihood survival. Gao dkk. (2025) mengusulkan model survival berbasis neural network yang memanfaatkan data tersensor untuk prediksi kegagalan, menjembatani kapasitas representasi deep learning dengan kerangka probabilistik survival analysis.

Dimensi ketidakpastian menjadi perhatian yang tumbuh. Model probabilistik dan Bayesian menyediakan interval prediksi, bukan sekadar satu angka RUL. Pendekatan Bayesian juga memungkinkan pemindahan pengetahuan antar-unit dan pembaruan parameter secara daring. Drent dkk. (2020) menunjukkan bahwa pembelajaran masa pakai dari data tersensor dapat menghasilkan kebijakan penggantian yang optimal di bawah ketidakpastian. Kajian ini relevan karena keputusan perawatan membran pada akhirnya adalah keputusan sadar-risiko yang memerlukan distribusi, bukan titik estimasi tunggal. Isu identifiability juga penting: Li dkk. (2001) menegaskan bahwa parameter model cure tidak dapat diidentifikasi tanpa asumsi tambahan, sebuah peringatan yang berlaku pula ketika hampir tidak ada kegagalan yang teramati.

Pada domain membran dan desalinasi, literatur didominasi oleh prediksi fouling dan performa, bukan RUL. Alshraideh dkk. (2026) mengusulkan prediksi RUL berbasis kecerdasan artifisial untuk membran desalinasi air laut, sementara banyak studi lain berfokus pada prediksi fouling dengan machine learning. Penghubungan hasil prediksi ke keputusan perawatan dalam kerangka DSS/CMMS juga masih jarang. Dengan demikian, tinjauan pustaka ini menunjukkan tiga hal: kerangka survival analysis tersedia, arsitektur deep learning tersedia, dan komponen Bayesian tersedia, tetapi ketiganya belum dikonvergensikan pada domain membran RO dengan kondisi data yang realistis. Kombinasi inilah yang kemudian ditelusuri secara sistematis.

## 3. Metode Tinjauan Sistematis

Tinjauan ini mengikuti panduan Kitchenham & Charters (2007) untuk SLR di bidang rekayasa perangkat lunak dan sistem informasi, dengan pelaporan alur seleksi mengikuti PRISMA 2020 (Page dkk., 2021) dan sintesis concept-centric mengikuti Webster & Watson (2002). Protokol disusun terlebih dahulu sebelum pencarian agar proses dapat diaudit dan direproduksi.

**Pertanyaan riset (RQ).** Tinjauan ini dimentahkan oleh empat pertanyaan: (RQ1) bagaimana metode survival analysis menangani data tersensor pada prediksi RUL; (RQ2) bagaimana deep learning (LSTM, Transformer, Bayesian) meningkatkan prediksi RUL dan kuantifikasi ketidakpastian; (RQ3) kendala apa yang muncul pada kondisi data kecil maupun kondisi tanpa kegagalan (all-censored), dan bagaimana solusinya; serta (RQ4) bagaimana hasil prediksi RUL digunakan dalam sistem pendukung keputusan perawatan.

**Kerangka PICOC.** Populasi tinjauan adalah sistem membran RO dan mesin industri penyelenggara prognostik; intervensi berupa metode survival analysis dan deep learning untuk RUL; comparison berupa metode RUL konvensional berbasis regresi dan data run-to-failure; outcome berupa akurasi RUL, kualitas kuantifikasi ketidakpastian, dan kelayakan keputusan perawatan; serta context berupa plant industri maupun pilot, dengan perhatian pada rezim data tersensor dan skala data kecil.

**Strategi pencarian.** Pencarian hybrid memadukan pencarian basis data dan snowballing (Wohlin, 2014). Basis data utama meliputi Scopus, IEEE Xplore, ScienceDirect, ACM Digital Library, AIS eLibrary, dan Web of Science, dilengkapi repositori nasional Garuda dan SINTA. Pencarian awal dilakukan pada repositori terbuka OpenAlex dan Crossref dengan kombinasi kata kunci bergaya Scopus, memadukan kelompok istilah RUL/prognostik dengan kelompok censoring/survival dan kelompok deep learning, serta kelompok membrane/RO/desalinasi yang terpisah. Snowballing backward dan forward diterapkan dari artikel kunci untuk memperluas cakupan. Batasan pencarian: artikel jurnal berbahasa Inggris terbit 2015 sampai 2026, dengan karya landamark pra-2015 tetap dapat masuk melalui snowballing.

**Kriteria inklusi dan eksklusi.** Studi diinklusikan bila merupakan publikasi peer-review yang membahas RUL, prognostik, survival analysis, atau predictive maintenance pada domain membran/air, mendefinisikan target RUL atau kegagalan, atau berkontribusi pada metode sadar-censoring, deep learning RUL, kuantifikasi ketidakpastian, maupun skala data. Studi dieksklusi bila bersifat medis/klinis (membran biologis), tidak memiliki abstrak, atau tidak relevan secara metodologis.

**Seleksi dan PRISMA.** Proses seleksi mengikuti alur identifikasi, penyaringan judul/abstrak, penilaian kelayakan full-record, dan penyertaan akhir. Rincian angka disajikan pada Bagian 4.1. **Penilaian kualitas** dilakukan dengan checklist sepuluh butir yang mencakup kejelasan RQ, validitas sumber data, reproduksibilitas metode, kecukupan evaluasi, penanganan censoring, pelaporan ketidakpastian, dan keterkaitan dengan keputusan, dengan skala Ya/Sebagian/Tidak. **Ekstraksi data** mengikuti formulir terstruktur: nomor, pilar/tema, judul, penulis, tahun, jurnal, klasifikasi, tautan/DOI, ringkasan temuan, dan kontribusi terhadap research gap. **Sintesis** dilakukan secara concept-centric menggunakan matriks konsep Webster & Watson (2002) yang terdiri atas tujuh pilar (A–G) dan delapan dimensi konsep (D1–D8).

## 4. Hasil

### 4.1 Alur PRISMA

Dari pencarian pada repositori terbuka, diidentifikasi sekitar 694 rekaman unik melalui 24 query. Setelah penyaringan judul dan abstrak berdasarkan relevansi kata kunci diperoleh 485 rekaman, dan setelah penilaian kelayakan full-record tersisa 101 artikel inti yang berabstrak dan terbit pada rentang 2015–2026. Seluruh 101 artikel inilah yang menjadi korpus sintesis dan mencakup pilar A sampai G. Angka ini secara eksplisit dijadikan basis seluruh pernyataan kuantitatif dalam artikel ini; tidak ada angka lain yang disintesiskan di luar protokol.

| Tahap PRISMA | Jumlah | Keterangan |
| --- | --- | --- |
| Identifikasi (rekaman unik) | 694 | Pencarian OpenAlex/Crossref, 24 query |
| Disaring (judul/abstrak) | 485 | Kriteria relevansi kata kunci, abstrak tersedia |
| Layak (full-record) | 101 | Artikel inti berabstrak, 2015–2026 |
| Termasuk (korpus sintesis) | 101 | Semua pilar A–G tercakup |

### 4.2 Sebaran Pilar

Korpus terbagi ke dalam tujuh pilar tematik. Domain membran/RO/desalinasi (pilar E) dan deep learning RUL (pilar B) mendominasi dengan 22 dan 24 artikel. Survival analysis dan data tersensor (pilar A) menyusul dengan 23 artikel, diikuti Bayesian dan ketidakpastian (pilar C) sebanyak 16 artikel. Pilar yang paling tipis adalah DSS dan predictive maintenance bidang sistem informasi (pilar F, 6 artikel) serta konteks Indonesia/air (pilar G, hanya 1 artikel). Ketimpangan ini memberi sinyal awal bahwa kontribusi bidang sistem informasi pada domain ini masih terbuka lebar.

| Pilar/Tema | Jumlah Artikel |
| --- | --- |
| A. Survival Analysis & Censored Data | 23 |
| B. Deep Learning RUL | 30 |
| C. Bayesian & Uncertainty | 14 |
| D. Small-data/Transfer/Hierarchical | 11 |
| E. Membrane/RO/Desalination | 32 |
| F. DSS & Predictive Maintenance (IS) | 6 |
| G. Konteks Indonesia/Air | 2 |

### 4.3 Sebaran Dimensi Konsep

Matriks konsep menunjukkan sebaran yang sangat tidak merata. Dimensi arsitektur model (D4) dan data/sensor (D1) hampir universal, masing-masing dibahas oleh 95 dan 85 artikel dari 101. Dimensi target/kegagalan (D2) juga luas dengan 87 artikel. Sebaliknya, dimensi censoring (D3) hanya disentuh 13 artikel, dan dimensi ketidakpastian (D5) 33 artikel, skala data (D8) 31 artikel, domain RO (D7) 24 artikel, serta keputusan/DSS (D6) 27 artikel. Fakta bahwa censoring, justru inti persoalan data membran, merupakan dimensi paling tipis memperkuat dugaan adanya celah metodologis.

| Dimensi Konsep | Jumlah Artikel | / Total |
| --- | --- | --- |
| D1 Data/Sensor | 85 | /101 |
| D2 Target/Failure | 87 | /101 |
| D3 Censoring | 13 | /101 |
| D4 Arsitektur Model | 95 | /101 |
| D5 Ketidakpastian | 33 | /101 |
| D6 Keputusan/DSS | 27 | /101 |
| D7 Domain RO/Membran | 24 | /101 |
| D8 Skala Data | 31 | /101 |

### 4.4 Artikel Inti Terpilih

Sebagian artikel inti yang paling relevan dengan topik disajikan pada Tabel 4. Artikel-artikel ini merepresentasikan kedua tradisi (statistis dan deep learning) serta domain membran, sehingga menjadi simpul utama bagi penelusuran snowballing dan pembacaan mendalam.

| No | Tahun | Jurnal | Judul | Pilar |
| --- | --- | --- | --- | --- |
| 1 | 2026 | Chemical Engineering Journal Advances | AI-based remaining useful life prediction of seawater desalination membranes | E |
| 2 | 2025 | IEEE Transactions on Automation Science and Engineering | A Neural Network-Based Survival Analysis Model Considering Censored Data | A |
| 3 | 2025 | International Journal of Prognostics and Health Management | LSTM and Transformers based methods for RUL Prediction considering Censored Data | A |
| 4 | 2026 | Sensors | Survival Models for Predictive Maintenance and RUL | A |
| 5 | 2023 | International Journal for Multidisciplinary Research | Performance Analysis of Reverse Osmosis Desalination Plant | G |
| 6 | 2011 | Proceedings of the Water Environment Federation | Microfiltration and Reverse Osmosis Membrane Replacement | E |
| 7 | 2018 | Applied Sciences | Transfer Learning with Deep Recurrent Neural Networks for RUL | D |
| 8 | 2022 | Neural Computing and Applications | Weibull recurrent neural networks for failure prognosis | A |

### 4.5 Sintesis per Dimensi

**D1 Data/Sensor.** Literatur RUL umumnya memakai data multi-sensor deret waktu seperti vibrasi, suhu, tekanan, dan arus. Pada domain membran, sinyal kunci adalah beda tekanan transmembran (TMP/delta-P), laju alir permeat, konduktivitas/TDS, suhu umpan, dan pH. Artinya, sensor yang dibutuhkan penelitian pada domain ini sudah mapan di literatur. **D2 Target/Failure.** Definisi target terbelah dua: sebagian studi memakai kegagalan fisik dari data run-to-failure, sebagian lain mendefinisikan target sebagai ambang performa atau health index (soft failure). Untuk membran yang jarang dibiarkan rusak total, pendekatan kedua lebih realistis. **D3 Censoring.** Kelompok survival analysis dan sejumlah metode deep learning modern secara eksplisit menangani data tersensor, tetapi mayoritas metode deep learning untuk RUL masih mengabaikan censoring dan dilatih hanya pada data lengkap. **D4 Arsitektur Model.** Arsitektur didominasi LSTM, CNN-LSTM, dan Transformer, dengan Bayesian Neural Network untuk pengeluaran probabilistik dan survival klasik (Cox, Weibull/AFT) untuk pemodelan waktu-ke-kejadian. **D5 Ketidakpastian.** Model probabilistik menyediakan interval prediksi, sedangkan model deterministik hanya mengeluarkan satu angka RUL. **D6 Keputusan/DSS.** Hanya sebagian kecil studi menghubungkan prediksi RUL ke keputusan perawatan, dan inilah ruang kontribusi bidang sistem informasi. **D7 Domain RO/Membran.** Domain membran jauh lebih sedikit dibanding mesin, dan sebagian besar berupa prediksi fouling atau performa, bukan RUL dengan survival analysis. **D8 Skala Data.** Sangat sedikit studi yang secara khusus menangani data kecil, few-shot, transfer learning, atau kondisi tanpa kegagalan; mayoritas berasumsi armada besar dengan banyak kegagalan teramati.

## 5. Diskusi

### 5.1 Sintesis Lintas Dimensi

Peta hasil menunjukkan sebuah paradoks. Di satu sisi, komponen-komponen yang dibutuhkan untuk prediksi RUL membran sebenarnya sudah tersedia: sensor (D1) sudah teridentifikasi, arsitektur model (D4) sudah matang, dan kerangka survival untuk data tersensor (D3) sudah dirumuskan. Di sisi lain, komponen-komponen tersebut berada pada komunitas riset yang berbeda. Survival analysis berkembang di komunitas reliabilitas dan statistik, deep learning RUL berkembang di komunitas prognostik mesin, sedangkan domain membran berkembang di komunitas teknik kimia dan lingkungan. Akibatnya, konvergensi antar-komponen jarang terjadi, dan justru pada titik konvergensi inilah nilai kebaruan berada.

Temuan paling menonjol adalah ketipisan dimensi censoring (D3, hanya 13 dari 101 artikel). Censoring bukan detail teknis kecil, melainkan kondisi yang secara fundamental mengubah cara kerja estimasi. Ketika sebuah unit belum gagal saat pengamatan berakhir, informasi yang tersedia hanyalah batas bawah waktu kegagalan. Mengabaikan informasi ini sama dengan membuang data, dan melatih model hanya pada unit-unit yang telah gagal akan menghasilkan estimasi yang bias terhadap kasus kegagalan dini. Pada membran RO, di mana penggantian preventif adalah praktik normal, hampir seluruh riwayat hidup elemen membran berbentuk data tersensor. Inilah sebabnya dimensi D3 yang tipis beresonansi langsung dengan domain RO yang juga tipis (D7, 24 artikel, dan itupun mayoritas berupa prediksi fouling, bukan RUL).

Dimensi D8 tentang skala data memperparah persoalan. Literatur yang ada sebagian besar mengasumsikan armada besar dengan banyak kegagalan teramati, kondisi yang tidak selalu berlaku pada satu plant pilot. Pada skala kecil dengan kegagalan mendekati nol, identifiability menjadi masalah serius. Sebagaimana ditegaskan Li dkk. (2001) pada konteks model cure, parameter tidak dapat diidentifikasi tanpa asumsi tambahan. Drent dkk. (2020) menunjukkan bahwa pada data tersensor, kebijakan keputusan tetap dapat dioptimalkan, tetapi memerlukan perlakuan Bayesian yang cermat terhadap prior dan struktur parameter. Konsekuensinya, penelitian pada domain ini harus bergerak dari pertanyaan akurasi semata menuju pertanyaan identifiability dan kuantifikasi ketidakpastian yang jujur.

### 5.2 Research Gap

Sintesis di atas menajamkan sebuah celah yang dapat dirumuskan secara tegas. Dari korpus yang diekstraksi, tidak ditemukan satu pun studi yang secara simultan menggabungkan empat elemen: (1) prediksi RUL membran reverse osmosis dengan survival analysis yang sadar-censoring; (2) kondisi data tanpa kegagalan akibat penggantian preventif, sehingga censoring mendominasi; (3) skala data kecil pada satu plant pilot; dan (4) integrasi hasil prediksi ke dalam sistem pendukung keputusan perawatan. Setiap elemen secara individual telah dibahas di literatur, namun kombinasinya belum. Inilah research gap yang menjadi dasar usulan penelitian tesis: bukan sekadar menerapkan metode X ke domain Y, melainkan menangani rezim data yang justru dihindari literatur, yaitu censoring yang mendominasi dengan jumlah kegagalan mendekati nol. Kontribusi yang dapat dipertahankan terletak pada metodologi yang jujur terhadap identifiability sekaligus pada artifact DSS yang menerjemahkan prediksi probabilistik menjadi keputusan perawatan.

### 5.3 Ancaman terhadap Validitas

Tiga ancaman validitas perlu dicatat. Pertama, ancaman terhadap validitas internal: sebagian besar metode dievaluasi pada dataset benchmark mesin seperti C-MAPSS atau data bearing dengan censoring yang disimulasikan, sehingga performa pada kondisi tersebut belum tentu bertransfer ke karakteristik membran nyata. Kedua, ancaman terhadap validitas konstruk: klasifikasi indeks Scopus dan penentuan pilar maupun dimensi konsep pada korpus bergantung pada penilaian peneliti dan perlu diverifikasi pada laman resmi penerbit. Ketiga, ancaman terhadap validitas eksternal: karena ringkasan bersumber terutama pada abstrak untuk sebagian besar korpus, detail metodologis yang halus berpotensi tidak tertangkap, sehingga generalisasi sebaran dimensi harus dibaca sebagai indikasi arah dan bukan hitungan yang sempurna. Penelusuran full-text pada artikel terpilih dan verifikasi metadata pada sumber resmi direkomendasikan sebagai langkah lanjutan.

## 6. Kesimpulan

SLR ini menegaskan adanya celah penelitian yang nyata. Kerangka survival analysis untuk data tersensor dan kapasitas deep learning untuk pemodelan deret waktu telah matang, tetapi konvergensinya pada domain membran reverse osmosis masih sangat terbatas. Dimensi censoring yang hanya dibahas 13 dari 101 artikel, disandingkan dengan domain RO yang didominasi prediksi fouling, menunjukkan bahwa rezim data yang paling relevan di lapangan justru paling sedikit diteliti. Belum ada studi yang secara simultan menggabungkan prediksi RUL membran RO sadar-censoring, kondisi data tanpa kegagalan, skala data kecil, dan integrasi DSS perawatan. Celah inilah yang menjadi dasar penelitian tesis yang diusulkan, dengan fokus pada estimasi RUL yang jujur terhadap identifiability dan pada artifact sistem informasi yang menerjemahkan prediksi probabilistik menjadi keputusan perawatan yang dapat dipertanggungjawabkan.

## Daftar Pustaka

[1] Gao, Y., Li, S., Wang, D., Mao, J., & Ouyang, L. (2025). A Neural Network-Based Survival Analysis Model Considering Censored Data for Failure Prediction. *IEEE Transactions on Automation Science and Engineering*. DOI 10.1109/TASE.2025.3640217.

[2] Alshraideh, H., Al Ali, F., Awad, M., & Al-Othman, A. (2026). AI-based remaining useful life prediction of seawater desalination membranes. *Chemical Engineering Journal Advances*, 26, 101217. DOI 10.1016/j.ceja.2026.101217.

[3] Noot, J.-P., Martin, M., & Birmelé, E. (2025). LSTM and Transformers based methods for RUL Prediction considering Censored Data. *International Journal of Prognostics and Health Management*, 16(2). DOI 10.36001/ijphm.2025.v16i2.4260.

[4] Si, X.-S., Wang, W., Hu, C.-H., & Zhou, D.-H. (2011). Remaining Useful Life Estimation – A Review on the Statistical Data Driven Approaches. *European Journal of Operational Research*, 213(1), 1–14.

[5] Kitchenham, B., & Charters, S. (2007). *Guidelines for Performing Systematic Literature Reviews in Software Engineering*. EBSE Technical Report.

[6] Page, M. J., et al. (2021). The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. *BMJ*, 372, n71.

[7] Webster, J., & Watson, R. T. (2002). Analyzing the Past to Prepare for the Future: Writing a Literature Review. *MIS Quarterly*, 26(2), xiii–xxiii.

[8] Wohlin, C. (2014). Guidelines for Snowballing in Systematic Literature Studies and a Replication in Software Engineering. *EASE '14*.

[9] Drent, C., Kapodistria, S., & Boxma, O. J. (2020). Censored lifetime learning: Optimal Bayesian age-replacement policies. *Operations Research Letters*, 48(6), 827–834. DOI 10.1016/j.orl.2020.10.005.

[10] Li, C.-S., Taylor, J. M. G., & Sy, J. P. (2001). Identifiability of cure models. *Statistics & Probability Letters*, 54(4), 389–395.

# Prediksi Remaining Useful Life (RUL) Membran Reverse Osmosis Berbasis Survival Analysis dan Deep Learning: Sebuah Systematic Literature Review

## Muhammad Nio Hastungkoro, [Nama Pembimbing]

**Program Studi Magister Sistem Informasi, Sekolah Pascasarjana, Universitas Diponegoro, mnioh@students.undip.ac.id**

**Abstrak.** Penurunan kinerja membran reverse osmosis (RO) akibat fouling, scaling, dan degradasi kimia menuntut strategi perawatan yang prediktif. Artikel ini menyajikan systematic literature review (SLR) yang memetakan pemanfaatan survival analysis dan deep learning untuk prediksi remaining useful life (RUL), dengan penekanan pada data tersensor kanan (right-censored) dan keterbatasan data. Tinjauan mengikuti Kitchenham dan Charters, pelaporan PRISMA 2020, sintesis concept-centric Webster dan Watson, serta snowballing Wohlin. Pencarian pada OpenAlex dengan 16 query mengidentifikasi 694 rekaman; 485 disaring, 101 dinilai kelayakannya, dan 79 artikel memenuhi kriteria inklusi. Dari 79 artikel tersebut, 46 tergolong Inti dan 19 ditetapkan sebagai core paper. Dimensi censoring (D3) dibahas 28 artikel, sedangkan domain RO (D7) hanya dibahas 2 artikel, dan irisan keduanya berjumlah nol. Artinya, belum ada studi yang secara simultan menangani data tersensor pada domain membran RO. Celah ini menjadi dasar penelitian tesis yang diusulkan, yaitu prediksi RUL membran RO yang sadar-censoring pada rezim data kecil dan terintegrasi dengan sistem pendukung keputusan perawatan.

**Kata kunci:** remaining useful life; survival analysis; data tersensor; deep learning; reverse osmosis; predictive maintenance; systematic literature review

**Abstract.** The performance degradation of reverse osmosis (RO) membranes due to fouling, scaling, and chemical degradation calls for predictive maintenance. This article presents a systematic literature review (SLR) mapping the use of survival analysis and deep learning for remaining useful life (RUL) prediction, with emphasis on right-censored data and limited data. The review follows Kitchenham and Charters, PRISMA 2020 reporting, Webster and Watson concept-centric synthesis, and Wohlin snowballing. A search on OpenAlex with 16 queries identified 694 records; 485 were screened, 101 were assessed for eligibility, and 79 met the inclusion criteria. Of the 79 included articles, 46 are Inti and 19 are core papers. The censoring dimension (D3) is addressed by 28 articles, while the RO domain (D7) is addressed by only 2 articles, with zero intersection between them. Hence, no study simultaneously handles censored data in the RO membrane domain. This gap motivates the proposed thesis: a censoring-aware RUL prediction for RO membranes under small-data regimes, integrated with a maintenance decision support system.

**Keywords:** remaining useful life; survival analysis; censored data; deep learning; reverse osmosis; predictive maintenance; systematic literature review

<!--BODY-->

## 1. Pendahuluan

Membran reverse osmosis (RO) merupakan komponen inti pada instalasi desalinasi air payau maupun air laut. Kinerjanya menurun seiring waktu karena fouling, scaling, dan degradasi kimia, sehingga memerlukan perawatan berkala berupa clean-in-place (CIP) atau penggantian elemen membran. Keputusan perawatan yang terlambat menimbulkan penurunan kualitas permeat, kenaikan tekanan operasi, dan konsumsi energi yang membengkak; sebaliknya, penggantian yang terlalu dini membuang sisa umur pakai yang sebenarnya masih tersedia. Karena itu, kemampuan memprediksi remaining useful life (RUL) membran secara akurat memiliki nilai ekonomi dan operasional yang tinggi [1], [2].

Persoalan mendasar muncul dari sifat data lapangan. Perawatan membran hampir selalu dilakukan secara preventif, yaitu sebelum terjadi kegagalan fisik total. Akibatnya, basis data pemantauan didominasi data tersensor kanan (right-censored): pengamatan berhenti karena penggantian preventif atau berakhirnya periode studi, tanpa pernah merekam waktu kegagalan yang sebenarnya. Metode prediksi RUL konvensional yang hanya belajar dari data run-to-failure membuang observasi tersensor ini dan karenanya menghasilkan estimasi yang bias [1], [9]. Survival analysis menawarkan kerangka waktu-ke-kejadian yang secara eksplisit memanfaatkan data tersensor [4], [11], sedangkan deep learning menawarkan kapasitas menangkap pola multi-sensor yang kompleks [3], [24].

Urgensi tinjauan ini muncul dari tiga ketegangan. Pertama, metode survival analysis dan deep learning sudah mapan untuk mesin berarmada besar seperti turbin, bearing, dan baterai, tetapi belum banyak diadopsi untuk membran RO [2], [14]. Kedua, di lapangan data membran justru berukuran kecil dan hampir tanpa kegagalan teramati, kondisi yang belum banyak diuji literatur [10], [14]. Ketiga, pemanfaatan hasil prediksi RUL untuk keputusan perawatan berbasis sistem pendukung keputusan (DSS) belum menjadi fokus utama [25], [27]. Ketiga ketegangan ini menunjukkan bahwa persoalannya bukan sekadar menerapkan metode tertentu pada domain tertentu, melainkan menangani rezim data yang justru dihindari literatur.

Tinjauan ini bertujuan menjawab empat pertanyaan riset. RQ1 menanyakan bagaimana survival analysis menangani data tersensor pada prediksi RUL. RQ2 menanyakan bagaimana deep learning, termasuk LSTM, Transformer, dan Bayesian neural network, meningkatkan prediksi RUL dan kuantifikasi ketidakpastian. RQ3 menanyakan kendala apa yang muncul pada kondisi data kecil maupun tanpa kegagalan (all-censored), serta solusinya. RQ4 menanyakan bagaimana hasil prediksi RUL digunakan dalam sistem pendukung keputusan perawatan.

Kontribusi artikel ini ada tiga. Pertama, artikel menyajikan peta taksonomi metode prediksi RUL dengan fokus pada censoring dan keterbatasan data. Kedua, artikel membangun matriks konsep yang menunjukkan sebaran dimensi riset pada korpus, sekaligus memisahkan basis bukti bertingkat menjadi included, Inti, dan core. Ketiga, artikel merumuskan research gap yang terukur dan dapat dipertanggungjawabkan, yaitu tidak adanya studi yang menggabungkan penanganan censoring dengan domain membran RO. Dengan demikian, artikel ini tidak berhenti pada Ringkasan literatur, tetapi menyediakan dasar empiris bagi perancangan model dan sistem perawatan.

Sisa artikel disusun sebagai berikut. Bagian 2 menyajikan tinjauan pustaka dan penelitian terkait. Bagian 3 menjelaskan metode tinjauan sistematis, termasuk protokol, strategi pencarian, kriteria seleksi, ekstraksi data, penilaian kualitas, dan sintesis. Bagian 4 melaporkan hasil, mulai dari alur PRISMA, sebaran pilar, matriks konsep, penentuan paper inti, hingga kualitas studi. Bagian 5 mendiskusikan sintesis lintas dimensi, research gap, implikasi, dan ancaman validitas. Bagian 6 menyajikan kesimpulan.

## 2. Tinjauan Pustaka dan Penelitian Terkait

### 2.1 Survival analysis dan data tersensor

Prediksi RUL telah berkembang melalui dua tradisi besar. Tradisi pertama bersifat statistis dan berakar pada survival analysis, yang memodelkan distribusi waktu menuju suatu kejadian melalui fungsi survival dan hazard. Tinjauan komprehensif oleh Si dkk. [4] memetakan pendekatan statistis berbasis data dan menegaskan bahwa pemodelan waktu-ke-kejadian merupakan fondasi estimasi RUL. Kekuatan tradisi ini terletak pada kemampuan menangani data tersensor secara formal, sedangkan keterbatasannya adalah asumsi bentuk distribusi dan kesulitan menangkap dinamika nonlinier dari sinyal multi-sensor.

Isu censoring bukan detail teknis kecil. Ketika sebuah unit belum gagal saat pengamatan berakhir, informasi yang tersedia hanyalah batas bawah waktu kegagalan. Drent dkk. [9] menunjukkan bahwa pembelajaran masa pakai dari data tersensor dapat menghasilkan kebijakan penggantian yang optimal di bawah ketidakpastian, tetapi memerlukan perlakuan Bayesian yang cermat terhadap prior dan struktur parameter. Pada kondisi ekstrem, yaitu ketika hampir seluruh data tersensor, parameter skala distribusi Weibull tidak teridentifikasi; Li dkk. [10] menegaskan bahwa parameter model cure tidak dapat diidentifikasi tanpa asumsi tambahan. Peringatan ini berlaku pula pada data membran yang hampir tanpa kegagalan teramati.

Tinjauan terbaru oleh Shadi dkk. [11] memetakan model survival untuk predictive maintenance pada jaringan energi bersensor dan menunjukkan bahwa model survival semakin banyak dipakai untuk menghasilkan estimasi yang sadar-risiko. Abdelhafid dkk. [19] membandingkan model Cox dan Weibull untuk komponen industri dan menegaskan bahwa pemilihan bentuk distribusi memengaruhi kualitas prediksi. Temuan-temuan ini memperkuat argumen bahwa survival analysis bukan sekadar alternatif, melainkan kerangka yang tepat ketika data didominasi observasi tersensor.

### 2.2 Deep learning untuk RUL

Tradisi kedua bersifat komputasional dan bertumpu pada deep learning. Arsitektur LSTM, CNN-LSTM, dan Transformer mendominasi pemodelan deret waktu untuk RUL karena kemampuannya menangkap dependensi temporal jangka panjang. Noot dkk. [3] mengembangkan metode berbasis LSTM dan Transformer yang secara khusus memperhitungkan data tersensor, menunjukkan bahwa arsitektur modern dapat diintegrasikan dengan fungsi likelihood survival. Gao dkk. [1] mengusulkan model survival berbasis neural network yang memanfaatkan data tersensor untuk prediksi kegagalan, menjembatani kapasitas representasi deep learning dengan kerangka probabilistik survival analysis.

Sejumlah studi memperluas arah ini. Chu dkk. [24] membangun model deep survival berbasis convolutional neural network dan LSTM untuk estimasi RUL. Dhada dkk. [16] mengusulkan Weibull recurrent neural network untuk prognosis kegagalan menggunakan data histogram, sedangkan Lv dkk. [13] memakai model general log-linear Weibull yang menggabungkan karakteristik vibrasi dan suhu untuk bearing. Reddy dkk. [15] memperkenalkan kerangka attention multisensor untuk estimasi RUL berbasis Weibull pada data industri nyata. Chen dkk. [26] menambahkan kerangka augmentasi deret waktu multisensor untuk RUL aero engine. Pola yang muncul adalah semakin banyak model deep learning yang mencoba memasukkan struktur survival ke dalam arsitektur neural, meskipun sebagian besar masih diuji pada dataset mesin, bukan membran.

### 2.3 Bayesian dan kuantifikasi ketidakpastian

Dimensi ketidakpastian menjadi perhatian yang tumbuh. Model probabilistik dan Bayesian menyediakan interval prediksi, bukan sekadar satu angka RUL. Tv dkk. [12] menggunakan ensemble deep ordinal regression untuk estimasi ketidakpastian prediktif, sedangkan Kraus dkk. [20] memakai variational Bayesian inference untuk menghasilkan prediksi RUL yang interpretable. Yu dkk. [23] mengusulkan Weibull variational autoencoder, dan Chiodo dkk. [27] memodelkan RUL baterai lithium-ion secara probabilistik. Maulana dkk. [25] menggabungkan metode explainable data-driven dengan Bayesian filtering untuk prediksi RUL mesin pesawat.

Pendekatan fisika dan pengetahuan domain juga mulai dilibatkan. Zheng dkk. [21] mengusulkan kerangka physical knowledge-guided dan data-driven untuk RUL turbofan, sedangkan E dkk. [22] memakai physics-informed neural network untuk memprediksi lintasan degradasi dan RUL supercapacitor. Di sisi transfer dan data terbatas, Li dkk. [18] mengusulkan domain adaptive RUL prediction dengan Transformer, dan Al-Dahidi dkk. [14] menangani armada heterogen dengan kondisi operasi yang bervariasi. Abdelhafid dkk. [17] menunjukkan bahwa panduan survival analysis dapat memperbaiki prediksi kegagalan dan RUL pada kompresor kereta api.

### 2.4 Domain membran RO dan DSS perawatan

Pada domain membran dan desalinasi, literatur didominasi oleh prediksi fouling dan performa, bukan RUL. Alshraideh dkk. [2] mengusulkan prediksi RUL berbasis kecerdasan artifisial untuk membran desalinasi air laut, sedangkan banyak studi lain berfokus pada prediksi fouling dengan machine learning. Penghubungan hasil prediksi ke keputusan perawatan dalam kerangka DSS/CMMS juga masih jarang. Konsekuensinya, tinjauan pustaka ini menunjukkan tiga hal: kerangka survival analysis tersedia [4], [9], [11], arsitektur deep learning tersedia [1], [3], [24], dan komponen Bayesian tersedia [12], [20], [23], tetapi ketiganya belum dikonvergensikan pada domain membran RO dengan kondisi data yang realistis. Kombinasi inilah yang kemudian ditelusuri secara sistematis.

## 3. Metode Tinjauan Sistematis

### 3.1 Protokol dan pedoman

Tinjauan ini mengikuti panduan Kitchenham dan Charters [5] untuk SLR di bidang rekayasa perangkat lunak dan sistem informasi, dengan pelaporan alur seleksi mengikuti PRISMA 2020 [6] dan sintesis concept-centric mengikuti Webster dan Watson [7]. Penelusuran lanjutan menggunakan snowballing backward dan forward menurut Wohlin [8]. Protokol disusun sebelum pencarian agar proses dapat diaudit dan direproduksi. Protokol memuat pertanyaan riset, kerangka PICOC, string pencarian, kriteria inklusi dan eksklusi, formulir ekstraksi, rubrik penilaian kualitas, serta prosedur sintesis.

### 3.2 Pertanyaan riset dan PICOC

Tinjauan ini dipandu oleh empat pertanyaan riset yang telah disebutkan pada Bagian 1. Kerangka PICOC dijabarkan sebagai berikut. Population mencakup sistem membran RO dan mesin industri yang menyelenggarakan prognostik. Intervention berupa metode survival analysis dan deep learning untuk RUL. Comparison berupa metode RUL konvensional berbasis regresi dan data run-to-failure. Outcome mencakup akurasi RUL, kualitas kuantifikasi ketidakpastian, dan kelayakan keputusan perawatan. Context mencakup plant industri maupun pilot, dengan perhatian pada rezim data tersensor dan skala data kecil.

### 3.3 Strategi pencarian dan kriteria seleksi

Pencarian hybrid memadukan pencarian basis data dan snowballing [8]. Eksekusi korpus ini menggunakan OpenAlex (metadata Crossref) dengan 16 query title dan abstract, filter type=article dan has_doi=true, serta pengambilan 50 hasil teratas per query. Contoh string Scopus yang disiapkan untuk replikasi adalah sebagai berikut: TITLE-ABS-KEY (("remaining useful life" OR "RUL" OR prognos* OR "predictive maintenance" OR "PHM") AND (censor* OR "survival analysis" OR Weibull OR "time-to-event") AND ("deep learning" OR "neural network" OR LSTM OR transformer OR "Bayesian")) AND PUBYEAR > 2014. Batas recall yang disadari adalah tidak adanya paginasi dan filter tahun di API, sehingga penyaringan tahun dilakukan pada tahap screening.

Kriteria inklusi bersifat konjungtif. IC1 menuntut studi primer peer-reviewed. IC2 menuntut bahasa Inggris atau Indonesia. IC3 menuntut rentang tahun 2015 sampai 2026, dengan karya seminal pra-2015 hanya melalui snowballing. IC4 merupakan gate topik: topik utama harus RUL, prognostik, survival analysis, degradation-to-failure, atau predictive maintenance pada aset teknik. IC5 menuntut kontribusi ke minimal satu RQ. IC6 menuntut ketersediaan abstrak, dengan ketersediaan full-text dicatat sebagai flag kualitas bukti. Studi dieksklusi bila topiknya di luar RUL atau prognostik (EC-T), merupakan review atau bukan studi primer (EC-R), berada di luar cakupan domain (EC-D), bersifat medis atau klinis (EC-M), tidak memiliki abstrak (EC-A), atau duplikat (EC-DUP).

### 3.4 Proses seleksi dan PRISMA

Proses seleksi mengikuti alur identifikasi, deduplikasi, penyaringan judul dan abstrak, penilaian kelayakan, serta penyertaan akhir. Setiap keputusan dicatat per paper pada eligibility log yang memuat nomor, DOI, tahun, pilar, tier, status included, kode eksklusi, alasan, ketersediaan full-text, dan judul. Pencatatan ini penting karena jumlah studi bukan target yang ditetapkan di awal, melainkan output dari penerapan kriteria. Dengan demikian, pertanyaan "mengapa 101" dijawab secara prosedural, bukan secara numerik.

### 3.5 Ekstraksi data dan penilaian kualitas

Ekstraksi data mengikuti formulir terstruktur yang memuat nomor, pilar atau tema, judul, penulis, tahun, jurnal, klasifikasi, tautan atau DOI, ringkasan temuan, dan kontribusi terhadap research gap. Setiap artikel juga diberi penanda dimensi D1 sampai D8 beserta bukti pendukungnya. Penilaian kualitas menggunakan sepuluh butir yang mencakup kejelasan tujuan, keterjelasan metodologi, kejelasan sumber data, penanganan censoring, metrik evaluasi, pelaporan ketidakpastian, perbandingan baseline, pembahasan keterbatasan, kontribusi terhadap praktik, dan ketertelusuran publikasi. Setiap butir dinilai Ya, Sebagian, atau Tidak, lalu dinormalisasi ke skala 0 sampai 10.

### 3.6 Sintesis dan penentuan paper inti

Sintesis dilakukan secara concept-centric menggunakan matriks konsep Webster dan Watson [7] dengan tujuh pilar (A sampai G) dan delapan dimensi konsep (D1 sampai D8). Karena studi heterogen, sintesis bersifat naratif dan tidak melakukan pooling efek kuantitatif. Untuk menjawab kebutuhan praktis tesis, korpus dipilah menjadi basis bukti bertingkat. Penentuan paper inti menggunakan rubrik skor 0 sampai 6 yang terdiri atas relevansi RQ (0 sampai 2), kedekatan metodologis (0 sampai 2), dan kualitas (0 sampai 2). Paper ditetapkan sebagai core bila skor total minimal 5,5 atau bertier Inti-Metode+Domain.

## 4. Hasil

### 4.1 Alur PRISMA dan korpus final

Pencarian mengidentifikasi 694 rekaman unik. Sebanyak 209 rekaman tanpa abstrak atau metadata tidak lengkap dikeluarkan sebelum penyaringan, menyisakan 485 rekaman yang disaring pada judul dan abstrak. Dari tahap ini diperoleh 72 artikel yang layak, lalu ditambah 29 artikel dari snowballing dan penggantian Open Access. Seluruh 101 artikel dinilai kelayakannya; 22 artikel dikeluarkan pada tahap eligibilitas, yaitu 15 karena topik di luar RUL atau prognostik, 6 karena merupakan review, dan 1 karena berada di luar cakupan domain. Dengan demikian, 79 artikel menjadi korpus sintesis.

{{FIG:fig01_prisma_flow.png|Alur PRISMA 2020 dan komposisi korpus final (n = 79 included)|15}}

| Tahap PRISMA | Jumlah | Keterangan |
| --- | --- | --- |
| Identifikasi (rekaman unik) | 694 | Pencarian OpenAlex, 16 query |
| Dihapus sebelum penyaringan | 209 | Tanpa abstrak atau metadata tidak lengkap |
| Disaring (judul/abstrak) | 485 | Kriteria relevansi kata kunci |
| Dikeluarkan pada judul/abstrak | 413 | Tidak relevan secara topik |
| Layak dari pencarian basis data | 72 | Artikel berabstrak, 2015 sampai 2026 |
| Ditambah snowballing dan pengganti OA | 29 | Backward, forward, dan penggantian |
| Dinilai kelayakannya | 101 | Gate topik dan kontribusi RQ |
| Dikeluarkan pada eligibilitas | 22 | 15 topik, 6 review, 1 domain |
| Termasuk dalam sintesis | 79 | Korpus sintesis |

### 4.2 Sebaran pilar

Korpus terbagi ke dalam tujuh pilar tematik. Pilar survival analysis dan censored data (A) serta deep learning RUL (B) masing-masing mencakup 24 artikel, diikuti Bayesian dan uncertainty (C) dengan 15 artikel serta small-data dan transfer (D) dengan 9 artikel. Pilar DSS dan predictive maintenance (F) mencakup 6 artikel, sedangkan domain membran dan RO (E) hanya 1 artikel karena studi domain yang murni fouling atau performance dikeluarkan pada gate topik. Konteks Indonesia (G) tidak tersisa pada korpus sintesis.

{{FIG:fig07_pillar_distribution.png|Sebaran artikel per pilar A sampai G (n = 79)|15}}

| Pilar/Tema | Jumlah Artikel |
| --- | --- |
| A. Survival Analysis dan Censored Data | 24 |
| B. Deep Learning RUL | 24 |
| C. Bayesian dan Uncertainty | 15 |
| D. Small-data/Transfer/Hierarchical | 9 |
| E. Membrane/RO/Desalination | 1 |
| F. DSS dan Predictive Maintenance | 6 |
| G. Konteks Indonesia/Air | 0 |

### 4.3 Matriks konsep dan sebaran dimensi

Matriks konsep menunjukkan sebaran yang tidak merata. Dimensi target dan kegagalan (D2) dibahas 79 artikel, arsitektur model (D4) 76 artikel, dan data atau sensor (D1) 73 artikel. Dimensi ketidakpastian (D5) dibahas 43 artikel, skala data (D8) 31 artikel, censoring (D3) 28 artikel, keputusan atau DSS (D6) 21 artikel, dan domain RO (D7) hanya 2 artikel. Meskipun D3 bukan dimensi paling tipis secara absolut, D3 justru paling kritis karena merupakan inti persoalan data membran. Yang paling penting, tidak ada satu pun artikel yang membahas D3 dan D7 secara bersamaan, sehingga celah metodologisnya bersifat struktural, bukan sekadar peringkat jumlah.

{{FIG:fig08_dimension_coverage.png|Cakupan dimensi konsep D1 sampai D8 (n = 79)|15}}

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

### 4.4 Paper inti dan core paper

Untuk menjawab kebutuhan praktis tesis, korpus 79 artikel dipilah menjadi basis bukti bertingkat. Sebanyak 46 artikel tergolong Inti yang terdiri atas 31 Inti-Metode, 13 Inti-Domain, dan 2 Inti-Metode+Domain, 31 Pendukung, dan 2 Konteks. Dengan rubrik skor 0 sampai 6, ditetapkan 19 core paper yang menjadi sumber utama model. Paper inti tersebut mencakup dua tradisi, yaitu statistis dan deep learning, serta domain membran, sehingga menjadi simpul utama bagi penelusuran snowballing dan pembacaan mendalam.

{{FIG:fig09_tier_funnel.png|Penyaringan korpus dan penentuan 19 core paper|14}}

| No | Tahun | Jurnal | Judul | Pilar |
| --- | --- | --- | --- | --- |
| 11 | 2025 | IEEE Transactions on Automation Science and Engineering | A Neural Network-Based Survival Analysis Model Considering Censored Data | A |
| 12 | 2025 | International Journal of Prognostics and Health Management | LSTM and Transformers based methods for RUL Prediction considering Censored Data | A |
| 13 | 2026 | Sensors | Survival Models for Predictive Maintenance and Remaining Useful Life | A |
| 48 | 2019 | International Journal of Prognostics and Health Management | Data-driven Prognostics with Predictive Uncertainty Estimation | C |
| 64 | 2020 | Shock and Vibration | General Log-Linear Weibull Model Combining Vibration and Temperature | A |
| 4 | 2016 | Reliability Engineering & System Safety | Remaining useful life estimation in heterogeneous fleets | D |
| 17 | 2026 | IEEE Sensors Letters | A Multisensor Cross-Modal Attention Framework for Weibull-Driven RUL | B |
| 19 | 2022 | Neural Computing and Applications | Weibull recurrent neural networks for failure prognosis | A |
| 9 | 2026 | Scientific Reports | Survival-analysis-guided machine learning for failure and RUL prediction | A |
| 35 | 2022 | IEEE Transactions on Instrumentation and Measurement | Domain Adaptive Remaining Useful Life Prediction With Transformer | D |

### 4.5 Kualitas studi dan tren publikasi

Skor kualitas studi berkisar 4 sampai 9 dari 10, dengan mayoritas berada pada rentang 6 sampai 8. Sebaran ini menunjukkan bahwa korpus cukup matang secara metodologis, tetapi belum merata pada aspek pelaporan ketidakpastian dan penanganan censoring. Dari sisi waktu, publikasi meningkat setelah 2018 seiring meluasnya deep learning untuk prognostik, dengan puncak pada beberapa tahun terakhir. Tren ini menegaskan bahwa bidangnya aktif, tetapi belum terkonsentrasi pada domain membran.

## 5. Diskusi

### 5.1 Sintesis lintas dimensi

Peta hasil menunjukkan sebuah paradoks. Di satu sisi, komponen yang dibutuhkan untuk prediksi RUL membran sebenarnya sudah tersedia: sensor (D1) sudah teridentifikasi, arsitektur model (D4) sudah matang, dan kerangka survival untuk data tersensor (D3) sudah dirumuskan [4], [9], [11]. Di sisi lain, komponen-komponen tersebut berada pada komunitas riset yang berbeda. Survival analysis berkembang di komunitas reliabilitas dan statistik, deep learning RUL berkembang di komunitas prognostik mesin, sedangkan domain membran berkembang di komunitas teknik kimia dan lingkungan. Akibatnya, konvergensi antar-komponen jarang terjadi, dan justru pada titik konvergensi inilah nilai kebaruan berada.

Temuan paling menonjol adalah terputusnya dimensi censoring (D3, 28 dari 79 artikel) dari domain RO (D7, 2 artikel): tidak ada satu pun artikel yang membahas keduanya. Censoring bukan detail teknis kecil, melainkan kondisi yang secara fundamental mengubah cara kerja estimasi. Mengabaikan informasi ini sama dengan membuang data, dan melatih model hanya pada unit yang telah gagal akan menghasilkan estimasi yang bias terhadap kasus kegagalan dini [1], [9]. Pada membran RO, di mana penggantian preventif adalah praktik normal, hampir seluruh riwayat hidup elemen membran berbentuk data tersensor. Inilah sebabnya terputusnya D3 dan D7 menjadi celah paling tajam: literatur domain RO mayoritas membahas prediksi fouling, bukan RUL yang sadar-censoring.

Dimensi D8 tentang skala data memperparah persoalan. Literatur yang ada sebagian besar mengasumsikan armada besar dengan banyak kegagalan teramati, kondisi yang tidak selalu berlaku pada satu plant pilot [10], [14]. Pada skala kecil dengan kegagalan mendekati nol, identifiability menjadi masalah serius. Sebagaimana ditegaskan Li dkk. [10] pada konteks model cure, parameter tidak dapat diidentifikasi tanpa asumsi tambahan. Drent dkk. [9] menunjukkan bahwa pada data tersensor, kebijakan keputusan tetap dapat dioptimalkan, tetapi memerlukan perlakuan Bayesian yang cermat terhadap prior dan struktur parameter. Konsekuensinya, penelitian pada domain ini harus bergerak dari pertanyaan akurasi semata menuju pertanyaan identifiability dan kuantifikasi ketidakpastian yang jujur.

### 5.2 Research gap

Sintesis di atas menajamkan sebuah celah yang dapat dirumuskan secara tegas. Dari korpus yang diekstraksi, tidak ditemukan satu pun studi yang secara simultan menggabungkan empat elemen: (1) prediksi RUL membran reverse osmosis dengan survival analysis yang sadar-censoring; (2) kondisi data tanpa kegagalan akibat penggantian preventif, sehingga censoring mendominasi; (3) skala data kecil pada satu plant pilot; dan (4) integrasi hasil prediksi ke dalam sistem pendukung keputusan perawatan. Setiap elemen secara individual telah dibahas di literatur [1], [9], [10], [14], namun kombinasinya belum. Inilah research gap yang menjadi dasar usulan penelitian tesis: bukan sekadar menerapkan metode X ke domain Y, melainkan menangani rezim data yang justru dihindari literatur, yaitu censoring yang mendominasi dengan jumlah kegagalan mendekati nol.

Secara kuantitatif, gap ini dapat dinyatakan dengan dua angka. D3 dibahas 28 artikel dan D7 dibahas 2 artikel, tetapi irisan D3 dan D7 berjumlah nol. Bahkan ketika kriteria diperketat menjadi D3, D4, D7, dan D6 secara simultan, jumlahnya tetap nol. Dengan demikian, kesimpulan gap tidak bergantung pada longgarnya kriteria inklusi, melainkan bertahan pada kriteria yang lebih ketat.

### 5.3 Implikasi teoretis dan praktis

Secara teoretis, penelitian ini memberi kontribusi pada bidang Sistem Informasi berupa rantai utuh dari data sensor menjadi prediksi RUL berketidakpastian, lalu menjadi rekomendasi keputusan. Prediksi RUL bukan tujuan akhir, melainkan keluaran antara. Inti persoalan Sistem Informasi adalah bagaimana aliran data sensor diubah menjadi informasi prediktif yang dapat ditindaklanjuti, dengan ketidakpastian yang tetap dibawa sampai momen pengambilan keputusan [25], [27].

Secara praktis, hasil tinjauan membantu pengelola plant RO menentukan kapan sebaiknya CIP atau mengganti modul. Dengan memakai aturan biaya per satuan waktu operasi, prediksi RUL dapat diterjemahkan menjadi keputusan yang mempertimbangkan biaya preventif dan biaya kegagalan. Pendekatan ini sejalan dengan model keputusan sadar-risiko yang telah dikembangkan pada domain lain [9], [20], tetapi belum diterapkan pada membran RO.

Secara metodologis, tinjauan ini menawarkan prosedur pemilihan paper inti yang transparan. Dengan menetapkan kriteria a priori, mencatat setiap keputusan, dan menghitung skor core, proses seleksi dapat direproduksi dan dipertanggungjawabkan. Prosedur ini juga menjawab kritik yang umum muncul dalam SLR, yaitu kesan bahwa jumlah dan pemilihan studi bersifat arbitrer.

### 5.4 Ancaman terhadap validitas

Empat ancaman validitas perlu dicatat. Pertama, ancaman terhadap validitas internal: sebagian besar metode dievaluasi pada dataset benchmark mesin seperti C-MAPSS atau data bearing dengan censoring yang disimulasikan, sehingga performa pada kondisi tersebut belum tentu bertransfer ke karakteristik membran nyata [26], [27]. Kedua, ancaman terhadap validitas konstruk: klasifikasi indeks Scopus dan penentuan pilar maupun dimensi konsep pada korpus bergantung pada penilaian peneliti dan perlu diverifikasi pada laman resmi penerbit.

Ketiga, ancaman terhadap validitas eksternal: karena ringkasan bersumber terutama pada abstrak untuk sebagian korpus, detail metodologis yang halus berpotensi tidak tertangkap. Pada korpus ini, 61 dari 79 artikel included memiliki full-text, sedangkan 18 artikel dinilai dari abstrak. Keempat, ancaman terhadap cakupan pencarian: pencarian menggunakan OpenAlex dengan 16 query dan 50 hasil teratas per query, tanpa paginasi penuh, sehingga artikel yang hanya terindeks di Scopus atau Web of Science berpotensi tidak tertangkap. Keterbatasan ini dicatat sebagai dasar replikasi pada basis data berlangganan dan sebagai agenda pengujian recall pada penelitian lanjutan.

## 6. Kesimpulan

SLR ini menegaskan adanya celah penelitian yang nyata. Kerangka survival analysis untuk data tersensor dan kapasitas deep learning untuk pemodelan deret waktu telah matang, tetapi konvergensinya pada domain membran reverse osmosis masih sangat terbatas. Dari 694 rekaman yang diidentifikasi, 101 artikel dinilai kelayakannya dan 79 artikel memenuhi kriteria inklusi. Dari 79 artikel tersebut, 46 tergolong Inti dan 19 ditetapkan sebagai core paper.

Dimensi censoring dibahas 28 artikel dan domain RO hanya 2 artikel, tetapi irisan keduanya nol. Belum ada studi yang secara simultan menggabungkan prediksi RUL membran RO sadar-censoring, kondisi data tanpa kegagalan, skala data kecil, dan integrasi DSS perawatan. Celah inilah yang menjadi dasar penelitian tesis yang diusulkan, dengan fokus pada estimasi RUL yang jujur terhadap identifiability dan pada artifact sistem informasi yang menerjemahkan prediksi probabilistik menjadi keputusan perawatan yang dapat dipertanggungjawabkan. Penelitian lanjutan disarankan menguji recall pencarian pada basis data berlangganan dan memvalidasi model pada data plant membran yang sebenarnya.

## Daftar Pustaka

[1] Y. Gao, S. Li, D. Wang, J. Mao, and L. Ouyang, "A neural network-based survival analysis model considering censored data for failure prediction," IEEE Trans. Autom. Sci. Eng., 2025, doi: 10.1109/TASE.2025.3640217.

[2] H. Alshraideh, F. Al Ali, M. Awad, and A. Al-Othman, "AI-based remaining useful life prediction of seawater desalination membranes," Chem. Eng. J. Adv., vol. 26, art. no. 101217, 2026, doi: 10.1016/j.ceja.2026.101217.

[3] J.-P. Noot, M. Martin, and E. Birmelé, "LSTM and transformers based methods for remaining useful life prediction considering censored data," Int. J. Progn. Health Manag., vol. 16, no. 2, 2025, doi: 10.36001/ijphm.2025.v16i2.4260.

[4] X.-S. Si, W. Wang, C.-H. Hu, and D.-H. Zhou, "Remaining useful life estimation: A review on the statistical data driven approaches," Eur. J. Oper. Res., vol. 213, no. 1, pp. 1-14, 2011, doi: 10.1016/j.ejor.2010.11.018.

[5] B. Kitchenham and S. Charters, "Guidelines for performing systematic literature reviews in software engineering," EBSE Tech. Rep., 2007.

[6] M. J. Page et al., "The PRISMA 2020 statement: An updated guideline for reporting systematic reviews," BMJ, vol. 372, n71, 2021, doi: 10.1136/bmj.n71.

[7] J. Webster and R. T. Watson, "Analyzing the past to prepare for the future: Writing a literature review," MIS Q., vol. 26, no. 2, pp. xiii-xxiii, 2002.

[8] C. Wohlin, "Guidelines for snowballing in systematic literature studies and a replication in software engineering," in Proc. EASE, 2014, doi: 10.1145/2601248.2601268.

[9] C. Drent, S. Kapodistria, and O. J. Boxma, "Censored lifetime learning: Optimal Bayesian age-replacement policies," Oper. Res. Lett., vol. 48, no. 6, pp. 827-834, 2020, doi: 10.1016/j.orl.2020.10.005.

[10] C.-S. Li, J. M. G. Taylor, and J. P. Sy, "Identifiability of cure models," Stat. Probab. Lett., vol. 54, no. 4, pp. 389-395, 2001, doi: 10.1016/S0167-7152(01)00105-5.

[11] M. Shadi et al., "Survival models for predictive maintenance and remaining useful life in sensor-enabled smart energy networks: A review," Sensors, vol. 26, no. 6, art. no. 1915, 2026, doi: 10.3390/s26061915.

[12] V. Tv et al., "Data-driven prognostics with predictive uncertainty estimation using ensemble of deep ordinal regression models," Int. J. Progn. Health Manag., vol. 10, no. 4, 2019, doi: 10.36001/ijphm.2019.v10i4.2612.

[13] Y. Lv et al., "General log-linear Weibull model combining vibration and temperature characteristics for remaining useful life prediction of rolling element bearings," Shock Vib., vol. 2020, art. no. 8829823, 2020, doi: 10.1155/2020/8829823.

[14] S. Al-Dahidi et al., "Remaining useful life estimation in heterogeneous fleets working under variable operating conditions," Reliab. Eng. Syst. Saf., vol. 156, pp. 109-124, 2016, doi: 10.1016/j.ress.2016.07.019.

[15] K. Reddy et al., "A multisensor cross-modal attention framework for Weibull-driven RUL estimation for liner using real-world industrial data," IEEE Sensors Lett., 2026, doi: 10.1109/LSENS.2026.3673123.

[16] M. Dhada et al., "Weibull recurrent neural networks for failure prognosis using histogram data," Neural Comput. Appl., vol. 34, pp. 21471-21488, 2022, doi: 10.1007/s00521-022-07667-7.

[17] A. Abdelhafid et al., "Survival-analysis-guided machine learning for failure and remaining-useful-life prediction in railway compressor," Sci. Rep., 2026, doi: 10.1038/s41598-026-65271-4.

[18] Y. Li et al., "Domain adaptive remaining useful life prediction with transformer," IEEE Trans. Instrum. Meas., vol. 71, 2022, doi: 10.1109/TIM.2022.3200667.

[19] A. Abdelhafid et al., "Reliable prediction of industrial components remaining useful life using Cox and Weibull models: A comparative study," Data Metadata, 2025, doi: 10.56294/dm20251102.

[20] M. Kraus et al., "Forecasting remaining useful life: Interpretable deep learning approach via variational Bayesian inferences," Decis. Support Syst., vol. 125, art. no. 113100, 2019, doi: 10.1016/j.dss.2019.113100.

[21] Y. Zheng et al., "A physical knowledge-guided and data-driven framework for remaining useful life prediction: The case of turbofan engines," J. Adv. Mech. Des. Syst. Manuf., vol. 19, 2025, doi: 10.1299/jamdsm.2025jamdsm0044.

[22] J. E et al., "A physics-informed neural network-based method for predicting degradation trajectories and remaining useful life of supercapacitors," Green Energy Intell. Transp., vol. 4, art. no. 100291, 2025, doi: 10.1016/j.geits.2025.100291.

[23] X. Yu et al., "Weibull variational autoencoder for remaining useful life prediction," Qual. Reliab. Eng. Int., 2026, doi: 10.1002/qre.70386.

[24] Y. Chu et al., "Developing deep survival model for remaining useful life estimation based on convolutional and long short-term memory neural networks," Wirel. Commun. Mob. Comput., vol. 2020, art. no. 8814658, 2020, doi: 10.1155/2020/8814658.

[25] F. Maulana, A. Starr, and A. P. Ompusunggu, "Explainable data-driven method combined with Bayesian filtering for remaining useful lifetime prediction of aircraft engines using NASA CMAPSS datasets," Machines, vol. 11, no. 2, art. no. 163, 2023, doi: 10.3390/machines11020163.

[26] J. Chen et al., "Multisensor time series forecasting-based augmentation framework for remaining useful life prediction of aero engines," IEEE Trans. Instrum. Meas., 2026, doi: 10.1109/TIM.2026.3684677.

[27] E. Chiodo et al., "Probabilistic modeling of Li-ion battery remaining useful life," IEEE Trans. Ind. Appl., vol. 58, no. 4, pp. 5210-5221, 2022, doi: 10.1109/TIA.2022.3170525.

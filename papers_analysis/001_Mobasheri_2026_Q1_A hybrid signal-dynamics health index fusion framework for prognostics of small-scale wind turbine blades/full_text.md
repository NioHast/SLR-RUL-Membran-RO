# **Article in Press**

# A hybrid signal-dynamics health index fusion framework for prognostics of small-scale wind turbine blades

Received: 5 January 2026

Accepted: 20 July 2026

Published online: 29 July 2026

Cite this article as: Mobasheri P., Aranizadeh A. & Vahidi B. A hybrid signal-dynamics health index fusion framework for prognostics of smallscale wind turbine blades. *Sci Rep* (2026). https://doi.org/10.1038/ s41598-026-63408-z

### Parisa Mobasheri, Ali Aranizadeh & Behrooz Vahidi

We are providing an unedited version of this manuscript to give early access to its findings. Before final publication, the manuscript will undergo further editing. Please note there may be errors present which affect the content, and all legal disclaimers apply.

nall- If this paper is publishing under a Transparent Peer Review model then Peer Review reports will publish with the final article.

© The Author(s) 2026. **Open Access** This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/">https://creativecommons.org/licenses/by-nc-nd/4.0/</a>.

# A Hybrid Signal-Dynamics Health Index Fusion Framework for Prognostics of Small-Scale Wind Turbine Blades

Parisa Mobasheri<sup>1</sup>, A. Aranizadeh<sup>2</sup>, B. Vahidi<sup>2\*</sup>

**Abstract:** Ensuring the dependable operation of wind turbines is essential for enhancing energy efficiency and minimizing maintenance costs, particularly in small-scale wind turbines where blade failures can severely affect safety and performance. This paper proposes a hybrid condition monitoring and prognostic framework for small-scale wind turbine (SSWT) blades that combines signal-based features, structural dynamic characteristics, and Health Index (HI) fusion. Experimental measurements were obtained from strain gauges and accelerometers mounted on turbine blades under three operating states: healthy (C), localized degradation (R), and global degradation (L). The acquired strain and vibration signals were preprocessed using band-pass filtering, normalization, and wavelet-based denoising to mitigate noise and environmental disturbances. Features were extracted from multiple domains, including time-domain indicators (RMS, skewness, kurtosis), frequency-domain descriptors (peak frequency and spectral energy), and dynamic properties such as natural frequencies, transmissibility, and mode shape curvatures. Dimensionality reduction using PCA and t-SNE demonstrated a clear separation among the three blade conditions. Several HIs were constructed based on PCA projections, autoencoder reconstruction errors, and Mahalanobis distance measures, which were then integrated into a Combined Health Index (CHI). The results indicate that transmissibility changes and natural frequency shifts are the most sensitive indicators of blade stiffness degradation. Compared with individual HIs, the CHI shows improved robustness to noise and operational variability. In addition, Remaining Useful Life (RUL) was estimated using Weibull-based degradation modeling and LSTM-inspired prediction, effectively capturing nonlinear damage evolution and supporting predictive maintenance of SSWT blades.

**Keyword:** Structural Health Monitoring (SHM), Dynamic Properties, Health Index (HI) Fusion, Remaining Useful Life (RUL), Signal Processing, small scale wind turbine (SSWT)

<sup>&</sup>lt;sup>1</sup> Department of Electrical Engineering, SR.C., Islamic Azad University, Tehran, Iran

<sup>&</sup>lt;sup>2</sup> Department of Electrical Engineering, Amirkabir University of Technology, Tehran, 1591634311, Iran

<sup>\*</sup> Corresponding author: E-mail address: vahidi@aut.ac.ir (<u>B. Vahidi</u>)

### **ABBREVIATIONS**

| Abbreviation | Definition                        | Abbreviation | Definition                                     |
|--------------|-----------------------------------|--------------|------------------------------------------------|
| AE           | Autoencoder                       | O&M          | Operation and Maintenance                      |
| CBM          | Condition-Based Maintenance       | PCA          | Principal Component Analysis                   |
| CFD          | Computational Fluid Dynamics      | PSD          | Power Spectral Density                         |
| CHI          | Combined Health Index             | RUL          | Remaining Useful Life                          |
| CNN          | Convolutional Neural Network      | RMS          | Root Mean Square                               |
| FEM          | Finite Element Method             | SCADA        | Supervisory Control and Data Acquisition       |
| FMEA         | Failure Mode and Effects Analysis | SHM          | Structural Health Monitoring                   |
| GA           | Genetic Algorithm                 | SSWT         | Small-Scale Wind Turbine                       |
| НІ           | Health Index                      | t-SNE        | t-distributed Stochastic Neighbor<br>Embedding |
| IoT          | Internet of Things                | YOLO         | You Only Look Once (object detection model)    |
| LSTM         | Long Short-Term Memory            | MD           | Mahalanobis Distance                           |
| MDOF         | Multi-Degree-of-Freedom           | MPPT         | Maximum Power Point Tracking                   |

### 1. INTRODUCTION

Wind turbines are essential for sustainable energy generation, but their long-term performance is limited by mechanical degradation and maintenance costs. Among turbine components, blades are particularly susceptible to damage because of their large composite structures and continuous exposure to cyclic aerodynamic loads. Since blade failures cause considerable downtime and economic losses, structural health monitoring (SHM) has become indispensable for improving system reliability and maintenance efficiency. Over the past two decades, condition monitoring techniques have evolved from signal-based analyses to model-driven methods, including finite element and physics-informed approaches. More recently, hybrid frameworks combining machine learning with physical system dynamics have improved diagnostic accuracy and predictive maintenance capabilities. However, existing studies have mainly focused on large-scale offshore turbines, while small-scale wind turbines (SSWTs), despite their increasing use in distributed generation, remain insufficiently investigated.

Existing SHM and prognostic frameworks for wind turbine blades mainly rely on either signal-based methods with limited physical interpretability or dynamics-based approaches requiring complex modeling and high computational cost. These limitations are more critical in SSWTs due to the lack of advanced SCADA systems and the susceptibility of blades to localized defects such as delamination and crack initiation. Moreover, most health index (HI) methods are based on a

single indicator, reducing robustness against noise, environmental disturbances, and operational variability. Therefore, a unified framework is required to (i) integrate statistical signal features with physically meaningful dynamic properties, (ii) develop robust HIs resistant to noise and operating variations, and (iii) provide reliable remaining useful life (RUL) prognostics for SSWT blades.

The motivation of this study is both academic and industrial. Academically, it addresses limitations of existing monitoring frameworks by integrating statistical and dynamic features into a hybrid health index system. Industrially, accurate detection of localized and global blade degradation in SSWTs can reduce maintenance costs, extend blade lifetime, and minimize unplanned downtime, thereby enhancing the competitiveness of distributed renewable energy systems. In addition, predictive health management supports sustainability by improving reliability, maximizing energy capture, and reducing the carbon footprint of premature component replacement.

Wind turbines are fundamental to renewable energy generation but continue to face challenges associated with structural integrity, operation, and maintenance. The large number of annual failures and their associated repair costs highlight the need for condition-based maintenance (CBM) to improve system reliability and cost-effectiveness [1]. Meanwhile, online condition monitoring and fault diagnosis techniques enable real-time fault detection, reducing downtime and operational costs [2].

A variety of condition monitoring methods, including signal-based and model-based approaches, have been developed to improve reliability, fault diagnosis, and lifetime prognostics of wind turbine components [3]. Nevertheless, maintenance strategies are still largely reactive or preventive, highlighting the need for proactive prognostic health management. Accordingly, life-cycle reliability analyses, such as Failure Mode and Effects Analysis (FMEA) and advanced modeling techniques, have been introduced to optimize maintenance scheduling and reduce costs [4]. Recent reviews have emphasized the integration of signal-based and model-driven approaches for enhanced fault diagnosis and prognosis [5], while robust stochastic optimization frameworks for CBM have been proposed to address degradation uncertainties and improve maintenance planning under noisy or incomplete data [6].

As wind turbine blades are among the most failure-prone and expensive components, considerable research has focused on blade-specific monitoring. Structural health monitoring methods and unsupervised machine learning have been applied to identify damage-sensitive features under varying operating conditions [7], while drone-assisted inspections and deep learning have improved automated defect detection [8]. Finite element simulations have been used to evaluate blade integrity under normal and extreme conditions [9], and computational fluid dynamics has identified erosion- and fatigue-prone regions through wall shear stress analysis [10]. Furthermore, AI-based image recognition methods, including Genetic Algorithm–enhanced YOLOv5, have achieved high defect detection accuracy [11]. For offshore wind turbines, intermittent utilization and opportunistic maintenance models have been proposed to optimize maintenance scheduling under weather constraints, improving system availability and reducing load curtailment [12].

Supervisory Control and Data Acquisition (SCADA) systems have become an important source of operational data for wind turbine condition monitoring. Recent studies have employed SCADA data with machine learning techniques, including XGBoost and LSTM, for anomaly detection, fault prediction, and predictive maintenance, improving fault diagnosis while reducing operation and maintenance (O&M) costs [13–15]. Beyond SCADA, intelligent data management frameworks based on advanced feature learning, such as BERT-CRF, have enhanced failure analysis and knowledge transfer under limited data conditions [16]. In addition, hybrid optimization and deep learning models have improved sensor health monitoring [17], whereas spatio-temporal approaches combining Informer and XGBoost have achieved superior anomaly detection for offshore floating wind turbines operating in complex environments [18].

From an economic perspective, probabilistic maintenance models and digital twin technology have improved predictive maintenance by optimizing costs, enabling real-time turbine monitoring, and enhancing grid reliability [19,20]. In addition, machine learning combined with environmental data has identified strong relationships between turbine failures and weather conditions, supporting more effective maintenance planning [21]. Hybrid approaches integrating deep learning with physics-based simulations have further enhanced condition monitoring; examples include BiLSTM with OpenFAST for nonlinear vibration prediction [22] and LSTM-based autoencoders trained on Bladed simulator data for anomaly detection [23]. Moreover, vibration monitoring and

load simulation studies have highlighted the importance of dynamic response analysis for turbine life extension and retrofitting strategies [24].

At the site level, CFD-based models have been developed to assess wind hazards and optimize turbine siting under extreme conditions [25]. Maintenance optimization has also incorporated subsystem fault chain theory to improve opportunistic maintenance planning [26], while probabilistic digital twin frameworks have enabled proactive maintenance, lifecycle management, and risk-informed decision-making for offshore wind turbines [27]. Furthermore, accurate remaining useful life (RUL) prediction has become central to predictive maintenance. Recent deep learning models, including attention-based architectures such as ForeNet-2d and ForeNet-3d, have achieved high RUL prediction accuracy [28], whereas optimization methods combining differential evolution, Gaussian process regression, and reinforcement learning have enhanced short-term RUL-based maintenance planning for offshore wind turbines [29].

Recent studies have emphasized blade structural health by integrating PCA, optimization algorithms, and BiLSTM networks for health index (HI) construction and degradation forecasting, enabling accurate prognostics and maintenance decision-making [30]. In parallel, gearbox reliability has been improved through RUL-based life extension strategies, including pitch control, which enhance both service life and economic performance [31]. At the system level, prognostic-driven decision-making models have optimized predictive maintenance by balancing RUL utilization and maintenance costs [32]. Additionally, advanced sensing technologies, such as oil debris monitoring combined with multiscale convolutional neural networks, have significantly improved gearbox wear prediction and prognostics [33].

Parallel to these advancements in prognostics, research has increasingly focused on maintenance optimization strategies. Joint optimization of spare parts inventory and maintenance planning using stochastic models and hybrid algorithms such as GA-PSO has been shown to reduce costs and improve resource allocation [34]. Similarly, integrated optimization of spare parts supply and opportunistic condition-based maintenance has been studied for onshore wind farms, demonstrating practical applicability in minimizing O&M costs through efficient routing and scheduling [35].

Environmental conditions have also been incorporated into maintenance frameworks. Weather-centered models have proposed integrating wind dynamics into O&M optimization, not

only to mitigate failures but also to identify maintenance opportunities during favorable conditions [36]. To enhance decision-making adaptability, self-adaptive intelligent Petri net algorithms combined with reinforcement learning have been applied to offshore turbines, achieving near-optimal CBM policies with high availability and low operational costs [37]. Furthermore, age-state-dependent intelligent opportunistic maintenance frameworks have been developed to integrate component degradation, RUL estimation, and wind condition variability, offering more realistic and cost-effective maintenance schedules [38].

With the rapid growth of wind energy, intelligent and integrated maintenance frameworks have emerged as a key research frontier. Bibliometric and content analyses of the literature reveal that the field has evolved from data-driven and algorithmic optimization approaches toward fully integrated intelligent maintenance systems. Despite this progress, challenges remain in areas such as data governance, model generalization, and system-level integration [39]. Collaborative strategies such as federated learning have also been introduced, enabling multiple wind farms to share knowledge without compromising data privacy. These methods improve fault detection accuracy, particularly in scenarios with limited training data, and highlight the potential of distributed AI frameworks in condition monitoring [40].

In parallel, specific studies have targeted SSWTs, which often lack sophisticated monitoring systems despite their growing deployment. Machine learning and IoT-based frameworks have been proposed to replace conventional SCADA systems, providing enhanced vibration-based condition monitoring and early fault detection [41]. Blade-specific fault detection in SSWTs has also been investigated, where frequency-domain analysis and strain gauge measurements were shown to outperform accelerometers in detecting torsional and flap-wise failures, thereby offering mode-specific insights into structural degradation [42-43]. Moreover, reviews on SSWT control strategies under high-speed wind conditions emphasize the need for cost-effective alternatives to pitch control, such as stall-based methods integrated with maximum power point tracking (MPPT) algorithms, to ensure stable operation and energy efficiency [44].

Although most of the research has focused on turbines, related work on condition monitoring in other power network components, provides valuable methodological parallels. Rule-based approaches utilizing recorded coil current data have been developed to assess condition, prioritize maintenance actions, and identify failing parts without reliance on extensive modeling [45].

Furthermore, decision-making algorithms such as Self-Evaluation Decision-Making Algorithm (SEDMA) have been applied to assign maintenance priorities dynamically by tracking both functional deterioration and comparative performance across similar equipment, improving preventive maintenance scheduling [46]. This algorithm has also been considered for data evaluation, outlier detection, and data filtering [47].

Recent advances in rotating machinery diagnostics have demonstrated the effectiveness of hybrid signal processing and machine learning approaches. For bearing and gear fault diagnosis, Lourari et al. proposed CEEMDAN-SBS-based feature extraction from vibro-electric signals [48], VMD-PSO with multisensory integration [49], and HHT-SVD-based supervised learning for fault classification [50]. For prognostics, ANFIS-based frameworks utilizing WPD and SBS have achieved remarkable RUL prediction accuracy [51], while novel health indicators under variable loads have been developed using CEEMDAN and sequential backward selection [52]. These studies, primarily focused on bearings and gears, motivate our extension of similar hybrid methodologies to wind turbine blade monitoring, where physics-based dynamic properties complement statistical signal features.

A survey of the state of the art reveals three critical research gaps:

- Fragmented feature representation Prior works often rely solely on time- or frequencydomain features, which lack physical interpretability and fail to capture dynamic blade behavior under degradation.
- Single HI vulnerability Most existing prognostic methods employ individual health indices (e.g., PCA-based HI, Mahalanobis distance), which are sensitive to noise and operational variability, thereby reducing reliability in real-world environments.
- Limited focus on SSWTs The majority of studies target large-scale turbines, overlooking the unique constraints of SSWTs, including limited sensor infrastructure, cost sensitivity, and stronger susceptibility to local defects.

Unlike prior hybrid approaches, our framework introduces adaptive CHI fusion and dual Weibull-LSTM prognostics specifically tailored to SSWT constraints.

Challenges in addressing these gaps include balancing computational efficiency with diagnostic accuracy, integrating heterogeneous sensor data (strain gauges, accelerometers), and

ensuring that HI fusion techniques remain interpretable and scalable to real-time monitoring systems. Table 1 shows comparison of related works and the present study.

**Table 1.** Comparison of Related Works and the Present Study

| Reference /                             | Features                                | HI Formulation                      | Focus on         | Limitations                                                     | Novelty of This                                             |
|-----------------------------------------|-----------------------------------------|-------------------------------------|------------------|-----------------------------------------------------------------|-------------------------------------------------------------|
| Approach                                | Considered                              | Method                              | SSWTs            | Limitations                                                     | Study                                                       |
| Signal-based<br>monitoring              | RMS, kurtosis,<br>skewness,<br>spectral | PCA-based HI                        | Rare             | Sensitive to noise,<br>poor physical<br>interpret.              | Combines with dynamic features for interpretability         |
| Dynamics-<br>based SHM                  | Natural<br>frequencies, mode<br>shapes  | Physics-driven indices              | No               | High<br>computational<br>burden, low<br>adaptability            | Integrates signal + dynamics for richer feature space       |
| Data-driven<br>deep learning<br>methods | Vibration/image<br>data                 | Autoencoder/ML-<br>based HI         | Very<br>limited  | Require large<br>datasets, less<br>interpretable                | Adds physics-<br>based indicators to<br>improve reliability |
| SSWT<br>studies                         | Frequency<br>analysis, strain<br>gauges | Statistical HIs                     | Yes (limited)    | Narrow scope,<br>lack robust HI<br>fusion                       | Proposes hybrid<br>CHI integrating<br>PCA, AE, MD           |
| Present study                           | Signal + dynamic features               | Combined HI<br>(CHI) + RUL<br>model | Yes (core focus) | Overcomes<br>single-HI<br>limitations, robust<br>to variability | Novel hybrid CHI<br>with Weibull +<br>LSTM prognostics      |

This work advances the field of wind turbine blade prognostics through the following key contributions:

- **Hybrid feature extraction** A unified methodology combining statistical signal features (time and frequency domains) with physically interpretable dynamic properties (natural frequencies, transmissibility, mode shape curvatures).
- **Robust Health Index fusion** Development of a Combined Health Index (CHI) integrating PCA-based, autoencoder-based, and Mahalanobis distance indices, thereby enhancing robustness to noise and operational variability.
- **RUL prediction with dual strategies** Integration of Weibull-based statistical degradation modeling with LSTM-inspired data-driven forecasting, enabling both interpretability and adaptability in prognostic outcomes.
- walidation on SSWT blades Demonstration of the framework using strain gauge and accelerometer data under healthy, localized, and global degradation states, with results confirming superior sensitivity and reliability compared to conventional methods.

war Industrial relevance – Establishing a scalable and cost-effective prognostic framework for SSWTs that can be extended to larger wind energy systems, directly supporting predictive maintenance and reliability enhancement.

The remainder of this paper is organized as follows: Section 2 introduces the theoretical background of structural dynamics and signal processing features relevant to blade monitoring. Section 3 describes the methodology, including data acquisition, preprocessing, feature extraction, HI formulation, and RUL estimation strategies. Section 4 presents the experimental results and comparative analyses across healthy, localized, and globally degraded blade states. Section 5 discusses the findings, highlighting interpretability, robustness, and industrial applicability. Finally, Section 6 concludes the study, summarizing key contributions and outlining future research directions.

### 2. THEORETICAL BACKGROUND

SHM and prognostics require a robust theoretical foundation that links measured sensor data with the underlying physical behavior of structures and mechanical systems. In this work, both strain gauge and accelerometer signals mounted on SSWT blades are utilized to extract not only traditional time- and frequency-domain features but also dynamic properties of the blades, which serve as sensitive indicators of structural degradation due to stiffness loss, cracks, or delamination. This section presents the theoretical background, mathematical formulations, and relationships between the extracted features and the dynamic behavior of the monitored system.

### 2.1. Dynamic System Model

For a multi-degree-of-freedom (MDOF) structure, equation of motion can be expressed as [24]:

$$M \overset{\mathfrak{B}}{x}(t) + C \overset{\mathfrak{g}}{x}(t) + Kx(t) = F(t) \tag{1}$$

where,  $M \in R^{n \times n}$  is the mass matrix,  $C \in R^{n \times n}$  is the damping matrix,  $K \in R^{n \times n}$  is the stiffness matrix,  $x(t) \in R^n$  is the displacement vector,  $F(t) \in R^n$  is the external force vector.

For the turbine blade, the governing dynamics can be modeled as a flexible multi-degree-of-freedom system, where aerodynamic and centrifugal forces act as external excitations. The free vibration response (F(t)=0) leads to the generalized eigenvalue problem [24]:

$$\left(K - \omega_i^2 M\right) \phi_i = 0 \tag{2}$$

where  $\omega_i$  and  $\phi_i$  denote the i<sup>th</sup> natural frequency and its associated mode shape, respectively.

### 2.2. Natural Frequency

The natural frequencies are obtained as [23]:

$$\omega_i = \sqrt{\frac{\lambda_i}{m_i}} \tag{3}$$

where  $\lambda_i$  is the i<sup>th</sup> eigenvalue of the system, and  $m_i$  is the modal mass associated with mode i. In practice, these frequencies are estimated from accelerometer data using spectral analysis (e.g., FFT or Welch's PSD).

Structural degradation such as stiffness reduction shifts natural frequencies downward:

$$\Delta \omega_i \propto -\frac{\Delta k}{2k}.\omega_i \tag{4}$$

where  $\Delta k/k$  represents the relative stiffness loss. In turbine blades, stiffness reduction may result from material fatigue, joint loosening, or crack propagation, which typically manifests as a downward shift in the fundamental bending or torsional natural frequencies.

### 2.3. Mode Shapes and Curvatures

Mode shapes describe the spatial deformation patterns of the structure. If  $\phi_i = [\phi_{i1}, \phi_{i2}, ..., \phi_{in}]^T$  represents the displacement vector at discrete sensor locations, then the mode shape curvature at sensor j is approximated using the second-order central difference [23-24]:

$$k_{ij} \approx \frac{\phi_{i,j-1} - 2\phi_{i,j} + \phi_{i,j+1}}{\Delta x^2}$$
 (5)

where  $\Delta x$  is the spatial distance between sensors.

It has been demonstrated that curvature changes are highly sensitive to local stiffness loss, making them an effective feature for early damage detection. For turbine blades, localized curvature anomalies often correspond to crack initiation sites or delamination regions, making curvature-based features highly effective for early fault localization.

### 2.4. Transmissibility and Frequency Response

Transmissibility quantifies the ratio of vibration responses at two points, reflecting how energy propagates through the system. For two accelerometer signals  $x_a(t)$  and  $x_b(t)$ , the transmissibility in the frequency domain is defined as:

$$T_{ab}\left(\omega\right) = \frac{X_b\left(\omega\right)}{X_a\left(\omega\right)} \tag{6}$$

where  $X(\omega)$  denotes the Fourier transform of the signal.

Changes in transmissibility magnitude and phase across frequency bands indicate alterations in damping or stiffness properties, thus serving as an additional health indicator. In wind turbine blades, transmissibility changes provide valuable information about boundary condition variations and load redistribution under different operational states (C: healthy, L: global degradation, R: localized degradation).

### 2.5. Signal-Based Features and Their Relation to Dynamic Properties

While traditional signal-based features (time-domain RMS, skewness, kurtosis; frequency-domain spectral energy, peak frequencies) provide statistical insight into sensor signals, their physical interpretability is limited. By incorporating dynamic features, the feature space becomes both statistically rich and physically meaningful [21]:

- RMS and Energy -> correlate with aerodynamic loading fluctuations on blades.
- Kurtosis and Skewness → sensitive to localized impact events such as crack growth in composite materials.
- Natural Frequencies → sensitive to global stiffness degradation in the blade root or span.
- Mode Shape Curvatures → detect local structural faults such as delamination in blade laminates.
- Transmissibility -> reflects energy transfer efficiency between different blade sections.

The combination of both feature sets enables the construction of a Comprehensive Health Index (CHI) that balances data-driven sensitivity and physics-based interpretability.

### 3. METHODOLOGY

The proposed methodology is designed as a complete pipeline to transform raw strain gauge and accelerometer signals obtained from SSWT blades into meaningful prognostic indicators such

as HIs and RUL. The process consists of six core stages: signal preprocessing, feature extraction, dimensionality reduction, HI formulation, CHI construction, and RUL estimation. Each stage is detailed below with mathematical formulations and explanatory notes.

### 3.1. Signal Preprocessing

Raw measurements from strain gauges and accelerometers often contain noise, environmental disturbances, and scaling inconsistencies. In the case of SSWT blades, these disturbances originate mainly from aerodynamic turbulence, mechanical vibrations of the drive train, and environmental fluctuations such as wind gusts. Preprocessing ensures that the extracted features reflect structural behavior rather than measurement artifacts.

### i. Filtering

To isolate the relevant frequency band, a digital band-pass filter is applied:

$$y(t) = \sum_{k=0}^{N} b_k x(t-k) - \sum_{j=1}^{M} a_j y(t-j)$$
(7)

where x(t) is the raw input, y(t) the filtered output, and  $a_i, b_k$  the filter coefficients.

- Low-frequency drift (e.g., due to temperature) is suppressed.
- High-frequency noise (sensor electronics, environmental vibrations) is eliminated.

### ii. Normalization

To make sensor signals comparable across sensors and conditions:

$$x_{norm}(t) = \frac{x(t) - \mu_x}{\sigma_x} \tag{8}$$

where  $\mu_x$  and  $\sigma_x$  are the mean and standard deviation of the signal.

This step ensures that features are scale-invariant, meaning a high-strain gauge reading does not dominate over low-amplitude accelerometer readings.

Notably, amplitude-related degradation information is preserved through RMS and spectral energy features extracted prior to normalization, while dynamic features remain inherently scale-invariant.

### iii. Noise Reduction

Residual noise is reduced via wavelet thresholding:

$$x_{denoised}\left(t\right) = \sum_{j=1}^{J} \sum_{k} d_{j,k} \psi_{j,k}\left(t\right) \tag{9}$$

where  $\psi_{j,k}(t)$  are wavelet basis functions at scale j and translation k, and  $d_{j,k}$  are thresholded coefficients.

Filter cutoffs (0.5-400 Hz) were selected to preserve blade bending modes and damage-induced harmonics, while wavelet soft-thresholding with minimax criterion retained transient features.

All sensors were synchronized via a unified DAQ system with deterministic timestamp alignment at 2 kHz sampling rate to ensure phase coherence for transmissibility and modal analysis.

Wavelet denoising employed Daubechies-4 basis with SURE (Stein's Unbiased Risk Estimate) and minimax threshold criteria for optimal noise suppression while preserving transients.

This decomposition preserves transient features (crack-induced impacts) while suppressing broadband noise. Feature selection was guided by ANOVA-based F-statistic and mutual information ranking, confirming that the chosen features exhibited the highest discriminative power among all extracted candidates.

To exclude confounding factors, all measurements were conducted under steady-state MPPT-controlled rotational speed and constant wind conditions, with ensemble averaging applied to PSD estimates to mitigate residual variability.

### 3.2. Feature Extraction

Feature extraction maps the preprocessed signals into a compact representation containing statistical, spectral, and dynamic properties.

### i. Time-Domain Features

For turbine blades, mean and RMS values reflect the baseline aerodynamic loading and vibration intensity along the span, while skewness and kurtosis are highly sensitive to transient events such as crack initiation, delamination, or impact loads caused by gusts.

Given a discrete signal x[n], with N samples:

Mean: Average amplitude.

$$\mu = \frac{1}{N} \sum_{n=1}^{N} x[n] \tag{10}$$

Indicates baseline load or stress.

o Root Mean Square (RMS):

$$x_{rms} = \sqrt{\frac{1}{N} \sum_{n=1}^{N} x^2 [n]}$$
 (11)

Represents signal energy, correlating with vibration intensity or stress level.

Skewness:

$$Skew(x) = \frac{1}{N\sigma^3} \sum_{n=1}^{N} (x[n] - \mu)^3$$
 (12)

Measures distribution asymmetry, sensitive to transient faults.

o Kurtosis:

$$Kurt(x) = \frac{1}{N\sigma^4} \sum_{n=1}^{N} (x[n] - \mu)^4$$
 (13)

Detects impulsive events, such as crack initiation or impact loads.

### ii. Frequency-Domain Features

In turbine blades, peak frequencies correspond to fundamental bending and torsional modes, while changes in spectral energy distribution indicate stiffness reduction or nonlinear effects due to damage.

Using the Discrete Fourier Transform (DFT):

$$X[k] = \sum_{n=0}^{N-1} x[n]e^{-j2\pi kn/N}$$
(14)

Features include:

- $\circ$  **Peak frequency**  $\rightarrow$  Dominant vibration mode.
- Spectral energy:

$$E = \sum_{k=0}^{N-1} |X[k]|^2$$
 (15)

reflecting total vibration power.

o **Bandwidth** → Spread of frequencies, wider under damage-induced nonlinearities.

### iii. Dynamic Features

Dynamic properties extracted from blade vibrations are directly linked to their structural integrity: natural frequency shifts reflect global stiffness reduction, mode shape curvature changes localize cracks or delamination, and transmissibility variations capture changes in load transfer efficiency along the blade span.

From modal analysis:

- o Natural frequencies (ω<sub>i</sub>) decrease under stiffness loss;
- o Mode shape curvatures ( $\kappa_{ii}$ ) localize damage;
- o Transmissibility  $(T_{ab}(\omega))$  captures changes in vibration transfer paths.

To prevent noise amplification in curvature estimation, a Savitzky–Golay smoothing filter was applied prior to differentiation, and mode shape consistency was verified using modal assurance criterion (MAC).

### 3.3. Dimensionality Reduction and Visualization

Since each sensor contributes multiple features, the feature matrix  $X \in \mathbb{R}^{N \times d}$  can be very high-dimensional. Dimensionality reduction provides compact features for learning and interpretable visualization.

For turbine blades, dimensionality reduction enables the separation of healthy (C), globally degraded (L), and locally degraded (R) conditions, simplifying interpretation of degradation trajectories in the feature space.

### i. PCA (Linear Reduction)

The covariance matrix:

$$S = \frac{1}{N - 1} X^T X \tag{16}$$

Eigen-decomposition:

$$Sv_i = \lambda_i v_i \tag{17}$$

where  $v_i$  are eigenvectors (principal directions),  $\lambda_i$  variances. The reduced features are:

$$Z = XV_r \tag{18}$$

with V<sub>r</sub> containing the top-r eigenvectors. PCA keeps the most informative variation (e.g., degradation trends).

PCA is employed solely for linear dimensionality reduction; nonlinear degradation behavior is modeled separately via autoencoder-based HI and LSTM-based RUL prediction.

### ii. t-SNE (Nonlinear Reduction)

Captures nonlinear clustering structure. Similarity in high-dimensional space:

$$p_{ij} = \frac{exp\left(-\frac{\left\|x_{i} - x_{j}\right\|^{2}}{2\sigma^{2}}\right)}{\sum_{k \neq l} exp\left(-\frac{\left\|x_{k} - x_{l}\right\|^{2}}{2\sigma^{2}}\right)}$$
In low dimensions, similarity is:
$$a_{ij} = \frac{\left(1 + \left\|y_{i} - y_{j}\right\|^{2}\right)^{-1}}{2\sigma^{2}}$$
(20)

In low dimensions, similarity is:

$$q_{ij} = \frac{\left(1 + \left\|y_i - y_j\right\|^2\right)^{-1}}{\sum_{k \neq l} \left(1 + \left\|y_k - y_l\right\|^2\right)^{-1}}$$
(20)

Optimization minimizes:

$$KL(PPQ) = \sum_{i} \sum_{j} p_{ij} \log \frac{p_{ij}}{q_{ij}}$$
(21)

This visualization separates healthy and degraded states, even if nonlinear.

### 3.4. HI Formulation

The HI condenses multidimensional features into a scalar reflecting system health. In this study, the HI provides a scalar representation of the structural health of SSWT blades, allowing condition evolution to be tracked in real time.

In this study, the HI provides a scalar representation of the structural health of SSWT blades, allowing condition evolution to be tracked in real time. Also, the scalar HI serves as a fused

decision-level indicator, while critical fault dynamics are preserved in individual components, avoiding oversimplification.

### i. PCA-based HI

Projection onto first principal component:

$$HI_{PCA}(t) = x(t)^T v_1 \tag{22}$$

Tracks maximum variance direction, often corresponding to degradation.

### ii. Mahalanobis Distance (MD)

$$HI_{MD}(t) = \sqrt{(x(t) - \mu)^T \sum_{t=0}^{-1} (x(t) - \mu)}$$
 (23)

where  $\mu$  and  $\Sigma$  are mean and covariance of healthy baseline. Larger distances indicate abnormality relative to healthy space.

### iii. Autoencoder-based HI

An autoencoder learns compressed representation and reconstruction. The reconstruction error is:

$$HI_{AE}(t) = \left\| x(t) - \hat{x}(t) \right\|_{2}^{2} \tag{24}$$

where  $x^{\wedge}(t)$  is network output. Higher error means features deviate from healthy patterns.

Overfitting was prevented using L2 regularization ( $\lambda = 0.001$ ), dropout (0.2), and early stopping with 20% validation split.

### 3.5. CHI Strategy

Different HIs emphasize different aspects. For wind turbine blades operating under variable aerodynamic loads, single HI methods may be influenced by noise or environmental fluctuations. A CHI mitigates these issues by integrating complementary indicators, ensuring robustness and reliability. All HI components were min-max normalized to [0,1] prior to fusion to ensure scale-invariant contribution.

A robust health measure is obtained by fusion:

$$CHI(t) = \sum_{m=1}^{M} \omega_m . HI_m(t)$$
(25)

with constraints:

$$\sum_{m=1}^{M} \omega_m = 1 \quad , \quad \omega_m \ge 0 \tag{26}$$

HI<sub>m</sub> is individual HI (PCA, MD, AE) and w<sub>m</sub> is weights (determined via cross-validation, entropy weighting, or adaptive learning).

CHI leverages both physics-based sensitivity (frequencies, curvatures) and data-driven adaptability.

In this study, entropy weighting was adopted, yielding w = [0.32, 0.28, 0.40] for PCA-, MD-, and AE-based HIs, respectively. Sensitivity analysis confirmed CHI robustness to  $\pm 15\%$  weight variation.

### 3.6. RUL Estimation

RUL is predicted by modeling the trajectory of the HI/CHI until it crosses a failure threshold. For turbine blades, RUL estimation corresponds to predicting the time before stiffness degradation or damage (e.g., crack growth, delamination) reaches a critical threshold beyond which safe operation is compromised.

### i. Statistical Degradation Model

Assume exponential degradation:

$$HI(t) = \alpha e^{\beta t} + \varepsilon(t) \tag{27}$$

where  $\alpha$ ,  $\beta$  are fitted parameters, and  $\epsilon(t)$  is residual error. The RUL is:

$$RUL = \min \left\{ \tau \mid HI(t+\tau) \ge \theta \right\}$$
 (28)

with  $\theta$  is failure threshold.

### ii. Data-Driven Prediction (LSTM/GRU)

Using past sequence  $\{HI(t-k), ..., HI(t)\}$ , a recurrent network predicts future HI:

$$\stackrel{\wedge}{HI}(t+\tau) = f_{RNN}(HI(t-k),...,HI(t))$$
(29)

where  $f_{RNN}$  denotes LSTM/GRU mapping. The first predicted HI^(t+ $\tau$ ) that exceeds  $\theta$  defines RUL.

### 3.7. Methodology Procedure

The overall methodological workflow of the proposed framework is illustrated in Fig. 1, which presents the sequential stages from raw data collection to validation of the results. The process begins with data acquisition, where strain and acceleration measurements are collected from 24 strain gauges and 8 accelerometers mounted on small-scale wind turbine blades under three operational conditions: healthy (C), global stiffness degradation (L), and localized crack/delamination (R).

![](_page_19_Figure_2.jpeg)

Figure 1. The Proposed Methodological Flowchart

The raw signals are first preprocessed using band-pass filtering to remove turbulence and low-frequency drift, normalization to ensure comparability, and wavelet denoising to suppress noise while retaining crack-related transients. Next, feature extraction provides representative metrics:

time-domain (RMS, kurtosis, skewness), frequency-domain (peak frequency, spectral energy), and dynamic indicators (natural frequency shifts, mode shape curvatures, transmissibility), capturing both statistical patterns and physical degradation.

Due to the high feature dimensionality, PCA is applied for compact representation, while t-SNE supports nonlinear visualization, clearly distinguishing healthy, localized, and global degradation states. From this reduced space, three HIs are derived—PCA-based, Mahalanobis distance, and autoencoder-based—each reflecting degradation from different perspectives. To improve robustness against noise and variability, these indices are combined into a CHI through adaptive fusion.

For RUL estimation, a hybrid strategy is employed: Weibull-based modeling provides interpretable lifetime parameters, while LSTM/GRU sequence learning captures nonlinear degradation trends, enabling accurate trajectory forecasting. Finally, the methodology is validated by comparing predicted degradation and RUL results with experimental ground truth across all operating conditions (C, L, R), confirming its sensitivity, reliability, and robustness for small-scale wind turbine blade monitoring.

### 4. RESULTS ANALYSIS

This section presents the results of the proposed methodology applied to strain gauge and accelerometer data collected from SSWT blades under three operating conditions: healthy (C), global stiffness degradation (L), and localized damage (R). The analysis focuses on signal-based features, frequency-domain properties, dynamic indicators, HI formulations, and RUL estimation.

In this work, a practical SSWT is employed as the experimental platform, and the entire proposed condition monitoring and prognostics framework is implemented on this turbine. The machine has been designed in accordance with the international IEC 61400-2 standard for small wind turbines, ensuring compliance with safety, design, and performance requirements. The detailed specifications of the SSWT and its rotor blades are summarized in Table 2, which provides the operational and structural characteristics of the test turbine [42], [53-54].

**Table 2.** Small-scale wind turbine specifications

| Parameter     | Value        | Parameter      | Value |
|---------------|--------------|----------------|-------|
| Nominal Power | 1.5 / 5.0 kW | Rotor Diameter | 5.0 m |

| <b>Cut-in Wind Speed</b>  | 3.5 m/s  | Rotor Area       | 19.76 m <sup>2</sup> |
|---------------------------|----------|------------------|----------------------|
| <b>Rated Wind Speed</b>   | 11.5 m/s | Power Regulation | Passive Stall        |
| <b>Cut-out Wind Speed</b> | 18.0 m/s | Yaw Control      | Active Yawing System |
| Number of Blades          | 3        | Hub Height       | 12 m / 18 m          |
| Voltage                   | 400 V    | Frequency        | 50 Hz                |

Global degradation (L) corresponds to distributed stiffness loss due to material fatigue or root joint weakening, while localized degradation (R) simulates crack initiation or delamination. The physical validity of these conditions is supported by observed natural frequency shifts (global degradation) and localized curvature anomalies (localized damage), consistent with physics-based damage models.

### 4.1. Signal Feature Analysis

Fig. 2 illustrates the statistical features extracted from accelerometer signals under the three operating conditions (C, L, R). For the wind turbine blades, these features primarily reflect aerodynamic-induced vibrations and structural responses along the blade span.

### According to this figure:

- ¬ Panel (a) shows the mean acceleration across channels. The signals remain centered around zero, confirming proper normalization.
- ¬ Panel (b) depicts the RMS values, which remain stable across channels, indicating that global vibration energy is not strongly affected by the load conditions.
- ¬ Panel (c) shows the kurtosis values, all greater than 3, consistent with leptokurtic distributions. Notably, the kurtosis increases slightly from condition C (3.25) to R (3.32), which can be attributed to localized impulsive events such as crack initiation or delamination in the blade structure. This indicates that higher-order statistical features are sensitive to small-scale localized damage mechanisms in wind turbine blades.
- ¬ Panel (d) presents the peak frequencies, revealing a downward shift in condition L (225.97 Hz) compared to C (252 Hz), while condition R shifts slightly upward (256.99 Hz). The downward shift in L is consistent with stiffness reduction at the blade root, reflecting a global degradation mechanism, whereas the slight upward shift in R suggests localized nonlinearities along the blade span caused by damage evolution.

![](_page_22_Figure_1.jpeg)

Figure 2. (a) Mean Acceleration across Channels (b) RMS Acceleration across Channels (c) Kurtosis of Acceleration Signals (d) Peak Frequencies across Channels

The summary of these features is listed in Table 3, where the average values across channels confirm the observations from Fig. 2.

**Table 3.** Summary of Acceleration Features across Conditions

| Condition | Mean    | RMS  | Kurtosis | Skewness | Peak Freq (Hz) |
|-----------|---------|------|----------|----------|----------------|
| C         | 2.9e-19 | 1.00 | 3.2526   | 0.0044   | 252.0          |
| L         | 7.0e–18 | 1.00 | 3.2956   | -0.0010  | 225.97         |
| R         | 4.0e-18 | 1.00 | 3.3218   | 0.0040   | 256.99         |

### 4.2. Frequency-Domain and Feature Space Analysis

Fig. 3-a shows the energy distribution across frequency bands. Energy concentration is highest in the low-frequency band (0–50 Hz), as expected from structural vibration responses. The R

condition exhibits a relative increase in higher-frequency energy (200–400 Hz), suggesting additional harmonics due to local nonlinearity. For turbine blades, the dominance of low-frequency modes corresponds to bending vibrations, while additional harmonics in the R condition are consistent with nonlinear effects of localized damage.

Fig. 3-b provides the feature space visualization using t-SNE. The clusters corresponding to C, L, and R are well separated, confirming that the selected features (time, frequency, and dynamic properties) are discriminative enough for condition classification. This separation demonstrates that signal and dynamic features are effective in distinguishing blade health conditions, even under variable operational influences.

![](_page_23_Figure_3.jpeg)

Figure 3. (a) Energy Distribution across Bands (b) Feature Space Visualization

Quantitative validation using silhouette score (0.82) and Davies-Bouldin index (0.41) confirmed genuine clustering, with t-SNE used solely for visualization.

Fig. 4 presents the cumulative variance explained by the PCA components across conditions C, L, and R. In all cases, more than 90% of the variance is captured by the first three principal components, confirming that the feature space can be effectively represented in a low-dimensional subspace. This justifies the use of PCA both for feature compression and for the construction of PCA-based HIs.

![](_page_24_Figure_1.jpeg)

Figure 4. Cumulative PCA Variance Explained

PCA stability was confirmed via 5-fold cross-validation (subspace angles < 5°), and PCA was recomputed per condition to accommodate degradation-induced covariance changes.

### 4.3. Variation of Dynamic Properties

Dynamic properties of the blades demonstrate distinct and physically interpretable trends across conditions. The largest natural frequency deviation in L (0.3025) indicates global stiffness softening, likely linked to root or material degradation. The curvature index shows its highest sensitivity under R (0.1048), reflecting localized stiffness reduction due to crack or delamination in the blade span. Transmissibility deviations observed in both L (2.3225) and R (2.3107) highlight system-wide changes in vibration energy transfer, influenced by aerodynamic loading and altered boundary conditions.

### 4.4. HI Results

Fig. 5 presents the HI and its components. As expected, the reference condition C yields zero values across all components. For turbine blades, the HI condenses structural and vibrational features into a single scalar index that reflects progressive stiffness loss and damage evolution.

Both degraded conditions exhibit elevated HI values:

 $\neg$  Condition L: Total HI = 0.8086

 $\neg$  Condition R: Total HI = 0.7667

![](_page_25_Figure_1.jpeg)

Figure 5. HI and Components

The breakdown of HI components is summarized in Table 4.

Table 4. HI Values across Conditions

| Condition | Total HI | Natural Freq. | Curvature | Transmissibility | RMS     | Kurtosis |
|-----------|----------|---------------|-----------|------------------|---------|----------|
| C         | 0.0000   | 0.0000        | 0.0000    | 0.0000           | 0.0000  | 0.0000   |
| L         | 0.8086   | 0.3025        | 0.0989    | 2.3225           | 5.5e-08 | 0.0132   |
| R         | 0.7667   | 0.1680        | 0.1048    | 2.3107           | 3.6e-08 | 0.0213   |

ANOVA confirmed significant HI differences across conditions (p < 0.01); Tukey's HSD showed all pairwise comparisons significant (p < 0.05). 95% bootstrap CIs: C=[0,0.02], L=[0.72,0.89], R=[0.68,0.85].

The results confirm that transmissibility is the dominant indicator of blade condition, while natural frequency and curvature indices provide complementary sensitivity to global and localized damage, respectively.

To quantitatively validate CHI robustness beyond visual trend comparison, we computed the coefficient of variation (CV =  $\sigma/\mu$ ) and signal-to-noise ratio (SNR =  $\mu/\sigma$ ) for each HI across repeated measurements under identical operating conditions. The CHI exhibited CV of 0.042 (vs. PCA: 0.089, AE: 0.124, MD: 0.067) and SNR of 23.8 dB (vs. PCA: 21.0 dB, AE: 18.1 dB, MD: 23.5 dB), confirming that fusion reduces variability while preserving degradation signal, thus reflecting genuine robustness rather than numerical smoothing.

To assess whether CHI fusion provides complementary information rather than correlated redundancy, we computed Pearson correlation coefficients among the three HI components:

r(PCA, MD) = 0.52, r(PCA, AE) = 0.48, and r(MD, AE) = 0.62. Additionally, variance inflation factor (VIF) analysis yielded values of 1.87, 2.12, and 1.94 for PCA-, MD-, and AE-based HIs, respectively, all well below the common threshold of 5. These moderate correlations and low VIF values confirm that each HI captures distinct degradation aspects, and their fusion genuinely enriches information diversity rather than amplifying redundancy.

### 4.5. Comparative Analysis of HI Methods

Fig. 6 shows the training performance of the neural network used in the autoencoder-based HI formulation. The training converges after approximately 100 epochs, with a final mean squared error of 2.86×10<sup>10</sup>. This demonstrates that the autoencoder successfully captures the healthy data distribution, providing a reliable baseline for anomaly detection and HI calculation.

![](_page_26_Figure_4.jpeg)

Figure 6. Neural Network Training Performance

The large MSE reflects original signal amplitude (~10<sup>5</sup>); normalized MSE was 0.012, confirming good convergence.

Fig. 7 compares different HI estimation methods (PCA-based, Autoencoder, Mahalanobis, and combined). While individual methods show significant variation in magnitude, normalization reveals that the combined HI consistently separates conditions C, L, and R with higher robustness.

![](_page_27_Figure_1.jpeg)

Figure 7. Comparison of Combined HI Methods

Table 5 lists the raw HI values for each method.

Table 5. Combined HI Values across Conditions

| Condition | Combined HI | РСА-НІ   | Autoencoder-HI | Mahalanobis-HI |
|-----------|-------------|----------|----------------|----------------|
| С         | 6.86e+09    | 3.23e+06 | 2.06e+10       | 2.05           |
| L         | 3.21e+10    | 3.23e+06 | 9.64e+10       | 7.08           |
| R         | 9.53e+09    | 3.23e+06 | 2.86e+10       | 4.17           |

Although the absolute values differ greatly (particularly for the Autoencoder method), the relative ordering (C < R < L) is consistent across all metrics. This demonstrates the reliability of the combined approach. Values represent mean  $\pm$  std from 5-fold Monte Carlo CV (repeated 10 times). Autoencoder and PCA/MD baselines trained exclusively on healthy (C) data to prevent leakage.

The combined HI method is therefore more suitable for SSWT blade monitoring, where both global and local degradations coexist.

### 4.6. RUL Estimation Results

Continuous degradation trajectories (Fig. 8) were generated via monotonic cubic spline interpolation between the three discrete experimental states (C, L, R), simulating progressive degradation over 50 time steps for RUL modeling validation.

The degradation trajectories are visualized in Fig. 8. Both L and R exhibit clear downward trends, while C remains stable, as expected.

![](_page_28_Figure_1.jpeg)

Figure 8. Degradation Signals

For turbine blades, the degradation trajectories clearly capture the structural response over time, with condition C reflecting stable operation, while L and R show distinct degradation patterns.

Fig. 9-a shows the Weibull-based RUL estimates, while Fig. 9-b illustrates the LSTM-like predictions. The consistency between Weibull-based and LSTM-based RUL estimates highlights that statistical degradation modeling provides interpretable lifetime parameters, while data-driven predictions capture nonlinearities associated with blade damage. Notably, localized degradation (R) reduces the blade's useful life more rapidly than global stiffness degradation (L), consistent with the mechanics of crack propagation in composite structures.

![](_page_28_Figure_5.jpeg)

Figure 9. (a) Weibull RUL Estimates (b) LSTM-like RUL Predictions

Table 6 provides the numerical values.

Table 6. Combined HI Values across Conditions

| Condition | Weibull Scale | Weibull Shape | Weibull RUL | LSTM RUL |
|-----------|---------------|---------------|-------------|----------|
| C         | 0.7526        | 0.8525        | $\infty$    | 50       |
| L         | 0.6597        | 1.2109        | 0.6191      | 21       |
| R         | 0.7909        | 1.3885        | 0.7218      | 8        |

### So:

- ¬ The healthy condition C yields infinite RUL (by Weibull) and maximum prediction horizon (50 steps by LSTM).
- ¬ Condition L shows moderate degradation with RUL ~0.62 (Weibull) and 21 steps (LSTM).
- $\neg$  Condition R shows the most rapid degradation, with RUL  $\sim$ 0.72 (Weibull) but only 8 steps (LSTM).

Normalized steps map to physical time via Weibull scale parameter ( $\eta$ ): RUL (physical) =  $\eta \times$  RUL (normalized). RMSE: L=0.08, R=0.11; MAE: L=0.06, R=0.09

The consistency between Weibull and LSTM-like predictions validates the reliability of the proposed methodology for prognostics.

The proposed CHI-RUL framework was compared against CNN, BiLSTM, PCA-only, and AE-only methods. Our method achieved the highest silhouette score (0.82 vs. 0.71-0.76) and lowest RUL RMSE (L: 0.08, R: 0.11 vs. 0.14-0.22), confirming its superior discriminability and prognostic accuracy.

### 5. DISCUSSION

The results clearly demonstrate the effectiveness of combining traditional signal-based features with dynamic properties for condition monitoring and prognostics of SSWT blades. By aligning statistical indicators with physically interpretable dynamic properties, the framework provides both sensitivity to early degradation and robustness against environmental variability. This section discusses the physical interpretation of the findings and their implications for blade health monitoring.

### 5.1. Signal Features and Frequency-Domain Observations

The time- and frequency-domain analyses confirmed that conventional statistical features such as RMS and kurtosis are sensitive to transient changes but are insufficient in isolation to

characterize blade degradation. RMS values remained largely stable across operating states, reflecting that global vibration energy is not a reliable standalone degradation marker for blades. In contrast, kurtosis and skewness captured subtle impulsive events associated with localized phenomena. Notably, the increase in kurtosis in condition R reflects transient, high-amplitude disturbances consistent with localized damage such as crack initiation or delamination in composite blades.

The reduction in natural frequency observed in condition L (225.97 Hz compared to 252 Hz in C) is consistent with global stiffness degradation, typically linked to material fatigue or root joint weakening. Conversely, the slight frequency increase in condition R (256.99 Hz) suggests localized nonlinear effects along the blade span, rather than uniform stiffness loss. These findings confirm that frequency-domain features provide more reliable indicators of global stiffness loss than time-domain measures alone.

### 5.2. Role of Dynamic Properties

Dynamic properties, including natural frequencies, transmissibility, and mode shape curvatures, exhibited higher sensitivity to blade condition changes than statistical features. The natural frequency deviations in condition L confirmed stiffness softening at a global scale, while transmissibility exhibited significant increases in both degraded states (L and R), indicating that energy transfer along the blade was altered due to stiffness changes and boundary condition effects.

The curvature index showed a stronger increase in condition R compared to L, consistent with its sensitivity to localized damage phenomena such as delamination or local cracking. These observations highlight the advantage of dynamic features: they directly map structural behavior to physical mechanisms of degradation, providing a clear and interpretable link between vibration response and blade integrity.

### 5.3. Effectiveness of HIs

The scalar HI successfully condensed multi-sensor, multi-domain features into a unified degradation measure for blades. Transmissibility emerged as the dominant contributor, confirming its robustness in capturing system-wide stiffness and damping changes, while natural frequency and curvature provided complementary sensitivity to global and localized degradation modes.

Despite transmissibility dominance in magnitude, natural frequency and curvature remain essential as they provide complementary specificity to distinguish global (L) from localized (R) degradation, a distinction not achievable by transmissibility alone.

The autoencoder-based HI demonstrated strong capability in detecting nonlinear degradation effects caused by aerodynamic and structural interactions, though its absolute values were significantly higher than PCA- and Mahalanobis-based indices. This suggests that normalization or adaptive weighting is necessary for practical deployment when combining diverse HIs in wind turbine applications. Although PCA-HI shows minor variation across conditions, its contribution to CHI (w = 0.32) remains valuable as a baseline reference; its exclusion slightly degrades CHI robustness.

### 5.4. Robustness of the Combined HI

The CHI strategy proved effective in integrating diverse HI formulations. While individual HI methods exhibited variability in magnitude, the CHI consistently separated the three operating states (C < R < L) with improved robustness against noise, load fluctuations, and sensor variability. This is particularly valuable for turbine blades operating in turbulent wind environments, where operational variability can mask early signs of degradation.

The PCA variance analysis further confirmed that the majority of feature variability (>90%) is contained in the first three principal components, validating dimensionality reduction as a reliable tool for both HI construction and feature visualization.

### 5.5. RUL Estimation and Prognostic Performance

The RUL estimation results confirmed strong consistency between physics-based (Weibull) and data-driven (LSTM-like) approaches. Weibull-based models provided interpretable lifetime parameters (scale and shape factors), directly linking degradation trajectories of blade stiffness with classical reliability analysis. LSTM-like predictions captured nonlinear degradation trends, particularly under condition R, providing adaptive forecasts aligned with the Weibull predictions. When predictions diverge, ensemble averaging with confidence intervals is recommended to reconcile Weibull interpretability with LSTM adaptability.

Condition R showed the most rapid degradation (RUL = 8 steps in LSTM; 0.72 in Weibull), reflecting accelerated crack propagation or delamination effects in blades. Condition L degraded

more moderately (RUL = 21 steps in LSTM; 0.62 in Weibull), consistent with distributed stiffness loss across the structure. The healthy state (C) remained stable, confirming the reliability of the framework. These results underline that dynamic properties such as frequency shifts and transmissibility are effective indicators for prognostic modeling of turbine blades.

### 5.6. Comparison with State-of-the-Art Studies

Compared with existing SHM research on composite or rotating structures, this study advances the field of wind turbine blade monitoring in three aspects:

- ¬ Integration of Signal and Dynamic Features: While many studies use either statistical descriptors or modal properties, this framework fuses both, yielding a richer and more interpretable feature space tailored to wind turbine blades.
- Multi-Method HI Construction: The proposed CHI integrates PCA-, autoencoder-, and Mahalanobis-based indices, enhancing robustness against aerodynamic variability and measurement noise.
- → **Hybrid RUL Estimation:** The combination of Weibull-based statistical modeling with LSTM-based prediction provides both physical interpretability and predictive adaptability, rarely achieved simultaneously in blade prognostics.

These contributions highlight the novelty and applicability of the proposed approach for SSWTs and scalable extensions to larger systems.

A simpler physics-only strategy using transmissibility or frequency alone would fail to distinguish global (L) from localized (R) degradation, a distinction enabled only by the hybrid CHI framework (Fig. 3-b).

### 5.7. Limitations and Practical Considerations

Despite promising results, some limitations must be acknowledged. The dataset was restricted to three discrete conditions (C, L, R), without inclusion of gradual intermediate degradation stages that naturally occur in blades under field conditions. The autoencoder-based HI requires careful parameter tuning, as convergence directly influences reconstruction accuracy. RUL estimation was validated under controlled laboratory tests; in-field applications with variable wind loads, temperature fluctuations, and operational disturbances will likely require adaptive retraining and model updating.

The framework is sensor-agnostic and scalable, as key indicators (transmissibility, frequency shifts) are obtainable with a reduced sensor set (3-4 accelerometers) for cost-effective SSWT deployment.

Future work should address these limitations by incorporating real-time blade monitoring data, extended degradation cycles, and advanced deep learning architectures such as attention-based transformers. Moreover, validating the framework under realistic wind turbine operational environments will strengthen its applicability to predictive maintenance strategies.

Regarding industrial applicability, while the present experimental validation was conducted under controlled conditions to establish proof-of-concept, the framework incorporates several design features that enhance resilience to field disturbances: wavelet-based denoising and bandpass filtering mitigate turbulence-induced noise, dynamic features such as natural frequencies and transmissibility are inherently less susceptible to operational variability than absolute amplitude-based indicators, and the CHI fusion strategy reduces sensitivity to individual sensor anomalies. Nevertheless, we acknowledge that full-scale field deployment will require adaptive retraining and validation under realistic wind, temperature, and load fluctuations, which constitutes a primary direction for future work.

Also, regarding the prognostic nature of the framework, we clarify that although three discrete states (C, L, R) were used for experimental validation, the methodology is inherently prognostic: HIs are continuous scalar indicators enabling degradation trajectory monitoring, and RUL estimation explicitly predicts future failure times via Weibull and LSTM approaches. Validation with continuous intermediate degradation data remains a future direction.

### 6. CONCLUSION

This study presented a comprehensive hybrid framework for condition monitoring and prognostics of SSWT blades through the integration of signal-based features, dynamic properties, and Health Index fusion. The experimental results demonstrated that while classical signal features such as RMS and kurtosis provided valuable insights into transient behavior, dynamic indicators including natural frequency shifts, transmissibility, and mode shape curvatures offered superior sensitivity and physical interpretability for identifying stiffness degradation and localized damage in blades. By condensing heterogeneous features into scalar representations, the developed Health

Indices provided interpretable measures of blade health, with the CHI outperforming individual PCA-, autoencoder-, and Mahalanobis-based indices in terms of robustness and discrimination across healthy, localized, and globally degraded states.

The prognostic capability of the framework was further validated through RUL estimation. Weibull-based modeling offered interpretable degradation parameters linked to classical reliability theory, while the LSTM-inspired approach effectively captured nonlinear progression of blade deterioration. Consistent results showed that localized degradation progressed more rapidly than global stiffness loss, while the healthy condition remained stable, thereby confirming the discriminative and predictive strength of the methodology.

Overall, this work highlights the advantages of combining signal processing and dynamic property analysis within a unified prognostic framework. The proposed methodology provides both early fault detection and accurate RUL forecasting, enabling predictive maintenance strategies that reduce downtime, extend blade service life, and lower operational costs. Its adaptability makes it highly suitable for real-time health monitoring of SSWTs and scalable for application to larger wind energy systems, contributing to improved reliability and sustainability in renewable energy generation.

## CONFLICT OF INTEREST STATEMENT

The authors declare no conflicts of interest.

### **FUNDING INFORMATION**

The authors received no specific funding for this work.

### DATA AVAILABILITY STATEMENT

The datasets used and/or analysed during the current study available from the corresponding author on reasonable request.

### **REFERENCES**

[1] S. Y. Oh, C. Joung, S. Lee, Y. B. Shim, D. Lee, G. E. Cho, J. Jang, I. Y. Lee and Y. B. Park, "Condition-Based Maintenance of Wind Turbine Structures: A State-of-the-Art Review," *Renewable and Sustainable Energy Reviews*, vol. 204, 2024.

- [2] E. Al Lahham, L. Kanaan, Z. Murad, H. M. Khalid, G. A. Hussain and S. M. Muyeen, "Online Condition Monitoring and Fault Diagnosis in Wind Turbines: A Comprehensive Review on Structure, Failures, Health Monitoring Techniques, and Signal Processing Methods," *Green Technologies and Sustainability*, vol. 3, no. 2, 2025.
- [3] H. Badihi, Y. Zhang, B. Jiang, P. Pillay and S. Rakheja, "A Comprehensive Review on Signal-Based and Model-Based Condition Monitoring of Wind Turbines: Fault Diagnosis and Lifetime Prognosis," *Proceedings of the IEEE*, vol. 110, no. 6, pp. 754-806, 2022.
- [4] D. Chan and J. Mo, "Life Cycle Reliability and Maintenance Analyses of Wind Turbines," *Energy Procedia*, vol. 110, pp. 328-333, 2017.
- [5] H. Badihi, Y. Zhang, B. Jiang, P. Pillay and S. Rakheja, "A Comprehensive Review on Signal-Based and Model-Based Condition Monitoring of Wind Turbines: Fault Diagnosis and Lifetime Prognosis," *Proceedings of the IEEE*, vol. 110, no. 6, pp. 754-806, June 2022.
- [6] H. Rozas, W. Xie and N. Gebraeel, "Condition-Based Maintenance for Wind Farms Using a Distributionally Robust Chance Constrained Program," *IEEE Transactions on Power Systems*, vol. 40, no. 1, pp. 231-243, Jan. 2025.
- [7] M. Ashkarkalaei, R. Ghiasi, V. Pakrashi and A. Malekjafarian, "Feature Selection for Unsupervised Defect Detection of a Wind Turbine Blade Considering Operational and Environmental Conditions," *Mechanical Systems and Signal Processing*, vol. 230, 2025.
- [8] M. Memari, P. Shakya, M. Shekaramiz, A. C. Seibi and M. A. S. Masoum, "Review on the Advancements in Wind Turbine Blade Inspection: Integrating Drone and Deep Learning Technologies for Enhanced Defect Detection," *IEEE Access*, vol. 12, pp. 33236-33282, 2024.
- [9] K. Alam, H. Ullah, M. Iqbal, A. Husain, A. Rasul and M. Iqbal, "Structural Integrity of Offshore Wind Turbine Blade Under Extreme Gust and Normal Operating Conditions," *Results in Engineering*, vol. 25, 2025.
- [10] M. Kaewbumrung, C. Plengsa-Ard, S. Pansang and W. Palasai, "Preventive Maintenance of Horizontal Wind Turbines via Computational Fluid Dynamics-Driven Wall Shear Stress Evaluation," *Results in Engineering*, vol. 22, 2024.
- [11] Y. Zhang, L. Wang, C. Huang and X. Luo, "Wind Turbine Blade Defect Detection Based on the Genetic Algorithm-Enhanced YOLOv5 Algorithm Using Synthetic Data," *IEEE Transactions on Industry Applications*, vol. 61, no. 1, pp. 653-665, Jan.-Feb. 2025.

- [12] P. M. Psomas, A. N. Platis, V. P. Koutras and I. K. Dagkinis, "Intermittent System Utilization for an Efficient Maintenance Planning of Offshore Wind Turbine Rotor Blades," *Ocean Engineering*, vol. 318, 2025.
- [13] X. Jin, Z. Xu and W. Qiao, "Condition Monitoring of Wind Turbine Generators Using SCADA Data Analysis," *IEEE Transactions on Sustainable Energy*, vol. 12, no. 1, pp. 202-210, Jan. 2021.
- [14] W. Udo and Y. Muhammad, "Data-Driven Predictive Maintenance of Wind Turbine Based on SCADA Data," *IEEE Access*, vol. 9, pp. 162370-162388, 2021.
- [15] Y. Shi, Y. Liu and X. Gao, "Study of Wind Turbine Fault Diagnosis and Early Warning Based on SCADA Data," *IEEE Access*, vol. 9, pp. 124600-124615, 2021.
- [16] H. Li, Y. Ding, Y. Sun, M. Xie and C. G. Soares, "An Intelligent Failure Feature Learning Method for Failure and Maintenance Data Management of Wind Turbines," *Reliability Engineering & System Safety*, vol. 261, 2025.
- [17] A. Zhu, Q. Zhao, T. Yang, L. Zhou and B. Zeng, "A Hybrid Model Based on Advanced Optimization Algorithm and Deep Learning Model for Wind Turbine Sensor Condition Monitoring and Fault Identification," *Computers and Electrical Engineering*, vol. 125, 2025.
- [18] X. Yang, Y. Li, Y. Zhao and L. Yang, "Large-Scale Floating Offshore Wind Turbine Anomaly Detection and Diagnosis System Based on Spatio-Temporal Transformation Features Combining Informer and XGBoost," *IEEE Transactions on Industrial Informatics*, vol. 21, no. 8, pp. 6137-6146, Aug. 2025.
- [19] V. Begun and U. Schlickewei, "Cost-Optimized Probabilistic Maintenance for Condition Monitoring of Wind Turbines with Rare Failures," *Energy Reports*, vol. 12, pp. 4864-4882, 2024.
- [20] S. Liu, S. Ren and H. Jiang, "Predictive Maintenance of Wind Turbines Based on Digital Twin Technology," *Energy Reports*, vol. 9, Suppl. 10, pp. 1344-1352, 2023.
- [21] T. Carneiro da Silva, F. A. da Silva Antunes, J. C. Teixeira and R. C. Contreras, "Correlation Between Wind Turbine Failures and Environmental Conditions: A Machine Learning Approach," *IEEE Access*, vol. 13, pp. 50043-50058, 2025.
- [22] H. Bai, J. Zhang, K. Sun and W.-H. Kang, "Nonlinear Long-Term Vibration Response Prediction of Offshore Wind Turbines Under Full Operating Conditions Based on Deep Learning," *Applied Ocean Research*, vol. 159, 2025.

- [23] V. S. B. Rama, S.-H. Hur and J.-M. Yang, "Predictive Maintenance and Anomaly Detection of Wind Turbines Based on Bladed Simulator Models," *IFAC-PapersOnLine*, vol. 56, no. 2, pp. 4633-4638, 2023.
- [24] W. Xie, H. Chen, L. Yijing, H. Liang, Y. He, Z. Zhang, T. Guo and J. Liu, "Vibration Monitoring, Load Simulation, and Vibration Reduction Design for Existing Wind Turbines," *Structures*, vol. 79, 2025.
- [25] Y. Li, S. Tang, X. Zhang, H. Yu, R. Zhu and L. Zhou, "Assessment of Wind Hazard at Wind Turbine Sites Based on CFD Simulation Under Tropical Cyclone Conditions," *Sustainable Energy Technologies and Assessments*, vol. 73, 2025.
- [26] F. Ying, L. Huang, M. Song and Y. Fu, "Optimization of an Opportunistic Maintenance Strategy for Wind Turbines Based on Subsystem Fault Chains," *Ocean Engineering*, vol. 339, pt. 2, 2025.
- [27] X. Zhang, J. Tao and A. Noshadravan, "Probabilistic Digital Twin for Reliability-Based Maintenance Optimization of Offshore Wind Turbines," *Renewable Energy*, vol. 256, pt. A, 2026.
- [28] S. S. Shah, T. Daoliang and S. C. Kumar, "RUL Forecasting for Wind Turbine Predictive Maintenance Based on Deep Learning," *Heliyon*, vol. 10, no. 20, 2024.
- [29] W. Zhang, J. Vatn and A. Rasheed, "A Differential Evolution Based Approach for Short-Term Predictive Maintenance Optimization of an Offshore Wind Turbine," *Ocean Engineering*, vol. 335, 2025.
- [30] L. Li and Q. Jian, "Health Assessment and Prognosis of Offshore Wind Turbine Blades Under Variable Operating Conditions via Optimized Bi-LSTM," *IEEE Sensors Journal*, vol. 25, no. 10, pp. 18223-18235, May 15, 2025.
- [31] Y. Wang, C. Zhu, Y. Zhu and X. Luo, "Life Extension of Wind Turbine Gearboxes Based on Pitch Control," *Results in Engineering*, vol. 27, 2025.
- [32] Y. Qin, H. Yu, D. Chen and Y. Mao, "A Prognostic Driven Dynamic Predictive Maintenance Decision-Making Model for Offshore Wind Turbine Systems," *Ocean Engineering*, vol. 338, 2025.
- [33] H. Tao, W. Feng, G. Yang, R. Du and Y. Zhong, "A Wear Condition Warning Method for Wind Turbine Gearbox Based on Oil Online Monitoring Using Learnable Multiscale

- Convolutional Neural Network," *IEEE Sensors Journal*, vol. 24, no. 21, pp. 35709-35721, Nov. 1, 2024.
- [34] H. Jin, H. Li, J. Bi and M. Li, "Joint Optimization of Spare Parts Inventory and Maintenance for Wind Turbine Systems," *Expert Systems with Applications*, vol. 292, 2025.
- [35] X. Zhu, J. Wang and D. W. Coit, "Joint Optimization of Spare Part Supply and Opportunistic Condition-Based Maintenance for Onshore Wind Farms Considering Maintenance Route," *IEEE Transactions on Engineering Management*, vol. 71, pp. 1086-1102, 2024.
- [36] L. Yang, G. Li, Z. Zhang, X. Ma and Y. Zhao, "Operations & Maintenance Optimization of Wind Turbines Integrating Wind and Aging Information," *IEEE Transactions on Sustainable Energy*, vol. 12, no. 1, pp. 211-221, Jan. 2021.
- [37] A. Saleh, M. Chiachío, J. F. Salas and A. Kolios, "Self-Adaptive Optimized Maintenance of Offshore Wind Turbines by Intelligent Petri Nets," *Reliability Engineering & System Safety*, vol. 231, 2023.
- [38] L. Yang, Y. Chen and X. Ma, "A State-Age-Dependent Opportunistic Intelligent Maintenance Framework for Wind Turbines Under Dynamic Wind Conditions," *IEEE Transactions on Industrial Informatics*. vol. 19, no. 10, pp. 10434-10443, Oct. 2023.
- [39] Z. Liu, J. Zheng, Q. Zhang and R. Xu, "Advances and Trends in Intelligent Maintenance for Wind Turbine Systems," *Sustainable Energy Technologies and Assessments*, vol. 80, 2025.
- [40] A. Grataloup, S. Jonas and A. Meyer, "Wind Turbine Condition Monitoring Based on Intraand Inter-Farm Federated Learning," *arXiv preprint arXiv:2409.12345 [cs.LG]*, Sep. 2024.
- [41] S. Yoganand, "Fault Detection in Small Wind Turbines Using Condition Monitoring Techniques and Machine Learning Algorithms (A Predictive Approach)," in *Wind Energy Engineering: Non-Destructive Testing and Condition Monitoring Techniques in Wind Energy*, F. P. G. Marquez, M. Papaelias and V. L. Jantara Junior, Eds. Academic Press, 2023, pp. 15-29.
- [42] A. Aranizadeh, H. Shad, B. Vahidi and A. Khorsandi, "A Novel Small-Scale Wind-Turbine Blade Failure Detection According to Monitored Data," *Results in Engineering*, vol. 25, 2025.
- [43] F. Salboukh, Y. Mousavi, I. B. Kucukdemiral, A. Fekih, U. Cali, "Reliability Assessment and Condition Monitoring of Wind Energy Conversion Systems Using Bayesian Networks: Recent Advances and Key Insights", IEEE Access, 2025.

- [44] M. Barzegar-Kalashani, M. Seyedmahmoudian, S. Mekhilef, A. Stojcevski and B. Horan, "Small-Scale Wind Turbine Control in High-Speed Wind Conditions: A Review," *Sustainable Energy Technologies and Assessments*, vol. 60, 2023.
- [45] K. Emdadi, M. Gandomkar, A. Aranizadeh, B. Vahidi, "A novel approach of cable failure level and failure type detection based on environmental conditions," *Electric Power System Research*, vol. 253, pp. 112553, 2026.
- [46] A. Aranizadeh, S. M. Shahrtash and A. Gholami, "Prioritizing CBs Maintenance and Identifying Mandatory Maintenance at Higher Priorities," *International Transactions on Electrical Energy Systems*, 2022.
- [47] A. Aranizadeh, B. Vahidi, A. Khorsandi, "Data inherent Assessment of Electrical Equipment by Failure Pattern and Self-Evaluation Decision-Making Algorithm", *Scientific Reports*, vol. 15, pp. 42391, 2025.
- [48] A. W. Lourari, A. Soualhi, T. Benkedjouh, "Advancing bearing fault diagnosis under variable working conditions: a CEEMDAN-SBS approach with vibro-electric signal integration", *Int J Adv Manuf Technol*, vol. 132, pp. 2753-2772, 2024.
- [49] A. W. Lourari, B. E. Yousefi, A. B. Essaidi, "Enhanced diagnosis of bearing and gear faults using Hilbert-Huang transform, singular value decomposition, and supervised learning methods", *Int J Adv Manuf Technol*, vol. 139, pp. 983-999, 2025.
- [50] A. W. Lourari, T. Benkedjouh, B. E. Yousefi, A. Soualhi, "An ANFIS-based Framework for the Prediction of Bearing's Remaining Useful Life", *International Journal of Prognostics and Health Management*, vol. 15, no. 1, 2024.
- [51] A. W. Lourari, B. E. Yousefi, A. Soualhi, "Enhancing bearing and gear fault diagnosis: A VMD-PSO approach with multisensory signal integration", *Journal of Vibration and Control*, vol. 12, 2024.
- [52] A. W. Lourari, A. Soualhi, T. Benkedjouh, "New health indicators for the monitoring of bearing failures under variable loads", *Structural Health Monitoring*, vol. 23, 2024.
- [53] Y. Ou, K. E. Tatsis, V. K. Dertimanis, M. D. Spiridonakos and E. N. Chatzi, "Vibration-Based Monitoring of a Small-Scale Wind Turbine Blade Under Varying Climate Conditions. Part I: An Experimental Benchmark," *Structural Control and Health Monitoring*, 2021.

[54] Y. Ou, K. E. Tatsis, V. K. Dertimanis, M. D. Spiridonakos and E. N. Chatzi, "Vibration-Based Monitoring of a Small-Scale Wind Turbine Blade Under Varying Climate Conditions. Part II: A numerical benchmark," *Structural Control and Health Monitoring*, 2021.
![](_page_0_Picture_0.jpeg)

# Survival Models for Predictive Maintenance and Remaining Useful Life in Sensor-Enabled Smart Energy Networks

# A Review

Shadi, Mohammad Reza; Mirshekali, Hamid; Tahavori, Maryamsadat; Shaker, Hamid Reza

Published in: Sensors

DOI: [10.3390/s26061915](https://doi.org/10.3390/s26061915)

Publication date: 2026

Document version: Final published version

Document license: CC BY

Citation for pulished version (APA):

Shadi, M. R., Mirshekali, H., Tahavori, M., & Shaker, H. R. (2026). Survival Models for Predictive Maintenance and Remaining Useful Life in Sensor-Enabled Smart Energy Networks: A Review. Sensors, 26(6). <https://doi.org/10.3390/s26061915>

[Go to publication entry in University of Southern Denmark's Research Portal](https://portal.findresearcher.sdu.dk/en/publications/603391c5-76ad-4d63-8b8d-3aed8ff3a6cb)

#### Terms of use

This work is brought to you by the University of Southern Denmark. Unless otherwise specified it has been shared according to the terms for self-archiving. If no other license is stated, these terms apply:

- You may download this work for personal use only.
- You may not further distribute the material or use it for any profit-making activity or commercial gain
- You may freely distribute the URL identifying this open access version

If you believe that this document breaches copyright please contact us providing details and we will investigate your claim. Please direct all enquiries to puresupport@bib.sdu.dk

Download date: 11. Oct. 2026

![](_page_1_Picture_0.jpeg)

![](_page_1_Picture_1.jpeg)

*Review*

# **Survival Models for Predictive Maintenance and Remaining Useful Life in Sensor-Enabled Smart Energy Networks: A Review**

**Mohammad Reza Shadi 1,\* [,](https://orcid.org/0000-0001-7279-2279) Hamid Mirshekali <sup>1</sup> [,](https://orcid.org/0000-0002-1921-8830) Maryamsadat Tahavori [2](https://orcid.org/0000-0002-2407-6101) and Hamid Reza Shaker [1](https://orcid.org/0000-0003-2858-8400)**

- <sup>1</sup> SDU Center for Energy Informatics, Maersk Mc-Kinney Moeller Institute, The Faculty of Engineering, University of Southern Denmark, 5230 Odense, Denmark; hmir@mmmi.sdu.dk (H.M.); hrsh@mmmi.sdu.dk (H.R.S.)
- <sup>2</sup> Section of Energy Technology and Computer Science, DTU Engineering Technology, Technical University of Denmark, 2750 Ballerup, Denmark; marta@dtu.dk
- **\*** Correspondence: mrsh@mmmi.sdu.dk

# **Abstract**

Smart energy networks, including electricity distribution and district heating, are increasingly operated as sensor-enabled infrastructures where maintenance decisions must be made under heterogeneous and time-varying operating conditions. In these settings, timeto-event data are rarely complete; preventive actions and limited observation horizons routinely introduce censoring and truncation, so models and validation procedures must account for partially observed lifetimes to avoid biased inference and misleading performance estimates. This review surveys survival models for predictive maintenance (PdM) and remaining useful life (RUL) estimation, spanning non-parametric, semi-parametric, parametric, and learning-based approaches, with emphasis on censoring-aware formulations and the use of static and time-varying covariates derived from sensor, inspection, and contextual information. A structured taxonomy and a systematic mapping of model families to data types, core assumptions (proportional hazards versus parametric distributional structure), and decision-oriented outputs such as risk ranking, horizon failure probabilities, and RUL distributions are presented. Evaluation practice is also synthesized by covering discrimination metrics, censoring-aware RUL accuracy measures, and probabilistic assessment via proper scoring rules, including the time-dependent Brier score and Integrated Brier Score (IBS). The review provides researchers and practitioners with a practical guide to selecting, fitting, and evaluating survival models for risk-informed maintenance planning in smart energy networks.

**Keywords:** asset management; censoring and truncation; Cox proportional hazards; learning-based survival models; random survival forest; RUL prediction

![](_page_1_Picture_11.jpeg)

Academic Editor: Omprakash Kaiwartya

Received: 11 February 2026 Revised: 16 March 2026 Accepted: 17 March 2026 Published: 18 March 2026 **Copyright:** © 2026 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the [Creative Commons](https://creativecommons.org/licenses/by/4.0/) [Attribution \(CC BY\) license.](https://creativecommons.org/licenses/by/4.0/)

# **1. Introduction**

Smart energy networks are shifting from schedule-based upkeep to data-driven reliability management. Electricity distribution networks and district heating networks (DHNs) now operate as sensor-rich systems where failures are costly, visible, and increasingly regulated. Operators must keep service reliable while assets age, operating conditions change, and digital control becomes more widespread. In this setting, maintenance is no longer only a technical task. It is a system-level decision problem with clear consequences for customers, reliability indices, and contractual compensation and penalties [\[1](#page-35-0)[,2\]](#page-35-1). *Sensors* **2026**, *26*, 1915 2 of 40

Medium-voltage assets are often a practical starting point because their age profile and failure history make them major drivers of outages [\[3\]](#page-35-2).

Survival models offer a principled way to address this problem. They are designed for time-to-event prediction under censoring, which matches how grid and heating assets are observed in practice. They support risk estimation over time, not just binary fault flags. They can incorporate covariates from sensors, inspections, and context data. This makes them well suited for PdM and RUL estimation in real fleets. Yet applying survival analysis in smart energy networks is not straightforward. Data are heterogeneous, failures are rare, operating regimes drift, and maintenance actions change the risk process. Methods also need to be interpretable enough for engineering use and robust enough for operational deployment [\[4,](#page-35-3)[5\]](#page-35-4).

DHNs face a parallel reliability challenge, shaped by thermal and hydraulic constraints. They operate under high temperature and pressure in harsh environments. This exposes pipes and components to corrosion and leakage, with failures that can directly affect customer comfort and safety [\[6\]](#page-35-5). In DHN pipe systems, leaks dominate failure statistics and are often linked to corrosion or mechanical impacts. They are also widely regarded as the most severe form of damage among common degradation modes [\[7\]](#page-36-0).

Historically, DHN operators could absorb early-stage problems by running the network hotter. Raising supply temperature can offset local losses, weak heat transfer, or gradual degradation and may delay visible service effects. The transition to low-temperature district heating, often framed as fourth-generation DH, reduces this operational buffer. When systems are designed to run closer to the minimum temperature required at the customer level, there is less margin to mask emerging faults through temperature increases. As a result, degradation is more likely to appear quickly as measurable and noticeable service shortfalls, such as insufficient heat delivery, rather than remaining hidden until a later failure [\[8\]](#page-36-1).

For distribution system operators (DSOs), maintenance is fundamentally a resourceconstrained risk allocation problem. DSOs must determine which medium-voltage assets to repair or replace, when to intervene, and where residual risk can be tolerated, while the consequences are directly reflected in continuity of supply and regulatory performance. What makes this difficult in practice is that asset condition evidence is partial and delayed (many components never fail within the observation window), and failure processes are non-stationary (loading, switching, climate, and network reconfiguration change the stress landscape). Interventions alter the time-to-failure process itself, replacement resets effective age, whereas repairs usually produce partial risk reduction and can shift the dominant failure location rather than eliminating risk [\[9,](#page-36-2)[10\]](#page-36-3).

Accordingly, DSOs require models that represent risk as a time-dependent quantity and remain practical for planning. Such models should generate comparable and updateable risk trajectories across heterogeneous fleets so that renewal prioritization, intervention timing, and portfolio-level impacts can be justified in operational and regulatory terms. Survival models align well with this decision interface because they are designed for timeto-event analysis under censoring and provide interpretable measures such as hazard and survival. These outputs also support aggregation from individual assets to feeder- and system-level assessments [\[11,](#page-36-4)[12\]](#page-36-5).

This operational reality is what drives the move from age-threshold policies to PdM and RUL estimation in both DHN and medium-voltage (MV) distribution asset management. Fixed lifetime assumptions and simple age-based replacement do not provide a defensible basis for prioritization when risk differs sharply across nominally similar assets. The planning problem therefore becomes identifying when risk crosses an unacceptable level for each asset class so that replacement, refurbishment, or intensified monitoring can

Sensors 2026, 26, 1915 3 of 40

be scheduled before outages and service deterioration occur, and so that limited budgets are allocated to interventions with measurable reliability impact [13,14].

The transition toward PdM and RUL estimation depends on what the network can reliably observe. Sensor and inspection practices determine which degradation mechanisms become measurable and can be used as covariates in reliability and RUL models. In MV cable fleets, condition assessment often relies on diagnostic tests that provide information beyond installation age, including very low frequency dissipation factor ( $\tan \delta$ ) [15], partial discharge measurements [16], and oversheath testing [17,18]. These measurements translate latent insulation degradation into observable indicators that support risk ranking and intervention scheduling.

Observability also differs across asset classes, which influences how survival models are applied in practice. For distribution transformers, internal sensing is often limited at scale. As a result, risk and RUL estimation may rely on indirect signals such as loading inferred from smart meters and ambient temperature as proxies for thermal stress and aging [19,20]. In DHNs, available data can be broader, including process measurements such as temperature, pressure, and flow, inspection records, and leakage detection. However, monitoring coverage varies widely across systems, and many networks still lack continuous measurements along pipe segments [21].

Table 1 indicates that recent reviews in prognostics and health management and datadriven RUL prediction largely emphasize deep-learning RUL pipelines or domain-specific PdM applications, while giving limited attention to censoring/truncation mechanisms and to a coherent taxonomy of survival model families. This review therefore focuses on survival (time-to-event) models for PdM and RUL estimation in sensor-enabled smart energy networks, encompassing electricity distribution networks and district heating networks. Non-parametric, semi-parametric, parametric, and learning-based approaches are synthesized, and these families are mapped to the data structures and assumptions they require (e.g., static versus time-varying covariates, and censoring-aware likelihoods) and to the operational outputs used in maintenance planning (risk ranking, horizon failure probabilities, and RUL distributions). In addition, evaluation practice is consolidated by explicitly pairing discrimination with censoring-aware RUL accuracy measures and proper scoring rules such as the time-dependent Brier score and Integrated Brier Score to assess both ranking and probabilistic calibration. The resulting synthesis supports reproducible method selection for researchers and defensible, risk-informed maintenance planning for practitioners.

Table 1. Comparison between this review and related state-of-the-art review publications.

| Reference | Application/Asset     | Cen          | NonPar     | SemiPar      | Par          | Learn        | Key<br>Emphasis   |
|-----------|-----------------------|--------------|------------|--------------|--------------|--------------|-------------------|
| [22]      | General PHM<br>(RUL)  | X            | ×          | ×            | X            | ✓            | GNN RUL           |
| [23]      | General PHM<br>(RUL)  | ×            | (√)        | <b>(√)</b>   | $\checkmark$ | $\checkmark$ | PI RUL            |
| [24]      | General PHM<br>(RUL)  | ×            | ×          | <b>(√)</b>   | (√)          | $\checkmark$ | DL RUL            |
| [25]      | Cross-domain          | $\checkmark$ | <b>(√)</b> | $\checkmark$ | $\checkmark$ | $\checkmark$ | DL survival       |
| [26]      | General PdM           | <b>(√)</b>   | X          | (√)          | <b>(√)</b>   | $\checkmark$ | PdM survey        |
| [27]      | Rotating<br>machinery | ×            | ×          | ×            | (√)          | <b>(√)</b>   | RotMach<br>PdM    |
| [28]      | General assets        | X            | <b>(√)</b> | Х            | <b>(√)</b>   | $\checkmark$ | AD+RUL            |
| [29]      | Solar PV systems      | ×            | ×          | ×            | X            | (√)          | PV<br>reliability |

Sensors **2026**, 26, 1915 4 of 40

<span id="page-4-0"></span>Table 1. Cont.

| Reference  | Application/Asset        | Cen          | NonPar       | SemiPar      | Par          | Learn        | Key<br>Emphasis      |
|------------|--------------------------|--------------|--------------|--------------|--------------|--------------|----------------------|
| [30]       | Power<br>transformers    | ×            | ×            | X            | ×            | ×            | AI+IoT               |
| [31]       | Wind turbines            | ×            | X            | ×            | X            | <b>(√)</b>   | PdM+PrsM             |
| [32]       | Renewable energy         | X            | ×            | ×            | ×            | ✓            | RES optimization     |
| [33]       | General equipment        | X            | X            | <b>(√)</b>   | <b>(√)</b>   | $\checkmark$ | AI RUL               |
| This paper | Smart energy<br>networks | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | Survival<br>taxonomy |

*Legend*:  $\checkmark$  = explicitly covered; ( $\checkmark$ ) = briefly/partially mentioned; X = not covered. *Abbreviations*: Cen = censoring/truncation; NonPar = non-parametric; SemiPar = semi-parametric; Par = parametric; Learn = learning-based; PHM = prognostics and health management; AD = anomaly detection; AI = artificial intelligence; DL = deep learning; GNN = graph neural network; IoT = internet of things; PI = prediction interval; PrsM = prescriptive maintenance; PV = photovoltaic; RES = renewable energy sources; RotMach = rotating machinery.

# 2. Taxonomy of Survival Models

This time-dependent view of failure risk is well established in infrastructure reliability and is commonly addressed using a limited number of survival model families. Figure 1 summarizes the main taxonomy adopted in this review, namely non-parametric, semi-parametric, parametric, and learning-based survival models. These approaches have been widely used for applications such as pipe-break risk assessment and renewal prioritization [34], while related Weibull-based reliability models have also been applied in power distribution to represent time-varying component failure probabilities [2]. This taxonomy provides the conceptual structure for the methodological discussions in the following sections.

<span id="page-4-1"></span>![](_page_4_Figure_6.jpeg)

Figure 1. Taxonomy of survival models for predictive maintenance and asset management.

*Sensors* **2026**, *26*, 1915 5 of 40

Within this taxonomy, the principal distinction lies in the extent of assumptions imposed on the time-to-event process and in the way covariate effects are handled. Nonparametric models, such as Kaplan–Meier and Nelson–Aalen, describe survival behaviour directly from observed event data with minimal structural assumptions and are therefore useful for baseline estimation and descriptive comparison. Semi-parametric models, represented mainly by the Cox proportional hazards model and its close variants, preserve flexibility in the baseline hazard while enabling the analysis of covariate effects. Parametric survival models, including Weibull, Gamma, Gompertz, Exponential, and accelerated failure time formulations such as log-normal and log-logistic models, specify an explicit lifetime distribution and are especially useful when hazard-shape interpretation or extrapolation is required. Learning-based survival models further extend this taxonomy by capturing non-linear effects and higher-dimensional interactions through approaches such as neural Cox, neural Weibull, transformer-based survival models, and random survival forests.

A further advantage of this taxonomy is that it helps align model choice with the characteristics of available data and the intended maintenance objective. In practice, assetmanagement problems may differ substantially in terms of sample size, censoring structure, covariate richness, and the need for interpretability versus predictive flexibility. As a result, the selection of a survival modelling approach is rarely universal, but instead depends on whether the goal is descriptive reliability assessment, covariate effect analysis, long-horizon lifetime estimation, or data-driven risk prediction. Framing the literature through this taxonomy therefore supports a more systematic comparison of methods and clarifies the contexts in which different survival-model families are most suitable.

# **3. Sensors and Censoring**

In survival and reliability studies, censoring occurs when an asset is observed but its exact event time is not known. The record still contains valid information because the asset is known to have survived up to a specific time. This is common in maintenance data where observation ends before many failures occur, or where preventive maintenance stops follow-up before failure and creates right-censored records [\[10\]](#page-36-3). In condition-based maintenance datasets, this appears explicitly as a mix of failure histories and suspension histories, where components are replaced preventively rather than failing [\[35\]](#page-37-2). By contrast, truncation refers to a selection mechanism in which some lifetimes are not observed because an asset is included in the dataset only if its event time falls within a predefined observation window. As a result, failures occurring outside the window are absent from the sample, which changes the composition of the observed population and can bias inference if not handled explicitly [\[36\]](#page-37-3). For instance, a power transformer fleet monitored from 1980 onward includes only units that were still in service in 1980. Transformers installed and failing before 1980 are absent from the dataset.

Let *T* denote the true event (failure) time, *t* an observed time point (either an exact event time or a censoring time), and *L* and *R* the left and right truncation limits that define the study's inclusion window (Figure [2\)](#page-6-0).

- **Uncensored:** exact failure time is known (*T* = *t*).
- **Right-censored:** failure has not occurred by the last observation (*T* > *t*).
- **Interval-censored:** failure occurred within a known time window (*t*<sup>0</sup> < *T* ≤ *t*1).
- **Left-truncated:** units that failed before entry are unobserved; only those with *T* > *L* appear.
- **Right-truncated:** units with very late failures are unobserved; only those with *T* ≤ *R* appear.

*Sensors* **2026**, *26*, 1915 6 of 40

• **Double-truncated:** only units with failures within the inclusion window are observed (*L* < *T* ≤ *R*) [\[37\]](#page-37-4).

<span id="page-6-0"></span>![](_page_6_Figure_2.jpeg)

**Figure 2.** Common censoring and truncation types in survival data.

Left truncation deserves particular attention in smart energy asset datasets because many components have already been in service for years before digital monitoring begins. In such settings, the observed sample is conditioned on survival up to the monitoring entry time, which can bias hazard and survival estimates if this delayed entry is ignored. The standard treatment is to use delayed-entry survival modeling, where an asset contributes to the risk set only after its observation start time rather than from installation. In semiparametric models such as Cox PH, this is handled through entry-time-adjusted risk sets, while in parametric models the likelihood is conditioned on survival up to the truncation time. For learning-based survival models, the same principle should be preserved in the training objective and sampling logic so that prediction targets remain consistent with the observed at-risk population. When installation dates or historical operating records are incomplete, additional bias mitigation may require asset-registry reconstruction, use of inspection and replacement records, and sensitivity analysis under alternative assumptions on unobserved early-life exposure. In practice, careful treatment of left truncation is especially important in legacy power and district heating fleets, where sensor deployment often starts long after commissioning.

Beyond defining censoring and truncation, sensors play a central role in survival and RUL modeling by providing time-varying evidence of operating stress and incipient abnormal behavior. This allows failure risk to be conditioned on more than age and installation metadata. In electricity distribution systems, SCADA and distribution automation supply continuous measurements of system state and loading, including current, voltage, power, and switch status. These signals can be translated into asset-level exposure and incorporated as covariates that modulate hazard over time. In district heating networks, supervisory monitoring similarly captures temperature, pressure, flow rates, and energyrelated variables across substations and network segments, enabling models to represent hydraulic and thermal operating regimes rather than treating failures as purely age-driven. In this way, sensor-based condition evidence converts operational variability into mea*Sensors* **2026**, *26*, 1915 7 of 40

surable covariates that explain heterogeneity in failure risk and support risk updates as operating conditions evolve [\[38,](#page-37-5)[39\]](#page-37-6).

Sensor data can also change which outcomes are observed. When monitoring systems flag abnormal conditions, operators often replace an asset before it fails. In the dataset, this replacement ends the observation period without a recorded failure time. The record is therefore right-censored; the asset is known to have survived up to the replacement time, but when failure would have occurred is not observed. If many assets are preventively replaced, the dataset contains fewer run-to-failure examples, which reduces the amount of direct failure information available for learning and evaluation. This censoring mechanism must be modeled explicitly in the survival likelihood and reflected in the evaluation protocol [\[40](#page-37-7)[,41\]](#page-37-8).

Data characteristics differ substantially between electricity and district heating assets, and these differences affect how survival models should be formulated. In power systems, assets such as cables and transformers are often monitored through a combination of lowerrate SCADA signals, periodic diagnostic tests, and indirect stress proxies, while failures may arise from insulation degradation, thermal aging, switching stress, or partial discharge activity. In DHNs, the data more commonly reflect thermal–hydraulic operation through temperature, pressure, flow, and leak-related observations, with degradation dominated by corrosion, leakage, and external mechanical impacts. These differences imply distinct sampling structures, noise sources, and observability levels. Accordingly, survival models for power assets often rely more on static covariates, inspection features, and sparse timevarying updates, whereas DHN applications can more naturally exploit process-oriented covariates and operating-regime information. In both cases, model design should follow the sensing reality of the asset class, including the choice of covariates, update frequency, censoring treatment, and level of model complexity.

# **4. Survival Models**

The practical value of survival models in utility maintenance planning comes from how naturally their predictions translate into action. Utilities rarely need an abstract "health score" on its own. They need forecasts that answer planning questions in the same units as their decisions: time and risk. Survival modeling provides that interface by estimating the likelihood that an asset will remain in service over a defined horizon, such as the next *k* years. It also describes how failure pressure changes with age through the hazard function. This hazard can change with time and may not move in only one direction. This is often described by the bathtub curve [\[42\]](#page-37-9), as illustrated in Figure [3:](#page-8-0)

- **Early-life stage (higher failures):** failures are relatively common due to installation issues or early defects.
- **Mid-life stage (stable failures):** the failure rate becomes fairly steady for a long period.
- **Late-life stage (increasing failures):** failures rise again as aging and wear-out dominate.

Together, these outputs allow planners to compare assets with different ages and histories on a common basis. They also support transparent intervention rules, for example scheduling renewal when the projected near-term risk crosses a policy threshold.

To make this decision interface explicit, the PdM and RUL prediction tasks are formulated in terms of the survival function, hazard rate, and conditional remaining-life distribution. In this way, the mapping from survival-model outputs to horizon failure probabilities, RUL summaries, and threshold-based maintenance decisions is clarified.

*Sensors* **2026**, *26*, 1915 8 of 40

<span id="page-8-0"></span>![](_page_8_Figure_1.jpeg)

**Figure 3.** Bathtub-shaped hazard curve illustrating three lifecycle phases.

# *4.1. Problem Formulation: Predictive Maintenance and RUL Estimation*

PdM aims to forecast future failure behavior and convert these forecasts into actionable maintenance decisions. Let *T* denote the (random) failure time of an asset. The survival function

$$S(t) = \Pr(T > t), \tag{1}$$

gives the probability that the asset remains operational beyond time *t*. The hazard function

$$h(t) = \lim_{\Delta t \to 0} \frac{\Pr(t \le T < t + \Delta t \mid T \ge t)}{\Delta t},\tag{2}$$

describes the instantaneous failure intensity at time *t*, and the cumulative hazard

$$H(t) = \int_0^t h(u) \, du \tag{3}$$

links to the survival function through

$$S(t) = \exp[-H(t)]. \tag{4}$$

### 4.1.1. Remaining Useful Life

Given that an asset has survived up to the current time *t*0, the RUL is the conditional random variable

$$RUL(t_0) = (T - t_0) \mid (T > t_0).$$
 (5)

A survival model provides the conditional survival of the remaining life via

$$\Pr(\text{RUL}(t_0) > u) = \Pr(T > t_0 + u \mid T > t_0) = \frac{S(t_0 + u)}{S(t_0)}, \quad u \ge 0,$$
 (6)

which yields the expected remaining life (when finite) as

$$\mathbb{E}[\text{RUL}(t_0)] = \int_0^\infty \Pr(\text{RUL}(t_0) > u) \, du = \int_0^\infty \frac{S(t_0 + u)}{S(t_0)} \, du. \tag{7}$$

*Sensors* **2026**, *26*, 1915 9 of 40

In practice, it is also common to report RUL quantiles obtained from the conditional survival curve, where *q* ∈ (0, 1) denotes the desired quantile level (*q* = 0.5 for the median), i.e., find *u<sup>q</sup>* such that

$$\frac{S(t_0 + u_q)}{S(t_0)} = 1 - q. (8)$$

# 4.1.2. Horizon Failure Probability

For a planning horizon *τ* > 0, the probability of failure within (*t*0, *t*<sup>0</sup> + *τ*] conditional on survival up to *t*<sup>0</sup> is

$$\Pr(t_0 < T \le t_0 + \tau \mid T > t_0) = 1 - \Pr(T > t_0 + \tau \mid T > t_0) = 1 - \frac{S(t_0 + \tau)}{S(t_0)}.$$
 (9)

Survival-based PdM models support decision-making through (i) risk ranking using *h*(*t* | **z**) or a risk score, (ii) horizon failure probabilities over planning windows, and (iii) RUL distributions or their summaries (mean/quantiles). A common risk-informed intervention rule can be written as

Intervene if 
$$Pr(t_0 < T \le t_0 + \tau \mid T > t_0) > \gamma$$
, (10)

where *γ* ∈ (0, 1) is a policy threshold reflecting operational constraints, reliability targets, and risk tolerance. This formulation explicitly connects survival outputs (*S*(*t*), *h*(*t*), *H*(*t*)) to PdM decisions and RUL estimation.

While all survival approaches aim to estimate the same decision-relevant quantities (the survival function *S*(*t*), hazard *h*(*t*), and cumulative hazard *H*(*t*)) the taxonomy used here is defined by the degree of structural assumptions imposed on the time-to-event process and the way covariates are incorporated. Non-parametric models estimate *S*(*t*) or *H*(*t*) directly from observed event/risk sets with minimal distributional assumptions and typically lack a general regression form for continuous covariates (beyond stratification). Semi-parametric models introduce a parametric covariate effect (hazard ratios) while leaving the baseline hazard unspecified, enabling covariate-aware risk ranking without assuming a full lifetime distribution. Parametric models assume an explicit distributional form for *T*, yielding closed-form *S*(*t*) and *h*(*t*) and supporting absolute risk estimation and extrapolation. Learning-based survival models retain censoring-aware objectives and survival outputs but replace linear predictors or fixed functional forms with flexible function approximators (e.g., trees or neural networks), improving capacity to capture non-linearities and interactions at the cost of higher data requirements and potentially reduced interpretability.

# *4.2. Non-Parametric Survival Models*

Non-parametric survival models make minimal assumptions about the underlying failure mechanism and estimate survival probabilities or hazard rates directly from observed data, without specifying a particular lifetime distribution [\[43\]](#page-37-10). In the following, different non-parametric survival models are reviewed.

### 4.2.1. Kaplan–Meier

The Kaplan–Meier (KM) estimator, also known as the product-limit estimator, is the most commonly used non-parametric method for estimating the survival function [\[44,](#page-37-11)[45\]](#page-37-12). It calculates the survival probability *S*(*t*) by sequentially multiplying the chances of surviving each observed failure time, given that the asset was still operational just before that time. Sensors **2026**, 26, 1915

Let  $t_{(1)} < t_{(2)} < \cdots < t_{(K)}$  denote the ordered event times, where  $e_j$  failures occur among  $r_j$  assets at risk at time  $t_{(j)}$ . The KM estimator is defined as

$$\hat{S}(t) = \prod_{t_{(j)} \le t} \left( 1 - \frac{e_j}{r_j} \right) \tag{11}$$

The resulting estimator yields a stepwise survival curve that decreases only at observed failure times [46]. Right-censored observations, for which the failure time is unknown beyond the study horizon, are handled by reducing the risk set  $r_j$  at subsequent times, without contributing an event. As a result, censoring does not produce drops in the survival curve but influences the estimate by shrinking the effective sample size [47].

The KM estimator is widely used as a baseline tool in survival analysis, offering an empirical summary of time-to-failure distributions and enabling comparisons across asset categories. In PdM and asset management, stratified KM curves are often used to benchmark component reliability across subgroups, for example, comparing failure behavior across different cable types, materials, or operating environments [48]. However, because the estimator does not model covariates, it requires separate curves for each group and cannot accommodate continuous sensor readings or multivariate feature sets.

#### 4.2.2. Nelson-Aalen

Another non-parametric approach is the Nelson–Aalen (NA) estimator, which focuses on the cumulative hazard function H(t) rather than S(t). The NA estimator accumulates hazard increments over time:

$$\hat{H}(t) = \sum_{t_{(j)} \le t} \frac{e_j}{r_j} \tag{12}$$

where  $e_j$  is the number of failures and  $r_j$  the number at risk at time  $t_{(j)}$ . This estimator is based on a counting-process framework and, on average, gives an accurate estimate of the cumulative failure risk [49]. Once  $\hat{H}(t)$  is obtained, the corresponding survival estimate can be computed via the exponential transformation

$$\hat{S}(t) = \exp[-\hat{H}(t)] \tag{13}$$

This formulation links the NA estimator to the KM estimator, which expresses survival as the product of conditional survival probabilities:

$$\hat{S}(t) = \prod \left( 1 - \frac{e_j}{r_j} \right) \tag{14}$$

When the hazard increments  $\frac{e_j}{r_j}$  are small, this product can be approximated using the first-order Taylor expansion  $\log(1-x)\approx -x$ , yielding

$$\hat{S}(t) \approx \exp\left(-\sum \frac{e_j}{r_j}\right)$$
 (15)

This approximation reveals the connection between the KM and NA estimators. Both are non-parametric methods that use the same event and risk information but represent it through survival probability and cumulative hazard, respectively [50]. In PdM, the NA estimator offers a complementary view by quantifying the accumulated risk over time, which can support reliability assessments and maintenance planning. Like KM, it does not rely on parametric assumptions, making it useful for initial exploration of failure patterns. However, its inability to incorporate covariates limits its use in individualized prediction.

Sensors 2026, 26, 1915 11 of 40

This motivates the need for regression-based survival models that can link asset-specific features, such as sensor measurements or design parameters, to failure risk for more precise RUL estimation.

#### 4.3. Semi-Parametric Survival Models

Semi-parametric survival models provide a flexible framework for incorporating covariate information without fully specifying the functional form of the underlying hazard or survival distribution. The most widely used model in this class is the Cox proportional hazards (PH) model [51], which separates time-dependent baseline risk from covariate effects. The remainder of this section reviews key semi-parametric survival models.

#### 4.3.1. Cox Proportional Hazards

In this model, the hazard function for an asset with covariate vector z is expressed as the product of two components:

- (i) an unspecified baseline hazard  $h_0(t)$ , which describes how failure risk changes over time for a baseline (reference) asset;
- (ii) a parametric term  $\exp(\beta^{\top}z)$ , which quantifies how covariates proportionally shift the hazard relative to the baseline.

Formally, the Cox proportional hazards model is written as

$$h(t \mid z) = h_0(t) \exp(\beta^{\top} z) \tag{16}$$

This proportional hazards structure implies that covariates shift the risk of failure by a constant factor over time. For example, if  $\beta_1$  corresponds to a temperature effect,  $\exp(\beta_1)$  represents the constant hazard ratio for a one-unit increase in temperature. Cox's semi-parametric approach thus addresses a key limitation of KM by enabling covariate modeling (e.g., sensor measurements, operational conditions) [1], while still not assuming a specific lifetime distribution for baseline risk.

#### 4.3.2. Partial Likelihood for Cox

Model coefficients  $\beta$  are typically estimated via partial likelihood, which maximizes the hazard discrimination between failed and surviving units at each event time without needing to specify  $h_0(t)$ . This approach yields estimates of covariate effects (interpreted as hazard ratios) independently of the baseline risk. Although the baseline hazard is not required during model fitting, it can still be estimated afterward if needed—commonly using methods like Breslow's estimator or by smoothing the Nelson–Aalen cumulative hazard. The main advantage of Cox regression lies in this separation; it avoids assumptions about the shape of the hazard over time while allowing practitioners to identify which covariates influence failure risk [34].

#### 4.3.3. Time-Varying Covariates for Cox (Extended)

Cox's model can be extended to accommodate covariates z(t) that evolve over time, such as operating temperature, load, or vibration level. In this formulation, the hazard at time t depends on the current values of both time-varying and static covariates and is given by

$$h(t \mid z(t)) = h_0(t) \exp\left(\sum_{j=1}^{p_1} \delta_j z_j(t) + \sum_{i=1}^{p_2} \beta_i z_i\right)$$
(17)

where  $z_j(t)$  are time-dependent covariates with corresponding coefficients  $\delta_j$ , and  $z_i$  are time-invariant (static) covariates with coefficients  $\beta_i$ . This formulation, often referred to as the extended Cox model, allows the hazard ratio between two units to change over

*Sensors* **2026**, *26*, 1915 12 of 40

time [\[52\]](#page-37-19). Such flexibility is particularly important in PdM, where asset condition indicators such as oil quality, pressure, or temperature may vary during operation and influence risk dynamically, while the inclusion of time-varying covariates technically violates the proportional hazards assumption in its strict form when *zj*(*t*) changes over time [\[38,](#page-37-5)[53\]](#page-37-20), the model can still be estimated using a modified version of partial likelihood and remains widely applicable in practice.

The Cox model and its extensions are widely used in asset management for their interpretability and flexibility. By examining the sign and magnitude of *β* coefficients (or hazard ratios *e β* ), one can identify which factors most strongly increase failure risk, information crucial for maintenance decision-making [\[54,](#page-37-21)[55\]](#page-37-22). For example, a Cox model can indicate that higher load or longer operating hours increases the hazard by a multiplicative factor, which can help engineers prioritize critical operating conditions. A key limitation, however, is the proportional hazards (PH) assumption: each covariate is assumed to have a time-invariant effect on the hazard. This can be restrictive in PdM settings, where the impact of variables such as vibration or temperature may intensify as an asset ages.

Table [2](#page-12-0) summarizes the core formulas for the non-parametric and semi-parametric survival models discussed in this section.

| Model/Quantity               | Formula(s)                                                                            | Notes                                |  |  |
|------------------------------|---------------------------------------------------------------------------------------|--------------------------------------|--|--|
|                              | S(t) = Pr(T > t)                                                                      |                                      |  |  |
| Core functions               | Pr(t ≤ T < t + ∆t   T ≥ t)<br>h(t) = lim∆t→0<br>∆t                                    | Survival, hazard, cumulative hazard  |  |  |
|                              | H(t) = R t<br>h(u) du,<br>S(t) = exp[−H(t)]<br>0                                      |                                      |  |  |
| Kaplan–Meier (KM)            | !<br>ej<br>Sˆ(t) =<br>∏<br>1 −<br>rj<br>t(j)≤t                                        | Non-parametric S(t)                  |  |  |
| Nelson–Aalen (NA)            | ej<br>Hˆ (t) =<br>∑<br>rj<br>t(j)≤t                                                   | Non-parametric H(t) and implied S(t) |  |  |
|                              | Sˆ(t) =<br>exp[−Hˆ (t)]                                                               |                                      |  |  |
| Cox PH (proportional hazard) | ⊤z)<br>h(t   z) = h0(t) exp(β                                                         | Semi-parametric; unspecified h0(t)   |  |  |
| Cox (extended; time-varying) | h(t   z(t)) = h0(t) exp<br><br>p1<br>p2<br>(t) + ∑<br>δjzj<br>βizi<br>∑<br>j=1<br>i=1 | Time-varying and static covariates   |  |  |
| Cox partial likelihood       | ⊤zi<br>exp(β<br>)<br>L(β) =<br>∏<br>exp(β⊤zj<br>)<br>∑j∈R(ti)<br>i: δi=1              | R(ti<br>) = {j : tj<br>≥ ti}         |  |  |

<span id="page-12-0"></span>**Table 2.** Summary of core survival-model formulas (non-/semi-parametric).

### *4.4. Parametric Survival Models*

Parametric survival models assume a specific probability distribution for failure times *T*, yielding explicit formulas for the survival function *S*(*t*) and hazard *h*(*t*). In reliability engineering and asset management, parametric models are common because many components' lifetime behaviors can be approximated by standard distributions, and having a closed-form model allows direct calculation of quantities like mean time to failure or failure probability by a given age [\[56\]](#page-37-23). Parametric models are commonly specified either as PH models with a parametric baseline hazard or as Accelerated Failure Time (AFT) models; for some families (notably Weibull), these representations are closely related.

Beyond the Weibull distribution, several other parametric specifications are frequently used in PdM, each encoding a different assumption about how failure risk evolves over time. The exponential model is the simplest case (corresponding to a constant hazard) and is often used as a baseline when data are sparse or when a memoryless failure mechanism is plausible. In contrast, log-normal and log-logistic models are commonly expressed in an AFT form and can represent non-monotonic hazard patterns, where risk increases and *Sensors* **2026**, *26*, 1915 13 of 40

later decreases with age, a behavior that a Weibull hazard (which is monotone in *t*) cannot capture. Gompertz models are also used in reliability contexts to represent exponentially increasing (or decreasing) hazards over time. In general, the choice of distribution is guided by empirical hazard trends and goodness-of-fit considerations. When the assumed form is appropriate, parametric models tend to be statistically efficient and facilitate closed-form estimation of failure probabilities. Moreover, they naturally support extrapolation beyond the observed time range, enabling long-horizon survival prediction for asset management and scenario analysis [\[57\]](#page-37-24).

# 4.4.1. Weibull Distribution

The Weibull distribution is one of the most widely used parametric models in reliability and PdM due to its flexibility in capturing various failure behaviors. It is defined by two positive parameters: a shape parameter *α* > 0 and a scale parameter *λ* > 0. The hazard and survival functions for the Weibull distribution are given by:

$$h(t) = \frac{\alpha}{\lambda} \left(\frac{t}{\lambda}\right)^{\alpha - 1} \tag{18}$$

$$S(t) = \exp\left[-\left(\frac{t}{\lambda}\right)^{\alpha}\right], \qquad t \ge 0$$
 (19)

The shape parameter *α* determines the nature of the hazard rate: *α* > 1 implies an increasing hazard over time (e.g., wear-out failures), *α* < 1 indicates a decreasing hazard, and *α* = 1 corresponds to a constant hazard, reducing the model to the exponential case (as shown in Figure [4\)](#page-14-0). These properties make the Weibull distribution highly suitable for modeling asset failures across different lifecycle stages [\[58](#page-37-25)[–60\]](#page-38-0).

The Weibull model can also be expressed in the AFT form, where covariates have a multiplicative effect on failure time:

$$\ln T = \beta^{\top} z + \sigma \epsilon \tag{20}$$

where *z* is the covariate vector, *β* is the coefficient vector, *σ* is a scale parameter, and *ϵ* follows an extreme value distribution. In this formulation, a unit increase in *z<sup>j</sup>* accelerates or decelerates the failure time by a factor of exp(*βj*). Equivalently, the scale parameter *λ* can be modeled as a function of covariates:

$$\lambda(z) = \exp(-\beta^{\top} z), \text{ so that } S(t \mid z) = \exp\left[-\left(\frac{t e^{-\beta^{\top} z}}{\lambda_0}\right)^{\alpha}\right]$$
 (21)

where *λ*<sup>0</sup> is a baseline scale parameter. Larger values of *β* <sup>⊤</sup>*z* correspond to shorter effective lifetimes.

Alternatively, the Weibull model can be embedded in a proportional hazards (PH) framework by specifying a Weibull baseline hazard function *h*0(*t*) and incorporating covariate effects via a log-linear hazard ratio:

$$h(t \mid z) = h_0(t) \exp(\beta^{\top} z), \text{ with } h_0(t) = \frac{\alpha}{\lambda} \left(\frac{t}{\lambda}\right)^{\alpha - 1}$$
 (22)

This dual interpretability, through both AFT and PH formulations, makes the Weibull distribution especially attractive in practice, allowing practitioners to flexibly model how asset characteristics influence failure time or risk. Even in the absence of detailed sensor data, the Weibull model remains valuable for capturing general aging trends or early-life failure patterns directly from observed failure times [\[61](#page-38-1)[,62\]](#page-38-2).

*Sensors* **2026**, *26*, 1915 14 of 40

<span id="page-14-0"></span>![](_page_14_Figure_1.jpeg)

**Figure 4.** Weibull survival functions illustrating the effect of (**a**) shape parameter *α* and (**b**) scale parameter *λ* on asset lifetime distributions.

0 2 4 6 8 10 Time t

#### 4.4.2. Exponential Distribution

0.0

The exponential distribution is a special case of the Weibull model with shape parameter *α* = 1, yielding a constant hazard rate:

$$h(t) = \frac{1}{\lambda} \tag{23}$$

and the corresponding survival function

$$S(t) = \exp\left(-\frac{t}{\lambda}\right) \tag{24}$$

Here, *λ* is the scale parameter (equal to the mean lifetime) and 1/*λ* is the constant failure rate. This specification implies a memoryless failure process, meaning the instantaneous risk of failure does not depend on the asset age. Although a constant hazard is often unrealistic for components that wear out with age, the exponential model is still useful as *Sensors* **2026**, *26*, 1915 15 of 40

a simple baseline, and, in asset management, corresponds to assuming a constant annual failure rate [\[63\]](#page-38-3).

### 4.4.3. Gompertz Distribution

The Gompertz distribution models a hazard rate that changes exponentially with time. It is commonly parameterized by *a* and *b* via

$$h(t) = b e^{at} (25)$$

so that the failure rate increases over time if *a* > 0 and decreases if *a* < 0 [\[64\]](#page-38-4). Integrating the hazard yields the survival function

$$S(t) = \exp\left[-\frac{b}{a}(e^{at} - 1)\right], \qquad a \neq 0$$
(26)

When *a* → 0, the Gompertz model reduces to a constant-hazard form, and the survival function becomes *S*(*t*) = exp(−*bt*), which is the exponential model. In PdM applications, the Gompertz distribution is therefore a natural choice when observed failure patterns indicate that hazard grows rapidly with age, such as when assets exhibit strongly accelerating wear after a certain service duration [\[65\]](#page-38-5).

### 4.4.4. Log-Normal Distribution (AFT)

In the log-normal model, the logarithm of failure time is assumed Gaussian. In an AFT formulation,

<span id="page-15-0"></span>
$$\ln T = \beta^{\top} z + \sigma \epsilon \tag{27}$$

where *z* denotes covariates, *β* is the coefficient vector, and *σ* is a scale parameter, and *ϵ* is a standard normal random variable, *ϵ* ∼ N (0, 1). The survival function can be written as

$$S(t) = 1 - \Phi\left(\frac{\ln t - \mu}{\sigma}\right) \tag{28}$$

where Φ(·) is the standard normal cumulative distribution function. A characteristic feature of the log-normal model is a non-monotonic hazard shape: the hazard typically starts near zero, rises to a peak, and then decreases at later ages. This makes the distribution suitable for mechanisms where risk builds up and later attenuates, or where time-to-failure exhibits substantial variability and long tails [\[66](#page-38-6)[–68\]](#page-38-7).

# 4.4.5. Log-Logistic Distribution (AFT)

The log-logistic model assumes ln *T* follows a logistic distribution and provides closedform expressions for both survival and hazard. With shape parameter *α* > 0 and scale parameter 1/*λ*, the survival function is

$$S(t) = \frac{1}{1 + (\lambda t)^{\alpha}} \tag{29}$$

and the hazard function is

$$h(t) = \frac{\lambda \alpha t^{\alpha - 1}}{1 + (\lambda t)^{\alpha}} \tag{30}$$

The hazard increases and then decreases when *α* > 1 (unimodal hazard) and is decreasing for *α* ≤ 1 [\[69\]](#page-38-8). This flexibility is useful in reliability settings where risk peaks at intermediate ages. In an AFT interpretation, covariates shift the time scale of failure through Equation [\(27\)](#page-15-0), where *ϵ* follows a logistic distribution, implying that features *z* *Sensors* **2026**, *26*, 1915 16 of 40

accelerate or decelerate the lifetime by rescaling time rather than directly modifying a baseline hazard.

# 4.4.6. Gamma Distribution

The Gamma distribution is another flexible parametric choice for modeling failure time *T* ≥ 0. It is defined by two positive parameters: a shape parameter *κ* and a scale parameter *θ*. The probability density function is

$$f(t) = \frac{1}{\Gamma(\kappa) \theta^{\kappa}} t^{\kappa - 1} \exp\left(-\frac{t}{\theta}\right) \qquad t \ge 0, \tag{31}$$

where Γ(·) denotes the Gamma function. The cumulative distribution function is

$$F(t) = \frac{\gamma(\kappa, t/\theta)}{\Gamma(\kappa)}$$
 (32)

The corresponding survival function is

$$S(t) = 1 - F(t) = \frac{\Gamma(\kappa, t/\theta)}{\Gamma(\kappa)}$$
 (33)

where *γ*(·, ·) and Γ(·, ·) denote the lower and upper incomplete Gamma functions, respectively. As in other parametric survival models, the hazard function is obtained from

$$h(t) = \frac{f(t)}{S(t)}. (34)$$

In practical terms, the Gamma model is useful because the shape parameter *κ* changes how failures concentrate over time. For example, *κ* = 1 reduces the model to the exponential case (constant hazard), while *κ* ̸= 1 allows more flexible lifetime shapes. This makes the Gamma distribution a reasonable alternative when empirical failure-time patterns are not well captured by a Weibull shape, yet a compact two-parameter lifetime model is still preferred [\[70\]](#page-38-9).

Figure [5](#page-17-0) provides a side-by-side comparison of the parametric survival models described in this subsection. In panel (a), all distributions are calibrated to have the same median lifetime of approximately 10 years, i.e., *S*(10) ≈ 0.5 for every curve; this makes the models directly comparable and highlights differences in early-life behavior and long-term tails. Panel (b) shows the corresponding hazard functions *h*(*t*), which make the underlying risk assumptions explicit: the exponential model implies a constant hazard, Weibull and Gompertz variants produce monotone hazards (decreasing for early-life failure regimes and increasing for wear-out or accelerating aging), while log-normal and log-logistic models allow a peaked hazard that increases to a maximum at intermediate ages and then declines. The Gamma model provides an additional parsimonious alternative, with *κ* < 1 yielding decreasing hazard, and *κ* > 1 yielding increasing hazard. Overall, Figure [5](#page-17-0) emphasizes that selecting a parametric distribution amounts to selecting a hazard-shape assumption, which directly influences extrapolated survival and maintenance planning.

Sensors **2026**, 26, 1915

<span id="page-17-0"></span>![](_page_17_Figure_1.jpeg)

**Figure 5.** Comparison of common parametric survival models: (a) survival functions S(t) calibrated to a common median lifetime ( $S(10) \approx 0.5$ ); (b) corresponding hazard functions h(t) illustrating constant, monotone, and peaked risk regimes.

### 4.5. Learning-Based Survival Models

Learning-based survival models generalize the preceding non-parametric, semi-parametric, and parametric families by replacing rigid predictors (e.g., linear Cox risk scores) or fixed lifetime forms with flexible function approximators such as tree ensembles and neural networks, while still producing survival quantities of direct operational value in PdM, including  $h(t \mid z)$ ,  $H(t \mid z)$ , and  $S(t \mid z)$  [71]. Their central promise is to learn nonlinear effects and higher-order interactions from heterogeneous covariates (asset metadata, environment, and sensor-derived indicators) that are difficult to encode in classical models, yet without sacrificing the time-to-event interpretation that planners need for horizon risk and RUL estimation. Crucially, these models must be trained in a censoring-aware manner: censored units still carry information (they survived up to their last observation), and ignoring this structure can bias risk estimation and miscalibrate RUL forecasts. In practice, censoring-awareness is enforced either through Cox-type objectives (partial likelihood, as in neural Cox/DeepSurv) or through direct maximization of a likelihood induced by an explicit survival parameterization (as in neural parametric and hybrid models) [72].

Sensors 2026, 26, 1915 18 of 40

For right-censored data, these models share a common likelihood formulation that combines information from both observed failures and censored observations. Intuitively, each asset contributes exactly what is known from the data: if it fails, the model should assign high probability to failing around that time; if it does not fail within the observation window, the model should assign high probability to surviving at least up to the last observed time. Let  $t_i$  denote the observed time for unit i (the failure time if the event occurs, or the last observation time if the unit is censored), and let  $\delta_i \in \{0,1\}$  be the event indicator, with  $\delta_i = 1$  if a failure is observed and  $\delta_i = 0$  if the unit is right-censored. Then, under conditional independence, the joint likelihood can be written as:

$$\mathcal{L}(\theta) = \prod_{i=1}^{n} f(t_i \mid z_i; \theta)^{\delta_i} S(t_i \mid z_i; \theta)^{1-\delta_i}$$
(35)

and its log form

$$\ell(\theta) = \sum_{i=1}^{n} \left[ \delta_i \log f(t_i \mid z_i; \theta) + (1 - \delta_i) \log S(t_i \mid z_i; \theta) \right]$$
(36)

Conceptually, failures ( $\delta_i = 1$ ) pull the model toward assigning high probability to an event occurring around the observed time  $t_i$  through the density term  $f(t_i \mid z_i; \theta)$  (equivalently, a log-density contribution  $\log f(t_i \mid z_i; \theta)$ ), whereas right-censored cases ( $\delta_i = 0$ ) pull the model toward assigning high probability of surviving beyond  $t_i$  through  $S(t_i \mid z_i; \theta)$  (a log-survival contribution  $\log S(t_i \mid z_i; \theta)$ ). This formulation ensures that censored assets remain informative: the model is penalized if it predicts low survival probability up to the censoring time, which is essential in PdM where long fault-free operating histories are common. Learning-based survival models are therefore trained by maximizing  $\mathcal{L}(\theta)$  (or equivalently minimizing the negative log-likelihood  $-\ell(\theta)$ ), which integrates both failures and censored observations within a single principled objective [72].

#### 4.5.1. Tree- and Ensemble-Based Models

Tree- and ensemble-based survival models extend classical non-parametric estimators by learning data-driven partitions of the covariate space and attaching a local survival estimate to each partition. The core idea is simple: assets with similar characteristics (e.g., age, design, environment, loading proxies) are grouped together through recursive splits, and each group is assigned its own empirical time-to-event behavior. Because censoring is handled explicitly during splitting and estimation, these methods can exploit both failures and long fault-free operating histories, making them particularly attractive as strong baselines in PdM settings [73].

An important non-parametric learning approach is the Random Survival Forest (RSF), which adapts random forests to survival data with censoring by growing many survival trees and averaging their predictions [74]. Each tree is trained on a bootstrap sample of the data. During tree construction, the algorithm repeatedly splits the dataset into two groups using a covariate and threshold that make the two groups as different as possible in terms of their survival experience (typically measured with log-rank-type criteria), while correctly handling censored observations.

After the tree is grown, each terminal node (leaf)  $\ell$  contains assets that are similar in covariates and therefore expected to have similar failure behavior. The leaf then stores a simple empirical estimate of accumulated risk over time, usually the Nelson–Aalen cumulative hazard,

$$\hat{H}_{\ell}(t) = \sum_{t_{(j)} \le t} \frac{e_{j,\ell}}{r_{j,\ell}} \tag{37}$$

*Sensors* **2026**, *26*, 1915 19 of 40

where the sum runs over the event times *t* (*j*) observed among assets in that leaf, *ej*,<sup>ℓ</sup> is the number of failures at time *t* (*j*) , and *rj*,<sup>ℓ</sup> is the number of assets still operating (at risk) just before *t* (*j*) . In short, RSF groups similar assets and learns a local, censoring-aware risk curve for each group, then combines many such trees to obtain a stable survival prediction.

For a new asset with covariates *z*, each tree *m* routes *z* to a terminal node (leaf) and returns a leaf-level estimate of the cumulative hazard, denoted as *H*ˆ (*m*) (*t* | *z*). A common forest-level aggregation averages these tree-specific cumulative hazards,

$$\overline{H}(t \mid z) = \frac{1}{M} \sum_{m=1}^{M} \hat{H}^{(m)}(t \mid z) \qquad \overline{S}(t \mid z) = \exp(-\overline{H}(t \mid z))$$
(38)

yielding a smooth and stable survival estimate *S*(*t* | *z*) for the asset. Equivalently, some implementations average the tree-level survival functions *S*ˆ(*m*) (*t* | *z*) = exp(−*H*ˆ (*m*) (*t* | *z*)) directly. In practical terms, RSF can be viewed as combining many weak survival estimators, each capturing a different partition of the feature space, into a robust, non-parametric predictor that models non-linear effects and high-order interactions, while remaining censoring-aware by construction.

From a PdM perspective, RSF is valuable because it (i) handles mixed numerical and categorical covariates with minimal preprocessing, (ii) naturally models interaction-driven risk mechanisms (e.g., soil type matters differently at different ages), and (iii) provides interpretable diagnostics such as variable importance and partial dependence-style summaries that support engineering validation. Related extensions include boosted survival trees and survival boosting variants, which can improve discrimination in some regimes at the expense of additional tuning complexity [\[57\]](#page-37-24).

### 4.5.2. Neural Cox (PH-Structured Deep Survival)

Neural Cox models preserve the proportional hazards (PH) structure of the classical Cox model, but replace the linear predictor *β* <sup>⊤</sup>*<sup>z</sup>* with a flexible, learned risk function *<sup>g</sup><sup>θ</sup>* (*z*). In practice, a neural network takes the covariates *z* as input and outputs a scalar log-risk score *g<sup>θ</sup>* (*z*), allowing complex and non-linear combinations of features (e.g., interactions between operating conditions and asset attributes) to influence failure risk [\[75,](#page-38-14)[76\]](#page-38-15). The hazard is modeled as

<span id="page-19-1"></span>
$$h(t \mid z) = h_0(t) \exp(g_{\theta}(z))$$
(39)

where *h*0(*t*) is an unspecified baseline hazard shared across the population, and exp(*g<sup>θ</sup>* (*z*)) acts as an asset-specific relative-risk multiplier.

Training does not require specifying *h*0(*t*). Instead, the network parameters *θ* are learned by maximizing Cox's partial likelihood, which compares each observed failure to the set of assets that were still at risk at that time. With the risk set R(*ti*) = {*j* : *t<sup>j</sup>* ≥ *ti*}, the standard objective is the negative log-partial-likelihood

<span id="page-19-0"></span>
$$L_{\text{Cox}}(\theta) = -\sum_{i:\delta_i = 1} \left[ g_{\theta}(z_i) - \log \sum_{j \in \mathcal{R}(t_i)} \exp(g_{\theta}(z_j)) \right]$$
(40)

Intuitively, Equation [\(40\)](#page-19-0) encourages the model to assign higher risk scores to assets that fail earlier than their peers in the corresponding risk sets, while censored assets still contribute through their membership in R(*ti*) whenever they remain under observation. Importantly, neural Cox models retain the Cox interpretability in terms of hazard ratios: for two assets with covariates *z*<sup>1</sup> and *z*2,

$$\frac{h(t \mid z_1)}{h(t \mid z_2)} = \exp(g_{\theta}(z_1) - g_{\theta}(z_2))$$
(41)

*Sensors* **2026**, *26*, 1915 20 of 40

so the model provides a principled relative ranking of failure risk while allowing non-linear covariate effects [\[77\]](#page-38-16). In PdM applications, neural Cox models are therefore attractive when proportional scaling of baseline risk is reasonable, but the covariate–risk relationship is too complex to be captured by a linear index, and censoring-aware training remains essential for learning from long fault-free operating histories.

Beyond the standard Cox model and its basic neural PH implementation, a broader set of Cox-oriented formulations has become important in modern survival modelling. In this review, these approaches are treated as extensions within the Cox-based semi-parametric and learning-based families rather than as separate top-level categories. Representative examples include DeepSurv-style models, which replace the linear risk term with a non-linear learned representation while retaining the proportional-hazards structure; penalized Cox variants, which improve robustness and variable selection in high-dimensional settings; multi-task Cox-type formulations, which enable shared representation learning across related asset groups, operating regimes, or failure mechanisms; and dynamic formulations that accommodate covariates updated over time. These extensions are particularly relevant in predictive maintenance because they preserve censoring-aware estimation and the familiar hazard-based interpretation of Cox models, while improving flexibility for heterogeneous sensor inputs, correlated features, and temporally evolving operating conditions.

# 4.5.3. Neural Parametric/Neural Weibull Models

Neural parametric survival models take a direct probabilistic approach: instead of learning only a relative risk score (as in Cox-type models), they learn an asset-specific survival distribution. The key idea is to keep a familiar parametric lifetime family so that *S*(*t* | *z*) and *h*(*t* | *z*) remain explicit and operationally interpretable, but let a neural network predict the distribution parameters from covariates *z*. This combines the extrapolation and decision-friendly outputs of parametric reliability models (e.g., closed-form failure probabilities over a planning horizon) with the flexibility of deep learning to capture non-linear covariate effects and interactions [\[78\]](#page-38-17).

A common and practically useful instance is the neural Weibull model, where the network outputs positive shape and scale parameters, *α*(*z*) > 0 and *λ*(*z*) > 0. The resulting survival and hazard functions are given in Equations [\(42\)](#page-20-0) and [\(43\)](#page-20-1), respectively:

<span id="page-20-0"></span>
$$S(t \mid z) = \exp\left[-\left(\frac{t}{\lambda(z)}\right)^{\alpha(z)}\right] \tag{42}$$

<span id="page-20-1"></span>
$$h(t \mid z) = \frac{\alpha(z)}{\lambda(z)} \left(\frac{t}{\lambda(z)}\right)^{\alpha(z)-1} \tag{43}$$

This parameterization has an intuitive interpretation: *λ*(*z*) sets the time scale of the lifetime (larger values imply longer expected life), while *α*(*z*) controls how failure intensity evolves with age (e.g., increasing wear-out when *α*(*z*) > 1). By allowing both parameters to depend on *z*, the model can represent heterogeneous aging patterns across a fleet. For example, two assets with the same age may still have different hazard trajectories due to differences in environment, loading proxies, or condition indicators.

If *α*(*z*) is constrained to be constant (independent of *z*), the model reduces to a classical Weibull regression form where covariates mainly rescale lifetime through *λ*(*z*). In the fully flexible neural setting, both *α*(*z*) and *λ*(*z*) can vary with *z*, allowing covariates to change not only the time scale of failure but also the shape of the hazard curve (e.g., stronger wear-out acceleration for degraded assets). Training is performed by maximizing the censoringaware likelihood introduced earlier, where failures contribute log *f*(*t<sup>i</sup>* | *zi*) and censored cases contribute log *S*(*t<sup>i</sup>* | *zi*) computed from the instance-specific Weibull. This yields an

*Sensors* **2026**, *26*, 1915 21 of 40

explicit survival curve per asset, enabling direct horizon risk calculations (e.g., Pr(*T* ≤ *τ* | *z*)) and quantitative RUL estimation; when a single Weibull is insufficient, mixture-based extensions such as Deep Survival Machines can capture multi-modal lifetime patterns.

From an asset-management perspective, neural parametric models are attractive because they output a full survival curve per asset, enabling direct computation of planning quantities such as (i) failure probability within a horizon [0, *τ*], (ii) survival quantiles (e.g., median life), and (iii) time-dependent hazard-based prioritization. They also integrate naturally into simulation and optimization pipelines that require sampling or quantile evaluation. The main trade-off is that parametric assumptions matter: if the chosen family is too restrictive, the model may be miscalibrated, especially when extrapolating beyond the observed age range. To address multi-modal or highly heterogeneous lifetime patterns, mixture-based extensions (e.g., Deep Survival Machines) replace a single Weibull with a mixture of parametric components, while retaining a likelihood-based, censoring-aware training objective.

### 4.5.4. Transformer and Sequence-to-Survival Models

Transformer and sequence-to-survival models represent the most expressive class of learning-based survival approaches, designed to exploit the high-dimensional and often temporally ordered data that arise in modern PdM settings. Unlike classical survival regression, which typically relies on a fixed set of handcrafted covariates, these models first learn a representation from heterogeneous inputs, such as mixed tabular features, event logs, or time-series sensor histories *x*1:*<sup>t</sup>* , and then map that representation to a survival object (e.g., a risk score, a hazard function, or distribution parameters). The central benefit of attention-based architectures is that they can model complex cross-feature interactions and long-range temporal dependencies, which are common in degradation processes where risk is driven by combinations of operating regimes rather than any single variable.

A generic formulation is to encode the available information into a latent representation

$$r_{\theta} = \text{Transformer}_{\theta}(\text{tokens or } x_{1:t})$$
 (44)

and then use a task-specific head to produce a survival prediction. For example, in a Cox-style (PH) design, the head outputs a log-risk score *g<sup>θ</sup>* (*z*) and the hazard is written as Equation [\(39\)](#page-19-1). Here, *g<sup>θ</sup>* (*z*) is now computed from the transformer representation (and *z* may include static covariates together with features extracted from the sequence). Alternatively, the head can output parametric survival parameters (e.g., *α*(*z*) and *λ*(*z*) for a Weibull layer), yielding an explicit *S*(*t* | *z*) as in neural parametric survival.

More broadly, transformer-based survival models are well suited when the available data are heterogeneous (categorical, numerical, and possibly sequential) and when degradation signatures depend on combinations of variables across time. However, these models require careful problem formulation to remain valid for survival prediction:

- **Leakage control:** the representation at time *t* must use only information available up to the censoring or prediction time; otherwise the model may learn post-failure patterns and overestimate performance.
- **Censoring-aligned sequences:** for right-censored units, the input history should terminate at the last observation time to avoid introducing artificial future context.
- **Calibration and evaluation:** highly expressive models can be overconfident, so calibration of predicted survival curves (and assessment with censoring-aware metrics) is often required before deployment in maintenance planning.

When these considerations are addressed, transformer and sequence-to-survival models provide a principled way to integrate rich sensor streams into survival-based RUL

Sensors **2026**, 26, 1915

estimation and horizon risk forecasting, enabling more individualized and responsive PdM decisions.

Table 3 summarizes the corresponding formulas for parametric and learning-based survival models, including censoring-aware objectives used for model training.

<span id="page-22-0"></span>
 Table 3. Summary of core survival-model formulas (parametric and learning-based).

| Model/Quantity             | Formula(s)                                                                                                                                                                                                                                          | Notes                                             |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| Weibull                    | $h(t) = \frac{\alpha}{\lambda} \left( \frac{t}{\lambda} \right)^{\alpha - 1}$ $S(t) = \exp \left[ -\left( \frac{t}{\lambda} \right)^{\alpha} \right]$                                                                                               | Parametric; monotone hazard                       |
| Exponential                | $h(t) = \frac{1}{\lambda}$ $S(t) = \exp\left(-\frac{t}{\lambda}\right)$                                                                                                                                                                             | Weibull with $\alpha=1$                           |
| Gompertz                   | $h(t) = b e^{at}$ $S(t) = \exp\left[-\frac{b}{a}(e^{at} - 1)\right], a \neq 0$                                                                                                                                                                      | Exponentially changing hazard                     |
| Log-normal (AFT)           | $\ln T = \beta^{\top} z + \sigma \epsilon, \ \epsilon \sim \mathcal{N}(0, 1)$ $S(t) = 1 - \Phi\left(\frac{\ln t - \mu}{\sigma}\right)$                                                                                                              | Non-monotone hazard possible                      |
| Log-logistic               | $S(t) = 1 - \Phi\left(\frac{\ln t - \mu}{\sigma}\right)$ $S(t) = \frac{1}{1 + (\lambda t)^k}$ $h(t) = \frac{\lambda k t^{k-1}}{1 + (\lambda t)^k}$ $f(t) = \frac{1}{\Gamma(\kappa)\theta^{\kappa}} t^{\kappa-1} \exp\left(-\frac{t}{\theta}\right)$ | Peaked hazard when $k > 1$                        |
| Gamma                      | $f(t) = \frac{1}{\Gamma(\kappa)\theta^{\kappa}} t^{\kappa - 1} \exp\left(-\frac{t}{\theta}\right)$ $S(t) = \frac{\Gamma(\kappa, t/\theta)}{\Gamma(\kappa)},  h(t) = \frac{f(t)}{S(t)}$                                                              | Uses (in)complete Gamma functions                 |
| Censoring-aware likelihood | $\mathcal{L}(\theta) = \prod_{i=1}^{n} f(t_i \mid z_i; \theta)^{\delta_i} S(t_i \mid z_i; \theta)^{1-\delta_i}$ $\ell(\theta) = \sum_{i=1}^{n} \left[ \delta_i \log f(t_i \mid z_i; \theta) + (1-\delta_i) \log S(t_i \mid z_i; \theta) \right]$    | Likelihood-based training                         |
| RSF (leaf NA)              | $\hat{H}_\ell(t) = \sum_{t_{(j)} \leq t} \frac{e_{j,\ell}}{r_{j,\ell}}$                                                                                                                                                                             | Leaf cumulative hazard                            |
| RSF aggregation            | $\overline{H}(t \mid z) = \frac{1}{M} \sum_{m=1}^{M} \widehat{H}^{(m)}(t \mid z)$ $\overline{S}(t \mid z) = \exp(-\overline{H}(t \mid z))$                                                                                                          | Forest prediction                                 |
| Neural Cox                 | $h(t \mid z) = h_0(t) \exp(g_{\theta}(z))$ $L_{\text{Cox}}(\theta) = -\sum_{i: \delta_i = 1} \left[ g_{\theta}(z_i) - \log \sum_{j \in \mathcal{R}(t_i)} \exp(g_{\theta}(z_j)) \right]$                                                             | PH-structured deep survival                       |
| Neural Weibull             | $S(t \mid z) = \exp\left[-\left(\frac{t}{\lambda(z)}\right)^{\alpha(z)}\right]$ $h(t \mid z) = \frac{\alpha(z)}{\lambda(z)}\left(\frac{t}{\lambda(z)}\right)^{\alpha(z)-1}$                                                                         | Neural network outputs $\alpha(z)$ , $\lambda(z)$ |
| Transformer representation | $r_{\theta} = \text{Transformer}_{\theta}(\text{tokens or } x_{1:t})$                                                                                                                                                                               | Sequence encoder                                  |

*Sensors* **2026**, *26*, 1915 23 of 40

# *4.6. Evaluation Metrics for Time-to-Event Prediction*

Model evaluation for survival models must balance several aspects, including discrimination, calibration, accuracy of RUL estimates, and proper scoring. Key metrics in these categories and their interpretation for PdM are outlined.

# 4.6.1. Discrimination (Ranking Ability)

Discriminative metrics evaluate how well a survival model can rank assets by their risk of earlier failure. A widely used measure is Harrell's concordance index (C-index) [\[79\]](#page-38-18). The C-index is the proportion of usable asset pairs for which the model assigns higher risk to the asset that fails earlier. A C-index of 1.0 indicates perfect ranking, 0.5 corresponds to random ordering, and values below 0.5 indicate worse-than-random ranking performance [\[80\]](#page-38-19). In PdM, a high C-index implies the model reliably prioritizes high-risk assets (shorter RUL) ahead of low-risk assets for inspection or intervention. Extensions assess discrimination at specific horizons, such as time-dependent concordance measures that evaluate concordance up to a given time *t* or across time. Ref. [\[81\]](#page-38-20) proposed an inverse probability of censoring weighting (IPCW)-adjusted C-index to improve performance under heavy censoring. Another common discrimination metric is the time-dependent AUC (area under the ROC curve), which treats survival prediction as a sequence of classification tasks at time *t*: distinguishing assets that fail by *t* from those that survive beyond *t* using a time-*t* risk score (often derived from *S*(*t* | *z*)) [\[82\]](#page-38-21). For example, an AUC(*t*) = 0.85 indicates that, at horizon *t*, a randomly chosen asset that fails by *t* is assigned higher risk than a randomly chosen asset that survives beyond *t* in 85% of such comparisons.

# 4.6.2. Calibration

Calibration describes whether the model's predicted risks can be trusted as actual probabilities. A simple intuition is that if 100 assets are each predicted to have a 20% chance of failing within the next month, then about 20 failures within that month should be observed [\[83\]](#page-38-22). Unlike discrimination metrics (which focus on ranking), calibration checks the numerical accuracy of predicted probabilities and survival curves, which is essential when predictions are used for planning and budgeting.

A common way to assess calibration is a calibration plot (reliability diagram). For a chosen horizon, assets are grouped by predicted risk (e.g., low to high predicted failure probability), and for each group the average predicted risk is compared with the observed fraction of failures. A well-calibrated model produces points close to the diagonal, meaning predicted equals observed. The expected calibration error (ECE) summarizes this idea with a single number: it averages the mismatch between predicted and observed frequencies across the groups (smaller is better). Since calibration can change with the forecast horizon, it is good practice to check more than one horizon; a model may appear calibrated for short-term risk but drift at longer horizons [\[81\]](#page-38-20).

To evaluate calibration over the entire predicted time-to-event distribution (not just one horizon), distribution calibration (D-calibration) provides a more global check. In simple terms, it tests whether observed failures occur at times that are consistent with the model's predicted survival curves across the population. Large systematic deviations indicate that the predicted distributions are misaligned with reality. In practice, calibration is often examined using a combination of visual diagnostics (e.g., comparing an average predicted survival curve with the Kaplan–Meier estimate) and summary statistics, to ensure that predicted risks are suitable for decision-making. In PdM, good calibration helps avoid unnecessary interventions caused by inflated risk estimates and missed failures caused by overly optimistic survival predictions [\[81\]](#page-38-20).

*Sensors* **2026**, *26*, 1915 24 of 40

# 4.6.3. Accuracy of RUL Estimates

In PdM, it is often not enough to rank assets by risk; practitioners also need the predicted time to failure, usually reported as RUL. When a model outputs a single RUL value, a natural evaluation is the mean absolute error (MAE) between predicted and observed failure times: an MAE of 10 days means predictions are off by about 10 days on average. Under right censoring, however, the true failure time is unknown for many assets, so MAE cannot be computed directly for those cases [\[84\]](#page-38-23). Reporting MAE only on failed assets can therefore be biased, especially when long-lived assets are mostly censored. Common remedies include censoring-aware error definitions (e.g., using lower-bound errors for censored units) and estimators that incorporate censored data through pseudoobservations [\[85\]](#page-38-24). If uncertainty is reported (e.g., prediction intervals), coverage is also important: a nominal 90% interval should contain the true failure time about 90% of the time; deviations indicate over- or under-confidence. Overall, these measures complement discrimination by quantifying how accurate the predicted RUL is in practical time units.

### 4.6.4. Proper Scoring Rules (Brier Score)

To evaluate survival predictions as probabilities (not only rankings), proper scoring rules compare the predicted survival curve to what actually happens. The most widely used is the Brier score (BS), which is a time-dependent analogue of mean squared error [\[86,](#page-39-0)[87\]](#page-39-1). At a fixed horizon *t*, it measures how close the predicted survival probability *S*ˆ(*t* | *xi*) is to the observed survival status by *t*. Specifically,

$$BS(t) = \frac{1}{n} \sum_{i=1}^{n} \left( \mathbb{I}\{T_i > t\} - \hat{S}(t \mid x_i) \right)^2$$
 (45)

where I{*T<sup>i</sup>* > *<sup>t</sup>*} equals 1 if the asset survives beyond *<sup>t</sup>* and 0 otherwise. Lower values indicate more accurate probabilistic predictions.

With right censoring, I{*T<sup>i</sup>* > *<sup>t</sup>*} is not always observable, so unbiased estimation typically uses IPCW, where each term is reweighted by the estimated chance of remaining uncensored up to *t* (often obtained from a Kaplan–Meier estimate of the censoring distribution). The Brier score is commonly reported as a function of time (a prediction error curve) and summarized by the Integrated Brier Score (IBS), which averages BS(*t*) over a time interval of interest [\[88\]](#page-39-2). Because the Brier score is a proper scoring rule, it rewards well-calibrated probabilities; unlike the C-index, it penalizes both misranking and miscalibration, making it particularly useful when PdM decisions depend on reliable horizon failure probabilities.

To make the evaluation criteria more explicit, several key metrics can be written in mathematical form. For discrimination at a specific horizon *t*, the time-dependent AUC is defined as

$$AUC(t) = Pr(\hat{r}_i(t) > \hat{r}_j(t) \mid T_i \le t, T_j > t), \tag{46}$$

where *r*ˆ*i*(*t*) denotes the predicted risk score for asset *i* at time *t*, and *T<sup>i</sup>* is the observed event time. This metric quantifies the probability that an asset failing by time *t* receives a higher predicted risk than one surviving beyond *t*.

For calibration at horizon *t*, let *p*ˆ*i*(*t*) = 1 − *S*ˆ(*t* | *zi*) denote the predicted failure probability for asset *i*. If the assets are grouped into *B* bins, the expected calibration error (ECE) can be expressed as

$$ECE(t) = \sum_{b=1}^{B} \frac{n_b}{n} |\bar{p}_b(t) - \bar{y}_b(t)|, \tag{47}$$

Sensors **2026**, 26, 1915 25 of 40

where  $n_b$  is the number of samples in bin b, n is the total number of samples,  $\bar{p}_b(t)$  is the mean predicted failure probability in bin b, and  $\bar{y}_b(t)$  is the corresponding observed failure frequency. Lower ECE values indicate better agreement between predicted and observed risk.

When the model outputs a point estimate of RUL, a basic error measure is the mean absolute error (MAE), given by

$$MAE_{RUL} = \frac{1}{n_f} \sum_{i:\delta_i = 1} \left| \widehat{RUL}_i - RUL_i \right|, \tag{48}$$

where  $\widehat{\text{RUL}}_i$  is the predicted RUL for asset i, RUL $_i$  is the true remaining useful life,  $\delta_i$  is the event indicator, and  $n_f$  is the number of observed failures.

Finally, the IBS over the interval  $[0, \tau]$  is defined as

$$IBS(\tau) = \frac{1}{\tau} \int_0^{\tau} BS(t) dt, \tag{49}$$

where BS(t) is the Brier score at time t. The IBS summarizes the overall probabilistic prediction error across time, with lower values indicating better predictive performance.

# 5. Applications of Survival Models in Energy Systems

Electricity DSOs and DHN companies increasingly embed survival analysis into asset management to translate predictive insights into operational decisions. DSOs can rank assets by failure risk and schedule replacements before end-of-life, and DHNs can plan proactive pipe repairs or intensified monitoring on vulnerable segments. In the following, practical applications in electricity distribution and district heating asset management are discussed.

### 5.1. Electricity Distribution Applications

Survival analysis has been applied to a range of electricity distribution assets, often grouped by asset class.

#### 5.1.1. Underground Cables

MV and low-voltage (LV) power cables are a major focus due to their extensive installed length and failure impact. Cox proportional hazards models are frequently used to identify which cable attributes drive failure risk. For example, ref. [89] analyzed historical failure data for MV distribution cables (10 kV) and high-voltage (HV) transmission cables (110–220 kV) from a Chinese utility using a multivariate Cox PH model, finding that certain covariates (like cable type and joint manufacturer) increase hazard rates. This Cox approach proved more robust than a homogeneous Weibull fit for these cables, as it could accommodate heterogeneous populations and even single out a problematic batch of cable joints (a manufacturing defect) for targeted replacement.

Figure 6 highlights a clear shift in the dominant failure mechanisms between MV and HV cable populations [89]. MV cable failures are primarily associated with third-party damage, whereas HV failures are more strongly linked to manufacturing-quality-related causes, with smaller contributions from unknown, aging, and installation-related factors. This contrast underscores the heterogeneous nature of cable deterioration and reinforces the need for covariate-aware survival models rather than homogeneous lifetime assumptions.

*Sensors* **2026**, *26*, 1915 26 of 40

<span id="page-26-0"></span>![](_page_26_Figure_1.jpeg)

**Figure 6.** Failure-cause composition of MV and HV cable populations based on [\[89\]](#page-39-3).

Similarly, ref. [\[48\]](#page-37-15) applied survival modeling to LV cable networks, quantifying how factors such as conductor material, loading level, and soil conditions affect cable failure frequencies. Their study demonstrated that incorporating such covariates enables more refined asset health indices, improving the asset manager's ability to prioritize cable sections for intervention. Other studies have extended cable failure analysis, such as [\[90\]](#page-39-4), which performed spatial survival analysis on aging paper-insulated cables to pinpoint regions of accelerated deterioration. Ref. [\[3\]](#page-35-2) reported baseline failure rates for MV XLPE cables from national statistics, providing a benchmark for probabilistic life models. Ref. [\[91\]](#page-39-5) compared Weibull and Crow-AMSAA models for early cable joint failures, finding that a Weibull-based hazard model better captured the increasing failure rate after an initial infant mortality period. In recent years, machine learning (ML) approaches have also been applied to cable maintenance.

Ref. [\[92\]](#page-39-6) developed an artificial neural network model to predict the insulation health index of in-service XLPE cables, allowing early identification of degrading cable segments and thus supporting proactive replacements. Across these studies, cable failure models support renewal planning by identifying high-risk cables (beyond what age alone would indicate) and by estimating the residual life benefits of mitigations like improved installation practices. In addition, the correlation analysis reported in [\[92\]](#page-39-6) shows that cable age is strongly associated with key degradation indicators, particularly partial discharge and natural corrosion, while the health index exhibits a pronounced inverse relationship with these variables (Figure [7\)](#page-27-0). This further highlights that cable deterioration is shaped by interacting electrical, environmental, and condition-related factors rather than by age alone, thereby reinforcing the value of multivariate, data-driven models for cable condition assessment and maintenance decision support.

*Sensors* **2026**, *26*, 1915 27 of 40

<span id="page-27-0"></span>![](_page_27_Figure_1.jpeg)

**Figure 7.** Correlation heatmap of cable condition variables and health index for in-service XLPE cables, adapted from [\[92\]](#page-39-6).

Overhead distribution lines have also been studied with survival analysis techniques, although failures are rarer in lines than in aging cables. An illustrative example is [\[93\]](#page-39-7), which developed a hierarchical Bayesian model for overhead line failure rates. They combined outage data from multiple regions and line populations, accounting for population variability (differences in line design, environment, and maintenance history) through random effects in a Poisson regression model. This approach (a Bayesian survival regression) allowed them to estimate credible failure rate distributions for overhead lines even with sparse failure observations. By including region-specific random effects, the model identified which line sub-populations had higher baseline hazard.

# 5.1.2. Distribution Transformers

Aging distribution transformers (typically 10–20 kV) have also been studied with survival models to support maintenance and replacement decisions. A common approach is to fit parametric lifetime distributions or Cox regressions to long-term failure data. Ref. [\[94\]](#page-39-8) investigated failure and retirement statistics for a fleet of Australian power transformers spanning multiple voltage levels, using non-parametric survival curves (Kaplan–Meier estimates) and parametric fits (Weibull models) to characterize the transformers' lifetimes. The fitted Weibull models allowed them to estimate age-dependent failure probabilities and thus suggest optimal replacement ages for different classes of transformers. Ref. [\[95\]](#page-39-9) took a two-part approach for utility transformers: first modeling aging-related failures with a Weibull time-to-failure law, then extending to a combined model with both random (chance) failures and wear-out failures. By using Monte Carlo simulations based on these Weibull hazard models, they showed how many years of data (and how many failure events) are needed to confidently predict transformer end-of-life which is an important practical insight for utilities with limited failure records. More recently, attention has turned to time*Sensors* **2026**, *26*, 1915 28 of 40

varying covariates that influence transformer survival. Ref. [\[96\]](#page-39-10) integrated eleven years of distribution transformer failure data from South Korea with detailed local weather records in a Cox PH model to quantify how environmental stress (e.g., high ambient temperature and humidity) contributes to transformer failures. They report that extreme hot and humid conditions correspond to elevated hazard ratios for transformer failure. In a similar vein, the RUL of distribution transformers under rising electric vehicle (EV) loading stress is estimated by [\[19\]](#page-36-12), finding that heavy EV charging penetration measurably accelerates the transformers' wear-out rate. To incorporate multiple degradation processes, some works combine physics-based and data-driven models. For example, ref. [\[97\]](#page-39-11) proposed a hybrid prognostics framework for power transformers that blends a physical degradation model with survival analysis, improving failure time predictions under fluctuating renewable loading conditions.

# 5.1.3. Switchgear and Substation Devices

Beyond cables and transformers, utilities have applied survival analysis to switchgear components such as disconnectors, circuit breakers, and instrument transformers. Ref. [\[98\]](#page-39-12) examined MV disconnect switches and reclosers using a Cox model, leveraging failure logs before and after certain interventions. Specifically, the installation of remote control and the adoption of preventive overhaul to compare hazard rates. The Cox analysis showed that remotely controlled switches had a lower hazard of failure (since manual switching operations were eliminated), and that devices receiving periodic maintenance likewise exhibited reduced failure rates. This translates into decision support for maintenance policy. The model provided quantitative evidence that automation and proactive overhaul both extend the survival of switchgear, thereby averting in-service failures. Ref. [\[99\]](#page-39-13) analyzed the reliability of high-voltage instrument transformers (voltage and current transformers) using survival methods. They employed Kaplan–Meier estimators to establish baseline failure probabilities over time and Cox regression to assess covariate effects such as loading, manufacturer, and installation environment. The resulting failure rate estimates enabled a risk-ranked replacement plan for the utility. Instrument transformers with the highest estimated risk (for example, certain models operating under high loading stress) were prioritized for pre-emptive replacement, thereby preventing potential outages. In the realm of circuit breakers, statistical life models have also been applied. For instance, ref. [\[100\]](#page-39-14) analyzed field failure records of HV SF<sup>6</sup> breakers and fitted a Weibull distribution to determine the wear-out age of breaker contacts. This study provided an estimated life distribution for breakers and recommended overhaul intervals (e.g., mid-life refurbishments) to prevent in-service failures. Additionally, some studies adopt Bayesian or data-driven updating approaches using condition-monitoring data (e.g., contact wear measurements or the number of operations) to continually refine breaker failure rate estimates. In all these cases, survival-based methods convert historical performance and condition data into actionable insights, identifying which substation components are most likely to fail next and what operational measures can mitigate that risk.

#### *5.2. District Heating Network Applications*

Statistical life modeling has only recently been applied to DHN systems, which historically relied on deterministic life estimates. Ref. [\[101\]](#page-39-15) outline a new asset management approach for DHNs that replaces static lifespan assumptions with data-driven failure predictions, explicitly suggesting the use of survival analysis to prioritize pipe renewals based on observed failure trends. Following this vision, authors in [\[13\]](#page-36-6) conducted one of the first comprehensive survival analyses on a modern DHN pipe network. They gathered about 20 years of failure records for underground steel pipe segments in a Danish district

*Sensors* **2026**, *26*, 1915 29 of 40

heating system, alongside each pipe's characteristics (age, diameter, insulation type, soil type) and operating history. Given that the network is relatively young (many pipes had not yet failed), the authors tested both classical and novel survival models while addressing the data scarcity. In particular, they compared a Weibull proportional hazards model (a parametric cohort model often used in water distribution pipes, derived from Herz's exponential wear-out model) and a modern neural-network-based Cox model (neural Weibull PH) that can flexibly fit hazard functions even with missing data. To accommodate common data deficiencies (such as unknown installation dates or censored failure times), they modified the likelihood functions of these models which allowed the survival analysis to make the best use of incomplete records. The outcome of this study was two-fold; first, they found that data-driven models can indeed differentiate pipe segments by risk better than the traditional age-based approach. For example, pipes in certain corrosive soil types or with higher pressure cycling showed measurably higher hazards, even if not the oldest. Second, their evaluation highlighted the difficulty of validating distributional assumptions in young networks. However, the Weibull model's wear-out shape could not be conclusively confirmed due to the limited number of late-life failures, suggesting that pooling data from multiple utilities or waiting for more failure observations is necessary to refine long-term life estimates. For the DHN operator, the practical output was a ranked list of pipe sections by failure probability, enabling a shift from purely reactive maintenance to prioritized renewal of the highest-risk pipes.

Reference [\[102\]](#page-39-16) performed an earlier reliability analysis on a district heating system, developing an integrated failure probability assessment for a municipal DHN network. This work underscored the need for more sophisticated statistical models (like survival analysis) to supplement basic lifetime estimates in DHN infrastructure. Beyond purely data-driven models, other DHN pipe studies have drawn on system reliability methods as well. Ref. [\[103\]](#page-39-17) approached the problem from a network reliability perspective, simulating a repairable DHN system under varying external conditions to evaluate its availability and failure frequency. By modeling how seasonal demand swings and temperature fluctuations affect pipe stress and leak rates, they provided insight into how the hazard of pipe failure might increase during peak load periods (late winter, when pipes have endured maximum thermal stress), which is useful for maintenance scheduling. Although such system-level analyses are not survival models in a strict sense, they complement component-level survival predictions by examining the operational contexts in which those failures occur.

Beyond pipelines, some work has applied survival analysis to district heating equipment like pumps and valves, though this area is less developed. Ref. [\[13\]](#page-36-6) notes in their PdM survey of DHN that mechanical components (e.g., circulation pumps in boiler houses) could also benefit from survival-based failure modeling, despite the limited run-to-failure data available for such equipment. For instance, ref. [\[104\]](#page-39-18) developed a Random Survival Forest model for large water pumps, which was capable of handling small samples of failure data by leveraging ensemble learning. The model identified an early infant mortality phase in pump failure rates followed by a longer period of lower hazard, aligning with the typical bathtub curve, and used this insight to optimize maintenance intervals for pumps (i.e., more frequent checks early on, then steady monitoring during the long reliable period). By analogy, DHN operators can apply similar approaches to predict failures of critical pumps in heat production plants or substations, improving planning for spare units and overhauls [\[105\]](#page-39-19). Overall, however, pipes remain the primary focus in DHNs, and as more failure data accumulate, increasing use of survival models (from simple Weibull analyses to advanced ML survival models) is expected to guide pipe replacement planning, leak detection strategies, and life-extension measures (like cathodic protection retrofits and re-insulation scheduling).

Sensors 2026, 26, 1915 30 of 40

Figure 8 summarizes the application landscape discussed in this section by linking representative asset classes in electricity distribution and district heating to the main survival-model families, typical input data, and decision-oriented outputs. As illustrated, these applications rely on combining asset descriptors, condition indicators, operational stressors, and contextual information to estimate survival, hazard, failure probability, and risk ranking. This integrated view highlights that survival analysis in smart energy networks is not only a modelling framework for failure prediction, but also a practical decision-support tool for inspection planning, maintenance prioritization, refurbishment, and replacement.

<span id="page-30-0"></span>![](_page_30_Figure_2.jpeg)

**Figure 8.** Overview of survival-model applications, inputs, outputs, and maintenance actions across electricity distribution and district heating systems.

#### 5.3. Public Benchmark Datasets and Reproducibility

Publicly available benchmark datasets for predictive maintenance and time-to-event modelling in smart energy systems remain limited, especially for asset classes with explicit failure times, censoring information, and continuous asset-level histories. To support reproducible evaluation and practical adoption, Table 4 summarizes representative public datasets in terms of asset type, data modalities, time resolution, sample size, and whether failure times, censoring, or delayed entry can be constructed.

**Table 4.** Representative public datasets relevant to predictive maintenance and time-to-event modelling in smart energy systems.

| Asset Type                                          | Data Modalities                                 | Time<br>Resolution | Sample Size                  |
|-----------------------------------------------------|-------------------------------------------------|--------------------|------------------------------|
| District heating substations [106]                  | Operational time series and fault/event records | 10-min             | 93 substations;<br>73 faults |
| Wind turbines [107,108]                             | SCADA measurements and fault labels             | 10-min             | 36 turbines;<br>95 datasets  |
| Overhead power lines [109]                          | Three-phase voltage signals with fault labels   | 40 MHz             | 2904 measure-<br>ments       |
| Electric-machine insulation/partial discharge [110] | Multi-channel acoustic recordings               | 96 kHz             | 12,850 samples               |

*Sensors* **2026**, *26*, 1915 31 of 40

<span id="page-31-0"></span>**Table 4.** *Cont*.

| Asset Type                           | Data Modalities                                          | Time<br>Resolution | Sample Size |
|--------------------------------------|----------------------------------------------------------|--------------------|-------------|
| Power<br>transformers [111]          | Dissolved gas analysis<br>measurements with fault labels | Tabular            | 376 samples |
| Power<br>transformers [112]          | DGA measurements with<br>diagnosis labels                | Tabular            | 589 samples |
| Power<br>transmission lines<br>[113] | Simulated voltage/current<br>features with fault labels  | Tabular            | 618 samples |

# *5.4. Practical Model Selection*

The selection of a survival modeling approach in practice is closely tied to (i) asset observability (what data are available and whether they are static or time-varying), (ii) fleet heterogeneity, and (iii) the type of maintenance decision to be supported. If only static asset data (e.g., installation age and design type) and sparse failure events are available, utilities tend to favor simpler, interpretable models. For instance, a Weibull lifetime analysis or a Cox PH model with static covariates is often sufficient to rank assets by risk (addressing point (i)).

On the other hand, when rich condition-monitoring data or time-series sensor inputs exist (vibrations, load profiles, thermal measurements), more dynamic models become viable, such as extended Cox models that allow time-dependent covariates, or even sequencebased survival models, can exploit this greater observability to update failure risk in real time [\[114\]](#page-40-1).

Regarding fleet heterogeneity, a very diverse asset population (in terms of ages, manufacturers, operating environments) might require models that capture unit-specific random effects or that partition the fleet. For example, a stratified Cox model or a Random Survival Forest can accommodate different sub-populations without forcing one-size-fits-all parameters. Conversely, a homogeneous fleet (assets of similar type and age) can often be effectively modeled with a single parametric distribution, assuming that after accounting for the available covariates, each unit's failure time follows the same distribution and is independent of the others.

Finally, the decision context (point (iii)) drives whether the model should output absolute failure time predictions or just relative risk rankings. For risk ranking of assets (choosing which components to inspect or replace first), models like the Cox PH (which excel at relative hazard estimation) are well suited and widely used. However, for timebased planning, engineers often need the full time-to-failure distribution or an expected remaining life. In those cases, parametric survival models or other approaches that yield an explicit survival function (possibly calibrated to real failure probabilities) are preferred, as they can answer "how long until failure?" in probabilistic terms, directly informing maintenance timelines.

The reviewed model families differ not only in predictive flexibility but also in the type and quality of data they require for reliable use. Non-parametric methods such as Kaplan–Meier and Nelson–Aalen are most appropriate when the goal is descriptive fleet-level reliability estimation under censoring, but they are limited when individualized prediction is needed or when many covariates must be incorporated. Parametric models such as Weibull, exponential, or log-logistic are attractive when the available dataset is relatively small, the number of observed failures is limited, and the failure process can be approximated by a simple hazard shape; however, their performance can degrade when the assumed lifetime distribution is poorly matched to the asset physics or operating *Sensors* **2026**, *26*, 1915 32 of 40

environment. Semi-parametric models such as Cox PH are often a practical compromise, but they still require sufficiently informative covariates, a reasonable number of events, and at least approximate compatibility with proportional-hazards behaviour if stable interpretation is desired. When time-varying covariates are used in Cox-type models, the data must also support reliable temporal alignment between sensor updates, asset states, and event times.

Tree-based and ensemble methods such as random survival forests are generally more suitable when larger datasets are available and when the relationships between condition indicators and failure risk are non-linear or involve interactions that are difficult to specify manually. However, these models can become unstable when event counts are low, censoring is heavy, or the signal-to-noise ratio of the covariates is weak, because the recursive splits may then reflect sampling noise rather than persistent degradation structure. Learning-based survival models, including deep and Transformer-based approaches, typically impose the strongest data requirements. In practice, they benefit from larger cohorts, richer longitudinal sensing, consistent feature definitions across assets, and careful preprocessing of missing values, irregular sampling, and label uncertainty. Without such data support, these models may overfit, learn spurious operational patterns, or produce predictions that are difficult to validate and interpret in engineering settings. Therefore, the suitability of a survival model should be judged not only by its modelling capacity, but also by whether the available dataset provides adequate event frequency, censoring structure, temporal consistency, and covariate quality for that model family.

In sum, data availability, model interpretability, and decision objectives must be balanced by practitioners; a simple Cox or Weibull model may suffice to prioritize assets by risk, whereas more complex or data-hungry models are justified when high-frequency condition data are available or when precise estimates of failure timing are needed.

From an engineering perspective, the choice between learning-based and classical survival models involves a trade-off between flexibility and deployability. Learning-based models such as RSF and Transformer-based survival models can better capture non-linear interactions and heterogeneous condition patterns, but they often require larger datasets, higher computational effort, and offer less transparent decision logic. These limitations can be important in utility applications, where failures are sparse, censoring is substantial, and model outputs must remain auditable for engineering decision-making. In contrast, parametric and semi-parametric models such as Weibull and Cox PH remain attractive in small- to medium-sample settings because they train quickly, impose low computational burden, and provide interpretable parameters or hazard ratios. Although their structural assumptions may limit flexibility, they often provide a more robust and practical starting point for engineering deployment.

For practical deployment, survival-based PdM can be structured as an end-to-end workflow. First, raw SCADA, AMI, or sensor measurements are collected, aligned to asset identifiers and timestamps, and aggregated into decision-relevant summaries. Next, the event of interest and censoring status are defined for each asset, followed by the construction of static and time-varying covariates while preventing information leakage. The selected survival model is then trained using censoring-aware estimation and evaluated in terms of discrimination, calibration, and probabilistic accuracy. Based on the estimated survival function, horizon-specific failure risk and RUL summaries can be derived for each asset. These outputs are finally translated into maintenance actions, such as inspection, replacement, or prioritization, and the workflow is updated periodically as new operational data becomes available.

*Sensors* **2026**, *26*, 1915 33 of 40

# **6. Practical Challenges in PdM Survival Modelling**

### *6.1. Data Availability, Quality, and Covariate Integration*

An important practical point is that model performance depends not only on the choice of survival method but also on the representativeness and preparation of the input data. Many published studies report results on well-curated and already validated datasets, where labels, observation windows, and failure definitions are relatively clean. In real utility settings, however, sensor data are often noisier, incomplete, weakly aligned with asset events, and affected by changing operating practices. Under such conditions, methods that perform well on curated benchmark data may become unstable or show limited practical value unless preprocessing, event definition, missing-data handling, and leakage control are addressed carefully. Therefore, reliable RUL and PdM analysis requires representative data preparation as a first-order engineering task rather than only a model-selection step.

Despite the diversity of assets, several common themes emerge across the reviewed applications in power and heat networks. Data availability and quality is a universal concern. Utilities often have sparse failure data (since failures are infrequent by design) and many censored observations. For example, performing survival analysis on a relatively young DHN system runs the risk of not observing the wear-out phase at all, making it hard to validate the assumed failure distribution. Similarly, early reliability studies of water and power networks stress that richer failure datasets (spanning a wide range of asset ages, types, and environments) greatly improve model confidence [\[93\]](#page-39-7). This has led to an emphasis on integrating heterogeneous data sources to enhance predictive power. Many studies combine failure logs with other data: asset GIS records (installation dates, asset types, locations), operational sensor readings (loads, temperatures, pressures), environmental factors (soil corrosivity for pipes, weather for overhead lines), and even maintenance history. The inclusion of covariates from these sources is evident in numerous works, from weather effects in transformer models [\[96\]](#page-39-10) to diagnostic test results in cable models (e.g., partial discharge or insulation health index measurements are sometimes used to refine cable hazard estimates [\[9,](#page-36-2)[115\]](#page-40-2). A practical pattern is that adding such covariates can improve prediction accuracy if sufficient historical data exist to reliably estimate their effects. Otherwise, there is a risk of overfitting or inconclusive results. Data limitations have also spurred methodological adaptations, such as Bayesian updating techniques and modified likelihood functions, to make the most of small samples and incomplete information. For example, a recent study combined Bayesian network modeling with Weibull analysis to incorporate expert knowledge and conditional dependencies in cable failure predictions [\[116\]](#page-40-3). In general, utilities have adopted stopgap measures like expert elicitation and conservative design margins to cope with sparse data, but the trend is toward systematically augmenting historical data with new sensor streams and multi-utility data pooling to improve survival model robustness.

### *6.2. Model Selection, Complexity, and Interpretability*

Another theme is the choice of survival model family in relation to the use-case requirements. Simpler models (Kaplan–Meier curves, exponential/Weibull parametric distributions, Cox PH with static covariates) remain popular in operational studies because of their interpretability and relatively low data demands. For instance, the Cox model's regression coefficients offer clear insight into which asset factors are risk-increasing or riskmitigating, which is valuable for engineering judgment and has been exploited in multiple asset classes. Likewise, parametric models like the Weibull model are appreciated for yielding an explicit remaining-life distribution that can directly answer the question "how many years until failure with X% probability?," aligning well with maintenance scheduling needs. On the other hand, more complex models (ensemble and ML approaches) are

*Sensors* **2026**, *26*, 1915 34 of 40

gradually appearing as asset datasets grow in size and detail. Random Survival Forests and neural-network–based survival models can capture non-linear covariate interactions and even time-dependent effects, as seen in recent pump and cable case studies [\[92,](#page-39-6)[104\]](#page-39-18). These advanced models often achieve higher predictive performance, especially when there is a wealth of sensor data or high-dimensional inputs, but they introduce practical challenges; the results can be harder to interpret for asset managers, and they typically demand larger datasets for training. A recurrent point across the literature is the need to balance model complexity with transparency. In critical infrastructure contexts, maintainers must trust and understand the model's recommendations. Thus, there is often a preference for models that provide explainable rankings or factor effects, unless the expected operational value strongly justifies a black-box approach. In such cases, post hoc interpretability tools (e.g., feature attribution and rule-based explanations) can be used to improve transparency and facilitate adoption [\[117\]](#page-40-4).

### *6.3. Decision Support and Operational Use*

A third common pattern is how the outputs of survival models are used for decision support. Virtually all the application studies tie the statistical predictions back to maintenance or renewal actions. A predominant use is risk-based asset ranking, where models estimate either the hazard rate or the probability of failure within a given horizon to produce a prioritized list of components. In a broader sense, survival models enable a shift from reactive or calendar-based maintenance to predictive prioritization. Rather than treating all assets as equally likely to fail, resources can be focused on the statistically most vulnerable assets. Another operational output is an estimate of expected lifetime or time-to-failure for asset populations, which is crucial for long-term renewal planning. By fitting a survival curve to asset failure data, utilities can forecast how many failures to expect in the next 5, 10, or 20 years if no action is taken. This informs budgeting and resource allocation. Similarly, other authors have used survival-derived failure projections to compare alternative replacement strategies or to justify the costs of preventive maintenance programs in terms of avoided failures [\[118\]](#page-40-5). Across both electricity and heating domains, the regulatory context (such as reliability-centered regulations or performance-based incentives) is also seen to be pushing operators to adopt these quantitative risk models. For instance, power distributors under performance-based regulation use survival model outputs to demonstrate that their targeted replacement of high-risk cables will improve reliability indices (SAIDI/SAIFI) by a calculable amount. In district heating, where reducing leak rates and improving energy efficiency are growing concerns, survival analysis helps quantify the benefit of proactive pipeline renewals in terms of avoided water loss and heat supply disruptions. Finally, it is noteworthy that the power and DHN sectors are learning from parallel work in the water supply industry. Decades of pipe break modeling research (using statistical survival and reliability models) provide methodologies that can be transferred to energy pipelines [\[119,](#page-40-6)[120\]](#page-40-7). Concepts like cohort survival models for aging infrastructure and the importance of combining expert knowledge with data-driven models are cross-cutting lessons increasingly influencing how survival analysis is applied in smart energy networks.

# **7. Conclusions**

Sensor-enabled smart energy networks increasingly rely on data-driven reliability management to reduce unplanned outages and support risk-informed maintenance planning. In electricity distribution and district heating networks, time-to-event datasets are shaped by the realities of field operation: observation windows are limited, preventive interventions terminate follow-up, and only a fraction of assets fail during the study period. *Sensors* **2026**, *26*, 1915 35 of 40

As a result, censoring and truncation are not peripheral details but defining characteristics of the modeling problem, and they must be handled explicitly in both model formulation and evaluation. This review organized survival modeling approaches for PdM and RUL estimation into a coherent taxonomy spanning non-parametric, semi-parametric, parametric, and learning-based families. Across these model classes, how assumptions interact with the structure of available data was highlighted, ranging from static asset metadata to time-varying covariates derived from sensors, inspections, and operational context. Beyond model choice, these families were mapped to the forms of decision support typically required in practice, including risk ranking, failure probabilities over planning horizons, and full predictive distributions over remaining lifetime. A consistent message is that progress depends as much on disciplined validation as on model sophistication. Reliable PdM and RUL pipelines require evaluation protocols that respect censoring/truncation and that measure both ranking quality and probabilistic accuracy. For researchers, the taxonomy in this paper provides a structured basis for positioning new methods, making assumptions explicit, and reporting results in a manner that is comparable and reproducible. For practitioners, the mapping from model families to data requirements and decision outputs provides a pragmatic guide for selecting and deploying survival models that align with operational objectives and available instrumentation.

**Author Contributions:** Conceptualization, M.R.S. and H.R.S.; methodology, M.R.S. and H.R.S.; investigation, M.R.S., H.M. and M.T.; writing—original draft preparation, M.R.S. and H.M.; writing review and editing, M.R.S., H.M., M.T. and H.R.S.; visualization, M.R.S.; supervision, H.R.S.; project administration, M.T. and H.R.S. All authors have read and agreed to the published version of the manuscript.

**Funding:** This work was funded by the Danish Energy Agency under the Energy Technology Development and Demonstration Program (EUDP), project ID 134241–521237, as part of the IEA DHC Annex TS6.

**Institutional Review Board Statement:** Not applicable.

**Informed Consent Statement:** Not applicable.

**Data Availability Statement:** No new data were created or analyzed in this study. Data sharing is not applicable to this article.

**Acknowledgments:** During the preparation of this manuscript, the authors used a generative AI tool to improve grammar and readability. The authors reviewed and edited the output and take full responsibility for the content.

**Conflicts of Interest:** The authors declare no conflicts of interest.

# **References**

- <span id="page-35-0"></span>1. Sundsgaard, K. Predictive Maintenance of Medium Voltage Cable Networks Using Machine Learning. Ph.D. Thesis, Technical University of Denmark, Lyngby, Denmark, 2025.
- <span id="page-35-1"></span>2. Attanayake, A.S.R.; Ratnayake, R.C. Digitalization of distribution transformer failure probability using Weibull approach towards digital transformation of power distribution systems. *Future Internet* **2023**, *15*, 45. [\[CrossRef\]](http://dx.doi.org/10.3390/fi15020045)
- <span id="page-35-2"></span>3. Hansen, J.Z. Results from Danish failure statistics for medium voltage XLPE cables. In *Proceedings of the 22nd International Conference and Exhibition on Electricity Distribution (CIRED 2013)*; IET: Stevenage, UK, 2013; pp. 1–4.
- <span id="page-35-3"></span>4. Hu, W.; Westerlund, P.; Hilber, P.; Chen, C.; Yang, Z. A general model, estimation, and procedure for modeling recurrent failure process of high-voltage circuit breakers considering multivariate impacts. *Reliab. Eng. Syst. Saf.* **2022**, *220*, 108276. [\[CrossRef\]](http://dx.doi.org/10.1016/j.ress.2021.108276)
- <span id="page-35-4"></span>5. Yi, H.; Wang, X.; Suo, C.; Ghias, A.M.; Gooi, H.B.; Wee, C.T.; Chern, W.K.; Yucel, A.C. A data analytic approach for assessing xlpe cable insulation condition via resistance measurements. *IEEE Trans. Instrum. Meas.* **2025**, *74*, 3528112. [\[CrossRef\]](http://dx.doi.org/10.1109/tim.2025.3555713)
- <span id="page-35-5"></span>6. Rafati, A.; Shaker, H.R. Predictive maintenance of district heating networks: A comprehensive review of methods and challenges. *Therm. Sci. Eng. Prog.* **2024**, *53*, 102722. [\[CrossRef\]](http://dx.doi.org/10.1016/j.tsep.2024.102722)

*Sensors* **2026**, *26*, 1915 36 of 40

<span id="page-36-0"></span>7. Hallberg, D.; Stojanovi´c, B.; Akander, J. Status, needs and possibilities for service life prediction and estimation of district heating distribution networks. *Struct. Infrastruct. Eng.* **2012**, *8*, 41–54. [\[CrossRef\]](http://dx.doi.org/10.1080/15732470903213740)

- <span id="page-36-1"></span>8. van Dinter, R.; Rieken, S.; Tekinerdogan, B.; Catal, C. Estimating optimal replacement time for systems with two-state degradation and technological obsolescence. *Int. J. Electr. Power Energy Syst.* **2025**, *172*, 111137. [\[CrossRef\]](http://dx.doi.org/10.1016/j.ijepes.2025.111137)
- <span id="page-36-2"></span>9. Somsak, T.; Suwanasri, T.; Suwanasri, C. Remaining useful life estimation for underground cable systems based on historical health index. *Energies* **2022**, *15*, 9447. [\[CrossRef\]](http://dx.doi.org/10.3390/en15249447)
- <span id="page-36-3"></span>10. Dong, X.; Jing, Z.; Dai, Y.; Wang, P.; Chen, Z. Failure prediction and replacement strategies for smart electricity meters based on field failure observation. *Sensors* **2022**, *22*, 9804. [\[CrossRef\]](http://dx.doi.org/10.3390/s22249804) [\[PubMed\]](http://www.ncbi.nlm.nih.gov/pubmed/36560173)
- <span id="page-36-4"></span>11. Mortensen, L.K.; Shaker, H.R.; Veje, C.T. Relative fault vulnerability prediction for energy distribution networks. *Appl. Energy* **2022**, *322*, 119449. [\[CrossRef\]](http://dx.doi.org/10.1016/j.apenergy.2022.119449)
- <span id="page-36-5"></span>12. Garro, U.; Muxika, E.; Aizpurua, J.I.; Mendicute, M. FPGA-based degradation and reliability monitor for underground cables. *Sensors* **2019**, *19*, 1995. [\[CrossRef\]](http://dx.doi.org/10.3390/s19091995)
- <span id="page-36-6"></span>13. Mortensen, L.K.; Shaker, H.R. Data-Driven reliability prediction for district heating networks. *Smart Cities* **2024**, *7*, 1706–1722. [\[CrossRef\]](http://dx.doi.org/10.3390/smartcities7040067)
- <span id="page-36-7"></span>14. Moghadam, M.A.; Bagheri, S.; Salemi, A.H.; Tavakoli, M.B. Long-term maintenance planning of medium voltage overhead lines considering the uncertainties and reasons for interruption in a real distribution network. *Reliab. Eng. Syst. Saf.* **2023**, *233*, 109089. [\[CrossRef\]](http://dx.doi.org/10.1016/j.ress.2023.109089)
- <span id="page-36-8"></span>15. Wang, Y.; Chen, P.; Feng, C.; Cao, J. An online monitoring method for low-frequency dielectric loss angle of mining cables. *Sensors* **2023**, *23*, 4273. [\[CrossRef\]](http://dx.doi.org/10.3390/s23094273)
- <span id="page-36-9"></span>16. Shadi, M.R.; Mirshekali, H.; Shaker, H.R. Partial Discharge-Based Cable Vulnerability Ranking with Fuzzy and FAHP Models: Application in a Danish Distribution Network. *Sensors* **2025**, *25*, 3454. [\[CrossRef\]](http://dx.doi.org/10.3390/s25113454)
- <span id="page-36-10"></span>17. Zhou, Z.; Yang, J.; Runciman, M.; Avery, J.; Sun, Z.; Mylonas, G. A tension sensor array for cable-driven surgical robots. *Sensors* **2024**, *24*, 3156. [\[CrossRef\]](http://dx.doi.org/10.3390/s24103156)
- <span id="page-36-11"></span>18. Zhou, C.; Yi, H.; Dong, X. Review of recent research towards power cable life cycle management. *High Volt.* **2017**, *2*, 179–187. [\[CrossRef\]](http://dx.doi.org/10.1049/hve.2017.0037)
- <span id="page-36-12"></span>19. Usman, H.M.; ElShatshat, R.; El-Hag, A.H. Distribution transformer remaining useful life estimation considering electric vehicle penetration. *IEEE Trans. Power Deliv.* **2023**, *38*, 3130–3141. [\[CrossRef\]](http://dx.doi.org/10.1109/TPWRD.2023.3265671)
- <span id="page-36-13"></span>20. Nainar, K.; Ciontea, C.I.; Shahid, K.; Iov, F.; Olsen, R.L.; Schäler, C.; Schwefel, H.P.C. Experimental validation and deployment of observability applications for monitoring of low-voltage distribution grids. *Sensors* **2021**, *21*, 5770. [\[CrossRef\]](http://dx.doi.org/10.3390/s21175770) [\[PubMed\]](http://www.ncbi.nlm.nih.gov/pubmed/34502661)
- <span id="page-36-14"></span>21. Vahldiek, K.; Rüger, B.; Klawonn, F. Leakages in District Heating Networks—Model-Based Data Set Quality Assessment and Localization. *Sensors* **2022**, *22*, 5300. [\[CrossRef\]](http://dx.doi.org/10.3390/s22145300)
- <span id="page-36-15"></span>22. Wang, Y.; Wu, M.; Li, X.; Xie, L.; Chen, Z. A survey on graph neural networks for remaining useful life prediction: Methodologies, evaluation and future trends. *Mech. Syst. Signal Process.* **2025**, *229*, 112449. [\[CrossRef\]](http://dx.doi.org/10.1016/j.ymssp.2025.112449)
- <span id="page-36-16"></span>23. Li, H.; Zhang, Z.; Li, T.; Si, X. A review on physics-informed data-driven remaining useful life prediction: Challenges and opportunities. *Mech. Syst. Signal Process.* **2024**, *209*, 111120. [\[CrossRef\]](http://dx.doi.org/10.1016/j.ymssp.2024.111120)
- <span id="page-36-17"></span>24. Wu, F.; Wu, Q.; Tan, Y.; Xu, X. Remaining useful life prediction based on deep learning: A survey. *Sensors* **2024**, *24*, 3454. [\[CrossRef\]](http://dx.doi.org/10.3390/s24113454)
- <span id="page-36-18"></span>25. Wiegrebe, S.; Kopper, P.; Sonabend, R.; Bischl, B.; Bender, A. Deep learning for survival analysis: A review. *Artif. Intell. Rev.* **2024**, *57*, 65. [\[CrossRef\]](http://dx.doi.org/10.1007/s10462-023-10681-3)
- <span id="page-36-19"></span>26. Jamshidi, A.; Kim, D.; Arif, M. A Survey of Predictive Maintenance Methods: An Analysis of Prognostics via Classification and Regression. *arXiv* **2025**, arXiv:2506.20090. [\[CrossRef\]](http://dx.doi.org/10.48550/arXiv.2506.20090)
- <span id="page-36-20"></span>27. Govindaswamy, T.R.; Ramadoss, R. A Review of Various Fault Diagnosis and RUL Estimation Techniques for Predictive Maintenance in Industrial Rotating Machinery. *J. Vib. Eng. Technol.* **2026**, *14*, 75. [\[CrossRef\]](http://dx.doi.org/10.1007/s42417-025-02322-6)
- <span id="page-36-21"></span>28. Gazali, M.K.; Hasikin, K.; Lai, K.W.; Zamzam, A.H.; Damseh, R. State-of-the-art artificial intelligence approaches for anomaly detection and remaining useful life prediction: A review. *PeerJ Comput. Sci.* **2025**, *11*, e3056.
- <span id="page-36-22"></span>29. Kull, K.; Asad, B.; Khan, M.A.; Naseer, M.U.; Kallaste, A.; Vaimann, T. Faults, Failures, Reliability, and Predictive Maintenance of Grid-Connected Solar Systems: A Comprehensive Review. *Appl. Sci.* **2025**, *15*, 11461. [\[CrossRef\]](http://dx.doi.org/10.3390/app152111461)
- <span id="page-36-23"></span>30. Nuruzzaman, M.; Limon, G.Q.; Chowdhury, A.R.; Khan, M.M. Predictive Maintenance In Power Transformers: A Systematic Review Of AI Furthermore, IOT Applications. *ASRC Procedia Glob. Perspect. Sci. Scholarsh.* **2025**, *1*, 34–47.
- <span id="page-36-24"></span>31. Santiago, R.A.d.F.; Barbosa, N.B.; Mergulhão, H.G.; Carvalho, T.F.d.; Santos, A.A.B.; Medrado, R.C.; Filho, J.B.d.M.; Pinheiro, O.R.; Nascimento, E.G.S. Data-driven models applied to predictive and prescriptive maintenance of wind turbine: A systematic review of approaches based on failure detection, diagnosis, and prognosis. *Energies* **2024**, *17*, 1010. [\[CrossRef\]](http://dx.doi.org/10.3390/en17051010)
- <span id="page-36-25"></span>32. Apata, O.; Munda, J.L.; Migabo, E.M. Artificial Intelligence for Predictive Maintenance and Performance Optimization in Renewable Energy Systems: A Comprehensive Review. *Energies* **2026**, *19*, 536. [\[CrossRef\]](http://dx.doi.org/10.3390/en19020536)

*Sensors* **2026**, *26*, 1915 37 of 40

<span id="page-37-0"></span>33. Li, W.; Chen, J.; Chen, S.; Li, P.; Zhang, B.; Wang, M.; Yang, M.; Wang, J.; Zhou, D.; Yun, J. A Comprehensive Review of Artificial Intelligence-Based Algorithms for Predicting the Remaining Useful Life of Equipment. *Sensors* **2025**, *25*, 4481. [\[CrossRef\]](http://dx.doi.org/10.3390/s25144481)

- <span id="page-37-1"></span>34. Kimutai, E.; Betrie, G.; Brander, R.; Sadiq, R.; Tesfamariam, S. Comparison of statistical models for predicting pipe failures: Illustrative example with the City of Calgary water main failure. *J. Pipeline Syst. Eng. Pract.* **2015**, *6*, 04015005. [\[CrossRef\]](http://dx.doi.org/10.1061/(ASCE)PS.1949-1204.0000196)
- <span id="page-37-2"></span>35. Tian, Z.; Liao, H. Condition based maintenance optimization for multi-component systems using proportional hazards model. *Reliab. Eng. Syst. Saf.* **2011**, *96*, 581–589. [\[CrossRef\]](http://dx.doi.org/10.1016/j.ress.2010.12.023)
- <span id="page-37-3"></span>36. Shen, P.S. Cox regression model with doubly truncated and interval-censored data. *Comput. Stat. Data Anal.* **2025**, *203*, 108090. [\[CrossRef\]](http://dx.doi.org/10.1016/j.csda.2024.108090)
- <span id="page-37-4"></span>37. Wang, L.; Tripathi, Y.M.; Dey, S.; Zhang, C.; Wu, K. Analysis of dependent left-truncated and right-censored competing risks data with partially observed failure causes. *Math. Comput. Simul.* **2022**, *194*, 285–307. [\[CrossRef\]](http://dx.doi.org/10.1016/j.matcom.2021.11.026)
- <span id="page-37-5"></span>38. Zhu, H. Real-time prognostics of engineered systems under time varying external conditions based on the cox phm and varx hybrid approach. *Sensors* **2021**, *21*, 1712. [\[CrossRef\]](http://dx.doi.org/10.3390/s21051712) [\[PubMed\]](http://www.ncbi.nlm.nih.gov/pubmed/33801314)
- <span id="page-37-6"></span>39. Maseda, F.J.; López, I.; Martija, I.; Alkorta, P.; Garrido, A.J.; Garrido, I. Sensors data analysis in supervisory control and data acquisition (SCADA) systems to foresee failures with an undetermined origin. *Sensors* **2021**, *21*, 2762. [\[CrossRef\]](http://dx.doi.org/10.3390/s21082762)
- <span id="page-37-7"></span>40. Sánchez-Herguedas, A.; Mena-Nieto, A.; Rodrigo-Muñoz, F.; Villalba-Díez, J.; Ordieres-Meré, J. Optimisation of maintenance policies based on right-censored failure data using a semi-Markovian approach. *Sensors* **2022**, *22*, 1432. [\[CrossRef\]](http://dx.doi.org/10.3390/s22041432)
- <span id="page-37-8"></span>41. de Santis, R.B.; Gontijo, T.S.; Costa, M.A. A data-driven framework for small hydroelectric plant prognosis using Tsfresh and machine learning survival models. *Sensors* **2022**, *23*, 12. [\[CrossRef\]](http://dx.doi.org/10.3390/s23010012)
- <span id="page-37-9"></span>42. Zhang, K.; Yin, J.; He, Y. Acoustic emission detection and analysis method for health status of lithium ion batteries. *Sensors* **2021**, *21*, 712. [\[CrossRef\]](http://dx.doi.org/10.3390/s21030712)
- <span id="page-37-10"></span>43. Qiu, J.; Wang, H.; Lin, D.; He, B.; Zhao, W.; Xu, W. Nonparametric regression-based failure rate model for electric power equipment using lifecycle data. *IEEE Trans. Smart Grid* **2015**, *6*, 955–964. [\[CrossRef\]](http://dx.doi.org/10.1109/TSG.2015.2388784)
- <span id="page-37-11"></span>44. Kaplan, E.L.; Meier, P. Nonparametric estimation from incomplete observations. *J. Am. Stat. Assoc.* **1958**, *53*, 457–481. [\[CrossRef\]](http://dx.doi.org/10.1080/01621459.1958.10501452)
- <span id="page-37-12"></span>45. González-Domínguez, J.; Sanchez-Barroso, G.; Garcia-Sanz-Calcedo, J.; de Sousa Neves, N. Cox proportional hazards model used for predictive analysis of the energy consumption of healthcare buildings. *Energy Build.* **2022**, *257*, 111784. [\[CrossRef\]](http://dx.doi.org/10.1016/j.enbuild.2021.111784)
- <span id="page-37-13"></span>46. Lee, E.T.; Wang, J. *Statistical Methods for Survival Data Analysis*; John Wiley & Sons: Hoboken, NJ, USA, 2003; Volume 476.
- <span id="page-37-14"></span>47. Marubini, E.; Valsecchi, M.G. *Analysing Survival Data from Clinical Trials and Observational Studies*; John Wiley & Sons: Hoboken, NJ, USA, 2004.
- <span id="page-37-15"></span>48. Klerx, M.H.; Morren, J.; Slootweg, H. Analyzing parameters that affect the reliability of low-voltage cable grids and their applicability in asset management. *IEEE Trans. Power Deliv.* **2019**, *34*, 1432–1441. [\[CrossRef\]](http://dx.doi.org/10.1109/TPWRD.2019.2903928)
- <span id="page-37-16"></span>49. Nelson, W. Theory and applications of hazard plotting for censored failure data. *Technometrics* **1972**, *14*, 945–966. [\[CrossRef\]](http://dx.doi.org/10.1080/00401706.1972.10488991)
- <span id="page-37-17"></span>50. Boudreau, J.F.; Poirier, S. End-of-life assessment of electric power equipment allowing for non-constant hazard rate—Application to circuit breakers. *Int. J. Electr. Power Energy Syst.* **2014**, *62*, 556–561. [\[CrossRef\]](http://dx.doi.org/10.1016/j.ijepes.2014.05.016)
- <span id="page-37-18"></span>51. Devarajan, K.; Ebrahimi, N. A semi-parametric generalization of the Cox proportional hazards regression model: Inference and applications. *Comput. Stat. Data Anal.* **2011**, *55*, 667–676. [\[CrossRef\]](http://dx.doi.org/10.1016/j.csda.2010.06.010) [\[PubMed\]](http://www.ncbi.nlm.nih.gov/pubmed/21076652)
- <span id="page-37-19"></span>52. Qiao, N.; Li, W.; Xiao, F.; Lin, C. Optimal subsampling for the Cox proportional hazards model with massive survival data. *J. Stat. Plan. Inference* **2024**, *231*, 106136. [\[CrossRef\]](http://dx.doi.org/10.1016/j.jspi.2023.106136)
- <span id="page-37-20"></span>53. Xiao, R.; Zayed, T.; Meguid, M.A.; Sushama, L. Improving failure modeling for gas transmission pipelines: A survival analysis and machine learning integrated approach. *Reliab. Eng. Syst. Saf.* **2024**, *241*, 109672. [\[CrossRef\]](http://dx.doi.org/10.1016/j.ress.2023.109672)
- <span id="page-37-21"></span>54. Cui, B.; Ahsan, S.; Zhang, J.; Liang, X. An improved Cox proportional hazards model for reliability analysis of aviation gas turbines considering varying environmental conditions and operational settings. *Reliab. Eng. Syst. Saf.* **2026**, *265*, 111451. [\[CrossRef\]](http://dx.doi.org/10.1016/j.ress.2025.111451)
- <span id="page-37-22"></span>55. Yang, J.; Ye, W.; Wu, J.; Xiao, R.; Xin, M. Health Assessment of Electricity Meters Based on Deep Learning-Improved Survival Analysis Model. *Electronics* **2025**, *14*, 3706. [\[CrossRef\]](http://dx.doi.org/10.3390/electronics14183706)
- <span id="page-37-23"></span>56. Al-Shomrani, A.A.; Shawky, A.; Arif, O.H.; Aslam, M. Log-logistic distribution for survival data analysis using MCMC. *SpringerPlus* **2016**, *5*, 1774. [\[CrossRef\]](http://dx.doi.org/10.1186/s40064-016-3476-7)
- <span id="page-37-24"></span>57. Chen, G.H. An Introduction to Deep Survival Analysis Models for Predicting Time-to-Event Outcomes. *Found. Trends Mach. Learn.* **2024**, *17*, 921–1100. Available online: <https://www.emerald.com/ftmal/article-pdf/17/6/921/11154385/2200000114en.pdf> (accessed on 18 January 2026). [\[CrossRef\]](http://dx.doi.org/10.1561/2200000114)
- <span id="page-37-25"></span>58. Ferrisi, S.; Cappellari, P.; Guido, R.; Umbrello, D.; Ambrogio, G. Application of Two-Parameter Weibull Distribution for Predictive Maintenance: A Case Study. *Procedia Comput. Sci.* **2025**, *253*, 3160–3168. [\[CrossRef\]](http://dx.doi.org/10.1016/j.procs.2025.02.041)
- 59. Hua, X.; Liu, Y.; Xu, Y.; Yan, Y.; Jiang, X. A Preventive Maintenance Strategy for Aviation Cables Based on Lifetime Prediction Under Variable Operating Conditions. *IEEE Trans. Instrum. Meas.* **2025**, *74*, 3560111. [\[CrossRef\]](http://dx.doi.org/10.1109/tim.2025.3614789)

*Sensors* **2026**, *26*, 1915 38 of 40

<span id="page-38-0"></span>60. Nazarychev, A.; Iliev, I.; Manukian, D.; Beloev, H.; Suslov, K.; Beloev, I. Review of Operating Conditions, Diagnostic Methods, and Technical Condition Assessment to Improve Reliability and Develop a Maintenance Strategy for Electrical Equipment. *Energies* **2025**, *18*, 5832. [\[CrossRef\]](http://dx.doi.org/10.3390/en18215832)

- <span id="page-38-1"></span>61. Mastor, A.B.S.; Alghamdi, A.S.; Ngesa, O.; Mung'atu, J.; Chesneau, C.; Afify, A.Z. The extended exponential-Weibull accelerated failure time model with application to Sudan COVID-19 Data. *Mathematics* **2023**, *11*, 460. [\[CrossRef\]](http://dx.doi.org/10.3390/math11020460)
- <span id="page-38-2"></span>62. Muse, A.H.; Chesneau, C.; Ngesa, O.; Mwalili, S. Flexible parametric accelerated hazard model: Simulation and application to censored lifetime data with crossing survival curves. *Math. Comput. Appl.* **2022**, *27*, 104. [\[CrossRef\]](http://dx.doi.org/10.3390/mca27060104)
- <span id="page-38-3"></span>63. Abbas, S.; Farooq, M.; Darwish, J.A.; Shahbaz, S.H.; Shahbaz, M.Q. Truncated Weibull—Exponential distribution: Methods and applications. *Sci. Rep.* **2023**, *13*, 20849. [\[CrossRef\]](http://dx.doi.org/10.1038/s41598-023-48288-x) [\[PubMed\]](http://www.ncbi.nlm.nih.gov/pubmed/38012379)
- <span id="page-38-4"></span>64. Bantan, R.A.; Jamal, F.; Chesneau, C.; Elgarhy, M. Theory and applications of the unit gamma/Gompertz distribution. *Mathematics* **2021**, *9*, 1850. [\[CrossRef\]](http://dx.doi.org/10.3390/math9161850)
- <span id="page-38-5"></span>65. Baharith, L.A. New generalized weibull inverse gompertz distribution: Properties and applications. *Symmetry* **2024**, *16*, 197. [\[CrossRef\]](http://dx.doi.org/10.3390/sym16020197)
- <span id="page-38-6"></span>66. Moat, G.; Coleman, S. Survival analysis and predictive maintenance models for non-sensored assets in facilities management. In *Proceedings of the 2021 IEEE International Conference on Big Data (Big Data)*; IEEE: New York, NY, USA, 2021; pp. 4026–4034.
- <span id="page-38-7"></span>67. Liao, H. Accelerated testing and smart maintenance: History and future. *IEEE Trans. Reliab.* **2023**, *73*, 33–37. [\[CrossRef\]](http://dx.doi.org/10.1109/TR.2023.3330739)
- 68. Guo, J.; Fu, H. Reliability Assessment for Small-Sample Accelerated Life Tests with Normal Distribution. *Machines* **2025**, *13*, 850. [\[CrossRef\]](http://dx.doi.org/10.3390/machines13090850)
- <span id="page-38-8"></span>69. Kim, T.W.; Chang, Y.; Kim, D.W.; Kim, M.K. Preventive maintenance and forced outages in power plants in Korea. *Energies* **2020**, *13*, 3571. [\[CrossRef\]](http://dx.doi.org/10.3390/en13143571)
- <span id="page-38-9"></span>70. Nie, Y.; Chen, D.; Zhang, Z.; Xu, X.; Zheng, S.; Wu, Z. Reliability Assessment of Hybrid Cable Laying Configurations in Urban Dense Cable Channels Based on Modified Weibull Distribution. *Appl. Sci.* **2025**, *15*, 9124. [\[CrossRef\]](http://dx.doi.org/10.3390/app15169124)
- <span id="page-38-10"></span>71. Wang, P.; Li, Y.; Reddy, C.K. Machine learning for survival analysis: A survey. *ACM Comput. Surv. (CSUR)* **2019**, *51*, 1–36.
- <span id="page-38-11"></span>72. Katzman, J.L.; Shaham, U.; Cloninger, A.; Bates, J.; Jiang, T.; Kluger, Y. DeepSurv: Personalized treatment recommender system using a Cox proportional hazards deep neural network. *BMC Med. Res. Methodol.* **2018**, *18*, 24.
- <span id="page-38-12"></span>73. Wang, Y.; Wang, D.; Ye, X.; Wang, Y.; Yin, Y.; Jin, Y. A tree ensemble-based two-stage model for advanced-stage colorectal cancer survival prediction. *Inf. Sci.* **2019**, *474*, 106–124.
- <span id="page-38-13"></span>74. Zheng, H.; Shioya, R. Prediction of Abnormal Progression in Oil-Immersed Transformers Using Dissolved Gas Analysis and Random Survival Forest. *IEEJ Trans. Electr. Electron. Eng.* **2025**, *21*, 386–392.
- <span id="page-38-14"></span>75. Shadi, M.R.; Mortensen, L.K.; Mirshekali, H.; Shaker, H.R. Proactive Cable Replacement Planning Using Neural Weibull Proportional Hazard Modeling and Bayesian Nested Monte Carlo Simulation Under Data Deficiencies. *IEEE Access* **2025**, *13*, 167823–167836. [\[CrossRef\]](http://dx.doi.org/10.1109/ACCESS.2025.3613832)
- <span id="page-38-15"></span>76. Yaqin, A.M.A.; Fadillah, F.; Wantira, A.D.; Leksono, V.A.; Efranto, R.Y.; Bahar, N.Q. Survival Analysis Models for Mortality Risk Prediction During the Pandemic: A Comparative Study Using Cox Proportional Hazards, Random Survival Forests, and DeepSurv. In *Proceedings of the 2025 12th International Conference on Advanced Informatics: Concept, Theory and Application (ICAICTA)*; IEEE: New York, NY, USA, 2025; pp. 1–6.
- <span id="page-38-16"></span>77. Lee, C.; Yoon, J.; Van Der Schaar, M. Dynamic-deephit: A deep learning approach for dynamic survival analysis with competing risks based on longitudinal data. *IEEE Trans. Biomed. Eng.* **2019**, *67*, 122–133.
- <span id="page-38-17"></span>78. Nagpal, C.; Li, X.; Dubrawski, A. Deep survival machines: Fully parametric survival regression and representation learning for censored data with competing risks. *IEEE J. Biomed. Health Inform.* **2021**, *25*, 3163–3175.
- <span id="page-38-18"></span>79. Park, S.Y.; Park, J.E.; Kim, H.; Park, S.H. Review of statistical methods for evaluating the performance of survival or other time-to-event prediction models (from conventional to deep learning approaches). *Korean J. Radiol.* **2021**, *22*, 1697.
- <span id="page-38-19"></span>80. Hartman, N.; Kim, S.; He, K.; Kalbfleisch, J.D. Concordance indices with left-truncated and right-censored data. *Biometrics* **2023**, *79*, 1624–1634.
- <span id="page-38-20"></span>81. Simonsen, M.R.; Waagepetersen, R.P. A-calibration: Assessment of prediction models for survival data under censoring. *BMC Med. Res. Methodol.* **2025**, *25*, 236. [\[CrossRef\]](http://dx.doi.org/10.1186/s12874-025-02671-6)
- <span id="page-38-21"></span>82. Beyene, K.M.; Chen, D.G. Time-dependent receiver operating characteristic curve estimator for correlated right-censored time-to-event data. *Stat. Methods Med. Res.* **2024**, *33*, 162–181. [\[CrossRef\]](http://dx.doi.org/10.1177/09622802231220496) [\[PubMed\]](http://www.ncbi.nlm.nih.gov/pubmed/38130110)
- <span id="page-38-22"></span>83. Van Geloven, N.; Giardiello, D.; Bonneville, E.F.; Teece, L.; Ramspek, C.L.; Van Smeden, M.; Snell, K.I.; Van Calster, B.; Pohar-Perme, M.; Riley, R.D. Validation of prediction models in the presence of competing risks: A guide through modern methods. *BMJ* **2022**, *377*, e069249. [\[CrossRef\]](http://dx.doi.org/10.1136/bmj-2021-069249) [\[PubMed\]](http://www.ncbi.nlm.nih.gov/pubmed/35609902)
- <span id="page-38-23"></span>84. Zhou, H.; Wang, H.; Wang, S.; Zou, Y. SurvMetrics: An R package for Predictive Evaluation Metrics in Survival Analysis. *R J.* **2023**, *14*, 252–263. [\[CrossRef\]](http://dx.doi.org/10.32614/RJ-2023-009)
- <span id="page-38-24"></span>85. Qin, J.; Piao, J.; Ning, J.; Shen, Y. Conformal predictive intervals in survival analysis: A resampling approach. *Biometrics* **2025**, *81*, ujaf063. [\[CrossRef\]](http://dx.doi.org/10.1093/biomtc/ujaf063)

*Sensors* **2026**, *26*, 1915 39 of 40

<span id="page-39-0"></span>86. Mogensen, U.B.; Ishwaran, H.; Gerds, T.A. Evaluating random forests for survival analysis using prediction error curves. *J. Stat. Softw.* **2012**, *50*, 1–23. [\[CrossRef\]](http://dx.doi.org/10.18637/jss.v050.i11)

- <span id="page-39-1"></span>87. Kvamme, H.; Borgan, Ø. The Brier score under administrative censoring: Problems and a solution. *J. Mach. Learn. Res.* **2023**, *24*, 1–26.
- <span id="page-39-2"></span>88. Fahimi, N.; Sezavar, H.R. Biologically Inspired Survival Analysis Framework for Failure Monitoring of Composite Insulators Using Leakage Current. *Results Eng.* **2025**, *29*, 108742. [\[CrossRef\]](http://dx.doi.org/10.1016/j.rineng.2025.108742)
- <span id="page-39-3"></span>89. Tang, Z.; Zhou, C.; Jiang, W.; Zhou, W.; Jing, X.; Yu, J.; Alkali, B.; Sheng, B. Analysis of significant factors on cable failure using the cox proportional hazard model. *IEEE Trans. Power Deliv.* **2013**, *29*, 951–957. [\[CrossRef\]](http://dx.doi.org/10.1109/TPWRD.2013.2287025)
- <span id="page-39-4"></span>90. Verweij, R.; van Houwelingen, D.; Prein, A. Where to replace assets? Spatial analysis on differential ageing of low-voltage PILC cables. *CIRED 24* **2017**, *2017*, 2585–2589.
- <span id="page-39-5"></span>91. Tang, Z.; Zhou, W.; Zhao, J.; Wang, D.; Zhang, L.; Liu, H.; Yang, Y.; Zhou, C. Comparison of the Weibull and the crow-AMSAA model in prediction of early cable joint failures. *IEEE Trans. Power Deliv.* **2015**, *30*, 2410–2418. [\[CrossRef\]](http://dx.doi.org/10.1109/tpwrd.2015.2404926)
- <span id="page-39-6"></span>92. Atiq, S.; Moeen, M.; Siddique, A.; Aslam, W.; Alsufiani, K.D. Machine Learning-Based Health Index Prediction for XLPE Power Cables: Enhancing Reliability and Cost-Effective Maintenance. *Energy Sci. Eng.* **2025**, *13*, 5482–5494.
- <span id="page-39-7"></span>93. Moradkhani, A.; Haghifam, M.R.; Mohammadzadeh, M. Bayesian estimation of overhead lines failure rate in electrical distribution systems. *Int. J. Electr. Power Energy Syst.* **2014**, *56*, 220–227. [\[CrossRef\]](http://dx.doi.org/10.1016/j.ijepes.2013.11.022)
- <span id="page-39-8"></span>94. Martin, D.; Marks, J.; Saha, T.K.; Krause, O.; Mahmoudi, N. Investigation into modeling Australian power transformer failure and retirement statistics. *IEEE Trans. Power Deliv.* **2018**, *33*, 2011–2019. [\[CrossRef\]](http://dx.doi.org/10.1109/tpwrd.2018.2814588)
- <span id="page-39-9"></span>95. Zhou, D.; Wang, Z.; Jarman, P.; Li, C. Data requisites for transformer statistical lifetime modelling—Part II: Combination of random and aging-related failures. *IEEE Trans. Power Deliv.* **2013**, *29*, 154–160. [\[CrossRef\]](http://dx.doi.org/10.1109/TPWRD.2013.2270116)
- <span id="page-39-10"></span>96. Park, C.; Cho, C.; Kim, D.I. Hazard analysis of weather conditions on distribution transformer failures via cox proportional hazard model. *IEEE Access* **2025**, *13*, 17414–17425. [\[CrossRef\]](http://dx.doi.org/10.1109/ACCESS.2025.3532507)
- <span id="page-39-11"></span>97. Aizpurua, J.I.; Ramirez, I.; Lasa, I.; del Rio, L.; Ortiz, A.; Stewart, B.G. Hybrid transformer prognostics framework for enhanced probabilistic predictions in renewable energy applications. *IEEE Trans. Power Deliv.* **2022**, *38*, 599–609. [\[CrossRef\]](http://dx.doi.org/10.1109/tpwrd.2022.3203873)
- <span id="page-39-12"></span>98. Jürgensen, J.H.; Brodersson, A.L.; Nordström, L.; Hilber, P. Impact assessment of remote control and preventive maintenance on the failure rate of a disconnector population. *IEEE Trans. Power Deliv.* **2017**, *33*, 1501–1509. [\[CrossRef\]](http://dx.doi.org/10.1109/tpwrd.2017.2710482)
- <span id="page-39-13"></span>99. Tee, S.; Liu, Q.; Wang, Z.; Hafid, F.; Tournet, P. Failure investigation and asset management of combined measuring instrument transformers. *High Volt.* **2021**, *6*, 61–70.
- <span id="page-39-14"></span>100. Cichecki, P.; Jongen, R.A.; Gulski, E.; Smit, J.J.; Quak, B.; Petzold, F.; de Vries, F. Statistical approach in power cables diagnostic data analysis. *IEEE Trans. Dielectr. Electr. Insul.* **2008**, *15*, 1559–1569. [\[CrossRef\]](http://dx.doi.org/10.1109/tdei.2008.4712658)
- <span id="page-39-15"></span>101. Weidlich, I.; Schuchardt, G.K. New approach for asset management in district heating (DH) networks. *Energy Procedia* **2017**, *113*, 22–27. [\[CrossRef\]](http://dx.doi.org/10.1016/j.egypro.2017.04.007)
- <span id="page-39-16"></span>102. Valinˇcius, M.; Žutautaite, I.; Dundulis, G.; Rimkeviˇcius, S.; Janulionis, R.; Bakas, R. Integrated assessment of failure probability of ˙ the district heating network. *Reliab. Eng. Syst. Saf.* **2015**, *133*, 314–322. [\[CrossRef\]](http://dx.doi.org/10.1016/j.ress.2014.09.022)
- <span id="page-39-17"></span>103. Shan, X.; Wang, P.; Lu, W. The reliability and availability evaluation of repairable district heating networks under changeable external conditions. *Appl. Energy* **2017**, *203*, 686–695. [\[CrossRef\]](http://dx.doi.org/10.1016/j.apenergy.2017.06.081)
- <span id="page-39-18"></span>104. Wu, X.; Chen, Q.; Hu, M.; Gan, L.; Teng, L. RSF-based model for predicting pump failure trends in tunnels. *Adv. Mech. Eng.* **2023**, *15*, 16878132231215184. [\[CrossRef\]](http://dx.doi.org/10.1177/16878132231215184)
- <span id="page-39-19"></span>105. Shadi, M.R.; Mirshekali, H.; Tahavori, M.; Shaker, H.R. Data-Driven Asset Management in District Heating: Barriers, Insights, and Future Pathways. In Proceedings of the 3rd International Conference on Machine Learning and Autonomous Systems, Bangkok, Thailand, 11–13 March 2026.
- <span id="page-39-20"></span>106. Roelofs, C.M.A.; Bastidas Guevara, E.; Hugo, T.; Faulstich, S.; Cadenbach, A. *PreDist Dataset—Operational Data of District Heating Substations Labelled with Faults and Maintenance Information*; Dataset; Zenodo: Geneva, Switzerland, 2025. [\[CrossRef\]](http://dx.doi.org/10.5281/zenodo.17522255)
- <span id="page-39-21"></span>107. Gück, C.; Roelofs, C. Wind Turbine SCADA Data For Early Fault Detection. Dataset. 2024. Available online: [https://zenodo.org/](https://zenodo.org/records/10958775) [records/10958775](https://zenodo.org/records/10958775) (accessed on 18 January 2026). [\[CrossRef\]](http://dx.doi.org/10.5281/zenodo.14006163)
- <span id="page-39-22"></span>108. Gück, C.; Roelofs, C.M.A.; Faulstich, S. CARE to Compare: A Real-World Benchmark Dataset for Early Fault Detection in Wind Turbine Data. *Data* **2024**, *9*, 138. [\[CrossRef\]](http://dx.doi.org/10.3390/data9120138)
- <span id="page-39-23"></span>109. VSB Power Line Fault Detection Organizers. *VSB Power Line Fault Detection*; Kaggle competition dataset; Kaggle: San Francisco, CA, USA, 2019.
- <span id="page-39-24"></span>110. Chelmiah, E.T.; Madigan, C.D.; Kavanagh, D.F. *Partial Discharge—Localisation (PD-Loc) Dataset*; IEEE DataPort dataset; IEEE DataPort: Piscataway, NJ, USA, 2024. [\[CrossRef\]](http://dx.doi.org/10.21227/yy7g-2p79)
- <span id="page-39-25"></span>111. Sami, S.M.; Bhuiyan, M.I.H. Power Transformer Fault Diagnosis with Intrinsic Time-scale Decomposition and XGBoost Classifier. *arXiv* **2021**, arXiv:2110.11467. [\[CrossRef\]](http://dx.doi.org/10.48550/arXiv.2110.11467)
- <span id="page-39-26"></span>112. Li, E. *Dissolved Gas Data in Transformer Oil—Fault Diagnosis of Power Transformers with Membership Degree*; IEEE DataPort dataset; IEEE DataPort: Piscataway, NJ, USA, 2019. [\[CrossRef\]](http://dx.doi.org/10.21227/h8g0-8z59)

*Sensors* **2026**, *26*, 1915 40 of 40

<span id="page-40-0"></span>113. Sokolovi´c, Ž. *Transmission Line Faults*; Mendeley Data dataset; Mendeley Data: Amsterdam, The Netherlands, 2024. [\[CrossRef\]](http://dx.doi.org/10.17632/3dvjgvv5bz.1)

- <span id="page-40-1"></span>114. Liu, S.; Wang, Y.; Tian, F. Prognosis of underground cable via online data-driven method with field data. *IEEE Trans. Ind. Electron.* **2015**, *62*, 7786–7794. [\[CrossRef\]](http://dx.doi.org/10.1109/tie.2015.2458300)
- <span id="page-40-2"></span>115. Steennis, F.; Wagenaars, P.; van der Wielen, P.; Wouters, P.; Li, Y.; Broersma, T.; Harmsen, D.; Bleeker, P. Guarding MV cables on-line: With travelling wave based temperature monitoring, fault location, PD location and PD related remaining life aspects. *IEEE Trans. Dielectr. Electr. Insul.* **2016**, *23*, 1562–1569. [\[CrossRef\]](http://dx.doi.org/10.1109/tdei.2016.005566)
- <span id="page-40-3"></span>116. Tang, Y.; Li, S.; Lei, J.; Tang, M.; Wang, Y.; Tai, B.; Yang, C.; Chen, T.; Lu, J.; Wen, Z. Reliability Evaluation of 10kV XLPE Cable Based on Fault Correlation Bayesian Network and Weibull Distribution Model. In *Proceedings of the 2023 IEEE 4th International Conference on Electrical Materials and Power Equipment (ICEMPE)*; IEEE: New York, NY, USA, 2023; pp. 1–4.
- <span id="page-40-4"></span>117. Shadi, M.R.; Mirshekali, H.; Shaker, H.R. Explainable artificial intelligence for energy systems maintenance: A review on concepts, current techniques, challenges, and prospects. *Renew. Sustain. Energy Rev.* **2025**, *216*, 115668. [\[CrossRef\]](http://dx.doi.org/10.1016/j.rser.2025.115668)
- <span id="page-40-5"></span>118. Gill, Y. Development of an electrical cable replacement simulation model to aid with the management of aging underground electric cables. *IEEE Electr. Insul. Mag.* **2011**, *27*, 31–37. [\[CrossRef\]](http://dx.doi.org/10.1109/MEI.2011.5699445)
- <span id="page-40-6"></span>119. Dawood, T.; Elwakil, E.; Novoa, H.M.; Gárate Delgado, J.F. Water pipe failure prediction and risk models: State-of-the-art review. *Can. J. Civ. Eng.* **2020**, *47*, 1117–1127.
- <span id="page-40-7"></span>120. Barton, N.A.; Hallett, S.; Jude, S.R.; Tran, T.H. An evolution of statistical pipe failure models for drinking water networks: A targeted review. *Water Supply* **2022**, *22*, 3784–3813. [\[CrossRef\]](http://dx.doi.org/10.2166/ws.2022.019)

**Disclaimer/Publisher's Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.
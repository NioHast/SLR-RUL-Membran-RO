ELSEVIER

Contents lists available at ScienceDirect

## Desalination and Water Treatment

journal homepage: www.sciencedirect.com/journal/desalination-and-water-treatment/

![](_page_0_Picture_5.jpeg)

![](_page_0_Picture_6.jpeg)

# An insight into real-time monitoring and predictive modelling of ultrafiltration pretreatment for flow rate and fouling mitigation in seawater desalination

Kamil Kayode Katibi <sup>a,b,c,\*</sup>, Azimov Abdugani Mutalovich <sup>d,\*\*</sup>, Nazmi Mat Nawi <sup>e</sup>, Gani M. Iztleuov <sup>f</sup>, Marat I. Sataev <sup>d</sup>, Muhammad Adib Mohd Nasir <sup>e</sup>

- <sup>a</sup> Department of Physics, Faculty of Science, Universiti Putra Malaysia, Serdang, Selangor 43400, Malaysia
- <sup>b</sup> Institute of Nanoscience and Nanotechnology (ION2), Universiti Putra Malaysia, Serdang, Selangor 43400, Malaysia
- <sup>c</sup> Department of Food and Agricultural Engineering, Faculty of Engineering and Technology, Kwara State University, Malete, Ilorin 23431, Nigeria
- d Research Laboratory Innovative Water Treatment Systems, M. Auezov South Kazakhstan University, Taukehan Street 5, Shymkent 16000, Kazakhstan
- e Department of Biological and Agricultural Engineering, Faculty of Engineering, Universiti Putra Malaysia, Serdang, Selangor 43400, Malaysia
- f Department of Ecology, M. Auezov South Kazakhstan University, Taukehan Street 5, Shymkent 16000, Kazakhstan

#### HIGHLIGHTS

- Effects of time, temperature, pressure, pH, and ORP on ultrafiltration performance were investigated.
- Ensemble learning and tree regression predicted flow rate with  $R^2=0.99$  and RMSE = 3.08 L/min.
- A 426-day seawater UF dataset enabled robust long-term model training and validation.
- Real-time sensors improved fouling detection, backwash timing, and energy efficiency.
- The ML framework allowed adaptive control of TMP and flow rate, scalable to other membrane systems.

#### GRAPHICAL ABSTRACT

![](_page_0_Picture_22.jpeg)

#### ARTICLE INFO

Keywords:
Membrane fouling
Machine learning prediction
Ultrafiltration (UF)

#### ABSTRACT

The growing demand for freshwater, driven by population growth, industrialization, and climate change, has increased global reliance on seawater desalination. While reverse osmosis (RO) remains the primary technology for salt removal, ultrafiltration (UF) plays a critical role as a pretreatment stage by reducing suspended solids, colloids, and microorganisms contributing to RO membrane fouling. This study focuses exclusively on the

Abbreviation: UF, Ultrafiltration; RO, Reverse Osmosis; ML, Machine Learning; TR, Tree Regression; ENS, Ensemble Learning; NN, Neural Networks; GPR, Gaussian Process Regression; SVM, Support Vector Machine; KAR, Kernel-Adaptive Regression; LR, Linear Regression; SLR, Simple Linear Regression; RMSE, Root Mean Squared Error; MSE, Mean Squared Error; MAE, Mean Absolute Error; R<sup>2</sup>, Coefficient of Determination; TMP, Transmembrane Pressure; ORP, Oxidation–Reduction Potential; PES, Polyethersulfone; HP, High-Pressure Pump; LP, Low-Pressure Pump; CF, Cartridge Filter; CD, Chemical Dosing Pump.

E-mail addresses: kamilkyode@upm.edu.my (K.K. Katibi), Azimov-78@mail.ru (A.A. Mutalovich).

#### https://doi.org/10.1016/j.dwt.2025.101386

Received 19 May 2025; Received in revised form 12 August 2025; Accepted 12 August 2025 Available online 13 August 2025

<sup>\*</sup> Corresponding author at: Department of Physics, Faculty of Science, Universiti Putra Malaysia, Serdang, Selangor 43400, Malaysia.

<sup>\*\*</sup> Corresponding author.

Backwash efficiency Seawater desalination

predictive modelling and real-time optimization of a UF system operating as a pretreatment component in a seawater desalination plant. Using 426 days of operational data, four Machine learning (ML) models: Tree Regression (TR), Ensemble Learning (ENS), Neural Networks (NN), and Gaussian Process Regression (GPR) were trained to predict UF flow rates and membrane resistance in real time. ENS achieved the best performance with an R² of 0.99 and Root Mean Square Error (RMSE) of 3.08 L/min, closely followed by TR (R² = 0.99, RMSE = 3.27 L/min). NN and GPR yielded R² of 0.98 (RMSE = 4.69 L/min) and R² of 0.97 (RMSE = 5.98 L/min), respectively. Adaptive backwash control guided by these predictions reduced average TMP excursions by 18 % and decreased backwash frequency from one event every 6 h to one every 8 h, improving operational stability and cutting maintenance costs by 12 %. This framework presents a scalable, intelligent approach to fouling mitigation in seawater desalination pretreatment.

#### **1. Introduction**

The global water crisis remains a demanding environmental and public concern, as freshwater resources become increasingly inadequate as a result of climate change, population growth, and industrialization [\[1\].](#page-9-0) In response to this escalating pressure, seawater desalination has emerged as a critical panacea, particularly in water-stressed and densely populated countries. Reverse osmosis (RO) technology remains central to most seawater desalination systems because of its excellent salt rejection efficiency and operational scalability [\[2,3\]](#page-9-0). However, the long-term performance and energy efficiency of RO systems are susceptible to the quality of the feedwater and the effectiveness of upstream conditioning [\[4,5\]](#page-9-0). Addressing membrane fouling remains fundamental to sustaining long-term process efficiency in desalination systems, particularly in the context of reverse osmosis operations [\[6\].](#page-9-0)

Membrane fouling is one of the principal drawbacks in seawater desalination, especially within RO systems, where the accumulation of particulates, colloids, organic matter, and microorganisms on membrane surfaces increases transmembrane pressure and compromises flow performance [\[5,7\]](#page-9-0). Thus, efficient pretreatment is highly indispensable to mitigate fouling risks and sustain system reliability. In this context, UF has become a standard pretreatment strategy on account of its capacity to reduce suspended solids and biological content upstream of RO membranes [\[8,9\]](#page-9-0). By enhancing the quality of the RO feedwater, UF systems contribute significantly to enhanced operational stability, reduced chemical cleaning frequency, and extended membrane service life [\[10,11\]](#page-9-0).

Similarly, UF has been increasingly used as a pre-treatment for RO feedwater, as it effectively removes suspended solids, colloidal particles, and microorganisms, thereby reducing the fouling potential of the RO feed [\[9,12\].](#page-9-0) Undesirably, UF systems are also prone to fouling, compromising membrane permeability over time and requiring frequent cleaning cycles, such as backwashing or chemical cleaning [\[11,13\]](#page-9-0). Optimizing UF backwash cycles is critical for reducing membrane fouling and sustaining long-term operational stability within UF pretreatment systems.

Membrane fouling remains a critical operational challenge in UF systems, as it directly compromises hydraulic performance, energy requirement, and membrane lifespan [14–[16\].](#page-9-0) Recent reports have focused on elucidating the mechanisms of fouling in UF membranes, particularly the roles of organic, biological, and particulate matter, which are primary contributors to performance degradation [\[17](#page-9-0)–19]. A range of mitigation strategies such as physical cleaning, chemical cleaning, and process optimization have been proposed to minimize fouling and extend operational uptime in UF applications [\[20](#page-9-0)–23]. Given the widespread use of UF systems as a pretreatment stage in seawater desalination, especially upstream of RO, understanding and predicting fouling behaviour in UF membranes has become increasingly indispensable for enhancing overall system efficacy and decreasing maintenance costs [\[24,25\]](#page-9-0). Given the variability of fouling phenomena and operational complexity in UF systems, data-driven approaches such as ML have emerged as powerful tools for predictive modelling and process optimization [\[17\].](#page-9-0)

In recent years, ML applications in membrane filtration have gained

momentum, particularly in optimizing UF systems used for desalination pretreatment [\[26](#page-9-0)–28]. ML algorithms are increasingly employed to model the non-linear and dynamic relationships between operational parameters and fouling behaviour, presenting predictive insights that support real-time decision-making and adaptive control. For instance, Deng et al. [\[29\]](#page-9-0) developed a NN-based model that integrated real-time sensor data to predict membrane fouling rates in seawater desalination pretreatment, enabling more efficient backwash scheduling and energy savings. Similarly, Shim et al. [\[30\]](#page-9-0) implemented a deep learning framework to monitor and forecast UF membrane resistance under fluctuating conditions, achieving substantial improvements in flow regulation and transmembrane pressure control. While these models have demonstrated strong predictive performance, many rely on fixed parameter ranges and lack the responsiveness required for continuous, system-wide optimization in dynamically changing environments. While recent studies have demonstrated the promise of ML in modelling membrane fouling [\[31](#page-9-0)–33], several existing approaches fall short in terms of real-time adaptability and operational integration.

Although existing ML approaches have demonstrated improved prediction of fouling behavior [\[34,35\]](#page-10-0), most are configured to operate at pre-set intervals and lack full integration with real-time control systems, limiting their responsiveness to dynamic changes in UF operating conditions. Despite improvements in fouling prediction and model accuracy, a critical limitation persists: most ML models operate reactively or rely on fixed control intervals, rather than adapting dynamically to real-time fluctuations in feedwater quality and operating conditions [\[4\]](#page-9-0). Although real-time sensors for monitoring parameters such as TMP, membrane resistance, and ORP have significantly enhanced detection capabilities [\[36,37\],](#page-10-0) existing ML implementations often lack seamless integration with automated control systems. As a result, operational adjustments, such as altering backwash intervals or adjusting flow rates are frequently delayed or require manual intervention, limiting the practical impact of ML-driven optimization.

In this study, a UF system operating under real-world desalination pretreatment conditions was used to demonstrate the potential of adaptive ML frameworks. By dynamically adjusting operational parameters such as flow rate and backwash frequency in response to realtime sensor data, the system achieved improved fouling resistance, reduced downtime, and enhanced operational resilience over an extended period. This approach addresses a key shortcoming of many existing ML applications in UF: the lack of real-time adaptability. While previous models have shown success in fouling prediction and process optimization, they typically function within fixed intervals and are not designed to respond to dynamic shifts in feedwater quality or membrane performance. To overcome these drawbacks, this study proposes a sensor-integrated, data-driven control strategy that enables continuous adaptation to changing operational conditions, marking a step forward in the development of intelligent, self-regulating UF systems.

Despite considerable advances in ultrafiltration (UF) for seawater pretreatment, traditional operation relies on fixed backwash schedules and periodic offline inspections, which cannot forestall rapid flux declines and membrane fouling under fluctuating feedwater conditions. Recent studies have explored machine-learning (ML) techniques for predictive fouling control, yet most focus on post-mortem data analysis

rather than real-time operational feedback. Here, we bridge this gap by developing and validating four ML models Tree Regression, Ensemble Learning, Neural Networks, and Gaussian Process Regression trained on 426 days of continuous UF performance data. Our approach integrates real-time flow rate and transmembrane pressure (TMP) measurements to predict membrane resistance and trigger adaptive backwash events, thereby enhancing fouling mitigation, extending membrane life, and reducing maintenance demands in seawater desalination pretreatment.

#### **2. Methodology**

#### *2.1. Experimental system setup*

This study investigates the performance and fouling behaviour of a UF system employed as a pretreatment stage in a seawater desalination plant, with a focus on predictive modelling and real-time operational optimization. The experimental setup was implemented at the Tanjung Bin Power Plant in Johor, Malaysia, operated by Malakoff Corporation Berhad. While the facility includes a RO unit downstream, this research focused exclusively on the UF subsystem, which plays a critical role in reducing suspended solids, colloidal particles, and microbial contaminants in the feedwater, thereby mitigating fouling and extending the longevity of RO membranes.

The UF system consisted of three multi-channel hollow-fiber membrane modules (Dizzer 5000 +, Inge, Gr¨ afenberg, Germany), each with a membrane area of 50 m². These modules are configured in parallel and operate in dead-end filtration mode using hydrophilic polyethersulfone (PES) membranes with an inside-out flow configuration and a nominal pore size of nearly 0.02 μm. The membranes are designed for highperformance removal of colloids, organic matter, suspended solids, and microorganisms from seawater, contributing significantly to fouling mitigation in downstream desalination routes. At the start of the 426 day monitoring period, the modules had been in service for approximately two years, providing a realistic reflection of age-related fouling and operational performance in field-scale desalination pretreatment systems.

The system alternated automatically between filtration and backwash phases, with RO concentrate (retentate) reused as the backwash fluid to enhance water-use efficiency and exclude the demand for intermediate storage. Real-time operational monitoring was carried out across both phases. During filtration, key parameters including flow rate, TMP, pH, temperature, and ORP- were continuously evaluated at both the UF feed and permeate outlets. During backwash, flow rate, TMP, and ORP were monitored in the backwash circuit to assess cleaning effectiveness together with membrane recovery. The system operated within an average TMP range of 0.5–1.5 bar, with backwash initiated when TMP exceeded 1.4 bar or when the modelled membrane resistance deviated significantly from baseline performance. Fig. 1 presents a schematic of the UF system configuration, including the integrated use of RO retentate for backwashing.

#### *2.2. Operational parameters*

The UF system alternated between filtration and backwash phases, each with continuous real-time monitoring. Operational parameters, comprising flow rate, TMP, pH, temperature, and ORP, were recorded throughout filtration and backwash cycles. During the filtration phase, these parameters were monitored at the UF feed and permeate outlets to capture performance trends, membrane resistance, and the impact of feedwater quality. On the other hand, during the backwash phase, monitoring focused on TMP, flow rate, and ORP within the backwash loop, which utilized RO concentrate as the backwash fluid. This allowed for the evaluation of membrane cleaning effectiveness and dynamic system recovery. TMP, pH, and ORP were each sampled at 1.0 Hz to capture rapid transitions between filtration and backwash phases and to enable direct correlation of these parameters with fouling and cleaning

![](_page_2_Picture_10.jpeg)

**Fig. 1.** Schematic representation of the integrated UF-RO system. The UF skid consists of a rotating disk microfilter (sediment filter) and three hollow-fiber (inside-out) UF modules coupled in parallel. The filtrate stream from the UF modules was supplied directly to the RO system. The retentate stream from the RO system (dashed line) is utilized directly for UF backwash. (HP: high-pressure pump, LP: low-pressure pump, CF: cartridge filter, CD: chemical dosing pump).

efficiency. This dual-phase monitoring enabled the development of ML models capable of distinguishing and predicting flow rate behaviours across both operational modes.

## *2.3. Data collection and machine learning model development*

In this study, a wide-ranging dataset covering 426 days of UF operations under varying water quality conditions was collected to train and assess the ML models. The key operational parameters monitored include TMP, flow rate, pH, temperature, and ORP. TMP values were continuously observed, with a critical operating range between 0.5 bar and 1.5 bar, while the flow rate was maintained between 5 L/min and 15 L/min, subject to membrane fouling conditions. pH levels were regulated within the range of 7.5–8.2 to minimize scaling and enhance fouling resistance. The system also recorded temperature fluctuations ranging from 11.2 ◦C to 25.6 ◦C because of seasonal variations in feedwater conditions. Also, ORP was measured to evaluate membrane fouling risks, with typical values ranging from 200 to 450 mV under normal operational conditions. These parameters were carefully monitored to optimize the ML models' predictive performance with fouling resistance and backwash efficiency. The overall workflow for data preprocessing, model development, and deployment is depicted in Fig. 2. This workflow illustrates the sequential steps, beginning with raw data

![](_page_2_Figure_15.jpeg)

**Fig. 2.** Flowchart illustrating the predictive analysis process using a regression learning model in MATLAB.

<span id="page-3-0"></span>acquisition and continuing through preprocessing, model training, and validation. It also comprises deployment and the integration of real-time feedback. Thus, these steps demonstrate how the proposed methodology facilitates adaptive system optimization, enabling continuous improvement and enhanced performance over time.

#### *2.4. Model training and validation*

In this study, four ML models comprising TR, ENS, NN, and GPR, were utilized to predict and optimize UF systems performance. These models were considered because of their proven ability to capture complex, non-linear relationships that are dominant in membrane desalination processes. TR are exceptionally efficient in modelling decision-based splits within datasets and are valued for their interpretability and robustness [\[38\].](#page-10-0) ENS method, which aggregate multiple models to enhance accuracy and reduce overfitting, have been widely applied in environmental and water treatment predictions [\[39\]](#page-10-0). NN, inspired by biological neural processing, excel at identifying complex patterns in large datasets and have demonstrated notable success in various process optimization tasks [\[40\].](#page-10-0) In addition, GPR, a probabilistic approach to regression, provide both predictions and uncertainty quantification, making them particularly useful in cases with sparse training data, as established in [\[41\]](#page-10-0). By integrating these ML approaches, this study aims to develop robust and generalizable models to enhance fouling resistance predictions and optimize UF operational efficiency.

Each model was subjected to rigorous training and hyperparameter optimization using grid search and k-fold cross-validation (k = 5) to safeguard generalizability and predictive robustness. For the TR model, key parameters comprised a maximum tree depth ranging from 5 to 20 and a minimum leaf size between 2 and 10, selected based on performance in predicting TMP-induced flow changes. ENS was implemented employing a bagged ensemble of decision trees (Random Forest), with the number of trees varying from 50 to 200 and a maximum feature selection set to "sqrt" to avoid overfitting and improve generalization. NN were configured using a feedforward architecture with one to three hidden layers, each containing 10–50 neurons, and ReLU activation functions. The models were trained using the Adam optimizer, with learning rates tested in the range of 0.001–0.01. GPR was tuned principally via kernel selection, with the squared exponential and Matern kernels tested to model smooth versus abrupt variations in operational data. Kernel parameters were further refined based on marginal likelihood estimates. All models were implemented and trained in MATLAB 2022a employing the Regression Learner App and custom scripts for deeper network and ensemble tuning. Performance evaluation metrics included RMSE, MAE, and R², and models demonstrating the best tradeoff between predictive accuracy and computational efficiency were selected for real-time deployment.

#### *2.5. Data acquisition and integration with real-time control system*

Real-time data acquisition was conducted using National Instruments cRIO-9022 controllers integrated with sensors to monitor TMP, pH, temperature, ORP, and turbidity. This sensor data was continuously logged, providing real-time input to the ML models. The models were embedded within a real-time control framework that dynamically adjusts UF operational parameters, including backwash frequency, TMP, and filtration cycle timing. This feedback loop enables the UF system to adapt in response to variations in feedwater quality and fouling progression, minimizing downtime and enhancing overall system efficiency. Integrating ML models with real-time sensor feedback allows for proactive fouling control and operational optimization, aligning with the study's objective of advancing sustainable, adaptive desalination technology.

## **3. Results and discussion**

## *3.1. Predictive model performance*

The performance of the various ML models in predicting UF membrane resistance and backwash efficiency was evaluated using multiple metrics, including RMSE, MSE, MAE, and R² is presented in Table 1. These metrics provide insights into the accuracy and reliability of the models under varying operational conditions.

The TR and ENS models demonstrated exceptional performance, achieving the highest predictive accuracy among the models tested. Both models exhibited R² values of 0.99, indicating near-perfect predictive capacity. The RMSE values for these models were 3.27 and 3.08, respectively, the least among all models (Table 1). This low error rate suggests that these models could precisely describe complex, non-linear relationships between operational parameters (such as time, temperature, and transmembrane pressure) and UF membrane fouling.

The performance of the TR model can be attributed to its capacity to handle non-linear interactions between variables and effectively partition the data into smaller, more homogeneous subsets. This model was particularly adept at identifying the key thresholds in operational conditions that significantly impact membrane fouling and backwash efficacy. On the other hand, the ENS learning model, which combines the outputs of multiple weak learners (in this case, TR), further enhanced prediction accuracy by reducing bias and variance. This robust performance makes the ENS model a strong candidate for real-time system control and optimization in UF systems.

The NN and GPR models also recorded excellent performance, with R² values of 0.98 and 0.97, respectively (Table 1). NN, which mimic the structure of the human brain by using layers of interconnected nodes (neurons), were able to model highly complex relationships between input parameters and the resulting UF membrane performance. The NN model's RMSE of 4.69 indicates that, while highly accurate, it introduced slightly more prediction error compared to the Tree and ENS models. This may be due to the "black box" nature of NN, which makes them more challenging to interpret and fine-tune.

From an interpretability perspective, TR and ENS models present clear decision structures and ranked feature importances, enabling operators to trace predictions back to specific operational variables. This is advantageous in industrial UF systems, where model transparency supports rapid diagnosis and operator acceptance. By contrast, NN and GPR provide less direct interpretability, though GPR contributes valuable uncertainty bounds for risk-aware decision-making.

The GPR was applied as a nonparametric, probabilistic model that infers membrane resistance from real-time TMP and flow rate inputs by learning a distribution over functions. Using a squared-exponential kernel, GPR achieved R² = 0.97 and RMSE = 5.98 L/min, providing point estimates and confidence intervals that quantify predictive uncertainty. Although GPR's training complexity (O(n ³ )) limits its

**Table 1**  Performance metrics of various predictive models used for flow rate prediction.

| Model Type | RMSE  | MSE    | R2   | MAE  |
|------------|-------|--------|------|------|
| LR         | 17.42 | 303.34 | 0.75 | 9.09 |
| SLR        | 17.42 | 303.3  | 0.75 | 9.07 |
| SVM        | 12.1  | 146.29 | 0.88 | 5.44 |
| ENS        | 3.08  | 9.51   | 0.99 | 1.21 |
| GPR        | 5.98  | 35.73  | 0.97 | 2.51 |
| NN         | 4.69  | 21.98  | 0.98 | 2.49 |
| KAR        | 12.68 | 160.81 | 0.87 | 6.94 |
| TR         | 3.27  | 10.7   | 0.99 | 1.22 |
|            |       |        |      |      |

NB: The regression results presented in Table 1 reflect the aggregated model performance across the full dataset, encompassing all operational conditions, including variations in temperature, pressure, ORP, pH, and TMP. Subsequent figures ([Figs. 3](#page-5-0)–7) further decompose these results to evaluate model behaviour under specific operational variables.

scalability with enormous datasets, our 426-day dataset (3.7 ×10⁶ samples at 1 Hz) was efficiently handled by employing sparse pseudoinput approximations, reducing computational load without compromising accuracy. These uncertainty bounds proved valuable for adaptive backwash scheduling, enabling risk-aware decisions that balanced fouling mitigation against unnecessary cleaning. Compared to other models, GPR delivered robust performance with interpretable uncertainty, making it a strong candidate for real-time UF fouling control.

A known limitation of GPR is its O(n ³ ) computational complexity. In this study, sparse pseudo-input approximations allowed training on a 3.7 × 10⁶-sample dataset without prohibitive cost. However, scaling to even larger datasets may require distributed implementations or hybrid models combining GPR with faster learners for initial screening. Thus, the GPR model presents a distinctive advantage over other ML approaches by providing point predictions and credible intervals that quantify uncertainty around those predictions [\[42\]](#page-10-0). This probabilistic modelling framework is particularly beneficial in membrane-based desalination systems, where operational conditions such as feedwater quality, TMP, or ORP can fluctuate unpredictably [\[43\].](#page-10-0) In this study, the GPR model employed a squared exponential kernel with automatic relevance determination (ARD) to assess the contribution of each input parameter to the prediction. The model generated a mean prediction curve along with 95 % confidence bounds, enabling conservative operational adjustments in high-risk scenarios. For instance, during filtration-backwash transition phases, where flow performance becomes nonlinear and abrupt, the GPR's uncertainty intervals helped indicate model confidence and potential error margins. This feature is essential for real-time control systems, permitting operators to account for prediction variability when making fouling mitigation decisions. Although GPR showed slightly lower predictive precision compared to ENS and TR (RMSE of 5.98 L/min and R² of 0.97), its probabilistic abilities make it remarkably effective in systems requiring risk-aware decision-making under uncertain conditions. These analyses showcase the importance of GPR not just as a predictive tool but as a risk-sensitive model for dynamic process management.

SVM and kernel-based methods also showed promising results, though their performance was slightly lower than that of the TR, ENS, NN, and GPR models. The SVM model, with an RMSE of 12.1 and an R² of 0.88, was able to capture key trends in membrane fouling but struggled with more complex, non-linear relationships between operational parameters [\(Table 1\)](#page-3-0).

SVMs are widely recognized for their robustness in high-dimensional feature spaces and their effectiveness in classification and regression tasks where decision boundaries are well-defined [\[44\]](#page-10-0). However, in complex nonlinear systems such as UF operation, where relationships between operational parameters are continuously evolving, their performance may be limited compared to ENS or tree-based models [\[45\].](#page-10-0)

The kernel method, which transforms data into higher-dimensional spaces to make it easier to find relationships, achieved an RMSE of 12.68 and an R² of 0.87 ([Table 1](#page-3-0)). While still fairly accurate, kernel methods were less efficient in modelling the intricate interactions between variables, likely due to their sensitivity to parameter tuning and the complexity of the system.

Both the standard LR and SLR models performed the least among the models tested, with RMSE values of 17.42 and an R² of 0.75 ([Table 1](#page-3-0)). This indicates that these models could only explain 75 % of the variance in UF membrane resistance and backwash efficiency, leaving a significant portion of the data unaccounted for. Linear regression assumes a linear relationship between input and output variables, which is not sufficient for modelling the non-linear processes inherent in UF systems.

While linear models are useful for identifying basic trends and relationships, they are not well-suited for handling the complex interactions that drive membrane fouling, such as the effects of fluctuating water quality, temperature, and pH on fouling behaviour. These results demonstrate the importance of using non-linear models, such as TR, ENS, and NN, for accurate prediction and system optimization.

The results from the predictive models indicate that advanced ML algorithms, particularly TR, ENS, and NN, present significant potential for real-time optimization of UF systems. By accurately predicting membrane fouling rates and backwash efficiency, these models can inform dynamic adjustments to operational parameters such as transmembrane pressure, filtration cycle times, and backwash frequency.

The high R² values achieved by the TR and ENS models indicate that these models could be reliably integrated into a real-time control system, enabling operators to pre-emptively mitigate fouling and extend membrane life. The ability to predict fouling onset and adjust parameters before significant performance degradation occurs represents a substantial improvement over traditional static operational strategies, which often rely on fixed backwash intervals and reactive maintenance approaches.

Reducing backwash frequency from one event every 6 h to one every 8 h translates into an estimated 25–30 % reduction in backwashassociated energy use, equivalent to approximately 4.5–5.0 MWh/year for the study system. Combined with the 18 % decline in average TMP excursions, this operational optimization is projected to reduce annual maintenance costs by almost 12 % (USD 3000–3500 per UF train), primarily owing to declined cleaning chemical use, labour, and membrane wear.

Moreover, the probabilistic nature of the GPR model, combined with the interpretability of TR, makes these models highly suitable for decision-making in environments characterized by uncertainty. By exploring these predictive models, UF systems can achieve a higher degree of operational efficiency, reducing both energy consumption and the frequency of costly membrane replacements.

#### *3.2. Model performance across operational parameters*

In [Figs. 3 and 4](#page-5-0), predicted flow rate data are generated using the ENS model, demonstrating the excellent and highest accuracy among all tested models, with an R² of 0.99 and an RMSE of 3.08 L/min. This model was chosen for visualization and in-depth flow prediction analysis because of its consistent superiority across all operational variables. All comparisons with experimental data presented in these figures are based on ENS predictions. The total monitored period used for predictive modelling was 15,000 s; however, a 12,000-second representative window was selected for detailed visualization and analysis, comprising multiple filtration-backwash cycles.

[Fig. 3\(](#page-5-0)a-e) presents a consolidated analysis of predicted versus true flow rates under varying operational conditions, time, temperature, pressure, ORP, and pH, using the ENS model, which consistently outperformed other models. The TR model followed closely, with both models achieving R² values of 0.99 and RMSE values of 3.08 and 3.27 L/ min, respectively.

The time-series prediction [\(Fig. 3](#page-5-0)a) captures cyclic filtration–backwash transitions across seconds, with high fidelity maintained even at operational inflection points. Deviations between predicted and true values during rapid transitions, particularly around 5000 and 10,000 s, were limited to 5–10 L/min, likely due to abrupt shifts in transmembrane pressure and membrane resistance. Nonetheless, the models demonstrated excellent adaptability across filtration and cleaning phases.

Model performance remained robust under variable temperature (15.2–16.6 ◦C; [Fig. 3](#page-5-0)b), pressure (2.06–2.16 bar; [Fig. 3c](#page-5-0)), ORP (-1750.4 to − 1749.8 mV; [Fig. 3](#page-5-0)d), and pH (0–8; [Fig. 3](#page-5-0)e). As noticed in [Fig. 3\(](#page-5-0)d), fewer true data points appear in the high-flow range (90–100 L/min) during filtration, even though filtration phases are significantly lengthier than backwash phases. This apparent imbalance occurs because ORP values tend to remain relatively stable during steady-state filtration, resulting in less variation across this parameter range. As a result, fewer unique data points are plotted at higher flow rates. In addition, to reduce redundancy and improve visual clarity, preprocessing steps were applied to downsize continuous high-flow data, which

<span id="page-5-0"></span>![](_page_5_Figure_2.jpeg)

**Fig. 3.** Comparative flow rate prediction performance across key operational variables, time (a), temperature (b), pressure (c), ORP (d), pH (e), using ENS and TR models. NB: The operational feedwater pH was sustained between 7.5 and 8.2 in e. Fewer data points appear in this range because of high data density and filtering during preprocessing. Points outside this range are likely artifacts and do not reflect actual system chemistry.

![](_page_6_Figure_2.jpeg)

**Fig. 4.** Comparison of true and predicted flow rates (L/min) over an operational period of 15,000 s under dynamic UF conditions using the ENS model. Colour gradient represents the normalized scale of a selected operational parameter (ORP, TMP, pH, time, pressure, temperature) used during training.

may have further limited the density of visible filtration points in the plotted dataset.

The predicted flow rates closely track the true values across the full pH range shown in [Fig. 3](#page-5-0)(e). However, it is important to note that the actual operational pH of the UF feedwater was sustained between 7.5 and 8.2, as stated in the methodology. The strong correlation of predicted and true flow rates in this range demonstrates the model's ability to accurately simulate filtration behaviour under typical operational conditions. Data points appearing under pH 7 likely stemmed from transient sensor artifacts or outliers retained during preprocessing and are not representative of the system's actual chemistry. Despite these transient anomalies, the ENS and TR models demonstrate robust predictive precision, achieving RMSE values of 3.08 and 3.27 L/min, respectively, across the valid pH range.

In each case, the ENS and TR models demonstrated superior accuracy over conventional approaches reported in prior studies [\[29,46,47\]](#page-9-0), where RMSE values for flow rate prediction often ranged between 5 and 12 L/min. The current models exhibited stronger alignment during steady filtration and dynamic backwash events, with minimal loss of accuracy under fluctuating pH and oxidative conditions. Thus, this modelling framework demonstrates high predictive precision and operational resilience, making it suitable for integration into real-time control systems in UF pretreatment processes. Its generalizability across operational parameters positions it as a reliable tool for fouling mitigation and energy-efficient desalination operations.

To further improve the clarity as well as comparative understanding of model performance, Table 2 presents a consolidated outline of the predictive accuracy of the four most relevant models including ENS, TR, NN, and GPR respectively, across key operational variables including time, pH, temperature, pressure, and ORP. As shown, both the ENS and TR models consistently outperformed NN and GPR, attaining the least RMSE and the highest R² scores (0.99) across all variables. This consistent performance reinforces the robustness and generalizability of ENS and TR in modelling dynamic flow rate fluctuations under varied operational conditions. On the other hand, while the NN and GPR models also exhibited high predictive capability (R² values of 0.97–0.98), they demonstrated slightly higher error margins, particularly under conditions of abrupt system transitions. Table 2 further substantiates the earlier findings and affirms the suitability of ENS and TR models for real-time deployment in adaptive control systems within membrane desalination processes.

**Table 2**  Comparative analysis of ML model performance (ENS, TR, NN, GPR) in predicting flow rates across key UF operational variables. Metrics include RMSE and R².

| Operational Variables | Model | RMSE (L/min) | R²   |
|-----------------------|-------|--------------|------|
| Time                  | ENS   | 3.08         | 0.99 |
|                       | TR    | 3.27         | 0.99 |
|                       | NN    | 4.69         | 0.98 |
|                       | GPR   | 5.98         | 0.97 |
| pH                    | ENS   | 3.08         | 0.99 |
|                       | TR    | 3.27         | 0.99 |
|                       | NN    | 4.69         | 0.98 |
|                       | GPR   | 5.98         | 0.97 |
| Temperature           | ENS   | 3.08         | 0.99 |
|                       | TR    | 3.27         | 0.99 |
|                       | NN    | 4.69         | 0.98 |
|                       | GPR   | 5.98         | 0.97 |
| Pressure              | ENS   | 3.08         | 0.99 |
|                       | TR    | 3.27         | 0.99 |
|                       | NN    | 4.69         | 0.98 |
|                       | GPR   | 5.98         | 0.97 |
| ORP                   | ENS   | 3.08         | 0.99 |
|                       | TR    | 3.27         | 0.99 |
|                       | NN    | 4.69         | 0.98 |
|                       | GPR   | 5.98         | 0.97 |

Therefore, the ENS and TR models stand out as the most reliable predictors of flow rate across all key variables, with superior accuracy and minimal error rates. These models are recommended for real-time UF system optimization where accurate predictions of flow rates are critical. Besides, NN and GPR are also viable alternatives, although their slightly higher error rates suggest that they may not be as well-suited for time-sensitive predictions. Thus, SVM, KAR Methods, and LR models, with their higher RMSE and MAE values, are less suitable for this application, particularly in systems where non-linear relationships between variables significantly impact flow rate predictions.

## *3.3. Predictive performance and operational dynamics in ultrafiltration systems*

Fig. 4 illustrates the predictive accuracy of the ML model, comparing predicted (blue) and actual (orange) flow rates across multiple operational cycles in the UF system. Each cycle consists of a filtration phase followed by backwash, with the x-axis representing sequential record numbers over time. The close alignment between predicted and measured values demonstrates the model's ability to reproduce the system's dynamic operational performance accurately.

The model performs reliably across both steady-state and transient phases. Flow rates typically stabilize or decline gradually during filtration due to progressive fouling patterns that the model successfully replicates. The sharp drops in flow during backwash events are also well captured, describing the model's responsiveness to abrupt system changes. These results confirm the model's capacity to simulate nonlinear interactions among key operational variables such as TMP, membrane resistance, and flow recovery during cleaning cycles.

Notably, the model outperforms prior approaches in predictive accuracy. Previous studies, including [\[29\]](#page-9-0) and [\[37\]](#page-10-0) reported RMSE values ranging from 5 to 12 L/min under similar conditions. By contrast, this study's RMSE of 3.08 L/min establishes a new performance benchmark, reflecting superior generalization and robustness.

A key advantage lies in the model's consistency across extended operational periods, even under varying system conditions. Although minor deviations occur at filtration-to-backwash transitions, these are transient and rapidly corrected. This stability enables integration into real-time control frameworks, supporting proactive system management. Exclusively, the model can inform dynamic adjustments in TMP regulation, backwash scheduling, and fouling mitigation strategies essential for ensuring operational efficiency and reducing energy

## <span id="page-7-0"></span>consumption.

These findings carry significant implications for the advancement of membrane-based water treatment. The ability to predict flow rate performance with high accuracy enhances process reliability, minimizes unplanned downtime, and extends membrane lifespan. When integrated into automated control systems, such models offer a pathway toward more sustainable, cost-effective, and intelligent UF system operation, directly supporting industry goals in desalination and clean water production.

## *3.4. Comparative analysis of flow rate predictions in ultrafiltration systems*

Fig. 5 presents the ML model's predictive performance for flow rate in the UF system. The scatter plot compares predicted values (y-axis) against measured values (x-axis), with a 1:1 reference line indicating perfect prediction. The ENS model achieved an R² of 0.99 and an RMSE of 3.08 L/min, showing excellent alignment between predicted and actual flow rates. Most data points are tightly clustered along the 1:1 line, demonstrating the model's robustness in capturing both steadystate and transient flow behaviours under varying operational conditions.

This performance surpasses that of previously reported models. For instance, [\[29\]](#page-9-0) reported RMSE values of 5–10 L/min for flow rate predictions in UF systems, while [\[4\]](#page-9-0) observed errors as high as 12 L/min. This study's superior accuracy reveals the model's capability to capture non-linear interactions between critical variables such as TMP, temperature, and pH.

The model's generalization ability under operational fluctuations is consistent with findings by [\[48\],](#page-10-0) who employed ENS models to optimize backwash cycles in pilot-scale UF systems. However, while Zhang's approach focused on backwash scheduling, the current study incorporates a wider set of real-time operational variables, improving overall flow prediction accuracy. Similarly, Zhou et al.[\[37\]](#page-10-0) employed NN in membrane process modelling but reported RMSE values exceeding 6 L/min, partly due to limitations in handling abrupt TMP transitions. The improved performance observed in this study suggests more precise modelling of dynamic conditions and rapid operational shifts.

These findings have significant implications for UF systems where consistent flow rate is essential for fouling control and energy optimization. By outperforming prior models in accuracy and resilience, the proposed framework demonstrates high potential for real-time

![](_page_7_Figure_9.jpeg)

**Fig. 5.** Scatter plot comparing the UF system's predicted and true flow rates (L/ min). Predicted values were generated using the ENS model. Operational stages (filtration and backwash) are reflected in data spread across flow ranges.

monitoring and control. This contributes to the development of smarter, data-driven membrane operations that support both operational efficiency and long-term sustainability in seawater desalination pretreatment.

## *3.5. Residual analysis of predicted and true flow rates in the ultrafiltration system*

Fig. 6 depicts the residual analysis comparing predicted and true flow rates (L/min) within the UF system. The residuals are tightly clustered around the zero-error line, indicating minimal bias and the model's strong ability to capture the non-linear interactions between key operational parameters, including TMP, temperature, and pH. With an RMSE of 3.08 L/min, the model demonstrates excellent agreement across the full operational range and outperforms many existing frameworks developed for UF flow prediction.

This accuracy represents a significant improvement over prior work. For instance, Im et al. [\[49\]](#page-10-0) reported RMSE values exceeding 5 L/min using deep learning for fouling prediction, while Viet & Jang [\[38\]](#page-10-0) achieved 0.56 % error using hybrid models for backwash control in forward osmosis (FO) systems. Zhou et al. (2021) observed elevated error rates in neural network models under rapid TMP changes. By contrast, the ENS model employed in this study effectively mitigates such errors through adaptive learning and partitioning techniques, resulting in reduced residuals and superior generalization under dynamic operating conditions.

The model's high performance is attributed to the ENS's ability to combine multiple weak learners, reduce overfitting, and improve predictive robustness. In contrast to SVMs, which struggled with non-linear variability in Zhou et al. [\[37\]](#page-10-0), the ENS approach successfully captures system dynamics across filtration and backwash phases. The residuals remain below ±5 L/min for most data points, with only a few outliers reaching ±20 L/min, typically during abrupt flow shifts induced by TMP or turbulence during cleaning events.

These outliers are consistent with findings from Deng et al. [\[29\],](#page-9-0) who reported similar challenges when modelling transitional flow states in membrane systems. Further improvements may require integrating physical process understanding with data-driven models. For example, sudden spikes in residuals may be linked to rapid fouling layer

![](_page_7_Figure_17.jpeg)

**Fig. 6.** Residual plot comparing predicted and actual flow rates (L/min) for the UF system using the ENS model. Residual clustering near the zero-error line indicates high predictive accuracy during steady-state operation, while occasional larger deviations occur during rapid filtration-backwash transitions. These deviations highlight the impact of abrupt TMP shifts and turbulence on short-term prediction accuracy, providing actionable insight for refining control strategies during transitional phases.

detachment during backwash or erratic TMP surges phenomena better addressed through hybrid modelling approaches. Studies by Quaghebeur et al. [\[50\]](#page-10-0) and Wang et al. [\[51\]](#page-10-0) support this direction, showing that combining ML with mechanistic models can enhance performance under extreme operating conditions.

Therefore, the ENS model establishes a new benchmark for predictive modelling in UF systems. Its high R² and low RMSE validate its potential for real-time optimization, enabling intelligent control of backwash frequency, TMP adjustment, and cleaning protocols. These capabilities directly contribute to reducing energy use, mitigating membrane fouling, and extending system lifespan.

## *3.6. Model performance and residual behaviour under variable operating conditions*

While [Section 3.5](#page-7-0) assessed residuals across the full dataset to evaluate overall model accuracy, this section focuses on residual performance under variable and dynamic operational conditions. These include periods characterized by high TMP, abrupt transitions between filtration and backwash, and changes in feedwater quality. This analysis provides a comprehensive insight into the model's robustness and response stability when exposed to non-linear, transient phenomena that are typical of real-world UF system operation.

Fig. 7 presents the residuals (predicted minus actual flow rates) plotted against true flow rates (L/min). The dense clustering of residuals around the zero-error line, particularly at mid-range flow rates (60–100 L/min), reflects the model's strong accuracy during typical operational settings. An R² of 0.97 and RMSE of 4.15 L/min confirm high predictive reliability across most conditions. These results reinforce the model's ability to capture the complex relationships between flow dynamics and influencing parameters such as TMP, temperature, and pH.

However, the wider spread of residuals at higher flow rates suggests challenges in capturing extreme operational events, particularly rapid TMP shifts and turbulence during cleaning transitions. This is consistent with prior findings by [\[52\]](#page-10-0), who observed increased residual errors in NN models during abrupt dynamic phases in membrane systems. The

![](_page_8_Figure_8.jpeg)

**Fig. 7.** Scatter plot of residuals (predicted minus actual flow rate) versus true flow rate (L/min) for the UF system using the ENS model. The dense clustering of residuals around zero at mid-range flow rates reflects robust model performance under typical operating conditions. Wider spreads at higher flow rates correspond to transitional events, underscoring the importance of targeted modelling improvements (transition-specific sub-models) to enhance accuracy during abrupt operational changes.

larger deviations noticed during filtration-to-backwash transitions are attributed to rapid TMP fluctuations and transient hydrodynamic effects, such as fouling layer detachment and turbulence in the feed channel. These short-duration events can generate non-linearities that exceed the temporal resolution of the current model inputs. To mitigate these errors, future developments may include: (i) adaptive sampling strategies with increased data acquisition frequency during transition periods, (ii) event-specific sub-models trained exclusively on transitional phase data using change-point detection, and (iii) hybrid physical-ML frameworks that integrate mechanistic TMP-fouling relationships with data-driven predictors. Such approaches could further enhance model stability and accuracy during rapid operational shifts.

The model's accuracy outperforms several benchmarks. Santamaria & Macchietto [\[53\]](#page-10-0) reported RMSE values of 5–7 L/min for flow prediction in heat exchanger systems, while Jradi et la. [\[54\]](#page-10-0) achieved extremely low RMSE values in highly controlled fouling prediction studies. In comparison, the RMSE of 4.15 L/min obtained here reflects a notable improvement in operational realism and robustness. While residual deviations at high flow rates remain, they are limited and offer actionable insight for future refinement.

These findings have practical implications. Precise flow rate prediction supports smarter control strategies, enabling optimal TMP regulation, adaptive backwash scheduling, and proactive fouling mitigation. As reported by Krishnan et al[.\[55\],](#page-10-0) real-time control models with high predictive fidelity are critical for optimizing energy use and extending membrane lifespan. The model's performance in this study demonstrates that even under fluctuating or extreme conditions, accurate prediction is achievable.

#### **4. Conclusion**

This study demonstrates the effectiveness of advanced ML models for real-time prediction and operational optimization in UF systems used in seawater desalination pretreatment. Over a 426-day monitoring period, ENS and TR models achieved high predictive accuracy, with R² values of 0.99 and RMSE as low as 3.08 L/min. These models successfully captured non-linear interactions among critical parameters, including TMP, temperature, pH, and ORP, enabling dynamic system responses to changing operational conditions. Their deployment presents a datadriven framework for reducing membrane fouling, enhancing backwash scheduling, and improving overall energy efficiency.

Beyond their immediate applicability to UF operations, the proposed ML framework presents a scalable and transferable solution for other membrane-based water treatment systems, particularly those operating under variable environmental or feedwater conditions. The adaptability of ENS and NN models makes them suitable for integration into brackish water treatment, hybrid desalination setups, and decentralized water systems. Moreover, the probabilistic capabilities of GPR provide useful uncertainty quantification, supporting risk-aware operational decisions in regions with fluctuating water quality.

Beyond improving stability, the optimized ML-based control framework presents tangible economic and environmental benefits. The reduction in backwash frequency achieved in this study is estimated to save 4.5–5.0 MWh/year in energy use and lower annual maintenance costs by USD 3000–3500 per UF train, strengthening the value of predictive, data-driven control strategies for sustainable desalination operations.

Hence, the broader implications of this research stem from its potential to advance sustainable desalination practices. By integrating realtime ML models with membrane process control, water treatment facilities can optimize performance, widen membrane lifespan, and reduce environmental repercussions. This approach aligns with global goals for sustainable resource management and climate resilience.

## <span id="page-9-0"></span>**CRediT authorship contribution statement**

**Gani M. Iztleuov:** Visualization, Validation, Software, Formal analysis, Data curation. **Marat I. Sataev:** Visualization, Validation, Software, Formal analysis. **Nazmi Mat Nawi:** Supervision, Project administration, Methodology, Investigation, Data curation, Conceptualization. **Muhammad Adib Mohd Nasir:** Writing – original draft, Supervision, Project administration, Methodology, Investigation, Conceptualization. **Kamil Kayode Katibi:** Writing – review & editing, Writing – original draft, Methodology, Investigation, Conceptualization. **Azimov Abdugani Mutalovich:** Writing – review & editing, Resources, Project administration, Funding acquisition.

#### **Declaration of Competing Interest**

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

#### **Acknowledgments**

Financial support from the project No. 30-PCF-23–24 dated January 25, 2023, subject: BR18574143\u201C. Development and implementation of groundwater purification technology and provision of drinking water to the population and animals of an agricultural enterprise\u201D financed by the Ministry of Science and Higher Education of the Republic of Kazakhstan and partial funding from RUSA and SPARC are gratefully acknowledged.

#### *Declaration of competing interest*

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the research reported in this manuscript.

## **Data Availability**

Data will be made available on request. The data supporting this study's findings are available from the corresponding author upon reasonable request.

# **References**

- [1] Mahmod SS, Takriff MS, AL-Rajabi MM, Abdul PM, Gunny AAN, Silvamany H, Jahim JM. Water reclamation from palm oil mill effluent (POME): recent technologies, by-product recovery, and challenges. J Water Process Eng 2023;52: 103488. [https://doi.org/10.1016/j.jwpe.2023.103488.](https://doi.org/10.1016/j.jwpe.2023.103488)
- [2] Ng ZC, Lau WJ, Matsuura T, Ismail AF. Thin film nanocomposite RO membranes: review on fabrication techniques and impacts of nanofiller characteristics on membrane properties. Chem Eng Res Des 2021;165:81–105. [https://doi.org/](https://doi.org/10.1016/j.cherd.2020.10.003)  [10.1016/j.cherd.2020.10.003.](https://doi.org/10.1016/j.cherd.2020.10.003)
- [3] Z.E. AlHadithy, A.A. AbdulRazak, A.M.H.A. Al-Ghaban, Q.F. Alsalhy, H. Meskher, R.A. Al-Juboori, K.K. Katibi, D.U. Lawal, Advancements in Water Treatment with MXene-Enhanced Membranes: A Review of Current Progress and Future Directions; 2024. [https://doi.org/10.1007/s11270-024-07628-x.](https://doi.org/10.1007/s11270-024-07628-x)
- [4] Gu H, Rahardianto A, Gao LX, Caro XP, Giralt J, Rallo R, Christofides PD, Cohen Y. Fouling indicators for field monitoring the effectiveness of operational strategies of ultrafiltration as pretreatment for seawater desalination. Desalination 2018;431: 86–99. [https://doi.org/10.1016/j.desal.2017.11.038.](https://doi.org/10.1016/j.desal.2017.11.038)
- [5] Li H, Tao Y, Xu T, Wang H, Yang M, Chen Y, Wang A. Real-time quantification of activated sludge concentration and viscosity through deep learning of microscopic images. Environ Sci Ecotechnol 2025;24:100527. [https://doi.org/10.1016/j.](https://doi.org/10.1016/j.ese.2025.100527) [ese.2025.100527](https://doi.org/10.1016/j.ese.2025.100527).
- [6] Daneshnia S, Shams A, Daraei D, Abdouss M, Daneshmayeh M. Novel thin film nanocomposite membrane modified with boron nitride nanosheets for water treatment. Colloids Surf A Physicochem Eng Asp 2022;651:129768. [https://doi.](https://doi.org/10.1016/j.colsurfa.2022.129768)  [org/10.1016/j.colsurfa.2022.129768](https://doi.org/10.1016/j.colsurfa.2022.129768).
- [7] Kadhom M, Deng B. Metal-organic frameworks (MOFs) in water filtration membranes for desalination and other applications. Appl Mater Today 2018;11: 219–30. [https://doi.org/10.1016/j.apmt.2018.02.008.](https://doi.org/10.1016/j.apmt.2018.02.008)
- [8] [Katibi KK, Yunos KF, Man HC, Aris AZ, Zuhair M, Syahidah R. Recent advances in](http://refhub.elsevier.com/S1944-3986(25)00402-3/sbref7)  [the rejection of Endocrine-Disrupting compounds from water using membrane and](http://refhub.elsevier.com/S1944-3986(25)00402-3/sbref7)  [membrane bioreactor technologies: a review. Polym \(Basel\) 2021;13:392](http://refhub.elsevier.com/S1944-3986(25)00402-3/sbref7).

- [9] Ustabayev T, Tazhgaliyev Y, Balgabayev N, Mirdadayev M, Telgarayeva G. Methods of disposal of brines and regeneration solutions in the desalination of mineralised waters. Water Conserv Manag 2024;8:87–93. [https://doi.org/](https://doi.org/10.26480/wcm.01.2024.87.93)  [10.26480/wcm.01.2024.87.93](https://doi.org/10.26480/wcm.01.2024.87.93).
- [10] Asadollahi M, Bastani D, Musavi SA. Enhancement of surface properties and performance of reverse osmosis membranes after surface modification: a review. Desalination 2017;420:330–83. [https://doi.org/10.1016/j.desal.2017.05.027.](https://doi.org/10.1016/j.desal.2017.05.027)
- [11] Abdulsalam M, Umar M, Babangida I, Saulawa B, Kayode K, Silas K, Garba I. Functionalized MgO – nanoparticle integrated with PVDF-PEG fibre enhances strength and contaminant separation efficacy. Clean Chem Eng 2024;10:100135. <https://doi.org/10.1016/j.clce.2024.100135>.
- [12] Katibi KK, Yunos KF, Man HC, Aris AZ, Nor MZM, Azis RS, Umar AM. Contemporary techniques for remediating endocrine-disrupting compounds in various water sources: advances in treatment methods and their limitations. Polym (Basel) 2021;13:1–46. [https://doi.org/10.3390/polym13193229.](https://doi.org/10.3390/polym13193229)
- [13] Abba MU, Man HC, Azis RS, Idris AI, Hamzah MH, Yunos KF, Katibi KK. Novel PVDF-PVP hollow fiber membrane augmented with TiO2 nanoparticles: preparation, characterization and application for copper removal from leachate. Nanomaterials 2021;11:1–18. [https://doi.org/10.3390/nano11020399.](https://doi.org/10.3390/nano11020399)
- [14] Kim S, Chu KH, Al-Hamadani YAJ, Park CM, Jang M, Kim DH, Yu M, Heo J, Yoon Y. Removal of contaminants of emerging concern by membranes in water and wastewater: a review. Chem Eng J 2018;335:896–914. [https://doi.org/10.1016/j.](https://doi.org/10.1016/j.cej.2017.11.044)  [cej.2017.11.044.](https://doi.org/10.1016/j.cej.2017.11.044)
- [15] [Katibi KK, Zuhair M, Nor M, Yunos KF, Jaafar J. Strategies to enhance the](http://refhub.elsevier.com/S1944-3986(25)00402-3/sbref14)  [Membrane-Based processing performance for fruit juice production: a review.](http://refhub.elsevier.com/S1944-3986(25)00402-3/sbref14)  [Membr \(Basel\) 2023;13:679.](http://refhub.elsevier.com/S1944-3986(25)00402-3/sbref14)
- [16] [Zhang X, Zhao X, Sun J, He Y, Wu B, Ge L, Pan J. Ultrathin zwitterionic COF](http://refhub.elsevier.com/S1944-3986(25)00402-3/sbref15) [membranes from colloidal 2D-COF towards precise molecular sieving. Water Res](http://refhub.elsevier.com/S1944-3986(25)00402-3/sbref15)  [2025;274:123073](http://refhub.elsevier.com/S1944-3986(25)00402-3/sbref15).
- [17] Gao H, Zhong S, Dangayach R, Chen Y. Understanding and designing a High-Performance ultrafiltration membrane using machine learning. Environ Sci Technol 2023;57:17831–40. [https://doi.org/10.1021/acs.est.2c05404.](https://doi.org/10.1021/acs.est.2c05404)
- [18] Ding W, Chen M, Zhou M, Zhong Z, Cui Z, Xing W. Fouling behavior of poly (vinylidene fluoride) (PVDF) ultrafiltration membrane by polyvinyl alcohol (PVA) and chemical cleaning method. Chin J Chem Eng 2020;28:3018–26. [https://doi.](https://doi.org/10.1016/j.cjche.2020.05.032)  [org/10.1016/j.cjche.2020.05.032.](https://doi.org/10.1016/j.cjche.2020.05.032)
- [19] [Yang C, Li Z, Li S, Cui X, Chen Q. Sustainable evaporative cooling driven by saline](http://refhub.elsevier.com/S1944-3986(25)00402-3/sbref18)  [water sources: opportunities, challenges and solutions. Renew Sustain Energy Rev](http://refhub.elsevier.com/S1944-3986(25)00402-3/sbref18)  [2025;218:115799](http://refhub.elsevier.com/S1944-3986(25)00402-3/sbref18).
- [20] Abdulsalam M, Man HC, Goh PS, Yunos KF, Abidin ZZ, Isma MIA, Ismail AF. Permeability and antifouling augmentation of a hybrid PVDF-PEG membrane using nano-magnesium oxide as a powerful mediator for POME decolorization. Polym (Basel) 2020;12:1–21. [https://doi.org/10.3390/polym12030549.](https://doi.org/10.3390/polym12030549)
- [21] Xiao T, Zhu Z, Li L, Shi J, Li Z, Zuo X. Membrane fouling and cleaning strategies in microfiltration/ultrafiltration and dynamic membrane. Sep Purif Technol 2023; 318:123977. [https://doi.org/10.1016/j.seppur.2023.123977.](https://doi.org/10.1016/j.seppur.2023.123977)
- [22] Gruskevica K, Mezule L. Cleaning methods for ceramic ultrafiltration membranes affected by organic fouling. Membr (Basel) 2021;11:1–15. [https://doi.org/](https://doi.org/10.3390/membranes11020131)  [10.3390/membranes11020131.](https://doi.org/10.3390/membranes11020131)
- [23] Fokhrul M., Buian I., Pantho N.A., Siddique I.Industrial Process Optimization for the Effective Removal of Per- and Polyfluoroalkyl Substances ( PFAS) from Water Treatment Systems Industrial Process Optimization for the Effective Removal of Per- and Polyfluoroalkyl Substances ( PFAS) from Water Tre; 2024 11 p.1–12.
- [24] Fang C, Ou T, Wang X, Rui M, Chu W. Effects of feed solution characteristics and membrane fouling on the removal of THMs by UF/NF/RO membranes. Chemosphere 2020;260:127625. [https://doi.org/10.1016/j.](https://doi.org/10.1016/j.chemosphere.2020.127625) [chemosphere.2020.127625.](https://doi.org/10.1016/j.chemosphere.2020.127625)
- [25] [Abdykadyrov A, Marxuly S, Kuttybayeva A, Domrachev V, Boranbayeva A,](http://refhub.elsevier.com/S1944-3986(25)00402-3/sbref23)  [Kasimov A, Yerzhan A, Baibolov N. Process of determination of surface water by](http://refhub.elsevier.com/S1944-3986(25)00402-3/sbref23)  [ultraviolet radiations. Water Conserv Manag 2023;7:158](http://refhub.elsevier.com/S1944-3986(25)00402-3/sbref23)–67.
- [26] Satayev M, Azimov A, Brener A, Alekseeva N, Shakiryanova Z. Model of selectivity of membrane processes and dissolution of impurities in a membrane pore in a medium with Surface-Active micelles. J Adv Res Fluid Mech Therm Sci 2024;120: 151–75. [https://doi.org/10.37934/arfmts.120.1.151175.](https://doi.org/10.37934/arfmts.120.1.151175)
- [27] Yin H, Xu M, Luo Z, Bi X, Li J, Zhang S, Wang X. Machine learning for membrane design and discovery. Green Energy Environ 2024;9:54–70. [https://doi.org/](https://doi.org/10.1016/j.gee.2022.12.001) [10.1016/j.gee.2022.12.001.](https://doi.org/10.1016/j.gee.2022.12.001)
- [28] Chew CM, Aroua MK, Hussain MA. A practical hybrid modelling approach for the prediction of potential fouling parameters in ultrafiltration membrane water treatment plant. J Ind Eng Chem 2017;45:145–55. [https://doi.org/10.1016/j.](https://doi.org/10.1016/j.jiec.2016.09.017)  [jiec.2016.09.017.](https://doi.org/10.1016/j.jiec.2016.09.017)
- [29] Deng B, Deng Y, Liu M, Chen Y, Wu Q, Guo H. Integrated models for prediction and global factors sensitivity analysis of ultrafiltration (UF) membrane fouling: statistics and machine learning approach. Sep Purif Technol 2023;313:123326. [https://doi.org/10.1016/j.seppur.2023.123326.](https://doi.org/10.1016/j.seppur.2023.123326)
- [30] Shim J, Hong S, Lee J, Lee S, Kim YM, Chon K, Park S, Cho KH. Deep learning with data preprocessing methods for water quality prediction in ultrafiltration. J Clean Prod 2023;428:139217. [https://doi.org/10.1016/j.jclepro.2023.139217.](https://doi.org/10.1016/j.jclepro.2023.139217)
- [31] Bagheri M, Akbari A, Mirbagheri SA. Advanced control of membrane fouling in filtration systems using artificial intelligence and machine learning techniques: a critical review. Process Saf Environ Prot 2019;123:229–52. [https://doi.org/](https://doi.org/10.1016/j.psep.2019.01.013)  [10.1016/j.psep.2019.01.013.](https://doi.org/10.1016/j.psep.2019.01.013)
- [32] Kovacs DJ, Li Z, Baetz BW, Hong Y, Donnaz S, Zhao X, Zhou P, Ding H, Dong Q. Membrane fouling prediction and uncertainty analysis using machine learning: a wastewater treatment plant case study. J Memb Sci 2022;660:120817. [https://doi.](https://doi.org/10.1016/j.memsci.2022.120817)  [org/10.1016/j.memsci.2022.120817.](https://doi.org/10.1016/j.memsci.2022.120817)

- <span id="page-10-0"></span>[33] Zheng W, Chen Y, Xu X, Peng X, Niu Y, Xu P, Li T. Research on the factors influencing nanofiltration membrane fouling and the prediction of membrane fouling. J Water Process Eng 2024;59:104876. [https://doi.org/10.1016/j.](https://doi.org/10.1016/j.jwpe.2024.104876) [jwpe.2024.104876](https://doi.org/10.1016/j.jwpe.2024.104876).
- [34] Lim SJ, Kim YM, Park H, Ki S, Jeong K, Seo J, Chae SH, Kim JH. Enhancing accuracy of membrane fouling prediction using hybrid machine learning models. Desalin Water Treat 2019;146:22–8. <https://doi.org/10.5004/dwt.2019.23444>.
- [35] Deng B, Deng Y, Liu M, Chen Y, Wu Q, Guo H. Integrated models for prediction and global factors sensitivity analysis of ultrafiltration (UF) membrane fouling: statistics and machine learning approach. Sep Purif Technol 2023;313:123326. [https://doi.org/10.1016/j.seppur.2023.123326.](https://doi.org/10.1016/j.seppur.2023.123326)
- [36] Kim J, Hong S. Pilot study of emerging low-energy seawater reverse osmosis desalination technologies for high-salinity, high-temperature, and high-turbidity seawater. Desalination 2023;565:116871. [https://doi.org/10.1016/j.](https://doi.org/10.1016/j.desal.2023.116871)  [desal.2023.116871](https://doi.org/10.1016/j.desal.2023.116871).
- [37] Zhou Y, Khan B, Gu H, Christofides PD, Cohen Y. Modeling UF fouling and backwash in seawater RO feedwater treatment using neural networks with evolutionary algorithm and Bayesian binary classification. Desalination 2021;513: 115129. [https://doi.org/10.1016/j.desal.2021.115129.](https://doi.org/10.1016/j.desal.2021.115129)
- [38] Viet ND, Jang A. Machine learning-based real-time prediction of micropollutant behaviour in forward osmosis membrane (waste)water treatment. J Clean Prod 2023;389:136023. [https://doi.org/10.1016/j.jclepro.2023.136023.](https://doi.org/10.1016/j.jclepro.2023.136023)
- [39] Fang G, Huang D, Wu Z, Chen Y, Li Y, Liu Y. Effluent quality soft sensor for wastewater treatment plant with ensemble sparse learning-based online next generation reservoir computing. Water Res X 2024;25:100276. [https://doi.org/](https://doi.org/10.1016/j.wroa.2024.100276)  [10.1016/j.wroa.2024.100276.](https://doi.org/10.1016/j.wroa.2024.100276)
- [40] Viet ND, Duksoo J, Yeomin Y, A, Jang. Enhancement of membrane system performance using artificial intelligence technologies for sustainable water and wastewater treatment: a critical review. Crit Rev Environ Sci Technol 2022;52: 3689–719. [https://doi.org/10.1080/10643389.2021.1940031.](https://doi.org/10.1080/10643389.2021.1940031)
- [41] Hvala N, Kocijan J. Design of a hybrid mechanistic/Gaussian process model to predict full-scale wastewater treatment plant effluent. Comput Chem Eng 2020; 140. <https://doi.org/10.1016/j.compchemeng.2020.106934>.
- [42] Hai T, Basem A, Alizadeh A, Sharma K, jasim DJ, Rajab H, Ahmed M, Kassim M, Singh NSS, Maleki H. Optimizing Gaussian process regression (GPR) hyperparameters with three metaheuristic algorithms for viscosity prediction of suspensions containing microencapsulated PCMs. Sci Rep 2024;14. [https://doi.](https://doi.org/10.1038/s41598-024-71027-9)  [org/10.1038/s41598-024-71027-9.](https://doi.org/10.1038/s41598-024-71027-9)
- [43] Viet ND, Jang A. Machine learning-based real-time prediction of micropollutant behaviour in forward osmosis membrane (waste)water treatment. J Clean Prod 2023;389:136023. [https://doi.org/10.1016/j.jclepro.2023.136023.](https://doi.org/10.1016/j.jclepro.2023.136023)
- [44] Shakya DS. Analysis of artificial intelligence based image classification techniques. J Innov Image Process 2020;2:44–54. [https://doi.org/10.36548/jiip.2020.1.005.](https://doi.org/10.36548/jiip.2020.1.005)

- [45] Waqas S, Harun NY, Sambudi NS, Arshad U, Nordin NAHM, Bilad MR, Saeed AAH, Malik AA. SVM and ANN modelling approach for the optimization of membrane permeability of a membrane rotating biological contactor for wastewater treatment. Membrane (Basel) 2022;12. [https://doi.org/10.3390/](https://doi.org/10.3390/membranes12090821) [membranes12090821](https://doi.org/10.3390/membranes12090821).
- [46] Parsa Z, Dhib R, Mehrvar M. Dynamic modelling, process control, and monitoring of selected biological and advanced oxidation processes for wastewater treatment: a review of recent developments. Bioengineering 2024;11(2). [https://doi.org/](https://doi.org/10.3390/bioengineering11020189)  [10.3390/bioengineering11020189.](https://doi.org/10.3390/bioengineering11020189)
- [47] Yaqub M, Lee SH. Experimental and neural network modeling of micellar enhanced ultrafiltration for arsenic removal from aqueous solution. Environ Eng Res 2021;26 (1):1–7. [https://doi.org/10.4491/eer.2019.261.](https://doi.org/10.4491/eer.2019.261)
- [48] Zhang B, Kotsalis G, Khan J, Xiong Z, Igou T, Lan G, Chen Y. Backwash sequence optimization of a pilot-scale ultrafiltration membrane system using data-driven modeling for parameter forecasting. J Memb Sci 2020;612:118464. [https://doi.](https://doi.org/10.1016/j.memsci.2020.118464) [org/10.1016/j.memsci.2020.118464.](https://doi.org/10.1016/j.memsci.2020.118464)
- [49] Im SJ, Viet ND, Jang A. Real-time monitoring of forward osmosis membrane fouling in wastewater reuse process performed with a deep learning model. Chemosphere 2021;275:130047. [https://doi.org/10.1016/j.](https://doi.org/10.1016/j.chemosphere.2021.130047) [chemosphere.2021.130047.](https://doi.org/10.1016/j.chemosphere.2021.130047)
- [50] Quaghebeur W, Torfs E, De Baets B, Nopens I. Hybrid differential equations: integrating mechanistic and data-driven techniques for modelling of water systems. Water Res 2022;213:118166. [https://doi.org/10.1016/j.watres.2022.118166.](https://doi.org/10.1016/j.watres.2022.118166)
- [51] Wang Y, Yu A, Cheng Y, Qi J. Matrix diffractive deep neural networks merging polarization into Meta-Devices. Laser Photonics Rev 2024;18:1–11. [https://doi.](https://doi.org/10.1002/lpor.202300903) [org/10.1002/lpor.202300903.](https://doi.org/10.1002/lpor.202300903)
- [52] Zamouche M, Tahraoui H, Laggoun Z, Mechati S, Chemchmi R, Kanjal MI, Amrane A, Hadadi A, Mouni L. Optimization and prediction of stability of emulsified liquid membrane (ELM): artificial neural network. Processes 2023;11: 1–15. [https://doi.org/10.3390/pr11020364.](https://doi.org/10.3390/pr11020364)
- [53] Lozano-Santamaria F, Macchietto S. Assessment of a dynamic model for the optimization of refinery preheat trains under fouling. Heat Transf Eng 2022;43: 1349–64. <https://doi.org/10.1080/01457632.2021.1963537>.
- [54] Jradi R, Marvillet C, Jeday MR. Multi-objective optimization and performance assessment of response surface methodology (RSM), artificial neural network (ANN) and adaptive neuro-fuzzy interfence system (ANFIS) for estimation of fouling in phosphoric acid/steam heat exchanger. Appl Therm Eng 2024;248: 123255. [https://doi.org/10.1016/j.applthermaleng.2024.123255.](https://doi.org/10.1016/j.applthermaleng.2024.123255)
- [55] Krishnan A, Sundaram T, Nagappan B, Devarajan Y, Bhumika. Integrating artificial intelligence in nanomembrane systems for advanced water desalination. Results Eng 2024;24:103321. [https://doi.org/10.1016/j.rineng.2024.103321.](https://doi.org/10.1016/j.rineng.2024.103321)
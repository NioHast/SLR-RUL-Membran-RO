#### **Article in Press**

# Survival-analysis-guided machine learning for failure and remaining-useful-life prediction in railway compressor

Received: 3 June 2026

Accepted: 30 July 2026

Published online: 07 August 2026

Cite this article as: Hamdi Alaoui A., Meddaoui A. & Hachmoud A. Survival-analysis-guided machine learning for failure and remaining-useful-life prediction in railway compressor. *Sci Rep* (2026). https://doi.org/10.1038/s41598-026-65271-4

#### Abdelhafid Hamdi Alaoui, Anwar Meddaoui & Adil Hachmoud

We are providing an unedited version of this manuscript to give early access to its findings. Before final publication, the manuscript will undergo further editing. Please note there may be errors present which affect the content, and all legal disclaimers apply.

Il-life
If this paper is publishing under a Transparent Peer Review model then Peer Review reports will publish with the final article.

038/

© The Author(s) 2026. **Open Access** This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/">https://creativecommons.org/licenses/by-nc-nd/4.0/</a>.

### Survival-analysis-guided machine learning for failure and remaining-usefullife prediction in railway compressor.

Dr. Hamdi Alaoui Abdelhafid

ENSAM, Hassan II university, Casablanca, Morocco

ab.hamdialaoui@gmail.com

ORCID: 0000-0001-6513-1130

Prof. Meddaoui Anwar\*

ENSAM, Hassan II university, Casablanca, Morocco

anwar.meddaoui@ensam-casa.ma ORCID: 0000-0001-9308-1679

Prof. Hachmoud Adil

EST, Sidi Mohamed Ben Abdellah University, Fes, Morocco

adil.hachmoud@usmba.ac.ma ORCID: 0000-0002-7450-1583

#### Abstract

Predictive maintenance requires reliable failure detection and remaining useful life (RUL) estimation under conditions of noisy sensor data, censored observations, and limited failure labeling. This work presents an interpretable predictive maintenance framework in which a Cox proportional hazards model is used to identify the operational variables most strongly associated with failure risk and to guide the construction of data-driven predictive models. The framework is validated on the real-world MetroPT-3 railway air-compressor dataset, using failure dates reported by the operator to derive both the binary failure-event label and a proxy RUL target. Machine learning and deep learning approaches, including neural networks, tree-based models, and sequential architectures, are then evaluated for failure event prediction and Proxy RUL estimation. The results show that Cox-guided variable selection enables effective dimensionality reduction while preserving high failure detection performance, particularly in terms of sensitivity and specificity. Sequential models prove well suited for failure event prediction, whereas nonlinear tree-based models are more robust for Proxy RUL estimation due to the non-stationary and discontinuous nature of the target variable. The main contribution is a unified, leakage-controlled pipeline that couples Cox-PH survival-based feature selection with a chronological evaluation protocol, showing when statistical guidance helps and when it does not across two distinct maintenance tasks. Overall, the study highlights the practical value of combining statistical explainability and machine learning performance to support robust and interpretable predictive maintenance decision-making in industrial contexts.

**Key words:** Predictive maintenance, failure, Remaining Useful Life, Cox PH survival analysis, ANNs, Random Forest, LSTM,

#### 1. Introduction

The manufacturing sector has undergone a major transformation driven by global competition and digital automation. Modern factories now operate as interconnected, sensor-equipped systems, where managers must ensure both performance and reliability. Machine breakdowns leading to unplanned downtime can disrupt production, increase costs, and create safety risks. Planned preventive maintenance reduces the occurrence of some breakdowns but can generate unnecessary

interventions and excessive expenses. Predictive maintenance, made possible by real-time machine condition monitoring and data analysis, offers a more efficient alternative by helping teams detect early signs of deterioration and schedule maintenance only when necessary. Deploying these strategies remains complex, especially for SMEs, as it requires high-quality data, technical expertise, trained personnel, and organizational support. Despite this, data-driven maintenance decisions continue to play a key role in improving productivity and maintaining the competitiveness of manufacturing operations.

#### • Stages of maintenance maturity

Maintenance maturity follows a staged evolution from reaction to anticipation (see Figure 1). It begins with corrective practices, where actions take place only after breakdowns, often causing avoidable downtime, extra costs, and schedule disruption. The next stage brings planned preventive routines based on fixed intervals, reducing major failures but still triggering some unnecessary interventions due to lack of condition awareness. The third stage adopts a proactive mindset, focusing on root-cause reduction and using condition-based monitoring like vibration or temperature to guide timely interventions. The final stage is predictive maintenance, where data analysis and learning models help estimate failures early, optimize scheduling, preserve asset health, and improve productivity. Progressing through these stages strengthens reliability, controls cost, extends equipment life, and supports competitive industrial performance.

![](_page_2_Figure_4.jpeg)

Figure 1. Maintenance maturity levels

#### • Predictive maintenance

Predictive Maintenance (PdM) has emerged as a practical alternative to schedule-driven preventive routines, which trigger interventions at fixed intervals without accounting for the actual condition

of assets. While preventive planning can reduce major breakdowns, it often generates unnecessary actions or delayed servicing, increasing maintenance costs and disrupting production (Ding et al., 2014). Lee et al. (2014) emphasize that modern manufacturing is shifting toward predictive paradigms, where maintenance must evolve from a support function into a value-creation driver that strengthens sustainability and operational performance. Florian et al. (2021) define PdM as a need-based strategy that activates maintenance only when justified by equipment condition, avoiding both unplanned downtime and over-maintenance waste. PdM combines operational history, analytical models, and domain expertise to detect degradation trends and forecast failures with better timing and precision. Even so, many PdM implementations remain context-dependent and face challenges related to data readiness and uncertainty management (Florian et al., 2021). As a result, current research continues to focus on improving model transferability, integrating business knowledge, and handling operational uncertainties to make predictive maintenance more robust and cost-effective across diverse manufacturing environments.

#### • Importance of proxy failure methods for identifying potential failures

In many industrial contexts, maintenance databases as CMMS have major limitations related to the non-reporting, incompleteness, or delay in recording failures. These shortcomings are particularly common in environments where corrective maintenance is performed without systematic documentation, or when downtime is short and considered a mere operational deviation. In this context, the lack of reliable failure labels is a critical obstacle to the deployment of supervised predictive maintenance methods.

To overcome this constraint, proxy failure methods offer a relevant alternative. Their objective is to detect abnormal or degraded operating situations based on available sensor data, without explicitly relying on a reported failure history. These approaches are based on the assumption that failures are preceded by statistically significant deviations of physical variables (temperature, torque, speed, current, etc.) from a nominal operating condition.

Among the most widely used methods, the multivariate Z-score quantifies the deviation of an operating state from the normalized historical average, taking into account data dispersion. This approach has the advantage of being simple, explainable, and easily deployable in an industrial context. Complementarily, unsupervised learning methods such as Isolation Forest leverage random partitioning principles to identify rare or atypical observations in the variable space, without any prior assumptions about distribution.

Thus, proxy failure methods play a central role in the early detection of potential failures, particularly when failure events are not explicitly recorded in maintenance logs. They constitute an essential intermediate step for generating actionable risk indicators for decision support, maintenance planning, and feeding more advanced predictive models. Statistical models vs. ML models for failures prediction. In the present study, however, the operator provided documented failure dates, so these methods are used as conceptual background rather than for label generation; the labels themselves are derived directly from the reported failure events, as detailed in Section 3

#### • Statistical models for maintenance prediction

Cox Proportional Hazards (Cox PH) and Weibull survival models are widely used statistical

approaches for failure analysis in maintenance engineering. Cox PH is a semi-parametric model that estimates how operational or environmental factors influence the risk of component failure over time without assuming a predefined baseline distribution. In another recent work, Si et al. (2011) examined the general survival analysis techniques of the Weibull model and the K-Meier estimator for the estimation of RUL. They highlighted that survival analysis provides a robust framework to deal, especially, with censored data in the domain of industrial information when machines are generally taken offline before failures. Gao (2022) and his team discussed the application of the Weibull distribution in reliability engineering. They utilized this approach to model industrial component life data. These authors found the Weibull model to be a highly effective model for typical wear-out failures in aging equipment, interesting for predictive maintenance. Otherwise, Godoy et al (2024) examined and compared various statistical models with Weibull/Cox PH models for the prediction of RUL. It was observed that among all the examined models, Cox PH model is more effective with many covariates and gave clear understandings of failure. They noted that Weibull model is more efficient for applications with understood failure mechanisms and distribution.

#### • ML models for maintenance prediction

A review of industrial predictive maintenance research shows sustained interest in machine-learning models for anticipating failures, improving reliability, and reducing downtime. More than 25 studies from the past decade highlight three dominant approaches: Artificial Neural Networks (ANN), Deep Learning (DL), and Random Forest (RF). ANN models remain widely used for structured sensor-based condition monitoring and have proven effective when integrated into Aircraft Health Monitoring for proactive MRO planning (Safoklova et al., 2022). Deep Learning architectures extend these capabilities by automatically extracting hierarchical patterns from raw time-series and visual data, capturing nonlinear degradation dynamics for early fault detection and RUL estimation, as demonstrated across multiple industrial domains (Malawade et al., 2021; Basora et al., 2021; Ning et al., 2021; Wang et al., 2022). Random Forest, introduced by Breiman (2001), remains a reliable supervised method due to its ensemble robustness, feature-importance interpretability, and strong performance in industrial failure classification and regression tasks (Narayan et al., 2022; Narayan et al., 2022). Collectively, these approaches support more precise maintenance timing, better generalization to real factory conditions, and actionable insights for maintenance decision workflows.

#### • Deep Learning (DL) and predictive maintenance

Deep Learning (DL) has revolutionized industrial maintenance by enabling the automatic extraction of complex features from massive and noisy sensor data. Among DL architectures, Long Short-Term Memory (LSTM) neural networks stand out for their unique ability to capture long-term temporal dependencies within time series. Unlike traditional statistical methods, LSTM models can memorize past degradation patterns to accurately predict the remaining life (RUL) of an asset.

Lei et al. (2020) provide an exhaustive review and roadmap on the evolution of machine learning algorithms, emphasizing their transition from traditional statistical analysis towards increasingly

autonomous fault diagnosis solutions. Li et al. (2019) demonstrated the effectiveness of a hybrid architecture combining CNN and LSTM networks to capture complex spatial and temporal characteristics, significantly improving the accuracy of predicting remaining equipment lifespan. Zhang et al. (2018) examined how Deep Learning transforms smart manufacturing by providing advanced methods for processing massive data, thereby facilitating proactive decision-making and real-time optimization of industrial processes.

#### Contributions of this work

While hybrid Cox-machine-learning architectures are well-documented in the literature such as Godoy et al. (2024), who integrated machine-learning estimators into Cox partial-likelihood estimation to refine hazard modeling most existing studies leverage survival models primarily to generate hazard curves. The present research departs from these conventional approaches in both purpose and design. Rather than optimizing the hazard estimate itself, we repurpose the Cox Proportional Hazards (Cox-PH) model as an interpretable, supervised feature-selection layer whose statistically significant covariates are propagated to four diverse learning algorithms, namely ANN, RF, XGBoost, and LSTM. These algorithms are subsequently evaluated across two distinct predictive tasks comprising discrete failure-event classification and continuous proxy Remaining Useful Life (RUL) regression. This study delivers several key contributions to the field, beginning with a unified, Cox-guided pipeline benchmarked against a purely statistical Principal Component Analysis under identical data conditions, which effectively isolates the impact of supervised versus unsupervised dimensionality reduction. Furthermore, we detail an explicit, leakage-controlled methodology for constructing failure-event and proxy RUL labels derived directly from operator-reported failure dates on the MetroPT-3 railway compressor. To ensure realistic deployment conditions, we implement a strictly chronological, time-ordered evaluation protocol that preserves temporal causality. Finally, our findings reveal a critical, task-dependent trade-off where Cox-guided reduction improves discrete event detection but degrades continuous RUL regression, a dynamic we contextualize through a practical discussion on how the resulting risk scores and proxy RULs can directly inform alarm thresholds and maintenance scheduling.

#### 2. The proposed framework

Machine learning has become a core approach for modeling complex systems where data volume and computing capacity continue to expand. Model choice remains a key challenge because algorithms differ in accuracy, interpretability, robustness, and computational cost. The illustrated framework benchmarks two established supervised learning families, by training and evaluating them on the same dataset to support objective model selection for deployment.

This work proposes a hybrid approach based on the integration of a statistical model with four families of machine learning (ML) algorithms and deep learning (DL): artificial neural networks (ANNs), Random Forest (RF), XGBOOST and LSTM models. The main objective is to compare the Cox+ANN and Cox+RF models within a strictly causal framework, where the abnormal degradation event is defined from a composite score derived from sensor signals of operating

equipment. This hybrid approach aims to leverage the ability of Cox PH to quantify the influence of covariates on failure risk, while also benefiting from the power of machine learning models to learn nonlinear interactions and improve the quality of survival and RUL predictions.

#### • The proposed approach

In this section, figure 2 shows the workflow used to create the potential failures, the estimated RUL and prediction of those parameters. The proposed model follows five main stages:

- 1) Collecting and cleaning data, using dataset of maintenance and reliability. Data should be structured and prepared, including labeled variables.
- 2) Identifying failures as Event (=1) and proceeding to calculation of Proxy\_RUL using the given date of failure. from the operator-reported failure dates, after segmenting the signal into operating cycles delimited by successive events (see Section 3)
- 3) Model training using reduced variables based on statistical ML models and ML models with all variables.
- 4) Prediction generation and accuracy evaluation using a chronological 80% / 20% train-test split that preserves temporal order.
- 5) Step 5 concerns the reliability study of the proposed models using several months to enhance prediction evaluation.

![](_page_6_Figure_9.jpeg)

Figure 2. The proposed research framework

#### 3. Case study:

#### Context and available data

Monitoring the condition of railway equipment is crucial for ensuring service continuity, system safety, and controlled maintenance costs. Air compressors, in particular, play a critical role in onboard air production units, used for essential functions such as door opening and closing, braking systems, and general pneumatic regulation. Their failure can cause unplanned shutdowns and disrupt train operations, justifying the use of advanced, data-driven maintenance approaches.

#### • Dataset used:

The MetroPT-3 dataset was created as part of run-to-failure industrial experiments conducted on an air compressor installed in a Porto metro train in Portugal. It is a multivariate dataset combining signals from analog and digital sensors, captured directly from an onboard device. Unlike synthetic datasets, this dataset reflects the real-world variability of industrial environments: noisy signals, intermittent operating regimes, and non-stationary operating conditions (Ribeiro et al., 2020). The available measurements cover several physical and logical quantities related to the compressor's condition and operation. The main categories of variables are:

- Pressure Sensors (Pneumatic)

TP2, TP3, H1, DVP, Reservoirs: air pressures measured at different points in the pneumatic system, expressed in bar. These signals allow monitoring the compression and air supply dynamics of the circuits.

- Thermal Sensors: Oil\_temperature: temperature of the compressor's lubricating oil, in °C, useful for detecting overheating, often associated with wear or lubrication problems.
- Electrical Sensors: Motor\_current: current drawn by the compressor motor, in amperes (A). An increase in current may indicate excessive mechanical stress, increased friction, or the beginning of internal damage.
- Logic (digital) sensors
- COMP: Compressor status (1 = ON, 0 = OFF), essential for identifying actual operating events.
- DV\_electronic, Pressure\_switch, Oil\_level, Towers, MPG, LPS, Oil\_level, Caudal\_impulses: Digital or pulse signals indicating component activation, oil presence, or pulses related to airflow.

These variables allow us to study both the influence of covariates on failure risk (through Cox PH) and the temporal evolution of degradation (via ANN and RF) within a causal framework.

#### • Failure event and Proxy RUL

The original dataset was recorded at 1 Hz (one measurement per second) over several months in 2020, representing a total volume of over 1 million rows. For testing and exploratory analysis purposes compatible with standard modeling tools, a reduced version of the dataset was used here, containing 65536 time-rows, each corresponding to a measurement point where the sensor signals are complete and usable. The importance of the used dataset in the railway sector is significant. The MetroPT-3 dataset offers a rich foundation for predictive maintenance research thanks to:

- the diversity of sensor signals (pneumatic, thermal, and electrical),
- the presence of a logic operating sensor (such as COMP),

- and a sufficient data volume, even in its reduced version, to test the influence of variables on the occurrence of a degradation event, compare statistical and ML models, or estimate a RUL proxy in a causal framework.

Failure Information: Although the dataset itself is unlabeled, the labelling procedure is as follows. First, each reported failure date is mapped to the nearest record in the time-ordered series, marking that record as an event (Event = 1), all other records are non-events (Event = 0). Second, the series is segmented into operating cycles, each cycle being delimited by two successive failure/maintenance events. Third, within every cycle the proxy RUL at time t is defined as the number of time steps remaining until the next event, i.e. Proxy\_RUL(t) = t\_event-t, and is reset to its maximum value immediately after each event.

Avoiding data leakage. Because the proxy RUL at time t depends only on the timestamp of the next event and never on future sensor readings, no future information is injected into the input features. All chronological ordering is preserved: the train-test split is performed on time (the first 80% of records for training, the last 20% for testing), so the model is always evaluated on records that occur strictly after those used for fitting. Feature scaling parameters are estimated on the training partition only and then applied to the test partition, preventing statistics of the test period from influencing training. Records straddling a cycle boundary are assigned to the cycle of their timestamp, so no label spans the train-test frontier.

#### • Rationale and limitations of the proxy RUL

Conventional RUL is defined against a physically measured degradation variable (e.g. crack length, bearing spall, or a calibrated health index) and decreases monotonically toward a known end-of-life threshold. Such a ground-truth degradation signal is not available in MetroPT-3. The proxy RUL adopted here instead approximates remaining life purely from the time elapsed to the next documented event. It therefore differs from conventional RUL in three ways:

- it is time-based rather than damage-based, so it assumes a roughly uniform progression toward failure within a cycle, it is cyclic and discontinuous, being reset after every maintenance action, which produces abrupt jumps rather than a smooth monotonic decay, and it is non-stationary across cycles of different lengths. Consequently, the proxy RUL should be read as a relative temporal risk indicator rather than an exact physical measure of the system's state. These properties, particularly the post-maintenance resets, make continuous regression intrinsically harder and partly explain the low determination coefficients reported in Section 4 for models that assume smooth temporal dynamics.

#### Experimental setup

Preprocessing. Records with missing or out-of-range sensor values were discarded, and the retained signals were kept in their native physical units. Continuous features were standardized (zero mean, unit variance); the scaler was fitted exclusively on the training partition and then applied to the test partition to avoid leakage. Digital logic signals were kept as binary indicators. Train test split. A single, consistent chronological split of 80% for training and 20% for testing is used throughout this study, the temporal order of the records is preserved (no shuffling), so every test record post-dates every training record. This point is emphasized because it governs both the

classification and the regression experiments and removes the split-ratio inconsistency. Hyperparameter selection. Hyperparameters were tuned by time-series (forward-chaining) cross-validation on the training partition only. Random Forest and XGBoost were tuned over the number of trees, maximum depth, and learning rate (XGBoost), the ANN (MLP) over the number and width of hidden layers, activation, and learning rate, and the LSTM over the number of units, sequence window length, dropout, and batch size, trained with the Adam optimizer and early stopping on a temporal validation fold. The configuration achieving the best validation score was then evaluated once on the untouched test partition.

Evaluation. For failure-event classification, models are assessed with accuracy, ROC-AUC, PR-AUC, F1, precision, sensitivity (recall), and specificity; sensitivity and specificity are emphasized because they map directly onto missed-failure and false-alarm rates in maintenance practice. For proxy RUL regression, models are assessed with MAE, RMSE, and R<sup>2</sup>.

#### • Variable reduction using Cox-PH

The comparison between the two approaches clearly highlights that Cox-PH is better suited than PCA for identifying and weighting critical variables related to failure events. While PCA distributes importance almost uniformly and independently of the phenomenon being studied, the Cox model highlights a limited number of key variables that are statistically significant and physically interpretable. This ability to directly link variables to failure mechanisms explains the superior performance subsequently observed in predicting events and Proxy\_RUL. In practice, these results justify the use of the Cox-PH model as a tool for supervised variable selection in predictive maintenance, particularly in hybrid approaches combining explainability and predictive performance.

|   | Variable        | Z            | p_value     | -log2(p)    | Weight_% |
|---|-----------------|--------------|-------------|-------------|----------|
| • | Oil_temperature | 23,17164695  | 8,7973E-119 | 392,1723891 | 29,65    |
| • | DV_pressure     | -13,74186546 | 5,69883E-43 | 140,3322431 | 17,48    |
| • | Reservoirs      | -12,62387576 | 1,55953E-36 | 118,9483023 | 17,17    |
| • | TP3             | -12,54924088 | 4,01339E-36 | 117,5845899 | 17,07    |
| • | Motor_current   | 6,563964588  | 5,23956E-11 | 34,15176201 | 8,82     |
| • | H1              | -4,01283204  | 5,99946E-05 | 14,02480776 | 5,49     |
| • | TP2             | 3,138010715  | 0,001700987 | 9,199412521 | 4,31     |

Table 1. Metrics of relative contribution of variables using Cox-PH Model for Event

| Variable        | PCA_weight_% |
|-----------------|--------------|
| • H1            | 7,78         |
| Oil_temperature | 7,68         |
| Motor_current   | 7,39         |
| DV_eletriconic  | 7,26         |
| • Towers        | 7,21         |
| • TP2           | 7,11         |
| • COMP          | 7,05         |
| • MPG           | 7,04         |
| • DV_pressure   | 6,47         |

| • TP3                          | 6,13 |
|--------------------------------|------|
| <ul> <li>Reservoirs</li> </ul> | 6,12 |
| • Caudal_impulses              | 6,11 |
| • LPS                          | 5,81 |
| Oil_level                      | 5,66 |
| Pressure_switch                | 5,20 |

Table 2. Metrics of relative contribution of variables using PCA Model for Event

#### • Accuracy of statistical models

The results presented in Table 3 demonstrate a clear superiority of the Cox proportional hazards model approach over PCA dimensionality reduction for predicting failure events. With the same number of variables used (7), the Cox-PH model achieves an accuracy of 0.96 and an AUC of 0.974, compared to 0.94 and 0.941, respectively, for the PCA approach. The difference is even more pronounced in the F1 score, with a value of 0.770 for Cox-PH versus 0.599 for PCA, reflecting a significantly better ability to balance failure detection and false alarm control. These results indicate that variable selection guided by failure hazard (Cox-PH) is more relevant than purely statistical PCA dimensionality reduction, which maximizes the explained variance without considering the direct link to the failure event.

| Method | Features_used | Accuracy | AUC   | F1    |
|--------|---------------|----------|-------|-------|
| Cox-PH | 7             | 0,96     | 0,974 | 0,770 |
| PCA    | 7             | 0,94     | 0,941 | 0,599 |

Table 3. Comparison between Cox-PH and PCA for Event

Table 4 confirms the superiority of the Cox-PH approach for predicting Proxy\_RUL, with significantly lower regression errors and higher explanatory power than PCA. The Cox-PH model achieves an MAE of  $5.83 \times 10^5$  and an RMSE of  $8.44 \times 10^5$ , compared to  $7.65 \times 10^5$  and  $1.07 \times 10^6$  for the PCA approach, while the coefficient of determination increases from 0.69 to 0.81. This improvement is explained by the ability of the Cox model to select variables directly related to failure dynamics and the system's temporal evolution, unlike PCA, which prioritizes overall variance without guaranteeing relevance to functional degradation.

| Method | Features_used | MAE         | RMSE        | R2   |
|--------|---------------|-------------|-------------|------|
| Cox-PH | 7             | 583407,7132 | 843998,4589 | 0,81 |
| PCA    | 7             | 764853,9547 | 1066066,905 | 0,69 |

Table 4. Comparison between Cox-PH and PCA for Proxy RUL

In this work, a Cox proportional-hazards survival model was applied to identify the variables most strongly associated with failure risk, using operating time (elapsed cycles) as the time scale and the occurrence of a reported failure as the event. The model shows good discriminatory power, with a concordance index (C-index) of 0.79, confirming the relevance of the adopted approach. The relative-contribution analysis reported in Table 1 identifies oil temperature as the dominant degradation factor (weight  $\approx 29.7\%$ ), significantly increasing the risk of failure, followed by the DV valve pressure, reservoir pressure, and TP3 pressure, which each carry a significant but more moderate effect (weights  $\approx 17\%$ ). The remaining significant sensors motor current, H1, and TP2 contribute more marginally, whereas the low-variance digital signals show no statistically

significant impact once the dominant thermal and pneumatic effects are accounted for. These MetroPT-3 covariates replace the generic variables mentioned in earlier drafts, which did not belong to this dataset

These results allow us to reduce the set of variables in a justified and interpretable way, and constituting a solid basis for the rest of the study, which consists of integrating these weighting variables into failure prediction models and proxy RUL, comparing direct ML approaches with hybrid Cox + ML approaches.

The Cox-PH criterion ranks variables by their association with the instantaneous hazard, i.e. by how sharply they discriminate the moment a failure becomes likely. For the discrete event-detection task this is exactly the right signal, so an aggressive reduction to a handful of high-hazard variables retains almost all of the useful discriminative information (Tables 3 and 5). Continuous proxy RUL regression, however, must reconstruct a full temporal trajectory, not just the neighbourhood of the event, it therefore benefits from lower-hazard variables that still carry variance about the system's slow evolution across a cycle. Discarding these variables removes information that is weakly linked to the instantaneous risk but useful for regression, which is why the reduced-variable scenario degrades proxy RUL accuracy (Table 6) even though it preserves event-detection accuracy. In short, hazard-relevance and regression-relevance are not the same objective, and Cox-guided selection is aligned with the former

#### 4. Prediction accuracy of failures and RUL:

The prediction study aims to highlight the prediction of Event and RUL failures by comparing two scenarios with four predictive models using Cox-PH and reliable metrics such as Sensitivity (Recall), which measures the ability to correctly detect events (failures), and Specificity, which indicates the model's ability to avoid false alarms. The latter two metrics are more relevant to maintenance engineers than F1, although the latter remains important for data science.

#### • Failure prediction

The failure event prediction results clearly demonstrate the superiority of models capable of capturing the temporal dynamics of signals, particularly the LSTM model. With the full set of sensor variables, the LSTM achieves the best overall performance, with a ROC-AUC of 0.96, a sensitivity greater than 92%, and a specificity close to 94%, indicating both excellent impending failure detection capabilities and strong control of false alarms (Table 5).

A particularly noteworthy result is that even when limited to four key variables selected by the Cox proportional hazards model (oil temperature, DV valve pressure, tank levels, and TP3 temperature), the LSTM maintains performance very close to that obtained with the full sensor set. For clarity, the Cox-PH versus PCA comparison in Tables 3 and 4 uses the seven statistically significant Cox variables, whereas the reduced-variable scenario in Tables 5 and 6 uses the four dominant ones both are drawn from the same Cox ranking in Table 1

This observation confirms that the Cox model plays a crucial role as a supervised mechanism for selecting variables related to failure risk, while the LSTM effectively leverages the remaining temporal information to ensure reliable prediction. Thus, the hybrid Cox-LSTM approach appears as an optimal compromise between predictive performance, interpretability and reduction of

instrumental complexity.

| Option              | Model   | Accuracy | ROC   | PR    | F1    | Precision | Sensitivity | Specificity |
|---------------------|---------|----------|-------|-------|-------|-----------|-------------|-------------|
|                     |         |          | AUC   | AUC   |       |           | Recall      |             |
| 1 D . 1 1           | LSTM    | 0,937    | 0,945 | 0,532 | 0,653 | 0,506     | 0,923       | 0,937       |
| 1.Reduced Variables | XGBOOST | 0,723    | 0,869 | 0,520 | 0,283 | 0,171     | 0,820       | 0,716       |
| v arrabics          | RF      | 0,752    | 0,823 | 0,469 | 0,278 | 0,173     | 0,717       | 0,754       |
|                     | ANN_MLP | 0,756    | 0,817 | 0,447 | 0,267 | 0,167     | 0,666       | 0,763       |
|                     | LSTM    | 0,945    | 0,961 | 0,702 | 0,692 | 0,543     | 0,951       | 0,945       |
| 2.Full              |         |          |       |       |       |           |             |             |
| Variables           | XGBOOST | 0,789    | 0,918 | 0,593 | 0,356 | 0,224     | 0,874       | 0,783       |
|                     | RF      | 0,786    | 0,902 | 0,569 | 0,346 | 0,217     | 0,847       | 0,781       |
|                     | ANN_MLP | 0,673    | 0,867 | 0,497 | 0,266 | 0,157     | 0,888       | 0,657       |

Table 5. Metrics for failure prediction options

#### • RUL prediction:

The Proxy\_RUL was calculated as the time remaining before the next failure or maintenance event, using only the temporal information available in the dataset. The data was first segmented into operating cycles, each cycle being delimited by two successive events. At each time t, the Proxy\_RUL is defined as the difference between the time of the next event and the current time, and is then reset after each maintenance. This Proxy\_RUL thus constitutes an artificial, cyclic, and non-stationary variable, intended to approximate the notion of remaining lifetime in the absence of an actual measurement of degradation, and should be interpreted as a relative temporal indicator rather than as an exact physical measure of the system's state.

Regarding the prediction of RUL, see table 6, the results highlight significantly different behaviors compared to those observed for event detection. Random Forest and XGBoost models prove to be the most effective, particularly when trained on the full set of sensor variables, with a coefficient of determination (R<sup>2</sup>) reaching approximately 0.40 for XGBoost. Conversely, reducing the number of variables to those from the Cox model leads to a notable degradation in regression performance, suggesting that continuous RUL estimation requires richer information than that strictly related to the instantaneous risk of failure.

Furthermore, LSTM models applied to RUL prediction exhibit insufficient performance, with low or even negative R<sup>2</sup> values. This can be explained by the very nature of the proxy RUL used, characterized by abrupt resets after maintenance and strong non-stationarity. These results indicate that, in the context studied, nonlinear tree-based machine learning models constitute a more robust solution for RUL estimation, while deep learning is particularly relevant for predicting discrete failure events.

| Option    | Model   | MAE     | RMSE    | R2    |
|-----------|---------|---------|---------|-------|
|           | XGBOOST | 1847130 | 2235120 | 0,20  |
| 1.Reduced | RF      | 1875722 | 2423773 | 0,06  |
| Variables | ANN_MLP | 2248489 | 2482115 | 0,02  |
|           | LSTM    | 3492326 | 4300548 | -1,94 |
|           | XGBOOST | 1443419 | 1946967 | 0,40  |

| 2.Full Variables | RF      | 1386594 | 1994224 | 0,37  |
|------------------|---------|---------|---------|-------|
| Scenario         | ANN_MLP | 1877845 | 2250545 | 0,19  |
|                  | LSTM    | 3492323 | 4300546 | -1,94 |

Table 6. Metrics for Proxy-RUL prediction options

A low or negative coefficient of determination R<sup>2</sup> observed during RUL prediction does not indicate a failure of the models used, but rather results primarily from the intrinsic characteristics of the target variable and the industrial context studied. The non-stationarity of the data, linked to the presence of multiple heterogeneous maintenance cycles, prevents the establishment of a global and stable relationship between the sensor variables and the remaining service life. This difficulty is exacerbated in the case of sequential models such as LSTMs, whose principle is based on learning continuous temporal dynamics, whereas the proxy RUL exhibits abrupt discontinuities due to post-maintenance resets. Under these conditions, classical regression metrics, particularly R<sup>2</sup>, become poorly suited for evaluating the actual performance of the models and should be interpreted with caution in favor of more robust indicators or a reformulation of the problem.

#### • Practical implications for railway compressor maintenance

The framework outputs two complementary signals that map directly onto maintenance decisions. The failure-event model produces a per-record failure probability that can drive a two-level alarm policy a lower threshold that raises an early advisory (increased inspection frequency) and a higher threshold that triggers an intervention request. Because maintenance engineers care most about missed failures and false alarms, the operating threshold can be chosen on the sensitivity specificity trade-off rather than on F1 for example, favouring the high-sensitivity full-variable LSTM (sensitivity  $\approx 0.95$ , specificity  $\approx 0.95$ ) when the cost of an undetected compressor failure is high. The proxy RUL model, in turn, provides a relative time-to-event estimate that can be used to rank assets and to open maintenance windows a shrinking proxy RUL flags units that should be scheduled sooner, supporting spare-part staging and crew planning. In deployment, the Cox-PH weights also give technicians an interpretable shortlist of the sensors (oil temperature, DV pressure, reservoir pressure, TP3) that most warrant monitoring, which lowers instrumentation and data-collection cost. Given the non-stationarity of the proxy RUL, we recommend using it as a prioritization indicator combined with the failure-probability alarm rather than as a hard countdown to failure.

#### 5. Conclusion

Predictive maintenance or PdM has emerged as one of the most transformative strategies in modern industry. Unlike reactive maintenance, where equipment is repaired after a breakdown, or preventive maintenance, which follows fixed schedules regardless of machine condition, predictive maintenance relies, on data analytics and real-time monitoring, to forecast failures before they occur.

Predicting failures and remaining lifespan or Proxy\_RUL is a major challenge in predictive maintenance, but these two objectives involve different types of problems and require appropriate modeling strategies. The results show that machine learning and deep learning models used alone can offer good predictive performance, particularly for detecting failure events, but at the cost of poor interpretability and increased dependence on a large number of variables. Conversely, hybrid

approaches incorporating explanatory models such as the Cox proportional hazards model make it possible to identify the variables truly linked to failure risk and improve the robustness and readability of downstream predictive models.

In the case of failure prediction, the combination of supervised variable selection using Cox-PH and advanced models, particularly sequential architectures such as LSTM, offers an optimal compromise between performance, interpretability, and reduced complexity. For proxy RUL prediction, however, strict hybrid approaches based on a high reduction of variables can lead to information loss, and nonlinear machine learning models such as Random Forest or XGBoost, applied to all sensors, prove to be more robust. Thus, the main advantage of hybrid models lies less in replacing machine learning or deep learning methods than in their complementarity, providing a structured approach to the problem, improved explainability, and a better fit for real-world industrial constraints.

Future work could examine the possibility of adding data augmentation to create a large dataset to evaluate data reliability and subsequently assess the accuracy of ML/DL prediction models.

#### **References:**

- Basora, L., Bry, P., Olive, X., Freeman, F., Aircraft fleet health monitoring with anomaly detection techniques, Aerospace 8, 2021.
- Breiman, L., Random forests, https://www.stat.berkeley.edu/~breiman/randomforest2001.pdf, 2001.
- Ding, S.H. et al., Maintenance strategy optimization, literature review and directions, Int. J. Adv. Manuf. Technol., 2014.
- Florian, E., Sgarbossa, F., Zennaro, I., Machine learning-based predictive maintenance: A cost-oriented model for implementation, International Journal of Production Economics, Volume 236, 2021.
- Godoy, D. R., Álvarez, V., Mena, R., Viveros, P., and Kristjanpoller, F., « Adopting New Machine Learning Approaches on Cox's Partial Likelihood Parameter Estimation for Predictive Maintenance Decisions », Machines, vol. 12, no 1, Art. no 1, 2024.
- Lee, J., M. Holgado, M., Kao, H., Macchi, M., New Thinking Paradigm for Maintenance Innovation Design, IFAC Proceedings, Volume 47, Issue 3, Pages 7104-7109, 2014.
- Lei, Y., Yang, B., Jiang, X., Jia, F., Li, N. and Nandi, A.K. (2020). 'Applications of machine learning to machine fault diagnosis: A review and roadmap', Mechanical Systems and Signal Processing, 138, p. 106587. doi.org.
- Li, J., Li, X. and He, D. (2019). 'A directed acyclic graph network combined with CNN and LSTM for remaining useful life prediction', Journal of Manufacturing Systems, 52, pp. 15-27. doi.org.
- Malawade, A.V., Costa, N.D., Muthirayan, D., Khargonekar, P.P., Al Faruque, M.A., Neuroscience-inspired algorithms for the predictive maintenance of manufacturing system IEEE Trans. Ind. Inform. 17, 12, 2021.
- Meddaoui, A., Hachmoud, A., Hain, M., Advanced ML for predictive maintenance: a case study on remaining useful life prediction and reliability enhancement, The

- International Journal of Advanced Manufacturing Technology, Published: 11 March 2024, Volume 132, pages 323–335, (2024).
- Narayan, K., B., Mishra, K.A., Rakesh, K. S., Sawmliana, C., Singh, P.K., Application of logistic regression, CART and random forest techniques in prediction of blast-induced slope failure during reconstruction of railway rock-cut slopes, Engineering Failure Analysis, 106-230, 2022.
- Ning, S., Sun, J., Liu, C., Yi, Y., Applications of deep learning in big data analytics for aircraft complex system anomaly detection, Proc. Inst. Mech. Eng. O 235 (5), 923–940, 2021.
- Ribeiro, M. and Guedes, K. (2020). MetroPT Predictive Maintenance Dataset. UCI Machine Learning Repository. https://doi.org/10.24432/C5VW3R
- Safoklova, B., Prokopenkoa, D., Deniskina, Y., Kostyshakb, M., Model of aircraft maintenance repair and overhaul using artificial neural networks, Transportation Research Procedia 63, 1534–1543, 2022.
- Si, X.-S., Wang, W., Hu, C.-H., and Zhou, D.-H., « Remaining useful life estimation A review on the statistical data driven approaches », European Journal of Operational Research, vol. 213, no 1, p. 1-14, 2011.
- Wang, H., Zhang, W., Yang, D., Xiang, Y., Deep-learning-enabled predictive maintenance in industrial internet of things: Methods, applications, and challenges, IEEE Syst. J., 2022.
- Zhang, H., et al., « Parameter estimation of three-parameter Weibull probability model based on outlier detection », RSC Advances, vol. 12, no 53, p. 34154-34164, 2022.
- Zhang, J., Wang, P., Yan, R. and Gao, R.X. (2018). 'Deep learning for smart manufacturing: Methods and applications', Journal of Manufacturing Systems, 48, pp. 144-156. doi.org.

## **Statements & Declarations ETHICAL APPROVAL:**

This study uses exclusively publicly available and anonymized data. No formal ethical approval is required for this type of research. Informed consent is not applicable.

#### Funding:

The authors declare that no funds, grants, or other support were received during the preparation of this manuscript.

#### Data availability:

The datasets generated and analysed during the current study are available in the UCI repository. The dataset was introduced by Ribeiro, M. and Guedes, K. (2020) on behalf of a transportation and train company based in Portugal. DOI: https://doi.org/10.24432/C5VW3R

Web Link of the dataset: https://archive.ics.uci.edu/dataset/791/metropt+3+dataset

#### **Conflicts of Interest:**

Authors of this paper have no financial interests and have no relevant financial or conflicts of interest to disclose.

#### **Author Contributions:**

All authors contributed to the study conception and design. Material preparation, data collection and analysis were performed by Meddaoui Anwar. The first draft of the manuscript was written by Mr. Hamdi

Alaoui. A and Prof. Meddaoui and revised by Prof. Hachmoud. A commented on previous versions of the manuscript. All authors read and approved the final manuscript.

![](_page_16_Picture_2.jpeg)
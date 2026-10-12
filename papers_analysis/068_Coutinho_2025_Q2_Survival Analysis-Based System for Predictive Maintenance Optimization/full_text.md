#### **ORIGINAL RESEARCH**

![](_page_0_Picture_2.jpeg)

![](_page_0_Picture_3.jpeg)

# **Survival Analysis‑Based System for Predictive Maintenance Optimization**

**Beatriz Coutinho1  [·](http://orcid.org/0000-0003-3893-3845) Margarida Moreira1 · Eliseu Pereira1 · Gil Gonçalves1**

Received: 9 May 2025 / Accepted: 8 August 2025 © The Author(s) 2025

#### **Abstract**

The adoption of predictive maintenance (PdM) in Industry 4.0 has become essential for optimizing operational efciency and reducing downtime. Traditional maintenance approaches, such as reactive and preventive maintenance, often result in inefciencies, highlighting the need for more proactive and data-driven strategies. This paper presents a modular PdM framework that uses survival analysis methods to estimate the remaining useful life (RUL) of industrial components and integrates a Simulated Annealing (SA)-based optimization algorithm to schedule maintenance interventions dynamically. Four survival models—Cox Proportional Hazards (Cox PH), Random Survival Forests (RSF), Gradient Boosting Survival Analysis (GBSA), and Survival Support Vector Machines (Survival SVM)—were evaluated to predict components' failure, with GBSA emerging as the most robust model due to its resistance to overftting and ability to capture non-linear degradation patterns. The maintenance scheduling optimization algorithm minimizes downtime by aligning maintenance windows with non-linear degradation/survival functions and production requirements, achieving a 25% reduction in downtime compared to non-optimized methods. The framework was validated on real-world welding electrode degradation data and a synthetic Microsoft Azure PdM dataset, demonstrating its adaptability to heterogeneous industrial environments. Unifying survival analysis with production-aware scheduling optimization enabled cost-efective, risk-informed decision-making for Industry 4.0 applications.

**Keywords** Maintenance scheduling optimization · Remaining useful life · Survival analysis · Predictive maintenance

## **Introduction**

Nowadays, manufacturing industries channel an important part of their eforts to efectively maintain equipment components, ensuring efcient operations and reducing costs. Traditional maintenance approaches, often reactive or time-based, have limitations in terms of cost efciency and operational efectiveness. For example, reactive maintenance can cause unexpected downtime and high repair

\* Beatriz Coutinho beatrizbguichard@fe.up.pt

> Margarida Moreira up201905217@edu.fe.up.pt

Eliseu Pereira eliseu@fe.up.pt

Gil Gonçalves gil@fe.up.pt

<sup>1</sup> SYSTEC ARISE, Faculdade de Engenharia, Universidade do Porto, Rua Dr. Roberto Frias, 4200-465 Porto, Portugal costs, while preventive maintenance may result in overmaintenance, creating unnecessary expenses. Consequently, traditional maintenance strategies, such as reactive and preventive approaches, remain costly and inefcient, resulting in between 15% to 60% of total manufacturing operating costs [\[1](#page-15-0)]. Therefore, there is a strong need for more proactive approaches to optimize maintenance schedules, reduce costs, and improve equipment production time [[2,](#page-15-1) [3\]](#page-15-2).

The maintenance strategies were transformed with the integration of Industry 4.0 technologies (e.g., Internet of Things (IoT) sensors, Artifcial Intelligence (AI)), leading to the rise of more proactive and data-driven techniques. Adopting those technologies leads industries to adopt predictive maintenance (PdM) strategies, heavily reliant on data analytics and AI-based methods to predict component failures before they occur, enabling timely and cost-efective interventions. Existing PdM systems often decouple remaining useful life (RUL) prediction from scheduling optimization, using deterministic failure thresholds that overlook the probabilistic nature of component degradation [[4\]](#page-15-3). Survival 766 Page 2 of 17 SN Computer Science (2025) 6:766

analysis methods provide robust estimates of time-to-failure (TTF) distributions (e.g., Fig. [2](#page-2-0)), facilitating their integration with maintenance schedule optimization algorithms. Integrating survival functions (which capture TTF uncertainty) with production-aware optimization remains a critical gap. Current frameworks fail to align maintenance windows with non-linear degradation trends or overlapping production constraints, limiting their practicality in real-world scenarios.

This paper presents the implementation of a modular and data-driven PdM framework that employs survival analysis methods to estimate the RUL of industrial components. The framework incorporates models such as the Cox Proportional Hazards Model (Cox PH), Random Survival Forest (RSF), Gradient Boosting Survival Analysis (GBSA), and Survival Support Vector Machines (SVM). Based on the resulting TTF distribution/survival function, a simulation and optimization algorithm based on Simulated Annealing (SA) determines the optimal maintenance schedule according to user-defned production requirements, which minimizes production downtime. The main contributions of this work include:

- Implementation of survival analysis methods for PdM applications, integrating censored data and enabling dynamic maintenance scheduling that adapts to nonlinear degradation patterns and probabilistic survival functions.
- Development of a simulation-based approach for longterm production planning optimization, using survival functions instead of fxed degradation rates to model component degradation over time. By strategically clustering interventions, the framework reduced downtime by 25% when compared to non-optimized PdM methods.
- Evaluation using two industrial datasets (real-world spot welding electrodes and synthetic Microsoft Azure PdM dataset), demonstrating the framework's adaptability to heterogeneous degradation behaviors.

The paper is organized as follows: Sect. "[Literature Review"](#page-1-0) presents the literature review, Sect. "[Methodology](#page-6-0)" details the system architecture, Sect. ["Implementation"](#page-7-0) details the implementation, Sect. ["Results and Discussion"](#page-10-0) discusses the main results, and Sect. ["Conclusions and Future Work"](#page-13-0) provides conclusions and future work directions.

# <span id="page-1-0"></span>**Literature Review**

This literature review provides an overview of the methodologies employed for implementing industrial maintenance modules. It begins by examining the diferent types of industrial maintenance before narrowing the focus to PdM approaches. The review then discusses RUL estimation, followed by exploring survival analysis techniques. Next, the impact of maintenance scheduling optimization on PdM systems is studied. The section concludes with a gap analysis, identifying areas for further development based on the studies reviewed.

#### **Industrial Maintenance**

A study by [[5\]](#page-15-4) estimated that maintenance accounts for 15% to 60% of total manufacturing operating costs. Such high costs can impact a company's fnancial viability. Therefore, having clear maintenance strategies is essential to reducing costs and keeping operations efcient. In today's industry, maintenance strategies can be classifed into three main types [\[6](#page-15-5)]:

- **Reactive Maintenance:** Equipment is repaired only after a failure occurs, without any prior planning or strategy. While simple to implement, this approach can lead to unplanned downtime and costly repairs.
- **Preventive Maintenance:** Scheduled maintenance performed at regular intervals to reduce the risk of equipment failure. Although this approach minimizes unexpected breakdowns, it can lead to over-maintenance, increasing costs by replacing components more often than necessary.
- **Predictive Maintenance:** A data-driven approach that uses real-time monitoring, AI, and sensor technology to predict failures before they occur. PdM aims to optimize maintenance schedules, reduce costs, and improve equipment production time. It has gained popularity, especially given the rise of Industry 4.0, due to its efciency compared to traditional methods.

More recently, proactive maintenance has emerged as the latest step in the evolution of maintenance strategies. It focuses on fnding and fxing the root causes of failures before they occur, improving long-term reliability and efciency [[7](#page-15-6)].

#### **Predictive Maintenance Approaches**

PdM's primary concept is its ability to generate scheduled maintenance actions based on equipment performance or condition over time, using the available data [[5\]](#page-15-4). A typical PdM system consists of condition monitoring, where data is continuously collected and analyzed; predictive modeling, which anticipates potential failures; decision-making and maintenance scheduling, where an optimal maintenance schedule is determined based on predictive modeling; and reporting, which informs users of the results and enables the required maintenance intervention, as illustrated in Fig. [1.](#page-2-1)

SN Computer Science (2025) 6:766 Page 3 of 17 766

<span id="page-2-1"></span>![](_page_2_Figure_1.jpeg)

![](_page_2_Picture_2.jpeg)

![](_page_2_Figure_3.jpeg)

<span id="page-2-0"></span>**Fig. 2** Survival analysis curve example [[13](#page-15-11)]

Predictive modeling techniques in PdM can be categorized into three main approaches [\[5\]](#page-15-4):

- **Physical Model-based Approaches**: Rely on mathematical modeling to refect the condition of a component, requiring precise measurements of its state and failure indices. Statistical methods are often used to establish limits for these indices.
- **Knowledge-based Approaches**: Simplify complex physical models and are often employed as hybrid strategies [[8\]](#page-15-7). Examples include expert systems and fuzzy logic.
- **Data-driven Approaches**: The most commonly used models in modern PdM solutions, which rely on historical data analysis, pattern recognition, and AI, including machine learning (ML) algorithms.

#### **Remaining Useful Life**

For the predictive aspect of PdM, many studies focus on estimating the RUL [[5](#page-15-4)], as it is a critical parameter for efectively scheduling maintenance [[4](#page-15-3)]. Estimating the RUL typically involves predicting the TTF using predictive models and then determining the best maintenance window to prevent unexpected breakdowns.

To estimate the RUL, several methodological approaches have been explored, including physics-based, experimental, data-driven, and hybrid techniques [[9](#page-15-8)]. Among these, data-driven ML approaches are increasingly preferred due to their ability to operate with minimal historical data, lower computational complexity, and greater cost-efectiveness compared to statistical or probabilistic methods [\[4\]](#page-15-3). Some of the ML methods used in the literature for RUL estimation include Random Forest (RF), XGBoost (XGB), Multilayer Perceptron (MLP), XGBoost, Long Short-Term Memory Networks (LSTM), Convolutional Neural Network (CNNs), Support Vector Regression (SVR), and Artifcial Neural Networks (ANN) [\[5,](#page-15-4) [10–](#page-15-9)[12](#page-15-10)].

#### **Survival Analysis**

Survival analysis is a statistical subfeld focused on modeling time-to-event data, helping to describe the length of time from a time origin to an endpoint of interest [[13,](#page-15-11) [14](#page-15-12)]. The survival function *S*(*t*) describes the probability that a system or component will survive beyond a certain time *t*, and can be expressed as [\[15\]](#page-15-13):

$$S(t) = P(T > t) = 1 - F(t)$$
 (1)

Here, *S*(*t*) represents the survival probability, and *T* is the number of cycles until the component fails. *F*(*t*) represents the cumulative distribution function (CDF) of the failure time *T*, which gives the probability that the component has failed by time *t*.

Figure [2](#page-2-0) illustrates a survival analysis curve. The horizontal axis represents time, while the vertical axis shows the estimated probability of survival. For example, assuming this curve relates to an industrial machine, it can be deduced that after 3000 days, the machine has less than a 50% probability of still functioning properly.

766 Page 4 of 17 SN Computer Science (2025) 6:766

Survival analysis is commonly used in the medical feld, where it plays an essential role in estimating a patient's survival time following a diagnosis of a disease. Although some researchers have explored survival analysis approaches for estimating the RUL of industrial components, its application in PdM and Industry 4.0 is still far from being as widespread or advanced as it is in the medical feld [[16–](#page-15-14)[18](#page-16-0)]. Despite this, RUL estimation through survival analysis has signifcant potential, as it can explicitly model the time until a component fails, thereby facilitating maintenance scheduling and resource optimization [[17\]](#page-15-15).

#### **Survival Analysis Methods**

Survival analysis methods are mainly classifed into two categories: statistical methods and machine learning (ML) based methods. Statistical methods are based on traditional mathematical models, while ML-based methods adapt existing ML techniques to handle survival data [[14\]](#page-15-12).

## • **Statistical Methods:**

- **Non-Parametric Methods:** Methods like the Kaplan-Meier estimator that make no assumptions about the distribution of the data. These methods are particularly useful when dealing with incomplete data.
- **Semi-Parametric Methods:** Models such as the Cox Proportional Hazards model analyze the efect of covariates on survival times without assuming a specifc distribution for the data.
- **Parametric Methods:** These methods assume the data follows a known distribution. They are most efective when the data aligns with the chosen distribution. Examples include the Tobit or the Buckley-James method.

## • **Machine Learning-Based Methods:**

- **Survival Trees:** Decision Trees (DT) adapted to predict survival outcomes based on splitting data using diferent factors.
- **Artificial Neural Networks (ANN):** ANNs are applied for complex pattern recognition and prediction of survival outcomes.
- **Advanced Machine Learning Approaches:** These include ensemble learning techniques like Bagging Survival Trees, Random Survival Forests, and Boosting, as well as methods like active learning, transfer learning, and multitask learning.

Figure [3](#page-4-0) shows a complete taxonomy of survival analysis methods [\[14](#page-15-12)].

Various performance metrics are used to evaluate the efectiveness of survival models. Some of the most common include the Concordance Index (C-index), Brier Score, and the Mean Absolute Error (MAE) [\[14](#page-15-12), [19](#page-16-1)].

## **Maintenance Scheduling Optimization**

PdM implementations are often integrated into systems that ofer additional functionalities beyond component lifetime prediction. These systems may also incorporate optimization and simulation models to enhance maintenance planning.

For instance, in the work of [[20\]](#page-16-2), a system was developed that integrates PdM with optimization and simulation modules. Beyond simply predicting component failures, the system uses a Genetic Algorithm (GA) to adjust maintenance schedules based on production targets and machine degradation. Similarly, in [\[12](#page-15-10)], a mixed-integer linear programming (MILP) model was developed to optimize aircraft engine maintenance scheduling, aiming to minimize the maximum maintenance time.

Optimized maintenance scheduling not only helps to reduce costs and minimize production downtime but also enhances overall system efciency and reliability. By applying optimization and simulation techniques, organizations can create more efective long-term maintenance strategies, ensuring that resources are used efciently without unnecessary expenses.

#### **Gap Analysis**

Despite the growing adoption of PdM strategies in Industry 4.0, some gaps remain in both the literature and practical applications of this technology. Table [1](#page-5-0) presents an overview of the reviewed studies.

First, survival analysis—a proven approach for timeto-event modeling in medical research [[13](#page-15-11), [15](#page-15-13)]—remains underexplored in industrial PdM, particularly for generating probabilistic survival functions that quantify failure risk over time. Most existing ML-based approaches for RUL estimation sufer from limitations: they typically produce point estimates without quantifying uncertainty, assume stationary test conditions, and often struggle to handle censored data. In contrast, survival analysis can ofer a promising alternative by modeling hazard rates, generating survival probability curves, and naturally incorporating censored observations, enabling more transparent and time-aware prognostics. The ability to incorporate censored data is especially important in RUL estimation, as failures may not always be observed for certain components. Additionally, existing studies [\[12,](#page-15-10) [20](#page-16-2)] prioritize deterministic thresholds (e.g., fxed degradation rates), limiting adaptability to dynamic degradation patterns.

SN Computer Science (2025) 6:766 Page 5 of 17 766

![](_page_4_Figure_1.jpeg)

<span id="page-4-0"></span>**Fig. 3** Taxonomy of the methods applied for survival analysis [[14](#page-15-12)]

Second, there is an ongoing misalignment between RUL prediction and maintenance scheduling optimization. While advanced models like RSF and GBSA demonstrate robust failure forecasting [[14](#page-15-12)], their integration

with production-aware optimization algorithms is rarely explored, leading to suboptimal downtime and resource allocation.

766 Page 6 of 17 SN Computer Science (2025) 6:766

<span id="page-5-0"></span>**Table 1** Summary of reviewed studies

| Study | Problem                                                 | Methods                                         | Main conclusions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-------|---------------------------------------------------------|-------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [10]  | RUL Estimation                                          | RF, XGB, SVR, MLP                               | The proposed methods to estimate the RUL,<br>particularly RF, performed relatively well<br>on test data. However, real-world validation<br>showed a performance drop due to random<br>failure causes, overftting risks, and chal<br>lenges in adapting to unpredictable real<br>world conditions.                                                                                                                                                                                                    |
| [21]  | RUL Estimation                                          | SVR                                             | The SVR-based model achieved high accuracy<br>in RUL estimation, even under testing condi<br>tions not included in training. However, it<br>was considered to lack the ability to quantify<br>prediction uncertainty.                                                                                                                                                                                                                                                                                |
| [11]  | RUL Estimation                                          | MLP, SVR, XGBoost, ETR, RF, Ridge<br>Regression | The MLP ensemble achieved the best overall<br>performance with consistent predictions<br>across most degradation levels. The study<br>demonstrated the potential of deep learn<br>ing models over traditional ML approaches.<br>However, model performance varied signif<br>cantly across degradation levels, especially in<br>underrepresented or non-represented regions<br>of the dataset (i.e., censored data).                                                                                  |
| [16]  | RUL Estimation                                          | Kaplan-Meier                                    | The Kaplan–Meier estimator was used to<br>analyze survival probabilities and model the<br>survival function of industrial components.<br>The authors emphasized that survival analy<br>sis enabled the identifcation of complex<br>failure patterns. However, they concluded<br>that applying a survival analysis framework<br>requires substantial pre-processing efort to<br>ensure model validity.                                                                                                |
| [17]  | RUL Estimation                                          | Kaplan-Meier, Cox Proportional Hazard<br>Models | Kaplan-Meier was used to estimate survival<br>probabilities for maintenance schedul<br>ing, while the Cox model identifed key<br>failure predictors. The study highlights the<br>importance of explainable models in PdM<br>and their strength in handling censored data<br>and multiple covariates. Survival analysis<br>provided valuable information about machin<br>ery reliability and failure patterns. The main<br>limitation include a lack of generalizability<br>across diferent settings. |
| [12]  | RULE stimation, Maintenance Sched<br>uling Optimization | BO-CNN-Bi-LSTM, MILP                            | Integrated RUL estimation with maintenance<br>scheduling into a single PdM framework.<br>The BO-CNN-Bi-LSTM-AM model outper<br>formed baselines in RUL prediction accu<br>racy. The MILP model optimized scheduling<br>to minimize maintenance and idle time. The<br>authors demonstrated that including RUL in<br>scheduling decisions led to more realistic and<br>efcient plans. The main limitations include<br>reliance on RUL accuracy and focus on a<br>single-objective optimization.        |

SN Computer Science (2025) 6:766 Page 7 of 17 766

| Table 1 (continued) |                                     |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  |  |  |
|---------------------|-------------------------------------|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|
| Study               | Problem                             | Methods         | Main conclusions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  |  |  |
| [20]                | Maintenance Scheduling Optimization | GA, Statistical | Proposed a system combining failure predic<br>tion, throughput optimization using a GA,<br>and simulation modules to test maintenance<br>impact. This integration was shown to be<br>highly benefcial, helping to meet production<br>targets and optimizing maintenance actions<br>while mitigating its efects. The main limi<br>tation include increased complexity and com<br>putation time as the number of components<br>or machines grows, which poses challenges<br>for real-world scalability. |  |  |  |

These gaps collectively highlight the need for frameworks that unify probabilistic RUL modeling with operational constraints, leveraging survival analysis strengths while addressing industrial realities. Addressing these limitations could unlock more reliable, adaptable, and cost-effective PdM solutions for Industry 4.0.

# <span id="page-6-0"></span>**Methodology**

The developed framework is built around the PdM concept and integrates survival analysis techniques to estimate the RUL of industrial components. Additionally, the system optimizes the maintenance scheduling for improved operational efciency.

The system's architecture is divided into four main modules, as shown in Fig. [4.](#page-6-1)

![](_page_6_Figure_6.jpeg)

<span id="page-6-1"></span>**Fig. 4** PdM framework architecture

766 Page 8 of 17 SN Computer Science (2025) 6:766

• **Data Acquisition and Pre-Processing:** Involves collecting and ingesting raw data from various sources. The acquired data then undergoes pre-processing steps to enhance accuracy and improve the efciency of subsequent models.

- **RUL Prediction:** Survival analysis techniques are applied to estimate the degradation of components over time.
- **Maintenance Scheduling Optimization:** Interprets the resulting survival function for each component and employs a production simulation and an optimization algorithm to determine the optimized maintenance schedules, minimizing production downtime and costs.
- **Maintenance Activities:** Users can execute maintenance tasks based on the optimized schedules and predictive information.

The solution was implemented in Python, using packages including (1) *scikit-survival* for implementing the survival models, (2) *scikit-learn* and *pandas* for data handling, preprocessing, and computing performance metrics, and (3) *scipy.optimize*, for developing the maintenance schedule optimization module.

The evaluation procedure includes experiments to validate both components (RUL prediction and maintenance scheduling optimization). The experiments to test the RUL prediction algorithm include two datasets: (1) the welding electrodes worn out dataset, collected from a manufacturer of domestic appliances (dishwashers), and (2) the synthetic Microsoft Azure dataset designed for building PdM models.[1](#page-7-1)

Welding electrodes, used by robots, play a crucial role in joining these components with precision, ensuring structural integrity. Figure [5](#page-7-2) illustrates the welding process performed to manufacture a dishwasher tub. With advances in predictive maintenance techniques, engineers can now monitor electrode wear and schedule replacements optimally. The prediction of the welding electrode or reel worn out will permit the replacement of that component at a more appropriate time, avoiding replacing the electrode too early (causing waste) or too late (causing degradation in the quality). This proactive approach not only ensures uninterrupted production but also enhances overall product quality and efciency in the manufacturing process. This dataset tests the RUL prediction and maintenance scheduling optimization modules' performance in a real scenario with a direct impact on factory productivity.

The Microsoft Azure dataset comprises multiple components, including sensor readings, maintenance logs, and operational parameters, that provide a detailed picture of

![](_page_7_Picture_10.jpeg)

**Fig. 5** Spot welding robot processing a dishwasher tub

<span id="page-7-2"></span>industrial machinery performance. When used alongside the welding electrodes dataset, it ofers a complementary scenario to rigorously test the RUL prediction algorithm, demonstrating its adaptability and robust performance across diverse industrial environments.

The RUL prediction module's performance was evaluated on two datasets using the concordance index (C-index) [\[22](#page-16-4)]. This metric quantifes a model's ability to correctly rank predictions of RUL by measuring the proportion of pairs where predicted and actual outcomes follow the same order. The maintenance scheduling optimization module's performance was evaluated using the total production downtime. The module minimizes downtime by strategically scheduling maintenance to maximize overlap, reducing production interruptions, and optimizing the production sequence.

## <span id="page-7-0"></span>**Implementation**

As mentioned above, the developed system comprises various modules, including (1) the data acquisition and pre-processing module, (2) the RUL prediction algorithm, and (3) the maintenance schedule optimization module. This section explains the implementation of each one.

<span id="page-7-1"></span><sup>1</sup> [https://www.kaggle.com/datasets/arnabbiswas1/microsoft-azure](https://www.kaggle.com/datasets/arnabbiswas1/microsoft-azure-predictive-maintenance)[predictive-maintenance.](https://www.kaggle.com/datasets/arnabbiswas1/microsoft-azure-predictive-maintenance)

SN Computer Science (2025) 6:766 Page 9 of 17 766

#### **Data Acquisition and Pre‑Processing**

The data acquisition and pre-processing modules comprises two steps: (1) the data acquisition from the industrial process, and (2) the data pre-processing, including data fusion, cleaning, and feature engineering. Depending on the scenario (spot welding use case or synthetic dataset), a different approach is required to acquire and convert the raw data into the structured format used by the RUL prediction algorithm. For that, in both datasets, the pre-processing module computes aggregated features (mean and standard deviation) from the sensor data for each operation cycle. By aggregating the data in operation cycles, any sporadic gaps in individual sensor readings are flled into the cycle-level statistics, so long as at least one valid reading exists in the cycle, resulting in a meaningful mean and standard deviation. This both mitigates the bias that raw missing values can introduce and ensures each cycle yields a complete, noisesmoothed feature vector for survival modeling.

## **Spot Welding Dataset**

The spot welding dataset has data collected from the operation of a spot welding robot. The data from the welding process was collected using an IoT gateway. That gateway stored the acquired data in three fles/tables. One fle contains features such as the minimum, mean, and maximum current of the welding component, with 629,444 samples. Another fle includes rotary table data, with a counter value indicating activations, totaling 96,869 samples. The third fle logs failure events, including the time of failure and error codes, with 248 samples.

This data was pre-processed by merging the datasets and aligning timestamps to synchronize all the data. The diference between successive counter values was then calculated to determine machine cycles, each representing an operational period of the welding machine. To prepare this data for the predictive models, feature engineering involved calculating the TTF and computing statistics like the mean and standard deviation of current sensor readings for each cycle. Based on historical failure data, each cycle was labeled as *Operational* or *Failure*. After the pre-processing, the resulting dataset included 70,971 cycles, composed of 5 features (mean and standard deviation of the welding current, cycles counter, cycle duration, and cumulative working hours) and 2 target variables (TTF and a binary variable indicating if the component was replaced in that cycle).

#### **Synthetic Dataset**

The synthetic dataset (Microsoft Azure PdM dataset) didn't require the data acquisition step because the data was already stored across several fles. One fle includes sensor readings for voltage, rotation, pressure, and vibration from 100 industrial machines. It also includes data related to machine error samples, maintenance records (both proactive and reactive), a subset of maintenance data with component replacements due to failures, and machine model and age information. In this dataset, a machine is assumed to be composed of four diferent components.

Following a similar approach to the spot welding dataset, the data was merged, cleaned, and fltered to include only records from one machine. Feature engineering was performed, where cycles for each of the four components were calculated, resetting the count after each replacement. The TTF of each component was also calculated. The resulting dataset included 50,407 cycles, composed of 16 features (mean and standard deviation of voltage, rotation, pressure, and vibration sensors, and for each component, the cycle counter and cumulative hours), and as target variables for each component, the TTF and a binary variable indicating the component replacement.

## **RUL Prediction**

The cleaned and preprocessed data from both datasets were split into training (80%) and testing (20%) sets, with target variables defned as component status (*Operating* or *Failure*) and TTF. Several survival models were trained, including the Cox Proportional Hazards (Cox PH) model and MLbased models like Random Survival Forest (RSF), Gradient Boosting Survival Analysis, and Fast Survival Support Vector Machine (Survival SVM). Hyperparameter tuning was performed via cross-validation within the training set. Model performance was evaluated using the C-index, and survival function plots were generated to compare estimated survival functions with actual outcomes.

The following sections provide a brief description of each survival model employed.

#### **Cox Proportional Hazards Model**

As previously stated, the Cox PH model is a statistical model used to understand how diferent factors afect the time until a specifc event happens. The model is based on a hazard function, which is represented by [[15\]](#page-15-13):

$$h(t, X) = h_0(t) \exp(\beta X)$$
 (2)

In this equation, *h*0(*t*) is the baseline hazard (the basic risk of failure over time), *𝛽* are the coefcients that show how much each factor (*X*) impacts the risk, and *X* are the factors or variables being considered. The model assumes that the survival times are independent, that the risk ratio stays consistent over time, and that the efect of the factors on the risk is linear and doesn't change during the observation period.

766 Page 10 of 17 SN Computer Science (2025) 6:766

#### **Random Survival Forests**

RSF extends traditional DT ensembles to survival analysis by building multiple survival trees using random data samples. At each split, a random set of features is used, which helps reduce tree correlations. The fnal survival predictions come from averaging the results across all the trees. The RSF model was implemented using the *scikit-survival* library and with the hyperparameters highlighted in the frst part of Table [2.](#page-9-0) For both RSF, GBSA, and Survival SVM models, the best hyperparameters were obtained using grid search cross-validation. For the RSF model, 100 estimators (*n\_estimators*) provided a good bias-variance trade-of, the split (*min\_samples\_split*) and leaf (*min\_samples\_leaf*) thresholds prevent overftting to noisy cycles, and fnally, using the square root of the total features (*max\_features*) when looking for the best split at each node typically improves generalization.

#### **Gradient Boosting Survival Analysis**

GBSA applies an ensemble learning approach that builds weak learners sequentially to minimize the prediction error iteratively. Unlike RSF, which averages predictions from independently trained survival trees, gradient boosting improves the model's predictions gradually, refning them at each stage. The model was trained with the hyperparameters shown in the second part of Table [2](#page-9-0). Like in the RSF model, the number of estimators (*n\_estimators*) in the GBSA, providing a good bias-variance tradeof, was 100, and the learning rate of 0.01 ensured gradual model updates that mitigated overftting to noisy sensor fuctuations.

## **Survival Support Vector Machines**

Survival SVM extends traditional SVM models to survival analysis by optimizing a margin-based loss function while dealing with censored data. The goal is to create a hyperplane that best separates survival times, considering

<span id="page-9-0"></span>**Table 2** Hyperparameters optimized for the RSF, GBSA, and Survival SVM models

| Model        | Hyperparameter    |      |
|--------------|-------------------|------|
| RSF          | n_estimators      | 100  |
|              | min_samples_split | 10   |
|              | min_samples_leaf  | 15   |
|              | max_features      | sqrt |
| GBSA         | n_estimators      | 100  |
|              | learning_rate     | 0.01 |
| Survival SVM | max_iter          | 1000 |
|              | tol               | 1e-5 |

incomplete data. Unlike standard SVMs, which are used for classifcation or regression, Survival SVM specifcally models the time-to-event structure. The model was implemented using the hyperparameters specifed in the third part of Table [2](#page-9-0). The obtained optimal hyperparameters were 1000 iterations (*max\_iter*) and a tolerance of 1e-5 (*tol*).

## **Maintenance Scheduling Optimization**

To make the PdM system more practical for end-users, the maintenance scheduling optimization module was developed. This module, built on the survival functions established by the predictive module, can simulate long-term production operations, returning not only the optimal times for machine maintenance but also the ideal production sequence to minimize production downtime. The developed algorithm is fexible and can be applied to any dataset, as it only requires a base survival function for each machine component, along with the necessary simulation parameters and production requirements. Figure [6](#page-10-1) illustrates a simplifed fow of the algorithm.

This algorithm simulates the total time required for production based on the given requirements. It considers machine availability, product characteristics, and the specifc needs of each machine while also considering the maintenance of the involved components. By factoring in these elements, the system ensures that production and maintenance are well-coordinated, and since machine component degradation over time is represented using survival functions, the algorithm can accurately estimate when maintenance is required.

A critical challenge in scheduling maintenance is that each component degrades at a diferent rate and may require maintenance at diferent times, depending on its individual condition and the specifc product types being processed. So, the goal of this algorithm is to try to align maintenance periods across machines, reducing the frequency of production stops. This is achieved by optimizing the production sequence so that maintenance activities overlap as much as possible.

The optimization of the production sequence is achieved using Simulated Annealing (SA), a metaheuristic stochastic optimization algorithm. Metaheuristic algorithms like SA have been widely applied across various engineering domains, including manufacturing process optimization and production scheduling [\[23\]](#page-16-5). SA is particularly efective for determining optimal confgurations within models or simulations, due to its fexibility in addressing a broad range of complex problem types [\[23,](#page-16-5) [24](#page-16-6)]. Therefore, it is the ideal choice for this module.

The optimization process follows these steps:

![](_page_10_Figure_1.jpeg)

<span id="page-10-1"></span>**Fig. 6** Flowchart illustrating the maintenance scheduling and optimization algorithm

- 1. Simulate and schedule a production sequence, obtaining maintenance intervals for each machine component *c* ∈ *C*.
- 2. After each iteration of the production simulation, obtain a set of maintenance intervals for each machine component *c* ∈ *C*, represented as:

$$I_c = \{(s_{c1}, e_{c1}), (s_{c2}, e_{c2}), \dots, (s_{cn}, e_{cin})\}$$

 where *scj* and *ecj* represent the start and end times of the *j*-th maintenance interval for machine component *c*. The scheduling of these intervals is directly infuenced by the production sequence being evaluated since diferent products cause diferent levels of component degradation, leading to diferent maintenance needs.

3. Compute the combined set of all maintenance intervals across components:

$$Maint = \bigcup_{c \in C} I_c$$

4. Since maintenance periods may overlap, calculate the total production downtime *D* by merging all overlapping intervals:

$$D = \bigcup_{(s,e) \in Maint} [s,e]$$

- 5. Evaluate the cost function that quantifes total downtime: Cost <sup>=</sup> <sup>|</sup>*D*<sup>|</sup>
- 6. Adjust the production sequence and recalculate the maintenance schedule.
- 7. Compare the new schedule's cost with the previous one.
- 8. Iterate continuously, refning the schedule to minimize downtime while aligning maintenance periods.

Detailed information regarding the implementation, including input variables and other defnitions, are available in the GitHub repository.[2](#page-10-2)

## <span id="page-10-0"></span>**Results and Discussion**

The designed experiments allow the complete validation of the developed modules: (1) the RUL prediction algorithm and (2) the maintenance scheduling optimization module. The following contents describe the results of the RUL prediction algorithm using the C-index performance metric and

<span id="page-10-2"></span><sup>2</sup> [https://github.com/DIGI2-FEUP/survival\\_analysis\\_degradation\\_](https://github.com/DIGI2-FEUP/survival_analysis_degradation_models) [models](https://github.com/DIGI2-FEUP/survival_analysis_degradation_models)

766 Page 12 of 17 SN Computer Science (2025) 6:766

<span id="page-11-0"></span>**Table 3** C-index performance evaluation of the survival analysis models for the spot welding dataset

| Component | Cox PH |       | RSF   |       | GBSA  |       | Survival SVM |       |
|-----------|--------|-------|-------|-------|-------|-------|--------------|-------|
|           | Train  | Test  | Train | Test  | Train | Test  | Train        | Test  |
| c1        | 0.763  | 0.974 | 0.897 | 0.791 | 0.789 | 0.789 | 0.722        | 0.865 |

<span id="page-11-1"></span>**Table 4** C-index performance evaluation of the survival analysis models for the synthetic dataset

| Component | Cox PH |       | RSF   |       | GBSA  |       | Survival SVM |       |
|-----------|--------|-------|-------|-------|-------|-------|--------------|-------|
|           | Train  | Test  | Train | Test  | Train | Test  | Train        | Test  |
| c1        | 0.531  | 0.926 | 0.709 | 0.689 | 0.627 | 0.645 | 0.510        | 0.553 |
| c2        | 0.518  | 0.858 | 0.702 | 0.387 | 0.627 | 0.509 | 0.516        | 0.544 |
| c3        | 0.480  | 0.649 | 0.751 | 0.458 | 0.722 | 0.543 | 0.511        | 0.496 |
| c4        | 0.518  | 0.792 | 0.687 | 0.601 | 0.602 | 0.579 | 0.507        | 0.514 |

gains obtained by using the maintenance scheduling optimization in terms of production downtime.

## **Predictive Models Performance**

The selected performance metric for evaluating the survival analysis methods for RUL prediction was the C-index. The models' evaluation used 80% of the data for training and 20% for testing. Within the training set, all model hyperparameters were tuned using 5-fold cross-validation before the fnal evaluation. Table [3](#page-11-0) presents the obtained results for the spot welding dataset using only one component (robot electrode).

The Cox PH model's moderate training C-index (0.763) versus its high test C-index (0.974) suggests possible overftting or sensitivity to the test split. RSF shows strong training performance (0.897) but drops to 0.791 on the test set, indicating some loss of generalization. GBSA yields identical scores (0.789) on both sets, which implies good generalization and no clear overftting/underftting. The Survival SVM, with its lower training score (0.722) yet higher test score (0.865), may indicate that the model is overftting to specifc patterns in the test set.

Although some test C-indices fall below 0.80, values above 0.70 are still useful in practice: they allow ranking of units by failure risk, which can meaningfully improve maintenance scheduling and reduce downtime.

When evaluating the synthetic dataset, performance was assessed for each machine component. The results are presented in Table [4.](#page-11-1)

The results show that the Cox PH model demonstrates a consistent pattern of overftting across all components, indicating model instability. RSF generalizes acceptably for *c1* and *c4* but overfts on *c2* and *c3*. GBSA maintains stable performance across most components. Survival SVM performs comparatively poorly, with C-indices around 0.50–0.55, indicating it may be underpowered for these datasets.

![](_page_11_Figure_12.jpeg)

<span id="page-11-2"></span>**Fig. 7** Resulting survival function using the GBSA model in the spot welding dataset

Figure [7](#page-11-2) illustrates an example of the resulting survival function for the spot welding dataset using the GBSA model. This plot explicitly shows the machine's component degradation as a function of the number of operational cycles it has performed, providing insight into its RUL and failure probability over time.

Based on the results, the GBSA model ofers the best balance between training and test performance. The GBSA model demonstrates the ability to capture complex, nonlinear degradation patterns. GBSA iteratively combines weak learners (e.g., decision trees) to minimize prediction errors, adaptively refning the model. Using a low learning rate (0.01) and a sufcient number of estimators (100) likely enabled stable learning, balancing bias and variance. Additionally, the GBSA ensemble approach inherently mitigates overftting by aggregating predictions from multiple trees, whereas methods like RSF may sufer from higher variance when individual trees overft specifc subsets. Even with a moderate C-index (0.70–0.80), it can provide actionable risk rankings in industrial maintenance, guiding inspection and replacement decisions to reduce unplanned failures.

SN Computer Science (2025) 6:766 Page 13 of 17 766

#### **Maintenance Scheduling Optimization**

To exemplify the functioning of the maintenance scheduling optimization, an example scenario with specifc inputs will be presented, along with the results and their interpretation.

Consider this scenario: a production system consisting of three sequential machines—*m1*, *m2*, and *m3*—where each machine has one component—*c1*, *c2*, and *c3*. Each component degradation is represented by its own survival function. At the start of the simulation, *c2* has already completed 5000 operational cycles, while both *c1* and *c3* have each completed 7100 cycles.

The system is tasked with producing four product types: *A0*, *A1*, *A2*, and *A3*. The production quantities for each product are 180 units of *A0*, 180 units of *A1*, 200 units of *A2*, and 180 units of *A3*.

For the simulation, the following parameters were defned: the maintenance duration for each component is equivalent to 5 operational cycles, and components undergo maintenance when their survival probability falls within the range of 0.1985 to 0.2. The survival probability interval between 0.1985 and 0.20 was chosen as the default value because it provides an optimal balance between preempting high-risk failures and avoiding unnecessary downtime, while remaining fully confgurable to each industry's risktolerance constraints. Operating within this interval ensures maintenance actions occur early enough to mitigate most failure risks without succumbing to over-maintenance.

It is important to note that the maintenance duration remains uniform throughout the simulation. Therefore, the chosen value should represent the average expected maintenance time. In real-world scenarios, maintenance tasks are subject to variability due to unexpected events such as delays, resource constraints, or technical complications. By using an average maintenance duration value, the simulation can better approximate the typical process and account for this inherent uncertainty without overcomplicating the model.

Another required simulation parameter is a productmachine-component cycle mapping that defnes how many cycles each product requires on each machine/component. Table [5](#page-12-0) illustrates the mapping used for this example scenario.

<span id="page-12-0"></span>**Table 5** Example of product-machine-component and operational cycle mapping

| Machine | Compo<br>nent | Product<br>A0 | Product<br>A1 | Product<br>A2 | Product A3 |
|---------|---------------|---------------|---------------|---------------|------------|
| m1      | c1            | 50            | 2             | 0             | 0          |
| m2      | c2            | 0             | 2             | 50            | 0          |
| m3      | c3            | 0             | 2             | 0             | 50         |

This mapping clearly shows that producing *A0* requires 50 operational cycles on *m1*. *A1* needs 2 operational cycles on *m1*, *m2*, and *m3* in that exact order. *A2* requires 50 operational cycles on *m2*, and *A3* requires 50 operational cycles on *m3*.

The simulation, combined with the SA algorithm, uses these parameters to generate the optimized production sequence. A sample output log from the simulation is shown in Fig. [8.](#page-13-1) The entire sequence is provided to the user, but only a portion is displayed here for illustration. For simplicity, time is represented in slots, with each slot corresponding to one operational cycle.

In addition to the log, the simulation generates a plot showing the survival probability of the machine components throughout their operating time. This plot refects how each component degrades based on the optimized production sequence and maintenance events.

For example, interpreting the plot in Fig. [9](#page-14-0) that represents the production planning for an optimized production sequence, *c1* and *c3* start the simulation with an initial survival probability of approximately 0.28, while *c2* started at 0.49. The optimized production sequence causes *c1* and *c3* to reach the maintenance threshold at similar times, allowing for their maintenance to be performed simultaneously. In contrast, *c2* did not need maintenance at that point, so it continued operating without intervention.

The frst maintenance event for *c2* occurred only at *t3589*, followed by a second overlapping maintenance for *c1* and *c3* at approximately *t10254*. Due to the specifc degradation rates and scheduling, *c2* did not require a second maintenance cycle in order to complete the full production requirement.

Now, consider the plot in Fig. [10,](#page-14-1) which represents the same parameters and requirements but follows a non-optimized production sequence. Here, while the frst maintenance for *c1* and *c3* can still be performed simultaneously, the second maintenance can't, leading to an additional maintenance cycle when compared to the previously analyzed optimized solution. This results in higher production downtime and increased maintenance costs.

The system efectively schedules maintenance interventions at optimal times, preventing unnecessary disruptions. The comparisons between the optimized and non-optimized production sequences highlight the advantages of the maintenance scheduling optimization algorithm, which successfully minimizes downtime by 25% and indirectly reduces maintenance costs. These results emphasize the importance of integrating PdM with scheduling techniques to improve overall operational performance.

766 Page 14 of 17 SN Computer Science (2025) 6:766

<span id="page-13-1"></span>**Fig. 8** Example output log from the scheduling optimization algorithm, showcasing results for the generated optimized production sequence

# <span id="page-13-0"></span>**Conclusions and Future Work**

This work introduced a data-driven PdM framework based on survival analysis, designed to extend the life cycle of industrial components by predicting failure events and optimizing maintenance schedules. The framework consists of three core modules—data acquisition/pre-processing, RUL prediction, and maintenance scheduling optimization—that collectively address the limitations of traditional PdM systems by integrating survival analysis with production-aware optimization. Data acquisition and pre-processing were focused on data cleaning, feature engineering, and preparing the available data to optimize the performance of the subsequent models. By applying survival analysis methods (Cox PH, RSF, GBSA, Survival SVM), the system probabilistically estimates RUL through survival functions, with GBSA SN Computer Science (2025) 6:766 Page 15 of 17 766

![](_page_14_Figure_1.jpeg)

<span id="page-14-0"></span>**Fig. 9** Maintenance schedule simulation for an optimized production sequence. Maintenances performed at *t1348*, *t3589* and *t10258*

![](_page_14_Figure_3.jpeg)

<span id="page-14-1"></span>**Fig. 10** Maintenance schedule simulation for a non-optimized production sequence. Maintenances performed at *t1128*, *t3384*, *t9986* and *t10449*

emerging as the most robust model due to its resistance to overftting and ability to generalize across heterogeneous datasets (welding electrodes, Microsoft Azure PdM).

Based on the components' survival functions, an algorithm was developed to simulate and optimize the production process according to input production requirements. By generating an optimal production sequence that strategically clusters interventions, the downtime was reduced by 25% compared to non-optimized methods. As major outcomes, the algorithm (1) maximizes the overlap of maintenance events to minimize production disruptions, (2) schedules maintenance only when needed, preventing unnecessary repairs, (3) uses SA to optimize the production sequence and maintenance timing iteratively, and (4) generates a detailed simulation report, providing users with an optimal production and maintenance plan. The integration of survival functions with production constraints ensures maintenance plans are both risk-informed and operationally efcient, aligning with Industry 4.0's demand for adaptive, data-driven solutions. By validating the framework on real-world and synthetic datasets, this study demonstrates its potential to enhance operational efciency, reduce costs, and support long-term maintenance planning in industrial environments.

Future eforts will focus on scaling the developed framework to production lines with several machines and components, assessing the main benefts behind this framework, 766 Page 16 of 17 SN Computer Science (2025) 6:766

and exploring different architectures based on parallel computing or distributed systems to handle more complex scenarios. Expanding the optimization algorithm to incorporate multidimensional cost factors, including labor costs, spare parts availability, environmental impact, and energy consumption, would enable more holistic decision-making. Finally, adding the functionality to validate diferent scenarios, including production line layouts, would be crucial to increase the framework's adaptability and robustness in diferent industrial settings.

**Acknowledgements** This work was partially supported by the HORI-ZON-CL4-2021-TWIN-TRANSITION-01 openZDM project, under Grant Agreement No. 101058673.

**Author Contributions** Conceptualization: Eliseu Pereira, Gil Gonçalves; Implementation: Beatriz Coutinho, Margarida Moreira; Funding Acquisition: Gil Gonçalves; Administration, Resources & Supervision: Eliseu Pereira, Gil Gonçalves; Validation: all; Writing: Beatriz Coutinho, Eliseu Pereira.

**Funding** Open access funding provided by FCT|FCCN (b-on). This work was partially supported by the HORIZON-CL4-2021-TWIN-TRANSITION-01 openZDM project, under Grant Agreement No. 101058673.

**Data Availability** Not applicable.

## **Declarations**

**Conflict of interest** The authors have no confict of interest to declare.

**Research Involving Human and/or Animals** Not applicable.

**Informed Consent** Not applicable.

**Open Access** This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit <http://creativecommons.org/licenses/by/4.0/>.

# **References**

- <span id="page-15-0"></span>1. Haarman M, Mulders M, Vassiliadis C. Predictive maintenance 4.0: predict the unpredictable. PwC and Mainnovation. 2017;4.
- <span id="page-15-1"></span>2. Moreira M, Pereira EM, Gonçalves G. Data-driven predictive maintenance for component life-cycle extension. In: International Conference on Informatics in Control, Automation and Robotics. 2024.<https://api.semanticscholar.org/CorpusID:274190108>
- <span id="page-15-2"></span>3. Rossini R, Prato G, Conzon D, Pastrone C, Pereira E, Reis J, Goncalves G, Henriques D, Santiago AR, Ferreira A. AI environment for predictive maintenance in a manufacturing scenario. In: 2021 26th IEEE International Conference on Emerging Technologies

- and Factory Automation (ETFA ), pp. 1–8. IEEE, Vasteras, Sweden. 2021. [https://doi.org/10.1109/ETFA45728.2021.96133](https://doi.org/10.1109/ETFA45728.2021.9613359) [59](https://doi.org/10.1109/ETFA45728.2021.9613359) . <https://ieeexplore.ieee.org/document/9613359/> Accessed 2024-07-24
- <span id="page-15-3"></span>4. Ferreira C, Gonçalves G. Remaining useful life prediction and challenges: A literature review on the use of machine learning methods. J Manuf Syst. 2022;63:550–62. [https://doi.org/10.](https://doi.org/10.1016/j.jmsy.2022.05.010) [1016/j.jmsy.2022.05.010.](https://doi.org/10.1016/j.jmsy.2022.05.010)
- <span id="page-15-4"></span>5. Zonta T, Costa CA, Rosa Righi R, Lima MJ, Trindade ES, Li GP. Predictive maintenance in the Industry 4.0: A systematic literature review. Comput Ind Eng. 2020;150: 106889. [https://doi.org/10.](https://doi.org/10.1016/j.cie.2020.106889) [1016/j.cie.2020.106889.](https://doi.org/10.1016/j.cie.2020.106889)
- <span id="page-15-5"></span>6. Trojan F, Marçal RF. Proposal of maintenance-types classifcation to clarify maintenance concepts in production and operations management. J Bus Econ. 2017;8(7):560–72. [https://doi.org/10.](https://doi.org/10.15341/jbe(2155-7950)/07.08.2017/005) [15341/jbe\(2155-7950\)/07.08.2017/005.](https://doi.org/10.15341/jbe(2155-7950)/07.08.2017/005)
- <span id="page-15-6"></span>7. Ramezani SB, Cummins L, Killen B, Carley R, Amirlatif A, Rahimi S, Seale M, Bian L. Scalability, Explainability and Performance of Data-Driven Algorithms in Predicting the Remaining Useful Life: A Comprehensive Review. IEEE Access. 2023;11:41741–69. [https://doi.org/10.1109/ACCESS.2023.32679](https://doi.org/10.1109/ACCESS.2023.3267960) [60.](https://doi.org/10.1109/ACCESS.2023.3267960) (**Accessed 2024-01-03**).
- <span id="page-15-7"></span>8. Almeida M, Pereira E, Gonçalves G. HyPredictor: Hybrid Failure Prognosis Approach Combining Data-Driven and Knowledge-Based Methods. In: Proceedings of the 21st International Conference on Informatics in Control, Automation and Robotics - Volume 1: ICINCO, pp. 245–252. SciTePress, Porto, Portugal. 2024. <https://doi.org/10.5220/0012924300003822> . INSTICC
- <span id="page-15-8"></span>9. Ahmadzadeh F, Lundberg J. Remaining useful life estimation: review. International Journal of System Assurance Engineering and Management. 2014;5:461–74. [https://doi.org/10.1007/](https://doi.org/10.1007/s13198-013-0195-0) [s13198-013-0195-0.](https://doi.org/10.1007/s13198-013-0195-0)
- <span id="page-15-9"></span>10. Taşcı B, Omar A, Ayvaz S. Remaining useful lifetime prediction for predictive maintenance in manufacturing. Computers & Industrial Engineering. 2023;184: 109566. [https://doi.org/10.1016/j.cie.](https://doi.org/10.1016/j.cie.2023.109566) [2023.109566](https://doi.org/10.1016/j.cie.2023.109566).
- <span id="page-15-16"></span>11. Matuszczak M, Zbikowski M, Teodorczyk A. Predictive modelling of turbofan engine components condition using machine and deep learning methods Eksploatacja i Niezawodnosc. Maintenance and Reliability. 2021;23:359–70. [https://doi.org/10.17531/](https://doi.org/10.17531/ein.2021.2.16) [ein.2021.2.16](https://doi.org/10.17531/ein.2021.2.16).
- <span id="page-15-10"></span>12. Wang L, Chen Y, Zhao X, Xiang J. Predictive maintenance scheduling for aircraft engines based on remaining useful life prediction. IEEE Internet Things J. 2024;11:23020–31. [https://doi.org/](https://doi.org/10.1109/JIOT.2024.3376715) [10.1109/JIOT.2024.3376715](https://doi.org/10.1109/JIOT.2024.3376715).
- <span id="page-15-11"></span>13. Kartsonaki C. Survival analysis. Diagn Histopathol. 2016;22(7):263–70. [https://doi.org/10.1016/j.mpdhp.2016.06.](https://doi.org/10.1016/j.mpdhp.2016.06.005) [005](https://doi.org/10.1016/j.mpdhp.2016.06.005). (**Mini-Symposium: Medical Statistics**).
- <span id="page-15-12"></span>14. Wang P, Li Y, Reddy CK. Machine learning for survival analysis: A survey. ACM Comput Surv. 2019;51(60):1–36. [https://doi.org/](https://doi.org/10.1145/3214306) [10.1145/3214306.](https://doi.org/10.1145/3214306)
- <span id="page-15-13"></span>15. Moat G, Coleman S. Survival Analysis and Predictive Maintenance Models for non-sensored Assets in Facilities Management. In: 2021 IEEE International Conference on Big Data (Big Data), pp. 4026–4034. IEEE, Orlando, FL, USA. 2021. [https://doi.org/](https://doi.org/10.1109/BigData52589.2021.9671625) [10.1109/BigData52589.2021.9671625](https://doi.org/10.1109/BigData52589.2021.9671625) . [https://ieeexplore.ieee.](https://ieeexplore.ieee.org/document/9671625/) [org/document/9671625/](https://ieeexplore.ieee.org/document/9671625/) Accessed 2024-01-03
- <span id="page-15-14"></span>16. Yang Z, Kanniainen J, Krogerus T, Emmert-Streib F. Prognostic modeling of predictive maintenance with survival analysis for mobile work equipment. Sci Rep. 2022;12(1):8529. [https://doi.](https://doi.org/10.1038/s41598-022-12572-z) [org/10.1038/s41598-022-12572-z.](https://doi.org/10.1038/s41598-022-12572-z)
- <span id="page-15-15"></span>17. Softic S, Hrnjica B. Case studies of survival analysis for predictive maintenance in manufacturing. International Journal of Industrial Engineering and Management. 2024;15:320–37. [https://doi.org/](https://doi.org/10.24867/IJIEM-2024-4-366) [10.24867/IJIEM-2024-4-366.](https://doi.org/10.24867/IJIEM-2024-4-366)

SN Computer Science (2025) 6:766 Page 17 of 17 766

<span id="page-16-0"></span>18. Dolgui A, Bernard A, Lemoine D, Cieminski GV, Romero D. Advances in production management systems artifcial intelligence for sustainable and resilient production systems ifp aict 2021;632. Technical report. <http://www.springer.com/series/6102>

- <span id="page-16-1"></span>19. Zeng C, Huang J, Wang H, Xie J, Zhang Y. Deep Bayesian survival analysis of rail useful lifetime. Eng Struct. 2023;295: 116822. [https://doi.org/10.1016/j.engstruct.2023.116822.](https://doi.org/10.1016/j.engstruct.2023.116822) (**Accessed 2024-07-18**).
- <span id="page-16-2"></span>20. Antão L, Reis J, Gonçalves G. Continuous maintenance system for optimal scheduling based on real-time machine monitoring. In 2018 IEEE 23rd International Conference on Emerging Technologies and Factory Automation (ETFA). 2018;1:410–7. [https://doi.](https://doi.org/10.1109/ETFA.2018.8502612) [org/10.1109/ETFA.2018.8502612.](https://doi.org/10.1109/ETFA.2018.8502612)
- <span id="page-16-3"></span>21. Nuhic A, Terzimehic T, Soczka-Guth T, Buchholz M, Dietmayer K. Health diagnosis and remaining useful life prognostics of lithium-ion batteries using data-driven methods. J Power Sources. 2013;239:680–8. [https://doi.org/10.1016/j.jpowsour.2012.11.146.](https://doi.org/10.1016/j.jpowsour.2012.11.146)

- <span id="page-16-4"></span>22. Harrell FE Jr, Lee KL, Calif RM, Pryor DB, Rosati RA. Regression modelling strategies for improved prognostic prediction. Stat Med. 1984;3(2):143–52.<https://doi.org/10.1002/sim.4780030207>.
- <span id="page-16-5"></span>23. Almufti SM, Shaban AA, Ali RI, Fuente J. Overview of metaheuristic algorithms. Polaris Global Journal of Scholarly Research and Trends. 2023;2:10–32. [https://doi.org/10.58429/](https://doi.org/10.58429/pgjsrt.v2n2a144) [pgjsrt.v2n2a144.](https://doi.org/10.58429/pgjsrt.v2n2a144)
- <span id="page-16-6"></span>24. Kochenderfer MJ, Wheeler TA. Algorithms for Optimization. MIT Press, Cambridge, MA. 2019.<http://mitpress.mit.edu>

**Publisher's Note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional afliations.
<span id="page-0-0"></span>ELSEVIER

Contents lists available at ScienceDirect

# Journal of Water Process Engineering

journal homepage: www.elsevier.com/locate/jwpe

![](_page_0_Picture_5.jpeg)

![](_page_0_Picture_6.jpeg)

# Optimizing silt density index prediction in water treatment systems using pressure-based gradient boosting hybridized with Salp Swarm Algorithm

Brahim Ouadi <sup>a,\*</sup>, Abdelwahhab Khatir <sup>a,b,\*\*</sup>, Erica Magagnini <sup>b</sup>, Maamar Mokadem <sup>c</sup>, Laith Abualigah <sup>d</sup>, Aseel Smerat <sup>e,f,g</sup>

- a Civil engineering department, University of sciences and technologies Mohamed Boudiaf of Oran (USTO-MB), 1505, EL MNAOUER, 31000 Oran, Algeria
- <sup>b</sup> Department of DICEA, Polytechnic University of Marche, via brecce bianche 12, 60131 Ancona, Italy
- <sup>c</sup> Institute of Sciences, University Center Morsli Abdalla of Tipaza, 42000, Algeria
- <sup>d</sup> Computer Science Department, Al al-Bayt University, Mafraq 25113, Jordan
- e Centre for Research Impact & Outcome, Chitkara University Institute of Engineering and Technology, Chitkara University, Rajpura, 140401, Punjab, India
- f Artificial Intelligence and Sensing Technologies (AIST) Research Center, University of Tabuk, Tabuk 71491, Saudi Arabia
- <sup>8</sup> Applied Science Research Center, Applied Science Private University, Amman 11931, Jordan

#### ARTICLE INFO

Editor: Guangming Jiang

Keywords:
Silt density index
Water treatment optimization
Desalination plant
Gradient boosting
Salp Swarm Algorithm
Predictive model

#### ABSTRACT

This study introduces a novel approach for predicting Silt Density Index (SDI) values in desalination systems by combining Gradient Boosting with the Salp Swarm Algorithm (GBSSA). The integration of GBSSA enhances predictive accuracy over a one-month period, addressing critical challenges related to water scarcity exacerbated by climate change. Data were collected from two desalination plants in western Algeria, specifically the Benisaf and El Mactaa plants, to train and validate the models. Pressure measurements were chosen as input features due to their ease of measurement and the use of simple, cost-effective equipment, minimizing the need for complex sensors and reducing manual intervention. The study compared the performance of three Gradient Boosting variants: the standard Gradient Boosting model (GB), Gradient Boosting optimized with Particle Swarm Optimization (GBPSO), and the proposed GBSSA model. Results demonstrated that the GBSSA model significantly outperformed both GB and GBPSO, achieving superior accuracy in predicting SDI values. This enhanced predictive capability is crucial for effective monitoring and management of fouling in desalination plants, facilitating better operational adjustments and maintenance decisions. The findings underscore the potential of combining advanced machine learning techniques with optimization algorithms to improve predictive modeling in critical environmental contexts.

#### 1. Introduction

#### 1.1. Background and motivation

In the field of water quality monitoring, the most commonly employed sensors for assessing the potential for particulate fouling in feedwater include those that measure the silt density index (SDI), turbidity, and particle count. SDI is a widely recognized parameter for evaluating water quality, specifically assessing the potential for membrane fouling by measuring the rate of decline in filtration flux [1]. These methods offer quick evaluations of water quality, allowing

operators to take timely actions. However, their effectiveness is limited as they often lack sensitivity to specific particle size ranges, leading to unreliable results in certain situations. Over the past four decades, extensive work has focused on creating membrane-based fouling indices to better assess the quality of reverse osmosis (RO) feedwater and to more accurately predict the likelihood of fouling in RO systems. While several of these fouling indices, like  $MFI_{0.45}$  and MFI-UF, focus on estimating the potential fouling resistance (R<sub>f</sub>), they do not account for the Cake Enhanced Osmotic Pressure (CEOP). Fouling indices are metrics that assess the likelihood of membrane fouling by measuring the rate of flux decline during filtration, which is essential in predicting and

E-mail addresses: brahim.ouadi@univ-usto.dz (B. Ouadi), a.khatir@pm.univpm.it, abdelwahhab.khatir@univ-usto.dz (A. Khatir).

<sup>\*</sup> Corresponding author.

<sup>\*\*</sup> Correspondence to: A. Khatir, Civil Engineering Department, University of Sciences and Technologies Mohamed Boudiaf of Oran (USTO-MB), 1505, EL MNAOUER, 31000 Oran, Algeria.

mitigating membrane fouling in water treatment systems [[2](#page-12-0)]. CEOP refers to the increased osmotic pressure that results from the accumulation of particulate matter on the membrane surface, which can exacerbate fouling by further reducing permeate flow. Only after the CEOP's influence on RO fouling rates was recognized did indices like CFS-MFIUF and FFM start incorporating this factor [\[3](#page-12-0)–5].

SDI was the earliest fouling index to receive standardization from the American Society for Testing and Materials (ASTM) among several available indices [[6](#page-12-0)]. It quickly became the most widely utilized metric for assessing the fouling potential of RO feedwater due to its ability to deliver results swiftly with minimal equipment [7–[9\]](#page-12-0) The SDI measures the filterability of feedwater by analyzing the decline in flux, making it particularly suitable for water with low fouling potential, like pretreated water destined for RO or nanofiltration (NF). The recommended SDI limits for RO feedwater can vary depending on the membrane manufacturer or specific guidelines provided with the RO membranes [\[5,10](#page-12-0)].

However, the SDI's reliance on a 0.45 μm nominal microfiltration (MF) membrane limits its effectiveness in detecting foulants smaller than this threshold [[11\]](#page-12-0). Additionally, smaller particles that bypass the SDI measurement can still contribute to fouling on the RO membranes. In response to these limitations, researchers have developed enhanced fouling metrics, including the modified fouling index (MFI) [[12\]](#page-12-0), crossflow sampler-modified fouling index (CFS-MFI) [\[2\]](#page-12-0), combined fouling index (CFI) [\[13](#page-12-0)], and multiple membrane array system (MMAS) [\[14](#page-12-0)]. The MFI, derived from a membrane filtration model, considers different filtration mechanisms such as blocking, cake formation, and depth filtration. The CFS-MFI, on the other hand, operates under hydrodynamic conditions similar to those in an RO module, allowing for more accurate simulation of particle deposition before measurement [[15\]](#page-12-0).

Despite these advancements, the inability of these indices to fully capture foulants smaller than 0.45 μm has hindered their broader application. To address this, indices based on membranes with smaller pore sizes, such as ultrafiltration (UF) or nanofiltration (NF) membranes, have been introduced [\[16](#page-12-0)–18]. For instance, the CFI employs a combination of three distinct membranes hydrophilic MF, hydrophobic MF, and hydrophilic UF to predict the fouling potential across a range of particle sizes in RO processes [\[19\]](#page-12-0). Similarly, the MMAS integrates MF, UF, and NF membranes in a series within a single process, allowing for comprehensive assessment of the fouling potential of particles, colloids, and organic materials during NF or RO operations [\[20](#page-12-0)[,21](#page-13-0)]. Although these advanced indices offer improved accuracy, their complexity and the specialized equipment required for their implementation have limited their widespread adoption. Consequently, the SDI remains the most commonly used parameter for evaluating fouling in practical applications.

# *1.2. Research gaps, objectives, and contributions*

Artificial Intelligence (AI) is transforming the water treatment and seawater desalination industries by addressing key challenges such as performance instability and high energy consumption [22–[24\]](#page-13-0). Despite efforts to reduce costs, these issues persist due to fluctuations in feed stream quality. AI offers innovative solutions, including self-adaptive flux enhancement and real-time optimization, to maintain stable performance and improve efficiency in water treatment processes [\[25](#page-13-0)]. These AI methodologies include a variety of approaches, such as Artificial Neural Networks (ANN) [\[26](#page-13-0)–28], Adaptive Neuro-Fuzzy Inference Systems (ANFIS) [\[29](#page-13-0)–31], genetic programming [\[32,33](#page-13-0)], and Gradient Boosting [[34,35](#page-13-0)].

Nasir et al. [\[36](#page-13-0)] evaluated various AI algorithms, including gradient boosting, to improve water quality classification. Using a nine-year dataset, the CATBoost model achieved 94.51 % accuracy, and when combined in a stacking ensemble, accuracy reached 100 %. The results suggest boosting algorithms are highly effective for reliable water quality prediction. Mahanna et al. [\[37](#page-13-0)] evaluated Machine Learning (ML) models to predict key water quality indicators at a Saudi

wastewater treatment plant. Random Forest (RF) excelled in predicting COD and SS, while Gradient Boosting (GB) was most accurate for BOD. These findings suggest that ensemble models like RF and GB are effective tools for modeling wastewater treatment performance. Bagherzadeh et al. [[38\]](#page-13-0) assesses the impact of seven feature selection methods on predicting total nitrogen (TN) in wastewater using machine learning models. The Gradient Boosting Machine (GBM) outperformed other models like, ANN and Random Forest (RF), especially when using features suggested by Mutual Information, demonstrating its effectiveness in wastewater prediction tasks. Zhang et al. [\[39](#page-13-0)] developed a novel method called Miss-GBRT to accurately impute missing wastewater quality data, even with limited training data. They found that Miss-GBRT outperforms traditional imputation methods, particularly in scenarios with significant data gaps. Tabari et al. [\[40](#page-13-0)] investigated the effectiveness of multi-layer perceptron (MLP) and radial basis function (RBF) neural networks in reconstructing missing data for 13 water quality parameters, using datasets from five monitoring stations along Iran's Maroon River. Helm et al. [\[41](#page-13-0)] applied ML, specifically a CatBoost method, to improve the forecasting of free chlorine residual (FCR) in a full-scale drinking water treatment system in Georgia, USA. They found that the ML model achieved high predictive accuracy (R2 = 0.937) and revealed that standard operating parameters, though not intuitively linked to FCR, significantly enhanced the model's performance. Several applications of ML can be found in researches like [42–[47\]](#page-13-0).

Deep learning techniques have shown transformative potential in water management applications, including water demand forecasting, leakage detection, and wastewater system monitoring, although practical implementation remains limited and faces challenges related to data privacy and algorithmic trustworthiness [[48\]](#page-13-0). Recent advancements in water management have employed smart water meters with IoT-based data collection and analysis systems, utilizing techniques such as Long Short-Term Memory (LSTM) for real-time water demand forecasting. This approach not only enables optimal management of water resources but also provides a scalable solution for broader water infrastructure applications [\[49](#page-13-0)]. LSTM was used for water demand prediction as well in optimal pump control [[50\]](#page-13-0). Fang et al. [[51\]](#page-13-0) utilized Convolutional Neural Networks (CNNs) trained on pressure data to detect leakage events across multiple points in a Water Distribution System (WDS). Their study involved training six CNN models on manually labeled data collected from a laboratory-based WDS, achieving an accuracy of 97.33 % with 21 pressure sensors and 92.11 % with 8 sensors, highlighting the effectiveness of CNNs in identifying leakage under varying sensor conditions. CNNs are the predominant deep learning approach for leakage detection, utilizing flow, pressure, acoustic, or vibration data to identify anomalies. Research in this area has largely focused on enhancing detection by optimizing training data size and format transformation [\[48](#page-13-0)]. Islam et al. [[34\]](#page-13-0) developed a water quality prediction model by applying principal component regression and GB Classifier techniques, achieving 95 % prediction accuracy and 100 % classification accuracy on a Gulshan Lake dataset. The approach effectively combines PCA for parameter extraction with advanced classification to provide robust water quality assessments.

In this study, we evaluated the performance of Gradient Boosting models for predicting Silt Density Index (SDI) values over a one-month period using pressure measurements as input features from the Benisaf and El Mactaa desalination plants in western Algeria. Three variants of Gradient Boosting were compared: Gradient Boosting alone (GB), Gradient Boosting combined with Particle Swarm Optimization (GBPSO), and Gradient Boosting combined with Salp Swarm Algorithm (GBSSA). The results indicate that the GBSSA model outperformed both GB and GBPSO, demonstrating superior predictive accuracy, making it a promising approach for SDI prediction in desalination systems.

#### *1.3. Layout*

This manuscript is organized as follows: [Section 1](#page-0-0) provides an

introduction with background and motivation, highlights research gaps, objectives, and contributions, and presents the overall layout of the paper. Section 2 describes the datasets used in the study, covering data sources, collection methods, and key characteristics. [Section 3](#page-3-0) details the methodology, including the GB model, the SSA, and the hybridization of these two approaches. [Section 4](#page-5-0) presents the experimental results for the Benisaf and El Mactaa desalination plants, discusses evaluation metrics, and highlights valuable outcomes. Finally, [Section 5](#page-11-0) concludes the study, summarizing the key findings and suggesting directions for future research."

#### **2. Data collection**

This study involves data collection from two desalination plants located in western Algeria which are Beni Saf and El Mactaa desalination plants. Detailed technical specifications for both plants are provided in Tables 1 and 2 and [Fig. 1](#page-3-0) illustrates a view of considered plants. The data collected includes various operational parameters and performance metrics, such as daily pressure readings and SDI values. Pressure data is utilized for training predictive models, while SDI values are used to validate these predictions. In real-world desalination systems, SDI is influenced by multiple factors, including water quality, temperature, and fouling agents. However, pressure is a critical operational parameter that directly impacts membrane performance and fouling rates. Moreover, pressure is easier to measure due to its simpler equipment and realtime capabilities. It involves fewer steps, less manual intervention, and lower maintenance requirements.

By focusing on pressure, the study aims to simplify the model while still capturing significant variations in SDI. This approach allows for a more controlled analysis and can highlight how pressure variations alone affect SDI predictions. By analyzing these specifications and model predictions, the study aims to provide a comprehensive understanding of the operational capabilities and challenges faced by each desalination facility in the region and to enhance the predictive accuracy of performance metrics based on the operational data.

# *2.1. Data characteristics and analysis*

To assess the suitability of pressure as an input variable for predicting SDI, a detailed exploratory data analysis (EDA) was conducted.

#### *2.1.1. Distribution analysis*

The distribution of pressure values across both plants revealed significant variation due to changes in operational conditions. The pressure data follows a relatively normal distribution with minor skewness observed in specific periods of operation, particularly during peak

**Table 1**  Specifications of Benisaf desalination plant.

| Item                          | Description                                                       |
|-------------------------------|-------------------------------------------------------------------|
| Geographical location         | Beni Saf, Ain T´emouchent State                                   |
| Owner                         | Beni Saf Water Company SPA.                                       |
| Builder                       | Ute desaladora beni saf construction                              |
| Treatment process             | Reverse Osmosis                                                   |
| Production capacity           | 200,000 m3<br>/d                                                  |
| Power consumption             | 4.15 kwh/m3                                                       |
| Project amount                | 240 million \$                                                    |
| Composition of the<br>station | 10 desalination units                                             |
| Product water quality         | alkalinity <65 mg, hardness 50–65 mg, pH 8–8.5, loin index<br>0.4 |
| chemical pre                  | Sodium Hypochlorite, Ferric Chloride, Sulfuric Acid,              |
| treatments                    | Sodium Metabisulphite, Dispersant.                                |
| Price of water<br>produced    | 0.6994 \$/m3                                                      |
| Date of<br>commissioning      | March 2010                                                        |

**Table 2**  Specifications of El Mactaa desalination plant.

| Item                             | Description                                                               |
|----------------------------------|---------------------------------------------------------------------------|
| Geographical location            | Mers El Hadjadj, Oran State                                               |
| Production capacity              | 500,000 m3<br>/d                                                          |
| Destination of produced<br>water | Oran State                                                                |
| Number of modules                | 25 units of 20,000 m3<br>/d each                                          |
| Desalination technology          | Reverse osmosis                                                           |
| Electricity consumption          | ≤ 4.15 kwh/m3                                                             |
| Mechanical pretreatments         | Ultrafiltration                                                           |
| Chemical pre-treatments          | Sodium hypochlorite, sulfuric acid, sodium<br>metabisulphite, dispersant. |
| Product treatment post           | Calcium carbonate- sodium hypochlorite                                    |
| Project amount                   | 492 million \$                                                            |
| Price of water produced          | 0.5577 \$/m3                                                              |
| Date of commissioning            | July 10, 2016                                                             |

demand times. The SDI values exhibit a more skewed distribution, reflecting the sensitivity of SDI to variations in feedwater quality and membrane fouling.

# *2.1.2. Correlation analysis*

A correlation analysis was performed to assess the relationship between pressure and SDI. The results indicate a strong negative correlation between pressure and SDI in both plants, supporting the use of pressure as a key predictor of SDI. Specifically, higher pressure values generally correspond to lower SDI values, which aligns with operational expectations, as well-maintained pressure helps reduce membrane fouling.

#### *2.1.3. Limitation of using pressures alone*

Although pressure is an effective predictor, it may not capture the full complexity of factors influencing SDI. Other variables, such as feedwater temperature, salinity, and turbidity, could also impact membrane fouling and SDI values. However, incorporating these variables was beyond the scope of this study due to data availability constraints. Future research could explore multivariate models that integrate additional parameters to improve predictive accuracy.

# *2.2. SDI and Pressure measurement*

The Silt Density Index (SDI) is a key parameter used to assess the quality of water after the pre-treatment process in desalination systems. It provides an indication of suspended solids and helps in predicting the potential fouling of reverse osmosis (RO) membranes. Although a high SDI value indicates a higher level of particulates in the water, it does not always directly correlate with actual membrane fouling. However, it remains a valuable tool for predicting the likelihood of fouling and is widely used in practice [\[52](#page-13-0)].

The SDI is determined by filtering a water sample through a 0.45 μm membrane and measuring the rate of flux decline over time. Specifically, SDI is calculated based on the initial filtration time (*Ti*) and the time after 15 min of filtration (*Tf*), following the Eq. (1):

$$SDI_{T} = \frac{\left[1 - \frac{t_{i}}{t_{f}}\right] \bullet 100}{T} \tag{1}$$

where *T* is the total time, *ti* is the first time required for filling the 500 ml for *t* = 15 min, and *tf* is second time required for filling the 500 ml.

In addition to SDI, monitoring pressure is also crucial in desalination systems. We have collected daily measurements of both SDI and pressure over a one-month period, with results detailed in [Table 3](#page-3-0). SDI, measured using a 0.45 μm filter, provides insight into the quality of filtered water and helps predict potential membrane fouling.

The pressure measurements used in this study were collected directly from the pre-treatment stage of the desalination plants, where pressure

<span id="page-3-0"></span>![](_page_3_Picture_2.jpeg)

![](_page_3_Picture_3.jpeg)

**Fig. 1.** Desalination plants of Benisaf and El Mactaa.

**Table 3**  SDI and Pressure values measured over one month for Benisaf and El Mactaa desalination plants.

| Items           | Margin of error |         |      |      |      |      |      |      |      |      |      |      |
|-----------------|-----------------|---------|------|------|------|------|------|------|------|------|------|------|
| Days            |                 |         | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 10   |
|                 | Pressure (bar)  | ± 0.016 | 10.1 | 10.5 | 9.4  | 9.5  | 10   | 12   | 11   | 9.9  | 8.3  | 10   |
| Beni Saf Plant  | SDI             | ± 0.05  | 1.8  | 1.8  | 1.7  | 1.7  | 1.7  | 1.9  | 1.8  | 1.7  | 1.6  | 1.7  |
|                 | Pressure (bar)  | ± 0.016 | 14.5 | 13.5 | 13   | 13.3 | 12.5 | 12.9 | 15   | 7    | 5.5  | 9.4  |
| El Mactaa Plant | SDI             | ± 0.05  | 2.46 | 2.04 | 2.22 | 2.38 | 1.95 | 2.02 | 2.56 | 1.41 | 0.99 | 1.75 |
| Days            |                 |         | 11   | 12   | 13   | 14   | 15   | 16   | 17   | 18   | 19   | 20   |
| Beni Saf Plant  | Pressure (bar)  | ± 0.016 | 11.5 | 11   | 8.5  | 8.5  | 9.3  | 10   | 9    | 7.5  | 11   | 10.5 |
|                 | SDI             | ± 0.05  | 1.8  | 1.7  | 1.6  | 1.6  | 1.7  | 1.7  | 1.6  | 1.5  | 1.7  | 1.7  |
|                 | Pressure (bar)  | ± 0.016 | 9    | 10.5 | 10.7 | 13.5 | 9.5  | 9.5  | 9    | 8.6  | 9.5  | 9.5  |
| El Mactaa Plant | SDI             | ± 0.05  | 1.60 | 1.82 | 1.88 | 2.06 | 1.75 | 1.41 | 2.39 | 2.74 | 2.33 | 2.17 |
| Days            |                 |         | 21   | 22   | 23   | 24   | 25   | 26   | 27   | 28   | 29   | 30   |
| Beni Saf Plant  | Pressure (bar)  | ± 0.016 | 11   | 11.5 | 10   | 10.5 | 13   | 12.5 | 11.3 | 9.5  | 10.3 | 10.5 |
|                 | SDI             | ± 0.05  | 1.7  | 1.8  | 1.7  | 1.7  | 1.9  | 1.9  | 1.8  | 1.7  | 1.7  | 1.7  |
| El Mactaa Plant | Pressure (bar)  | ± 0.016 | 13.2 | 8    | 14.9 | 7    | 7.5  | 8.9  | 10   | 13.5 | 10.5 | 8    |
|                 | SDI             | ± 0.05  | 1.95 | 1.6  | 2.5  | 1.42 | 1.57 | 1.67 | 1.87 | 1.99 | 1.82 | 1.6  |

sensors are installed to monitor the operational pressure levels before water enters the filtration stage. These sensors provide real-time pressure data, which is critical for assessing the performance of the membranes and predicting SDI values. The pressure data is continuously monitored and recorded to reflect daily operational conditions. While SDI is a straightforward tool for assessing fouling risk, pressure data is invaluable for detecting anomalies such as changes in fouling or membrane blockages. Together, these measurements are essential for optimizing system performance, predicting maintenance needs, and ensuring efficient operation of desalination facilities. [Fig. 2](#page-4-0) illustrate a flowchart of SDI measurement method and tools, and [Fig. 3](#page-5-0) illustrate the equipment used for SDI measurement in both desalination plants.

### *2.3. Data preprocessing*

Before training the models, the data underwent a preprocessing phase to ensure its quality and suitability for predictive modeling. First, missing data points were identified and imputed using linear interpolation methods. To address potential outliers, a robust *Z*-score method was applied, removing data points that deviated more than three standard deviations from the mean. This ensures the model is not overly influenced by anomalous readings. The data was then normalized to a [0,1] scale to improve the convergence of the GB and SSA models during training. Finally, a random 70/30 split was used to partition the dataset into training and test sets, ensuring that the model was evaluated on unseen data.

#### **3. Methodology**

This section outlines the approach and techniques employed to predict SDI values, focusing on the use of GB models with pressure data as input. This section details the development, optimization, and evaluation of the models, including GB, and GBSSA variants.

The choice of GB for this study is based on its proven effectiveness in handling regression tasks with tabular data, especially in capturing nonlinear relationships between input variables. GB constructs a series of weak learners, typically decision trees, that progressively focus on correcting the residuals of previous iterations, leading to highly accurate models. Compared to other Machine Learning techniques, GB is known for its robustness and ability to minimize both bias and variance.

The SSA was chosen as an optimization algorithm due to its excellent exploration and exploitation capabilities, which are critical for finetuning the hyperparameters of the GB model. SSA offers an effective balance between global search (exploration of the solution space) and local search (refining existing solutions). Compared to other optimization algorithms like PSO, SSA has demonstrated superior performance in handling complex optimization tasks with fewer computational resources. This makes SSA particularly suitable for hybridization with GB, ensuring better convergence and reduced prediction error.

# *3.1. Gradient Boosting*

Gradient Boosting (GB) is an advanced machine learning method widely applied in both regression and classification tasks. It constructs a series of decision trees in a step-by-step manner, with each tree focusing

<span id="page-4-0"></span>![](_page_4_Figure_2.jpeg)

**Fig. 2.** Flowchart of SDI measurement method and tools.

on addressing the mistakes made by its predecessor. The essential elements of GB consist of:

- 1. **Base Learner**: Typically, shallow decision trees (also known as weak learners) are used.
- 2. **Loss Function**: A differentiable loss function that quantifies model's prediction error.
- 3. **Boosting**: The algorithm sequentially fits new trees to the residual errors of the previous trees, updating the model to minimize the loss function.
- 4. **Learning Rate**: Regulates the influence of each added tree on the overall model, aiding in minimizing overfitting.

The model is trained by iteratively adding trees to the ensemble. Each new tree is trained to predict the residuals or errors of the combined prediction from all previous trees. The final model is a weighted sum of all trees, leading to improved prediction accuracy.

The GB algorithm updates the model by fitting new trees to the residuals of the predictions from previous trees. The prediction update for a given iteration mmm is given by following Eq. (2) [\[53](#page-13-0)]:

$$F_m(x) = F_{m-1}(x) + \eta h_m(x)$$
 (2)

where *Fm*(*x*) is the model prediction after mmm iterations, *Fm*<sup>−</sup> <sup>1</sup>(*x*) is the model prediction after *m* − *1* iterations, *η* is the learning rate, and *hm (x)*  is the prediction of the new tree at iteration *m*.

# *3.1.1. Objective function*

The loss function used in GB is minimized during training. For

regression problems, a common loss function is the Mean Squared Error (MSE):

$$L(y, \hat{y}) = \frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2$$
 (3)

where *yi* is the actual value, ̂*yi* is the predicted value and *N* is the number of samples.

## *3.2. Salp Swarm Algorithm (SSA)*

Salp Swarm Algorithm (SSA) is a metaheuristic optimization algorithm inspired by the swarming behavior of salps, a type of marine organism. SSA is used for solving optimization problems by mimicking the social behavior and movement patterns of salps in the ocean [\[54](#page-13-0)]. Key aspects of SSA include:

- 1. **Salps**: Represent solutions in the search space, with their movement determined by the fitness of the solutions.
- 2. **Swarm Behavior**: Salps move in a swarm to explore the search space, with the goal of finding optimal solutions by balancing exploration and exploitation.
- 3. **Objective Function**: Salps update their positions based on the objective function value, aiming to find the best solution.
- 4. **Global and Local Search**: The algorithm combines global search (exploring new areas) and local search (refining solutions) to improve convergence.

In SSA, the position of each salp (solution) is updated based on its

<span id="page-5-0"></span>![](_page_5_Picture_2.jpeg)

Fig. 3. Measurement equipment for SDI in Benisaf and El Mactaa desalination plants.

fitness and the fitness of other salps. The position update equation is:

$$X_i^{t+1} = X_i^t + \alpha. \left( X_g^t - X_i^t \right) \tag{4} \label{eq:4}$$

where  $X_i^{t+1}$  is the updated position of salp i at iteration t+1,  $X_i^t$  is the current position of salp i at iteration t,  $X_g^t$  is the global best position found by the swarm at iteration t, and  $\alpha$  is a step size parameter controlling the influence of the global best position.

#### 3.3. Hybridization of Gradient Boosting and Salp Swarm Algorithm

The hybridization of GB with the SSA aims to optimize the model by fine-tuning critical hyperparameters such as the learning rate, the number of estimators, and the maximum depth of trees in Gradient Boosting. The process begins by initializing a population of salps, each representing a possible set of hyperparameters for Gradient Boosting. SSA is used to explore and exploit the hyperparameter space, iteratively updating salp positions based on their fitness measured as the Mean Absolute Error (MAE) or Mean Squared Error (MSE) of the GB model. The goal is to minimize the error while ensuring optimal convergence.

The hybrid approach involves three main steps:

- 1. **Initialization**: A population of salps is generated with random hyperparameter values (learning rate, number of estimators).
- 2. **Evaluation**: Each salp's hyperparameters are used to train a Gradient Boosting model, and the fitness (error) is calculated.
- Optimization: SSA updates the hyperparameter values for the next iteration based on the fitness scores, refining the model with each cycle.

The final optimized hyperparameters are those that yield the lowest error. This hybrid method allows for a balance between global exploration (searching broadly for possible solutions) and local exploitation (refining the best solutions). The tuned hyperparameters include the learning rate  $(\eta)$ , number of trees, and tree depth (max\_depth). These parameters were chosen because they directly affect the model's complexity, convergence speed, and accuracy.

#### 3.3.1. Objective function for hybrid GBSSA

The objective function to be minimized during the optimization process could be the MAE or any other evaluation metric. The SSA minimizes the MAE of the GB model by finding the optimal hyperparameters:

Objective Function :  $min MAE (F_m(x, X_i))$ 

where  $Xi = [NumTrees_i \ LearningRate_i]$  is the vector of hyperparameters (number of trees and learning rate) for salp i, and  $MAE \ (F_m(x,X_i))$  is the Mean Absolute Error of the GB model using the hyperparameters  $X_i$ .

After running the SSA for T iterations, the best hyperparameters  $X_{\sigma}^{T}$  are used to train the final GB model with Eq. (5):

$$F_{\text{final}}(x) = GB\left(x, X_g^T\right) \tag{5}$$

where  $F_{final}$  (x) is the final trained GB model with the optimal hyper-parameters  $X_{\sigma}^{T}$ .

Fig. 4 presents a flowchart illustrating the hybridization process, beginning with the initialization of salps, followed by model training, evaluation, and hyperparameter optimization through SSA. This step-by-step visual representation clarifies the hybrid modeling workflow.

#### 4. Results and discussion

In this study, we applied the Gradient Boosting combined with Salp Swarm Algorithm (GBSSA) to predict the SDI values over a one-month period. The proposed approach utilizes pressure measurements as input features and aims to forecast SDI values, which serve as the output. For comparison, we also evaluated the performance of GB combined

<span id="page-6-0"></span>![](_page_6_Figure_2.jpeg)

**Fig. 4.** GBSAA approach flowchart.

with Particle Swarm Optimization (GBPSO) and GB alone.

The data used for model training and evaluation are detailed in [Table 3,](#page-3-0) which includes daily SDI and pressure values collected over the month. The performance of each model was assessed based on prediction accuracy, with GBSSA demonstrated to offer superior results compared to the GBPSO and GB approaches.

Breakdown of the typical modeling parameters considered for each

**Table 4**  Parameters setting for considered algorithms.

| Parameter                   | Gradient<br>Boosting (GB) | Particle Swarm<br>Optimization (PSO) | Salp Swarm<br>Algorithm (SSA) |
|-----------------------------|---------------------------|--------------------------------------|-------------------------------|
| Number of Trees             | 100                       | N/A                                  | N/A                           |
| Learning Rate               | 0.1                       | N/A                                  | N/A                           |
| Maximum Depth<br>of Trees   | 3                         | N/A                                  | N/A                           |
| Subsample                   | 0.8                       | N/A                                  | N/A                           |
| Min Samples Split           | 2                         | N/A                                  | N/A                           |
| Population Size             | N/A                       | 50                                   | 50                            |
| Max Iterations<br>(PSO/SSA) | N/A                       | 100                                  | 100                           |
| Inertia Weight              | N/A                       | 0.7                                  | N/A                           |
| Step Size                   | N/A                       | N/A                                  | 0.2                           |
| Convergence                 | Fixed after 100           | Based on error                       | Based on error                |
| Criteria                    | estimators                | minimization                         | minimization                  |

algorithm are displayed in Table 4.

# *4.1. Benisaf desalination plant*

[Figs. 5 and 6](#page-7-0) display the prediction performance of SDI values for the Benisaf desalination plant using the three models: GB, GBSSA, and GBPSO. [Fig. 5](#page-7-0) presents the prediction plots, showcasing the SDI value forecasts generated by each model, while [Fig. 6](#page-8-0) illustrates the train and test plots for each model. These plots provide a visual assessment of how well each model fits the training data and generalizes to unseen test data, offering insight into their predictive performance and potential for accurate forecasting.

The standard GB model provided a baseline for our analysis. While it achieved acceptable accuracy in predicting SDI values, its performance was limited by the inherent tuning parameters and optimization techniques available within the standard GB framework.

The integration GBPSO led to improvements in model performance compared to the standard GB approach. PSO's optimization capabilities enhanced the tuning of GB parameters, resulting in better predictive accuracy and more robust model performance.

The most significant improvements were observed with the GB model optimized by the SSA. The GBSSA approach outperformed both GB and GBPSO in terms of prediction accuracy. The SSA's optimization capabilities provided superior parameter tuning, leading to the best

<span id="page-7-0"></span>![](_page_7_Figure_2.jpeg)

**Fig. 5.** Prediction performance of SDI in Benisaf desalination plant using GB, GBSSA, and GBPSO models.

<span id="page-8-0"></span>![](_page_8_Figure_2.jpeg)

**Fig. 6.** Train and Test performance of SDI prediction in Benisaf desalination plant using (a) GB, (b) GBSSA, and (c) GBPSO models.

![](_page_8_Figure_4.jpeg)

**Fig. 7.** Actual and predicted SDI for Benisaf plant using GB, GBSSA, and GBPSO.

<span id="page-9-0"></span>results among the models tested. This indicates that GBSSA effectively captured the complex patterns in the data and improved the model's ability to predict SDI values accurately.

The train and test plots for each model variant illustrate the predictive performance over the training and validation phases.

The train and test plots for GB alone showed moderate alignment between predicted and actual SDI values, with some discrepancies indicating room for improvement in model accuracy. The GBPSO model exhibited better alignment between predicted and actual values compared to GB alone, reflecting the effectiveness of PSO in optimizing Gradient Boosting parameters.

The train and test plots for GBSSA displayed the closest alignment

with actual SDI values. The minimal deviations between predicted and observed values highlight the superior performance of GBSSA. This suggests that the Salp Swarm Algorithm provided the most effective optimization, capturing the nuances in the data more accurately than GBPSO and GB alone.

[Fig. 7](#page-8-0) illustrate the comparison between the actual and predicted SDI values in Benisaf desalination plant for the GB, GBSSA, and GBPSO models.

#### *4.2. El Mactaa dessalination plant*

Figs. 8 and 9 display the prediction performance of SDI values for the

![](_page_9_Figure_10.jpeg)

**Fig. 8.** Prediction performance of SDI in El Mactaa desalination plant using GB, GBSSA, and GBPSO models.

<span id="page-10-0"></span>![](_page_10_Figure_2.jpeg)

**Fig. 9.** Train and Test performance of SDI prediction in El Mactaa desalination plant using (a) GB, (b) GBSSA, and (c) GBPSO models.

El Mactaa desalination plant using the considered three models: GB, GBSSA, and GBPSO. [Fig. 8](#page-9-0) presents the prediction plots, showcasing the SDI value forecasts generated by each model, while Fig. 9 illustrates the

train and test plots for each model.

The enhanced performance of GBSSA can be attributed to the Salp Swarm Algorithm's efficient exploration of the parameter space, leading

![](_page_10_Figure_7.jpeg)

**Fig. 10.** Actual and predicted SDI in El Mactaa Plant using GB, GBSSA, and GBPSO.

<span id="page-11-0"></span>to optimal model settings that significantly improve prediction accuracy. This result underscores the value of advanced optimization techniques in refining machine learning models, particularly for complex prediction tasks such as SDI forecasting.

The comparative analysis demonstrates that while both GBPSO and GBSSA offer improvements over the standard GB model, GBSSA provides the most accurate and reliable predictions. This can be attributed to the superior optimization capabilities of the Salp Swarm Algorithm, which appears to be more effective in tuning the GB model parameters for this specific application.

[Fig. 10](#page-10-0) illustrate the comparison between the actual and predicted SDI values in El Mactaa desalination plant for the GB, GBSSA, and GBPSO models.

The superior performance of GBSSA can be attributed to the strengths of the SSA in effectively searching the hyperparameter space. SSA's ability to balance exploration and exploitation ensures a more thorough optimization of GB's hyperparameters, leading to reduced prediction error. By comparison, GBPSO offers less effective global search capabilities, often resulting in suboptimal tuning. Standard GB, without any optimization, suffers from fixed hyperparameters, limiting its ability to adjust to the complexity of the data. The optimized hyperparameters found through SSA allow GBSSA to capture subtle patterns in the data, leading to more accurate SDI predictions, particularly in fluctuating operational conditions.

The GBSSA model was trained and tested on SDI values ranging from 1.5 to 2.5. Based on the evaluation metrics, the model shows high predictive accuracy within this range. Predicting SDI values outside this range may require further training with more diverse data, as the model's accuracy could decrease when extrapolating beyond the limits of the training set.

# *4.3. Evaluation metrics*

To assess the performance of the Gradient Boosting models in predicting SDI values, we utilized four evaluation metrics: Root Mean Square Error (RMSE), Mean Absolute Error (MAE), the coefficient of determination (R2 ), and Mean Absolute Percentage Error (MAPE). Table 5 outlines the errors for each GB model. These metrics collectively provide a comprehensive evaluation of model performance, with lower RMSE and MAE values and a higher R2 value indicating better predictive accuracy.

Results in Table 5 show that the Gradient Boosting model optimized with SSA performs best across all metrics, with the lowest MAE, RMSE, and MAPE, and the highest R2 . This indicates superior accuracy and precision, particularly in minimizing both absolute and percentage errors.

The GBPSO model also shows good performance but with slightly higher errors and a lower R2 than GBSSA. Its MAPE reflects a higher percentage error, indicating it is less effective in capturing fine variations compared to GBSSA.

The standard GB model, however, has the highest error metrics and the lowest R2 , making it the least accurate. Its high MAPE underscores its difficulty in handling relative errors, making it less suitable for accurate SDI predictions.

For real-world desalination operations, these improvements

**Table 5**  Evaluation metrics for GB models for SDI prediction in Benisaf and El Mactaa plants.

|           |       | MAE      | RMSE     | R2      | MAPE (%) |
|-----------|-------|----------|----------|---------|----------|
|           | GB    | 0.048986 | 0.070172 | 0.13647 | 69.8     |
| Benisaf   | GBSSA | 0.005617 | 0.008996 | 0.98879 | 62       |
|           | GBPSO | 0.009387 | 0.015127 | 0.96208 | 62.4     |
|           | GB    | 0.256980 | 0.335280 | 0.42925 | 76.6     |
| El Mactaa | GBSSA | 0.060048 | 0.086527 | 0.96526 | 69.4     |
|           | GBPSO | 0.062448 | 0.086981 | 0.95059 | 71.8     |

translate to more reliable forecasts of SDI values, allowing plant operators to make timely adjustments to prevent fouling. The lower RMSE and MAPE values achieved by GBSSA reduce the risk of underestimating fouling rates, which can lead to costly maintenance interventions. Accurate SDI predictions enable better planning for membrane cleaning schedules, optimizing the balance between operational efficiency and cost.

When selecting an appropriate method, researchers must consider the dataset size, computational resources, and the specific prediction task. For small to medium-sized tabular datasets, GB provides a solid baseline due to its ability to model non-linear relationships. However, GB's performance is highly dependent on proper hyperparameter tuning, which can be efficiently managed by integrating optimization techniques. The GBSSA model outperforms GB and GBPSO because SSA's exploration-exploitation balance ensures superior hyperparameter tuning, reducing prediction error.

In contrast, GBPSO, while effective, demonstrates slightly higher errors due to less optimal search strategies. For researchers working with datasets similar to this study (moderate size, with well-understood features), GBSSA offers the best combination of accuracy and efficiency. On the other hand, if researchers have access to significantly larger datasets, deep learning algorithms may be more suitable, although they require greater computational resources and careful tuning to prevent overfitting.

## *4.4. Convergence performance comparison*

To demonstrate the convergence performance of the optimization algorithms, [Table 6](#page-12-0) presents the fitness values for PSO and SSA, which were used to optimize the Gradient Boosting model, across different iterations. The fitness values, represented by MAE (Mean Absolute Error) as the objective function to be minimized, show that SSA consistently achieves faster convergence and lower final MAE values in both the Benisaf and El Mactaa cases. For example, in the Benisaf case, SSA achieves a final MAE of 0.005617, while PSO converges to a higher MAE of 0.009387. Similarly, in the El Mactaa case, SSA demonstrates superior performance with a final MAE of 0.060048, outperforming the PSO result of 0.062448.

# **5. Conclusion**

This study introduces a novel approach for predicting Silt Density Index (SDI) values in desalination systems by combining Gradient Boosting (GB) with the Salp Swarm Algorithm (GBSSA). The integration of GBSSA enhances the predictive accuracy of SDI values over a onemonth period. Data collected from two desalination plants in western Algeria Benisaf and El Mactaa were used to train and validate the models, with pressure measurements serving as the primary input due to their critical role in influencing membrane performance and fouling rates.

The study compared three variants of GB: the standard GB model GB, Gradient Boosting optimized with Particle Swarm Optimization (GBPSO), and the proposed GBSSA model. Results demonstrated that the GBSSA model significantly outperformed both GB and GBPSO, achieving superior accuracy in predicting SDI values. This capability is vital for effective monitoring and management of membrane fouling in desalination plants, where accurate SDI predictions allow for timely operational adjustments and maintenance, thereby improving system performance and reducing long-term costs.

In practical terms, the GBSSA model holds promise for optimizing desalination plant operations by enhancing decision-making and potentially reducing operational costs. Its ability to improve predictive accuracy means that plant operators can make more informed decisions regarding maintenance schedules and operational settings, contributing to more sustainable and efficient water treatment practices.

While this study presents promising results, several limitations

<span id="page-12-0"></span>**Table 6**  Convergence for each algorithm performance.

| Desalination plant | Optimization |                    | Fitness following number of iterations |                    |                    |                    |                    |                    |  |  |
|--------------------|--------------|--------------------|----------------------------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--|--|
|                    |              | 1                  | 10                                     | 20                 | 30                 | 50                 | 70                 | 100                |  |  |
| Benisaf            | SSA          | 0.08240            | 0.05194                                | 0.03000            | 0.02456            | 0.01050            | 0.00911            | 0.00561            |  |  |
|                    | PSO          | 0.09601            | 0.07305                                | 0.05099            | 0.03545            | 0.02417            | 0.01100            | 0.00938            |  |  |
| El Mactaa          | SSA<br>PSO   | 0.20044<br>0.25904 | 0.15033<br>0.26565                     | 0.10765<br>0.15065 | 0.08456<br>0.10344 | 0.07165<br>0.08049 | 0.06279<br>0.07853 | 0.06004<br>0.06244 |  |  |

should be acknowledged. The data used for training the model was collected from two desalination plants, which may limit the generalizability of the findings to other plants with different operational conditions, water sources, or treatment processes. Additionally, potential biases in data collection, such as the reliance on pressure as the sole input variable, could impact the model's performance under varied operational stresses. Finally, while the implementation of AI-based models like GBSSA can potentially reduce operational costs and energy consumption, the long-term environmental impact of such technologies in desalination processes requires further exploration.

In conclusion, the superior performance of the GBSSA model demonstrates the potential of combining advanced Machine Learning techniques with optimization algorithms for predictive modeling in critical industrial processes. This study sets the stage for future research into hybrid machine learning techniques that could revolutionize operational efficiency and decision-making in desalination plants, fostering long-term sustainability in water treatment practices.

#### *5.1. Future work*

Future research could extend the model by incorporating additional operational parameters, such as temperature, water quality metrics (e. g., salinity and turbidity), and chemical dosing rates, which may further improve predictive performance. Additionally, applying the methodology across different geographical locations and types of desalination systems would help validate its robustness and adaptability to varied operational conditions.

To enhance the practical applicability of the GBSSA model, future studies should consider gathering qualitative insights from industry stakeholders, including plant operators and environmental regulators. Interviews or surveys could provide valuable feedback on the model's real-world implementation, operational acceptance, and regulatory considerations, helping bridge the gap between theoretical performance and practical deployment.

# **Funding**

This work has not received any funding.

#### **CRediT authorship contribution statement**

**Brahim Ouadi:** Writing – review & editing, Supervision, Project administration. **Abdelwahhab Khatir:** Writing – original draft, Software, Conceptualization. **Erica Magagnini:** Writing – review & editing, Data curation. **Maamar Mokadem:** Writing – review & editing. **Laith Abualigah:** Writing – review & editing, Validation, Resources. **Aseel Smerat:** Formal analysis, Writing – review & editing.

# **Declaration of competing interest**

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

# **Data availability**

The data that support the findings of this study are available from the corresponding author upon reasonable request.

#### **References**

- [1] S.G. Salinas Rodriguez, et al., Monitoring particulate fouling of North Sea water with SDI and new ASTM MFI0.45 test, Desalination 454 (2019) 10–19, [https://doi.](https://doi.org/10.1016/j.desal.2018.12.006)  [org/10.1016/j.desal.2018.12.006.](https://doi.org/10.1016/j.desal.2018.12.006)
- [2] C.H. Koo, A.W. Mohammad, F. Suja, Correlation between modified fouling index (MFI) and crossflow sampler-modified fouling index (CFS-MFI) under constant flux filtration, J. Water Process. Eng. 3 (2014) 151–154, [https://doi.org/10.1016/j.](https://doi.org/10.1016/j.jwpe.2014.06.006) [jwpe.2014.06.006](https://doi.org/10.1016/j.jwpe.2014.06.006).
- [3] M. Yaqub, W. Lee, Testing functional polyketones to remove scaling calcium and magnesium from real reverse osmosis concentrate and optimizing the process using machine learning models, J. Water Process Eng. 63 (2024) 105553, [https://doi.](https://doi.org/10.1016/j.jwpe.2024.105553)  [org/10.1016/j.jwpe.2024.105553.](https://doi.org/10.1016/j.jwpe.2024.105553)
- [4] V.R. Moreira, et al., Integrating reverse osmosis to a conventional river water treatment plant as a strategy to produce drinking water after mining dam rupture events: A case study, Environ. Technol. (2024) 1–12, [https://doi.org/10.1080/](https://doi.org/10.1080/09593330.2024.2326799)  [09593330.2024.2326799.](https://doi.org/10.1080/09593330.2024.2326799)
- [5] L.N. Sim, et al., A review of fouling indices and monitoring techniques for reverse osmosis, Desalination 434 (2018) 169–188, [https://doi.org/10.1016/j.](https://doi.org/10.1016/j.desal.2017.12.009) [desal.2017.12.009](https://doi.org/10.1016/j.desal.2017.12.009).
- [6] ASTM Standard (D 4189–[-07\), Standard Test Method for Silt Density Index \(SDI\) of](http://refhub.elsevier.com/S2214-7144(24)01711-2/rf0025)  [Water, D19.08 on Membranes and Ion Exchange Materials, 2007.](http://refhub.elsevier.com/S2214-7144(24)01711-2/rf0025)
- [7] A. Alhadidi, et al., The influence of membrane properties on the Silt Density Index, J. Membr. Sci. 384 (1) (2011) 205–218, [https://doi.org/10.1016/j.](https://doi.org/10.1016/j.memsci.2011.09.028)  [memsci.2011.09.028](https://doi.org/10.1016/j.memsci.2011.09.028).
- [8] Y. Jin, et al., Application of multiple modified fouling index (MFI) measurements at full-scale SWRO plant, Desalination 407 (2017) 24–32, [https://doi.org/10.1016/j.](https://doi.org/10.1016/j.desal.2016.12.006)  [desal.2016.12.006](https://doi.org/10.1016/j.desal.2016.12.006).
- [9] H. Lee, et al., Role of transparent exopolymer particles (TEP) in initial bacterial deposition and biofilm formation on reverse osmosis (RO) membrane, J. Membr. Sci. 494 (2015) 25–31, <https://doi.org/10.1016/j.memsci.2015.06.049>.
- [10] L. Dahdouh, et al., Size-cartography of orange juices foulant particles: contribution to a better control of fouling during microfiltration, J. Membr. Sci. 509 (2016) 164–172, <https://doi.org/10.1016/j.memsci.2016.01.052>.
- [11] A. Gul, J. Hruza, F. Yalcinkaya, Fouling and chemical cleaning of microfiltration membranes: a mini-review, Polymers 13 (2021), [https://doi.org/10.3390/](https://doi.org/10.3390/polym13060846) [polym13060846.](https://doi.org/10.3390/polym13060846)
- [12] Y. Jin, et al., ASTM standard modified fouling index for seawater reverse osmosis desalination process: status, limitations, and perspectives, Separation & Purification Reviews 49 (1) (2020) 55–67, [https://doi.org/10.1080/](https://doi.org/10.1080/15422119.2018.1515777) [15422119.2018.1515777.](https://doi.org/10.1080/15422119.2018.1515777)
- [13] H.Y. Yoo, et al., Silt density index as a fouling propensity parameter of various membrane materials using dissolved organic matter, J. Water Process Eng. 44 (2021) 102391, <https://doi.org/10.1016/j.jwpe.2021.102391>.
- [14] A. Ruiz-García, N. Meli´ an-Martel, I. Nuez, Short review on predicting fouling in RO desalination, Membranes 7 (2017), [https://doi.org/10.3390/membranes7040062.](https://doi.org/10.3390/membranes7040062)
- [15] N. Najid, et al., Fouling control and modeling in reverse osmosis for seawater desalination: a review, Comput. Chem. Eng. 162 (2022) 107794, [https://doi.org/](https://doi.org/10.1016/j.compchemeng.2022.107794)  [10.1016/j.compchemeng.2022.107794](https://doi.org/10.1016/j.compchemeng.2022.107794).
- [16] R. Mulyanti, H. Susanto, Wastewater treatment by nanofiltration membranes, IOP Conference Series: Earth and Environmental Science 142 (1) (2018) 012017, [https://doi.org/10.1088/1755-1315/142/1/012017.](https://doi.org/10.1088/1755-1315/142/1/012017)
- [17] C. Liu, et al., From ultrafiltration to nanofiltration: Nanofiltration membrane fabricated by a combined process of chemical crosslinking and thermal annealing, Sep. Purif. Technol. 212 (2019) 465–473, [https://doi.org/10.1016/j.](https://doi.org/10.1016/j.seppur.2018.11.041)  [seppur.2018.11.041.](https://doi.org/10.1016/j.seppur.2018.11.041)
- [18] E.M. Romero-Dondiz, et al., Comparison of the performance of ultrafiltration and nanofiltration membranes for recovery and recycle of tannins in the leather industry, J. Clean. Prod. 135 (2016) 71–79, [https://doi.org/10.1016/j.](https://doi.org/10.1016/j.jclepro.2016.06.096) [jclepro.2016.06.096](https://doi.org/10.1016/j.jclepro.2016.06.096).
- [19] U.W.R. Siagian, et al., High-performance ultrafiltration membrane: recent progress and its application for wastewater treatment, Curr. Pollut. Rep. 7 (4) (2021) 448–462, [https://doi.org/10.1007/s40726-021-00204-5.](https://doi.org/10.1007/s40726-021-00204-5)
- [20] K.C. Khulbe, T. Matsuura, Membrane Modification, in: K.C. Khulbe, T. Matsuura (Eds.), Nanotechnology in Membrane Processes, Springer International Publishing, Cham, 2021, pp. 135–170, [https://doi.org/10.1007/978-3-030-64183-2\\_4.](https://doi.org/10.1007/978-3-030-64183-2_4)

- <span id="page-13-0"></span>[21] M. Norouzi, H. Sharifnezhad, S.G. Hosseini, Preparation and modification of polyethersulphone MF/UF membrane by TiO2 nanoparticles for pre-treatment of pink water, Int. J. Environ. Anal. Chem. 100 (2) (2020) 175–188, [https://doi.org/](https://doi.org/10.1080/03067319.2019.1634700)  [10.1080/03067319.2019.1634700](https://doi.org/10.1080/03067319.2019.1634700).
- [22] M. Fan, et al., A review on experimental design for pollutants removal in water treatment with the aid of artificial intelligence, Chemosphere 200 (2018) 330–343, <https://doi.org/10.1016/j.chemosphere.2018.02.111>.
- [23] S.S. Ray, et al., A holistic review on how artificial intelligence has redefined water treatment and seawater desalination processes, Desalination 546 (2023) 116221, <https://doi.org/10.1016/j.desal.2022.116221>.
- [24] C.A. Igwegbe, et al., Enhancing municipal solid waste leachate treatment efficiency: AI-based prediction of electrocoagulation/flocculation recovery using iron electrodes, Environ. Technol. (2024) 1–16, [https://doi.org/10.1080/](https://doi.org/10.1080/09593330.2024.2328659)  [09593330.2024.2328659.](https://doi.org/10.1080/09593330.2024.2328659)
- [25] Q. He, et al., Artificial intelligence application in a renewable energy-driven desalination system: a critical review, Energy and AI 7 (2022) 100123, [https://doi.](https://doi.org/10.1016/j.egyai.2021.100123)  [org/10.1016/j.egyai.2021.100123](https://doi.org/10.1016/j.egyai.2021.100123).
- [26] I. Akkurt, P. Boodaghi Malidarreh, R. Boodaghi Malidarre, Simulation and prediction of the attenuation behaviour of the KNN–LMN–based lead-free ceramics by FLUKA code and artificial neural network (ANN)–based algorithm, Environ. Technol. 44 (11) (2023) 1592–1599, [https://doi.org/10.1080/](https://doi.org/10.1080/09593330.2021.2008017)  [09593330.2021.2008017.](https://doi.org/10.1080/09593330.2021.2008017)
- [27] K. Wang, et al., Application of a combined response surface methodology (RSM) artificial neural network (ANN) for multiple target optimization and prediction in a magnetic coagulation process for secondary effluent from municipal wastewater treatment plants, Environ. Sci. Pollut. Res. 29 (24) (2022) 36075–36087, [https://](https://doi.org/10.1007/s11356-021-18060-7)  [doi.org/10.1007/s11356-021-18060-7.](https://doi.org/10.1007/s11356-021-18060-7)
- [28] W.M. Warren-Vega, et al., Development of an artificial neural network (ANN) for the prediction of a pilot scale mobile wastewater treatment plant performance, J. Environ. Manage. 366 (2024) 121612, [https://doi.org/10.1016/j.](https://doi.org/10.1016/j.jenvman.2024.121612) [jenvman.2024.121612.](https://doi.org/10.1016/j.jenvman.2024.121612)
- [29] S. Narges, et al., Prediction of the optimal dosage of coagulants in water treatment plants through developing models based on artificial neural network fuzzy inference system (ANFIS), J. Environ. Health Sci. Eng. 19 (2) (2021) 1543–1553, [https://doi.org/10.1007/s40201-021-00710-0.](https://doi.org/10.1007/s40201-021-00710-0)
- [30] A. Izady, et al., Impurity effect on clear water evaporation: toward modelling wastewater evaporation using ANN, ANFIS-SC and GEP techniques, Hydrol. Sci. J. 62 (11) (2017) 1856–1866, <https://doi.org/10.1080/02626667.2017.1356023>.
- [31] A. Baranwal, B.S. Das, Live-bed scour depth modelling around the bridge pier using ANN-PSO, ANFIS, MARS, and M5Tree, Water Resour. Manag. 38 (2024) 4555–4587, [https://doi.org/10.1007/s11269-024-03879-9.](https://doi.org/10.1007/s11269-024-03879-9)
- [32] R. Goebel, M. Skiborowski, Machine-based learning of predictive models in organic solvent nanofiltration: pure and mixed solvent flux, Sep. Purif. Technol. 237 (2020) 116363, <https://doi.org/10.1016/j.seppur.2019.116363>.
- [33] J. Jawad, A.H. Hawari, S. Javaid Zaidi, Artificial neural network modeling of wastewater treatment and desalination using membrane processes: a review, Chem. Eng. J. 419 (2021) 129540, <https://doi.org/10.1016/j.cej.2021.129540>.
- [34] M.S. Islam Khan, et al., Water quality prediction and classification based on principal component regression and gradient boosting classifier approach, Journal of King Saud University - Computer and Information Sciences 34 (8, Part A) (2022) 4773–4781, <https://doi.org/10.1016/j.jksuci.2021.06.003>.
- [35] A. Khatir, et al., An efficient improved gradient boosting for strain prediction in near-surface mounted fiber-reinforced polymer strengthened reinforced concrete beam, Frontiers of Structural and Civil Engineering 18 (2024) 1148–1168, [https://](https://doi.org/10.1007/s11709-024-1079-x)  [doi.org/10.1007/s11709-024-1079-x.](https://doi.org/10.1007/s11709-024-1079-x)
- [36] N. Nasir, et al., Water quality classification using machine learning algorithms, Journal of Water Process Engineering 48 (2022) 102920, [https://doi.org/10.1016/](https://doi.org/10.1016/j.jwpe.2022.102920)  [j.jwpe.2022.102920.](https://doi.org/10.1016/j.jwpe.2022.102920)

- [37] H. Mahanna, et al., Prediction of wastewater treatment plant performance through machine learning techniques, Desalin. Water Treat. 319 (2024) 100524, [https://](https://doi.org/10.1016/j.dwt.2024.100524) [doi.org/10.1016/j.dwt.2024.100524.](https://doi.org/10.1016/j.dwt.2024.100524)
- [38] F. Bagherzadeh, et al., Comparative study on total nitrogen prediction in wastewater treatment plant and effect of various feature selection methods on machine learning algorithms performance, Journal of Water Process Engineering 41 (2021) 102033, [https://doi.org/10.1016/j.jwpe.2021.102033.](https://doi.org/10.1016/j.jwpe.2021.102033)
- [39] W. Zhang, et al., Miss-gradient boosting regression tree: a novel approach to imputing water treatment data, Appl. Intell. 53 (19) (2023) 22917–22937, [https://](https://doi.org/10.1007/s10489-023-04828-6)  [doi.org/10.1007/s10489-023-04828-6.](https://doi.org/10.1007/s10489-023-04828-6)
- [40] H. Tabari, P. Hosseinzadeh Talaee, Reconstruction of river water quality missing data using artificial neural networks, Water Quality Research Journal 50 (4) (2015) 326–335, <https://doi.org/10.2166/wqrjc.2015.044>.
- [41] W. Helm, et al., Development of gradient boosting-assisted machine learning datadriven model for free chlorine residual prediction, Front. Environ. Sci. Eng. 18 (2) (2023) 17, [https://doi.org/10.1007/s11783-024-1777-6.](https://doi.org/10.1007/s11783-024-1777-6)
- [42] A. Oulad Brahim, et al., Artificial neural network and YUKI algorithm for notch depth prediction in X70 steel specimens, Theor. Appl. Fract. Mech. 129 (2024) 104227, [https://doi.org/10.1016/j.tafmec.2023.104227.](https://doi.org/10.1016/j.tafmec.2023.104227)
- [43] A. Khatir, et al., Advancing structural integrity prediction with optimized neural network and vibration analysis, J. Struct. Integr. Maint. 9 (3) (2024) 2390258, [https://doi.org/10.1080/24705314.2024.2390258.](https://doi.org/10.1080/24705314.2024.2390258)
- [44] A. Ouladbrahim, et al., Prediction of Gurson damage model parameters coupled with hardening law identification of steel X70 pipeline using neural network, Met. Mater. Int. 28 (2) (2022) 370–384, [https://doi.org/10.1007/s12540-021-01024-4.](https://doi.org/10.1007/s12540-021-01024-4)
- [45] S. Khatir, et al., An improved artificial neural network using arithmetic optimization algorithm for damage assessment in FGM composite plates, Compos. Struct. 273 (2021) 114287, [https://doi.org/10.1016/j.compstruct.2021.114287.](https://doi.org/10.1016/j.compstruct.2021.114287)
- [46] A. Khatir, et al., A new hybrid PSO-YUKI for double cracks identification in CFRP cantilever beam, Composite Structures 311 (2023) 116803, [https://doi.org/](https://doi.org/10.1016/j.compstruct.2023.116803)  [10.1016/j.compstruct.2023.116803](https://doi.org/10.1016/j.compstruct.2023.116803).
- [47] M. Lubbad, et al., Machine learning applications in detection and diagnosis of urology cancers: a systematic literature review, Neural Computing and Applications 36 (12) (2024) 6355–6379, [https://doi.org/10.1007/s00521-023-](https://doi.org/10.1007/s00521-023-09375-2) [09375-2.](https://doi.org/10.1007/s00521-023-09375-2)
- [48] G. Fu, et al., The role of deep learning in urban water management: a critical review, Water Res. 223 (2022) 118973, [https://doi.org/10.1016/j.](https://doi.org/10.1016/j.watres.2022.118973)  [watres.2022.118973](https://doi.org/10.1016/j.watres.2022.118973).
- [49] A.A. Nasser, M.Z. Rashad, S.E. Hussein, A two-layer water demand prediction system in urban areas based on Micro-services and LSTM neural networks, IEEE Access 8 (2020) 147647–147661, [https://doi.org/10.1109/](https://doi.org/10.1109/ACCESS.2020.3015655)  [ACCESS.2020.3015655.](https://doi.org/10.1109/ACCESS.2020.3015655)
- [50] C. Kühnert, et al., Application of LSTM networks for water demand prediction in optimal pump control, Water 13 (2021), <https://doi.org/10.3390/w13050644>.
- [51] Q. Fang, et al., Detection of multiple leakage points in water distribution networks based on convolutional neural networks, Water Supply 19 (8) (2019) 2231–2239, <https://doi.org/10.2166/ws.2019.105>.
- [52] X. Zhang, et al., A review of resource recovery from seawater desalination brine, Rev. Environ. Sci. Biotechnol. 20 (2) (2021) 333–361, [https://doi.org/10.1007/](https://doi.org/10.1007/s11157-021-09570-4)  [s11157-021-09570-4](https://doi.org/10.1007/s11157-021-09570-4).
- [53] C. Bent´ejac, A. Csorg ¨ o, ˝ G. Martínez-Munoz, ˜ A comparative analysis of gradient boosting algorithms, Artif. Intell. Rev. 54 (3) (2021) 1937–1967, [https://doi.org/](https://doi.org/10.1007/s10462-020-09896-5)  [10.1007/s10462-020-09896-5.](https://doi.org/10.1007/s10462-020-09896-5)
- [54] L. Abualigah, et al., Salp swarm algorithm: a comprehensive survey, Neural Comput. & Applic. 32 (15) (2020) 11195–11215, [https://doi.org/10.1007/](https://doi.org/10.1007/s00521-019-04629-4)  [s00521-019-04629-4](https://doi.org/10.1007/s00521-019-04629-4).
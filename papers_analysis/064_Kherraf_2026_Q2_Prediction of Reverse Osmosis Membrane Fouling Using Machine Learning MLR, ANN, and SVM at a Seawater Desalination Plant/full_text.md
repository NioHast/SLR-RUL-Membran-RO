![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_1.jpeg)

*Article*

# **Prediction of Reverse Osmosis Membrane Fouling Using Machine Learning: MLR, ANN, and SVM at a Seawater Desalination Plant**

**Siham Kherraf <sup>1</sup> , Fatima-Zahra Abahdou <sup>1</sup> , Maria Benbouzid <sup>1</sup> [,](https://orcid.org/0000-0002-5318-9156) Zakaria Izouaouen <sup>2</sup> [,](https://orcid.org/0009-0006-5005-0016) Abdellatif Aarfane <sup>3</sup> , Abdoullatif Baraket <sup>3</sup> , Hamid Nasrellah 3,[\\*](https://orcid.org/0000-0002-9224-2220) , Meryem Bensemlali [3](https://orcid.org/0000-0002-4860-4829) , Soumia Ziti <sup>2</sup> [,](https://orcid.org/0000-0002-5357-9170) Najoua Labjar <sup>4</sup> and Souad El Hajjaji 1,\***

- <sup>1</sup> Laboratory of Spectroscopy, Molecular Modeling, Materials, Nanomaterials, Water and Environment, (LS3MN2E), Chemistry Department, Faculty of Sciences, Mohammed V University in Rabat, Rabat 10000, Morocco; kherraf.siham1@gmail.com (S.K.); fatimazahra\_abahdou@um5.ac.ma (F.-Z.A.); mariabenbouzid@hotmail.fr (M.B.)
- 2 Intelligent Processing and Security of Systems, Faculty of Sciences, Mohammed V University in Rabat, Rabat 10000, Morocco; s.ziti@um5r.ac.ma
- <sup>3</sup> Higher School of Education and Training, Chouaib Doukkali University, El Jadida 24000, Morocco; aaarfane@yahoo.com (A.A.); a.baraket@gmail.com (A.B.); bensemlali.meryem@gmail.com (M.B.)
- <sup>4</sup> Laboratory of Spectroscopy, Molecular Modeling, Materials, Nanomaterials, Water and Environment, (LS3MN2E), ENSAM-Rabat, Mohammed V University in Rabat, Rabat 10000, Morocco; najoua.labjar@ensam.um5.ac.ma
- **\*** Correspondence: nasrellah.h@ucd.ac.ma (H.N.); s.elhajjaji@um5r.ac.ma (S.E.H.)

### **Abstract**

Membrane fouling remains a major obstacle to the performance of the reverse osmosis (RO) desalination processes. Artificial intelligence (AI) is now a promising approach for the reliable modeling of these complex systems. This study evaluates three modeling techniques—multiple linear regression (MLR), artificial neural networks (ANNs), and support vector regression (SVR)—for predicting transmembrane pressure (TMP) at the Boujdour desalination plant, based on five input parameters: temperature, turbidity, pH, conductivity, and feedflow. The analysis is based on an original dataset of 195 daily measurements, and due to the absence of timestamps, the study focuses on state-to-TMP prediction rather than chronological forecasting, with no temporal generalization claimed. Approximately 2000 augmented training samples generated using a conservative SMOGN approach were used for model development, while performance evaluation relied exclusively on 39 independent real test observations. Two modeling strategies were adopted: (i) a minimalist approach based on significant variables identified by an ordinary least squares (OLS) model (pH and conductivity), and (ii) a multivariate approach integrating all parameters to capture non-linear interactions. A rigorous validation framework was put in place to avoid information leakage and ensure the robustness and generalizability of the models. Performance was evaluated using R<sup>2</sup> , RMSE, and MAE metrics, supplemented by robustness and significance analyses including bootstrap confidence intervals, paired statistical comparisons, and interpretability analyses based on permutation importance, partial dependence plots (PDPs), and individual conditional expectation (ICE) curves. The results indicate that the SVR model achieves the best average predictive accuracy among the tested models, albeit with moderate explanatory power.

**Keywords:** reverse osmosis; prediction; multiple linear regression; artificial neural network; support vector machines

![](_page_0_Picture_13.jpeg)

Academic Editors: Stanisław Wacławek, Juvenal Rodriguez-Resendiz, Akos Odry, Marco Antonio Aceves-Fernandez and José Manuel Álvarez-Alvarado

Received: 25 November 2025 Revised: 23 February 2026 Accepted: 26 February 2026 Published: 28 February 2026

**Copyright:** © 2026 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the [Creative Commons](https://creativecommons.org/licenses/by/4.0/) [Attribution \(CC BY\) license.](https://creativecommons.org/licenses/by/4.0/)

*Eng* **2026**, *7*, 106 2 of 17

# **1. Introduction**

Increasing demand for water and climate change risks threatening to reduce the world's available resources; it has become essential to effectively manage water resources [\[1\]](#page-15-0). Meanwhile, access to potable water is challenging, as usable freshwater represents approximately 2.5% of the global water reserves, but saltwater accounts for nearly 97.5% of the world's global water reserves and is available to nearly all countries, which makes desalination the only viable solution for securing water supplies in many water-stressed regions [\[2\]](#page-15-1). As a result, the water shortage has led to significant advancements in desalination technology in urban and coastal regions, focusing on the treatment of seawater, brackish water, and wastewater [\[3\]](#page-15-2). The global desalination capacity in 2020 was estimated at around 100 million cubic meters per day, generated by nearly 16,000 plants worldwide, with about half of this capacity located in the Middle East and North Africa (MENA) [\[4\]](#page-15-3). Membrane processes, such as RO, have developed rapidly since the 1960s and are becoming increasingly popular due to their low specific energy consumption, reduced environmental impact and greater flexibility compared with their thermal counterparts [\[5\]](#page-15-4). Morocco, characterized by a semi-arid area and affected by climate change and global warming estimated at around 1 ◦C, as well as the temporal and spatial variability of rainfall, with a significant decline varying between 3% and 30% depending on the region, has a low potential of natural water resources, estimated in 2020 at 22 billion m<sup>3</sup> per year, including 18 billion m<sup>3</sup> of reserves in surface waters and about 4 billion m<sup>3</sup> in groundwater [\[6\]](#page-15-5). To address this situation, several programs aiming to mobilize non-conventional water resources, in particular water desalination and the reuse of treated wastewater, have been implemented, along with demand management measures [\[7\]](#page-15-6). Boujdour desalination plant is situated in southern Morocco, and draws seawater from the Atlantic Ocean through coastal boreholes. The plant is designed to produce up to 9500 m<sup>3</sup> of potable water per day [\[8\]](#page-15-7). Membrane fouling is considered a significant problem in RO systems. It results in higher operational costs and a shorter membrane lifespan. Fouling is typically characterized by a decrease in permeate flux or an increase in transmembrane pressure [\[9\]](#page-15-8). This challenge is complex and impacted by various factors, such as feedwater quality, pretreatment processes, and operating conditions, include equipment and chemicals used. To assess operating conditions and improve the long-term performance of the RO plant, fouling prediction can be used as an effective strategy to prevent its effects before it reaches a critical and irreversible stage [\[10\]](#page-15-9). Many modeling approaches have been proposed in the literature to describe the impact of fouling on reverse osmosis unit performance, particularly through changes in TMP. Conventional models, including empirical and mechanistic models based on filtration laws and series resistance theory, have been widely used to link operating conditions to membrane performance and to interpret fouling behavior. However, their application to industrial units remains limited due to the simplifying assumptions adopted and the variability of actual operating conditions [\[11](#page-15-10)[,12\]](#page-15-11). In this context, machine learning approaches such as MLR, ANN and SVR appear to be promising tools for improving TMP predictions associated with fouling.

Various models have been developed to predict membrane fouling in RO using artificial intelligence. Artificial neural networks are very effective at understanding complex and non-linear relationships between input and output parameters based on historical data and optimal selection of hidden layers and neurons [\[13\]](#page-15-12). Support vector machines (SVM) is a supervised machine learning approach applied to classification, regression and anomaly detection. Developed in the 1990s by Vladimir Vapnik, SVM proved their remarkable performance, particularly where experimental data is limited and the functions are non-linear [\[14\]](#page-15-13). Abunada et al. [\[15\]](#page-15-14) studied the implementation and validation of the MFI-UF method to predict particle fouling in two large-scale RO facilities with an average

*Eng* **2026**, *7*, 106 3 of 17

capacity ranging from 800 to 2000 m3/h. Teng et al. [\[16\]](#page-15-15) successfully demonstrated the potential of using an integrated model to predict RO membrane fouling by incorporating an adsorption model into a data-driven approach to predict TMP. Lim et al. [\[17\]](#page-15-16) developed a predictive model of seawater RO membrane fouling based on a hybrid machine learning approach, combined with a Kalman filter and an ANN or SVR approach over a period of 18 months. The results revealed the superior performance of the SVR method in membrane resistance prediction compared with the ANN. Roehl et al. [\[18\]](#page-15-17) used data collected over six years to develop neural network models, including 59 parameters concerning water quality and hydraulics, to study the causes of membrane fouling in the first stage of a large-scale RO system.

Input parameter selection in RO system prediction is particularly important to optimize result efficiency. Although TMP is widely used as an indicator of fouling in the literature [\[19\]](#page-15-18), only a few studies have proposed a prediction approach that integrates several operational and physicochemical parameters (temperature, turbidity, pH, conductivity and flow rate) under real industrial reverse osmosis conditions, such as at the Boujdour desalination plant, where the specific composition of the feed water and local climatic constraints limit the existing models' ability to provide reliable and operational TMP prediction.

In this context, this study proposes a comparative modeling approach to state-to-TMP prediction, combining MLR and two machine learning methods, namely ANN and support SVR. In the absence of time-series data, this study addresses a state–TMP regression problem rather than a time-series forecasting task, and the results will be interpreted within this strictly non-chronological framework.

Two strategies are implemented: one based on the two statistically significant variables identified in OLS (pH and conductivity), and the other integrating all five input parameters in order to fully exploit the non-linear relationships. The models are optimized using GridSearchCV (ANN and SVR) and Ridge regularization (MLR), and their performance is evaluated using R<sup>2</sup> , RMSE and MAE. Additional analyses, including permutation importance, partial dependence plots, overfitting test and bootstrap confidence intervals, reinforce the statistical and physical interpretation of the results. This study provides a robust framework for comparing the capabilities of linear and non-linear models to state-to-TMP prediction and understanding membrane fouling phenomena in the Boujdour plant. The manuscript is structured as follows: Section [2](#page-2-0) describes the methodology, Section [3](#page-5-0) presents the results and discussion, Section [4](#page-14-0) concludes the study.

# <span id="page-2-0"></span>**2. Material and Methods**

## *2.1. Study Area*

Boujdour (26◦08′ N, 14◦30′ W), part of the southern provinces of Morocco, has a total area of around 43,753 km<sup>2</sup> and has a population of 52,214 as of 2020. The province experiences an arid climate [\[20\]](#page-15-19). Boujdour's desalination plant was built in 1977, utilizing mechanical compression distillation to supply drinking water to the local population. In 1995, the plant added two RO skids. Today, it operates with a capacity of 125 L/s, comprising three skids from the old station and two skids from the new station.

## *2.2. Data Collection*

Data used in this study was obtained from daily operational measurements collected at the Boujdour plant. After a preprocessing stage aimed at correcting inconsistencies, removing outliers, and eliminating invalid records, a real dataset consisting of 195 observations and six variables was constructed. Five input variables were selected to predict TMP as the output variable: temperature, pH, turbidity, feed water conductivity, and feed

*Eng* **2026**, *7*, 106 4 of 17

water flow. To prevent any information leakage (data leakage), the separation into training and test sets was performed exclusively on real data, prior to any augmentation procedure. The dataset was thus split into 156 real samples for training (80%) and 39 real samples for testing (20%), forming a 100% real, invariant, and non-augmented test set. Data augmentation was then applied only to the training set using a conservative-SMOGN (Synthetic Minority Over-sampling Technique for Regression with Gaussian Noise) strategy, based on a k-NN algorithm (k = 3) and a controlled Gaussian perturbation (1%), allowing the training set to reach approximately 1961 augmented samples, while limiting the generation of synthetic points far from the real observations. The final dataset therefore consists of 1961 augmented training samples and 39 real test samples, for a total of approximately 2000 observations. All variables were normalized using the Min–Max method within the [0, 1] interval, based exclusively on the statistics of the training set, in order to guarantee a strict data leakage control [\[21\]](#page-15-20). This protocol also ensures that, during cross-validation, the validation folds remain entirely real, providing a robust, realistic, and unbiased evaluation of the model's generalization performance. The dataset composition and augmentation strategy are summarized in Table [1.](#page-3-0)

<span id="page-3-0"></span>**Table 1.** Dataset composition and augmentation strategy.

| Item                   | Value                                                                                                       |
|------------------------|-------------------------------------------------------------------------------------------------------------|
| Original dataset       | 195 daily operational observations (Boujdour seawater RO plant)                                             |
| Training set (real)    | 156 observations (80%)                                                                                      |
| Test set (real)        | 39 observations (20%)—100% real, never augmented                                                            |
| Augmented training set | ~2000 observations (156 real + ~1844 conservative SMOGN-like synthetic)                                     |
| Augmentation protocol  | SMOGN-kNN interpolation (k = 3, perturbation = 1%, α ∈ [0.3, 0.7]) applied only inside<br>fit()             |
| Leak-free guarantee    | Augmentation occurs inside CV folds and final training only; test data is never seen<br>during augmentation |

## *2.3. Methodology (Modeling Framework)*

In this study, a modeling framework for membrane fouling prediction based on TMP was developed. Three modeling techniques, namely MLR, ANN, and SVR, were implemented in the Python environment (version 3.11.5) using the scikit-learn library, with the objective of comparing their predictive performance and identifying the most effective model. A rigorous methodological strategy was adopted, based on a strict anti-leakage framework. The separation of the data into training and test sets was performed exclusively on real data prior to any augmentation procedure, ensuring a 100% real, invariant, and non-augmented test set. Data augmentation was then applied only to the training set using the SMOGN approach, enabling improved model learning while preserving experimental realism and evaluation integrity. Two modeling strategies were considered: (i) the use of a limited number of statistically significant input variables, and (ii) the integration of all available variables, in order to assess the impact of information complexity on predictive performance. Min–Max normalization, based exclusively on the statistics of the training set, was applied to prevent information leakage. For the MLR model, Ridge regularization was used to limit overfitting. In contrast, for ANN and SVR models, automatic hyperparameter optimization was performed using the GridSearchCV algorithm, embedded within a crossvalidation framework that ensures the validation folds remain entirely real. Predictive performance was then evaluated using standard statistical indicators, including the R<sup>2</sup> , RMSE, and MAE, in order to identify the most optimal configuration for TMP prediction within a robust, realistic, and reproducible experimental framework.

*Eng* **2026**, *7*, 106 5 of 17

## *2.4. Modeling Methods*

This subsection presents three modeling methods applied for predicting TMP, namely MLR, ANN and SVM.

## 2.4.1. MLR

MLR is commonly employed in statistics to model the dependency of a variable on several explanatory factors [\[22\]](#page-15-21). The regression equation developed for prediction purposes is given by the following:

$$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \beta_3 X_3 + \dots + \beta_n X_n + \varepsilon$$
 (1)

Y is the dependent variable, while β0, β1, . . ., β<sup>n</sup> represent the regression coefficients. X1, X2, . . ., X<sup>n</sup> are the independent variables, and ε represents the residual error. In order to develop an MLR model, the OLS method is applied as a statistical technique to estimate the coefficients of linear regression. Its aim is to adjust the model by minimizing the sum of the squared differences (or residuals) between the predicted values and the observed data values [\[23\]](#page-15-22). In this study, the MLR model was developed in Python software using Ridge regularization in order to stabilize the estimation of coefficients and improve the robustness of the model [\[24\]](#page-15-23).

#### 2.4.2. ANN

ANNs are becoming more and more commonly used to predict RO systems. Inspired by the human brain, ANNs are capable of capturing non-linear relationships between input and output variables [\[25\]](#page-15-24). Each network consists of an input layer, one or more hidden layers, and an output layer, with each layer containing a number of neurons interconnected by weights and biases. In this study, ANNs were implemented in Python software, and hyperparameter optimization was performed using GridSearchCV, allowing the most efficient configuration for predictive modeling to be determined.

## 2.4.3. SVR

SVR, derived from SVM theory, is an effective machine learning method for modeling complex non-linear relationships [\[26\]](#page-15-25). Based on the principle of structural risk minimization, it limits overfitting and ensures good generalization capacity [\[27\]](#page-16-0). In this study, SVR was implemented using Python software and optimized with the GridSearch method to determine the optimal hyperparameters. These key parameters are cost (C), which controls the balance between model complexity and learning error, Gamma (γ), which defines the influence of training data, and Epsilon (ε), which represents the insensitivity region of the regression function. Optimizing these hyperparameters improved the accuracy and reliability of predictions.

#### *2.5. Model Performance Evaluation*

The TMP prediction models were evaluated using three performance indicator parameters, namely *R* 2 , RMSE and MAE. Its mathematical equations are represented as follows:

$$R^{2} = \frac{\sum_{i=1}^{N} (y_{i} - \hat{y}_{i})^{2}}{\sum_{i=1}^{N} (y_{i} - \overline{y}_{i})^{2}}$$
(2)

$$RMSE = \sqrt{\left[ (1/n) \sum_{i} (y_i - \hat{y}_i)^2 \right]}$$
 (3)

$$MAE = \frac{1}{n} \sum_{i=1}^{N} | y_i - \hat{y}_i |$$
 (4)

*Eng* **2026**, *7*, 106 6 of 17

where *y*<sup>i</sup> represents the observed value, ˆy<sup>i</sup> is the predicted value, *y* is the mean of observed values and *n* defines the total number of observations [\[28\]](#page-16-1).

# <span id="page-5-0"></span>**3. Results and Discussions**

The initial dataset comprised 195 observations of input and output parameters. The dataset was divided into two sets: 80% for training (156 observations) and 20% for actual testing (39 observations); the latter remained completely unchanged to ensure objective evaluation. The training set was then augmented using the conservative SMOGN method, bringing the total number of observations to 1961, in order to improve the representative nature of the models and prevent information leakage (anti-leakage). Two modeling approaches were studied: approach A, based on the significant variables identified by the OLS model (pH and conductivity), and approach B, incorporating all five input parameters to capture non-linear interactions. The ANN and SVR models were optimized using GridSearchCV, and the MLR was regularized by Ridge. The robustness and stability of the models were evaluated using several protocols: ∆R <sup>2</sup> between training and test sets, learning curves, repeated K-Fold validation on real data, and 95% bootstrap confidence intervals on the real test. Additional tests were performed to verify robustness and detect overfitting, including variable permutations, paired bootstrap tests, the Diebold–Mariano test (DM) for the significance of differences between models, and the autocorrelation of residuals via Durbin–Watson and ACF as a temporal proxy. The SVR model's sensitivity to the hyperparameter γ was analyzed over a wide range (100–1000), allowing us to assess the impact of complexity on performance. The interpretability of the models was examined using partial dependence plots (PDPs) and ICE curves, with 5–95% uncertainty intervals, and the permutation importance calculated on the actual test confirmed consistency with the significant variables identified by OLS. All performance metrics, bootstrap confidence intervals, paired statistical tests, and interpretability diagnostics reported below are computed exclusively on the 39 real test observations. The results are presented in the form of figures illustrating the distribution of predicted values, residuals, and the observed vs. predicted comparison, allowing for a comprehensive evaluation of the performance and the relevance of the models for predicting transmembrane pressure (TMP).

#### *3.1. Model Development and Input Parameter Analysis*

#### 3.1.1. Determination of Input Parameters

Determining the input parameters is the most important step in prediction [\[29\]](#page-16-2). In this study, we have chosen five inputs essential in RO treatment, that can impact our output (TMP) and which have not been elaborated in the literature. The variables chosen for modeling were selected from among the parameters most regularly measured and continuously available at the desalination plant, in order to ensure the operational relevance of the model. These parameters are:

- Temperature: Always acts in conjunction with pressure.
- Turbidity: An essential parameter in RO systems.
- Feed conductivity: Raw water conductivity always affects RO system parameters.
- Feedflow: A parameter that always correlates with pressure.
- pH: An essential parameter in RO treatment.

The descriptive statistics of the input and output parameters, along with their units, are presented in Table [2.](#page-6-0)

*Eng* **2026**, *7*, 106 7 of 17

| Number  | Variable     | Range         | Mean ± SD       | Unit  |
|---------|--------------|---------------|-----------------|-------|
| Input:  |              |               |                 |       |
| 1       | Temperature  | 19.1–23.5     | 21.0 ± 0.97     | ◦C    |
| 2       | pH           | 7.2–7.63      | 7.41 ± 0.085    |       |
| 3       | Turbidity    | 0.16–2.32     | 0.39 ± 0.23     | NTU   |
| 4       | Feed         | 40,500–47,800 | 44,238 ± 1414   | µs/cm |
| 5       | conductivity |               |                 |       |
|         | Feed flow    | 273–605       | 447.22 ± 148.08 | m3/h  |
| Output: |              |               |                 |       |
|         | TMP          | 0.1–2.28      | 0.36 ± 0.42     | Bar   |

<span id="page-6-0"></span>**Table 2.** Transmembrane pressure prediction input and output variables.

#### 3.1.2. Analysis of Linear Significance and Predictive Importance of Variables

OLS linear regression was initially applied in order to evaluate the statistical significance of the input variables within a linear and interpretable context. The results presented in Table [3](#page-6-1) show that only the pH and conductivity variables represent a statistically significant linear relationship with TMP (*p* < 0.05), while temperature, turbidity and feedflow are not significant (*p* ≥ 0.05) [\[30\]](#page-16-3). On this basis, the variables pH and conductivity were selected for approach A, which consists of developing MLR, ANN and SVR models from a reduced and physically interpretable set of variables.

**Term Estimation Error Standard t-Ratio Prob. > |t| [0.025 0.975]** const 0.3095 0.070 4.447 0.000 0.172 0.447 Temperature −0.1185 0.069 −1.720 0.087 −0.255 0.018 pH 0.3201 0.072 4.455 0.000 0.178 0.462 Turbidity 0.1980 0.126 1.569 0.119 −0.051 0.447 Conductivity 0.2551 0.080 3.174 0.002 0.096 0.414 Feed flow 0.0239 0.039 0.619 0.537 −0.052 0.100

<span id="page-6-1"></span>**Table 3.** Transmembrane pressure OLS analysis result.

However, OLS analysis is limited to the detection of linear relationships and does not capture non-linear dependencies that may influence TMP. Thus, for the non-linear ANN and SVR models, the selection and interpretation of variables were completed with an adapted method such as permutation importance, which evaluates the contribution of variables according to their impact on the predictive performance of the model, considering complex interactions and non-linear effects. Permutation importance is evaluated on the 100% real test set (SVR leak-free), while OLS *p*-values provide a linear reference.

The table and graph in Figure [1](#page-7-0) showing permutation importance evaluated on the actual test set consistently indicate that pH has the greatest influence on SVR model performance, followed by feedflow and temperature, which play a major role in prediction but are secondary. Conductivity makes a moderate contribution, while turbidity shows very low, even negligible, importance, suggesting that it provides little useful information to the model. The OLS model results show that pH is the only statistically highly significant variable (*p* < 0.001), followed by conductivity; temperature and turbidity are not statistically significant at the 5% threshold, while feedflow appears insignificant in the linear model. In contrast, the permutation importance analysis applied to the SVR model on the actual test set highlights pH as the dominant factor, followed by feedflow and temperature, indicating that these variables contribute substantially to the predictive power of the non-linear model. This difference between OLS and SVR suggests the presence of non-linear relationships

*Eng* **2026**, *7*, 106 8 of 17

<span id="page-7-0"></span>and complex interactions captured by SVR but not by OLS, while the agreement on the central role of pH enhances the overall robustness of the conclusions.

| Feature      | Importance_mean | Importance_std |  |  |  |  |  |
|--------------|-----------------|----------------|--|--|--|--|--|
| pH           | 0.479384        | 0.159604       |  |  |  |  |  |
| Feedflow     | 0.324911        | 0.129698       |  |  |  |  |  |
| Temperature  | 0.284914        | 0.125021       |  |  |  |  |  |
| Conductivity | 0.168852        | 0.105904       |  |  |  |  |  |
| Turbidity    | 0.022148        | 0.040627       |  |  |  |  |  |

**Figure 1.** Permutation importance (∆R 2 ) computed on 39 real test samples using the leak-free SVR model. Pink bars represent the mean importance values, and black horizontal lines indicate the 95% confidence intervals.

## 3.1.3. Hyperparameter Optimization

Model hyperparameters were determined using a GridSearchCV (combined with a cross-validation) optimization procedure rigorously defined in the code, in a strictly leakfree framework, ensuring complete separation of the actual data before any augmentation in order to identify the configurations, offering the best compromise between precision and generalization [\[31,](#page-16-4)[32\]](#page-16-5). For the SVR model, the search space for the γ parameter was deliberately limited to a conventional range (from 10−<sup>3</sup> to 10, including the scale option), in order to guarantee stable behavior and good generalization capacity. The extreme values of (*γ* = 100 and 1000), although part of the theoretically possible range, are not discussed in this section; they will be the subject of a specific analysis in a separate section of the article devoted to a sensitivity study, aimed at evaluating their impact on the behavior of the model. Reported hyperparameters thus corresponding to the best configurations selected at the end of the optimization process and saved in the experimental framework are represented in Table [4.](#page-7-1)

| Model       | Hyperparameter Grids | Values                           | Optimal Values |  |  |
|-------------|----------------------|----------------------------------|----------------|--|--|
| Ridge (MLR) | alpha                | 0.001, 0.01, 0.1, 1, 10          | 10             |  |  |
| SVR         | Cost (C)             | 0.1, 1, 10, 100                  |                |  |  |
|             | epsilon (ε)          | 0.01, 0.05, 0.1                  | 0.05           |  |  |
|             | gamma (γ)            | 0.001, 0.01, 0.1, 1, 10, 'scale' | 10             |  |  |
| ANN         | hidden_layer_sizes   | (5,), (10,), (5,5)               | (5,)           |  |  |
|             | activation           | relu, tanh                       | ReLU           |  |  |
|             | alpha                | 0.001, 0.01, 0.1, 1.0            | 0.01           |  |  |
|             | learning_rate_init   | 0.001, 0.01                      | 0.01           |  |  |

<span id="page-7-1"></span>**Table 4.** Hyperparameter grids and optimal values.

#### *3.2. Models Results*

## 3.2.1. Results of Performance Models

In this subsection, TMP prediction is performed using two distinct modeling approaches. The first approach relies exclusively on the two significant input variables, namely pH and conductivity. The second approach consists of integrating all five input variables, including pH, conductivity, temperature, turbidity and feed flow. Approach

*Eng* **2026**, *7*, 106 9 of 17

1 is a reference approach based exclusively on real data, while approach 2 applies data augmentation in a leak-free setting to improve model generalization. The MLR, ANN and SVR models are developed using these two approaches, and their performance is then compared using statistical indicators in order to identify the most effective model for predicting TMP.

According to the results analysis presented in Table [5,](#page-8-0) models in approach 1 show modest overall performance, with the R<sup>2</sup> test remaining below 0.20. The Ridge model has limited performance (R<sup>2</sup> test = 0.192), reflecting the limitations of linear approaches in this context. The ANN model achieves an R<sup>2</sup> test = 0.165, while the SVR model, despite showing a better fit in training (R<sup>2</sup> train = 0.311), sees its performance deteriorate on the test set (R<sup>2</sup> = 0.118), suggesting limited generalization ability. Positive ∆R <sup>2</sup> values for the ANN and SVR models also confirm an increased sensitivity to model complexity in approach 1. In contrast, approach 2 (leak-free) leads to a notable improvement in performance for all models, highlighting the impact of input parameters. The Ridge model shows significant progress with an R<sup>2</sup> test = 0.306, accompanied by a reduction in RMSE and MAE errors. The ANN model achieves an R<sup>2</sup> = 0.281, indicating a more balanced compromise between learning and generalization. The SVR model stands out in particular in this approach, with the best overall performance (R<sup>2</sup> test = 0.435) among the evaluated models, combined with the lowest error values on the test set (RMSE = 0.323 and MAE = 0.253). ∆R <sup>2</sup> values confirm that, despite increased complexity, SVR retains superior generalization ability among the evaluated models when trained in a leak-free setting. Overall, approach 2 (five variables) systematically outperforms approach 1 (OLS-selected variables), confirming the benefit of including all five operational features; these results highlight that rigorous hyperparameter selection, combined with a leak-free methodology, allows non-linear models, particularly SVR, to exploit available information more effectively while maintaining a satisfactory balance between accuracy and predictive robustness [\[33\]](#page-16-6). Figure [1](#page-7-0) illustrates the performance of the selected SVR model, showing the distribution of actual values relative to predicted values and the dispersion of residuals on the real test set.

<span id="page-8-0"></span>**Table 5.** Results analysis of the performance of MLR, ANN, and SVR models with significant and 5-input variables.

| Model                          | 2<br>R<br>train | R2<br>test | RMSE_train | RMSE_test | MAE_train | MAE_test | delta_R2  |
|--------------------------------|-----------------|------------|------------|-----------|-----------|----------|-----------|
| Approach1_RIDGE                | 0.177193        | 0.191613   | 0.382079   | 0.385828  | 0.316296  | 0.334779 | −0.014420 |
| Approach1_ANN                  | 0.229989        | 0.164943   | 0.369618   | 0.392141  | 0.300564  | 0.317683 | 0.065046  |
| Approach1_SVR                  | 0.311221        | 0.118165   | 0.349578   | 0.402975  | 0.259448  | 0.308487 | 0.193056  |
| Approach2_RIDGE<br>(leak-free) | 0.226471        | 0.306325   | 0.370461   | 0.357407  | 0.298459  | 0.312146 | −0.079854 |
| Approach2_ANN<br>(leak-free)   | 0.345328        | 0.281063   | 0.340813   | 0.363856  | 0.259714  | 0.286287 | 0.064266  |
| Approach2_SVR<br>(leak-free)   | 0.681053        | 0.434703   | 0.237883   | 0.322643  | 0.164808  | 0.253027 | 0.246350  |

Figure [2](#page-9-0) provides a complementary assessment of the SVR model's performance on the entire actual test set. Comparison of the distributions of observed and predicted values shows satisfactory overall coverage, indicating that the model successfully reproduces the general trend and range of variation in the TMP, despite slight deviations for some high values. Residual analysis shows a distribution that is generally centered around zero, with no marked systematic bias, suggesting a generally balanced prediction, although a few extreme residuals reflect occasional errors. Finally, the observed versus predicted graph *Eng* **2026**, *7*, 106 10 of 17

<span id="page-9-0"></span>illustrates a moderate correlation between actual and estimated values (R<sup>2</sup> = 0.435), with a dispersion around the ideal line, confirming a reasonable generalization capacity of the SVR model while highlighting that there is still margin for improvement, particularly for extreme values.

![](_page_9_Figure_2.jpeg)

**Figure 2.** SVR performance on the real test set. Residual distribution (observed − predicted) shown as orange histograms with the corresponding density curve; the black vertical line indicates zero residual. Observed vs. predicted TMP values are shown as pink dots; the black dashed line represents the identity line (y = x).

#### 3.2.2. Overfitting Test

A leak-free analysis of overfitting, based on the difference between training and testing R<sup>2</sup> (Train R<sup>2</sup> − Test R<sup>2</sup> ) and 100% real test set, is shown in Table [5](#page-8-0) and Figure [3,](#page-9-1) and highlights distinct behaviors depending on the model. SVR shows marked overfitting (∆R <sup>2</sup> ≈ 0.25), reflecting a strong ability to adjust to training data but limited generalization. Conversely, the Ridge model shows underfitting behavior (∆R <sup>2</sup> < 0), revealing a structural bias related to its linear nature. ANN displays a moderate training/test gap (∆R <sup>2</sup> ≈ 0.06), indicating a more balanced bias–variance trade-off and better generalization stability, although its predictive performance remains inferior to that of SVR in learning [\[34,](#page-16-7)[35\]](#page-16-8).

<span id="page-9-1"></span>![](_page_9_Figure_6.jpeg)

**Figure 3.** Overfitting diagnostic (∆R 2 ).

*Eng* **2026**, *7*, 106 11 of 17

An analysis of learning curves was performed to evaluate the generalization behavior and overfitting risk of the SVR and ANN models (Figure [4\)](#page-10-0). The SVR learning curve shows marked overfitting, characterized by high and stable performance in learning (R <sup>2</sup> ≈ 0.68–0.75) and significantly lower performance in cross-validation (R<sup>2</sup> ≈ 0.30–0.35). The persistent gap between the learning and validation curves, which does not narrow with increasing training set size, indicates a high variance regime and limited generalization ability. This structural divergence suggests that the complexity of the model is not sufficiently controlled by regularization and that increasing the volume of data alone does not correct overfitting. ANN learning curves (leak-free learning, early stopping enabled) show rapid and stable convergence of training loss, associated with an increase and then stabilization of validation performance (R<sup>2</sup> ). The absence of degradation in validation performance over time, as well as the absence of divergence between training and validation, indicate effective control of overfitting. The model thus exhibits stable and robust behavior, characterized by a balanced trade-off between bias and variance. However, the stabilization of performance suggests a limitation related to the informative capacity of the data rather than to learning instability [\[36](#page-16-9)[,37\]](#page-16-10).

<span id="page-10-0"></span>![](_page_10_Figure_2.jpeg)

**Figure 4.** Learning curves of SVR and ANN models. Solid lines represent the mean performance, while shaded areas (pink for training, brown for validation) indicate ±1 standard deviation across cross-validation folds.

Uncertainty analysis based on 95% bootstrap confidence intervals on a real test set reveals significant variability in SVR model performance, with an R<sup>2</sup> of 0.435 and a wide 95% CI ([0.102; 0.642]), confirming that the point estimate of R<sup>2</sup> ≈ 0.43 carries substantial uncertainty. Claims of superior or strong performance must be tempered: The lower bound (0.10) is near zero explanatory power. This uncertainty is consistent with the robustness analysis using repeated K-Fold (5 × 3, 15 runs) on real data, which shows an average performance of R<sup>2</sup> ≈ 0.325, associated with high dispersion (σ ≈ 0.213) and a wide range of variation (q05–q95 ≈ [−0.050; 0.620]), indicating high sensitivity to training subsamples. The mean CV R<sup>2</sup> = 0.325 ± 0.213 (5th–95th percentile: −0.050 to 0.620); this is lower and more variable than the holdout R<sup>2</sup> = 0.435, consistent with the moderate performance narrative. Some folds yield negative R<sup>2</sup> , confirming that model reliability varies considerably across data splits. Convergence between the wide bootstrap confidence intervals and the high inter-fold variability reveals high model variance and unstable generalization, confirming overfitting behavior (unbalanced trade-off between bias and variance), in line with the diagnostics derived from the learning curves and ∆R <sup>2</sup> analysis; the results of bootstrap IC 95% and robustness analysis are presented in Table [6](#page-11-0) [\[38\]](#page-16-11). Full numerical results, including detailed cross-validation statistics, complete γ-sensitivity tables, and Diebold–Mariano test results, are provided in the Supplementary Material (Tables S1 and S2, Figure S1) for readers interested in the complete technical details.

*Eng* **2026**, *7*, 106 12 of 17

<span id="page-11-0"></span>**Table 6.** Bootstrap IC 95% (real test—39 observations).

| Model | 2 Test<br>R | IC Bootstrap 95% (R2<br>) | RMSE   | IC Bootstrap 95% (RMSE) | MAE    | IC Bootstrap 95% (MAE) |
|-------|-------------|---------------------------|--------|-------------------------|--------|------------------------|
| SVR   | 0.4347      | [0.1022; 0.6421]          | 0.3226 | [0.2455; 0.3900]        | 0.2530 | [0.1920; 0.3160]       |

## 3.2.3. Significance of Differences Between Models

SVR, ANN, and Ridge performance was evaluated on the 100% real test set (n = 39), where the lag parameter *h* corresponds to the state used to predict the current TMP. Errors were assessed using MAE and MSE. Given the i.i.d. state–response structure of the dataset, model comparisons rely primarily on paired permutation tests and bootstrap confidence intervals computed on the real test observations. These analyses illustrated in Table [7](#page-11-1) reveal a nuanced pattern. For SVR versus Ridge, the mean ∆MAE is negative (lower error for SVR), and the 95% bootstrap confidence interval excludes zero (p\_perm ≈ 0.03), indicating a statistically significant advantage at α = 0.05 for absolute error. In contrast, although the mean ∆MSE is also negative, its confidence interval includes zero (p\_perm ≈ 0.28), suggesting no statistically significant difference in squared error. This indicates that the observed SVR improvement is mainly driven by reductions in moderate deviations rather than the systematic mitigation of larger errors. For SVR versus ANN and ANN versus Ridge, neither ∆MAE nor ∆MSE reaches statistical significance, implying that these performance differences cannot be reliably distinguished given the limited test size (n = 39). Overall, the evidence supports a modest and partially supported advantage of SVR over Ridge—significant for MAE but not for MSE—while comparisons involving ANN remain statistically inconclusive. For completeness, a DM test based on row order as a proxy chronology is reported in Supplementary Material (Table S2). However, in the absence of timestamps, this test is considered illustrative only and does not constitute a formal time-series validation. Consequently, inference is based primarily on the paired bootstrap and permutation results rather than on the DM statistic.

<span id="page-11-1"></span>**Table 7.** Model performance comparison based on error metrics.

| A_minus_B | delta_MAE_<br>mean | delta_MAE_<br>ci95_low | delta_MAE_<br>ci95_high | p_perm_<br>delta_MAE | delta_MSE_<br>mean | delta_MSE_<br>ci95_low | delta_MSE<br>_ci95_high | p_perm_<br>delta_MSE | n_test_<br>real |
|-----------|--------------------|------------------------|-------------------------|----------------------|--------------------|------------------------|-------------------------|----------------------|-----------------|
| SVR—RIDGE | −0.059119          | −0.109468              | −0.009519               | 0.029394             | −0.023641          | −0.064158              | 0.018027                | 0.280544             | 39              |
| SVR—ANN   | −0.033260          | −0.090285              | 0.025045                | 0.276945             | −0.028293          | −0.078970              | 0.026005                | 0.316937             | 39              |
| ANN—RIDGE | −0.025859          | −0.072781              | 0.022505                | 0.313137             | 0.004652           | −0.030025              | 0.042708                | 0.802839             | 39              |

## 3.2.4. Residual Autocorrelation Analysis: Durbin–Watson Test and Autocorrelation Function (ACF)

Using a proxy chronological ordering based on row indices (in the absence of an explicit time index), a temporal split (80% train, 20% test) was applied to explore potential residual sequential patterns. For the SVR model, the Durbin–Watson statistic is DW = 2.033, and the residual ACF (Figure [5\)](#page-12-0) shows coefficients close to zero across lags, indicating no pronounced autocorrelation under the adopted row-order proxy. In contrast, Ridge exhibits a slightly lower DW (1.74) and a few low-amplitude peaks in the ACF, suggesting limited sequential structure. Importantly, in the absence of true timestamps, these diagnostics do not establish genuine temporal independence; they only indicate the absence of marked sequential patterns relative to the given row ordering and should be interpreted as exploratory.

*Eng* **2026**, *7*, 106 13 of 17

<span id="page-12-0"></span>![](_page_12_Figure_1.jpeg)

**Figure 5.** Residual autocorrelation function (ACF) for SVR and Ridge models using a proxy temporal ordering.

## 3.2.5. SVR γ Parameter Sensitivity

A sensitivity analysis of the SVR model with respect to the γ parameter is provided in the Supplementary Material (Figure S1) with extreme values (γ = 100 and 1000), highlighting a clear non-linear bias–variance structure. This test checks whether extreme values of γ really improve generalization on the 100% real test, or whether they lead to overly local behavior (interpolation). It evaluates several γ values on the same optimal (leakage-free) pair (C, ε), and we also report the number of support vectors (complexity). For low γ values, the model exhibits marked underfitting, characterized by poor predictive performance and a high number of support vectors. Conversely, extreme γ values lead to a sharp degradation of performance, reflecting the overfitting and instability of the RBF kernel. The best performance is achieved for intermediate γ values (≈1–10 and γ = scale), corresponding to an optimal trade-off between model complexity and generalization ability, with minimal errors on the real test set and controlled structural complexity. These results confirm the robustness of SVR tuning and the absence of opportunistic hyperparameter optimization, as well as the methodological validity of the leak-free pipeline and the reliability of the reported performance.

#### 3.2.6. Partial Dependence Plots Analysis of TMP

The combined PDP and ICE analysis (Figure [6\)](#page-13-0) provided insights into the influence of conductivity and pH on the TMP predicted by the SVR model [\[39\]](#page-16-12). For conductivity, TMP exhibits a bell-shaped non-linear relationship, slightly increasing from ~43,000 to 45,000 µS/cm, peaking around 45,000 µS/cm, and then declining beyond 45,500 µS/cm. The wider confidence band (~44,500–45,500 µS/cm) in this region indicates increased uncertainty, suggesting model sensitivity and potential interactions with other variables. ICE curves further highlight individual variability, with some instances showing TMP values significantly higher or lower than the average. For pH, TMP gradually rises up to ~7.50 before stabilizing or slightly decreasing, with greater uncertainty at higher pH levels (7.45–7.50). The ICE curves also reveal notable sample-to-sample variability. The slight decrease in TMP at high conductivity, as suggested by the PDP, appears mainly as a statistical artifact due to the scarcity of observations and individual variability captured by the ICE curves, and does not contradict the established physics of reverse osmosis. At elevated conductivity levels, operational adjustments such as adaptive antiscalant dosing, cleaning interventions, or flow regulation may modulate the effective TMP response, leading to dataset-conditional behavior that does not directly reflect intrinsic osmotic pressure effects. It is important to emphasize that this data-driven model cannot be used to infer physical laws; therefore, the conductivity PDP tail should not be interpreted as implying that higher conductivity reduces TMP in general. Overall, these analyses indicate

*Eng* **2026**, *7*, 106 14 of 17

<span id="page-13-0"></span>that conductivity and pH are critical determinants of TMP, exhibiting non-linear main effects and condition-dependent sensitivity, offering valuable guidance for parameter optimization and understanding variable interactions [\[40,](#page-16-13)[41\]](#page-16-14).

![](_page_13_Figure_2.jpeg)

**Figure 6.** Partial dependence plot (PDP) and Individual Conditional Expectation (ICE) analysis of TMP. Gray lines represent individual ICE curves for each sample, the red line indicates the mean partial dependence, and the shaded area corresponds to the 5–95% variability band.

## *3.3. Global Synthesis of Results and Model Comparison*

This study is based exclusively on real operational data (n = 195), with a rigorously leak-free evaluation, and a test set consisting entirely of authentic observations (n = 39), independent of any augmentation procedure. A conservative SMOGN augmentation, applied only to the training data, stabilized model training without contaminating the validation folds or the final evaluation. On the real test set, SVR achieves, on average, the best predictive accuracy among the tested models on the real test set (R2\_test ≈ 0.43, RMSE ≈ 0.32, MAE ≈ 0.25), but with higher variance and a notable train–test gap (∆R 2 ), indicating a certain risk of overfitting. This limits its reliability for critical operational decisions without further external validation. Ridge is more stable but under-fits, while ANN is competitive in stability but less accurate than SVR on this dataset. The 95% bootstrap CI for SVR R<sup>2</sup> is wide (0.10–0.64), reflecting the instability inherent to small real sample sizes. The improvement of SVR over Ridge, while consistent, is modest and only partially supported statistically. Robustness was further assessed through multiple validation schemes (bootstrap, repeated K-Fold on real data, paired procedures), ensuring unbiased performance estimation. Paired statistical comparisons show a significant advantage of SVR over Ridge in terms of MAE (∆MAE = −0.059; 95% CI [−0.108, −0.009]; *p* = 0.0286), while other pairwise differences were not significant in this small test context. Sequential dependence analysis, based on a proxy temporal ordering, revealed no residual autocorrelation for SVR (Durbin–Watson ≈ 2; flat ACF), indicating that its performance does not rely on data-order bias. In contrast, Ridge displayed minor residual correlations, reflecting a limited ability to capture certain non-linear structures. In the absence of actual timestamps, no temporal forecasting claims can be made, and the problem is more accurately framed as a mapping from operational states to TMP rather than a time-series prediction task. SVR sensitivity to the γ parameter revealed a clear interpolation–generalization pattern: Performance peaks at moderate values (γ < 10 or γ = scale) and collapses at extreme values, ruling out any physical or operational interpretation of high γ as a meaningful optimum. Regarding interpretability, PDP + ICE analyses with empirical support revealed non-linear relationships, notably for conductivity and pH, but with strong inter-sample heterogeneity and significant inter-variable correlations. Importantly, the SVR model acts primarily as a similarity-based interpolator within the training domain, providing predictive insights without directly

*Eng* **2026**, *7*, 106 15 of 17

learning underlying physical relationships. These results support a dataset-dependent interpretation, rather than a universal mechanistic reading of the observed effects, highlighting the potential influence of unmeasured operational variables and multicollinearity. Overall, this study establishes a methodologically robust, interpretable, and statistically controlled framework for TMP modeling from real operational data, while clearly identifying structural limitations related to sample size and the absence of temporal indices. Predictions from the SVR model are reliable only within the range of operating conditions observed in the training data. Extrapolation to new regimes—such as different pretreatment processes, other membrane types, or substantially higher salinity—is not supported by the current dataset and should not be relied upon for operational decisions [\[42](#page-16-15)[,43\]](#page-16-16).

# <span id="page-14-0"></span>**4. Conclusions**

This study investigates the potential of TMP modeling at Boujdour desalination plant based on real operational data. The SVR model exhibited superior performance compared to Ridge and ANN, although its advantage remained moderate. A detailed analysis also revealed signs of overfitting for certain configurations, highlighting the need for cautious interpretation and the restriction of extreme hyperparameter values. The adopted approach—strict leakage control, uncertainty quantification, and interpretability constrained by empirical support—ensures the scientific robustness of the results. These findings confirm that non-linear modeling can capture complex relationships in membrane processes, while also revealing limitations related to the dataset size and operational variability. Generally, SVR represents a promising tool for decision support and TMP monitoring, enabling the anticipation of fouling and the optimization of membrane operation, while remaining aware of its limitations and the risk of overfitting. Future work should prioritize (a) the collection of multi-year datasets with explicit timestamps, (b) the inclusion of additional operational covariates such as antiscalant dosing and cleaning events, and (c) external validation across multiple installations.

**Supplementary Materials:** The following supporting information can be downloaded at: [https:](https://www.mdpi.com/article/10.3390/eng7030106/s1) [//www.mdpi.com/article/10.3390/eng7030106/s1,](https://www.mdpi.com/article/10.3390/eng7030106/s1) Table S1: Repeated K-Fold robustness (real folds, augmentation only inside fit); Figure S1: Impact of γ on SVR Performance: Bias–variance trade-off and model robustness; Table S2: DM-style proxy comparison (row-order split).

**Author Contributions:** S.K.: Methodology, Software, Validation, Formal analysis, Investigation, Writing—original draft; F.-Z.A.: Methodology, Software, Validation, Formal analysis, Investigation; M.B. (Maria Benbouzid): Methodology, Software, Investigation; Z.I.: Software, Formal analysis, Investigation; A.A.: Methodology, Data curation; A.B.: Conceptualization, Methodology, Data curation; H.N.: Conceptualization, Methodology, Data curation; M.B. (Meryem Bensemlali): Conceptualization, Methodology; S.Z.: Software, Validation, Formal analysis, Data curation; N.L.: Conceptualization, Methodology, Writing—review and editing; S.E.H.: Methodology, Validation, Formal analysis, Supervision, Writing—review and editing. All authors have read and agreed to the published version of the manuscript.

**Funding:** The authors gratefully acknowledge the financial support provided by the Moroccan national project AVENIR-ESEF (projects: A.Aarfane and H.Nasrellah) from the High School of Education and Training El Jadida, Chouaïb Doukkali University, El Jadida, Morocco.

**Institutional Review Board Statement:** Not applicable.

**Informed Consent Statement:** Not applicable.

**Data Availability Statement:** The original contributions presented in this study are included in the article/Supplementary Material. Further inquiries can be directed to the corresponding author.

**Conflicts of Interest:** The authors declare no conflicts of interest.

*Eng* **2026**, *7*, 106 16 of 17

# **References**

- <span id="page-15-0"></span>1. Mekonnen, M.M.; Hoekstra, A.Y. Four billion people facing severe water scarcity. *Sci. Adv.* **2016**, *2*, e1500323. [\[CrossRef\]](https://doi.org/10.1126/sciadv.1500323)
- <span id="page-15-1"></span>2. Damania, R.; Desbureaux, S.; Hyland, M.; Islam, A.; Moore, S.; Rodella, A.S.; Russ, J.; Zaveri, E. *Uncharted Waters: The New Economics of Water Scarcity and Variability*; World Bank Group: Washington, DC, USA, 2017.
- <span id="page-15-2"></span>3. Birch, H.; Pasture, L.d.L.; Gall, M.; Gasson, C.; Pankratz, T.; Quaresma, M.; Qureshi, Z.; Walker, C. *Market Focus Deck: Desalination & Reuse Markets*; Media Analytics Ltd.: Oxford, UK, 2023.
- <span id="page-15-3"></span>4. Jones, E.; Qadir, M.; Van Vliet, M.T.H.; Smakhtin, V.; Kang, S. The state of desalination and brine production: A global outlook. *Sci. Total Environ.* **2019**, *657*, 1343–1356. [\[CrossRef\]](https://doi.org/10.1016/j.scitotenv.2018.12.076) [\[PubMed\]](https://www.ncbi.nlm.nih.gov/pubmed/30677901)
- <span id="page-15-4"></span>5. Ruiz-García, A.; Melián-Martel, N.; Nuez, I. Short review on predicting fouling in RO desalination. *Membranes* **2017**, *7*, 62. [\[CrossRef\]](https://doi.org/10.3390/membranes7040062)
- <span id="page-15-5"></span>6. Mayaux, P.L.; Fernandez, S. Blinded like a state: Water scarcity and the quantification dilemma in Morocco. *Geoforum* **2024**, *155*, 104093. [\[CrossRef\]](https://doi.org/10.1016/j.geoforum.2024.104093)
- <span id="page-15-6"></span>7. Houdret, A.; Amichi, H. The rural social contract in Morocco Algeria: Reshaping through economic liberalisation new rules practices. *J. North Afr. Stud.* **2022**, *27*, 641–662. [\[CrossRef\]](https://doi.org/10.1080/13629387.2020.1848560)
- <span id="page-15-7"></span>8. Hafsi, M. Analysis of Boujdour desalination plant performance. *Desalination* **2001**, *134*, 93–104. [\[CrossRef\]](https://doi.org/10.1016/s0011-9164(01)00119-9)
- <span id="page-15-8"></span>9. Dhakal, N.; Abushaban, A.; Mangal, M.N.; Abunada, M.; Schippers, J.C.; Kennedy, M. Membrane fouling and scaling in reverse osmosis. In *Membrane Desalination*; Sapalidis, A., Ed.; CRC Press: Boca Raton, FL, USA, 2020; pp. 325–344.
- <span id="page-15-9"></span>10. AlSawaftah, N.; Abuwatfa, W.; Darwish, N.; Husseini, G. A comprehensive review on membrane fouling: Mathematical modeling, prediction, diagnosis, and mitigation. *Water* **2021**, *13*, 1327. [\[CrossRef\]](https://doi.org/10.3390/w13091327)
- <span id="page-15-10"></span>11. Abdulsalam, A.; Le, T.P.P.; Nguyen, T.S.; Ali, J.K.; Abubasha, M.Y.; Jouini, M.S.; Alhseinat, E. A review of fouling prediction techniques in membrane desalination: From empirical to intelligent models. *Desalination* **2025**, *616*, 119363. [\[CrossRef\]](https://doi.org/10.1016/j.desal.2025.119363)
- <span id="page-15-11"></span>12. Meighani, H.M.; Dehghani, A.; Rekabdar, F.; Hemmati, M.; Goodarznia, I. Artificial intelligence vs. classical approaches: A new look at the prediction of flux decline in wastewater treatment, Desalin. *Desalination Water Treat.* **2013**, *51*, 7476–7489. [\[CrossRef\]](https://doi.org/10.1080/19443994.2013.773861)
- <span id="page-15-12"></span>13. Niu, C.; Li, X.; Dai, R.; Wang, Z. Artificial Intelligence-Incorporated Membrane Fouling Prediction for Membrane-Based Processes in the Past 20 Years: A Critical Review. *Water Res.* **2022**, *216*, 118299. [\[PubMed\]](https://www.ncbi.nlm.nih.gov/pubmed/35325824)
- <span id="page-15-13"></span>14. Arshad, U.; Taqvi, S.A.A.; Buang, A.; Awad, A. SVM, ANN, and PSF modelling approaches for prediction of iron dust minimum ignition temperature (MIT) based on the synergistic effect of dispersion pressure and concentration. *Process Saf. Environ. Protect.* **2021**, *152*, 375–390. [\[CrossRef\]](https://doi.org/10.1016/j.psep.2021.06.001)
- <span id="page-15-14"></span>15. Abunada, M.; Dhakal, N.; Gulrez, R.; Ajok, P.; Li, Y.; Abushaban, A.; Smit, H.; Kennedy, M.D. Prediction of particulate fouling in full-scale reverse osmosis plants using the modified fouling index—Ultrafiltration (MFI-UF) method. *Desalination* **2023**, *553*, 116478. [\[CrossRef\]](https://doi.org/10.1016/j.desal.2023.116478)
- <span id="page-15-15"></span>16. Teng, Y.A.; Yong, N.H. Prediction of reverse osmosis membrane fouling in water reuse by integrated adsorption and data-driven models. *Desalination* **2024**, *576*, 117353. [\[CrossRef\]](https://doi.org/10.1016/j.desal.2024.117353)
- <span id="page-15-16"></span>17. Lim, S.J.; Kim, Y.M.; Park, H.; Ki, S.; Jeong, K.; Seo, J.; Chae, S.H.; Kim, J.H. Enhancing accuracy of membrane fouling prediction using hybrid machine learning models. *Desalination Water Treat.* **2019**, *146*, 22–28. [\[CrossRef\]](https://doi.org/10.5004/dwt.2019.23444)
- <span id="page-15-17"></span>18. Roehl, E.A.; Ladner, D.A.; Daamen, R.C.; Cook, J.B.; Safarik, J.; Phipps, D.W.; Xie, P. Modeling fouling in a large RO system with artificial neural networks. *J. Membr. Sci.* **2018**, *552*, 95–106. [\[CrossRef\]](https://doi.org/10.1016/j.memsci.2018.01.064)
- <span id="page-15-18"></span>19. Abuwatfa, W.H.; AlSawaftah, N.; Darwish, N.; Pitt, W.G.; Husseini, G.A. A Review on Membrane Fouling Prediction Using Artificial Neural Networks (ANNs). *Membranes* **2023**, *13*, 685. [\[CrossRef\]](https://doi.org/10.3390/membranes13070685) [\[PubMed\]](https://www.ncbi.nlm.nih.gov/pubmed/37505052)
- <span id="page-15-19"></span>20. Elismaili, I.E.; Najy, M.; El Qryefy, M.; El Atmani, A.; Habibi, S.; El Kharrim, K.; Belghyti, D. Study of desalination processes of seawater from the desalination plant of Laayoune (South of Morocco). *Invent. J. Res. Technol. Eng. Manage.* **2018**, *2*, 1–6.
- <span id="page-15-20"></span>21. Kherraf, S.; Bakkouche, C.; Barhmi, S.; Mabrouki, J.; El Hajjaji, S.; Elfatni, O.; Dhiba, D.; Maissine, K. Forecasting of Permeate Conductivity using MLR and ANN Methods of Boujdour Seawater Reverse Osmosis Desalination Plant. *Curr. Anal. Chem.* **2023**, *19*, 348–355. [\[CrossRef\]](https://doi.org/10.2174/1573411019666230221143245)
- <span id="page-15-21"></span>22. Guisan, A.; Edwards, T.C.; Hastie, T. Generalized linear and generalized additive models in studies of species distributions: Setting the scene. *Ecol. Model.* **2002**, *157*, 89–100. [\[CrossRef\]](https://doi.org/10.1016/s0304-3800(02)00204-1)
- <span id="page-15-22"></span>23. Arulsundar, N.; Subramanian, N.; Murth, R.S.R. Comparison of artificial neural networks and multiple liner regression in optimization of formulation parameters of leuprlide acetate loaded leptosomes. *J. Pharm. Sci.* **2005**, *8*, 243–258.
- <span id="page-15-23"></span>24. Schreiber-Gregory, D.N. Ridge regression and multicollinearity: An in-depth review. *Model Assist. Stat. Appl.* **2018**, *13*, 359–365. [\[CrossRef\]](https://doi.org/10.3233/MAS-180446)
- <span id="page-15-24"></span>25. Schmitt, F.; Banu, R.; Yeom, I.T.; Do, K.U. Development of artificial neural networks to predict membrane fouling in an anoxicaerobic membrane bioreactor treating domestic wastewater. *Biochem. Eng. J.* **2018**, *133*, 47–58. [\[CrossRef\]](https://doi.org/10.1016/j.bej.2018.02.001)
- <span id="page-15-25"></span>26. Charrouf, O.; Betka, A.; Abdeddaim, S.; Ghamri, A. Artificial neural network power manager for hybrid PV-wind desalination system. *Math. Comput. Simul.* **2020**, *167*, 443–460. [\[CrossRef\]](https://doi.org/10.1016/j.matcom.2019.09.005)

*Eng* **2026**, *7*, 106 17 of 17

<span id="page-16-0"></span>27. Esmail, M.; Saif, A.; Ragheb, A.; Alshebeili, S.A. Free space optic channel monitoring using machine learning. *Opt. Express* **2021**, *29*, 10967–10981. [\[CrossRef\]](https://doi.org/10.1364/oe.416777) [\[PubMed\]](https://www.ncbi.nlm.nih.gov/pubmed/33820219)

- <span id="page-16-1"></span>28. Ortiz-García, E.G.; Salcedo-Sanz, S.; Perez-Bellido, A.M.; Portilla-Figueras, J.A.; Prieto, L. Prediction of hourly O<sup>3</sup> concentrations using support vector regression algorithms. *Atmos. Environ.* **2010**, *44*, 4481–4488. [\[CrossRef\]](https://doi.org/10.1016/j.atmosenv.2010.07.024)
- <span id="page-16-2"></span>29. Nohair, M.; St-Hilaire, A.; Ouarda, T.B. The bayesian-regularized neural network approach to model daily water temperature in a small stream. *Water Sci.* **2008**, *21*, 373–382.
- <span id="page-16-3"></span>30. Barhmi, S.; Elfatni, O.; Belhaj, I. Forecasting of wind speed using multiple linear regression and artificial neural networks. *Energy Syst.* **2020**, *11*, 935–946.
- <span id="page-16-4"></span>31. Mohandes, M. Support vector machine for shortterm electrical load forecasting. *Int. J. Energy Res.* **2002**, *26*, 335–345. [\[CrossRef\]](https://doi.org/10.1002/er.787.abs)
- <span id="page-16-5"></span>32. Hou, Z.; Lian, Z. An application of support vector machines in cooling load prediction. In Proceedings of the 2009 International Workshop on Intelligent Systems and Applications, Wuhan, China, 23–24 May 2009; pp. 1–4.
- <span id="page-16-6"></span>33. Louis, B.; Agrawal, V.K.; Khadikar, P.V. Prediction of intrinsic solubility of generic drugs using MLR, ANN and SVM analyses. *Eur. J. Med. Chem.* **2010**, *45*, 4018–4025. [\[CrossRef\]](https://doi.org/10.1016/j.ejmech.2010.05.059)
- <span id="page-16-7"></span>34. Leng, X.; Wang, J.; Ji, H.; Wang, Q.; Li, H.; Qian, X.; Li, F.; Yang, M. Prediction of size-fractionated airborne particle-bound metals using MLR, BP-ANN and SVM analyses. *Chemosphere* **2017**, *180*, 513–522. [\[PubMed\]](https://www.ncbi.nlm.nih.gov/pubmed/28431389)
- <span id="page-16-8"></span>35. Zhang, H.; Nguyen, H.; Bui, X.N.; Pradhan, B.; Asteris, P.G.; Costache, R.; Aryal, J. A generalized artificial intelligence model for estimating the friction angle of clays in evaluating slope stability using a deep neural network and Harris Hawks optimization algorithm. *Eng. Comput.* **2022**, *38*, 3901–3914. [\[CrossRef\]](https://doi.org/10.1007/s00366-020-01272-9)
- <span id="page-16-9"></span>36. Ashrafian, A.; Panahi, E.; Salehi, S.; Karoglou, M.; Asteris, P.G. Mapping the strength of agro-ecological lightweight concrete containing oil palm by-product using artificial intelligence techniques. *Structures* **2023**, *48*, 1209–1229. [\[CrossRef\]](https://doi.org/10.1016/j.istruc.2022.12.108)
- <span id="page-16-10"></span>37. Kherraf, S.; Ennouhi, M.; el Mansouri, A.; el Hajjaji, S.; Nasrellah, H.; Bensemlali, M.; Aarfane, A.; Cherrat, A.; Labjar, N. Autopsy Results and Inorganic Fouling Prediction Modeling Using Artificial Neural Networks for Reverse Osmosis Membranes in a Desalination Plant. *Eng* **2025**, *6*, 98. [\[CrossRef\]](https://doi.org/10.3390/eng6050098)
- <span id="page-16-11"></span>38. Xu, Z.; Cuquerella-Gilabert, M.; Zarzoso-Foj, J.; Merino-Sanjuan, M.; Mangas-Sanjuan, V.; García-Arieta, A. Comparison of dissolution profiles: 90% confidence intervals of different f2 estimators using bootstrap methodology versus the Euclidean Distance of the Non-standardized Expected (EDNE) values. *Eur. J. Pharm. Biopharm.* **2025**, *216*, 114839. [\[CrossRef\]](https://doi.org/10.1016/j.ejpb.2025.114839)
- <span id="page-16-12"></span>39. Sawarkar, P.G.; Pote, A.; Khan, M.A.; Abed, M.H.; Hadi, A.A.; Smerat, A.; Khishe, M. Sustainable geopolymer concrete evaluation using machine learning and PDP analysis: Comparative insights into strength prediction. *Hybrid Adv.* **2025**, *11*, 100569. [\[CrossRef\]](https://doi.org/10.1016/j.hybadv.2025.100569)
- <span id="page-16-13"></span>40. Paris, G.; Robilliard, D.; Fonlupt, C. (2004) Exploring Overfitting in Genetic Programming. In Proceedings of the Artificial Evolution, 6th International Conference, Evolution Artificielle, EA 2003, Marseilles, France, 27–30 October 2003; DBLP; pp. 267–277.
- <span id="page-16-14"></span>41. Caruana, R.; Lawrence, S.; Giles, L. Overfitting in neural nets: Backpropagation, conjugate gradient, and early stopping. In *Proceedings of the International Conference on Neural Information Processing Systems 13, Papers from Neural Information Processing Systems (NIPS) 2000*; MIT Press: Denver, CO, USA, 2000; pp. 381–387.
- <span id="page-16-15"></span>42. Lan, S.; Wu, L.; Zhang, D.; Hu, C. Effects of light and temperature on open cultivation of desert cyanobacterium *Microcoleus vaginatus*. *Bioresour. Technol.* **2015**, *182*, 144–150. [\[CrossRef\]](https://doi.org/10.1016/j.biortech.2015.02.002)
- <span id="page-16-16"></span>43. Tayeh, Y.A.; Alazaiza, M.Y.D.; Alzghoul, T.M.; Bashir, M.J.K. A comprehensive review of RO membrane fouling: Mechanisms, categories, cleaning methods and pretreatment technologies. *J. Hazard. Mater. Adv.* **2025**, *18*, 100684. [\[CrossRef\]](https://doi.org/10.1016/j.hazadv.2025.100684)

**Disclaimer/Publisher's Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.
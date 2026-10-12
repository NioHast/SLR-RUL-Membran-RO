ELSEVIER

Contents lists available at ScienceDirect

# Desalination and Water Treatment

journal homepage: www.sciencedirect.com/journal/desalination-and-water-treatment/

![](_page_0_Picture_5.jpeg)

![](_page_0_Picture_6.jpeg)

# Harnessing machine learning for transmembrane pressure prediction in MBR systems during textile wastewater treatment

Onaira Zahoor<sup>a</sup>, Sher Jamal Khan<sup>a</sup>, Muhammad Usama<sup>b</sup>, Henry J. Tanudjaja<sup>c</sup>, Noreddine Ghaffour<sup>c</sup>, Muhammad Saqib Nawaz<sup>c,\*</sup>

- <sup>a</sup> Institute of Environmental Sciences and Engineering (IESE), School of Civil and Environmental Engineering (SCEE), National University of Sciences and Technology (NUST), Sector H-12, Islamabad, Pakistan
- <sup>b</sup> Department of Civil and Environmental Engineering, Northeastern University, Boston, MA 02115, USA
- <sup>c</sup> Environmental Science and Engineering Program, Division of Biological and Environmental Science and Engineering (BESE), King Abdullah University of Science and Technology (KAUST), Thuwal 23955-6900, Saudi Arabia

#### HIGHLIGHTS

- Transmembrane pressure (TMP) predicted in MBR treating textile wastewater.
- Random forests, support vector, and lasso regression models used for prediction.
- Machine learning (ML) model uncertainties and extreme values bias are quantified
- Importance rank of the sludge parameter towards membrane fouling was determined
- TMP prediction via ML models offer insights into key operational challenges.

#### ARTICLE INFO

Keywords:
Machine learning models
Transmembrane pressure
Textile wastewater treatment
Extra polymeric substances
Membrane bioreactor

#### GRAPHICAL ABSTRACT

![](_page_0_Figure_21.jpeg)

## ABSTRACT

Membrane Bioreactors (MBRs) are preferred for treating high-strength industrial wastewater due to their exceptional treatment efficiency and compact design. However, membrane fouling remains a significant challenge that limits their broader application. Since transmembrane pressure (TMP) is closely associated with membrane fouling mechanisms, its accurate prediction is essential for anticipating fouling events. This study focuses on predicting TMP in a bench-scale MBR by employing advanced regression models such as Lasso, support vector machines, and random forest. The bioreactor is operated using synthetic textile wastewater, with a primary focus on critical sludge parameters. A total of 60 datasets were compiled for training and testing of the models. The random forest model attained an  $R^2$  of 0.95 and 0.86 and root mean square error values of 1.75 kPa and 3.3 kPa for the training and test datasets, respectively, demonstrating the best predictive accuracy. Extra polymeric substances were the most influential parameter, while particle size distribution was the least. The random forest and lasso regression models predicted high values more accurately, while the support vector regression model was inclined towards making more conservative predictions for extreme values. The effectiveness of the proposed models showcases the significance of utilizing machine learning in advancing MBR technology for wastewater treatment. Accurate TMP predictions through machine learning can help in

E-mail address: muhammad.nawaz.1@kaust.edu.sa (M.S. Nawaz).

<sup>\*</sup> Corresponding author.

## **1. Introduction**

The discharge of untreated wastewater from residential and industrial sectors endangers both terrestrial and groundwater reserves. As water demand continues to surpass available resources, the advancement of wastewater treatment technologies becomes crucial for conserving water and addressing shortages. Textile wastewater is particularly challenging due to its high concentrations of dyes, salts, suspended solids, and processing chemicals [\[1](#page-10-0)**,2**]. As a result, effluents from the textile industry adversely affect the environment by altering the physical, chemical, and biological properties of the receiving water bodies [\[3\]](#page-10-0). The complex nature of textile effluents demands strict global discharge standards, making it essential to treat textile wastewater before disposal. Effective wastewater treatment removes all pollutants and produces high-quality effluent, ensuring safe discharge and easing pressure on natural resources [\[4\].](#page-10-0)

Membrane Bioreactor (MBR) technology has become a leading method for wastewater treatment, integrating conventional biological processes with membrane filtration under various conditions [\[5\].](#page-10-0) They are favored for their high treatment efficiency and compact footprint. Despite its advantages, the widespread application of the MBR process is constrained by membrane fouling, which significantly limits its broader use. Thus, membrane fouling remains a critical issue in MBR systems [\[6](#page-10-0)**,**  [7\]](#page-10-0). It involves the accumulation of solid particles on the membrane surface or the intrusion of colloidal particles into the membrane pores [\[8\].](#page-10-0) This leads to a decline in the membrane's hydraulic performance, resulting in reduced permeability or a rapid rise in transmembrane pressure (TMP). Consequently, this drives up maintenance and operating costs due to increased energy consumption and the need for frequent membrane cleaning. Therefore, controlling fouling in MBRs is crucial for maintaining optimal performance, extending membrane lifespan, and ensuring consistent product quality [\[9\].](#page-10-0) Timely cleaning or replacement of membrane modules before the occurrence of fouling can extend their service life and reduce operating cost [\[10](#page-10-0)**]**.

The MBRs are operated by either keeping the permeate flux constant with TMP increasing gradually or at a constant TMP with periodically declining flux due to membrane fouling. The subsequent rise in TMP and membrane fouling is determined by various parameters, hydrodynamic conditions and the chemical composition of wastewater [\[11\]](#page-10-0). Similarly, the length of the membrane's operation cycle in the MBR system is of utmost importance. Therefore, analysis of physical and chemical interactions in the system is necessary [\[12\].](#page-10-0) Thus, there is a need for precise analysis and accurate prediction of membrane fouling to provide effective decision support in MBR systems [\[13\]](#page-10-0). Given the strong association between TMP and the processes that cause membrane fouling, TMP prediction is highly related to membrane fouling forecasting [\[12\]](#page-10-0). Researchers have traditionally used mathematical models incorporating membrane flux, TMP, and pollutant rejection to predict membrane fouling in wastewater treatment. However, conventional models are limited by their inflexibility, high data requirements, and reliance on simplified assumptions, reducing their effectiveness across varying membrane systems and conditions [\[14\]](#page-10-0).

Membrane fouling primarily arises due to three factors: operating conditions, membrane properties, and the characteristics of the sludge mixture [\[11\].](#page-10-0) In the literature, mechanistic models have been increasingly applied to predict membrane fouling behaviors in membrane-based processes [\[15\]](#page-10-0). These models are developed by considering the physical phenomena occurring within the particular analyzed process. For instance, Pizzichetti and Cristina conducted an in-depth analysis of membrane fouling caused by various microplastics, evaluating the trends of kinetic constants under different operational

conditions and aiming to determine optimal filtration settings using the famous Hermia's equations [\[16,17\]](#page-10-0). Another mechanistic model presented the idea of predicting TMP by utilizing MBR process parameters and the resistance-in-series [\[18\]](#page-10-0). While such mechanistic models have been applied successfully, they have certain limitations. These models often require considerable time for development and solution.

The complexity of membrane fouling cannot be fully captured due to the dynamic and non-linear characteristics of the MBR systems. These models are unable to provide a comprehensive picture of membrane fouling without considering the temporal variations [\[19\]](#page-10-0). Additionally, the influence of operating parameters on membrane fouling can vary significantly among different systems. Many models reported in the literature are empirical or semi-empirical [\[20\]](#page-10-0). As a result, there is an increasing demand for advanced methods to more effectively predict membrane performance and fouling.

Machine learning models have shown promise in membrane research and are anticipated to be crucial for designing systems, optimizing processes, and predicting fouling [\[15\]](#page-10-0). These models can identify complex patterns in large datasets, enabling accurate predictions and efficient optimization of membrane systems' capabilities that traditional models may not offer [\[21,22\].](#page-10-0) Recently, various machine learning models have been developed and successfully validated for predicting membrane fouling in different types of MBRs. For example, David and team accurately predicted TMP based on artificial neural network (ANN), random forest and long short-term memory models using 4 years high-resolution data of a wastewater treatment plant at various stages of the MBR production cycle [\[12\].](#page-10-0) In another study, an ANN was applied to a four-month dataset from a pilot-sized MBR, using mixed liquor suspended solids (MLSS) concentration, hydraulic retention time as input variables to successfully predict chemical oxygen demand (COD) and TMP [\[23\]](#page-10-0).

Similarly, a random forest model was implemented on the Hadoop big data platform to predict membrane fouling by forecasting membrane flux. ANN and support vector machine models were also developed to assess and compare the random forest model's accuracy, showing that it outperformed the others [\[24\]](#page-10-0). By inputting ten parameters measured at various locations, Schmitt and co-workers predicted TMP differences in an anoxic-aerobic membrane bioreactor treating domestic wastewater using ANN [\[25\].](#page-10-0) Despite their promising results, the data-driven models have several limitations. Previously developed models are often built on small datasets or have often neglected important parameters as key predictor variables. For instance, sludge properties in MBR systems are mostly overlooked in many models or the models are built by using only a limited set of parameters. Meanwhile, sludge properties are crucial in MBR operations, impacting filtration and presenting challenges in managing excess sludge [\[26\].](#page-10-0) The poor sludge quality increases membrane fouling and decreases filtration performance.

Thus, optimizing sludge parameters can improve membrane fouling mitigation, extend membrane life, and reduce energy and cleaning costs. This study stresses the pivotal role of activated sludge parameters, such as MLSS, particle size distribution (PSD), specific oxygen uptake rate (SOUR), diluted sludge volume index (DSVI), and extra polymeric substances (EPS), and the importance rank of each parameter towards membrane fouling. Although various machine learning models have been applied for TMP prediction, to the best of our knowledge, no studies have simultaneously used all these activated sludge parameters as significant predictors. This study aims to; a) bridge this gap of overlooking sludge properties in an MBR system by predicting TMP using key sludge parameters and leveraging machine learning regression techniques, b) evaluate the performance of the developed models and compare model accuracy, c) understand the importance rank of each

sludge parameter on its influence towards the membrane fouling, and d) draw important information from the developed models for optimizing sludge parameters, to develop better strategies for membrane fouling mitigation, leading to prolonged membrane cycles and reduced energy consumption and cleaning costs.

#### 2. Material and methods

#### 2.1. Laboratory setup and operating procedures

An acrylic MBR was operated with a working volume of 16 L. The schematic diagram of the MBR system is shown in Fig. 1. A peristaltic pump (BT300–2 J, Longer Pump, China) was used to draw permeate through a submerged hollow fiber polyvinylidene fluoride (PVDF) membrane module (Mitsubishi Rayon, Japan) with a filtration area of 0.2  $\rm m^2$  and nominal pore size of 0.1  $\rm \mu m$ . The pump, connected to the membrane via a discharge line, operated in ten minutes on and two minutes off cycles. Continuous aeration was provided via rod-type diffusers placed at the bottom of the tank to keep the sludge in suspension and supply dissolved oxygen (DO) for microbial growth. The reactor was divided into two zones by perforated plates with a volume ratio of 1:2. The larger zone contained a mechanical mixer (50007–25, Cole-Parmer, USA), while the smaller zone housed air diffusers and the membrane. Aeration was maintained via fish tank air blowers at 3–6 liters per minute, achieving a DO level of 2–5 mg/L.

The MBR was operated for 120 days (including the sludge acclimatization phase). However, the data used for this study covers 60 days (three membrane cycles). The reactor operated at a hydraulic retention time of 12 hr and a solid retention time of 30 days. During this phase, efficiency and performance were evaluated for COD and nutrient removal from the textile wastewater, and sludge parameters were also analyzed. The application of powdered activated carbon (PAC) in a dosage of 100 mg/L/day to MBR was a reason for a slight increase in the reactor's MLSS concentration.

## 2.2. Textile wastewater composition

Textile wastewater was synthesized in the laboratory, copying the composition of real textile effluent received from a local textile industry.

The recipe comprised of hydrated D-glucose (1000 mg/L), ammonium chloride (760 mg/L), potassium dihydrogen phosphate (220 mg/L), calcium chloride (10 mg/L), magnesium sulphate (10 mg/L), ferric chloride (3.3 mg/L), magnesium chloride (2 mg/L) and sodium bicarbonate (800 mg/L) which was added as a buffer solution for pH adjustment. The synthetic textile feed wastewater characteristics were COD = 1000 mg/L, turbidity = 359 NTU, pH= 9–9.5, total organic carbon (TOC) = 407 mg/L, and total nitrogen (TN) = 147 mg/L.

#### 2.3. Analytical methods

The efficiency of MBR system was determined in terms of COD removal, dyes biodegradation and color removal, analyzed regularly. TOC and TN were analyzed by TOC/TN analyzer (Multi N/C Analytik Jena, Germany), and the nutrients (NO<sup>-3</sup>-N, NO<sup>-2</sup>-N, and NH<sup>+4</sup>-N) and PO<sup>-4</sup>-P were measured using a spectrophotometer (DR/2010, HACH, USA). DO and pH were measured using pH/DO meter (Oakton PD 300, USA). TMP was monitored by the data logging manometer (8400, Taiwan). For measuring TMP, the data logging manometer was connected to the membrane to record a complete profile of the pressure variation through the membrane.

The membrane was functional till the TMP reached 30 kPa, at the continuous desired flux rate of 6.25 liters per square meter per hour (LMH). The deposition of a cake layer on the membrane surface caused fouling, raising TMP over 30 kPa. The membrane was then physically and chemically cleaned, allowing the process to continue. The general profile of TMP during the process is shown in Fig. 2. The membrane fouled every 19–21 days on average. MLSS and mixed liquor volatile suspended solids (MLVSS) levels in the reactor were measured and evaluated weekly. Adding PAC in low dosage slightly increased the MLSS concentration. Measuring the SOUR helped in assessing the microbial respirometric activity by tracking DO depletion over a 30-minute aeration period.

Soluble EPS was analyzed by centrifugation of sludge sample using a centrifuge machine (Laborzentrifugen, Sigma 204, Germany), while for bound EPS extraction, the cation exchange resin method was adopted, as described elsewhere [27]. Carbohydrate and protein concentrations were measured using spectrophotometric methods stated in previous studies [28,29]. Sludge settleability was assessed by measuring the

![](_page_2_Picture_14.jpeg)

Fig. 1. Schematic diagram of MBR augmented with PAC.

<span id="page-3-0"></span>![](_page_3_Figure_2.jpeg)

**Fig. 2.** TMP profile during the filtration process.

DSVI. A higher index value is an indication of low sludge settleability, resulting in reduced filtration and vice versa. This index was measured according to protocols given in standard methods [\[30\].](#page-10-0) PSD was determined using a particle size analyzer (LA300, Horiba, Japan) through ultra-sonication followed by laser light scattering. The total resistance offered by the membrane to activated sludge, denoted by *Rt*, was measured. After physical cleaning, another filter run was performed at incremental flow rates to calculate the resistance by pore-clogging (R*p*). A third run was carried out to calculate the resistance offered by the membrane itself (Rm). To calculate this resistance, the membrane was chemically cleaned after 8 hr, and tap water was passed through the membrane. The resistances were evaluated using the equation reported in earlier study [\[31\]](#page-10-0).

Analysis of nascent and inside reactor PAC, biological activated carbon (BAC), was carried out in terms of parameters including pore size, pore volume and its surface area using nitrogen adsorption with micromeritics (Surface porosity and sample degas system, Gemini VII 2390 t, USA). The application of PAC into sludge resulted in decreased surface area, pore size and pore volume. Sludge containing PAC was taken twice a month, oven dried at 105 ◦C for 2 hr, and then analyzed. The laboratory performance evaluation for the MBR system is shown in Tables 1–3.

# *2.4. Characterization of PAC*

A substantial decrease in surface area (m2 /g) of nascent PAC (Single point: 545, BET: 540, Langmuir: 759.3) was observed after its conversion to BAC (Single point: 530 ± 10, BET: 546, Langmuir: 750 ± 5). Similarly, a significant decrease in pore size (40 %) from 2.5 nm to 0.01 nm was observed, revealing that there has been greater adsorption (pore saturation *>* 95 %) of the solute particles and dyes contained in the feed textile wastewater.

**Table 1**  Effluent parameters.

| Effluent Parameters | Average | Max  | Min   | SD   |
|---------------------|---------|------|-------|------|
| TN effluent (mg/L)  | 18      | 24   | 12.65 | 4.63 |
| TN removal (%)      | 87      | –    | –     | –    |
| TOC effluent (mg/L) | 30.2    | 36.2 | 18.14 | 5.82 |
| TOC removal (%)     | 92      | –    | –     | –    |
| COD effluent (mg/L) | 65      | 96   | 48    | 13   |
| COD removal (%)     | 93      | –    | –     | –    |
| NH+4<br>-N (mg/L)   | 4.87    | 6.42 | 3.92  | 0.82 |
| NO− 2<br>-N (mg/L)  | 4.63    | 5.98 | 3.25  | 0.82 |
| NO− 3<br>-N (mg/L)  | 5.98    | 7.92 | 5.19  | 0.92 |
| PO− 4<br>-P (mg/L)  | 2.74    | 3.42 | 2.32  | 0.94 |

**Table 2**  Activated sludge parameters.

| Parameter           | Average | Max  | Min  | SD   |
|---------------------|---------|------|------|------|
| MLSS (g/L)          | 9.5     | 11.8 | 6.8  | 1.01 |
| MLVSS (g/L)         | 7.12    | 8.4  | 5.2  | 0.67 |
| DSVI (ML/L)         | 74.5    | 84   | 62.5 | 5.93 |
| SOUR (mg/O2/gVSS/h) | 70      | 77   | 58   | 5.4  |
| PSD (µm)            | 78      | —    | —    | —    |

**Table 3**  Bound and soluble EPS (protein & polysaccharide components).

| Parameter            | Bound EPS (mg/L) | Soluble EPS (mg/L) |
|----------------------|------------------|--------------------|
| Protein              | 83.13 ± 10.14    | 10.60 ± 2.24       |
| Carbohydrate         | 28.73 ± 4.20     | 7.6 ± 1.25         |
| Total                | 111.86 ± 14.34   | 18.2 ± 3.49        |
| Protein/Carbohydrate | 2.89             | 1.39               |

## **3. Machine learning models development and evaluation**

The designated modeling scheme contained two steps. The first step modeled the relationship between different sludge parameters and TMP, and the other focused on prediction outcomes as a regression problem. The former step helped in exploring an association between TMP as a target variable and important sludge parameters as predictors by establishing a significant correlation (Pearson correlation). When two or more independent variables are highly correlated, i-e. above 0.80, the associated regression coefficients will result in a large standard error [\[32\]](#page-10-0). As a result, it becomes challenging or even impossible to accurately assess the impact of individual variables [\[33\].](#page-10-0) For this reason, inter-predictor correlations were treated as multi-collinearity problems. However, no two variables with a high level of collinearity were found before model construction.

To develop robust machine learning models for predicting TMP in a lab-scale MBR, we used a time series dataset of 58 observations, capturing daily TMP and sludge properties (MLSS, PSD, DSVI, B\_Car, SOUR) over 20-day cycles post-chemical cleaning. Autocorrelation analysis using the autocorrelation function in R revealed a strong lagone autocorrelation coefficient of 0.745, statistically significant at the 5 % level, indicating substantial temporal dependence in TMP values.

We avoided random splitting to prevent data leakage. Instead, we partitioned the data into a training set (first 80 %, 46 observations) and a testing set (last 20 %, 12 observations) to preserve chronological order, ensuring no future data influenced past predictions. Contrary to

random sampling, which is unsuitable for temporally correlated data, this method was chosen specifically to respect the strong autocorrelation identified in TMP values (lag-1 autocorrelation coefficient of 0.745, p<0.05). All models were implemented in R using the caret package, with the sequential split ensuring unbiased generalization assessment on temporally unseen data.

The analysis began with an initial dataset comprising eight variables. To refine the predictive relevance of our model, we excluded variables with a correlation effect size below 0.3, as they exhibited less influence on TMP. This process yielded five key predictors: PSD, MLSS, DSVI, SOUR, and B\_Car (representing carbonaceous EPS). Fig. 3 illustrates the model architectures, demonstrating their capability to reliably correlate sludge properties with TMP.

## 3.1. Random forest regression (RFR) model

RFR is an ensemble method that enhances the predictive power of decision trees by averaging the outputs of multiple trees, each trained on different subsets of the data and features. This approach improves accuracy and robustness and reduces overfitting. Each tree is trained on a bootstrapped sample, and a random subset of features is considered at each split. The final prediction is the average of all tree predictions. The out-of-bag (OOB) error, calculated using samples not included in the training of corresponding trees, offers an internal estimate of model performance without a separate validation set. Additionally, the random forest provides measures of feature importance, helping identify the most influential variables in predicting the target, thus clarifying the underlying structure of data. The mathematical expression for the random forest algorithm is given in Eq. 1 below.

$$f(x) = \frac{1}{\beta} \sum_{b=1}^{\beta} T_b(x)$$
 (1)

where "f(x)" represents the final predicted value for the input data point x, " $\beta$ " denotes the total number of trees, " $\sum_{b=1}^{\beta} T_b(x)$ " is the summation of the predictions from all the individual trees in the ensemble for the input data point x, and " $\frac{1}{\beta}$ " shows the average of the predictions from all the trees.

#### 3.2. Support vector regression (SVR)

Support vector machines (SVM), are used for classification and regression [34]. SVR adapts SVM to predict continuous outcomes by fitting a function within a tolerance margin (epsilon) around observed values. Support vectors, or data points outside this margin, shape the regression line. The regularization parameter "C" controls the trade-off between training error and model complexity. SVR can employ various kernel functions (linear, polynomial, radial basis) to capture complex, non-linear relationships between input features and the target variable. Mathematically, the SVR problem can be formulated as in Eq. 2:

$$f(x) = \sum_{i=1}^{n} (\alpha_i - \alpha_{i^*}) K(x_i, x) + b$$
 (2)

where "f(x)" is the predicted value, " $x_i$ " are the support vectors, " $K(x_i, x)$ " is the kernel function, " $\alpha_i$  and  $\alpha_i$ ." are the Lagrange multipliers, and "b" is the bias term.

![](_page_4_Figure_12.jpeg)

Fig. 3. Schematic of (a) Random forest regression, (b) Support vector regression, and (c) Lasso regression models.

#### 3.3. Lasso regression (L1R)

Lasso (Least absolute shrinkage and selection operator) is a linear regression technique that uses L1 regularization to enhance model accuracy and interpretability. By adding a penalty proportional to the sum of the absolute values of coefficients, Lasso can shrink some coefficients to zero, effectively selecting the most predictive features. This results in simpler, more interpretable models and helps prevent overfitting by discouraging overly complex models. The regularization strength is controlled by a parameter, " $\lambda$ ". Lasso also handles multicollinearity by selecting one variable from correlated groups and shrinking the others to zero. The mathematical formulation is given in Eq. 3:

$$\widehat{\beta} = \operatorname{argmin}_{\beta} \left\{ \frac{1}{2n} - \sum_{i=1}^{n} (y_i - X_i \beta)^2 + \lambda \sum_{i=1}^{p} |\beta_j| \right\}$$
(3)

where " $\widehat{\beta}"$  represents the estimated coefficients, "n" is the number of observations, "p" is the number of predictors, " $y_i$ " is the observed response for the i-th observation, " $X_i$ " is the vector of predictors for the i-th observation, " $\beta$ " is the vector of coefficients to be estimated, " $\lambda$ " is the regularization parameter that controls the amount of shrinkage applied to the coefficients, and " $\sum_{j=1}^p |\beta_j|$ " is the L1 norm of the coefficient vector, which adds the penalty for having large coefficients.

#### 3.4. Variables selection criteria and correlation matrix

Variable selection is intended to select the best predictor of an outcome for modeling. Because of the addition of unnecessary noise to the estimates of other variables, redundant insignificant variables are removed before modeling. Often, the variables are chosen for modeling based on statistical significance.

Variables with effect size  $\geq 0.3$  and significance level < 0.001 were selected based on prior reasoning or based on the ratio of observations to variables for the designed models [35]. Five of the eight variables analyzed for their correlation with TMP showed strong associations, as illustrated in Table 4. Carbonaceous bound EPS emerged as the most influential factor with the strongest correlation of 0.83 with TMP, signaling a significant positive impact, with DSVI following closely having a correlation of 0.76, reinforcing its critical role, while PSD and SOUR demonstrated notable positive correlations of 0.67 and 0.62, respectively. With a correlation of 0.58, MLSS also indicated a meaningful connection.

**Table 4**Correlation of different sludge parameters with TMP.

| Variable | Correlation with TMP |  |
|----------|----------------------|--|
| B_Car    | 0.83 * *             |  |
| MLSS     | 0.58 * *             |  |
| SOUR     | 0.62 * *             |  |
| DSVI     | 0.76 * *             |  |
| PSD      | 0.67 * *             |  |
| Sol_P    | 0.08                 |  |
| Sol_Car  | -0.28                |  |
| B Pro    | 0.13                 |  |
|          |                      |  |

<sup>-\*\*</sup> The correlation is significant at the 0.001 level (2-tailed).

Input variables for RFR and SVR: B Car, MLSS, SOUR, DSVI, and PSD.

Input variables for L1R: B Car, MLSS, SOUR, and DSVI.

- -B\_Car: (Bound EPS-Carbohydrates)
- -B\_Pro: (Bound EPS-Protein)
- -Sol\_P: (Soluble EPS-Protein) -Sol Car: (Soluble EPS-Carbohydrates)

#### 3.5. Uncertainty analysis

In machine learning based membrane fouling models, uncertainty stems from model structure, inputs, and parameters. This study also addresses uncertainties related to model structure and parameters by conducting an uncertainty analysis focused on hyperparameter and model structure uncertainties. Grid search was employed to quantify hyperparameter uncertainty, systematically exploring a predefined grid of values for parameter tuning, which offers a more thorough exploration compared to random sampling methods like Monte Carlo simulation and genetic algorithms that come with challenges for smaller datasets. The hyperparameters selected for analysis were ntree and mtry for random forest, cost, epsilon, kernel, and gamma for SVR, and lambda and alpha for L1R. To assess model structure uncertainty, the effect of different algorithms was evaluated on predicting extreme TMP values, examining minimum, maximum, and average predictions to understand model performance at the extremes.

### 3.6. Machine learning models for TMP prediction

In the MBR operation, the TMP increases mainly due to membrane fouling, and after reaching the manufacturer's specified value, the membrane cleaning procedure is deployed. The prediction of TMP with machine learning models helps for future operations where the TMP profile can be mapped early at the beginning of the process, and an adaptive cleaning plan can take place to mitigate severe fouling and prolong membrane operational time. In this study, three models, RFR, SVR, and L1R were used to predict TMP using five key variables. Since TMP values vary across different stages of the MBR production cycle, the data was divided into three subsets, creating an index (k = 3), corresponding to three production cycles (19-21 days on average), ensuring that the training and testing data were specific to each cycle. By looping over each fold and combining, a total of 60 datasets were compiled, where each dataset consists of five input parameters (MLSS, SOUR, DSVI, PSD, and B\_Car) and one output parameter (TMP). Hence, it is 360 data points in total.

The L1R model was implemented with an alpha value of 1, ensuring pure Lasso regression. This method applied L1 regularization, adding a penalty equal to the absolute value of the coefficients, effectively performing variable selection and enhancing both prediction accuracy and model interpretability. Cross-validation determined the optimal lambda value for regularization strength. For the RFR model, a grid search identified the best hyperparameters, configuring the model with 500 trees (ntree = 500) and setting the number of variables considered at each split (mtry = 2). The SVR model was trained with a cost parameter of 1 and a gamma parameter of 0.1, balancing the trade-off between maximizing the margin and minimizing regression error. These hyperparameters were carefully chosen to optimize the model's performance and generalization. Bootstrapping inherently handled data resampling, so additional cross-validation was unnecessary for the RF model, while 10-fold cross-validation was employed for both the SVR and L1R models.

## 4. Results and discussion

## 4.1. Models performance evaluation

Two model performance measures were used to compare the models developed in this study, including coefficient of determination  $(R^2)$  and root mean squared error (RMSE). In regression analysis,  $R^2$  is a very important index as it provides information about how well data fits into a regression line. In these models,  $R^2$  is used to determine the correlation between predicted and actual target variables from the datasets. There is not a one-size-fits-all benchmark for the  $R^2$  value, as what constitutes a 'good' value can vary depending on the specific problem. Generally, a higher  $R^2$  indicates a stronger correlation between the observed and predicted values, approaching 1 (ranging between 0 and 1). Mean

squared error (MSE) measures the average of the squared differences between predicted and actual values. The squaring of errors ensures that all differences are positive and emphasizes larger errors more than smaller ones. RMSE is derived by taking the square root of MSE. This metric has the same units as the predicted variable (TMP), making the interpretation of the predicted variable more straightforward. However, RMSE's utility in comparing different models can be limited due to variations in system elements and operating conditions.

## *4.1.1. RFR model*

The three models were tuned to optimize performance while minimizing the risk of overfitting. The resulting performance metrics for each model and stage are shown in Table 5. The best-performing algorithm was the random forest with the highest *R*2 and lowest RMSE. The RFR model, as shown in Fig. 4, shows excellent performance on the training set with an *R*2 of 0.95 and a low RMSE of 1.75, indicating that it explains 95 % of the variance with high accuracy. For the testing set, the model maintains a strong predictive capability, with an *R*2 of 0.86, showing 86 % of the variance explained. The RMSE values of 3.3 for testing set, though higher than the training set, suggest reasonable performance on unseen data with slight overfitting. To capture both the uncertainty in the model's parameters and the inherent variability in the data, Fig. 4 uses prediction intervals, which provide a statistical range estimating where future TMP values are likely to lie with 80 % confidence.

[Fig. 5](#page-7-0) presents partial dependence plots (PDPs) illustrating the pairwise interactions between important predictors of TMP as identified by the RFR model. Each plot visualizes the model-predicted TMP values as a function of two input variables, using a standardized grayscale color map (black for low TMP and white for high TMP). These plots highlight nonlinear relationships and interaction effects that contribute to membrane performance and are essential for interpreting the model's behavior in an operational context.

The PDPs reveal several patterns aligned with MBR operational theory. For example, B\_Car, which represents carbonaceous extracellular polymeric substances (EPS), shows a strong positive association with TMP. As B\_Car increases from approximately 24 to 32 mg/L, TMP values rise steadily from around 13.2 to over 18.8 kPa, indicating increased fouling potential due to EPS accumulation on membrane surfaces. This finding reflects well-established knowledge that EPS contributes significantly to membrane clogging and resistance. Similarly, DSVI—an indicator of sludge settleability—shows a monotonic increase in TMP beyond a threshold of approximately 68–70 mL/g. As DSVI values exceed this range, TMP rises sharply, consistent with the notion that poorly settling sludge leads to higher concentrations of suspended solids in the reactor, exacerbating membrane fouling.

MLSS and PSD exhibited interactions in the PDP heatmaps. Higher MLSS generally leads to elevated TMP, a relationship well-understood in MBR operations due to the increased solids loading. Changes in PSD, particularly the shift toward finer particles, were also associated with higher TMP values, likely due to their greater propensity to penetrate and block membrane pores. SOUR, a measure of microbial activity, showed a more complex relationship. TMP remained relatively stable across moderate SOUR values but rose at higher SOUR levels, possibly due to increased biological by-product formation, which can elevate EPS

**Table 5**  Models performance comparison metrics for each algorithm.

| Model       | R2   | RMSE | Top predictors |
|-------------|------|------|----------------|
| RFR (Train) | 0.95 | 1.75 | B_Car, DSVI    |
| RFR (Test)  | 0.83 | 3.3  | –              |
| SVR (Train) | 0.87 | 2.93 | B_Car, DSVI    |
| SVR (Test)  | 0.74 | 4.49 | –              |
| L1R (Train) | 0.81 | 3.59 | B_Car, MLSS    |
| L1R (Test)  | 0.69 | 4.75 | –              |

![](_page_6_Figure_10.jpeg)

**Fig. 4.** Actual vs. TMP with 80 % Prediction Intervals. This scatter plot compares actual and predicted TMP values (kPa) from a Random Forest model for training (blue circles) and testing (green triangles) datasets. The dashed line indicates perfect prediction (y = x). Error bars represent 80 % prediction intervals based on tree-level variability.

concentrations and biofouling risk.

These insights underscore the operational relevance of the machine learning models. Variables such as MLSS and DSVI are actively controlled in full-scale MBRs through sludge retention time, aeration control, and sludge wasting. By quantifying their individual and joint impacts on TMP, the PDPs provide a decision-support framework for optimizing MBR operations. The ability to interpret model behavior in terms of established process mechanisms enhances the trustworthiness and applicability of these models in practical settings. This integration of interpretable machine learning with domain-specific understanding represents a novel contribution to predictive modeling in membrane treatment systems.

# *4.1.2. SVR model*

The SVR model illustrated in [Fig. 6](#page-7-0), demonstrates strong performance in the training set, with an *R*2 of 0.87 and an RMSE of 2.93, indicating that it explains 87 % of the variance with good accuracy. The validation set shows a lower *R*2 of 0.71 and a higher RMSE of 4.85, suggesting some overfitting. The testing set has an *R*2 of 0.74 and a relatively high RMSE of 4.49, indicating decent generalization but also reflecting variability and reduced predictive power on unseen data compared to the RFR model. Overall, the model performs well in the training phase, but there is room for improvement in generalization, as indicated by the higher RMSE values in the validation and testing sets.

# *4.1.3. L1R model*

[Fig. 7](#page-7-0) presents the actual versus predicted TMP values for the training, validation, and testing sets using L1R. In the training set, the model explains 81 % of the variance in TMP values (*R*2 = 0.81), with an RMSE of 3.59, indicating a good fit. The validation set shows an even better performance, with an *R*2 of 0.84, demonstrating that the model captures 84 % of the variance. Additionally, the RMSE of 3.27 suggests strong generalization. In the testing set, the model explains 69 % of the variance (*R*2 = 0.69), indicating decent performance. The higher RMSE on the testing set suggests slightly greater variability in the data. The model performs well on the training and validation sets, as indicated by high *R*2 values (0.81 and 0.84, respectively) and reasonably low RMSE values. The performance on the testing set, with an *R*2 of 0.69, still demonstrates that the model generalizes well.

<span id="page-7-0"></span>![](_page_7_Figure_2.jpeg)

**Fig. 5.** Pairwise partial dependence plots of TMP across top predictors.

![](_page_7_Figure_4.jpeg)

**Fig. 6.** Actual vs. TMP with 80 % Prediction Intervals. This scatter plot compares actual and predicted TMP values (kPa) from a SVR model, trained on a membrane bioreactor dataset. Training data (blue circles) and testing data (green triangles) are shown with a dashed line indicating perfect prediction (y = x). Error bars represent 80 % prediction intervals estimated via bootstrapping (100 iterations).

# *4.2. Feature importance rank comparison for the three models*

[Fig. 8](#page-8-0) illustrates the importance rank of features in the RFR, SVR, and L1R models used for predicting TMP. For RFR, the x-axis represents the increase in MSE expressed as a percentage, which indicates how much the prediction error increases when a particular feature is randomly

![](_page_7_Figure_8.jpeg)

**Fig. 7.** Actual versus predicted TMP plot for L1R model. This scatter plot compares actual and predicted TMP values (kPa) from an L1R model applied to a membrane bioreactor dataset. Training data (blue circles) and testing data (green triangles) are shown with a dashed line indicating perfect prediction (y = x). Error bars represent 80 % prediction intervals estimated via bootstrapping (100 iterations).

permuted. Features with higher values have a greater impact on the model's predictions. The input variable B\_Car shows the highest importance, with an increase in MSE close to 60 %, implying that B\_Car is the most influential factor in predicting TMP. The model relies heavily on this variable, and its perturbation significantly degrades model's accuracy. DSVI is the second most important feature, with an increase in

<span id="page-8-0"></span>![](_page_8_Figure_2.jpeg)

**Fig. 8.** Feature importance comparison in RFR, L1R, and SVR models.

MSE of around 50 %, indicating a strong influence on TMP predictions, although slightly less critical than *BCar*, closely followed by MLSS (MSE increase of 45 %). While SOUR shows an increase in MSE of around 42 %, suggesting that biological activity, as measured by SOUR, plays a significant role in TMP prediction. It likely correlates with membrane fouling and system efficiency. The least important among the five features is PSD, with an increase in MSE (35 %), but it still contributes to the model's predictions and affects the TMP, indicating its relevance to the particle characteristics in the sludge.

The feature importance for the SVR model reveals that B\_Car is the most influential predictor with an importance coefficient of approximately 0.7, followed by DSVI with a coefficient close to 0.6, indicating its substantial role. With coefficients around 0.55 and 0.5 respectively, MLSS and PSD also contribute significantly. While SOUR has the lowest importance at about 0.45, it still impacts the model's predictions.

The feature importance of the L1R model is shown in terms of the coefficients of the predictors. The coefficients represent the importance of each feature in predicting the target variable i.e., TMP. The magnitude of the coefficients indicates the strength and direction of the relationship between the predictor and the response variable. Positive coefficients indicate that as the predictor increases, the response variable (TMP) also increases. A negative coefficient indicates that as the predictor increases, the response variable decreases. A zero coefficient indicates that the predictor is not contributing to the model, effectively being excluded from it. Predictor B\_Car got the highest, approximately 1.8, being the most significant predictor in the model, followed by MLSS (1.7), DSVI (0.6) and SOUR (0.3), with the latter two being less significant. The input variable PSD showed a zero coefficient (not shown in the plot) and has been excluded from the model. This indicates that PSD does not significantly contribute to predicting TMP in the presence of other predictors.

## *4.3. Models bias and extreme values detection*

To further analyze model performance, error distribution, and bias detection, the most extreme values (maximum and minimum TMP) in the observed testing and training datasets were investigated. Table 6 presents a summary of the statistical measures associated with the predictions of these extreme maximum and minimum observed values.

The mean prediction values from the RFR model were generally closest to the actual minimum or maximum observed TMP values, indicating superior accuracy in most cases. For the RFR training dataset, the observed minimum and maximum TMP values were 2.57 and 30 kPa, 5.35 and 29.54 kPa for the testing dataset, respectively. The average predictions for the observed minimum value are 2.51kPa, 5.35kPa for SVR and 2.59kPa and 4.73kPa for L1R training and testing dataset, respectively. The average predictions for the observed maximum value are 30kPa, 29.98kPa for SVR and 29.94kPa and 30kPa

**Table 6**  Extreme values prediction.

| Model              | Actual TMP (kPa) | Predicted TMP (kPa) |
|--------------------|------------------|---------------------|
| RFR (Train) – High | 30               | 27.08               |
| RFR (Train) – Low  | 2.57             | 3.86                |
| RFR (Test) – High  | 29.54            | 27.52               |
| RFR (Test) – Low   | 5.35             | 7.58                |
| SVR (Train) – High | 30               | 26.50               |
| SVR (Train) – Low  | 2.51             | 3.38                |
| SVR (Test) – High  | 29.98            | 26.13               |
| SVR (Test) – Low   | 5.35             | 7.10                |
| L1R (Train) – High | 29.94            | 26.70               |
| L1R (Train) – Low  | 2.59             | 3.32                |
| L1R (Test) – High  | 30               | 29.23               |
| L1R (Test) – Low   | 4.73             | 6.54                |
|                    |                  |                     |

for L1R for training and test datasets, respectively. Both RFR and L1R models predicted the high values more accurately, while SVR tends to make more conservative predictions for extreme values.

The models developed in this study, based on a bench-scale MBR treating textile wastewater, exhibited performance comparable to existing empirical, semi-empirical, and machine learning models for TMP prediction reported in the literature, as shown in Table 7. While the literature often utilizes pilot-scale MBRs and larger datasets, our study leveraged a dataset that included both significant and previously overlooked input variables. Despite this advantage, the SVR and L1R models demonstrated slightly lower accuracies compared to the RFR model. This discrepancy may be attributed to the inherent feature selection capability of RF, which can inherently manage many variables and identify the most important features without introducing bias. Additionally, differences in the importance of model input variables, model structure, and dataset size also contributed to the observed performance variations.

## **5. Discussion on the effect of significant sludge parameters on TMP**

Bound EPS which is rich in carbohydrates, significantly impacted fouling by increasing sludge viscosity and cake layer density. This helps to understand why B\_Car becomes the top influential sludge parameter towards the TMP prediction. DVSI, which reflects sludge settleability, decreased due to larger floc formation with PAC addition. Lower DSVI indicated better dewaterability and reduced fouling, resulting in a less compressible cake layer and lower TMP. SOUR measured at 70 mg O2/ gVSS/h, indicated lower microbial activity in anoxic conditions, correlating with less biomass production and slower fouling rates.

PSD varied due to hydrodynamic and biological conditions in the reactor. Under controlled aeration and PAC addition, larger particles formed, though shear stresses from Kaldnes® media caused a slight reduction in size [\[11](#page-10-0)**]**. Larger particles created a porous but thicker cake layer on the membrane, increasing TMP due to higher hydraulic resistance, while smaller particles clogged pores. This suggests an optimal PSD range that minimizes TMP, as both too small and too large particles lead to higher fouling. However, PAC's interaction with flocs reduced fouling by forming BAC, which provided more adsorptive area. High MLSS levels increased viscosity and cake layer resistance, leading to higher TMP, though moderate concentrations were more manageable

**Table 7**  TMP models performance metrics from the literature.

| Model                           | Performance                                           | Remarks                                                                                                                                               | Reference |
|---------------------------------|-------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| RF, ANN,<br>LSTM                | R2 = 0.88, 0.93,<br>0.96<br>0.99, 0.92,<br>0.97, 0.91 | 80,000 samples, Full scale<br>municipal WWTP                                                                                                          | [12]      |
| Model<br>Tree                   | RMSE= 1.93–2<br>kPa                                   | Dataset of 462 days                                                                                                                                   | [36]      |
| ANN                             | R2 = 0.72                                             | Dataset of 938 observations,<br>PVDF membrane of pore size<br>= 0.1 µm                                                                                | [37]      |
| ANN                             | R2 = 0.97                                             | Lab scale AO-MBR operated for<br>180 days, 10 input parameters<br>used                                                                                | [25]      |
| ANN                             | R2 = 0.99                                             | MBR operation spanning 125<br>days, EPS (Protein in biofilm<br>layer) as the dominant fouling<br>factor, MLSS, the most sensitive<br>parameter on TMP | [23]      |
| ANN,<br>NARX<br>ANFIS           | R2 = 0.99                                             | Pilot scale SMBR (20 L), SMBR<br>operated for less than 1 hr                                                                                          | [38]      |
| MLP,<br>ANN-GA,<br>RBFANN<br>GA | R2 = 0.99                                             | Pilot scale SMBR, 60 days<br>operation with varying hydraulic<br>retention time                                                                       | [39]      |

for optimal membrane operation. A slightly elevated MLSS increased fouling rates, emphasizing the need for balanced sludge concentrations to maintain MBR efficiency.

The study's findings highlight the critical role of monitoring and controlling sludge parameters to maintain optimal TMP levels in MBR systems. A clear understanding of the relationship between TMP and key sludge variables enables operators to predict the need for interventions, helping to prevent excessive membrane fouling and ensuring efficient system operation. The observed increase in these variables leads to a proportional rise in TMP, suggesting that the membrane system is highly sensitive to changes in sludge characteristics, which can directly affect both performance and maintenance demands. However, further research is necessary to explore the full range of sludge parameters and their correlation with TMP, considering the impact of varying hydrodynamic and operating conditions over time, and expand the applicability of the model prediction in this study. Based on these insights, practical steps can be taken to mitigate TMP spikes, such as adjusting solid retention time, optimizing aeration rates, and implementing prefiltration methods. Regular monitoring of sludge parameters should also be employed as an effective strategy for managing TMP in MBR systems.

## **6. Conclusions**

Machine learning regression models were developed in this study, employing RFR, SVR, and L1R algorithms to predict TMP and characterize membrane fouling throughout various stages of the MBR production cycle. These models utilized operation data spanning 60 days from a bench-scale MBR treating textile wastewater. Following the selection of input variables, the models effectively predicted TMP for RFR, SVR, and L1R, demonstrating good predictive accuracy. The analysis of model uncertainties offered valuable insights into both hyper-parameter and model structure uncertainties, particularly concerning extreme TMP predictions. The RFR model outperformed both SVR and L1R models in terms of statistical metrics such as *R*2 and RMSE. Specifically, the RFR model achieved *R*2 values of 0.95, whereas SVR attained 0.87, and L1R gained a value of 0.81. This indicates that the RFR model was the most consistent and reliable within the tested hyperparameter ranges. Rich carbohydrates-bound EPS was observed as the most influential sludge parameter towards membrane fouling, while PSD was the least. While the current study demonstrates machine learning's potential for TMP prediction in bench-scale MBRs, we recognize the need to validate these models under industrial conditions and better articulate their operational value. The study emphasizes that the identified key predictors can inform several practical interventions at full-scale plants. For instance, real-time monitoring of these parameters could trigger early cleaning cycles when approaching critical TMP thresholds, potentially reducing energy consumption by through optimized cleaning schedules. Similarly, the strong correlation between B\_Car and fouling rates suggests that operators might adjust sludge retention times to manage EPS production. Although full-scale testing is beyond our present scope, we are actively pursuing collaborations with wastewater treatment facilities to: (1) validate these operational hypotheses, (2) expand our dataset to include diverse wastewater compositions and long-term fouling trends under varying process conditions, and (3) develop temporal forecasting models that integrate plant-specific operational data (e.g., flux rates, cleaning protocols) to enable proactive fouling control. A key next step will be benchmarking our ML predictions against conventional models and operator heuristics to identify hybrid modeling opportunities that combine data-driven insights with process knowledge. These efforts will specifically address the transition from lab-scale findings to real-world applicability by quantifying the actual energy and cost savings achievable through ML-guided operations.

#### <span id="page-10-0"></span>CRediT authorship contribution statement

Onaira Zahoor: Software, Methodology, Formal analysis, Investigation, Writing – original draft. Sher Jamal Khan: Funding acquisition, Supervision, Writing – review & editing. Muhammad Usama: Writing – review & editing. Henry J. Tanudjaja: Writing – review & editing. Noreddine Ghaffour: Writing – review & editing. Muhammad Saqib Nawaz: Writing – review & editing.

### **Declaration of Competing Interest**

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

#### Acknowledgments

The authors would like to acknowledge the technical support provided for this study by the laboratory staff at the National University of Science and Technology (NUST), Islamabad.

#### Data availability

Data will be made available on request.

#### References

- Haider A, Khan SJ, Nawaz MS, Saleem MU. Effect of intermittent operation of labscale upflow anaerobic sludge blanket (UASB) reactor on textile wastewater treatment. Desalin Water Treat 2018;136:120–30. https://doi.org/10.5004/ dwt.2018.23231
- [2] Nawaz MS, Khan SJ. Effect of HRT on SBR performance for treatability of combined domestic and textile wastewaters. J Chem Soc Pak 2013;35(2):527–32.
- [3] Khalid MZ, Jamil A, Nawaz MS, Ghaffour N. Assessment of wastewater quality of Paharang drain and its impact on the ground water quality of adjacent areas. Int J Econ Environ Geol 2021;11(4):6–13.
- [4] Yasmeen M, Nawaz MS, Manzoor K, Khan SJ, Ghaffour N. Evaluating dye recovery and reusability potential from dyebath effluent using forward osmosis membranes for minimum liquid discharge. Chemosphere Oct 2023;338:139433. https://doi. org/10.1016/j.chemosphere.2023.139433.
- [5] Malik SM, Nawaz MS, Ali M, Manzoor K, Khan SJ, Ghaffour N. Treatment of highstrength synthetic textile wastewater through anaerobic osmotic membrane bioreactor and effect of sludge characteristics on flux. Environ Qual Manag 2021; 31(1):85–98. https://doi.org/10.1002/tqem.21756.
- [6] Ayub M, Saeed N, Chung S, Nawaz MS, Ghaffour N. Physical and economical evaluation of laboratory-scale membrane bioreactor by long-term relative costbenefit analysis (in English) J Water Reuse Desalin Sep 2020;10(3):239–50. https://doi.org/10.2166/wrd.2020.023.
- [7] Sohail N, Ahmed S, Chung S, Nawaz MS. Performance comparison of three different reactors (MBBR, MBR and MBBMR) for municipal wastewater treatment (in English) Desalin Water Treat Jan 2020;174:71–8. https://doi.org/10.5004/ dwt.2020.24866.
- [8] Campo R, Capodici M, Di Bella G, Torregrossa M. The role of EPS in the foaming and fouling for a MBR operated in intermittent aeration conditions. Biochem Eng J 2017;118:41–52.
- [9] Goh P, Lau W, Othman M, Ismail A. Membrane fouling in desalination and its mitigation strategies. Desalination 2018;425:130–55.
- [10] Siddique MS, Khan SJ, Shahzad MA, Nawaz MS, Hankins NP. Insight into the effect of organic and inorganic draw solutes on the flux stability and sludge characteristics in the osmotic membrane bioreactor. Bioresour Technol Feb 2018; 249:758–66. https://doi.org/10.1016/j.biortech.2017.10.064.
- [11] Nawaz MS, Parveen F, Khan SJ, Hankins NP. Impact of osmotic backwashing, particle size distribution and feed-side cross-flow velocity on flux in the forward osmosis membrane bioreactor (FO-MBR). J Water Process Eng Oct 2019;31: 100861. ARTN 10086110.1016/j.jwpe.2019.100861.
- [12] Kovacs DJ, et al. Membrane fouling prediction and uncertainty analysis using machine learning: A wastewater treatment plant case study. J Membr Sci 2022; 660:120817.

- [13] Wu X-L, Han H-G, Zhang H-J, Qiao J-F. Intelligent warning of membrane fouling based on robust deep neural network. Int J Fuzzy Syst 2022:1–18.
- [14] Horseman T, Yin Y, Christie KS, Wang Z, Tong T, Lin S. Wetting, scaling, and fouling in membrane distillation: state-of-the-art insights on fundamental mechanisms and mitigation strategies. ACS EST Eng 2020;1(1):117–40.
- [15] Zuthi MFR, et al. New and practical mathematical model of membrane fouling in an aerobic submerged membrane bioreactor. Bioresour Technol 2017;238:86–94 [Online]. Available: https://www.sciencedirect.com/science/article/pii/ S096085241730487X?via%3Dihub.
- [16] Hermia J. Blocking filtration. Application to non-Newtonian fluids. Mathematical models and design methods in solid-liquid separation. Springer; 1985. p. 83–9.
- [17] Pizzichetti ARP, Pablos C, Álvarez-Fernández C, Reynolds K, Stanley S, Marugán J. Kinetic and mechanistic analysis of membrane fouling in microplastics removal from water by dead-end microfiltration. J Environ Chem Eng 2023;11(2):109338.
- [18] Ludwig T, et al. An advanced simulation model for membrane bioreactors: development, calibration and validation. Water Sci Technol 2012;66(7):1384–91 [Online]. Available: https://iwaponline.com/wst/article-abstract/66/7/1384/ 16716/An-advanced-simulation-model-for-membrane?redirectedFrom=fulltext.
- [19] Huang H, Young TA, Jacangelo JG. Unified membrane fouling index for low pressure membrane filtration of natural waters: principles and methodology. Environ Sci Technol 2008:42(3):714–20
- [20] Solle D, et al. Between the poles of data-driven and mechanistic modeling for process operation. Chem Ing Tech 2017;89(5):542–61.
- [21] Abuwatfa WH, AlSawaftah N, Darwish N, Pitt WG, Husseini GA. A review on membrane fouling prediction using artificial neural networks (ANNs). Membranes 2023;13(7):685 [Online]. Available: https://pmc.ncbi.nlm.nih.gov/articles/ PMC10383311/pdf/membranes-13-00685.pdf.
- [22] Niu C, Li X, Dai R, Wang Z. Artificial intelligence-incorporated membrane fouling prediction for membrane-based processes in the past 20 years: a critical review. Water Res 2022;216:118299 [Online]. Available: https://www.sciencedirect.com/ science/article/pii/S0043135422002627?via%3Dihub.
- [23] Hazrati H, Moghaddam AH, Rostamizadeh M. The influence of hydraulic retention time on cake layer specifications in the membrane bioreactor: experimental and artificial neural network modeling. J Environ Chem Eng 2017;5(3):3005–13.
- [24] Li W, Li C, Wang T. Application of machine learning algorithms in MBR simulation under big data platform. Water Pract Technol 2020;15(4):1238–47.
- [25] Schmitt F, Banu R, Yeom I-T, Do K-U. Development of artificial neural networks to predict membrane fouling in an anoxic-aerobic membrane bioreactor treating domestic wastewater. Biochem Eng J 2018;133:47–58.
- [26] Pollice A, Giordano C, Laera G, Saturno D, Mininni G. Physical characteristics of the sludge in a complete retention membrane bioreactor. Water Res 2007;41(8): 1832–40. (https://www.sciencedirect.com/science/article/pii/S0043135 4070003957via%3Dihub) ([Online]. Available).
- [27] Frølund B, Palmgren R, Keiding K, Nielsen PH. Extraction of extracellular polymers from activated sludge using a cation exchange resin. Water Res 1996;30(8): 1740-58
- [28] DuBois M, Gilles KA, Hamilton JK, Rebers P t, Smith F. Colorimetric method for determination of sugars and related substances. Anal Chem 1956;28(3):350–6.
- [29] Lowry OH, Rosebrough NJ, Farr AL, Randall RJ. Protein measurement with the Folin phenol reagent. J Biol Chem 1951;193(1):265–75. (https://www.sciencedirect.com/science/article/pii/S0021925819524516?via%3Dihub) ([Online]. Available).
- [30] APHA, Standard methods for the examination of water and wastewater, 23 ed. American Public Health Association 2017.
- [31] Lee S-B, Habetler TG, Harley RG, Gritter DJ. An evaluation of model-based stator resistance estimation for induction motor stator winding temperature monitoring. IEEE Trans Energy Convers 2002;17(1):7–15.
- [32] Garson GD. Fundamentals of hierarchical linear and multilevel modeling. Hierarchical Linear Model: Guide Appl 2013:3–25.
- [33] B.G. Tabachnick, L.S. Fidell, and J.B. Ullman, *Using multivariate statistics*. pearson Boston, MA, 2013.
- [34] Cortes C. Support-Vector Networks. Mach Learn 1995.
- [35] Cohen J. Statistical power analysis for the behavioral sciences. routledge; 2013.
- [36] Dalmau M, Atanasova N, Gabarrón S, Rodriguez-Roda I, Comas J. Comparison of a deterministic and a data driven model to describe MBR fouling. Chem Eng J 2015; 260:300-8
- [37] Liu Q-F, Kim S-H, Lee S. Prediction of microfiltration membrane fouling using artificial neural network models. 2009/11/19/ Sep Purif Technol 2009;70(1): 96–102. https://doi.org/10.1016/j.seppur.2009.08.017.
- [38] Yusuf Z, Wahab NA, Sahlan S. Modeling of submerged membrane bioreactor filtration process using NARX-ANFIS model. 31 May-3 June 2015 2015 10th Asian Control Conf (ASCC) 2015:1–6. https://doi.org/10.1109/ASCC.2015.7244710.
- [39] Mirbagheri SA, Bagheri M, Bagheri Z, Kamarkhani AM. Evaluation and prediction of membrane fouling in a submerged membrane bioreactor with simultaneous upward and downward aeration using artificial neural network-genetic algorithm. 2015/07/01/ Process Saf Environ 2015;96:111–24. https://doi.org/10.1016/j. psep.2015.03.015.
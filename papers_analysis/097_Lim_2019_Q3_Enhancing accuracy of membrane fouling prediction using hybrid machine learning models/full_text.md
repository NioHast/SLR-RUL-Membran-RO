doi: 10.5004/dwt.2019.23444

146 (2019) 22–28 April

# Enhancing accuracy of membrane fouling prediction using hybrid machine learning models

Seung Ji Lima , Young Mi Kimb,\*, Hosik Parkb , Seojin Kic , Kwanho Jeongd, Jangwon Seoe , Sung Ho Chaea , Joon Ha Kima,b

*a School of Earth Sciences and Environmental Engineering, Gwangju Institute of Science and Technology (GIST), Gwangju 61005, Korea b Membrane Research Center, Korea Research Institute of Chemical Technology(KRICT), Daejeon 34114, Korea, Tel. +82 42 860 7527; email: youngmi@krict.re.kr (Y.M. Kim)*

*Department of Environmental Engineering, Gyeongnam National University of Science and Technology, 33 Dongjin-ro, Jinju-si, Gyeongsangnam-do 52725, Korea*

*d Singapore Membrane Technology Centre, Nanyang Environment and Water Research Institute, Nanyang Technological University, Singapore 637141, Singapore*

*e Research Institute for Solar and Sustainable Energies, Gwangju Institute of Science and Technology, Gwangju 61005, Korea*

Received 10 September 2018; Accepted 8 December 2018

# **abstract**

Membrane fouling significantly affects membrane performance, but cleaning and replacement schedules are often set at regular time intervals, regardless of the extent of deterioration in performance. The aim of this study is to develop an improved prediction model for membrane fouling in the seawater reverse osmosis (SWRO) process using a hybrid machine learning approach. A Kalman filter (KF) was combined with either an artificial neural network (ANN) or a support vector machine (SVM)—a family of machine learning models—in series. The performance of these integrated models was evaluated with training and testing data sets compiled from the Fujairah SWRO plant over a period of 18 months. Our findings showed that the SVM alone provided, on average, slightly better prediction of membrane resistance (an indirect indicator of membrane fouling) than a single ANN during training and testing sets. However, hybrid machine learning methods consistently outperformed any single model, with the combination of the KF and SVM exhibiting better performance than that of the KF and ANN, except for one special case in which the accuracy of a single SVM already exceeded 0.8 for both Nash–Sutcliffe model efficiency and *R*<sup>2</sup> . Taken together, our results demonstrated that the hybrid machine learning approach not only enhanced the prediction ability of membrane resistance in classical fouling and machine learning models, but could also be used to adjust cleaning and replacement schedules correctly in response to progressive deterioration in membrane performance during operation.

*Keywords:* Hybrid model; Reverse osmosis; Kalman filter; Artificial neural network; Support vector machine; Membrane maintenance

### **1. Introduction**

While freshwater demand is increasing due to climate change, population growth, and industrialization, it is hard to meet the increased needs using limited conventional water resources such as rivers, lakes, and groundwater. Seawater, as an alternative water resource, provides an opportunity to solve such an imbalance between water demand and supply [1]. Out of available desalination technologies, reverse osmosis (RO) is widely adopted for producing freshwater [2], applying high pressure to a semipermeable RO membrane to purify seawater. The high-pressure pump employed in RO systems, in general, consumes a large portion of the energy

This article was originally published with errors on page 23. This version has been updated. Please see Corrigendum in vol. 270(2022) 320 [doi: 10.5004/dwt.2022.29011].

<sup>\*</sup> Corresponding author.

required in the process [3]. Accordingly, a lot of research efforts have been devoted to reduce energy consumption, including the influence of membrane performance on energy reduction [4,5], efficiency and types of energy recovery devices [3,6], and membrane fouling control strategies [7].

One of the most important elements in reducing energy consumption is fouling control. When foulants are deposited in the membrane, operating pressures must be increased to meet the designed permeate flow, which leads to an increase in energy consumption. Appropriate membrane cleaning and replacement are needed to avoid or reduce the extent of membrane fouling, thereby decreasing energy consumption required in the RO process. Prediction of membrane fouling on time, therefore, plays an important role in not only improving performance of the RO membrane, but also reducing irrelevant membrane cleaning and replacement schedules performed regularly during the operation.

Either index-based approach or numerical simulation is adopted for predicting membrane fouling. The index-based approach refers to generating an indicator that corresponds to the scaling and fouling potential of feedwater from steady state operating data in a small test plant. The Langelier Saturation Index (LSI) was developed to analyze the degree of scaling, and the Stiff and Davis Saturation Index value was proposed as a modification of the LSI [8]. The silt density index and modified fouling index (MFI) are used to predict the degree of colloidal fouling potential [9], and index values such as the MFI-ultrafiltration and the crossflow samplermodified foul-ing index have been developed to overcome the limitations of earlier methods [10,11]. However, because these indices were developed from steady state conditions, such indices had a limitation in assessing the progress deterioration of membrane fouling observed during the operation [12].

In contrast, numerical simulation adopted transport theory and statistical equations in predicting membrane fouling at discrete and continuous time intervals. The resistance-in-series model assesses membrane fouling as a resistance to solution passage; the model works with a solution–diffusion model to simulate the effect of membrane fouling in the RO process [13,14]. As a statistical approach, the nonlinear recursive least squares method has been employed to estimate membrane resistance and the friction coefficient in the RO process [15]. Machine learning algorithms have also been used to develop advanced membrane fouling

prediction models. Out of them, artificial neural networks (ANN) were frequently adopted in predicting membrane fouling in various types of water treatment processes [16–18].

The objective of this study is to present a prediction method for membrane fouling in the RO process. In this study, a Kalman filter (KF) is employed to reduce noise in the operating data. Two machine learning models—an ANN and a support vector machine (SVM)—are used to construct models based on operational data. A KF and the machine learning models are then combined in series as a hybrid model. Fujairah desalination operational data is used to test the prediction performance of the single and hybrid machine learning models. The specific objectives of this study are (1) to propose a noise reduction method as a data pre-processing step for machine learning algorithms, (2) to compare the prediction performance of single and hybrid machine learning models based on simulation results, and (3) to suggest prediction accuracy enhancement methods for membrane fouling. We hope the proposed methodology will be used to determine or adjust appropriate cleaning and replacement times for RO membranes during the operation.

# **2. Materials and methods**

# *2.1. Operational data in real plant*

Table 1 presents the operational data at the feed, permeate, and brine sides from the Fujairah seawater reverse osmosis (SWRO) plant, obtained during an 18-month monitoring period from January 2005 to June 2006. As shown in the table, the Fujairah SWRO plant was found to receive feedwater with fluctuating temperatures (23°C–36°C) and total dissolved solid (TDS) concentrations (35,000–40,000 mg/L). However, feed pressure at the SWRO plant was almost always in the constant pressure mode, while its recovery rate was steadily maintained at around 43%. The SWRO plant also produced the intended permeated water quality, although the TDS concentration fluctuated significantly between 339 and 978 mg/L. This operational data was used as input to both classical fouling and machine learning models, in addition to the KF algorithm, described in detail in the following three sections. It is noted that the operational data of Fujairah plant was previously used to simulate the longterm fouling model for the reverse osmosis process [14] and to estimate membrane fouling in the reverse osmosis process [15].

Table 1 Summary statistics of observed data during operation of the Fujairah SWRO plant over 18 months

| Side     | Parameters                       | N   | Range         | Mean   |
|----------|----------------------------------|-----|---------------|--------|
| Feed     | Temperature (Tf<br>), °C         | 522 | 23–36         | 29     |
|          | Pressure (Pf<br>), bar           | 522 | 66–68         | 67     |
|          | Flow rate (Qf<br>), m3<br>/h     | 522 | 1,052–1,117   | 1,066  |
|          | TDS concentration (Cf<br>), mg/L | 522 | 34,920–39,538 | 36,985 |
| Permeate | Pressure (Pp<br>), bar           | 522 | 4–13          | 8      |
|          | Flow rate (Qp<br>), m3<br>/h     | 522 | 452–480       | 458    |
|          | Recovery, %                      | 522 | 43–44         | 43     |
|          | TDS concentration (Cp<br>), mg/L | 522 | 339–978       | 474    |
| Brine    | Pressure (Pb<br>), bar           | 522 | 63–66         | 64     |
|          | ), m3<br>Flow rate (Qb<br>/h     | 522 | 600–637       | 608    |

### 2.2. Membrane fouling and resistance

We used membrane resistance to indicate the extent of fouling occurring along the membrane surface. This is because the accumulation of membrane foulants over time results in an increase in membrane resistance. Membrane resistance was calculated in two ways—both with and without the properties of the membrane materials. The first method was adopted to explain how membrane resistance changed in response to progressive fouling of the membrane. Total membrane resistance  $R_{\text{tot,m}}(t)$  can be expressed as follows:

$$R_{\text{tot},m}(t) = R_m + R_a(t) \tag{1}$$

where  $R_m$  and  $R_a$  indicate the intrinsic and variable membrane resistances (fluctuating with the degree of membrane fouling), respectively.  $R_a$  is estimated by the following equation [13]:

$$R_a(t) = k_{fp} \int_0^t v(\tau) d\tau \tag{2}$$

where  $k_{\rm fp}$  is the fouling potential of feedwater, which is dependent on raw water quality.  $\tau$  is used as a dummy variable for integration. Note that  $k_{\rm fp}$ , which is calculated using the Fujairah plant operational data, is a fixed constant value during the simulation.

The second method stems from membrane transport theory. The equation for membrane resistance was originally developed to calculate permeate flow rate in the membrane. Total membrane resistance  $R_{\rm tot}(t)$  is determined by the following equation:

$$R_{\text{tot}}(t) = \frac{\Delta p(t) - \Delta \pi(t)}{v(t)} \tag{3}$$

where  $\Delta p(t)$  and  $\Delta \pi(t)$  are transmembrane pressure and osmotic pressure differences, respectively, at time t. v(t) indicates permeate flow rate at time t in the RO process [13]. Note that the simple term membrane resistance is used, instead of total membrane resistance, for the remainder of this paper.

### 2.3. Prediction algorithm for membrane resistance

# 2.3.1. KF algorithm

The KF algorithm is a recursive data processing method for a linear system with noise [19,20], consisting of two steps. The first step is prediction of data using mathematical equations in time variance form; prediction results are used to update the measurement. The second step is correction of data; at this step, weights for sensor data and prediction results are calculated based on statistical theory, and the weightings are then applied to each term to estimate data by reducing noise. These sequential calculations are conducted at every time point, making the KF algorithm a recursive process. Membrane resistance was set as a system variable to be estimated using the KF algorithm,

but using  $x_t$  in place of  $R_t$  to distinguish membrane resistance from error covariance of measurement R in this section. The KF estimation procedure uses the following equations [21]:

$$\hat{x}_{t}^{-} = A \hat{x}_{t-1} + B u_{t-1} \tag{4}$$

$$P_{t}^{-} = AP_{t-1}A^{T} + Q {5}$$

$$K_{t} = P_{t}^{-} H^{T} \left( H P_{t}^{-} H^{T} + R \right)^{-1}$$
 (6)

$$\hat{x}_t = \hat{x}_t + K_t(z_t - H\hat{x}_t) \tag{7}$$

$$P_t = P_t^- - K_t H P_t^- \tag{8}$$

where Eqs. (4) and (5) are employed in the prediction step, and Eqs. (6)–(8) are utilized in the correction step. In Eq. (4), the prediction result of the system variable is calculated. In Eq. 7, the system variable is estimated, depending on the weightings for the prediction result and the measurement value  $z_t$ ,  $K_t$  is the Kalman gain at time step t, and H is the parameter expressing the relationship between the observed and calculated data.  $P_t$  is the error covariance, and Q is the error covariance matrix of noise for the process.

### 2.3.2. Artificial neural network

An ANN is a machine learning algorithm, which is widely used to predict time-series data [16,17,19,22]. The prediction process consists of two sequential phases—the training phase and the test phase. In the training phase, weightings that minimize error between the observed and predicted values are calculated by continuous repetition of feedforward and back propagation. Feedforward is a set of calculations establishing a relationship between parameters in the input and output layers. Weightings in each layer are modified in back propagation to reduce the mean squared error (MSE) between the observed and predicted target outputs. Forecast performance for the test data is assessed, and the weightings in the algorithm are adjusted to increase prediction accuracy in the test phase.

In this study, we employed an ANN structure with three layers: an input layer with *D* inputs, a hidden layer with *M* neurons, and an output layer with *K* outputs. The inputs and outputs for the hidden layer have the following mathematical relationship [23]:

$$z_{j} = \varphi \left( \sum_{i=0}^{D} w_{h,ji} \cdot x_{i} + b_{h,j0} \right)$$

$$\tag{9}$$

where  $z_j$  refers to the output from the hidden layer and  $x_i$  refers to the input of the ANN.  $w_{h,ji}$  and  $b_{h,j0}$  are the connection weighting and bias for the hidden layer, respectively.  $\varphi$  represents the activation function of the hidden layer, and the prediction result for the activation function  $\varphi$  is calculated using following equation [23]:

$$y_k(x,w) = \sigma \left( \sum_{j=0}^{M} w_{o,ji} \cdot z_j + b_{o,j0} \right)$$
 (10)

where  $y_k(x, w)$  is the predicted target output corresponding to the input x and weight w for the k-th output. Subscript o in both the connection weighting and bias indicates the output layer. Lastly, the MSE is calculated as follows:

$$E(w) = \frac{1}{N} \sum_{n=1}^{N} ||y(x_n, w) - t_n||^2$$
(11)

where E is the MSE, N is the number of input vectors, and  $t_n$  is the target output value matching to  $x_n$ . Fig. 1(a) shows information about the ANN structure used in this study. Each input layer has 8 inputs (temperature for feed; flow rate for brine and permeate; pressure for feed, brine, and permeate; and concentration for feed and permeate). Each hidden layer has M neurons, as determined by the optimization algorithm, and each output layer has one neuron (membrane resistance).

#### 2.3.3. Support vector machine

An SVM is a supervised learning algorithm used in regression analysis [22,24,25]. The basic idea of an SVM is to find a function, *f*, fitting the following mathematical equation [26]:

$$f(x) = \langle w, x \rangle + b \tag{12}$$

![](_page_3_Figure_9.jpeg)

Fig. 1. Structure of the two different types of machine learning algorithm employed in this study: (a) ANN and (b) SVM (refer Table 1 for more detailed information on input parameters).

where the  $\langle \ \rangle$  operator indicates the dot product. w is determined by solving a convex optimization problem:

minimize 
$$\frac{1}{2} \|w\|^2$$
subject to 
$$\begin{cases} y_i - \langle w, x_i \rangle - b \le \varepsilon \\ \langle w, x_i \rangle + b - y_i \le \varepsilon \end{cases}$$
 (13)

where  $y_i$  is the target output corresponding to input  $x_i$ . Constraints for the optimization problem mean that the difference between  $y_i$  and f is in the range from  $-\varepsilon$  to  $+\varepsilon$ . However, Eq. (12) can only be used in linear regression analysis; this linear model is extended to nonlinear regression analysis by employing the mapping function  $\varphi$  and kernel k. ( $x_i$ ) represents the mapping  $x_i$  from input space to feature space. The weighting for the SVM is changed to the following form:

$$w = \sum_{i=1}^{N} \left( \alpha_i - \alpha_i^* \right) \phi(x_i) \tag{14}$$

where  $\alpha$  is the Lagrange multiplier. An asterisk indicates the difference between above the regression line and below the regression line in the feature space. The generalized form of the equation is created by substituting Eq. (14) into (12) and introducing the kernel  $k(x_i,x) = \langle \phi(x_i), \phi(x) \rangle$ . Either linear or nonlinear regression can be conducted, depending on the kernel function. Fig. 1(b) illustrates the SVM model structure used in this study. Inputs are the parameters given in Table 1. Support vectors and the kernel function form the relationship between the inputs and output.

$$f(x) = \sum_{i=1}^{N} (\alpha_i - \alpha_i^*) k(x_i, x) + b$$
(15)

### 2.3.4. Hybrid algorithm

The term hybrid algorithm indicates a combined algorithm of the KF and one of the machine learning methods [19]. The KF algorithm processes operational data to reduce noise; that data is then used to train and test the machine learning algorithms. Noise contained in sensor data can often affect prediction accuracy; a training algorithm that learns from data with noise as if it were normal data could produce invalid forecast results. The forecast accuracy of the machine leaning algorithms is therefore modified by employing the KF. Note that KF-ANN and KF-SVM are used to indicate hybrid algorithms using the KF—ANN with KF and SVM with KF, respectively.

### 3. Results and discussion

### 3.1. Prediction of membrane resistance from classical methods

Fig. 2 illustrates calculation results for membrane resistance using SWRO plant operational data and the prediction results for membrane resistance using classical forecast methods. The calculated membrane resistance

contains uncertainty from the sensor data. The predicted result of the membrane resistance using the fouling model is based on the equation presented in Section 2.2 and reflects the increasing trend of the operational data. However, actual values are not predictable using the model. Estimation results from the KF show a reduction of noise in the membrane resistance during the monitoring periods. The KF follows the fluctuation of data during the initial 100 d of plant operations; after 300 d of plant operations, membrane cleaning was conducted, and peak error is observed at that time due to misreading of sensors during the membrane-cleaning period.

### *3.2. Prediction of membrane resistance from single machine learning algorithm*

Figs. 3(a) and (b) show a 14-d forecast for membrane resistance using the ANN and SVM, respectively. In the training phase for the ANN, there are two sections where the difference between the predicted value and the actual value is large. The first section is for the initial 50 d; the second is from 150 to 300 d, when the membrane resistance monotonically increases. In the second section, the ANN predicts the membrane resistance as higher than the actual value.

![](_page_4_Figure_5.jpeg)

Fig. 2. Membrane resistance estimated from the KF (solid blue line) and fouling (dotted red line) models during the operation of the Fujairah SWRO plant over 18 months. Observations are indicated by discrete black points.

In the training phase for the SVM, it correctly predicts the actual value and follows the trend of the data. In the test phase, both of the machine learning algorithms are unable to accurately predict actual values. The ANN predicts noise with a more magnified value than from the operational data. The SVM is able to follow the variation of the data; however, it predicts membrane resistance as lower than the actual value. The forecast accuracies in terms of Nash–Sutcliffe model Efficiency (NSE) and coefficient of determination (*R*<sup>2</sup> ) for the single machine learning algorithms are shown in Table 2. The NSE value is 0.45 for the ANN and 0.46 for the SVM. When comparing *R*<sup>2</sup> values, the SVM (*R*<sup>2</sup> = 0.76) is 1.5 times more accurate than the ANN (*R*<sup>2</sup> = 0.5). The prediction accuracy of the test phase is significantly lower than for the training phase.

# *3.3. Prediction of membrane resistance from hybrid machine learning algorithms*

Figs. 4(a) and (b) represent the 14-d forecasts of membrane resistance using KF-ANN and KF-SVM, respectively. Both hybrid algorithms fail to predict

![](_page_4_Figure_10.jpeg)

Fig. 3. 14-d forecast of membrane resistance during the operational period of 522 d obtained from the (a) ANN and (b) SVM.

Table 2 Performance comparison of the ANN and SVM in predicting membrane resistance in terms of the NSE and coefficient of determination (*R*<sup>2</sup> )

| Forecasting level | Forecasting method | NSE      |      | R2       |      |  |
|-------------------|--------------------|----------|------|----------|------|--|
|                   |                    | Training | Test | Training | Test |  |
| 7 d               | ANN                | 0.84     | 0.48 | 0.84     | 0.76 |  |
|                   | SVM                | 0.93     | 0.42 | 0.94     | 0.84 |  |
| 14 d              | ANN                | 0.71     | 0.45 | 0.76     | 0.50 |  |
|                   | SVM                | 0.86     | 0.46 | 0.86     | 0.76 |  |
| 7 d               | KF-ANN             | 0.85     | 0.73 | 0.88     | 0.82 |  |
|                   | KF-SVM             | 0.94     | 0.77 | 0.96     | 0.89 |  |
| 14 d              | KF-ANN             | 0.78     | 0.63 | 0.82     | 0.75 |  |
|                   | KF-SVM             | 0.85     | 0.72 | 0.88     | 0.82 |  |

![](_page_5_Figure_2.jpeg)

Fig. 4. 14-d forecast of membrane resistance during the operational period of 522 d obtained from (a) KF-ANN and (b) KF-SVM. Note that KF-(machine learning algorithm) indicates a hybrid method that combines a Kalman filter and a machine learning algorithm in series.

fluctuations in the initial 50 d of operations. However, the remainder of the data in the training and test phases is predicted well. KF-ANN predicts membrane resistance with a reduced gap between predicted and observed values in the operational period from 150 to 300 d. The effect of the KF on the machine learning algorithm in the 14-d forecast is shown in Fig. 5. From the figure it can be seen that the value of the NSE in the test step increases from 0.4 to 0.6 and 0.7 for KF-ANN and KF-SVM, respectively, by applying KF. The *R*<sup>2</sup> value increases by 0.2, when comparing ANN with KF-ANN. The implementation of the KF also affects prediction accuracy according to changes in prediction level. When the machine learning algorithm is used alone, the NSE value is 0.42–0.46, irrespective of the algorithm. However, the influence of prediction level on accuracy is reduced by using the KF, although the prediction level changes from 7 to 14 d. In the case of the ANN, the variation of the prediction accuracy decreases to within 0.1, even when the forecast period is doubled.

# **4. Conclusions**

In this study, membrane resistance is predicted using classical methods, single machine learning models, and

![](_page_5_Figure_7.jpeg)

Fig. 5. Performance comparison of single (i.e., ANN and SVM) and hybrid machine learning algorithms (i.e., KF-ANN and KF-SVM) evaluated using operational data from the Fujairah SWRO plant (*N* = 522). (a) and (b) are the accuracies computed in terms of NSE during the training and test steps, respectively. (c) and (d) are the accuracies estimated with respect to *R*<sup>2</sup> during the training and test steps, respectively.

hybrid machine learning models. The ANN and SVM models are employed to predict membrane fouling. In the hybrid models, a KF is applied to decrease noise in the membrane resistance data. Performance of the models is compared in terms of prediction accuracy, depending on model type and forecast limits. From this study, the following conclusions can be drawn:

- (1) When the membrane fouling model is used to predict membrane resistance, only the increasing trend of membrane resistance is predictable.
- (2) Single machine learning algorithms can predict membrane resistance with only low accuracy due to noise in the data. Prediction performance of the algorithm decreases when the prediction level is changed.
- (3) Hybrid machine learning algorithms can predict membrane resistance with higher accuracy than any single machine learning algorithm. The prediction accuracy remains high, although the prediction level is changed. The KF-SVM model shows higher prediction accuracy for plant operational data at each forecasting level.
- (4) It appears that membrane fouling prediction models can be utilized to create early warning systems for membrane fouling.

# **Acknowledgments**

This research was supported by a grant (code 16IFIP-C088924-03) from the Industrial Facilities and Infrastructure Research Program funded by the Ministry of Land, Infrastructure, and Transport of the Korean government and the Korea Agency for Infrastructure Technology Advancement. In addition, we thank Doosan Heavy Industries and Construction for assisting our study by providing experimental data from the Fujairah plant in Dubai.

# **References**

- [1] L.F. Greenlee, D.F. Lawler, B.D. Freeman, B. Marrot, P. Moulin, Reverse osmosis desalination: water sources, technology, and today's challenges, Water Res., 43 (2009) 2317–2348.
- [2] L. Malaeb, G.M. Ayoub, Reverse osmosis technology for water treatment: state of the art review, Desalination, 267 (2011) 1–8.
- [3] V.G. Gude, Energy consumption and recovery in reverse osmosis, Desal. Wat. Treat., 36 (2011) 239–260.
- [4] J.R. Werber, C.O. Osuji, M. Elimelech, Materials for nextgeneration desalination and water purification membranes, Nat. Rev. Mater., 1 (2016) 16018.
- [5] T.I. Yun, C.J. Gabelich, M.R. Cox, A.A. Mofidi, R. Lesan, Reducing costs for large-scale desalting plants using largediameter, reverse osmosis membranes, Desalination, 189 (2006) 141–154.
- [6] I.B. Cameron, R.B. Clemente, SWRO with ERI's PX Pressure Exchanger device—a global survey, Desalination, 221 (2008) 136–142.
- [7] S. Jiang, Y. Li, B.P. Ladewig, A review of reverse osmosis membrane fouling and control strategies, Sci. Total Environ., 595 (2017) 567–583.

- [8] J.C. Schippers, A. Kostense, H.C. Folmer, Effect of Pretreatment of River Rhine Water on Fouling of Spiral Wood Reverse Osmosis Membranes, Vol. 2, Proceedings International Symposium on Fresh Water from the Sea, 1980, pp. 297–306.
- [9] J.C. Schippers, J. Verdouw, The modified fouling index, a method of determining the fouling characteristics of water, Desalination, 32 (1980) 137–148.
- [10] S.F.E. Boerlage, M. Kennedy, M.P. Aniye, J.C. Schippers, Applications of the MFI-UF to measure and predict particulate fouling in RO systems, J. Membr. Sci., 220 (2003) 97–116.
- [11] M.A. Javeed, K. Chinu, H.K. Shon, S. Vigneswaran, Effect of pre-treatment on fouling propensity of feed as depicted by the modified fouling index (MFI) and cross-flow sampler–modified fouling index (CFS–MFI), Desalination, 238 (2009) 98–108.
- [12] L.N. Sim, T.H. Chong, A.H. Taheri, S.T.V. Sim, L. Lai, W.B. Krantz, A.G. Fane, A review of fouling indices and monitoring techniques for reverse osmosis, Desalination, 434 (2018) 169–188.
- [13] K.L. Chen, L. Song, S.L. Ong, W.J. Ng, The development of membrane fouling in full-scale RO processes, J. Membr. Sci., 232 (2004) 63–72.
- [14] Y.G. Lee, Y.S. Lee, D.Y. Kim, M. Park, D.R. Yang, J.H. Kim, A fouling model for simulating long-term performance of SWRO desalination process, J. Membr. Sci., 401–402 (2012) 282–291.
- [15] D.Y. Kim, M.H. Lee, S. Lee, J.H. Kim, D.R. Yang, Online estimation of fouling development for SWRO system using real data, Desalination, 247 (2009) 200–209.
- [16] Y.G. Lee, Y.S. Lee, J.J. Jeon, S. Lee, D.R. Yang, I.S. Kim, J.H. Kim, Artificial neural network model for optimizing operation of a seawater reverse osmosis desalination plant, Desalination, 247 (2009) 180–189.
- [17] G.R. Shetty, S. Chellam, Predicting membrane fouling during municipal drinking water nanofiltration using artificial neural networks, J. Membr. Sci., 217 (2003) 69–86.
- [18] F. Schmitt, K.U. Do, Prediction of membrane fouling using artificial neural networks for wastewater treated by membrane bioreactor technologies: bottlenecks and possibilities, Environ. Sci. Pollut. Res. Int., 24 (2017) 22885–22913.
- [19] O.B. Shukur, M.H. Lee, Daily wind speed forecasting through hybrid KF-ANN model based on ARIMA, Renewable Energy, 76 (2015) 637–647.
- [20] M. Karasalo, X. Hu, An optimization approach to adaptive Kalman filtering, Automatica, 47 (2011) 1785–1793.
- [21] Q. Li, R. Li, K. Ji, W. Dai, Kalman Filter and Its Application, 8th International Conference on Intelligent Networks and Intelligent Systems (ICINIS), 2015, pp. 74–77.
- [22] Y. Park, K.H. Cho, J. Park, S.M. Cha, J.H. Kim, Development of early-warning protocol for predicting chlorophyll-a concentration using machine learning models in freshwater and estuarine reservoirs, Korea, Sci. Total Environ., 502 (2015) 31–41.
- [23] C.M. Bishop, Pattern Recognition and Machine Learning, Springer-Verlag, New York, 2006.
- [24] P.-F. Pai, K.-P. Lin, C.-S. Lin, P.-T. Chang, Time series forecasting by a seasonal support vector regression model, Expert Syst. Appl., 37 (2010) 4261–4265.
- [25] U. Thissen, R. van Brakel, A.P. de Weijer, W.J. Melssen, L.M.C. Buydens, Using support vector machines for time series prediction, Chemom. Intell. Lab. Syst., 69 (2003) 35–49.
- [26] A.J. Smola, B. Schölkopf, A tutorial on support vector regression, Stat. Comput., 14 (2004) 199–222.
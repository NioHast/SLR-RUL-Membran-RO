Hindawi Shock and Vibration Volume 2020, Article ID 8829823, 17 pages <https://doi.org/10.1155/2020/8829823>

![](_page_0_Picture_1.jpeg)

# *Research Article*

## **General Log-Linear Weibull Model Combining Vibration and Temperature Characteristics for Remaining Useful Life Prediction of Rolling Element Bearings**

#### **Mingzhu Lv [,](https://orcid.org/0000-0002-0608-0852) 1,2 Shixun Liu,1,3 Xiaoming Su,<sup>1</sup> and Changzheng Chen<sup>1</sup>**

*1 School of Mechanical Engineering, Shenyang University of Technology, Shenyang 110870, China*

Correspondence should be addressed to Mingzhu Lv; [zhaogx@sut.edu.cn](mailto:zhaogx@sut.edu.cn)

Received 4 March 2020; Revised 18 July 2020; Accepted 3 August 2020; Published 20 August 2020

Academic Editor: Yongteng Zhong

Copyright © 2020 Mingzhu Lv et al. \*is is an open access article distributed under the [Creative Commons Attribution License](https://creativecommons.org/licenses/by/4.0/), which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.

In industrial applications, the vibration and temperature measurements of rolling element bearings are known as two popular condition monitoring methods. \*e previously published method for remaining useful life (RUL) prediction has been limited to using the vibration signal. However, a single signal source cannot fully reflect the degradation trend of bearings, influencing the RUL prediction precision. In this paper, a novel general log-linear Weibull (GLL-Weibull) model is constructed by considering vibration and temperature condition monitoring signals to estimate the model parameters. During the feature extraction stage, the relative root mean square (RRMS) is derived from the monitored vibration signal, and the relative temperature trend value is extracted from the monitored temperature signal to eliminate individual differences in bearings and random signal fluctuations. \*en, a fuzzy operator is introduced to describe the degree of an "overheated bearing" and "excessive bearing vibrations." During the RUL prediction stage, both the extracted vibration and temperature characteristics are used to create the GLL-Weibull model. \*e best parameters are attained by employing the maximum likelihood estimation approach. \*e algorithm performance is checked with criteria like the root mean square error (RMSE) and the mean absolute percentage error (MAPE). \*e effectiveness and superiority of the presented approach are validated by two real-life prognosis cases. According to the experimental results, the presented approach provides superior prediction precision and lower computational cost than other approaches for bearings under constant or variable operating conditions.

## **1. Introduction**

Rolling element bearings are known as important parts in various machines, and bearing failure can lead to considerable losses in production and human casualties. \*erefore, a higher reliability and readiness state for bearings is urgently required, especially for complex and high-maintenance-cost machines such as wind turbines [\[1\]](#page-15-0). In Industry 4.0, industrial cyberphysical systems (ICPSs) have attracted increasing attention both in industry and academia [[2](#page-15-0)–[4](#page-15-0)]. With the development of new intelligent sensors, it is possible to replace the condition monitoring maintenance of large and complex machines with preventive maintenance. To ensure machinery safety, prognostics and health management, including the prediction of performance degradation, have drawn much attention. Prognostics and health management can be utilized to conduct timely maintenance and attain timely RUL predictions and intelligent accident prevention [\[5, 6](#page-15-0)].

\*e effective prediction of RUL must overcome two fundamental deficiencies: developing a useful model and choosing the parameters that reflect the efficiency degradation procedure. Statistical model-based methods estimate the machinery RUL by developing empirical knowledgebased statistical models and employing a probability density function (PDF) to present the observation-dependent prediction results. In the mentioned methods, RUL prediction models are established by fitting the acquired measurements

*<sup>2</sup> School of Automatic Control, Liaoning Equipment Manufacturing Professional Technology Institute, Shenyang 110161, China 3 CQC (ShenYang) North Laboratory, Shenyang 110164, China*

<span id="page-1-0"></span>into stochastic coefficient or stochastic process models by using a probabilistic approach without utilizing any physical concepts. Therefore, statistical model-based methods can be utilized to model the degradation procedure uncertainty and its impact on RUL prediction. Among these approaches, the proportional hazards model (PHM) was first presented by Cox [7] in 1972. In the mentioned model, it was assumed that the system hazard rate consists of two multiplicative functions, including baseline hazard and covariate functions. PHM has no special requirements for data distribution and can analyze failure data and suspension data at the same time. They have been extensively studied and applied in the area of reliability assessment and RUL predicting of mechanical parts. In the literature, Kundu et al. [8] presented a Weibull accelerated failure time regression model for bearings working under multiple operating conditions for the URL prediction. Regattieri et al. [9] presented a novel generalized log-linear Weibull (GLL-Weibull) distributionbased method to estimate the gear life. Kundu et al. [10] combined the clustering output with a change point identification technique to develop RUL prediction models using a general log-linear Weibull (GLL-Weibull) distribution.

Most of the current research is limited to the statistical analysis of a single signal source. Using signal processing techniques, the condition monitoring information is obtained as the input of the prediction model. Vibration signals have been extensively utilized for bearing fault detection and prognosis because they are easy to collect and sensitive to the degradation performance of rolling bearings [11-14]. For instance, Wang et al. [15] extracted time-frequency domain degradation features to construct an enhanced Wiener process model to predict the RUL by utilizing the vibration information of the bearing and predicting the rolling element bearings RUL. However, the vibration signal easily interferes with rolling element bearings working in the presence of variable load and speed situations, and the prediction accuracy is reduced due to the poor signal-tonoise ratio. Therefore, other signals should be used. Recently, the temperature signal has attracted the attention of some scholars. For example, Hu et al. [16] used temperature characteristics to realize the RUL prediction of a wind turbine generator rear bearing. Although the temperature signal has good anti-interference performance, its linear change trend cannot fully demonstrate the nonlinear degradation procedure of the bearing, and the available degradation information can be limited.

In light of the above problems, we propose a novel GLL-Weibull model for the RUL prediction of bearings that considers both vibration and temperature characteristics by taking full advantage of the high sensitivity of vibration characteristics and the powerful anti-interference capability of temperature characteristics (temperature can be utilized to detect the bearings decay caused by the thermal inertia). The extracted features can contain more effective degradation information; thus, the performance of the model is greatly improved. According to the experimental results, the presented approach provides a superior prediction precision and lower computational cost than other approaches for

rolling bearings under constant or variable operating conditions.

The rest of the current study is organized as follows: Section 2 first presents the GLL-Weibull model theory. Then, the methods for multicovariate selection are presented, which include the extraction of vibration features from vibration signals and the extraction of temperature trends from temperature signals. Next, the procedure for the RUL estimation is described in detail in Section 3. The performance of the constructed model is evaluated through a PRONOSTIA data set and a real wind turbine high-speed shaft (HSS) bearing data set for 50 days in Section 4. In the end, conclusions are provided in Section 5.

#### 2. GLL-Weibull Prediction Model

The evolution law of bearing failure probability basically follows the classic "bathtub curve" with service time shown in Figure 1, which can be divided into three state stages: early failure stage, occasional failure stage, and fatigue failure stage. The early failure stage is mainly caused by the initial design, manufacture, and transportation of the equipment and defects resulting from the installation. Before service, each bearing is subjected to a series of industrial tests according to predefined rules, which can effectively suppress the probability of early failure for the bearing in operation. The occasional failure stage and fatigue failure stage occur during the normal bearing service life and are affected by the combined actions of thermal, mechanical, and chemical stresses as well as environmental factors. During these two stages, defects are formed in the bearing, or fatigue gradually deteriorates the bearing, which leads to an increase in the failure rate.

2.1. Fundamental Theory. In accordance with the proportional hazards model (PHM) proposed by Cox, the system failure rate depends on its operation time and the operation covariates. Mathematically, the widely accepted cumulative density function (CDF) of the 2-parameter Weibull distribution can be defined as follows:

$$F(t) = 1 - \exp\left(-\left(\frac{t}{\eta}\right)^{\beta}\right),\tag{1}$$

where t denotes the service time of the wind turbine bearing, i.e., the primary ageing parameter,  $\eta$  describes the characteristic life parameter that indicates when the failure probability is equal to 63%, and  $\beta$  represents the shape parameter that is used to describe different failure stages. The shape parameter defines failure dispersion.

 $\beta$  < 1: The failure component risk reduces by increasing the ageing parameter value, which belongs to the early failure stage.

 $\beta$  = 1: The failure component risk is not changed while increasing the ageing parameter value, which belongs to the occasional failure stage.

<span id="page-2-0"></span>![](_page_2_Figure_2.jpeg)

FIGURE 1: Bathtub curve of failure probability.

 $\beta$  > 1: The failure component risk grows by increasing the ageing parameter value, which belongs to the fatigue failure stage.

Although the failure probability will change with time, various stimulus parameters will also accelerate the expansion of failure rate improvement. The mentioned parameters include the exerted load, operating velocity, pressure, vibration, temperature, torque, etc. Here, these parameters are called covariates. Covariates can be categorized into external and internal covariates. Factors like speed, load, and pressure are named as external covariates. Measurement data from various sensors are used to monitor health status, including vibration, temperature, and torque signals. The outputs of these sensors are termed internal covariates. For bearing problems, when external operating conditions (load, speed) change, the vibration and temperature feature indicators will also be affected. In other words, when external covariates are uncertain or not easy to identify analytically and experimentally, the utilization of various measurable parameters (i.e., vibration and temperature signal) can guarantee the reduction of various uncertainties that originate from environmental conditions, loading levels, and measurement equipment. Therefore, this paper introduces the internal covariates into the Weibull distribution model to establish a general log-linear Weibull (GLL-Weibull) model, which can also be called the Weibull accelerated failure model. The CDF for the GLL-Weibull model is given by the following:

$$F(t,x) = 1 - \exp\left(-\left(\frac{t}{\exp(a_0 + \sum_{i=1}^k a_i x_i)}\right)^{\beta}\right), \quad (2)$$

where the intercept is denoted by  $a_0$ , the i-th covariate (i = 1, 2, ..., k), is described by  $x_i$ , and  $a_i$  represents the influence coefficient of the covariates, which can also be called the regression coefficient.

Letting  $\eta' = \exp(a_0 + \sum_{i=1}^k a_i x_i)$ , the CDF for the GLL-Weibull model can be rewritten as follows:

$$F(t, \eta') = 1 - \exp\left(-\left(\frac{t}{\eta'}\right)^{\beta}\right). \tag{3}$$

The hazard rate function for the GLL-Weibull model is as follows:

$$h(t,\eta') = \frac{\beta}{\eta'} \left(\frac{t}{\eta'}\right)^{\beta-1}, \quad t \ge 0.$$
 (4)

According to the principle of reliability analysis [17], the CDF reliability is also referred to as unreliability. Consider that the distribution reliability function can be easily obtained by subtracting the CDF from one. Thus, the reliability function of the GLL-Weibull model can be written as follows:

$$R(t, \eta') = \left[1 - F(t, \eta')\right] = \exp\left(-\left(\frac{t}{\eta'}\right)^{\beta}\right). \tag{5}$$

Similarly, F(t) is defined as the probability that failure happens at time t or the cumulative distribution function of the failure distribution. Accordingly, the density function of the failure probability is described as follows:

$$f(t,\eta t) = \frac{\mathrm{d}F(t)}{\mathrm{d}t} = -\frac{\mathrm{d}R(t)}{\mathrm{d}t} = h(t,\eta t)R(t,\eta') = \frac{\beta}{\eta'} \left(\frac{t}{\eta'}\right)^{\beta-1} \exp\left(-\left(\frac{t}{\eta t}\right)^{\beta}\right). \tag{6}$$

<span id="page-3-0"></span>The maximum likelihood estimation method (MLE) is usually employed to obtain the unknown parameters of the GLL-Weibull model. The likelihood function can be obtained as follows:

$$L(\beta, \eta \prime) = \prod_{i=1}^{n} f\left(t_{i}, \eta \prime\right) \prod_{j=1}^{m} R\left(t_{j}, \eta \prime\right) = \prod_{i=1}^{n} \frac{\beta}{(\eta \prime)^{\beta}} (t_{i})^{\beta-1} \exp\left(-\left(\frac{t_{i}}{\eta \prime}\right)^{\beta}\right) \prod_{j=1}^{m} \exp\left(-\left(\frac{t_{j}}{\eta \prime}\right)^{\beta}\right), \tag{7}$$

where i is the failure time, j is the suspension time, n describes the number of failure samples, and m indicates the number of suspension samples. Usually, the log-likelihood function is more tractable than the likelihood function, and the simplified form of the log-likelihood function for the GLL-Weibull model can be expressed as follows:

$$\ln[L(\beta, \eta t)] = n \ln \beta - n \beta \ln \eta t + (\beta - 1) \sum_{i=1}^{n} \ln t_i - \sum_{j=1}^{n+m} \left(\frac{t_j}{\eta t}\right)^{\beta}.$$
(8)

Equation (8) can also be written as follows:

$$\begin{split} & \operatorname{In} \left[ L \left( \beta, a_0, a \right) \right] = n \operatorname{In} \beta - n \beta \left( a_0 + \sum_{i=1}^k a_i x_i \right) + (\beta - 1) \sum_{i=1}^n \operatorname{In} t_i \\ & - \sum_{j=1}^{n+m} \left( \frac{t_j}{\exp \left( a_0 + \sum_{i=1}^k a_i x_i \right)} \right)^{\beta}. \end{split} \tag{9}$$

By setting the first partial derivatives of  $\beta$ ,  $a_0$ , a in equation (9) equal to zero and then adopting the Newton-Raphson [18] iterative method for numerical calculation, the optimal estimation of each parameter can be obtained as  $\beta$ ,  $\hat{a}_0$ ,  $\hat{a}$ . The GLL-Weibull model is a completely parameterized model that combines historical condition monitoring data to estimate the RUL at any time. In the presented method, multiple covariates (through measured vibration signals and temperature signals) have been considered to enhance the modeling accuracy and prediction precision.

- 2.2. Feature Extraction Method. In condition monitoring, vibration and temperature features are two important indicators that can reflect the dynamic behavior of bearing degradation. Vibration monitoring is a useful tool for the primary prediction and identification of the bearing failures. On the other hand, bearing temperature can provide information on the upcoming deterioration procedure from extreme mechanical friction.
- 2.2.1. Vibration Feature Extraction. The root mean square (RMS) describes the effective amount (magnitude) of the vibration signal. It can be obtained by calculating the square root of the mean of the sum of the squares of the signal samples using the following equation:

(7)

$$x_{\rm rms} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (x(i))^2},$$
 (10)

where x(i) denotes the ith sample of the primary signal, while the number of samples is represented by n.

Usually, the vibration signals' RMS values are utilized to verify the whole status of the mechanical parts. The reason is that the whole vibration extent generally grows with the service life due to deterioration of the parts like gearbox and bearing. RMS is used as a widely accepted characteristic index for bearing fault diagnosis.

However, even under similar operating situations, the RMS values of various bearings in a stable working stage differ from the others. Therefore, the relative root mean square (RRMS) is proposed as a measurement in this paper, which can be computed by the following equation:

$$x_{\rm rrms} = \frac{x_{\rm rms}}{x_{\rm base}},\tag{11}$$

where  $x_{\text{base}}$  represents the baseline value.

Note that the average mean square root within the relatively flat occasional failure stage of a bearing can be taken as  $x_{\text{base}}$ . Single differences in bearings do not influence the RRMS as a simple index. The RRMS is sensitive to the primary damage and continuously increases with the damage growth.

Then, the smoothing method with 7 points 3 times is adopted to reduce the impact of stochastic vibration, which can be described in the following equation:

$$x_{k}^{\text{MA}} = \begin{cases} \frac{1}{k+3} \sum_{i=1}^{k+3} x_{i}, & k \leq 3, \\ \frac{1}{7} \sum_{i=k-3}^{k+3} x_{i}, & 4 \leq k \leq N-3, \\ \frac{1}{N-k+4} \sum_{i=k-3}^{N} x_{i}, & N-2 \leq k \leq N, \end{cases}$$
(12)

where x is the signal before smoothing,  $x^{MA}$  is the signal after smoothing, and k = 1, 2, ..., N denotes the number of signal samples.

2.2.2. Temperature Trend Analysis. Temperature characteristics can reflect the degradation process of wind turbine bearings caused by many external uncertain factors. To extract the temperature trend of the degradation period

from the temperature monitoring data,  $(t_1, r_1)$ ,  $(t_2, r_2)$ , ...,  $(t_m, r_m)$  denoting the bearing speed time series and  $(t_1, c_1)$ ,  $(t_2, c_2)$ , ...,  $(t_m, c_m)$  denoting the bearing temperature time series are initially obtained. Then, the relative temperature data  $(t_1, c_1')$ ,  $(t_2, c_2')$ , ...,  $(t_m, c_m')$  under different speed operating conditions can be calculated as follows:

$$c'_{k} = \frac{c_{k}}{r_{k}}, \quad k = 0, 1, \dots, m.$$
 (13)

Furthermore, the moving average method is used to eliminate random fluctuations, and the temperature trend data of the bearing degradation period is obtained, which is expressed in the following equation:

$$x_k = \frac{1}{p} \sum_{i=k-p+1}^{k} c_i', \tag{14}$$

where x represents the temperature trend data at the kth time instant and p stands for the number of adjacent data points calculating the mean value.

Based on equation (14), the time series of the temperature trend can be described as  $(t_1, x_1)$ ,  $(t_2, x_2)$ , ...,  $(t_m, x_m)$ , which will gradually increase with the deterioration of the bearing.

2.3. Fuzzification Processing. During practical testing, although the vibration and temperature trend values can reflect the evolution of the bearing from the degradation state to final failure, the sensitivity of the two signals to different types of faults is inconsistent. For example, the vibration and temperature signals are susceptible to position and coupling faults, respectively. Each signal will grow faster under the corresponding sensitive faults, so the change rate of the two signals may be different under the same fault.

By using fuzzy logic, it is possible to process the indications from temperature measurements in parallel with indications from vibration measurements, which can be accomplished such that the signals from the temperature and vibration recording will be processed with a disjunctive-probabilistic fuzzy operator. In a fuzzy set, for each variable t, a fuzzy operator is defined, which may have values in the range between 0 and 1. Expressions of fuzzy operators for vibration and temperature signals are given by the set of equations (15) and (16), respectively:

$$Vib = \begin{cases} 0, & \text{for } v(t) \le v_a, \\ \frac{v(t) - v_a}{v_b - v_a}, & \text{for } v_a < v(t) < v_b, \\ 1, & \text{for } v(t) \ge v_b, \end{cases}$$
(15)

$$Tem = \begin{cases} 0, & \text{for } x(t) \le \theta_a, \\ \frac{x(t) - \theta_a}{\theta_b - \theta_a}, & \text{for } \theta_a < x(t) < \theta_b, \\ 1, & \text{for } x(t) \ge \theta_b, \end{cases}$$
(16)

where Vib and Tem are the fuzzy operators for vibration and temperature indicators, respectively, v(t) and x(t) are the indicator values corresponding to each variable t, the vibration limitations are  $v_a$  and  $v_b$ , and the temperature limitations are  $\theta_a$  and  $\theta_b$ .

Through fuzzification processing, real data are transformed into fuzzy operators. In this paper, the fuzzy subsets of vibration and temperature correspond to three various scenarios, as shown in Figure 2.

- (i) Normal state: All the parameters have under control amounts, while the bearing status is accurate. The fuzzy operator is smaller than 0.5.
- (ii) Early warning: Bearings have begun to degrade, and defects will continue to expand if preventive maintenance is not available. The fuzzy operator ranges from 0.5 to 0.8.
- (iii) Near failure: Recognition and immediate intervention are required to set proper values for the status parameters. In other words, the area belongs to the fuzzy set named "excessive vibrations" or "overheated bearing." The fuzzy operator is greater than 0.8

Based on the vibration and temperature fuzzy operators proposed in this paper, the reliability function at time t for the bearing issue with vibration and temperature coordination is described as follows:

$$R(t, \text{Vib}, \text{Tem}) = \exp\left(-\left(\frac{t}{\exp(a_0 + a_1 \times \text{Vib} + a_2 \times \text{Tem})}\right)^{\beta}\right),$$
(17)

where the intercept is represented by  $a_0$ ,  $\beta$  describes the distribution shape parameter and  $a_1$  and  $a_2$  are the regression coefficients for vibration and temperature fuzzy operators, respectively. Then, the bearing RUL is determined using the following conditional reliability:

$$R(t \mid t_0) = \frac{R(t + t_0)}{R(t_0)},\tag{18}$$

where  $t_0$  denotes the present time, t indicates the bearing failure time, while  $R(t \mid t_0)$  represents the conditional reliability, which is a component or system that has survived to the given time  $t_0$  and works without failure until time t. At the current time, the bearing reliability can be obtained from equation (17). The time to failure of the bearing can be approximately obtained by extrapolating the present condition monitoring to the critical conditional reliability presented in (18) in which its value is determined by the user, and the time t is the RUL of the bearing at  $t_0$ .

2.4. Performance Metrics. Performance criteria are utilized to check the precision of the forecasting method and compare the fluctuation degree of the forecasting results obtained by the different methods. In the current work, the RMSE and MAPE are utilized for evaluating the predicted results. The model performance is measured by the RMSE to

<span id="page-5-0"></span>![](_page_5_Figure_2.jpeg)

FIGURE 2: The fuzzy operators of vibration and temperature features. (a) The fuzzy operator of vibration feature. (b) The fuzzy operator of temperature feature.

reduce the absolute error. The MAPE is employed to prevent the error canceling issue and specifically shows the magnitude of the real prediction error. The RMSE and MAPE can be obtained as follows:

$$RMSE = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2},$$
 (19)

MAPE = 
$$\frac{1}{n} \sum_{i=1}^{n} \left| \frac{y_i - \hat{y}_i}{y_i} \right| \times 100\%,$$
 (20)

where  $y_i$  and  $\hat{y}_i$  describe the real and predicted RUL values, respectively. n denotes the number of data points, and i is the predicted point sequence number. Smaller values of these two criteria indicate higher prediction.

# 3. Remaining Useful Life Prediction Procedure for Rolling Bearings

The prognostic procedure for determining the RUL is shown in Figure 3. The proposed method can be divided into offline and online stages. During the offline stage, by analyzing the data of historically failed bearings, the RRMS and the relative temperature value are derived from the raw vibration and temperature signals as some features, respectively. The smoothing process is performed so that the obtained features better reflect bearing degradation. Then, according to the allowable variation range of vibration and temperature, the two feature values are fuzzified, and the fuzzy operators are used as two internal covariates to estimate the values of unknown parameters of the GLL-Weibull model. The model performance is evaluated using specific performance criteria. During the online stage, the GLL-Weibull model coefficients attained from model training are employed to estimate the RUL. For a service bearing, the RUL estimation is performed

based on the current time. Then, the maintenance decision is made by the user.

#### 4. Experimental Validation and Analysis

#### 4.1. Case 1: PRONOSTIA Experimental Dataset

4.1.1. Experimental Framework and Data Statement. The experimental verification is performed on an accelerated ageing PRONOSTIA platform developed by the FEMTO-ST Institute in France [19]. The experimental equipment is shown in Figure 4. This platform provides practical data describing the normal degradation process of rolling bearings from run to failure under different working situations. Two accelerometers and a thermocouple are installed to pick up the horizontal and vertical vibration signals and the temperature signal. The vibration and temperature signals are acquired every 10 s and 60 s at sampling rates of 25.6 kHz and 10 Hz, respectively. The experiments are finished when the amplitude of the monitoring vibration data becomes greater than 20 g. Hence, the vibration data from run to failure is chosen as a threshold for model training and validation. The observed time to failure information for different bearings under specific working conditions is presented in Table 1. Some studies have shown that some bearings in the data set have an abnormal degradation trend due to improper installation or operation [20-22]. Based on overall vibration and temperature history, bearings 4, 5, 6, and 7 from operating condition (1) (OC1), bearing 4 from OC2, and bearing 3 from OC3 have been considered during initial modeling.

4.1.2. Experimental Results. The presented prediction approach includes two parts. The first one processed the vibration and temperature signals of the bearing's degradation status, including feature extraction, smoothing, and fuzzification, to observe the trend behavior of the two signals.

3148, 2020, 1, Downloaded from https://onlinelibrary.wiely.com/doi/10.1155/20208829823 by Nat Prov Indonesia, Wiley Online Library on [11/1/20206]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons Licensed

<span id="page-6-0"></span>Shock and Vibration

![](_page_6_Figure_2.jpeg)

FIGURE 3: The block diagram of the RUL prediction for rolling bearings.

![](_page_6_Picture_4.jpeg)

FIGURE 4: Overview of the PRONOSTIA experimental platform.

First, according to the content in Section 2, the RRMS amounts of the target bearing vibration signal and the relative temperature amounts of the target bearing temperature signal are calculated. At the same time, the

smoothing process is performed, as small fluctuation regions in the feature can influence the stability of the prognosis model. Figure 5 shows the corresponding feature after the smoothing process for bearing 4 from OC1.

Table 1: Observed time to failure information for bearings (in seconds).

<span id="page-7-0"></span>

| Bearings under different operation conditions (OC) |                       |                       |
|----------------------------------------------------|-----------------------|-----------------------|
| OC1: speed � 1800 rpm                              | OC2: speed � 1650 rpm | OC3: speed � 1500 rpm |
| Load � 4000 N                                      | Load � 4200 N         | Load � 5000 N         |
| 1-1 (28030)                                        | 2-1 (9110)            | 3-1 (5150)            |
| 1-2 (8710)                                         | 2-2 (7970)            | 3-2 (16370)           |
| 1-3 (23750)                                        | 2-3 (19550)           | 3-3 (4040)            |
| 1-4 (14280)                                        | 2-4 (7510)            |                       |
| 1-5 (24630)                                        | 2-5 (23110)           |                       |
| 1-6 (24480)                                        | 2-6 (7010)            |                       |
| 1-7 (22590)                                        | 2-7 (2300)            |                       |

![](_page_7_Figure_4.jpeg)

Figure 5: Vibration and temperature features of bearing 4 from OC1. (a) Vibration features, (b) temperature features.

In addition, the extracted feature must appropriately correlate with the age and health of the bearing. \*e mentioned correlation level can also affect the further stages and even the ultimate prognosis results. \*e fuzzy operator indicates the feature correlation to time and varies among zero and one and tells us when "overheated bearing" and "excessive bearing vibrations" appear. Figure [6](#page-8-0) shows the corresponding fuzzy operator for 6 bearings from different operation conditions. As can be seen from Figure [6,](#page-8-0) the vibration characteristics of all bearings change slightly in the early stage and sharply increase in the later stage. It is complicated to detect the early degradation point of the bearing using the vibration characteristics alone. A single vibration signal cannot fully reflect the degradation trend of the bearing. \*erefore, other signals should be used. In this paper, temperature characteristics are introduced to assist the diagnosis of early bearing degradation. Rapid temperature change or continuous high temperature can cause bearing thermal strain, which accelerates bearing failure. \*erefore, the point when the rising rate of the temperature fuzzy operator suddenly accelerates (i.e., bearings 1-4 and 1- 6) or the temperature fuzzy operator fluctuates near 0.8 (i.e., bearings 1-5, 1-7, 2-4, 3-3) is selected as the starting point of bearing degradation to prepare for the next RUL prediction.

\*e second part of the presented approach describes the GLL-Weibull model establishment and RUL prediction. Six bearing failure records are utilized for model training and validation, as previously illustrated in Section [2.1.](#page-1-0) \*e leaveone-out cross-validation technique is utilized to check the model efficiency. Five bearing failure records are employed to estimate the model parameters. \*e model's effectiveness is evaluated with the sixth bearing, which was not assumed within estimating model parameters. For example, bearings 1-5, 1-6, 1-7, 2-4, and 3-3 are utilized to estimate the model parameters for the RUL prediction of bearing 1-1. Now, the same procedure is performed for remaining bearings (see Table [2\)](#page-9-0).

Table [3](#page-9-0) presents the corresponding values of the model parameters attained from various training data sets. \*e calculated values for the bearing shape coefficients belong to [1.67, 1.68]. \*e intercept amount is in a range from 6.02 to 6.15, the coefficient for the vibration fuzzy operator lies in a range from 0.063 to 0.099, and the coefficient range for the temperature fuzzy operator lies between 0.0024 and 0.0057. Considering several training data sets, a small change in the model coefficient values indicates model consistency. Generally, when the bearings approach the failure status (i.e., failure state degradation or the wear increase), both the vibration and temperature fuzzy operators increase. \*ese coefficients usually describe the impact of covariates on the failure procedure. \*e coefficient values of the vibration and temperature fuzzy operators are positive. It can be

<span id="page-8-0"></span>![](_page_8_Figure_2.jpeg)

Figure 6: Vibration and temperature fuzzy operator for 6 bearings from different operation conditions. (a) Bearing 1-4. (b) Bearing 1-5. (c) Bearing 1-6. (d) Bearing 1-7. (e) Bearing 2-4. (f ) Bearing 3-3.

<span id="page-9-0"></span>

|          |          | OC1      |          | OC2      | OC3      |
|----------|----------|----------|----------|----------|----------|
| 1-4      | 1-5      | 1-6      | 1-7      | 2-4      | 3-3      |
| Test     | Training | Training | Training | Training | Training |
| Training | Test     | Training | Training | Training | Training |
| Training | Training | Test     | Training | Training | Training |
| Training | Training | Training | Test     | Training | Training |
| Training | Training | Training | Training | Test     | Training |
| Training | Training | Training | Training | Training | Test     |

Table 2: Training and testing GLL-Weibull model development.

Table 3: Model parameters for various training data sets under vibration and temperature fuzzy operators.

| Tested bearing     | a0<br>(intercept) | a1<br>(vibration coefficient) | a2<br>(temperature coefficient) | β (shape parameter) |
|--------------------|-------------------|-------------------------------|---------------------------------|---------------------|
| 1-4                | 6.13              | 0.063                         | 0.0048                          | 1.67                |
| 1-5                | 6.08              | 0.072                         | 0.0057                          | 1.68                |
| 1-6                | 6.02              | 0.099                         | 0.0024                          | 1.67                |
| 1-7                | 6.15              | 0.075                         | 0.0041                          | 1.67                |
| 2-4                | 6.14              | 0.086                         | 0.0035                          | 1.68                |
| 3-3                | 6.18              | 0.078                         | 0.0037                          | 1.67                |
| Mean               | 6.104             | 0.079                         | 0.0041                          | 1.67                |
| Standard deviation | 0.054             | 0.014                         | 0.0013                          | 0.0055              |

concluded that an increase in the amount of vibration and fuzzy temperature operators leads to degradation or wear in the bearing. Besides, the corresponding value for the vibration fuzzy operator is higher compared with the fuzzy temperature operator, demonstrating a powerful impact of vibration on the bearing life.

\*e RUL predicting results for the GLL-Weibull model are presented in Figure [7.](#page-11-0) \*e mentioned results correspond to the 95% critical failure probability, i.e., (1 − *R*(*t* + *t*0)). \*e user can select various values for the critical failure probability, and in the current state, the optimal RUL predicting results are achieved with the 95% failure probability. Twenty sets of prediction points were obtained at each 5% time range from the beginning of the degradation phase to its end.

Moreover, *α* − *λ* performance [[23](#page-16-0)] is utilized to verify the predicting performance of the presented approach, where the parameter *α* is adopted to draw upper and lower bounds for error in the RUL estimation procedure, and the parameter *λ* describes the relative time distance of a determined point within working from the end of life. In the current work, the efficiency of the presented approach with *α* � 20% is verified. As seen in Figure [7,](#page-11-0) the prediction accuracy can be guaranteed around *α* � 20% for almost all instances (the experimental results are achieved by computing the mean values). Accordingly, after training the GLL-Weibull by historical data, the RUL value can also be predicted for different values of the load and speed and similar bearing types.

*4.1.3. Comparison Analysis.* To further evaluate the efficiency and advantage of the presented approach, it is compared with previous approaches for the RUL estimating of bearings, like a linear regression model (LRM) [\[24\]](#page-16-0), a support vector machine (SVM) [\[25\]](#page-16-0), a Kalman filter (KF) [\[26\]](#page-16-0), and a convolutional neural network (CNN) [[27](#page-16-0)]. (\*e similar data set is utilized in these approaches—the PRO-NOSTIA data set.) Table [4](#page-11-0) shows the performance metrics of the different methodologies. In Table [4](#page-11-0), it is observed that the LRM has the largest prediction error because the LRM is not suitable for describing nonlinear and nonstationary processes. An LRM trained on all the samples of the entire history may not be able to model the life patterns well. \*e SVM provides better prediction for RUL with large data sets, but improper parameters significantly affect the prediction results due to the lack of any standard approach for choosing the kernel function. \*e present and future failure states can be predicted through the KF. However, a system dynamics knowledge is required to construct straightforward model relations that depend on domain knowledge and a large data set. Although CNN has a higher and longer prediction horizon, finding the optimal network framework is complicated. Moreover, the neural network is unstable and provides various results for various numbers of runs. \*e proposed method can obtain more accurate RUL results with fewer condition monitoring histories from each operating condition, and the computation time is low.

#### *4.2. Case 2: Wind Turbine Bearings*

*4.2.1. Testing Data Description.* To validate the efficiency of the presented RUL predicting approach, a high-speed shaft bearing of a 2 MW wind turbine at a wind farm in Northeast China is taken as another example for analysis. \*e running speed range of the bearing is 1200 rpm∼1800 rpm. In March 2019, a wind turbine stopped working due to a high temperature exceeding the maximum permissible limit of 95°C. \*e wind turbine gearbox suffered from excessive vibration and a continuous rise in temperature. \*e root cause of the failure was the high-speed shaft (HSS) bearing in the

![](_page_10_Figure_1.jpeg)

3148, 2020, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2020/8829823 by Nat Prov Indonesia, Wiley Online Library on [11/10/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

Figure 7: Continued.

<span id="page-11-0"></span>![](_page_11_Figure_2.jpeg)

Figure 7: \*e prognostic performance of the presented approach in terms of the *α* − *λ* metric for 6 bearings from different operation conditions. (a) Bearing 1-4, (b) Bearing 1-5, (c) Bearing 1-6, (d) Bearing 1-7, (e) Bearing 2-4, (f ) Bearing 3-3.

| Tested  |       | LRM   |      | SVM   |      | KF    |      | CNN   |      | Proposed method |
|---------|-------|-------|------|-------|------|-------|------|-------|------|-----------------|
| bearing | RMSE  | MAPE  | RMSE | MAPE  | RMSE | MAPE  | RMSE | MAPE  | RMSE | MAPE            |
| 1-4     | 12.85 | 41.62 | 4.32 | 32.11 | 2.45 | 21.35 | 2.21 | 17.24 | 1.43 | 14.25           |
| 1-5     | 13.68 | 43.24 | 3.57 | 28.72 | 2.53 | 21.42 | 1.23 | 12.31 | 1.62 | 15.56           |
| 1-6     | 15.86 | 44.99 | 4.31 | 32.42 | 2.86 | 24.51 | 1.84 | 13.26 | 1.25 | 13.53           |
| 1-7     | 20.97 | 53.65 | 1.25 | 16.66 | 0.94 | 9.64  | 0.22 | 8.44  | 0.13 | 5.45            |
| 2-4     | 16.73 | 48.28 | 2.56 | 22.32 | 0.33 | 11.66 | 0.25 | 8.96  | 0.28 | 9.02            |
| 3-3     | 11.36 | 37.31 | 3.27 | 28.17 | 2.62 | 25.22 | 0.43 | 9.89  | 0.14 | 6.73            |
| Average | 15.24 | 44.85 | 3.21 | 26.73 | 1.96 | 18.97 | 1.03 | 11.68 | 0.81 | 10.76           |

Table 4: Numerical prognostic performance comparisons of various approaches.

gearbox, and the vibration data were collected for 50 consecutive days by an acceleration sensor mounted on the horizontal direction of the bearing seat. \*e sampling rate of the bearing vibration signal was 97 656 Hz. \*e time domain signal of the bearing life is presented in Figure 8. At the same time, viewing the temperature and speed data recorded in the supervisory control and data acquisition (SCADA) system (data sampled in 10 min intervals), it was found that the bearing temperature showed a total temperature trend rising sharply as a fluctuation until failure (see Figure [9](#page-12-0)).

According to the above data, the RUL prediction process shown in Section [3](#page-5-0) is used to verify and analyze the HSS bearing of the wind turbine.

Figures [10](#page-12-0) and [11](#page-12-0) show the corresponding features after the smoothing process and the fuzzy operator for the HSS bearing from run to failure, respectively. As seen from Figures [10](#page-12-0) and [11](#page-12-0), the vibration feature is sensitive to early bearing faults but has larger fluctuations. On the other hand, the temperature feature demonstrates a steady upward trend with bearing degradation, but the detection of weak faults is

![](_page_11_Figure_9.jpeg)

Figure 8: \*e time domain signal of the HSS bearing.

not effective. In summary, the vibration signal combined with the temperature signal can fully reflect the dynamic degradation of the HSS bearing. \*e proposed approach is an effective and reliable technique for monitoring the health status and predicting the RUL of bearings.

<span id="page-12-0"></span>![](_page_12_Figure_2.jpeg)

FIGURE 9: Temperature monitoring data of the HSS bearing.

![](_page_12_Figure_4.jpeg)

FIGURE 10: Vibration and temperature feature of the HSS bearing. (a) Vibration feature, (b) temperature feature.

![](_page_12_Figure_6.jpeg)

FIGURE 11: Vibration and temperature fuzzy operator of the HSS bearing.

| TT F OTT TAT 11 11   | 1 1   |            | C        | •. •       | . 1     |
|----------------------|-------|------------|----------|------------|---------|
| Table 5: GLL-Weibull | model | parameters | of every | monitoring | period  |
| INDEE 3. GEE TICIOUN | mouci | parameters | or crer, | momitoring | periou. |

| Monitoring period and range (hour) | $a_0$ (intercept) | $a_1$ (vibration coefficient) | $a_2$ (temperature coefficient) | $\beta$ (shape parameter) |
|------------------------------------|-------------------|-------------------------------|---------------------------------|---------------------------|
| Period 1 (1~168)                   | 5.62              | 0.099                         | 0.050                           | 1.69                      |
| Period 2 (167~336)                 | 4.01              | 0.065                         | 0.036                           | 1.70                      |
| Period 3 (337~504)                 | 3.93              | 0.064                         | 0.0023                          | 1.70                      |
| Period 4 (505~672)                 | 3.09              | 0.073                         | 0.0037                          | 1.71                      |
| Period 5 (673~840)                 | 2.64              | 0.077                         | 0.0035                          | 1.68                      |
| Period 6 (841~1008)                | 2.06              | 0.065                         | 0.0046                          | 1.69                      |
| Period 7 (1009~1176)               | 0.45              | 0.055                         | 0.0041                          | 1.72                      |

![](_page_13_Figure_4.jpeg)

FIGURE 12: The distribution of RUL probability density.

4.2.2. Results and Discussion. To estimate the GLL-Weibull model parameters, the 50-day monitoring data are divided into 7 monitoring periods. The time of every monitoring period is 168 hours (h), including 1008 sample points (10 min per sample interval). According to the discussion in Section 2, the four parameters of each monitoring period are estimated using equation (9), as shown in Table 5.

The probability density function (PDF) distribution for the RUL of the HSS bearing is obtained from the estimated parameters presented in Table 5. After 168 h monitoring interval, the PDF distribution of the RUL is determined (see Figure 12). According to Figure 12, the maximum PDF value Fis attained at the corresponding time of the predicted RUL amount, and the RUL time of the HSS bearing after the initial monitoring time range is 2192 h for about 91 days. Likewise, a similar procedure is employed to attain the RUL conditions under the remaining monitoring periods.

The predicted and real RUL amounts of each monitoring period for the HHS bearing are illustrated in Figure 13, and their two error types are also listed as shown in Table 6. Figure 13 demonstrates that the efficiency of the HSS bearing degenerates considerably as the monitoring period interval increases. Narrowing the PDF width makes the RUL predicted results closer to their corresponding real ones

Figure 13 shows that the probability density distribution changes from wide to narrow with the deterioration of the

bearing and the increase of the monitoring data, and the predicting result of the RUL gradually converges to the real one. In Table 6, two different errors are calculated with equations (19) and (20).

The degradation procedure of the HSS bearing includes initial, middle, and final phases. It can be observed that the two errors at the initial stage are larger than those at the middle and final phases. The errors decrease as the monitoring periods increase, and there are some small fluctuations at the middle stage, as shown in Figure 14.

The reasons are analyzed in accordance with Table 6, Figures 13 and 14. At the initial stage of RUL prediction, there are fewer data points available and more uncertainties in the parameter estimation. Compared with the real RUL values, the predicted ones are large. Thus, the two errors are also large. At the middle stage, the vibration and temperature fuzzy operator enters a fluctuating state with the development of the fault. The parameters vary over a small range, so the prediction results also fluctuate. At the final stage, the parameters of the model gradually converge as the monitoring data increase, and the predicted results are more accurate.

In summary, this study demonstrates that the real-time RUL of HSS bearings can be attained by the presented approach using the recorded data of vibration and temperature.

<span id="page-14-0"></span>![](_page_14_Figure_1.jpeg)

FIGURE 13: Comparisons of the RUL results for bearings under different monitoring periods.

Actual RUI.

TABLE 6: Comparisons among real and predicted RUL values

| indee of comparisons among real and predicted Roll values. |                      |                   |      |          |  |  |  |
|------------------------------------------------------------|----------------------|-------------------|------|----------|--|--|--|
| Monitoring period and range (hour)                         | Predicted RUL (hour) | Actual RUL (hour) | RMSE | MAPE (%) |  |  |  |
| Period 1 (1~168)                                           | 2192                 | 1032              | 1160 | 112.4    |  |  |  |
| Period 2 (167~336)                                         | 1036                 | 864               | 172  | 19.9     |  |  |  |
| Period 3 (337~504)                                         | 710                  | 696               | 14   | 2.01     |  |  |  |
| Period 4 (505~672)                                         | 507                  | 528               | 21   | 3.98     |  |  |  |
| Period 5 (673~840)                                         | 396                  | 360               | 36   | 10       |  |  |  |
| Period 6 (841~1008)                                        | 188                  | 192               | 4    | 2.08     |  |  |  |
| Period 7 (1009~1176)                                       | 25                   | 24                | 1    | 4.17     |  |  |  |

![](_page_14_Figure_5.jpeg)

FIGURE 14: RUL predicting the result of the constructed model.

### 5. Conclusions

The present paper proposed a novel general log-linear Weibull (GLL-Weibull) model combining vibration and temperature characteristics for bearing RUL prediction. According to the attained results, the upcoming results can be derived.

- (1) The GLL-Weibull model is a multicovariate-based reliability model that can be used for the reliable estimation of mechanical components. During
- model development, the effects of vibration and temperature monitoring data are considered.

3148,020.0.1, Downloaded from https://onlinelibrary.vinley.com/doi/10.1155/2020/882923 by Nat Prov Indonesia, Wiley Online Library on [11/10/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/rerms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

- (2) By extracting the RRMS of the vibration signal, the influence of individual differences on different degradation stages can be eliminated.
- (3) By extracting the relative temperature feature, it can be observed that the relative temperature increases the trend of the bearing from run to failure.

- <span id="page-15-0"></span>(4) Due to asynchronous problems in vibration and temperature characteristics, the fuzzy operator is a reliable tool for describing the degree of faulty bearing degradation.
- (5) \*e effectiveness and superiority of the presented approach are evaluated using two different bearing data sets. Due to its robustness, this approach can be applied to bearings under constant or variable working situations.

Although the presented approach is evaluated with bearings examined in different cases, its usefulness and progress under strong interference working situations will be verified in the future. In addition, a mixed RUL prediction model after bearing maintenance will be explored in our next research project.

## **Data Availability**

\*e data used to support the findings of this study are available from the corresponding author upon request.

## **Conflicts of Interest**

\*e authors declare no conflicts of interest.

## **Authors' Contributions**

Mingzhu Lv and Shixun Liu performed conceptualization. Mingzhu Lv performed methodology. Xiaoming Su provided resources. Changzheng Chen performed data curation. : Mingzhu Lv wrote the original draft. Mingzhu Lv reviewed and edited the article. Xiaoming Su and Changzheng Chen supervised the study. All authors have read and agreed with the published version of the paper.

## **Acknowledgments**

\*e presented work was supported by the National Natural Science Foundation of China (No. 51675350). \*e authors would like to thank the Longyuan Renewable Energy Wind Power Co., Ltd. for providing the necessary data.

## **References**

- [1] J. Wang, Y. Liang, Y. Zheng, R. X. Gao, and F. Zhang, "An integrated fault diagnosis and prognosis approach for predictive maintenance of wind turbine bearing with limited samples," *Renewable Energy*, vol. 145, pp. 642–650, 2020.
- [2] S. Yin, J. J. Rodriguez-Andina, and Y. Jiang, "Real-time monitoring and control of industrial cyberphysical systems," *IEEE Industrial Electronics Magazine*, vol. 13, no. 4, pp. 38–47, 2019.
- [3] Y. Jiang and S. Yin, "Recent advances in Key-Performance-Indicator oriented prognosis and piagnosis with a MATLAB Toolbox: DB-KIT," *IEEE Transactions on Industrial Informatics*, vol. 15, no. 5, pp. 2849–2858, 2018.
- [4] Y. Jiang, S. Yin, and O. Kaynak, "Data-driven monitoring and safety control of industrial cyber-physical systems: basics and beyond," *IEEE Access*, vol. 6, pp. 47374–47384, 2018.

[5] W. Teng, X. Zhang, Y. Liu, A. Kusiak, and Z. Ma, "Prognosis of the remaining useful life of bearings in a wind turbine gearbox," *Energies*, vol. 10, no. 1, p. 32, 2017.

- [6] J. Carroll, S. Koukoura, A. McDonald, A. Charalambous, S. Weiss, and S. McArthur, "Wind turbine gearbox failure and remaining useful life prediction using machine learning techniques," *Wind Energy*, vol. 22, no. 3, pp. 360–375, 2019.
- [7] P. Mazidi, M. Du, L. B. Tjernberg, and M. A. S. Sanz, "A health condition model for wind turbine monitoring through neural networks and proportional hazard models," *Proceedings of the Institution of Mechanical Engineers, Part O: Journal*, vol. 231, no. 5, pp. 481–494, 2017.
- [8] P. Kundu, A. K. Darpe, and M. S. Kulkarni, "Weibull accelerated failure time regression model for remaining useful life prediction of bearing working under multiple operating conditions," *Mechanical Systems and Signal Processing*, vol. 134, Article ID 106302, 2019.
- [9] A. Regattieri, A. Casto, F. Piana, M. Faccio, and E. Ferrari, "Reliability assessment of a packaging automatic machine by accelerated life testing approach," *Procedia Manufacturing*, vol. 11, pp. 2178–2186, 2017.
- [10] P. Kundu, S. Chopra, and B. K. Lad, "Multiple failure behaviors identification and remaining useful life prediction of ball bearings," *Journal of Intelligent Manufacturing*, vol. 30, no. 4, pp. 1795–1807, 2019.
- [11] D. P. Rommel, D. D. Maio, and D. Tinga, "Calculating wind turbine component loads for improved life prediction," *Renewable Energy*, vol. 146, pp. 223–241, 2020.
- [12] Z. Liu, L. Zhang, and J. Carrasco, "Vibration analysis for largescale wind turbine blade bearing fault detection with an empirical wavelet thresholding method," *Renewable Energy*, vol. 146, pp. 99–110, 2020.
- [13] J. Wang, M. Xu, C. Zhang, B. Huang, and F. Gu, "Online bearing clearance monitoring based on an accurate vibration Analysis," *Energies*, vol. 13, no. 2, p. 389, 2020.
- [14] W. Bao, X. Miao, H. Wang, G. Yang, and H. Zhang, "Remaining useful life assessment of slewing bearing based on spatial-temporal sequence," *IEEE Access*, vol. 8, pp. 9739– 9750, 2020.
- [15] H. Wang, X. Ma, and Y. Zhao, "An improved Wiener process model with adaptive drift and diffusion for online remaining useful life prediction," *Mechanical Systems and Signal Processing*, vol. 127, pp. 370–387, 2019.
- [16] Y. Hu, H. Li, and X. Liao, "Performance degradation model and prediction method of real-time remaining life for wind turbine bearings," *Proceedings of the CSEE*, vol. 36, no. 6, pp. 1643–1649, 2016.
- [17] C. E. Ebeling, *An Introduction to Reliability and Maintainability Engineering*, McGraw-Hill, New York, NY, USA, 2004.
- [18] J. Wen, H. Gao, and J. Zhang, "Bearing remaining useful life prediction based on a nonlinear wiener process model," *Shock and Vibration*, vol. 2018, Article ID 4068431, 13 pages, 2018.
- [19] P. Nectoux, R. Gouriveau, K. Medjaher et al., "PRONOSTIA: an experimental platform for bearings accelerated degradation tests," *IEEE International Conference on Prognostic Health Management*, pp. 1–8, 2012.
- [20] W. Ahmad, S. A. Khana, M. M. M. Islama, and J.-M. Kim, "A reliable technique for remaining useful life estimation of rolling element bearings using dynamic regression models," *Reliability Engineering & System Safety*, vol. 184, pp. 67–76, 2019.
- [21] A. Z. Hinchi and M. Tkiouat, "Rolling element bearing remaining useful life estimation based on a convolutional

- <span id="page-16-0"></span>long-short-term memory network," *Procedia Computer Science*, vol. 127, pp. 123–132, 2018.
- [22] F. Xu, F. Yan, X. Fan, Z. Huang, and K. L. Tsui, "Extracting degradation trends for roller bearings by using a movingaverage stacked auto-encoder and a novel exponential function," *Measurement*, vol. 152, Article ID 107371, 2020.
- [23] Z. Pan, Z. Meng, Z. Chen, W. Gao, and Y. Shi, "A two-stage method based on extreme learning machine for predicting the remaining useful life of rolling-element bearings," *Mechanical Systems and Signal Processing*, vol. 144, Article ID 106899, 2020.
- [24] S. Vesely, C. A. Klockner, and M. Dohnal, "Predicting recycling behaviour: comparison of a linear regression model and a fuzzy logic model," *Waste Management*, vol. 49, pp. 530–536, 2016.
- [25] Z. Chen, S. Cao, and Z. Mao, "Remaining useful life estimation of aircraft engines using a modified similarity and supporting vector machine (SVM) approach," *Energies* , vol. 11, no. 1, p. 28, 2018.
- [26] R. K. Singleton, E. G. Strangas, and S. Aviyente, "Extended kalman filtering for remaining-useful-life estimation of bearings," *IEEE Transactions on Industrial Electronics*, vol. 62, no. 3, pp. 1781–1790, 2015.
- [27] X. Li, W. Zhang, and Q. Ding, "Deep learning-based remaining useful life estimation of bearings using multi-scale feature extraction," *Reliability Engineering & System Safety* , vol. 182, pp. 208–218, 2019.
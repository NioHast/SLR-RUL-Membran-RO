![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_1.jpeg)

*Article*

# **Statistical Characterization of the State-of-Health of Lithium-Ion Batteries with Weibull Distribution Function—A Consideration of Random Effect Model in Charge Capacity Decay Estimation**

**Chinedu I. Ossai \* [ID](https://orcid.org/0000-0002-9749-3256) and Nagarajan Raghavan \***

Engineering Product Development (EPD) Pillar, Singapore University of Technology and Design, Singapore 487372, Singapore

**\*** Correspondence: chinedu\_ossai@sutd.edu.sg (C.I.O.); nagarajan@sutd.edu.sg (N.R.); Tel.: +65-8196-8960 (C.I.O.); Tel: +65-6499-8756 (N.R.)

Academic Editor: James Marco

Received: 4 August 2017; Accepted: 9 October 2017; Published: 16 October 2017

**Abstract:** Effective prognosis of lithium-ion batteries involves the inclusion of the influences of uncertainties that can be incorporated through random effect parameters in a nonlinear mixed effect degradation model framework. This study is geared towards the estimation of the reliability of lithium-ion batteries, using parametric effects determination involving uncertainty, using a multiphase decay patterned sigmoidal model, experimental data and the Weibull distribution function. The random effect model, which uses Maximum Likelihood Estimation (MLE) and Stochastic Approximation Expectation Maximization (SAEM) algorithm to predict the parametric values, was found to estimate the remaining useful life (RUL) to an accuracy of more than 98%. The State-of-Health (SOH) of the batteries was estimated using the Weibull distribution function, which is found to be an appropriate formulation to use.

**Keywords:** charge capacity decay; end of life; reliability; state of health; uncertainty; Weibull distribution function

## **1. Introduction**

Monitoring the State-of-Health (SOH) of lithium-ion batteries by means of remaining useful life (RUL) estimation and the measurement of other health indicators, such as the State-of-Charge (SOC), are vital for intelligent battery management systems [\[1\]](#page-11-0). This practice is especially important for monitoring systems on critical missions where the lithium-ion battery serves as the main power source, because the right information on the wear-out state and lifecycle of the battery will, in turn, ensure a higher probability of a successful mission. To this end, many researchers [\[1](#page-11-0)[–9\]](#page-11-1) have worked on the charge capacity decay modeling of lithium-ion batteries, in a bid to predict the degradation over time and to predict the SOH at different lifecycle phases [\[10\]](#page-11-2). Since total asset integrity management protocol entails the understanding of the performance and reliability of its components, sub-systems and systems, it is imperative that the trend of lithium-ion battery degradation is well understood, to forestall unplanned failures of facilities such as that of the plagued spacecrafts, which suffered fatal failures in the recent past due to power system failures [\[11\]](#page-11-3).

Coincidentally, the practice of lithium-ion battery prognosis, which depends on the charge capacity degradation estimation over the period of use of the battery, has not yet resulted in an effective and standardized lifetime estimation procedure, predominantly due to the negligence of uncertainties that affect the charge capacity of these batteries. These uncertainties can come from numerous sources that include the manufacturing and assembly of the lithium-ion battery components, measurement

*Batteries* **2017**, *3*, 32 2 of 14

errors associated with the reading of charge and discharge related values, operational environmental conditions of the battery, errors inherent in charge capacity decay modeling equations and uncertainties inherent in the electrochemical reactions in the battery system [\[5,](#page-11-4)[12](#page-11-5)[,13\]](#page-11-6). When considering the cumulative effects of these uncertainties that result in poor model development, since parametric values may not be precisely estimated, it is imperative that the influences of these uncertainties associated with the battery charge capacity be considered a priori in the model development stage. Inclusion of uncertainties as constituent terms in the degradation models will certainly account for the imbalances they create, thereby enhancing the predictability of the models. Moreover, since it is difficult to certify that the components in every lithium-ion battery are defect free, it is a safer option to construct charge capacity decay estimation models with uncertainties embedded in the framework. Another factor to consider is that of time-dependent uncertainties in the components of lithium-ion batteries that may originate and propagate during the operational life of the battery due to the unwarranted responses and the transient nature of the operating and environmental conditions. To this end, the best approach to predictive estimation of the RUL and SOH of lithium-ion batteries involves the consideration of uncertainties, through the random effect model framework [\[14,](#page-11-7)[15\]](#page-11-8). Imperatively, the random effect model has the potential of incorporating uncertainties in prediction models, an attribute that many models used in literature for the estimation of battery retention life have not got. Random effect model also considers individual time changes amongst the covariates, while implementing a continuous time architecture, making it easier to estimate future behavioral patterns from the model. Due to the flexibility of the technique, variables that have repetitive values are easily captured in predictions and generic formulation of trends for non-normally distributed datasets are effortlessly achieved, because the covariances used for measurements are adaptable.

To date, researchers have used several techniques to predict the RUL distribution and SOH for Li-ion batteries including particle filters, improved particle filters and Kalman filters [\[4](#page-11-9)[,13,](#page-11-6)[16–](#page-11-10)[19\]](#page-12-0). Several machine learning approaches involving artificial neural networks, support vector machines, relevance vector machine, and Fuzzy K-means [\[6,](#page-11-11)[20](#page-12-1)[–22\]](#page-12-2) have also been used in the recent past. Other approaches include the use of the Wiener process for RUL prediction with the maximum likelihood estimation and Bayesian updated expectation and maximization algorithm, which potentially gave a good fit for the experimental results for Li-ion battery charge decay [\[23\]](#page-12-3). Ng et al. [\[24\]](#page-12-4) used the naïve Bayes model for different operating conditions of the Li-ion battery and concluded that the capacity fade is always higher at elevated temperatures. This capacity fade was further shown to be associated with the rise of impedance at the cathodes [\[25\]](#page-12-5). Similarly, after analyzing the failure cycles of the lithium ion battery, Harris et al. [\[26\]](#page-12-6) concluded that the variation in failure times of the batteries was wide among the various cells. Despite the poor failure estimation results obtained by them using the three-parameter Weibull distribution function [\[26\]](#page-12-6), they also obtained results that showed better fits to the experimental data with a two-parameter Weibull distribution as well as the normal distribution.

Although the work of numerous researchers on lithium-ion battery prognosis, RUL and SOH estimation as summarized above [\[2](#page-11-12)[–4](#page-11-9)[,8](#page-11-13)[,17](#page-12-7)[,22](#page-12-2)[,27](#page-12-8)[,28\]](#page-12-9) have gained sufficient ground, our aim here is to add a new dimension to the study by accounting for uncertainty, using the random effect model, to enhance the predictability of RUL for lithium-ion batteries under real-life test. It is important to note that the prognostic studies on Li-ion batteries carried out by most of the reviewed papers here, did not account for uncertainties in the charge decay patterns and their impact on the prediction accuracy. This makes it imperative that the effects of uncertainties be considered in the right way, so as to understand the influences of these random factors on the RUL estimation. Negligence of uncertainties could be a fundamental source of faulty prognosis and unreliable RUL predictions. Since the uncertainties associated with the battery charge capacity decay such as manufacturing defects, environmental conditions, experimental measurement errors and physical and chemical characteristics of defects in materials etc. [\[17\]](#page-12-7) are difficult to measure and can alter the health of the battery and the subsequent charging and discharging patterns, the use of the nonlinear mixed effect model (NLMEM) [\[14,](#page-11-7)[15\]](#page-11-8) will help to determine the influences of

Batteries 2017, 3, 32 3 of 14

these random variables on the parametric values of the charge decay prediction model. NLMEM provides a methodology for estimating the influences of the uncertainties on the model parameters, thereby making it easier to understand the behavioral trend of the battery charge capacity decay. Also, the decay patterns of different Li-ion batteries, used for nonlinear mixed effect modeling, provide holistic information for better prognosis of similar batteries, since heterogeneous charge capacity decay information from different batteries with similar characteristics will help to develop better-fit generic prediction models for the RUL. This study will incorporate the uncertainties in the parametric values by using a multiphase decay sigmoidal model, to estimate the charge capacity decay trend of the batteries and use a two-parameter Weibull distribution function for fitting the RUL distribution, which has been shown to be robust for RUL estimation [29–31] to determine the characteristic life of the batteries at 70% end-of life (EOL) failure threshold. Since battery charge capacity decay is expected to be a non-reversible process (synonymous to wear-out failures), the use of the two-parameter Weibull function for estimating the expected characteristic life at a given EOL threshold will give an indication of the RUL and the SOH of the battery at a given cycle.

#### 2. Formulation of Charge Capacity Decay Model Considering Uncertainties

We analyzed the data of Li-ion battery charge capacity decay for four batteries—B0029, B0030, B0031, and B0032 that were experimentally tested under accelerated stress conditions from an initial charge capacity of 2.0 Ah at the NASA AMES laboratory [32]. The charge capacities at the charging cycles and times were obtained for individual batteries through operations that involved charging, discharging and impedance measurements at a temperature of 43  $^{\circ}$ C. The charging was carried out via a constant current of 1.5 A to a voltage of 4.2 V, which was held constant until the battery capacity discharged to 20 mA. The discharge was carried out at a current of 4 A until the batteries B0029, B0030, B0031, and B0032 got to a voltage of 2.0 V, 2.2 V, 2.5 V, and 2.7 V respectively. The charge capacity decay trend of the lithium-ion batteries versus cycles of charge/discharge as obtained from the experiment are plotted in Figure 1.

<span id="page-2-0"></span>![](_page_2_Figure_4.jpeg)

**Figure 1.** Degradation trend of charge capacity for lithium-ion batteries—B0029, B0030, B0031, and B0032 as a function of various operational cycles.

The model for battery charge decay has been shown to follow a sigmoidal curve pattern [2,4,5] and can be ascribed to a multiphase decay pattern as per Equation (1).

$$Q(t) = P_1 \exp(-r_1 t) + P_2 \exp(-r_2 t)$$
(1)

Batteries 2017, 3, 32 4 of 14

where Q(t) represents the charge capacity at time t,  $P_1$  and  $P_2$  represent the battery charge capacity baseline values that depend on the internal impedance of the battery, whereas  $r_1$  and  $r_2$  are charge capacity decay constants, which are related to the battery cell rechargeability and the electrolyte status of the battery. Incorporating the uncertainties in the modeling will result in the implementation of a nonlinear mixed effect model; hence, Equation (1) will be modeled with consideration of the fixed and random effects, to cater for the inherent uncertainties in the battery charge capacity decay.

To ensure a better fit to the dataset, stabilize the variance and ensure normally distributed variables, Equation (1) was reparametrized according to Equation (2).

$$Q(t) = P_1 \exp(-\lambda_1 t) + P_2 \exp(-\lambda_2 t)$$

$$\lambda_1 = \log(r_1)$$

$$\lambda_2 = \log(r_2)$$
(2)

By using the general form of the NLMEM that has response  $y_{ij}$  as the charge capacity decay and the covariate  $x_{ij}$  as the time of observation of capacity decay, the charge capacity at any time of observation with known and unknown parameters can be represented by Equation (3).

$$y_{ij} = f(x_{ij}, \phi_{ij}) + \varepsilon_{ij}, \ 1 \le i \le n, 1 \le j \le m_i$$
(3)

where  $\varepsilon_{ij}$  is the error, which is assumed to be independent and identically distributed (*iid*) Gaussian random number with zero mean and unknown variance  $\sigma^2 \to N$  (0,  $\sigma^2$ ), n represents the number of covariates,  $m_i$  is the number of observations of ith covariates, whereas f is a nonlinear function of the fixed and random effects, and  $\phi_{ij}$  represents a vector that combines the fixed and random effects according to Equation (4).

$$\Phi_{ij} = A_{ij}\alpha + \beta_{ij}b_i; \ b_i = N(0, \sigma^2 D)$$
(4)

Here,  $A_{ij}$  denotes a matrix for combining the fixed effects, while  $\beta_{ij}$  is the matrix for combining the random effects,  $b_i$  represents the random effect vector of the parameters and  $\sigma^2 D$  is a covariance matrix.

To determine the response vector,  $y_i$ , for the ith individual, using the individual fixed and random effect  $\phi_i$ , the relationship in Equation (5) was used [33].

$$y_{i} = \begin{bmatrix} y_{i1} \\ y_{i2} \\ \vdots \\ y_{im_{i}} \end{bmatrix}; \quad \varepsilon_{i} = \begin{bmatrix} \varepsilon_{i1} \\ \varepsilon_{i2} \\ \vdots \\ \varepsilon_{im_{i}} \end{bmatrix}; \quad \eta_{i}(\phi_{i}) = \begin{bmatrix} f(\phi_{i}, x_{i1}) \\ f(\phi_{i}, x_{i1}) \\ \vdots \\ f(\phi_{i}, x_{im_{i}}) \end{bmatrix}; \quad (5)$$

Equation (5) can be further simplified to Equation (6).

$$y_i = \eta_i(\phi_i) + \varepsilon_i \; ; \; \varepsilon_i \sim N(0, \sigma^2 \Lambda_i)$$
 (6)

where  $\eta_i$  is a function of the known and unknown variables and  $\Lambda_i$  is an identity matrix.

For n individual models, the response vector, y, the vector,  $\phi$ , and the nonlinear function of the  $\phi$  vector,  $\eta$ , can be expressed by Equation (7).

$$y = \begin{bmatrix} y_1 \\ y_2 \\ \vdots \\ y_n \end{bmatrix}; \quad \phi = \begin{bmatrix} \phi_1 \\ \phi_2 \\ \vdots \\ \phi_n \end{bmatrix}; \quad \eta(\phi) = \begin{bmatrix} \eta_1(\phi_1) \\ \eta_1(\phi_1) \\ \vdots \\ \eta_n(\phi_n) \end{bmatrix}; \quad (7)$$

Batteries **2017**, 3, 32 5 of 14

If  $\check{D} = diag(D_1, D_2, \dots, D_n)$  and  $\Lambda = diag(\Lambda_1, \Lambda_2, \dots, \Lambda_n)$ , then the response variable y can be expressed by Equation (8).

$$y|(\alpha,b) \sim N(\eta(\sigma^2\Lambda), \phi = A\alpha + \beta b, b \sim (0,\sigma^2D))$$
 (8)

where  $B = diag(B_1, B_2, ..., B_n)$ ,  $b = diag(b_1, b_2, ..., b_n)^T$  and  $A = diag(A_1, A_2, ..., A_n)^T$ .

Estimation of Future Battery Charge Capacity

Estimation of the future battery charge capacity is a vital aspect of prognostics as this information will be essential to provide details of the RUL of the battery at a given time, for a predetermined failure threshold such as 70% of maximum retainable charge capacity. To determine the future charge capacity, the parametric values of the random effect model, which incorporates uncertainties was needed. The following steps were adopted for the prediction and computation of these parametric values:

1. Determine the maximum likelihood function value, L, of the battery charge capacity over time using the experimental data and apply Equation (9) that has  $P(Q_{ij}, \phi_{ij})$ , representing the probability density function of the nonlinear battery charge decay [34].

$$L(\phi_{ij}, Q_{ij}) = \prod_{i=1}^{n} \prod_{j=1}^{m_i} P(Q_{ij}, \phi_{ij}) = \prod_{i=1}^{n} \prod_{j=1}^{m_i} \int P(Q_{ij}, b_i, \phi_{ij}) db$$
 (9)

2. Estimate the maximum likelihood of the parameters in  $\phi$  that will maximize *L* by following Equation (10) [35,36].

$$\frac{\partial \log(L)}{\partial b} = 0 \tag{10}$$

- 3. Apply stochastic approximation, expectation, and maximization technique that uses Markov Chain Monte Carlo (MCMC) simulation and Metropolis-Hasting algorithm to estimate the known and unknown parameters of the model, φ.
  - i. Simulation step: For kth iterative evaluation, determine the variable  $s_{k+1}$  such that the condition in Equation (11) is satisfied [37].

$$s_{k+1} = E[\log P(Q, b, \phi) | Q, \phi_k] \tag{11}$$

ii. Stochastic approximation step: Update the value of  $s_{k+1}$  as per Equation (12).

$$s_{k+1} = s_k + \gamma_k \left[ \log P\left(Q, b^{(k)}; \phi\right) - s_k \right]$$
(12)

where  $\gamma_k$  represents decreasing positive numbers that satisfy the conditions in Equation (13).

$$\begin{cases} \gamma_k = [0, 1] \\ \sum_{k=1}^{\infty} \gamma_k = \infty \\ \sum_{k=1}^{\infty} \gamma_k^2 < \infty \end{cases}$$
 (13)

iii. Maximization step: Update  $\phi_k$  so as to maximize its value based on the relationship in Equation (14).

$$\phi_{k+1} = \underset{\phi}{\operatorname{argmax}}(L(s_{k+1}, \phi)) \tag{14}$$

4. Determine the charge capacity of the batteries using the estimated parameters such that the charge capacity prediction ( $Q_{pred}$ ) is a function of the fixed effect parameters defined— $P_1$ ,  $\lambda_1$ ,  $P_2$ ,

Batteries 2017, 3, 32 6 of 14

 $\lambda_2$ , and the random effects  $\rightarrow \psi_{11}$ ,  $\psi_{22}$ ,  $\psi_{33}$ , and  $\psi_{44}$ , which are the random effects on  $P_1$ ,  $\lambda_1$ ,  $P_2$ , and  $\lambda_2$ , respectively.

- 5. Estimate the residual ( $R_{es}$ ) of the random effect model estimated charge capacity from the measured charge capacity.
- 6. Predict the charge capacity of the lithium-ion batteries by incorporating the noise to  $Q_{pred}$  to obtain the random effect modelled charge capacity decay ( $Q_{rnd}$ ), as per Equation (15).

$$Q_{rnd} = Q_{pred} + normrnd[0, std(R_{es})]$$
(15)

7. Estimate the distribution of times of the battery discharge for a 70% End-of-Life (EOL) failure threshold, which is the time instant at which the battery retains 70% of the original charge capacity.

#### 3. Results and Discussion

3.1. Battery Prognosis using Stochastic EM Algorithm

The summary of the parametric values of the lithium-ion batteries obtained with the stochastic approximation, expectation, and maximization (SAEM) technique is shown in Table 1.

<span id="page-5-0"></span>**Table 1.** Summary of the parametric values of the Lithium-ion battery charge decay model using the stochastic approximation expectation and maximization algorithm.

| Parameters  | B0029   | B0030   | B0031   | B0032   |
|-------------|---------|---------|---------|---------|
| $P_1$       | 1.8445  | 1.7729  | 1.8232  | 1.8812  |
| $\lambda_1$ | -6.6079 | -6.6265 | -7.0221 | -6.5622 |
| $P_2$       | -2.4236 | -2.4666 | -2.4418 | -2.4521 |
| $\lambda_2$ | 0.3542  | 0.4402  | 0.3330  | 0.2969  |

The parametric values of the batteries in Table 1 were used for estimating the battery charge capacities over the time interval of the experiment, which is shown in Figure 2 with 95% and 99% confidence intervals and the measurement results.

<span id="page-6-0"></span>Batteries 2017, 3, 32 7 of 14

![](_page_6_Figure_1.jpeg)

**Figure 2.** Comparison of the measured data with the random effect model estimated lithium-ion battery charge decay for the four batteries assessed in this study at 95% and 99.5% confidence intervals—(a) B0029, (b) B0030, (c) B0031 and (d) B0032.

### 3.2. Validation of Estimation Modeling Technique

To validate the random effect model, the Mean Absolute Error (MAE), Mean Absolute Percentage Error (MAPE), and Coefficient of Efficiency (COE), as shown in Equation (16) were used:

$$\begin{cases}
MAE = \frac{1}{m} \sum_{i=1}^{m} |Q_{exp_i} - Q_{rnd_i}| \\
MAPE = \frac{1}{m} \sum_{i=1}^{m} \left| \frac{Q_{exp_i} - Q_{rnd_i}}{Q_{exp_i}} \right| * 100 \\
COE = 1 - \sum_{i=1}^{m} \left( Q_{exp_i} - Q_{rnd_i} \right)^2 \\
\sum_{i=1}^{m} \left( Q_{exp_i} - Q_{mean} \right)^2
\end{cases}$$
(16)

where  $Q_{exp}$  is the experimental result,  $Q_{rnd}$  is the random effect model prediction results, m is the number of samples, and  $Q_{mean}$  is the mean of the experimental result. The results of the MAE, MAPE, and COE are shown in Tables 2 and 3.

*Batteries* **2017**, *3*, 32 8 of 14

<span id="page-7-0"></span>**Table 2.** Mean Absolute Error (MAE) and Mean Absolute Percentage Error (MAPE) of the Lithium-ion batteries obtained at 95% and 99% confidence intervals.

| Error Measure<br>Technique | Mean Absolute Error (MAE) |             |             | Mean Absolute Percentage Error (MAPE) |             |             |  |
|----------------------------|---------------------------|-------------|-------------|---------------------------------------|-------------|-------------|--|
| Lithium ion battery        | Mean value                | Lower value | Upper value | Mean value                            | Lower value | Upper value |  |
| 95% Confidence Interval    |                           |             |             |                                       |             |             |  |
| B0029                      | 0.0138                    | 0.0246      | 0.0204      | 0.8035                                | 1.4242      | 1.1832      |  |
| B0030                      | 0.0168                    | 0.0200      | 0.0237      | 1.0116                                | 1.1933      | 1.4323      |  |
| B0031                      | 0.0124                    | 0.0168      | 0.0173      | 0.7096                                | 0.9593      | 0.9915      |  |
| B0032                      | 0.0166                    | 0.0248      | 0.0254      | 0.9440                                | 1.4105      | 1.4524      |  |
| 99% confidence interval    |                           |             |             |                                       |             |             |  |
| B0029                      | 0.0121                    | 0.0253      | 0.0271      | 0.7044                                | 1.4601      | 1.5751      |  |
| B0030                      | 0.0148                    | 0.0253      | 0.0276      | 0.8893                                | 1.5211      | 1.6652      |  |
| B0031                      | 0.0124                    | 0.0191      | 0.0202      | 0.7094                                | 1.0874      | 1.1638      |  |
| B0032                      | 0.0160                    | 0.0298      | 0.0288      | 0.9066                                | 1.6909      | 1.6473      |  |

<span id="page-7-1"></span>**Table 3.** Coefficient of Efficiency (COE) for the lithium-ion battery estimation at 95% and 99% confidence intervals.

| Battery | B0029  | B0030  | B0031  | B0032  |
|---------|--------|--------|--------|--------|
| 95%     | 0.9196 | 0.8900 | 0.8731 | 0.8948 |
| 99%     | 0.9394 | 0.9044 | 0.8848 | 0.9069 |

The results in Table [2](#page-7-0) showed that the percentage variation between the random effect model predicted battery charge capacity trend and the charge capacity determined experimentally is 0.71% and 1.45% at 95% confidence interval and between 0.70% and 1.69% for 99% confidence interval. Imperatively, the random effect model estimated charge capacity had predicted the experimental results to an error of <2%. The high values of the coefficient of efficiency (0.8731–0.9394) in Table [3](#page-7-1) also confirmed the effectiveness of the random effect model used in this research to determine the lithium-ion battery charge decay. The error level obtained in this study is comparable to that obtained for the same battery using combinational Gaussian process functional regression [\[8\]](#page-11-13), Gaussian Hermite particle filter [\[2\]](#page-11-12), and improved particle and Kalman filters with particle swarm optimization [\[4\]](#page-11-9).

Batteries 2017, 3, 32 9 of 14

#### 3.3. Weibull Distribution Function Estimation of the Battery State-of-Health (SOH)

To estimate the battery State-of-Health (SOH) at the failure threshold, which corresponds to 70% End-of-Life (EOL), the random effect model was used to estimate the charge capacities, and times to reach the EOL at 1.4 Ah (Figure 3).

<span id="page-8-0"></span>![](_page_8_Figure_3.jpeg)

**Figure 3.** Experimental data of the lithium-ion batteries and estimated future charge capacity decay to 70% End-of-Life (EOL) failure threshold- Battery No. (a) B0029, (b) B0030, (c) B0031 and (d) B0032.

The charging cycles corresponding to the charge capacities of the battery from the initial charge cycle to the EOL charge cycle at 70% EOL failure threshold were used for computation of the cycles (equivalent time) to failure and the state-of-health of the batteries, based on the probability density function (w(t)) and cumulative density function (W(t)) of Weibull distribution, as per Equation (17). Note here that t refers to the time equivalent of the number of "remaining" cycles to failure of the battery unit.

$$\begin{cases} w(t) = \left(\frac{\rho}{\mu}\right) \left(\frac{t}{\mu}\right)^{\rho-1} exp\left(-\left(\frac{t}{\mu}\right)^{\rho}\right) \rho, \mu > 0 \\ W(t) = 1 - exp\left(-\left(\frac{t}{\mu}\right)^{\rho}\right) \rho, \mu > 0 \\ 0 \text{ otherwise} \end{cases}$$
(17)

The values of  $\rho$  and  $\mu$ , which represent the shape parameter and characteristic life (scale parameter) can be obtained by using double logarithmic transformation of the cumulative density function as per Equation (18). Since Equation (18) is a linear function, using median ranking, mean ranking, or symmetrical cumulative density function, we may extract the parametric values of the Weibull distribution, which is a very standard textbook exercise [36].

Batteries 2017, 3, 32 10 of 14

$$\log[-\log[1 - W(t)]] = \rho\log(t) - \rho\log(\mu) \tag{18}$$

<span id="page-9-0"></span>The goodness of fit of the Weibull distribution was estimated using the coefficient of determination ( $R^2$ ), which was obtained for all the four battery data sets. The value of  $R^2$  ranged from 0.9846–0.9852 indicated a good correlation between the random effect model data (battery charging times to 70% EOL—Figure 3) and the Weibull distribution function fitting. Figure 4 plots the "cycles to failure" data of one of the batteries investigated (B0029). The other Weibull plots were omitted here for redundancy sake.

![](_page_9_Figure_3.jpeg)

**Figure 4.** Goodness of fit test of Weibull distribution function fit to the remaining cycles to failure data for lithium-ion battery (B0029) considering the charge capacity decay threshold of 70% EOL. F(t) is a function that represents the median ranking of the age of the battery at various charge capacities.

The parametric values of the Weibull distribution function were used for the SOH estimation, according to Equation (19), which is basically the reliability function for the Weibull distribution.

$$SOH = exp\left(-\left(\frac{t}{\mu}\right)^{\rho}\right) \tag{19}$$

The SOH of the batteries at 70% EOL threshold, as shown in Figure 5 for the four batteries, indicates the characteristic life of the batteries i.e., the time that they will take to lose 63.2% of the lifecycle for EOL failure threshold of 70%. The fact that the shape parameters of the batteries are all larger than unity ( $\rho > 1$ ) is an indication of a charge decay related failure that generally increases in occurrence probability with time of usage of the battery, which is a "wear-out" condition that is common for Li-ion batteries, as also shown by other researchers [38,39]. The information in this figure is a vital tool for estimating the remaining useful life of the battery at any given time during its lifecycle for effective prior planning and decision making on the utilization of assets powered by these charging units.

The probability density function plots (Figure 6) show that the variance of the batteries with shorter lifecycle durations is smaller than those with longer lifecycle durations. It can also be deduced from the figure that the rate of charge capacity decay is expected to be higher as the age of the battery increases [11,39], due to problems associated with lithium corrosion, surface area degradation of the electrodes and local lithium plating that results in a faded power output [38]. This could be a plausible physical explanation to the observed variances where wider tails are evident at higher exposure times.

<span id="page-10-0"></span>Batteries 2017, 3, 32

![](_page_10_Figure_1.jpeg)

<span id="page-10-1"></span>**Figure 5.** State-of-Health of the four lithium-ion batteries at 70% EOL failure threshold where  $\mu$  represents the characteristic life and  $\rho$  represents the shape factor of the batteries.

![](_page_10_Figure_3.jpeg)

**Figure 6.** Probability density function plot for the four lithium-ion battery data sets with a failure threshold of 70% of maximum charge capacity.

#### 4. Conclusions of the Study

Understanding the influence of uncertainties in lithium-ion battery charge decay is vital for prognosis and remaining useful life estimation. This study used the random effect model that comprised of fixed and random effect parametric values of lithium-ion batteries, to estimate the future battery lifecycle and predict the State-of-Health (SOH) at 70% End-of-Life (EOL) failure threshold. After determining the parameters of this nonlinear mixed effect degradation model using the Maximum Likelihood Estimation (MLE) and Stochastic Approximation Expectation and Maximization (SAEM) algorithm, the predicted results were compared with NASA's experimental results on four chosen lithium-ion batteries that were tested at 43 °C using charging, discharging, and impedance profiles.

The results of the predicted battery charge capacity were found to vary from the experimental results by less than 2% on average. The State-of-Health (SOH) of the batteries were also estimated

*Batteries* **2017**, *3*, 32 12 of 14

considering the Weibull distribution function, which showed good predictive power, assuming 70% of EOL as the user defined failure threshold. The findings revealed that the battery charge capacity decay rate tends to increase with aging of the batteries due to problems that can be attributed to retarded electrode functionalities, lithium corrosion, and reduced reaction surface area, which impairs the functionalities of the electrodes and the electrolytes and impedes Li-ion diffusion through the electrolytes. Hence, there is a clear need to incorporate uncertainties in battery charge capacity decay modeling to enhance the robustness of prognostic estimates of remaining useful life in the future for mission critical applications.

**Acknowledgments:** This work is jointly funded by the SUTD-ZJU Collaboration Research Grant No. ZJURP1500103, Temasek Seed Grant No. IGDSS1604021 and the SUTD Start-Up Research Grant No. SREP15108.

**Author Contributions:** The original idea was conceived by Ossai, C.I, Nagarajan Raghavan helped to modify the ideas, and the preparation of the paper was done by both authors.

**Conflicts of Interest:** The authors do not have any conflict of interest.

## **References**

- <span id="page-11-0"></span>1. Liu, D.; Wang, H.; Peng, Y.; Xie, W.; Liao, H. Satellite lithium-ion battery remaining cycle life prediction with novel indirect health indicator extraction. *Energies* **2013**, *6*, 3654–3668. [\[CrossRef\]](http://dx.doi.org/10.3390/en6083654)
- <span id="page-11-12"></span>2. Hu, C.; Jain, G.; Tamirisa, P.; Gorka, T. Method for estimating capacity and predicting remaining useful life of lithium-ion battery. *Appl. Energy* **2014**, *126*, 182–189. [\[CrossRef\]](http://dx.doi.org/10.1016/j.apenergy.2014.03.086)
- 3. Xing, Y.; Ma, E.W.; Tsui, K.L.; Pecht, M. An ensemble model for predicting the remaining useful performance of lithium-ion batteries. *Microelectron. Reliab.* **2013**, *53*, 811–820. [\[CrossRef\]](http://dx.doi.org/10.1016/j.microrel.2012.12.003)
- <span id="page-11-9"></span>4. Mo, B.; Yu, J.; Tang, D.; Liu, H. A remaining useful life prediction approach for lithium-ion batteries using Kalman filter and an improved particle filter. In Proceedings of the 2016 IEEE International Conference on Prognostics and Health Management (ICPHM), Ottawa, ON, Canada, 20–22 June 2016; pp. 1–5.
- <span id="page-11-4"></span>5. He, W.; Williard, N.; Osterman, M.; Pecht, M. Prognostics of lithium-ion batteries based on Dempster–Shafer theory and the Bayesian Monte Carlo method. *J. Power Sources* **2011**, *196*, 10314–10321. [\[CrossRef\]](http://dx.doi.org/10.1016/j.jpowsour.2011.08.040)
- <span id="page-11-11"></span>6. Nuhic, A.; Terzimehic, T.; Soczka-Guth, T.; Buchholz, M.; Dietmayer, K. Health diagnosis and remaining useful life prognostics of lithium-ion batteries using data-driven methods. *J. Power Sources* **2013**, *239*, 680–688. [\[CrossRef\]](http://dx.doi.org/10.1016/j.jpowsour.2012.11.146)
- 7. Wang, D.; Miao, Q.; Pecht, M. Prognostics of lithium-ion batteries based on relevance vectors and a conditional three-parameter capacity degradation model. *J. Power Sources* **2013**, *239*, 253–264. [\[CrossRef\]](http://dx.doi.org/10.1016/j.jpowsour.2013.03.129)
- <span id="page-11-13"></span>8. Liu, D.; Pang, J.; Zhou, J.; Peng, Y.; Pecht, M. Prognostics for state of health estimation of lithium-ion batteries based on combination Gaussian process functional regression. *Microelectron. Reliab.* **2013**, *53*, 832–839. [\[CrossRef\]](http://dx.doi.org/10.1016/j.microrel.2013.03.010)
- <span id="page-11-1"></span>9. Orchard, M.E.; Hevia-Koch, P.; Zhang, B.; Tang, L. Risk measures for particle-filtering-based state-of-charge prognosis in lithium-ion batteries. *IEEE Trans. Ind. Electron.* **2013**, *60*, 5260–5269. [\[CrossRef\]](http://dx.doi.org/10.1109/TIE.2012.2224079)
- <span id="page-11-2"></span>10. Zhang, J.; Lee, J. A review on prognostics and health monitoring of Li-ion battery. *J. Power Sources* **2011**, *196*, 6007–6014. [\[CrossRef\]](http://dx.doi.org/10.1016/j.jpowsour.2011.03.101)
- <span id="page-11-3"></span>11. Broussely, M.; Biensan, P.; Bonhomme, F.; Blanchard, P.; Herreyre, S.; Nechev, K.; Staniewicz, R.J. Main aging mechanisms in Li ion batteries. *J. Power Sources* **2005**, *146*, 90–96. [\[CrossRef\]](http://dx.doi.org/10.1016/j.jpowsour.2005.03.172)
- <span id="page-11-5"></span>12. Scrosati, B.; Hassoun, J.; Sun, Y.K. Lithium-ion batteries. A look into the future. *Energy Environ. Sci.* **2011**, *4*, 3287–3295. [\[CrossRef\]](http://dx.doi.org/10.1039/c1ee01388b)
- <span id="page-11-6"></span>13. Hu, C.; Youn, B.D.; Chung, J. A multiscale framework with extended Kalman filter for lithium-ion battery SOC and capacity estimation. *Appl. Energy* **2012**, *92*, 694–704. [\[CrossRef\]](http://dx.doi.org/10.1016/j.apenergy.2011.08.002)
- <span id="page-11-7"></span>14. Wolfinger, R.D.; Lin, X. Two Taylor-series approximation methods for nonlinear mixed models. *Comput. Stat. Data Anal.* **1997**, *25*, 465–490. [\[CrossRef\]](http://dx.doi.org/10.1016/S0167-9473(97)00012-1)
- <span id="page-11-8"></span>15. Davidian, M. Nonlinear mixed effects models. In *International Encyclopedia of Statistical Science*; Springer: Berlin, Germany, 2011; pp. 947–950.
- <span id="page-11-10"></span>16. Sun, F.; Hu, X.; Zou, Y.; Li, S. Adaptive unscented Kalman filtering for state of charge estimation of a lithium-ion battery for electric vehicles. *Energy* **2011**, *36*, 3531–3540. [\[CrossRef\]](http://dx.doi.org/10.1016/j.energy.2011.03.059)

*Batteries* **2017**, *3*, 32 13 of 14

<span id="page-12-7"></span>17. He, H.; Xiong, R.; Zhang, X.; Sun, F.; Fan, J. State-of-charge estimation of the lithium-ion battery using an adaptive extended Kalman filter based on an improved Thevenin model. *IEEE Trans. Veh. Technol.* **2011**, *60*, 1461–1469.

- 18. Saha, B.; Goebel, K. Modeling Li-ion battery capacity depletion in a particle filtering framework. In Proceedings of the Annual Conference of the Prognostics and Health Management Society, San Diego, CA, 27 September–1 October 2009; pp. 2909–2924.
- <span id="page-12-0"></span>19. Dalal, M.; Ma, J.; He, D. Lithium-ion battery life prognostic health management system using particle filtering framework. *Proc. Inst. Mech. Eng. Part O J. Risk Reliab.* **2011**, *225*, 81–90. [\[CrossRef\]](http://dx.doi.org/10.1177/1748006XJRR342)
- <span id="page-12-1"></span>20. Miao, Q.; Xie, L.; Cui, H.; Liang, W.; Pecht, M. Remaining useful life prediction of lithium-ion battery with unscented particle filter technique. *Microelectron. Reliab.* **2013**, *53*, 805–810. [\[CrossRef\]](http://dx.doi.org/10.1016/j.microrel.2012.12.004)
- 21. Liu, J.; Saxena, A.; Goebel, K.; Saha, B.; Wang, W. *An Adaptive Recurrent Neural Network for Remaining Useful Life Prediction of Lithium-Ion Batteries*; National Aeronautics and Space Administration Moffett Field CA Ames Research Center: Mountain View, CA, USA, 2010.
- <span id="page-12-2"></span>22. Hu, X.; Li, S.E.; Yang, Y. Advanced machine learning approach for lithium-ion battery state estimation in electric vehicles. *IEEE Trans. Transp. Electr.* **2016**, *2*, 140–149. [\[CrossRef\]](http://dx.doi.org/10.1109/TTE.2015.2512237)
- <span id="page-12-3"></span>23. Tang, S.; Yu, C.; Wang, X.; Guo, X.; Si, X. Remaining useful life prediction of lithium-ion batteries based on the wiener process with measurement error. *Energies* **2014**, *7*, 520–547. [\[CrossRef\]](http://dx.doi.org/10.3390/en7020520)
- <span id="page-12-4"></span>24. Ng, S.S.; Xing, Y.; Tsui, K.L. A naive Bayes model for robust remaining useful life prediction of lithium-ion battery. *Appl. Energy* **2014**, *118*, 114–123. [\[CrossRef\]](http://dx.doi.org/10.1016/j.apenergy.2013.12.020)
- <span id="page-12-5"></span>25. Shim, J.; Kostecki, R.; Richardson, T.; Song, X.; Striebel, K.A. Electrochemical analysis for cycle performance and capacity fading of a lithium-ion battery cycled at elevated temperature. *J. Power Sources* **2002**, *112*, 222–230. [\[CrossRef\]](http://dx.doi.org/10.1016/S0378-7753(02)00363-4)
- <span id="page-12-6"></span>26. Harris, S.J.; Harris, D.J.; Li, C. Failure statistics for commercial lithium ion batteries: A study of 24 pouch cells. *J. Power Sources* **2017**, *342*, 589–597. [\[CrossRef\]](http://dx.doi.org/10.1016/j.jpowsour.2016.12.083)
- <span id="page-12-8"></span>27. Andre, D.; Appel, C.; Soczka-Guth, T.; Sauer, D.U. Advanced mathematical methods of SOC and SOH estimation for lithium-ion batteries. *J. Power Sources* **2013**, *224*, 20–27. [\[CrossRef\]](http://dx.doi.org/10.1016/j.jpowsour.2012.10.001)
- <span id="page-12-9"></span>28. Xing, Y.; He, W.; Pecht, M.; Tsui, K.L. State of charge estimation of lithium-ion batteries using the open-circuit voltage at various ambient temperatures. *Appl. Energy* **2014**, *113*, 106–115. [\[CrossRef\]](http://dx.doi.org/10.1016/j.apenergy.2013.07.008)
- <span id="page-12-10"></span>29. Rufus, F.; Lee, S.; Thakker, A. Health monitoring algorithms for space application batteries. In Proceedings of the International Conference on Prognostics and Health Management (PHM 2008), Denver, CO, USA, 6–9 October 2008; pp. 1–8.
- 30. Syracuse, K.C.; Clark, W.D. A statistical approach to domain performance modeling for oxyhalide primary lithium batteries. In Proceedings of the Twelfth Annual Battery Conference on Applications and Advances, Long Beach, CA, USA, 14–17 January 1997; pp. 163–170.
- <span id="page-12-11"></span>31. Schuster, S.F.; Brand, M.J.; Berg, P.; Gleissenberger, M.; Jossen, A. Lithium-ion cell-to-cell variation during battery electric vehicle operation. *J. Power Sources* **2015**, *297*, 242–251. [\[CrossRef\]](http://dx.doi.org/10.1016/j.jpowsour.2015.08.001)
- <span id="page-12-12"></span>32. Saha, B.; Goebel, K. *Battery Data Set, NASA Ames Prognostics Data Repository*; NASA Ames Research Center: Moffett Field, CA, USA, 2007. Available online: <http://ti.arc.nasa.gov/project/prognostic-data-repository> (accessed on 16 July 2017).
- <span id="page-12-13"></span>33. Lindstrom, M.J.; Bates, D.M. Nonlinear mixed effects models for repeated measures data. *Biometrics* **1990**, *46*, 673–687. [\[CrossRef\]](http://dx.doi.org/10.2307/2532087) [\[PubMed\]](http://www.ncbi.nlm.nih.gov/pubmed/2242409)
- <span id="page-12-14"></span>34. Zhu, H.; Gu, M.; Peterson, B. Maximum likelihood from spatial random effects models via the stochastic approximation expectation maximization algorithm. *Stat. Comput.* **2007**, *17*, 163–177. [\[CrossRef\]](http://dx.doi.org/10.1007/s11222-006-9012-9)
- <span id="page-12-15"></span>35. Harter, H.L.; Moore, A.H. Maximum likelihood estimation of the parameters of Gamma and Weibull populations from complete and from censored samples. *Technometrics* **1965**, *7*, 639–643. [\[CrossRef\]](http://dx.doi.org/10.1080/00401706.1965.10490304)
- <span id="page-12-16"></span>36. Cohen, A.C. Maximum likelihood estimation in the Weibull distribution based on complete and on censored samples. *Technometrics* **1965**, *7*, 579–588. [\[CrossRef\]](http://dx.doi.org/10.1080/00401706.1965.10490300)
- <span id="page-12-17"></span>37. Kuhn, E.; Lavielle, M. Maximum likelihood estimation in nonlinear mixed effects models. *Comput. Stat. Data Anal.* **2005**, *49*, 1020–1038. [\[CrossRef\]](http://dx.doi.org/10.1016/j.csda.2004.07.002)
- <span id="page-12-18"></span>38. Arora, P.; White, R.E.; Doyle, M. Capacity fade mechanisms and side reactions in lithium-ion batteries. *J. Electrochem. Soc.* **1998**, *145*, 3647–3667. [\[CrossRef\]](http://dx.doi.org/10.1149/1.1838857)

*Batteries* **2017**, *3*, 32 14 of 14

<span id="page-13-0"></span>39. Daigle, M.; Kulkarni, C.S. End-of-discharge and End-of-life Prediction in Lithium-ion Batteries with Electrochemistry-based Aging Models. In Proceedings of the AIAA Infotech@ Aerospace, San Diego, CA, USA, 4–8 January 2016; p. 2132.

![](_page_13_Picture_2.jpeg)

© 2017 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license [\(http://creativecommons.org/licenses/by/4.0/\)](http://creativecommons.org/licenses/by/4.0/.).
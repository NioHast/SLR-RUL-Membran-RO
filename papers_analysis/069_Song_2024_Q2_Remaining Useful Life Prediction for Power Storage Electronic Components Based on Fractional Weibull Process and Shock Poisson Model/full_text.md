![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_1.jpeg)

Article

# Remaining Useful Life Prediction for Power Storage Electronic Components Based on Fractional Weibull Process and Shock Poisson Model

Wanqing Song <sup>1</sup>, Xianhua Yang <sup>1</sup>, Wujin Deng <sup>2</sup>,\*, Piercarlo Cattani <sup>3</sup> and Francesco Villecco <sup>4</sup>

- School of Electronic and Electrical Engineering, Minnan University of Science and Technology, Quanzhou 362700, China; swqls@126.com (W.S.); 18059214837@163.com (X.Y.)
- School of Electronic & Electrical Engineering, Shanghai University of Engineering Science, Shanghai 201620, China
- Department of Computer, Control and Management Engineering, University of Rome La Sapienza, Via Ariosto 25, 00185 Roma, Italy; cattani.1642354@studenti.uniroma1.it
- Department of Industrial Engineering, University of Salerno, Via Giovanni Paolo II 132, 84084 Fisciano, Italy; fvillecc@unisa.it
- \* Correspondence: dwj058@126.com

Abstract: For lithium-ion batteries and supercapacitors in hybrid power storage facilities, both steady degradation and random shock contribute to their failure. To this end, in this paper, we propose to introduce the degradation-threshold-shock (DTS) model for their remaining useful life (RUL) prediction. Non-homogeneous compound Poisson process (NHCP) is proposed to simulate the shock effect in the DTS model. Considering the long-range dependence and heavy-tailed characteristics of the degradation process, fractional Weibull process (fWp) is employed in the diffusion term of the stochastic degradation model. Furthermore, the drift and diffusion coefficients are constantly updated to describe the environmental interference. Prior to the model training, steady degradation and shock data must be separated, based on the three-sigma principle. Degradation data for the lithium-ion batteries (LIBs) and ultracapacitors are employed for model verification under different operation protocols in the power system. Recent deep learning models and stochastic process-based methods are utilized for model comparison, and the proposed model shows higher prediction accuracy.

**Keywords:** hybrid energy storage system; lithium-ion batteries; supercapacitor; remaining useful life prediction; fractional Weibull process; non-homogeneous compound Poisson process

# updates Citation: Song. W

check for

Citation: Song, W.; Yang, X.; Deng, W.; Cattani, P.; Villecco, F. Remaining Useful Life Prediction for Power Storage Electronic Components Based on Fractional Weibull Process and Shock Poisson Model. *Fractal Fract*. 2024, 8, 485. https://doi.org/ 10.3390/fractalfract8080485

Academic Editor: António Lopes

Received: 7 July 2024 Revised: 2 August 2024 Accepted: 13 August 2024 Published: 19 August 2024

![](_page_0_Picture_16.jpeg)

Copyright: © 2024 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https://creativecommons.org/licenses/by/4.0/).

### 1. Introduction

In the new energy power system, power storage facilities are developed to keep constant balance between energy generation and consumption by stabilizing the grid output and smoothing the electricity demand [1]. The traditional pumped-storage hydropower stations have a relatively slow response speed. Thus, a hybrid power storage system based on lithium-ion batteries (LIBs) and ultracapacitors has been proposed [2], which combines the high power density of ultracapacitor and the large storage capacity of LIBs. The electric failures of these components compromise the grid reliability, and thus, their remaining useful life (RUL) should be predicted to instruct the preventive maintenance [3,4].

Currently, the mainstream research methods are data-driven, which utilizes deep neural layers and stochastic processes to extract the degradation pattern [5]. Convolutional neural network (CNN) can effectively extract features from the degradation data. Thus, RUL prediction models based on CNN have been proposed for energy storage equipment such as LIBs and supercapacitors [6,7]. However, CNN is not suitable to model the temporal fluctuation. To this aim, researchers have proposed recurrent neural network for the RUL prediction [8,9]. In ref. [10], an RUL prediction model has been proposed for supercapacitors, based on empirical mode decomposition and gated recurrent unit

(EMD-GRU). The degradation features are extracted by the empirical mode decomposition algorithm and then modeled by recurrent neural cells. Deep learning models do not have stochastic representation. Thus, the versatility of the model is not satisfactory. Furthermore, deep neural networks are not interpretable. On the contrary, stochastic degradation models are formulated with stochastic modeling and Monte Carlo interpretation [11,12].

During normal operation, the equipment suffers from continuous material degradation. However, in the same time, the random shock also contributes to equipment failure [13]. These two different failure modes are independent from each other [14]. Currently, most stochastic degradation models only describe the continuous degradation trend and its fluctuation, while ignoring the random jumps. The degradation-threshold-shock (DTS) model considers the continuous degradation and shock at the same time [15]. In the DTS model, random shock is generally represented by the non-homogenous compound Poisson process (NHCP) [16,17]. Based on the DTS model, researchers have proposed RUL prediction models with random shock. A DTS-based RUL prediction model is proposed in ref. [18], and Brownian motion (BM) is used to model the continuous degradation trend (DTS-BM). The NHCP process is selected to construct the shock term.

In the power system operation, there exists two kinds of degradation patterns [19]. The first one is the steady degradation caused by the ordinary electric and thermal stress. The second one is the shock originated from unexpected power outage. Therefore, a DTS-based RUL prediction model should be used for the electric components in the power system.

During the equipment degradation process, the degradation rate is constantly changing due to the environmental noise. Thus, the drift coefficient should be updated [20]. In a real degradation scene, the degradation variation also changes due to environmental interference [21]. Therefore, the diffusion coefficient should also be updated randomly.

Electric component degradation often shows long-range dependence, which indicates strong temporal correlations. However, BM is Markovian. Fractional Brownian motion (FBM) is non-Markovian when the Hurst exponent resides in the interval of (0.5, 1) [22]. In ref. [23], FBM with an adaptive drift is proposed for the RUL prediction of LIBs (adaptive FBM). FBM has a Gaussian assumption, which contracts with the fact that the majority of the engineering degradation data are heavy-tailed. Considering this, without a shock representation, adaptive FBM can only describe the stochasticity of steady degradation.

Fractional Weibull process (fWp) is proposed in [24]. The heavy-tailed characteristics and long-range dependence of the fWp have been proven [25]. Therefore, the feature extraction ability of the fWp is better than BM and FBM. In this paper, we introduce the fWp to drive the stochastic degradation model with a shock term due to its fractal properties.

In summary, we can establish a comparative table for the current advance of the RUL prediction of energy storage electric components. Four metrics are considered: versatility, interpretability, feature extraction and fluctuation modeling. The comparison results can be found in Table 1.

|                | Versatility | Interpretability | Feature<br>Extraction | Degradation<br>Modeling |
|----------------|-------------|------------------|-----------------------|-------------------------|
|                |             | ,                | ,                     | ,                       |
| proposed       | $\sqrt{}$   | $\checkmark$     | $\sqrt{}$             | $\checkmark$            |
| CNN            | ×           | ×                | $\sqrt{}$             | X                       |
| <b>EMD-GRU</b> | ×           | ×                | $\sqrt{}$             | $\sqrt{}$               |
| DTS-BM         | $\sqrt{}$   | $\sqrt{}$        | ×                     | $\sqrt{}$               |
| adaptive FBM   | 1/          | 1/               | ×                     | ×                       |

<span id="page-1-0"></span>Table 1. Evaluation among the above-mentioned RUL prediction models.

There are three main contributions in this paper:

①: During the grid operation, there exists two independent processes of steady material degradation and shock pulse. Thus, this paper proposes the DTS model for the RUL prediction of power storage electronic components.

②: In the degradation process, environmental noise often deviates the degradation trend and the variation mode. In this paper, these phenomena are simulated by the updates of drift and diffusion coefficients.

③: Previous RUL prediction models do not focus on the long-range dependence and heavy-tailed characteristics. To this end, we introduce the fWp as the temporal variability term in the degradation model.

The remainder of this paper is arranged as such. The NHCP and adaptive fWp are introduced in Section 2. In Section 3, RUL prediction model for the power storage electric components is proposed based on the DTS model. In the case study, two different grid operation protocols are used to validate the proposed model.

#### <span id="page-2-0"></span>2. The Adaptive fWp and NHCP for Degradation Modeling with Shock Impacts

#### 2.1. NHCP for Shock Simulation in the Degradation Model

In ref. [18], researchers proposed a jump diffusion degradation model with time-varying random shock. The random shock is simulated with NHCP with increasing intensity. This assumption is based on the fact that as the machinery health deteriorates, the shock occurrence frequency also increases.

The jump diffusion degradation model is formulated in Equation (1) [18]:

$$X(t) = X(0) + \gamma \int_{0}^{t-1} \Phi(s) ds + \eta B(t) + \sum_{j=0}^{N(t)} \varepsilon_{j},$$
 (1)

where  $\gamma$  is the drift coefficient, and  $\eta$  is the diffusion coefficient.  $\Phi(t)$  is the drift function. Drift function  $\Phi(t)$  follows the Gaussian assumption, and its mean and variance are estimated from the increments of the steady degradation data. B(t) represents the BM, and N(t) is the non-homogeneous Poisson process with intensity function H(t).  $\varepsilon_j$  is Gaussian white noise, and its parameters can be estimated from the shock amplitudes. The initial value is zero.

The shock term  $\sum\limits_{j=0}^{N(t)} \varepsilon_j$  (also known as NHCP  $N_{\rm C}(t)$ ) is a combination of two independent

dent processes: non-homogeneous Poisson process and Gaussian white noise [26]. The non-homogeneous Poisson process is utilized to describe the random occurrence of sudden shocks, and the individual shock impact is modeled by Gaussian white noise. Thus, the NHCP can express the accumulated damage to the equipment health caused by unexpected and intermittent shocks.

Definition of non-homogeneous Poisson process is as follows:

A counting process  $\{N(t); t \ge 0\}$  is said to be a non-homogeneous Poisson process with an intensity function H(t), if the initial value is zero and the increments are independently distributed following Equation (2):

$$P(N(t+h) - N(t) = n) = \frac{(\int_{t}^{t+h} H(x)dx)^{n}}{n!} \exp\left\{-\int_{t}^{t+h} H(x)dx\right\},\tag{2}$$

where h is a preset time increment.

Then, we can represent the NHCP  $N_C(t)$  as the summation of independent Gaussian white noises, as shown in Equation (3):

$$N_{C}(t) = \sum_{j=1}^{N(t)} \varepsilon_{j}$$

$$= \varepsilon_{1} + \varepsilon_{2} + \ldots + \varepsilon_{N(t)}$$
(3)

Several exemplary simulation paths of the NHCP are provided in Figure 1.

<span id="page-3-0"></span>![](_page_3_Figure_1.jpeg)

Figure 1. Simulations of different NHCP.

#### 2.2. The fWp with an Adaptive Diffusion for the Modeling of Degradation Stochasticity

Since the real degradation data usually possess fractal characteristics, i.e., long-range dependence and heavy-tailed characteristics, we propose to use the fWp to describe the degradation variability [25]. The definition of fWp is strictly related to fractional Weibull distribution [27]:

$$f(x) = \frac{k}{\lambda} (1 - \delta) \left(\frac{x}{\lambda}\right)^{k-1} \exp\left\{-\left(\frac{x}{\lambda}\right)^{k}\right\},\tag{4}$$

where k is the shape parameter,  $\lambda$  is the scale parameter and  $\delta \in (0,1)$  is the fractal parameter. The physical meaning of the fractal parameter is the discarding rate of initial data for a better probabilistic fitting.

Therefore, the fractional Weibull distribution is viewed as a fractal generalization of the normal Weibull distribution, by the fractal parameter  $\delta$ . Setting the fractal parameter to zero, one can transform the fractional Weibull distribution to the Weibull distribution.

The probability density function (PDF) of fractional Weibull distribution with different fractal parameters is depicted in Figure 2. As we can see from Figure 2, the PDF shifts vertically as the fractal parameter decreases. In the shifting process, the best-fitting distribution can be established by discarding a fractal tiny portion of the original data.

<span id="page-3-1"></span>![](_page_3_Figure_9.jpeg)

Figure 2. Fractional Weibull distributions with different fractal parameters.

The stochastic process is said to be fWp if the following three conditions are met:

- ①: P(fWp(0) = 0) = 1.
- (2): The increments are stationary.
- ③: The increments are independently and identically distributed as fractional Weibull distribution.

In Figure 3, an iterative path of the fWp is demonstrated. In order to express the environmental impact to the degradation variability, an adaptive diffusion coefficient is attached to the fWp, as provided in Figure 4. The fWp with an adaptive diffusion is referred as adaptive fWp in this paper.

<span id="page-4-1"></span>![](_page_4_Figure_6.jpeg)

Figure 3. Simulated path for the fWp.

<span id="page-4-2"></span>![](_page_4_Figure_8.jpeg)

**Figure 4.** The fWp with an adaptive diffusion.

#### <span id="page-4-0"></span>3. RUL Prediction Model for the Power Storage Electric Components

#### 3.1. DTS Model Based on the Adaptive fWp and NHCP

Considering the fractal characteristics of the real degradation data, we propose to substitute the BM in Equation (1) with the fWp:

$$X(t) = X(0) + \gamma \int_{0}^{t-1} \Phi(s) ds + \eta f W p(t) + \sum_{j=0}^{N(t)} \varepsilon_{j},$$
 (5)

Equation (5) can be separated into a steady degradation process Y(t) and an NHCP shock term  $N_C(t)$ :

$$X(t) = Y(t) + N_{C}(t) = Y(t) + \sum_{j=1}^{N(t)} \varepsilon_{j}$$
(6)

The increment of Y(t) is calculated as

$$\Delta Y(t-1) = Y(t) - Y(t-1)$$

$$= \gamma \int_{t-2}^{t-1} \Phi(s)ds + \eta f W p(\Delta t), \tag{7}$$

where  $fWp(\Delta t) = fWp(t) - fWp(t-1)$ .

Therefore, the steady degradation process Y(t) can be calculated discretely as

$$Y(t) = Y(t-1) + \Delta Y(t-1) = Y(t-1) + \gamma_t \int_{t-2}^{t-1} \Phi(s) ds + \eta_t f W p(\Delta t),$$
(8)

In Equation (8), we further consider both the drift and diffusion coefficients to be Gaussian white noises, i.e.,  $\gamma_t \sim N(1, \sigma_\gamma^2)$  and  $\eta_t \sim N(1, \sigma_\eta^2)$ . The variances in drift coefficient and diffusion coefficient are estimated from the increments of steady degradation data and raw degradation data, respectively.

#### 3.2. Monte Carlo Simulation for the RUL Prediction

RUL prediction results based on stochastic degradation models are obtained with Monte Carlo simulation algorithm [28]. Mode value of the simulation results is viewed as the point prediction. For each of the degradation simulations, when the degradation path passes the predefined failure threshold (FT), we consider that a failure happened or the end of life (EOL) occurred. The mathematical expression is in Equation (9).

$$L(t) = \inf\{t : X(t) \ge w | X(t-1) < w\},\tag{9}$$

where *w* is the FT.

<span id="page-5-0"></span>Flowchart of the RUL prediction model is depicted in Figure 5.

![](_page_5_Figure_14.jpeg)

Figure 5. Flowchart of the proposed RUL prediction model.

Prior to parameter estimation, the steady degradation data and the shock data must be separated from the raw degradation data of power storage electric components. These two degradation components can be separated based on their changing amplitude and

occurrence probability. The steady degradation data are used to train the drift term, and the parameters in the shock term are estimated by the shock data.

To begin with the iteration loop, the fWp is generated for stochasticity modeling of the raw degradation data. Due to the environmental interference, the drift and diffusion coefficients should be considered as Gaussian random variables. NHCP with an ever-increasing intensity is employed to simulate the shock to the degradation of energy storage equipment caused by intermittent power interruption.

#### 3.3. Parameter Estimation

Shape parameter k and scale parameter  $\lambda$  of the fWp are estimated with maximum likelihood estimation approach. Maximum likelihood function of fractional Weibull distribution is

$$L(x|\lambda,k) = \prod_{i=1}^{n} \left[ (1-\delta) \left(\frac{k}{\lambda}\right) \left(\frac{x_i}{\lambda}\right)^{k-1} \exp\left\{ -\left(\frac{x_i}{\lambda}\right)^{k} \right\} \right]$$

$$= (1-\delta)^{n} \left(\frac{k^{n}}{\lambda^{n}}\right) \left(\frac{1}{\lambda}\right)^{n(k-1)} \prod_{i=1}^{n} x_i^{k-1} \exp\left\{ -\left(\frac{1}{\lambda}\right)^{k} \sum_{i=1}^{n} x_i^{k} \right\}$$
(10)

Take the logarithm of Equation (10):

$$\ln L(x|\lambda,k) = n\ln(1-\delta) + n\ln(\frac{k}{\lambda}) + n(k-1)\ln(\frac{1}{\lambda}) + (k-1)\sum_{i=1}^{n}\ln x_i - (\frac{1}{\lambda})^k \sum_{i=1}^{n} x_i^k$$
 (11)

Estimations of shape parameter k and scale parameter  $\lambda$  can be reached by the partial derivation of Equation (11).

A large fractal parameter  $\delta$  can achieve a better fitting accuracy, while compromising the initial statistical properties. Thus, the estimation method for the fractal parameter should consider both the fitting accuracy and the data integrity. Goodness of fitting (GoF) experiments should be used to estimate the value of fractal parameter  $\delta$ .

The physical meaning of the intensity function H(t) in the non-homogeneous Poisson process is the PDF of the average number of occurrences. We can express this relation mathematically in Equation (12).

$$E(N(t)) = \int_{0}^{t} H(s)ds \tag{12}$$

As the degradation process proceeds, the occurrence rate of the shock also increases. Thus, we need to define an increasing function of H(t). For simplicity, we choose the intensity function H(t) as

$$H(t) = \kappa t \tag{13}$$

The slope  $\kappa$  can be calculated with Equation (14):

$$S = \int_0^{t_*} \kappa t dt$$
  
=  $\frac{1}{2} \kappa (t_*)^2$  (14)

where  $t_*$  is the prediction length, and S is the total number of shocks that happened in this time area.

#### 4. Case Study

#### 4.1. Experimental Description

The degradation data of LiFePO<sub>4</sub>-type LIBs and Maxwell ultracapacitors in the case study were provided by University of Science and Technology, which contain voltage and

current values (negative for discharging and positive for charging) [29]. The datasets were achieved in room temperature and the sampling time was 1 s.

<span id="page-7-0"></span>The type of LIB was IFP-1665130-10 Ah (produced by Fujian Brother Electric CO., Ltd of China, Ningde, China), and the type of ultracapacitor was BCAP3000-P270 2.7 V/3.0 Wh (produced by Maxwell Technologies, Inc., Shanghai, China). The rated capacity for the LIBs was 10 Ah, and the normal capacitance for the ultracapacitor was 3000 F. The LIB pack was series-connected by four batteries. The LIBs and supercapacitors used in the experiments are depicted in Figure 6.

![](_page_7_Picture_3.jpeg)

**Figure 6.** LIBs and supercapacitors in the degradation experiment. (a) Tested LIBs; (b) tested supercapacitor.

The experimental setup of the hybrid power storage system is illustrated in Figure 7 [30]. Neware BTS-8000 (produced by the Shen Zhen Neware Technology Co. Ltd., Shenzhen, China) was used to provide programmable environment for experiments. PC 1 was the control port for Neware BTS-8000. The LIBs and supercapacitor were connected by the DC/DC converter module, which was controlled by the Neware BTS-8000 test platform. The two current sensors were used to measure the current fluctuation in the whole experimental platform. The battery management system (BMS) was used to monitor the health state of LIBs. The collected data were transferred to the controller area network (CAN) monitor and then sent to the PC 2 for record. The DC power supply was employed to support the BMS with stable voltage input.

<span id="page-7-1"></span>![](_page_7_Picture_6.jpeg)

Figure 7. Test platform of the hybrid power storage system.

#### 4.2. Degradation Data of the Energy Storage Components in Operational Conditions

The experiments were conducted in two types of operational protocols of the power system. One is called dynamic stress test (DST), and the other one is called urban dynamometer driving schedule (UDDS) [31,32].

DST is a widely used stress aging test for energy storage equipment. Compared with the accelerated thermal stress aging test, DST can simulate the dynamic variations in voltage and current caused by the normal disturbance of a power system, which makes the test results more reasonable. UDDS is a standardized charging and discharging for the electric vehicles in urban areas. The charging and discharging activities of electric vehicles can inject shock and voltage deviation to the power grid, which calls for the load smoothing ability of the energy storage components. Therefore, we also use the UDDS test for the model validation.

The degradation data for LIBs and supercapacitor in DST protocol are plotted in Figures 8 and 9, respectively. As for the raw degradation data under UDDS control, they are provided in Figures 10 and 11.

<span id="page-8-0"></span>![](_page_8_Figure_5.jpeg)

Figure 8. LIB degradation data under DST protocol.

<span id="page-8-1"></span>![](_page_8_Figure_7.jpeg)

Figure 9. Ultracapacitor degradation data under DST protocol.

<span id="page-9-0"></span>![](_page_9_Figure_1.jpeg)

Figure 10. LIB degradation data under UDDS protocol.

<span id="page-9-1"></span>![](_page_9_Figure_3.jpeg)

Figure 11. Supercapacitor degradation data under UDDS protocol.

#### 4.3. Feature Selection for Degradation Data under DST and UDDS Protocols

As we can see from Figures 8 and 10, the voltages of LIBs have an obvious dropping tendency. Notably, researchers have proposed that voltage can be considered a metric of state of health (SOH) [33]. Therefore, we choose the voltage as the health indicator for the LIBs.

In the power system, the maximum of tolerable terminal voltage deviation is 10%. Since the voltage drop is detrimental to the charging devices, we choose 95% of the maximum terminal voltage as FT, featuring the incipient failure phenomenon. The voltage degradations with FT notation for both protocols (normalized) are provided in Figure 12.

<span id="page-10-0"></span>![](_page_10_Figure_1.jpeg)

Figure 12. Voltage degradation and incipient failure identification for LIBs.

Capacitance is often used as the SOH for supercapacitors. In general, the supercapacitor should be replaced when the capacitance drops below 80% of the rated capacitance [34]. The capacitance of the supercapacitor can be calculated with Equation (15):

$$C = \frac{Q}{U} = \frac{\int\limits_{0}^{t} I(s)ds}{U} \tag{15}$$

The normalized capacitance degradation and the corresponding FT are demonstrated in Figures 13 and 14 for both protocols.

<span id="page-10-1"></span>![](_page_10_Figure_6.jpeg)

Figure 13. Capacitance degradation for the supercapacitor under DTS protocol.

<span id="page-11-0"></span>![](_page_11_Figure_1.jpeg)

Figure 14. Capacitance degradation for the supercapacitor under UDDS protocol.

#### 4.4. Fractal Characteristics of the Raw Degradation Data

For a hybrid energy storage system containing LIBs and supercapacitors, a complete maintenance must be scheduled when the less endurable component shows incipient failure tendencies. In the DST protocol, the supercapacitor and LIBs reach the FT in 1664 sec and 7469 s, separately. Thus, the supercapacitor is the vulnerable component and should be employed for model training. For the hybrid energy storage system under UDDS protocol, the supercapacitor and LIBs reach their EOL in 995 s and 313 s, individually. Therefore, degradation data of LIBs should be used for the RUL prediction experiment of UDDS protocol.

In order to ascertain the fractal characteristics of the raw degradation data, we need to estimate some parameters. To begin with, we conduct GoF experiments to evaluate the best fractal parameters [35]. Root mean squared error (RMSE) is chosen as the evaluation metric for the fitting. The fitting results are compiled in Table 2. Thus, for the DST and UDDS protocols, the fractal parameters are 0.02 and 0.04, respectively.

<span id="page-11-1"></span>

| Table 2. RMS | E values for the | estimation of fractal | parameters. |
|--------------|------------------|-----------------------|-------------|
|--------------|------------------|-----------------------|-------------|

|                      | $\delta = 0$ | $\delta = 0.02$ | $\delta = 0.04$ | $\delta = 0.06$ |
|----------------------|--------------|-----------------|-----------------|-----------------|
| supercapacitor (DST) | 6.1426       | 5.9624          | 6.0842          | 6.2581          |
| LIBs (UDDS)          | 5.6311       | 5.4763          | 5.2540          | 5.6514          |

Hurst exponent is the indicator of long-range dependence. If the Hurst value is between 0.5 and 1, then the time series is long-range dependent. Wavelet-variance approach is employed to calculate the Hurst exponents, since the raw degradation data are non-stationary [36]. Kurtosis value is utilized to measure the heavy-tailed characteristics of the stochastic time series. If the Kurtosis value is larger than three, then the time series has a heavy probability tail. The hurst values and kurtosis values of raw degradation data are compiled in Table 3. In Table 3, we can also find the scale and shape parameters, calculated by the wblfit function of MATLAB R2022b.

<span id="page-12-0"></span>

| <b>Table 3.</b> Statistical values for the raw degradation d | the raw degradation data. |
|--------------------------------------------------------------|---------------------------|
|--------------------------------------------------------------|---------------------------|

|                      | Hurst  | Kurtosis | Scale  | Shape   |
|----------------------|--------|----------|--------|---------|
| supercapacitor (DST) | 0.9522 | 11.7911  | 2.0041 | 38.5888 |
| LIBs (UDDS)          | 0.7375 | 6.8088   | 0.9490 | 55.7275 |

#### 4.5. Separation of Shock Data and Steady Degradation Data

The amplitude of the shock is larger than the steady degradation, and the shock occurrence is also scarcer. Therefore, the shock data and steady degradation data can be filtered apart based on the amplitude and probability.

In general, occurrences scatter around the expectation. According to the three-sigma principle, appropriately 68% of data reside in the area where the deviation to the expectation is smaller than the standard deviation (std). Thus, in this paper, we consider the occurrence in this area as steady degradation and outside this area as shock data. In order to use the three-sigma principle, we need to assume that the incremental degradation data are semi-Gaussian. As we can see from Figure 15, the incremental degradation data for the model validation are semi-symmetrical; thus, the semi-Gaussian assumption is valid.

<span id="page-12-1"></span>![](_page_12_Figure_6.jpeg)

Figure 15. Incremental degradation data.

After the separation of steady degradation and shock data, we can estimate the slope  $\kappa$  in the intensity function H(t). The estimation process is documented in Table 4.

<span id="page-12-2"></span>**Table 4.** Estimation results for the slope in the intensity function.

|                      | S   | $t_*$ | κ                       |
|----------------------|-----|-------|-------------------------|
| supercapacitor (DST) | 297 | 8079  | $9.1006 \times 10^{-6}$ |
| LIBs (UDDS)          | 912 | 4864  | $7.7097 \times 10^{-5}$ |

#### 4.6. Performance Evaluation for the Proposed Model

As discussed in the introduction, there are two major types of RUL prediction models, i.e., deep learning-based models and stochastic process-based models. In this section, we will conduct numerical RUL prediction experiments to properly evaluate our model with previous proposed methods in these two disciplines. RMSE, mean absolute error (MAE), score of accuracy (SOA) and std are selected as the evaluation metrics.

# 4.6.1. Experiment for the DTS Protocol

<span id="page-13-0"></span>In Figure 16, RUL prediction results for the supercapacitor are depicted for the DST protocol. Deep learning models such as LSTM and CNN are utilized as the compare set. Point prediction results are plotted in Figure 17. The values of the evaluation metrics are deposited in Table 5.

![](_page_13_Figure_3.jpeg)

<span id="page-13-1"></span>Figure 16. RUL prediction results for supercapacitor under DST protocol.

![](_page_13_Figure_5.jpeg)

Figure 17. Point prediction results for supercapacitors under DST protocol.

<span id="page-13-2"></span>Table 5. Evaluation metrics for supercapacitors under DST protocol.

|          | MAE    | RMSE   | SOA    | std    |
|----------|--------|--------|--------|--------|
| proposed | 6.748  | 7.216  | 0.8132 | 0.0324 |
| CNN      | 13.123 | 14.852 | 0.5784 | 0.1254 |
| EMD-GRU  | 10.478 | 12.769 | 0.7231 | 0.0876 |

# 4.6.2. Experiment for the UDDS Protocol

Degradation data of LIBs under UDDS protocol are utilized for the model comparison among different stochastic process-based RUL prediction models (see Figure 18). In Figure 19, the point prediction results are provided. The evaluation metrics for this batch of validation experiments can be found in Table 6.

<span id="page-14-0"></span>![](_page_14_Figure_3.jpeg)

Figure 18. RUL prediction results for LIBs under UDDS protocol.

<span id="page-14-1"></span>![](_page_14_Figure_5.jpeg)

Figure 19. Point prediction results for LIBs under UDDS protocol.

<span id="page-14-2"></span>**Table 6.** Evaluation metrics for LIBs under UDDS protocol.

|              | MAE    | RMSE   | SOA    | std    |
|--------------|--------|--------|--------|--------|
| proposed     | 7.053  | 8.421  | 0.7968 | 0.0423 |
| DTS-BM       | 12.949 | 13.847 | 0.6125 | 0.1143 |
| adaptive FBM | 13.792 | 14.639 | 0.5263 | 0.1420 |

*Fractal Fract.* **2024**, *8*, 485 16 of 18

# *4.7. Discussion*

As elaborated in the introduction, steady degradation and shock impact both lead to the failure of power storage electric components. Therefore, shock term must be added into the degradation model. The RUL prediction based on adaptive FBM does not have a shock representation, and thus, the prediction results are not satisfactory. CNN also cannot deal with complex degradation modeling, which undermines its prediction accuracy.

Although DTS-BM model can track the degradation process with shock, it is both Markovian and Gaussian. The real degradation data usually possess fractal characteristics, which is in sharp contract to the DTS-BM model.

As for the EMD-GRU algorithm, the empirical mode decomposition is utilized for the feature extraction, and the degradation process with shock is modeled by the recurrent neural network. However, the model is not suitable to be used in the environment with plenty of environmental noise. Further, as a kind of deep learning model, the model is not interpretable.

Our model is established upon the shock simulation and fractal feature extraction, which are beneficial for prediction accuracy. With the parameter update based on random noise, the versatility of the model is enhanced. Furthermore, the proposed model has a firm Monte Carlo interpretation.

#### **5. Conclusions**

In this paper, a DTS-based RUL prediction model is proposed for the power storage electric components in a hybrid energy storage system, i.e., LIBs and supercapacitors. Two types of stochastic processes are proposed to construct the stochastic degradation model. NHCP is used to simulate the shock effect, which exists independently with the steady degradation process. Considering the fractal characteristics of the degradation process, the fWp is proposed to model the degradation variability due to its long-range dependence and heavy probability tail. The robustness of the stochastic degradation model is enhanced by the random update of drift and diffusion coefficients.

In the experiment section based on real degradation data, CNN, EMD-GRU, DTS-BM and adaptive FBM were chosen for model comparison. Prediction results show the superiority of our method.

Shock phenomena and fractal characteristics can also be found in the meshing process of mechanical gears. Fractional compound Poisson process can describe the shock impacts and the fractal characteristics at the same time [\[37\]](#page-17-18). In the future, we will establish a more advanced DTS model based on the fractional compound Poisson process.

**Author Contributions:** Conceptualization, W.S. and X.Y.; methodology, W.D.; software, P.C.; validation, F.V.; formal analysis, W.D.; investigation, X.Y.; resources, W.D.; data curation, F.V.; writing—original draft preparation, W.S.; writing—review and editing, X.Y. and W.D.; visualization, W.S.; supervision, W.S.; project administration, F.V.; funding acquisition, W.S. All authors have read and agreed to the published version of the manuscript.

**Funding:** This research was funded by the Major Project of Science and Technology of Quanzhou (No. 2022GZ8), the Technology Innovation Project of Minnan University of Science and Technology (Grant No. 23XTD113).

**Data Availability Statement:** Degradation data used in experiment can be downloaded at [http://dx.doi.org/10.1016/j.dib.2017.01.019,](http://dx.doi.org/10.1016/j.dib.2017.01.019) accessed on 6 July 2024.

**Conflicts of Interest:** The authors declare no conflicts of interest.

# **Abbreviations**

LIBs lithium-ion batteries RUL remaining useful life

CNN convolutional neural network

*Fractal Fract.* **2024**, *8*, 485 17 of 18

empirical mode

EMD-GRUdecomposition-

gated recurrent unit

DTS degradation-threshold-shock

NHCP non-homogeneous compound Possion process

BM Brownian motion

FBM fractional Brownian motion fWp fractional Weibull process PDF probability density function

FT failure threshold EoL end of life

GoF goodness of fitting

BMS battery management system CAN controller area network DST dynamic stress test

UDDS urban dynamometer driving schedule

SOH state of health

RMSE root mean squared error std standard deviation MAE mean absolute error SOA score of accuracy

# **References**

<span id="page-16-0"></span>1. Koohi-Kamali, S.; Tyagi, V.V.; Rahim, N.A.; Panwar, N.L.; Mokhlis, H. Emergence of energy storage technologies as the solution for reliable operation of smart power systems: A review. *Renew. Sust. Energ. Rev.* **2013**, *25*, 135–165. [\[CrossRef\]](https://doi.org/10.1016/j.rser.2013.03.056)

- <span id="page-16-1"></span>2. Rezaei, H.; Abdollahi, S.E.; Abdollahi, S.; Filizadeh, S. Energy management strategies of battery-ultracapacitor hybrid storage systems for electric vehicles: Review, challenges, and future trends. *J. Energy Storage* **2022**, *53*, 105045. [\[CrossRef\]](https://doi.org/10.1016/j.est.2022.105045)
- <span id="page-16-2"></span>3. Song, W.Q.; Deng, W.J.; Cattani, P.; Qi, D.Y.; Yang, X.H.; Yao, X.Y.; Chen, D.D.; Yan, W.D.; Zio, E. On the prediction of power outage length based on linear multifractional Lévy stable motion. *Pattern Recogn. Lett.* **2024**, *181*, 120–125. [\[CrossRef\]](https://doi.org/10.1016/j.patrec.2024.03.013)
- <span id="page-16-3"></span>4. Enrico, Z. Prognostics and Health Management (PHM): Where are we and where do we (need to) go in theory and practice. *Reliab. Eng. Syst. Saf.* **2021**, *218*, 108119. [\[CrossRef\]](https://doi.org/10.1016/j.ress.2021.108119)
- <span id="page-16-4"></span>5. Lei, Y.G.; Li, N.P.; Guo, L.; Li, N.B.; Yan, T.; Lin, J. Machinery health prognostics: A systematic review from data acquisition to RUL prediction. *Mech. Syst. Signal Process.* **2018**, *104*, 799–834. [\[CrossRef\]](https://doi.org/10.1016/j.ymssp.2017.11.016)
- <span id="page-16-5"></span>6. Zhou, B.T.; Cheng, C.; Ma, G.J.; Zhang, Y. Remaining Useful Life Prediction of Lithium-ion Battery based on Attention Mechanism with Positional Encoding. *IOP Conf. Ser Mater. Sci. Eng.* **2020**, *895*, 012006. [\[CrossRef\]](https://doi.org/10.1088/1757-899X/895/1/012006)
- <span id="page-16-6"></span>7. Wang, C.X.; Xiong, R.; Tian, J.P.; Lu, J.H.; Zhang, C.M. Rapid ultracapacitor life prediction with a convolutional neural network. *Appl. Energy* **2022**, *305*, 117819. [\[CrossRef\]](https://doi.org/10.1016/j.apenergy.2021.117819)
- <span id="page-16-7"></span>8. Zhang, Y.; Xiong, R.; He, H.; Pecht, M.G. Long Short-Term Memory Recurrent Neural Network for Remaining Useful Life Prediction of Lithium-Ion Batteries. *IEEE Trans. Veh. Technol.* **2018**, *67*, 5695–5705. [\[CrossRef\]](https://doi.org/10.1109/TVT.2018.2805189)
- <span id="page-16-8"></span>9. Zhou, Y.T.; Huang, Y.N.; Pang, J.B.; Wang, K. Remaining useful life prediction for supercapacitor based on long short-term memory neural network. *J. Energy Storage* **2019**, *440*, 227149. [\[CrossRef\]](https://doi.org/10.1016/j.jpowsour.2019.227149)
- <span id="page-16-9"></span>10. Guo, F.; Lv, H.T.; Wu, X.W.; Yuan, X.H.; Liu, L.L.; Ye, J.L.; Wang, T.; Fu, L.J.; Wu, Y.P. A machine learning method for prediction of remaining useful life of supercapacitors with multi-stage modification. *J. Energy Storage* **2023**, *73*, 109160. [\[CrossRef\]](https://doi.org/10.1016/j.est.2023.109160)
- <span id="page-16-10"></span>11. Zhang, Z.X.; Si, X.S.; Hu, C.H.; Lei, Y.G. Degradation data analysis and remaining useful life estimation: A review on Wienerprocess-based methods. *Eur. J. Oper. Res.* **2018**, *271*, 775–796. [\[CrossRef\]](https://doi.org/10.1016/j.ejor.2018.02.033)
- <span id="page-16-11"></span>12. Dong, G.; Chen, Z.; Wei, J.; Ling, Q. Battery Health Prognosis Using Brownian Motion Modeling and Particle Filtering. *IEEE Trans. Ind. Electron.* **2018**, *65*, 8646–8655. [\[CrossRef\]](https://doi.org/10.1109/TIE.2018.2813964)
- <span id="page-16-12"></span>13. Wang, P.; Gao, R.X.; Woyczynski, W.A. Lévy Process-Based Stochastic Modeling for Machine Performance Degradation Prognosis. *IEEE Trans. Ind. Electron.* **2021**, *68*, 12760–12770. [\[CrossRef\]](https://doi.org/10.1109/TIE.2020.3047037)
- <span id="page-16-13"></span>14. Huang, W.; Askin, R.G. Reliability analysis of electronic devices with multiple competing failure modes involving performance aging degradation. *Qual. Reliab. Eng. Int.* **2003**, *19*, 241–254. [\[CrossRef\]](https://doi.org/10.1002/qre.524)
- <span id="page-16-14"></span>15. Lemoine, A.J.; Wenour, M.L. On Failure Modeling. *Nav. Res. Log.* **2021**, *32*, 497–508. [\[CrossRef\]](https://doi.org/10.1002/nav.3800320312)
- <span id="page-16-15"></span>16. Wang, Z.L.; Huang, H.Z.; Li, Y.F.; Xiao, N.C. An Approach to Reliability Assessment Under Degradation and Shock Process. *IEEE Trans. Reliab.* **2011**, *60*, 852–863. [\[CrossRef\]](https://doi.org/10.1109/TR.2011.2170254)
- <span id="page-16-16"></span>17. Klutku, G.A.; Yang, Y.J. The availability of inspected systems subject to shocks and graceful degradation. *IEEE Trans. Reliab.* **2002**, *51*, 371–374. [\[CrossRef\]](https://doi.org/10.1109/TR.2002.802891)
- <span id="page-16-17"></span>18. Zhang, J.X.; Hu, C.H.; He, X.; Si, X.S.; Liu, Y.; Zhou, D.H. Lifetime prognostics for deteriorating systems with time-varying random jumps. *Reliab. Eng. Syst. Saf.* **2017**, *167*, 338–350. [\[CrossRef\]](https://doi.org/10.1016/j.ress.2017.05.047)

*Fractal Fract.* **2024**, *8*, 485 18 of 18

<span id="page-17-0"></span>19. Wang, Y.P.; Pham, H. Imperfect preventive maintenance policies for two-process cumulative damage model of degradation and random shocks. *Int. J. Syst. Assur. Eng. Manag.* **2011**, *2*, 66–77. [\[CrossRef\]](https://doi.org/10.1007/s13198-011-0055-8)

- <span id="page-17-1"></span>20. Pang, Z.N.; Pei, H.; Li, T.M.; Zhang, J.X.; Hu, C.H.; Si, X.S. An Adaptive Prognostic Approach for Partially Observable Degrading Products With Random Shocks. *IEEE Sens. J.* **2021**, *21*, 17926–17946. [\[CrossRef\]](https://doi.org/10.1109/JSEN.2021.3082953)
- <span id="page-17-2"></span>21. Wang, H.; Ma, X.; Zhao, Y. An improved Wiener process model with adaptive drift and diffusion for online remaining useful life prediction. *Mech. Syst. Signal Process.* **2019**, *127*, 370–387. [\[CrossRef\]](https://doi.org/10.1016/j.ymssp.2019.03.019)
- <span id="page-17-3"></span>22. Zhang, H.; Chen, M.; Shang, J.; Yang, C.; Sun, Y. Stochastic process-based degradation modeling and RUL prediction: From Brownian motion to fractional Brownian motion. *Sci. China Inf. Sci.* **2021**, *64*, 171201. [\[CrossRef\]](https://doi.org/10.1007/s11432-020-3134-8)
- <span id="page-17-4"></span>23. Li, X.; Ma, Y. Remaining useful life prediction for lithium-ion battery using dynamic fractional brownian motion degradation model with long-term dependence. *J. Power Electron.* **2022**, *22*, 2069–2080. [\[CrossRef\]](https://doi.org/10.1007/s43236-022-00507-w)
- <span id="page-17-5"></span>24. Deng, W.J.; Song, W.Q.; Cattani, C.; Chen, J.X.; Chen, X.L. On the fractional Weibull process. *Front. Phys.* **2022**, *10*, 790791. [\[CrossRef\]](https://doi.org/10.3389/fphy.2022.790791)
- <span id="page-17-6"></span>25. Song, W.Q.; Chen, D.D.; Zio, E. Heavy Tail and Long-Range Dependence for Skewed Time Series Prediction Based on a Fractional Weibull Process. *Fractal Fract.* **2023**, *8*, 7. [\[CrossRef\]](https://doi.org/10.3390/fractalfract8010007)
- <span id="page-17-7"></span>26. Franciszek, G. Nonhomogeneous Poisson Process and Compound Poisson Process in the Modelling of Random Processes Related to Road Accidents. *J. KONES* **2019**, *26*, 39–46. [\[CrossRef\]](https://doi.org/10.2478/kones-2019-0005)
- <span id="page-17-8"></span>27. Yu, Z.W.; Tuzuner, A. Fractional Weibull wind speed modeling for wind power production estimation. In Proceedings of the International Conference on Sustainable Power Generation and Supply, Nanjing, China, 6–7 April 2009. [\[CrossRef\]](https://doi.org/10.1109/SUPERGEN.2009.5348198)
- <span id="page-17-9"></span>28. Deng, W.; Gao, Y.; Song, W.; Zio, E.; Li, G.; Liu, J.; Kudreyko, A. Adaptive Residual Useful Life Prediction for the Insulated-Gate Bipolar Transistors with Pulse-Width Modulation Based on Multiple Modes and Transfer Learning. *Fractal Fract.* **2023**, *7*, 614. [\[CrossRef\]](https://doi.org/10.3390/fractalfract7080614)
- <span id="page-17-10"></span>29. Wang, Y.J.; Liu, C.; Pan, R.; Chen, Z.H. Experimental data of lithium-ion battery and ultracapacitor under DST and UDDS profiles at room temperature. *Data Brief.* **2017**, *12*, 161–163. [\[CrossRef\]](https://doi.org/10.1016/j.dib.2017.01.019) [\[PubMed\]](https://www.ncbi.nlm.nih.gov/pubmed/28459088)
- <span id="page-17-11"></span>30. Wang, Y.J.; Liu, C.; Pan, R.; Chen, Z.H. Modeling and state-of-charge prediction of lithium-ion battery and ultracapacitor hybrids with a co-estimator. *Energy* **2017**, *121*, 739–750. [\[CrossRef\]](https://doi.org/10.1016/j.energy.2017.01.044)
- <span id="page-17-12"></span>31. Cai, M.; Chen, W.J.; Tan, X.J. Battery State-Of-Charge Estimation Based on a Dual Unscented Kalman Filter and Fractional Variable-Order Model. *Energies* **2017**, *10*, 1577. [\[CrossRef\]](https://doi.org/10.3390/en10101577)
- <span id="page-17-13"></span>32. Collins, K.E. Simulation of the Emission Impact of a Hybrid-Electric Vehicle. *Int. J. Eng. Technol. Sci.* **2013**, *1*, 251–259.
- <span id="page-17-14"></span>33. Yang, S.J.; Zhang, C.P.; Jiang, J.C.; Zhang, W.G.; Zhang, L.J.; Wang, Y.B. Review on state-of-health of lithium-ion batteries: Characterizations, estimations and applications. *J. Clean. Prod.* **2021**, *314*, 128015. [\[CrossRef\]](https://doi.org/10.1016/j.jclepro.2021.128015)
- <span id="page-17-15"></span>34. Lou, G.M.; Lin, W.W.; Huang, G.X.; Xiang, W. A two-stage online remaining useful life prediction framework for supercapacitors based on the fusion of deep learning network and state estimation algorithm. *Eng. Appl. Artif. Intel.* **2023**, *123*, 106399. [\[CrossRef\]](https://doi.org/10.1016/j.engappai.2023.106399)
- <span id="page-17-16"></span>35. Zheng, H.B.; Huang, W.F.; Zhao, J.H.; Liu, J.F.; Zhang, Y.Y.; Shi, Z.; Zhang, C.H. A novel falling model for wind speed probability distribution of wind farms. *Renew. Energ.* **2022**, *184*, 91–99. [\[CrossRef\]](https://doi.org/10.1016/j.renene.2021.11.073)
- <span id="page-17-17"></span>36. Paparoditis, E.; Politis, D.N. The asymptotic size and power of the augmented Dickey-Fuller test for a unit root. *Econom. Rev.* **2018**, *37*, 955–973. [\[CrossRef\]](https://doi.org/10.1080/00927872.2016.1178887)
- <span id="page-17-18"></span>37. Laskin, N. Fractional Poisson process. *Commun. Nonlinear Sci.* **2003**, *8*, 201–213. [\[CrossRef\]](https://doi.org/10.1016/S1007-5704(03)00037-6)

**Disclaimer/Publisher's Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.
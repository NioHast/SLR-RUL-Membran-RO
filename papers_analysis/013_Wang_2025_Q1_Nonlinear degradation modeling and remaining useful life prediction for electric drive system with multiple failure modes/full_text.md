# scientific reports

![](_page_0_Figure_2.jpeg)

#### **OPEN**

# Nonlinear degradation modeling and remaining useful life prediction for electric drive system with multiple failure modes

Zhen Wang<sup>1,2™</sup>, Yadong Li³, Shuishi Li³, Yandong Hou¹, Weimin Du³ & Lihui Zhao⁴™

Accurate modeling of performance degradation and dynamic prediction of remaining useful life (RUL) for electric driving system (EDS) with multiple failure modes are critical for reliability assessment and health management. This study presents an integrated framework that encompasses composite health indicator construction, nonlinear degradation modeling, and RUL prediction. The entropy weight method is used to integrate the damage contributions of different components under various failure modes, resulting in a composite health indicator for the EDS. A nonlinear degradation model construction method for the EDS is presented, with failure thresholds and inherent uncertainties determined through actual bench testing over the full life cycle. The model is further refined by incorporating the acceleration factor between the accelerated and user spectra. Additionally, a Bayesian parameter update method is proposed for RUL prediction and uncertainty quantification, users with varying degradation rates across different service cycles are analyzed. The case study demonstrates that after approximately 20% of the service life, the proposed method achieves prediction errors within 10%. As historical data accumulates, model parameter estimates stabilize, and the predicted RUL probability distribution becomes increasingly concentrated. Comparative experiments against Wiener and CNN-LSTM models further demonstrate the superior robustness and accuracy of the proposed method. This study provides specific references and technical support for the reliability assessment and intelligent operation and maintenance of complex systems.

**Keywords** Electric drive system, Remaining useful life prediction, Nonlinear degradation modeling, Composite health indicators, Bayesian updating

The electric drive system (EDS), as the core of new energy vehicles, is pivotal to the overall driving safety and operational reliability. As EDS continues to evolve toward higher power density, increased rotational speeds, elevated voltage platforms, and greater integration, the intensified load under multi-physical field coupling exacerbates performance degradation and fault occurrence, thereby constraining further improvements in the reliability of new energy vehicles<sup>1</sup>. Furthermore, the EDS comprises multiple components, including the motor, reducer, and controller, which are susceptible to various failure modes such as fatigue and aging<sup>2</sup>. Traditional reliability assessment methods, which rely on failure times and specific distributions, account for a single failure mode and are mainly applicable to steady-state operating conditions<sup>3</sup>. Under complex and dynamic real-world environments, the above approach fails to adequately capture the degradation behaviors and predict the remaining useful life (RUL) of EDS. Therefore, conducting research on EDS degradation modeling and RUL prediction is of paramount importance for enhancing driving safety and extending system longevity.

With the rapid advancement of prognostics and health management technology, real-time monitoring, diagnostics, and prediction of a system's health status and RUL enable effective assessment of safety and reliability under actual operating conditions<sup>4</sup>. Such capabilities facilitate enhanced product health management and optimized maintenance strategies. Extensive research on RUL prediction has been conducted by scholars

<sup>1</sup>School of Artificial Intelligence, Henan University, Zhengzhou 450046, Henan, China. <sup>2</sup>Base for Postdoctoral Innovation and Practice of Yuxin Electronic Technology Group Co., Ltd, Zhengzhou 450000, Henan, China. <sup>3</sup>Yuxin Electronic Technology Group Co., Ltd, Zhengzhou 450000, Henan, China. <sup>4</sup>School of Mechanical Engineering, University of Shanghai for Science and Technology, Shanghai 200093, China. <sup>⊠</sup>email: wangzhenares@yeah.net; Pheigoe@126.com

worldwide, primarily encompassing physics-based modeling, artificial intelligence-based methods, and statistical data-driven approaches<sup>5</sup>. Physics-based approaches require explicit knowledge of failure mechanisms and typically establish degradation models based on the physics of failure<sup>6</sup>. Representative models include the Paris law for fatigue crack propagation<sup>7</sup>, the Basquin equation for fatigue life prediction<sup>8</sup>, the Coffin-Manson equation for low-cycle fatigue life<sup>9</sup>, and the Arrhenius equation for aging life prediction<sup>10</sup>. For instance, Zhao<sup>11</sup> constructed a Paris-based degradation model using gear monitoring data and applied Bayesian updating to model parameter distributions, achieving accurate RUL prediction. Vega-Garita<sup>12</sup> provides an overview of the aging mechanisms in lithium-ion batteries and methods for lifetime prediction, while also exploring parameter control strategies to reduce aging rates and enhance the lifespan of battery packs. However, physics-based methods depend heavily on extensive real-world failure data, which is challenging to obtain during vehicle operation and incurs significant costs. In contrast, artificial intelligence-based RUL prediction methods eliminate the need for explicit degradation models<sup>13</sup>, leveraging machine learning algorithms to establish an end-to-end mapping from monitoring data to RUL<sup>14</sup>. Li<sup>15</sup> enhanced prediction performance by integrating knowledge-driven insights with a CNN-LSTM model. However, artificial intelligence-based approaches often neglect the underlying physical failure mechanisms, rendering the prediction process less interpretable, with model accuracy heavily reliant on the quantity and quality of training data.

Statistical data-driven approaches are primarily grounded in degradation modeling, employing prior parameter estimation and posterior distribution updates to derive the probability distribution function of the RUL<sup>16</sup>. A prerequisite for degradation modeling is the construction of health indicators (HIs) that characterize system performance degradation. Current HIs construction methods include physics-based health indicators (PHIs) and virtual health indicators (VHIs)<sup>17</sup>. PHIs are grounded in explicit failure mechanisms and reflect degradation features closely associated with failure processes, examples include direct physical quantities such as crack length and wear volume, as well as indirect quantities such as vibration and internal resistance. For instance, Feng<sup>18</sup> utilized crack length and depth to characterize the performance degradation of welded plates, while Xu<sup>19</sup> assessed wear in external gear pumps using parameters such as rotational speed, pressure, and flow. However, these physical quantities are difficult to obtain in large-scale real-world operations. In contrast, VHIs are constructed through data fusion techniques. Li<sup>20</sup> developed a virtual health indicator based on frequencydomain similarity and transfer learning, which effectively identified both the health states and degradation progression of bearings. Qin<sup>21</sup> generated an HI with evident degradation trends from multi-dimensional features of vibration signals by incorporating a variational autoencoder model. Nevertheless, a key challenge persists in the ambiguous correlation between VHIs and physical degradation patterns, which compromises RUL prediction accuracy. For establishing degradation models based on HIs, common empirical models include linear<sup>22</sup>, exponential<sup>23</sup>, and power-law models. Additionally, stochastic processes such as the Gamma process<sup>24</sup>, Inverse Gaussian process<sup>25</sup>, and Wiener process<sup>26</sup> are widely applied. The Gamma and Inverse Gaussian processes are suitable for modeling continuous monotonic degradation data<sup>27</sup>, whereas the Wiener process is better suited for non-monotonic degradation processes but assumes stable operating environments and constant degradation rates. For the subject of this study, degradation modeling must align with actual degradation patterns to ensure the precision and effectiveness of RUL predictions.

Previous studies typically assume that the exceedance of a single performance degradation indicator beyond its threshold leads to a single failure mode. For complex systems involving coupled multiple failure modes, researchers have integrated multiple degradation indicators into a composite health indicator as a system performance evaluation metric, establishing a unified failure threshold to guide life prediction and maintenance decision-making<sup>28</sup>. The failure that occurs when the fused hi exceeds the composite threshold is referred to as a fusion failure mode<sup>29</sup>. For instance, when the weighted fusion of multiple degradation indicators in a gas turbine exceeds the total failure threshold, the turbine is considered to have failed<sup>30</sup>. Ye<sup>31</sup> proposed a RUL prediction method based on parallel multi-attention and contrastive fusion across multi-source domains, capable of extracting composite fault features from the main reducer and validating the method's effectiveness using full life cycle vibration data. Zhang et al.<sup>32</sup> analyzed multiple performance indicators to classify different fault types and developed corresponding RUL prediction models. Under fusion failures, they introduced a weighting strategy to account for the contributions of different indicators to the overall system health state. Li et al.<sup>33</sup> further proposed a generalized cumulative degradation model for wind turbines, in which root mean square values of vibration signals and variations in rotational speed are used to characterize degradation processes. These studies provide valuable insights and references for constructing health indicators and modeling degradation in EDS.

Moreover, for complex systems exhibiting nonlinear degradation, the RUL prediction process is subject to various uncertainties, including measurement uncertainty in sample data, random uncertainty arising from individual differences, and parameter uncertainty in degradation modeling, all of which ultimately influence the prediction outcomes<sup>34,35</sup>. Niu<sup>36</sup> applied the Monte Carlo method, randomly sampling values from uncertain parameter estimation intervals, conducting multiple RUL prediction simulations, and adopting the average as the final predicted value. Zhang<sup>37</sup> leveraged prior knowledge from physical models alongside statistical patterns from empirical data to develop a random effects Inverse Gaussian process model for tools, employing Bayesian methods for estimating and updating unknown parameters, deriving the RUL probability density function, and quantifying prediction uncertainty. Therefore, a central focus of this study is to incorporate multiple failure modes in EDS to construct realistic health indicators, and enable RUL prediction with uncertainty quantification across diverse user scenarios. The main contributions of this study are as follows:

- (1) A novel method is proposed for constructing composite health indicators that integrates multidimensional damage contribution features of the EDS, with the slope of linear fitting utilized to characterize the variability in degradation rates across different users.
- (2) Through multi-prototype bench life testing, the degradation trajectories and inherent uncertainties of EDS are elucidated. By accounting for the differences in degradation rates between accelerated and unaccelerated

spectrum, nonlinear degradation trajectories are generated, and the corresponding degradation models are established.

(3) The expectation-maximization (EM) parameter estimation and Bayesian update methods are employed to predict the RUL and quantify uncertainty for EDS across various service stages, demonstrating applicability across diverse user scenarios.

This study primarily presents a nonlinear degradation modeling and RUL prediction method for complex systems with multiple failure modes. The rest of this study is organized as follows: Sect. "Composite health indicator construction" focuses on the construction of composite health indicators. Section "Nonlinear degradation modeling" details the nonlinear degradation modeling. Section "Model construction and degradation trajectory generation" discusses the RUL prediction model. Section "Parameter estimation with the EM algorithm" provides case studies and comparative analysis, and Sect. "Parameter updates based on bayesian theory" concludes the study. The overall research content and implementation framework are illustrated in Fig. 1. The research is divided into three main stages, each highlighted in a different color to clearly illustrate the processes of composite health indicator construction, nonlinear degradation modeling, and remaining useful life prediction for the electric drive system.

#### <span id="page-2-0"></span>Composite health indicator construction

HIs as representative parameters for evaluating the degradation state of systems or components, play a critical role in quantifying failure thresholds, monitoring service conditions, and supporting predictive maintenance. In complex systems with multiple components, the risk loads and failure mechanisms vary significantly among components under stochastic operating conditions. Therefore, constructing composite health indicators that effectively characterize the overall degradation state of complex systems is essential.

Consider a system comprising core components such as shafts, gears, bearings, stators, and rotors, which are subject to multiple failure modes, including fatigue failure of rotating mechanical components, aging of stator windings, and fatigue of rotor magnetic bridges. Lifetime analysis of these components can be performed based on their respective failure mechanisms<sup>38</sup>.

<span id="page-2-2"></span>For mechanical components like shafts and gears, the Basquin equation is used to establish the relationship between stress and fatigue life. Equation (1) illustrates the shear stress caused by the torque on the motor shaft<sup>39</sup>.

$$\tau = \frac{16T}{\pi D^3} \tag{1}$$

where  $\tau$  is shear stress, T is motor torque, D is the motor shaft section diameter.

For gear components in EDS, the contact fatigue life of tooth surface caused by contact stress  $\sigma_H$  and the bending fatigue life of tooth root generated by bending stress  $\sigma_F$  are mostly considered. The above stress calculation approach can be determined by referring to ISO 6336<sup>40</sup>. For the calculation of bearing life, the basic rating life  $L_{10}$  of the bearing can be obtained based on the Lundberg-Palmgren theory<sup>41</sup>, which can be denoted as:

<span id="page-2-1"></span>![](_page_2_Figure_11.jpeg)

Fig. 1. Flow chart of the proposed research content and implementation framework.

$$L_{10} = (\frac{C}{P})^{\frac{10}{3}} \tag{2}$$

where C is the basic dynamic load rating, P is the equivalent dynamic load. The calculation equation of equivalent dynamic load P is calculated as:

$$P = f_p(XF_r + YF_a) \tag{3}$$

where  $f_p$  is the load factor, X is the radial load factor, Y is the axial load factor,  $F_r$  is the radial force,  $F_a$  is the axial force.

To account for the risk of fatigue failure caused by significant centrifugal forces due to speed, the maximum stress of the bridge in the permanent magnet synchronous motor is calculated using the equivalent center of mass principle<sup>42</sup>, as follows:

$$\sigma_{\text{max}} = \alpha_{\sigma} R_0^2 \omega^2 \rho_{eg} \tag{4}$$

where  $\alpha_{\sigma}$  is stress concentration factor,  $R_0$  is rotor equivalent radius (m),  $\rho_{eq}$  is rotor equivalent density (kg/m^2),  $\omega$  is motor speed (rad/s).

The insulation aging failure of stator winding, which may occur during continuous high-temperature operation, can be addressed by using the Arrhenius equation to describe the aging life<sup>43</sup>.

$$ln L = \frac{E_a}{kT} - G$$
(5)

where L represents the average insulation life (in hours), T represents the temperature of the insulation material (in Kelvin), k represents the Boltzmann constant (in eV/K), and  $E_a$  and G represent parameters related to the insulation material.

Under stochastic user conditions, the number of load cycles experienced by each component can be determined using methods such as the rainflow cycle counting or the joint distribution counting methods<sup>44</sup>. Rainflow cycle counting is typically used to extract alternating stress cycles for shaft-like components, while the joint distribution counting is more suitable for rotating parts such as gears and bearings, as it considers the impact of rotational speed on the cycle count. Assuming the operational data is divided into n segments, the damage incurred by component j in segment i can be calculated using Palmgren-Miner rule as follows:

$$D_{ji} = \sum_{k=1}^{N_k} \frac{r_{i_k}}{N_{i_k}} \tag{6}$$

where  $N_k$  represents the number of stress levels,  $r_{i\_k}$  denotes the rainflow cycle counting or rotational rainflow counting for segment i at stress level k, and  $N_{i\_k}$  is the fatigue life at stress level k for segment i.

Assuming the failure threshold of component j over its full life cycle (e.g., 300,000 km) is  $\delta_j$ , the damage contribution  $d_{ji}$  for component j during operational segment i is defined as:

$$d_{ji} = D_{ji}/\delta_j \tag{7}$$

where i = 1, 2, ..., n, j = 1, 2, ..., m.

To evaluate the overall damage contribution of the system under different failure modes, the entropy weight method is introduced to determine the weights of various factors during information fusion. The entropy weight method assigns weights based on the inherent attributes of the original data<sup>45</sup>, using information entropy to represent the degree of dispersion of an indicator. A smaller entropy value indicates greater dispersion of the indicator and, consequently, more valuable information. Assuming the normalized damage contribution matrix under multiple failure modes is  $d_{ij}^z$ , the information entropy  $E_j$  for the j-th indicator is defined as:

$$E_{j} = -\frac{1}{\ln n} \sum_{i=1}^{n} p_{ji} \cdot \ln(p_{ji})$$
 (8)

$$p_{ji} = d_{ji}^z / \sum_{i=1}^n d_{ji}^z \tag{9}$$

where  $E_j \in [0, 1]$ . Since entropy values and weights are inversely related, the weight coefficient for each feature is defined as:

$$\omega_j = (1 - E_j) / \sum_{i=1}^m (1 - E_j)$$
(10)

In addressing the construction of degradation trajectory under coupled multiple failure modes, the entropy weight method is initially employed to fuse damage contribution metrics from multiple components, generating the composite health indicator and a linear degradation trajectory. Subsequently, this trajectory is refined based

on actual degradation patterns observed in bench testing, yielding a nonlinear composite health indicator for the electric drive system. Let  $x_{p\_i}$  represent the composite health indicator for the p-th  $(p=1,2,\cdots,U)$  user during the i-th operational segment. The damage contribution of component j for the p-th user in segment i is denoted as  $d_{pj}(i)$ , while the weight coefficient  $\omega_j$  reflects the proportional impact of the component j. The composite health indicator is expressed as:

$$x_{p_{\underline{i}}} = \mathbf{D}_p(i) \cdot \mathbf{W} = \sum_{j=1}^m d_{pj}(i) \cdot \omega_j$$
(11)

where  $\mathbf{D}_p(i) = [d_{p1}(i), d_{p2}(i), \cdots, d_{pm}(i)], \mathbf{D}_p(i) \in \mathbf{R}^{1 \times m}$  denotes the damage contribution vector of the m-th component for the p-th user, and  $\mathbf{W} = [\omega_1, \omega_2, \cdots, \omega_m]^\mathrm{T}, \mathbf{W} \in \mathbf{R}^{m \times 1}$  represents the vector of weight coefficients.

#### <span id="page-4-0"></span>Nonlinear degradation modeling

#### <span id="page-4-1"></span>Model construction and degradation trajectory generation

Assuming that the cumulative impact of operating condition cycles on system degradation is negligible, and that degradation accumulates linearly across service cycles, the linear equation characterizing the degradation state of user *p* is formulated as follows:

$$y_{p_{-i}} = k_p \cdot \sum_{i=1}^{n} x_{p_{-i}} + b_p \tag{12}$$

where  $k_p$  represents the linear degradation rate of different users.

For complex systems such as the electric drive system in NEVs, multiple failure modes with components emerge under the influence of multi-physical field loads such as mechanical stress, thermal stress, and electromagnetic stress. the interaction of these failure modes leads to a nonlinear degradation trend in the system. Since actual degradation trajectories over the full life cycle are difficult to obtain, researchers typically rely on bench accelerated durability tests to monitor vibration signal features that reflect the evolution of degradation states. However, a key challenge lies in the fact that degradation rates observed during accelerated testing are significantly higher than those experienced under normal user conditions. Therefore, developing a method to transfer the degradation patterns observed in experimental conditions to actual operational environments is critical for ensuring prediction accuracy.

Assuming that the RMS of vibration signals monitored during the full life cycle in bench tests follows an exponential distribution, the generalized exponential model is formulated as:

$$f_i = a \exp(b \cdot s_i) \tag{13}$$

where  $s_i (i = 1, 2, \dots, n)$  represents the RMS of the vibration signals, while a and b are fitting parameters.

To determine the fitting parameters a and b in the exponential model, the least squares method is applied. The objective function S is formulated to minimize the sum of squared residuals between the observed values and the predicted values. The parameters a and b are estimated using the following equation:

$$S = \min\left(\sum_{i=1}^{c} \left(f_i - ae^{bs_i}\right)^2\right) \tag{14}$$

$$b = \frac{c\sum_{i=1}^{c} s_i f_i - \sum_{i=1}^{c} s_i \sum_{i=1}^{c} f_i}{c\sum_{i=1}^{c} s_i^2 - (\sum_{i=1}^{c} s_i)}$$
(15)

$$a = \frac{1}{c} \left( \sum_{i=1}^{c} f_i - b \sum_{i=1}^{c} s_i \right)$$
 (16)

To address the heterogeneity in user operating conditions and empirical observations from bench testing regarding degradation patterns, we develop a nonlinear exponential function to formulate the system degradation trajectory:

$$f_{p-i} = a \exp(k_i \delta \cdot t) \cdot y_{p-i} + \varepsilon \tag{17}$$

where  $f_{p\_i}$  represents the composite degradation indicator, a represents the model's initial random parameter,  $k_i$  is the degradation slope in the linear model, which characterizes the variation in degradation rates across different users.  $\delta$ is the correction factor that represents the relationship between the degradation rate under experimental conditions and that under user conditions, and  $\varepsilon \sim N(0, \sigma^2)$  is the random noise in the degradation process.

To determine  $\delta$ , bench tests are performed under both accelerated durability conditions and non-accelerated user conditions, with vibration signals from the electric drive system monitored during the tests. These signals are

used to evaluate the acceleration factor m between the accelerated test spectrum and the user's non-accelerated spectrum. The degradation trajectories of the electric drive system under both accelerated and non-accelerated spectra are illustrated in Fig. 2.

<span id="page-5-2"></span>Assuming the degradation equation under the accelerated test spectrum is  $f_{\rm A}(t)$  and the degradation equation under the non-accelerated user spectrum is  $f_{\rm B}(t)$ , the acceleration factor and the coefficient  $\delta$ can be expressed as follows:

$$\begin{cases} \ln(f_{A}(t)) = \ln(a_{A}) + b_{A}t \\ \ln(f_{B}(t)) = \ln(a_{B}) + b_{B}t \\ \frac{\ln(f_{A}(t+\Delta)) - \ln(f_{A}(t))}{\ln(f_{B}(t+\Delta)) - \ln(f_{B}(t))} = \frac{b_{A}}{b_{B}} = m \\ \delta = b_{B} = b_{A}/m \end{cases}$$
(18)

Based on the nonlinear degradation trajectory, the user degradation model is constructed. Considering the inherent uncertainty introduced by the use uncertainty of different users and the performance difference of the prototype in the degradation process of the electric drive system, the exponential model is used to describe the cumulative process of the degradation state of the electric drive system. Assuming that the discrete time monitoring point is  $t_s$ ,  $s=1,2,\cdots,L$ , the degradation amount at time  $t_s$  can be described as:

$$Y(t_s) = \varphi + \theta \exp(\beta t_s + \varepsilon(t_s) - \frac{\sigma^2}{2})$$
(19)

where  $\varphi$  is the constant representing the intercept of the model,  $\theta$  and  $\beta$  are random parameters that determine the slope of the model and captures the variability in usage conditions and individual differences among users. It's assumed that  $\ln \theta$  follows a normal distribution with mean  $\mu_1$  and variance  $\sigma_1^2$ ,  $\ln \theta \sim N(\mu_1, \sigma_1^2), \beta \sim N(\mu_2, \sigma_2^2)$ . The  $\varepsilon(t_s)$  are the stochastic error terms which express inherent uncertainties due to monitoring errors on the degradation data from the test machine,  $\varepsilon(t_s) \sim N(0, \sigma^2)$  and  $\varepsilon(0) = 0$ . Assuming they are mutually independent and identically distributed,  $-\sigma^2/2$  is defined such that the expected value of the degradation state  $Y(t_s)$  equals  $E[Y(t_s)|\theta,\beta] = \varphi + \theta \exp(\beta t_s)$ .

$$F(t_s) = \ln(Y(t_s) - \varphi)$$

$$= \ln \theta - \frac{\sigma^2}{2} + \beta t_s + \varepsilon(t_s)$$

$$= \lambda + \beta t_s + \varepsilon(t_s)$$
(20)

where  $\lambda = \ln \theta - \sigma^2 / 2$ ,  $\lambda \sim N(\mu_1 - \sigma^2 / 2, \sigma_1^2)$ ,  $\mu_1' = \mu_1 - \sigma^2 / 2$ . such that  $\lambda$  follows a Gaussian distribution. When considering  $\varphi = 0$ , the degenerate quantity  $F(t_s) = \ln(Y(t_s))$ .

#### <span id="page-5-0"></span>Parameter Estimation with the EM algorithm

In nonlinear degradation models with unknown parameters  $\Theta = \{\mu'_1, \sigma_1^2, \mu_2, \sigma_2^2, \sigma^2\}$ , prior to updating the model parameters, it is essential to integrate prior distributions with historical monitoring data for parameter estimation, which subsequently updates the posterior distribution of the stochastic parameters. Considering the randomness of latent variables  $\lambda$  and  $\beta$  as historical data updates, the expectation-maximization (EM) algorithm is employed to estimate the parameter set  $\Theta^{46}$ . First, the expectation step computes the expected value using the current estimates of the latent variables. Next, the maximization step updates the parameter estimates by maximizing the complete log-likelihood function. Define the degradation indicator at time  $t_s$  as  $\mathbf{F}_{1:s} = \{F(t_1), F(t_2), \cdots, F(t_s)\}$ , with the estimated parameter is  $\Theta_s = \{\mu'_{1,s}, \sigma_{1,s}^2, \mu_{2,s}, \sigma_{2,s}^2, \sigma_s^2\}$ . after

<span id="page-5-1"></span>![](_page_5_Figure_11.jpeg)

Fig. 2. Schematic of degradation trajectories under accelerated and non-accelerated spectra.

the *n*-th iteration, the parameter estimate is represented as  $\hat{\Theta}_s^{(n)} = \{\hat{\mu}_{1,s}^{\prime(n)}, \hat{\sigma}_{1,s}^{2(n)}, \hat{\mu}_{2,s}^{(n)}, \hat{\sigma}_{2,s}^{2(n)}, \hat{\sigma}_s^{2(n)}\}$ . In the expectation step, the complete log-likelihood function can be expressed as:

$$L(\boldsymbol{\Theta}_{s}|\hat{\boldsymbol{\Theta}}_{s}^{(n)}) = E_{\lambda,\beta|F_{1:s},\hat{\boldsymbol{\Theta}}_{s}^{(n)}}[ln(\mathbf{F}_{1:s},\lambda,\beta|\boldsymbol{\Theta}_{s})]$$

$$= \ln p(\mathbf{F}_{1:s}|\lambda,\beta,\boldsymbol{\Theta}_{s}) + \ln p(\lambda,\beta|\boldsymbol{\Theta}_{s})$$

$$= -\frac{s+2}{2}\ln 2\pi^{2} - \frac{s}{2}\ln \sigma_{s}^{2} - \sum_{j=1}^{s} \frac{(F_{j} - \lambda - \beta t_{j})^{2}}{2\sigma_{s}^{2}}$$

$$-\frac{1}{2}\ln \sigma_{1,s}^{2} - \frac{1}{2}\ln \sigma_{2,s}^{2} - \frac{(\lambda - \mu_{1,s}')^{2}}{2\sigma_{1,s}^{2}} - \frac{(\beta - \mu_{2,s})^{2}}{2\sigma_{2,s}^{2}}$$
(21)

By maximizing the complete log-likelihood function, the estimated value after the (n + 1)-th iteration is obtained as follows:

$$\hat{\mathbf{\Theta}}_{s}^{(n+1)} = \operatorname{argmax} L(\mathbf{\Theta}_{s} | \hat{\mathbf{\Theta}}_{s}^{(n)})$$
(22)

<span id="page-6-1"></span>The first-order partial derivative with respect to parameter  $\Theta_s$  is calculated based on Eq. (23) as follows:

$$\frac{\partial L(\mathbf{\Theta}_s|\hat{\mathbf{\Theta}}_s^{(n)})}{\partial \mathbf{\Theta}_s} = 0 \tag{23}$$

The estimated result for parameter  $\hat{\Theta}_s^{(n+1)}$  after the (n+1)-th iteration is given by:

$$\hat{\sigma}_s^{2(n+1)} = \frac{1}{s} \sum_{j=1}^s \left( F_j^2 - 2F_j(\mu_{\lambda,s} + \mu_{\beta,s}) + \mu_{\lambda,s}^2 + \sigma_{\lambda,s}^2 + 2t_j(\rho_s \sigma_{\lambda,s} \sigma_{\beta,s} + \mu_{\lambda,s} \mu_{\beta,s}) + t_j^2(\mu_{\beta,s}^2 + \sigma_{\beta,s}^2) \right)$$
(24)

$$\begin{cases}
\hat{\mu}_{1,s}^{\prime(n+1)} = \mu_{\lambda,s} \\
\hat{\sigma}_{1,s}^{2(n+1)} = \sigma_{\lambda,s}^{2} \\
\hat{\mu}_{2,s}^{(n+1)} = \mu_{\beta,s} \\
\hat{\sigma}_{2,s}^{2(n+1)} = \sigma_{\beta,s}^{2}
\end{cases}$$
(25)

where  $\mu_{\lambda,s}$  and  $\sigma_{\lambda,s}^2$  represent the mean and variance of the posterior distribution of parameter  $\lambda$ , while  $\mu_{\beta,s}$  and  $\sigma_{\beta,s}^2$  denote the mean and variance of the posterior distribution of parameter  $\beta$ , and  $\rho_s$  is the correlation coefficient. when the estimation error  $\|\hat{\mathbf{\Theta}}_s^{(n+1)} - \hat{\mathbf{\Theta}}_s^{(n)}\|$  falls below a predefined threshold, the parameter estimation results at time  $t_s$  is output.

#### <span id="page-6-0"></span>Parameter updates based on bayesian theory

For the parameter updates of  $\lambda$  and  $\beta$ , the posterior distribution is computed using Bayesian theory based on prior distributions and historical observations. Given that  $\lambda$ ,  $\beta$ , and  $\varepsilon(t_s)$  are mutually independent and  $\varepsilon(t_1), \varepsilon(t_2), \cdots, \varepsilon(t_L)$  is an independently and identically distributed random variable, the Bayesian process utilizes the degradation index  $\mathbf{F}_{1:s} = [F_1, F_2, \cdots, F_s]$  as prior information to perform posterior estimation of the model parameters, enabling real-time updates of the joint posterior distribution of the random parameter  $(\lambda, \beta)$ . The joint probability density function of  $\mathbf{F}_{1:s}$  is given as follows:

$$p(F_1, F_2, \dots, F_s | \lambda, \beta) = \left(\frac{1}{\sqrt{2\pi\sigma^2}}\right)^s \times \exp\left(-\sum_{j=1}^s \left(\frac{(F_j - \lambda - \beta t_j)^2}{2\sigma^2}\right)\right)$$
(26)

where the joint posterior distribution of  $\lambda$  and  $\beta$  given  $\mathbf{F}_{1:s} = [F_1, F_2, \cdots, F_s]$  follows a Gaussian distribution,  $\lambda, \beta | \mathbf{F}_{1:s} \sim N(\mu_{\lambda,s}, \sigma_{\lambda,s}^2, \mu_{\beta,s}, \sigma_{\beta,s}^2, \rho_s)$ .

Assuming the prior joint bivariate normal distribution of the random parameter  $(\lambda, \beta)$  is  $p(\lambda, \beta)$ , the posterior joint density function is expressed as:

$$p(\lambda, \beta | \mathbf{F}_{1:s}) \propto p(\mathbf{F}_{1:s} | \lambda, \beta) \cdot p(\lambda, \beta)$$

$$\propto \frac{1}{2\pi\sigma_{\lambda,s}\sigma_{\beta,s}\sqrt{1-\rho_s^2}} \times \exp\left\{\frac{1}{2(1-\rho_s^2)} \cdot \left[\frac{(\lambda-\mu_{\lambda,s})^2}{\sigma_{\lambda,s}^2} - 2\rho_s \frac{(\lambda-\mu_{\lambda,s})(\beta-\mu_{\beta,s})}{\sigma_{\lambda,s}^2\sigma_{\beta,s}^2} + \frac{(\beta-\mu_{\beta,s})^2}{\sigma_{\beta,s}^2}\right]\right\}$$
(27)

<span id="page-6-2"></span>Through algebraic manipulation, the expression for parameter  $\mu_{\lambda,s}$ ,  $\sigma_{\lambda,s}^2$ ,  $\mu_{\beta,s}$ ,  $\sigma_{\beta,s}^2$ ,  $\rho_s$  in Eqs. (28), (29), (30), (31), and (32) is derived as follows:

$$\mu_{\lambda,s} = \frac{\left(\sum_{j=1}^{s} F_{j}\sigma_{1}^{2} + \mu_{1}'\sigma^{2}\right)\left(\sum_{j=1}^{s} t_{j}^{2}\sigma_{2}^{2} + \sigma^{2}\right) - \left(\sum_{j=1}^{s} t_{j}\sigma_{1}^{2}\right)\left(\sum_{j=1}^{s} F_{j}t_{j}\sigma_{2}^{2} + \mu_{2}\sigma^{2}\right)}{\left(s\sigma_{1}^{2} + \sigma^{2}\right)\left(\sum_{j=1}^{s} t_{j}^{2}\sigma_{2}^{2} + \sigma^{2}\right) - \left(\sum_{j=1}^{s} t_{j}\sigma_{2}^{2}\right)\left(\sum_{j=1}^{s} t_{j}\sigma_{1}^{2}\right)}$$
(28)

<span id="page-7-1"></span><span id="page-7-0"></span>
$$\mu_{\beta,s} = \frac{\left(s\sigma_1^2 + \sigma^2\right) \left(\sum_{j=1}^s F_j t_j \sigma_2^2 + \mu_2 \sigma^2\right) - \left(\sum_{j=1}^s t_j \sigma_2^2\right) \left(\sum_{j=1}^s F_j \sigma_1^2 + \mu_1' \sigma^2\right)}{\left(s\sigma_1^2 + \sigma^2\right) \left(\sum_{j=1}^s t_j^2 \sigma_2^2 + \sigma^2\right) - \left(\sum_{j=1}^s t_j \sigma_2^2\right) \left(\sum_{j=1}^s t_j \sigma_1^2\right)}$$
(29)

$$\sigma_{\lambda,s}^{2} = \frac{\bar{\sigma}^{2}}{\sigma_{2}^{2}} \frac{\sum_{j=1}^{s} t_{j}^{2} \sigma_{2}^{2} + \sigma^{2}}{(s\sigma_{1}^{2} + \sigma^{2}) \left(\sum_{j=1}^{s} t_{j}^{2} \sigma_{2}^{2} + \sigma^{2}\right) - \left(\sum_{j=1}^{s} t_{j}\right)^{2} \sigma_{1}^{2} \sigma_{2}^{2}}$$
(30)

<span id="page-7-2"></span>
$$\sigma_{\beta,s}^{2} = \frac{\bar{\sigma}^{2}}{\sigma_{1}^{2}} \frac{s\sigma_{1}^{2} + \sigma^{2}}{(s\sigma_{1}^{2} + \sigma^{2}) \left(\sum_{j=1}^{s} t_{j}^{2} \sigma_{2}^{2} + \sigma^{2}\right) - \left(\sum_{j=1}^{s} t_{j}\right)^{2} \sigma_{1}^{2} \sigma_{2}^{2}}$$
(31)

$$\rho_s = \frac{-\sigma_1 \sigma_2 \sum_{j=1}^s t_j}{\sqrt{s\sigma_1^2 + \sigma^2} \sqrt{\sigma_2^2 \sum_{j=1}^s t_j^2 + \sigma^2}}$$
(32)

<span id="page-7-3"></span>where  $\bar{\sigma}^2 = \sigma^2 \sigma_1^2 \sigma_2^2$ ,  $\mu_{\lambda,s}$ , and  $\sigma_{\lambda,s}^2$  denote the mean and variance of the posterior distribution of parameter  $\lambda$ , while  $\mu_{\beta,s}$  and  $\sigma_{\beta,s}^2$  represent the mean and variance of the posterior distribution of parameter  $\beta$ .

### Remaining useful life prediction model Model construction

<span id="page-7-4"></span>Based on the degradation model parameter estimation and updates, the degradation degree  $F(t_s+t)$  at time  $t_s+t$  can be predicted using the historical degradation data  $\mathbf{F}_{1:s}$ , and  $F(t_s+t)=\lambda+\beta(t_s+t)+\varepsilon(t_s+t)-\sigma^2/2$ . As the predicted degradation degree follows a Gaussian distribution, its mean and variance are given by the following expressions:

$$\tilde{\mu}(t_s + t) = \mu_\lambda + \mu_\beta(t_s + t) - \frac{\sigma^2}{2} \tag{33}$$

$$\tilde{\sigma}^2(t_s + t) = \sigma_\lambda^2 + (t_s + t)^2 \sigma_\beta^2 + \sigma^2 + 2\rho_s(t_s + t)\sigma_\lambda\sigma_\beta \tag{34}$$

The RUL L is defined as the time between the degradation degree reaching the given failure threshold  $\delta$ . Since  $F(t_s)$  is the degradation model after a logarithmic transformation, L should satisfy  $F(L+t_s)=\ln\delta$ . Therefore, the conditional cumulative distribution function of the RUL can be expressed as:

$$R_{L|\mathbf{F}_{1:s}}(t) = P(L \leqslant t|F_1, F_2, \cdots F_s)$$

$$= P(F(t_s + t) \geqslant \ln \delta | F_1, F_2, \cdots F_s)$$

$$= P\left(Z \geqslant \frac{\ln \delta - \tilde{\mu}(t_s + t)}{\sqrt{\tilde{\sigma}^2(t_s + t)}}\right) = \mathbf{\Phi}(g(t))$$
(35)

$$g(t) = \frac{\tilde{\mu}(t + t_s) - \ln \delta}{\sqrt{\tilde{\sigma}^2(t_s + t)}}$$
(36)

where Z is a random variable following the standard normal distribution, and  $\Phi(\cdot)$  is the cumulative distribution function of the standard normal distribution.

Since the RUL is non-negative ( $L \ge 0$ ), the actual conditional cumulative distribution function is given by:

$$R_{L|\mathbf{F}_{1:s}}(t) = P(L \leq t|F_1, F_2, \cdots F_s, L \geq 0)$$

$$= \frac{P\{0 \leq L \leq t|F_1, F_2, \cdots F_s\}}{P\{L \geq 0|F_1, F_2, \cdots F_s\}}$$

$$= \frac{\mathbf{\Phi}(g(t)) - \mathbf{\Phi}(g(0))}{1 - \mathbf{\Phi}(g(0))}$$
(37)

<span id="page-8-0"></span>Further derivation leads to the conditional probability density function of the RUL as:

$$f_{L|F_1,F_2,\cdots F_s,L\geqslant 0}(t) = \frac{\psi(g(t))g'(t)}{1 - \Phi(g(0))}$$
(38)

<span id="page-8-1"></span>In Eq. (38),  $\psi(\cdot)$  represents the probability density function of a standard normal distribution. For the RUL estimation, based on Eq. (33), the predicted mean  $\tilde{\mu}(t_s+t)$  from the degradation state is used in place of  $F(L+t_s)$ . Then, combining the failure threshold  $F(L+t_s)=\ln\delta$ , the expected RUL can be expressed as:

$$RUL_s = \frac{\ln \delta - \mu_{\lambda,s} + \sigma^2/2}{\mu_{\beta,s}} - t_s \tag{39}$$

#### **Evaluation metrics**

To comprehensively evaluate the prediction performance of the proposed degradation modeling and RUL prediction framework, three evaluation metrics are employed: root mean square error (RMSE), mean absolute error (MAE), and confidence interval coverage (CIC). These metrics jointly assess both the accuracy and reliability of the predicted results.

RMSE quantifies the average magnitude of prediction errors by penalizing larger deviations more heavily. it provides an overall measure of the prediction accuracy and is expressed as:

RMSE = 
$$\sqrt{\frac{1}{N} \sum_{i=1}^{N} (\hat{y}_i - y_i)^2}$$
 (40)

where  $y_i$  denotes the true value,  $\hat{y}_i$  represents the predicted value, and N is the number of samples.

MAE captures the average absolute difference between predicted and true values, reflecting the robustness of the model against outliers. the metric is defined as:

$$MAE = \frac{1}{N} \sum_{i=1}^{N} |\hat{y}_i - y_i|$$
 (41)

CIC evaluates the reliability of the predicted confidence intervals by measuring the proportion of true values that fall within the estimated bounds. It is calculated as:

CIC = 
$$\frac{1}{N} \sum_{i=1}^{N} F(y_i \in [L_i, U_i])$$
 (42)

where  $[L_i, U_i]$  represents the lower and upper bounds of the prediction interval for the *i*-th sample, and  $F(\cdot)$  is the indicator function.

In this study, the pseudocode for the nonlinear degradation modeling and RUL prediction algorithm for the electric drive system is presented as Algorithm 1. The algorithm incorporates input data including user operational data, bench test data, model initialization parameters, and failure thresholds, integrating failure physics models for different components to enable RUL predictions across various service stages under real-world user scenarios.

#### **Case study**

.

#### **Degradation trajectory modeling based on bench test correction**

The datasets used in this study consists of operational data from 30 vehicles of the same model, covering one year of driving behavior and road conditions from different users. The schematic representation of user timedomain data is illustrated in Fig. [3.](#page-10-0) Furthermore, statistics are compiled for each user, including total operating time, annual mileage, cumulative damage contribution, and damage contribution rate, as illustrated in Fig. [4](#page-11-0).

In Fig. [4,](#page-11-0) the cumulative damage contribution is defined as the ratio of a user's composite health indicator to the total composite health indicator across all users. The damage contribution rate is calculated by dividing a user's cumulative damage contribution by their total mileage.

The composite health indicator integrates the effects of multiple failure modes and reflects the overall degradation trend of the system. This study employs the entropy weight method to linearly fuse damage contribution features across different failure modes. Additionally, a comparative analysis of weighting method variations is conducted, utilizing the coefficient of variation method and the CRITIC weighting method to construct composite health indicators[47.](#page-22-33) Linear fitting is applied to the resulting composite health indicators, yielding the slope of the linear fitting equation for each user under different methods, which represents the linear degradation rate, as depicted in Fig. [5](#page-11-1). The result reveals that the degradation rates of different users are highly consistent across the various methods, indicating that the choice of weighting method has a minimal impact on the composite health indicator.

How to refine the aforementioned composite health indicator into a degradation trajectory that aligns with actual degradation patterns is of paramount importance. To address this, an accelerated durability test of the EDS is conducted, during which vibration signals from the test prototype are monitored to characterize the evolution of its degradation state. Furthermore, a comparative analysis between the degradation rates under user non-accelerated conditions and bench accelerated conditions is performed to establish an equivalence relationship, which is then used to correct the nonlinear degradation model under real-world user conditions.

For the accelerated durability test of the electric drive system, a load spectrum is developed based on realworld user operation data. Simulated load signals are applied to both ends of the electric drive assembly using the dynamometer to replicate typical user conditions. The test bench setup and a single-cycle load spectrum are shown in Fig. [5.](#page-11-1)

Each cycle lasts 12 h and is repeated 100 cycles to replicate the equivalent damage corresponding to 300,000 km of user operation, resulting in a total test duration of 1,200 h. Throughout the test, key parameters such as rotational speed, torque, voltage, current, oil temperature, and vibration are continuously monitored to track the degradation process.

<span id="page-10-0"></span>![](_page_10_Figure_1.jpeg)

**Fig. 3**. Schematic diagram of user time-domain data

In this study, the vibration signals of the prototype monitored during the bench tests are used to indirectly represent its degradation trajectory. The RMS of the vibration signals from each test cycle is extracted to establish the system's degradation model. Considering the impact of inherent uncertainties, such as material properties, manufacturing processes, and assembly errors, on the lifespan of the prototype, accelerated durability tests are conducted on three identical prototypes to quantify these uncertainties. As the number of cycles increases, the degradation trends and fitting models for each prototype are shown in Figs. [7](#page-12-0) and [8,](#page-12-1) and [9](#page-13-0). The RMS values of the vibration signals from the three prototypes are normalized to the [0,1] range, and an exponential model is used to fit the RMS values of the vibration signals. The overall degradation exhibits nonlinear accumulation, and the degradation rate increases non-stationarily. The fitting formula and the 95% confidence interval of the fitting parameters are as follows:

$$\begin{cases}
f_1(x) = a_1 \cdot \exp(b_1 \cdot x) = 0.1501 \cdot \exp(0.0182 \cdot x) \\
f_2(x) = a_2 \cdot \exp(b_2 \cdot x) = 0.0964 \cdot \exp(0.0237 \cdot x) \\
f_3(x) = a_3 \cdot \exp(b_3 \cdot x) = 0.1536 \cdot \exp(0.0186 \cdot x) \\
a_1 \in [0.1222, 0.1780]; b_1 \in [0.0163, 0.0201] \\
a_2 \in [0.0715, 0.1214]; b_2 \in [0.0216, 0.0258] \\
a_3 \in [0.1271, 0.1801]; b_3 \in [0.0168, 0.0204]
\end{cases}$$
(43)

Based on the normal distribution characteristics of the fitting parameters, the Monte Carlo method is used to randomly sample the distribution of the fitting parameters, generating 30 degradation datasets. The initial values are normalized, and the degradation indicator distribution model corresponding to the full life cycle is used to quantify the inherent uncertainty of the prototype, as shown in Fig. [10](#page-13-1). The results indicate that the accelerated durability test effectively defines the range of inherent uncertainty in the random fluctuations of the degradation indicator. However, in real-world user applications, it is crucial to consider the correlation between the acceleration factor of the accelerated test spectrum and the actual user load spectrum.

Given that the degradation rate under real-world operating conditions is significantly lower than that in accelerated tests, a dual-prototype comparative test is conducted in this study. Prototype A is subjected to the

<span id="page-11-0"></span>![](_page_11_Figure_1.jpeg)

**Fig. 4**. Statistical characteristics of different user data.

<span id="page-11-1"></span>![](_page_11_Figure_3.jpeg)

**Fig. 5**. Comparison of composite health indicator results across different weighting methods; (**a**) Entropy weight method; (**b**) Coefficient of variation method; (**c**) CRITIC weighting method; (**d**) Comparison of linear degradation rates.

![](_page_12_Figure_2.jpeg)

**Fig. 6**. Electric drive system test bench and load spectrum; (**a**) Test bench; (**b**) Durability test load spectrum.

<span id="page-12-0"></span>![](_page_12_Figure_4.jpeg)

**Fig. 7**. The degradation trajectory fitting of prototype 1

<span id="page-12-1"></span>![](_page_12_Figure_6.jpeg)

**Fig. 8**. The degradation trajectory fitting of prototype 2.

<span id="page-13-0"></span>![](_page_13_Figure_1.jpeg)

**Fig. 9**. The degradation trajectory fitting of prototype 3

<span id="page-13-1"></span>![](_page_13_Figure_3.jpeg)

**Fig. 10**. The quantification of the inherent uncertainty of prototypes.

<span id="page-13-2"></span>![](_page_13_Picture_5.jpeg)

**Fig. 11**. Test bench schematic of the EDS.

user's non-accelerated load spectrum, while prototype B is exposed to the accelerated test load spectrum. The total test duration under the accelerated spectrum is 875 h, aimed at replicating the damage target corresponding to 300,000 km of user operation. The accelerated spectrum consists of 350 cycles, with vibration signals recorded every 10 cycles. Vibration acceleration signals in the Y-axis of the bearing, Y-axis of the differential, and Z-axis of the gearbox are monitored simultaneously, as shown in Fig. [11](#page-13-2).

To quantify the relationship between the degradation rates of the accelerated and user spectra, the acceleration factor is defined, as the ratio of the linear fit slope of the vibration signal under the accelerated spectrum to the linear fit slope of the vibration signal under the non-accelerated load spectrum[48.](#page-22-34) The comparison of the threeaxis vibration signals is shown in Figs. [12](#page-14-0) and [13,](#page-14-1) and [14](#page-14-2). The average acceleration factor of the three directions is 8.7, which is used as the overall acceleration factor and substituted into Eq. ([18](#page-5-2)) to correct the degradation model parameters. The standard deviation ratios for vibration acceleration (VA) of the three directions are also

<span id="page-14-0"></span>![](_page_14_Figure_1.jpeg)

**Fig. 12**. Comparison of VA at the bearing Y-direction.

<span id="page-14-1"></span>![](_page_14_Figure_3.jpeg)

**Fig. 13**. Comparison of VA at the differential Y-direction.

<span id="page-14-2"></span>![](_page_14_Figure_5.jpeg)

**Fig. 14**. Comparison of VA at the gearbox Z-direction.

calculated, and by combining the standard deviation of the failure threshold in the accelerated test from Fig. [8](#page-12-1), the random error term under user conditions is derived to follow *N*(0*,* 0*.*0146<sup>2</sup>).

To account for the variability in degradation rates among different users, the overall user failure threshold is defined based on the damage target replicated in the bench test. The user sample set is selected corresponding to the 50th percentile of cumulative damage contribution rates from Fig. [4.](#page-11-0) Using damage equivalence and factor

<span id="page-15-0"></span>![](_page_15_Figure_1.jpeg)

Fig. 15. Nonlinear degradation trajectories of different users.

<span id="page-15-1"></span>![](_page_15_Figure_3.jpeg)

**Fig. 16**. Sensitivity analysis of the initial mean values of parameters  $\lambda$  and  $\beta$ .

extrapolation, the user failure threshold  $\delta_T = 1.65$  at 50th percentile is determined. Subsequently, nonlinear degradation trajectories incorporating random errors are generated for different users, as shown in Fig. 15.

#### Model parameter Estimation and dynamic updating

This section selects four representative users corresponding to the 25th, 50th, 75th, and 95th percentiles of the cumulative damage rate distribution (damage rate - cumulative distribution function, Ds-CDF) to perform model parameter estimation. Based on the nonlinear degradation trajectories derived in Sect. 5.1, it is essential to first specify the prior distribution of the model parameters before performing parameter estimation and dynamic updating.

In this study, the user at the 50th percentile of the Ds-CDF is selected as the target subject. For the prior distribution parameters  $\Theta = \{\mu_1', \sigma_1^2, \mu_2, \sigma_2^2, \sigma^2\}$ , the initial ranges are determined based on historical degradation data and bench test results, with  $\mu_1' \in [0.05, 1], \sigma_1^2 \in [0.01, 0.5], \mu_2 \in [0.05, 1], \sigma_2^2 \in [0.01, 0.5], \sigma^2 \in [0.001, 0.01]$ . From each range, 10 evenly spaced sample points are selected, resulting in a total of 100,000 parameter sets. Each parameter set is used as input for model parameter estimation and Bayesian updating, followed by RUL prediction. To evaluate the influence of different hyperparameter combinations on the prediction results, the prediction accuracy is assessed using the RMSE. The optimal parameter combination is selected when the RMSE reached its minimum value. Among the 100,000 tested combinations, the best set is found to be  $\mu_1' = 0.05$ ,  $\sigma_1^2 = 0.5$ ,  $\mu_2 = 0.05$ ,  $\sigma_2^2 = 0.01$ ,  $\sigma_2^2 = 0.002$ .

To further analyze the influence of individual parameters, the control variable method is applied. When keeping  $\sigma_1^2, \sigma_2^2, \sigma^2$  constant and varying the initial mean values of parameters  $\lambda$  and  $\beta$ , the corresponding prediction errors are shown in Fig. 16. Similarly, by keeping  $\mu_1', \mu_2, \sigma^2$  constant and varying the initial variances of parameters  $\lambda$  and  $\beta$ , the sensitivity of variance selection is analyzed as shown in Fig. 17. These results indicate that the choice of prior parameter values significantly affects RUL prediction performance. In particular, the sensitivity analysis of the initial mean values of the parameters shows that the lowest RMSE is achieved when  $\mu_1' = 0.05, \mu_2 = 0.05$ . For sensitivity analysis of the initial variance values of the parameters, the lowest RMSE is observed when  $\sigma_1^2 = 0.5, \sigma_2^2 = 0.01$ . Since the noise variance  $\sigma^2$  is closely related to the actual degradation process, its prior information is derived from user degradation trajectories, and the optimal value is identified

<span id="page-16-0"></span>![](_page_16_Figure_1.jpeg)

**Fig. 17**. Sensitivity analysis of the initial variance values of parameters  $\lambda$  and  $\beta$ .

<span id="page-16-1"></span>![](_page_16_Figure_3.jpeg)

Fig. 18. Variation trend of RMSE under different iteration thresholds.

as  $\sigma^2 = 0.002$ . Additionally, for other users, the aforementioned method is similarly applied to conduct a sensitivity analysis of the model's prior distribution parameters, ensuring the accuracy of RUL predictions.

In addition, the influence of the EM iteration threshold  $\omega$  on RUL prediction is examined. The iteration stopping criterion is defined as  $\left\|\hat{\mathbf{\Theta}}_s^{(n+1)} - \hat{\mathbf{\Theta}}_s^{(n)}\right\| < \omega$ , with the threshold range set to [1E-10,1E-02]. The

RMSE variation under different thresholds is presented in Fig. 18. Results show that large values of  $\omega$  lead to higher prediction errors, while decreasing  $\omega$ results in progressively lower RMSE values. when the threshold reaches 1E-06, the RMSE stabilizes at its minimum level. Hence, the iteration threshold in this study is set to  $\omega=1\text{E}$ -06.

The user's full life cycle data is divided into 100 operational cycles. For each cycle, model parameters are estimated, including the mean  $\mu_1'$  and variance  $\sigma_1^2$  of parameter  $\lambda$ , the mean  $\mu_2$  and variance  $\sigma_2^2$  of parameter  $\beta$ , and the estimated correlation coefficient  $\rho_s$  between parameters  $\lambda$  and  $\beta$ . The true values of the parameters are defined as the converged values of the degradation model parameters for the target user. As more historical degradation data becomes available, the model parameters are dynamically updated, with the results shown in Fig. 19. It is observed that as the number of iterations increases, the variation in parameter estimates gradually decreases and tends toward stability. In particular, the variances of parameters  $\lambda$  and  $\beta$  show minimal changes after approximately 30 iterations. Therefore, a logarithmic scale is used to present the variance update process, allowing for a clearer illustration of the convergence behavior.

The final degradation model parameters for the target user are as follows:  $\mu_1'=0.0237$ ,  $\sigma_1^2=1.869\text{E}-04$ ,  $\mu_2=0.0103$ ,  $\sigma_2^2=6.9213\text{E}-08$ ,  $\rho_s=-0.8684$ . Following the above analytical procedure, parameter estimation is performed for four representative users at the 25th, 50th, 75th, and 95th percentiles of cumulative damage rate. The parameters of the exponential degradation model for each user are iteratively updated, and the final estimation results are summarized in Table 1.

#### Remaining useful life prediction and result evaluation

To elucidate the evolution of degradation states, this study examines the degradation process across the full user life cycle by selecting the 25th, 50th, 75th, and 95th percentiles of service cycles. It analyzes the performance degradation of the electric drive system and the dynamic changes in RUL predictions under different service cycles, as shown in Fig. 20.

<span id="page-17-0"></span>![](_page_17_Figure_1.jpeg)

Fig. 19. Parameter estimation results for the target user's degradation model; (a) Mean  $\mu'_1$  estimation of parameter  $\lambda$ ; (b) Variance  $\sigma^2_1$  estimation of parameter  $\lambda$ ; (c) Mean  $\mu_2$  estimation of parameter  $\beta$ ; (d) Variance  $\sigma^2_2$  estimation of parameter  $\beta$ ; (e) Correlation coefficient  $\rho_s$  estimation between parameters  $\lambda$  and  $\beta$ .

<span id="page-17-1"></span>

| User        | $\mu_1'$ | $\sigma_1^2$ | $\mu_2$ | $\sigma_2^2$ | $\rho_s$ |
|-------------|----------|--------------|---------|--------------|----------|
| 25%(Ds-CDF) | 0.0212   | 1.830E-04    | 0.0099  | 5.965E-08    | -0.8675  |
| 50%(Ds-CDF) | 0.0237   | 1.869E-04    | 0.0103  | 6.921E-08    | -0.8684  |
| 75%(Ds-CDF) | 0.0126   | 1.712E-04    | 0.0100  | 5.596E-08    | -0.8687  |
| 95%(Ds-CDF) | 0.0492   | 1.935E-04    | 0.0096  | 5.967E-08    | -0.8683  |

**Table 1**. Estimated parameters of the exponential degradation model for different users.

<span id="page-18-0"></span>![](_page_18_Figure_1.jpeg)

**Fig. 20**. RUL prediction results of the EDS at different service stages; (**a**) RUL prediction at the 25th percentile service cycle; (**b**) RUL prediction at the 50th percentile service cycle; (**c**) RUL prediction at the 75th percentile service cycle; (**d**) RUL prediction at the 95th percentile service cycle.

Figure [20](#page-18-0) illustrates the evolution of the composite health indicator for the electric drive system, the RUL predictions, and the 95% confidence intervals across four service cycles. At the 25th percentile service cycle, limited historical degradation data result in larger errors in parameter estimation, leading to wider confidence intervals and significant discrepancies between the predicted and actual RUL values. As service cycles accumulate, the degradation model parameters converge toward optimal values, the confidence intervals for the nonlinear composite health indicator narrow, and the RUL probability density distribution becomes more concentrated, reducing the error between predicted and actual RUL values. These findings confirm the effectiveness of the degradation model and parameter estimation method in modeling the composite health indicator and predicting RUL for the electric drive system.

To thoroughly analyze the RUL predictions across different service cycles, the RUL probability density functions are calculated for each cycle using Eq. [\(38\)](#page-8-0). The expected RUL values are derived from Eq. [\(39](#page-8-1)) and compared with actual RUL values, as shown in Fig. [21a](#page-19-0). The RUL probability density functions for all service cycles encompass the actual RUL values of the target user, with the distributions becoming increasingly concentrated as service cycles progress. Comparison of predicted and actual RUL values reveals that, in earlier cycles, limited historical data lead to inaccurate parameter estimation, resulting in significant deviations. However, after the 20th percentile service cycle, predicted values closely align with actual values. Furthermore, the prediction error, defined as the difference between predicted and actual values, is presented in Fig. [21b](#page-19-0). Beyond the 20th percentile, the prediction error stabilizes, with relative errors consistently within 10%.

The RUL prediction results for the four representative users are shown in Fig. [22](#page-19-1), including comparisons between actual and predicted RUL values, as well as the corresponding RUL probability density distributions.

As illustrated in Fig. [22,](#page-19-1) the RUL probability density distributions for different users at specific service cycles consistently encompass the actual RUL values. In the early service stages, the predicted RUL mean exhibits noticeable deviations from the actual values. However, as historical data accumulate, the model parameter estimates stabilize, leading to closer alignment between predicted and actual RUL values in later service stages, with probability density distributions becoming more concentrated compared to earlier stages.

<span id="page-19-0"></span>![](_page_19_Figure_1.jpeg)

![](_page_19_Figure_2.jpeg)

**Fig. 21**. Comparison of RUL Prediction results and relative error; (**a**) Comparison between predicted and actual RUL values; (**b**) Relative error.

<span id="page-19-1"></span>![](_page_19_Figure_4.jpeg)

**Fig. 22**. RUL prediction results for users under different cumulative damage rates; (**a**) The user at the 25th percentile of the Ds-CDF; (**b**) The user at the 50th percentile of the Ds-CDF; (**c**) The user at the 75th percentile of the Ds-CDF; (**d**) The user at the 95th percentile of the Ds-CDF.

#### **Comparative analysis**

To validate the effectiveness of the proposed method, comparative experiments are conducted using the classical wiener process model and a CNN-LSTM deep learning model on the same degradation dataset. Prediction performance is evaluated in terms of RMSE, MAE, and CIC.

The Wiener process model characterizes degradation dynamics according to drift and diffusion terms, with parameters estimated online from degradation increments. RUL is predicted under the assumption of an inverse Gaussian distribution, where the expected value serves as the point estimate. The confidence bounds [*<sup>F</sup> <sup>−</sup>*<sup>1</sup>(*α/*2)*, F <sup>−</sup>*<sup>1</sup>(1 *<sup>−</sup> α/*2)] are computed using the inverse cumulative distribution function, with the significance level set to 0.05, corresponding to a 95% confidence interval.

The CNN-LSTM deep learning model integrates the strengths of convolutional neural networks and long short-term memory networks, enabling the simultaneous capture of spatial features and temporal dependencies during degradation processes. The model architecture comprises convolutional layers, batch normalization layers, activation layers, pooling layers, LSTM layers, and fully connected layers. The input to the model includes features representing the current degradation state, supplemented by statistical feature parameters such as the mean, variance, and extrema of the electric drive system's rotational speed, torque, and temperature over the service cycle. Hyperparameters for this model have been optimized through sensitivity analysis, with the number of convolutional filters set to 32, the number of LSTM units to 30, the convolutional kernel size to 10, the initial learning rate to 0.001, and the learning rate decay factor to 0.1. To mitigate overfitting, a dropout ratio of 0.3 is incorporated. During training, degradation data from 26 users are utilized, with the aforementioned four target users employed for prediction. Given that the CNN-LSTM model inherently produces point predictions, the standard deviation of the prediction error *σ*res is derived through residual analysis, assuming the residuals approximate a normal distribution. Confidence intervals for the predicted values are then constructed using the quantiles of this normal distribution, defined as [ˆ*y − z*<sup>1</sup>*−α/*<sup>2</sup> *· σ*res*, y*ˆ + *z*<sup>1</sup>*−α/*<sup>2</sup> *· σ*res].

Figure [23](#page-20-0) presents the comparison of RUL prediction results across the three models for the four target users. As observed, the wiener model exhibits large fluctuations and significant deviations from the ground truth. The CNN-LSTM model is able to track the degradation trend more effectively, but with occasional overestimation or underestimation. In contrast, the proposed method produces prediction curves closely aligned with the true RUL, demonstrating superior robustness and accuracy across different users.

To further quantify prediction accuracy and uncertainty, a comparative analysis of evaluation metrics across different models for various users is presented, as detailed in Table [2.](#page-21-11)

The Wiener model, which relies solely on assumptions of linear drift and Gaussian noise, exhibits significant prediction variability when degradation trajectories display pronounced nonlinearity, resulting in notably higher RMSE and MAE values compared to other models, alongside a lower CIC metric. In contrast, the CNN-LSTM model demonstrates superior RMSE and MAE performance across different stages compared to the Wiener model, with CIC values ranging from 0.87 to 0.91, indicating robust fitting capabilities for complex nonlinear degradation data. However, this model is limited to point predictions and lacks explicit modelling of prediction uncertainty. The proposed method in this study addresses these limitations by explicitly incorporating

<span id="page-20-0"></span>![](_page_20_Figure_6.jpeg)

**Fig. 23**. Comparison of RUL prediction expected values across different models; (**a**) The user at the 25th percentile of the Ds-CDF; (**b**) The user at the 50th percentile of the Ds-CDF; (**c**) The user at the 75th percentile of the Ds-CDF; (**d**) The user at the 95th percentile of the Ds-CDF.

<span id="page-21-11"></span>

|             | Wiener model |       |      | CNN-LSTM model |      |      | Proposed model |      |      |
|-------------|--------------|-------|------|----------------|------|------|----------------|------|------|
| User        | RMSE         | MAE   | CIC  | RMSE           | MAE  | CIC  | RMSE           | MAE  | CIC  |
| 25%(Ds-CDF) | 30.15        | 25.27 | 0.67 | 5.82           | 4.70 | 0.87 | 4.30           | 3.99 | 0.97 |
| 50%(Ds-CDF) | 34.83        | 28.93 | 0.76 | 5.91           | 4.76 | 0.90 | 3.70           | 3.29 | 0.97 |
| 75%(Ds-CDF) | 35.45        | 29.67 | 0.69 | 6.12           | 4.82 | 0.89 | 5.88           | 4.24 | 0.96 |
| 95%(Ds-CDF) | 24.53        | 21.69 | 0.89 | 5.84           | 4.70 | 0.91 | 5.42           | 4.38 | 0.93 |

**Table 2**. Comparative results of evaluation metrics for each user across different models.

degradation mechanisms and constructing nonlinear degradation trajectories during the modelling process. By integrating an exponential degradation model with EM parameter estimation and Bayesian updates, it effectively models and predicts complex nonlinear degradation processes. The results reveal a high degree of consistency between predicted and actual RUL values, with RMSE and MAE maintained at low levels, and a CIC metric exceeding 0.93, significantly outperforming both the Wiener and CNN-LSTM models.

#### **Conclusion**

This study introduces an innovative framework for nonlinear degradation modeling and RUL prediction tailored to electric drive system with multiple failure modes. The conclusions are as follows:

- (1) Leveraging actual operational data collected from the EDS, this study correlates the failure physics characteristics of core EDS components and employs the entropy weight method to construct a composite health indicator for the system. Accelerated durability bench testing of EDS is conducted, with comparative experiments between accelerated and unaccelerated spectra, establishing nonlinear degradation trajectories and models under user-specific scenarios.
- (2) Building on the foundation of nonlinear degradation modeling, a RUL prediction model is proposed, integrating EM parameter estimation with Bayesian updates. This model enables dynamic RUL prediction and uncertainty quantification across multiple users and various service stages. The case study reveals that prediction errors stabilize within 10% after approximately 20% of the service life.
- (3) Comparative experiments involving multiple algorithmic models are performed, revealing that the Wiener model exhibits significant prediction variability and notable deviations from actual values. The CNN-LSTM model demonstrates robust fitting capabilities for nonlinear degradation data but is subject to fluctuations involving overestimation and underestimation. In contrast, the method proposed in this study explicitly incorporates degradation mechanisms and nonlinear degradation modeling, exhibiting enhanced robustness and precision across different users and degradation stages.

Overall, the proposed methods not only improve the accuracy of health state monitoring and RUL prediction for electric drive system but also lay the groundwork for broader applications in industries involving complex, multi-component systems. Future research can expand on this approach by incorporating additional failure modes, enhancing the model's scalability, and exploring its integration with other condition monitoring technologies to further advance predictive maintenance strategies.

#### **Data availability**

The data in this article involves business cooperation and is not allowed to be shared on the Internet. The datasets used and/or analysed during the current study available from the corresponding author on reasonable request.

Received: 22 April 2025; Accepted: 1 October 2025

### **References**

- <span id="page-21-0"></span>1. De Souza, D. F., Da Silva, P. P. F., Sauer, I. L., De Almeida, A. T. & Tatizawa, H. Life cycle assessment of electric motors - A systematic literature review. *J. Clean. Prod.* **456**, 142366 (2024).
- <span id="page-21-1"></span>2. Pengbo, Z., Renxiang, C., Xiangyang, X., Lixia, Y. & Mengyu, R. Recent progress and prospective evaluation of fault diagnosis strategies for electrified drive powertrains: A comprehensive review. *Measurement* **222**, 113711 (2023).
- <span id="page-21-2"></span>3. Friederich, J. & Lazarova-Molnar, S. Reliability assessment of manufacturing systems: A comprehensive overview, challenges and opportunities. *J. Manuf. Syst.* **72**, 38–58 (2024).
- <span id="page-21-3"></span>4. Hu, Y., Miao, X., Si, Y., Pan, E. & Zio, E. Prognostics and health management: A review from the perspectives of design, development and decision. *Reliab. Eng. Syst. Saf.* **217**, 108063 (2022).
- <span id="page-21-4"></span>5. Huang, C. et al. Prognostics and health management for predictive maintenance: A review. *J. Manuf. Syst.* **75**, 78–101 (2024).
- <span id="page-21-6"></span><span id="page-21-5"></span>6. Chen, G. Residual useful life prediction of lithium-ion battery based on accuracy SoH Estimation. *Sci. Rep.* **15**, 6010 (2025).
- 7. Yan, F., Lu, H. & Xiao, L. Fatigue life prediction of cracked cross beam of mining linear vibrating screen under Cyclic load. *Sci. Rep.* **14**, 19631 (2024).
- <span id="page-21-7"></span>8. Maiorana, E., Aloisio, A., Tasse, V. & Briseghella, B. Prediction of fatigue life of a bolted joint in railway steel arch Bridge using multiaxial fatigue criteria. *Eng. Fail. Anal.* **166**, 108908 (2024).
- <span id="page-21-8"></span>9. Nebo, S. E., Amalu, E. H. & Hughes, D. J. Effective number of accelerated thermal cycles (ATCs) for accurate prediction of damage and fatigue life of solder joints in IGBT power module. *Microelectron. Reliab.* **171**, 115798 (2025).
- <span id="page-21-9"></span>10. Lugt, P. M. On the use of the arrhenius equation to describe the impact of temperature on grease life. *Tribol. Int.* **179**, 108142 (2023).
- <span id="page-21-10"></span>11. Zhao, F., Tian, Z. & Zeng, Y. Uncertainty quantification in gear remaining useful life prediction through an integrated prognostics method. *IEEE Trans. Reliab.* **62**, 146–159 (2013).

- <span id="page-22-0"></span>12. Vega–Garita, V., Heydarzadeh, M., Dadash, A. H. & Immonen, E. The need for aging-aware control methods in lithium-ion batteries: A review. *J. Energy Storage*. **132**, 117653 (2025).
- <span id="page-22-1"></span>13. Saeed, A. et al. Deep learning based approaches for intelligent industrial machinery health management and fault diagnosis in resource-constrained environments. *Sci. Rep.* **15**, 1114 (2025).
- <span id="page-22-2"></span>14. Sultan, Y. A., Eladl, A. A., Hassan, M. A. & Gamel, S. A. Enhancing electric vehicle battery lifespan: integrating active balancing and machine learning for precise RUL Estimation. *Sci. Rep.* **15**, 777 (2025).
- <span id="page-22-3"></span>15. Li, Y., Chen, Y., Hu, Z. & Zhang, H. Remaining useful life prediction of aero-engine enabled by fusing knowledge and deep learning models. *Reliab. Eng. Syst. Saf.* **229**, 108869 (2023).
- <span id="page-22-4"></span>16. Duan, F., Wang, G., Wei, W. & Jiang, M. Remaining useful life evaluation for accelerated wiener degradation process model with mixed random effects and measurement errors. *Qual. Reliab. Eng. Int.* **39**, 1334–1351 (2023).
- <span id="page-22-5"></span>17. Wen, P., Zhao, S., Chen, S. & Li, Y. A generalized remaining useful life prediction method for complex systems based on composite health indicator. *Reliab. Eng. Syst. Saf.* **205**, 107241 (2021).
- <span id="page-22-6"></span>18. Feng, L. & Qian, X. Enhanced real-time crack monitoring and updating in welded structural components with limited measurement data. *Mech. Syst. Signal Process.* **198**, 110403 (2023).
- 19. Xu, W. et al. Wear state assessment of external gear pump based on system-level hybrid digital twin. *Mech. Syst. Signal Process.* **209**, 111123 (2024).
- <span id="page-22-7"></span>20. Li, Y., Fu, C., Liu, T., Hu, Z. & Song, G. Two-stage remaining useful life prediction method across operating conditions based on small samples and novel health indicators. *Reliab. Eng. Syst. Saf.* **264**, 111290 (2025).
- <span id="page-22-8"></span>21. Qin, Y., Zhou, J. & Chen, D. Unsupervised health indicator construction by a novel Degradation-Trend-Constrained variational autoencoder and its applications. *IEEE/ASME Trans. Mechatron.* **27**, 1447–1456 (2022).
- <span id="page-22-9"></span>22. Veloso, G. A. & Loschi, R. H. Dynamic linear degradation model: dealing with heterogeneity in degradation paths. *Reliab. Eng. Syst. Saf.* **210**, 107446 (2021).
- <span id="page-22-10"></span>23. Wang, T., Zhang, Y., Feng, K., Li, Y. & Liu, J. An improved exponential model for machine remaining useful life prediction using empirical Bayes. *Mech. Syst. Signal Process.* **236**, 112970 (2025).
- <span id="page-22-11"></span>24. Song, K. Multivariate degradation modeling and reliability evaluation using gamma processes with hierarchical random effects. *J. Comput. Appl. Math.* **465**, 116591 (2025).
- <span id="page-22-12"></span>25. Jiang, P., Wang, B., Wang, X. & Zhou, Z. Inverse Gaussian process based reliability analysis for constant-stress accelerated degradation data. *Appl. Math. Model.* **105**, 137–148 (2022).
- <span id="page-22-13"></span>26. Guan, Q., Wei, X., Bai, W. & Jia, L. Two-stage degradation modeling for remaining useful life prediction based on the wiener process with measurement errors. *Qual. Reliab. Eng. Int.* **38**, 3485–3512 (2022).
- <span id="page-22-14"></span>27. Niu, T., Xu, Z., Luo, H. & Zhou, Z. Hybrid Gaussian process regression with Temporal feature extraction for partially interpretable remaining useful life interval prediction in aeroengine prognostics. *Sci. Rep.* **15**, 11057 (2025).
- <span id="page-22-15"></span>28. Wu, B., Zeng, J., Shi, H., Zhang, X. & Qin, Y. Remaining useful life prediction for multiple degradation indicators systems considering random correlation. *Comput. Ind. Eng.* **186**, 109736 (2023).
- <span id="page-22-16"></span>29. Wu, B., Shi, H., Zeng, J., Zhang, X. & Wang, Z. Remaining useful life prediction for complex systems with multiple indicators of stochastic correlation considering random shocks. *Mech. Syst. Signal Process.* **204**, 110767 (2023).
- <span id="page-22-17"></span>30. Li, T., Si, X., Pei, H. & Sun, L. Data-model interactive prognosis for multi-sensor monitored stochastic degrading devices. *Mech. Syst. Signal Process.* **167**, 108526 (2022).
- <span id="page-22-18"></span>31. Ye, Q., Lin, M., Zhou, H. & Bu, Y. Remaining useful life prediction of main reducer based on parallel multi-attention and contrastive fusion multi-source domain adaption considering compound-fault. *Mech. Syst. Signal Process.* **236**, 112950 (2025).
- <span id="page-22-19"></span>32. Wu, B., Zhang, X., Shi, H. & Zeng, J. Failure mode division and remaining useful life prognostics of multi-indicator systems with multi-fault. *Reliab. Eng. Syst. Saf.* **244**, 109961 (2024).
- 33. Li, N., Xu, P., Lei, Y., Cai, X. & Kong, D. A self-data-driven method for remaining useful life prediction of wind turbines considering continuously varying speeds. *Mech. Syst. Signal Process.* **165**, 108315 (2022).
- <span id="page-22-20"></span>34. Wen, B. et al. Multivariate degradation system reliability analysis with multiple sources of uncertainty. *Comput. Ind. Eng.* **185**, 109666 (2023).
- <span id="page-22-21"></span>35. Rao, Z., Wu, J., Li, G. & Wang, H. Voltage abnormity prediction method of lithium-ion energy storage power station using informer based on bayesian optimization. *Sci. Rep.* **14**, 21404 (2024).
- <span id="page-22-22"></span>36. Niu, C., Fang, Z. & Dong, W. An uncertain nonlinear remaining useful life prediction model integrating multiple uncertainties quantification for small sample systems. *Mech. Syst. Signal Process.* **230**, 112586 (2025).
- <span id="page-22-23"></span>37. Zhang, N. et al. Model-data hybrid driven approach for remaining useful life prediction of cutting tool based on improved inverse Gaussian process. *J. Manuf. Process.* **124**, 604–620 (2024).
- <span id="page-22-24"></span>38. Wang, Z., Zhao, L., Zhang, D. & Yan, C. Study on dynamic prediction method for degradation state of electric drive system based on deep learning and uncertainty quantification. *Proc. Institution Mech. Eng. Part. D: J. Automobile Eng.* **239**, 1–19 (2023).
- <span id="page-22-25"></span>39. Hou, N. et al. Failure modes, mechanisms and causes of shafts in mechanical equipment. *Eng. Fail. Anal.* **136**, 106216 (2022).
- <span id="page-22-26"></span>40. He, H., Yang, D., Ren, Z., Zhao, R. & Huang, J. The proportion between the gear bending fatigue crack initiation and total life: A quantitative study. *Eng. Fail. Anal.* **175**, 109611 (2025).
- <span id="page-22-27"></span>41. Zhao, L. H., Li, Q. C., Feng, J. Z. & Zheng, S. L. Service life prediction method for wheel-hub-bearing under random multi-axial wheel loading. *Eng. Fail. Anal.* **122**, 105211 (2021).
- <span id="page-22-28"></span>42. Chai, F., Li, Y., Liang, P. & Pei, Y. Calculation of the maximum mechanical stress on the rotor of interior Permanent-Magnet synchronous motors. *IEEE Trans. Industr. Electron.* **63**, 3420–3432 (2016).
- <span id="page-22-29"></span>43. Wang, S. et al. Failure analysis and accelerated test development for rotor magnetic Bridge of electric vehicle drive motor. *Appl. Sci.* **13**, 4753 (2023).
- <span id="page-22-30"></span>44. Guo, Y., Li, L., Gui, J. & Hu, S. Neural network approaches for real-time fatigue life Estimation by surrogating the rainflow counting method. *Int. J. Fatigue*. **197**, 108941 (2025).
- <span id="page-22-31"></span>45. Zare Banadkouki, M. R. Selection of strategies to improve energy efficiency in industry: A hybrid approach using entropy weight method and fuzzy TOPSIS. *Energy* **279**, 128070 (2023).
- <span id="page-22-32"></span>46. Zhu, J. X. & Au, S. K. Bayesian two-stage structural identification with equivalent formulation and EM algorithm. *Mech. Syst. Signal Process.* **209**, 111025 (2024).
- <span id="page-22-33"></span>47. Tang, F. et al. Thermal risk assessment in the mine of TOPSIS based on game theory subjective and objective comprehensive weighting. *Therm. Sci. Eng. Progress*. **59**, 103367 (2025).
- <span id="page-22-34"></span>48. Wang, Z., Zhao, L., Kong, Z., Yu, J. & Yan, C. Development of accelerated reliability test cycle for electric drive system based on vehicle operating data. *Eng. Fail. Anal.* **141**, 106696 (2022).

#### **Acknowledgements**

This research was partially supported by the National Natural Science Foundation of China under Grant 62303162 and by the Postdoctoral Fellowship Program of CPSF under Grant GZC20251194.

#### **Author contributions**

Z.W: Conceptualization, Methodology, Software, Investigation, Formal Analysis, Visualization, Writing - Origi-

nal Draft. Y.D.L: Conceptualization, Project Administration, Supervision. S.S.L: Supervision, Writing - Review & Editing. Y.D.H: Resources, Writing - Review & Editing. W.M.D: Data Curation, Resources. L.H.Z: Methodology, Resources, Validation. All authors reviewed and approved the final version of the manuscript before submission.

#### **Declarations**

#### **Competing interests**

The authors declare no competing interests.

#### **Additional information**

**Correspondence** and requests for materials should be addressed to Z.W. or L.Z.

**Reprints and permissions information** is available at www.nature.com/reprints.

**Publisher's note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

**Open Access** This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit [http://creativecommo](http://creativecommons.org/licenses/by-nc-nd/4.0/) [ns.org/licenses/by-nc-nd/4.0/.](http://creativecommons.org/licenses/by-nc-nd/4.0/)

© The Author(s) 2025
Contents lists available at [ScienceDirect](http://www.elsevier.com/locate/asoc)

# Applied Soft Computing

journal homepage: [www.elsevier.com/locate/asoc](http://www.elsevier.com/locate/asoc)

![](_page_0_Picture_5.jpeg)

# Remaining useful life prediction of rolling bearing under limited data based on adaptive time-series feature window and multi-step ahead strategy

![](_page_0_Picture_7.jpeg)

Weili Kong [a](#page-0-0) , Hai Li [b](#page-0-1),[∗](#page-0-2)

- <span id="page-0-0"></span><sup>a</sup> *West China Hospital, Sichuan University, Chengdu, 610064, China*
- <span id="page-0-1"></span>*School of Mechanical and Electrical Engineering, University of Electronic Science and Technology of China, Chengdu, 611731, China*

#### a r t i c l e i n f o

#### *Article history:* Received 31 January 2022 Received in revised form 1 September 2022 Accepted 14 September 2022 Available online 20 September 2022

*Keywords:* Rolling bearing Remaining useful life prediction Time-series feature window Limited data Multi-step ahead strategy

#### a b s t r a c t

Predicting the remaining useful life (RUL) of rolling bearings can effectively prevent the breakdown of rotating machinery systems and catastrophic accidents. Most existing RUL prediction methods require massive run-to-failure datasets for modeling. However, it is difficult to obtain these rolling bearing datasets, and for newly or recently deployed rolling bearings, the degradation data are limited with no failure data. Meanwhile, the distribution difference of degradation data of bearings under different working conditions is great, and it is a challenge to employ existing methods to predict RUL. According to the investigation, the health indicators of rolling bearings related to RUL increase exponentially with time. Motivated by this, a novel rolling bearing RUL prediction approach under limited data is proposed in this study. First, a first prediction time (FPT) identification method is developed to obtain the appropriate FPT. Then, the degradation factor is derived mathematically and used to adaptively compress the time-series feature window to better capture the degradation trends of rolling bearings. Subsequently, a stacked bidirectional long short-term memory network (SBiLSTM) is designed to predict and smoothen sequential data. Combined with the degradation factor and SBiLSTM, a multi-step ahead rolling prediction method is presented to predict RUL. Finally, several experiments are conducted on rolling bearings, and the mean absolute percentage error of the proposed method for three representative rolling bearings are 6.77%, 18.92%, and 8.95%, which are superior to other methods. Accordingly, this study contributes to revealing future degradation trends of rolling bearings mathematically, and providing a new idea for implementing other mechanical system prognostics under limited data.

© 2022 Elsevier B.V. All rights reserved.

# **1. Introduction**

<span id="page-0-3"></span>Rolling bearings are joint hubs of fixed and rotating parts in rotating machinery and play a critical role in industrial production [\[1,](#page-17-0)[2\]](#page-17-1). Faults commonly occur in rolling bearings as they operate under heavy loads and in high-speed environments. The failure of rolling bearings may lead to the breakdown of rotating machinery systems and even cause catastrophic accidents. However, the fault of rolling bearings is a gradual degradation process, and its fault does not occur suddenly [[3](#page-17-2)]. If the remaining useful life (RUL) of rolling bearings can be accurately predicted and these failures can be detected early, replacing damaged rolling bearings before accidents will help reduce machinery downtime and maintenance costs and arrange maintenance activities in a timely manner [\[4](#page-17-3)]. Owing to its importance, great efforts have

<span id="page-0-2"></span>∗ Corresponding author. *E-mail address:* [lhight@163.com](mailto:lhight@163.com) (H. Li). been made in rolling bearing RUL prediction in recent years, and a significant process has been achieved [[5](#page-17-4)[,6](#page-17-5)].

Rolling bearing RUL prediction models are generally divided into physics models, data-driven models and hybrid models. Physics models describe physical phenomena based on failure mechanisms by establishing mathematical models, such as Paris Law [\[7\]](#page-17-6) and mechanics [\[8\]](#page-17-7). Although it has high interpretability and prediction accuracy, the construction of physics models is expensive and time-consuming. Meanwhile, establishing an accurate physics model of a complex mechanical system is also a challenge. To address the above problems, data-driven models are widely applied to predict bearing RUL, including filtering-based methods [[9\]](#page-17-8), Wiener process [[10](#page-17-9)], Gaussian process regression [[11](#page-17-10)], artificial neural network [[12](#page-17-11)], support vector machine [\[13](#page-17-12)] and transfer learning [\[14\]](#page-17-13). These methods can adaptively learn the input–output relationship of complex systems using monitoring data and do not establish physics models. However, they need massive run-to-failure datasets to train prediction models and the parameter determination of data-driven models is difficult and time-consuming. Additionally, to integrate the advantages of physics models and data-driven models, hybrid models are considered as a new research direction, such as phase space warping and Paris crack growth [[15](#page-17-14)] and deep convolutional neural network and particle filtering [\[16](#page-17-15)]. The hybrid model has a better generalization ability, but it also requires large run-to-failure datasets and parameter optimization.

Although satisfactory results have been achieved by the abovementioned methods, most existing studies ignore the following problems, which limits their applications.

- (1) Due to the large amount of funds and time required to collect whole-life monitoring data of rolling bearings, it is difficult to obtain massive run-to-failure datasets of rolling bearings [\[17\]](#page-17-16).
- (2) To avoid damaging high-value machinery, rolling bearing failures are considered unacceptable, resulting in no failure data. Moreover, only a few data are available for new or recently deployed rolling bearings [18]. Therefore, limited data are common in the field of rolling bearing health prognostics.
- (3) Due to the influence of the operating environment, manufacturing errors, bearing materials and other factors, the data distribution of bearing degradation signals under different working conditions is quite different [\[18\]](#page-17-17). Therefore, when the mode established in one working condition is applied to another, its prediction accuracy is greatly reduced.

The above problems reveal that limited data are common in mechanical prognostics, and bearing RUL prediction under limited data is truly significant and highly challenging. To the best of our knowledge, most rolling bearing RUL prediction models have been established using massive run-to-failure data. If such failure data are unavailable and degradation data are limited, it is difficult for these methods to accurately track the bearing degradation process, resulting in a large RUL prediction error. However, to date, there are few studies on rolling bearing RUL prediction under limited data [[19](#page-17-18)].

According to our research and investigation, it is found that the degradation indicators of rolling bearings related to RUL increase exponentially with time, and the more serious the degradation is, the faster the indicator increases [\[20\]](#page-17-19). Therefore, if the increasing trend of degradation indicator is revealed, the rolling bearing degradation trend can be analyzed. Motivated by this, this study presents a rolling bearing RUL prediction method under limited data by analyzing the increasing trend of the degradation indicator. The main novelty can be concluded as follows.

- (1) A novel method for predicting rolling bearing RUL using limited data is proposed.
- (2) An adaptive time-series feature window is developed by using degradation factor derived mathematically to describe the degradation process of rolling bearings.
- (3) A multi-step ahead rolling prediction method of sequential data is presented based on stacked bidirectional LSTM and degradation factor to predict degradation trends.

Through the above analysis, this paper has the following contributions.

- (1) This study contributes to predicting rolling bearing RUL under limited data and providing a new idea for implementing other mechanical system prognostics.
- (2) This study contributes to revealing future degradation trends of rolling bearings mathematically and accurately monitoring their working conditions by constructing time-series feature windows.
- (3) This study contributes to providing an effective strategy for predicting sequential data of rolling bearing degradation with limited data availability.

The remainder of this paper is organized as follows. Section [2](#page-1-0) presents a brief review of related work. Section [3](#page-2-0) presents the framework of the proposed method. Section [4](#page-8-0) conducts several experiments on rolling bearings. Section [5](#page-16-0) concludes the paper.

# **2. Related works**

<span id="page-1-0"></span>This section presents a brief review of related work on rolling bearing RUL prediction methods, and these methods are divided into three types, including physics model, data-driven model and hybrid model.

#### *2.1. Physics model*

Physics models attempt to describe physical phenomena based on failure mechanisms by establishing mathematical models [\[21\]](#page-17-20). Paris law, which is widely used as the fatigue crack growth model, can reflect the failure mechanism of materials and is usually used as a method to predict RUL. Liao et al. [[7](#page-17-6)] employed a continuous Bayesian method that assumes fault growth following Paris Law to realize RUL prediction. To solve the measurement of variables in Paris law online, Dong et al. [[22\]](#page-17-21) integrated empirical mode decomposition and RMS into the Paris law to realize bearing RUL prediction. In addition, by analyzing the effect of the impact force and friction force on bearing wear, El-thalji and Jantunen [[8\]](#page-17-7) studied the change in the tribological and topographical properties over the lifetime and then established a dynamic wear evolution model. The physics models of RUL prediction of bearings have the characteristics of strong interpretability and superior prediction accuracy. However, in practice, the construction of these models is time-consuming and expensive, and their reusability is limited. In addition, due to the complex failure mechanism of complex machinery, it is difficult to construct an accurate mathematical model of complex machinery. Moreover, physics models have a large number of parameters, and parameter estimation is also a challenge [\[23\]](#page-17-22). Therefore, physics models have some limitations due to their inherent characteristics.

# *2.2. Data-driven model*

Data-driven models contain three steps: data acquisition, health indicator construction and RUL prediction method. In data acquisition, multiple sensory signals are considered, such as vibration signals [\[18,](#page-17-17)[19](#page-17-18)] and acoustic signals [\[24,](#page-17-23)[25](#page-17-24)]. Subsequently, health indicators will be constructed to monitor the degradation of rotating machinery, including root mean square [[26](#page-17-25)], variational mode decomposition [[27\]](#page-17-26), mathematical morphology spectrum entropy [\[28\]](#page-17-27) and principal component analysis [[29](#page-17-28)]. On this basis, RUL prediction methods are employed to obtain RUL. Traditionally, data-driven RUL prediction methods are divided into statistical models and artificial intelligence models.

# *2.2.1. Statistical model*

Statistical models assume that the degradation process of rolling bearings obeys a certain mathematical function and distribution, and then the parameters of the corresponding function and distribution are optimized using all degradation data [\[30\]](#page-17-29). On this basis, the trained statistical model is employed to predict the RUL of rolling bearings. Liu et al. [\[12\]](#page-17-11) employed a Kalman filter (KF) to recursively estimate the degradation state of rolling bearings and then achieved RUL prediction using an expectation maximization algorithm. To effectively process monitoring data of different stages, Cui et al. [[31](#page-17-30)] developed an automatic switching method of filtering models, and then proposed a time-varying KF to predict RUL of rolling bearings. Different from the KF method, the particle filter (PF) uses a group of particles with specific weights to approximate the stage estimation. Liu et al. [\[32\]](#page-17-31) utilized the basic PF to predict bearing RUL. To solve the poor generalization ability of PF, Cui et al. [[33](#page-17-32)] achieved rolling bearing RUL prediction by using a time-vary KF method. Combining the advantages of PF and KF, Du et al. [[16\]](#page-17-15) presented the unscented PF to establish a time-varying degradation model to predict bearing RUL. In addition, to effectively solve the randomness of measured information, stochastic filtering (SF) is developed. Zhang et al. [[34\]](#page-17-33) proposed a two-stage SF model to measure the relationship between the Bayesian-inferred distance and RUL, so as to achieve online dynamic RUL prediction. In addition to filtering algorithms, other statistical-based methods are also employed to predict RUL. To address the problem of the nonstationary characteristics of vibration signals, Ment et al. [\[35\]](#page-18-0) integrated empirical mode decomposition (EMD) based on differential and gray Markov model to predict RUL, and the results demonstrated that the fractal spectrum is beneficial for improving prediction accuracy. Li et al. [[10](#page-17-9)] proposed a Wiener-based RUL prediction method using KF algorithm, and then presented an adaptive modification method to further reduce prediction error. To further solve the measuring error and stochasticity of degradation stages, Guan et al. [[36](#page-18-1)] employed the Wiener process to predict RUL, and the KF and expectation maximization algorithm were utilized to estimate variables and model parameters. Moreover, Lu et al. [\[37\]](#page-18-2) proposed a three-phase prognostic algorithm to assess reliability, and a proportional hazard model (PH) was generated to forecast bearing RUL. Additionally, regression-based statistical models are also used to predict bearing RUL. Wang et al. [[38](#page-18-3)] employed exponential degradation models coupled with the Frechet distance to adaptively estimate RUL. To get more accurate RUL prediction results, the gradient descent method was utilized to optimize the exponential model [[20](#page-17-19)]. Furthermore, to effectively solve the RUL prediction problem with small and high-dimensional datasets, Kumaraswamidhas et al. [[11](#page-17-10)] developed a health degradation indicator based on Kullback–Leibler and then utilized Gaussian process regression (GPR) with a 95% confidence interval to realize bearing RUL prediction.

# *2.2.2. Artificial intelligence model*

Artificial intelligence model (AI) is the most widely used RUL prediction method for rolling bearings, and has the advantages of strong applicability and high prediction accuracy. This method does not need to establish a physics model, and only employs degradation data to construct the input–output relationship, which is an effective technique to solve the problem of RUL prediction model construction for complex systems. Accordingly, various RUL prediction methods of rolling bearings have been proposed in recent decades. Neural network and its many derivative algorithms are critical methods in the field of artificial intelligence. Huang et al. [[12\]](#page-17-11) employed a self-organizing map to generate a health indicator and then utilized backpropagation neural network (BPNN) to predict the bearing RUL. Pan et al. [\[39\]](#page-18-4) presented the relative root mean square to divide the operation stage into two stages and the multivariable feedback extreme learning machine model (ELM) was constructed to realize bearing RUL prediction. Li et al. [[40](#page-18-5)] developed a data alignment method to reduce the distribution discrepancy between different machines and then employed generative adversarial networks to estimate bearing RUL. Yu et al. [[41](#page-18-6)] employed ensemble EMD to process the decomposed vibration signal, and the multiscale attention mapping strategy was employed in residual neural network (RNN) to achieve RUL prediction. Furthermore, to accurately capture temporal information, recurrent neural network is introduced. Que et al. [[42](#page-18-7)] constructed a stacked gated recurrent unit network to predict bearing RUL and a Bayesian approach was employed to analyze the prediction uncertainty. Meanwhile, Long–short term memory (LSTM) and its derivative algorithms were also introduced to perform bearing RUL prediction tasks [[43](#page-18-8)[,44\]](#page-18-9). In addition to neural networks, support vector machine (SVM) is also widely utilized to achieve bearing RUL prediction [[13](#page-17-12)[,45\]](#page-18-10).

Moreover, deep learning and its extended algorithms have developed rapidly in recent years. These algorithms have been successfully applied to perform bearing RUL prediction tasks, which can establish the complex nonlinear relationship between raw sensor data and achieve satisfactory results. Wang et al. [\[46\]](#page-18-11) constructed a health indicator by deep convolutional autoencoder and self-organizing map. On this basis, a one-dimensional convolutional neural network (1D-CNN) is used to predict bearing RUL. Wang et al. [\[47\]](#page-18-12) also used a 1D-CNN and empirical wavelet transform to obtain RUL prediction results. To more sufficient and comprehensive extract features, an improved deep CNN (DCNN) with the dual-channel input from the time and frequency domains in parallel is developed to predict RUL [[48](#page-18-13)]. Besides, Ding et al. [[49](#page-18-14)] combined the DCNN model without a pooling layer and 3-sigma criterion to implement bearing RUL prediction. To improve the generalization ability of data-driven models, transfer learning (TL) is attracting more and more researcher's research interest. According to investigations, TL is usually utilized to perform classification tasks, such as bearing fault diagnosis [\[50\]](#page-18-15). There are only a few references about the application of TL to bearing RUL prediction [[51](#page-18-16)[–54\]](#page-18-17). However, a small number of datasets and a larger distribution discrepancy will greatly restrict the effect of TL [[54](#page-18-17)].

In general, statistical models require less parameter information than physics models. However, these models need to assume that the degradation process of rolling bearings satisfies a given mathematical function or distribution. If these assumptions are inappropriate, the RUL prediction performance will be poor. Additionally, data-driven models require massive run-to-failure datasets to construct models. If the failure data are unavailable and the whole-life degradation data are limited, the datadriven models have difficulty capturing the degradation process of rolling bearings, resulting in a large RUL prediction error.

# *2.3. Hybrid model*

Owing to the disadvantages and advantages of physics and data-driven models, hybrid models attempt to integrate the advantages of different models to predict rolling bearing RUL. Qian et al. [\[15\]](#page-17-14) presented an enhanced phase space warping method to establish a correlation between defect growth variables and vibration signals. This research achieved real-time rolling bearing RUL prediction based on a modified Paris crack growth model with a time-piecewise approach. Maio et al. [[55](#page-18-18)] employed relevance vector machines (RVM) to select basis functions, and then used exponential regression to compute bearing RUL. Liu et al. [[16](#page-17-15)] utilized DCNN to construct a deterioration index of bearings based on vibration monitoring data, and PF was employed to estimate the bearing RUL.

Through the above review (see [Table](#page-3-0) [1](#page-3-0)), it can be found that most existing methods require massive run-to-failure datasets to establish prediction models. However, limited data are common in the field of rolling bearing prognostics. In such cases, the existing RUL prediction methods have difficulty achieving accurate prediction results. Therefore, developing a novel rolling bearing RUL prediction method under limited data is necessary.

# **3. Proposed approach for rolling bearing RUL prediction under limited data**

#### <span id="page-2-0"></span>*3.1. Systematic overview*

Limited data are common in the field of machinery health prognostics [\[19\]](#page-17-18). There are two scenarios of limited data: the ''Known–Unknown'' scenario and the ''Unknown-Known– Unknown'' scenario, as shown in [Fig.](#page-3-1) [1.](#page-3-1) The rolling bearing RUL

<span id="page-3-0"></span>**Table 1** Related works on bearing RUL prediction methods.

| Type                 | Method                                                                                                                                                                                                                            | Advantage                                                                                                                                   | Disadvantage                                                                                                                                                                                                                        |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Physics<br>model     | Paris Law [7,22], Mechanics [8]                                                                                                                                                                                                   | • Has high interpretability.<br>• Has high prediction accuracy.                                                                             | • Difficult to establish physics models for complex<br>mechanical system.<br>• Expensive and time-consuming to construct<br>physics model.<br>• Has poor reusability.                                                               |
| Data-driven<br>model | • Statistical model:<br>KF [31], PF [16], SF [34], Markov [35],<br>Wiener process [36], PH [37], GPR<br>[11], Exponential regression [38]<br>• Artificial model:<br>BPNN [12], ELM [39], RNN [41], SVM<br>[45], CNN [46], TL [51] | • Does not require much prior knowledge<br>about physics models.<br>• Adaptively learn the input–output<br>relationship of complex systems. | • Effect greatly restricted by distribution discrepancy<br>of datasets.<br>• Requires a large number of run-to-failure datasets<br>to train prediction model.<br>• Difficult and time-consuming to determine model's<br>parameters. |
| Hybrid<br>model      | PSW and Paris crack growth [15],<br>RVM and exponential regression [55],<br>DCNN and PF [16]                                                                                                                                      | • Integrates the advantage of physics and<br>data-driven models.<br>• Has better generalization ability.                                    | • Requires a large number of run-to-failure datasets<br>to train prediction model.<br>• Difficult and time-consuming to determine model's<br>parameters.                                                                            |

![](_page_3_Figure_4.jpeg)

**Fig. 1.** Two scenarios under limited data availability for rolling bearing RUL prediction.

<span id="page-3-1"></span>will be obtained when the sensitive feature *F<sup>t</sup>* exceeds the failure threshold (*FFT* ).

This study aims to predict RUL of rolling bearings under limited data, and [Fig.](#page-4-0) [2](#page-4-0) illustrates its flowchart. The proposed method mainly contains the following three parts.

- (1) Part 1 proposes a first prediction time (FPT) identification method. The kurtosis and root mean square (RMS) are extracted first by collecting the raw vibration signals. Owing to the strong sensitivity of kurtosis and RMS to rolling bearing degradation, an FPT determination method based on kurtosis and RMS is presented to obtain the appropriate FPT.
- (2) Part 2 constructs the adaptive time-series feature window. This study selects RMS as the sensitive feature, and the sensitive feature within a period of time are used to construct the time-series feature window, which is dynamically compressed to better describe the local degradation process of rolling bearings.
- (3) Part 3 develops a multi-step ahead rolling prediction method. This method is triggered at FPT, and the information in the compressed feature windows will be utilized to construct a stacked BiLSTM network. Subsequently, the RUL of rolling bearing will be predicted using the rolling prediction method.

#### *3.2. First prediction time identification*

<span id="page-3-3"></span>For a rolling bearing, an entire cycle of the vibration signal includes the health and degradation stages, as shown in [Fig.](#page-4-1) [3.](#page-4-1) The amplitude changes of vibration signals before and after the red line show two different trends. Before the red line, the amplitude change is small. In contrast, after the red line, the amplitude gradually increases, which indicates that the rolling bearing performance is gradually degraded. Therefore, the red line divides the operation condition of the rolling bearing into health and degradation stages, and its position is the start time for executing the prediction method, which is called FPT.

In addition, if the RUL prediction method is performed before the FPT, the prediction error will be large and meaningless. After the FPT, the rolling bearing enters the degradation stage and it is meaningful to predict the RUL in this stage. The existing research shows that the kurtosis value obtained from the vibration signal can effectively indicate the occurrence of early faults [[56](#page-18-19)]. However, as kurtosis is very sensitive to noise, FPT will be identified earlier if kurtosis is utilized as the only indicator to determine FPT, making it difficult to accurately capture the real degradation. Moreover, RMS has better robustness to noise and is employed as the indicator to determine FPT [[57](#page-18-20)], but RMS cannot identify transient impact. Therefore, RMS and kurtosis should be utilized synthetically to determine FPT. The identification process of FPT is as follows:

(1) Compute the RMS (*RMSt*) and kurtosis (*Kurt*) of the vibration signals at time *t*.

<span id="page-3-2"></span>
$$RMS = \sqrt{\frac{1}{n} \sum_{i=1}^{n} x_i^2} \tag{1}$$

$$Kur = \frac{1}{n} \sum_{i=1}^{n} x_i^4 \tag{2}$$

where *x<sup>i</sup>* represents the raw vibration signal at time *i*.

![](_page_4_Figure_2.jpeg)

**Fig. 2.** Illustration of the proposed RUL prediction method with limited data.

<span id="page-4-0"></span>![](_page_4_Figure_4.jpeg)

**Fig. 3.** Raw vibration signal.

- <span id="page-4-1"></span>(2) Calculate the normal range [µ − σ, µ + σ] of kurtosis and RMS using all signals before *t*, where σ and µ represent the standard deviation and mean value of vibration signals, respectively.
- (3) If *Kur<sup>t</sup>* and *RMS<sup>t</sup>* exceed the normal range after three consecutive abnormal points, as shown in [Fig.](#page-5-0) [4](#page-5-0), this time will be selected as the FPT, that is, FPT = *t*−2. Otherwise, return to step (1) and *t* = *t* + 1.

$$\{|Kur_{t-i} - \mu| > \sigma \& |RMS_{t-i} - \mu| > \sigma\}_{i=0,1,2}$$
 (3)  
(4) Output FPT.

# *3.3. Adaptive time-series feature window*

# *3.3.1. Rolling bearing degradation factor*

The values of feature of rolling bearings (i.e., RMS) increases exponentially with time from normal service to serious failure [\[20\]](#page-17-19). Accordingly, the feature value *F<sup>t</sup>* can be expressed as

$$F_t = \varphi_0 \exp(\kappa(t)) \tag{4}$$

where *F<sup>t</sup>* represents the feature value at time *t*. κ(*t*) is determined by the rolling bearing operating condition at time *t*. ϕ<sup>0</sup> and κ ([1\)](#page-3-2) are equal to *F*<sup>1</sup> and 0, respectively.

Based on Eq. [\(4](#page-4-2)), the relationship between the values of the feature at time *t*−1 and *t* is given as

<span id="page-4-3"></span>
$$IP_t = \frac{F_t}{F_{t-1}} = \exp(g(t)), \text{ where } g(t) = \kappa(t) - \kappa(t-1)$$
 (5)

where *g*(*t*) and *IP<sup>t</sup>* denote the degradation factor and increase factor at time *t*, respectively.

From Eqs. ([4](#page-4-2)) and ([5](#page-4-3)), it can be observed that *g*(*t*) has a significant effect on determining *IP<sup>t</sup>* and *F<sup>t</sup>* . Accordingly, exploring an effective method for determining *g*(*t*) is necessary. In particular, when the values of feature at time *t*−1 and *t* are close, *g*(*t*) is very small and even close to zero. Therefore, the relationship between *IP<sup>t</sup>* and *g*(*t*) can be further established based on Taylor expansion [\[58](#page-18-21)].

$$\lim_{g(t)\to 0} IP_t = \exp(g(t)) \propto (1+g(t)) \tag{6}$$

In addition, the values of feature at time *t* (*Ft*) and failure time *FT* (*FFT* ) are expressed as

$$F_{t} = F_{1} \prod_{u=1}^{t} IP_{u}$$

$$F_{FT} = F_{FPT} \prod_{n=1}^{FT - FPT} IP_{n} \le F_{FPT}$$

$$(7)$$

<span id="page-4-5"></span><span id="page-4-4"></span>
$$\times \left(\max\left(IP_{FPT+1}, IP_{FPT+2}, \dots, IP_{FT-FPT-1}\right)\right)^{FT-FPT-1} \tag{8}$$

where *FT* and *FPT* represent the failure time and first prediction time, respectively. *FFT* and *FFPT* denote the feature value at *FT* and *FPT*, respectively. *max*(•) is the maximum of all elements.

<span id="page-4-2"></span>Furthermore, the feature threshold ratio (*FTR*) *a<sup>t</sup>* is introduced for measuring the proximity degree of *F<sup>t</sup>* to *FFT* . *a<sup>t</sup>* can be defined

![](_page_5_Figure_2.jpeg)

![](_page_5_Figure_3.jpeg)

(b) Enlargement from t=70 to t=85

Fig. 4. Diagram of the first prediction time.

<span id="page-5-0"></span>![](_page_5_Figure_6.jpeg)

<span id="page-5-1"></span>Fig. 5. Relationship between the feature window and start prediction time.

as

$$a_{t} = \frac{F_{t}}{F_{FT}} = \frac{F_{1} \prod_{m=1}^{t-1} IP_{m}}{F_{1} \prod_{n=1}^{FT-FPT} IP_{n}} = \frac{\prod_{m=1}^{t-1} IP_{m}}{\prod_{\mu=1}^{FT-FPT-1} IP_{u}} \cdot \frac{IP_{t}}{IP_{FT-FPT}}$$

$$\geq \frac{(1+g(t))}{(1+g_{\text{max}})}$$
(9)

$$g(t) \le a_t \times g_{\text{max}} \tag{10}$$

where  $g_{max}$  is the maximum degradation factor and  $a_t$  is [0,1]. Combined with Eqs. (6) and (8), g(t) can be further computed by

$$g(t) \le a_t \times \left( \left( \frac{F_{FT}}{F_{FPT}} \right)^{\frac{1}{FT - FPT - 1}} - 1 \right), \text{ where}$$

$$g_{\text{max}} = \left( \left( \frac{F_{FT}}{F_{FPT}} \right)^{\frac{1}{FT - FPT - 1}} - 1 \right)$$
(11)

#### 3.3.2. Time-series feature window construction without outliers

<span id="page-5-3"></span>In this section, the time-series feature window  $\mathbf{M}$  is proposed to capture the degradation trends of rolling bearings.  $\mathbf{M} = [F_1, F_2, \ldots, F_i, \ldots, F_{n^l}]$  is a typical time-series feature window, and its length is  $n^l$ , which represents the total number of samples of the selected feature in a feature window. It should be noted that the total number of samples in different feature windows is the same.

Moreover, to further evaluate the increasing trend of two adjacent feature windows, this study proposes the increase rate R based on the geometric mean. Fig. 5 pictures the relationship among the start prediction time SP ( $SP \ge FPT$ ), two feature windows  $M_{01}$  and  $M_{02}$ , and the length of a feature window  $n_0^l$ .

The two initial feature window  $M_{01}$  and  $M_{02}$ , initial degradation factor  $g_0$  and initial increase rate  $R_0$  are defined as follows:

$$\mathbf{M}_{01} = [F_{SP-2n_0^l+1}, F_{SP-2n_0^l+2}, \dots, F_{SP-n_0^l}]$$

$$\mathbf{M}_{02} = [F_{SP-n_0^l+1}, F_{SP-n_0^l+2}, \dots, F_{SP}]$$
(12)

where  $M_{01}$  and  $M_{02}$  are the first and second initial feature windows before *SP*, respectively.  $n_0^l$  is the length of an initial feature window

$$g_0 \le \frac{\sum_{i=1}^{n_0^l} F_{SP-n_0^l+i}}{n_0^l} \times \left( \left( \frac{F_{FT}}{F_{FPT}} \right)^{\frac{n_0^l}{FT-FPT-1}} - 1 \right)$$
 (13)

$$R_0 = \sqrt[n_0^l] \prod_{i=1}^{n_0^l} \left( F_{SP-n_0^l+i} / F_{SP-2n_0^l+i} \right)$$
 (14)

<span id="page-5-4"></span>From the definition of the feature window, degradation factor and increase rate, it can be seen that the length of the feature window  $n^l$  is critical to determine them, which also determines the total number of samples of the selected feature in the feature window. On the one hand, if the length is very small, the total number of samples contained in the feature window is small. Although this can simplify the computational complexity of the whole prediction process, the local degradation trends of rolling bearings are difficult to capture due to the small number of training samples. However, if the length is very large, the total number of samples contained in the feature window will also be large. In this case, RUL prediction will overly depend on the global trend, and the local degradation trend of rolling bearings is also difficult to monitor. Meanwhile, the large length makes the calculation of feature window complicated and consumes more computational resources. Therefore, the length should be adjusted dynamically according to the changing trend of the selected feature.

To solve the above problems, the degradation factor and increase rate R are used to dynamically determine the length of the feature window. If  $(1+g_0(SP))$  is smaller than  $R_0$ , the initial feature window does not need to be compressed. In contrast, if  $(1+g_0(SP))$  is greater than  $R_0$ , two adjacent feature windows should be gradually compressed from  $SP-2 \times n_0^l$  to SP in a step of 1 until  $R_k$  is greater than  $(1+g_0(SP))$  or the length of feature window reaches the minimum compression limit  $n_{kl}^l$ . The feature windows, degradation factor and increase rate after the kth compression are expressed in Eqs. (15)-(17), and Fig. 6 illustrates their relationship.

<span id="page-5-2"></span>
$$\mathbf{M}_{k1} = [F_{SP-2n_k^l+1}, F_{SP-2n_k^l+2}, \dots, F_{SP-n_k^l}] 
\mathbf{M}_{k2} = [F_{SP-n_k^l+1}, F_{SP-n_k^l+2}, \dots, F_{SP}]$$
(15)

where  $M_{k1}$  and  $M_{k2}$  are the first and second feature windows after kth compression before SP, respectively.  $n_k^l$  is the length of

![](_page_6_Figure_2.jpeg)

<span id="page-6-1"></span>Fig. 6. Time-series feature window compression process.

![](_page_6_Figure_4.jpeg)

<span id="page-6-2"></span>Fig. 7. Time-series feature window encompassing outliers.

the feature window after kth compression.

$$g_k \le \frac{\sum_{i=1}^{n_k^l} F_{SP-n_k^l+i}}{n_k^l} \times \left( \left( \frac{F_{FT}}{F_{FPT}} \right)^{\frac{n_k^l}{FT-FPT-1}} - 1 \right)$$
 (16)

$$R_{k} = \sqrt[n_{k}^{l}]{\prod_{i=1}^{n_{k}^{l}} \left(F_{SP-n_{k}^{l}+i}/F_{SP-2n_{k}^{l}+i}\right)}$$
(17)

where  $g_k$  and  $R_k$  represent the degradation factor and increase rate after kth compression, respectively.

#### 3.3.3. Time-series feature window construction with outliers

<span id="page-6-6"></span>The increase rate R has a significant effect on the construction of the time-series feature window. In Section 3.3.2, the feature windows will be compressed if  $(1 + g_0(SP))$  is larger than  $R_0$ . Otherwise, the initial feature window does not need to be compressed. However, when outliers appear in the initial or compressed feature windows,  $(1 + g_{max})$  may be smaller than  $R_0$ . Here, a point whose feature value rapidly increases or decreases in a feature window will be identified as an outlier, such as outlier  $F_{SP-n_k^l+1}$  in Fig. 7, and this feature window will be identified as an outlier region, such as outlier region  $M_{k2}$ . If the feature window encompassing the outliers is not properly compressed, the feature window M, FTR and RUL prediction results will be inaccurate.

To address the problem of outliers in the feature window, this study develops a method for constructing time-series feature windows containing outliers. The identification of the outlier

![](_page_6_Figure_13.jpeg)

<span id="page-6-5"></span><span id="page-6-3"></span>**Fig. 8.** Relationships between  $M_{s1}$ ,  $M_{s2}$ ,  $M_k$ ,  $n_k^l$  and  $n_s^l$ .

region should simultaneously satisfy the following two conditions shown in Eqs. (18) and (19).

$$C(k) = \frac{\sum_{i=1}^{n_k^l} \left( F_{SP-n_k^l+i} - \operatorname{mean} \left( F_{W_{k2}} \right) \right)^2}{\sum_{i=1}^{n_k^l} \left( F_{SP-2n_k^l+i} - \operatorname{mean} \left( F_{W_{k1}} \right) \right)^2} > 1 \text{ or}$$

$$C(k) = \frac{\sum_{i=1}^{n_k^l} \left( F_{SP-2n_k^l+i} - \operatorname{mean} \left( F_{W_{k1}} \right) \right)^2}{\sum_{i=1}^{n_k^l} \left( F_{SP-n_k^l+i} - \operatorname{mean} \left( F_{W_{k2}} \right) \right)^2} > 1$$
(18)

<span id="page-6-4"></span>
$$Min(\mathbf{M}_{k2}) > Max(\mathbf{M}_{k1}) \text{ or} Min(\mathbf{M}_{k1}) > Max(\mathbf{M}_{k2})$$
(19)

where C(k) denotes the increase coefficient between two adjacent feature windows. The  $min(\bullet)$  is the minimum of all elements.

If outliers exist in a feature window after kth compression, this feature window will also be continuously compressed until two conditions are satisfied or the length of the feature window reaches a given minimum limit  $n_{sl}^l$ , and  $M_{k2}$  is divided into  $M_{s1}$  and  $M_{s2}$ , which is called the outlier process method. The relationships among  $n_k^l$ ,  $n_s^l$  (where  $n_s^l = \lfloor n_k^l/2 \rfloor$ ),  $M_k$ ,  $M_{s1}$  and  $M_{s2}$  are shown in Fig. 8.

<span id="page-6-0"></span>After the completion of the outlier process,  $M_{s1}$ ,  $M_{s2}$ ,  $R_s$  and  $g_s$  are calculated as follows:

$$\mathbf{M}_{s1} = [F_{SP-2n_s^l+1}, F_{SP-2n_s^l+2}, \dots, F_{SP-n_s^l}] 
\mathbf{M}_{s2} = [F_{SP-n_s^l+1}, F_{SP-n_s^l+2}, \dots, F_{SP}]$$
(20)

where  $M_{s1}$  and  $M_{s2}$  are the first and second feature windows after the outlier process before *SP*, respectively.  $n_s^l$  is the length of the feature window after outlier process.

$$g_{s} \leq \frac{\sum_{i=1}^{n_{s}^{l}} F_{SP-n_{s}^{l}+i}}{n_{s}^{l}} \times \left( \left( \frac{F_{FT}}{F_{FPT}} \right)^{\frac{n_{s}^{l}}{FT-FPT-1}} - 1 \right)$$
 (21)

$$R_{s} = \sqrt[n]{\sum_{i=1}^{n_{s}^{l}} \left( F_{SP-n_{s}^{l}+i} / F_{SP-2n_{s}^{l}+i} \right)}$$
 (22)

where  $g_s$  and  $R_s$  represent the degradation factor and increase rate after outlier process, respectively.

Based on the above analysis, the final length of the feature window  $n_f^l$ , feature window  $M_f$ , degradation factor  $g_f$  and increase rate  $R_f$  are derived as follows:

$$\begin{split} n_f^l &= \begin{cases} &n_0^l \quad R_0 \in [1+g_0(SP), 1+g_{\text{max}}] \\ &n_k^l \quad \text{without outlier, } R_0 \in (-\infty, 1+g_0(SP)) \\ &\text{ or } R_0 \in (1+g_{\text{max}}, +\infty) \\ &\text{ and } R_k \in [1+g_0(SP), 1+g_{\text{max}}] \end{cases} \\ &n_s^l \quad \text{with outlier} \end{cases} \\ &\mathbf{M_0} \quad R_0 \in [1+g_0(SP), 1+g_{\text{max}}] \\ &\mathbf{M_k} \quad \text{without outlier, } R_0 \in (-\infty, 1+g_0(SP)) \\ &\text{ or } R_0 \in (1+g_{\text{max}}, +\infty) \\ &\text{ and } R_k \in [1+g_0(SP), 1+g_{\text{max}}] \end{cases} \\ &\mathbf{M_s} \quad \text{with outlier} \end{cases} \\ &\left[ \frac{\sum_{i=1}^{n_0^l} F_{SP-n_0^l+i}}{n_0^l} \right] \\ &\times \left( \left( \frac{F_{FT}}{F_{FPT}} \right)^{\frac{n_0^l}{FT-FPT-1}} - 1 \right) \quad R_0 \in [1+g_0(SP), 1+g_{\text{max}}] \right. \\ &\left. \sum_{i=1}^{n_s^l} F_{SP-n_s^l+i}}{n_s^l} \right. \\ &\left. \times \left( \left( \frac{F_{FT}}{F_{FPT}} \right)^{\frac{n_s^l}{FT-FPT-1}} - 1 \right) \quad \text{without outlier,} \\ &\left. R_0 \in (-\infty, 1+g_0(SP)) \\ &\text{ or } R_0 \in (1+g_{\text{max}}, +\infty) \text{ and} \\ &R_k \in [1+g_0(SP), 1+g_{\text{max}}] \right. \\ &\left. \times \left( \left( \frac{F_{FT}}{F_{FPT}} \right)^{\frac{n_s^l}{FT-FPT-1}} - 1 \right) \quad \text{with outlier} \right. \\ &R_0 = R_0 \in [1+g_0(SP), 1+g_{\text{max}}] \\ &R_k \quad \text{without outlier,} \quad R_0 \in (-\infty, 1+g_0(SP)) \\ &\text{ or } R_0 \in (1+g_{\text{max}}, +\infty) \\ &\text{ and} \quad R_k \in [1+g_0(SP), 1+g_{\text{max}}] \\ &R_s \quad \text{with outlier} \end{cases} \end{aligned}$$

#### 3.4. Multi-step ahead rolling prediction

#### 3.4.1. Stacked bidirectional LSTM neural network

<span id="page-7-2"></span>The performance degradation of rolling bearings is a gradual process, and the performance degradation at the current moment can be estimated from the performance degradation at subsequent and previous moments. Here,  $NF_t$  is the normalized value of the selected feature at time t. Therefore, when training the rolling bearing RUL prediction model, the previous and future data should be fully utilized to optimize the current data. To process sequential information effectively, long short term memory (LSTM) algorithm is proposed. However, this algorithm can only process the forward information [59]. In addition, to independently process sequential data in backward and forward paths, a bidirectional LSTM (BiLSTM) was proposed to predict tool wear [60]. This study proposes a stacked BiLSTM (SBiLSTM) to better predict rolling bearing RUL, as shown in Fig. 9, which employs the previous and future data to optimize the current data and stacks multiple BiLSTMs simultaneously.

There are two paths in the SBiLSTM network. The forward path and backward path are employed to predict future information and smooth the prediction results obtained in the forward path, respectively. The outputs of these paths are concatenated and then fed forward to the input of the next layer. According to the final feature window  $\mathbf{M_f}$ , the input and output of SBiLSTM network are  $M_{f1} = \begin{bmatrix} F_{SP-2n_f^l+1}, F_{SP-2n_f^l+2}, F_{SP-2n_f^l+3}, \dots, F_{SP-n_f^l} \end{bmatrix}$  and  $M_{f2} = \begin{bmatrix} F_{SP-n_f^l+1}, F_{SP-n_f^l+2}, F_{SP-n_f^l+3}, \dots, F_{SP} \end{bmatrix}$ , respectively.

### 3.4.2. Multi-step ahead rolling prediction

<span id="page-7-3"></span>Before training the SBiLSTM network,  $NF_t = (F_t - mean(\mathbf{M_f}))/$  $standard(M_f)$  is used to normalize  $M_{f1}$  and  $M_{f2}$  to obtain  $NF_{f1}$ and  $NF_{f2}$ , respectively, where  $standard(\bullet)$  represents the standard deviation function and *mean*(●) denotes the mean function. Then,  $NF_{f1}$  and  $NF_{f2}$  are utilized to train the SBiLSTM model, and  $NF_{f2}$ will be employed to perform rolling prediction strategy, as shown in Fig. 10. Generally, the one-step and multi-step are commonly used rolling ahead prediction strategies [61,62]. The one-step strategy gets only one point at each iteration, which makes it difficult to reflect the temporal characteristics of the prediction results, as shown in Eq. (24). Meanwhile, when a feature window contains a large number of samples, more computing resources and running time are needed to train a one-step rolling prediction model. Accordingly, a multi-step rolling ahead prediction strategy is adopted in this study, as shown in Eq. (25), and the rolling prediction results of each iteration should be denormalized by PR<sub>t</sub> =  $mean(\mathbf{M_f}) + NF_t \times standard(\mathbf{M_f})$  to obtain bearing RUL. Eqs. (24) and (25) are given in Box I where  $NF_{SP}$  is the normalized value of the selected feature at time SP.

It is well known that the more serious the performance degradation of rolling bearings, the faster the increase in health indicators. The degradation factor should be considered in the rolling prediction process. Therefore, a postprocessing method for the predicted results  $PR_t$  is proposed considering the degradation factor, as shown in Eq. (26).

$$PR_{t} = \begin{cases} PR_{t-n_{f}^{l}}, & \text{if } PR_{t} \leq PR_{t-n_{f}^{l}} \\ \left(1 + \frac{\sum_{t=FPT+(i-1)*n_{f}^{l}}^{FFT+i*n_{f}^{l}} F_{SP-n_{f}^{l}+t}}{F_{FT}\cdot n_{0}^{l}} \times \left(\left(\frac{F_{FT}}{F_{1}}\right)^{\frac{n_{f}^{l}}{FT-FPT-1}} - 1\right)\right) \\ \times PR_{t-n_{f}^{l}}, \left(i = 0, 1, \dots, \left\lceil \frac{FT-FFT}{n_{f}^{l}} \right\rceil\right), else \end{cases}$$

$$(26)$$

<span id="page-7-0"></span>where  $PR_t$  represents the predicted result at time t.

When the predicted result  $PR_t$  exceeds  $F_{FT}$ , the RUL of rolling bearing is obtained, as shown in Eq. (27) and Fig. 10.

<span id="page-7-1"></span>
$$RUL = \begin{cases} FT - SP & \text{if } PR_t \ge F_{FT} \\ \text{rolling prediction} & \text{if } PR_t < F_{FT} \end{cases}$$
 (27)

Therefore, combined with the first prediction time determination and time-series feature window construction, the overall steps of the proposed method are summarized as follows, as shown in Fig. 11.

Step I: Collect vibration signals of rolling bearing and calculate kurtosis and RMS value at each time *t*.

Step II: If  $kur_t$  and  $rms_t$  exceed the normal range (see Section 3.2), this time will be regarded as FPT, and go to Step III. Otherwise, return to Step I.

Step III: Construct two initial time-series feature windows  $M_{01}$  and  $M_{02}$  based on the RMS and then adaptively compress them to obtain  $M_{k1}$  and  $M_{k2}$  (see Section 3.3.2). If the compressed feature windows have outlier regions, go to Step IV. Otherwise, go to Step V.

![](_page_8_Figure_2.jpeg)

Fig. 9. Architecture of the SBiLSTM network.

<span id="page-8-1"></span>
$$[F_{1}, F_{2}, F_{3}, F_{4}, F_{5}, F_{6}] \rightarrow F_{7}$$

$$[F_{2}, F_{3}, F_{4}, F_{5}, F_{6}, F_{7}] \rightarrow F_{8}$$

$$\vdots \qquad \vdots$$

$$[F_{m+1}, F_{m+2}, F_{m+3}, F_{m+4}, F_{m+5}, F_{m+6}] \rightarrow F_{m+7}$$

$$[NF_{SP-2n_{f}^{l}+1}, NF_{SP-2n_{f}^{l}+2}, \dots, NF_{SP-n_{f}^{l}}] \rightarrow [NF_{SP-n_{f}^{l}+1}, NF_{SP-n_{f}^{l}+2}, \dots, NF_{SP}]$$

$$[NF_{SP-n_{f}^{l}+1}, NF_{SP-n_{f}^{l}+2}, \dots, NF_{SP}] \rightarrow [NF_{SP+1}, NF_{SP+2}, \dots, NF_{SP+1*n_{f}^{l}}]$$

$$[NF_{SP+1}, NF_{SP+2}, \dots, NF_{SP+1*n_{f}^{l}+1}, NF_{SP+1*n_{f}^{l}+2}, \dots, NF_{SP+2*n_{f}^{l}}]$$

$$\vdots \qquad \vdots \qquad \vdots \qquad \vdots \qquad \vdots \qquad \vdots \qquad \vdots \qquad \vdots \qquad \vdots \qquad \vdots \qquad$$

Box I.

<span id="page-8-5"></span>![](_page_8_Figure_6.jpeg)

Fig. 10. Multi-step ahead rolling prediction from FPT.

<span id="page-8-2"></span>Step IV: Perform the outlier process method and continue to compress the feature windows ( $M_{s1}$  and  $M_{s2}$ ) obtained in Step III until the stopping criteria are met (Section 3.3.3), and go to Step V.

<span id="page-8-4"></span><span id="page-8-3"></span>Step V: Train the SBiLSTM model using the normalized timeseries feature windows  $NF_{f1}$  and  $NF_{f2}$  (Section 3.4.1).

Step VI: Implement multi-step ahead rolling prediction method using the trained SBiLSTM model (Section 3.4.2). If the predicted RMS exceeds the failure threshold  $F_{FT}$ , go to Step VII.

Step VII: Output the rolling bearing RUL.

# 4. Experimental validation

#### <span id="page-8-0"></span>4.1. Experimental setup

The widely used XJTU-SY rolling bearing dataset is adopted to comprehensively validate the feasibility of the proposed method, and there are 15 run-to-failure datasets of rolling bearings [63]. The experimental setup is shown in Fig. 12, and detailed information can be found in [63]. Three different conditions are considered: 2100 rpm (35 Hz), 12 kN; 2250 rpm (37.5 Hz), 11 kN; 2400 rpm (40 Hz), 10 kN. In addition, two accelerometers

<span id="page-9-1"></span>**Table 2**Detailed information of the X|TU-SY rolling bearing dataset.

| Running condition | Bearing dataset | Number of files | Bearing lifetime (min) | FPT (min) | FT-FPT (min) | $F_{FT}/F_{FPT}$ | Failure mode                          |
|-------------------|-----------------|-----------------|------------------------|-----------|--------------|------------------|---------------------------------------|
| Condition 1       | Bearing1_1      | 123             | 123                    | 76        | 47           | 4.06             | Outer race                            |
| (35 Hz/12 kN)     | Bearing1_2      | 161             | 161                    | 44        | 117          | 2.82             | Outer race                            |
|                   | Bearing1_3      | 158             | 158                    | 60        | 98           | 6.79             | Outer race                            |
|                   | Bearing1_4      | 122             | 122                    | _         | -            | -                | Cage                                  |
|                   | Bearing1_5      | 52              | 52                     | 39        | 13           | 5.29             | Inner race and outer race             |
| Condition 2       | Bearing2_1      | 491             | 491                    | 455       | 36           | 6.45             | Inner race                            |
| (37.5 Hz/11 kN)   | Bearing2_2      | 161             | 161                    | 48        | 113          | 6.05             | Outer race                            |
|                   | Bearing2_3      | 533             | 533                    | 327       | 206          | 3.64             | Cage                                  |
|                   | Bearing2_4      | 42              | 42                     | 30        | 12           | 10.1             | Outer race                            |
|                   | Bearing2_5      | 281             | 281                    | 141       | 140          | 5.81             | Outer race                            |
| Condition 3       | Bearing3_1      | 2538            | 2538                   | 2344      | 194          | 10.5             | Outer race                            |
| (40 Hz/10 kN)     | Bearing3_2      | 2496            | 2496                   | _         | -            | -                | Inner race, ball, cage and outer race |
|                   | Bearing3_3      | 371             | 371                    | 340       | 31           | 8.24             | Inner race                            |
|                   | Bearing3_4      | 1515            | 1515                   | 1418      | 97           | 7.62             | Inner race                            |
|                   | Bearing3_5      | 114             | 114                    | 9         | 105          | 5.37             | Outer race                            |

![](_page_9_Figure_4.jpeg)

<span id="page-9-0"></span>Fig. 11. Flowchart of the proposed RUL prediction method.

(vertical and horizontal) with a sampling frequency of 25.6 kHz are installed at 90° on the tested rolling bearings. Moreover, there are four failure modes of rolling bearings, including outer race fracture, inner race wear, outer race wear and cage fracture, as shown in Fig. 13.

In addition, Table 2 lists the detailed information of the 15 rolling bearings. The third column presents the total number of

files, with each file containing 32 768 data. For clarity, Fig. 14 illustrates the raw vibration signals of the bearing and their corresponding kurtosis and FPT identification results. Note that the FPT and  $F_{FPT}$  of bearing\_1\_4 and bearing\_3\_2 are not shown owing to sudden failure characteristics and multiple failures, respectively. Therefore, the data of 13 rolling bearings are utilized to validate the generalization and effectiveness of the proposed method.

# 4.2. Experimental result analysis and discussion

In this section, three representative rolling bearings (bearing\_1\_3, bearing\_2\_5 and bearing\_3\_1) are employed to validate the effectiveness of the proposed method, because their running conditions are different and their lifetimes are relatively short (123 min), medium (281 min), and long (2532 min), respectively. Therefore, if the proposed method is effective for three representative bearings, it is expected that it would also be effective for the remaining ten bearings. The superiority of the proposed method is verified by eight RUL prediction methods of rolling bearings.

(1) Method 1 (Proposed method): This method employs the first prediction time identification and multi-step ahead rolling prediction with adaptive time-series feature windows to achieve RUL prediction. It is well known that RMS is an effective feature to represent rolling bearing faults [26,41]. Therefore, this study selects RMS as the most sensitive feature to construct the feature window.

In addition,  $n_0^l$ ,  $n_{kl}^l$  and  $n_{sl}^l$  are set to 10, 6 and 3, respectively. Besides, the averages of *FT-FFT* and  $F_{FT}/F_{FPT}$  are 94.152 and 6.36, respectively, as shown in Table 2. Therefore, according to Eq. (9),  $g_{max}$  is 0.2197 (6.36<sup>(10/93.152)</sup>-1). Moreover, the input of SBiLSTM network is  $\left[F_{SP-2*n_f^l+1}, F_{SP-2*n_f^l+2}, \ldots, F_{SP-n_f^l}\right]$  and the output is  $\left[F_{SP-n_f^l+1}, F_{SP-n_f^l+2}, \ldots, F_{SP}\right]$ . After utilizing k-fold cross-validation method, its optimal parameters (epoch: 250, neurons: [140,150], learning rate: 0.002 and batch size: 32) are determined.

- (2) Method 2: Some publications assume that the rolling bearing degradation process is linear [57]. This method employs the linear regression method to establish feature windows based on RMS. Therefore, the degradation factor is fixed (g=0.1) during the whole prediction process. Other settings are the same as in Method 1.
- (3) Method 3: Some publications assume that the rolling bearing degradation process is linear [57]. This method employs the linear regression method to establish feature windows based on RMS. Therefore, the degradation factor is fixed (g=0.2) during the whole prediction process. Other settings are the same as in Method 1.

![](_page_10_Picture_2.jpeg)

**Fig. 12.** Experimental setup of rolling bearing.

<span id="page-10-0"></span>![](_page_10_Picture_4.jpeg)

**Fig. 13.** Photographs of the tested bearings.

- <span id="page-10-1"></span>(4) Method 4: Most existing data-driven RUL prediction methods use whole operational life data to construct a prediction model [\[39\]](#page-18-4). Therefore, the initial time-series feature windows are constructed by all historical data before *SP*, as shown in [Fig.](#page-11-1) [15,](#page-11-1) and these feature windows are directly employed to perform multi-step ahead rolling prediction without compression. Other settings are the same as in Method 1.
- (5) Method 5: This method employs the compressed feature window to perform the multi-step ahead rolling prediction method. However, there is no postprocessing strategy for the prediction results, and these results only need to satisfy the following equation. Other settings are the same as in Method 1.

$$DF_t \ge DF_{t-n_f^l} \tag{28}$$

(6) Method 6: This method utilizes an exponential model to predict the bearing RUL [\[20\]](#page-17-19), and the input and output are the RMS and bearing RUL, respectively. Each sample contains an RMS and its corresponding RUL value. For each rolling bearing, the dataset contains all samples from the first prediction time to failure time. Therefore, there are 13 datasets except for bearings 1\_4 and 3\_2. To evaluate the effectiveness of the exponential model, one dataset is the testing dataset and the others are the training datasets.

$$RUL = a \times e^{b \times RMS_t} + c \tag{29}$$

where *a*, *b* and *c* are three constants and are determined by training datasets. RMS*<sup>t</sup>* denotes the RMS value at time *t*. [Table](#page-11-2) [3](#page-11-2)

![](_page_11_Figure_2.jpeg)

Fig. 14. First prediction time result of bearing\_1\_3.

<span id="page-11-0"></span>![](_page_11_Figure_4.jpeg)

<span id="page-11-1"></span>Fig. 15. Diagram of the initial time-series feature window in Method 4.

**Table 3**Parameter determination of exponential model for three representative rolling bearings.

<span id="page-11-2"></span>

| Bearing     | FPT  | Value  |         |       |  |  |  |
|-------------|------|--------|---------|-------|--|--|--|
|             |      | а      | b       | С     |  |  |  |
| bearing_1_3 | 80   | 81.02  | -8621.9 | 117.5 |  |  |  |
|             | 90   | 90.55  | -12643  | 112.5 |  |  |  |
|             | 100  | 93.15  | -13809  | 107.5 |  |  |  |
|             | 110  | 91     | -13156  | 102.5 |  |  |  |
|             | 120  | 85.1   | -11155  | 97.5  |  |  |  |
|             | 130  | 79.63  | -9440.4 | 92.5  |  |  |  |
| bearing_2_5 | 161  | 161.06 | -6524.5 | 258   |  |  |  |
|             | 181  | 167.7  | -8061.1 | 248   |  |  |  |
|             | 201  | 145.5  | -4272.5 | 238   |  |  |  |
|             | 221  | 143.5  | -4133.4 | 228   |  |  |  |
|             | 241  | 144.1  | -4401.8 | 218   |  |  |  |
|             | 261  | 143.3  | -4431.9 | 208   |  |  |  |
| bearing_3_1 | 2364 | 86.3   | -504.8  | 172   |  |  |  |
|             | 2394 | 90.1   | -1958.5 | 171   |  |  |  |
|             | 2424 | 106    | -8310.2 | 156   |  |  |  |
|             | 2454 | 104.3  | -8097.4 | 141   |  |  |  |
|             | 2484 | 96.67  | -6431   | 126   |  |  |  |
|             | 2514 | 95.86  | -6479   | 111   |  |  |  |

lists the detailed information of parameters a, b and c at different FPTs.

(7) Method 7: This method uses BPNN to predict bearing RUL [12]. The inputs are five time-domain features, including RMS, kurtosis, mean, variance and maximum, and the output is the RUL value. Furthermore, the training dataset and testing dataset are the same as those in Method 6. In the BPNN algorithm, the numbers of neurons in the input and output layers are set to 5 and 1, respectively. Meanwhile, the activation function and number of neurons in the hidden layers are set to tan-sigmoid and 10, and the desired performance and maximum epochs are set to 0.00001 and 5000, respectively.

$$mean = \frac{1}{n} \sum_{i=1}^{n} x_i \tag{30}$$

$$variance = \frac{1}{n} \left( \sum_{i=1}^{n} (|x_i| - mean)^2 \right)$$
 (31)

$$maximum = max(x_i) (32)$$

where  $x_i$  denotes the vibration signal at *ith* sampling point.

(8) Method 8: This method utilizes the LSTM network [64] instead of SBiLSTM and its optimal parameters are determined (epoch: 250, neurons: [140,150], learning rate: 0.002 and batch size: 32). The input is  $\left[F_{SP-2*n_f^l+1}, F_{SP-2*n_f^l+2}, \ldots, F_{SP-n_f^l}\right]$  and output is  $\left[F_{SP-n_f^l+1}, F_{SP-n_f^l+2}, \ldots, F_{SP}\right]$ . Moreover, the other settings are the same as those in Method 1.

For eight RUL prediction methods, their prediction performance is evaluated by the root mean square percentage error (RMSPE) and mean absolute percentage error (MAPE).

$$RMSPE = \sqrt{\frac{1}{n} \sum_{i=1}^{n} \left( \frac{PRUL_i - RRUL_i}{RRUL_i} \right)^2} \times 100\%$$
 (33)

$$MAPE = \frac{1}{n} \sum_{i=1}^{n} \frac{|PRUL_i - RRUL_i|}{RRUL_i} \times 100\%$$
 (34)

![](_page_12_Figure_2.jpeg)

**Fig. 16.** RUL prediction for bearing\_1\_3 using Methods 1–3.

<span id="page-12-1"></span>where *PRUL* and *RRUL* represent the predicted RUL and real RUL, respectively.

The RUL prediction results of bearing\_1\_3, bearing\_2\_5 and bearing\_3\_1 by employing eight methods are listed in [Tables](#page-12-0) [4–](#page-12-0) [6](#page-13-0). In Method 1 (the proposed method), the MAPE and RMSPE (6.77% and 8.87% for bearing\_1\_3; 18.92% and 29.19% for bearing\_2\_5; 8.95% and 10.42% for bearing\_3\_1) are smaller than other methods, proving the superiority of the proposed method.

Additionally, Method 1 achieves superior prediction performance under limited data compared to Methods 2 and 3, as shown in [Tables](#page-12-0) [4](#page-12-0)[–6](#page-13-0). Particularly, the larger fixed degradation factor (*g* = 0.2) in Method 3 performed worse than Method 2 at the incipient degradation stage and better than Method 2 at the later degradation stage (where *SP* ranges from 181 to 221 for bearing\_2\_5 and from 2484 to 2514 for bearing\_3\_1). The main reason is that a large degradation factor makes the value of the sensitive feature increase faster, and only a small number of rolling iterations are required to reach the failure threshold. This indicates that Method 3 is improper for RUL prediction in

<span id="page-12-0"></span>**Table 4** Bearing\_1\_3 prediction results of different RUL prediction methods.

| SP                    | RRUL | PRUL result (eight methods) |                |                |                |            |                |                |                |
|-----------------------|------|-----------------------------|----------------|----------------|----------------|------------|----------------|----------------|----------------|
|                       |      | 1                           | 2              | 3              | 4              | 5          | 6              | 7              | 8              |
| 80                    | 67   | 66                          | 73             | 31             | 73             | Inf        | 72             | 75             | 59             |
| 90                    | 57   | 59                          | 66             | 26             | 64             | Inf        | 88             | 81             | 62             |
| 100                   | 47   | 51                          | 58             | 23             | 63             | Inf        | 67             | 52             | 52             |
| 110                   | 37   | 36                          | 45             | 19             | 50             | Inf        | 58             | 43             | 43             |
| 120                   | 27   | 22                          | 32             | 12             | 36             | Inf        | 34             | 33             | 30             |
| 130                   | 17   | 16                          | 21             | 6              | 22             | Inf        | 19             | 20             | 24             |
| MAPE (%)<br>RMSPE (%) |      | 6.77<br>8.87                | 18.64<br>19.32 | 54.68<br>54.91 | 28.68<br>32.37 | Inf<br>Inf | 33.14<br>38.42 | 25.86<br>27.99 | 16.34<br>20.06 |

the incipient degradation stage, but is appropriate in the later degradation stage. Conversely, as the fixed degradation factor (*g* = 0.1) is small, the prediction performance of Method 2 is worse than that of Method 3 in the later degradation stage, and the performance of Method 2 is superior to that of Method 3 in the incipient degradation stage (where *SP* increases from

![](_page_13_Figure_2.jpeg)

**Fig. 17.** RUL prediction for bearing\_2\_5 using Methods 1–3.

**Table 5** Bearing\_2\_5 prediction results of different RUL prediction methods.

| SP       | RRUL      | PRUL result (eight methods) |       |       |       |     |       |       |       |
|----------|-----------|-----------------------------|-------|-------|-------|-----|-------|-------|-------|
|          |           | 1                           | 2     | 3     | 4     | 5   | 6     | 7     | 8     |
| 161      | 120       | 125                         | 171   | 87    | 51    | Inf | 187   | 167   | 109   |
| 181      | 100       | 84                          | 132   | 71    | 41    | Inf | 127   | 131   | 187   |
| 201      | 80        | 26                          | 28    | 15    | 38    | Inf | 41    | 55    | 23    |
| 221      | 60        | 52                          | 33    | 17    | 84    | Inf | 43    | 51    | 57    |
| 241      | 40        | 41                          | 61    | 31    | 21    | Inf | 26    | 32    | 34    |
| 261      | 20        | 22                          | 48    | 22    | 18    | Inf | 16    | 17    | 17    |
| MAPE (%) |           | 18.92                       | 62.83 | 40.32 | 44.42 | Inf | 35.82 | 25.23 | 33.74 |
|          | RMSPE (%) | 29.19                       | 72.38 | 48.20 | 47.43 | Inf | 37.97 | 26.83 | 46.91 |

80 to 120 in bearing\_1\_3, from 161 to 211 in bearing\_2\_5, and from 2364 to 2454 in bearing\_3\_1), as shown in [Figs.](#page-12-1) [16](#page-12-1)[–18](#page-14-0). The primary reason is that a small degradation factor demonstrates that the value of the sensitive feature increases slowly, making Method 2 need more rolling iterations to reach the failure

<span id="page-13-0"></span>**Table 6** Bearing\_3\_1 prediction results of different RUL prediction methods.

| SP        | RRUL |       | PRUL result (eight methods) |       |       |     |       |       |       |
|-----------|------|-------|-----------------------------|-------|-------|-----|-------|-------|-------|
|           |      | 1     | 2                           | 3     | 4     | 5   | 6     | 7     | 8     |
| 2364      | 168  | 166   | 73                          | 37    | 141   | Inf | 136   | 142   | 220   |
| 2394      | 138  | 146   | 108                         | 56    | 91    | Inf | 98    | 81    | 153   |
| 2424      | 108  | 124   | 84                          | 41    | 102   | Inf | 130   | 141   | 131   |
| 2454      | 78   | 85    | 67                          | 36    | 81    | Inf | 95    | 86    | 80    |
| 2484      | 48   | 51    | 48                          | 26    | 51    | Inf | 41    | 44    | 53    |
| 2514      | 18   | 21    | 44                          | 23    | 28    | Inf | 17    | 20    | 19    |
| MAPE (%)  |      | 8.95  | 43.17                       | 54.48 | 20.22 | Inf | 18.39 | 19.51 | 13.61 |
| RMSPE (%) |      | 10.42 | 64.84                       | 56.61 | 27.66 | Inf | 19.73 | 23.01 | 16.71 |

threshold. This indicates that Method 2 is not suitable for RUL prediction at the later degradation stage, but it is suitable at the incipient degradation stage. For Method 1, the degradation factor is updated adaptively according to the dynamic change in the FTR. The degradation factor is small in the incipient degradation stage

![](_page_14_Figure_2.jpeg)

**Fig. 18.** RUL prediction for bearing\_3\_5 using Methods 1–3.

<span id="page-14-0"></span>and large in the later degradation stage. Therefore, the overall prediction accuracy of this method is higher than that of Method 2 and Method 3, indicating that the adaptive determination of the degradation factor is beneficial to better monitor rolling bearing degradation. [Figs.](#page-12-1) [16](#page-12-1)[–18](#page-14-0) and [Tables](#page-12-0) [4–](#page-12-0)[6](#page-13-0) show the prediction results of these methods.

Method 4 constructs the time-series feature window based on all the historical data before *SP*. These feature windows are not compressed, and thus, the length of the feature windows is large, which means that these feature windows are more conducive to describing the global degradation trend. If the SBiLSTM model is trained by these feature windows directly, the rolling prediction process will overly depend on the global trend, which makes this method difficult to accurately reflect the local degradation characteristics of rolling bearings, resulting in a large RUL prediction error. Taking bearing \_1\_3 as an example, in the later degradation stage, for *SP* = 120, 160, 180, and 200, Method 4 requires more iterations than Method 1 to reach the failure threshold, so that MAPE (34.04%, 54.05%, 33.33%, and 29.41%, respectively) is greater than that of Method 1 (8.51%, 2.70%, 18.52%, and 5.88%, respectively), as shown in [Fig.](#page-15-0) [19.](#page-15-0) Therefore, the comparison results (see [Tables](#page-12-0) [4–](#page-12-0)[6](#page-13-0)) indicate that the time-series feature window needs to be compressed, which is conducive to capturing the rolling bearing degradation trend more accurately.

Method 5 does not adopt a postprocessing strategy in the rolling prediction process. This method ignores the fact that rolling bearing degradation is a gradual process. If the degradation factor is not considered when performing multi-step ahead rolling prediction, the value of the sensitive feature increases slowly. In this case, Method 5 requires more iterations to reach the failure threshold or even fail to exceed the failure threshold, which makes it difficult for Method 5 to accurately predict the rolling bearing RUL, as shown in [Fig.](#page-15-0) [19.](#page-15-0)

Although a large number of data-driven models have been employed to predict rolling bearing RUL, the comparison results between Methods 6-7 and other methods demonstrate that the RUL prediction performance of the exponential model and

![](_page_15_Figure_2.jpeg)

**Fig. 19.** RUL prediction for bearing\_1\_3 using Methods 1, 4, and 5.

<span id="page-15-0"></span>BPNN trained using all run-to-failure data is poor. The essential reason is that these methods are overly dependent on the global degradation trends of all training objects (rolling bearings), and the data distribution discrepancy between training objects and predicted objects is great different, resulting in a large RUL prediction error. Compared with Methods 6 and 7, Method 1 considers the local trend determined by two adjacent time-series feature windows before *SP* when predicting RUL, which can more accurately describe the real degradation trend of each rolling bearing. Therefore, Method 1 not only has a strong generalization ability in RUL prediction, but also avoids the large number of training resources required for training high-accuracy prediction models [\[65\]](#page-18-28).

Method 8 uses LSTM to predict rolling bearing RUL, and the prediction results of SBiLSTM are superior to LSTM, as shown in [Tables](#page-12-0) [4](#page-12-0)–[6.](#page-13-0) The MAPE of Method 8 for bearing \_1\_3, bearing \_2\_5 and bearing \_3\_1 is 16.34%, 33.74% and 13.61%, respectively, whereas those of Method 1 are 6.77%, 18.92%, and 8.95%, respectively. The main reason is that SBiLSTM utilizes the previous and future information to smoothen the current data through multiple forward and backward paths, while LSTM can only process the previous information with a forward path, ignoring the temporal characteristics of rolling bearing degradation data. Accordingly, the SBiLSTM network can describe the degradation trends of rolling bearings more accurately. Meanwhile, artificial algorithms will be considered to optimize the network parameters in the future [[66\]](#page-18-29).

#### *4.3. Analysis of the time-series feature window with outliers*

When the running conditions such as the load and speed of the rolling bearing change, the bearing degradation trends also change, which leads to a rapid increase or decrease in RMS. This behavior is usually regarded as an outlier in the dataset, presenting a challenge when predicting the RUL of rolling bearings. Taking bearing\_2\_5 as an example, [Fig.](#page-16-1) [20](#page-16-1) and [Table](#page-16-2) [7](#page-16-2) demonstrate the outlier process method proposed in this study. [Fig.](#page-16-1) [20](#page-16-1) depicts the overall steps of the outlier process from the

![](_page_16_Figure_2.jpeg)

![](_page_16_Figure_3.jpeg)

![](_page_16_Figure_6.jpeg)

**Fig. 20.** Outlier process for bearing\_3\_1.

<span id="page-16-2"></span><span id="page-16-1"></span>**Table 7** Prediction result with outlier process at *SP* = 171.

| Item                          | Without outlier<br>process (Mk) | With outlier<br>process (Ms ) |
|-------------------------------|---------------------------------|-------------------------------|
| Maximum (M2)                  | 2.045                           | 2.045                         |
| Minimum (M2)                  | 1.835                           | 2.013                         |
| Maximum (M1)                  | 1.819                           | 1.919                         |
| Minimum (M1)                  | 1.546                           | 1.835                         |
| Increase rate (R)             | 1.227                           | 1.078                         |
| Feature-threshold ratio (FTR) | 0.247                           | 0.256                         |
| MAPE (%)                      | 82.73                           | 9.09                          |

initial feature window at *SP* = 171 to the prediction result. In [Table](#page-16-2) [7](#page-16-2), it can be observed that after the *k*th compression (*Mk*), the minimum value of *Mk*<sup>2</sup> (1.835) is larger than the maximum value of *Mk*<sup>1</sup> (1.819), and the increase rate *R<sup>k</sup>* (1.227) is larger than 1 + *gmax*, as shown in [Fig.](#page-16-1) [20\(](#page-16-1)a)–(b). If these compressed feature windows are directly used to establish the SBiLSTM prediction model, the model will remember the time-series information of Section [1](#page-0-3), as shown in [Fig.](#page-16-1) [20\(](#page-16-1)b). Meanwhile, the RMS in Section [2](#page-1-0) is larger than that in Section [1](#page-0-3). This results in a great difference between the actual degradation process and predicted results. Therefore, according to the identification conditions of the outlier region in Eqs. ([18](#page-6-3)) and [\(19\)](#page-6-4), the feature window at *SP* = 171 is regarded as an outlier region, and then the outlier processing method is used to process it.

After the application of the outlier process, the increase rate *Rs* is 1.078, and the *FTR* increases from 0.247 to 0.256, which is more representative of the degradation process at *SP* = 171. These compressed feature windows *M<sup>s</sup>* is utilized to train the SBiLSTM model, and the MAPE decreases from 82.73% to 9.09%, as shown in [Fig.](#page-16-1) [20\(](#page-16-1)c). Therefore, the outlier process is effective, which can capture the local characteristics more accurately and obtain better RUL prediction results.

Most of the existing roll bearing RUL prediction methods utilize the entire degradation data of the similar or same bearings to construct models, which are called ''group'' models. However, the previous researches indicate that the degradation process of similar or the same bearings under different running conditions (including load and speed) may be different, which requires an ''individual'' model. The proposed method is weakly associated with the overall degradation process of the similar or same bearings, and only closely related to the current working condition of predicted objects. Therefore, although the RUL prediction error is inevitable, the proposed method also provides guidance for constructing ''individual'' RUL prediction models of other mechanical systems.

#### **5. Conclusion and future scope**

<span id="page-16-0"></span>This study develops a novel method to accurately predict the rolling bearing RUL with limited data. The main conclusions are summarized as follows:

- (1) This study proposes a rolling bearing RUL prediction method under limited data. Experimental results reveal that the proposed method can accurately predict RUL. For three rolling bearings, MAPE of the proposed approach is 6.77%, 18.92% and 8.95%, respectively, which are superior to other existing methods.
- (2) This study presents the first prediction time identification method based on kurtosis and RMS. The results of FPT demonstrate that the proposed method can effectively divide the entire cycle of 13 rolling bearings into the health and degradation stages.
- (3) This study develops an adaptive time-series feature window to better describe the degradation process of rolling bearings. Compared with feature windows without compression, the MAPE of the adaptive compression method for three bearings

is reduced by 21.91%, 25.5% and 11.27%, respectively. After the application of the outlier process method, the MAPE of the outlier region is reduced from 82.73% to 9.09%.

(4) This study develops a stacked bidirectional LSTM network and proposes a multi-step ahead rolling method. The results show that it can accurately predict the future degradation trend of rolling bearings under limited data. This provides an effective strategy for other mechanical systems to predict degradation trends when data are limited.

Future research intends to investigate methods for further determining the failure threshold and degradation factor of rolling bearings to enhance RUL prediction performance under limited data. Other sensitive features will be further studied to more accurately track the degradation trends of rolling bearings. In addition, the practical application of the proposed method in other prognostic scenarios is also of interest.

### **CRediT authorship contribution statement**

**Weili Kong:** Writing – review & editing, Writing – original draft, Software, Validation. **Hai Li:** Supervision, Reviewing.

#### **Declaration of competing interest**

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

# **Data availability**

No data was used for the research described in the article.

#### **Acknowledgments**

The author would like to thank the Major Project of National Science and Technology, China under Grant 2017ZX04002001- 002.

# **References**

- <span id="page-17-0"></span>[1] [O. AlShorman, M. Irfan, N. Saad, D. Zhen, N. Haider, A. Glowacz, A.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb1) [AIShorman, A review of artificial intelligence methods for condition moni](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb1)[toring and fault diagnosis of rolling element bearings for induction motor,](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb1) [Shock. Vib. 2020 \(2020\) 1–20.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb1)
- <span id="page-17-1"></span>[2] [N.W. Nirwan, H.B. Ramani, Condition monitoring and fault detection in](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb2) [roller bearing used in rolling mill by acoustic emission and vibration](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb2) [analysis, Mater. Today Proc. 51 \(2022\) 344–354.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb2)
- <span id="page-17-2"></span>[3] [X.Y. Su, H.M. Liu, L.F. Tao, C. Lu, M.L. Suo, An end-to-end framework for](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb3) [remaining useful life prediction of rolling bearing based on feature pre](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb3)[extraction mechanism and deep adaptive transformer model, Comput. Ind.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb3) [Eng. 161 \(2021\) 107531.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb3)
- <span id="page-17-3"></span>[4] [L. Xu, P. Pennacchi, S. Chatterton, A new method for the estimation of](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb4) [bearing health state and remaining useful life based on the moving average](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb4) [cross-correlation of power spectral density, Mech. Syst. Signal Process. 139](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb4) [\(2020\) 106617.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb4)
- <span id="page-17-4"></span>[5] [M. Cerrada, R.V. Sánchez, C. Li, F. Pacheco, D. Cabrera, J.V.D. Oliveira,](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb5) [R.E. Vasquez, A review on data-driven fault severity assessment in rolling](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb5) [bearings, Mech. Syst. Signal Process. 99 \(2018\) 169–196.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb5)
- <span id="page-17-5"></span>[6] [I. El-Thalji, E. Jantunen, A summary of fault modelling and predictive health](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb6) [monitoring of rolling element bearings, Mech. Syst. Signal Process. 60](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb6) [\(2015\) 252–272.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb6)
- <span id="page-17-6"></span>[7] [L.X. Liao, Discovering prognostic features using genetic programming in](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb7) [remaining useful life prediction, IEEE Trans. Ind. Electron. 61 \(5\) \(2013\)](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb7) [2464–2472.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb7)
- <span id="page-17-7"></span>[8] [I. EI-Thalji, E. Jantunen, Dynamic modelling of wear evolution in rolling](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb8) [bearings, Tribol. Ind. 84 \(2015\) 90–99.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb8)
- <span id="page-17-8"></span>[9] [S.J. Liu, L.X. Fan, An adaptive prediction approach for rolling bear](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb9)[ing remaining useful life based on multistage model with three-source](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb9) [variability, Reliab. Eng. Syst. Saf. 218 \(2022\) 108182.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb9)
- <span id="page-17-9"></span>[10] [Y.X. Li, X.Z. Huang, P.F. Ding, C.Y. Zhao, Wiener-based remaining useful life](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb10) [prediction of rolling bearings using improved Kalman filtering and adaptive](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb10) [modification, Measurement 182 \(2021\) 109706.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb10)

- <span id="page-17-10"></span>[11] [P.S. Kumar, L.A. Kumaraswamidhas, S.K. Laha, Bearing degradation as](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb11)[sessment and remaining useful life estimation based on Kullback–Leibler](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb11) [divergence and Gaussian processes regression, Measurement 174 \(4\)](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb11) [\(2021\) 108948.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb11)
- <span id="page-17-11"></span>[12] [R.Q. Huang, L.F. Xi, X.L. Li, C.R. Liu, H. Qiu, J. Lee, Residual life predictions](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb12) [for ball bearings based on self-organizing map and back propagation neural](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb12) [network methods, Mech. Syst. Signal Process. 21 \(1\) \(2007\) 193–207.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb12)
- <span id="page-17-12"></span>[13] [T. Zan, Z.H. Liu, H. Wang, M. Wang, X.S. Gao, Z.L. Pang, Prediction of](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb13) [performance deterioration of rolling bearing based on JADE and PSO-SVM,](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb13) [Proc. Inst. Mech. Eng. C-J. Mech. 235 \(9\) \(2021\) 1684–1697.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb13)
- <span id="page-17-13"></span>[14] [Y.S. Zou, S.J. Zhao, Y.Z. Liu, Z.X. Li, G.F. Ding, The transfer prediction](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb14) [method of bearing remain use life based on dynamic benchmark, IEEE](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb14) [Trans. Instrum. Meas. 70 \(2021\) 1–11.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb14)
- <span id="page-17-14"></span>[15] [Y. Qian, R. Yan, R.X. Gao, A multi-time scale approach to remaining useful](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb15) [life prediction in rolling bearing, Mech. Syst. Signal Process. 83 \(2017\)](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb15) [549–567.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb15)
- <span id="page-17-15"></span>[16] [X.Y. Liu, G. Chen, Z.J. Cheng, X.K. Wei, H. Wang, Convolution neural](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb16) [network based particle filtering for remaining useful life prediction of](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb16) [rolling bearing, Adv. Mech. Eng. 14 \(6\) \(2022\) 16878132221100631.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb16)
- <span id="page-17-16"></span>[17] [W. Mao, J. He, M.J. Zuo, Predicting remaining useful life of rolling bearings](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb17) [based on deep feature representation and transfer learning, IEEE Trans.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb17) [Instrum. Meas. 69 \(4\) \(2019\) 1594–1608.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb17)
- <span id="page-17-17"></span>[18] [L. Guo, N.P. Li, F. Jia, Y.G. Lei, J. Lin, A recurrent neural network](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb18) [based health indicator for remaining useful life prediction of bearings,](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb18) [Neurocomputing 240 \(2017\) 98–109.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb18)
- <span id="page-17-18"></span>[19] [Y.G. Lei, N.P. Li, L. Guo, N.B. Li, T. Yan, Y. Lin, Machinery health prognostics:](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb19) [A systematic review from data acquisition to RUL prediction, Mech. Syst.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb19) [Signal Process. 104 \(2018\) 799–834.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb19)
- <span id="page-17-19"></span>[20] [G. Wang, J.W. Xiang, Remain useful life prediction of rolling bearings based](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb20) [on exponential model optimized by gradient method, Measurement 176](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb20) [\(2021\) 109161.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb20)
- <span id="page-17-20"></span>[21] [H. Liu, Z.L. Mo, H. Zhang, X.F. Zeng, J.Y. Wang, M. Qiang, Investigation on](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb21) [rolling bearing remaining useful life prediction: A review, in: 2018 Prog.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb21) [Syst. Health. Manag. Conf., 2018, pp. 979–984.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb21)
- <span id="page-17-21"></span>[22] [D. Xu, J. Huang, Q. Zhu, X. Chen, Y.C. Xu, S. Wang, Residual fatigue life](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb22) [prediction of ball bearings based on Paris law and RMS, Chin. J. Mech.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb22) [Eng-Eng. 25 \(2\) \(2012\) 320–327.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb22)
- <span id="page-17-22"></span>[23] [D. An, N.H. Kim, J.H. Choi, Practical options for selecting data-driven or](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb23) [physics-based prognostics algorithms with reviews, Reliab. Eng. Syst. Saf.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb23) [133 \(2015\) 23–236.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb23)
- <span id="page-17-23"></span>[24] [A. Glowacz, R. Tadeusiewicz, S. Legutko, W.H. Caesarendra, M. Irfan, H. Liu,](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb24) [F. Brumericik, M. Gutten, M. Sulowiza, J.A.A. Daviu, T.S. Gyan, P. Fracz, A.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb24) [Kumar, J.W. Xiang, Fault diagnosis of angle grinders and electric impact](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb24) [drills using acoustic signals, Appl. Acoust. 179 \(5\) \(2021\) 108070.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb24)
- <span id="page-17-24"></span>[25] [O. AlShorman, F. Alkahatni, M. Masadeh, M. Irfan, A. Glowacz, F. Althobiani,](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb25) [J. Kozik, W. Glowacz, Sounds and acoustic emission-based early fault](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb25) [diagnosis of induction motor: A review study, Adv. Mech. Eng. 13 \(2\)](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb25) [\(2021\) 1687814021996915.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb25)
- <span id="page-17-25"></span>[26] [A. Klausen, H.V. Khang, K.G. Robbersmyr, RMS based health indicators for](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb26) [remaining useful lifetime estimation of bearings, Model. Identif. Control](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb26) [43 \(1\) \(2022\) 21–38.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb26)
- <span id="page-17-26"></span>[27] [A. Kumar, C.P. Gandhi, G. Vashishtha, P. Kundu, H.S. Tang, A. Glowacz, R.K.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb27) [Shukla, J.W. Xiang, VMD based trigonometric entropy measure: a simple](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb27) [and effective tool for dynamic degradation monitoring of rolling element](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb27) [bearing, Meas. Sci. Technol. 33 \(1\) \(2021\) 014005.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb27)
- <span id="page-17-27"></span>[28] [R. Yao, C. Guo, W. Deng, H.M. Zhao, A novel mathematical morphology](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb28) [spectrum entropy based on scale-adaptive techniques, ISA Trans. 126](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb28) [\(2022\) 691–702.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb28)
- <span id="page-17-28"></span>[29] [H.Y. Chen, F. Miao, Y.J. Chen, Y.J. Xiong, T. Chen, A hyperspectral image](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb29) [classification method using multifeature vectors and optimized KELM, IEEE](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb29) [J. Starts 14 \(2021\) 2781–2795.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb29)
- <span id="page-17-29"></span>[30] [X.S. Si, W. Wang, C.H. Hu, D.H. Zhou, Remaining useful life estimation–a](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb30) [review on the statistical data driven approaches, European J. Oper. Res.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb30) [213 \(1\) \(2011\) 1–14.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb30)
- <span id="page-17-30"></span>[31] [L.l. Cui, X. Wang, H.Q. Wang, J.F. Ma, Research on remaining useful life](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb31) [prediction of rolling element bearings based on time-varying Kalman filter,](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb31) [IEEE Trans. Instrum. Meas. 69 \(6\) \(2020\) 2858–2867.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb31)
- <span id="page-17-31"></span>[32] [W.L. Du, X.K. Hou, H.C. Wang, Time-varying degradation model for re](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb32)[maining useful life prediction of rolling bearings under variable rotational](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb32) [speed, Appl. Sci-Basel 12 \(8\) \(2022\) 4044.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb32)
- <span id="page-17-32"></span>[33] [L. Cui, W. Li, X. Wang, D.Z. Zhao, H.Q. Wang, Comprehensive remaining](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb33) [useful life prediction for rolling element bearings based on time-varying](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb33) [particle filtering, IEEE Trans. Instrum. Meas. 71 \(2022\) 1–10.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb33)
- <span id="page-17-33"></span>[34] [Y. Zhang, A.C. Wang, Remaining useful life prediction of rolling bearings](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb34) [using electrostatic monitoring based on two-stage information fusion](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb34) [stochastic filtering, Math. Probl. Eng. 2020 \(2020\) 1–12.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb34)

- <span id="page-18-0"></span>[35] [Z. Meng, J. Li, N. N. Yin, Z.Z. Pan, Remaining useful life prediction of rolling](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb35) [bearing using fractal theory, Measurement 156 \(2020\) 107572.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb35)
- <span id="page-18-1"></span>[36] Q.L. Guan, X.K. Wei, W.F. Bai, L.M. Jia, Two-stage degradation modeling for remaining useful life prediction based on the Wiener process with measurement errors, Qual. Reliab. Eng. Int. (2022) [http://dx.doi.org/10.](http://dx.doi.org/10.1002/qre.3147) [1002/qre.3147.](http://dx.doi.org/10.1002/qre.3147)
- <span id="page-18-2"></span>[37] [L. Wang, L. Zhang, X.Z. Wang, Reliability estimation and remaining useful](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb37) [lifetime prediction for bearing based on proportional hazard model, J. Cent.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb37) [South. Univ. 22 \(12\) \(2015\) 4625–4633.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb37)
- <span id="page-18-3"></span>[38] [P. Wang, Z.Q. Long, G. Wang, A hybrid prognostics approach for estimating](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb38) [remaining useful life of wind turbine bearings, Energy Rep. 6 \(2020\)](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb38) [173–182.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb38)
- <span id="page-18-4"></span>[39] [Z.Z. Pan, Z. Meng, Z.J. Chen, W.Q. Gao, Y. Shi, A two-stage method based](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb39) [on extreme learning machine for predicting the remaining useful life of](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb39) [rolling-element bearings, Mech. Syst. Signal Process. 144 \(2020\) 106899.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb39)
- <span id="page-18-5"></span>[40] [X.L. Li, W. Zhang, H. Ma, Z. Luo, X. Li, Data alignments in machinery](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb40) [remaining useful life prediction using deep adversarial neural networks,](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb40) [Knowl-Based Syst. 197 \(2020\) 105843.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb40)
- <span id="page-18-6"></span>[41] [W. Yu, D.C. Pi, L.Q. Xie, Y. Luo, Multiscale attentional residual neural](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb41) [network framework for remaining useful life prediction of bearings,](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb41) [Measurement 177 \(2021\) 109310.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb41)
- <span id="page-18-7"></span>[42] [Z.J. Que, X.H. Jin, Z.G. Xu, Remaining useful life prediction for bearings](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb42) [based on a gated recurrent unit, IEEE Trans. Instrum. Meas. 70 \(2021\)](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb42) [1–11.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb42)
- <span id="page-18-8"></span>[43] [T. Han, J. Pang, A.C.C. Tan, Remaining useful life prediction of bearing based](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb43) [on stacked autoencoder and recurrent neural network, J. Manuf. Syst. 61](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb43) [\(2021\) 576–591.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb43)
- <span id="page-18-9"></span>[44] [G.J. Huang, H.K. i, J.Y. Ou, Y.L. Zhang, M.L. Zhang, A reliable prognosis](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb44) [approach for degradation evaluation of rolling bearing using MCLSTM,](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb44) [Sensors 20 \(7\) \(2020\) 1864.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb44)
- <span id="page-18-10"></span>[45] [Z.L. Liu, M.J. Zuo, Y. Qin, Remaining useful life prediction of rolling element](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb45) [bearings based on health state assessment, Proc. Inst. Mech. Eng. C-J. Mech.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb45) [230 \(2\) \(2016\) 314–330.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb45)
- <span id="page-18-11"></span>[46] [C.Y. Wang, W.L. Jiang, X.K. Yang, S.Q. Zhang, RUL prediction of rolling](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb46) [bearings based on a DCAE and CNN, Appl. Sci-Basel 11 \(23\) \(2021\) 11516.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb46)
- <span id="page-18-12"></span>[47] [W.B. Wang, J.J. Zhao, G.R. Ding, RUL prediction of rolling bearings based on](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb47) [improved empirical wavelet transform and convolutional neural network,](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb47) [Adv. Mech. Eng. 14 \(6\) \(2022\) 16878132221106609.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb47)
- <span id="page-18-13"></span>[48] [Y.M. Guo, H. Zhang, Z.J. Xia, C. Dong, Z.S. Zhang, Y.F. Zzhou, H. Sun, An](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb48) [improved deep convolution neural network for predicting the remain](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb48)[ing useful life of rolling bearings, J. Intell. Fuzzy. Syst. 40 \(3\) \(2021\)](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb48) [5743–5751.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb48)
- <span id="page-18-14"></span>[49] [H. Ding, L.L. Yang, Z.Y. Cheng, Z.J. Yang, A remaining useful life prediction](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb49) [method for bearing based on deep neural networks, Measurement 172](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb49) [\(2020\) 108878.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb49)
- <span id="page-18-15"></span>[50] [J. Zhu, N. Chen, C.Q. Shen, A new deep transfer learning method for bearing](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb50) [fault diagnosis under different working conditions, IEEE Sens. J. 20 \(15\)](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb50) [\(2019\) 8394–8402.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb50)

- <span id="page-18-16"></span>[51] [J. Zhu, N. Chen, C.Q. Shen, A new data-driven transferable remaining useful](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb51) [life prediction approach for bearing under different working conditions,](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb51) [Mech. Syst. Signal Process. 139 \(2020\) 106602.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb51)
- [52] [Y.F. Ding, M.P. Jia, Q.H. Miao, P. Huang, Remaining useful life estimation](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb52) [using deep metric transfer learning for kernel regression, Reliab. Eng. Syst.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb52) [Saf. 212 \(2021\) 107583.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb52)
- [53] [H. Cheng, X.G. Kong, G.G. Chen, Q.B. Wang, R.B. Wang, Transferable](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb53) [convolutional neural network based remaining useful life prediction of](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb53) [bearing under multiple failure behaviors, Measurement 168 \(2021\) 108286.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb53)
- <span id="page-18-17"></span>[54] [T. Hu, Y.M. Guo, L.D. Gu, Y.F. Zhou, Z.S. Zhang, Z.T. Zhou, Remaining useful](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb54) [life prediction of bearings under different working conditions using a deep](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb54) [feature disentanglement based transfer learning method, Reliab. Eng. Syst.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb54) [Saf. 219 \(2022\) 108265.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb54)
- <span id="page-18-18"></span>[55] [F. Di-Maio, K.L. Tsui, E. Zio, Combining relevance vector machines and](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb55) [exponential regression for bearing residual life estimation, Mech. Syst.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb55) [Signal Process. 31 \(2012\) 405–427.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb55)
- <span id="page-18-19"></span>[56] [N.P. Li, Y.G. Lei, J. Lin, S.X. Ding, An improved exponential model for](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb56) [predicting remaining useful life of rolling element bearings, IEEE Trans.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb56) [Ind. Electron. 62 \(12\) \(2015\) 7762–7773.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb56)
- <span id="page-18-20"></span>[57] [C.X. Gao, K. Lv, T. Wu, J.K. Si, Y.H. Hu, Method for determining start](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb57)[ing point of rolling bearing life prediction based on linear regression,](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb57) [Electronics 8 \(9\) \(2019\) 923.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb57)
- <span id="page-18-21"></span>[58] [R. Nazir, Taylor series expansion based repetitive controllers for power](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb58) [converters, subject to fractional delays, Control Eng. Pract. 64 \(2017\)](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb58) [140–147.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb58)
- <span id="page-18-22"></span>[59] [F.A. Gers, J. Schmidhuber, F. Cummins, Learning to forget: Continual](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb59) [prediction with LSTM, Neural Comput. 12 \(10\) \(2000\) 2451–2471.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb59)
- <span id="page-18-23"></span>[60] [H.H. Qiao, T.Y. Wang, P. Wang, A tool wear monitoring and prediction](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb60) [system based on multiscale deep learning models and fog computing, Int.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb60) [J. Adv. Manuf. Technol. 108 \(2020\) 2367–2384.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb60)
- <span id="page-18-24"></span>[61] [Z.G. Tian, L. Wong, N. Safaei, A neural network approach for remaining](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb61) [useful life prediction utilizing both failure and suspension histories, Mech.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb61) [Syst. Signal Process. 24 \(5\) \(2010\) 1542–1555.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb61)
- <span id="page-18-25"></span>[62] [V.T. Tran, B.S. Yang, A. Tan, Multi-step ahead direct prediction for the ma](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb62)[chine condition prognosis using regression trees and neuro-fuzzy systems,](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb62) [Expert. Syst. Appl. 36 \(5\) \(2009\) 9378–9387.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb62)
- <span id="page-18-26"></span>[63] [B. Wang, Y.G. Lei, N.P. Li, A hybrid prognostics approach for estimating](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb63) [remaining useful life of rolling element bearings, IEEE Trans. Reliab. 69 \(1\)](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb63) [\(2018\) 401–412.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb63)
- <span id="page-18-27"></span>[64] [M.F. He, Y.G. Zhou, Y. Li, G.F. Wu, G. Tang, Long short-term memory](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb64) [network with multi-resolution singular value decomposition for prediction](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb64) [of bearing performance degradation, Measurement 156 \(2020\) 107582.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb64)
- <span id="page-18-28"></span>[65] [C. Hu, B.D. Youn, P.F. Wang, J.T. Yoon, Ensemble of data-driven prognostic](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb65) [algorithms for robust prediction of remaining useful life, Reliab. Eng. Syst.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb65) [Saf. 103 \(2012\) 120–135.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb65)
- <span id="page-18-29"></span>[66] [X.B. Zhou, H.J. Ma, J.G. Gu, H.L. Chen, W. Deng, Parameter adaptation-based](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb66) [ant colony optimization with dynamic hybrid mechanism, Eng. Appl. Artif.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb66) [Intel. 114 \(2022\) 105139.](http://refhub.elsevier.com/S1568-4946(22)00679-2/sb66)
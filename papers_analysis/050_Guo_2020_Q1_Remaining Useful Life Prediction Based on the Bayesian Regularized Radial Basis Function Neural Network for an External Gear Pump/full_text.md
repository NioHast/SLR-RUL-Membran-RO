![](_page_0_Picture_0.jpeg)

Received May 27, 2020, accepted June 5, 2020, date of publication June 9, 2020, date of current version June 19, 2020.

*Digital Object Identifier 10.1109/ACCESS.2020.3001013*

# Remaining Useful Life Prediction Based on the Bayesian Regularized Radial Basis Function Neural Network for an External Gear Pump

RUI GUO [1](https://orcid.org/0000-0003-0506-6677),2[, Y](https://orcid.org/0000-0003-4959-7234)ONGTAO L[I](https://orcid.org/0000-0003-2825-5075) 1,3, LIJIANG [ZH](https://orcid.org/0000-0001-7133-7485)A[O](https://orcid.org/0000-0001-5537-7559) 1,3 , JINGYI ZHAO 1,4, AND DIANRONG GAO 1,4

<sup>1</sup>Hebei Provincial Key Laboratory of Heavy Machinery Fluid Power Transmission and Control, Yanshan University, Qinhuangdao 066004, China

Corresponding author: Rui Guo (guorui@ysu.edu.cn)

This work was supported in part by the National Key Research and Development Program of China under Grant 2019YFB2005204, in part by the National Natural Science Foundation of China under Grant 51675461 and Grant 11673040, and in part by the Open Foundation of the State Key Laboratory of Fluid Power and Mechatronic Systems under Grant GZKF-201922.

**ABSTRACT** A remaining useful life (RUL) prediction method for an external gear pump is proposed by Bayesian regularized radial basis function neural network (Trainbr-RBFNN). The variational mode decomposition (VMD) algorithm has been used to denoise the vibration data of accelerated degradation test, followed by which, using the Hilbert modulation the reconstructed signal has been demodulated. After which, compared with the ensemble empirical mode decomposition (EEMD) algorithm and the modified ensemble empirical mode decomposition (MEEMD) algorithm. Subsequently, factor analysis (FA) has been selected to realize the fusion of various characteristic parameters, after which, the external gear pump's degradation evaluation index established and analyzed. Finally, the degradation evaluation index has been used to train the Trainbr-RBFNN model, and achieve gear pump degradation evaluation model for RUL prediction. Experiment results evidence that the RUL of the external gear pump can be accurately evaluated with the method used.

**INDEX TERMS** External gear pump, RUL, Trainbr-RBFNN, VMD, parameter fusion.

# **I. INTRODUCTION**

As a typical hydraulic pump, gear pump is widely used in the fields of mobile machine, ship and aerospace, and its service life and performance have a significant effect on the normal operation of mechanical equipment. Various factors, such as maintenance status and working environment, and others easily affects the gear pump's performance status. Thus, it is of great significance to study the life prediction technology of hydraulic pump for fault prediction and health management of equipment [1]–[3].

Performance degradation-based method of life prediction can derive the product's hidden life information without observing the occurrence of failure. In fact, it has emerged as a high reliability and long-life product reliability evaluation and life prediction development trend [4]. Under the

The associate editor coordinating the [rev](https://orcid.org/0000-0002-2673-9909)iew of this manuscript and approving it for publication was Zhaojun Li .

condition of accelerated test, it is the current research focus to establish a proper model to accurately predict the RUL of in-service parts. RUL prediction models of various hydraulic pumps can be roughly divided into physical model, statistical and random process model, machine learning algorithm model, etc.

In terms of physical models, Ma *et al.* [5] combined with the evaluation method of degradation model parameters under Weibull distribution, selected high temperature and small flow as the performance degradation parameters of the piston pump, carried out reliability evaluation and RUL under Weibull distribution. Using pressure and speed as acceleration stress together, Huang *et al.* [6] conducted an accelerated degradation test on the piston pump, extracted high temperature and small flow signals as degradation characteristics, and established a prediction method for the remaining life of the piston pump. Based on the dynamic randomness of the performance degradation trajectory of the hydraulic pump, the

<sup>2</sup>State Key Laboratory of Fluid Power and Mechatronic Systems, Zhejiang University, Hangzhou 310027, China

<sup>3</sup>Key Laboratory of Advanced Forging and Stamping Technology and Science, Yanshan University, Qinhuangdao 066004, China

<sup>4</sup>Hebei Key Laboratory of Special Delivery Equipment, Yanshan University, Qinhuangdao 066004, China

![](_page_1_Picture_1.jpeg)

Wiener process in the random process can be used to describe the performance degradation process of the hydraulic pump. According to Wang *et al.* [1] the return oil flow characterizes the internal wear state of the axial piston pump. Based on Wiener process, the performance degradation model of piston pump is established. With gear pump as the research object Liu *et al.* [7] used the Wiener process with random effect and established the gear pump's volumetric efficiency and total efficiency degradation process model. Based on binary Wiener process, a small sample reliable life prediction method is proposed.

The machine learning algorithm model has powerful data processing ability and good robustness, and it has strong adaptability to the degradation trajectory of the research object, so it is widely used. Through oil state detection, the hydraulic pump's life characteristic information was obtained by He et al. [8] Thereby, based on the improved gray neural network, they established a prediction model of gray support vector machine. Jiao et al. [9] built a airborne fuel pump life test platform, extracted the average pressure signal as the performance degradation characteristics, and proposed a combined RUL prediction method based on adaptive differential evaluation grey wolf optimization-support vector machine (ADEGWO-SVM). According to the degradation characteristics of the plunger pump, Li et al. [10] proposed a method to extract the degradation characteristics of the hydraulic pump based on the relative entropy, and predicted the remaining life of the plunger pump.

Thus, the current research is usually based on a single characteristic parameter obtained from the time-domain, frequency-domain or time-frequency-domain to predict the RUL of the hydraulic pump. It can only reflect the degradation trend of the hydraulic pump to a certain extent, but cannot predict the performance degradation trend of the hydraulic pump under the working environment affected by various factors.

In line with the above-cited concerns, based on Trainbr-RBFNN – which belongs to feed-forward neural network – a RUL prediction method of gear pump is proposed. Each characteristic parameter obtained from the time-domain, frequency-domain and time-frequency-domain was fused to construct degradation index. The degenerate fusion index was used to train the Trainbr-RBFNN, and a gear pump degradation model was constructed. Through the degradation model, the gear pump flow is effectively predicted, and the RUL prediction of the gear pump is completed.

In the rest of the paper: Section 2: The algorithm used in this paper is introduced. Section 3: The characterization of the degradation performance of the external gear pump is selected and in noise reduction the superiority of the variational mode decomposition algorithm is compared and analyzed. Section 4: The degradation performance indicators are analyzed and with multiple feature parameters degradation fusion indicators were analyzed and constructed. Section 5: The Trainbr-RBFNN algorithm is elaborated and by the RUL prediction of the external gear pump the superiority of the

algorithm is verified. Section 6: The paper is brought to a conclusion.

#### **II. PRELIMINARIES**

In this section, the VMD method, the RBFNN prediction method, and the Bayesian regularization algorithm (Trainbr) principle is introduced.

#### A. VARIATIONAL MODE DECOMPOSITION

According to VMD, the intrinsic mode function (IMF) is defined as the amplitude-modulated-frequency-modulated signal, as shown below:

<span id="page-1-0"></span>
$$u_k(t) = A_k(t)\cos(\varphi_k(t)) \tag{1}$$

where,  $A_k(t)$  is the instantaneous amplitude of  $u_k(t)$ ,  $\varphi_k(t)$  is a non-decreasing function, the instantaneous frequency of  $u_k(t)$  is  $\omega_k(t)$ , and  $\omega_k(t) := \varphi'_k(t)$ .

VMD establishes the following constraint variational model:

<span id="page-1-1"></span>
$$\begin{cases} \min_{\{u_k\}, \{\omega_k\}} \left\{ \sum_k \left\| \partial_t \left[ \left( \delta \left( t \right) + \frac{j}{\pi t} \right) * u_k \left( t \right) \right] e^{-j\omega_k t} \right\|_2^2 \right\} \\ \text{s.t. } \sum_k u_k = f \end{cases}$$
 (2)

where,  $u_k$  is the modal function, and  $\{u_k\} := \{u_1, \dots, u_k\}, \omega_k$  is the frequency of each center, and  $\{\omega_k\} := \{\omega_1, \dots, \omega_k\}, k$  is the number of modes to be decomposed,  $\delta(t)$  is the Dirac function.

It is essential change the constrained variational problem into a non-constrained variational problem, when solving the variational problem. As such, the Lagrange multiplication operator  $\lambda$  (t) and the second penalty factor  $\alpha$  are introduced into it. This section gives the extended Lagrangian expression.

<span id="page-1-2"></span>
$$L\left(\left\{u_{k}\right\},\left\{\omega_{k}\right\},\lambda\right)$$

$$:=\alpha\sum_{k}\left\|\partial_{t}\left[\left(\delta\left(t\right)+\frac{j}{\pi t}\right)*u_{k}\left(t\right)\right]e^{-j\omega_{k}t}\right\|_{2}^{2}$$

$$+\left\|f\left(t\right)-\sum_{k}u_{k}\left(t\right)\right\|_{2}^{2}+\left\langle\lambda\left(t\right),f\left(t\right)-\sum_{k}u_{k}\left(t\right)\right\rangle$$
(3)

where  $\alpha$  is the second penalty factor.

The alternate direction method of multipliers is used to solve the above variational problem, and the saddle point of the extended Lagrangian expression is obtained by iterative optimization of  $u_k^{n+1}$ ,  $\omega_k^{n+1}$ ,  $\lambda^{n+1}$ . The iteration steps are as follows:

- (1) Initialize  $\{\hat{u}_k^1\}$ ,  $\{\omega_k^1\}$ ,  $\hat{\lambda}^1$ ,  $n \leftarrow 0$ .
- (2)  $n \leftarrow n + 1$ , execute the entire loop.
- (3) Update  $u_k$ :

$$\widehat{u}_{k}^{n+1}(\omega) \leftarrow \frac{\widehat{f}(\omega) - \sum_{i < k} \widehat{u}_{i}^{n+1}(\omega) - \sum_{i > k} \widehat{u}_{i}^{n}(\omega) + \frac{\widehat{\lambda}^{n}(\omega)}{2}}{1 + 2\alpha \left(\omega - \omega_{k}^{n}\right)^{2}}$$

$$\tag{4}$$

![](_page_2_Picture_1.jpeg)

![](_page_2_Figure_2.jpeg)

FIGURE 1. RBF neural network topology diagram.

(4) Update  $\omega_k$ 

$$\omega_k^{n+1} \leftarrow \frac{\int_0^\infty \omega \left| \hat{u}_k^{n+1} \left( \omega \right) \right|^2 d\omega}{\int_0^\infty \left| \hat{u}_k^{n+1} \left( \omega \right) \right|^2 d\omega} \tag{5}$$

(5) Update  $\hat{\lambda}$ 

$$\widehat{\lambda}^{n+1}(\omega) \leftarrow \widehat{\lambda}^{n}(\omega) + \tau \left(\widehat{f}(\omega) - \sum_{k} \widehat{u}_{k}^{n+1}(\omega)\right)$$
 (6)

By repeating the above steps until the following formulas 6 are satisfied, *K* modal components can be obtained.

$$\sum_{k} \left\| \widehat{u}_{k}^{n+1} - \widehat{u}_{k}^{n} \right\|_{2}^{2} / \left\| \widehat{u}_{k}^{n} \right\|_{2}^{2} < \varepsilon \tag{7}$$

where,  $\varepsilon$  and  $\tau$  are the tolerance range and Lagrangian multiplier update parameter respectively,  $\varepsilon=10^{-7}$  and  $\tau=0$ .

# B. RADIAL BASIS FUNCTION NEURAL NETWORK

Radial basis function (RBF) neural network is a three-layer forward network, which can approximate any continuous nonlinear network with any accuracy. It has been widely used in speech recognition, function approximation, pattern recognition, image processing and fault diagnosis [13]. The input layer is the first layer which consists of signal source nodes. The second layer is the hidden layer and their number depends on the solutions needed. The third layer is the output layer, which is the response to the input mode. Fig. 1 presents the RBF neural network topology.

In the figure, x is the input vector, and  $x = (x_1, x_2, \dots, x_n)^T \in \mathbb{R}^n$ , W is the output weight matrix, and  $W \in \mathbb{R}^{h \times m}$ , y is network output, and  $y = (y_1, y_2, \dots, y_m)$ , c is the center of network hidden layer node, and  $c = (c_1, c_2, \dots, c_h)$ ,  $\Sigma$  indicates that the neuron in the output layer adopts the linear activation function.

In this paper, a Gaussian function that is easy to program and calculate is used as the activation function of the RBF neural network. The output of the network is as follows:

$$y_j = \sum_{i=1}^h W_{ij} \exp\left(-\frac{1}{2\sigma^2} \|x_k - c_i\|^2\right)$$
 (8)

where,  $\sigma$  is the variance between the expected output and the actual output of the sample, and the formula is as follows:

$$\sigma = \frac{1}{n} \sum_{i=1}^{m} \|d_i - y_j c_i\|^2$$
 (9)

where, i represents the number of hidden layer nodes, and  $i=1,2,\cdots,h,j$  is the number of network outputs, and  $j=1,2,\cdots,m,k$  represents the number of network inputs, and  $k=1,2,\cdots,n,d$  represents the expected output of the sample.

#### C. BAYESIAN REGULARIZATION ALGORITHM

In the training process of the neural network, Trainbr minimizes the error of the performance function by introducing a correction function. The correction function is as follows:

$$f(w) = VE_w + \beta E_d \tag{10}$$

where, f(w) is the modified performance function, V and  $\beta$  are the regularization parameters,  $E_w$  is the mean square error of the network ownership value, and  $E_d$  is the mean square error of the network output result.

Trainbr can adjust the size of V and  $\beta$  adaptively, so as to optimize the network weight. Under the Bayesian rule, when the learning set is determined, the posterior probability density function of the weight is as follows:

$$p(\omega|D, V, \beta, M) = \frac{p(D|\omega, \beta, M)p(\omega|V, M)}{p(D|V, \beta, M)} \quad (11)$$

where,  $\omega$  is the weight vector, D is the learning set data, M is the adopted neural network model,  $p(D|V,\beta,M)$  is the standardization factor, to ensure that the overall probability is 1,  $p(\omega|V,M)$  is the prior probability density function of the weight vector, and  $p(D|\omega,\beta,M)$  is the probability density function output when the weight is given.

Assuming that the noise and weight vector in the sample data are Gaussian distribution, the following formula holds.

$$\begin{cases} p(D|\omega, \beta, M) = \frac{\exp(-\beta E_d)}{Z_n(\beta)} \\ p(\omega|V, M) = \frac{\exp(-VE_w)}{Z_m(V)} \end{cases}$$
 (12)

where,  $Z_n(\beta) = (\pi/\beta)^{n/2}$ , and  $Z_m(V) = (\pi/V)^{m/2}$ .

Take formula (12) into formula (11), which can be written as follows:

$$p(\omega|D, V, \beta, M) = \frac{e^{-(VE_w + \beta E_d)} / (Z_n(\beta) Z_m(V))}{p(D|V, \beta, M)}$$
$$= \frac{e^{-f(\omega)}}{Z(V, \beta)}$$
(13)

where,  $Z(V, \beta) = p(D|V, \beta, M)/(Z_n(\beta)Z_m(V))$ .

![](_page_3_Picture_1.jpeg)

![](_page_3_Figure_2.jpeg)

**FIGURE 2.** Test system schematic diagram.

In the Bayesian model, the posterior probability density function *p* (ω |*D*, *V*, β, *M* ) of the optimal weight vector should be the largest. In addition, the performance function *f* (ω) should be the minimum when *Z* (*V*, β) is determined. The optimal solution of *v* and β at the minimum point ω<sup>0</sup> of *f* (ω) is obtained as follows:

$$\begin{cases} V = \frac{\gamma}{2E_w(\omega_0)} \\ \beta = \frac{m - \gamma}{2E_d(\omega_0)} \end{cases}$$
 (14)

where, γ is the number of effective parameters of neural network, and *m* is the total number of parameters of neural network.

# **III. CONSTRUCTION OF TEST BENCH AND DATA COLLECTION AND PROCESSING**

The step-stress acceleration test is conducted by accelerated life test(ALT)bench on four Hefei Changyuan gear pumps CBW-F304 of the same type. Throughout the ALT, in order to monitor and collect changes in the output flow, vibration of the gear pump, torque and speed, various sensors are installed in the test. Fig. 2 shows the principle of the gear pump ALT bench.

The main purpose of the ALT is to collect vibration signal, torque speed signal and flow signal to predict the life of the gear pump. In the vertical direction, horizontal direction and axial direction of the gear pump, acceleration sensors are installed to collect vibration signals. The experimental device is shown in Fig. 3:

In this experiment, the external gear pump is loaded with step-stress. The minimum pressure is 23 MPa, and the maximum pressure is 27 MPa. According to the industry standard *Hydraulic gear pump JBT7014.2-2018*, under the rated working condition, the volume efficiency is less than 82%, which is considered as failure. Using quantitative truncation method, when one of the four pumps reaches the specified amount of degradation for two consecutive measurements, the stress is raised to the next stress stage, as shown in Table 1:

![](_page_3_Picture_11.jpeg)

**FIGURE 3.** Test device physical map.

**TABLE 1.** Quantitative truncation method.

| Pressure (MPa)             | 23 | 25 | 27 |
|----------------------------|----|----|----|
| Volunetric efficiency drop | 5% | 5% | 5% |

The ALT is to collect data every 10 minutes. The specific test process is as follows:

- (1) Pressure of the collection branch to be adjusted to 20 Mpa and the test pressure to 23 Mpa;
- (2) The system to be switched to the collection branch and the initial flow of the gear pump recorded;
- (3) During the experiment, the system has been working under the accelerated stress. Every ten minutes, the system will automatically switch to the acquisition branch for data acquisition.
- (4) This experiment uses a quantitative truncation method. When the flow of the external gear pump drops to the specified degradation amount, the stress is increased to the next stage. In the final stress stage, when the flow reaches the specified degradation amount, the test is terminated.

During the entire ALT cycle of the gear pump, the vibration test data obtained in the early stage, the middle stage and the later stage of ALT are selected for analysis and processing. Fig. 4 shows that change trend of gear pump vibration signal in time-domain.

During different ALT periods, the change in trend of the vibration signal in the frequency-domain of the gear pump is shown in Fig. 5.

The vibration signal of gear pump contains a lot of life characteristic information. No matter what kind of fault the gear pump is, it can be seen from the vibration of pump shaft and pump shell. It can be seen from time-domain and frequency-domain that the amplitude and frequency of vibration signal of gear pump change with the operation of ALT, which reflects the performance degradation trend of the gear pump, so vibration signal can be chosen as the characterization of the degradation performance of external gear pump.

![](_page_4_Figure_2.jpeg)

**FIGURE 4.** Time-domain plot of vibration signals at different test periods:(a) Early test, (b) Mid test, and (c) Late test.

![](_page_4_Figure_4.jpeg)

**FIGURE 5.** Frequency-domain diagram of vibration signals at different test periods:(a) Early test, (b) Mid test, and (c) Late test.

In this paper, the VMD method is selected to reduce the noise of vibration signal, and the envelope demodulation of the reconstructed signal is carried out. A comparative analysis of simulation signals was used to illustrate the superiority of the VMD algorithm relative to the EEMD and MEEMD algorithms. The simulation signal *x* (*t*) is composed of two cosine signals and a 2db white noise signal, wherein the expression of the cosine signal is as follows:

$$x_1(t) = \cos(2\pi \times 2t) \tag{15}$$

$$x_2(t) = \frac{1}{4}\cos(2\pi \times 24t)$$
 (16)

The following figure illustrates the simulation signal composition process:

In order to extract the fault information, in addition to filtering and reducing the noise of the measured signal, the envelope signal must be obtained through Hilbert transform in order to extract the fault information in the low-frequency signal from the high-frequency signal. The EEMD, MEEMD and VMD algorithms are used to perform noise reduction analysis on the simulation signals. Figs. 7-9 show the steps to obtain IMF components of the simulation signals under the three algorithms:

![](_page_4_Figure_11.jpeg)

**FIGURE 6.** Schematic diagram of simulation signal composition: (a) Cosine signal 1, (b) Cosine signal 2, (c) noise signal, and (d) Simulation signal.

![](_page_4_Figure_13.jpeg)

**FIGURE 7.** Decomposition results of EEMD method: (a) Component of IMF, and (b) Spectrum of IMF.

Figs. 7-8 shows that the frequency components of the first four IMF components of the simulation signal are still complex after noise reduction by the EEMD algorithm. Although the high-frequency signal of the fifth IMF component is reduced, the mode aliasing phenomenon appears, and the noise reduction effect is not obvious. After the noise reduction process of the MEEMD algorithm, the frequency components of the first IMF component are complex, and the second and third IMF components also exhibit modal aliasing.

Fig. 9 shows that VMD has a better decomposition effect as (i) the fluctuation trend of the first modal component signal basically conforms to the original simulated signal; (ii) there is no modal aliasing problem for each modal component.

After the simulation signal is modally decomposed by EEMD, MEEMD and VMD methods, the effective information contained in the signal is decomposed into various

![](_page_5_Picture_1.jpeg)

![](_page_5_Figure_2.jpeg)

**FIGURE 8.** Decomposition results of MEEMD method: (a) Component of IMF, and (b) Spectrum of IMF.

![](_page_5_Figure_4.jpeg)

**FIGURE 9.** Decomposition results of VMD method: (a) Component of IMF, and (b) Spectrum of IMF.

IMF components. If there is unreal information in the IMF component, it will cause a negative impact on the signal reconstruction, so screening out the useful IMF component is the premise of signal reconstruction. To filter out the useful component and the false component effectively the correlation coefficient between each IMF component and the original signal is calculated using correlation coefficient method.

Formula (17) presents the calculation process of the correlation coefficient:

$$R = \frac{\sum_{n=0}^{\infty} x(n) y(n)}{\sqrt{\sum_{n=0}^{\infty} x^2(n) \sum_{n=0}^{\infty} y^2(n)}}$$
(17)

where, *x* (*n*) and *y* (*n*) are the two sequences for solving the correlation coefficient.

This method is an important method to judge whether the IMF component is effective or not. Its threshold value is set to 10% of the maximum value in the correlation coefficient sequence. The correlation between the IMF component and the original signal is proportionate to the correlation coefficient. According to formula (17), the correlation coefficient

![](_page_5_Figure_11.jpeg)

**FIGURE 10.** Signal reconstruction diagram after decomposition by EEMD, MEEMD and VMD: (a) Simulation signal, (b) EEMD Reconstructed signal, (c) MEEMD Reconstructed signal, AND (d) VMD Reconstructed signal.

**TABLE 2.** Calculation results of SNR and RMSE.

| Noise reduction method | SNR/db | RMSE |
|------------------------|--------|------|
| EEMD                   | 3.58   | 0.95 |
| MEEMD                  | 12.24  | 0.18 |
| VMD                    | 15.43  | 0.13 |

*R* of each IMF component relative to the simulation signal is calculated, and the effective component is screened out according to the correlation coefficient *R*. Finally, the effective components of the three methods are selected for signal reconstruction, as shown in Fig. 10.

It can be seen from Fig. 10 that in the reconstructed waveform of simulated signal processed by EEMD and MEEMD methods, the frequency component is still relatively complex and the noise reduction effect is not good. After noise reduction by the VMD method, the resulting waveform of the reconstructed signal is clearer and the noise reduction effect is better.

Also, the signal to noise ratio (SNR) and the root mean square error (RMSE) is used to further evaluate the effect of three noise reduction methods. Based on the SNR and the RMSE, Table 2 shows the calculation results of the three noise reduction methods.

It can be seen from Table 2 that after denoising the signal based on the VMD method, the SNR obtained is the largest and the RMSE is the smallest, indicating that the VMD method has the best noise reduction effect.

In view of the signal modulation phenomenon of the vibration signal of the gear pump measured in the experiment, this paper uses the Hilbert transform method to perform envelope demodulation on the signal after noise reduction and reconstruction. After the vibration signal undergoes Hilbert transform, the negative frequency component of the analytical signal is zero, and only the analytical signal containing the positive frequency component is obtained, and the size

![](_page_6_Figure_2.jpeg)

**FIGURE 11.** Vibration data of the gear pump at a certain time: (a) X axis amplitude, (b) Y axis amplitude, AND (c) Z axis amplitude.

of the signal becomes twice the original. In this way, the real signal of fault information can be demodulated from the actual signal.

# **IV. CONSTRUCTION OF DEGRADATION INDEX BASED ON MULTI FEATURE PARAMETER FUSION**

This paper focuses on one of the four tested gear pumps to analyze its vibration data using the No. 2 gear pump as an example. Obtain the vibration data in three directions of xaxis, y-axis, and z-axis at a certain moment, as shown in Fig. 11.

As can be seen from Fig. 11, in the vibration data of the gear pump in three directions, the amplitude in the z-axis direction is the largest. In addition, in the ALT, the wear of the end face of the gear pump is the most serious, so the vibration data in the z-axis direction is selected for the extraction and analysis of characteristic parameters.

As the earliest and most commonly used feature extraction method, time domain analysis has a wide range of applications in fault diagnosis and life prediction of mechanical equipment. The measured vibration signal is processed first to obtain the envelope demodulation signal in the degradation process. Following which, features of the envelope demodulation signal are extracted through the analysis of timedomain. The maximum, minimum, peak-to-peak, and mean values over the ALT cyclical trends are shown in Fig. 12.

It can be seen from the figure that in the whole ALT cycle of gear pump, the maximum value, minimum value and peakto-peak value only fluctuate slightly in the local range, which can not reflect the performance degradation trend of gear pump and can not be used for the RUL prediction of gear pump. It fails to reflect the degradation trend of gear pump performance as the overall change trend is still fixed in a small range, even though the mean value fluctuates greatly in a certain time point.

Over the entire ALT cycle, the trend of variance, margin, crest factor, and kurtosis are presented in Fig. 13.

The kurtosis is a dimensionless parameter, which is particularly sensitive to shock signals, and is particularly suitable for surface damage. The kurtosis index, in the middle and

![](_page_6_Figure_12.jpeg)

**FIGURE 12.** Time-domain characteristic parameters: (a) Maximum, (b) Minimum, (c) Peak-to-peak, AND (d) Mean.

![](_page_6_Figure_14.jpeg)

**FIGURE 13.** Time-domain characteristic parameters: (a) Variance, (b) Margin, (c) Crest factor, AND (d) Kurtosis.

![](_page_6_Figure_16.jpeg)

**FIGURE 14.** Time-domain characteristic parameters: (a) Root mean square value, AND (b) Pulse index.

late stages of the ALT, has a slight upward trend and clearly indicates the failure and performance degradation of gear pump.

Over the entire ALT period, the trend of the RMS value and pulse index is seen in Fig. 14.

In the middle and later period of gear pump working, the value of RMS has a slight upward trend. Thus, indicating a large vibration in the middle and later period for the gear pump with aggravated performance degradation, which reflects the performance degradation trend of gear pump.

![](_page_7_Picture_1.jpeg)

![](_page_7_Figure_2.jpeg)

**FIGURE 15.** Frequency-domain characteristic parameters: (a) Frequency standard deviation, (b) Mean square frequency, (c) Frequency center, AND (d) Frequency-domain amplitude average.

![](_page_7_Figure_4.jpeg)

**FIGURE 16.** Energy diagram of envelope signal.

This paper, as such, selects the kurtosis and RMS as the degradation performance index of the gear pump.

The characteristic index of frequency domain is analyzed by fast Fourier transform. Over the entire ALT period, the trend of the frequency standard deviation, the mean square frequency, the frequency center, and the average value of the frequency-domain are presented in Fig. 15.

The four characteristic parameters of frequency-domain have a slight upward trend over the ALT cycle. Thus, suggesting that during the test, the gear pump performance gradually degenerates with more and more severe vibrations.

This paper chooses a method combining VMD and Hilbert transform to process the nonlinear vibration signal of gear pump. After the signal is subjected to VMD noise reduction processing, the first IMF obtained is the effective component. The envelope demodulation of the effective component is carried out, and the energy diagram of the envelope signal is shown in Fig. 16. It can be seen from the figure that when the gear pump deteriorates seriously in the later stage, the energy value of envelope signal will rise.

Thus, a high dimension matrix can be formed by combining the six characteristic parameters of gear pump (i.e. kurtosis, RMS, frequency standard deviation, mean square frequency, frequency-domain amplitude average and the energy of the first IMF) with the torque and speed of gear pump.

Before the RUL prediction of the gear pump, the FA method is needed to feature fusion and dimension reduction

**TABLE 3.** No. 2 pump.

| Feature vector | Cumulative contribution rate |
|----------------|------------------------------|
| 1              | 0.9632                       |
| 2              | 0.9736                       |
| 3              | 0.9865                       |
| 4              | 0.9987                       |
| 5              | 1.0000                       |
| 6              | 1.0000                       |

![](_page_7_Figure_14.jpeg)

**FIGURE 17.** No. 2 pump: (a) Output flow change trend, AND (b) Degradation fusion index.

of the high dimension matrix, and a low latitude matrix containing the life information of the gear pump is obtained, which forms a new feature vector. The contribution rate indicates the percentage of the gear pump feature information contained in the feature vector to the original high dimension Matrix information. Typically, the cumulative contribution rate of factor analysis reaches 85%, which can meet the use requirements.

The six characteristic parameters of No. 2 gear pump in time-domain, frequency-domain and time-frequency-domain are selected and fused with torque and speed to get the eigenvector. Table 3 presents the cumulative contribution rate of each feature vector.

It can be seen from Table 3 that the cumulative contribution rate of the first feature vector has reached 96%, which can characterize the degraded trend of the gear and achieve the experimental purpose. Therefore, the first feature vector is selected as the gear pump degraded fusion index. Fig. 17 presents the degradation fusion index and flow change trend of No. 2 gear pump.

In the flow rate trend graph, there are two horizontal dashed lines. The first dotted line is the cutoff line of the failure threshold of gear pump. According to the industry standard *Hydraulic gear pump JBT7014.2-2018*, when the pressure of gear pump is within 10-25mpa, the volumetric efficiency is lower than 82%, and the parts are worn or damaged, it is considered as failure. The purpose of setting this dotted line is to determine the failure time of gear pump. The second dotted line is the cut-off line when the volumetric efficiency of gear

![](_page_8_Figure_2.jpeg)

**FIGURE 18.** Prediction results of degradation fusion index of No. 2 pump.

![](_page_8_Figure_4.jpeg)

**FIGURE 19.** Pump No. 2 prediction error.

pump reaches 75%. The purpose of setting this dotted line is to further verify the accuracy of Trainbr-RBFNN algorithm when the failure threshold is reached.

For the No. 2 gear pump, Holt two-parameter exponential smoothing method is used for the degradation fusion index prediction. Fig. 18 shows the prediction results.

From the middle and later period of the test, i.e. 600 hours, the degradation fusion index is predicted, and the prediction results are shown in the blue box in Fig. 18. The prediction results can be used for RUL prediction as they are largely in line with the actual trend. The error between the forecast and the actual trend is seen in Fig. 19.

It can be seen from Fig. 19 that the prediction error of the degraded fusion index of the No. 2 tested gear pump is very small, and it is basically maintained at about 1%. Thus, Holt two-parameter exponential smoothing method can provide accurate degradation fusion index predictions as well as smoothen the degradation trajectory.

## **V. LIFE PREDICTION OF EXTERNAL GEAR PUMP**

It is essential to train the network model, before using Trainbr-RBFNN for the gear pumps' RUL prediction. The training set data of the Trainbr-RBFNN model is the output flow and degradation fusion index between the 0h and 650h of the four gear pumps. While, the test set data is the degradation fusion index between 650h and 1000h. However, before the model training and prediction, the training set data and the test set data need to be normalized. The purpose of normalization processing is to make the training set data and the test set

![](_page_8_Figure_12.jpeg)

**FIGURE 20.** Comparison of actual flow value of No. 2 pump and predicted value of RBFNN.

![](_page_8_Figure_14.jpeg)

**FIGURE 21.** Comparison of actual flow value of No. 2 pump and ANFIS predicted value.

![](_page_8_Figure_16.jpeg)

**FIGURE 22.** Comparison of actual flow value of No. 2 pump with Trainbr-BP predicted value.

data have the same order of magnitude, so as to eliminate the influence of dimension.

In order to verify the accuracy of the algorithm in this paper, the prediction results of this algorithm are compared with the prediction results of RBFNN algorithm, adaptivenetwork-based fuzzy inference system (ANFIS) algorithm and Trainbr back propagation (BP) algorithm respectively. The comparison results are shown in Figs. 20-23. The solid black line in these figures is the fitted line between the actual flow value and the predicted flow value. In addition, there are two horizontal dashes in each figure, which have the same meaning as the dashes in Figure 17.

According to Figs. 20-23 shows that compared with the actual values, the fitting effect of the predicted values of the gear pump flow through the Trainbr-RBFNN algorithm is better than the other three methods. As shown in Table 4, the mean square error of the Trainbr-RBFNN algorithm is

![](_page_9_Picture_1.jpeg)

![](_page_9_Figure_2.jpeg)

**FIGURE 23.** Comparison of the actual flow value of No. 2 pump and the predicted value of Trainbr-RBFNN.

**TABLE 4.** Mean square error of four algorithms.

| Algorithm name          | Mean square error |
|-------------------------|-------------------|
| RBFNN algorithm         | 0.0069            |
| ANFIS algorithm         | 0.0034            |
| Trainbr-BP algorithm    | 9.9903e-04        |
| Trainbr-RBFNN algorithm | 3.7843e-04        |

the smallest among the four prediction algorithms. Thus, it is safely inferred that the prediction accuracy of the method is the highest.

Compared with other life distribution models, Weibull distribution has the advantages of being suitable for small sample sampling, and has strong adaptability to various types of test data [36]. The life of hydraulic pump depends on the weak link, so it is suitable to use Weibull distribution as the life distribution model.

When studying the Weibull distribution, in order to improve its universality, generally make γ = 0. At this time, the three-parameter Weibull distribution is converted into a two-parameter Weibull distribution, which greatly reduces the difficulty of parameter solving and improves the applicability. According to a large number of practical experience, and combined with the characteristics of external gear pump, this paper uses two parameter Weibull distribution model to process the failure data of step-stress ALT, and its distribution function is as follows:

$$F(t) = 1 - \exp\left[-\left(\frac{t}{\eta}\right)^m\right] \tag{18}$$

where, *m* is the shape parameter, η is the scale parameter, which also represents the characteristic life of the product.

In addition, the probability density function under the two parameter Weibull distribution is shown in formula [\(19\)](#page-9-0), and the mean time to failure (MTTF) is shown in formula [\(20\)](#page-9-0).

<span id="page-9-0"></span>
$$f(t) = \frac{m}{\eta} \left(\frac{t}{\eta}\right)^{m-1} e^{-\left(\frac{t}{\eta}\right)^m} \tag{19}$$

$$MTTF = \int_{-\infty}^{\infty} tf(t) = \eta \Gamma\left(1 + \frac{1}{m}\right)$$
 (20)

It can be seen from the above formula that the problem of average life and characteristic life of gear pump can be solved by solving parameters *m* and η of Weibull distribution.

**TABLE 5.** Reliability parameter index.

| Parameter name | m    | η      | MTTF(h) |
|----------------|------|--------|---------|
| Real life      | 1.47 | 9316.8 | 8430    |
| Predicted life | 1.34 | 9032.7 | 8298    |

The basic idea of ALT is to extrapolate the life characteristics under normal stress by using the life characteristics under high stress level. The key to realizing this basic idea is to establish the relationship between life characteristics and stress level. The relationship is called the acceleration model. The Arrhenius model and the inverse power law model are the most commonly used single-stress acceleration models, and their linearized form can be uniformly written as follows:

$$\ln \xi = a + b\phi (s) \tag{21}$$

where, ξ is the life characteristic, and φ (*s*) is the known function of the stress level *s*.

When the life of the product follows the Weibull distribution, the characteristic life η is commonly used as the life feature, so its acceleration model is as follows:

$$\ln \eta_i = a + b\varphi(s_i) \tag{22}$$

where, *a* and *b* are the estimated parameters, φ (*si*) is a function of the stress level, *i* indicates different levels of stress.

The parameters of the Weibull distribution model are estimated by the maximum likelihood estimation method, and then the reliability of the hydraulic pump is evaluated. The reliability parameters of the external gear pump of this sample were obtained through calculation. Table 5 gives the parameters under usual stress:

It can be seen from the above table that the RUL of the external gear pump predicted by this paper is similar to the actual RUL. The relative error is about 1.5%. It shows that the prediction method of RUL of external gear pump based on Trainbr-RBFNN has high accuracy.

# **VI. CONCLUSIONS**

[\(1\)](#page-1-0) A signal denoising method based on VMD-Hilbert is proposed. In addition, based on the test signal and the traditional noise reduction decomposition methods EEMD and MEEMD are compared, the results show that the VMD-Hilbert method has better noise reduction effect.

[\(2\)](#page-1-1) The degradation index of multi-feature parameter fusion is constructed. The characteristic parameters of the time-domain, frequency-domain and time-frequency-domain are used to extract and analyze the degradation performance index of vibration signal. The multi-feature parameters are fused and dimensionally reduced using the FA method. Finally, for increasing the robustness and smoothness of degradation fusion index, the Holt two-parameter exponential smoothing method is proposed. Through this method, the accurate prediction of the degradation fusion index of the external gear pump is realized.

![](_page_10_Picture_1.jpeg)

[\(3\)](#page-1-2) In this paper, the output flow of the external gear pump serves as the basis for failure judgment, and a RUL prediction method of the external gear pump based on Trainbr-RBFNN is proposed. Trainbr-RBFNN was trained based on the flow rate and degradation fusion index of gear pump. The degradation assessment model of gear pump was established, and the failure time of the gear pump under accelerated stress is effectively predicted. In addition, according to the life distribution model and acceleration model of the gear pump, the failure time under usual stress was deduced, and the RUL prediction of the external gear pump is completed.

## **REFERENCES**

- [1] X. Wang, S. Lin, S. Wang, Z. He, and C. Zhang, ''Remaining useful life prediction based on the Wiener process for an aviation axial piston pump,'' *Chin. J. Aeronaut.*, vol. 29, no. 3, pp. 779–788, Jun. 2016.
- [2] L. Han, S. Wang, and C. Zhang, ''A partial lubrication model between valve plate and cylinder block in axial piston pumps,'' *Proc. Inst. Mech. Eng. C, J. Mech. Eng. Sci.*, vol. 229, no. 17, pp. 3201–3217, Dec. 2015.
- [3] J. Du, S. Wang, and H. Zhang, ''Layered clustering multi-fault diagnosis for hydraulic piston pump,'' *Mech. Syst. Signal Process.*, vol. 36, no. 2, pp. 487–504, Apr. 2013, doi: [10.1016/j.ymssp.2012.10.020.](http://dx.doi.org/10.1016/j.ymssp.2012.10.020)
- [4] Z.-S. Ye, N. Chen, and Y. Shen, ''A new class of Wiener process models for degradation analysis,'' *Rel. Eng. Syst. Saf.*, vol. 139, pp. 58–67, Jul. 2015, doi: [10.1016/j.ress.2015.02.005.](http://dx.doi.org/10.1016/j.ress.2015.02.005)
- [5] J. Ma, J. Chen, H. Liu, and L. Wang, ''Life prediction and reliability analysis based on accelerated degradation data,'' *Comp. Dig. Eng.*, vol. 47, no. 7, pp. 1613–1617, Jul. 2019.
- [6] A. Huang, Y. Guo, and J. Yu, ''Research on residual life prediction technique of hydraulic pump based on accelerated degradation data,'' *Mach. Des. Man.*, vol. 1, pp. 154–155, Jan. 2011, doi: [10.19356/j.cnki.1001-](http://dx.doi.org/10.19356/j.cnki.1001-3997.2011.01.062) [3997.2011.01.062.](http://dx.doi.org/10.19356/j.cnki.1001-3997.2011.01.062)
- [7] X. Liu, B. Guo, D. Cui, Z. Wu, and L. Zhang, ''Q-precentile life prediction based on bivariate Wiener process for gear pump with small sample size,'' *Chin. Mech. Eng.*, vol. 31, no. 11, pp. 1–9, Jun. 2020.
- [8] Q. He, G. Chen, X. Chen, and C. Yao, ''Life prediction of hydraulic pump based on an improved grey neural network,'' *Chin. Mech. Eng.*, vol. 24, no. 4, pp. 500–506, Feb. 2013.
- [9] X. Jiao, B. Jing, J. Li, M. Sun, and Y. Wang, ''Research on remaining useful life prediction of fuel pump based on adaptive differential evaluation grey wolf optimizer-support vector machine,'' *Chin. J. Sci. Instr.*, vol. 39, no. 8, pp. 43–52, Aug. 2018, doi: [10.19650/j.cnki.cjsi.J1803322.](http://dx.doi.org/10.19650/j.cnki.cjsi.J1803322)
- [10] H. Li, J. Sun, H. Ma, Z. Tian, and Y. Li, ''A novel method based upon modified composite spectrum and relative entropy for degradation feature extraction of hydraulic pump,'' *Mech. Syst. Signal Process.*, vol. 114, pp. 399–412, Jan. 2019, doi: [10.1016/j.ymssp.2018.04.040.](http://dx.doi.org/10.1016/j.ymssp.2018.04.040)
- [11] J. Ma and X. Zhan, ''Performance reliability analysis of a Piston Pump affected by random degradation,'' *J. Mech. Eng.*, vol. 46, no. 14, pp. 189–193, Jul. 2010.
- [12] H. Shen, Z. Li, L. Qi, and L. Qiao, ''A method for gear fatigue life prediction considering the internal flow field of the gear pump,'' *Mech. Syst. Signal Process.*, vol. 99, pp. 921–929, Jan. 2018, doi: [10.1016/j.ymssp.2016.09.022.](http://dx.doi.org/10.1016/j.ymssp.2016.09.022)
- [13] C. Xie, Y. Wang, and B. Zhang, ''Engine fault diagnosis technology based on RBF neural network,'' *For. Eng.*, vol. 35, no. 6, pp. 61–66, Oct. 2019, doi: [10.16270/j.cnki.slgc.2019.06.027.](http://dx.doi.org/10.16270/j.cnki.slgc.2019.06.027)
- [14] J. Fang, X. Wei, and L. Fan, ''Reliability analysis of aircraft hydraulic pump based on performance degradation data,'' *Mech. Res. App.*, vol. 21, no. 6, pp. 30–33, Dec. 2008.
- [15] D. Wang, K.-L. Tsui, and Q. Miao, ''Prognostics and health management: A review of vibration based bearing and gear health indicators,'' *IEEE Access*, vol. 6, pp. 665–676, 2018, doi: [10.1109/ACCESS.2017.2774261.](http://dx.doi.org/10.1109/ACCESS.2017.2774261)
- [16] N. Li, Y. Lei, L. Guo, T. Yan, and J. Lin, ''Remaining useful life prediction based on a general expression of stochastic process models,'' *IEEE Trans. Ind. Electron.*, vol. 64, no. 7, pp. 5709–5718, Jul. 2017, doi: [10.1109/TIE.2017.2677334.](http://dx.doi.org/10.1109/TIE.2017.2677334)
- [17] C. Ordóñez, F. Sánchez Lasheras, J. Roca-Pardiñas, and F. J. D. C. Juez, ''A hybrid ARIMA–SVM model for the study of the remaining useful life of aircraft engines,'' *J. Comput. Appl. Math.*, vol. 346, pp. 184–191, Jan. 2019, doi: [10.1016/j.cam.2018.07.008.](http://dx.doi.org/10.1016/j.cam.2018.07.008)

- [18] X. Li, Q. Ding, and J.-Q. Sun, ''Remaining useful life estimation in prognostics using deep convolution neural networks,'' *Rel. Eng. Syst. Saf.*, vol. 172, pp. 1–11, Apr. 2018, doi: [10.1016/j.ress.2017.11.021.](http://dx.doi.org/10.1016/j.ress.2017.11.021)
- [19] C. Hu, Z. Zhou, J. Zhang, and X. Si, ''A survey on life prediction of equipment,'' *Chin. J. Aeronaut.*, vol. 28, no. 1, pp. 25–33, Feb. 2015.
- [20] J. Zhao and C. Yao, ''Overview of China's hydraulic reliability technology,'' *Chin. Hydraul. Pneumatic*, vol. 10, pp. 1–7, Oct. 2013.
- [21] Q. He, G. Chen, X. Chen, C. Yao, and X. Zhang, ''Life prediction method of hydraulic pump based on grey support vector machines,'' *Lubr. Eng.*, vol. 37, no. 4, pp. 73–77, Apr. 2012.
- [22] E. Kilic, M. Dolen, H. Caliskan, A. Bugra Koku, and T. Balkan, ''Pressure prediction on a variable-speed pump controlled hydraulic system using structured recurrent neural networks,'' *Control Eng. Pract.*, vol. 26, pp. 51–71, May 2014, doi: [10.1016/j.conengprac.2014.01.008.](http://dx.doi.org/10.1016/j.conengprac.2014.01.008)
- [23] R. Khelif, B. Chebel-Morello, S. Malinowski, E. Laajili, F. Fnaiech, and N. Zerhouni, ''Direct remaining useful life estimation based on support vector regression,'' *IEEE Trans. Ind. Electron.*, vol. 64, no. 3, pp. 2276–2285, Mar. 2017, doi: [10.1109/TIE.2016.2623260.](http://dx.doi.org/10.1109/TIE.2016.2623260)
- [24] M. Kuai, G. Cheng, Y. Pang, and Y. Li, ''Research of planetary gear fault diagnosis based on permutation entropy of CEEMDAN and ANFIS,'' *Sensors*, vol. 18, no. 3, pp. 782–798, Mar. 2018, doi: [10.3390/s18030782.](http://dx.doi.org/10.3390/s18030782)
- [25] Y. Cai, Y. Zhao, X. Ma, Z. Yang, and Y. Ding, ''An extended model for fatigue life prediction and acceleration considering load frequency effect,'' *IEEE Access*, vol. 6, pp. 21064–21074, 2018, doi: [10.1109/ACCESS.2018.2820689.](http://dx.doi.org/10.1109/ACCESS.2018.2820689)
- [26] D. Wang and P. W. Tse, ''Prognostics of slurry pumps based on a moving-average wear degradation index and a general sequential Monte Carlo method,'' *Mech. Syst. Signal Process.*, vols. 56–57, pp. 213–229, May 2015.
- [27] G. Pan, J. Qiao, W. Chai, and N. Dimopoulos, ''An improved RBM based on Bayesian regularization,'' in *Proc. Int. Joint Conf. Neural Netw. (IJCNN)*, Jul. 2014, pp. 2935–2939.
- [28] D. Wang and Q. Lei, ''Fault diagnosis of power transformer based on BR-DBN,'' *Electr. Power Automat. Equip.*, vol. 38, no. 5, pp. 129–135, May 2018, doi: [10.16081/j.issn.1006-6047.2018.05.019.](http://dx.doi.org/10.16081/j.issn.1006-6047.2018.05.019)
- [29] Z. Liu, W. Jiang, W. Tan, and Y. Zhu, ''Fault identification method for hydraulic pumps based on multi-feature fusion and multiple kernel learning SVM,'' *Chin. Mech. Eng.*, vol. 27, no. 24, pp. 3355–3361, Dec. 2016.
- [30] Z. Chen, J. He, and Z. Yun, ''An adaptive identification and control scheme using radial basis function networks,'' *J. Syst. Eng. El.*, vol. 10, no. 1, pp. 54–61, Mar. 1999.
- [31] B. Cai, Y. Liu, Q. Fan, Y. Zhang, Z. Liu, S. Yu, and R. Ji, ''Multi-source information fusion based fault diagnosis of ground-source heat pump using Bayesian network,'' *Appl. Energy*, vol. 114, pp. 1–9, Feb. 2014.
- [32] M. S. Hoseinzadeh, S. E. Khadem, and M. S. Sadooghi, ''Quantitative diagnosis for bearing faults by improving ensemble empirical mode decomposition,'' *ISA Trans.*, vol. 83, pp. 261–275, Dec. 2018.
- [33] Z. Wang, G. He, W. Du, J. Zhou, X. Han, J. Wang, H. He, X. Guo, J. Wang, and Y. Kou, ''Application of parameter optimized variational mode decomposition method in fault diagnosis of gearbox,'' *IEEE Access*, vol. 7, pp. 44871–44882, Apr. 2019, doi: [10.1109/ACCESS.2019.2909300.](http://dx.doi.org/10.1109/ACCESS.2019.2909300)
- [34] W. Li, N. Wang, D. Shao, and Z. Li, ''RBF network model with EEMD phase space reconstruction application in storage life prediction of sealed electromagnetic relay,'' *Elect. Energy Manage. Technol.*, vol. 2015, no. 18, pp. 1–6, Set. 2015, doi: [10.16628/j.cnki.2095-8188.2015.18.004.](http://dx.doi.org/10.16628/j.cnki.2095-8188.2015.18.004)
- [35] Y. Sun, Y. Cao, M. Zhou, T. Wen, P. Li, and C. Roberts, ''A hybrid method for life prediction of railway relays based on multi-layer decomposition and RBFNN,'' *IEEE Access*, vol. 7, pp. 44761–44770, 2019, doi: [10.1109/ACCESS.2019.2906895.](http://dx.doi.org/10.1109/ACCESS.2019.2906895)
- [36] W. Weihull, ''A statistical distribution function of wide applicability,'' *J. Appl. Mech.*, vol. 18, no. 3, pp. 293–297, Sep. 1951.

![](_page_10_Picture_40.jpeg)

RUI GUO received the Ph.D. degree from Yanshan University, in 2010. He is currently an Associate Professor with the College of Mechanical Engineering, Yanshan University. His research interests include reliability of complex mechanical electrical and hydraulic products.

![](_page_11_Picture_1.jpeg)

![](_page_11_Picture_2.jpeg)

YONGTAO LI received the B.S. degree from the Liren College, Yanshan University, in 2018. He is currently pursuing the M.S. degree with the College of Mechanical Engineering, Yanshan University. His research interest includes life prediction of hydraulic components.

![](_page_11_Picture_4.jpeg)

JINGYI ZHAO received the Ph.D. degree from the Harbin Institute of Technology, in 2000. He is currently a Professor with the College of Mechanical Engineering, Yanshan University. His research interests include innovative design and reliability research of fluid drive and control systems.

![](_page_11_Picture_6.jpeg)

LIJIANG ZHAO received the B.S. degree from the Liren College, Yanshan University, in 2017. He is currently pursuing the M.S. degree with the College of Mechanical Engineering, Yanshan University. His research interest includes life prediction of hydraulic components.

![](_page_11_Picture_8.jpeg)

DIANRONG GAO received the Ph.D. degree from Yanshan University, in 2001. He is currently a Professor with the College of Mechanical Engineering, Yanshan University. His research interests include numerical calculation and visualization of flow field.
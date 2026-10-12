Hindawi Shock and Vibration Volume 2017, Article ID 8927937, 10 pages <https://doi.org/10.1155/2017/8927937>

![](_page_0_Picture_1.jpeg)

# *Research Article*

# **Remaining Useful Life Prediction of Bearing with Vibration Signals Based on a Novel Indicator**

## **Bo Wu, Wei Li, and Ming-quan Qiu**

*School of Mechanical and Electrical Engineering, China University of Mining and Technology, Xuzhou, China*

Correspondence should be addressed to Wei Li; liwei cmee@163.com

Received 9 July 2017; Accepted 24 September 2017; Published 29 October 2017

Academic Editor: Mickael Lallart ¨

Copyright © 2017 Bo Wu et al. This is an open access article distributed under the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.

Aiming at reducing the production downtime and maintenance cost, prognostics and health management (PHM) of rotating machinery often includes the remaining useful life (RUL) prediction of bearings. In this paper, a method combining the generalized Weibull failure rate function (WFRF) and radial basis function (RBF) neural network is developed to deal with the RUL prediction of bearings. A novel indicator, namely, the power value on the sensitive frequency band (SFB), is proposed to track bearing degradation process. Generalized WFRF is used to fit the degradation indicator series to reduce the effect of noise and avoid areas of fluctuation in the time domain. RBF neural network is employed to predict the RUL of bearings with times and fitted power values at present and previous inspections as input. Meanwhile, the life percentage is selected as output. The performance of the proposed method is validated by an accelerated bearing run-to-failure experiment, and the results demonstrate the advantage of this method in achieving more accurate RUL prediction.

## **1. Introduction**

Prognostics and health management (PHM) has received extensive attention in recent years for its effectiveness in improving reliability and reducing costs [\[1](#page-8-0), [2](#page-8-1)]. PHM generally combines condition monitoring, fault diagnostics, fault prognostics, and decision support [\[3\]](#page-8-2). Remaining useful life (RUL) prediction aims at assessing the performance degradation of equipment and detecting the impending failure [\[4\]](#page-8-3). Therefore, accurate RUL prediction is regarded as one of the most central components in performing PHM, since necessary maintenance actions are implemented based on the RUL prediction result [\[5](#page-8-4)].

Bearing is the basic component of rotating machinery and the health condition of it plays an important role in the machinery. In order to predict the RUL of bearings, many kinds of measurements are considered, including acoustic, temperature, oil analysis, and pressure. Among them, vibration is most commonly used because it is easy to measure and analyze. Besides, it can reflect the status of bearings roundly and timely [\[6](#page-8-5)]. It mainly takes two steps to realize accurate RUL prediction of bearings in vibration-based methods. Firstly, an appropriate degradation indicator should

be selected from various features. This step is the premise of RUL prediction and the selection result is crucial to the prediction accuracy. Secondly, an optimal prediction model should be developed. For the former step, there are three conventional feature extraction methods including time domain, frequency domain, and time-frequency domain. Time domain methods are directly based on the time waveform to obtain the factors such as root mean square (RMS), kurtosis, and peak. Most frequency domain methods utilize fast Fourier transformation (FFT) to convert time domain signal into frequency domain. Thus it is easy to identify the frequency components and recognize the fault characteristic frequency. Time-frequency domain methods investigate signal in both time and frequency domain, and the change of frequencies with time is described clearly. Typical time-frequency domain methods are short time Fourier transformation (STFT), Wavelet analysis, Wigner-Ville distribution, and Hilbert Huang transformation. After feature extraction, the degradation indicator is selected from them by certain standard. Various indicators have been utilized to depict the degradation process in previous research. Mahamad et al. [\[7\]](#page-8-6) selected RMS and kurtosis obtained from time waveform, while Huang et al. [\[8](#page-8-7)] utilized the minimum

quantisation error (MQE) index produced by three time features and three frequency features. Ocak et al. [\[9](#page-8-8)] and Pan et al. [\[10](#page-8-9)] decomposed the signals into wavelet packets and used the node energies of decomposition tree to indicate bearing degradation. Zhang et al. [\[11\]](#page-8-10) firstly decomposed the preprocessed signals and then selected the peak values of FFT for decomposed signals to judge the degradation of the monitored machine. In order to extract the most relevant features to the degradation process, Liao and Lee [\[12\]](#page-8-11) and Lu et al. [\[13\]](#page-8-12) used principal component analysis (PCA) to eliminate the superfluous and less-relevant features.

After the selection of degradation indicator, a prediction model should be established to perform the RUL prediction. There are mainly two categories of prediction methods: model-based methods and data-driven methods. An accurate physical model and a correct fault propagation model are essential to a model-based method. Liu and Mahadevan [\[14](#page-8-13)] proposed a unified multiaxial fatigue damage model for rolling contact fatigue, while Xu et al. [\[15\]](#page-8-14) developed an improved Paris model to predict residual fatigue life of bearings online. Jin et al. [\[16](#page-8-15)] built a degradation model for lubricant loss in bearing to predict the RUL of an individual momentum wheel bearing. If precise models are obtained, the model-based methods can provide satisfying prediction results. However, due to the complex structure, it is hard to build the physical-based models. In contrast, the data-driven methods are practical and easy to be operated, since they predict the RUL only based on the condition monitoring data. Moreover, the prediction result can be updated with new inspection data available. Yan and Lee [\[17\]](#page-9-0) utilized logistic regression to achieve performance degradation assessment. Pham and Yang [\[18](#page-9-1)] developed a liner autoregressive moving average (ARMA) model and a nonlinear generalized autoregressive conditional heteroscedasticity (GARCH) model to explain the fault condition of machine. Fei and He [\[19](#page-9-2)] applied multiple-kernel relevance vector machine (MkRVM) as an intelligent system to predict the state of bearings. Dong et al. [\[20\]](#page-9-3) employed the support vector machine (SVM) to track the degradation process of bearings and utilized Markov model to improve the prediction accuracy. Artificial neural network (ANN) has also been widely used to RUL prediction due to the well performance of function approximation. Tian [\[21](#page-9-4)] proposed an ANN to predict the RUL of pump bearings, with ages and velocity measurements as inputs and the life percentage as output. Wu et al. [\[22\]](#page-9-5) and Huang et al. [\[8\]](#page-8-7) developed a back-propagation (BP) neural network for estimating the failure time of bearings. Lee et al. [\[23](#page-9-6)] utilized an Elman neural network for health condition prediction. In order to achieve more accurate prediction, Shao and Nezu [\[24](#page-9-7)] applied different neural networks to different running stages of bearings. Gebraeel et al. [\[25\]](#page-9-8) proposed two classes of neural network models to perform the RUL prediction, and the result testified the advantages.

This paper proposes a hybrid method for RUL prediction utilizing the generalized Weibull failure rate function (WFRF) and radial basis function (RBF) neural network. The proposed method differs from other methods which have been used in past literature in adopting a novel indicator to capture the performance degradation of bearings. A new concept named sensitive frequency band (SFB) is defined and the power value on the SFB is selected as the degradation indicator. The SFB power value series along the lifetime is calculated and fitted by the generalized WFRF, then the fitted measurements are fed into RBF neural network. The remainder of this paper is organized as follows. [Section 2](#page-1-0) presents the different steps of the proposed method. In this section, the reason of degradation indicator selection is given and the basic principles of generalized WFRF and RBF neural network are detailed. Experimental setup is shown in [Section 3](#page-3-0) and the datasets used for validation are described. [Section 4](#page-4-0) is dedicated to evaluating the proposed method with the experimental data. Finally, some conclusions are drawn in [Section 5.](#page-7-0)

## <span id="page-1-0"></span>**2. Description of the Proposed Approach**

As mentioned above, it takes several steps to implement the proposed method. In this section, the procedure of the proposed method is discussed and the relevant theoretical bases are introduced in detail.

*2.1. Indicator Selection.* An appropriate indicator that can capture the evolution of the bearing's degradation is vital to perform RUL prediction [\[8](#page-8-7)]. A good indicator should be sensitive to initial degradation and be consistent with degradation process [\[30\]](#page-9-9). As a bearing fatigue occurs, a spall develops on the surface of the race and the defective frequency is excited. During the process of the bearing's degradation, the amplitude of this frequency is proportional to the spall size [\[31](#page-9-10)]. In other words, the amplitude of the defective frequency is the most intuitive and accurate reaction of the bearing's degradation process. In view of this, the average amplitude of the defective frequency and its first six harmonics is selected as indicator in [\[25](#page-9-8)] to predict the RUL of bearings. However, there exist several problems. Firstly, the diagnostics will be performed many times from beginning to initial failure occurrence, in order to identify the fault pattern and determine the defective frequency. It is meaningless and time-consuming when the bearing is normal for a long time. Secondly, it is not easy to calculate the defective frequency at the stage of incipient failure because of the heavy noise and the weak signature. Finally, there is always a frequency modulation phenomenon due to the bearing slackness [\[8](#page-8-7)], resulting in dramatic changes of amplitudes on modulated frequency band rather than defective frequency. To overcome these problems, the power value on the SFB is developed as a novel degradation indicator.

SFB is defined as a frequency band on which the FFT spectrums along the bearing degradation process are significantly different. It is an isolation of the frequencies associated with bearing defects from overall frequencies. As an example, [Figure 1](#page-2-0) presents a plot of FFT spectrums for a bearing at different stages of its life cycle. It is obvious that the amplitudes of frequency lines on [3000 Hz, 5000 Hz] increase more dramatically than other frequency bands with time until the bearing failure.

From the physical interpretation of the SFB power value we can see this indicator is robust to failure categories.

![](_page_2_Figure_2.jpeg)

<span id="page-2-0"></span>FIGURE 1: Evolution of the FFT spectrum.

Comparing with several statistical features usually adopted in previous studies, such as RMS and kurtosis, the SFB power value is superior. The disadvantage of the statistical features lies in that they depict vibration signals from overall range, which introduces insensitive factors to the degradation process.

In conclusion, the power value on the SFB is typically a good indicator which is used to predict the RUL of bearing in this work.

2.2. The Generalized Weibull Failure Rate Function. The generalized WFRF is derived from Weibull distribution and failure rate function. Weibull distribution is one of the most commonly used models in reliability assessment for a mechanical component. It is flexible to represent different life distributions with different parameters. Failure rate function is the measurement which indicates the failure probability of a certain unit at a given time [21]. Defined by three parameters, the WFRF is mathematically represented as [32]

$$z(t) = \frac{\beta}{\alpha} \left( \frac{t - \gamma}{\alpha} \right)^{\beta - 1}, \tag{1}$$

where z(t) is the failure rate of equipment at time t,  $\alpha$  is the scale parameter denoting characteristic life,  $\beta$  is the shape parameter representing Weibull slope, and  $\gamma$  is the position parameter. It is obvious in a degradation process that z(t) increases from 0 to 1 as time goes. Therefore,  $\beta$  is usually greater than 1 [33]. 2-parameter WFRF, which is widely used in bearing life prognosis, is derived by setting  $\gamma = 0$ .

The generalized WFRF is the updated version of WFRF. The equation of the generalized WFRF is as follows [21, 32].

$$\widehat{z}(t) = H + K \frac{\beta}{\alpha^{\beta}} t^{\beta - 1}, \tag{2}$$

where  $\hat{z}(t)$  is the fitted measurement value and t is the age of the equipment. H and K are introduced to adapt the equation to any situation.

2.3. Radial Basis Function Neural Network. RBF neural network as a feedforward network [34] is shown in Figure 2.

![](_page_2_Figure_13.jpeg)

<span id="page-2-1"></span>FIGURE 2: Structure of RBF neural network

It consists of three layers: an input layer with M neurons, a hidden layer with S neurons, and an output layer with N neurons. The input values are transferred from the input layer to the hidden layer. The basis functions in the hidden layer will give out a response to the inputs and generate the outputs in the neurons of the output layer. The response is nonzero only when the input falls within a limited region of the input space. Hence RBF neural network is also regarded as a local range network [35, 36].

The transfer function of the hidden layer is a Gaussian function. The output value of the sth neuron in the hidden layer is expressed as [34]

$$R_s(x) = \exp\left(-\frac{\|x - c_s\|^2}{2\sigma_s^2}\right), \quad s = 1, 2, \dots, S,$$
 (3)

where  $c_s$  and  $\sigma_s$  are the central and width parameters of the sth Gaussian function, respectively.

In RBF neural network, the hidden layer realizes the nonlinear mapping of  $x \to R(x)$  while the output layer realizes the linear mapping of  $R(x) \to y$ . The projection between input x and output y can be expressed as [37]

$$y_n = \sum_{s=1}^{S} \omega_{sn} R_s(x), \quad n = 1, 2, ..., N,$$
 (4)

where  $\omega_{sn}$  is the connection weight from hidden layer to output layer.

Although both RBF and BP neural networks can approximate any nonlinear function, RBF neural network has the advantage of a fast converging time without local minimum, since it only performs linear adjustment of the weights.

2.4. RUL Prediction Method. The framework of the proposed method is presented in Figure 3.

Firstly, SFB is determined by comparing FFT spectrums along the bearing degradation process. Secondly, the power value on the SFB is calculated for each FFT spectrum. As an example shown in Figure 4, although the trend of the power value is roughly increasing, there are large fluctuations

![](_page_3_Figure_2.jpeg)

<span id="page-3-1"></span>FIGURE 3: Procedure of the proposed method.

appearing especially after the occurrence of an initial defect. This may be because of the degradation mechanism that the spall is rounded after grinding for many times [10]. However, it is obvious that the health condition of a bearing deteriorating with time is a monotonic process [38]. For the sake of consistency with degradation process, the generalized WFRF is applied to fit the obtained power value series and four parameters of the generalized WFRF, namely, H, K,  $\alpha$ , and  $\beta$ , are derived.

Thereafter, RBF neural network is used as an intelligent system to predict the RUL of a bearing with the fitted measurements. In this case, four parameters including  $t_i$ ,  $t_{i-1}$ ,  $\widehat{z}_i$ , and  $\widehat{z}_{i-1}$  are selected as the inputs of the RBF neural network.  $t_i$  and  $t_{i-1}$  are the ages at current and previous inspections, respectively, while  $\widehat{z}_i$  and  $\widehat{z}_{i-1}$  are the fitted SFB power values at  $t_i$  and  $t_{i-1}$ . These four measurements are selected as inputs because they are crucial to represent the health condition of bearings. On the one hand, the fitted SFB power values at current and previous inspections can not only import the degradation status into RBF neural network but also introduce the change information of the measurements. On the other hand, we choose the fitted measurements at two inspections instead of more because it can give the ANN

![](_page_3_Figure_6.jpeg)

<span id="page-3-2"></span>FIGURE 4: The SFB power value series.

better generalization capability. As it comes to the output, the life percentage is preferred. The failure occurs when the life percentage reaches 100%. We denote the life percentage as  $p\ (0 \le p \le 1)$  at the time inspection of t. Then the RUL of the bearing  $\widetilde{t}$  is derived by

$$\widetilde{t} = \frac{t}{p} - t. \tag{5}$$

#### <span id="page-3-0"></span>3. Experimental Setup

The vibration signals used in this paper are provided by Center for Intelligent Maintenance Systems (IMS), University of Cincinnati [26]. Figure 5 presents the experimental setup of IMS.

As it is shown in Figure 5, four Rexnord ZA-2115 double row bearings were installed on the shaft which was driven by an AC motor via rub belts. The rotation speed of the shaft was kept constant at 2000 rpm. Through a spring mechanism, a radial load of 6000 lbs was exerted on the shaft and bearings. One PCB 353B33 High Sensitivity Quartz ICP accelerometer for each bearing was installed on the bearing housing to collect the vibration signal. With the sampling rate of 20 KHz, a set of data consisting of 20480 points was collected for one second every 10 minutes. Lubricant was driven by an oil circulation system to lubricate the test rig. The bearing degradation process was indicated by the debris adhered to a magnetic plug installed in the oil feedback pipe. The test would stop when the accumulated debris arrived to a preset amount. More detailed information about this experiment can be found in [39].

In this research, two vibration datasets are applied for the validation of the proposed RUL prediction method. Dataset 2 Bearing 1 of 984 vibration signals with an outer race failure is selected as an example to illustrate the proposed method in detail, while Dataset 1 Bearing 3 of 2156 vibration signals with an inner race defect is adopted to perform a comparative analysis. Figure 6 shows the failure bearing components after run-to-failure experiment [4].

![](_page_4_Picture_1.jpeg)

FIGURE 5: The experimental setup of IMS [26].

<span id="page-4-1"></span>![](_page_4_Picture_3.jpeg)

FIGURE 6: Photo of bearing components after experiment: (a) inner race defect in Dataset 1 Bearing 3 and (b) outer race defect in Dataset 2 Bearing 1 [4].

#### <span id="page-4-2"></span><span id="page-4-0"></span>4. Results and Discussion

The development of FFT spectrum for Dataset 2 Bearing 1 is shown in Figure 1. Intuitively, we can observe that the spectrum evolves gradually at the beginning and dramatically at the end. In order to identify the SFB mathematically,

we compute the accumulated amplitude difference of FFT spectrums on each frequency line as follows.

$$f_{\text{diff}}(q) = \sum_{i=2}^{L} |f_i(q) - f_{i-1}(q)|,$$
 (6)

3148, 2017, 1, Downloaded from https://olinelibtary.vielye.com/doi/10.1155/2017/892797 by Nat Prov Indonesia, Wiley Online Library on [11/10/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/rerms-and-conditions) on Wiley Online Library or rules of use; OA articles are governed by the applicable Creative Commons License

![](_page_5_Figure_2.jpeg)

![](_page_5_Figure_3.jpeg)

<span id="page-5-0"></span>Figure 7:  $f_{\text{diff}}(q)$  and H(j) of Dataset 2 Bearing 1.

where  $f_i(q)$  is the amplitude of the qth frequency line on the ith FFT spectrum and L is the number of FFT spectrums which is equal to 984. It is clear that  $f_{\rm diff}(q)$  can represent the variation of each frequency line throughout the lifetime. Based on  $f_{\rm diff}(q)$  we define an indicator H(j), which is

$$H(j) = \sum_{q=1}^{j} f_{\text{diff}}(q). \tag{7}$$

It is the summation of  $f_{\rm diff}(q)$ , which stands for the total difference from the 1st frequency line to the jth frequency line. If the differences of the corresponding frequency line amplitudes along with lifetime are small, the change of H(j) will be smooth. If such differences are large, the value of H(j) will increase rapidly. We would like to choose the frequency band as the SFB, on which the slope of H(j) is relatively larger.

In Figure 7,  $f_{\text{diff}}(q)$  and H(j) are depicted. It is easy to identify that the slope of H(j) is relatively larger from 3000 Hz to 5000 Hz. In other words, the amplitudes of frequency lines evolve dramatically on this frequency band. Hence the SFB in this case is selected as [3000 Hz, 5000 Hz].

It should be noted that the amplitudes on the SFB hardly appear to be different until the degradation process of bearing reaches to certain degree. For Dataset 2 Bearing 1, the amplitudes on [3000 Hz, 5000 Hz] do not increase abruptly until the life percentage comes to nearly 60%. Nevertheless, this matter does not become a barrier to the proposed prediction method. In comparison to the early stage of the bearing's lifetime, what counts more in the RUL prediction is the accurate prediction late in its life, because this directly affects whether and when to replace the bearing [21].

To depict the advantage of the proposed degradation indicator, we draw a comparison among the SFB power value and several most used features for diagnosis and prognosis of bearings defined, respectively, in Table 1.

In order to describe the signal from multiangles, the average amplitude of the defective frequency and its first six harmonics (AADFSH) is picked as the frequency domain feature [8, 25]. Furthermore, as it was proposed in [40],

<span id="page-5-1"></span>TABLE 1: Original time domain features.

| Feature   | Formula                                                                         |
|-----------|---------------------------------------------------------------------------------|
| RMS       | $\sqrt{\frac{1}{N}{\sum_{i=1}^{N}}{x_i}^2}$                                     |
| Kurtosis  | $\frac{1}{N} \sum_{i=1}^{N} \frac{\left(x_i - \overline{x}\right)^4}{\sigma^4}$ |
| Skewness  | $\frac{1}{N} \sum_{i=1}^{N} \frac{\left(x_i - \overline{x}\right)^3}{\sigma^3}$ |
| Peak-Peak | $\max(x_i) - \min(x_i)$                                                         |
| Variance  | $\frac{1}{N-1}\sum_{i=1}^{N}\left(x_{i}-\overline{x}\right)^{2}$                |

 $x_i$  is the vibration signal series;  $\overline{x}$  and  $\sigma$  are the mean value and the variance of the series, respectively.

the vibration signal was decomposed by empirical mode decomposition (EMD) and the first three intrinsic mode function (IMF) energy datasets were selected. Together with the five time domain features presented in Table 1, the original feature set was constructed. Then PCA was conducted and the first principal component was chosen as an ultimate indicator.

To evaluate the foregoing features and select the most sensitive indicator, three goodness metrics, namely, correlation (Corr), monotonicity (Mon), and robustness (Rob) are utilized [41]. Before then, each of the feature series is decomposed into two parts.

$$fea(t) = fea_T(t) + fea_R(t),$$
 (8)

where fea(t) is the degradation feature value at time t, fea<sub>T</sub>(t) is the trend value, and fea<sub>R</sub>(t) is the residual value.

The feature goodness metrics are computed by the following equations [32, 41–43]:

| Feature   | Corr   | Mon    | Rob    | Cri    | Time      |
|-----------|--------|--------|--------|--------|-----------|
| RMS       | 0.6287 | 0.0010 | 0.9849 | 0.5000 | 91.4562   |
| Kurtosis  | 0.4895 | 0.0051 | 0.9763 | 0.4963 | 93.2149   |
| Skewness  | 0.5202 | 0.0051 | 0.5195 | 0.2185 | 93.4770   |
| Peak-Peak | 0.5049 | 0.0132 | 0.9464 | 0.6382 | 91.5909   |
| Variance  | 0.3965 | 0.0010 | 0.9716 | 0.3654 | 91.7569   |
| AADFSH    | 0.2602 | 0.0051 | 0.6445 | 0.1579 | 92.7336   |
| PC1       | 0.5174 | 0.0031 | 0.7609 | 0.3348 | 2570.6297 |

0.9593

0.0275

<span id="page-6-3"></span>TABLE 2: Metrics comparison of features.

$$\operatorname{Corr} = \frac{\left|\sum_{t=1}^{L} \left(\operatorname{fea}(t) - \overline{\operatorname{fea}}\right) (t - \overline{t})\right|}{\sqrt{\sum_{t=1}^{L} \left(\operatorname{fea}(t) - \overline{\operatorname{fea}}\right)^{2} \sum_{t=1}^{L} (t - \overline{t})^{2}}},$$

$$\operatorname{Mon} = \left|\frac{\operatorname{number of positive}\left(\operatorname{diff}\left(\operatorname{fea}(t)\right)\right)}{L - 1}\right|$$

$$-\frac{\operatorname{number of negative}\left(\operatorname{diff}\left(\operatorname{fea}(t)\right)\right)}{L - 1}\right|,$$

$$\operatorname{Rob} = \frac{1}{L} \sum_{t=1}^{L} \exp\left(-\left|\frac{\operatorname{fea}_{T}(t)}{\operatorname{fea}(t)}\right|\right),$$

$$(9)$$

0.4888

SFB

where L = 984 denotes the number of observations during the lifetime,  $\overline{\text{fea}}$  and  $\overline{t}$  are the corresponding means of fea and t, and diff(fea(t)) is the difference between two successive points.

Corr is the measurement of linearity between feature and time. Mon evaluates the consistency of feature variation tendency and Rob reflects the tolerance of the feature to outliers. From the equations, we can see that all three goodness metrics are fallen into the range [0, 1] and are positively correlated with performance of features. In order to consider three metrics comprehensively, a weighted linear combination is proposed in [41] as the degradation indicator selection criteria:

$$Cri = \omega_1 Corr + \omega_2 Mon + \omega_3 Rob, \tag{10}$$

where  $\omega_1=0.2$ ,  $\omega_2=0.5$ , and  $\omega_3=0.3$  are the weights of the metrics, respectively, and determined by the contribution to the degradation process [41]. However, this fusion method by directly formulating on the metrics brings great distortion and thus leads to false selection of degradation indicator because the scales of these three metrics are not at the same level. See Figure 8. To eliminate this inequality, each of the metric dataset is normalized through  $\tilde{x}=(x-x_{\min})/(x_{\max}-x_{\min})$  before the criteria are computed.

The feature datasets obtained above are processed by (9)-(10), and the results of three metrics and criteria are tabulated in Table 2.

The characteristic frequency of outer race defect of Dataset 2 Bearing 1 used in AADFSH is determined in [44].

From Table 2, we can see the SFB power value has the largest Mon, which indicates that the tendency of this feature is closest to the degradation process. Moreover, the

<span id="page-6-1"></span>![](_page_6_Figure_12.jpeg)

0.9076

93.7524

<span id="page-6-0"></span>FIGURE 8: Goodness metrics of 8 features.

<span id="page-6-4"></span>TABLE 3: Estimated generalized WFRF parameters.

|           | Н      | K         | α   | β     |
|-----------|--------|-----------|-----|-------|
| SFB power | 0.0083 | 1.32e - 9 | 220 | 16.09 |

<span id="page-6-2"></span>computing time of each feature dataset is also obtained. In this paper, a computer equipped with an Intel® Xeon<sup>R</sup> E5-1620 processor CPU @ 3.60 GHz, 16 Gb RAM, and the 64-bit Windows 7 operating system (OS) was utilized. The feature PC1 took considerably more time than other features because EMD was conducted 984 times which required high computing burdens. This makes PC1 unsuitable for online prognostics. With the largest Cri and relatively less running time, the SFB power value is the most sensitive feature and selected as degradation indicator in this paper.

Figure 4 presents the SFB power value series of Dataset 2 Bearing 1, in which 1 data point denotes 10 minutes and this stipulation is valid throughout this paper. The generalized WFRF is adopted to fit the measurement line. Table 3 shows the results of the estimated parameters computed by nonlinear least squares method. To evaluate the fitting performance, Figure 9 shows the actual SFB power value series and the fitted series. It is obvious that the fitted series gives a better indication of the bearing degradation.

![](_page_7_Figure_2.jpeg)

<span id="page-7-1"></span>FIGURE 9: SFB power value series and fitted series.

According to the vibration signals of Dataset 2 Bearing 1, there are 984 inspections throughout the lifetime. Due to two fitted measurements at current and previous inspections combining as one input of RBF neural network, 983 pairs of data are obtained. In order to verify the effectiveness of the proposed method, we segment these 983 datasets into two categories: a training set and a test set. 500 pairs of data are chosen randomly from 983 pairs as training set and 100 pairs are selected arbitrarily from the remaining 483 pairs as test set. Then RBF neural network is trained utilizing the training set. During the training process, the inherent configure of the RBF neural network is adjusted to minimize the mean square error (MSE) between the network outputs and the actual life percentages.

MSE = 
$$\frac{1}{W} \sum_{i=1}^{W} (LP_P - LP_A)^2$$
, (11)

where W is the number of data,  $LP_P$  is the network output, and  $LP_A$  is the actual life percentage.

As the training process completed, the test set is fed into the trained network to testify its performance. The training and test performance is illustrated in Figures 10(a) and 10(b). The actual life percentage values are represented by "+", and the predicted life percentage values are denoted by "blue circle". The MSE for the test set in this paper is 2.45e – 15, which is smaller than both training and validation MSE in [7]. From Figure 10, we can see that the actual percentage values and the predicted values coincide almost at each selected data point, which indicates the good performance of the RBF neural network.

The proposed method has been compared with other methods in previous research. The performance of prediction can be simply calculated as

Accuracy = 
$$\left(1 - \frac{|ActRUL - PreRUL|}{ActRUL}\right) \times 100\%$$
, (12)

<span id="page-7-2"></span>Table 4: Comparison between the current work and published work.

| References | Data      | Reference       | Proposed |
|------------|-----------|-----------------|----------|
|            |           | accuracy        | accuracy |
| [27]       | Dataset 2 | 95.9%           | 99.28%   |
|            | Bearing 1 | 93.970          | 99.2070  |
| [28]       | Dataset 1 | 98.47%          | 99.42%   |
|            | Bearing 3 | 90.47 70        | 99.4270  |
| [29]       | Dataset 1 | 99.02%          | 99.28%   |
|            | Bearing 3 | 99 <b>.</b> UZ% | 77.20%   |

where ActRUL is the actual RUL and PreRUL is the predicted RUL.

Adopting the same run-to-failure datasets collected from IMS, the results are shown in Table 4. In order to compare the performance fairly, the same failure threshold is utilized in the corresponding reference.

It is clear that the accuracy of the proposed method is higher, which indicates a good performance of this method in predicting the RUL of bearings.

#### <span id="page-7-0"></span>5. Conclusion

Accurate RUL prediction of bearing is crucial to perform PHM of rotating machinery for preventing fatal failure and reducing maintenance cost. Most literature concentrating on RUL prediction mainly adopts two steps: indicator selection and life prediction model construction. This paper proposes a novel degradation indicator, namely, the SFB power value; it is the direct reflection of bearing health condition. The advantage of this indicator is verified by comparing with several commonly used features. Subsequently, the SFB power value series along the lifetime is fitted with the generalized WFRF to keep consistent with the degradation process. RBF neural network is utilized to perform bearing RUL prediction with the ages and the fitted power values at present and previous inspections as inputs and the life percentage as output.

In the experimental verification, three prognostic methods were compared with the proposed method. The results showed that the proposed method provided a more accurate prediction, which demonstrated the effectiveness and superiority of this method in predicting the RUL of bearings. Moreover, the proposed method is suitable for practical application and industrial field, because the novel indicator in this paper is easy to obtain and robust to fault categories.

#### **Conflicts of Interest**

The authors declare that there are no conflicts of interest regarding the publication of this paper.

### Acknowledgments

This work is supported by National Key R&D Program of China (2016YFC0802908), National Natural Science Foundation of China (no. 51475455), and the Project Funded by the

<span id="page-8-16"></span>![](_page_8_Figure_2.jpeg)

<span id="page-8-18"></span>Figure 10: Performance of (a) training and (b) test.

Priority Academic Program Development of Jiangsu Higher Education Institutions (PAPD).

## **References**

- <span id="page-8-0"></span>[1] A. Heng, S. Zhang, A. C. C. Tan, and J. Mathew, "Rotating machinery prognostics: state of the art, challenges and opportunities," *Mechanical Systems and Signal Processing*, vol. 23, no. 3, pp. 724–739, 2009.
- <span id="page-8-1"></span>[2] J. Lee, F. Wu, W. Zhao, M. Ghaffari, L. Liao, and D. Siegel, "Prognostics and health management design for rotary machinery systems—reviews, methodology and applications," *Mechanical Systems and Signal Processing*, vol. 42, no. 1-2, pp. 314–334, 2014.
- <span id="page-8-2"></span>[3] T. Benkedjouh, K. Medjaher, N. Zerhouni, and S. Rechak, "Remaining useful life estimation based on nonlinear feature reduction and support vector regression," *Engineering Applications of Artificial Intelligence*, vol. 26, no. 7, pp. 1751–1760, 2013.
- <span id="page-8-3"></span>[4] H. Qiu, J. Lee, J. Lin, and G. Yu, "Robust performance degradation assessment methods for enhanced rolling element bearing prognostics," *Advanced Engineering Informatics*, vol. 17, no. 3-4, pp. 127–140, 2003.
- <span id="page-8-4"></span>[5] X.-S. Si, W. Wang, M.-Y. Chen, C.-H. Hu, and D.-H. Zhou, "A degradation path-dependent approach for remaining useful life estimation with an exact and closed-form solution," *European Journal of Operational Research*, vol. 226, no. 1, pp. 53–66, 2013.
- <span id="page-8-5"></span>[6] H. T. Pham, V. T. Tran, and B.-S. Yang, "A hybrid of nonlinear autoregressive model with exogenous input and autoregressive moving average model for long-term machine state forecasting," *Expert Systems with Applications*, vol. 37, no. 4, pp. 3310–3317, 2010.
- <span id="page-8-6"></span>[7] A. K. Mahamad, S. Saon, and T. Hiyama, "Predicting remaining useful life of rotating machinery based artificial neural network," *Computers and Mathematics with Applications*, vol. 60, no. 4, pp. 1078–1087, 2010.

- <span id="page-8-17"></span><span id="page-8-7"></span>[8] R. Huang, L. Xi, X. Li, C. Richard Liu, H. Qiu, and J. Lee, "Residual life predictions for ball bearings based on selforganizing map and back propagation neural network methods," *Mechanical Systems and Signal Processing*, vol. 21, no. 1, pp. 193–207, 2007.
- <span id="page-8-8"></span>[9] H. Ocak, K. A. Loparo, and F. M. Discenzo, "Online tracking of bearing wear using wavelet packet decomposition and probabilistic modeling: a method for bearing prognostics," *Journal of Sound and Vibration*, vol. 302, no. 4-5, pp. 951–961, 2007.
- <span id="page-8-9"></span>[10] Y. N. Pan, J. Chen, and L. Guo, "Robust bearing performance degradation assessment method based on improved wavelet packet-support vector data description," *Mechanical Systems and Signal Processing*, vol. 23, no. 3, pp. 669–681, 2009.
- <span id="page-8-10"></span>[11] Z. Zhang, Y. Wang, and K. Wang, "Fault diagnosis and prognosis using wavelet packet decomposition, Fourier transform and artificial neural network," *Journal of Intelligent Manufacturing*, vol. 24, no. 6, pp. 1213–1227, 2013.
- <span id="page-8-11"></span>[12] L. Liao and J. Lee, "A novel method for machine performance degradation assessment based on fixed cycle features test," *Journal of Sound and Vibration*, vol. 326, no. 3-5, pp. 894–908, 2009.
- <span id="page-8-12"></span>[13] C. Lu, J. Chen, R. Hong, Y. Feng, and Y. Li, "Degradation trend estimation of slewing bearing based on LSSVM model," *Mechanical Systems and Signal Processing*, vol. 76-77, pp. 353– 366, 2016.
- <span id="page-8-13"></span>[14] Y. Liu and S. Mahadevan, "Probabilistic fatigue life prediction using an equivalent initial flaw size distribution," *International Journal of Fatigue*, vol. 31, no. 3, pp. 476–487, 2009.
- <span id="page-8-14"></span>[15] D. Xu, J. Huang, Q. Zhu, X. Chen, Y. Xu, and S. Wang, "Residual fatigue life prediction of ball bearings based on Paris law and RMS," *Chinese Journal of Mechanical Engineering*, vol. 25, no. 2, pp. 320–327, 2012.
- <span id="page-8-15"></span>[16] G. Jin, D. Matthews, Y. Fan, and Q. Liu, "Physics of failure-based degradation modeling and lifetime prediction of the momentum wheel in a dynamic covariate environment," *Engineering Failure Analysis*, vol. 28, pp. 222–240, 2013.

<span id="page-9-0"></span>[17] J. Yan and J. Lee, "Degradation assessment and fault modes classification using logistic regression," *Journal of Manufacturing Science and Engineering*, vol. 127, no. 4, pp. 912–914, 2005.

- <span id="page-9-1"></span>[18] H. T. Pham and B.-S. Yang, "Estimation and forecasting of machine health condition using ARMA/GARCH model," *Mechanical Systems and Signal Processing*, vol. 24, no. 2, pp. 546– 558, 2010.
- <span id="page-9-2"></span>[19] S.-W. Fei and Y. He, "A multiple-kernel relevance vector machine with nonlinear decreasing inertia weight pso for state prediction of bearing," *Shock and Vibration*, vol. 2015, Article ID 685979, 6 pages, 2015.
- <span id="page-9-3"></span>[20] S. Dong, S. Yin, B. Tang, L. Chen, and T. Luo, "Bearing degradation process prediction based on the support vector machine and Markov model," *Shock and Vibration*, vol. 2014, Article ID 717465, 15 pages, 2014.
- <span id="page-9-4"></span>[21] Z. Tian, "An artificial neural network method for remaining useful life prediction of equipment subject to condition monitoring," *Journal of Intelligent Manufacturing*, vol. 23, no. 2, pp. 227–237, 2012.
- <span id="page-9-5"></span>[22] S.-J. Wu, N. Gebraeel, M. A. Lawley, and Y. Yih, "A neural network integrated decision support system for condition-based optimal predictive maintenance policy," *IEEE Transactions on Systems, Man, and Cybernetics - Part A: Systems and Humans*, vol. 37, no. 2, pp. 226–236, 2007.
- <span id="page-9-6"></span>[23] J. Lee, J. Ni, D. Djurdjanovic, H. Qiu, and H. Liao, "Intelligent prognostics tools and e-maintenance," *Computers in Industry*, vol. 57, no. 6, pp. 476–489, 2006.
- <span id="page-9-7"></span>[24] Y. Shao and K. Nezu, "Prognosis of remaining bearing life using neural networks," *Proceedings of the Institution of Mechanical Engineers, Part I: Journal of Systems and Control Engineering*, vol. 214, no. 3, pp. 217–230, 2000.
- <span id="page-9-8"></span>[25] N. Gebraeel, M. Lawley, R. Liu, and V. Parmeshwaran, "Residual life predictions from vibration-based degradation signals: a neural network approach," *IEEE Transactions on Industrial Electronics*, vol. 51, no. 3, pp. 694–700, 2004.
- <span id="page-9-18"></span>[26] J. Lee, H. Qiu, G. Yu, and J. Lin, "Rexnord Technical Services, "Bearing Data Set", IMS, University of Cincinnati. NASA Ames Prognostics Data Repository," NASA Ames, Moffett Field, CA, [http://ti.arc.nasa.gov/tech/dash/pcoe/prognostic-data-reposi](http://ti.arc.nasa.gov/tech/dash/pcoe/prognostic-data-repository/)[tory/.](http://ti.arc.nasa.gov/tech/dash/pcoe/prognostic-data-repository/)
- <span id="page-9-24"></span>[27] A. Widodo and B.-S. Yang, "Application of relevance vector machine and survival probability to machine degradation assessment," *Expert Systems with Applications*, vol. 38, no. 3, pp. 2592–2599, 2011.
- <span id="page-9-25"></span>[28] S. Hong and Z. Zhou, "Remaining useful life prognosis of bearing based on Gauss process regression," in *Proceedings of the 5th International Conference on Biomedical Engineering and Informatics, (BMEI)*, pp. 1575–1579, October 2012.
- <span id="page-9-26"></span>[29] W. Caesarendra, A. Widodo, and B.-S. Yang, "Combination of probability approach and support vector machine towards machine health prognostics," *Probabilistic Engineering Mechanics*, vol. 26, no. 2, pp. 165–173, 2011.
- <span id="page-9-9"></span>[30] Y. Pan, J. Chen, and X. Li, "Bearing performance degradation assessment based on lifting wavelet packet decomposition and fuzzy c-means," *Mechanical Systems and Signal Processing*, vol. 24, no. 2, pp. 559–566, 2010.
- <span id="page-9-10"></span>[31] P. E. William and M. W. Hoffman, "Identification of bearing faults using time domain zero-crossings," *Mechanical Systems and Signal Processing*, vol. 25, no. 8, pp. 3078–3088, 2011.
- <span id="page-9-11"></span>[32] J. Ben Ali, B. Chebel-Morello, L. Saidi, S. Malinowski, and F. Fnaiech, "Accurate bearing remaining useful life prediction

- based on Weibull distribution and artificial neural network," *Mechanical Systems and Signal Processing*, vol. 56, pp. 150–172, 2015.
- <span id="page-9-12"></span>[33] Y. Feng, X.-D. Huang, R.-J. Hong, and J. Chen, "Online residual useful life prediction of large-size slewing bearings—A data fusion method," *Journal of Central South University*, vol. 24, no. 1, pp. 114–126, 2017.
- <span id="page-9-13"></span>[34] M. Asadizadeh and M. F. Hossaini, "Predicting rock mass deformation modulus by artificial intelligence approach based on dilatometer tests," *Arabian Journal of Geosciences*, vol. 9, no. 2, article no. 96, 15 pages, 2016.
- <span id="page-9-14"></span>[35] W. X. Lai, P. W. Tse, G. C. Zhang, and T. L. Shi, "Classification of gear faults using cumulants and the radial basis function network," *Mechanical Systems and Signal Processing*, vol. 18, no. 2, pp. 381–389, 2004.
- <span id="page-9-15"></span>[36] Y. Tasdemir, E. Kolay, and K. Kayabali, "Comparison of three artificial neural network approaches for estimating of slake durability index," *Environmental Earth Sciences*, vol. 68, no. 1, pp. 23–31, 2013.
- <span id="page-9-16"></span>[37] M. Kalkat, "Investigations on the effect of oil quality on gearboxes using neural network predictors," *Industrial Lubrication and Tribology*, vol. 67, no. 2, pp. 99–109, 2015.
- <span id="page-9-17"></span>[38] Z. G. Tian, L. N. Wong, and N. M. Safaei, "A neural network approach for remaining useful life prediction utilizing both failure and suspension histories," *Mechanical Systems and Signal Processing*, vol. 24, no. 5, pp. 1542–1555, 2010.
- <span id="page-9-19"></span>[39] H. Qiu, J. Lee, J. Lin, and G. Yu, "Wavelet filter-based weak signature detection method and its application on rolling element bearing prognostics," *Journal of Sound and Vibration*, vol. 289, no. 4-5, pp. 1066–1090, 2006.
- <span id="page-9-20"></span>[40] L. Mi, W. Tan, and R. Chen, "Multi-steps degradation process prediction for bearing based on improved back propagation neural network," *Proceedings of the Institution of Mechanical Engineers, Part C: Journal of Mechanical Engineering Science*, vol. 227, no. 7, pp. 1544–1553, 2013.
- <span id="page-9-21"></span>[41] B. Zhang, L. Zhang, and J. Xu, "Degradation feature selection for remaining useful life prediction of rolling element bearings," *Quality and Reliability Engineering International*, vol. 32, no. 2, pp. 547–554, 2016.
- [42] L. Guo, N. Li, F. Jia, Y. Lei, and J. Lin, "A recurrent neural network based health indicator for remaining useful life prediction of bearings," *Neurocomputing*, vol. 240, pp. 98–109, 2017.
- <span id="page-9-22"></span>[43] W. He, Q. Miao, M. Azarian, and M. Pecht, "Health monitoring of cooling fan bearings based on wavelet filter," *Mechanical Systems and Signal Processing*, vol. 64-65, pp. 149–161, 2015.
- <span id="page-9-23"></span>[44] C. Zhang, B. Li, B. Chen, H. Cao, Y. Zi, and Z. He, "Weak fault signature extraction of rotating machinery using flexible analytic wavelet transform," *Mechanical Systems and Signal Processing*, vol. 64-65, pp. 162–187, 2015.
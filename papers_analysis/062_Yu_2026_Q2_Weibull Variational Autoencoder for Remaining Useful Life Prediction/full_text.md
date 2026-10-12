![](_page_0_Picture_1.jpeg)

![](_page_0_Picture_2.jpeg)

![](_page_0_Picture_3.jpeg)

## **Weibull Variational Autoencoder for Remaining Useful Life Prediction**

JunWoo Yu Yoojin Jang Kwanghui Shin Jinsoo Jeong Yong Soo Kim

Department of Industrial and System Engineering, Kyonggi University Suwon, Suwon-si, Gyeonggi-do, South Korea

**Correspondence:** Yong Soo Kim [\(kimys@kyonggi.ac.kr\)](mailto:kimys@kyonggi.ac.kr)

**Received:** 9 April 2026 **Revised:** 22 August 2026 **Accepted:** 2 September 2026

**Keywords:** prognostics and health management (PHM) | remaining useful life (RUL) | uncertainty quantification | variational autoencoder (VAE) | weibull distribution | weibull variational autoencoder (WVAE)

## **ABSTRACT**

Remaining useful life (RUL) prediction is a critical technology for preventing unexpected failures and reducing maintenance costs in modern industrial systems. However, traditional model-based approaches are limited by the need for explicit mathematical modeling of degradation mechanisms, while data-driven methods often require large-scale datasets and lack interpretability. To address these challenges, this study proposes a Weibull Variational Autoencoder (WVAE). The WVAE is designed to learn probabilistic characteristics grounded in the Weibull distribution from failure history data and predict failure times accordingly. A composite loss function combining mean squared error (MSE) with negative log-likelihood is employed to jointly ensure predictive accuracy and distributional fidelity, while Monte Carlo Dropout–based inference is used to quantify uncertainty and provide confidence intervals. Simulated datasets incorporating three types of failures, including infant mortality, random, and wear-out failures, as well as multiple levels of noise, were constructed to reflect diverse system characteristics and industrial conditions. Evaluation results demonstrate that, compared with several benchmarking models, the WVAE produces predictions statistically consistent with historical failure distributions while maintaining stable forecasting performance. Furthermore, by directly estimating the parameters of the Weibull distribution, the WVAE provides statistically interpretable predictions that can be trusted by domain experts. The model is further validated on the Backblaze hard drive field-reliability dataset, confirming its applicability to real-world failure data with diverse distributional characteristics.

## **1 Introduction**

Remaining useful life (RUL) represents how long a mechanical system can continue to be used from a certain point in time [\[1\]](#page-19-0). RUL prediction is a critical task in Prognostics and Health Management (PHM) of mechanical systems [\[2\]](#page-19-0). This is because accurate RUL prediction can greatly contribute to preventing unexpected equipment failures in advance, thereby reducing production downtime costs and maintenance costs [\[3–5\]](#page-19-0).

Approaches to achieve this are divided into two categories: model-based and data-driven [\[6\]](#page-19-0). Model-based methods are based on domain knowledge and experience about the physical characteristics and failure mechanisms of the system [\[7\]](#page-19-0), and require that the system's degradation and failure processes be expressed as a mathematical model[\[8\]](#page-19-0).In particular, probabilistic lifetime models assume probability distributions such as the Weibull distribution [\[9\]](#page-19-0), exponential distribution [\[10\]](#page-19-0), and lognormal distribution [\[11\]](#page-19-0) to predict the system'sfailure time. These models mainly estimate parameters based on historical failure data of equipment, and the estimated model is then used to predict future failure probability and RUL. Qin et al.[\[12\]](#page-19-0) proposed a Weibull-based reliability model for k-out-of-n load-sharing systems, which characterizes the lifetime of each component and

This is an open access article under the terms of the Creative Commons [Attribution-NonCommercial-NoDerivs](http://creativecommons.org/licenses/by-nc-nd/4.0/) License, which permits use and distribution in any medium, provided the original work is properly cited, the use is non-commercial and no modifications or adaptations are made. © 2026 The Author(s). *Quality and Reliability Engineering International* published by John Wiley & Sons Ltd.

predicts failure probability and RUL using maximum likelihood estimation. Dong et al. [\[13\]](#page-19-0) proposed an approach using a Weibull distribution-based model to predict the failure probability and reliability of powersystem assets, thereby improving the accuracy of reliability evaluation of complex systems. However, with the rapid advancement of industry, mechanical systems have become increasingly complex, making it difficult both to fully understand specific failure modes and phenomena and to model them in detail [\[14\]](#page-19-0). Moreover, since operating mechanisms differ from system to system, model-based methods have limitations in terms of flexibility and generality [\[15\]](#page-19-0). In contrast, data-driven methods employ machine learning and deep learning techniques to capture failure patterns and to predict the RUL using sensor data [\[16\]](#page-19-0) and operational data collected from the system [\[17\]](#page-19-0). This approach can be utilized even when it is difficult to clearly understand the physical mechanisms [\[18\]](#page-19-0) and when information on the direct degradation of machinery is insufficient [\[19\]](#page-19-0). Loutas et al.[\[20\]](#page-19-0) proposed a data-driven approach that estimatestheRUL of rolling bearings based on support vector regression (SVR).

Sun et al. [\[21\]](#page-19-0) proposed an approach for RUL prediction of cutting tools. In this method, vibration signals collected via accelerometers are analyzed using deep transfer learning (DTL) with a sparse autoencoder(SAE). However, data-driven methodsrequire a large amount of data [\[22,](#page-19-0) 23], and their prediction performance varies greatly depending on the quality and characteristics of the collected data. In particular, data-driven approaches lack interpretability of the prediction models [\[24\]](#page-19-0), which poses a problem that makes it difficult for maintenance personnel to understand and trust the model's prediction results.

To overcome these limitations, this study proposes a Weibull variational autoencoder(WVAE)that integratesthe advantages of both model-based and data-driven methods. The proposed model is designed to take equipment failure history data as input and to provide a probabilistic prediction of the failure time by learning the shape and scale parameters of the Weibull distribution in the latent space. The primary contributions of this paper are as follows.

- 1. The proposed model learns the characteristics of the data based on failure history without defining complex degradation mechanisms by equations. Accordingly, it can be easily applied to a variety of product types and operating scenarios, thereby effectively overcoming the limitations of conventional model-based approaches such as limited flexibility and applicability.
- 2. Experimental results on datasets with various levels of white noise showed that the proposed model captured failure patterns more precisely and exhibited robust predictive performance against noise, compared to conventional deep learning-based prediction models. These results confirmed the applicability of the proposed model even in situations of data quality degradation that frequently occur in real-world environments.
- 3. The proposed method offers higher interpretability than conventional deep learning methods by explicitly incorporating physically interpretable Weibull distribution parameters into its latent variables. This approach provides maintenance

personnel with a basis to better understand and trust the prediction results.

The structure of this paper is as follows. Section 2 provides a review of prior research on RUL prediction, categorized into model-based and data-driven approaches. Section [3](#page-2-0) presents the proposed methodology in detail, together with the baseline models on which it is built. Section [4](#page-7-0) presentsthe experimentalresults and performance evaluation based on simulation data containing various levels of white noise, and verifies the performance of the proposed method through comparison with benchmark models. Section [5](#page-15-0) validatesthe proposed method on the Backblaze dataset. Finally, Section [6](#page-18-0) discusses the conclusion and future research directions.

### **2 Related Works**

RUL prediction methods are largely divided into model-based approaches and data-driven approaches. In model-based approaches, there exist physical degradation models and probabilistic reliability models [\[25\]](#page-19-0). Liao [\[26\]](#page-19-0) proposed an RUL prediction method using a proportional hazards model and a logistic regression model, and compared the two models using bearing test data. You et al. [\[27\]](#page-19-0) proposed a two-segment Cox regression model for equipment RUL prediction. Lei et al. [\[5\]](#page-19-0) predicted the RUL of machinery by combining the health indicator weighted minimum quantization error(WMQE), which captures inter-feature mutual information, with a maximum likelihood estimation and particle filter-based algorithm, and validated its effectiveness using bearing degradation test data. Data-driven approaches are subdivided into two categories according to the depth of the neural network structure: shallow learning methods and deep learning methods with complex architectures. As an example of shallow learning methods, Malik et al. [\[28\]](#page-19-0) predicted the RUL of aircraft engine batteries by applying SVR based on NASA CMAPSS data. Alfarizi et al. [\[29\]](#page-19-0) predicted bearing life for RUL estimation by extracting features from vibration signals through empirical mode decomposition (EMD) and employing a random forest regression model whose hyperparameters were tuned using Bayesian optimization. Jin et al. [\[30\]](#page-20-0) proposed a deep learning model that combines dynamic time series attention with a channel–time series mixed multilayer perceptron (MLP), and demonstrated superior RUL prediction performance compared to existing state-of-the-art techniques through experiments on a bearing dataset. Pandit et al. [\[31\]](#page-20-0) proposed a model that combines SVM, random forest, and Gaussian process regression with the sparrow search algorithm (SSA) for RUL prediction of wind turbine bearings, and verified its performance using real 2 MW wind turbine data. Such shallow learning-based RUL prediction generally requires manual feature extraction that relies on domain knowledge. In contrast, deep learning-based approaches can simultaneously perform feature extraction and prediction, automatically learn important patterns from raw data, and demonstrate high generalization performance [\[25\]](#page-19-0). These characteristics contribute to improving the accuracy and applicability of RUL prediction, and recently, deep learning-based approaches have been actively studied in the field of RUL prediction. Babu et al. [\[32\]](#page-20-0) proposed a convolutional neural network (CNN)-based model for RUL prediction and demonstrated superior predictive <span id="page-2-0"></span>performance compared to conventional shallow learning-based algorithms through experiments on two datasets. Ahmed et al. [33] employed various deep learning-based models, including CNN, long short-term memory (LSTM), and CNN-LSTM, for PHM of manufacturing systems, and showed that they outperform shallow models such as SVM and random forest, thereby demonstrating the effectiveness of deep learning. Malhi et al. [34] proposed a prediction model based on recurrent neural network (RNN) and real-time recurrent learning (RTRL) for predicting defect progression in roller bearings, and improved long-term prediction performance through a training technique combined with competitive learning. Zhang et al. [35] proposed a bidirectional LSTM-based model for RUL prediction, effectively learning long-term dependencies using time series sensor data. However, such deep learning-based time series prediction models are sensitive to noise and tend to replicate the last value of the input time series, producing outputs that are closer to simple repetition than to actual prediction [36]. This can be interpreted as improved performance from the perspective of RMSE, but in real operating environments, it may lead to inaccurate predictions and consequently reduce reliability.

In addition, most RNN-based prediction models follow the iterated multi-step (IMS) structure of multi-stage prediction, which operates by repeatedly using the prediction values from previous steps as the input for the next step [37]. However, this prediction procedure causes prediction errors to accumulate during the iterative process, leading to a rapid decrease in prediction accuracy. The direct multi-step (DMS) approach, which generates all values of the prediction horizon at once, has been regarded as an alternative since it can effectively mitigate the error accumulation problem of IMS [38]. Recently, approaches based on the variational autoencoder (VAE) have been actively studied, in which the entire input time series is encoded into a compressed latent space and the values of the entire prediction horizon are generated collectively. Remadna et al. [39] proposed a new hybrid deep learning architecture for RUL prediction of aircraft engines by combining an attention convolutional variational autoencoder (ACVAE) with an ensemble learning classifier. Su et al. [14] predicted RUL using a hybrid deep learning model that combines a VAE and a timewindow-based sequence neural network (twSNN) for aircraft turbine engine data. However, conventional VAE models have the limitation of not being able to sufficiently capture the characteristics of complex failure patterns because they assume the latent space to follow a normal distribution. To address this issue, this study assumes the latent space of the conventional VAE structure to follow a Weibull distribution, thereby aiming to more accurately capture actual failure patterns and enhance reliability-based RUL prediction performance. The representative methods addressed in this paper are systematically compared in Table 1.

#### 3 | Methodology

In this section, an overview of the proposed WVAE model is first introduced, followed by detailed explanations of the main components, including the model architecture, loss function, data composition, and uncertainty quantification method. The overall process is presented in Figure 1.

#### 3.1 | Variational Autoencoder

The VAE is designed as a generative model that captures the probability distribution of input data within a latent space, enabling the representation of high-dimensional data by low-dimensional latent variables [39]. A VAE generally includes two modules, the encoder and the decoder. The encoder converts input data into a probabilistic latent representation, and the decoder reconstructs the data from that representation [40]. The VAE regards the direct maximum likelihood estimation of the data distribution as a difficult problem and introduces latent variables to maximize the marginal likelihood as follows:

$$\log p(x) = \log \int p_{\theta}(x|z) p(z) dz$$
 (1)

However, since the above integral calculation is difficult, variational inference introduces an approximate distribution  $q_{\phi}(z|x)$  for p(z|x). Through this, the evidence lower bound (ELBO) for  $\log p(x)$  is derived, and the model is trained by maximizing the ELBO. The ELBO is defined as follows:

ELBO = 
$$E_{q\phi}(z|x) [\log p_{\theta}(x|z)]$$
  
-  $D_{KL}(q_{\theta}(z|x) \parallel p(z))$  (2)

In summary, the ELBO of the VAE is expressed as follows:

$$\log p(x) \ge \mathrm{E}_{q\phi}(z|x) [\log p_{\theta}(x|z)] - \mathrm{D}_{\mathrm{KL}} (q_{\theta}(z|x) \parallel p(z))$$
(3)

Here, the first term is the reconstruction loss, which encourages the reconstructed data from the latent variable z to be similar to the actual input x. The second term is the Kullback–Leibler divergence (KL divergence) between  $q_{\phi}(z|x)$  and the prior distribution p(z), which serves to regularize the latent variable distribution so that it follows the assumed prior distribution. The KL divergence quantifies the discrepancy between two probability distributions, P and Q, and can be expressed as:

$$D_{KL}(P \parallel Q) = E_{x \sim P} \left[ \log \left( \frac{P(x)}{Q(x)} \right) \right]$$
 (4)

when applied to the conditional distribution, it is expressed as follows:

$$\mathrm{D_{KL}}\left(q_{\phi}\left(z|x\right)\parallel p\left(z\right)\right)=\mathrm{E}_{q_{\phi}\left(z|x\right)}\left[\log q_{\phi}\left(z|x\right)\right]-\mathrm{E}_{q_{\phi}\left(z|x\right)}\left[\log p\left(z\right)\right]\tag{5}$$

That is, the KL divergence is the expected value of the log ratio between the approximate posterior distribution  $q_{\emptyset}(z|x)$  and the prior distribution p(z), and it becomes 0 when the two distributions are identical. In general, the VAE assumes the prior distribution p(z) to be a normal distribution  $\mathcal{N}(0, 1)$  with mean 0 and variance 1, while the distribution  $q_{\emptyset}(z|x)$  output by the encoder is modeled as a normal distribution with mean  $\mu$  and variance  $\sigma$ , as follows:

$$q_{\phi}(z|x) = N(z; \mu(x), \operatorname{diag}(\sigma^{2}(x)))$$
 (6)

To ensure differentiability during the training process, the VAE employs the reparameterization trick. That is, the latent variable

<span id="page-3-0"></span>**TABLE 1** Comparison of the methods discussed in this study.

| Method                        | Related<br>publications | Model<br>driven | Data-driven | Deep learning | DMS |
|-------------------------------|-------------------------|-----------------|-------------|---------------|-----|
| Log-normal distribution       | [11]                    | Yes             | No          | No            | No  |
| Weibull distribution          | [12, 13]                | Yes             | No          | No            | No  |
| SVR                           | [20, 28]                | No              | Yes         | No            | No  |
| SAE                           | [21]                    | No              | Yes         | Yes           | Yes |
| Logistic regression model     | [26]                    | No              | Yes         | No            | No  |
| Cox regression                | [27]                    | Yes             | No          | No            | No  |
| Maximum Likelihood Estimation | [5]                     | Yes             | No          | No            | No  |
| Random Forest                 | [29, 31]                | No              | Yes         | No            | No  |
| MLP                           | [30]                    | No              | Yes         | No            | No  |
| 1D-CNN                        | [32, 33]                | No              | Yes         | Yes           | No  |
| CNN-LSTM                      | [33]                    | No              | Yes         | Yes           | No  |
| RNN                           | [34]                    | No              | Yes         | Yes           | No  |
| LSTM                          | [35]                    | No              | Yes         | Yes           | No  |
| VAE                           | [14]                    | No              | Yes         | Yes           | Yes |

![](_page_3_Figure_3.jpeg)

**FIGURE 1** Overall framework of the proposed approach.

is expressed as follows:

$$z = \mu(x) + \sigma(x) \odot \varepsilon, \ \varepsilon \sim N(0, 1) \tag{7}$$

By separating the sampling in this way, differentiation in the stochastic sampling process becomes possible, enabling efficient learning through backpropagation. Finally, within the VAE framework, the loss function is formulated as the negative ELBO, comprising the reconstruction loss and the KL divergence, as follows:

$$L (\theta, \phi; x) = -\mathbb{E}_{q_{\phi}(z|x)} [\log p_{\theta}(x|z)] + D_{\text{KL}} (q_{\phi}(z|x) \parallel p(z))$$
(8)

The VAE has attracted attention in various application fields due to its advantage of effectively learning and reconstructing the latent characteristics of data. In particular, by representing the complex patterns and uncertainties of data in the latent space, it has shown the potential to improve the accuracy of RUL prediction. However, conventional VAE models have the limitation of not being able to sufficiently capture various distributional characteristics, such as asymmetry and scale variation, because they use the normal distribution asthe prior distribution of latent variables.

Therefore, this study proposes the WVAE, which assumes the Weibull distribution instead of the normal distribution as the prior distribution, in order to more accurately capture the characteristics of failure patterns and improve the reliability of RUL prediction.

## 3.2 | Variational Autoencoder for Probabilistic Non-Negative Matrix Factorization

The variational autoencoder for probabilistic non-negative matrix factorization (PAE-NMF) extends the VAE framework by modeling the prior distribution of the non-negative latent variable  $h \ge 0$ with a Weibull distribution characterized by shape parameter  $\beta$ and scale parameter  $\eta$ . The input data are represented as  $V \in$  $\mathbb{R}^{m \times n}$ , where m denotes the number of features and n indicates the sequence length or the number of data points. The encoder network maps each input vector  $\mathbf{x} \in \mathbb{R}^m$  to the shape and scale parameters of the latent distribution q(h|x), and applies the reparameterization trick to enable differentiable sampling from the Weibull distribution [41]. The Weibull distribution ensures non-negativity and offers flexibility to capture skewness and scale variations. By adjusting the shape parameter, it can effectively model various failure patterns, including infant mortality, random failures, and wear-out failures. These characteristics enable the PAE-NMF to learn latent representations that reflect failure behavior more faithfully than a Gaussian-based VAE. The model is trained by maximizing the ELBO, where the reconstruction loss forms the first term, and the KL divergence serves as the second term to constrain the posterior towards the prior.

ELBO 
$$(x) = \mathbb{E}_{q_{\phi}(h|x)} [\log p_{\theta}(x|h)]$$
  
 $-D_{\text{KL}} (q_{\phi}(h|x) \parallel p(h))$ 

$$(9)$$

In the PAE-NMF, the latent distribution is replaced with a Weibull distribution instead of a Gaussian. For each latent dimension  $j=1,\ldots,r$ , the encoder outputs the parameters  $\beta_j(x)>0$  and  $\eta_j(x)>0$ , while the prior is defined as the same family of Weibull distributions. The reconstruction term is identical to that of a standard VAE, with the difference lying in the KL term. The posterior and prior distributions are therefore formulated as:

$$q_{\phi}(h|x) = \prod_{j=1}^{r} \text{Weibull}(h_{j}; \beta_{j}(x), \eta_{j}(x))$$
(10)

$$p(h) = \prod_{j=1}^{r} \text{Weibull}\left(h_{j}; \beta_{j}^{(0)}, \eta_{j}^{(0)}\right)$$
 (11)

The KL term uses the closed-form expression of the KL divergence between two Weibull distributions for each dimension, as follows:

$$\begin{aligned} \mathrm{D_{KL}} \; & (\mathrm{Weibull} \, (\beta_1, \eta_1) \parallel \mathrm{Weibull} \, (\beta_2, \eta_2)) = log \left( \frac{\beta_1}{\eta_1^{\beta_1}} \right) \\ & - \log \left( \frac{\beta_2}{\eta_2^{\beta_2}} \right) + (\beta_1 - \beta_2) \left[ \log \; (\eta_1) - \frac{\gamma}{\beta_1} \right] \\ & + \left( \frac{\eta_1}{\eta_2} \right)^{\beta_2} \Gamma \left( 1 + \frac{\beta_2}{\beta_1} \right) - 1 \end{aligned} \tag{12}$$

 $\gamma \approx$  0.5772, known as the Euler–Mascheroni constant, and the overall loss function is expressed as the combination of the reconstruction error and the KL term, formulated as:

$$\mathcal{L}_{PAE} (x) = \frac{1}{2\sigma^{2}} \| x - \hat{x}_{\theta}(h) \|^{2} +$$

$$D_{KL} (q_{\phi}(h|x) \| p(h))$$
(13)

However, when applying the above loss function, the performance can vary sensitively depending on the parameter setting of the prior distribution, and a significant computational cost is required during training due to the complexity of calculating the KL divergence term. To overcome these limitations, this study newly designs a loss function for the WVAE that does not rely on a fixed prior distribution assumption but instead directly estimates the Weibull distribution parameters from the data. The proposed loss function enables data-driven distribution learning while simultaneously aiming to improve computational efficiency and generalization performance.

## 3.3 | Weibull Variational Autoencoder Based RUL Prediction

#### 3.3.1 | Proposed Framework

The WVAE proposed in this study is designed with both the encoder and decoder adopting a 1D-CNN architecture to effectively capture the patterns of input failure history data. The input data are denoted as  $\mathbf{X} = \{x_1, x_2, \ldots, x_M\}$ , where  $x_i$  represents the ith failure record and M indicates the number of time steps in the failure history sequence used as input. The encoder  $\mathbf{f}_{\text{enc}}(\cdot)$  estimates the shape parameter  $\beta$  and the scale parameter  $\eta$  of the Weibull distribution from the input  $\mathbf{X}$ , as follows:

$$(\beta, \eta) = f_{enc} (X; \Theta_{enc})$$
 (14)

Here,  $\Theta_{\rm enc}$  denotes the set of learnable parameters of the encoder. The estimated parameters  $(\beta, \eta)$  are used for the generation of latent variables, and z is defined by the inverse cumulative distribution function of the Weibull distribution as follows:

$$z = \eta(-\ln(1-\varepsilon))^{\frac{1}{\beta}} \tag{15}$$

Here,  $\varepsilon \sim \mathcal{U}(0, 1)$ . The latent variable z defined in this way reflects the stochastic characteristics of the Weibull distribution and is used as the input to the decoder. The decoder  $f_{\text{dec}}(\cdot)$  reconstructs the input sequence based on the latent variable z and predicts the failure time  $\hat{y}$ , which can be formulated as

$$\hat{y} = f_{\text{dec}} (z; \Theta_{\text{dec}}). \tag{16}$$

Here,  $\Theta_{\rm dec}$  denotes the set of learnable parameters of the decoder. Consequently, the WVAE probabilistically defines the latent variable z using the parameters of the Weibull distribution estimated from the input data X. Unlike the conventional VAE that restricts the latent variables to follow a normal distribution, the WVAE adopts the Weibull distribution, which is more suitable for capturing the statistical characteristics of actual failure history data, thereby ensuring both the realism and validity of failure time prediction. The overall structure and data processing flow of the WVAE are illustrated in Figure 2.

#### 3.3.2 | Loss Function

The proposed WVAE model employs a loss function that combines the mean squared error (MSE) term with the negative log-likelihood term of the Weibull distribution in order to not

<span id="page-5-0"></span>![](_page_5_Figure_1.jpeg)

**FIGURE 2** Overall architecture of the proposed WVAE.

only enhance the accuracy of failure time prediction but also effectively learn the probabilistic characteristics inherent in the time-seriesfailure patterns. This composite lossfunction not only minimizes the prediction error but also guides the model to effectively capture the statistical characteristics of the observed failure time distribution. The loss function is defined as

$$L(y, \hat{y}, \beta, \eta) = \frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2 + \lambda \cdot \left[ N \left( \ln \frac{\eta^{\beta}}{\beta} \right) + \sum_{i=1}^{N} \left( \frac{y_i}{\eta} \right)^{\beta} - (\beta - 1) \sum_{i=1}^{N} \ln y_i \right] + \delta$$

$$(17)$$

Here, denotes the actual failure time of the -th time series sample, and ̂ denotes the failure time predicted by the WVAE. and are the shape and scale parameters of the Weibull distribution estimated by the encoder, and represents the total number of samples in the batch. The first term is the MSE term, which directly penalizes point-wise deviations between the predicted and observed failure times. While the negative loglikelihood term encourages the estimated Weibull distribution to match the overall statistical pattern of the failure data, it does not by itself guarantee accurate prediction at each individual time step; the MSE term therefore complementsthe distributional objective by directly constraining point-wise prediction errors. The coefficient controls the relative importance between the two loss terms. If is excessively large, the model focuses on distribution fitting, which may degrade the accuracy of actual failure time prediction. Conversely, if is too small, distribution learning is insufficient, resulting in the inability to properly reflect uncertainty.

Therefore, serves as a critical tuning parameter that balances predictive performance and distribution learning.In addition, the constant is introduced as an additive constant to maintain a positive loss value. Maintaining a positive loss value is useful in practice because training progress is typically monitored through the loss value logged or plotted at each epoch, and such monitoring is most easily and consistently interpreted when the loss remains positive throughout training; a value that changes sign could otherwise be mistaken for a numerical error. Because *δ* is an additive constant that does not depend on any of the model's trainable parameters, its gradient with respect to those parameters is identically zero. Consequently, adding *δ* has no effect on the optimization trajectory, the converged solution, or the estimated Weibull parameters, provided that *δ* is chosen large enough to keep the loss positive throughout training.In thisstudy, *δ* = 50 was selected as a sufficiently large offset to maintain a positive loss value across all experimental conditions; therefore, a separate sensitivity analysis for *δ* was not deemed necessary.

#### **3.3.3 Sensitivity Analysis of the Hyperparameter** *λ*

A sensitivity analysis was performed to examine the effect of the loss-function hyperparameter on the predictive performance of the WVAE and to justify the selection of = 0.01. The hyperparameter determines the relative contribution of the negative log-likelihood (NLL) term to the MSE-based prediction loss. To evaluate its effect, was varied over the following range: {0.001, 0.003, 0.005, 0.01, 0.03, 0.05, 0.1, 0.2, 0.3, 0.5,1.0}. For each value, the WVAE was trained and evaluated on the nine simulation datasets described in Section [4.1,](#page-7-0) with 10 independent repetitions conducted for each condition. The results are summarized in Table [2](#page-6-0) and Table [3.](#page-7-0)

A key finding is that the model performance is highly robust to the choice of . Across all 11 tested values, the average CRPS varies by only 9.67, corresponding to a relative variation of 1.4%, while the average PICP varies by 0.013. This indicates that the WVAE is not sensitive to the specific setting of , which is a desirable property for practical applications where exhaustive hyperparameter tuning may not be feasible.

Within this narrow variation, = 0.01 achieves the highest average PICP of 0.134 among all tested values, while its average CRPS of 704.4 remains within 0.8% of the best-performing value on average across the nine datasets. In all individual datasets, the CRPS at = 0.01 falls within 5.3% of the dataset-specific optimum. This demonstrates that = 0.01 provides the best balance between interval coverage and distributional accuracy among the tested configurations.

The estimated Weibull shape parameter ̂, presented in Table [3,](#page-7-0) provides additional insight into the distributional learning behavior. For all three failure types, ̂ stabilizes at ≥ 0.01 and remains virtually constant for further increases in . For the infant mortality dataset (true = 0.8), ̂ converges from 0.634 at = 0.001 to 0.645 for ≥ 0.01. For the random failure dataset (true = 1.0), ̂ stabilizes at approximately 0.690 for *λ* ≥ 0.01, compared to 0.771 at = 0.001. For the wear-out failure dataset (true = 2.5), ̂ ranges between 1.35 and 1.42 across all values. This convergence confirmsthat the Weibull distributional learning is effectively activated at = 0.01 and remains stable regardless of further increases in .

<span id="page-6-0"></span>**TABLE 2** | Sensitivity of the WVAE predictive performance to the loss-function hyperparameter  $\lambda$  across the nine simulation datasets.

|                       |         |        |        |        |        |        | Λ      |        |        |        |        |        |
|-----------------------|---------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| Dataset               | Metrics | 0.001  | 0.003  | 0.005  | 0.01   | 0.03   | 0.05   | 0.1    | 0.2    | 0.3    | 0.5    | 1.0    |
| Infant mortality      | PICP    | 0.1067 | 0.0917 | 0.0917 | 0.0950 | 0.0883 | 0.0883 | 0.0867 | 0.0867 | 0.0867 | 0.0850 | 0.0850 |
| $(\sigma = 50)$       | CRPS    | 943.17 | 951.45 | 951.98 | 950.70 | 953.54 | 952.92 | 953.25 | 953.44 | 953.46 | 953.87 | 953.88 |
| Infant mortality      | PICP    | 0.1533 | 0.1383 | 0.1417 | 0.1417 | 0.1450 | 0.1467 | 0.1467 | 0.1467 | 0.1467 | 0.1467 | 0.1467 |
| $(\sigma = 100)$      | CRPS    | 643.88 | 649.06 | 649.73 | 649.62 | 649.33 | 649.72 | 650.07 | 649.96 | 650.17 | 650.19 | 650.19 |
| Infant mortality      | PICP    | 0.2067 | 0.1783 | 0.1750 | 0.1733 | 0.1717 | 0.1750 | 0.1733 | 0.1617 | 0.1617 | 0.1617 | 0.1617 |
| $(\sigma = 150)$      | CRPS    | 853.40 | 869.46 | 866.19 | 865.56 | 865.14 | 864.74 | 865.09 | 866.04 | 866.03 | 866.04 | 866.04 |
| Random ( $\sigma$ =   | PICP    | 0.0133 | 0.0133 | 0.0100 | 0.0100 | 0.0100 | 0.0100 | 0.0100 | 0.0100 | 0.0100 | 0.0100 | 0.0100 |
| 50)                   | CRPS    | 808.68 | 809.01 | 809.27 | 809.29 | 809.28 | 809.29 | 809.35 | 809.35 | 809.35 | 809.34 | 809.34 |
| Random ( $\sigma$ =   | PICP    | 0.0017 | 0.0083 | 0.0050 | 0.0017 | 0.0017 | 0.0017 | 0.0017 | 0.0017 | 0.0017 | 0.0017 | 0.0017 |
| 100)                  | CRPS    | 889.85 | 889.52 | 889.48 | 890.09 | 890.02 | 890.01 | 890.02 | 890.02 | 890.02 | 890.02 | 890.03 |
| Random ( $\sigma$ =   | PICP    | 0.0767 | 0.0583 | 0.0583 | 0.0583 | 0.0633 | 0.0650 | 0.0667 | 0.0667 | 0.0667 | 0.0667 | 0.0667 |
| 150)                  | CRPS    | 603.62 | 604.95 | 604.65 | 604.78 | 604.81 | 604.70 | 604.67 | 604.65 | 604.65 | 604.65 | 604.65 |
| Wear-out ( $\sigma$ = | PICP    | 0.3117 | 0.3250 | 0.2833 | 0.3133 | 0.2300 | 0.2467 | 0.2683 | 0.2267 | 0.2250 | 0.2250 | 0.2200 |
| 50)                   | CRPS    | 430.87 | 454.05 | 434.56 | 453.52 | 438.93 | 437.75 | 435.61 | 438.89 | 439.41 | 439.91 | 440.05 |
| Wear-out ( $\sigma$ = | PICP    | 0.0200 | 0.0467 | 0.0350 | 0.1000 | 0.1000 | 0.1000 | 0.1000 | 0.1000 | 0.0817 | 0.1000 | 0.1000 |
| 100)                  | CRPS    | 662.90 | 696.36 | 662.04 | 667.00 | 674.81 | 673.28 | 663.36 | 665.85 | 659.00 | 676.87 | 671.24 |
| Wear-out ( $\sigma$ = | PICP    | 0.2733 | 0.2850 | 0.2900 | 0.3117 | 0.3317 | 0.3600 | 0.3467 | 0.3733 | 0.3750 | 0.3850 | 0.3600 |
| 150)                  | CRPS    | 454.25 | 453.81 | 451.04 | 449.08 | 448.11 | 447.43 | 448.47 | 445.78 | 445.92 | 445.61 | 447.50 |
| Average               | PICP    | 0.1293 | 0.1272 | 0.1211 | 0.1339 | 0.1269 | 0.1326 | 0.1333 | 0.1304 | 0.1283 | 0.1313 | 0.1280 |
|                       | CRPS    | 698.96 | 708.63 | 702.10 | 704.40 | 703.77 | 703.32 | 702.21 | 702.67 | 702.00 | 704.06 | 703.66 |

Based on these observations,  $\lambda=0.01$  was selected as the operating point. This value corresponds to the onset of the stable regime where the distributional learning component becomes fully effective, and it simultaneously achieves the highest PICP among all tested values while maintaining near-optimal CRPS performance.

#### 3.3.4 | Data Preparation and Input Configuration

In this study, the preprocessing and structuring of input data were designed as follows to train and evaluate the WVAE model based on product failure history data. The entire failure history time series of each product was treated as a single training batch, since the negative log-likelihood term requires the full time series interval as input to accurately estimate the parameters of the Weibull distribution. This design enables the model to effectively capture the inherent failure patterns of each product.

The complete time series was divided into training and evaluation datasets. Specifically, the first 70% of each series was used as model input, while the target prediction interval was defined up to 80% of the series. The final 20% of the series was excluded from training and used solely for evaluation by comparing the model's predictions with the actual failure history. This partitioning strategy guides the model to learn forecasting after the input interval, thereby enhancing long-term predictive performance while objectively validating generalization performance on unseen data.

Data normalization was carefully designed to prevent abnormal training under the negative log-likelihood term and to avoid mathematical errors during loss computation. Since logarithmic operations yield errors when input values are non-positive, all inputs were normalized with respect to the maximum value within each product's input interval to guarantee positivity. Each time point of the input sequence  $\boldsymbol{X}$  was normalized as follows:

$$x_i' = \frac{x_i}{\max(\mathbf{X})} \tag{18}$$

Here,  $x_i'$  denotes the normalized input value.

This approach ensures that the input values remain strictly within the positive domain and are normalized to the range between 0 and 1, thereby allowing the logarithmic function to be applied while securing both the stability of model training and the mathematical validity of loss function computation.

# 3.3.5 | Uncertainty Quantification via Monte Carlo Dropout

In this study, monte carlo dropout (MC Dropout) was introduced to quantify the uncertainty of predictions. This method is a probabilistic approach that estimates the predictive distribution by enabling dropout during inference and repeatedly performing multiple forward passes for the same input sequence [42]. Specifically, the model performs a total of K stochastic forward passes

<span id="page-7-0"></span>**TABLE 3** Estimated Weibull shape parameter of the WVAE for each value of across the nine simulation datasets.

|                               |        |        |        |        |        |        | λ      |        |        |        |        |        |
|-------------------------------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| Dataset                       | True β | 0.001  | 0.003  | 0.005  | 0.01   | 0.03   | 0.05   | 0.1    | 0.2    | 0.3    | 0.5    | 1.0    |
| Infant mortality<br>(σ = 50)  | 0.8    | 0.6547 | 0.6416 | 0.6407 | 0.6605 | 0.6605 | 0.6610 | 0.6699 | 0.6703 | 0.6703 | 0.6720 | 0.6720 |
| Infant mortality<br>(σ = 100) | 0.8    | 0.6587 | 0.6707 | 0.6655 | 0.6660 | 0.6705 | 0.6707 | 0.6723 | 0.6721 | 0.6731 | 0.6730 | 0.6730 |
| Infant mortality<br>(σ = 150) | 0.8    | 0.5884 | 0.5921 | 0.5963 | 0.6008 | 0.5996 | 0.5967 | 0.5974 | 0.5913 | 0.5912 | 0.5912 | 0.5912 |
| Random (σ =<br>50)            | 1.0    | 0.7416 | 0.7188 | 0.6766 | 0.6750 | 0.6736 | 0.6732 | 0.6733 | 0.6733 | 0.6738 | 0.6735 | 0.6734 |
| Random (σ =<br>100)           | 1.0    | 0.8095 | 0.7629 | 0.7392 | 0.6838 | 0.7059 | 0.7050 | 0.7032 | 0.7031 | 0.7031 | 0.7030 | 0.7033 |
| Random (σ =<br>150)           | 1.0    | 0.7618 | 0.7109 | 0.7073 | 0.7104 | 0.6927 | 0.6946 | 0.6944 | 0.6943 | 0.6945 | 0.6944 | 0.6944 |
| Wear-out (σ =<br>50)          | 2.5    | 1.5504 | 1.6621 | 1.6361 | 1.6373 | 1.5637 | 1.5473 | 1.4687 | 1.5445 | 1.5622 | 1.5697 | 1.5776 |
| Wear-out (σ =<br>100)         | 2.5    | 1.0858 | 1.0245 | 1.0011 | 0.9832 | 1.0126 | 0.9505 | 0.9667 | 1.0042 | 0.9981 | 0.9968 | 0.9945 |
| Wear-out (σ =<br>150)         | 2.5    | 1.5670 | 1.5845 | 1.4949 | 1.6520 | 1.5853 | 1.5510 | 1.6235 | 1.5499 | 1.5503 | 1.5787 | 1.5615 |
| Avg. — Infant<br>mortality    | 0.8    | 0.6339 | 0.6348 | 0.6342 | 0.6424 | 0.6435 | 0.6428 | 0.6465 | 0.6446 | 0.6449 | 0.6454 | 0.6454 |
| Avg. —<br>Random              | 1.0    | 0.7710 | 0.7309 | 0.7077 | 0.6897 | 0.6908 | 0.6909 | 0.6903 | 0.6902 | 0.6905 | 0.6903 | 0.6904 |
| Avg. —<br>Wear-out            | 2.5    | 1.4011 | 1.4237 | 1.3774 | 1.4242 | 1.3872 | 1.3496 | 1.3530 | 1.3662 | 1.3702 | 1.3817 | 1.3779 |

for the same input , thereby generating a set of predictions at each time step, ̂() = [̂ () <sup>1</sup> , ̂ () <sup>2</sup> , ..., ̂ () ] , = 1, 2, ..., The final prediction at each time step is then computed as the mean of the predictions, which is defined as follows:

$$\bar{y}_m = \frac{1}{K} \sum_{k=1}^K \hat{y}_m^{(k)}, \quad m = 1, 2, ..., M$$
 (19)

In addition, to account for uncertainty, a 95% confidence interval was computed at each time step from the predictive distribution. Specifically, the interval was defined by excluding the lower 2.5% and upper 2.5% of the distribution of the predicted samples {̂ () } =<sup>1</sup>. Unlike conventional approaches that provide only a single point estimate, this method reflects both the variability and uncertainty of the predictions. Therefore, in this study, both the mean prediction and the corresponding confidence interval were presented to provide more practical predictive results.

### **4 Evaluation**

#### **4.1 Data Description**

In this study, failure time series data for repairable systems were simulated based on the Weibull distribution to reproduce various failure patterns. During data generation, the scale parameter wasfixed at 800, and the shape parameter wasset to 0.8,1.0, and 2.5 to represent infant mortality, random, and wear-out failures, respectively. These settings reflect typical failure mechanisms observed in industrial environments.

To emulate a more realistic operational environment, white noise with a mean of 0 and standard deviations of 50, 100, and 150 was added to the failure times.In cases where the added noise resulted in negative or zero failure times, values were replaced with the first percentile to ensure the physical plausibility of the data.

A total of nine conditions were created by combining the three shape parameters with the three noise levels, and 300 time series samples were generated for each condition. The detailed composition of the resulting 2,700 time series dataset is presented in Table [4,](#page-8-0) which was used to assess the predictive performance of the proposed WVAE model across various failure types.

### **4.2 Evaluation Metrics**

The probabilistic predictive performance of the WVAE is assessed in this study from two main perspectives: first, the adequacy and efficiency of the predictive confidence interval, and second, the reproducibility of failure patterns. These two aspects act

<span id="page-8-0"></span>**TABLE 4** | Parameter settings for simulated failure patterns using Weibull distribution.

|                  | Data sa            | mpling             | Nois                  | se   | Number of |
|------------------|--------------------|--------------------|-----------------------|------|-----------|
| Failure pattern  | Shape<br>parameter | Scale<br>parameter | Standard<br>deviation | Mean | samples   |
| Infant mortality | 0.8                | 800                | 50                    | 0    | 300       |
| failure          |                    |                    | 100                   |      |           |
|                  |                    |                    | 150                   |      |           |
| Random failure   | 1.0                |                    | 50                    |      |           |
|                  |                    |                    | 100                   |      |           |
|                  |                    |                    | 150                   |      |           |
| Wear-out failure | 2.5                |                    | 50                    |      |           |
|                  |                    |                    | 100                   |      |           |
|                  |                    |                    | 150                   |      |           |

complementarily, providing a comprehensive basis for assessing model performance.

The predictive distribution was approximated by applying the MC Dropout technique, performing 100 repeated inferences for the same input. Accordingly, at time point m, the prediction interval is defined by the lower bound  $L_m$  and upper bound  $U_m$  according to the confidence level  $1-\alpha$ , corresponding to the lower  $\frac{\alpha}{2}$  and upper  $1-\frac{\alpha}{2}$  quantiles of the distribution, respectively. In this experiment, a 95% confidence level was applied, so the prediction interval at each time point was defined by the 2.5% lower and 97.5% upper quantiles of the distribution.

1. **Prediction Interval Coverage Probability**: The Prediction Interval Coverage Probability (PICP) is defined as the proportion of actual observations  $y_m$  that fall within the predictive confidence interval  $[L_m, U_m]$  at a given time point. It is calculated as follows [43]:

$$PICP = \frac{1}{M} \sum_{m=1}^{M} a_m \tag{20}$$

Here, M denotes the total number of time points, and  $a_m$  is a binary variable defined as follows:

$$a_{m} = \begin{cases} 1, \ y_{m} \in [L_{m}, U_{m}] \\ 0, \ y_{m} \notin [L_{m}, U_{m}] \end{cases}$$
 (21)

That is, if the observation falls within the confidence interval at a given time point, it is recorded as 1; otherwise, it is recorded as 0. Ideally, the PICP value should be close to the confidence level  $1-\alpha$ , which can be interpreted as a measure of how well the predictive interval captures the actual values.

2. **Mean Prediction Interval Width**: The Mean Prediction Interval Width (MPIW) represents the average width of the predictive confidence interval and indicates how wide the prediction intervals are on average across all time points. For a given confidence level, a smaller MPIW indicates a more efficient representation of information and serves as an indicator of the

prediction interval's quality. It is defined as follows [44]:

$$MPIW = \frac{1}{M} \sum_{m=1}^{M} (U_m - L_m)$$
 (22)

At an equivalent confidence level, a narrower MPIW indicates that the prediction interval conveys information more compactly, thereby serving as a quantitative measure of its efficiency and reliability.

3. **Continuous Ranked Probability Score**: The Continuous Ranked Probability Score (CRPS) is defined as the area obtained by integrating the difference between the predicted cumulative distribution function (CDF)  $\hat{F}_M(z)$  and the actual observation  $y_m$  after transforming it into a unit step CDF. It can evaluate the accuracy of the entire distribution, making it a more comprehensive performance metric than simple pointwise errors [44], as follows:

$$CRPS(\widehat{F}_M, y_m) = \int_{-\infty}^{\infty} \left[ \widehat{F}_M(z) - \mathbb{I}\{y_m \le z\} \right]^2 dz \qquad (23)$$

Here,  $\hat{F}_M(z)$  denotes the predicted cumulative distribution function at time point m. Using K predictive samples  $\hat{y}_m^{(k)}$  obtained from MC Dropout, CRPS can be approximated as follows:

CRPS 
$$(\hat{F}_{M}, y_{m}) = \frac{1}{K} \sum_{k=1}^{K} |\hat{y}_{m}^{(k)} - y_{m}|$$

$$-\frac{1}{2K^{2}} \sum_{k=1}^{K} \sum_{k'=1}^{K} |\hat{y}_{m}^{(k)} - \hat{y}_{m}^{(k')}|$$
(24)

The mean CRPS over the entire time series length *M* is calculated as follows:

$$\overline{\text{CRPS}} = \frac{1}{M} \sum_{m=1}^{M} CRPS(\hat{F}_{M}, y_{m})$$
 (25)

In this study, the overall predictive performance was evaluated by assessing conformity through PICP, efficiency through MPIW, and distributional reproduction through CRPS. A fair performance comparison was conducted between the proposed model

and the benchmarking models by applying the same number of repeated inferences, confidence level, and evaluation intervals.

**4.3 Benchmark Models**

For quantitative evaluation of the proposed method, representative benchmarking models were compared.

- 1. **LSTM**: LSTM is a variant ofRNN that mitigatesthe long-term dependency problem and vanishing gradients. The LSTM architecture consists of a cell state and gating units. The input gate controls incoming information, the forget gate manages past memory, and the output gate generates the output. Through this mechanism, LSTM effectively learns long-term patterns in time-series data [\[45\]](#page-20-0).
- 2. **1D-CNN**: 1D-CNN extracts local features through convolution operations, reduces dimensionality via pooling operations, and learns increasingly complex features hierarchically. The extracted features are directed to fully connected layers for prediction tasks. 1D-CNN can effectively capture local patterns in time series data [\[46\]](#page-20-0).
- 3. **MLP**: MLP is the most basic feedforward neural network structure in deep learning, which models nonlinear relationships effectively through multiple fully connected layers and nonlinear activation functions [\[47\]](#page-20-0). The network consists of input, hidden, and output layers. The activation of each neuron is computed from the weighted sum of the previous layer's outputs and a bias. Training is performed based on the backpropagation algorithm, which updates weightsin the direction of the input by differentiating the lossfunction [\[48\]](#page-20-0). Through the universal approximation theorem, an MLP with adequate hidden units can approximate continuousfunctions with arbitrary accuracy.
- 4. **VAE**: VAE is a probabilistic generative model that maps high-dimensional data to a lower-dimensional latent variable space to learn the data distribution [\[49\]](#page-20-0). The encoder maps the input data to the mean and variance of latent variables, and the decoder reconstructs the original data from them. Training is conducted by maximizing the ELBO, assuming the latent variables follow a standard normal prior (0, 1).
- 5. **PAE-NMF**: PAE-NMF extends the VAE architecture by adopting a Weibull distribution, instead of a normal distribution, asthe priorforlatent variables. The Weibull distribution ensures non-negative values and allows flexible modeling of various failure patterns. This enables latent space learning that better reflects failure characteristics compared to the standard VAE.

#### **4.4 Experimental Details**

All experiments for the proposed WVAE model and the benchmarking algorithms were conducted on the same workstation equipped with 8 core CPUs of Intel i9-9900K 3.60 GHz and a GPU of NVIDIA GeForce RTX 2080 Ti, ensuring that the entire process of training and evaluation was performed consistently. To guarantee stable convergence and a fair comparison with the benchmarking models, various network architectures and hyperparameter combinations were explored.

Specifically, the depth of the network and the number of neurons perlayer were varied to analyze differencesin model capacity and expressiveness, and training-related variables such as learning rate, batch size, and number of epochs were adjusted to evaluate performance. In addition, for the estimation of Weibull distribution parameters, the shape parameter *β* was passed through a Softplus activation function to ensure it always takes positive values while allowing smooth changes near small values, and the scale parameter *η* was passed through an Exponential activation function to guarantee positivity and, due to the logarithmic rate-of-change property, to facilitate faster training convergence. Through this exploration process, the final selected hyperparameters are summarized in Tabl[e6,](#page-13-0) and the detailed network architecture is presented in Table [5.](#page-10-0)

In addition, considering the stochastic characteristic of neural network training, each experiment was repeated 10 times. The performance metrics, such as PICP, MPIW, and CRPS, were then evaluated by calculating the average over all repeated experiments.

#### **4.5 Results on Simulated Data**

In this section, we present a comparison between the WVAE and the benchmarking models using the simulation dataset classified into infant mortality failures, random failures, and wear-out failures. To verify the reproduction of probabilistic characteristics, the prediction results of each model and the actual data were converted into probability density functions and cumulative failure probabilities for analysis. In addition, for a fair quantitative comparison among models, the MPIW was fixed at 480, which is the average value across all models, and under the same conditions, PICP and CRPS were evaluated.

Figures [3,](#page-10-0) 4 and [5](#page-11-0) show the predicted failure time PDFs for the infant mortality failure, random failure, and wear-out failure datasets, respectively. The predictive density of WVAE maintained a shape similar to the raw data not only in the high-frequency failure intervals but also in the sparse failure occurrence intervals, which suggests that it learned the distributional characteristics themselves rather than the simple mean trend. In contrast, VAE, by assuming the prior distribution as a standard normal distribution, performed limited variance estimation in non-Gaussian characteristics such as the early and random intervals, and PAE-NMF, by assuming the shape parameter as 2.5 and the scale parameter as 800 as the prior distribution, lacked expressive power in the early and random failure intervals. LSTM and 1D-CNN showed tendencies where the distribution was excessively concentrated or distorted in certain intervals. MLP, because prediction is performed based on the DMS structure, showed relatively less sequential cumulative error, which provided certain advantages in terms of nonlinear pattern learning. However, at the two ends of the distribution, that is, in the regions where failures occur very early or are extremely delayed, the prediction reliability was low, showing a limitation in sufficiently reflecting the sparse patterns of the raw data.

<span id="page-10-0"></span>**TABLE 5** Detailed configuration parameters of the WVAE.

| Submodule | Layer             | In<br>channels | Kernel | Stride | Activation  | Trainable<br>parameter | Output<br>size |
|-----------|-------------------|----------------|--------|--------|-------------|------------------------|----------------|
| Encoder   | Conv 1D           | 1              | 1      | 1      | ReLU        | 1,024                  | 512 ×<br>210   |
|           | Conv 1D           | 512            | 1      | 1      | ReLU        | 131,328                | 256 ×<br>105   |
|           | AvgPool           | —              | —      | —      |             | 0                      | 256 × 1        |
|           | Flatten           | —              | —      | —      |             | 0                      | 256            |
| Weibull 𝛽 | Linear            | 256            | —      | —      | ReLU        | 131,584                | 512            |
|           | Linear            | 512            | —      | —      | ReLU        | 131,328                | 256            |
|           | Linear            | 256            | —      | —      | Softplus    | 257                    | 1              |
| Weibull 𝜂 | Linear            | 256            | —      | —      | ReLU        | 131,584                | 512            |
|           | Linear            | 512            | —      | —      | ReLU        | 131,328                | 256            |
|           | Linear            | 256            | —      | —      | Exponential | 257                    | 1              |
| Decoder   | Conv Transpose 1D | 256            | 1      | 1      | ReLU        | 131,584                | 512 ×<br>500   |
|           | Conv Transpose 1D | 512            | 1      | 1      | Sigmoid     | 513                    | 1 × 500        |

![](_page_10_Figure_3.jpeg)

**FIGURE 3** Comparison of probability density functions between actual and predicted failure timesfor infant mortality failure data generated from a Weibull distribution with shape parameter = 0.8 and scale parameter = 800, under additive noise = 150.

Figures [6,](#page-12-0) 7 and [8](#page-13-0) show the results of CDF comparison for each failure type. The predicted cumulative failure probability curve of WVAE exhibited generally high consistency with the empirical curve, and although local differences existed depending on the intervals, the overall cumulative pattern was stably maintained. This indicates that WVAE demonstrates balanced performance in predicting the cumulative behavior of failure data.

Tabl[e8](#page-14-0) summarizes the quantitative evaluation results under the same condition where the prediction interval width of all models was fixed to MPIW = 480. In this condition, WVAE recorded the lowest CRPS in all datasets, showing that the predicted distribution most closely approximated the actual distribution. In the case of PICP, other models showed higher values in some conditions, but in many other datasets, WVAE maintained high interval conformity even under the same width condition.

<span id="page-11-0"></span>![](_page_11_Figure_1.jpeg)

**FIGURE 4** Comparison of probability density functions between actual and predicted failure times for random failure data generated from a Weibull distribution with shape parameter = 1 and scale parameter = 800, under additive noise = 150.

![](_page_11_Figure_3.jpeg)

**FIGURE 5** Comparison of probability density functions between actual and predicted failure times for wear-out failure data generated from a Weibull distribution with shape parameter = 2.5 and scale parameter = 800, under additive noise = 150.

In summary, under the same condition, WVAE consistently secured superiority in distributional conformity and presented competitive results in interval conformity.

Furthermore, Table [7](#page-14-0) presents the shape and scale parameters of the Weibull distribution estimated by WVAE along with their 95% confidence intervals. Overall, the estimated parameters

<span id="page-12-0"></span>![](_page_12_Figure_1.jpeg)

**FIGURE 6** Comparison of predicted cumulative failure probabilities on infant mortality failure data generated from a Weibull model ( = 0.8, = 800) with additive noise = 150: (a) Proposed, (b) VAE, (c) PAE-NMF, (d) MLP, (e) LSTM, (f) 1D-CNN.

![](_page_12_Figure_3.jpeg)

**FIGURE 7** Comparison of predicted cumulative failure probabilities on random failure data generated from a Weibull model ( = 1, = 800) with additive noise = 150: (a) Proposed, (b) VAE, (c) PAE-NMF, (d) MLP, (e) LSTM, (f) 1D-CNN.

<span id="page-13-0"></span>![](_page_13_Figure_2.jpeg)

**FIGURE 8** Comparison of predicted cumulative failure probabilities on wear-out failure data generated from a Weibull model ( = 2.5, = 800) with additive noise = 150: (a) Proposed, (b) VAE, (c) PAE-NMF, (d) MLP, (e) LSTM, (f) 1D-CNN.

**TABLE 6** Hyperparameters for Training the Proposed WVAE Model.

| Hyperparameter | Value   | Remark                                                     |
|----------------|---------|------------------------------------------------------------|
| Learning rate  | 0.00001 | Step size for weight updates<br>during training            |
| Batch size     | 256     | Number of samples processed<br>in each training iteration  |
| Optimizer      | Adam    | Algorithm for updating model<br>parameters during training |
| Epochs         | 300     | Number of complete passes<br>through the training dataset  |

were close to the actual values used for data generation, and in particular, was stably derived around 800 under most conditions. However, in the case of the early failure dataset with a high noise level ( = 150), was estimated larger than the actual value and was derived lower, showing a pronounced deviation. Nevertheless, in many conditions, both and maintained values approximate to the actual ones, which demonstrates that WVAE not only reproduces the distributional shape but also secures a certain level of reliability in parameter estimation. These performance differences stem from the structural assumptions and learning mechanisms of each model. For example,VAE,since it assumes a unit Gaussian prior in the latent space, could not sufficiently capture non-Gaussian behavior, resulting in limited expressiveness. Similarly, PAE-NMF due to the restriction of fixed Weibull distribution parameters, provided relatively reasonable approximation in the wear-outstage but lacked flexibility in early or random failure patterns. In addition, LSTM and 1D-CNN were sensitive to noise and temporal variability inherent in the data, showing tendencies where the predicted distribution became unnecessarily narrow in certain intervals or, conversely, exhibited biases deviating from the actual trend. In contrast, WVAE mitigated these limitations by directly learning the parameters and maintained stable performance across various failure types.

### **4.6 Computational Efficiency and Modeling Robustness in Comparison to PAE-NMF**

In this section, WVAE and PAE-NMF are compared from the perspectives of computational efficiency and modeling robustness. First, PAE-NMF was evaluated under the same prior distribution settings asthe Weibull distribution used for data generation. That is, Figure [9](#page-15-0) presentsthe results when the Weibull parameters used in the data generation stage were given as priors for each failure type. In this configuration, the PDF and CDF fitting of PAE-NMF showed an improvement compared to Figures [3–8](#page-10-0) where a single prior distribution was fixed, indicating that the performance of PAE-NMF heavily depends on the prior distribution settings. In contrast, in practical applications, it is difficult to know the prior parameters precisely, and the optimal prior settings may vary depending on the dataset and product family, so the vulnerability to prior mismatch can act as a modeling limitation.

However, WVAE constructsthe predictive distribution by directly estimating the Weibull parameters from the data without assuming fixed prior parameters. As a result, its performance is not

<span id="page-14-0"></span>**TABLE 7** Estimated Weibull parameters with 95% confidence intervals obtained from the proposed WVAE model under different datasets and noise levels.

| Dataset          |                       | Parameter | Parameter<br>Estimate | Lower<br>Bound | Upper<br>Bound |
|------------------|-----------------------|-----------|-----------------------|----------------|----------------|
| Infant Mortality | Noise level (𝜎 = 50)  | 𝛽         | 0.742                 | 0.714          | 0.770          |
| failure          |                       | 𝜂         | 909.864               | 770.399        | 1091.385       |
|                  | Noise level (𝜎 = 100) | 𝛽         | 0.774                 | 0.747          | 0.801          |
|                  |                       | 𝜂         | 879.715               | 733.221        | 1061.108       |
|                  | Noise level (𝜎 = 150) | 𝛽         | 0.609                 | 0.584          | 0.637          |
|                  |                       | 𝜂         | 1457.664              | 1233.273       | 1729.375       |
| Random failure   | Noise level (𝜎 = 50)  | 𝛽         | 0.995                 | 0.950          | 1.035          |
|                  |                       | 𝜂         | 811.424               | 699.975        | 948.526        |
|                  | Noise level (𝜎 = 100) | 𝛽         | 1.092                 | 1.042          | 1.138          |
|                  |                       | 𝜂         | 887.353               | 768.750        | 1031.162       |
|                  | Noise level (𝜎 = 150) | 𝛽         | 1.035                 | 0.983          | 1.084          |
|                  |                       | 𝜂         | 835.287               | 715.409        | 986.587        |
| Wear-out         | Noise level (𝜎 = 50)  | 𝛽         | 2.297                 | 2.126          | 2.453          |
| failure          |                       | 𝜂         | 752.598               | 697.391        | 817.340        |
|                  | Noise level (𝜎 = 100) | 𝛽         | 2.287                 | 2.108          | 2.455          |
|                  |                       | 𝜂         | 801.864               | 734.475        | 880.257        |
|                  | Noise level (𝜎 = 150) | 𝛽         | 2.082                 | 1.919          | 2.229          |
|                  |                       | 𝜂         | 782.550               | 720.828        | 848.452        |

**TABLE 8** Performance comparison of proposed WVAE and benchmark models under different failure types and noise levels.

|           |             |         | WVAE       |       |         |       |       |        |
|-----------|-------------|---------|------------|-------|---------|-------|-------|--------|
| Dataset   |             | Metrics | (Proposed) | VAE   | PAE-NMF | MLP   | LSTM  | 1D-CNN |
| Infant    | Noise level | PICP    | 0.227      | 0.025 | 0.085   | 0.168 | 0.142 | 0.202  |
| mortality | (𝜎 = 50)    | CRPS    | 655        | 1051  | 1013    | 815   | 762   | 680    |
| failure   | Noise level | PICP    | 0.213      | 0.045 | 0.050   | 0.167 | 0.207 | 0.225  |
|           | (𝜎 = 100)   | CRPS    | 424        | 819   | 797     | 622   | 562   | 495    |
|           | Noise level | PICP    | 0.212      | 0.033 | 0.132   | 0.133 | 0.167 | 0.107  |
|           | (𝜎 = 150)   | CRPS    | 670        | 1102  | 1012    | 964   | 708   | 739    |
| Random    | Noise level | PICP    | 0.253      | 0.047 | 0.108   | 0.252 | 0.175 | 0.240  |
| failure   | (𝜎 = 50)    | CRPS    | 468        | 979   | 869     | 622   | 568   | 530    |
|           | Noise level | PICP    | 0.180      | 0.082 | 0.092   | 0.165 | 0.142 | 0.175  |
|           | (𝜎 = 100)   | CRPS    | 486        | 911   | 873     | 691   | 675   | 647    |
|           | Noise level | PICP    | 0.252      | 0.148 | 0.083   | 0.244 | 0.180 | 0.193  |
|           | (𝜎 = 150)   | CRPS    | 396        | 630   | 627     | 600   | 589   | 617    |
| Wear-out  | Noise level | PICP    | 0.578      | 0.390 | 0.432   | 0.467 | 0.562 | 0.560  |
| failure   | (𝜎 = 50)    | CRPS    | 183        | 269   | 285     | 280   | 245   | 241    |
|           | Noise level | PICP    | 0.552      | 0.510 | 0.498   | 0.510 | 0.533 | 0.493  |
|           | (𝜎 = 100)   | CRPS    | 183        | 239   | 257     | 255   | 238   | 232    |
|           | Noise level | PICP    | 0.473      | 0.430 | 0.457   | 0.500 | 0.445 | 0.471  |
|           | (𝜎 = 150)   | CRPS    | 217        | 284   | 286     | 271   | 305   | 284    |

<span id="page-15-0"></span>![](_page_15_Figure_1.jpeg)

**FIGURE 9** Comparison of predicted probability density functions and cumulative failure probabilities of PAE-NMF under different Weibull prior settings.

influenced by the choice of prior settings, and even when the failure type changes, performance variations are mild, showing consistent distribution fitting in both PDF and CDF. In terms of computational efficiency, WVAE also demonstrated competitiveness. When measuring training time with the same network structure and hyperparameters, the average time per epoch for PAE-NMF was 0.0718 s, while for WVAE it was 0.0681 s. Although the difference is not large, as the data size increases and the network structure becomes more complex, the training time gap between WVAE and PAE-NMF is likely to widen. This can be interpreted as an effect of the loss design adopted by WVAE to reduce computational load, as presented in Section [3.](#page-2-0)

Overall, PAE-NMF showed improved performance when an appropriate prior distribution was provided, but its effectiveness was highly dependent on the prior. In contrast, WVAE achieved independence from prior settings while maintaining computational efficiency. Considering situations similar to realworld applications, where prior knowledge is incomplete or the characteristics vary across products and batches, the results of this section support that WVAE provides both modeling robustness and scalable computational efficiency.

#### **5 VALIDATION ON THE BACKBLAZE HARD DRIVE DATASET EVALUATION**

## **5.1 Backblaze Hard Drive Dataset**

To assess the applicability of the proposed WVAE beyond the simulation-based evaluation presented in Section [4,](#page-7-0) this study additionally validates the model using the Backblaze Drive Stats dataset [\[50\]](#page-20-0), a publicly available field-reliability dataset for hard disk drives (HDDs). Since 2013, Backblaze has continuously published daily operational snapshots of the HDDs deployed across its data centers. For the calendar year 2025 alone, Backblaze reported a total of 344,196 drives across 31 models satisfying its minimum reporting criteria, with an overall annualized failure rate (AFR) of 1.36% [\[51\]](#page-20-0). Each daily record includes, among other attributes, a drive identifier, the drive model, a binary failure indicator, and a set of Self-Monitoring, Analysis, and Reporting Technology (SMART) attributes. In particular, SMART attribute 9 represents the cumulative power-on time of a drive, measured in hours[\[52\]](#page-20-0). In thisstudy, the raw value of this attribute, denoted smart\_9\_raw, was adopted as the observed failure time whenever a drive was flagged as failed.

For this validation, the complete data recorded across all four quarters of the 2025 calendar year were used. This period was selected for three reasons. First, it represents the most recent complete calendar year available at the time of this study, thereby reflecting drive models that are currently deployed in industrial environments. Second,restricting the analysisto a single calendar year helps ensure internal consistency of the recorded SMART attribute schema, since the set of reported attributes may vary across longer time spans. Third, aggregating data over a full year, rather than a single quarter, provides a sufficient number of failure events for the stable estimation of Weibull distribution parameters.

To ensure a sufficient sample size for stable Weibull parameter estimation, drive models with fewer than 30 recorded failures during 2025 were excluded, and the six models with the highest failure counts were selected for subsequent analysis. Table [9](#page-16-0) summarizesthe number of failure events and descriptive statistics

<span id="page-16-0"></span>**TABLE 9** Descriptive statistics of observed failure times for the selected drive models in 2025.

| Model                | n   | Mean     | Std. Dev. | Min   | Max    |
|----------------------|-----|----------|-----------|-------|--------|
| ST12000NM0008        | 479 | 45,409.9 | 7,477.0   | 2,268 | 54,064 |
| TOSHIBA MG07ACA14TA  | 432 | 45,744.4 | 8,036.5   | 6,399 | 63,314 |
| HGST HUH721212ALN604 | 393 | 52,877.3 | 7,135.0   | 5,906 | 62,385 |
| TOSHIBA MG08ACA16TA  | 361 | 18,935.8 | 5,843.8   | 405   | 34,169 |
| HGST HUH721212ALE604 | 356 | 35,759.0 | 7,193.8   | 47    | 47,983 |
| TOSHIBA MG08ACA16TEY | 318 | 32,872.5 | 6,819.6   | 4,536 | 43,719 |

of the observed failure times, measured in hours, for each selected model.

It should be noted that, for consistency with the structure of the simulation-based evaluation presented in Section [4,](#page-7-0) only drives with a failure event were included in the present analysis. Drives that remained uncensored throughout 2025 were excluded, and a comprehensive treatment of such observations is left as a direction for future research discussed in Section [6.](#page-18-0)

## **5.2 Results on Backblaze Data**

In this section, the proposed WVAE and the benchmarking models are evaluated on the six drive models described in Section [5.1.](#page-15-0) The data preprocessing and partitioning follow the protocol established in Section [3.3.4:](#page-6-0) for each drive model, the failure events are independently and identically distributed across units rather than temporally dependent. Accordingly, the training, testing, and validation subsets were constructed via stratified sampling across the range of observed failure times, ensuring comparable distributional characteristics across subsets, rather than by preserving chronological order asin the simulation-based evaluation of Section [4.](#page-7-0) Normalization was performed using a fixed constant of 100,000 h, common across all six drive models, chosen to comfortably exceed the maximum observed failure time in each model. Figures [10](#page-17-0) and [11](#page-17-0) present the cumulative failure probability and probability density function plots, respectively, of the proposed WVAE model on each of the six Backblaze drive models.

For a fair quantitative comparison among all models under identical conditions, the prediction interval width was standardized for each drive model by fixing the MPIW to the average value across all six algorithms. The fixed MPIW value used for each drive model is summarized in Table 10. Under these fixed-width conditions, PICP and CRPS were evaluated, and the results are summarized in Table [11.](#page-18-0)

Overall, WVAE achieved the highest PICP in five of the six drive models (ST12000NM0008, TOSHIBA MG07ACA14TA, HGST HUH721212ALN604, TOSHIBA MG08ACA16TA, and HGST HUH721212ALE604), indicating that its predictive intervals most reliably coverthe observed failure times across most drive models. In terms of CRPS, however, MLP was the strongest performer overall, achieving the lowest CRPS in four of the six models, while WVAE achieved the lowest CRPS on TOSHIBA MG08ACA16TA and HGST HUH721212ALE604. This pattern suggests that while

**TABLE 10** Fixed MPIW values used for standardized comparison across models, by drive model.

| Model                | Fixed MPIW |
|----------------------|------------|
| ST12000NM0008        | 11,178.5   |
| TOSHIBA MG07ACA14TA  | 11,964.4   |
| HGST HUH721212ALN604 | 14,911.9   |
| TOSHIBA MG08ACA16TA  | 9,193.2    |
| HGST HUH721212ALE604 | 9,857.6    |
| TOSHIBA MG08ACA16TEY | 10,395.4   |
|                      |            |

WVAE's predictive intervals are generally well calibrated in terms of coverage, MLP's point-wise predictions tend to align more closely with the full observed distribution in terms of overall distributional accuracy. On TOSHIBA MG08ACA16TEY, WVAE underperformed both benchmarks on PICP and CRPS; as discussed below, this is likely attributable to the coexistence of more than one failure mode within the population, which is inconsistent with the assumption of a single failure mode underlying the Weibull distribution used by WVAE.

This pattern points to a broader trade-off between the two evaluation criteria: WVAE, by explicitly modeling the Weibull shape and scale parameters, tends to produce well-calibrated prediction intervals that reliably cover the observed failure times, whereas MLP, optimized primarily for point-wise accuracy, tends to align more closely with the overallshape of the observed distribution as captured by CRPS. This distinction suggeststhat WVAE and MLP may be complementary in practice, with WVAE better suited to applications prioritizing reliable uncertainty coverage and MLP better suited to applications prioritizing point-forecast accuracy.

A further advantage of WVAE lies in its interpretability. Table [12](#page-18-0) compares the Weibull shape and scale parameters estimated by WVAE, averaged with their 95% confidence intervals over repeated independent training runs, against the corresponding classical Weibull maximum likelihood estimates (MLE) obtained directly from the observed failure times for each drive model. For the scale parameter , the classical MLE value falls within the 95% confidence interval of the WVAE estimate for all six drive models. For the shape parameter , the classical MLE value falls within the WVAE confidence interval for three of the six models (TOSHIBA MG07ACA14TA, TOSHIBA MG08ACA16TA, and TOSHIBA MG08ACA16TEY), while for the remaining three (ST12000NM0008, HGST HUH721212ALN604, and HGST

<span id="page-17-0"></span>![](_page_17_Figure_1.jpeg)

**FIGURE 10** Cumulative failure probability plots of the proposed WVAE model on the Backblaze dataset.

![](_page_17_Figure_3.jpeg)

**FIGURE 11** Probability density function plots of the proposed WVAE model on the Backblaze dataset.

HUH721212ALE604) the classical MLE lies just outside, though still close to, the WVAE confidence interval. Taken together, these results indicate that WVAE's latent Weibull parameters are, in most cases, statistically consistent with an established classical reference despite being learned entirely through the deep learning pipeline, providing evidence that WVAE offers an interpretability advantage over conventional black-box deep learning models by relating its predictions directly to physically meaningful, statistically grounded reliability parameters.

#### **5.3 Limitations**

Several limitations of the present validation should be noted. First, the failure-time distribution of TOSHIBA MG08ACA16TEY exhibited a pronounced bimodal pattern, as illustrated in Figure 11(f)), where two distinct peaks suggest the coexistence of an early-life failure mode and a wear-out failure mode within the same drive population. This represents a structural limitation of the single Weibull assumption underlying both WVAE and the

<span id="page-18-0"></span>**TABLE 11** Performance comparison of proposed WVAE and benchmark models under the Backblaze dataset.

|                 |         | WVAE       |        |         |        |        |        |
|-----------------|---------|------------|--------|---------|--------|--------|--------|
| Dataset         | Metrics | (Proposed) | VAE    | PAE-NMF | LSTM   | 1D-CNN | MLP    |
| ST12000NM0008   | PICP    | 0.8386     | 0.4450 | 0.1267  | 0.2983 | 0.2567 | 0.8333 |
|                 | CRPS    | 3245       | 8851   | 10210   | 24147  | 8898   | 3149   |
| TOSHIBA         | PICP    | 0.5788     | 0.4983 | 0.4133  | 0.2950 | 0.3017 | 0.5733 |
| MG07ACA14TA     | CRPS    | 5346       | 6751   | 9335    | 24903  | 9882   | 5035   |
| HGST            | PICP    | 0.9800     | 0.5533 | 0.1833  | 0.4733 | 0.3267 | 0.9617 |
| HUH721212ALN604 | CRPS    | 2482       | 7450   | 9664    | 27553  | 10018  | 2208   |
| TOSHIBA         | PICP    | 0.5634     | 0.4583 | 0.4500  | 0.2783 | 0.3533 | 0.5500 |
| MG08ACA16TA     | CRPS    | 3822       | 4534   | 4476    | 11490  | 5884   | 4157   |
| HGST            | PICP    | 0.8114     | 0.5950 | 0.1983  | 0.2733 | 0.3117 | 0.7633 |
| HUH721212ALE604 | CRPS    | 2814       | 5431   | 10942   | 19867  | 7279   | 2990   |
| TOSHIBA         | PICP    | 0.4385     | 0.4550 | 0.2550  | 0.2050 | 0.4233 | 0.5283 |
| MG08ACA16TEY    | CRPS    | 5149       | 5957   | 7890    | 18908  | 6961   | 4452   |

**TABLE 12** Estimated Weibull parameters obtained from the proposed WVAE model, with 95% confidence intervals, compared against classical Weibull maximum likelihood estimates (MLE) for each drive model.

|                      |           | Parameter |             |             |               |
|----------------------|-----------|-----------|-------------|-------------|---------------|
| Dataset              | Parameter | Estimate  | Lower Bound | Upper Bound | Classical MLE |
| ST12000NM0008        | 𝛽         | 8.988     | 8.369       | 9.546       | 9.57          |
|                      | 𝜂         | 47,820.2  | 45,229.2    | 50,573.2    | 47,531.5      |
| TOSHIBA MG07ACA14TA  | 𝛽         | 6.142     | 5.704       | 6.556       | 6.30          |
|                      | 𝜂         | 49,214.4  | 46,461.1    | 52,294.5    | 49,034.2      |
| HGST HUH721212ALN604 | 𝛽         | 11.307    | 10.511      | 12.080      | 12.92         |
|                      | 𝜂         | 54,819.2  | 52,478.5    | 57,732.4    | 54,853.9      |
| TOSHIBA MG08ACA16TA  | 𝛽         | 3.445     | 3.168       | 3.672       | 3.48          |
|                      | 𝜂         | 21,320.1  | 18,828.3    | 24,429.3    | 20,932.1      |
| HGST HUH721212ALE604 | 𝛽         | 5.576     | 5.149       | 5.954       | 6.13          |
|                      | 𝜂         | 38,157.1  | 35,579.6    | 40,957.1    | 37,600.5      |
| TOSHIBA              | 𝛽         | 5.556     | 5.189       | 5.950       | 5.71          |
| MG08ACA16TEY         | 𝜂         | 35,993.1  | 33,279.2    | 38,957.7    | 35,560.5      |

classical MLE reference, and extending the framework to mixture distributions is left for future work. Second, only drives with an observed failure event during 2025 were included in the present analysis;right-censored observations corresponding to drivesthat remained operational throughout the year were excluded.

### **6 Conclusion**

In this study, we proposed WVAE as a new approach for failure prediction of repairable systems and evaluated its performance against existing probabilistic and deep learning-based models. The evaluation utilized a simulation dataset classified into infant mortality failure, random failure, and wear-out failure types. WVAE faithfully reproduced the distributional characteristics of the actual data in the comparisons of probability density functions and cumulative failure probabilities, and also showed superior results compared to the benchmarking models in terms of CRPS and PICP under the same prediction interval width.

In addition, the proposed WVAE was further validated on a realworld field-reliability dataset, namely the Backblaze Drive Stats dataset, as presented in Section [5.](#page-15-0) Across six hard drive models, WVAE achieved the best or comparable PICP and CRPS relative to the benchmarking models in most cases, while a weaker performance was observed for a drive model exhibiting evidence of more than one coexisting failure mode, which is inconsistent with the single-failure-mode assumption underlying the Weibull distribution used by WVAE. Thisfinding, together with the exclusion of right-censored observations from the present analysis, further motivates extending WVAE to accommodate censored observations, as discussed above.

<span id="page-19-0"></span>Future research will focus on extending WVAE to be applicable to warranty data, which typically involves incomplete observation and right-censoring not addressed in the simulation-based and Backblaze-based evaluations presented in this study. This will require complementing the loss function and model structure to accommodate such censored observations. The resulting extended WVAE will then be applied to warranty data from actual industrial operations to verify its effectiveness under these more complex observation conditions. Through this, it is expected that WVAE will go beyond its demonstrated validity in both simulated and field-reliability settings and be positioned as a practical tool applicable to product life prediction and reliability management.

#### **Funding**

The author has nothing to report.

#### **Data Availability Statement**

The data that support the findings of this study are available from the corresponding author upon reasonable request.

#### **References**

- 1. J. Lei, W. Zhang, Z.Jiang, and Z. Gao, "A Review: Prediction Method for the Remaining Useful Life of the Mechanical System," *Journal of Failure Analysis and Prevention* 22, no. 6 (2022): 2119–2137.
- 2. L. Liao and F. Köttig, "A Hybrid Framework Combining Data-Driven and Model-Based Methodsfor System Remaining Useful Life Prediction," *Applied Soft Computing* 44 (2016): 191–199.
- 3. J. Zeng and Z. Liang, "A Dynamic Predictive Maintenance Approach Using Probabilistic Deep Learning for a Fleet of Multi-Component Systems," *Reliability Engineering & System Safety* 238 (2023): 109456.
- 4. Y. Choo and S.-J. Shin, "Integrating Machine Learning-Based Remaining Useful Life Predictions with Cost-Optimal Block Replacement for Industrial Maintenance," *International Journal of Prognostics and Health Management* 16, no. 1 (2025): 4242.
- 5. Y. Lei, N. Li, S. Gontarz, J. Lin, S. Radkowski, and J. Dybala, "A Model-Based Method for Remaining Useful Life Prediction of Machinery," *IEEE Transactions on Reliability* 65, no. 3 (2016): 1314–1326.
- 6. P. Baraldi, F. Cadini, F. Mangili, and E. Zio, "Model-Based and Data-Driven Prognostics Under Different Available Information," *Probabilistic Engineering Mechanics* 32 (2013): 66–79.
- 7. R. K. Singleton, E. G. Strangas, and S. Aviyente, "Extended Kalman Filtering for Remaining-Useful-Life Estimation of Bearings," *IEEE Transactions on Industrial Electronics* 62, no. 3 (2014): 1781–1790.
- 8. T. Brotherton, G. Jahns, J. Jacobs, and D. Wroblewski, "Prognosis of Faults in Gas Turbine Engines," in *2000 IEEE Aerospace Conference*, Proceedings (Cat. No. 00TH8484) (IEEE, 2000), 163–171.
- 9. Y. Wang, Z. Chen, Y. Zhang, X. Li, and Z. Li, "Remaining Useful Life Prediction of Rolling Bearings Based on the Three-Parameter Weibull Distribution Proportional Hazards Model," *Insight-Non-Destructive Testing and Condition Monitoring* 62, no. 12 (2020): 710–718.
- 10. N. Li, Y. Lei, J. Lin, and S. X. Ding, "An Improved Exponential Model for Predicting Remaining Useful Life of Rolling Element Bearings," *IEEE Transactions on Industrial Electronics* 62, no. 12 (2015): 7762–7773.
- 11. M. Kraus and S. Feuerriegel, "Forecasting Remaining Useful Life: Interpretable Deep Learning Approach via Variational Bayesian Inferences," *Decision Support Systems* 125 (2019): 113100.
- 12. S. Qin, B. X. Wang, T. Tsai, and X. Wang, "The Prediction of Remaining Useful Lifetime for the Weibull k-out-of-n Load-Sharing System," *Reliability Engineering & System Safety* 233 (2023): 109091.

- 13. M. Dong and A. B. Nassif, "Combining Modified Weibull Distribution Models for Power System Reliability Forecast," *IEEE Transactions on Power Systems* 34, no. 2 (2018): 1610–1619.
- 14. C. Su, L. Li, and Z. Wen, "Remaining Useful Life Prediction via a Variational Autoencoder and a Time-Window-Based Sequence Neural Network," *Quality and Reliability Engineering International* 36, no. 5 (2020): 1639–1656.
- 15. W. Ahmad, S. A. Khan, and J. Kim, "A Hybrid Prognostics Technique for Rolling Element Bearings Using Adaptive Predictive Models," *IEEE Transactions on Industrial Electronics* 65, no. 2 (2017): 1577 –1584.
- 16. C. Ferreira and G. Gonçalves, "Remaining Useful Life Prediction and Challenges: A Literature Review on the Use of Machine Learning Methods," *Journal of Manufacturing Systems* 63, no. May (2022): 550 –562.
- 17. X. Du, W. Jia, P. Yu, Y. Shi, and S. Cheng, "A Remaining Useful Life Prediction Method Based on Time-Frequency Images of the Mechanical Vibration Signals," *Measurement* 202 (2022): 111782.
- 18. R. Liu, Q. Zhang, T. Han, et al., "Survey on Foundation Models for Prognostics and Health Management in Industrial Cyber-Physical Systems," *IEEE Transactions on Industrial Cyber-Physical Systems* 2 (2024): 264–280.
- 19. G. A. Susto, A. Schirru, S. Pampuri, S. McLoone, and A. Beghi, "Machine Learning for Predictive Maintenance: A Multiple Classifier Approach," *IEEE Transactions on Industrial Informatics* 11, no. 3 (2014): 812–820.
- 20. T. H. Loutas, D. Roulias, and G. Georgoulas, "Remaining Useful Life Estimation in Rolling Bearings Utilizing Data-Driven Probabilistic E-Support Vectors Regression," *IEEE Transactions on Reliability* 62, no. 4 (2013): 821–832.
- 21. C. Sun, M. Ma, Z. Zhao, S. Tian, R. Yan, and X. Chen, "Deep Transfer Learning Based on Sparse Autoencoder for Remaining Useful Life Prediction of Tool in Manufacturing," *IEEE transactions on industrial informatics* 15, no. 4 (2018): 2416–2425.
- 22. B. C. Wen, M. Q. Xiao, X. qi Wang, X. Zhao, J. feng Li, and X. Chen, "Data-Driven Remaining Useful Life Prediction Based on Domain Adaptation," *PeerJ Computer Science* 7 (2021): e690.
- 23. N. Gebraeel, A. Elwany, and J. Pan, "Residual Life Predictions in the Absence of Prior Degradation Knowledge," *IEEE Transactions on Reliability* 58, no. 1 (2009): 106–117.
- 24. Y. Liu, J. Wen, X. Liu, S. Yang, and G. Wang, "A Comprehensive Overview of Remaining Useful Life Prediction: From Traditional Literature Review to Scientometric Analysis," *Machine Learning with Applications* 21 (2025): 100704.
- 25. Z. Chen, M. Wu, R. Zhao, F. Guretno, R. Yan, and X. Li, "Machine Remaining Useful Life Prediction via an Attention-Based Deep Learning Approach," *IEEE Transactions on Industrial Electronics* 68, no. 3 (2020): 2521–2531.
- 26. H. Liao, W. Zhao, and H. Guo, "Predicting Remaining Useful Life of an Individual Unit Using Proportional Hazards Model and Logistic Regression Model," in *RAMS'06. Annual Reliability and Maintainability Symposium 2006* (IEEE, 2006), 127–132.
- 27. M. You, L. Li, G. Meng, and J. Ni, "Two-Zone Proportional Hazard Model for Equipment Remaining Useful Life Prediction," *Journal of Manufacturing Science and Engineering* 132, no. 4 (2010): 041008.
- 28. Y. Ma, D. Shen, L. Wu, Y. Guan, and H. Zhu, "The Remaining Useful Life Estimation of Lithium-ion Batteries Based on the HKA-ML-ELM Algorithm," *International Journal of Electrochemical Science* 14, no. 8 (2019): 7737–7757.
- 29. M. G. Alfarizi, B. Tajiani, J. Vatn, and S. Yin, "Optimized Random Forest Model for Remaining Useful Life Prediction of Experimental Bearings," *IEEE Transactions on Industrial Informatics* 19, no. 6 (2022): 7771–7779.

- <span id="page-20-0"></span>30. Z. Jin, C. Chen, A. Syntetos, and Y. Liu, "Enhanced Bearing RUL Prediction Based on Dynamic Temporal Attention and Mixed MLP," *Autonomous Intelligent Systems* 5, no. 1 (2025): 2.
- 31. R. Pandit and W. Xie, "Data-Driven Models for Predicting Remaining Useful Life of High-Speed Shaft Bearings in Wind Turbines Using Vibration Signal Analysis and Sparrow Search Algorithm," *Energy Science & Engineering* 11, no. 12 (2023): 4557–4569.
- 32. G. Sateesh Babu, P. Zhao, and X. Li, "Deep Convolutional Neural Network Based Regression Approach for Estimation of Remaining Useful Life," in *International conference on database systems for advanced applications* (Springer, 2016), 214–228.
- 33. W. Li and T. Li, "Comparison of Deep Learning Models for Predictive Maintenance in Industrial Manufacturing Systems Using Sensor Data," *Scientific Reports* 15, no. 1 (2025): 23545.
- 34. A. Malhi, R. Yan, and R. X. Gao, "Prognosis of Defect Propagation Based on Recurrent Neural Networks," *IEEE Transactions on Instrumentation and Measurement* 60, no. 3 (2011): 703–711.
- 35. J. Zhang, P. Wang, R. Yan, and R. X. Gao, "Long Short-Term Memory for Machine Remaining Life Prediction," *Journal of Manufacturing Systems* 48 (2018): 78–86.
- 36. C. Kosma, G. Nikolentzos, N. Xu, and M. Vazirgiannis, "Time Series Forecasting Models Copy the Past: How to Mitigate," in *International Conference on Artificial Neural Networks* (Springer, 2022), 366–378.
- 37. G. Chevillon, "Direct Multi-Step Estimation and Forecasting," *Journal of Economic Surveys* 21, no. 4 (2007): 746–785.
- 38. G. Chevillon and D. F. Hendry, "Non-Parametric Direct Multi-Step Estimation for Forecasting Economic Processes," *International Journal of Forecasting* 21, no. 2 (2005): 201–218.
- 39. I. Remadna, L. S. Terrissa, Z. Al Masry, and N. Zerhouni, "RUL Prediction Using a Fusion of Attention-based Convolutional Variational Autoencoder and Ensemble Learning Classifier," *IEEE Transactions on Reliability* 72, no. 1 (2022): 106–124.
- 40. D. P. Kingma and M. Welling, "An Introduction to Variational Autoencoders," *Foundations and Trends*® *in Machine Learning* 12, no. 4 (2019): 307–392.
- 41. L. Montesdeoca, S. Squires, and M. Niranjan, "Variational Autoencoder for Non-Negative Matrix Factorization With Exogenous Inputs Applied to Financial Data Modelling," in 2019 11th International Symposium on Image and Signal Processing and Analysis (ISPA) (IEEE, 2019), 312–317.
- 42. I. Alarab, S. Prakoonwit, and M. I. Nacer, "Illustrative Discussion of Mc-Dropout in General Dataset: Uncertainty Estimation in Bitcoin," *Neural Process Letters* 53, no. 2 (2021): 1001–1011.
- 43. L. Xue, K. Zhou, and X. Zhang, "Continuous Optimization for Construction of Neural Network-Based Prediction Intervals," *Knowledge-Based Systems* 293 (2024): 111669.
- 44. M. Zamo and P. Naveau, "Estimation of the Continuous Ranked Probability Score With Limited Information and Applications to Ensemble Weather Forecasts," *Mathematical Geosciences* 50, no. 2 (2018): 209–234.
- 45. W. Zha, Y. Liu, Y. Wan, et al., "Forecasting Monthly Gas Field Production Based on the CNN-LSTM Model," *Energy* 260 (2022): 124889.
- 46. A. Mulyadi and E. C. Djamal, "Sunshine Duration Prediction Using 1D Convolutional Neural networks," in 2019 6th International Conference on Instrumentation, Control, and Automation (ICA) (IEEE, 2019), 77–81.
- 47. M. Popescu, V. E. Balas, L. Perescu-Popescu, and N. Mastorakis, "Multilayer Perceptron and Neural Networks," *WSEAS Transactions on Circuits and Systems* 8, no. 7 (2009): 579–588.
- 48. S. K. Pal and S. Mitra, "Multilayer Perceptron, Fuzzy Sets, and Classification," *IEEE Transactions on Neural Networks* 3, no. 5 (1992): 683–697.

- 49. A. He and X. Jin, "Deep Variational Autoencoder Classifier for Intelligent Fault Diagnosis Adaptive to Unseen Fault Categories," *IEEE Transactions on Reliability* 70, no. 4 (2021): 1581–1595.
- 50. Backblaze. "Hard Drive Data and Stats." Available at: https://www.backblaze.com/cloud-storage/resources/hard-drive-test-data(accessed 8 August 2026).
- 51. Backblaze. "Backblaze Drive Stats for 2025." Backblaze Blog, 12 February 2026. Available at: https://www.backblaze.com/blog/backblaze-drive-stats-for-2025/(accessed 8 August 2026).
- 52. Backblaze. "Making Sense of SSD SMART Stats." Backblaze Blog. Available at: https://www.backblaze.com/blog/making-sense-of-ssd-smart-stats/(accessed 8 August 2026).
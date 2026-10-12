# **A physical knowledge-guided and data-driven framework for remaining useful life prediction**

(**The case of turbofan engines**)

Haiyang ZHENG\*, Xinqin GAO\*, Gangcheng JING\*, Xueqi YANG\*, Jiarong QIU\* and Mingshun YANG\* \* School of Mechanical and Precision Instrument Engineering, Xi'an University of Technology, No.5 Jinhua South Road, Xi'an 710048, China E-mail: gaoxinqin@xaut.edu.cn

**Received: 27 August 2025; Revised: 18 October 2025; Accepted: 27 November 2025** 

#### **Abstract**

Accurate prediction of the remaining useful life (RUL) of turbofan engines is crucial for predictive maintenance and operational reliability. Although data-driven methods have shown strong potential in capturing degradation patterns, several practical challenges remain, including the limited integration of physical domain knowledge and the insufficient characterization of prediction uncertainty. To address these issues, this paper proposes a hybrid RUL prediction and uncertainty quantification framework (PhyMix-UQ-RUL) that combines physical knowledge with data-driven approaches. Specifically, a multi-scale dilated convolutional neural network (MsDCNN) is incorporated to extend the WTTE-RNN framework. By introducing a learnable channel-attention weighting mechanism, the model dynamically adjusts the importance of features across different temporal scales, thereby enhancing its ability to extract local features at multiple resolutions. Furthermore, a gated degradation stage regularization (GDSR) module is designed based on the bathtub curve theory, which dynamically constrains the parameter of the Weibull distribution to ensure consistency with physical laws. In addition, a global stability constraint is applied to suppress abrupt fluctuations in the parameter, while a stage-adaptive constraint is introduced to further improve the physical rationality of the model's predictions. Finally, the proposed method is comprehensively validated on the NASA C-MAPSS turbofan engine dataset, and its generalization capability is further evaluated on selected subsets of the N-CMAPSS dataset. Experimental results demonstrate that PhyMix-UQ-RUL delivers competitive prediction accuracy and effectively quantifies prediction uncertainty. Moreover, the proposed framework features a concise architecture and high interpretability, offering valuable support for equipment health assessment and risk management.

*Keywords* : Remaining useful life prediction, Physical knowledge-guided, Uncertainty quantification, Weibull distribution

# **1. Introduction**

Turbofan engines, as a major form of jet propulsion technology, have been widely applied in commercial airliners, cargo aircraft, and certain unmanned aerial vehicles, making them central to modern aviation power systems. Their reliability directly affects flight safety, operational efficiency, and maintenance costs. Because aircraft engines must continuously adapt to variations in altitude, speed, and load during flight, their performance and lifetime characteristics are strongly dependent on operating environments and integration with the airframe. Unexpected failures can result not only in substantial economic losses but also in catastrophic safety incidents (Wang et al., 2020; Zhou et al., 2023; Xu et al., 2022). Preventive maintenance strategies supported by accurate remaining useful life (RUL) prediction have been shown to significantly reduce both maintenance expenses and failure risks (Mitici et al., 2023). Consequently, RUL prediction for turbofan engines has emerged as a central research focus in advanced mechanical systems, providing vital support for safe operation, reliability-oriented design, and maintenance planning in the aviation industry.

RUL prediction approaches are broadly classified into physics-based models, data-driven strategies, and hybrid

![](_page_0_Picture_12.jpeg)

frameworks that seek to integrate domain knowledge with machine learning techniques (Meng and Li, 2019). Physicsbased methods (Chen et al., 2022) involve constructing mathematical models by studying the operational mechanisms of equipment. These methods exhibit strong physical interpretability but rely heavily on precise knowledge of failure mechanisms (Wang et al., 2020), thereby reducing their suitability for deployment in complex industrial settings. Concurrently, the emergence of big data analytics and advances in machine learning have catalyzed the adoption of datadriven methods for RUL estimation. These methods establish mappings between sensor data and equipment health states, eliminating the need for physical models (Xiang et al., 2024), and are capable of capturing subtle changes in equipment degradation processes from high-dimensional and complex data.

Within data-driven RUL prediction, methods primarily rely on machine learning techniques. These approaches can be categorized into traditional machine learning and deep learning (Hong et al., 2019). Industrial monitoring data often suffer from low value density and quality issues (Arunan et al., 2024), which pose challenges to accurate RUL estimation. Traditional machine learning methods, such as shallow neural networks and support vector machines (SVMs), typically exhibit suboptimal prediction performance due to their limited feature extraction capabilities. In contrast, deep learning methods demonstrate powerful spatiotemporal feature learning abilities. In recent years, researchers have proposed various RUL prediction models based on convolutional neural networks (CNNs) (Li et al., 2020), RUL prediction models based on recurrent neural networks (RNNs) (Zhu et al., 2024), and RUL prediction models based on Transformers (Liu et al., 2022), achieving breakthroughs in capturing complex features of equipment degradation processes. Zhang et al. (2022) developed BiGRU-TSAM, a bidirectional gated recurrent unit equipped with a temporal self-attention mechanism. Tian et al. (2023) constructed an RUL prediction framework grounded in long short-term memory (LSTM) networks, incorporating two complementary mechanisms to enhance modeling depth. Zhou et al. (2023) proposed a DCNN–GRU model that combines convolutional feature extraction with temporal modeling for bearing health monitoring.

However, existing data-driven RUL prediction methods still face two major challenges:

- (1) Limited integration of physical knowledge: Data-driven RUL prediction models often use complex structures and numerous parameters to improve accuracy (Liao et al., 2023). This makes the results less transparent and harder to interpret (Zhang et al., 2025). Moreover, it is difficult to include physical knowledge from real-world engineering into these models (de Beaulieu et al., 2024). This reduces their practical use in industry and weakens the reliability of maintenance decisions.
- (2) Lack of uncertainty quantification: Data-driven models are typically based on fixed architectures and cannot provide predictions with confidence intervals. However, knowing the probability distribution of RUL is crucial for assessing risks and planning maintenance (Lin and Li, 2022). Without this, predictions can be overconfident, leading to operational inefficiencies or safety risks (Nemani et al., 2023).

To address these challenges, physics-informed neural networks (PINNs) (Raissi et al., 2019) have been proposed as hybrid models that integrate data-driven methods with physics-based approaches, incorporating physical or prior knowledge into neural networks. Liao et al. (2023) introduced AttnPINN, a hybrid RUL prediction model that merges physics-informed neural networks (PINNs) with a self-attention strategy. Wen et al. (2024) developed a semi-empirical and semi-physical partial differential equation model to simulate battery degradation dynamics. They integrated this into the PINN framework to reveal underlying governing dynamics and enhance information fusion. This ensures that RUL prediction results align more closely with physical laws (Raissi et al., 2019), thereby enhancing model interpretability and prediction accuracy (Wen et al., 2024; Li et al., 2024). However, the multi-physics coupling characteristics of complex systems often make it difficult to construct accurate physical models (Li et al., 2024), which significantly limits their engineering applications.

In terms of uncertainty quantification for RUL prediction results, only a limited number of studies have explored the probability distribution of RUL (Mitici et al., 2023). Lin and Li (2022) proposed a Bayesian deep learning framework that combines uncertainty quantification and calibration. This framework integrates epistemic and aleatoric uncertainties to describe the model's limitations in representing unknown scenarios and observation noise. It also introduces a novel iterative calibration method to refine the uncertainty of RUL predictions. Xu et al. (2025) integrated quantile regression into a deep learning-based RUL prediction model, producing probabilistic results with explicit uncertainty representation. Zhan et al. (2024) designed a multi-distribution fusion-based uncertainty quantification method. This approach generates multiple possible RUL predictions and combines them with weighted distributions to produce a final probabilistic prediction. However, most current RUL prediction models typically output point estimates and rely on post-processing techniques to indirectly quantify uncertainty. This indirect approach not only increases modeling complexity but also has

difficulty in accurately capturing the time-dependent characteristics of RUL distributions.

Motivated by the above limitations, we propose a physics-informed probabilistic degradation modeling framework that integrates prior reliability knowledge with data-driven feature learning. Based on an extended WTTE-RNN (Martinsson, 2016), our model incorporates a multi-scale dilated CNN (MsDCNN), an LSTM network, and a Gated Degradation Stage Regularization (GDSR) mechanism, which enables simultaneous RUL estimation and uncertainty quantification. The main contributions of this study are summarized as follows:

- (1) A unified physics-informed probabilistic framework is established by embedding degradation-stage priors (bathtub-curve knowledge) into WTTE-RNN, thereby bridging physical degradation laws and data-driven reliability modeling.
- (2) An end-to-end probabilistic RUL prediction model is developed by integrating MsDCNN, LSTM, and WTTE-RNN, which directly learns the mapping from degradation signals to lifetime distribution parameters (*α, β*), thereby achieving unified outputs for RUL and uncertainty.
- (3) A Gated Degradation Stage Regularization (GDSR) mechanism is proposed to impose stage-aware constraints on the Weibull shape parameter *β*, enabling the model to adaptively adjust reliability distributions across degradation phases for improved interpretability.
- (4) A Dual Regularization Loss Function is proposed to ensure parameter smoothness and stage coherence, combining a global consistency term and a stage-adaptive constraint to enhance model stability and uncertainty robustness.

# **2. Physical knowledge-guided and data-driven framework for RUL prediction and uncertainty quantification**

The proposed physical knowledge-guided and data-driven RUL prediction framework consists of the following four components:

- (1) Data preprocessing: The collected data are cleaned and organized to ensure its quality and completeness. Outliers are removed to minimize their impact on RUL prediction.
- (2) Shallow feature extraction: An extended sliding window technique is employed to extract features from the preprocessed data. This method captures short-term dependencies in the time series while reducing the dimensionality of the input data, thereby improving modeling efficiency.
- (3) RUL prediction model establishment: The model is based on an improved WTTE-RNN framework that integrates MsDCNN, an LSTM network, and the GDSR module. By incorporating a doubly-regularized WTTE loss function, it predicts Weibull distribution parameters to enable RUL prediction with uncertainty quantification.
- (4) Prediction and evaluation: Test data are fed into the trained model to generate RUL predictions. The model's performance is then comprehensively evaluated using multiple evaluation metrics.

# **2.1 Data preprocessing**

The raw sensor data collected often contain missing values and outliers. Directly inputting outliers into the model may lead to significant errors in RUL predictions, necessitating preprocessing to improve data quality. However, since outliers may also carry important degradation information for RUL prediction, they are retained. The data preprocessing process includes the following steps:

- (1) Redundant Feature Removal: Certain constant-value features in the raw data contribute little to RUL prediction. To ensure data quality, redundant features are removed to reduce the impact of irrelevant information.
- (2) Missing Value Imputation: Missing values are unavoidable during data collection due to equipment limitations or transmission conditions. In this study, missing data are imputed using the K-Nearest Neighbor (KNN) technique, which leverages instance-based learning without assuming specific distributional properties, which makes it a practical choice for handling incomplete datasets.
- (3) Data Normalization: Sensor-based equipment data often contain features with heterogeneous ranges. To harmonize scale disparities across variables, this study adopts the Min–Max scaling technique, transforming all feature values into the [0,1] interval for consistent downstream modeling. This improves the stability of model training.
- (4) RUL labeling: Remaining useful life values are labeled to transform the raw degradation sequences into supervised learning targets. This step provides consistent ground truth for model training and evaluation.

(5) Temporal feature extraction: To capture both short-term fluctuations and long-term degradation trends, a combined sliding–expanding window strategy was employed. This approach integrates the advantages of sliding windows, which emphasize local temporal variations, with expanding windows, which progressively incorporate longer historical information. In this way, temporal features are enriched during the early degradation stage while computational efficiency is maintained for longer sequences. To handle variable-length inputs and preserve a uniform structure for model training, mask processing was applied.

## 2.2 PhyMix-UQ-RUL prediction model

The structure of the proposed PhyMix-UQ-RUL model is shown in Fig. 1. This section provides a detailed description of the key components of the PhyMix-UQ-RUL model, including the WTTE-RNN framework, MsDCNN-based feature extraction, LSTM-based degradation trend modeling, the GDSR model, and an improved WTTE loss function.

![](_page_3_Figure_4.jpeg)

Fig. 1 Structure of the PhyMix-UQ-RUL prediction model

#### 2.2.1 WTTE-RNN framework

WTTE-RNN is a probabilistic prediction framework developed for survival analysis. It models time series data to capture the dynamic patterns of event occurrences (Martinsson, 2016). In equipment reliability analysis, survival analysis focuses on two key aspects: the probability of the equipment remaining operational at a given time *t*, and the hazard rate within a specific time interval. In reliability engineering, the Weibull distribution is widely used to describe equipment lifetime due to its flexible mathematical properties and broad engineering applicability (Guo et al., 2009).

The WTTE-RNN model integrates RNN with survival analysis methods. During training, it maps multivariate sensor time series data to the Weibull distribution parameters of the equipment's RUL, thereby enabling probabilistic RUL modeling. Unlike traditional deterministic prediction methods, this model uses a loss function based on maximum likelihood estimation. The model parameters are optimized by maximizing the log-likelihood function of the training data. This approach not only provides point estimates of RUL but also outputs complete produces full probabilistic information, including confidence intervals and probability density functions. The log-likelihood loss of the WTTE-RNN model, denoted as  $\mathcal{L}_{loglik}$ , is formulated in Eq. (1).

$$\mathcal{L}_{\text{loglik}} = -\sum_{t=0}^{T} \left( u_t \cdot \left[ \exp\left[ \left( \frac{y_t + 1}{\alpha_t} \right)^{\beta_t} - \left( \frac{y_t}{\alpha_t} \right)^{\beta_t} \right] - 1 \right] - \left( \frac{y_t + 1}{\alpha_t} \right)^{\beta_t} \right)$$
 (1)

where T denotes the total length of the time sequence,  $y_t$  represents the length of time from moment t to the occurrence of the event (equipment failure),  $\alpha_t$  is the scale parameter of the Weibull distribution,  $\beta_t$  is the shape parameter of the Weibull distribution,  $u_t$  indicates whether time t is the actual failure time. Specifically,  $u_t = 1$  if t is the actual failure time; otherwise,  $u_t = 0$ .

#### **2.2.2 MsDCNN**

In RUL prediction tasks, equipment degradation processes often exhibit feature patterns across multiple time scales. To achieve multi-scale modeling of the degradation process, a multi-scale dilated convolution module (Yu and Koltun, 2016) is employed. Through parallel multi-kernel convolution and feature fusion, this module can capture representative features across different temporal scales. Let the input sequence be denoted as  $X \in \mathbb{R}^{T \times d}$ . Three different scales of dilated

convolution are applied in parallel, and the output of each convolutional kernel, denoted as  $H_i$ , is defined as shown in Eq. (2).

$$H_{i} = \sigma(K_{i}^{(\gamma_{i})} \cdot X + b_{i}), i \in \{1, 2, 3\}$$
(2)

where X represents the input time series; d denotes the dimensionality of the input features, T indicates the length of the time series,  $K_i^{(\gamma_i)}$  denotes the convolutional kernel with a dilation rate of  $\gamma_i$ , which adjusts the span of the convolutional kernel to capture features at different scales,  $\sigma(\cdot)$  is the activation function, enhancing nonlinear capabilities; and  $b_i$  is the bias term, used to adjust the baseline value of the convolutional output.

A learnable channel attention mechanism is introduced to dynamically balance the importance of features across different scales. This mechanism enables the model to automatically adjust the contribution weights of multi-scale features based on the current input characteristics, t thereby adaptively emphasizing informative features across temporal scales. The calculation method for the channel attention weights  $\alpha_i$  is shown in Eq. (3).

$$\alpha_i = \text{Softmax}(\text{FC}(\text{GAP}(H_i))), i \in \{1, 2, 3\}$$
(3)

where FC(.) represents the fully connected layer,  $GAP(\cdot)$  denotes the global average pooling operation, and  $Softmax(\cdot)$  is used to normalize the weights. The fused multi-scale feature representation, denoted as  $H_{\text{fused}}$ , is obtained as in Eq. (4).

$$H_{\text{fused}} = \sum_{i=1}^{3} \alpha_i \odot H_i \tag{4}$$

where  $\odot$  denotes element-wise multiplication across channels. Through this multi-scale convolution module, the model can comprehensively capture degradation features at different time scales.

### 2.2.3 LSTM

As an improved recurrent architecture, the LSTM introduces gated components that modulate feature propagation and retention across time steps, thereby alleviating the vanishing and exploding gradient problems commonly observed in traditional RNNs. In RUL modeling, the LSTM effectively captures the long-term trends of equipment degradation through multi-step prediction of degradation time series. By integrating LSTM with MsDCNN, local features at different time scales are extracted and provided as enriched input to LSTM, thereby enhancing its ability to model the degradation process. This fusion strategy simultaneously captures both local and global features of the degradation process, significantly improving the accuracy and robustness of RUL prediction.

#### 2.2.4 GDSR module

In equipment reliability and lifetime prediction, the classical bathtub curve theory (Klutke et al., 2003) describes the degradation process, which typically consists of three stages: early failure, mid-term stability, and late-life wear. Each stage exhibits distinct degradation characteristics, which correspond to variations in the Weibull distribution's  $\beta$  parameter at different phases.

To effectively integrate the bathtub curve degradation theory into the RUL prediction model and ensure that the predicted Weibull distribution parameters align with physical degradation patterns, this study proposes a GDSR module-based approach. The GDSR mechanism utilizes a dynamic threshold generator to partition the degradation process into three distinct stages—early failure, mid-term stability, and late-life wear—based on the Degradation Index (DI). The *DI*, defined as the temporal mean of input features, is computed as defined in Eq. (5).

$$DI(t) = \frac{1}{n} \sum_{i=1}^{n} x_i(t)$$
 (5)

where  $x_i(t)$  denotes the value of the *i*-th feature at time t, and n represents the total number of features.

The degradation stages are partitioned into three phases by dynamic thresholds  $\tau_{low}$  and  $\tau_{high}$  :early degradation stage ( $DI(t) < \tau_{low}$ ), mid-term degradation stage ( $\tau_{low} \le DI(t) < \tau_{high}$ ), late degradation stage ( $DI(t) \ge \tau_{high}$ ). The dynamic threshold generator adaptively adjusts these degradation-stage thresholds using a lightweight neural network. Given an input sequence  $X \in \mathbb{R}^{T \times d}$ , it outputs threshold adjustments  $\Delta_{low}$  and  $\Delta_{high}$ , as defined by Eq. (6) and (7), respectively.

$$\Delta_{\text{low}} = \tanh(W_1 \cdot \text{GAP}(X) + b_1) \cdot \delta \tag{6}$$

$$\Delta_{\text{high}} = \tanh(W_2 \cdot \text{GAP}(X) + b_2) \cdot \delta \tag{7}$$

where, GAP(·) represents the global average pooling operation,  $W_1$  and  $W_2$  denote the weight matrices,  $b_1$  and  $b_2$  refer to the bias term, and  $\delta$  indicates the adjustment amplitude constraint factor. The adjusted thresholds, denoted as  $\tau_{\text{low}}$  and  $\tau_{\text{high}}$  are computed as in Eq. (8) and (9).

$$\tau_{\text{low}} = \tau_{\text{low}}^{\text{base}} + \Delta_{\text{low}} \tag{8}$$

$$\tau_{\rm high} = \tau_{\rm high}^{\rm base} + \Delta_{\rm high} \tag{9}$$

where,  $\tau_{\rm low}^{\rm base}$  and  $\tau_{\rm high}^{\rm base}$  represent the initial thresholds.

Based on the degradation stages identified by GDSR, different constraints are applied to the Weibull distribution's  $\beta$  parameter. The constraint ranges for  $\beta$  are determined with reference to classical bathtub curve theory (Klutke et al., 2003; von Hahn and Mechefske, 2022), where:

- early degradation stage:  $\beta_{\text{early}} \in [0.1, 1.0]$
- mid-term stage:  $\beta_{\text{mid}} \in [0.9, 1.1]$
- late stage:  $\beta_{\text{late}} \in [1.0, \beta_{\text{max}}]$

The stage-dependent constraints for the  $\beta$  parameter are formally defined in Eq. (10).

$$\begin{cases} \beta_{\text{early}} = 0.1 + 0.9 \cdot \sigma(\beta_{\text{raw}}) \\ \beta_{\text{mid}} = 0.9 + 0.2 \cdot \sigma(\beta_{\text{raw}}) \\ \beta_{\text{late}} = 1.0 + (\beta_{\text{max}} - 1.0) \cdot \sigma(\beta_{\text{raw}}) \end{cases}$$

$$(10)$$

where,  $\sigma(\cdot)$  denotes the sigmoid activation function, and  $\beta_{\text{raw}}$  represents the raw shape parameter output by the model, and  $\beta_{\text{max}}$  represents the maximum allowable value of  $\beta$ .

#### 2.2.5 Improved WTTE-RNN loss function

To enhance the accuracy and interpretability of the prediction of Weibull distribution parameters, an improved WTTE-RNN loss function is proposed. The composite loss function consists of three components: (1) log-likelihood optimization, (2) global regularization, and (3) stage-dependent regularization.

The log-likelihood loss serves as the foundation, maximizing the observed data to optimize both the shape and scale parameters of the Weibull distribution. Specifically, it ensures the predicted parameters closely match the actual failure time distribution.

The global regularization term constrains both the standard deviation and mean deviation of the shape parameter  $\beta$  to ensure parameter stability. The global regularization term, denoted as  $\mathcal{L}_{\text{beta}}$  elobal, is defined in Eq. (11).

$$\mathcal{L}_{\text{beta\_global}} = \lambda_{\text{global}} \cdot \left( | \operatorname{std}(\beta) - \sigma_{\beta} | + | \operatorname{mean}(\beta) - \mu_{\beta} | \right) \tag{11}$$

where  $\lambda_{\text{global}}$  denotes the regularization coefficient,  $\text{std}(\beta)$  and  $\text{mean}(\beta)$  represent the standard deviation and mean of the predicted  $\beta$  values, respectively,  $\mu_{\beta}$  is the target mean of  $\beta$  (set to 1.5 in this study), and  $\sigma_{\beta}$  is the target standard deviation (set to 0.5), following empirical knowledge from Nelson (1985).

The stage-dependent regularization applies distinct constraints to parameter  $\beta$  based on degradation stage characteristics (early, mid-term, and late stages) identified by the GDSR module. This module generates stage masks through its dynamic threshold generator to classify samples into respective degradation stages. The stage-dependent regularization term, denoted as  $\mathcal{L}_{\text{beta}\_\text{stage}}$ , is given in Eq. (12).

$$\mathcal{L}_{\text{beta\_stage}} = \lambda_{\text{early}} \cdot \text{mean}(\text{ReLU}(\beta - 1.0) \cdot \text{mask}_{\text{early}})$$

$$+\lambda_{\text{mid}} \cdot \text{mean}(|\beta - 1.0| \cdot \text{mask}_{\text{mid}})$$

$$+\lambda_{\text{late}} \cdot \text{mean}(\text{ReLU}(1.0 - \beta) \cdot \text{mask}_{\text{late}})$$
(12)

where  $\lambda_{\text{early}}$ ,  $\lambda_{\text{mid}}$ ,  $\lambda_{\text{late}}$  represent the regularization coefficients for each stage, and  $\text{mask}_{\text{early}}$   $\text{mask}_{\text{mid}}$ ,  $\text{mask}_{\text{late}}$  denote the corresponding stage masks.

Combining these components, the enhanced WTTE-RNN loss function denoted as  $\mathcal{L}_{total}$ , is expressed in Eq. (13).

$$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{lostlik}} + \mathcal{L}_{\text{heta-global}} + \mathcal{L}_{\text{heta-stage}} \tag{13}$$

#### 2.3 Evaluation metrics

In RUL prediction tasks, Root Mean Square Error (RMSE), Mean Absolute Error (MAE), and Coefficient of Determination (R<sup>2</sup>) are commonly used evaluation metrics for models performance. The scoring function is another common evaluation metric for RUL prediction models. To avoid situations where the predicted RUL value is greater than the actual RUL, the scoring function assigns a higher penalty. The calculation method of the scoring function is shown in Eq. (14).

$$Score = \begin{cases} \sum_{i=1}^{N} \left[ exp\left(-\frac{\hat{y}_{i} - y_{i}}{13}\right) - 1 \right], & \hat{y}_{i} < y_{i} \\ \sum_{i=1}^{N} \left[ exp\left(\frac{\hat{y}_{i} - y_{i}}{10}\right) - 1 \right], & \hat{y}_{i} \ge y_{i} \end{cases}$$

$$(14)$$

where, N denotes the number of samples,  $y_i$  denotes the actual values, and  $\hat{y}_i$  denotes the predicted values.

## 3. Case study

To assess the effectiveness of PhyMix-UQ-RUL, we conducted extensive experiments using the C-MAPSS turbofan engine dataset (Saxena et al., 2008). Model evaluations were performed on a computing platform equipped with an NVIDIA Tesla P100 GPU with 16GB of memory. The implementation was implemented in Python 3.10 with TensorFlow 3.2 serving as the primary deep learning framework.

#### 3.1 Data preprocessing for C-MAPSS

Within the C-MAPSS dataset, turbofan engine health deterioration is simulated under a range of operational environments and fault types, comprising four subsets. Each subset consists of 26-dimensional multivariate time-series data. To reduce the input dimensionality, redundant variables with limited contribution to RUL prediction were eliminated, and 14 sensor signals with indices [2,3,4,7,8,9,11,12,13,14,15,17,20,21] were selected as input features for the model, consistent with previous research (Song et al., 2021). Since the C-MAPSS dataset contains simulated data without

missing values, no imputation was required. However, due to differences in value ranges among features, Min–Max normalization was applied to rescale all variables into the [0,1] interval, thereby mitigating scale disparities and improving training stability.

After normalization, each sample's corresponding RUL was labeled to provide supervised targets for model training. In this study, a piecewise linear function was employed for RUL labeling (Liu et al., 2022; Song et al., 2021), with the maximum engine lifespan truncated at 125 cycles. Engines exceeding this threshold were labeled as 125, while those with lifespans shorter than 125 cycles were labeled according to their actual RUL values. This labeling strategy ensures consistency with prior work and prevents extremely long lifespans from biasing the training process.

To capture temporal dependencies in the degradation sequences, an extended sliding window strategy was employed. The initial window length was set to 40 cycles, with a maximum window size of 125 cycles to cover the full operational lifecycle. Since different samples have varying sequence lengths, masking was introduced to maintain a consistent input structure across all samples. A padding value of -999, which is unlikely to occur in real sensor data, was used to distinguish between actual signal values and padded positions. This design allows the model to effectively learn from both short-term fluctuations and long-term degradation trends while enhancing robustness to variable-length sequences.

### 3.2 Prediction results and analysis

The official C-MAPSS dataset provides only training and test sets. In this study, 20% of the training set was split by engine unit ID and reserved as a validation set. This validation subset was not used for parameter updates and was used exclusively for monitoring the training process and tuning hyperparameters. Key hyperparameters were optimized using Keras Tuner, and the optimized hyperparameter settings are summarized in Table 1. The training process was limited to 150 epochs, with an early stopping strategy applied. Training was terminated if the validation performance did not improve for 10 consecutive epochs, thereby reducing the risk of overfitting. The Adam optimizer was used throughout training, combined with an adaptive learning rate scheduling strategy based on validation performance. Specifically, the learning rate was reduced by a factor of 0.5 if no improvement was observed for two consecutive epochs, with a minimum learning rate set to  $1 \times 10^{-6}$ , to enhance convergence stability and training efficiency. The batch size was fixed at 256, with best-model checkpointing saving and gradient clipping enabled. To further regularize the model, L2 weight decay, batch normalization, and dropout were incorporated to mitigate overfitting.

| Table 1 Hyperparameters for the training process. |           |  |  |  |  |
|---------------------------------------------------|-----------|--|--|--|--|
| Hyperparameters                                   | Value     |  |  |  |  |
| CNN Filters                                       | 160       |  |  |  |  |
| Kernel Sizes                                      | [3, 7, 7] |  |  |  |  |
| Dilation Rate                                     | [2,2,1]   |  |  |  |  |
| Activation (CNN)                                  | Linear    |  |  |  |  |
| LSTM Units                                        | 256       |  |  |  |  |
| Activation (LSTM)                                 | Tanh      |  |  |  |  |
| Dropout Rate                                      | 0.35      |  |  |  |  |
| Learning Rate                                     | 0.0005    |  |  |  |  |

Table 1 Hyperparameters for the training process

The loss function consists of the negative log-likelihood term from WTTE-RNN, a physics-gated constraint, and dual regularization terms. The regularization coefficients  $\lambda_{global} = 1.0 \times 10^{-3}$ ,  $\lambda_{early} = 5.0 \times 10^{-4}$ ,  $\lambda_{mid} = 1.0 \times 10^{-3}$ , and  $\lambda_{late} = 1.5 \times 10^{-3}$  were uniformly set to enforce temporal smoothness and stage consistency. Their values were determined through grid search, with the candidate set  $\{5 \times 10^{-4}, 1 \times 10^{-3}, 1.5 \times 10^{-3}, 2 \times 10^{-3}\}$ , following the principle that later-stage constraints carry greater weight than early-stage ones, reflecting the accelerated wear in the bathtub curve's final phase. For comparability, these coefficients were kept identical across FD001–FD004 and all baseline models. The training, validation, and test loss curves for the four datasets are shown in Fig. 2, all exhibiting consistent convergence trends without divergence or signs of overfitting.

To mitigate experimental randomness, all tests were repeated 10 times under a fixed random seed, and the average results were reported as the final predictions. Table 2 summarizes the model's predictive performance across the four datasets. On FD001 (single operating condition/single fault mode), the model achieved its best performance with

RMSE = 13.73 and Score = 234, indicating high accuracy in relatively simple scenarios. On FD002 and FD003, the RMSE values were 14.50 and 14.54, respectively, demonstrating that the model maintained strong adaptability under multiple fault modes. On FD004, the RMSE increased to 17.14 and the Score to 1148, reflecting the compounded challenges introduced by the interaction between operating conditions and fault modes.

![](_page_8_Figure_2.jpeg)

Fig. 2 Training, validation, and test loss curves for the four datasets

| Data set | RMSE  | MAE   | R2   | Score |
|----------|-------|-------|------|-------|
| FD001    | 13.73 | 10.01 | 0.88 | 234   |
| FD002    | 14.50 | 11.19 | 0.89 | 689   |
| FD003    | 14.54 | 10.92 | 0.86 | 385   |
| FD004    | 17.14 | 13.49 | 0.84 | 1148  |
| Average  | 14.48 | 11.40 | 0.87 | 614   |

Table 2 Performance of PhyMix-UQ-RUL on C-MAPSS dataset.

To further evaluate the computational efficiency of the model, two commonly used baseline methods were selected for comparison: WTTE-RNN and CNN-WTTE-RNN, the latter incorporating convolutional structures to enhance feature extraction. As shown in Table 3, the average execution time per epoch across the four sub-datasets indicates that the proposed model requires slightly higher training time than WTTE-RNN and CNN-WTTE-RNN. This additional cost is primarily attributed to the introduction of the physics-informed constraints and uncertainty quantification modules. Table 4 presents a comparative analysis of predictive performance, where the proposed model achieves lower RMSE and Score on FD001–FD004, with an average RMSE of 14.48 and an average Score of 614. These results correspond to reductions of approximately 14% and over 30%, respectively, compared with the CNN-WTTE-RNN model. Overall, the proposed method appears to strike a reasonable balance between computational efficiency and predictive accuracy.

Table 3 Average execution time per epoch of different models on the C-MAPSS subsets.

| Model        | FD001 | FD002 | FD003 | FD004 |
|--------------|-------|-------|-------|-------|
| WTTE-RNN     | 3.86  | 10.06 | 4.76  | 11.75 |
| CNN-WTTE-RNN | 4.05  | 10.50 | 5.03  | 12.49 |
| Proposed     | 4.71  | 12.10 | 5.80  | 14.17 |

|               | FD001 |       | FD002 |       | FD003 |       | FD004 | Score<br>6380 | Average |       |
|---------------|-------|-------|-------|-------|-------|-------|-------|---------------|---------|-------|
| Model         | RMSE  | Score | RMSE  | Score | RMSE  | Score | RMSE  |               | RMSE    | Score |
| WTTE-RNN      | 14.44 | 255   | 23.35 | 2010  | 15.87 | 567   | 25.61 |               | 19.82   | 3053  |
| CNN-WTTE-RNN  | 14.02 | 238   | 15.02 | 702   | 14.93 | 427   | 21.25 | 2341          | 16.81   | 927   |
| PhyMix-UQ-RUL | 13.73 | 234   | 14.50 | 689   | 14.54 | 385   | 17.14 | 1148          | 14.48   | 614   |

Table 4 RUL prediction performance comparison.

# **3.3 Discussion**

To validate the predictive capability and applicability of the proposed model, this study conducts an in-depth discussion of the prediction results from multiple perspectives. As illustrated in Fig. 3, the engine IDs were reordered according to the true RUL values to improve clarity of comparison. The proposed model's predicted RUL values generally exhibit strong agreement with ground-truth labels across the test subsets, with the correspondence tending to be stronger in late-stage predictions when actual RUL values approach zero. This indicates that the model achieves relatively high prediction accuracy during the equipment's end-of-life stage, which may provide useful guidance for maintenance planning and failure prevention.

Furthermore, it is observed that units with smaller IDs (corresponding to larger RUL values and the early degradation stage) tend to show relatively larger discrepancies between predicted and true RUL values. This phenomenon is consistent with prior studies (Liu et al., 2025), which indicate that during the early stage of degradation, state parameters change only slightly, making it challenging for prediction models to detect degradation signals. As the degradation progresses and the RUL decreases, the signals become more evident, enabling the model to capture the degradation trend more effectively and improve prediction accuracy.

![](_page_9_Figure_6.jpeg)

Fig. 3 Prediction results of the PhyMix-UQ-RUL model on the test set

To further validate the rationale for setting the mean and variance of the *β* parameter (1.5 and 0.5, respectively), a sensitivity analysis was conducted on the FD002 subset. Table 5 summarizes the average RMSE and Score values over 10 repeated runs for different combinations of and . The analysis shows that the predictive accuracy remains robust across different parameter settings. The results indicate that the model performance remains stable across different parameter settings, with = 1.5 and = 0.5 yielding the lowest RMSE and one of the lowest Score values.

| Table 5 Sensitivity analysis of β regularization parameters on FD002 dataset. |  |  |
|-------------------------------------------------------------------------------|--|--|
|                                                                               |  |  |

|     | 1.0   | 1.0   | 1.0   | 1.5   | 1.5   | 1.5   | 2.0   | 2.0   | 2.0   |
|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
|     | 0.2   | 0.5   | 0.8   | 0.2   | 0.5   | 0.8   | 0.2   | 0.5   | 0.8   |
| RMSE  | 15.11 | 15.17 | 14.98 | 15.25 | 14.50 | 14.91 | 15.12 | 14.99 | 15.61 |
| Score | 734   | 739   | 754   | 775   | 689   | 771   | 738   | 769   | 791   |

Figure 4 shows the two-dimensional density plots of predicted RUL parameters *α* and *β* for equipment in all four test subsets. When *α* values are small, *β* values are typically low, indicating higher confidence and stronger consistency in model predictions as equipment approaches failure. With increasing *α* values (corresponding to longer time before failure), *β* values gradually rise, showing a trend of increasing prediction uncertainty as equipment lifetime extends. This global distribution pattern reflects the model's prediction characteristics at different stages of the equipment lifecycle.

![](_page_10_Figure_5.jpeg)

Fig. 4 Two-dimensional density plots of predicted α and β parameters across all four test subsets.

To further highlight the model's advantages in uncertainty quantification, an additional case study was conducted on Unit 42 from the FD002 test set, which involves six different operating conditions and thus represents a more complex and challenging scenario. Unit 42 was selected because it contains a relatively large number of samples and its true RUL spans a wide range across different degradation stages. Figure 5 illustrates the evolution of the predicted Weibull distributions at different time points for Unit 42. During the initial operation phase, the RUL predictions exhibited substantial uncertainty, reflected in relatively flat probability density function (PDF) curves. As the equipment approached its actual failure time, the PDF curves became progressively steeper, with predicted RUL values decreasing and prediction variances narrowing, indicating improved stability and accuracy.

![](_page_11_Figure_2.jpeg)

Fig. 5 Dynamic changes of Weibull PDF for Unit 42 in FD002 test set

Figure 6 presents the prediction results and the corresponding [10%, 90%] prediction intervals (PIs) for Unit 42 at each time step. At the beginning of operation, the PIs are relatively wide, with the 90% PI width reaching about 117 cycles, reflecting higher uncertainty in early-life predictions. As the equipment approaches failure, the intervals narrow to around 33 cycles, representing a 72.2% reduction in width. This behavior is consistent with expectations in prognostics, where accumulating degradation data allows more stable predictions. In this case, the last sample's true RUL (27 cycles) was contained within the predicted 90% PI [13.0, 45.5], indicating that the interval remained valid while becoming narrower. These results suggest that the narrowing of the prediction intervals provides useful guidance for maintenance planning, helping maintenance teams arrange inspections within a clearer window and reducing the risk of premature or delayed interventions.

![](_page_11_Figure_5.jpeg)

Fig. 6 RUL predictions with confidence intervals for Unit 42 at different time steps

Figure 7 shows the survival curves of Test Unit 42 in the FD002 dataset, including all survival curves generated from multiple sets of parameters *α* and *β* predicted by the model, as well as the typical survival curve generated based on the median values of *α* and *β*. This figure visually demonstrates the equipment's remaining survival probability, providing reference for maintenance threshold selection and decision-making. For example, the median survival curve shows that in the 0 to 60 time range, Test Unit 42 has approximately an 80% probability of not failing.

![](_page_12_Figure_1.jpeg)

Fig. 7 Survival curves for Test Unit 42 in FD002 dataset

# **3.4 Comparisons**

Table 6 compares the performance of the proposed RUL prediction model with several representative state-of-theart methods across the four C-MAPSS subsets. The RMSE and Score values are directly taken from the corresponding published papers, ensuring consistency with prior studies. As shown in Table 6, the proposed model achieves lower RMSE and Score values on FD002 and FD004, which are the more challenging subsets with multiple operating conditions and fault modes. For example, on FD004 the RMSE of our model is reduced by about 22.9% compared with MS-DCNN, and the Score is lower by more than 68.2% relative to BiGRU-TSAM. On FD002, the RMSE is about 15.1% lower than CNN-Transform. Overall, the outcomes imply that the proposed framework achieves a modest advantage and sustains reasonable predictive capability in multi-condition environments.

| Table 6 Comparison of RMSE and score between the proposed RUL prediction model and other models on four subsets. |  |
|------------------------------------------------------------------------------------------------------------------|--|
|                                                                                                                  |  |

|                                    | FD001 |       | FD002 |       | FD003 |       | FD004 |       | Average |       |
|------------------------------------|-------|-------|-------|-------|-------|-------|-------|-------|---------|-------|
| Method                             | RMSE  | Score | RMSE  | Score | RMSE  | Score | RMSE  | Score | RMSE    | Score |
| MS-DCNN (Li et al., 2020)          | 11.44 | 196   | 19.35 | 3747  | 11.67 | 241   | 22.22 | 4844  | 16.17   | 2257  |
| BiGRU-TSAM (Zhang et al., 2022)    | 12.56 | 213   | 18.94 | 2264  | 12.45 | 232   | 20.47 | 3610  | 16.11   | 1580  |
| CNN-Transform (Liu et al., 2022)   | 12.25 | 198   | 17.08 | 1575  | 13.39 | 290   | 19.86 | 1741  | 15.65   | 961   |
| MSIDSN (Zhao et al., 2023)         | 11.74 | 196   | 18.26 | 3747  | 12.04 | 242   | 22.48 | 4844  | 16.13   | 2257  |
| Attention-LSTM (Tian et al., 2023) | 12.10 | 207   | 16.90 | 1267  | 12.14 | 248   | 21.93 | 3310  | 15.77   | 1258  |
| BiLSTM (Zhu et al., 2024)          | 12.44 | 249   | 15.55 | 1215  | 12.22 | 258   | 18.28 | 1838  | 14.62   | 890   |
| CATA-TCN (Lin et al., 2024)        | 12.80 | 234   | 17.61 | 1361  | 13.16 | 290   | 21.04 | 2303  | 16.15   | 1047  |
| Proposed                           | 13.73 | 234   | 14.50 | 689   | 14.54 | 385   | 17.14 | 1148  | 14.48   | 614   |

# **3.5 Generalization capability validation of the model**

To further validate the generalization capability of the proposed model, experiments were conducted on the N-CMAPSS (Arias Chao et al., 2021) dataset. As an extended version of the C-MAPSS dataset, N-CMAPSS provides a more comprehensive simulation of flight processes, including climb, cruise, and descent phases. The dataset comprises eight subsets, each containing five categories of data: scenario descriptors, sensor measurements, virtual sensor data, model health parameters, and auxiliary information.

In this study, subset DS02 was selected for validation, with fourteen sensor measurements adopted as input features for the RUL prediction model. DS02 includes run-to-failure trajectories of nine engine units. Following the configuration in prior work (Wang et al., 2025), six units (2, 5, 10, 16, 18, 20) were allocated for training, while the remaining three units (11, 14, 15) were reserved for testing. Notably, N-CMAPSS offers richer timestamp information compared to C-MAPSS. To reduce computational costs during training and evaluation, the raw data was downsampled at an interval of 100. Additionally, the maximum RUL was capped at 88.

Table 7 compares the evaluation metrics of the proposed RUL prediction model with state-of-the-art methods on test units 11, 14, and 15. The proposed PhyMix-UQ-RUL achieved the lowest RMSE and Score on Unit 11, demonstrating superior performance. Although its RMSE on Units 14 and 15 slightly exceeded those of fullyconnected spatial-temporal graph (FC-STGNN) and hierarchical attention graph convolutional network (HAGCN), respectively, PhyMix-UQ-RUL still attained the lowest Score across all test units. This result highlights the model's effectiveness and generalization capability.

| Table 7 Comparison of RUL prediction performance of different models on the N-CMAPSS dataset. |
|-----------------------------------------------------------------------------------------------|
|-----------------------------------------------------------------------------------------------|

|                              |      | Unit 11 | Unit 14 |       | Unit 15 |       |
|------------------------------|------|---------|---------|-------|---------|-------|
| Models                       | RMSE | Score   | RMSE    | Score | RMSE    | Score |
| RGCNU (Zhu et al., 2023)     | 9.61 | 9222    | 11.84   | 2714  | 9.70    | 5524  |
| STGNN (Liu et al., 2023)     | 8.72 | 8017    | 11.45   | 2673  | 8.26    | 4392  |
| FC-STGNN (Wang et al., 2024) | 5.06 | 3211    | 8.48    | 1586  | 4.96    | 1904  |
| HAGCN (Li et al., 2021)      | 5.45 | 3593    | 8.95    | 1693  | 4.56    | 1718  |
| PhyMix-UQ-RUL                | 4.35 | 2891    | 8.85    | 1384  | 4.90    | 1581  |

# **4. Conclusion**

This paper presents an enhanced WTTE-RNN framework that integrates MsDCNN, GDSR, and dual-phase regularization for RUL prediction and uncertainty quantification. The MsDCNN module captures local degradation features at multiple temporal scales, while a learnable channel attention mechanism adaptively adjusts feature importance to improve fusion quality. Stage-aware constraints are applied to the Weibull shape parameter () via the GDSR module, aiming to improve alignment with typical degradation patterns. Dual-phase regularization is introduced to mitigate parameter fluctuations and promote physical consistency. Experimental results on the C-MAPSS dataset indicate that the proposed PhyMix-UQ-RUL model achieves competitive RMSE and Score values, with promising robustness under complex multi-failure conditions. Its generalization capability was preliminarily explored on selected subsets of the N-CMAPSS dataset, suggesting potential adaptability to varying operational scenarios. The model also features a concise architecture and interpretable structure, contributing to uncertainty-aware RUL estimation and offering useful references for maintenance planning.

This study focuses on the degradation prediction of aero-engine components, where the proposed PhyMix-UQ-RUL model is particularly applicable to critical rotating machinery with continuous monitoring data and monotonic degradation patterns, such as aero-engines and gas turbines. The framework captures multi-stage degradation behavior and provides reliable uncertainty quantification. However, its performance may be less effective for systems with discontinuous sensing or highly dynamic operating conditions. For future work, we plan to extend the applicability of the model to other types of electromechanical equipment and more complex industrial environments, incorporating finergrained physical failure mechanisms to further enhance interpretability and prediction accuracy.

# **Acknowledgments**

This research was supported by the Science and Technology Plan Project of Yulin City, China (Grant No. 2023-CXY-206), the Key Research and Development Projects of Shaanxi Province (Grant No. 2024CY2-GJHX-16), and the Doctoral Dissertation Innovation Fund of Xi'an University of Technology (Grant No. BC202603).

# **References**

Arunan, A., Qin, Y., Li, X. and Yuen, C., A federated learning-based industrial health prognostics for heterogeneous edge devices using matched feature extraction, IEEE Transactions on Automation Science and Engineering[, Vol.21, No.3](https://doi.org/10.1109/TASE.2023.3274648)  [\(2024\), pp.3065–3079, DOI:10.1109/TASE.2023.3274648.](https://doi.org/10.1109/TASE.2023.3274648)

Arias Chao, M., Kulkarni, C., Goebel, K. and Fink, O., Aircraft engine run-to-failure dataset under real flight conditions for prognostics and diagnostics, Data, Vol.6, No.1 (2021), p.5, DOI:10.3390/data6010005.

- Chen, J., Shen, C., Jing, Z., Wu, Y. and Chen, R., Remaining useful life prediction of aircraft flap control system with mode transition, AIAA Journal, Vol.60, No.2 (2022), pp.401–412, DOI:10.2514/1.j060828.
- de Beaulieu, M. H., Jha, M. S., Garnier, H. and Cerbah, F., Remaining useful life prediction based on physics–informed data augmentation, Reliability Engineering & System Safety, Vol.252 (2024), p.110451, DOI:10.1016/j.ress.2024.110451.
- Guo, H., Watson, S., Tavner, P. and Xiang, J., Reliability analysis for wind turbines with incomplete failure data collected from after the date of initial installation, Reliability Engineering & System Safety, Vol.94, No.6 (2009), pp.1057– 1063, DOI[:10.1016/j.ress.2008.12.004.](https://doi.org/10.1016/j.ress.2008.12.004)
- Hong, P., Hu, C., Si, X., Zhang, J., Pang, Z. and Zhang, P., Review of machine learning based remaining useful life prediction methods for equipment. Journal of Mechanical Engineering, [Vol.55, No.8 \(2019\), pp.1–13,](https://doi.org/10.3901/jme.2019.08.001)  [DOI:10.3901/jme.2019.08.001.](https://doi.org/10.3901/jme.2019.08.001)
- Klutke, G. A., Kiessler, P. C. and Wortman, M. A., A critical look at the bathtub curve, IEEE Transactions on Reliability, Vol.52, No.1 (2003), pp.125–129, DOI[:10.1109/TR.2002.804492.](https://doi.org/10.1109/TR.2002.804492)
- Li, H., Zhang, Z., Li, T. and Si, X., A review on physics-informed data-driven remaining useful life prediction: Challenges and opportunities, Mechanical Systems and Signal Processing, [Vol.209 \(2024\), p.111120,](https://doi.org/10.1016/j.ymssp.2024.111120)  [DOI:10.1016/j.ymssp.2024.111120.](https://doi.org/10.1016/j.ymssp.2024.111120)
- Li, H., Zhao, W., Zhang, Y. and Zio, E., Remaining useful life prediction using multi-scale deep convolutional neural network, Applied Soft Computing, Vol.89 (2020), DOI:10.1016/j.asoc.2020.106113.
- Li, T., Zhao, Z., Sun, C., Yan, R. and Chen, X., Hierarchical attention graph convolutional network to fuse multi-sensor signals for remaining useful life prediction, Reliability Engineering & System Safety, Vol.215 (2021), p.107878, DOI:10.1016/j.ress.2021.107878.
- Liao, X., Chen, S., Wen, P. and Zhao, S., Remaining useful life with self-attention assisted physics-informed neural network, Advanced Engineering Informatics, Vol.58 (2023), p.102195, DOI:10.1016/j.aei.2023.102195.
- Lin, L., Wu, J., Fu, S., Zhang, S., Tong, C. and Zu, L., Channel attention and temporal attention based temporal convolutional network: A dual attention framework for remaining useful life prediction of the aircraft engines, Advanced Engineering Informatics, Vol.60 (2024), p.102372, DOI[:10.1016/j.aei.2024.102372.](https://doi.org/10.1016/j.aei.2024.102372)
- Lin, Y. H. and Li, G. H., A Bayesian Deep Learning Framework for RUL Prediction Incorporating Uncertainty Quantification and Calibration, IEEE Transactions on Industrial Informatics, Vol.18, No.10 (2022), pp.7274–7284, DOI:10.1109/TII.2022.3156965.
- Liu, J., Wang, X., Xie, F., Wu, S. and Li, D., Condition monitoring of wind turbines with the implementation of spatiotemporal graph neural network, Engineering Applications of Artificial Intelligence, Vol.121 (2023), p.106000, DOI:10.1016/j.engappai.2023.106000.
- Liu, L., Song, X. and Zhou, Z., Aircraft engine remaining useful life estimation via a double attention-based data-driven architecture, Reliability Engineering & System Safety, Vol.221 (2022), p.108330, DOI[:10.1016/j.ress.2022.108330.](https://doi.org/10.1016/j.ress.2022.108330)
- Liu, M., Zheng, D., Gou, P., Zhang, J., Lai, Z. and Chen, D., A two-phase equipment remaining useful life prediction model with sequence-feature attention mechanism, IEEE Transactions on Instrumentation and Measurement, Vol.74 (2025), pp.1–14, DOI:10.1109/TIM.2025.3576953.
- Martinsson, E., Wtte-rnn: Weibull time to event recurrent neural network, Chalmers University of Technology & University of Gothenburg (2016).
- Meng, H. and Li, Y., A review on prognostics and health management (PHM) methods of lithium-ion batteries, Renewable and Sustainable Energy Reviews, Vol.116 (2019), p.109405, DOI:10.1016/j.rser.2019.109405.
- Mitici, M., de Pater, I., Barros, A. and Zeng, Z., Dynamic predictive maintenance for multiple components using datadriven probabilistic RUL prognostics: The case of turbofan engines, Reliability Engineering & System Safety, Vol.234 (2023), p.109199, DOI[:10.1016/j.ress.2023.109199.](https://doi.org/10.1016/j.ress.2023.109199)
- Nelson, W., Weibull Analysis of Reliability Data with Few or No Failures, Journal of Quality Technology, Vol.17, No.3 (1985), pp.140–146, DOI[:10.1080/00224065.1985.11978953.](https://doi.org/10.1080/00224065.1985.11978953)
- Nemani, V., Biggio, L., Huan, X., Hu, Z., Fink, O., Tran, A., Wang, Y., Zhang, X. and Hu, C., Uncertainty quantification in machine learning for engineering design and health prognostics: A tutorial, Mechanical Systems and Signal Processing, Vol.205 (2023), p.110796, DOI:10.1016/j.ymssp.2023.110796.
- Raissi, M., Perdikaris, P. and Karniadakis, G.E., Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations, Journal of Computational

- Physics, [Vol.378 \(2019\), pp.686–707, DOI:10.1016/j.jcp.2018.10.045.](https://doi.org/10.1016/j.jcp.2018.10.045)
- Saxena, A., Goebel, K., Simon, D. and Eklund, N., Damage propagation modeling for aircraft engine run-to-failure simulation, Proceedings of the International Conference on Prognostics and Health Management (PHM) (2008), pp.1–9, DOI:10.1109/PHM.2008.4711414.
- Song, Y., Gao, S., Li, Y., Jia, L., Li, Q. and Pang, F., Distributed attention-based temporal convolutional network for remaining useful life prediction, IEEE Internet of Things Journal, Vol.8, No.12 (2021), pp.9594–9602, DOI[:10.1109/JIOT.2020.3004452.](https://doi.org/10.1109/JIOT.2020.3004452)
- von Hahn, T. and Mechefske, C.K., Knowledge Informed Machine Learning using a Weibull-based Loss Function, Journal of Prognostics and Health Management, Vol.2, No.1 (2022), pp.9–44, DOI:10.22215/jphm.v2i1.3162.
- Wang, B., Lei, Y., Li, N. and Li, N., A hybrid prognostics approach for estimating remaining useful life of rolling element bearings, IEEE Transactions on Reliability, Vol.69, No.1 (2020), pp.401–412, DOI[:10.1109/TR.2018.2882682.](https://doi.org/10.1109/TR.2018.2882682)
- Wang, Y., Wu, M., Li, X., Xie, L. and Chen, Z., A survey on graph neural networks for remaining useful life prediction: Methodologies, evaluation and future trends, Mechanical Systems and Signal Processing, Vol.229 (2025), p.112449, DOI:10.1016/j.ymssp.2025.112449.
- Wang, Y., Xu, Y., Yang, J., Wu, M., Li, X., Xie, L. and Chen, Z., Fully-connected spatial-temporal graph for multivariate time-series data, Proceedings of the AAAI Conference on Artificial Intelligence, Vol.38, No.14 (2024), pp.15715– 15724, DOI:10.1609/aaai.v38i14.29500.
- Wen, P., Ye, Z.S., Li, Y., Chen, S., Xie, P. and Zhao, S., Physics-informed neural networks for prognostics and health management of lithium-ion batteries, IEEE Transactions on Intelligent Vehicles[, Vol.9, No.1 \(2024\), pp.2276–2289,](https://doi.org/10.1109/TIV.2023.3315548)  [DOI:10.1109/TIV.2023.3315548.](https://doi.org/10.1109/TIV.2023.3315548)
- Xiang, F., Zhang, Y., Zhang, S., Wang, Z., Qiu, L. and Choi, J.H., Bayesian gated-transformer model for risk-aware prediction of aero-engine remaining useful life, Expert Systems with Applications, Vol.238 (2024), p.121859, DOI:10.1016/j.eswa.2023.121859.
- Xu, E., Li, Y., Han, Z., Du, J., Yang, M. and Gao, X., A method for predicting the remaining life of equipment based on WTTE-CNN-LSTM. Journal of Advanced Mechanical Design, Systems, and Manufacturing, Vol.16, No.1 (2022), p.2022jamdsm0001, DOI:10.1299/jamdsm.2022jamdsm0001.
- Xu, Q., Wang, Z., Jiang, C. and Jing, Z., Data-driven predictive maintenance framework considering the multi-source information fusion and uncertainty in remaining useful life prediction, Knowledge-Based Systems, Vol.303 (2025), p.112408, DOI[:10.1016/j.knosys.2024.112408.](https://doi.org/10.1016/j.knosys.2024.112408)
- Yu, F. and Koltun, V., Multi-scale context aggregation by dilated convolutions, arXiv (2016), [DOI:10.48550/arXiv.1511.07122.](https://doi.org/10.48550/arXiv.1511.07122)
- Zhan, Y., Kong, Z., Wang, Z., Jin, X. and Xu, Z., Remaining useful life prediction with uncertainty quantification based on multi-distribution fusion structure, Reliability Engineering & System Safety, Vol.251 (2024), p.110383, DOI[:10.1016/j.ress.2024.110383.](https://doi.org/10.1016/j.ress.2024.110383)
- Zhang, J., Jiang, Y., Wu, S., Li, X., Luo, H. and Yin, S., Prediction of remaining useful life based on bidirectional gated recurrent unit with temporal self-attention mechanism, Reliability Engineering & System Safety, Vol.221 (2022), p.108297, DOI:10.1016/j.ress.2021.108297.
- Zhao, K., Jia, Z., Jia, F. and Shao, H., Multi-scale integrated deep self-attention network for predicting remaining useful life of aero-engine, Engineering Applications of Artificial Intelligence, Vol.120 (2023), p.105860, DOI:10.1016/j.engappai.2023.105860.
- Zhou, Z., Wang, H., Li, Z. and Chen, W., Fault diagnosis of rolling bearing based on deep convolutional neural network and gated recurrent unit, Journal of Advanced Mechanical Design, Systems, and Manufacturing, Vol.17, No.2 (2023), p.2023jamdsm0017, DOI:10.1299/jamdsm.2023jamdsm0017.
- Zhu, Q., Xiong, Q., Yang, Z. and Yu, Y., RGCNU: Recurrent Graph Convolutional Network With Uncertainty Estimation for Remaining Useful Life Prediction, IEEE/CAA Journal of Automatica Sinica, Vol.10, No.7 (2023), pp.1640– 1642, DOI:10.1109/JAS.2023.123369.
- Zhu, Q., Zhou, Z., Li, Y. and Yan, R., Contrastive BiLSTM-enabled Health Representation Learning for Remaining Useful Life Prediction, Reliability Engineering & System Safety, Vol.249 (2024), p.110210, DOI[:10.1016/j.ress.2024.110210.](https://doi.org/10.1016/j.ress.2024.110210)
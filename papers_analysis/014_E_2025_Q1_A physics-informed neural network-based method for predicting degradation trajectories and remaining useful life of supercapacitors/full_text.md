Contents lists available at [ScienceDirect](www.sciencedirect.com/science/journal/27731537)

# Green Energy and Intelligent Transportation

journal homepage: <www.journals.elsevier.com/green-energy-and-intelligent-transportation>

![](_page_0_Picture_5.jpeg)

# Full length article

# A physics-informed neural network-based method for predicting degradation trajectories and remaining useful life of supercapacitors

![](_page_0_Picture_8.jpeg)

Lixin E [a](#page-0-0) , Jun Wang [a](#page-0-0) , Ruixin Yang [a](#page-0-0),\* , Chenxu Wang [a](#page-0-0) , Hailong Li [b](#page-0-1) , Rui Xiong [a](#page-0-0),[\\*\\*](#page-0-2)

- <span id="page-0-0"></span><sup>a</sup> Department of Vehicle Engineering, School of Mechanical Engineering, Beijing Institute of Technology, Beijing 100081, China
- <span id="page-0-1"></span><sup>b</sup> School of Business, Society and Engineering, Malardalen University, V € asterås 72123, Sweden €

- Integration of physical and data-driven models for accurate degradation prediction.
- Considering both degradation trajectories and RUL enhances the comprehensiveness of health assessment.
- Dynamic adjustment of hyperparameters improves the predictive capability of the network.
- Limited training data shows strong early prediction capability.
- Future trends in health management driven by PINN and Bayesian optimization.

#### ARTICLE INFO

Keywords: Supercapacitor Physics-informed neural network Degradation trajectories Remaining useful life

#### HIGHLIGHTS GRAPHICAL ABSTRACT

![](_page_0_Figure_21.jpeg)

# ABSTRACT

Supercapacitors are widely used in transportation and renewable energy fields due to their high power density, stable cycling performance, and rapid charge–discharge capabilities. To ensure efficient applications of supercapacitors, accurately predicting their degradation trajectories and remaining useful life (RUL) is crucial. For this purpose, a physics-informed neural network (PINN) model is developed using Long Short-Term Memory (LSTM) as the base architecture. Physical equations are embedded into the loss function to ensure consistency with domain knowledge, allowing the loss function to incorporate both physical and data-driven components. The balance between these two loss components is dynamically determined through Bayesian optimization, to enhance the model's accuracy further. Validation results show a root mean square error (RMSE) of 3 mF (the rated capacity is 1 F) in the degradation trajectory prediction and a RMSE of 269 cycles (the average cycle life is 5180 cycles) for the RUL. Ablation experiments were conducted to validate the effectiveness of integrating physical information into the LSTM framework. Results demonstrate that the proposed model outperforms both the datadriven LSTM method and the empirical equation-based method that the PINN model can reduce the RMSE by 85% and 87.5% for degradation trajectory prediction, and 86.5% and 94.6% for RUL prediction, respectively. In addition, a comparison with advanced models demonstrates that our model reduces the requirement significantly on training data while maintaining comparable prediction accuracy, which favors scenarios where data is scarce.

This article is part of a special issue entitled: AAINBESS published in Green Energy and Intelligent Transportation.

E-mail addresses: [yangruixin@bit.edu.cn](mailto:yangruixin@bit.edu.cn) (R. Yang), [rxiong@bit.edu.cn](mailto:rxiong@bit.edu.cn) (R. Xiong).

#### <https://doi.org/10.1016/j.geits.2025.100291>

<sup>\*</sup> Corresponding author.

<span id="page-0-2"></span><sup>\*\*</sup> Corresponding author.

| Abbreviations and notations |                                                 |  |  |
|-----------------------------|-------------------------------------------------|--|--|
| ANN                         | Artificial Neural Network                       |  |  |
| BO                          | Bayesian Optimization                           |  |  |
| CNN                         | Convolutional Neural Network                    |  |  |
| GRU                         | Gated Recurrent Unit                            |  |  |
| LSTM                        | Long Short-Term Memory                          |  |  |
| MAE                         | Mean Absolute Error                             |  |  |
| MAPE                        | Mean Absolute Percentage Error                  |  |  |
| NARX                        | Nonlinear Autoregressive Network with Exogenous |  |  |
|                             | Inputs                                          |  |  |
| NSGAIII                     | Non-dominated Sorting Genetic Algorithm III     |  |  |
| OLS                         | Ordinary Least Squares                          |  |  |
| PINN                        | Physics-Informed Neural Network                 |  |  |
| RMSE                        | Root Mean Square Error                          |  |  |
| RUL                         | Remaining Useful Life                           |  |  |
| SOH                         | State of Health                                 |  |  |
|                             |                                                 |  |  |

#### 1. Introduction

Supercapacitors, as a novel energy storage device, offer higher capacitance, greater specific capacity, a broader operating temperature range, and a longer lifespan compared to traditional capacitors [\[1\]](#page-12-0). They are currently widely utilized in hybrid vehicles, playing a crucial role in power output coordination [[2\]](#page-12-1). To ensure safe supercapacitor usage, optimizing management strategies through accurate prediction of degradation trajectories and RUL is essential [[3](#page-12-2)]. This approach addresses key challenges in electric vehicle battery monitoring, safety, and energy management, meeting the demand for high-precision performance evaluation across the vehicle's lifecycle [\[4](#page-12-3)].

Current methods for predicting supercapacitor degradation trajectories and RUL are mainly divided into model-based and data-driven approaches [[5](#page-12-4)]. Model-based methods are developed by studying supercapacitor failure mechanisms and aging process parameters, aiming to capture the underlying physical and chemical processes of aging. However, their accuracy is limited by assumptions about degradation mechanisms and parameter derivation. For instance, Xu et al. developed a capacity degradation model based on the Arrhenius equation, using temperature, current, and cycle numbers as variables, achieving a root mean square error (RMSE) of approximately 10.5 F over the lifetime, but assuming exponential decay under varying conditions, which may oversimplify the process [[6](#page-12-5)]. German et al. proposed an SEI-based aging law for capacitance loss during floating aging, tested on 81 commercial supercapacitors, with an RMSE of 3% for state of health (SOH) estimation, yet it assumes irreversible aging, potentially overlooking reversible factors like gas adsorption [\[7\]](#page-12-6). Wu et al. introduced a life prediction method based on the "ten-degree rule," assuming reaction rates double every 10 C, achieving an RMSE of 1562.5 cycles, but this may oversimplify temperature-degradation relationships, limiting accuracy in extreme conditions [\[8\]](#page-12-7).

In contrast, data-driven methods do not require understanding internal physicochemical processes or prior model assumptions, typically resulting in black-box models. However, they heavily rely on large, highquality training datasets. For example, Wang et al. proposed a CNN-based RUL prediction method, mapping five consecutive charge–discharge cycles to RUL with an RMSE of 501 cycles, but requiring 85% of data for training [\[9\]](#page-12-8). Ren et al. used an artificial neural network (ANN) model, achieving an RMSE of 599 cycles using the first 16% of cycles from 88 supercapacitors, highlighting dataset dependency [\[10](#page-12-9)]. Zhou et al. applied a residual convolutional neural network (Res-CNN) for lithium iron phosphate (LFP) battery cycle life prediction, with mean absolute errors (MAEs) of 43.366 cycles and mean absolute percentage errors (MAPEs) below 4.557%, yet needing data from the first 30% of cycles [[11\]](#page-12-10). Recent advances in sensing technologies, such as acoustic sensing (e.g., ultrasonic testing and acoustic emission) and internal temperature monitoring (e.g., NTC sensors, fiber optic sensors), offer insights for supercapacitor state prediction, particularly in capturing nonlinear aging characteristics, despite focusing primarily on lithium-ion batteries [[12,](#page-12-11) [13\]](#page-13-0). These methods, while achieving high accuracy, share a common limitation: reliance on data quality and quantity. A summary of relevant studies is summarized in [Table 1](#page-1-0).

Both model-based and data-driven methods have inherent limitations: model-based approaches often oversimplify processes, reducing flexibility [[20\]](#page-13-1), while data-driven methods lack interpretability and require extensive data [[21,](#page-13-2)[22\]](#page-13-3).

Although the application of PINN in predicting supercapacitor degradation trajectories and RUL remains limited, their success in other fields highlights their potential to address the shortcomings of both model-based and data-driven approaches. For instance, Gong et al. [[23\]](#page-13-4) developed an energy-based PINN for low-frequency electromagnetic prediction, where physical constraints were embedded into the loss function, ensuring outputs aligned with the underlying physical model. Their results demonstrated that physics-informed loss functions significantly outperformed conventional deep-learning approaches in predicting magnetic field distributions. Similarly, Cho et al. [[24\]](#page-13-5) applied PINNs to predict lithium-ion battery cell temperature by integrating an empirical thermal model into the loss function, achieving a prediction error of only 0.05 C.

A key challenge in PINNs is balancing the weight between physical constraints and data fitting. Traditional methods rely on fixed weights, such as those used by Colby et al. for solving the Allen–Cahn equation, where a large fixed weight was assigned to the physical loss term to ensure accuracy near initial conditions [[25\]](#page-13-6). However, such static approaches often fail to adapt to diverse datasets or dynamic optimization processes, leading to suboptimal performance, overfitting, or slow convergence. Manual weight tuning, while straightforward, is labor-intensive, error-prone, and heavily dependent on expert knowledge, particularly in high-dimensional problems.

To address these, this paper proposes a PINN method for predicting degradation trajectories and the remaining useful life of supercapacitors, combining LSTM with an empirical aging equation in the loss function, balanced by a parameter optimized via Bayesian optimization for enhanced adaptability and performance. The main contributions of this paper are shown as follows:

<span id="page-1-0"></span>Table 1 Summary of literature on data-driven models.

| Reference | Method                                         | Accuracy                                                   | Training data requirements                      |
|-----------|------------------------------------------------|------------------------------------------------------------|-------------------------------------------------|
| [9]       | CNN-based method                               | RMSE of 501 cycles                                         | 85% of the total number of supercapacitor units |
| [10]      | ANN-based method                               | RMSE of 599 cycles                                         | 16% of full life cycle data                     |
| [11]      | Res–CNN–based<br>method                        | MAEs of 43.366 cycles                                      | 30% of full life cycle data                     |
| [14]      | Gaussian process regression-based method       | RMSE of less than 2%                                       | 60% of the total number of supercapacitor units |
| [15]      | LSTM-based method                              | RMSE of 0.026,1 on online data and 0.033,8 on offline data | 80% of the total number of supercapacitor units |
| [16]      | Bidirectional-LSTM-based method                | RMSE of 0.027,5                                            | 60% of full life cycle data                     |
| [17]      | LSTM-based model with hybrid genetic algorithm | RMSE ranging from 0.016,1 to 0.026,4                       | 50% of full life cycle data                     |
| [18]      | Bayesian optimization-based hyperband method   | MAPE of 1.05%                                              | 6% of full life cycle data                      |
| [19]      | NARX neural networks method                    | RMSE of 0.032,8                                            | 60% of full life cycle data                     |

## (1) Physics-Data Synergistic Framework via Embedded PINN Architecture

An aging physical model is proposed to describe the aging process of supercapacitors. A physics-informed neural network based on an LSTM framework is developed, in which a deep coupling between the physical model and the data-driven model is achieved through the integration of the physical model into the loss function.

#### (2) Adaptive Loss Balancing in PINNs via Bayesian Optimization

A novel method is proposed to dynamically balance data-driven and physics-based losses within the PINN framework. A tunable hyperparameter is introduced to adaptively weigh the trade-off between data fitting and physical constraints, with its optimal value efficiently determined through Bayesian optimization. The proposed approach is demonstrated to accelerate model convergence, mitigate overfitting and underfitting risks, and significantly enhance generalizability while ensuring the effective integration of physical constraints.

The subsequent chapters are outlined as follows: Section [2](#page-2-0) provides a detailed introduction to the theoretical knowledge of the models involved in this study; Section [3](#page-5-0) presents a detailed overview of the dataset used in this research and the model construction process; Section [4](#page-6-0) offers the experimental results and discussions; And Section [5](#page-12-12) concludes the findings.

#### <span id="page-2-0"></span>2. Methodology

The overall process for predicting the degradation trajectory and remaining useful life of supercapacitors based on the PINN is shown in [Fig. 1](#page-3-0), including the parts of data acquisition, data processing, model training, and model testing and evaluation. The modelling principles discussed in this paper will be explained in the following sections.

#### 2.1. Supercapacitor aging physical model

For lithium-ion batteries under dynamic charge–discharge conditions, the initial aging stage is predominantly characterized by solid electrolyte interphase (SEI) layer growth, while the later aging stage is primarily governed by cathode material phase transformation and lithium deposition [[26\]](#page-13-13). Consequently, the capacity degradation exhibits a distinct two-phase characteristic under different dominant aging mechanisms [\[27](#page-13-14)]. This phenomenon is also applicable to supercapacitors. Relevant studies demonstrate that carbon-electrode-based supercapacitors generally exhibit nonlinear degradation patterns [\[28](#page-13-15)].

<span id="page-2-1"></span>Therefore, this study develops a supercapacitor aging physical model, with the specific mathematical formulations presented as follows:

$$SOH_i = A \cdot \ln(\text{cycle}_i) + B \tag{1}$$

In addition, the two parameters A and B in the equation, whose specific values are not explicitly provided, will be iteratively updated along with the network parameters such as weights and biases in the subsequently developed PINN model for degradation trajectory prediction, which will be described in detail later.

#### 2.2. Physics-informed neural network

The LSTM network is chosen as the foundational network framework for the PINN in this study. LSTM is a special structure of Recurrent Neural Networks [\[29](#page-13-16)]. As an improved version of RNN, it retains the traditional RNN structure, while optimizing the design of the hidden layer [\[30](#page-13-17)]. By introducing a "gate" mechanism, LSTM can flexibly control the flow of information and selectively remember or forget information within the network through these gates [\[31](#page-13-18)], effectively addressing the vanishing or exploding gradient problem commonly encountered by traditional RNNs when processing long sequence data. This makes LSTM particularly well-suited for long-term sequence prediction tasks. For instance, K. Park et al. employed the LSTM model to capture the long-term aging trajectory of lithium-ion batteries, achieving high-precision RUL predictions with a MAPE ranging from 0.47% to 1.88% [[32\]](#page-13-19). Similarly, Liu, J. et al. leveraged the long-term sequence sensitivity of the LSTM network to achieve high-precision predictions in the ocean temperature forecasting problem [[33\]](#page-13-20).

[Fig. 2](#page-4-0) shows the typical structure of an LSTM memory block, where each block contains three gated structures: the input gate, output gate, and forget gate [\[34](#page-13-21)].

The operational process is as follows [\[35\]](#page-13-22): the network first utilizes the output of the memory block at the previous time step, ht-1, along with the current input, xt, to calculate the input gate it, forget gate ft, output gate Ot, and the storage cell C~<sup>t</sup> . Next, the forget gate ft acts on the memory cell from the previous time step, Ct-1, while the input gate it acts on the storage cell C~<sup>t</sup> , determining which information is retained. Together, these gates update the current memory cell Ct. Finally, the output gate Ot transmits the current state of the memory cell to the memory block output ht. The specific computation formulas are as follows:

$$i_{t} = \sigma(W_{t}x_{t} + U_{t}h_{t-1} + b_{t})$$

$$f_{t} = \sigma(W_{t}x_{t} + U_{t}h_{t-1} + b_{t})$$

$$o_{t} = \sigma(W_{o}x_{t} + U_{o}h_{t-1} + b_{o})$$

$$\tilde{C}_{t} = tan h(W_{c}x_{t} + U_{c}h_{t-1} + b_{c})$$

$$C_{t} = f_{t} \otimes C_{t-1} + i_{t} \otimes \tilde{C}_{t}$$

$$h_{t} = o_{t} \otimes tan h(C_{t})$$

$$(2)$$

In the equations, Wi, Wf, and W<sup>o</sup> represent the weight matrices for the input gate, forget gate, and output gate, respectively. Ui, Uf, and U<sup>o</sup> represent the weight matrices for the hidden layer, and bi, bf, and b<sup>o</sup> are the bias matrices for the respective gate structures. σ represents the activation function.

The loss function of the LSTM network will be modified to achieve the coupling of model-based and data-driven approaches. The specific modifications are detailed below:

<span id="page-2-2"></span>
$$Loss_{total} = Loss_{data} + Loss_{physics}$$
 (3)

Under this loss function framework, when the neural network converges to the global optimum, the total loss reaches its minimum, indicating an optimal equilibrium between data-driven characteristics and physical constraints. Specifically, the model sufficiently learns temporal degradation patterns from the training set while constraining the parameter space through the embedded physical equation, ensuring predictions align with known aging mechanisms. This dual-objective optimization mechanism not only guarantees fidelity to historical data but also effectively mitigates overfitting risks, enabling the model to maintain high generalizability even with limited data.

Specifically, the total loss function consists of two components. The first component is the loss calculated based on the discrepancy between the actual degradation trajectory and the predicted degradation trajectory:

$$Loss_{data} = \frac{1}{n} \sum_{i=1}^{n} \left( y_{true,i} - \widehat{y}_i \right)^2$$
 (4)

where n represents the length of the training data, ytrue;<sup>i</sup> denotes the true maximum available capacity at the <sup>i</sup>-th cycle, and <sup>b</sup>yi represents the model-predicted maximum available capacity at the i-th cycle.

<span id="page-3-0"></span>![](_page_3_Figure_2.jpeg)

Fig. 1. Overall process of degradation trajectory and remaining useful life prediction for supercapacitors based on the proposed model: (a) Data preprocessing: The raw dataset was partitioned into training and testing subsets, followed by Min-Max normalization to eliminate dimensional heterogeneity. (b) Model construction and training: A PINN was developed based on an LSTM architecture, incorporating supercapacitor degradation equations as physical constraints. (c) Prediction and evaluation: Full lifecycle degradation trajectories were predicted on the test set, and the RUL estimation accuracy was quantified through multiple metrics (RMSE, MAE, MAPE), with comparative analysis against baseline models.

![](_page_3_Figure_4.jpeg)

The second component is introduced to achieve the coupling of physical information, and it is computed based on the deviation between the physics-based aging equation and the predicted values:

$$Loss_{physics} = \frac{1}{n} \sum_{i=1}^{n} (y_{physics,i} - \widehat{y}_i)^2$$
 (5)

<span id="page-4-0"></span>![](_page_4_Figure_2.jpeg)

Fig. 2. The structure of an LSTM network memory block.

where yphysics;<sup>i</sup> represents the maximum available capacity at the i-th cycle, calculated using the segmented multi-factor aging model (Eq. [\(1\)\)](#page-2-1) proposed in this paper.

The architecture of the network is shown in [Fig. 3](#page-4-1). The data into the neural network will have a two-fold effect, on the one hand, based on the black-box model of LSTM to carry out the nonlinear mapping of input and output, and on the other hand, it will be based on the embedded physical information to carry out the restriction of this nonlinear mapping as well as the correction. At the same time, Bayesian optimization will provide the optimal hyperparameters to balance data loss and physical loss, so as to obtain the high-precision and high-generalization prediction model.

The PINN model in this study aims to capture the temporal variation pattern of the supercapacitor degradation trajectory. Therefore, the model takes the cycle number, representing time, as input feature and outputs the corresponding state of health (SOH) for each cycle number. To perform time series prediction, we adopt a one-step input and onestep output strategy, with the specific input-output relationships as follows:

$$X = \operatorname{cycle}_i \tag{6}$$

$$Y = SOH_i (7)$$

<span id="page-4-1"></span>Where X represents the network input, and Y represents the network output.

Before feeding data into the model, preprocessing is required. Specifically, to accelerate the convergence of the network and improve numerical stability, Min-Max normalization is applied to the data. The normalization formula is as follows:

$$X' = \frac{X - \min(X)}{\max(X) - \min(X)}$$
(8)

$$Y' = \frac{Y - \min(Y)}{\max(Y) - \min(Y)} \tag{9}$$

The data is divided into two parts: training and testing. During the training process, historical cycle numbers are input to predict the corresponding historical SOH values.

Once the model training is complete, the parameters will be fixed and used for model testing. During the testing process, the model predicts the degradation trajectory of the supercapacitor based on the test data by iteratively updating the time steps. When the predicted result reaches the predefined lifespan threshold, the iterative updating stops.

#### 2.3. Bayesian optimization

Bayesian optimization is a statistical technique for global optimization, particularly well-suited for optimizing expensive, black-box functions [\[36](#page-13-23)]. Unlike traditional optimization methods, Bayesian optimization constructs a surrogate model, typically a Gaussian process,

![](_page_4_Figure_17.jpeg)

Fig. 3. Schematic diagram of the PINN model framework, incorporating physics-informed embedding, Bayesian optimization, and other key steps.

to approximate the objective function. It then selects the next point to evaluate based on this model, aiming to minimize the use of computational resources. The basic steps of Bayesian optimization are as follows [[37\]](#page-13-24):

Step 1: Model Initialization. Initialize the number of iterations N, the search space Ω; and randomly selected sample points.

Step 2: Model Training. Train the surrogate model, using a Gaussian process regression model as an example, which can be expressed as G(λ). Simultaneously, construct a robust acquisition function and optimize the acquisition function.

Step 3: Obtain the function value at the evaluation point, add it to the current set of evaluation points, update the surrogate model, and finally output the optimal candidate evaluation point to obtain the optimal hyperparameter value.

In this paper, Bayesian optimization is applied to solve for the optimal value of the hyperparameter λ in the PINN loss function. Therefore, the objective function f(m) is treated as a black-box model. In this context, the goal of Bayesian optimization is to find the point M\* that maximizes f(m) within the given search space Ω:

$$M^* = \underset{m \in \Omega}{\arg \max} f(m) \tag{10}$$

Bayesian optimization approximates f(m) using a Gaussian process bfðmÞ and guides the search by selecting an appropriate acquisition function αðMÞ:

$$M_{n+1} = \arg\max \alpha(M; \widehat{f}(m), \sigma(M))$$
 (11)

In this expression, σðMÞ represents the uncertainty at the input point M. Ultimately, the goal is to find the global optimum of f(m) with as few evaluations as possible.

Through a systematic exploration and exploitation strategy, Bayesian optimization can effectively handle complex optimization problems, making it a powerful tool for optimizing intricate systems.

#### <span id="page-5-0"></span>3. Data generation and model parameters setting

#### <span id="page-5-3"></span>3.1. Supercapacitors dataset

The degradation dataset for supercapacitors published in Ref. [\[10](#page-12-9)] includes 113 commercial supercapacitors with carbon-based electrodes.

These supercapacitors underwent 10,000 charge and discharge cycles at room temperature (28 C), with upper and lower cut-off voltages of 2.7 and 1 V, respectively. To generate a wide range of cycle lives, the 113 supercapacitors were divided into four Batches and tested under two different experimental conditions. Batches 1, 3, and 4 were cycled using a constant current of 20 mA for both charging and discharging, while Batches 2 was charged using a stepped current and discharged at a constant current of 20 mA. The details of batches are as [Table 2.](#page-5-1)

<span id="page-5-1"></span>Table 2 Supercapacitor experimental conditions.

| Batch  | Number of cells | Charging conditions                                                                  | Discharging conditions |
|--------|-----------------|--------------------------------------------------------------------------------------|------------------------|
| Batch1 | 28 SCs          | Constant at 20 mA                                                                    | Constant at 20 mA      |
| Batch2 | 25 SCs          | Stepwise current profile of [20, 15, 10, 5] mA, cutoff voltages at [1, 1.85, 2.36] V | Constant at 20 mA      |
| Batch3 | 30 SCs          | Constant at 20 mA                                                                    | Constant at 20 mA      |
| Batch4 | 30 SCs          | Constant at 20 mA                                                                    | Constant at 20 mA      |

<span id="page-5-2"></span>![](_page_5_Figure_18.jpeg)

Fig. 4. Degradation trajectory of supercapacitors: (a) Complete dataset encompassing all charge–discharge cycles. (b) Early-stage dataset covering the initial 500 cycles. (c) Late-stage dataset corresponding to the final 500 cycles.

The failure of a supercapacitor is defined as when its capacitance decreases to 90% of its initial value (0.90 F) [9]. The lifetimes of the 113 supercapacitors, based on this criterion, range from several hundred cycles to nearly ten thousand cycles. Fig. 4 shows the distribution of their degradation trajectories, illustrating the capacitance of all 113 SCs as a function of the cycle number for the first 10,000 cycles. In contrast to commercial lithium batteries, which have negligible capacity fade in the early cycles and accelerated fade near the end of life [38], SCs exhibit rapid capacitance loss in the early cycles and slower loss afterward, as seen in Fig. 4(b) and (c).

#### 3.2. Model parameters setting

Training parameter setting: The training process of the model involves configuring several complex hyperparameters, each of which influences the network's final performance to varying degrees. Eko Putra Wahyuddin et al. analyzed errors in identifying ideal hyperparameters and defined appropriate validation methods, exploring the effects of different hyperparameter combinations [39]. Building on their work, the specific hyperparameter settings for the constructed models are defined in this study. The hyperparameters of the PINN model are presented in Table 3.

It is important to emphasize that this study employs three distinct training/testing set partitioning strategies to evaluate the model's generalization performance under varying data volumes. Specifically, for each supercapacitor's degradation trajectory, the capacity data from the initial 100, 300, and 500 cycles are designated as training sets, with the remaining subsequent cycles forming the corresponding testing sets. Through systematic comparison of model performance across these three partitioning ratios (100/300/500 cycles), this approach not only quantitatively reveals the relationship between training data volume and prediction accuracy but also rigorously validates the model's robustness boundaries in extreme data-scarce scenarios (e.g., training with only 100 cycles of data). This tiered partitioning methodology establishes a rigorous experimental benchmark for assessing the few-shot learning capability of the proposed framework.

**Evaluation metrics**: To evaluate the accuracy of the proposed model, three distinct evaluation metrics have been used [40], including mean absolute error (MAE), root mean squared error (RMSE), and mean absolute percentage error (MAPE), defined as follows:

$$RMSE = \sqrt{\frac{1}{N} \sum_{i=1}^{N} \left( \hat{y}_i - y_i \right)^2}$$
 (12)

$$MAE = \frac{1}{N} \sum_{i=1}^{N} |\hat{y}_i - y_i|$$
 (13)

$$MAPE = \frac{100\%}{N} \sum_{i=1}^{N} \frac{\left| \hat{y}_i - y_i \right|}{y_i}$$
 (14)

<span id="page-6-1"></span>**Table 3**Training parameters of the PINN model.

| Parameter Name               | Value |
|------------------------------|-------|
| Number of LSTM layers        | 2     |
| Neurons in first LSTM layer  | 128   |
| Neurons in second LSTM layer | 256   |
| Max epoch                    | 5,000 |
| Mini-batch size              | 32    |
| Initial learning rate        | 0.001 |
| Dropout rate                 | 0.2   |
| Optimizer                    | Adam  |
| Learning rate decay epochs   | 2,000 |
| Learning rate decay factor   | 0.5   |
| Activation function          | ReLU  |

For the degradation trajectory prediction,  $y_i$  and  $\hat{y}_i$  denote the true SOH and predicted SOH of the supercapacitor at the ith cycle, respectively. For the RUL prediction,  $y_i$  and  $\hat{y}_i$  represent the true RUL and predicted RUL of the supercapacitor, respectively.

#### <span id="page-6-0"></span>4. Results and discussion

To better demonstrate the effectiveness of integrating physical information with neural networks, the proposed framework is decomposed into two components: (1) The LSTM model, which does not incorporate physical information, and (2) the empirical equation curve fitting model based on the ordinary least squares (OLS) method, which does not include any neural network components and uses the same empirical equation as the physical information introduced in this paper [41]. The proposed PINN model will be compared with these two baseline models to validate the effectiveness of combining physical information with the neural network framework. To further demonstrate the advantages of the proposed model, we also conducted a comparative analysis with three mainstream models [16,17,19]. Additionally, the experiments were conducted using Python 3.9 and Torch 1.12.0 within an Anaconda 3 environment. The hardware used included an NVIDIA RTX 4070 GPU and 8 GB of system RAM. The details are described as follows.

#### 4.1. Training results

The proposed PINN model was trained using datasets with varying proportions of training and testing data. Fig. 5 illustrates the convergence of the hybrid loss function (Equation (3)) and the evolution of key aging parameters A and B during the training process for 113 supercapacitors under different input sequence lengths (500, 300, and 100 cycles). As shown in Fig. 5(a), the total loss rapidly decreased to a stable value of 1e-4 within 5,000 iterations, demonstrating the effective optimization of the data-physics coupling objective. Fig. 5(b) and (c) reveal that parameters A and B stabilized around -0.18 and -0.12, respectively, closely matching the values obtained from least-squares fitting of the full-lifecycle degradation trajectories.

### 4.2. Degradation trajectory prediction results

In this section, we will provide a detailed comparison of the supercapacitor degradation trajectories under different training data proportions and various models. The details are described as follows.

Results under different training data proportions: Conventional data-driven methods typically require over 50% of the total data to ensure performance, whereas the proposed PINN framework substantially reduces reliance on large datasets through physics integration. To validate the model's effectiveness in data-scarce scenarios, training was conducted using only the initial 500, 300, and 100 cycle. As shown in Fig. 6, even with merely 100-cycle training data, the model achieved precise full-lifecycle degradation trajectory predictions, exhibiting a maximum SOH prediction RMSE of 14.8 mF. This demonstrates its exceptional generalization capability and effectiveness in capturing critical degradation features. Prediction accuracy further improved with increased training data (300/ 500 cycles), showing closer alignment with ground-truth trajectories. The model's high-precision early-life predictions provide reliable technical support for supercapacitor SOH assessment and cascade utilization strategies (e.g., secondary applications in energy storage systems), underscoring its practical value in industrial applications.

Results under different models: To further evaluate the effectiveness of integrating physics-based information with neural networks, an ablation study was conducted to compare three models: (1) the PINN model, (2) the LSTM model, and (3) the OLS model. Fig. 7 illustrates the error distributions (RMSE, MAE, and MAPE) of the proposed model and the two baseline models under different input lengths (100, 300, and 500 cycles). Each subplot corresponds to a specific error metric, with boxplots

<span id="page-7-0"></span>![](_page_7_Figure_2.jpeg)

<span id="page-7-1"></span>Fig. 5. Training results of PINN: (a) The loss function under different proportions of training data. (b) The parameter A under different proportions of training data. (c) The parameter B under different proportions of training data.

![](_page_7_Figure_4.jpeg)

Fig. 6. Distribution of RMSEs under different training cycle lengths and the predictive results of representative samples under 500 training cycle lengths and 100 training cycle lengths.

grouped by input length and distinguished by color for different models. The results indicate that the proposed model consistently achieves the lowest median error across all input lengths. Its narrower interquartile range further demonstrates its superior robustness, while its sensitivity to outliers is significantly lower than that of the baseline models. Moreover, in terms of RMSE, when the input data length is short, both the LSTM and OLS models exhibit excessively large errors, rendering them completely ineffective in trajectory prediction tasks.

[Fig. 8](#page-8-1) presents the prediction results for three representative samples (Num001, Num043, and Num070) under different training data lengths. It is evident that the proposed PINN model significantly outperforms the LSTM and OLS models in degradation trajectory prediction. Due to the

<span id="page-8-0"></span>![](_page_8_Figure_2.jpeg)

Fig. 7. Distribution of prediction errors across models and input lengths.

<span id="page-8-1"></span>![](_page_8_Figure_4.jpeg)

Fig. 8. Degradation trajectory prediction results of the three models for representative samples Num001, Num043, and Num070 for different training cycle lengths.

limited training data, the LSTM model exhibits a plateauing effect in the later stages of prediction, while the OLS model fails to accurately fit the actual trajectory, with this issue becoming more pronounced as the training data decreases. In contrast, the proposed PINN model consistently tracks the actual degradation curve across all training data lengths, achieving accurate degradation trajectory prediction.

Additionally, [Fig. 9](#page-9-0) shows the prediction errors for the three models on the aforementioned samples. The errors for the PINN model are significantly smaller compared to the other two models, which show greater volatility.

Furthermore, we conducted an in-depth analysis of the absolute percentage error distribution for degradation trajectory predictions across 113 supercapacitors under different lengths of historical data inputs. As shown in [Fig. 10](#page-9-1), subplots (a), (b), and (c) illustrate the error distributions of the three models with 500, 300, and 100 cycles of historical data as inputs, respectively. The results reveal that the proposed PINN model predominantly exhibits errors within 2%, demonstrating high prediction accuracy and stability. In contrast, the LSTM and OLS models show broader error distributions, with a significant number of supercapacitors exceeding 5% error, indicating substantial deviations from the true values. These findings further validate the robustness and superiority of the PINN model in data-scarce scenarios.

To comprehensively evaluate the performance of the proposed PINN model and validate its superiority over existing approaches, a comparative analysis is conducted against several well-established models that have been widely adopted in related fields for similar tasks. These models have demonstrated excellent predictive accuracy and robustness in supercapacitor degradation trajectory forecasting. Specifically, the Bidirectional LSTM-based method proposed by Liu et al. effectively captures both forward and backward temporal dependencies, enhancing sequence prediction accuracy and robustness [[16\]](#page-13-9). The Hybrid Genetic Algorithm method introduced by Zhou et al. combines global search capabilities with local optimization strategies, enabling efficient solutions for complex problems and finding extensive applications in optimization tasks

<span id="page-9-0"></span>![](_page_9_Figure_2.jpeg)

<span id="page-9-1"></span>Fig. 9. Degradation trajectory prediction errors of the three models for representative samples Num001, Num043, and Num070 for different training cycle lengths.

![](_page_9_Figure_4.jpeg)

Fig. 10. Prediction error distributions under different input lengths: (a) Absolute percentage error distributions of the PINN, LSTM, and OLS models with 500 cycles of historical data as input. (b) Absolute percentage error distributions of the three models with 300 cycles of historical data as input. (c) Absolute percentage error distributions of the three models with 100 cycles of historical data as input.

[[17\]](#page-13-10). The NSGAIII-NARX method, developed by Haris et al., integrates the Nonlinear Autoregressive Network with Exogenous Inputs (NARX) and the Non-Dominated Sorting Genetic Algorithm III (NSGAIII), effectively addressing performance challenges under different degradation modes. This approach significantly improves prediction accuracy and excels in multi-trend learning scenarios [[19\]](#page-13-12). A comparative evaluation of these models provides a solid foundation for assessing the effectiveness of the proposed PINN model. The detailed comparison results are presented in [Table 4.](#page-10-0) As demonstrated in the table, the proposed physics-informed model achieves comparable RMSE performance with significantly less training data compared to other models, highlighting its promising potential for data-scarce scenarios. However, due to potential

<span id="page-10-0"></span>Table 4 Comparison of performance metrics between PINN and existing models.

| Method                                            | Accuracy                                | Training Data Requirements      |
|---------------------------------------------------|-----------------------------------------|---------------------------------|
| Proposed PINN method                              | RMSE ranging from 0.003 F to 0.005,7 F  | 1%–5%<br>of the full life cycle |
| Bidirectional-LSTM-based method [16]              | RMSE of 0.027,5 F                       | 60% of the full life cycle      |
| Hybrid genetic algorithm method [17]              | RMSE ranging from 0.0161 F to 0.026,4 F | 50% of the full life cycle      |
| Bayesian optimization-based hyperband method [18] | MAPE of 1.05%                           | 6% of the full life cycle       |

biases introduced by different datasets, future studies are warranted to evaluate its generalizability and ensure more equitable benchmarking across diverse experimental configurations.

#### 4.3. RUL prediction results

<span id="page-10-1"></span>By iterating the model at each time step and using the failure threshold defined in Section [3.1,](#page-5-3) we can obtain the predicted RUL of the supercapacitor. [Fig. 11](#page-10-1) shows the RUL prediction results of three models trained using data from 100 cycles. The results demonstrate that the PINN model significantly outperforms the other models in terms of RUL prediction accuracy, further validating the superiority of the proposed method in predicting degradation trajectories.

The evaluation metric scores for the three models with training data lengths of 500, 300, and 100 cycles are presented in [Fig. 12.](#page-10-2) The RUL prediction error of the PINN model is consistently smaller than that of the other two models across all training data sizes. Specifically, when 500 cycles are used for training, the average RMSE of the proposed model's

![](_page_10_Figure_9.jpeg)

Fig. 11. RUL prediction results of different models: (a) PINN, (b) LSTM, (c) OLS.

<span id="page-10-2"></span>![](_page_10_Figure_11.jpeg)

Fig. 12. RUL prediction results of different models under varying training data proportions. (a) Results based on 500-cycle input data. (b) Results based on 300-cycle input data. (c) Results based on 100-cycle input data.

<span id="page-11-0"></span>![](_page_11_Figure_2.jpeg)

Fig. 13. Bayesian Optimization results under varying input data lengths.

RUL prediction is 269.4 cycles, which is significantly lower than the RMSE of 1,993.9 for the LSTM model and 3,273.3 for the OLS model. This trend holds for both the 300-cycle and 100-cycle training data.

## 4.4. Bayesian Optimization results

This study systematically investigates the optimization strategies and underlying mechanisms of the critical hyperparameter λ in PINN, which balances data-driven loss terms and physics-informed loss terms. Through the implementation of a Bayesian optimization framework, a quantitative mapping relationship between the λ parameter and model prediction accuracy was established (as shown in [Fig. 13](#page-11-0)). The experimental results reveal that the optimization process of this hyperparameter exhibits notable dependence on training data volume: when the training cycle is 100, the optimal λ value reaches 4.116; when the training cycle increases to 500, the λ value decreases to 1.09. This parameter evolution pattern uncovers the intrinsic learning mechanism of PINN models—under limited training data conditions, enhancing the physical constraint term (corresponding to larger λ values) effectively compensates for data scarcity while increasing training data volume allows appropriate reduction of λ (i.e., elevating the weight of data-driven modules) to better exploit the high-dimensional representation capability of neural networks. This observation aligns with the theoretical analysis presented in Ref. [\[42](#page-13-29)].

<span id="page-11-1"></span>![](_page_11_Figure_8.jpeg)

Fig. 14. Impact of λ on model training and testing performance. (a) Training set predictions. (b) Testing MSE as a function of λ.

<span id="page-12-13"></span>**Table 5**The impact of different Bayesian optimization iteration numbers.

| Number of bayesian iterations | Optimization time/min | MSE         |
|-------------------------------|-----------------------|-------------|
| 5                             | 9.7                   | 0.001,8     |
| 10                            | 20.3                  | 0.001,5     |
| 15                            | 30.3                  | 3.935,4e-04 |
| 20                            | 40.1                  | 3.919,3e-04 |
| 25                            | 51.03                 | 3.916,6e-04 |
| 30                            | 61.4                  | 3.133,9e-04 |

Furthermore, we systematically analyzed the impact of varying  $\lambda$  values on both the training process and model generalizability. Taking Cell #7 as an example, Fig. 14(a) illustrates the training set predictions under different  $\lambda$  values. The results reveal that as  $\lambda$  increases (assigning a higher weight to the physics-informed loss), the model predictions gradually deviate from the training ground truth. This behavior stems from the enhanced physics constraints guiding parameter optimization while reducing over-reliance on data fitting. Critically, this deviation does not indicate suboptimal training but reflects the model's pursuit of a global optimum under the combined loss objective. Minimizing data loss alone ( $\lambda$  $\rightarrow$ 0) risks overfitting, whereas appropriate physical regularization ( $\lambda$  > 0) enhances generalization. As validated in Fig. 14(b), the model achieves the lowest test MSE at  $\lambda$  = 2.7, demonstrating an optimal balance between data fidelity and physical consistency.

Additionally, we further investigated the computational cost and its impact on model prediction accuracy under different Bayesian optimization iteration counts. As shown in Table 5, we present the iteration time and the mean squared error (MSE) on the test set for varying Bayesian optimization iterations (ranging from 5 to 30 with an interval of 5). The results demonstrate that the optimization time increases approximately linearly with the number of iterations, while the rate of MSE reduction significantly slows down once the iteration count reaches 15. This indicates that, from the perspective of balancing computational cost and performance gain, 15 iterations represent a cost-effective choice.

#### <span id="page-12-12"></span>5. Conclusion

This study presents a PINN model for predicting supercapacitor degradation trajectories and remaining useful lifetime (RUL), addressing critical challenges in modeling complex aging processes. Three major findings can be concluded:

- (1) The developed PINN model can achieve high accuracy based on limited data. Utilizing merely 100 cycles of data, the model demonstrates robust performance with RMSE values of 5.7 mF (the rated capacity is 1 F) in the degradation trajectory prediction and 790.8 cycles (the average cycle life is 5,180 cycles) in RUL prediction. Increasing training data to 500 cycles further reduces errors to 3 mF and 269.4 cycles, respectively.
- (2) The model convergence speed and operational adaptabilit can be improved by the implementation of Bayesian optimization for hyperparameter tuning (specifically, the physics-informed weighting coefficient λ).
- (3) Ablation studies confirm the PINN model is superior to the standalone LSTM and ordinary least squares (OLS) models. For predictions of degradation trajectory and RUL, PINN reduces RMSE by 85% and 87.5% and 86.5% and 94.6% compared to LSTM and OLS, respectively.

While demonstrating promising predictive capabilities, two strategic enhancements could extend the model's applicability:

 Architectural Advancements: Adoption of bidirectional LSTM or GRU networks may improve temporal feature extraction efficiency, particularly for capturing complex degradation patterns in large datasets. (2) Mechanistic Integration: Explicit incorporation of electrochemical-thermal degradation models (e.g., voltagedependent aging kinetics) could strengthen physical consistency under extreme operating conditions, bridging the gap between data-driven predictions and first-principles behavior.

This work establishes a paradigm for synergizing domain knowledge with machine learning in energy storage prognostics, offering a scalable solution for predictive maintenance in electric vehicles and grid-scale storage systems.

#### CRediT authorship contribution statement

Lixin E: Writing – review & editing, Writing – original draft, Validation, Methodology, Investigation, Conceptualization. Jun Wang: Supervision, Methodology, Conceptualization. Ruixin Yang: Project administration, Funding acquisition. Chenxu Wang: Writing – review & editing, Methodology, Conceptualization. Hailong Li: Writing – review & editing, Methodology. Rui Xiong: Writing – review & editing, Writing – original draft, Supervision, Project administration, Methodology, Conceptualization.

#### Data availability statement

The data and materials used to support the findings of this study are available from the corresponding author upon reasonable request.

#### **Declaration of competing interest**

The authors have declared no conflict of interest.

#### Acknowledgements

This work was supported by the National Natural Science Foundation of China (Grant No. 52107222) and Beijing Natural Science Foundation (Grant No. L242075).

#### <span id="page-12-0"></span>References

- <span id="page-12-1"></span> Olabi AG, Abbas Q, Al Makky A. Supercapacitors as next generation energy storage devices: properties and applications. Energy 2022;248:123617.
- <span id="page-12-2"></span>[2] Wang J, Zhou J, Zhao W. Deep reinforcement learning based energy management strategy for fuel cell/battery/supercapacitor powered electric vehicle. Green Energy Intell Transp 2022;1(2):100028. https://doi.org/10.1016/j.geits.2022.100028.
- <span id="page-12-3"></span>[3] Liu X, Ren Y, Chen H, Feng D, Tian J. Supercapacitor life prediction based on improved support vector regression. J Power Supply 2023:1–13.
- <span id="page-12-4"></span>[4] Xiong R, Kim J, Shen W, Lv C, Li H, Zhu X, et al. Key technologies for electric vehicles. Green Energy Intell Transp 2022;1(2):100041. https://doi.org/10.1016/ j.geits.2022.100041.
- <span id="page-12-5"></span>[5] Ayob A, Ansari S, Lipu MSH, Hussain A, Soc MHM Saad. SOH and RUL estimation for supercapacitor management system: Methods, implementation factors, limitations and future research improvements. Batteries 2022;8(10):189.
- <span id="page-12-6"></span>[6] Xu X, Liu H, Lu X, et al. Research on capacity life prediction model of supercapacitor. Power Sources 2019;43(2):270–272+282.
- [7] German R, Sari A, Venet P, Ayadi M, Briat O, Vinassa J. Prediction of supercapacitors floating ageing with surface electrode interface based ageing law. Microelectron Reliab 2014;54(9–10):1813–7. https://doi.org/10.1016/ j.microrel.2014.07.105.
- <span id="page-12-8"></span><span id="page-12-7"></span>[8] Wu L, Shan J, Guan Y, Wang H. Life prediction method of supercapacitor for considering temperature and voltage. Chin J Power Sources 2018;42(1):90–2.
- <span id="page-12-9"></span>[9] Wang C, Xiong R, Tian J, Lu J, Zhang C. Rapid ultracapacitor life prediction with a convolutional neural network. Appl Energy 2022;305:117819. https://doi.org/ 10.1016/j.apenergy.2021.117819.
- <span id="page-12-10"></span>[10] Ren J, Lin X, Liu J, Han T, Wang Z, Zhang H, et al. Engineering early prediction of supercapacitors' cycle life using neural networks. Mater Today Energy 2020;18: 100537. https://doi.org/10.1016/j.mtener.2020.100537.
- [11] Zhou Z, Liu Y, You M, Xiong R, Zhou X. Two-stage aging trajectory prediction of LFP lithium-ion battery based on transfer learning with the cycle life prediction. Green Energy Intell Transp 2022;1(1):100008. https://doi.org/10.1016/ i.geits.2022.100008.
- <span id="page-12-11"></span>[12] Pan Y, Xu K, Wang R, Wang H, Chen G, Wang K. Lithium-ion battery condition monitoring: a frontier in acoustic sensing technology. Energies 2025;18(18):1068. https://doi.org/10.3390/en18181068.

- <span id="page-13-0"></span>[13] Pan Y, Xu K, Chen Z, Wang K. Advanced techniques for internal temperature monitoring in lithium-ion batteries: a review of recent developments. Coatings Feb. 2025;15(3):268. <https://doi.org/10.3390/coatings15030268>.
- <span id="page-13-7"></span>[14] Roman D, Saxena S, Bruns J, Robu V. A machine learning degradation model for electrochemical capacitors operated at high temperature. IEEE Access 2021;9: <sup>25544</sup>–53. <https://doi.org/10.1109/ACCESS.2021.3057959>.
- <span id="page-13-8"></span>[15] Zhou Y, Huang Y, Pang J, Wang K. Remaining useful life prediction for supercapacitor based on long short-term memory neural network. J Power Sources 2019;440:227149. <https://doi.org/10.1016/j.jpowsour.2019.227149>.
- <span id="page-13-9"></span>[16] Liu C, Zhang Y, Sun J, Cui Z, Wang K. Stacked bidirectional LSTM RNN to evaluate the remaining useful life of supercapacitor. Int J Energy Res 2022;46(3):3034–43. <https://doi.org/10.1002/er.7360>.
- <span id="page-13-10"></span>[17] Zhou Y, Wang Y, Kang L, Wang K, Peng F, Wang L, et al. Hybrid genetic algorithm method for efficient and robust evaluation of remaining useful life of supercapacitors. Appl Energy 2020;260:114169. [https://doi.org/10.1016/](https://doi.org/10.1016/j.apenergy.2019.114169) [j.apenergy.2019.114169.](https://doi.org/10.1016/j.apenergy.2019.114169)
- <span id="page-13-11"></span>[18] Haris M, Hasan MN, Qin S. Early and robust remaining useful life prediction of supercapacitors using BOHB optimized deep belief network. Appl Energy 2021;286: 116541. <https://doi.org/10.1016/j.apenergy.2021.116541>.
- <span id="page-13-12"></span>[19] Haris M, Hasan MN, Qin S. State of health prediction of supercapacitors using multitrend learning of NARX neural network. Mater Today Sustain 2022;20:100201. [https://doi.org/10.1016/j.mtsust.2022.100201.](https://doi.org/10.1016/j.mtsust.2022.100201)
- <span id="page-13-1"></span>[20] Bellomo M, Giazitzis S, Rosetti F, Dolara A. Deep learning regression with sequences of different length: an application for state of health trajectory prediction and remaining useful life estimation in lithium-ion batteries. Batteries 2024;10(8):292. <https://doi.org/10.3390/batteries10080292>.
- <span id="page-13-2"></span>[21] Feng H, Xu A, Liu Y. Health prognostics for lithium-ion batteries: mechanisms, methods, and prospects. Energy Environ Sci 2022;15:312–28. [https://doi.org/](https://doi.org/10.1039/D2EE03019E) [10.1039/D2EE03019E](https://doi.org/10.1039/D2EE03019E).
- <span id="page-13-3"></span>[22] Feng H, Xu A. A data compensation model for predicting SOH and RUL of lithium–ion battery. J Electr Eng Technol 2024;19:395–406. [https://doi.org/](https://doi.org/10.1007/s42835-023-01524-w) [10.1007/s42835-023-01524-w.](https://doi.org/10.1007/s42835-023-01524-w)
- <span id="page-13-4"></span>[23] Gong R, Tang Z. Further investigation of convolutional neural networks applied in computational electromagnetism under physics-informed consideration. IET Electr Power Appl 2022;16(6):653–74. [https://doi.org/10.1049/elp2.12183.](https://doi.org/10.1049/elp2.12183)
- <span id="page-13-5"></span>[24] Cho G, Wang M, Kim Y, Kwon J, Su W. A physics-informed machine learning approach for estimating lithium-ion battery temperature. IEEE Access 2022;10: <sup>88117</sup>–26. <https://doi.org/10.1109/ACCESS.2022.3199652>.
- <span id="page-13-6"></span>[25] Wight CL, Zhao J. Solving Allen-Cahn and Cahn-Hilliard equations using the adaptive physics informed neural networks. 2020. [https://doi.org/10.4208/](https://doi.org/10.4208/CICP.OA-2020-0086) [CICP.OA-2020-0086](https://doi.org/10.4208/CICP.OA-2020-0086).
- <span id="page-13-13"></span>[26] Naumann M, Spingler FB, Jossen A. Analysis and modeling of cycle aging of a commercial LiFePO4/graphite cell. J. Power Sources 2020; 451: 227666.
- <span id="page-13-14"></span>[27] Ali MA, Da Silva CM, Amon CH. Multiscale modelling methodologies of lithium-ion battery aging: a review of most recent developments. Batteries 2023;9(9):434. [https://doi.org/10.3390/batteries9090434.](https://doi.org/10.3390/batteries9090434)

- <span id="page-13-15"></span>[28] Chen X, Wu Y, Holze R. Ag(e)ing and degradation of supercapacitors: Causes, mechanisms, models and countermeasures. Molecules 2023;28(13):5028. [https://](https://doi.org/10.3390/molecules28135028) [doi.org/10.3390/molecules28135028](https://doi.org/10.3390/molecules28135028).
- <span id="page-13-16"></span>[29] Dhaked DK, Dadhich S, Birla D. Power output forecasting of solar photovoltaic plant using LSTM. Green Energy Intell Transp 2023;2(5):100113. [https://doi.org/](https://doi.org/10.1016/j.geits.2023.100113) [10.1016/j.geits.2023.100113](https://doi.org/10.1016/j.geits.2023.100113).
- <span id="page-13-17"></span>[30] Lindemann B, Mvller T, Vietz H, Jazdi N, Weyrich M. A survey on long short-term memory networks for time series prediction. Procedia CIRP 2021;99:650–5. <https://doi.org/10.1016/j.procir.2021.03.088>.
- <span id="page-13-18"></span>[31] Zheng Q, Zhou G, Liu D. Method of modeling temperature-displacement correlation for long-span arch bridges based on long short-term memory neural networks. Eng Mech 2021;38(4):68–79. [https://doi.org/10.6052/j.issn.1000-4750.2020.05.0323.](https://doi.org/10.6052/j.issn.1000-4750.2020.05.0323)
- <span id="page-13-19"></span>[32] Park K, Choi Y, Choi W, Ryu H, Kim H. LSTM-based battery remaining useful life prediction with multi-channel charging profiles. IEEE Access 2020;8:20786–98. [https://doi.org/10.1109/ACCESS.2020.2968939.](https://doi.org/10.1109/ACCESS.2020.2968939)
- <span id="page-13-20"></span>[33] Liu J, Zhang T, Han G, Gou Y. TD-LSTM: temporal dependence-based LSTM networks for marine temperature prediction. Sensors 2018;18(11):3797. [https://](https://doi.org/10.3390/s18113797) [doi.org/10.3390/s18113797.](https://doi.org/10.3390/s18113797)
- <span id="page-13-21"></span>[34] [Wang Z, Liu N, Chen C. Adaptive self-attention LSTM for RUL prediction of lithium](http://refhub.elsevier.com/S2773-1537(25)00041-6/sref35)[ion batteries. Information Sciences 2023;635:398](http://refhub.elsevier.com/S2773-1537(25)00041-6/sref35)–[413](http://refhub.elsevier.com/S2773-1537(25)00041-6/sref35).
- <span id="page-13-22"></span>[35] Salem FM. Gated RNN: the long short-term memory (LSTM) RNN. In: Recurrent neural networks. Cham: Springer; 2022. p. 45–68. [https://doi.org/10.1007/978-3-](https://doi.org/10.1007/978-3-030-89929-5_4) [030-89929-5\\_4](https://doi.org/10.1007/978-3-030-89929-5_4).
- <span id="page-13-23"></span>[36] Shahriari B, Swersky K, Wang Z, Adams R, Freitas N. Taking the human out of the loop: a review of Bayesian optimization. Proc IEEE 2016;104(1):148–75. [https://](https://doi.org/10.1109/JPROC.2015.2494218) [doi.org/10.1109/JPROC.2015.2494218.](https://doi.org/10.1109/JPROC.2015.2494218)
- <span id="page-13-24"></span>[37] [Valladares H, Tovar A. Multi-objective Bayesian optimization supported by deep](http://refhub.elsevier.com/S2773-1537(25)00041-6/sref38) [Gaussian processes. SAE Tech. Paper 2023-01-0031 2023](http://refhub.elsevier.com/S2773-1537(25)00041-6/sref38).
- <span id="page-13-25"></span>[38] Wang X, Hu B, Su X, Xu L, Zhu D. State of health estimation for lithium-ion batteries using random forest and gated recurrent unit. J Energy Storage 2024;76:109796. <https://doi.org/10.1016/j.est.2023.109796>.
- <span id="page-13-26"></span>[39] Wahyuddin EP, Caraka RE, Kurniawan R, Caesarendra W, Gio PU, Pardamean B. Improved LSTM hyperparameters alongside sentiment walk-forward validation for time series prediction. J Open Innov Technol Mark Complex 2024;10:100458. <https://doi.org/10.1016/j.joitmc.2024.100458>.
- <span id="page-13-27"></span>[40] Chen B, Liu Y, Xiao B. A novel hybrid neural network-based SOH and RUL estimation method for lithium-ion batteries. J Energy Storage 2024;98:113074. <https://doi.org/10.1016/j.est.2024.113074>.
- <span id="page-13-28"></span>[41] Zdaniuk B. Ordinary least-squares (OLS) model. In: Encyclopedia of quality of life and well-being research. Dordrecht: Springer; 2014. p. 4471–2. [https://doi.org/](https://doi.org/10.1007/978-94-007-0753-5_2008) [10.1007/978-94-007-0753-5\\_2008.](https://doi.org/10.1007/978-94-007-0753-5_2008)
- <span id="page-13-29"></span>[42] Wang S, Teng Y, Perdikaris P. Understanding and mitigating gradient flow pathologies in physics-informed neural networks. SIAM J Sci Comput 2021;43(5): A3055–81. <https://doi.org/10.1137/20M1318043>.
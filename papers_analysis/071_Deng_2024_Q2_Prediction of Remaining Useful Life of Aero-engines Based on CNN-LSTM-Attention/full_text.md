#### **RESEARCH ARTICLE**

![](_page_0_Picture_3.jpeg)

# **Prediction of Remaining Useful Life of Aero‑engines Based on CNN‑LSTM‑Attention**

**Sizhe Deng1 · Jian Zhou2**

Received: 24 June 2024 / Accepted: 19 August 2024 © The Author(s) 2024

## **Abstract**

Accurately predicting the remaining useful life (RUL) of aircraft engines is crucial for maintaining fnancial stability and aviation safety. To further enhance the prediction accuracy of aircraft engine RUL, a deep learning-based RUL prediction method is proposed. This method possesses the potential to strengthen the recognition of data features, thereby improving the prediction accuracy of the model. First, the input features are normalized and the CMAPSS (Commercial Modular Aero-Propulsion System Simulation) dataset is utilized to calculate the RUL for aircraft engines. After extracting attributes from the input data using a convolutional neural network (CNN), the extracted data are input into a long short-term memory (LSTM) network model, with the addition of attention mechanisms to predict the RUL of aircraft engines. Finally, the proposed aircraft engine model is evaluated and compared through ablation studies and comparative model experiments. The results indicate that the CNN-LSTM-Attention model exhibits superior prediction performance for datasets FD001, FD002, FD003, and FD004, with RMSEs of 15.977, 14.452, 13.907, and 16.637, respectively. Compared with CNN, LSTM, and CNN-LSTM models, the CNN-LSTM model demonstrates better prediction performance across datasets. In comparison with other models, this model achieves the highest prediction accuracy on the CMAPSS dataset, showcasing strong reliability and accuracy.

**Keywords** RUL · CNN · LSTM · Attention · CNN-LSTM-Attention

# **1 Introduction**

As the core propulsion system, precise prediction of the remaining life of an aeroengine can dynamically perceive future changes in its health status, which plays a crucial role in ensuring fight safety, reducing operating costs, optimizing maintenance decisions, and improving overall operating efficiency [[35\]](#page-11-0). Prognostic and health management (PHM) technology is often used by researchers to estimate the remaining usable life (RUL) of aeroengines. The accurate estimation of remaining useful life relies on in-depth analysis of historical trajectory data to reveal the patterns and trends of performance degradation [[10\]](#page-10-0). As technology continues to progress and its range of applications grows, how to make more accurate predictions of the remaining life of aeroengines through continuous iteration and optimization of model parameters has received widespread attention in PHM [\[11](#page-11-1), [12](#page-11-2)].

Utilizing feature extraction techniques and trend prediction methods for predicting the remaining useful life (RUL) of aeroengines is a crucial step in establishing efcient prediction models. Three primary areas are covered by the standard RUL prediction models: deep learning, superfcial machine learning, and statistical analysis. Traditional statistical models are built based on physical theorems or probability distributions to describe actual data or phenomena, including methods based on Wiener and Gamma processes [[27\]](#page-11-3), Weibull distribution [\[1](#page-10-1)], and Kalman flter methods [\[28](#page-11-4)]. For instance, Gebraeel et al. [\[7](#page-10-2)] used a Bayesian updating technique to link the historical and present degradation data of the same system, update the random parameters of the exponential degradation model, and determine the equipment's residual life distribution. It should be noted that while traditional statistical analysis can quickly construct a basic model for predicting the RUL of aero-engines, it has difculties in fully considering the complexity and uncertainty in actual operations, considering the interactions and

![](_page_0_Picture_17.jpeg)

<sup>\*</sup> Sizhe Deng 1171680406@qq.com

<sup>1</sup> College of Mathematics and Statistics, Kashi University, Kashi 844000, People's Republic of China

<sup>2</sup> Research Center of China-Pakistan Economic Corridor, Kashi University, Kashi 844000, People's Republic of China

relationships between multiple parameters and indicators, and often adopts a unifed model for prediction, which cannot fully refect the performance degradation characteristics of diferent components, leading to inaccurate prediction results. Compared to statistical analysis, machine learning exhibits broader practical applications in RUL prediction, reducing the complexity of modeling with less human intervention and computational cost. Deep learning structures such as recurrent neural networks (RNN) and long short-term memory (LSTM) models can process long-term dependencies in time series data by introducing memory units and gating units, which may be difcult to achieve in traditional statistical analysis. The RUL of aeroengines has been commonly predicted using shallow machine learning, such as artifcial neural networks (ANN) [[6](#page-10-3)], extreme learning machines (ELM) [[31\]](#page-11-5), support vector regression (SVM) [\[14](#page-11-6)], and hidden Markov models (HMM) [[4](#page-10-4)]. However, shallow machine learning faces challenges in predicting the RUL of aero-engines, such as reliance on manually designed feature extraction quality and limited capabilities in handling high-dimensional and redundant data. More advanced and efective technical methods need to be explored to address these issues.

Deep learning enables the acquisition of richer performance indicators, operational parameters, and environmental variables of aeroengines from monitored multi-sensor data, capturing, and simulating the complex dynamics of engine performance over time. With the rapid growth and complexity of monitored data for aeroengines, when faced with multi-sensor data (such as vibration, temperature, pressure, sound, etc.), Conventional prediction models that rely on superfcial machine learning frequently fail to completely capture the in-depth, nonlinear relationships within the data. Therefore, to predict the remaining useful life (RUL) of aeroengines more accurately, a shift from shallow machine learning models to more advanced deep learning models is necessary [\[40](#page-11-7)]. In recent years, deep learning-based life prediction models have achieved remarkable results, demonstrating high prediction accuracy and efficiency, including convolutional neural networks (CNN) [[37\]](#page-11-8), autoencoders (AE) [[23\]](#page-11-9), deep belief networks (DBN) [[22](#page-11-10)], and other methods. Xie et al. [\[33\]](#page-11-11) utilized an ensemble network of deep learning to predict the RUL of aero-engines and ftted key parameters using the Backpropagation (BP) algorithm. Li et al. [\[13](#page-11-12)] proposed a novel data-driven method using a deep convolutional neural network (DCNN) to efectively extract critical features, thus achieving accuracy in RUL prediction. Ruan et al. [\[25\]](#page-11-13) further pointed out that the CNN model possesses the characteristics of simple and efcient computation as well as high prediction accuracy. In more complex operating environments, mixed failure modes, and strong noise backgrounds, According to Chang et al. [[3](#page-10-5)], prediction accuracy may be signifcantly increased by using long shortterm memory (LSTM) to accurately capture both short- and long-term temporal relationships in time series data. Yuan et al. [\[34\]](#page-11-14) also proposed a neural network solution based on LSTM to accurately predict and evaluate the RUL of aeroengines. Liu et al. [\[19](#page-11-15)] introduced an improved multilevel long short-term memory network (ILSTMC) as a novel RUL prediction model for aero-engines, demonstrating that the ILSTMC prediction model can efectively reduce the prediction error of aero-engine RUL. It should be noted that traditional CNN, LSTM, and their variants still have some limitations, especially when capturing long-distance features or building associations between non-adjacent data [[38](#page-11-16)]. For instance, traditional convolution operations are limited by the size of the convolutional kernel and cannot capture dependencies between distant features in the sequence. While LSTM can handle long sequences through its internal gating mechanism, it still has limitations in constructing complex associations between non-adjacent data. Additionally, in parallel training, traditional models need to process data sequentially, making it difcult to achieve efcient parallel computation, limiting the training speed of the model and its deployment capabilities in large-scale applications. Moreover, deep learning often faces issues of information overload due to the large amount of stored information.to overcome these limitations, combining selfattention mechanisms with LSTM networks can signifcantly enhance the comprehensive processing ability of input sequence information. By using this technique, information processing becomes more accurate and efcient while also allowing deep learning models to automatically recognize and prioritize important aspects while stifing those that do not contribute as much, resulting in more precise analysis and prediction. The self-attention mechanism can correlate features at diferent positions [[15\]](#page-11-17), directly capturing longdistance features and associations between non-adjacent data by calculating the correlation coefcients between any two input sequence places. To precisely estimate the equipment's remaining useful life, Zhang et al. [\[36\]](#page-11-18) fused Temporal Self-Attention Modules (TSAM) with Bidirectional Gated Recurrent Units. Liu et al. [[16\]](#page-11-19) proposed integrating a channel attention mechanism before Bidirectional Gated Recurrent Units for predicting the RUL of aeroengines, adjusting BiGRU's attention to information from various channels, thus improving the accuracy and efciency of RUL prediction.

Modern aviation places greater emphasis on improving the reliability, quality, and safety of aircraft systems [\[21,](#page-11-20) [29](#page-11-21)]. As a critical component of an aircraft, the engine requires the further development of more precise prediction models for the remaining useful life (RUL) of aerospace engines. The adoption of hybrid methods can leverage the advantages of each method while avoiding its disadvantages, resulting in

![](_page_1_Picture_8.jpeg)

lower regression analysis errors and degradation prediction errors, thus enhancing the overall performance, stability, and generalization ability of the model. This paper proposes an innovative combined prediction method that integrates CNN, LSTM, and Self-attention for more accurate predictions of the RUL of aerospace engines. Firstly, the dataset for the RUL of aerospace engines undergoes preprocessing to meet the input requirements of the model. Secondly, the processed data undergoes feature extraction using the CNN model, which utilizes the CNN network to deeply mine each feature, capturing the key local features in the data. Finally, a combined model based on LSTM and the self-attention mechanism (LSTM-Attention) is employed to model the extracted features. Leveraging its ability to analyze time series data, it achieves precise predictions of the RUL of aerospace engines. In summary, the contributions made in this research on the issue can be summarized as follows:

- The proposed model for predicting the remaining useful life (RUL) of aero-engines can extract effective information from various engine characteristics and demonstrate good performance in subsequent RUL predictions.
- (2) By incorporating a self-attention mechanism into the CNN-LSTM model, the LSTM component pays more attention to the important parts of the features reconstructed by CNN during the final prediction.
- (3) To prevent potential overfitting issues in predicting the RUL of engines, the Dropout method was applied, and the experimental results have proven the effectiveness of this method in the study.

## 2 Algorithm Theoretical Basis

### 2.1 CNN Model

The basic function of a CNN, which is a type of feedforward neural network, is to extract features from input data by applying several filters [24, 42]. Layer by layer, these filters extract aspects of the input data's topological structure by performing pooling and convolution operations. The retrieved features get increasingly abstract as the number of network layers increases gradually, until robust features with translation and rotation invariance are derived from the original input data.

Sparse connection and weight sharing are features of the CNN network itself. Among these, sparse connectivity lowers the number of parameters needed for model training by using spatial topology to create non-fully linked spatial connections between neighboring layers; the algorithm is kept from overfitting by using weight sharing. Furthermore, by using the local characteristics of the data, pooling techniques minimize the data dimension while enhancing feature resilience and network structure optimization.

A CNN network generally consists of an input layer, convolutional layers, pooling layers, fully connected layers, and an output layer. Early on in the CNN feature extraction process, convolutional and pooling layers are alternately used to extract features from the input data layer by layer, and typical multi-layer neural networks are almost fully implemented at the output layer. The convolution kernel of the convolutional layer convolutionizes the output feature vectors from the previous layer, and then uses nonlinear activation functions to construct the output feature vectors. The output of each layer is the convolution of its numerous input properties, which are expressed mathematically as follows:

<span id="page-2-0"></span>
$$x_{j}^{l} = f \left( \sum_{i \in M_{j}} x_{i}^{l-1} * k_{ij}^{l} + b_{j}^{l} \right)$$
 (1)

In Eq. (1),  $M_j$  represents the input feature vector; l represents the l layer of the network; k represents the convolution kernel; b represents the network bias;  $x_i^l$  represents the output of the lth layer; and  $x_i^{l-1}$  represents the input of the lth layer. In CNNs, rectified linear units (ReLUs) are commonly selected as the nonlinear activation function. ReLU has the benefit of allowing certain neurons' output to be zero, which increases the sparsity of the network and decreases parameter dependency, hence minimizing the risk of overfitting. The following is the formulaic representation of ReLU:

$$a_i^{l+1}(j) = f(y_i^{l+1}(j)) = \max\{0, y_i^{l+1}(j)\}$$
 (2)

<span id="page-2-1"></span>In Eq. (2),  $y_i^{l+1}(j)$  represents the output value of the convolution operation;  $a_i^{l+1}(j)$  is the activation value of  $y_i^{l+1}(j)$ 

The pooling layer is a downscaling mapping of the previous layer's data. In practical applications, the max pooling operator is often adopted, which extracts local maxima from the input features, reducing the number of trainable parameters and improving the robustness of the features. The transformation function of max pooling is shown as follows:

$$P_i^{l+1}(j) = \max_{(i-1)W+1 \le i < iW} \left\{ q_i^l(t) \right\} \tag{3}$$

In Eq. (3),  $q_i^l(t)$  represents the value of the tth neuron in the ith feature vector of the lth layer; W is the width of the pooling region;  $P_i^{l+1}(j)$  represents the corresponding value of the l+1 layer neuron.

To discover the group with the highest correlation, all of the aforementioned findings are weighted and summed via the fully connected layer to arrive at the final

<span id="page-2-2"></span>![](_page_2_Picture_22.jpeg)

recognition result. Because of its distinct convolutional structure, CNN can process data more quickly by using a lot less compute and effort. This article selects one-dimensional CNN because the remaining life sequence of the aeroengine is one-dimensional data.

#### 2.2 LSTM Model

LSTM model [8] is a popular and reliable prediction method in the field of remaining usable life prediction. A unique neural network with a memory function, the long short-term memory network (LSTM) modifies the memory state during information transmission via a "gating" mechanism. This allows for selective forgetting and retention of information within the network, allowing information from previous time steps to be transferred to cells in subsequent time steps. When compared to conventional deep learning techniques, LSTM successfully mitigates gradient disappearance to a certain degree, increasing prediction accuracy.

Specifically, LSTM consists of three parts, namely, the forget gate, the input gate, and the output gate, and their functions are as follows:

- (1) The forget gate  $f_t$  controls how much information from the previous internal state  $c_{t-1}$  needs to be forgotten;
- (2) The input  $i_t$  gate controls how much information from the candidate state  $c_t$  at the current moment needs to be saved.
- (3) The output gate  $o_t$  controls how much information from the internal state  $c_t$  at the current moment needs to be output to the external state  $h_t$ .

The calculation formulas for the three gates are as follows:

$$f_{t} = \sigma(W_{f}x_{t} + U_{f}h_{t-1} + b_{f})$$

$$i_{t} = \sigma(W_{i}x_{t} + U_{i}h_{t-1} + b_{i})$$

$$o_{t} = \sigma(W_{o}x_{t} + U_{o}h_{t-1} + b_{o})$$

$$c_{t} = f_{t} \odot c_{t-1} + i_{t} \odot c_{t}$$

$$h_{t} = o_{t} \odot \tanh(c_{t})$$

$$c_{t} = \tanh(W_{c}x_{t} + U_{c}h_{t-1} + b_{c})$$

$$(4)$$

In Eq. (4),  $x_t$  is the input variable;  $c_t$  represented as memory unit;  $c_{t-1}$  is the memory unit of the previous moment;  $W_f$ ,  $W_o$ ,  $W_c$  are, respectively, the input weight vectors of the forgetting gate, the input gate, the output gate and the candidate unit;  $U_f$ ,  $U_i$ ,  $U_o$ ,  $U_c$  are the cyclic weight vectors of each gating unit;  $b_f$ ,  $b_i$ ,  $b_o$ ,  $b_c$  is the bias vector of each gated unit;  $\sigma(\cdot)$  indicates changes in the

![](_page_3_Picture_14.jpeg)

Fig. 1 LSTM neuronal structure

<span id="page-3-1"></span>sigmoid function; tanh is the tanh activation function. See Fig. 1 for LSTM structure diagram.

#### 2.3 Attention

The essential tenet of the attention mechanism is that distinct brain areas require attention at various times. This approach may be used to efficiently lessen the focus of prediction models to other locations at a given time, thus increasing its focus on key regions. This redistribution of attention between key and non-key regions improves the model's prediction accuracy [5, 18, 32]. The attention mechanism can mitigate the situation where LSTM networks lose important information due to excessively long temporal data, by replacing random weight allocation with a probabilistic approach.

In specifically introducing the attention mechanism into a model, the first step is to take the input set as a list of feature vectors as the model's input. At the same time, the model is trained to perform dot-product training on the sample data, generating three different representation vectors for each sample: Q (query), K (key), and V (value).

<span id="page-3-2"></span><span id="page-3-0"></span>
$$Q = W^{Q} \times I$$

$$K = W^{K} \times I$$

$$V = W^{V} \times I$$
(5)

In Eq. (5), I indicates the input data and  $W^Q$ ,  $W^K$ , and  $W^V$  are the weight matrices to be learned. Next, a similarity function F(Q, K) is used to score the samples and obtain the attention scores. Finally, the attention scores are normalized using the softmax function to obtain the weight coefficients for each part.

![](_page_3_Picture_22.jpeg)

$$F(Q, K) = \text{Soft max}\left(\frac{Q \times K^T}{\sqrt{dk}}\right)$$
 (6)

In Eq. (6), F(Q, K) represents the attention matrix, it represents the degree of correlation between the elements in each column; dk represents the data input dimension.

These weight coefficients are then used to perform a dotproduct operation with the known value vector V, resulting in the output of the attention mechanism, attention value.

$$Attention(Q, K, V) = F(Q, K) \times V \tag{7}$$

# 3 Proposed Method

## 3.1 Model Principle and Prediction Framework

#### 3.1.1 Model Principle

The remaining life prediction model of aero-engine built this time is shown in Fig. 2. The specific principle is as follows:

First, the RUL (remaining useful life) of the aeroengine is calculated, and various performance parameters are standardized. The processed features and the remaining useful life of the engine are then input into the model. A CNN network is used to extract and fuse the features, generating several feature maps  $H_-CNN = CNN(x_1, x_2, ..., x_n)$ . Next, the feature maps and their corresponding RUL values are input into the LSTM-Attention network for prediction and the output variable is the RUL value  $H_-out = LSTM - Attention(H_-CNN)$ . Using a comparative analysis technique, the procedure determines the model's

<span id="page-4-0"></span>hyperparameter values. The trained model is then given the test set data to obtain the prediction results and accuracy.

To prevent overfitting of the model, the methods of dropout and early stopping are adopted, which are described as follows:

- (1) Dropout [2]. Dropout can randomly discard a certain proportion of neuron weights during forward propagation, achieving the effect of model averaging ensemble and increasing sparsity, thus preventing the occurrence of co-adaptation relationships between feature detectors. In this model, a certain proportion of weights in the LSTM layer are randomly discarded.
- (2) Early stopping. Determining the model parameters when the validation set error stops decreasing for consecutive iterations as the final parameters can effectively address the overfitting issue that arises during the training process.

#### 3.1.2 Forecasting Framework

As seen in Fig. 3, the methodology for estimating an aeroengine's remaining usable life (RUL) in this article is broken down into three stages: data preprocessing, model establishment, and model training and testing. First, the sensor values are standardized and the engine's RUL is computed and segmented for the dataset. Subsequently, training, validation, and testing sets are created from the processed data. The CNN-LSTM-Attention model developed in this research is then fed the training set, and the validation set is utilized to decide when to end the training. Finally, the testing set is input into the trained model to output the final predicted value and prediction accuracy.

<span id="page-4-1"></span>![](_page_4_Picture_19.jpeg)

Fig. 2 Model structure diagram

![](_page_4_Picture_21.jpeg)

![](_page_5_Figure_4.jpeg)

<span id="page-5-0"></span>**Fig. 3** Experimental fow chart

<span id="page-5-1"></span>**Table 1** C-MAPASS data set

| Dataset           | FD001 | FD002 | FD003 | FD004 |
|-------------------|-------|-------|-------|-------|
| Train data        | 100   | 260   | 100   | 249   |
| Test data         | 100   | 259   | 100   | 248   |
| Working condition | 1     | 6     | 1     | 6     |
| Fault type        | 1     | 1     | 2     | 2     |

# **3.2 Introduction and Analysis of the Experimental Dataset**

C-MAPSS is a turbofan engine dataset that contains degradation data of multi-source performance of turbofan engines under diferent operating conditions and fault modes [\[43\]](#page-11-26). It consists of four sub-datasets, and each dataset can be further divided into a training set, a testing set, and RUL (remaining useful life) labels for the testing set [[20](#page-11-27)]. Specifcally, the training set includes all state parameters of the turbofan engine from startup to a point before failure occurs; the testing set contains state parameters from startup to a certain time point before failure; The remaining useful life of the engine at the last time point in the testing set is represented by the RUL labels, which can be used to gauge how well the prediction model generalizes. Table [1](#page-5-1) displays the fundamental data for the four datasets. It can be seen from the number of test sets and training sets in the table that the test sets and training sets of the four data sets are roughly divided into a ratio of 1:1. The Working condition of Data Set 1 and Data Set 3 is one type, while Data Set 2 and Data Set 4 are two types. In terms of fault types, Data Set 1 and Data Set 2 have the same fault type and are manifested as one type. Data Set 3 and Data Set 4 both have two fault types. To verify the robustness of the remaining life prediction model of aero-engine in this paper, Data Set 2 with multiple working conditions and single fault type is selected for focused discussion, and the other three data sets are also verifed. Data Set 2 has more complex working conditions than Data Set 1 and Data Set 3 with single working condition, and has fewer fault types than Data Set 4 (Table [2\)](#page-6-0).

In the C-MAPSS-FD002 dataset, each engine mainly includes three operational condition monitoring parameters (fight altitude, Mach number, and thrust lever angle) and 21 performance monitoring parameters, as shown in Fig. [2.](#page-4-1)

A visual analysis of the frst nine performance parameters of Engine No. 1 from the training set of Dataset 2 is presented in Fig. [4](#page-7-0). Compared to the engine performance parameters of Dataset 1, the parameters in Dataset 2 do not exhibit a clear degradation trend over time, which is attributed to the presence of six distinct operating conditions in Dataset 2. Consequently, when selecting a model for construction, we favor the use of a convolutional neural network (CNN) model to more fully realize feature interactions and output reconstructed features, which collectively determine the RUL.

![](_page_5_Picture_13.jpeg)

<span id="page-6-0"></span>Table 2 Definition of indicators

| Serial number | Symbol    | Description                     |
|---------------|-----------|---------------------------------|
| 1             | T2        | Total temperature at fan inlet  |
| 2             | T24       | Total temperature at LPC outlet |
| 3             | T30       | Total temperature at HPC outlet |
| 4             | T50       | Total temperature at LPT outlet |
| 5             | P2        | Pressure at fan inlet           |
| 6             | P15       | Total pressure in bypass-duct   |
| 7             | P30       | Total pressure at HPC outlet    |
| 8             | NF        | Physical fan speed              |
| 9             | NC        | Physical core speed             |
| 10            | EPR       | Engine pressure ratio (P50/P2)  |
| 11            | PS30      | Static pressure at HPC outlet   |
| 12            | PHI       | Ratio of fuel flow to Ps30      |
| 13            | NRF       | Corrected fan speed             |
| 14            | NRC       | Corrected core speed            |
| 15            | BPR       | Bypass ratio                    |
| 16            | FARB      | Burner fuel-air ratio           |
| 17            | HT_BLEED  | Bleed enthalpy                  |
| 18            | NF_DMD    | Demanded fan speed              |
| 19            | PCNFR_DMD | Demanded corrected fan speed    |
| 20            | W31       | HPT coolant bleed               |
| 21            | W32       | LPT coolant bleed               |

#### 3.3 Data Preprocessing

#### 3.3.1 Standardized Processing

Considering that the large differences in the dimensions and orders of magnitude of different indicators can affect the prediction effect of the model to a certain extent, while standardized data can help improve the convergence speed of the model. Therefore, we standardize the three operational condition monitoring parameters and 21 performance monitoring parameters, and the calculation formula is as follows:

$$Z_i = \frac{X_i - u}{\sigma} \tag{8}$$

In Eq. (8),  $X_i$  represents the *i*th monitoring indicator in the dataset, u,  $\sigma$  represent the mean and standard deviation of the *i*th monitoring indicator, respectively; and  $Z_i$  represents the *i*th monitoring indicator after standardization.

#### 3.3.2 Life Prediction Evaluation Index

To compare the remaining useful life prediction results of different prediction models, this paper selects the commonly used regression algorithm evaluation metrics, RMSE and MAPE, as the comparative evaluation indicators. RMSE is an indicator that measures the difference between the predicted value output by the model and the true value, while MAPE is the average of absolute errors. The specific calculation formulas are as follows:

RMSE = 
$$\sqrt{\frac{1}{n} \sum_{i=1}^{n} (\hat{y}_{i} - y_{i})^{2}} \text{ MAPE} = \frac{1}{n} \sum_{i=1}^{n} \left| \frac{\hat{y}_{i} - y_{i}}{y_{i}} \right|$$
 (9)

<span id="page-6-2"></span>In Eq. (9),  $\hat{y}$  is the predicted life value and y is the true-life value.

#### 3.3.3 RUL Segmentation

When modeling and predicting the RUL labels, it is necessary to consider the characteristics of the turbofan engine itself. Under normal conditions, the engine's lifetime will decay in a certain way after a period of normal operation [17]. Therefore, this paper adopts a piecewise linear model to represent the remaining useful life decay of an aeroengine. To increase the accuracy of the model prediction, it is assumed that there is no degradation phenomenon during the initial operation phase of the engine, and its lifetime remains constant. Only when it exceeds the turning point of lifetime decay, does the engine's RUL begin to degrade linearly, and its lifetime becomes the actual value. This is specifically shown in Fig. 5. In this figure, the horizontal axis represents the operating cycle, and the vertical axis represents the remaining useful life (RUL). The true RUL is represented by a dashed line, while the adjusted RUL is represented by a red line. Specifically, the adjustment operation is to set the RUL to 100 as a threshold value. When the true life is higher than 100, it is replaced with a life value of 100 and when it is lower than 100, it shows normal decline.

#### <span id="page-6-1"></span>3.3.4 Sliding Window Processing

Due to the long-term periodicity of sensor monitoring data, a sliding window method is adopted to dynamically read data according to a certain step size and window size until the entire data sequence is traversed [39, 41]. The step size is set to 1 in the experiment, and the window size is selected through experimental design. Specifically, moving windows of sizes 30, 35, 40, and 45 are selected, and the results are shown in Fig. 6. As the window size increases, the RMSE decreases. When the window size changes from 35 to 40, the RMSE shows a significant decrease. When the window

![](_page_6_Picture_19.jpeg)

![](_page_7_Figure_4.jpeg)

<span id="page-7-0"></span>**Fig. 4** Partial performance parameters

![](_page_7_Picture_6.jpeg)

**Fig. 5** Demonstration diagram of RUL segmentation processing **Fig. 6** Error diagram of sliding window

<span id="page-7-1"></span>size changes from 40 to 45, the RMSE decreases slightly, but considering that an increase in the window size can lead to the loss of some prediction information for the remaining battery life, this paper sets the moving window size to 40.

![](_page_7_Picture_9.jpeg)

# <span id="page-7-2"></span>**3.4 Predictive Research and Analysis**

The experimental comparison method was used to select hyperparameters in the CNN-LSTM-Attention model and the selection results are shown in Table [3](#page-8-0).

![](_page_7_Picture_13.jpeg)

<span id="page-8-0"></span>**Table 3** Model hyperparameter

| Parameter name                  | Value |
|---------------------------------|-------|
| Input layer size                | 24    |
| CNN layers                      | 1     |
| LSTM layers                     | 1     |
| Attention neuron                | 32    |
| Convolutional kernel size       | [3 1] |
| Numbers of convolutional kernel | 36    |
| CNN stride                      | 1     |
| Pooling size                    | [3 1] |
| Pooling stride                  | 1     |
| LSTM hidden size                | 64    |
| Dropout scale                   | 0.8   |
| Training rounds                 | 25    |
| Batch size                      | 128   |

A comparison of the remaining useful life (RUL) and predicted RUL of four randomly selected aeroengines from the test set is shown in Fig. [7](#page-8-1). During the initial operation of the engines, their various sensor monitoring parameters did not exhibit signifcant degradation characteristics. Therefore, there is a big diference between the predicted remaining life and the original data, which is manifested as up and down fuctuations. As the number of engine operations increases, the battery exhibits degradation characteristics, and the model also demonstrates strong predictive capabilities during this period. Overall, the predicted life of a single engine is consistent with the actual life pattern, and it shows high prediction accuracy in the later stages. Therefore, the model has strong generalization capabilities in dataset 2 with varying operating conditions.

Figure [8](#page-9-0) shows the comparison between the output prediction results of the CNN-LSTM-Attention model in the test set and the actual results in the variable working condition engine dataset. It can be seen from the fgure that most of the predicted remaining lifetimes overlap with the actual remaining lifetimes, and only a few predicted values show large diferences. Therefore, the prediction results are accurate and reliable.

![](_page_8_Figure_9.jpeg)

<span id="page-8-1"></span>**Fig. 7** Real and predicted life of 4 engines in FD002

![](_page_8_Picture_11.jpeg)

<span id="page-9-0"></span>**Fig. 8** Real and predicted residual life of diferent engines

![](_page_9_Figure_5.jpeg)

<span id="page-9-1"></span>**Table 4** Prediction accuracy of diferent data set models

| Dataset | Working<br>condition | Fault type | RMSE   | MAPE  |
|---------|----------------------|------------|--------|-------|
| FD001   | 1                    | 1          | 15.977 | 0.161 |
| FD002   | 6                    | 1          | 14.452 | 0.139 |
| FD003   | 1                    | 2          | 13.907 | 0.115 |
| FD004   | 6                    | 2          | 16.637 | 0.130 |

<span id="page-9-2"></span>**Table 5** Ablation experiment

| Model              | RMSE   | MAPE  |
|--------------------|--------|-------|
| CNN                | 21.574 | 0.232 |
| LSTM               | 18.730 | 0.189 |
| CNN-LSTM           | 17.879 | 0.183 |
| CNN-LSTM-Attention | 14.452 | 0.139 |

To further validate the model's generalization ability for the same fault, training and validation were conducted on three other datasets, and the results are shown in Table [4.](#page-9-1) The test set with the best model performance is FD003 with root mean square error (RMSE) and MAPE of 13.907 and 0.115, respectively. The accuracy of the FD004 dataset is relatively low, with RMSE and MAPE of 16.637 and 0.130, respectively. Therefore, based on the performance of the other datasets, it can be concluded that the aero-engine remaining useful life prediction model built in this paper has strong generalization ability.

# **3.5 Ablation Study**

To verify the efectiveness of the proposed fusion algorithm for predicting the remaining useful life of aero-engines, three

<span id="page-9-3"></span>**Table 6** Prediction accuracy of diferent network models

| Model              | RMSE   | MAPE  |
|--------------------|--------|-------|
| BP                 | 21.868 | 0.262 |
| GRU                | 21.762 | 0.223 |
| CNN-GRU            | 17.863 | 0.178 |
| DCNN               | 19.826 | 0.193 |
| TCNN               | 18.217 | 0.187 |
| CNN-LSTM-Attention | 14.452 | 0.139 |

structures: CNN, LSTM, and CNN-LSTM were selected. With the hyperparameter settings kept unchanged, RMSE and MAPE were used as evaluation metrics for comparison. The results are shown in Table [5.](#page-9-2) As can be seen from the table, when used as individual learners, CNN, LSTM, and CNN-LSTM do not perform as well as the proposed CNN-LSTM-Attention fusion model in terms of prediction accuracy. The RMSE of the fusion model after learning is reduced by approximately 3.427 to 7.122 compared to the individual learners. Therefore, it can be concluded that the proposed fusion model for predicting the remaining useful life of aeroengines has achieved signifcant improvements.

# **3.6 Model Comparison**

To validate the performance of the CNN-LSTM-Attention model, its accuracy in predicting the remaining useful life of variable condition turbofan engines was compared with BP [[2\]](#page-10-8), GRU [\[26](#page-11-31)], LSTM [\[34](#page-11-14)], CNN-GRU [[9\]](#page-10-9), DCNN [\[13](#page-11-12)], and TCNN [[30](#page-11-32)], as detailed in Table [6.](#page-9-3) For BP, the RMSE and MAPE in the lifetime prediction problem both reached around 30. A unique kind of recurrent neural network known as GRU uses a gating mechanism to efciently update and choose data, resulting in prediction accuracy of 0.223 MAPE

![](_page_9_Picture_18.jpeg)

and 21.762 RMSE. While DCNN, TCNN, and CNN-GRU all outperformed the CNN-LSTM-Attention model in terms of prediction accuracy, they fell short in terms of estimating the remaining usable life of variable condition turbofan engines.

# **4 Conclusion**

Estimating an aeroengine's remaining usable life is essential to risk prevention, risk reduction, and improved property and human safety. Optimizing forecast accuracy can also yield more sensible recommendations for engine health management, allowing for the implementation of more sensible maintenance practices.

In response to the question of estimating an aero-engine's remaining usable life, this research suggests a prediction model based on CNN-LSTM-Attention. First, local characteristics are extracted from the aero-engine's sensor data using CNN. The deep mining of data characteristics is then realized by using the LSTM-Attention network to learn and forecast the engine's remaining usable life. Following that, investigations are carried out that compare various models of usable life remaining after ablation. The CNN-LSTM-Attention model performs well in predictions on four datasets, according to experimental results; the RMSEs of the FD001, FD002, FD003, and FD004 datasets are 15.977, 14.452, 13.907, and 16.637, respectively. This model performs better in terms of prediction accuracy on the test datasets when compared to single models and other existing network models. In conclusion, the CNN-LSTM-Attention model shows excellent accuracy and consistency when estimating an aero engine's remaining usable life.

Although the CNN-LSTM-Attention model shows strong performance in predicting the remaining service life of aero engines, the experiment still has some shortcomings. Firstly, the performance of the model on dataset 4 with multiple operating conditions and multiple faults is worse than that on other datasets. Secondly, the prediction model of residual service life of aero-engine under complex work and fault conditions is not considered. Thirdly, this paper mainly focuses on optimizing the prediction accuracy of the remaining service life of the engine from the perspective of model adaptation, and less emphasis is placed on noise reduction and related pre-processing of the data set. Therefore, this paper will optimize the model on future datasets with more failure modes and try to mine more efective information from the data itself.

 **Author contributions** Sizhe Deng and Jian Zhou wrote the main manuscript text. All authors reviewed the manuscript.

 **Funding** This research was funded by the Kashi University China-Pakistan Economic Corridor Research Center Foundation project (grant number 2023HX0158). The funders had no role in the design of the study, data collection and analysis, decision to publish, or preparation of the manuscript.

 **Data availability** No datasets were generated or analyzed during the current study.

# **Declarations**

**Conflict of interest** The authors declare that there are no competing interests.

**Open Access** This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit<http://creativecommons.org/licenses/by/4.0/>.

# **References**

- <span id="page-10-1"></span>1. Ben Ali, J., Chebel-Morello, B., Saidi, L., Malinowski, S., Fnaiech, F.: Accurate bearing remaining useful life prediction based on Weibull distribution and artifcial neural network. Mech. Syst. Signal Process. **56–57**, 150–172 (2015)
- <span id="page-10-8"></span>2. Caceres, J., Gonzalez, D., Zhou, T.T., Droguett, E.L.: A probabilistic Bayesian recurrent neural network for remaining useful life prognostics considering epistemic and aleatory uncertainties. Struct. Control. Health Monit. **28**, e2811 (2021)
- <span id="page-10-5"></span>3. Chang, Y.-S., Chiao, H.-T., Abimannan, S., Huang, Y.-P., Tsai, Y.-T., Lin, K.-M.: An LSTM-based aggregated model for air pollution forecasting. Atmos. Pollut. Res.Pollut. Res. **11**, 1451–1463 (2020)
- <span id="page-10-4"></span>4. Dong, M., He, D.: A segmental hidden semi-Markov model (HSMM)-based diagnostics and prognostics framework and methodology. Mech. Syst. Signal Process. **21**, 2248–2266 (2007)
- <span id="page-10-7"></span>5. Gan, F.F., Shao, H.D., Xia, B.Z.: An adaptive model with dualdimensional attention for remaining useful life prediction of aeroengine. Knowl.-Based Syst. **293**, 111738 (2024)
- <span id="page-10-3"></span>6. Gebraeel, N., Lawley, M., Liu, R., Parmeshwaran, V.: Residual life, predictions from vibration-based degradation signals: a neural network approach. IEEE Trans. Ind. Electron. **51**, 694–700 (2004)
- <span id="page-10-2"></span>7. Gebraeel, N.Z., Lawley, M.A., Li, R., Ryan, J.K.: Residual-life distributions from component degradation signals: a Bayesian approach. IIE Trans. **37**, 543–557 (2005)
- <span id="page-10-6"></span>8. Hochreiter, S., Schmidhuber, J.: Long short-term memory. Neural Comput.Comput. **9**, 1735–1780 (1997)
- <span id="page-10-9"></span>9. Jafari, S., Byun, Y.C.: A CNN-GRU approach to the accurate prediction of batteries' remaining useful life from charging profles. Computers **12**, 219 (2023)
- <span id="page-10-0"></span>10. Lee, J., Wu, F., Zhao, W., Ghafari, M., Liao, L., Siegel, D.: Prognostics and health management design for rotary machinery

![](_page_10_Picture_26.jpeg)

- systems-reviews, methodology and applications. Mech. Syst. Signal Process. **42**, 314–334 (2014)
- <span id="page-11-1"></span>11. Lei, Y.G., Li, N.P., Guo, L., Li, N.B., Yan, T., Lin, J.: Machinery health prognostics: a systematic review from data acquisition to RUL prediction. Mech. Syst. Signal Process. **104**, 799–834 (2018)
- <span id="page-11-2"></span>12. Li, W., Zhong, X., Shao, H.D., Cai, B.P., Yang, X.K.: Multi-mode data augmentation and fault diagnosis of rotating machinery using modifed ACGAN designed with new framework. Adv. Eng. Inform. **52**, 101552 (2022)
- <span id="page-11-12"></span>13. Li, X., Ding, Q., Sun, J.-Q.: Remaining useful life estimation in prognostics using deep convolution neural networks. Reliab. Eng. Syst. Saf.. Eng. Syst. Saf. **172**, 1–11 (2018)
- <span id="page-11-6"></span>14. Liang, Z., Ramakrishnan, K.R., Ng, C.-T., Zhang, Z., Fu, J.: Vibration-based prediction of residual fatigue life for composite laminates through frequency measurements. Compos. Struct. **329**, 117771 (2024)
- <span id="page-11-17"></span>15. Lin, L., Wu, J.L., Fu, S., Zhang, S.H., Tong, C.S., Zu, L.Z.: Channel attention & temporal attention based temporal convolutional network: a dual attention framework for remaining useful life prediction of the aircraft engines. Adv. Eng. Inform. **60**, 102372 (2024)
- <span id="page-11-19"></span>16. Liu, H., Liu, Z.Y., Jia, W.Q., Lin, X.K.: Remaining useful life prediction using a novel feature-attention-based end-to-end approach. IEEE Trans. Industr. Inf.Industr. Inf. **17**, 1197–1207 (2021)
- <span id="page-11-28"></span>17. Liu, H., Liu, Z.Y., Jia, W.Q., Lin, X.K., IEEE.: A novel deep learning-based encoder-decoder model for remaining useful life prediction. International Joint Conference on Neural Networks (IJCNN), Jul 14–19 2019 Budapest, Hungary. (2019)
- <span id="page-11-24"></span>18. Liu, H., Sun, Y.C., Ding, W.H., Wu, H.L., Zhang, H.Y.: Enhancing non-stationary feature learning for remaining useful life prediction of aero-engine under multiple operating conditions. Measurement **227**, 114242 (2024)
- <span id="page-11-15"></span>19. Liu, J., Lei, F., Pan, C., Hu, D., Zuo, H.: Prediction of remaining useful life of multi-stage aero-engine based on clustering and LSTM fusion. Reliab. Eng. Syst. Saf. **214**, 107807 (2021)
- <span id="page-11-27"></span>20. Liu, L., Song, X., Zhou, Z.T.: Aircraft engine remaining useful life estimation via a double attention-based data-driven architecture. Reliab. Eng. Syst. Saf. **221**, 108330 (2022)
- <span id="page-11-20"></span>21. Olivier, J.M., Ron, R., Price, J.C., Forrest, J.S.: Overview of the aviation industry and security in the post-9/11 world. (2016)
- <span id="page-11-10"></span>22. Peng, K., Pi, Y., Jiao, R., Tang, P.: Health indicator construction and remaining useful life prediction for aircraft engine. Control Theory Appl. **37**, 713–720 (2020)
- <span id="page-11-9"></span>23. Remadna, I., Terrissa, L.S., Al Masry, Z., Zerhouni, N.: RUL prediction using a fusion of attention-based convolutional variational autoencoder and ensemble learning classifer. IEEE Trans. Reliab. **72**, 106–124 (2023)
- <span id="page-11-22"></span>24. Ren, G.H., Wang, Y., Shi, Z.Y., Zhang, G.G., Jin, F., Wang, J.: Aero-engine remaining useful life estimation based on CAE-TCN neural networks. Appl. Sci.-Basel **13**, 17 (2023)
- <span id="page-11-13"></span>25. Ruan, D.W., Wu, Y.H., Yan, J.P., IEEE.: Remaining useful life prediction for aero-engine based on LSTM and CNN. 33rd Chinese Control and Decision Conference (CCDC), May 22–24 2021 Kunming, Peoples R China. 6706–6712. (2021)
- <span id="page-11-31"></span>26. Shang, Y.F., Zheng, H., Duan, S.Q., Zhao, D.Z., IEEE.: Prediction of remaining engine life based on multi-sensing fusion. 11th International Conference on Mechanical and Aerospace Engineering (ICMAE), Jul 14–17 2020 Athens, GREECE. 68–71. (2020)
- <span id="page-11-3"></span>27. Si, X.-S., Wang, W., Hu, C.-H., Chen, M.-Y., Zhou, D.-H.: A Wiener-process-based degradation model with a recursive flter algorithm for remaining useful life estimation. Mech. Syst. Signal Process. **35**, 219–237 (2013)

- <span id="page-11-4"></span>28. Simon, D., Simon, D.L.: Constrained Kalman fltering via density function truncation for turbofan engine health estimation. Int. J. Syst. Sci. **41**, 159–171 (2010)
- <span id="page-11-21"></span>29. Strohmeier, M., Schäfer, M., Smith, M., Lenders, V., Martinovic, I.: Assessing the impact of aviation security on cyber power. 8th International Conference on Cyber Confict - Cyber Power (CyCon), May 31-Jun 03 2016 Tallinn, Estonia. 223–241. (2016)
- <span id="page-11-32"></span>30. Wang, H.K., Cheng, Y. Song, K.: Remaining useful life estimation of aircraft engines using a joint deep learning model based on TCNN and transformer. Comput. Intell. Neurosci. 2021, 5185938 (2021).<https://doi.org/10.1155/2021/5185938>
- <span id="page-11-5"></span>31. Wang, Q., Sun, C., Li, Y.L., Liu, Y.C.: Numerical simulation of erosion characteristics and residual life prediction of defective pipelines based on extreme learning machine. Energies **15**, 3750 (2022)
- <span id="page-11-25"></span>32. Wang, X., Li, Y., Xu, Y.X., Liu, X.D., Zheng, T., Zheng, B.: Remaining useful life prediction for aero-engines using a timeenhanced multi-head self-attention model. Aerospace **10**, 80 (2023)
- <span id="page-11-11"></span>33. Xie, C., Zhang, P., Yan, Z.: Correlation analysis of aeroengine operation monitoring using deep learning. Soft. Comput.. Comput. **25**, 551–562 (2021)
- <span id="page-11-14"></span>34. Yuan, M., Wu, Y.T., Lin, L., IEEE.: Fault diagnosis and remaining useful life estimation of aero engine using LSTM neural network. IEEE/CSAA International Conference on Aircraft Utility Systems (AUS), Oct 10–12 2016 Beijing, Peoples R China. 135–140. (2016)
- <span id="page-11-0"></span>35. Zhang, H., Liu, E.H., Zhang, B., Miao, Q.: RUL prediction and uncertainty management for multisensor system using an integrated data-level fusion and UPF approach. IEEE Trans. Ind. Inf. **17**, 4692–4701 (2021)
- <span id="page-11-18"></span>36. Zhang, J.S., Jiang, Y.C., Wu, S.M., Li, X., Luo, H., Yin, S.: Prediction of remaining useful life based on bidirectional gated recurrent unit with temporal self-attention mechanism. Reliab. Eng. Syst. Saf. **221**, 108297 (2022)
- <span id="page-11-8"></span>37. Zhang, Q., Liu, Q., Ye, Q.: An attention-based temporal convolutional network method for predicting remaining useful life of aero-engine. Eng. Appl. Artif. Intell. **127**, 107241 (2024)
- <span id="page-11-16"></span>38. Zhang, Z.G.: Evolution paths of green economy modes and their trend of hypercycle economy. Chin. J. Popul. Resour. Environ. **20**, 105860 (2022)
- <span id="page-11-29"></span>39. Zhao, C.Y., Huang, X.Z., Li, Y.X., Li, S.J.: A novel Cap-LSTM model for remaining useful life prediction. IEEE Sens. J. **21**, 23498–23509 (2021)
- <span id="page-11-7"></span>40. Zhao, K., Jia, Z., Jia, F., Shao, H.D.: Multi-scale integrated deep self-attention network for predicting remaining useful life of aeroengine. Eng. Appl. Artif. Intell. **120**, 105860 (2023)
- <span id="page-11-30"></span>41. Zhou, Z.K., Yang, L.C., Wang, Z., Yao, Y.T., IEEE.: Remaining useful life prediction of aero-engine using CNN-LSTM and mRMR feature selection. 4th International Conference on System Reliability and Safety Engineering (SRSE), Dec 15–18 2022 Electr Network. 41–45. (2022)
- <span id="page-11-23"></span>42. Zhu, J.Y., Ma, J., Wu, J.D.: A regularized constrained two-stream convolution augmented transformer for aircraft engine remaining useful life prediction. Eng. Appl. Artif. Intell. **133**, 108161 (2024)
- <span id="page-11-26"></span>43. Saxena, A., Goebel, K.: Turbofan Engine Degradation Simulation Data Set; NASA Ames Prognostics Data Repository. NASA Ames: Mofett Field, CA, USA (2008)

**Publisher's Note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional afliations.

![](_page_11_Picture_39.jpeg)
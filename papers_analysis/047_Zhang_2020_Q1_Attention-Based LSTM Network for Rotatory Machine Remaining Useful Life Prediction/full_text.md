![](_page_0_Picture_0.jpeg)

Received June 22, 2020, accepted July 14, 2020, date of publication July 17, 2020, date of current version July 29, 2020.

*Digital Object Identifier 10.1109/ACCESS.2020.3010066*

# Attention-Based LSTM Network for Rotatory Machine Remaining Useful Life Prediction

HAO ZHANG [1](https://orcid.org/0000-0001-6223-6535) , QIANG ZHANG<sup>2</sup> , SIYU SHA[O](https://orcid.org/0000-0003-3180-2180) <sup>2</sup> , (Member, IEEE), TIANLIN NIU<sup>2</sup> , AND XINYU YANG<sup>2</sup>

<sup>1</sup>Graduate School, Air Force Engineering University, Xi'an 710051, China

<sup>2</sup>Air and Missile Defense College, Air Force Engineering University, Xi'an 710051, China

Corresponding author: Siyu Shao (cathygx.sy@gmail.com)

This work was supported by the National Natural Science Foundation of China under Grant 61372033.

**ABSTRACT** As one of the key components in mechanical systems, rotatory machine plays a significant role in safe and stable operation. Accurate prediction of the Remaining Useful Life (RUL) of rotatory machine contributes to realization of intelligent operation and maintenance for mechanical manufacturing. In order to overcome the limitations of traditional machine learning algorithms in dealing with complex nonlinear signals, a novel prediction framework for RUL of rotatory machine based on deep learning is proposed in this paper. One-dimensional convolutional neural network is utilized to extract local features from the original signal sequence. In addition, the proposed framework analyzes sensor signals and predicts RUL by combining Long Short-Term Memory (LSTM) network with attention mechanism. Multi-layer LSTM is set up to extract useful temporal features layer by layer and improve the robustness of the model, while attention mechanism is able to effectively solve the problem of information loss in the long-distance signal transmission of LSTM. Through the feature extraction of multi-layer LSTM and the strong supervision ability of attention mechanism, the RUL of rotatory machine can be accurately predicted. The experimental results show that the proposed method for RUL estimation is efficient and has higher prediction accuracy than the traditional machine learning algorithms.

**INDEX TERMS** Rotatory machine, deep learning, long short-term memory, attention mechanism, remaining useful life.

# **I. INTRODUCTION**

Electro-mechanical systems are widely used in nowadays industrial manufacture. Due to the increasing system complexity, it is crucial to conduct engineering maintenance and prognostics to ensure system efficiency and reliability. As a key component of mechanical systems, rotatory machine has significant influence upon the whole system, and the degradation of rotatory machine may lead to deadly industrial accidents. Therefore, prognostics and health management (PHM) technology is highly desired to reduce maintenance costs and to improve system reliability and safety. PHM uses advanced technology to evaluate the working condition of the mechanical systems and predict the fault location, failure time and remaining useful life (RUL) [1]–[3]. Continued advancement in intelligent manufacturing has led to an ever-increasing attention on equipment fault diagnosis and its

The associate editor coordinating the review of this manuscript and approving it for publication was Moussa Boukhnife[r](https://orcid.org/0000-0002-1729-5453) .

RUL estimation. Accurate RUL prediction helps to prevent sudden accidents and therefore contributes to efficient and reliable industrial manufacture [4]–[6].

Generally, there are two main kinds of methods that are commonly used in RUL prediction, model-based methods and data-driven methods. Model-based methods rely on mathematical principles such as statistics and probability [7], [8], which try to establish accurate mathematical models through prior knowledge to predict the equipment RUL. However, prior knowledge dependence may lead to insufficient generalization, and human participation is also needed which is time consuming and laborious. How to mine the potential characteristics of data and establish an accurate model is a difficult problem to be solved by model-based methods. With the development of technology and the generation of big data, traditional PHM strategies are becoming unable to meet the increasing industrial requirements, and more and more intelligent RUL approaches based on machine learning and big data analysis are

![](_page_1_Picture_1.jpeg)

emerging [9], [10]. Data-driven methods aim at exploring the potential relationship between monitored sensor data and its RUL value based on historical data. As the emergence of artificial intelligence, signal processing and analysis technology, deep learning-based approaches have gradually become the mainstream of RUL prediction [11], [12]. Deep learning model is designed to build deep neural network architectures to model human learning process from massive data, which is able to form high-level representations by combining low-level features to discover the distributed representations of data [13]. It can be regarded as a supervised/unsupervised machine learning technology with multiple hidden layers of neural network. Compared with traditional RUL prediction methods, deep learning-based methods have strong feature learning ability, which can automatically extract hierarchical representations from a large number of samples through layer by layer abstraction, reducing the resource consumption of human participation [14]–[17]. Moreover, the complex mapping relationship between signals and working condition can be well represented through the training of deep model [18]. Therefore, the application of deep learning to RUL prediction provides a new solution for this research area.

Due to the superior feature learning ability, deep learningbased models enable data-driven approaches great potential in the research field of RUL prediction [19], [20]. Zhu *et al.* designed a multiscale convolutional neural network to evaluate equipment, which obtained desired prediction results [21]. The network strengthens the connection between local information and global information compared to traditional convolutional neural network. Recurrent Neural Network (RNN) was proposed to model the distribution of time series data [22], and for effectively dealing with long time series to overcome the problem of gradient disappearance or gradient explosion due to the length of the sequence, LSTM, a variant of RNN, was proposed, which has made great achievements in the field of long time series prediction [23], [24]. As the increasing in data complexity, single LSTM network has its limitations on modeling sequence of time-domain signal. Wang *et al.* designed a residual LSTM network framework to solve the degradation problem of the deep LSTM model, and verified the superiority of the structure by experiments [25].

Attention mechanism is an effective way to enhance model feature learning ability, which can be regarded as the further screening of data information to highlight the key parts of information so as to achieve analysis and accurate prediction. The deep neural network combined with the attention mechanism has been successfully applied in a variety of tasks such as machine translation [26], handwriting synthesis [27], visual object classification [28] and image caption generation [29]. In this paper, a deep learning-based model combining attention mechanism with LSTM network is proposed to improve model performance in terms of efficiency and effectiveness. Experiments show that the proposed framework can accurately predict the RUL of the rotatory machine. The contributions of this paper are as follows:

- 1. A stacked two-layer LSTM network is established, which allows hidden output not only to be propagated to adjacent LSTM cells, but also to be treated as the input to the next LSTM layer. More hidden layers enable more accurate distribution between network input and output by observing the mapping relation in multi-dimensional space, which improves the model ability in dealing with nonlinear data.
- 2. By integrating the attention mechanism and two-layer LSTM into a framework, the proposed framework is able to accurately capture the key information of the input signal, whose performance in RUL prediction exceeds the traditional LSTM-based methods.

The rest of the paper is organized as follows. Section II introduces the theoretical background of the proposed method, including convolutional neural networks, LSTM and attention mechanism. In Section III, the overall RUL prediction framework is illustrated in detail. In Section IV, experimental studies are carried out to verify the effectiveness of the proposed model, together with performance comparisons with other methods. Conclusions and future work are presented in Section V.

# **II. THEORETICAL BACKGROUND**

# A. BASIC THEORY OF CNN

Convolutional neural network (CNN) is one of the most successful applications of deep learning algorithms, which has extraordinary feature expression and feature learning ability [30]. CNN-based model has made several remarkable achievements in the field of computer vision, such as target detection, image segmentation and object recognition. The unique network structure of CNN can effectively reduce the complexity of the feedback neural network. In addition, CNN also has superior performance in dealing with one-dimensional sequence data, including natural language processing (NLP) and speech recognition. One Dimensional Convolutional Neural Network (1DCNN) uses multiple local filters to extract features of the input signal sequence and the corresponding feature maps are generated by sliding the filters over the sequence. The weights of the windows in each convolution layer are shared, which reduces the number of parameters [31], [32]. 1DCNN can effectively analyze the signal data with fixed length period and extract important features from it.

The 1DCNN is composed of convolution layer and pooling layer to process time series data. Each convolutional layer is composed of several convolutional units, and the parameters of each convolutional unit are optimized by back-propagation algorithm. The purpose of the convolution layer is to extract different features of the input. The first convolutional layer extracts low-level features, while more hidden layers can iteratively extract more complex features from low-level features. The pooling layer is used to compress extracted features and generate more critical feature information. The specific

![](_page_2_Picture_1.jpeg)

![](_page_2_Picture_2.jpeg)

FIGURE 1. Working principle of RNN.

calculation method is as follows:

<span id="page-2-0"></span>
$$a_{i:i+m-1} = a_i \oplus a_{i+1} \oplus \cdots \oplus a_{i+m-1} \tag{1}$$

$$x_i = f(u^T a_{i:i+m-1} + b)$$
 (2)

The multiplication of vectors between convolution layers is shown in the formula (1)-(2),  $a_{i:i+m-1}$  represents m continuous time windows at the beginning of the i-th time step,  $\oplus$  means stacking the different time windows. x is the result of convolution operation. T is the matrix transpose. b represents the bias. f() is the Rectified Linear Unit (ReLu) activation function, and u can be regarded as the filter.

The pooling layer refers to descending sampling operation, which is carried out after feature extraction in the convolution layer. The vector extracted by the convolution layer can be expressed as  $x_j = [x_1, x_2, \cdots x_{l-m+1}]$ , j represents the j-th filter. Assuming that the step size of the pooling layer is n, the vector extracted from the maxpooling layer is the largest value of continuous n values in  $x_j$ .

The compressed vector can be expressed as  $p = [p_1, p_2, p_i, \dots, p_{(l-m)/n+1}]$ , here

$$p_i = \max[x_{(i-1)n}, x_{(i-1)n+1}, \cdots, x_{in-1}].$$

### B. RECURRENT NEURAL NETWORK AND LSTM

As shown in Fig.1, RNN is composed of a certain number of recurrent neurons. Input sequence  $x = (\cdots x_{(t-1)}, x_{(t)}, x_{(t+1)} \cdots)$  is fed into the neurons, generating the output of each corresponding neuron  $h = (\cdots h_{(t-1)}, h_{(t)}, h_{(t+1)} \cdots)$ . The subscripts in the Fig.1 represent the time steps for each sequence. Different from the traditional neural networks, the recurrent neuron output is connected to the next neuron, which enables the network to learn the sequence characteristics from different time. The output of a single neuron can be expressed as:

$$h_{(t)} = \tanh(w_x x_{(t)} + w_h h_{(t-1)} + b) \tag{3}$$

where  $w_x$  and  $w_h$  represent the weight vector. b is the bias.

When the time step of the input sequence is large, it is difficult to train the standard RNN. Thus, LSTM is proposed to solve the training difficulty when dealing with long sequence data. Compared with the traditional RNN, LSTM controls the transmission state through the gated state. The forget gate  $f_{(t)}$  controls whether the input removes the previous information after a long state  $c_{(t-1)}$ . The function of the input gate  $i_{(t)}$  is

![](_page_2_Picture_16.jpeg)

FIGURE 2. Structure of LSTM neural network.

used to estimate whether to let the input information into the current memory cell state  $c_{(t)}$ . The function of the output gate  $o_{(t)}$  is much the same as the input gate, it is used to determine whether to output the current signal to the next layer. The structure of LSTM network is shown in figure 2.

<span id="page-2-1"></span>
$$f_{(t)} = \sigma(W_f x_{(t)} + V_f h_{(t-1)} + b_f) \tag{4}$$

$$i_{(t)} = \sigma(W_i x_{(t)} + V_i h_{(t-1)} + b_i)$$
(5)

$$o_{(t)} = \sigma(W_o x_{(t)} + V_o h_{(t-1)} + b_o)$$
(6)

$$c_{(t)} = f_{(t)} \otimes c_{(t-1)} + i_{(t)} \otimes \tanh(W_c x_{(t)} + V_c h_{(t-1)} + b_c)$$
 (7)

$$h_{(t)} = o_{(t)} \otimes \tanh(c_{(t)}) \tag{8}$$

Formula (4)-(8) shows the calculation principle of each gate structure. Where  $x = (x_1, x_2 \dots x_n)$  is an input sequence and  $h = (h_1, h_2 \dots h_n)$  is an output sequence, W and V are the weight matrix, b represents the threshold,  $\sigma(x) = 1/1 + e^{-x}$  is the sigmoid activation function,  $\otimes$  is the dot product.

#### C. STACKED LSTMs

In order to improve the learning ability of LSTM network, multiple LSTMs can be stacked into layers. Zhou et al. explored the advantages of deep stacked LSTMs in handwriting recognition and sentiment analysis [33]. Wang et al. explored a variety of ways to combine multiple single LSTM layers together and discussed the advantages and disadvantages of deep LSTMs [25]. In this paper, two LSTMs are stacked as part of the model architecture. By stacking the LSTM layers, the output of the hidden layer can be propagated not only to the adjacent LSTM cells, but also as the input to the next LSTM layer. More hidden layers enable the model to discover the distribution between network input and output by observing the mapping relation in multi-dimensional space and improve the ability of the model to deal with nonlinearity. As shown in the figure 3, each LSTM layer outputs a sequence of vectors that will be used as the input for the subsequent LSTM layers. The n-th layer can be updated by formula (9)-(13).

<span id="page-2-2"></span>
$$f_{(t)}^{n} = \sigma(W_f^n h_{(t)}^{n-1} + V_f^n h_{(t-1)}^n + b_f^n)$$
(9)

$$i_{(t)}^{n} = \sigma(W_{i}^{n} h_{(t)}^{n-1} + V_{i}^{n} h_{(t)}^{n} + b_{i}^{n})$$
(10)

$$o_{(t)}^{n} = \sigma(W_{o}^{n} h_{(t)}^{n-1} + V_{o}^{n} h_{(t-1)}^{n} + b_{o}^{n})$$
(11)

$$c_{(t)}^{n} = f_{(t)}^{n} \otimes c_{(t-1)}^{n} + i_{(t)}^{n} \otimes \tanh(W_{c}^{n} h_{(t)}^{n-1} + V_{c}^{n} h_{(t-1)}^{n} + b_{c}^{n})$$
(12)

$$h_{(t)}^n = o_{(t)}^n \otimes \tanh(c_{(t)}^n) \tag{13}$$

![](_page_3_Picture_1.jpeg)

![](_page_3_Figure_2.jpeg)

**FIGURE 3.** Diagram of a two-layer LSTM networ.

The input of the first layer is the feature maps extracted by CNN while the output of the first layer is regarded as hierarchical features. Stacking multiple LSTM layers enables the model to recompose the representations learned from previous layer, and new representations with high level of abstraction can be achieved. The model parameters are distributed in the whole space of the model, which can accelerate the training convergence and perform better nonlinear operation on the data. Although a single LSTM can solve certain problems that existing in RNN, it is still very difficult to deal with long and complex sequences. Using two-layer LSTM as part of the network structure can make the hidden layer more closely related, so as to improve the prediction accuracy.

# D. ATTENTION MECHANISM

The attention mechanism in neural network is a resource allocation scheme to allocate computing resources to more important tasks and solve the problem of information overload with limited computation resource. In neural networks, the more parameters a model has, the stronger feature expression ability it will has, and the more information stored by the model will be. However, this may lead to the problem of information overload. By introducing the attention mechanism, the network is able to focus on the information that is more critical to the current task among many input information, reducing the attention to other useless information. Generally speaking, attention mechanism can solve the problem of information overload and improve the model efficiency and accuracy.

Through attention mechanism, better model is obtained by combining the elements with the attention distribution coefficients. Attention mechanism preserves the intermediate results of the training model, selectively learns these intermediate results, and associates the output sequence with them by assigning weights [28]. In addition, compared with the traditional RNN, attention mechanism is able to be computed in parallel where the calculation of each step no longer depends on the calculation results of the previous step. Therefore, the attention mechanism has fewer parameters and more efficient calculation.

The calculation of attention value can be divided into two steps: [\(1\)](#page-2-0) calculate attention distributions among all input information; [\(2\)](#page-2-0) calculate the weighted average of input information according to the attention distributions.

![](_page_3_Picture_9.jpeg)

**FIGURE 4.** Principle of the attention mechanism.

The formula [\(14\)](#page-3-0)-[\(17\)](#page-3-0) show the computational principles of the attention mechanism. Hidden state variable *h<sup>t</sup>* is obtained by the input *x* and the previous hidden state variable *ht*−1. *c<sup>i</sup>* is the weighted average of the next hidden layer unit and all hidden layers of the RNN layer. α represents the corresponding weight ratio between two hidden layer units. *h<sup>s</sup>* is the target value.*s*represents the weight calculation method.

<span id="page-3-0"></span>
$$h_t = RNN(x_t, h_{t-1}) \tag{14}$$

$$c_i = \sum_{j=1}^n \alpha_{ij} h_j \tag{15}$$

$$\alpha_{ij} = \frac{\exp(s(h_t, \overline{h_s}))}{\sum_{k=1}^{n} \exp(s(h_t, \overline{h_s}))}$$
(16)

$$s(h_t, \overline{h_s}) = h_t \overline{h_s} \tag{17}$$

# E. DEEP LSTMs WITH ATTENTION MECHANISM

As the input of the network is one-dimensional vibration signal, the signal contains a large number of useless information for RUL prediction, and it is difficult to effectively filter this information using a single LSTM network, which will cause interference to the final prediction accuracy. In order to establish a model with high prediction accuracy, the proposed model combines the attention mechanism with the two-layer LSTM network. The traditional LSTM may code sequence into a fixed-length vector representation no matter the length of the input signal sequence, which limits the model learning ability for the long sequence. The attention mechanism enables closer connection between hidden layers and emphasizes important information through the allocation of weight coefficients to improve the prediction accuracy.

Through the LSTM encoder, the combined attention mechanism is utilized to preserve the intermediate output. Where the proposed model is trained to selectively learn useful representations from the input sequence and provide the correlation between the output sequence and the input. As shown in figure 5, attention mechanism calculates the score value corresponding to each variable through the intermediate variables of the LSTM hidden layers. The weight value of each variable indicates the corresponding degree of importance. Finally, the context vector layer will integrate the information

![](_page_4_Picture_2.jpeg)

FIGURE 5. Diagram of the two-layer LSTM with attention mechanism.

and capture the key feature information in the input sequence, where the key feature information will be given a higher weight.

The formula (18)-(22) shows the update rules of each parameter after LSTM combined with the attention mechanism.

<span id="page-4-0"></span>
$$\begin{pmatrix} f_{(t)}^n \\ i_{(t)}^n \\ o_{(t)}^n \\ g_{(t)}^n \end{pmatrix} = \begin{pmatrix} \sigma \\ \sigma \\ \sigma \\ \tanh \end{pmatrix} Z_{L+M}^n \begin{pmatrix} Ed_{t-1}^n \\ h_{t-1}^n \\ v_t \end{pmatrix}$$
(18)

$$v_t = \sum_{i}^{N} \beta_i^t x_i \tag{19}$$

$$s_i^t = W_s \tanh(W_h h_{(t-1)}^n + W_x x_i + b_s)$$
 (20)

$$s_{i}^{t} = W_{s} \tanh(W_{h} h_{(t-1)}^{n} + W_{x} x_{i} + b_{s})$$
 (20)  
$$\beta_{i}^{t} = \frac{\exp(s_{k}^{t})}{\sum_{k=1}^{N} \exp(s_{k}^{t})}$$
 (21)

$$\sum_{i=1}^{N} \beta_i^t = 1 \tag{22}$$

where  $Z_{L+M}^n$  denotes the parameters of *n*-th layer in LSTM model and  $\sigma$  is the sigmoid function.  $Ed_{t-1}^n$  represents an embedding matrix, L is the dimensionality of the LSTM network. Where  $v_t$  denotes the context vector which is a representation of the relevant vector of the input at time t. M represents the dimension of  $v_t$ .  $\beta_i^t$  is the attention weights given by the relevance score  $s_i^t$ . The network is able to obtain the attention weights once the relevant scores for the features  $X = \{x_1, x_2, \dots, x_N\}$  are computed.

Through the amplification of weights, the neural network will focus on learning the corresponding data. To sum up, the weight matrixes used in the proposed LSTM at the time instant t' are given by

$$w'_{t',ih} = w_{t',ih}\beta_{t'} (23)$$

$$w'_{t',oh} = w_{t',oh}\beta_{t'} \tag{24}$$

$$w'_{t'\ fh} = w_{t',fh}\beta_{t'} \tag{25}$$

![](_page_4_Picture_16.jpeg)

FIGURE 6. The flowchart of LSTM with attention mechanism.

where

$$\beta_{t'} = \begin{bmatrix} 1 + \beta_{t',1} & 1 + \beta_{t',1} & , \cdots, & 1 + \beta_{t',1} \\ 1 + \beta_{t',2} & 1 + \beta_{t',2} & , \cdots, & 1 + \beta_{t',2} \\ \vdots & \vdots & & \vdots \\ 1 + \beta_{t',m} & 1 + \beta_{t',m} & , \cdots, & 1 + \beta_{t',m} \end{bmatrix}_{m \times m}.$$

Fig.6 illustrates the flowchart of LSTM with attention mechanism.

#### **III. PREDICTION NETWORK**

In this section, a novel RUL prediction model is proposed, which is mainly composed of three parts: 1DCNN-based feature extraction, deep LSTMs with attention mechanism, and fully connected layers. The whole model architecture is shown in the figure 7. The signal sequence is firstly extracted by 1DCNN. 1DCNN can extract important features from the signal data effectively through convolution and pooling operation. Each convolution kernel in the convolution layer extracts a certain kind of features, and various convolution kernels enable different feature maps. Max-pooling is adopted in the pooling layer. Furthermore, two-layer LSTM with attention mechanism learns higher level representations. Stacked LSTMs makes the network more compact and enables the model to learn features of the original data at each time point. The proposed model utilizes attention mechanism to selectively learn from the input and associate the output sequence with the input to improve the prediction accuracy. The output of two-layer LSTM with attention mechanism is fed into fully-connected layers. Finally, the RUL prediction results are predicted through the fully connected layers.

Before training, the data is reconstructed into a matrix X in chronological order. Each column of the matrix represents the signal sequence of each stage, corresponding to the RUL value respectively. Therefore, the input can be expressed as  $X = [X_t, X_{t-1}, \dots, X_{t-a-1}]$ . a represents the number of the samples selected. The output is expressed as RUL = $[RUL_t, RUL_{t-1}, \dots, RUL_{t-a-1}]$ . Since the amplitude of the signal sequence is much smaller than the RUL value, it is

![](_page_5_Picture_1.jpeg)

![](_page_5_Figure_2.jpeg)

**FIGURE 7.** Flowchart of the proposed RUL method.

#### **TABLE 1.** Model training process.

$$L = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y^{i} - RUL^{i})^{2}}$$

$$w \leftarrow \operatorname{Adam}(\nabla_w \sum_{r=1}^n L, w)$$

$$b \leftarrow \operatorname{Adam}(\nabla_b \sum_{r=1}^n L, b)$$

necessary to normalize the real RUL value to help train the model and achieve the accurate prediction. The formula [\(26\)](#page-5-0) is the normalization formula. Min represents the minimum value of the RUL, Max means the maximum value of the RUL.

<span id="page-5-0"></span>
$$RUL = \frac{RUL - RUL_{\min}}{RUL_{\max} - RUL_{\min}}$$
 (26)

Detailed information of model training process for RUL prediction is illustrated in Table 1.

In order verify the effectiveness of the proposed model, the trained model is used to predict both the future vibration signal sequence and RUL value of the rotatory machine.

For the prediction of future time signal, assuming input signal is *u<sup>t</sup>* = [*u*1, *u*2, . . . *up*], signal length is *p*. The signal value at next moment *up*+<sup>1</sup> can be predicted by the trained model. Then the input signal is updated into *ut*+<sup>1</sup> = [*u*2, *u*3, . . . *up*, *up*+1], and *ut*+<sup>2</sup> is updated from *ut*+1. Repeat this step until the prediction is complete.

The network adopts supervision training, and the parameters of the model are randomly initialized. Errors are generated by comparing the predicted results with the expected outputs. The relative error is calculated by the given cost function, and the initial weights are updated according to the gradient direction. The parameter update process is repeated until the value of the cost function is decreased below the preset threshold or the training process reaches the predefined number of iterations. In the actual training process, the complete training data set is put into the network in batches, and the cost function is adjusted by using the Adaptive Moment estimation (Adam) optimizer. Adam optimizer calculates the adaptive learning rate of each parameter and limits the update step size to a general range. Adam optimizer is able to adjust the learning rate automatically during training.

# **IV. EXPERIMENT AND ANALYSIS**

To explore the performances of model and validate its effectiveness, several experiments are carried out on bearing dataset. The dataset contains vibration data of various bearings collected at Xi'an Jiaotong University (XJTU) and the Changxing Sumyoung Technology (SY). The entire data contains the whole process of bearing from run-to-failure tests under different conditions. The whole experiments are divided into two parts. One is designed to verify the model prediction ability for future time series. The other is to verify the model prediction ability for the bearing RUL value. Through the comparisons of several models, the advantages and disadvantages of each model are discussed. Finally, the performances under different model structures are tested and discussed.

# A. DATA DESCRIPTION

The experimental data were collected by the bearing testbed. As shown in the figure 8, the testbed is composed of AC induction motor, a support shaft, a speed motor, two support

![](_page_6_Picture_2.jpeg)

**FIGURE 8.** Bearing contact fatigue testing machin.

**TABLE 2.** Details of experiment datasets.

| On anatin a                  | Danning    | Daarina   | Fault      |
|------------------------------|------------|-----------|------------|
| Operating                    | Bearing    | Bearing   | raun       |
| condition                    | dataset    | lifetime  | element    |
| Condition 1<br>(35Hz/12kN)   | Bearing1_1 | 2h 3min   | Outer race |
|                              | Bearing1_2 | 2h 41min  | Outer race |
|                              | Bearing1_3 | 2h 38min  | Outer race |
|                              | Bearing1_4 | 2h 2min   | Cage       |
|                              | Bearing1_5 | 52min     | Inner race |
| Condition 2<br>(37.5Hz/12kN) | Bearing2_1 | 8h 11min  | Inner race |
|                              | Bearing2_2 | 2h 41min  | Outer race |
|                              | Bearing2_3 | 8h 53min  | Cage       |
|                              | Bearing2_4 | 42 min    | Outer race |
|                              | Bearing2_5 | 5h 39min  | Outer race |
| Condition 3<br>(40Hz/10kN)   | Bearing3_1 | 42h 18min | Outer race |
|                              | Bearing3_2 | 41h 36min | Cage       |
|                              | Bearing3_3 | 6h 11min  | Inner race |
|                              | Bearing3_4 | 25h 15min | Inner race |
|                              | Bearing3_5 | 1h 54min  | Outer race |

bearings, a hydraulic loading system. The testbed is designed for the degradation test of rolling bearings under different working conditions [34]. Table 2 shows the detailed description of the experimental data. Four different fault types are set, including inner race wear, cage fracture, outer race fracture and out race wear.

Figure 9 shows the boxplot of Bearing1\_4 amplitude values in each different stage. It is illustrated that the amplitude value of the signal has a significant increase after a certain time. It indicates that the bearing is obviously degraded at this moment, and the probability of failure is much higher than that of normal operation. The main task of the proposed model is to accurately predict the residual life of the target bearing in the failure stage, which has great importance to industrial production.

# B. BUILDING AND TRAINING

The detailed framework of the proposed model is illustrated in Section III, and in this part, the specific parameters of the model during experimental verification are introduced.

![](_page_6_Figure_10.jpeg)

**FIGURE 9.** The boxplot of Bearing1\_4 amplitude values.

Before model training, data preparation for training and testing data is adopted. In order to obtain effective training process, the standard normalization method is conducted on the input data.

The following methods will be compared with the proposed model:

CNN: Convolution layer with max-pooling

CNN\_MLP: CNN combined with Multi-Layer Perception (MLP)

CNN\_SVR: CNN combined with Support Vector Regression (SVR)

RNN: Basic RNN with CNN

OLSTM: One-layer LSTM with CNN TLSTM: Two-layer LSTM with CNN

OLSTM-A: One-layer LSTM with Attention mechanism and CNN

TLSTM-A: Two-layer LSTM with Attention mechanism and CNN

Since MLP and SVR have limited ability to extract the signal features, the convolution layer is combined with the models respectively. In SVR, the value of regularization parameter C is from {0.001, 0.01, 0.1, 1,10}. In MLP, we design three fully connected layers, the number of neurons in each layer is 64, 32, 1 respectively.

As for the proposed framework, the one-dimensional convolution layer consists of 16 convolution kernels, each kernel size is 64 and the activation function is ''ReLu'' function. The pooling layer adopts the maximum pooling and the step size is set to 2. The number of LSTM neurons in both layers is 128, and the number of attention neurons is the same as LSTM. Multi-layer LSTM is followed by three fully connected layers, the number of which is 64, 32 and 1 respectively. The last layer outputs the actual predicted RUL or vibration amplitude of the sensor data. The loss function of the model is set as Root-Mean-Square Error (RMSE), and RMSE is shown in the formula [\(27\)](#page-6-0), *y* represents the prediction of the model, and *RUL* represents the real RUL value. The Adam optimizer is used in the training process, where the initial learning rate is set to 0.005.

<span id="page-6-0"></span>
$$RMSE = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y^{i} - RUL^{i})^{2}}$$
 (27)

![](_page_7_Picture_1.jpeg)

![](_page_7_Figure_2.jpeg)

**FIGURE 10.** Future signal prediction results in different datasets.

## C. DEGRADATION TRACKING

As for the prediction of future time series, the methods mentioned in the previous section are used for comparison. Different from predicting RUL value, in order to maintain the effectiveness of network model training, the data set is not normalized. Since the amplitude of the signal is smaller than the RUL value, it is better to train the model without normalization.

The figure 10 shows the prediction results of the future signal sequence by the proposed model in three different kinds of fault data sets. The amplitude of the signal in the future is predicted by the input data sets. It can be seen from the figure that the proposed approach is able to model the time series and provide accurate prediction of the changing trend for the vibration amplitude in the future although the prediction effect at some points is not satisfactory. The RMSE values for each model are shown in Table 3. The prediction of future time series still belongs to the analysis of signal sequence in essence, so prediction performance of linear model is still unsatisfactory. Due to the combination of two-layer LSTM and attention mechanism, the feature extraction ability of our model is significantly improved compared with other models.

# D. BEARING RUL PREDICTION AND RESULTS

As each RUL prediction is independent, the continuity of the predicted results is limited. Actually, based on the continuity requirements, the predicted RUL is smoothed to achieve consistence with the actual situation. For the experimental verification in this section, the predicted results were smoothed by the linear smoothing method, and the linear smoothing is

**TABLE 3.** RMSE for different methods on degradation tracking.

| Methods | Datasets   |            |            |
|---------|------------|------------|------------|
|         | Bearing1_1 | Bearing1_5 | Bearing2_4 |
| CNN     | 12.33      | 13.58      | 13.89      |
| CNN_SVR | 9.96       | 10.32      | 12.51      |
| CNN_MLP | 10.21      | 11.35      | 12.59      |
| RNN     | 6.96       | 6.56       | 7.88       |
| OLSTM   | 6.78       | 6.33       | 7.45       |
| TLSTM   | 5.89       | 5.24       | 6.79       |
| OLSTM-A | 3.15       | 2.67       | 4.46       |
| TLSTM-A | 1.88       | 1.32       | 2.34       |

performed by every 10 points. The data of each fault type will be used as the training data set. The test set information will not appear in the training mode. It can be used for cross prediction of the same type of bearing. The core of our paper is to predict the residual life of bearing in the failure stage. The probability of bearing damage in failure stage is high, so it is necessary to predict the remaining useful life of bearings in the failure stage to prevent accidents from happening.

To comprehensively assess the performance of the RUL estimation approach, more metrics are used for further comparison, including Mean Absolute Deviation (MAE) and Score function. The Score function in the IEEE PHM 2012 challenge [21] is defined as formula [\(28\)](#page-7-0)-[\(30\)](#page-7-0). Where *E<sup>i</sup>* denotes the percent error for the *i*-th experiment, *y* represents the prediction of the model, and *RUL* represents the real RUL value. The score function can objectively judge the fitting degree of RUL curve. The higher the score, the better the prediction effect of RUL.

<span id="page-7-0"></span>
$$Score = \frac{1}{n} \sum_{i=1}^{n} A_i \tag{28}$$

$$A_{i} = \begin{cases} \exp(-\ln(0.5) \times (E_{i}/5), & E_{i} \leq 0\\ \exp(-\ln(0.5) \times (E_{i}/20), & E_{i} \geq 0 \end{cases}$$
 (29)

$$E_i\% = \frac{RUL_i - y_i}{RUL_i} \times 100 \tag{30}$$

$$MAE = \frac{1}{n} \sum_{i=1}^{n} |RUL_i - y_i|$$
 (31)

In this part, comparison experiments are given with several models mentioned in the previous section and Table 4 to VI show the evaluation indicator of all methods on three datasets. It can be seen from the Tables that although CNN has strong feature extraction ability, its prediction ability for time series is poor. For linear models such as SVR and MLP, even if the input sequence is the extracted features by CNN, the prediction accuracy is still lower than that of recurrent models. It shows that the recurrent model has its own advantages in the analysis and prediction of signal sequences.

![](_page_8_Figure_2.jpeg)

**FIGURE 11.** RUL prediction performances on various models from bearing1\_5.

**TABLE 4.** RMSE for different methods on RUL prediction.

| Methods | Datasets   |            |            |
|---------|------------|------------|------------|
|         | Bearing1_1 | Bearing1_5 | Bearing2_4 |
| CNN     | 495.67     | 550.69     | 580.64     |
| CNN_SVR | 301.35     | 396.53     | 368.57     |
| CNN_MLP | 402.69     | 449.36     | 458.85     |
| RNN     | 232.43     | 325.96     | 312.57     |
| OLSTM   | 201.78     | 300.58     | 256.34     |
| TLSTM   | 156.41     | 294.13     | 225.78     |
| OLSTM-A | 123.64     | 273.56     | 201.65     |
| TLSTM-A | 102.36     | 258.19     | 183.74     |

**TABLE 5.** MAE for different methods on RUL prediction.

|         | Datasets   |            |            |  |
|---------|------------|------------|------------|--|
| Methods | I          |            |            |  |
|         | Bearing1_1 | Bearing1_5 | Bearing2_4 |  |
| CNN     | 325.63     | 368.21     | 379.84     |  |
| CNN_SVR | 204.92     | 267.09     | 249.57     |  |
| CNN_MLP | 273.83     | 292.08     | 298.25     |  |
| RNN     | 158.05     | 215.87     | 210.24     |  |
| OLSTM   | 137.21     | 195.38     | 189.44     |  |
| TLSTM   | 106.36     | 191.34     | 165.95     |  |
| OLSTM-A | 91.63      | 177.81     | 131.07     |  |
| TLSTM-A | 75.54      | 157.82     | 120.71     |  |

In the recurrent model, the performance of RNN is slightly worse than basic one-layer LSTM, which may be explained by that LSTM is able to better capture the feature correspondence in the long sequence signal by using gate function compared with RNN.

The performance of the LSTM with two hidden layers is better than that of the one-layer LSTM, indicating that the deep-layer model can learn more abstract representations, which is conducive to the prediction of long-term complex signal sequences. The key information of the input signal can be more accurately captured by adding the attention mechanism into the two-layer LSTM. It can be seen from the experimental results that the model proposed in this paper has a higher accuracy in predicting problems.

Figure 11 shows the prediction of the RUL value in the bearing degradation stage. It can be seen intuitively from

![](_page_9_Picture_1.jpeg)

**TABLE 6.** Score evaluation for different methods on RUL prediction.

| Methods | Datasets   |            |            |  |
|---------|------------|------------|------------|--|
|         | Bearing1_1 | Bearing1_5 | Bearing2_4 |  |
| CNN     | 0.486      | 0.445      | 0.429      |  |
| CNN_SVR | 0.657      | 0.563      | 0.581      |  |
| CNN_MLP | 0.562      | 0.548      | 0.555      |  |
| RNN     | 0.739      | 0.629      | 0.644      |  |
| OLSTM   | 0.766      | 0.686      | 0.698      |  |
| TLSTM   | 0.793      | 0.695      | 0.724      |  |
| OLSTM-A | 0.849      | 0.721      | 0.768      |  |
| TLSTM-A | 0.895      | 0.752      | 0.784      |  |

![](_page_9_Figure_4.jpeg)

**FIGURE 12.** Model prediction performances on different input sequence length.

the figure that the accuracy of proposed model has obvious advantages over other algorithms in predicting the RUL value in the degradation stage.

# E. MODEL ARCHITECTURE DISCUSSION

In order to further discuss the prediction performances based on various model parameters and hyper parameters, several experiments are carried out to realize model architecture discussion, including model with different input sequence lengths, different initial learning rate, whether to combine CNN module and different numbers of LSTM-Attention neurons.

Figure 12 shows the influence of different input sequence lengths on the model prediction performances. It can be seen that when the input sequence is relatively short, the model feature extraction capability is limited which affected the RUL prediction accuracy. When the input sequence length is longer than 1000, RMSE value does not decrease significantly, indicating that excessively long input signal has limited improvement for model training. In order to achieve both desired model training efficiency and prediction accuracy, the length of input signal sequence is set to 1000 in this paper.

Figure 13 shows the influence of the combination of CNN module and the setting of various initial learning rate on the training results. It can be seen from the results that the

![](_page_9_Figure_11.jpeg)

**FIGURE 13.** Model prediction performances on combination of CNN module and various learning rate.

![](_page_9_Figure_13.jpeg)

**FIGURE 14.** Model performances on different number of neurons in LSTM-Attention structure.

combination of CNN module with the prediction model can significantly improve the prediction accuracy. By setting different initial learning rates, a learning rate value is found to greatly improved the training results. Therefore, 0.005 is taken as the initial learning rate of the experimental model.

The number of neurons in LSTM-Attention module is also discussed. In order to discuss the model efficiency and in the experimental verification, RMSE = 200 is set as the threshold value to stop training to compare the number of iterations required by each model. As seen from Figure 14, the number of neurons in this module has no significant influence on the experimental results. For the high efficiency and stability of the proposed model, the neurons of LSTM-Attention module were set to 128.

# **V. CONCLUSION**

In this paper, a novel rotatory machine RUL prediction model based on deep learning is proposed. In TLSTM-A, a onedimensional CNN with convolution layer and pooling layer is designed to extract local features from the original signal sequences. Then a two-layer LSTM with attention mechanism is used to encode the time information. More hidden layers are able to discover the relationship between network input and output by observing the mapping relation

![](_page_10_Picture_1.jpeg)

in multi-dimensional space and improve the model ability in dealing with nonlinearity. Attention mechanism is able to emphasize useful connection between hidden layers to improve the prediction accuracy. Through feature learning by two-layer LSTM combined with strong supervision by the attention mechanism, accurate RUL prediction of bearings is realized. The validity and feasibility of our method is proved by comparing the prediction results with different models.

In the future work, we will further improve our model and consider to optimize the two-layer LSTM structure, trying to further improve the time efficiency of training and the accuracy of prediction results.

## **REFERENCES**

- [1] K. Javed, R. Gouriveau, and N. Zerhouni, ''State of the art and taxonomy of prognostics approaches, trends of prognostics applications and open issues towards maturity at different technology readiness levels,'' *Mech. Syst. Signal Process.*, vol. 94, pp. 214–236, Sep. 2017.
- [2] R. Zhao, R. Yan, Z. Chen, K. Mao, P. Wang, and R. X. Gao, ''Deep learning and its applications to machine health monitoring,'' *Mech. Syst. Signal Process.*, vol. 115, pp. 213–237, Jan. 2019.
- [3] Y. Lei, ''Machinery health prognostics: A systematic review from data acquisition to RUL prediction,'' *Mech. Syst. signal Process.*, vol. 104, pp. 436–444, May 2018.
- [4] Y. Qi, C. Shen, D. Wang, J. Shi, X. Jiang, and Z. Zhu, ''Stacked sparse autoencoder-based deep network for fault diagnosis of rotating machinery,'' *IEEE Access*, vol. 5, pp. 15066–15079, Oct. 2017.
- [5] G. V. Demarie and D. Sabia, ''A machine learning approach for the automatic long-term structural health monitoring,'' *Struct. Health Monitor.*, vol. 18, no. 3, pp. 819–837, May 2019.
- [6] K. T. Huynh, I. T. Castro, A. Barros, and C. Berenguer, ''On the use of mean residual life as a condition index for condition-based maintenance decision-making,'' *IEEE Trans. Syst., Man, Cybern. Syst.*, vol. 44, no. 7, pp. 877–893, Jul. 2014.
- [7] Y. Lei, N. Li, S. Gontarz, J. Lin, S. Radkowski, and J. Dybala, ''A model-based method for remaining useful life prediction of machinery,'' *IEEE Trans. Rel.*, vol. 65, no. 3, pp. 1314–1326, Sep. 2016.
- [8] Z. Gao, C. Cecati, and S. X. Ding, ''A survey of fault diagnosis and fault-tolerant techniques—Part I: Fault diagnosis with model-based and signal-based approaches,'' *IEEE Trans. Ind. Electron.*, vol. 62, no. 6, pp. 3757–3767, Jun. 2015.
- [9] J. Carroll, S. Koukoura, A. McDonald, A. Charalambous, S. Weiss, and S. McArthur, ''Wind turbine gearbox failure and remaining useful life prediction using machine learning techniques,'' *Wind Energy*, vol. 22, no. 3, pp. 360–375, Mar. 2019.
- [10] A. Mosallam, K. Medjaher, and N. Zerhouni, ''Data-driven prognostic method based on Bayesian approaches for direct remaining useful life prediction,'' *J. Intell. Manuf.*, vol. 27, no. 5, pp. 1037–1048, Oct. 2016.
- [11] J. P. Hofmeister, D. L. Goodman, and F. Szidarovszky, ''Gradation modeling from condition-based data to functional failure signature data,'' *Int. J. Comadem*, vol. 22, no. 1, pp. 33–44, 2019.
- [12] P. Kundu, S. Chopra, and B. K. Lad, ''Multiple failure behaviors identification and remaining useful life prediction of ball bearings,'' *J. Intell. Manuf.*, vol. 30, no. 4, pp. 1795–1807, Apr. 2019.
- [13] Y. Qin, X. Wang, and J. Zou, ''The optimized deep belief networks with improved logistic sigmoid units and their application in fault diagnosis for planetary gearboxes of wind turbines,'' *IEEE Trans. Ind. Electron.*, vol. 66, no. 5, pp. 3814–3824, May 2019.
- [14] Y. LeCun, Y. Bengio, and G. Hinton, ''Deep learning,'' *Nature*, vol. 521, pp. 436–444, May 2015.
- [15] S. Shao, S. McAleer, R. Yan, and P. Baldi, ''Highly accurate machine fault diagnosis using deep transfer learning,'' *IEEE Trans. Ind. Informat.*, vol. 15, no. 4, pp. 2446–2455, Apr. 2019.
- [16] F. Sun, N. Wang, X. Li, and W. Zhang, ''Remaining useful life prediction for a machine with multiple dependent features based on Bayesian dynamic linear model and copulas,'' *IEEE Access*, vol. 5, pp. 16277–16287, Aug. 2017.

- [17] A. Rohani Bastami, A. Aasi, and H. A. Arghand, ''Estimation of remaining useful life of rolling element bearings using wavelet packet decomposition and artificial neural network,'' *Iranian J. Sci. Technol., Trans. Electr. Eng.*, vol. 43, no. 1, pp. 233–245, Jul. 2019.
- [18] L. Ren, L. Zhao, S. Hong, S. Zhao, H. Wang, and L. Zhang, ''Remaining useful life prediction for lithium-ion battery: A deep learning approach,'' *IEEE Access*, vol. 6, pp. 50587–50598, Jul. 2018.
- [19] X. Li, Q. Ding, and J.-Q. Sun, ''Remaining useful life estimation in prognostics using deep convolution neural networks,'' *Rel. Eng. Syst. Saf.*, vol. 172, pp. 1–11, Apr. 2018.
- [20] J. Deutsch and D. He, ''Using deep learning-based approach to predict remaining useful life of rotating components,'' *IEEE Trans. Syst., Man, Cybern. Syst.*, vol. 48, no. 1, pp. 11–20, Jan. 2018.
- [21] J. Zhu, N. Chen, and W. Peng, ''Estimation of bearing remaining useful life based on multiscale convolutional neural network,'' *IEEE Trans. Ind. Electron.*, vol. 66, no. 4, pp. 3208–3216, Apr. 2019.
- [22] A. Malhi, R. Yan, and R. X. Gao, ''Prognosis of defect propagation based on recurrent neural networks,'' *IEEE Trans. Instrum. Meas.*, vol. 60, no. 3, pp. 703–711, Mar. 2011.
- [23] S. Hochreiter and J. Schmidhuber, ''Long short-term memory,'' *Neural Comput.*, vol. 9, no. 8, pp. 1735–1780, 1997.
- [24] J. Zhang, P. Wang, R. Yan, and R. X. Gao, ''Long short-term memory for machine remaining life prediction,'' *J. Manuf. Syst.*, vol. 48, pp. 78–86, Jul. 2018.
- [25] J. Wang, B. Peng, and X. Zhang, ''Using a stacked residual LSTM model for sentiment intensity prediction,'' *Neurocomputing*, vol. 322, pp. 93–101, Dec. 2018.
- [26] H. Choi, K. Cho, and Y. Bengio, ''Fine-grained attention mechanism for neural machine translation,'' *Neurocomputing*, vol. 284, pp. 171–176, Apr. 2018.
- [27] K. B. Charbonneau and O. Shouno, ''Neural trajectory analysis of recurrent neural network in handwriting synthesis,'' 2018, *arXiv:1804.04890*. [Online]. Available: http://arxiv.org/abs/1804.04890
- [28] L. Wu, Y. Wang, X. Li, and J. Gao, ''Deep attention-based spatially recursive networks for fine-grained visual recognition,'' *IEEE Trans. Cybern.*, vol. 49, no. 5, pp. 1791–1802, May 2019.
- [29] P. Anderson, ''Bottom-up and top-down attention for image captioning and visual question answering,'' in *Proc. IEEE Conf. Comput. Vis. Pattern Recognit.*, Jun. 2018, pp. 6077–6086.
- [30] W. Sun, R. Zhao, R. Yan, S. Shao, and X. Chen, ''Convolutional discriminative feature learning for induction motor fault diagnosis,'' *IEEE Trans. Ind. Informat.*, vol. 13, no. 3, pp. 1350–1359, Jun. 2017.
- [31] H. Wang, Z. Liu, D. Peng, and Y. Qin, ''Understanding and learning discriminant features based on multiattention 1DCNN for wheelset bearing fault diagnosis,'' *IEEE Trans. Ind. Informat.*, vol. 16, no. 9, pp. 5735–5745, Sep. 2020.
- [32] S. Shao, R. Yan, Y. Lu, P. Wang, and R. X. Gao, ''DCNN-based multi-signal induction motor fault diagnosis,'' *IEEE Trans. Instrum. Meas.*, vol. 69, no. 6, pp. 2658–2669, Jun. 2020.
- [33] J. Zhou, Y. Lu, H.-N. Dai, H. Wang, and H. Xiao, ''Sentiment analysis of chinese microblog based on stacked bidirectional LSTM,'' *IEEE Access*, vol. 7, pp. 38856–38866, Oct. 2019.
- [34] B. Wang, Y. Lei, N. Li, and N. Li, ''A hybrid prognostics approach for estimating remaining useful life of rolling element bearings,'' *IEEE Trans. Rel.*, vol. 69, no. 1, pp. 401–412, Mar. 2020.

![](_page_10_Picture_39.jpeg)

HAO ZHANG was born in 1995. He received the B.S. degree from the University of Electronic Science and Technology, Chengdu, China, in 2018. He is currently pursuing the master's degree in electrical engineering with Air Force Engineering University, China. His research interests include electromechanical equipment prognostic and health management, machine learning algorithms, and intelligent fault diagnosis.

![](_page_11_Picture_1.jpeg)

![](_page_11_Picture_2.jpeg)

QIANG ZHANG received the Ph.D. degree from Air Force Engineering University, Xi'an, China. He is currently an Associate Professor in electrical engineering with Air Force Engineering University. His research interests include electrical engineering and automation, and prognostic and health management of dynamical systems.

![](_page_11_Picture_4.jpeg)

TIANLIN NIU received the Ph.D. degree from Air Force Engineering University, Xi'an, China. He is currently a Lecturer in electrical engineering with Air Force Engineering University. His research interests include intelligent fault diagnosis, and prognostic and health management of dynamical systems.

![](_page_11_Picture_6.jpeg)

SIYU SHAO (Member, IEEE) was born in 1991. She received the Ph.D. degree in instrument science and technology from Southeast University, Nanjing, China, in 2019. She is currently a Lecturer with the Air and Missile Defense College, Air Force Engineering University, Xian, China. Her research interests include machine learning, intelligent fault diagnosis, and prognostic and health management of dynamical systems.

![](_page_11_Picture_8.jpeg)

XINYU YANG received the master's degree from Air Force Engineering University, Xi'an, China. He is currently an Associate Professor in electrical engineering with Air Force Engineering University. His research interests include electrical engineering and automation, and prognostic and health management of dynamical systems.
RESEARCH Open Access

## Check for updates

# Graph neural network-based remaining useful life prediction of milling tools using multi-sensor data

Satish Kumar<sup>1,2\*</sup>, Dhruvi Ramaiya<sup>1†</sup>, Sameer Sayyad<sup>1†</sup>, Arunkumar Bongale<sup>1†</sup>, Vivek Warke<sup>1†</sup> and Vaibhav Joshi<sup>1†</sup>

<sup>†</sup>Dhruvi Ramaiya, Sameer Sayyad, Arunkumar Bongale, Vivek Warke, and Vaibhav Joshi contributed equally to this work.

\*Correspondence:
Satish Kumar
satishkumar.vc@gmail.com

¹Symbiosis Institute of Technology,
Pune Campus Symbiosis
International (Deemed University),
Pune, Maharashtra 412115, India

²Symbiosis Centre for Applied
Artificial Intelligence, Symbiosis
International (Deemed University),
Pune, Maharashtra 412115, India

#### **Abstract**

Forecasting the Remaining Useful Life (RUL) of cutting tools plays a key role in intelligent predictive maintenance and downtime reduction in today's manufacturing. Traditional approaches based on hand-designed features or conventional machine learning models are typically incapable of handling intricate temporal relationships and sensor-interaction. This paper proposes a graph-based deep learning pipeline for tool wear forecasting in CNC milling, employing vibration, spindle load, and cutting force signals. Features from both the time-domain (mean, standard deviation, skewness, and kurtosis) and the frequency domain (FFT coefficients, power spectral density) were extracted, and graphs were formed based on correlation and temporal edges in order to model feature dependencies and sequential relationships. Three graph neural network (GNN) architectures were utilized: graph convolutional network (GCN), graph recurrent network (GRN), and graph attention network (GAT). Models were trained and tested on 120 machining runs, and hyperparameter optimization was performed using Optuna and Bayesian Optimization. The experimental results show that Optuna tuning enabled GRN to achieve the strongest time-domain performance (RMSE = 3.68,  $R^2$  = 0.9963), while Bayesian Optimization yielded improved frequency-domain performance for GAT (RMSE = 13.50,  $R^2$  = 0.9487). The designed framework illustrates the power of GNNs for tool-condition monitoring and offers a scalable solution for predictive maintenance, with future work considering physics-informed graph modeling and transfer learning for real-time application.

Keywords Tool wear prediction, GNN, RUL, Multi-domain fusion, CNC milling

#### 1 Introduction

Predictive maintenance is now a key aspect of Industry 4.0 in contemporary manufacturing, with the goal of reducing unwanted downtime, optimizing resource utilization, and maximizing product quality [1]. In machining applications, an accurate prediction of the RUL of cutting tools is important to avoid excessive tool wear, minimize production costs, and prevent sudden failures [2].

Conventional tool condition monitoring (TCM) systems are mainly based on manually designed characteristics obtained from vibration, spindle load, and cutting force signals,

![](_page_0_Picture_14.jpeg)

© The Author(s) 2026. **Open Access** This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.

Kumar *et al. Discover Applied Sciences* (2026) 8:480 Page 2 of 29

along with statistical or machine learning models [[3\]](#page-27-2). Although useful under controlled conditions, these are not good generalizers under dynamic cutting conditions because of the nonlinear and time-varying nature of wear development. DL architectures such as CNNs and RNNs have shown enhanced feature learning and temporal modeling abilities in RUL prediction, yet they continue to struggle to model complex intersensor dependencies and long-term temporal correlations explicitly [\[2](#page-27-1)].

GNNs are now a strong paradigm for learning from structured data, offering the flexibility to model machining systems as dynamic graphs in which nodes are sensor measurements and edges represent correlations or temporal relationships [\[4](#page-27-3)]. Experiments in application areas such as bearing failure diagnosis and machinery condition monitoring have established the capability of GNNs to efficiently learn rich sensor interdependencies and degradation patterns [[2\]](#page-27-1), but their application to forecasting milling tool wear is unexplored. In addition, integration of multidomain representation of features (time- and frequency-domain) in a GNN paradigm presents opportunities for enhanced modeling and better predictive accuracy, though little has been explored in this regard.

For the purpose of overcoming these challenges, the current research presents a graphbased learning pipeline for tool wear progression forecasting in milling operations. The used sensor signals of vibration, spindle load, and cutting forces are processed to derive statistical and frequency domain features as node properties in graph-structured data. Graphs are formed with temporal and correlation-based edges to model both intersensor relationships and sequential wear processes. Three GNN models [\[4](#page-27-3)], GCN [[5\]](#page-27-4), GRN [[6\]](#page-27-5), and GAT [[7\]](#page-27-6) are used and trained with an RFR to perform tool wear regression and prediction of RUL. The results of the experiment show that the introduced GRN has better predictive accuracy and reliability compared to the baseline deep learning methods.

The uniqueness of this work is not about GNN architecture. Rather, the main contribution is the creation of the first comprehensive and domain-specific evaluation framework on RUL prediction of milling tools, leveraging several existing families of GNNs. Recent papers have started using individual GNN architectures such as GAT, GRN, or ST-GCN and attempting RUL estimation, though these papers target improving metrics while using a single modeling approach and in a single application domain. On the other hand, this work methodically looks at how various families of GNNs perform and contribute towards the same goal using the same modeling techniques of graph construction, feature representations, regression heads, and optimization techniques based on the milling process signals.

In view of correlative and temporal interlinkages between multi-sensor features and by equally assessing the values of the time and frequency domains along with the detachment of Graph Representation learning from the Regression task via the employment of a Random Forest Regressor, this specific work can offer architectural and domain insights that not only advance along the lines of improving upon current state-of-the-art accuracy values but also acquaint readers with meaningful ramifications concerning the interplay between architectural inductive biasses and domains and optimization techniques of hyperparameters that have not been well explored along the current state of art in literature of Graph Neural Network applications to RUL estimation problems.

*The main contributions of this work are summarized as follows:*

• *Unified GNN evaluation framework for milling tool RUL prediction:* Contrary to most existing research works done using GNNs for RUL prediction, which were limited Kumar *et al. Discover Applied Sciences* (2026) 8:480 Page 3 of 29

to a particular model architecture or type of application, this research presents a unified evaluation framework within which GCN, GRN, as well as GAT models are compared.

- *Domain-aware multi-domain feature analysis:* Instead of showcasing a novel feature extraction method in the paper, the paper carries out a careful comparison among time-domain and frequency-domain feature representation in the same graphbased learning process. The paper focuses on the complementarity of various feature domains in the wear mechanisms.
- *Correlation–temporal graph construction strategy:* The proposed strategy combines correlation edges and temporal edges. As such, it ensures that the graphs are more sparse and meaningful and account for the sensor correlations and the progress of wear, unlike other studies that use completely connected and temporal graphs.
- *Hybrid representation regression design:* Involving a separate regression step with a Random Forest Regressor instead of going with a purely neural regression, as has been done in previous works, increases robustness and explainability gained by learning a graph representation through a GNN-RUL model.
- *Optimization-driven architectural insight:* By performing a systematic comparison of strategies based on Optuna and Bayesian Optimization, this work reports new insights about how hyperparameter search interacts with inductive biases of the architectural model - GRN and GAT - that explains the observed performance difference rather than stating best-case results.

Combining these contributions together creates an authentic and reproducible pipeline for tool wear RUL estimation using advanced graph neural network architectures.

This document is divided into several parts. In Sect. [2](#page-2-0), we analyze recent advancements in predicting RUL, application of GNNs, and modeling tool wear. Section [3](#page-6-0) describes the proposed methodology, i.e., feature extraction, GNN-structured graph creation, and models. In Sect. [4](#page-15-0), we present the details of the experimental setup, the metrics used to evaluate the results, and Sect. [5](#page-26-0) assessment of the work, and outlines the possible directions for future work.

#### <span id="page-2-0"></span>**2 Literature review**

In modern manufacturing, Predictive Maintenance has become critical for mitigating unplanned downtimes, optimizing the utilization of tools, and keeping the product quality consistent. A key component of Predictive Maintenance is Remaining Useful Life (RUL) prediction, which is the estimate of how long a component and tool will continue functioning before breaking. In operations like milling where the machining, infused with precision, is high, the surface finish quality and the effectiveness of the expense (operational) get affected owing to the wear of the tool. Hence, accurate prediction of the RUL is foundational [[1\]](#page-27-0). This subsection focuses on the progression of different RUL prediction methods (statistical to deep learning methods based on graph).

#### **2.1 Physics-based and statistical approaches**

In the beginning, research focused on physics-centered approaches and traditional statistical methods. For modeling the tool wear history, regression, ARIMA, and Kalman filter methods were implemented [\[8](#page-27-7)]. Estimations of life based on equations such as Taylors tool life and other tool wear rate equations, were derived from the machining Kumar *et al. Discover Applied Sciences* (2026) 8:480 Page 4 of 29

parameters and material properties [[9](#page-27-8)]. While these approaches were quite strong and accurate within a controlled environment, they seamed to struggle with generalizing to other machining scenarios to develop a robust model. They were also poor at modeling complex interdependencies between the sensors.

#### **2.2 Machine learning-based methods**

RUL estimation benefits from the multi-sensor data, and therefore data-driven approaches such as ML, are quite common. Tool wear level estimation using ML has been done with methods such as Random Forest, Gradient Boosting and SVM, where the features are hand-crafted [[3\]](#page-27-2). These features, typically computed using the time and frequency domains, involve statistical measures, and methods such as FFT and wavelet transforms. Feature ML would improve the prediction accuracy, but as noted with the challenge of dynamic machining, the reliance on domain knowledge for feature engineering limits scalability [[1\]](#page-27-0).

In [[10\]](#page-27-9), the author proposes an adapted RUL prediction method for lithium-ion batteries using small, unlabeled datasets with uncertain parameters. It employs Wienerprocess degradation model using an online Kalman filter with EM-RTS. Even though the main focus of the paper is of batteries, it illustrates the challenges of few labeled runs, and parameter uncertainty, both equally applicable for the case of tool-wear RUL estimation.

#### **2.3 Deep learning-based approaches**

Due to their ability to learn from unprocessed data, deep learning algorithms decreased the need for manual feature extraction. For instance, RNN, LSTM, and GRU models excelled at temporal modeling, while CNNs were adept at pulling local spatial patterns from data. [\[11](#page-28-0)]. Ignoring inter-sensor dependencies, critical for understanding complex machine behaviors, has been a shortcoming of the majority of deep learning models, as they tend to evaluate data streams from sensors in a siloed manner.

Most recently, hybrid deep learning architecture models for RUL have gained some attention.One of the more notable of these is Wu et al. [\[10](#page-27-9)] with their tightly integrated CNN–Informer architecture, which predicts remaining useful life by efficiently removing local patterns and retaining long-term temporal dependencies. While the model has some real strengths in battery degradation forecasting, domain-specific tuning, and high computational costs, reduces real-time use in machining and multi-sensor tool wear scenarios. These studies have encompassed the need for more challenging, inter-sensor related deep learning RUL models, which have shifted to graph architectures.

This is evident in Wu et al. [\[11](#page-28-0)] who, building on the work on hybrid deep learning architectures for RUL, at long last, provide a general model for deep learning RUL prediction (including CNNs, RNNs, Transformers).

#### **2.4 Graph neural networks for RUL**

Recent developments have incorporated GNNs to explicitly account for sensor dependencies and capture spatiotemporal patterns [[12](#page-28-1)]. Within these approaches, GCNs and GATs model sensor features as nodes while the relationships are represented as edges, allowing for enhanced feature representation and temporal modeling. More advanced versions, such as hierarchical GNNs and hypergraph attention networks (HGAT), have Kumar *et al. Discover Applied Sciences* (2026) 8:480 Page 5 of 29

also shown enhanced capabilities for RUL prediction through higher-order feature fusion [[13](#page-28-2), [14\]](#page-28-3).

ST-GCN and its variants are recent hybrid architecture in prognostic systems which combine graph convolution with temporal convolution [[7,](#page-27-6) [15](#page-28-4)]. This design allows the model to capture relationships between nodes and their degradation over time. Incorporating domain knowledge as mechanistic constraints during the learning process, Physics-informed GNNs have also emerged, allowing for greater robustness and interpretability within the model in some systems [[14](#page-28-3)].

Hybrid models are designed to deliver specific features and functionalities. However, they need to be more complex in their architecture and require more domain-focused priors and crossover dataset integration [[7,](#page-27-6) [13\]](#page-28-2). Conversely, GNN-focused tool wear prediction, and more specifically, milling tool wear prediction, remains largely absent from central literature [[2\]](#page-27-1). We present solutions to several of these challenges in the literature in our proposed work. These involve the integration of several lightweight architecture features specifically designed to meet the complexities of industrial milling environments, more multi-domain feature integration, and optimal graph construction. These three are best examined through a comparative study of three canonical GNN families, GCN, GRN, and GAT, and specifically correlate with our proposed multi-domain feature fusion with a temporal graph and milling tool wear, wear state prediction, and remaining useful life prediction [\[4](#page-27-3), [16\]](#page-28-5).

There is something of a copeland circle from our work, this being the work of Zhang et al. (2024). Zhang proposed a multi-hop graph pooling adversarial network under a federated learning framework to achieve domain-agnostic, cross-domain RUL prediction where multiple sensor clients can cooperatively train a model without sharing their private datasets, mitigating domain alterations via adversarial pooling, and sequenced multi-hop feature propagation. Zhang's work highlights that GNNs can be applied in a federated and cross-domain context, a useful comparison to our single-domain, milling wear-focused pipeline.

Wu et al. [[17](#page-28-6)] discussed a distinct model of a 'multi-view fully-connected graph' for RUL prediction with multi-sensors in mechanical equipment, where each sensor's view is a graph, and the cross-view edges of the graph are fully inter-connected. Although the model's performance indicates effective multi-sensor fusion, the model is designed for general mechanical equipment, and fully-connected graphs may be less effective as they comprise redundant edges and are more expensive to compute. Our work, unlike these, is the first of its kind in focusing on milling tool wear, employs correlation and temporal edges to construct sparser and more interpretable graphs and, within a unified framework, tests three foundational GNN architectures.

#### **2.5 Hybrid and physics-informed approaches**

Given the rising popularity of hybrid, data-driven modeling, and physics-informed approaches for their stability and interpretability [\[9](#page-27-8), [18\]](#page-28-7). Physics-informed deep learning, BRANNs, and transfer learning have been applied to improve generalization performance over varying machining configurations [\[19\]](#page-28-8). Other approaches have also demonstrated competitiveness, including PSD-CVT based CNNs, GAF based deep residual networks, and multi-source bilinear fusion architectures.

Kumar *et al. Discover Applied Sciences* (2026) 8:480 Page 6 of 29

#### **2.6 Summary of literature**

Table [1](#page-5-0) For the most part, the author summarizes the main contributions, the methodologies used, and the downsides of these studies. The gap in the literature is still in the use of graph-based structures for remaining useful life prediction in milling, especially in the ideal feature extraction and hyperparameter tuning. The purpose of this study is to fill in this gap, proposing a comprehensive pipeline using graph neural networks, comparing

<span id="page-5-0"></span>**Table 1** Selected literature on RUL and tool-wear prediction (top journals)

| Authors                               | Title                                                                                                                             | Method/model                              | Key finding/limitation                                                                                                                |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Wang et al.<br>(2025) [2]             | A survey on graph neural networks<br>for remaining useful life prediction                                                         | Survey (GNNs for<br>RUL)                  | Identifies comprehensive research<br>gaps in graph construction, spatio<br>temporal modeling, and scalability<br>for RUL applications |
| Wang et al.<br>(2024) [7]             | Remaining useful life predic<br>tion using graph convolutional<br>attention networks with temporal<br>convolution-aware residuals | GCN + Attention<br>+ TCN                  | Hybrid spatiotemporal modeling<br>improves RUL accuracy at the cost of<br>increased architectural complexity                          |
| Wu et al.<br>(2024) [13]              | Temporal multi-resolution hyper<br>graph attention network for RUL<br>prediction of rolling bearings                              | Hypergraph Atten<br>tion Network          | Captures high-order and multi-scale<br>temporal dependencies; evaluation<br>limited to bearing datasets                               |
| Li et al. (2021)<br>[12]              | Hierarchical attention graph convo<br>lutional network to fuse multi-sen<br>sor signals for RUL prediction                        | HAGCN (multi<br>sensor fusion)            | Strong sensor fusion capability;<br>requires predefined and carefully<br>designed graph structures                                    |
| Mallioris et al.<br>(2024) [1]        | Predictive maintenance in Industry<br>4.0: A systematic multi-sector<br>mapping                                                   | Systematic litera<br>ture review          | Provides a broad overview of predic<br>tive maintenance strategies across<br>industries; lacks model-level analysis                   |
| Pashmfo<br>roush et al.<br>(2024) [9] | Physics-informed tool wear<br>prediction in turning using thermo<br>mechanical modeling                                           | Physics-informed<br>machine learning      | Integrates physical constraints to im<br>prove prediction robustness; requires<br>accurate model calibration                          |
| Li et al. (2025)<br>[18]              | Application of physics-guided deep<br>learning in tool wear monitoring of<br>high-speed milling                                   | Physics-guided<br>deep learning           | Improves generalization and physical<br>consistency; introduces additional<br>modeling complexity                                     |
| Yau et al.<br>(2024) [20]             | Milling wear prediction using<br>artificial neural networks                                                                       | ANN-based<br>regression                   | Provides a strong non-graph baseline<br>for milling wear prediction; limited<br>temporal dependency modeling                          |
| Truong et al.<br>(2024) [21]          | Data-driven prediction of tool wear<br>using Bayesian regularization                                                              | Bayesian<br>regularized neural<br>network | Achieves accurate predictions on<br>laboratory data; field-scale general<br>ization remains uncertain                                 |
| Si et al. (2024)<br>[19]              | Intelligent tool wear prediction<br>based on PSD-CVT deep learning<br>model                                                       | CNN-based time–<br>frequency learning     | Demonstrates high accuracy using<br>PSD representations; involves sub<br>stantial preprocessing overhead                              |
| He et al.<br>(2023) [14]              | Systematic RUL estimation based<br>on physics-informed graph neural<br>networks                                                   | Physics-informed<br>GNN                   | Robust multisensor modeling with<br>physical constraints; increased train<br>ing complexity                                           |
| Guo et al.<br>(2025) [22]             | Unlabeled-data-enhanced tool RUL<br>prediction based on graph neural<br>networks                                                  | Semi-supervised<br>GNN                    | Effectively leverages unlabeled<br>data; transferability to different tools<br>requires further validation                            |
| Cheng et al.<br>(2024) [23]           | Multi-signal milling tool wear pre<br>diction based on GAF-ResNeXt                                                                | GAF + deep<br>residual network            | Transforms time-series into images<br>for feature learning; computationally<br>intensive                                              |
| Lin et al.<br>(2025) [24]             | Tool wear prediction using XG<br>Boost feature selection and PSO-BP<br>network                                                    | XGBoost + PSO-BP                          | Combines classical ML and neural<br>networks; lacks explicit temporal<br>modeling                                                     |
| Xia et al.<br>(2025) [15]             | Spatial–temporal adaptive graph<br>convolutional network for tool<br>wear prediction                                              | ST-AGCN                                   | Advanced spatiotemporal graph<br>modeling with multi-sensor signals;<br>higher computational demand.                                  |
| Wu et al.<br>(2025) [17]              | Multi-view fully connected graph<br>for multi-sensor RUL prediction                                                               | Fully connected<br>GNN                    | Strong sensor fusion capability;<br>dense graph connectivity increases<br>computational cost.                                         |

Kumar *et al. Discover Applied Sciences* (2026) 8:480 Page 7 of 29

<span id="page-6-1"></span>**Table 2** Machining parameters used for the milling experiments

| Expt. no | Spindle speed | Feed     | Depth of cut | Material/operation                                                                                                     |
|----------|---------------|----------|--------------|------------------------------------------------------------------------------------------------------------------------|
|          | (rpm)         | (mm/min) | (mm)         |                                                                                                                        |
| 1        | 1000          | 10       | 0.1          | Tool Material:<br>Coated<br>Tungsten Carbide<br>Workpiece Material:<br>D3 Steel<br>Operation:<br>End Milling: Slotting |
| 2        | 1000          | 20       | 0.2          |                                                                                                                        |
| 3        | 1000          | 30       | 0.3          |                                                                                                                        |
| 4        | 1100          | 10       | 0.2          |                                                                                                                        |
| 5        | 1100          | 20       | 0.3          |                                                                                                                        |
| 6        | 1100          | 30       | 0.1          |                                                                                                                        |
| 7        | 1200          | 10       | 0.3          |                                                                                                                        |
| 8        | 1200          | 20       | 0.1          |                                                                                                                        |
| 9        | 1200          | 30       | 0.2          |                                                                                                                        |

<span id="page-6-2"></span>**Table 3** Components and experimental equipment specifications

| Component/equipment              | Specifications                                          |
|----------------------------------|---------------------------------------------------------|
| Machine                          | Jyoti VMC, NVU PX 100                                   |
| Workpiece Material and Dimension | D3 Steel (Length = 200 mm                               |
|                                  | Breadth = 100 mm, Width = 50 mm)                        |
| Wear Measurement – Microscope    | Radical Tool Makers Microscope                          |
| End Mill Tool                    | Cutter Coated Tungsten Carbide Insert (End-mill Cutter) |
| Maximum Permissible Flank Wear   | 0.30 mm, ISO 3685                                       |

GCN, GAT, and GRN with both frequency and time domain features along with hyperparameter tuning using Optuna and Bayesian Optimization.

The effectiveness of GNN-based models in RUL prediction is prominent from recent works, most research works currently focus on improving performance through architecture-specific optimization and/or the design of hybrid models. As such, there is always a need to explore systematically the performance of various GNN architectures in relation to domains, thereafter, graph construction methods, as well as optimization techniques under one research framework. This research bridges this knowledge deficit by placing GCN, GRN, and GAT not as rivals to newer models but instead as controlled baselines in one research framework in relation to milling tool wear prediction. As such, this research moves forward in relation to how design-as opposed to innovation-plays an important role in real-world settings.

#### <span id="page-6-0"></span>**3 Methodology**

The forthcoming research proposes the use of a graph-based learning pipeline for estimating the tool wear over time during the milling process [\[2](#page-27-1), [15](#page-28-4)]. For this purpose, the time and frequency domain features of signals from various sensors, such as vibration, spindle load, and control of milling process, serve as node attributes of graph-structured data. The data sets from the sensors were gathered during controlled machining and equipment setup, which are presented in Tables [2](#page-6-1) and [3.](#page-6-2)

Graphs are built using correlation-based and temporal edges for each of the intersensor relationships and sequential dependencies [\[7](#page-27-6), [13](#page-28-2)]. Three models of the GNN are employed in this pipeline: GCN, GRN, and GAT. Each of the models is trained with a Random Forest regressor (RFR) in a tool wear regression and Remaining Useful Life (RUL) prediction [\[25](#page-28-14)]. Thus, Fig. [1](#page-7-0) illustrates the overall workflow of the proposed approach.

#### **3.1 Experimental setup**

This section details the use of GNNs for the estimation of the remaining useful life RUL of milling tools. It describes the entire setup used for this purpose, including an overview of the dataset, feature extraction, construction of the graph-building pipeline, model configurations, training, and implementation details for reproducibility. The realtime data acuqisition experimental setup is shown in Fig. [2](#page-8-0).

<span id="page-7-0"></span>![](_page_7_Figure_6.jpeg)

**Fig. 1** Proposed methodology for tool wear prediction using GCN, GRN, and GAT with both time- and frequencydomain features

Kumar *et al. Discover Applied Sciences* (2026) 8:480 Page 9 of 29

<span id="page-8-0"></span>![](_page_8_Picture_1.jpeg)

**Fig. 2** Experimental setup for real-time data-acquisition **A** Milling center. **B** Tool wear measurement. **C** Data acquisition system. **D** Data visualization and storage. **E** Vibration sensor. **F** Three-axis milling tool dynamometer. **G** Current clamp

#### **3.2 Experimental machining parameters**

Taking into account spindle speed, feed rate, and depth of cut, we conducted nine different milling tests, each with a unique combination of these cutting parameters. The chosen machining axes parameters affect the amplitude of the signal being measured for vibration, force, and spindle current. These signals are subsequently analysed for timedomain and frequency-domain feature extraction and used to construct a signal graph. The chosen machining parameters, tool and workpiece materials, and the milling operation carried out are summarised and presented in Table [2](#page-6-1).

As detailed in Table [3,](#page-6-2) the project utilized machine, tooling, measurement systems, and workpieces. All milling tests were done on the Jyoti VMC nvux px 100 vertical machining center. We chose workpieces in D3 tool steel 200,mm *×* 100,mm *×* 50,mm for its availability and tooling wear characteristics. Tool wear was measured using Radical Tool Makers Microscope, which allowed for the review of flank wear at each cutting time more precisely. The cutter employed was a coated tungsten carbide insert, which is applicable to end-milling of high-strength steel. The maximum flank wear allowed for the tests was 0.30,mm, which is in agreement with the requirements of ISO 3685 for the analysis of tool life.

#### **3.3 Graph convolutional network (GCN)**

The Graph Convolutional Network (GCN) updates node features by aggregating information from their neighbors through a normalized spectral convolution [\[12](#page-28-1)]. For a graph *G* = (*V , E* ) with adjacency matrix *A*, degree matrix *D*, and node features *<sup>X</sup> <sup>∈</sup>* <sup>R</sup>*<sup>N</sup>×<sup>F</sup>* , a GCN layer is defined as

$$H^{(l+1)} = \sigma \left( \tilde{D}^{-\frac{1}{2}} \tilde{A} \tilde{D}^{-\frac{1}{2}} H^{(l)} W^{(l)} \right), \tag{1}$$

where  $\tilde{A}=A+I$  introduces self-loops,  $\tilde{D}$  is its degree matrix,  $H^{(l)}$  is the feature matrix on the layer l, and  $W^{(l)}$  is a learnable weight matrix.

Intuitively, the GCN performs a form of weighted neighborhood averaging: each node updates its representation by mixing its own features with those of its neighbors in the graph. This means that if two features (e.g. vibration RMS and force variance) exhibit strong correlation, the GCN smooths and blends their information. As a result, GCN is particularly effective at capturing stable and consistent inter-feature relationships that occur during gradual tool degradation.

This neighbourhood-aggregation property makes GCN well-suited for modelling the correlation-based edges used in this work, where relationships among statistical and frequency-domain features often remain steady over consecutive time windows. Thus, the architecture of GCN is demonstrated in Fig. 3.

#### 3.4 Graph recurrent network (GRN)

The supple GRN incorporates GNNs with recurrent neural networks like GRUs or LSTMs [6]. GRNs process sequences of data. Rather than utilizing a single static graph, they model a *sequence of graph snapshots*  $\{G_1, G_2, \ldots, G_T\}$ . Each "snapshot" represents a distinct time window of feature relationships during the machining process. this design permits the model to capture the evolution of feature dependencies as tool wear increases.

The GRN architecture updates the embeddings of the graph nodes as follows, using the current feature matrix  $X_t$  and the previous memory cell  $h_{t-1}$ :

<span id="page-9-0"></span>![](_page_9_Figure_8.jpeg)

Fig. 3 Graph Convolution Network (GCN) architecture used for tool wear prediction

$$h_t = \text{GRU}(X_t, h_{t-1}) \tag{2}$$

To provide clarity, the GRU operations inside the GRN can be writtenas follows.

$$z_t = \sigma(W_z X_t + U_z h_{t-1}) \tag{3}$$

$$r_t = \sigma(W_r X_t + U_r h_{t-1}) \tag{4}$$

$$\tilde{h}_t = \tanh(W_h X_t + U_h(r_t \odot h_{t-1})) \tag{5}$$

$$h_t = (1 - z_t) \odot h_{t-1} + z_t \odot \tilde{h}_t \tag{6}$$

*Intuitively, GRN performs two key operations:*

- *Temporal memory:* It remembers patterns from previous time windows, such as gradually increasing vibration amplitude or spindle-load fluctuations.
- *Temporal smoothing of graph features:* If multiple features consistently show degradation trends, GRN strengthens these trends in the updated node states.

This allows GRNs to be particularly effective for progressive tool wear, which is characterised by gradual degradation rather than sudden wear. Because of how GRNs capture long-term dependencies across graph snapshots, they have a greater ability to track slowly accumulated wear than static GNN architectures. The Fig. [4](#page-10-0) illustrates the architecture of GNN-GRN.

#### **3.5 Graph attention network (GAT)**

GAT means Graph Attention Network, which modifies standard message passing processes in networks so that nodes can learn to attend to their neighbours differentially. Instead of concentrating on all connected features in the network in the same manner,

<span id="page-10-0"></span>![](_page_10_Figure_15.jpeg)

**Fig. 4** Graph Recurrent Network (GRN) architecture for sequential graph modelling in tool wear prediction

GAT pays attention to features that demonstrate most salient relationships and determines their attention coefficients. This is beneficial in situations where some vibration or force features display distinct behaviour with regard to predicting wear. This is because GAT is able to automatically attend to the most relevant features.

For neighbor *j* of node *i*, the attention coefficient *αij* is calculated as:

$$\alpha_{ij} = \frac{\exp\left(\text{LeakyReLU}(a^{\top}[Wh_i|Wh_j])\right)}{\sum_{k \in \mathcal{N}(i)} \exp\left(\text{LeakyReLU}(a^{\top}[Wh_i|Wh_k])\right)}$$
(7)

The updated node representation is:

$$h_i' = \sum_{j \in \mathcal{N}(i)} \alpha_{ij} W h_j$$

Here, *W* is the shared attention weight matrix, *a* is a learnable attention vector, and *N* (*i*) denotes the neighborhood of node *i*.

*Intuitively, this mechanism allows the model to:*

- assign higher weights to features that show strong correlation with tool wear,
- suppress noisy or less informative features,
- dynamically adjust the importance of features depending on the machining condition.

Training is also made more stable through multi-head attention, as it can compute several independent attention scores, concatenate their outputs, and explore different inter-feature dependencies, such as those between vibration harmonics, force peaks, and spindle load fluctuations, which leads to better overall representation learning. The architecture of GAT is shown in Fig. [5.](#page-11-0)

#### **3.6 Metrics of evaluation**

This study uses four standard regression metrics to evaluate the models performance *MSE, RMSE, MAE, and R*<sup>2</sup>. Besides the metrics having numerical values, *MSE, RMSE, MAE, and R*<sup>2</sup> have an individual theoretical interpretation and are applicable to different scenarios for evaluation [\[26](#page-28-15)].

<span id="page-11-0"></span>![](_page_11_Figure_16.jpeg)

**Fig. 5** Graph Attention Network (GAT) architecture with multi-head attention for improved representation learning

Mean Squared Error (MSE): MSE takes the average of the squares of the errors
between the predicted values and the actual values and since the errors are squared,
the higher the error, the more it is affected. Because of this, MSE is especially
appropriate for situations where predicting errors is damaging (e.g., sudden fast tool
degradation (Chicco, 2021)).

$$MSE = \frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2$$
 (8)

• Root Mean Squared Error (RMSE): RMSE is the square root of MSE and is expressed in the same units as the target variable. When it comes to health monitoring, there is, on an absolute basis, an interpretative metric for the degree of the error, and the metric is used extensively in that context. Also, it is true that we would want to outliers to be as positive as possible, we would want that when deciding on the aim to be as positive as possible when it comes to reducing the degree of divergence from the prediction of the RUL [26].

RMSE = 
$$\sqrt{\frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2}$$
 (9)

 Mean Absolute Error (MAE): MAE is the metric that is taking the average absolute (linear) difference between the predicted values and the values being predicted.
 MAE is very different compared to MSE and RMSE as it weighs all errors the same and is less affected by outliers.

This is applicable when equating the average accuracy of the predictions of all the different wear stages and being okay with some larger errors that get their predictions off more significantly [26].

$$MAE = \frac{1}{N} \sum_{i=1}^{N} |y_i - \hat{y}_i|$$
 (10)

• Coefficient of Determination  $(R^2)$ :  $R^2$  identifies how much variation in true values was explained by the model. Predictive alignment is strong above a value of 1. Considering  $R^2$  in predicting RUL is useful because it is a measure of how well the model is able to understand the overall degradation trends instead of just being accurate at predicting values at a specific point in time [26].

$$R^{2} = 1 - \frac{\sum_{i=1}^{N} (y_{i} - \hat{y}_{i})^{2}}{\sum_{i=1}^{N} (y_{i} - \bar{y})^{2}}$$
(11)
$$R^{2} \text{ identifies how}$$

much variation in true values was explained by the model. Predictive alignment is strong above a value of 1. Considering  $\mathbb{R}^2$  in predicting RUL is useful because it is a measure of how well the model is able to understand the overall degradation trends instead of just being accurate at predicting values at a specific point in time [26].

Kumar *et al. Discover Applied Sciences* (2026) 8:480 Page 14 of 29

#### **3.7 Dataset description**

The assessment was carried out on a multisensor milling dataset obtained from a highly accurate Computer Numerical Control (CNC) machining center. Data was collected at various machining configurations, i.e, various spindle speeds, feed rates, and depthof-cut positions, to imitate actual shop floor scenarios. The data set contains vibration signals in three orthogonal directions (X, Y, Z), spindle current/load signals, and threecomponent cutting force signals collected via a dynamometer. All signals were recorded at a frequency of 25 kHz on a National Instruments DAQ system.

During the machining process, a cutting tool underwent flank wear which was measured in intervals in accordance with provisions set in ISO 8688 standards using an optical microscope. A total of 120 machining runs were performed. Marking tool wear per pass facilitated supervised RUL modeling. Hence, the dataset captures a wide range of deterioration states from recently acquired and freshly sharpened cutting tools to those which have reached the end of their service lives.

Owing to disparities in signal transformation techniques and methods of windowing, there are variations in the number of graph instances for different domains of features. Specifically, it has been noticed that the time domain graph has an increased number of graph samples compared to that of the frequency domain graph. This has been highlighted in Sect. [4.5.](#page-23-0)

#### **3.8 Feature extraction**

In order to build a pipeline to process data collected by a time series sensor, various statistical features are extracted, and include mean, root mean square, variance, order of peakedness, order of peakedness, crest factor and are combined with Fast Fourier Transform coefficients, distinct dominant frequencies, and power stored in a specific frequency layer of the data collected by the time series sensor.

In order to understand the dynamics of time and allow a short-term RUL to be predicted, a window that slides 20 times with a prediction horizon of 1 was created. Every sliding window was normalized using the z-score method to keep the same scale across all signals. As stated in the tool wear model, combining statistical and spectral components is crucial [[19](#page-28-8)].

#### **3.9 Graph construction**

A graph *G* = (*V , E* ) was assigned to each individual time window, where *V* stands for the vertices which are the extracted features, and *E* are the edges which depict the relations among the vertices. Two types of edges were considered.

- *Feature correlation edges:* A pairwise Pearson correlation *ρ* was calculated among the features. If *ρ* was higher than a threshold of *ρ >* 0*.*8, an edge was added to the graph, allowing the graph to retains features which are strongly correlated.
- *Temporal edges:* Every feature node was connected to its counterpart in the preceding and the succeeding time window to depict time series relationships. This maintains a temporal coherence in the graph structure.

The dual edge strategy allows the GNN to simultaneously learn spatial (relation between features) and temporal (time) patterns, which enhances the performance of the model.

Kumar *et al. Discover Applied Sciences* (2026) 8:480 Page 15 of 29

#### **3.10 Model configuration**

Three graph neural network (GNN) architectures were implemented and compared:

- 1. *GCN:* Two layers were included to learn the relationships of the features of each node through spectral convolutions with a ReLU activating function.
- 2. *GAT:* Eight attention heads were included to dynamically adjust the weight on the importance of the neighboring nodes through multi-head attention.
- 3. *GRN:*The addition of the recurrent node units were used to learn the temporal characteristics of the nodes in the graph sequence, which were in themselves units of a recurrent neural network.

For all models, a latent dimension of 128, a 0.2 dropout rate, and the Adam Optimizer with a learning rate of <sup>1</sup> *<sup>×</sup>* <sup>10</sup>*−*<sup>3</sup> were used. In predicting RULs from the embeddings provided by GNNs, the RFR was used as the last regression head, having 100 trees and a maximum depth of 10.

#### **3.11 Training and evaluation**

So as not to have further data leakage to mitigate further data leakage, the sample tests were taken from different machining runs, data were split to 80%, 10%, and 10% as training, validation, and testing sets, respectively, and to avoid overfitting, all of the models (GCN, GRN, and GAT) were trained with a maximum of 150 epochs with early stopping after a validation loss of 10 epochs in patience of epochs. The models were evaluated over 4 metrics of RMSE, MAE, MSE, and the *R*<sup>2</sup> score. Each feature set had its best model, from the time and frequency domains which were selected based on their validation results after training and testing epochs. To avoid redundancy and help with the generalization performance, the training of those models were done with all the training and validation sets combined from scratch.

Hyperparameter tuning was conducted using Optuna, a fast and responsive optimization library, paired with Bayesian Optimization, to squeeze an extra measure of performance out of the models. Key hyperparameters that included, but were not limited to, batch size, dropout probability, number of GNN layers, learning rate, and hidden layer sizes were cycled through several pre-defined ranges during several trials. After every trial, we fully trained the networks with a validation early stopping procedure and chose the winning trial that achieved the best validation *R*<sup>2</sup>. Models were then retrained with the best hyperparameters and tested with the held-out test set. The models qualified for strong selection from the validation set to test set and through this multi-step process. The process also brought out the trade-offs clearly, in accuracy and generalizability, with respect to model complexity.

The following metrics were used to assess performance:

- Coefficient of Determination (*R*<sup>2</sup>)
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE) item Root Mean Square Error (RMSE)

These metrics comprehensively measure both the prediction accuracy and the explanation of variance.

Kumar *et al. Discover Applied Sciences* (2026) 8:480 Page 16 of 29

#### **3.12 Implementation details**

The experiments were implemented in Python 3.10 using PyTorch 2.0 and PyTorch Geometric 2.4.0. Hyperparameter optimization was conducted using Optuna. All experiments were executed on a workstation equipped with an NVIDIA RTX 3080 GPU (10 GB), an AMD Ryzen 9 5900X CPU (12 cores), and 64 GB RAM. The codebase is containerized using Docker to facilitate reproducibility.

#### <span id="page-15-0"></span>**4 Results and discussion**

#### **4.1 Tool wear prediction using time-domain features**

In order to represent the time-related changes and illustrate the tool's wear behaviours during grinding, time-domain attributes, which included the average value, standard deviation, skewness and kurtosis, were evaluated from the sensor signal data. Lessening of the patterns was exhibited by these features.

For the training of the three graph-based models, GCN, GRN, and GAT, we used a Random Forest Regressor as a base learner. To mitigate the problem of overfitting and to enhance generalization, training for each of the models was performed for 100 epochs and had early stopping.

Furthermore, a sensitivity analysis was performed with regard to the correlation threshold being used for the construction of time-domain graphs. In particular, models were trained by using three different thresholds, namely (*ρ*) = 0.3, 0.5, and 0.8. Indeed, lower thresholds constructed denser graphs and comparatively yielded degraded performance due to the involvement of weak or noisy feature relationships. Among the threshold values tested, (*ρ*) = 0.8 gave the lowest prediction error and highest coefficient of determination across all three GNN architectures. Therefore, results presented in Table pertain to the optimum setting of the threshold, i.e., (*ρ*) = 0.8 (Table [4](#page-15-1)).

Table [5](#page-16-0) summarizes the results in terms of RMSE, MAE, Coefficient of Determination (*R*<sup>2</sup>), and MSE (Fig. [6](#page-16-1)).

Graph [7](#page-16-2) displays prediction performance graphs for all models which show predicted value of tool wear alongside the actual values. The **GRN model** has highest *R*<sup>2</sup> (*R*<sup>2</sup> = 0.9377) with the lowest RMS and MSE validating its ability to learn temporal dependencies. GAT also performed well, while GCN was somewhat slow predicting. The results demonstrate the importance of temporal modeling in order to accurately predict tool wear.

<span id="page-15-1"></span>**Table 4** GNN models performance for different correlation thresholds used during graph construction

| Model | Threshold (ρ) | RMSE    | MAE     | R2     | MSE      |
|-------|---------------|---------|---------|--------|----------|
| GCN   | 0.3           | 18.5346 | 13.4871 | 0.8943 | 343.5002 |
| GCN   | 0.5           | 17.8129 | 12.9364 | 0.9078 | 317.2769 |
| GCN   | 0.8           |         | 12.4192 | 0.9202 | 289.1293 |
| GRN   | 0.3           | 16.8924 | 11.7642 | 0.9121 | 285.3789 |
| GRN   | 0.5           | 15.9768 | 10.9846 | 0.9258 | 255.2581 |
| GRN   | 0.8           | 15.0181 | 10.3415 | 0.9377 | 225.5435 |
| GAT   | 0.3           | 19.6247 | 14.0832 | 0.8835 | 385.1056 |
| GAT   | 0.5           | 18.7139 | 13.2764 | 0.8998 | 350.2054 |
| GAT   | 0.8           | 17.8469 | 12.6340 | 0.9120 | 318.5130 |

Kumar *et al. Discover Applied Sciences* (2026) 8:480 Page 17 of 29

<span id="page-16-0"></span>

|  |  |  |  |  | Table 5 Comparison of GCN, GRN, and GAT Models (100 Epochs) |
|--|--|--|--|--|-------------------------------------------------------------|
|--|--|--|--|--|-------------------------------------------------------------|

| Model | No. of epochs | Early stopping | RMSE    | MAE     | R2     | MSE      |
|-------|---------------|----------------|---------|---------|--------|----------|
| GCN   | 100           | 100            | 17.0038 | 12.4192 | 0.9202 | 289.1280 |
| GRN   | 100           | 100            | 15.0181 | 10.3415 | 0.9377 | 225.5435 |
| GAT   | 100           | 32             | 17.8469 | 12.6340 | 0.9120 | 318.5130 |

<span id="page-16-1"></span>![](_page_16_Figure_3.jpeg)

**Fig. 6** Performance comparison of the proposed graph neural network models on time-domain features

<span id="page-16-2"></span>![](_page_16_Figure_5.jpeg)

**Fig. 7** Comparison of GCN, GRN, and GAT predictions on time-domain features with Actual VS Predicted

#### **4.2 Tool wear prediction using frequency-domain features**

Real-time sensor signals were processed to capture frequency-domain features through the use of FFT to determine the spectrum of the features of the milling process. The features capture recurring patterns and identify the noise and the vibration signatures characteristic of tool wear in rotating equipment.

Three models were built using a Random Forest Regressor as the learner and were trained using a GCN, GRN, and GAT. All models employed early stopping upon reaching 100 epochs of training based on validation performance.

Apart from assessing model performance at the chosen threshold, a sensitivity analysis was performed regarding the choice of the correlation threshold in the frequency domain. In this context, the models GCN, GRN, and GAT were trained using three different thresholds for correlation ((*ρ*) = 0.3, 0.5, and 0.8). Lower thresholds generated spectral graphs that were much denser, increasing noise propagation and reducing predictive accuracy. With an increase in threshold value, all models showed regular improvements in RMSE, MAE, MSE, and R<sup>2</sup>. The threshold value of (*ρ*) = 0.8 allowed Kumar *et al. Discover Applied Sciences* (2026) 8:480 Page 18 of 29

<span id="page-17-0"></span>

| Table 6 Sensitivity analysis of frequency-domain GNN models to different correlation thresholds |
|-------------------------------------------------------------------------------------------------|
| used during graph construction                                                                  |

| Model | Threshold (ρ) | RMSE    | MAE     | R2     | MSE      |
|-------|---------------|---------|---------|--------|----------|
| GCN   | 0.3           | 22.5874 | 16.4389 | 0.8486 | 510.1867 |
| GCN   | 0.5           | 21.4361 | 15.7683 | 0.8659 | 459.5104 |
| GCN   | 0.8           | 20.6032 | 15.1072 | 0.8828 | 424.4910 |
| GRN   | 0.3           | 17.8326 | 12.4879 | 0.9041 | 318.0316 |
| GRN   | 0.5           | 16.9423 | 11.8942 | 0.9168 | 287.0445 |
| GRN   | 0.8           | 16.0865 | 11.3010 | 0.9285 | 258.7771 |
| GAT   | 0.3           | 1.0426  | 0.8413  | 0.8874 | 1.0870   |
| GAT   | 0.5           | 0.9589  | 0.7764  | 0.9042 | 0.9195   |
| GAT   | 0.8           | 0.8750  | 0.7160  | 0.9190 | 0.7656   |

<span id="page-17-1"></span>**Table 7** Performance of GCN, GRN, and GAT models on frequency-domain features selected using correlation threshold of 0.8

| Model | Epochs | Early stop | RMSE    | MAE     | R2     | MSE      |
|-------|--------|------------|---------|---------|--------|----------|
| GCN   | 100    | 72         | 20.6032 | 15.1072 | 0.8828 | 424.4910 |
| GRN   | 100    | 100        | 16.0865 | 11.3010 | 0.9285 | 258.7771 |
| GAT   | 100    | 79         | 0.8750  | 0.7160  | 0.9190 | 0.7656   |

<span id="page-17-2"></span>![](_page_17_Figure_5.jpeg)

**Fig. 8** Comparison of GCN, GRN, and GAT predictions on frequency-domain features with training vs validation loss

the best performance for all architectures and was thus considered for final frequencydomain evaluation (Table [6\)](#page-17-0).

The outcomes presented, including RMSE, MAE, Coefficient of Determination (*R*<sup>2</sup>), and MSE, are compiled in Table [7](#page-17-1). Among the various models, the GAT model performed the best, demonstrating the least RMSE at 0.8614 and *R*<sup>2</sup> of 0.9190, which indicates how best GAT could capture frequency domain features. The GCN performed competitively, but in comparison, the GRN yielded a higher RMSE and MSE, indicating weaker performance in modeling the spectral dependencies (Figs. [8](#page-17-2), [9](#page-18-0)).

#### **4.3 Retraining of best performing models (GAT and GRN)**

The top performers from the initial assessment of the frequency- and time-domain feature sets were the time-domain GRN and frequency-domain GAT. In response, both constructions were retrained with an adaptive learning rate and an increased epoch limit of 150 for generalization enhancement and the model's ability to learn advanced temporal dependencies. An early stopping technique with a 0.3 patience parameter, in which

<span id="page-18-0"></span>![](_page_18_Figure_1.jpeg)

**Fig. 9** Comparison of GCN, GRN, and GAT predictions on frequency-domain features with Actual VS Predicted Value

<span id="page-18-1"></span>![](_page_18_Figure_3.jpeg)

**Fig. 10** Training and validation loss curves of the retrained models: **a** GAT in the frequency domain, **b** GRN in the time domain

training was terminated to avoid overfitting when there were minimal changes in progress, was employed (Figs. [10](#page-18-1), [11\)](#page-19-0).

The GRN's ability to learn and model sequential dependencies in time was further enhanced by the model's recurrent nature, while the GAT model used multi-head attention to amplify feature representation in the frequency domain. Error score retraining results are summarized in Table [8.](#page-19-1)

The findings emphasize that the GRN produced better predictive performance in the time domain with an *R*<sup>2</sup> of 0.9707 and significantly outperformed the GAT on the same domain. In contrast, the GAT had excellent performance in the frequency domain with an *R*<sup>2</sup> of 0.9118. The complementary behavior also emphasizes the significance of domain-specific modeling approaches when using graph-based deep learning for time series regression problems.

#### **4.4 Hyperparameter tuning of GAT and GRN models with RFR features**

To further improve model performance and analyze the interaction between optimization strategies and GNN architectures, hyperparameter tuning was conducted using two widely adopted approaches: Optuna with a Tree-structured Parzen Estimator (TPE) Kumar *et al. Discover Applied Sciences* (2026) 8:480 Page 20 of 29

<span id="page-19-0"></span>![](_page_19_Figure_1.jpeg)

**Fig. 11** Predicted vs actual tool wear values for retrained models

<span id="page-19-1"></span>**Table 8** Retrained GAT and GRN Evaluation (RFR Features)

| Model & domain         | No. of epochs | Early stopping | RMSE    | MAE    | R2     | MSE      |
|------------------------|---------------|----------------|---------|--------|--------|----------|
| GAT (Frequency Domain) | 150           | 59             | 0.9129  | 0.7545 | 0.9118 | 0.8334   |
| GRN (Time Domain)      | 150           | 150            | 10.3083 | 6.7376 | 0.9707 | 106.2629 |

sampler and Bayesian Optimization. Rather than exhaustively describing parameterlevel variations, this section focuses on the comparative behavior and practical impact of these optimization strategies on GAT and GRN models for tool wear RUL prediction.

#### *4.4.1 Hyperparameter tuning of GAT and GRN models with RFR features using optuna*

Using Optuna, hyperparameters were optimized over 20 trials with 300 training epochs per trial. Optuna consistently identified configurations that favored stable convergence for temporal modeling, particularly for the GRN architecture. The optimized GRN achieved the best overall time-domain performance, indicating that Optuna's adaptive sampling strategy is well suited for models with strong temporal dependencies and sensitive learning dynamics (Figs. [12](#page-20-0), [13,](#page-20-1) Table [9\)](#page-20-2).

In the **GAT (Frequency Domain)**, the optimal parameters were a hidden dimension equal to 64, gauged to be the best at 3, with a very small dropout rate at around 0.021, and a learning rate equal to 0.0029. From this configuration the model managed to produce a RMSE equal to MSE equal to 6.28 and an *R*<sup>2</sup> score equal to 0.9763 with a Pearson coefficient intact at 0.9888. This shows the eficiency of the approach using multi-head attention to capture the realtion with the data with multiple heads.

In the **GRN (Time Domain)**, a larger hidden dimension (256), dropout were also of considerable proportion at 0.31, A small a minor batch size of 32 was utilized with a learning rate set to a value of 0.00051. This model produced the best performance with a RMSE at 3.68, and MAE at 2.65 and an *R*<sup>2</sup> of 0.9963 with the Pearson coefficient exceeding at about 0.99 of the best values demonstrated the GRN model to capture minor Wear patterns in a temporal series.

Kumar *et al. Discover Applied Sciences* (2026) 8:480 Page 21 of 29

<span id="page-20-0"></span>![](_page_20_Figure_1.jpeg)

**Fig. 12** Training and validation loss curves for hyperparameter-tuned models

<span id="page-20-1"></span>![](_page_20_Figure_3.jpeg)

**Fig. 13** Predicted vs actual tool wear for hyperparameter-tuned models using Optuna

<span id="page-20-2"></span>**Table 9** Hyperparameter-tuned GAT and GRN evaluation results (Optuna)

| Model & domain         | RMSE   | MAE    | R2     | MSE     |
|------------------------|--------|--------|--------|---------|
| GAT (Frequency Domain) | 9.2545 | 6.3640 | 0.9763 | 85.6451 |
| GRN (Time Domain)      | 3.6830 | 2.6537 | 0.9963 | 13.5645 |

### *4.4.2 Hyperparameter tuning of GAT and GRN models with RFR features using Bayesian optimization*

Bayesian Optimization was applied to explore a smoother and more global search of the hyperparameter space. This strategy proved particularly effective for the GAT model in the frequency domain, where attention mechanisms benefited from more conservative and structured parameter exploration. Compared to Optuna, Bayesian Optimization demonstrated improved generalization for attention-based architectures, albeit with reduced effectiveness for recurrent graph models.

The final Bayesian-tuned model performance is summarized below (Figs. [14](#page-21-0), [15](#page-21-1), Table [10\)](#page-21-2):

These outcomes show that Bayesian Optimization probably has success because of the smooth and structured parameter space configuration for GAT. However, GRN, which has recurrent memory components, may need a broader search which may explain why GRN did so much better with Optuna's TPE-based sampling. In the end, Bayesian

<span id="page-21-0"></span>![](_page_21_Figure_1.jpeg)

![](_page_21_Figure_2.jpeg)

**Fig. 14** Training and validation loss curves for hyperparameter-tuned models

<span id="page-21-1"></span>![](_page_21_Figure_6.jpeg)

![](_page_21_Figure_7.jpeg)

**Fig. 15** Predicted vs actual tool wear for hyperparameter-tuned models using bayesian optimization

<span id="page-21-2"></span>**Table 10** Hyperparameter-tuned GAT and GRN evaluation results (Bayesian Optimization)

| Model & domain         | RMSE    | MAE     | R2     | MSE      |
|------------------------|---------|---------|--------|----------|
| GAT (Frequency Domain) | 13.5095 | 9.9422  | 0.9487 | 182.5053 |
| GRN (Time Domain)      | 17.2065 | 13.1237 | 0.9167 | 296.0643 |

Optimization gives a valuable better performing search mechanism more usable for attention-based GNNs as a more principal Global Optimizer compared to Optuna.

#### *4.4.3 Comparison between optuna and Bayesian optimization*

The comparative analysis reveals that the effectiveness of a hyperparameter optimization strategy is closely tied to the inductive biases of the underlying GNN architecture. Optuna's TPE-based sampler demonstrated superior performance for GRN models by effectively navigating sensitive temporal dynamics and identifying configurations that support stable long-term dependency learning. In contrast, Bayesian Optimization was more effective for GAT models, where attention mechanisms benefit from smoother hyperparameter landscapes and conservative exploration.

These results indicate that no single optimization strategy is universally optimal. Instead, the choice of optimizer should be guided by the architectural characteristics of the model and the nature of the feature domain. Optuna is better suited for recurrent and temporally sensitive graph models, whereas Bayesian Optimization provides advantages for attention-based architectures operating in frequency-dominant representations.

Kumar *et al. Discover Applied Sciences* (2026) 8:480 Page 23 of 29

#### *4.4.4 Interpretation of optimized hyperparameters*

Other than identifying the best configurations, one should also learn how each of the hyperparameters that has been configured optimally affects the learning dynamics of the model and how they contribute to the increased RUL prediction. This research considers two of the hyperparameters search methodologies, Optuna (TPE-based) and Bayesian Optimization, and their configured parameters underscore fundamental differences in architectural behavior for GAT and GRN.

*Hidden dimension.* The hidden dimension determines how much information a node embedding can hold and therefore how much expressive capability a GNN has. For GAT, Optuna found the hidden size of 64 to be optimal, which aligns with the findings of attention-based models which perform better with smaller representations and selective feature weighting. On the other hand, GRN had a much larger optimal hidden size of 256, which is needed in order to store long-term temporal dependencies with its recurrent memory mechanism.

GRN was able to utilize smaller hidden dimensions with Bayesian Optimization, and while this was detrimental to its ability to capture temporal degradation patterns, and thus contributed to its poorer performance compared to the Optuna tuned GRN, this was in a more positive light for GAT which also Bayesian search assigned smaller hidden dimensions to. This indicates the surrogate model to be more favorable of smoother parts of the search space, which enables GAT to retain its competitive performance, relative to other GNN models, despite being tuned with Bayesian Optimization. The difference in the optimal hidden size for the different tuning strategies shows how different the inductive biases are between GRN and GAT, with temporal models needing to have a wider memory capacity and attention models relying more with feature selection over the width of the embedding.

*Dropout rate.*

Optuna showed that GRN does well with a high dropout rate as extra regularization helps mitigate overfitting brought on by the recurrent memory accumulation through time steps. In comparison, less dropout was needed by GAT as too much dropout would impair the stability of attention weight computations and reduce the model's ability to attend to useful spectral components. In GAT, Bayesian Optimization has an inclination toward converging with moderately higher dropout values relative to Optuna. While this resulted in a slight increase in generalization, the attention weights lost selectiveness leading to a small decrease in relative predictive performance. For GRN, Bayesian search frequently resulted in the selection of dropout values that were excessively higher, leading to too much oversmoothing in the hidden-state dynamics. This oversmoothing led to the model's inability to capture small spatial temporal wear pattern leading to poor performance relative the GRN tuned by Optuna.

*Depth of the GNN (graph neural network) layers.* Optuna showed that the GAT with 3 layers was the best fit for depth to capture a multi-hop and spectral dependency while keeping training stable. Similar convergence has been witnessed in Bayesian Optimization with GATs that are, in some cases, slightly deeper suggesting that the attention mechanisms are a good fit for the more structured and surrogate centered global search offered by Bayesian Optimization. That was not the case with GRN, however, as it showed less stable convergence in deeper architectures while tuning with Bayesian Optimization. Additional layers of recurrent graphs lead to greater message passing Kumar *et al. Discover Applied Sciences* (2026) 8:480 Page 24 of 29

and greater recursion over time which increases the possibility of a catastrophe with exploding and over-smoothing of the gradient. This resulted in the deeper configurations of GRN selected via Bayesian Optimization to be less useful than the ones found by Optuna which showcased a more optimal architecture in maintaining the integrity of the temporal signals.

*Learning rate.* The two hyperparameter search methods had different preferences for learning rates. Optuna determined a very low learning rate for the GRN (0.00051), which helps avoid the exploding and vanishing gradient problems that are especially important for capturing the more subtle recurrent changes in tool wear. On the other hand, for GAT, Optuna determined a relatively high learning rate (0.0029), which enables quicker optimization of attention weights and more efficient learning of the prevalent patterns in the spectral domain.

Bayesian optimization, on the other hand, preferred more moderate and conservative learning rates for both models. While more balanced learning rates can help in maintaining stability, they can also impose a convergence lag, especially for models that require high rates of aggressive learning (like GAT) or that need finely tuned updates (like GRN). This is partially why GAT was able to perform reasonably well under Bayesian optimization while GRN couldn't. The learning rate picked by Bayesian optimization was simply not low enough to capture the more subtle temporal changes that the GRN had, which resulted in maintaining a slower convergence rate and hence, predictive accuracy that was lower than that of the Optuna tuned GRN.

*Batch size.* Optuna's findings revealed that smaller batch sizes (for example, 32) led to greater GRN stability as smaller batch sizes allow for more frequent and gradual parameter updates that greatly benefit many temporal models. Due to attention-based feature aggregation, GAT was less affected by batch size as it does not have the same sequential processing. On the other hand, Bayesian Optimization would sometimes choose larger batch sizes leading to increased gradient smoothness but less temporal granularity to GRN. GRN's comparatively lower performance with the Bayesian tuning strategy was due to this weaker preservation of short-term wear patterns. For GAT this was less pronounced as performance was more dependent on selective spectral feature weighting, as opposed to batch-wise temporal structure, than on performance.

*Summary.* The optimized hyperparameters across both tuning strategies reflect the distinct inductive biases of the two architectures. GRN requires strong temporal capacity, smaller learning rates, and higher regularization—conditions that Optuna's TPE sampler identified effectively. GAT, on the other hand, benefits from smooth hyperparameter landscapes, making Bayesian Optimization well-suited for attention-based modeling. These differences explain why GRN performed best under Optuna, while Bayesian Optimization yielded comparatively better generalization for GAT.

#### <span id="page-23-0"></span>**4.5 Discussion**

Variations in spindle speed, feed rate, and depth of cut are inherent parts of milling operations, affecting vibration patterns, force signatures, and tool–workpiece interaction in general. Although there was a limitation in the number of samples for some machining conditions, the available dataset can be used to gain valuable insight into the behavior of the three GNN models:

Kumar *et al. Discover Applied Sciences* (2026) 8:480 Page 25 of 29

• **GRN**, that models time and file sequential order, which performs, on average, the best during progressive or smooth wear, where time-domain statistics, on the average, vary slightly within and across windows.

- **GAT**, with its attention mechanism, performed comparatively better under high-speed and vibration-intensive cutting conditions, where dominant spectral components emerge. The ability of GAT to selectively focus on the most informative frequency nodes enhances its performance in frequency-domain scenarios.
- **GCN** showed stable performance under consistent machining conditions due to its uniform neighborhood aggregation. However, it may struggle to capture sudden or localized variations under highly dynamic loads.

In addition to being used for performance evaluation, the obtained data set allows us to examine GNN architecture design choices within the context of RUL estimation of a milling tool. The findings that GRN excels in the time domain and GAT performs very well in the frequency domain indicate, respectively, that GNNs have a natural advantage when modeling long-range temporal relationships during a progressive degradation process, while the use of attention mechanisms is helpful when trying to focus on dominant spectral patterns amidst vibration-heavy ambient conditions. These findings confirm that there is no GNN architecture universally superior in RUL prediction tasks, but architecture, domain, and method must match or align, as implicitly argued in this work.

These findings help highlight the effectiveness of the inductive bias present in different GNN architectures for specific machining processes. Moreover, the two techniques for hyperparameter optimization used in this study, Optuna and Bayesian Optimization, have also highlighted these differences. Optuna optimization has always converged on GRN as the better algorithm for time-domain data, while Bayesian Optimization has been able to show better performance for GAT on the frequency-domain data.

*Effect of graph sample-size imbalance.*

One of the major reasons why there are varying performances in time domain and frequency domain models has to do with the unequal number of graph samples available to each model. The time domain processing strategy produces 31,000 graph samples because of its high graph segmentation rate compared to FFT graph transformation processing in the frequency domain, which produces 980 graphs. There is a 32 times difference in graph samples that are available to each model.

The increased number of graphs based on the time domain offers greater resolution and a more detailed depiction of the development of progressive wear. This allows the models, especially GRN, to better capture the smooth trend associated with degradation. The depiction based on the frequency domain offers a more compressed summary that relies more on the spectral aspects. While this is useful for capturing a progression that is rich in vibrations, it is important to note that it has a lower number of instances, and its results are more prone to noise.

Therefore, part of the observed discrepancy in RMSE and *R*<sup>2</sup> between time-domain and frequency-domain experiments should be attributed not to the architectural limitations of the GNN models, but to intrinsic differences in data volume and representation granularity. This observation lends great importance to interpreting the results in the frequency domain within a limited-sample regime and highlights the complementary role of timeand frequency-domain modeling for milling tool wear prediction.

Kumar *et al. Discover Applied Sciences* (2026) 8:480 Page 26 of 29

*Dataset limitation:* This work is based on a single in-house milling dataset due to the fact that publicly available datasets with comparable sensor configurations and annotated tool wear are scant. Although there are several machining conditions for each type of material in the dataset, generalization cannot be comprehensively evaluated due to the absence of cross-dataset validation. However, the proposed correlation–temporal graph construction method is inherently extensible to other datasets by recalculating feature correlations and temporal edges.

*Future work:* Future research should be directed toward systematic condition-wise analysis across a more extensive and balanced dataset, evaluation across multiple milling datasets and machines, and the integration of transfer learning or domain adaptation techniques. These would further strengthen generalization and prepare the framework for deployment in diverse industrial environments.

While the existence of variance in this real-world effect of data imbalance translates to challenges in practical applications of feature extraction in the frequency domain, future research aims to consider techniques like adaptive windowing, data augmentation in the spectral space, as well as transfer learning across domains.

#### **4.6 Computational efficiency and real-time feasibility**

In addition to predicted performance, practical deployment of tool wear monitoring systems also needs to factor in cost of computation and inference latency especially in edge and embedded systems in CNC machines. The three GNN architectures used in this experiments in this study have different computative characteristics informing different suitability and levels of performance for sustained real time monitoring.

*GCN efficiency.* GCN does simple neighborhood aggregation using normalized matrix multiplication, which is low computing complexity and low inference latency. Because of the low overhead, and thus lightweight cost of performance of the graph convolutions, GCN is especially preference for edge deployment systems where real time tool wear decisions have to be made in short cycle times.

*GRN latency considerations.* GRN incorporates recurrent units (GRU/LSTM) on top of graph propagation which on its own is already more complex computing wise than GCN and GAT. And while this architecture allows to turn temporal wear progression into something that can be learned, that is latency wise an expensive architecture. fire is placed for more real time performance and in monitoring observations that requires more than once cycle in an inferencing structure the sub one hundred milliseconds is a must have for many systems in CNC use.

*GAT models and overshoot computation details.* As opposed to GCN, GAT calculates edge attention coefficients, and thus incurs more of a computational overhead. This overhead is especially relevant to highly connected or large nodes dense graphs. But, attention score calculation is where the GAT is efficient in the forward pass, and thus this is streamlined through the increase in computational overhead.Even in demanding applications, a small attention-head or a sparse attention variant can be efficiently applied to targeted feature domains. Latency can be suppressed to advantageous levels, but performance to GATS is lost.

*Overall assessment.* The proposed GNN-RFR framework with the rather small graphs and small time frames in the feature computing used in this problem allows, with a contemporary embedded processor, for GCN or a less heavy derivative of GAT to drop Kumar *et al. Discover Applied Sciences* (2026) 8:480 Page 27 of 29

computation latency to less than 100 ms. Also, for an field deployment of the predictions less than 100 ms, GCN or a light derivative GAT lead to more efficient computation and similar performance. This should be more models in edge computers, like the Jetson, other industrial MCUs, and reasonably estimate of real time latency and memory.

#### <span id="page-26-0"></span>**5 Conclusion**

This research details the development of the first fully integrated graph-based deep learning architecture for the analysis of multi-sensor vibration, spindle load, and cutting force signals to predict the remaining useful life of milling tools. In the time and frequency domains, features that were extracted and encoded into correlation-temporal graphs, which permitted the use of the GCN, GRN, and GAT to capture the featuresínterdependencies and the sequence of wear. At the end of the sequence, a Random FoRest Regression head was opted for predicting due to its ability to perform complex nonlinear regression.

This research records that GRN has the best overall result across time-domain of features, while GAT has the best overall result across frequency-domain of features. In addition, both Optuna and Bayesian optimisation improved the model, especially GRN for Optuna and GAT for Bayesian optimisation. These results demonstrate the impact that feature-domain characteristics and architecture inductive biases have on tool-wear predictive outcomes.

Even though the proposed machine learning framework achieves a high predictive accuracy, the study was confined to a single in-house milling dataset. Generalization will most likely be improved by substantial validation across several tools, machine types, and cutting conditions, which is the priority for the immediate future.

Future research may extend this work in the following directions:

- *Integration of physics-based modeling:* Combining physical wear mechanisms with deep learning to improve interpretability and robustness.
- *Advanced graph construction methods:* Exploring dynamic graph learning, selfsupervised edge discovery, and graph sparsification for more adaptive graph structures.
- *Cross-machine transfer learning:* Transferring trained models across different CNC machines, tool geometries, and machining environments.
- *Edge-device deployment:* Designing lightweight GNN variants and profiling computational latency for real-time industrial implementation.
- *Condition-wise analysis:* Performing systematic studies under varied cutting speeds, feed rates, and depths of cut using larger, balanced datasets.

Overall, this research demonstrates the strong potential of graph neural networks for predictive maintenance and tool-wear monitoring, paving the way for more intelligent, adaptive, and sustainable manufacturing systems.

#### **Abbreviations**

RUL Remaining useful life FFT Fast Fourier transform SFS Sequential feature selection ML Machine learning SVM Support vector machine CNN Convolutional neural network RNN Recurrent neural network DL Deep learning

| LSTM | Long short-term memory      |
|------|-----------------------------|
| GRU  | Gated recurrent unit        |
| RMSE | Root mean square error      |
| MSE  | Mean square error           |
| MAE  | Mean absolute error         |
| GNN  | Graph neural network        |
| GCN  | Graph convolutional network |
| GAT  | Graph attention network     |
| GRN  | Graph recurrent network     |
| RFR  | Random forest regressor     |
| PSD  | Power spectral density      |
|      |                             |

#### **Acknowledgements**

We acknowledge Symbiosis International (Deemed University), Pune, for research support. We also thank the anonymous reviewers for their valuable suggestions that enriched this study.

#### **Author Contributions**

S.K. contributed to conceptualization. S.K., D.R., and S.S. were involved in manuscript writing. S.K., S.S., and V.W. contributed to methodology. A.B. performed formal analysis. S.S., V.W. and V.J. carried out data curation. S.K. and A.B. provided resources, supervision, and funding acquisition.

#### **Funding:**

Open access funding provided by Symbiosis International (Deemed University). None.

#### **Data availability**

The datasets used and analyzed during the current study are available from the corresponding author upon reasonable request. Due to confidentiality agreements and institutional policies, access to certain data may be restricted. However, processed and anonymized data supporting the findings of this study can be made available upon request for academic and research purposes.

#### **Declarations**

#### **Ethics approval and consent to participate**

Not applicable.

#### **Consent to publish**

All listed authors grant permission for publication.

#### **Conflict of interest**

The authors report there are no conflict of interest to declare.

Received: 28 September 2025 / Accepted: 3 February 2026

#### **References**

- <span id="page-27-0"></span>1. Mallioris P, Aivazidou E, Bechtsis D. Predictive maintenance in industry 4.0: a systematic multi-sector mapping. CIRP J Manuf Sci Technol. 2024;50:80–103.
- <span id="page-27-1"></span>2. Wang Y, Wu M, Li X, Xie L, Chen Z. A survey on graph neural networks for remaining useful life prediction: methodologies, evaluation and future trends. Mech Syst Signal Process. 2025;229:112449. [https://doi.org/10.1016/j.ymssp.2025.112449.](https://doi.org/10.1016/j.ymssp.2025.112449)
- <span id="page-27-2"></span>3. Jones T, Cao Y. Tool wear prediction based on multisensor data fusion and machine learning. Int J Adv Manuf Technol. 2025;1–13.
- <span id="page-27-3"></span>4. Corso G, Stark H, Jegelka S, Jaakkola T, Barzilay R. Graph neural networks. Nat Rev Methods Primers. 2024;4(1):17. [https://do](https://doi.org/10.1038/s43586-024-00294-7) [i.org/10.1038/s43586-024-00294-7.](https://doi.org/10.1038/s43586-024-00294-7)
- <span id="page-27-4"></span>5. Deng L, Liu J, Liu M, Cao Y, Wen C, Deng X. Remaining useful life prediction based on cross-temporal dynamic graph convolutional network. Eksploatacja i Niezawodność-Maintenance and Reliability. 2025;27(4). [https://doi.org/10.17531/ein](https://doi.org/10.17531/ein/203249) [/203249](https://doi.org/10.17531/ein/203249)
- <span id="page-27-5"></span>6. Chen Y, Zeng A, Yu Q, Zhang K, Yuanpeng C, Wu K, et al. Recurrent temporal revision graph networks. Adv Neural Inf Process Syst. 2023;36:69348–60.
- <span id="page-27-6"></span>7. Wei Y, Wu D, Terpenny J. Remaining useful life prediction using graph convolutional attention networks with temporal convolution-aware nested residual connections. Reliab Eng Syst Saf. 2024;242:109776. [https://doi.org/10.1016/j.ress.2023.1](https://doi.org/10.1016/j.ress.2023.109776) [09776](https://doi.org/10.1016/j.ress.2023.109776).
- <span id="page-27-7"></span>8. Tambake N, Deshmukh B, Pardeshi S, Salunkhe S, Čep R, Abouel NE. Condition monitoring of a cnc hobbing cutter using machine learning approach. Adv Mech Eng. 2024;16(9):16878132241275750. [https://doi.org/10.1177/1687813224127575](https://doi.org/10.1177/16878132241275750) [0](https://doi.org/10.1177/16878132241275750).
- <span id="page-27-8"></span>9. Pashmforoush F, Ebrahimi Araghizad A, Budak E. Physics-informed tool wear prediction in turning process: a thermomechanical wear-included force model integrated with machine learning. J Manuf Syst. 2024;77:266–83. [https://doi.org/1](https://doi.org/10.1016/j.jmsy.2024.09.008) [0.1016/j.jmsy.2024.09.008](https://doi.org/10.1016/j.jmsy.2024.09.008).
- <span id="page-27-9"></span>10. Wu J, He D, Jin Z, Zhao M, Sun H, Wang Y. Remaining useful life prediction of lithium-ion battery based on real-time decomposition and tightly coupled convolutional informer. Renew Energy. 2025;253:123641. [https://doi.org/10.1016/j.ren](https://doi.org/10.1016/j.renene.2025.123641) [ene.2025.123641.](https://doi.org/10.1016/j.renene.2025.123641)

- <span id="page-28-0"></span>11. Wu F, Wu Q, Tan Y, Xu X. Remaining useful life prediction based on deep learning: a survey. Sensors. 2024;24(11):3454. <https://doi.org/10.3390/s24113454>.
- <span id="page-28-1"></span>12. Li T, Zhao Z, Sun C, Yan R, Chen X. Hierarchical attention graph convolutional network to fuse multi-sensor signals for remaining useful life prediction. Reliab Eng Syst Saf. 2021;215:107878.<https://doi.org/10.1016/j.ress.2021.107878>.
- <span id="page-28-2"></span>13. Wu J, He D, Li J, Miao J, Li X, Li H, et al. Temporal multi-resolution hypergraph attention network for remaining useful life prediction of rolling bearings. Reliab Eng Syst Saf. 2024;247:110143.<https://doi.org/10.1016/j.ress.2024.110143>.
- <span id="page-28-3"></span>14. He Y, Su H, Zio E, Peng S, Fan L, Yang Z, et al. A systematic method of remaining useful life estimation based on physicsinformed graph neural networks with multisensor data. Reliab Eng Syst Saf. 2023;237:109333. [https://doi.org/10.1016/j.res](https://doi.org/10.1016/j.ress.2023.109333) [s.2023.109333](https://doi.org/10.1016/j.ress.2023.109333).
- <span id="page-28-4"></span>15. Xia Y, Zheng G, Li Y, Liu H. A spatial-temporal adaptive graph convolutional network with multi-sensor signals for tool wear prediction. Appl Sci. 2025;15(4):2058. <https://doi.org/10.3390/app15042058>.
- <span id="page-28-5"></span>16. Vrahatis AG, Lazaros K, Kotsiantis S. Graph attention networks: a comprehensive review of methods and applications. Future Internet. 2024;16(9):318. <https://doi.org/10.3390/fi16090318>.
- <span id="page-28-6"></span>17. Wu J, He D, Jin Z, Zhao M, Li X, Chen Y. Multi-view fully connected graph to fuse multi-sensor signals for mechanical equipment remaining useful life prediction. J Manuf Syst. 2025;80:1029–52.<https://doi.org/10.1016/j.jmsy.2025.05.009>.
- <span id="page-28-7"></span>18. Li S, Li J, Zhu K. Application of physics-guided deep learning model in tool wear monitoring of high-speed milling. Mech Syst Signal Process. 2025;224:111949. [https://doi.org/10.1016/j.ymssp.2024.111949.](https://doi.org/10.1016/j.ymssp.2024.111949)
- <span id="page-28-8"></span>19. Si S, Mu D, Si Z. Intelligent tool wear prediction based on deep learning psd-cvt model. Sci Rep. 2024;14(1):20754. [https://](https://doi.org/10.1038/s41598-024-71795-4) [doi.org/10.1038/s41598-024-71795-4.](https://doi.org/10.1038/s41598-024-71795-4)
- <span id="page-28-9"></span>20. Yau H-T, Kuo P-H, Hong S-W. Milling wear prediction using an artificial neural network model. Eng Appl Artif Intell. 2024;135:108686.<https://doi.org/10.1016/j.engappai.2024.108686>.
- <span id="page-28-10"></span>21. Truong TT, Airao J, Karras P, Hojati F, Azarhoushang B, Aghababaei R. Data-driven prediction of tool wear using Bayesian regularized. Sci Direct. 2024.<https://doi.org/10.1016/j.measurement.2024.115303>.
- <span id="page-28-11"></span>22. Guo D, Zhou H, Sun L, Li G. Unlabeled-data-enhanced tool remaining useful life prediction based on graph neural network. Sensors. 2025;25(13):4068. [https://doi.org/10.3390/s25134068.](https://doi.org/10.3390/s25134068)
- <span id="page-28-12"></span>23. Cheng Y, Lu M, Gai X, Guan R, Zhou S, Xue J. Research on multi-signal milling tool wear prediction method based on gafresnext. Robot Comput-Integr Manuf. 2024;85:102634. [https://doi.org/10.1016/j.rcim.2023.102634.](https://doi.org/10.1016/j.rcim.2023.102634)
- <span id="page-28-13"></span>24. Lin Z, Fan Y, Tan J, Li Z, Yang P, Wang H, et al. Tool wear prediction based on xgboost feature selection combined with psobp network. Sci Rep. 2025;15(1):3096.<https://doi.org/10.1038/s41598-025-85694-9>.
- <span id="page-28-14"></span>25. Sipper M, Moore JH. Conservation machine learning: a case study of random forests. Sci Rep. 2021;11:3629. [https://doi.org](https://doi.org/10.1038/s41598-021-83247-4) [/10.1038/s41598-021-83247-4](https://doi.org/10.1038/s41598-021-83247-4).
- <span id="page-28-15"></span>26. Hodson TO. Root mean square error (RMSE) or mean absolute error (MAE): when to use them or not. Geosci Model Dev Discuss. 2022;2022:1–10.<https://doi.org/10.5194/gmd-15-5481-2022>.

#### **Publisher's Note**

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.
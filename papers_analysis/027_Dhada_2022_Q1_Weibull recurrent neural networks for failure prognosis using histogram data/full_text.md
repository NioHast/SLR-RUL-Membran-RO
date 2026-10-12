## S.I.: APPLICATIONS OF MACHINE LEARNING IN MAINTENANCE ENGINEERING AND MANAGEMENT (IFAC AMEST 2020)

![](_page_0_Picture_2.jpeg)

# Weibull recurrent neural networks for failure prognosis using histogram data

Maharshi Dhada<sup>1</sup> · Ajith Kumar Parlikad<sup>1</sup> · Olof Steinert<sup>2</sup> · Tony Lindgren<sup>3</sup>

Received: 10 July 2021/Accepted: 22 July 2022/Published online: 3 September 2022 © The Author(s) 2022

#### **Abstract**

Weibull time-to-event recurrent neural networks (WTTE-RNN) is a simple and versatile prognosis algorithm that works by optimising a Weibull survival function using a recurrent neural network. It offers the combined benefits of the sequential nature of the recurrent neural network, and the ability of the Weibull loss function to incorporate censored data. The goal of this paper is to present the first industrial use case of WTTE-RNN for prognosis. Prognosis of turbocharger conditions in a fleet of heavy-duty trucks is presented here, where the condition data used in the case study were recorded as a time series of sparsely sampled histograms. The experiments include comparison of the prediction models trained using data from the entire fleet of trucks vs data from clustered sub-fleets, where it is concluded that clustering is only beneficial as long as the training dataset is large enough for the model to not overfit. Moreover, the censored data from assets that did not fail are also shown to be incorporated while optimising the Weibull loss function and improve prediction performance. Overall, this paper concludes that WTTE-RNN-based failure predictions enable predictive maintenance policies, which are enhanced by identifying the sub-fleets of similar trucks.

Keywords Prognosis · Statistical modelling · Neural networks · Machine learning · Weibull distribution

#### 1 Introduction

Real-time asset condition data from embedded sensors, microprocessors, and communication technologies have extensively automated industrial operations over the recent decades. Asset failure prognosis in particular has evolved from relying on physics-based formulations to data-driven machine learning (ML) algorithms. Data-driven prognosis is significantly more flexible in terms of evaluating real-

This research was supported by Scania CV, Sweden.

- Maharshi Dhada mhd37@cam.ac.uk
- Department of Engineering, Institute for Manufacturing, University of Cambridge, Cambridge CB3 0FS, UK
- Strategic Product Planning and Advanced Analytics, Scania CV, Scania AB (publ), SE-151 87 Södertälje, Sweden
- Department of Computer and Systems Sciences, Stockholm University, P.O. Box 7003, SE-164 07 Kista, Sweden

time asset reliabilities and the diversity of failures that can be predicted [5, 10, 22].

Prognosis also forms the bedrock for servitisation, saving production costs and times for the manufacturing industries by enabling real-time asset health analyses. Manufacturers selling servitised contracts are responsible for the asset uptime and their associated maintenance costs [28]. This is made possible by predictive maintenances policies characterised by optimal procurement of spare parts and labour, thus saving significant production costs for the service providers [11, 21]. Data-driven prognosis techniques enable the manufacturers to predictively plan the maintenance activities for imminent failures, compared to the traditional preventive and corrective maintenance policies relying on a fixed maintenance schedule/ plan of action.

Data-driven prognosis involves evaluating either the time until asset failure, or the probability of the asset's failure in a fixed time window into the future [34]. Regression or classification models are used for predictions in respective cases. A predictive model is usually trained

![](_page_0_Picture_19.jpeg)

using time series of observed asset condition data. Such a time series is known as a trajectory, where the asset condition is monitored since its healthy state [\[30](#page-13-0)]. Predictive models are trained using the asset condition parameters at each time-step as the features, and their remaining times before failures (if observed) as the required outputs. Comprehensive information about the algorithms used for optimising model parameters, feature extraction techniques, and evaluation measures can be found in [\[34](#page-13-0), [40](#page-13-0)].

## 1.1 Weibull time-to-event recurrent neural networks

In this context, Weibull time-to-event recurrent neural networks (WTTE-RNN) is a simple and versatile algorithm for discrete event predictions. It is simple enough to avoid data sparsity, and at the same time provides the operators with the necessary information for maintenance planning such as increasing, decreasing, or stationary risk. WTTE-RNN combines survival theory with recurrent neural networks, in order to generate a failure density curve of a given asset in real time. It involves optimising the parameters of a Weibull log-likelihood loss function describing the probability of occurrence of an event for the future time horizon of a given asset. As such, WTTE-RNN generates a failure density curve that enables the maintenance managers to make a risk-based maintenance decision depending on the variance of the density curve. A higher variance indicates a less confident prediction and vice versa. The Weibull function can be used either for discrete or continuous events, but the current application of industrial prognosis is treated as discrete event prediction.

The parameters of the Weibull loss function are optimised using a recurrent neural network (RNN). RNNs are Turing-complete and can learn complex temporal patterns, corresponding to the typical characteristics of industrial failure data such as nonlinearity, noise, and time dependency [\[27](#page-13-0), [29](#page-13-0), [30](#page-13-0)]. The caveats of using recurrent neural networks, however, are that they require more computational resources than other regression methods and that they have a tendency towards overfitting [[35\]](#page-13-0). The first problem was handled in the experiments discussed here via parallel processing across the CPU cores, whereas overfitting was controlled by early-stopping and a network with few free parameters.

Another significant advantage of WTTE-RNN is its ability to use both censored and uncensored failure data for learning the failure statistics of the concerned fleet [\[27](#page-13-0), [29](#page-13-0)]. Often the industrial condition data originates from the assets that do not fail and is often unusable by off-the-shelf data-driven prognosis algorithms [\[23](#page-13-0)]. However, WTTE-RNN is able to incorporate the condition of not failing until the current time-step in its loss function, discussed later in Sect. [3](#page-4-0), and therefore account for the uncensored data in the fleet by flattening the failure density function until that time-step.

WTTE-RNN was first presented as a consumer churn prediction algorithm or a discrete event prediction in general in the Masters thesis [\[27](#page-13-0)]. Comparing with a standard binary fixed window prediction algorithm, [[27\]](#page-13-0) concluded that promising results were achieved with varying degrees of censoring and temporal resolution while using the run-to-failure data of simulated turbofans [\[27](#page-13-0)]. Consequently, WTTE-RNN enjoyed immediate popularity in the applications for discrete event predictions, mostly in the medical domain, for example, in [\[8](#page-12-0)] for hypoglycemic event prediction based on data collected by wearable devices and in [\[20](#page-12-0)] for breast cancer-related data. Several other applications in the medical prognosis field exist such as in [\[4](#page-12-0), [18](#page-12-0), [39\]](#page-13-0). WTTE-RNN also finds applications in telecom industry, such as in [\[33](#page-13-0)] which compared a multilayered perceptron (MLP) with WTTE-RNN algorithm for customer churn prediction in the telecom industry. However, [[33\]](#page-13-0) claimed based on their experimental results that the model performance of MLP was better than the WTTE-RNN, achieving a higher AUC, precision, and recall. In another application for change point detection in the industrial systems data, [\[17](#page-12-0)] compare the OC-SVM technique with the WTTE-RNN and conclude that WTTE-RNN eliminates the need for depending on the choice of the training data and the hyperparameters of the network, making it a good model in the absence of labelled data for cross-validation.

The first industrial prognosis applications for predicting failures in a fleet of simulated turbofans features in [[29\]](#page-13-0) and [\[30](#page-13-0)]. Both papers [[29](#page-13-0), [30](#page-13-0)] achieved performance improvement for WTTE-RNN via the technique of collaborative prognosis, which aims at identifying the subfleets of similarly operating assets and enabling learning across them by selectively pooling the training datasets. [\[26](#page-13-0)] presented an extensive analysis of using WTTE-RNN for prognosis of simulated turbofan failures by comparing WTTE-RNN with other standard prognosis techniques and concluded that WTTE-RNN was the most flexible and accurate. Other applications of WTTE-RNN for failure prediction include [\[1](#page-12-0), [15](#page-12-0), [16\]](#page-12-0).

The literature also presents several instances where the variants of WTTE-RNN have been developed to make it better suitable for a specific application, such as WTTE-CNN-LSTM in [[38\]](#page-13-0). [[38\]](#page-13-0) presents a variant of WTTE-RNN where a convolutional neural network is first used for data extraction, followed by using a long short-term memory network instead of an RNN. Based on a case study for failure prediction of a construction machinery component and theoretical foundation, [[38\]](#page-13-0) propose that the WTTE-CNN-LSTM model has a higher prediction

![](_page_1_Picture_11.jpeg)

accuracy. [[2\]](#page-12-0) presented experiments to identify an optimal neural network architecture of WTTE-RNN for machine failure prognosis. In another thesis [\[26](#page-13-0)], the author proposes several techniques and considerations for improving the performance of WTTE-RNN especially for the industrial prognosis applications. Lastly, [\[3](#page-12-0)] compares several algorithms for discrete events prediction, focusing on churn prediction, and say that the deep learning-based techniques such as WTTE-RNN show promising performance hoping to see the increasing reliability of such techniques in the future.

As such, the authors deem WTTE-RNN a highly suitable algorithm for industrial prognosis, for its ability to support risk-informed decision-making and to account for the censored data while generating the failure statistics of the fleet.

## 1.2 Histogram data for industrial prognosis

Asset condition data are often recorded by the industries as histograms, due to their memory efficiency and homogeneity across the variables [[13,](#page-12-0) [24\]](#page-13-0). Formally, the histogram data used for experiments in this paper are categorical histogram data, where a frequency is assigned to each bin [\[7](#page-12-0)]. Histograms are different than the often expected scalar input of the ML algorithms and must systematically be preprocessed to extract the information. On a wider scale, complex data structures different from the commonly encountered numeric and categorical variable types are studied under the field of symbolic data analysis [\[7](#page-12-0)]. But to the best of authors knowledge, literature presents only few instances which specifically target prognosis using histogram data.

These include the works of [\[9](#page-12-0), [32](#page-13-0)], and [\[12–14](#page-12-0)] who investigated compressor, battery failures, and NOx sensor failures in heavy-duty trucks, respectively. [[9\]](#page-12-0) did not clearly outline the preprocessing steps while using the histogram data, and the study of [[32\]](#page-13-0) was limited by the small fleet size used for analysis. The closest of the above three works to the case study discussed in this paper is that of [[12–14\]](#page-12-0) who used a dataset very similar to the one used here, but for a different prognosis technique and target component. The authors in [\[12–14](#page-12-0)] used random forest algorithm for classifying the data corresponding to failure and non-failure class. However, their technique relied on recursively combining the histogram bins using a sliding window, in contrast to the entropy of the histogram distributions used in this paper. The technique is detailed in later sections, but it essentially relies on evaluating the relative entropies of the consecutive histograms to quantify the deterioration in reduced dimension.

This paper presents the first industrial use case of WTTE-RNN for industrial prognosis. The idea was to predict turbocharger failures in a fleet of heavy-duty trucks owned by Scania CV (referred as Scania in the following text), so that maintenance activities can be planned in real time. There are a number of truck components that do not have an associated maintenance model with them; hence, at the moment Scania maintains them in a run until failure setting. The drivers can sometimes sense the symptoms of imminent failure and avoid such failures but in many cases failures lead to high costs; for late goods delivery, reloading, and towing tucks to workshop. Lately, Scania is facing an increased demand on operational availability from many customers. Accurate prognosis algorithms, like the WTTE-RNN algorithm, lower the customer costs and improve the uptimes of Scania trucks. WTTE-RNN also improves the situations at workshops as more work shifts from unplanned workshop visits to planned workshop visits. Since the condition data used in the case study were recorded as a time series of sparsely sampled histograms, a technique to preprocess such data is also shown.

In particular, the objectives of the paper are to (1) evaluate the efficacy of WTTE-RNN for prognosis using an industrial dataset and (2) present a technique for preprocessing sparsely sampled histogram data for prognosis.

The following paper is structured as: Section 2 explains the truck-fleet data and its preprocessing steps. The WTTE-RNN algorithm is briefly discussed in Sect. [3](#page-4-0), where the Weibull discrete loss function that allows the model to be trained on censored and uncensored failure data is mathematically described. Section [4](#page-6-0) presents the experimental cases to extensively analyse the efficacy of WTTE-RNN. Results obtained from the experiments are presented and discussed in Sect. [5.](#page-7-0) Finally, important conclusions are summarised in Section [6](#page-11-0).

## 2 Dataset description

This section discusses the structure and preprocessing steps for the turbochargers health data obtained from the Scania truck fleet. But first, the physical properties of the turbocharger are briefly discussed in the initial paragraphs.

Turbocharger is a modern improvement in the internal combustion engines, which increases the density of air going into the combustion chamber of the engines. Increased density of the inlet air improves the power output and efficiency compared to a naturally aspirated engine. A turbocharger is powered by the engine exhaust, further information about which can be found in [\[37](#page-13-0)]. Turbocharger are critical for a truck's operations, failure of which results in unplanned vehicle downtime and increased service costs for the maintenance provider.

Turbochargers health in the Scania trucks fleet were monitored by recording internal and environmental

![](_page_2_Picture_15.jpeg)

operating parameters such as ambient temperature and pressure, axle loads, boost air pressure over the course of the trucks' usage. Each parameter for a given truck was recorded as a histogram, such that the range of possible values for a given parameter was binned by separating it into intervals. The values falling in each of these bins represented the time that truck spent operating in that interval since it was commissioned. Whenever the conditions for sharing the data were met, the values corresponding to the histogram bins were recorded as a snapshot of data. These represented the time spent by the truck in each of those temperature ranges since it was commissioned.

Over the course of observation, a temporal evolution of the histograms could be obtained and analysed for failure prognosis. However, snapshots of these values were recorded at irregular intervals depending on the truck age, data contract with the customers, network capability, etc. This led to irregular and sometimes sparsely sampled timeseries data. The number of samples (snapshots of the histograms) per truck ranged from 10 to 30.

The data used for the case study presented herewith were collected from trucks that were monitored for a fixed period of time since they commenced their operations. Within this period, certain trucks experienced turbocharger failures while the rest didn't. As a result, prognosis here is a survival analysis problem where we have a population of trucks observed over time, and the goal is to predict the time until a new truck fails, given its turbocharger health data.

The fleet data were also typical due to the customisation offered by Scania. Customised trucks are best suitable for their end use, but at the same time diversify the fleet, thereby making turbocharger prognosis challenging. The specifications were categorical and did not evolve over time, for example the type of exhaust manifold, trailer connection, braking system, etc. Apart from the histogram and categorical types, certain parameters were also recorded as plain scalars. The combined set of all histogram, categorical, and scalar parameters constituted the overall operating conditions, and a representative sample of it is shown in Table 1. The Date\_recorded column in Table 1

Table 1 Representative example of the dataset containing different types of features in tabular format

| Truck id | Date recorded | Cat_1 | Cat_2 | Scalar_1 | H1_b1 | H1_b2 | H2_b1 | H2_b2 | H2_b3 |
|----------|---------------|-------|-------|----------|-------|-------|-------|-------|-------|
| 1        | 01-01-2000    | A     | E     | 32       | 6     | 8     | 4     | 2     | 8     |
| 1        | 05-06-2000    | A     | E     | 79       | 14    | 23    | 13    | 12    | 34    |
| 1        | 23-11-2000    | A     | E     | 136      | 43    | 76    | 98    | 43    | 132   |
| 2        | 03-02-2000    | B     | E     | 14       | 2     | 9     | 1     | 6     | 10    |
| 2        | 16-05-2000    | B     | E     | 67       | 21    | 87    | 24    | 76    | 129   |
| 2        | 12-01-2001    | B     | E     | 83       | 54    | 124   | 36    | 89    | 154   |
| 2        | 06-07-2001    | B     | E     | 178      | 98    | 201   | 67    | 103   | 198   |

![](_page_3_Picture_8.jpeg)

### 2.1 Preprocessing the dataset

The steps followed while preprocessing the Scania dataset are explained here and summarised as a flowchart in Fig. [2.](#page-5-0) Illustrations describing the corresponding changes in the raw data are shown wherever necessary in the flowchart.

As a first step, the trucks with a sampling frequency of at least 10 snapshots in 200 time-steps before the end of study were selected from the overall dataset. Out of all the trucks present in the fleet, 14% trucks encountered turbocharger failures. Next, the features relevant for predicting turbocharger failures were selected from all the parameters monitored by the sensors. Table [2](#page-5-0) describes the total histogram, categorical, and scalar features that were deemed useful for turbocharger prognosis, along with the examples corresponding to each feature type. These were selected based on a combination of expert knowledge and their prevalence across the fleet. Number of bins per each of the histogram variables were 8 (4), 10 (3), 12 (3), 18 (2), and 19 (2), where the numbers in the parentheses denote the number of operating parameters with the corresponding number of bins mentioned outside.

The condition data also comprised of features that were co-recorded as matrices, which are essentially two-dimensional histograms with either feature on each of its axes. For example, a matrix of axle load vs. speed is a twodimensional histogram, which records the time the truck spends in a given speed/ load combination. If a possible range of load is divided into 5 bins and that of speed into 8 bins, then the total bins in a matrix would be 5 8 ¼ 40

![](_page_3_Picture_13.jpeg)

<span id="page-4-0"></span>![](_page_4_Figure_2.jpeg)

**Fig. 1** Schematic description of a set of features recorded as histograms. The values in the array of recorded data correspond to the heights of the histograms, which in turn are the time spent by the truck in the corresponding bins

bins. An example of such a matrix is shown in Fig. 2. Matrices were converted into their constituent histograms by adding the elements across the axes, as illustrated in Fig. 2.

Because the histograms stored the time spent by the truck since its commissioning, it was important to subtract a given snapshot of bin values from the previous one. This way the histograms represented the truck's operation between consecutive snapshots. Therefore, the next preprocessing step involved evaluating differences between subsequent snapshots of the bin values (i.e.  $\sum_{i=1}^{n} [H_i^t - H_i^{t-1}])$  and normalising them (i.e.  $H_i^t = \frac{H_i^t - H_{\text{max}}^t}{H_{\text{max}}^t - H_{\text{min}}^t})$  where  $H_i^t$  is the  $i^{\text{th}}$  bin of the histogram consisting of n bins and recorded at time-step t.  $H_{\text{max}}^t$  and  $H_{\min}^{t}$  are the maximum and minimum bin values recorded for the histogram, respectively. An example of varying bin values over a course of the truck's usage is shown in Fig. 2 where it is clear how the distribution changes as the truck ages and the performance depreciates over time. The categorical features were binary-encoded, and the scalar features were min-max normalised.

However, the number of features still needed to be reduced, because (1) a neural network would not be able to distinguish between bins belonging to separate features and (2) the total features if each bin was an input to the neural network were more than 300 causing the problem of high-dimensional input. The second problem commonly known as the curse of dimensionality leading to overfitting is explained extensively in [36].

To address the above challenges and compress the information contained in the histogram, the overlap between the consecutive histograms was evaluated in the next step. The overlap, which is formally called the relative entropy of the two distributions, served as a measure for deviation in the truck's condition compared to the previous snapshot and therefore also the drop in its performance.

The overlap was evaluated by adding the minimum among the corresponding bin values of the subsequent normalised histograms. Mathematically, this was evaluated as  $\sum_{i=1}^{N} \min(A_i^{t-1}, A_i^t)$  where A is the histogram feature containing N bins, i is the bin index, and t is the indicator of the timestamp. Similar overlap difference was also evaluated with the very first histogram (representing the truck's healthiest state) and added as another column of input.

After the above step, every histogram was reduced to only two features, i.e. the overlaps evaluated with the antecedent histogram and the first histogram representing the truck's healthiest state. Total features reduced to 1/30 th of the original count, and the design matrix was a 3-D matrix of the shape (fleet size × Features × Max RUL) where Max RUL was the maximum trajectory length (= number of snapshots) among the trucks that failed in the study. The trucks with a trajectory shorter than max RUL were masked with an arbitrary and constant value to complete the matrix. The masked values were ignored while training the model. This is the input format required by the Keras RNN library, more information about which can be found in [19].

#### 3 WTTE-RNN algorithm

A brief description of the WTTE-RNN algorithm used here for prognosis is provided in this section. The WTTE-RNN algorithm combines techniques from survival analysis and recurrent neural networks. A bespoke log-likelihood loss function is used to train a recurrent neural network to provide the two parameters of a Weibull probability distribution of the time to event, given a vector of asset health data. The reader is referred to [27] for the comprehensive details. The application of WTTE-RNN is the same as in [29], but with a differently processed condition data from an industrial fleet of trucks.

The proposed log-likelihood function to be maximised by the recurrent neural network is:

$$\log(L) = \sum_{n=1}^{N} \sum_{t=0}^{T_n} \left[ u_t^n \log[Pr(Y_t^n = y_t^n | x_{0:t}^n)] + (1 - u_t^n) \log[Pr(Y_t^n > y_t^n | x_{0:t}^n)] \right]$$
(1)

where  $u_t^n$  indicates whether the observation at time t is censored (we have not yet observed the real failure time,  $u_t^n = 0$ ). The first probability to appear is  $u_t^n \log[Pr(Y_t^n = y_t^n|x_{0:t}^n)]$ , which means in case that we have observed the real time to failure  $(u_t^n = 1$ , uncensored), maximise the probability of our predicted time to failure  $Y_t^n$  being equal to the real time to failure  $y_t^n$  given the known values of the time-series of preprocessed histograms before

![](_page_4_Picture_15.jpeg)

<span id="page-5-0"></span>![](_page_5_Figure_2.jpeg)

Fig. 2 Flowchart describing the steps followed while processing the Scania dataset for the case study

Table 2 Description of the histogram, categorical, and scalar features selected for turbocharger prognosis

|             | Number of features | Examples                                                         |  |
|-------------|--------------------|------------------------------------------------------------------|--|
| Histogram   | 14                 | Ambient temperature and pressure, axle loads, boost air pressure |  |
| Categorical | 6                  | Cab type, engine type                                            |  |
| Scalar      | 3                  | Turbocharger uptime, turbocharger load                           |  |

![](_page_5_Picture_6.jpeg)

<span id="page-6-0"></span>time t,  $x_{0:t}^n$ . The second term,  $(1 - u_t^n)\log[Pr(Y_t^n > y_t^n|x_{0:t}^n)]$  means: if we have not yet observed the real time to failure  $(u_t^n = 0$ , censored), maximise instead the probability of the predicted time to failure  $Y_t^n$  being bigger than time left until the time at which we know that there has been no failure yet  $(y_t^n)$ .  $\sum_{n=1}^N \sum_{t=0}^{T_n}$  account for the summation over all the recorded failure trajectories (N) and over all the timesteps of each trajectory  $(T_n)$ . The probabilities appearing in (1) can be obtained by the means of survival analysis, in essence for the discrete case it translates to:

$$\log(L) = u * \log(e^{d(t)} - 1) - \Lambda(t+1)$$
(2)

where  $\Lambda(t)$  is known as the cumulative hazard function and  $d(t) = \Lambda(t+1) - \Lambda(t)$  is the step cumulative hazard function.

If one assumes that the failure probability follows a Weibull distribution, the discrete log-likelihood (added over all trajectories and all time-steps) can be shown to be:

$$\log(L_{d}) = \sum_{n=1}^{N} \sum_{t=0}^{T_{n}} (u_{t}^{n} \log[exp[(\frac{y_{t}^{n}+1}{\alpha_{t}^{n}})^{\beta_{t}^{n}} - (\frac{y_{t}^{n}}{\alpha_{t}^{n}})^{\beta_{t}^{n}}] - 1] - (\frac{y_{t}^{n}+1}{\alpha_{t}^{n}})^{\beta_{t}^{n}}$$
(3)

where  $\alpha_t^n$ ,  $\beta_t^n$  are the parameters of the Weibull distribution. The unconstrained optimisation problem to be solved by the recurrent neural network can be then summarised in finding the weights w that maximise  $\log(L_d)$ .

In summary, the outputs after the RNN optimises the loss function in (3) are the  $\alpha$  and  $\beta$  values for the Weibull distribution describing the truck's failure density distribution into the future.

This distribution is parameterised as  $f(t) = \frac{\beta}{\alpha} \left(\frac{t}{\alpha}\right)^{\beta-1} exp\left[-\left(\frac{t}{\alpha}\right)^{\beta}\right]$  where f(t) is the probability of failure at time t. For the results presented here, the mode of this distribution was used as the time to failure for a given truck. Once a new snapshot of histograms was obtained, the distribution was re-evaluated.

An example of prediction is shown in Fig. 3 where the data used for test prediction for a single truck is indicated, along with the predicted distribution of failure probability. Fig. 4 shows the true and predicted times to failures for a single truck throughout its lifetime.

#### 4 Experimental cases

The experiments in the case study were aimed at evaluating the efficacy of the WTTE-RNN algorithm for training the prediction model with datasets without censored data and a mix of uncensored and censored data.

![](_page_6_Figure_13.jpeg)

**Fig. 3** Example showing the predicted failure probability distribution, where mode corresponds to the predicted time to failure

![](_page_6_Figure_15.jpeg)

**Fig. 4** True and predicted times to failures for a single truck randomly chosen from testing dataset, where the *x*-axis indicates the truck's trajectory of data recorded since its healthiest state

The experiments with uncensored data further involved exploring the effects of clustering the trucks based on their technical similarities. Such clustering of assets comes off as an intuitively systematic method to train a prognosis model and is also supported in the literature on several instances. Researchers have shown improved prognosis performance with both static and dynamic clustering of the assets, especially for collaborative or transfer learning applications [6, 25, 29–31]. It is reasoned that clustering the assets based on their operational similarities makes the training dataset homogeneous, thus improving the prediction performance. However, clustering also reduces the size of the training dataset. A training dataset with fewer trucks leads to overfitting especially when using a model with several free parameters such as RNN. The trade-off between having a statistically homogeneous dataset vs. a larger training dataset is demonstrated here, for the uneven distribution of trucks comprising the clusters.

Figure 5a presents the distribution of trucks that encountered a turbocharger failure (these are the trucks

![](_page_6_Picture_19.jpeg)

<span id="page-7-0"></span>![](_page_7_Figure_2.jpeg)

![](_page_7_Figure_3.jpeg)

Fig. 5 Bar graphs showing the distributions of failed and non-failed trucks across clusters

comprising the uncensored training dataset) across the clusters. The x-axes in Fig. 5 denote the combinations of technical specifications present in the fleet, where each letter denotes a specific type of specification. Overall, five clusters were present in the fleet, and proportion of trucks in the fleet present in each cluster are shown along the yaxis. A similar distribution of the trucks that did not encounter a turbocharger failure (these are the trucks comprising the censored training dataset) is shown in Fig. 5b. The axes in Fig. 5a and b are not numbered to protect the details of the industrial dataset used for this case study.

![](_page_7_Picture_6.jpeg)

In the first case, data from the trucks that encountered a turbocharger failure during the study were only used for the analysis. The training dataset was divided into clusters of trucks containing same specifications. Following which, the prediction performance of WTTE-RNN was compared for the cases where it was trained using individual cluster data only (cluster specific model), versus when trained using overall fleet data (general model). The comparison was made based on testing datasets from the corresponding individual clusters.

Data from every cluster were split in 70–30 ratio for training and testing purposes. The cluster-specific models were trained using data from corresponding clusters only, and the training data from all clusters were accumulated to train the general model. It was ensured that the testing datasets were consistent while comparing the clusterspecific and general models. Figure [6](#page-8-0) schematically describes the training and testing datasets corresponding to each test case.

The same testing datasets were also used for evaluating the performance of the case where a mixture of censored and uncensored data were used for training. This is explained in the following section.

## 4.2 Case 2: a mix of censored and uncensored data used for training

The goal of this experiment case was to analyse the effect of using censored data in addition to the uncensored data on the prognosis performance. A mixture of censored and uncensored training datasets were therefore used for training the algorithm. The data from the trucks that did not fail were used, in addition to the training data used in the first case. Only cluster-specific models were compared in this case.

## 5 Experimental results

This section presents and discusses the results obtained from the experimental cases explained in Sect. [4](#page-6-0).

## 5.1 Performance evaluation

Concisely evaluating and presenting the performance across the testing dataset was challenging due to the uneven sampling/ time gaps between the subsequent snapshots of data across the trucks (and also for a single truck). To address this issue, the shortest trajectory in the

![](_page_7_Picture_16.jpeg)

<span id="page-8-0"></span>Fig. 6 Schematic description of the training and testing datasets used for the experiments with uncensored training data only

![](_page_8_Figure_3.jpeg)

testing dataset was divided into ten equal time-segments. The average difference between true and predicted time at every snapshot within the segments was evaluated, and the values across the testing dataset were plotted as boxes.

This process of segmenting and evaluating the performance is shown in Fig. 7. Using the shortest trajectory ensured that the number of trucks within each time segment were constant, and the company experts approved that the time was more than sufficient for planning the maintenance activities.

## 5.2 Results and discussion

This section presents and discusses the results obtained from the experiments, and using the evaluation measure described above.

The results obtained from the uncensored training dataset experiments are shown in Fig. [8,](#page-9-0) with the corresponding clusters mentioned in the captions.

1. The box plots represented by Clusters: 'Y' show the performances of the cluster-specific models, and the general model performance is indicated by Clusters: 'N'. Different time segments since the 120 th time-step till failure are shown along the x-axes, where the average true - predicted errors were calculated for each truck in the testing dataset. A segment was 12 timesteps long. Y-axes of the plots represents the calculated errors in the same time units.

2. It is observed in Fig. [8](#page-9-0) that the interquartile ranges of the errors of cluster-specific models shown in subfigure a, b, and c lie within the range of ± 25 time-steps. The company experts believe this provides them with sufficient time to plan the maintenance measures and mitigate the imminent failures.

- 3. The plots in Fig. [8a](#page-9-0), b, and c also advocate the reason behind clustering that it systematically homogenises the training dataset. This benefit is observed as the mean and variance of the evaluated errors are near zero and much lesser compared to the general models, respectively.
- 4. Nevertheless, clustering is not visibly advantageous in the plots of subfigures d and e. This difference in the benefit from clustering is attributed to lesser training dataset for the latter clusters. The trucks in the latter two clusters are nearly one-third of the trucks comprising either of the former three clusters. However, the cluster-specific model performs similar to the general model in terms of error medians and variances.
- 5. Moreover, the errors (of the cluster-specific models) are initially negative, but trend towards being positive as the trucks approach the point of failure. This means that WTTE-RNN under-predicts the failures, thus providing the maintenance managers with a conservative estimate-further reducing the adversity of the failure even when the predictions are not as accurate.

Fig. 7 Schematic representation of segmenting the time series into equal-time segments to evaluate algorithm performance

![](_page_8_Figure_15.jpeg)

![](_page_8_Picture_16.jpeg)

<span id="page-9-0"></span>![](_page_9_Figure_2.jpeg)

Fig. 8 Comparison of cluster-specific and general model for uncensored training data case, the clusters mentioned in sub-captions

Similar plots presenting the results from the experiments containing a mixture of uncensored and censored training data are shown in Fig. [9.](#page-10-0) But unlike Fig. 8, the performances of only cluster-specific models are presented here. This is because it is concluded from Fig. 8, discussed in the above points, that the cluster-specific model performs better than the general model. The corresponding cases are mentioned in the captions, and the performance was evaluated using the same testing dataset as in Fig. 8. The following salient features can be observed in Fig. [9](#page-10-0):

1. Here again, the interquartile error ranges and errors of the predictions in Fig. [9a](#page-10-0) and c are within actionable ranges, for the maintenance managers to plan the

![](_page_9_Picture_7.jpeg)

<span id="page-10-0"></span>![](_page_10_Figure_2.jpeg)

Fig. 9 True-predicted times to failure error shown for a mixture of uncensored and censored data

mitigation measures. The plot in Fig. 9 d is ambiguous due to the presence of little testing data compared to the training data when the censored data was included. The poor performance of the algorithm in Fig. 9b and e is due to extremely high imbalance of censored and

- uncensored training data. This is further discussed in the following points.
- 2. From Fig. 9 a and c, the performance of WTTE-RNN is observed to improve, especially in terms of reduced error variance, compared to Fig. [8](#page-9-0)a and c where only

![](_page_10_Picture_7.jpeg)

<span id="page-11-0"></span>![](_page_11_Figure_2.jpeg)

Fig. 10 Extension of the experiment corresponding to Fig. [9b](#page-10-0) and e, where the proportion of uncensored data for training was systematically decreased, as indicated in the plots

uncensored data was used for training. The error variance in the time segment just before failure is nearly halved when a combination of censored and uncensored data is used for training WTTE-RNN. This is due to the fact that the algorithm is now able to make better informed estimates of a and b Weibull parameters.

3. However, such an improvement is not observed for Fig. [9](#page-10-0)b and e due to the highly imbalanced censored and uncensored training datasets. In both cases, the censored training data is 15 times the uncensored training data. This causes over-generalisation of the Weibull loss function which is trained such that the trucks fail with a very low probability.

To highlight the reason in the last point above, an extension of this experiment was conducted where the proportion of uncensored/censored data was systematically decreased in steps of 4 : 1, 1 : 1, and 1 : 15 for the clusters shown in Fig. [9](#page-10-0) b and e. The errors for these are plotted in similar format in Fig. 10.

It is seen in Fig. 10 that the prediction performance improves (especially in the subfigure Fig. 10b until a certain proportion of the censored data and then deteriorates as the proportion of censored data is further increased.

## 6 Conclusions

This paper presents the first industrial use case of WTTE-RNN for prognosis. Since the condition data used in the case study were recorded as a time series of sparsely sampled histograms, a technique to preprocess such data is also shown.

The case study shown involves real-world turbocharger failures dataset obtained from a fleet of trucks monitored over a fixed period of time since they commenced their operations. The performance of WTTE-RNN is analysed in the experiments for cases where uncensored, and a mixture of uncensored and censored data are used for prognosis of turbocharger failures.

The following key conclusions are deduced based on the experiments discussed in this paper:

![](_page_11_Picture_12.jpeg)

- <span id="page-12-0"></span>1. The high dimensionality of histogram data can be reduced by evaluating the relative entropies (like presented here, or by using KL-divergence measures) of consecutive snapshots of data, and of the current histogram with that corresponding to the healthy asset. This substantially reduces the dimensions while retaining the information necessary for prognosis.
- 2. The above point is presented as remarkable performance of WTTE-RNN shown in Figs. [8](#page-9-0) and [9](#page-10-0) where the error variances and means lie within ranges that enable the maintenance managers to plan mitigation measures in real time.
- 3. Clustering is not necessarily beneficial for training a prognosis algorithm. This is because clustering reduces the size of the training dataset, sometimes to an extent that a model with several free parameters can overfit. This is represented in Fig. [8](#page-9-0)d and e where clustering shows no substantial benefit compared to the general fleet model.
- 4. Censored data from the assets that did not fail are often ignored by the industries. But the results in Fig. [9](#page-10-0) show that incorporating censored data while training a prognosis model can improve the predictions. This can be obtained with the Weibull loss function of the WTTE-RNN algorithm.
- 5. However, care must be taken while incorporating censored data for training because if the training dataset is highly imbalanced the algorithm performance deteriorates drastically, as shown in Fig. [10.](#page-11-0)

Data availability The data that support the findings of this study are available from Scania CV in Sweden but restrictions apply to the availability of these data, which were used under license for the current study, and so are not publicly available. Data are however available from the authors upon reasonable request and with permission of Scania CV.

## Declarations

Conflict of interest The authors declare that they have no conflict of interest.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit [http://creativecommons.](http://creativecommons.org/licenses/by/4.0/) [org/licenses/by/4.0/.](http://creativecommons.org/licenses/by/4.0/)

## References

- 1. Alutoin M (2020) Scheduling of preventive maintenance using prognostic models-a case study on elevator doors
- 2. Cawley R, Burns D (2019) Analysis of wtte-rnn variants that improve performance. Mach Learn Appl An Int J 3:35–47
- 3. C¸ elik O, Osmanoglu UO (2019) Comparing to techniques used in customer churn analysis. J Multidiscip Dev 4(1):30–38
- 4. CHAMI S, Kaabouch N, Tavakolian K Comparative study of light-gbm and a combination of survival analysis with deep learning for early detection of sepsis
- 5. Da Xu L, He W, Li S (2014) Internet of things in industries: a survey. IEEE Trans Ind Inf 10(4):2233–2243
- 6. Dhada M, Jain AK, Parlikad AK (2020) Empirical convergence analysis of federated averaging for failure prognosis. IFAC-PapersOnLine 53(3):360–365
- 7. Diday E, Noirhomme-Fraiture M (2008) Symbolic data analysis and the SODAS software. Wiley, NewYork
- 8. Eom TH, Lee H (2022) A wtte-rnn based hypoglycemic event prediction. In: 2022 International Conference on Information Networking (ICOIN), pp. 378–379. IEEE
- 9. Frisk E, Krysander M, Larsson E (2014) Data-driven lead-acid battery prognostics using random survival forests. Linkoping University, Linkoping, Sweden
- 10. Gilchrist A (2016) Industry 4.0: the industrial internet of things. Springer
- 11. Goyal D, Pabla B (2015) Condition based maintenance of machine tools?a review. CIRP J Manuf Sci Technol 10:24–35
- 12. Gurung R, Lindgren T, Bostro¨m H (2018) Learning random forest from histogram data using split specific axis rotation. Int J Mach Learn Comput 8(1):74–79
- 13. Gurung RB, Lindgren T, Bostr H et al (2017) Predicting nox sensor failure in heavy duty trucks using histogram-based random forests. Int J Progn Health Manag. 8(1)
- 14. Gurung RB, Lindgren T, Bostro¨m H (2016) Learning decision trees from histogram data using multiple subsets of bins. In: Twenty-Ninth International Florida Artificial Intelligence Research Society Conference, FLAIRS, Key Largo, Florida, May 16-18, 2016, pp. 430–435. AAAI Press
- 15. Jain A, Dhada M, Perez Hernandez ME, Herrera Fernandez A, Parlikad A (2020) Influence of imperfect prognostics on maintenance decisions
- 16. Jain AK, Dhada M, Hernandez MP, Herrera M, Parlikad AK (2021) A comprehensive framework from real-time prognostics to maintenance decisions
- 17. Jin B, Chen Y, Li D, Poolla K, Sangiovanni-Vincentelli A (2019) A one-class support vector machine calibration method for time series change point detection. In: 2019 IEEE International conference on prognostics and health management (ICPHM), pp. 1–5. IEEE
- 18. Joosse C (2020) Absence seizure prediction using recurrent neural networks
- 19. Ketkar N (2017) Introduction to keras. In: Deep learning with Python, pp. 97–111. Springer
- 20. Kim JY, Lee YS, Yu J, Park Y, Lee SK, Lee M, Lee JE, Kim SW, Nam SJ, Park YH et al (2021) Deep learning based prediction model for breast cancer (bc) recurrence using adjuvant bc cohort in tertiary cancer center registry. Front Oncol 11:655
- 21. Kwon D, Hodkiewicz MR, Fan J, Shibutani T, Pecht MG (2016) Iot-based prognostics and systems health management for industrial applications. IEEE Access 4:3659–3670
- 22. Lee J, Jin C, Liu Z, Ardakani HD (2017) Introduction to datadriven methodologies for prognostics and health management. In: Probabilistic prognostics and health management of energy systems, pp. 9–32. Springer

![](_page_12_Picture_34.jpeg)

- <span id="page-13-0"></span>23. Ma Z, Krings AW (2008) Survival analysis approach to reliability, survivability and prognostics and health management (phm). In: 2008 IEEE Aerospace Conference, pp. 1–20. IEEE
- 24. Madhusudana C, Kumar H, Narendranath S (2016) Condition monitoring of face milling tool using k-star algorithm and histogram features of vibration signal. Eng Sci Technol Int J 19(3):1543–1551
- 25. Mahmoodian A, Durali M, Abbasian Najafabadi T, Saadat M (2020) Optimized age dependent clustering algorithm for prognosis: a case study on gas turbines. Scientia Iranica
- 26. Maragall Cambra M (2018) Using recurrent neural networks to predict the time for an event
- 27. Martinsson E (2016) Wtte-rnn: Weibull time to event recurrent neural network. In: Ph.D. thesis, Chalmers University of Technology & University of Gothenburg
- 28. Neely A (2008) Exploring the financial consequences of the servitization of manufacturing. Oper Manag Res 1(2):103–118
- 29. Palau AS, Bakliwal K, Dhada MH, Pearce T, Parlikad AK (2018) Recurrent neural networks for real-time distributed collaborative prognostics. In: 2018 IEEE international conference on prognostics and health management (ICPHM), pp. 1–8. IEEE
- 30. Palau AS, Dhada MH, Bakliwal K, Parlikad AK (2019) An industrial multi agent system for real-time distributed collaborative prognostics. Eng Appl Artif Intell 85:590–606
- 31. Palau AS, Liang Z, Lu¨tgehetmann D, Parlikad AK (2019) Collaborative prognostics in social asset networks. Future Gener Comput Syst 92:987–995
- 32. Prytz R, Nowaczyk S, Ro¨gnvaldsson T, Byttner S (2015) Predicting the need for vehicle compressor repairs using

- maintenance records and logged vehicle data. Eng Appl Artif Intell 41:139–150
- 33. Ren Y (2021) Churn prediction methods evaluation and implementation for telecom industry. In: Ph.D. thesis, Applied Sciences: School of Computing Science
- 34. Schwabacher M, Goebel K (2007) A survey of artificial intelligence for prognostics. In: AAAI Fall Symposium: Artificial Intelligence for Prognostics, pp. 108–115
- 35. Siegelmann HT, Sontag ED (1995) On the computational power of neural nets. J Comput Syst Sci 50(1):132–150
- 36. Verleysen M, Franc¸ois D (2005) The curse of dimensionality in data mining and time series prediction. In: International workconference on artificial neural networks, pp. 758–770. Springer
- 37. Watson N, Janota M (1982) Turbocharging the internal combustion engine. Macmillan International Higher Education, London
- 38. Xu E, Li Y, Han Z, Du J, Yang M, GAO X, (2022) A method for predicting the remaining life of equipment based on wtte-cnnlstm. J Adv Mech Des Syst Manuf 16(1):JAMDSM0001– JAMDSM0001
- 39. Yasodhara A, Bhat M, Goldenberg A (2018) Prediction of new onset diabetes after liver transplant. arXiv preprint [arXiv:1812.](http://arxiv.org/abs/1812.00506) [00506](http://arxiv.org/abs/1812.00506)
- 40. Zhong K, Han M, Han B (2019) Data-driven based fault prognosis for industrial systems: a concise overview. IEEE/CAA J Autom Sinica 7(2):330–345

Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](_page_13_Picture_22.jpeg)
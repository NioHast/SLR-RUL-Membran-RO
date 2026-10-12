### **Article in Press**

# A two-stage framework for cost-sensitive predictive maintenance using deep learning, GANs, and risk-aware clustering

Received: 7 November 2025

Accepted: 27 February 2026

Published online: 21 March 2026

Cite this article as: Hakami A. A twostage framework for cost-sensitive predictive maintenance using deep learning, GANs, and risk-aware clustering. *Sci Rep* (2026). https://doi. org/10.1038/s41598-026-42910-4

### Ali Hakami

We are providing an unedited version of this manuscript to give early access to its findings. Before final publication, the manuscript will undergo further editing. Please note there may be errors present which affect the content, and all legal disclaimers apply.

If this paper is publishing under a Transparent Peer Review model then Peer //doi.
Review reports will publish with the final article.
-4

© The Author(s) 2026. **Open Access** This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit <a href="https://creativecommons.org/licenses/by/4.0/">https://creativecommons.org/licenses/by/4.0/</a>.

# A Two-Stage Framework for Cost-Sensitive Predictive Maintenance Using Deep Learning, GANs, and Risk-Aware Clustering

Ali Hakami<sup>1\*</sup>

<sup>1\*</sup>Mechanical and Industrial Department, College of Engineering and Computing in Al-Gunfudha, Umm Al-Qura University, 21961 Mecca, Saudi Arabia.

\*Corresponding: amahakami@uqu.edu.sa

### **Abstract**

Predictive maintenance (PdM) has seen significant advances through machine learning, yet its practical deployment remains challenged by data scarcity, system complexity, and uncertainty in cost-related decisions. The majority of current PdM strategies are concerned with enhancing Remaining Useful Life Prediction accuracy of (RUL) in isolation and with maintenance scheduling as a problem (secondary or fixed). This study proposes a component based, decision oriented predictive maintenance (PdM) approach that links Remaining Useful Life (RUL) to optimization of maintenance.

The two-stage framework proposed anticipates the component-specific RUL prediction where Long Short-Term Memory (LSTM) models was used to predict the Remaining Useful Life (RUL) of individual components. To address sparsity in failure data, Wasserstein Generative Adversarial Networks Gradient Penalty (WGAN-GP) were utilised to fill in run-to-failure sequences, stabilizing downstream modeling. In the second step, similar components in terms of Remaining Useful Life (RUL) degradation are clustered together by Density-Based Clustering Space (DBSCAN), which allows opportunistic maintenance. A decision on maintenance is then optimized cost-conscious grid search which works on fitted RUL distributions and a normalized. Not only based on point RUL estimates, but on a risk proxy.

Empirical experimentation across multiple industrial components of a water bottling plant system indicates that the proposed approach continually reduces corrective failures and normalized maintenance costs as opposed to non-clustering approaches such as random choice and fixed choice of maintenance point. Sensitivity analysis also indicates that the optimal maintenance levels be consistent over a vast spectrum of cost assumptions, which emphasizes the resilience of the structure in economic

uncertainty.

Overall, this study contributes a robust and scalable maintenance literature that combines data augmentation, component based clustering, and risk aware optimization. This helps advance predictive maintenance practices into a more practical, cost aware decisions.

**Keywords:** Predictive Maintenance (PdM), WGAN-GP, Maintenance Scheduling, Clustering, Data Scarcity, GAN-based Data Augmentation, Maintenance Optimization

![](_page_2_Picture_4.jpeg)

### Introduction

Industrial maintenance is an important practice in ensuring reliability and efficiency in production systems, especially in high throughput production systems like water bottling plants [1]. This is because it focuses on reducing unplanned failures that cause severe financial losses, through unanticipated production downtimes, costly repairs, and disruptions in the supply chain [2]. With the advent of Artificial intelligence (AI) such failures can be monitored and avoided This allows industrial systems to remain running in their most productive state thus increasing system throughput and consequently the overall profitability [3].

Industrial maintenance strategies can be categorized as reactive (run-to-failure), time-based, and condition-based [4]. Reactive maintenance is costly due to unexpected breakdowns [5], preventive maintenance on the other hand can necessitate unnecessary servicing and added expenses [3]. Predictive maintenance involving the use of advanced technologies such as machine learning (ML) and other data driven techniques, has gained popularity and can help optimize maintenance schedules while minimizing maintenance costs [6–8].

Predictive maintenance (PdM) incorporates failure prognostics that estimate degradation or Remaining Useful Life (RUL) of industrial components [9]. RUL prediction models use historical failure dataset to determine when a specific machine is most likely to fail, which enable maintenance teams to intervene prior to failure [10]. The advancement in technology and incorporation of artificial intelligence has sparked growing interest in many fields, including PdM [11].

### Data scarcity as a challenge to PdM

Past research have also shown that new components or systems for instance, in predictive maintenance using machine learning, may have little to no historical data available [12]. The next available set data may be unrepresentative of the normal operation, with limited failure instances. [13]. This leads to poor model generalization and poor ability to predict failure [14].

To overcome this problem, several approaches, including data augmentation, trans- fer learning, and physics-informed models, have been proposed. Data augmentation methods such as bootstrapping and SMOTE (Synthetic Minority Over-sampling Tech- nique) have been employed to artificially increase failure samples [15, 16] while transfer learning has helped models learn from related domains where there maybe abundant failure data [17].

One augmentation strategy that has received much attention in recent years is Generative Adversarial Networks (GANs). GANs model features a generator model, and a discriminator model, the two work in a competitive way, where the generator generates fake failure trajectories, and the discriminator learns to differentiate between the real data and fake data. In this context, GANs mimic failure regions and produce synthetic data with inherent characteristics of real failure patterns [12]. Recent studies have demonstrated that data augmentation utilizing Generative Adversarial

Network can enhance the resilience of ML models in industrial settings.

For instance[18] proposed a novel approach, called Scarcity-GAN, to data limitations. Their model used external datasets of defect features and an encoder-decoder network. The comparison of the proposed augmentation methods with other existing augmentation methods for industrial datasets pointed to higher accuracy.

[19] presented an approach which employed Conditional Wasserstein GANs (CWGANs) to generate syn- thetic spectral data. The study also revealed that conditioning WGANs for proper labeling and avoiding mode collapse helped to enhance the performance of the model. The CWGAN also showed that the use of images and augmentation of Mel-Frequency Cepstral Coefficients (MFCCs) enhanced a feed-forward neural network for classification, thereby highlighting the general applicability of GANs for more than image generation tasks.

Vilela-perez [20] presented the EffBaGAN architecture, a GAN-based augmentation model designed to mitigate the issues of data scarcity and class imbalance in RS. This paper proposes an EfficientNet-based discriminator and generator developed on BAGAN to help improve the computational efficiency of the model. When tested on multispectral vegetation images, EffBaGAN has increased in efficiency both in training and testing compared to vision transformers and Residual BAGAN, making it significantly accurate for data sets with limited data samples. Hakami[12] addressed data scarcity in predictive maintenance (PdM) by leveraging GANs to generate synthetic run-to-failure data, improving ML model training. Their findings highlighted the importance of GANs in data augmentation in PdM. Many other researchers, including [21-24] and [25], have successfully applied GANs for data augmentation in various fields, such as disease diagnosis, pharmacogenetics, Synthetic Tabular Data Generation (STDG) and solid rocket motors (SRMs) remote sensing. However, the challenge is not only the limited use of data augmentation techniques, but the absence of frameworks that explicitly link augmented data to robust maintenance decision-making. Existing PdM studies that employ GANs or other augmentation methods primarily focus on improving Remaining Useful Life (RUL) prediction accuracy, often treating prediction as an isolated objective. As a result, little attention is given to how augmented data influences downstream tasks such as component grouping, maintenance coordination, and cost-aware scheduling under uncertainty.

In this work, component-specific GANs are used not merely to increase data volume, but to stabilize RUL distributions in the presence of severe failure sparsity. This enables reliable clustering of components with similar degradation states and supports risk-aware optimization of maintenance thresholds. By integrating data augmentation with decision-oriented clustering and scheduling, the proposed framework moves beyond prediction-centric PdM toward a coordinated, component-level maintenance strategy.

### Clustering maintenance practices

The primary goal of maintenance strategies is to minimize unnecessary interventions which add on to the costs while at the same time avoid failure-related costs that arise from downtime [26]. Over-maintenance leads to performing unnecessary repair and replacement of parts, expenses in labor, and inactivity time, while under- maintenance leads to system failures, reduction in system throughput, and high downtime expenses [27]. In response, several clustering techniques have been employed in various maintenance settings for decision-making enhancement. The purpose of clustering is to categorize the components or the maintenance tasks for a particular system based on the degradation pattern, operational condition or failure risk and hence flexibility in the scheduling and resource allocation [28]. In certain industries, clustering has been applied to similar but related idea covered under condition-based maintenance, where assets are grouped according to wear patterns to improve modeling. For instance, [29] proposed the genetic algorithm for clustering in maintenance scheduling related to healthcare facilities with improved asset performance and high operational availability.

Additionally, [30] pointed that clustering maintenance actions in manufacturing systems which failure modes take into consideration three and move toward the perfect maintenance action centralized type influence was seen to lower cost in relation to the frequent rate of failure as well as a time optimization. They also stress on the utility of using clustering to reduce on the maintenance costs and production loss as high- lighted by [31] where the authors write on the identification of phases in algorithms of TVIPs specifically when using clustering to monitor production assets whenever fault annotated databases for supervised learning models are scarce. Their work utilised a new method called Latent Dirichlet Allocation for clustering of applications in maintenance. [32] further elaborate on early-stage maintenance clustering and its effectiveness on maintenance planning. The literature analysis together with the case studies used in the study showed that gains made through clustering in identification phase were

4.6 per cent of the planned work hours while the gains made in the planning phase were 2.7 per cent and 2.4 per cent in the scheduling phase. Especially, the findings highlight the positive aspects of early clustering in terms of eradicating wasteful work, while calling for further study on the issue. Yet, clustering has not been a subject of extensive research in PdM. Most of the works use a global approach, where the goal is to train models to predict failure probability or Remaining Useful Life (RUL) for the overall system. This perspective fails to consider that there are different RULs associated with different components. In addition, some parts might be maintained more often than required, while others may not be maintained when they should be, and this leads to ineffectiveness. For example [33] focused on the significance of each individual RUL estimations in multi-component systems to minimize the costs of equipment upkeep. Likewise, analysing the case of turbofan engines, [34] showed that incorporating probabilistic RUL prognostics in maintenance planning enhances the capacity to curb costs compared to non-probabilistic time-based policies. Also, studies have focused on the issues with the system-level prognosis and stressed the importance of considering the

state of the each component as well as their interaction with one another to improve the accuracy and efficacy of predictions [35]. From these considerations, this work introduces a localized maintenance scheduling strategy where components are grouped according to their RULs. Hence, putting similar components with similar failure profiles in a group will ensure that maintenance effort is focused on specific components, leading to reduced overall cost through minimizing time lost and efficient utilization of resources.

Beyond improving prediction accuracy, an important objective of predictive maintenance is to enable coordinated and cost-efficient maintenance actions across system components. In practice, maintaining components independently based solely on individual RUL estimates can lead to redundant interventions, unnecessary downtime, or missed opportunities for joint servicing. By explicitly grouping components with similar degradation states using RUL-based clustering, the proposed framework enables opportunistic maintenance, whereby components that are likely to require service within a similar horizon can be maintained together. This approach contrasts with existing PdM strategies that either assume homogeneous component behavior or apply global maintenance thresholds without coordination. As a result, the proposed clustering-based strategy supports more flexible, interpretable, and economically efficient maintenance planning at the component level.

### **Experimental Methods**

### **Data Collection and Augmentation**

This research aims at analysing run-to-failure data obtained at one-hour time intervals from a water bottling plant with 16 components. The system was observed for a total of 3,319 operating hours; data collected includes throughput, defined as gross and net number of bottles produced, failure time and type if any, line speed, bottle size, and machine/component code. These recordings were carried out by the production engineers at the different machine stations on the production line. In an effort to ensure that the system components are not overtly named or de-identified, the component names were coded as M1,M2,...,M16.

Prior to model training, the raw maintenance logs were processed to obtain consistent machine-level time series at an hourly resolution. Planned maintenance activities (e.g., CIP changeovers) were excluded, as these operations are deterministic and do not reflect stochastic degradation behavior. Since failures were recorded for different machines independently, the data were processed separately for each machine, with system-level events involving multiple machines included in the data of each affected component.

For each machine, hourly records were segmented into run-to-failure sequences, where a run is defined as the period between two consecutive

failure events. Run lengths are therefore variable and non-deterministic, reflecting the stochastic nature of component degradation, as summarized in Table 1. For simplicity, it was assumed that every time a component (machine) failed, it was fully restored, hence failures on the previous runs does not affect operations on the next run. This defines the independence between the runs.

A set of degradation-relevant features was selected, including failure duration, line speed, product SKU (bottle volume), age at repair (approximated by the midpoint for ranged values), and a derived throughput deficit feature computed as the difference between gross and net production. All features were normalized using min-max scaling on a per-machine basis to ensure comparability and to prevent information leakage across components.

| Machine<br>Component | Total<br>Runs | Min Run<br>(hrs) | Max Run<br>(hrs) | Mean Run<br>(hrs) | Median<br>Run (hrs) |
|----------------------|---------------|------------------|------------------|-------------------|---------------------|
| MO                   | 594           | 1                | 427              | 5.49              | 1                   |
| M1                   | 612           | 1                | 130              | 5.33              | 3                   |
| M2                   | 223           | 1                | 222              | 14.62             | 2                   |
| M3                   | 161           | 1                | 202              | 20.25             | 5                   |
| M4                   | 104           | 1                | 340              | 31.35             | 2                   |
| M5                   | 29            | 1                | 642              | 112.41            | 7                   |
| M6                   | 19            | 1                | 541              | 171.58            | 99                  |
| M7                   | 27            | 1                | 936              | 120.74            | 7                   |
| M8                   | 18            | 2                | 657              | 181.11            | 116                 |
| M9                   | 3             | 549              | 1589             | 1086.67           | 1122                |
| M10                  | 2             | 1106             | 2154             | 1630.00           | 1630                |
| M11                  | 2             | 1237             | 2023             | 1630.00           | 1630                |
| M12                  | 2             | 843              | 2417             | 1630.00           | 1630                |
| M13                  | 2             | 714              | 2546             | 1630.00           | 1630                |
| M15                  | 2             | 552              | 2708             | 1630.00           | 1630                |
| M15                  | 2             | 193              | 3067             | 1630.00           | 1630                |

**Table 1.** Run statistics for machine components

A common problem in PdM datasets is data sparsity, especially where failures are rare in some components. For example, components M9 to M15 had at most 3 runs, ability of learning-based models to capture degradation patterns. To get around this issue, data augmentation was performed using a Wasserstein Generative Adversarial Network with Gradient Penalty (WGAN-GP) trained separately for each machine with sufficient failure history. The WGAN-GP learns the distribution of machine-specific run-to-failure sequences and generates additional synthetic runs with similar temporal and statistical characteristic. The WGAN-GP learns the distribution of machine-specific run-to-failure sequences and generates additional synthetic runs with similar temporal and statistical characteristics. The Lipschitz constraint was

enforced using a gradient penalty term with coefficient  $\[ \] = 10$  and the critic was updated five times for each generator update to ensure stable training. Due to the variable and potentially long sequence lengths, a batch size of one was used during training to manage computational cost. Models were trained for up to 100 epochs with early stopping (patience = 5) based on convergence of the Wasserstein objective. To control the extent of augmentation, a fixed ratio  $\[ \] = 15$  was used, meaning that for each observed run-to-failure sequence, 15 synthetic sequences were generated. The synthetic and real sequences were then combined to form augmented training sets, improving robustness while preserving machine-specific degradation behavior. Figure 1 visualizes the GAN workflow.

![](_page_8_Figure_2.jpeg)

Figure 1. The structure of GANs model

### Remaining Useful Life (RUL) Prediction Model

To estimate the RUL of each component, the Long Short-Term Memory (LSTM), a recurrent neural network specialized for sequential, was utilized. In this context it was intended to capture temporal dependencies and failure deceleration patterns by using historical failure sequences. The models operate on variable-length run-to-failure sequences. Each model(one per machine) operate on variable-length run-to-failure sequences and accepts multivariate time-series inputs and applies a masking layer to handle padded time steps arising from variable-length sequences. The masked inputs are processed through one or more stacked LSTM layers, all configured to return full sequences, followed by a linear dense output layer that predicts RUL at each time step.

Due to heterogeneity in degradation behavior and data availability across components, RUL models were trained independently for each machine using a common architectural template with per-machine hyperparameter

tuning. The tuning process explored architectures with one to three LSTM layers and 64 to 256 units per layer, as well as learning rates between  $10^{-3}$  and  $10^{-4}$ . For each machine, a limited random search of 5 trials each of 20 epochs was conducted to select the best-performing configuration based on validation loss. Model training was performed for up to 100 epochs using the Adam optimizer, with early stopping applied (patience = 10) to mitigate overfitting. A custom loss function was used, combining custom mean squared error with monotonicity and trend penalty terms to enforce physically consistent, non-increasing RUL trajectories over time while respecting padded regions of the sequences. Validation loss was monitored throughout training to guide model selection and convergence.

### **Probability Estimation of Failure**

To quantify degradation and failure risk for each component, parametric probability distributions were fitted to the predicted Remaining Useful Life (RUL) values obtained from the LSTM models. The candidate distributions were restricted to forms commonly used to model lifetime and degradation behavior (Weibull, exponential, gamma, lognormal, inverse Gaussian, Gompertz, and fatigue-life), and the best-fitting distribution for each component was selected based on goodness-of-fit criteria.

Most importantly fitting distributions to predicted RUL values does not directly yield failure-time probabilities. Instead, the fitted distribution characterizes the empirical distribution of RUL magnitudes, where larger values indicate healthier operation and values approaching zero indicate proximity to failure. To account for this, a normalized CDF-based survival index was defined as a proxy for relative health and failure risk.

Let  $f_i(t)$  denote the probability density function (PDF) of the fitted RUL distribution for component iii, and

Let 
$$F_{Ri}(t_k) = \int_0^{t_k} f_i(t) dt$$

be the corresponding cumulative distribution function (CDF). Since failure corresponds to RUL=0, the probability mass at or below the failure boundary is given by  $F_{Ri}$  (0). The proposed survival index at horizon  $t_k$  is defined as:

$$SI_{i}(t_{k}) = \frac{F_{Ri}(t_{k}) - F_{Ri}(0)}{1 - F_{Ri}(0)}$$
(2)

which represents the normalized probability mass between the failure boundary and the predicted RUL value. This index increases monotonically as the predicted RUL moves farther from zero and is bounded in the interval [0,1].

A corresponding relative failure risk proxy is then defined as

$$Risk_{i}(t_{k}) = 1 - SI_{i}(t_{k})$$
(3)

This representation gives a numerically stable distribution-sensitive measure of distance to failure, without a real failure-time representation. The resulting risk proxy is then adopted to aid clustering and cost-conscious maintenance decision-making to facilitate planning, which takes into account relative degradation severity, but not the point estimates of RUL individually.

### **Maintenance Scheduling Strategy**

In order to reduce the cost of maintenance and enhance efficiency, we will implement a two-stage, component-based maintenance schedule approach based on distributions of the RUL (Remaining Useful Life) that is predicted.

### Stage 1: Clustering Based on RUL Proximity

We initially cluster components with statistically similar degradation pattern (RUL predictions) instead of using a global predictive maintenance (PdM) rule to all components. It is used to cluster together components whose remaining lifetimes are similar [33], and not have to waste time servicing components that are in dissimilar health conditions[30].

Let  $C_1$ ,  $C_2$ ...  $C_k$  be the resulting clusters from a similarity-based grouping of components based on predicted RULs  $R\hat{U}L$ , where each component  $i \in C_k$ . We define a proximity threshold parameter  $\delta$ , which determines the distance between RULs for components to belong to the same cluster:

$$|R\hat{U}L_i - R\hat{U}L_j| \le \delta, \ \forall i, j \in C_k$$
(3)

This threshold  $\delta$  is an important optimization variable, it determines the number of granules in a clustering and consequently, it influences the scheduling and costs obtained. Our implementation availed Density-Based Spatial Clustering of Applications with Noise (DBSCAN), in which the number of clusters is not specified, which automatically identifies noise and outlier elements that are unsuitable to maintenance coordination, and cluster formation on the basis of RUL space proximity. According to this formulation, the threshold d is equal to the e parameter and it determines the maximum distance that can exist between the elements of the same cluster.

### Stage 2: Optimal Maintenance Timing via Grid Search

After creating clusters, we calculate the maintenance RUL threshold  $t_k$  per cluster  $C_k$  to be minimum of the expected cost of servicing.

### **Cost Components**

The total expenditure incurred in maintaining a cluster  $C_k$  at RUL

Treventive Maintenance Cost Cp: Cost incurred when a component is serviced before reaching the failure boundary.
 Corrective (Failure) Maintenance Cost Cf: Higher cost associated with unplanned repairs and interventions related to failure.
 Downtime Cost Cd: Cost related to lost production output due to component failure or maintenance downtime.
 Let r(tk) be the RUL-based failure risk proxy for component i∈ Ck evaluated at the maintenance RUL tk, the expected maintenance cost for the cluster is computed using this risk proxy to weight corrective and downtime costs.

$$Cost(C_k, t_k) = [r_i(t_k) \cdot (c_f + c_d) + (1 - r_i(t_k)) \cdot C_p](4)$$

$$i \in C_k$$

The objective is:

to:

- $||R\hat{U}L_i R\hat{U}L_i| \leq \delta, \forall i, j \in C_k$
- $| r_i(t_k) | \ge \theta$ , where | is a predefined risk threshold triggering maintenance.
- $\sqcap t_k \leq min_{i \in C_k} RU^{\hat{i}} L_i$  to prevent maintenance beyond the earliest predicted

failure within the cluster

Throughout our maintenance scheduling approach, we adopted a grid search to establish the best threshold  $t_k$  of every cluster of components with similar Remaining Useful Life (RUL) distributions. This was due to the nature of the anticipated cost function which is usually a piecewise constant then monotonic function. RUL-based failure risk proxy on small values of tk.

probability of failure  $r_i(t_k)$  is almost zero, which leads to a flat cost region, in which the overall cost is about the same as the cost of preventive maintenance. As  $t_k$  gets closer to the critical region of the RUL distribution,  $r_i(t_k)$  starts to increase at a high rate which results in the cost suddenly soaring because of the danger of failure and the resultant downtime. Due to this phenomenon, the classical optimization tools such as the gradient descent cannot be used- they can become trapped in the flat areas or cannot recognize the steep cost rise.

Instead, grid search methodically considers a finite set of candidate  $t_k$  values in the range of observed UR, with which we can determine the best maintenance threshold without utilizing gradients. When there is a set of candidate  $t_k$  values which produce the same minimal cost we select the largest one and delay maintenance as long as we can without exposing ourselves to higher risk. We also have restrictions to prevent premature and late maintenance, i.e.  $t_k$  should not be greater than the earliest noted RUL within the cluster and the probability of failure should be less than a given cut-off.

### Stage 3: Scheduling Maintenance Time per Cluster

Then, for every cluster  $C_k$ , the optimal maintenance RUL threshold  $t_k$  is chosen such that it decreases the overall expected cost of maintaining all the components of the cluster to the least. This threshold is not fixed a priori but an optimized based on different factors. This represents the RUL between the potential for performing early, possibly unnecessary preventive maintenance and when the gear could fail with subsequent downtime. The chosen threshold  $t_k$  makes it possible to estimate the total risk of failure of components in the cluster until a given time point, thereby successfully moderating the identified risks. This means that after calculating candidate maintenance thresholds for all units in a feasible range (from the current time to the maximum RUL within the cluster), the model identifies the point that leads to the minimum total cost of preventive and failure cost for the entire cluster. It enables systematic planning and efficient execution of maintenance so as to reflect the state of degradation of parts involved in the system. Figure 2 below illustrated the conceptual framework of this proposed methodology.

![](_page_12_Figure_3.jpeg)

<span id="page-12-0"></span>**Figure 2.** The Conceptual framework

### Results

### Synthetic Data Generation Using GANs

Since failure sequences are grossly scarce for each of the components, WGAN-GP was trained separately on each of the machine component dataset for up to 100 epochs with a batch size of 1. To overcome cases of overfitting and improve training rate, early stopping was applied based on Wasserstein critic distance, with 10 epochs of patience to allow model training to stop as soon as the performance stagnates. Training history curves for Machines 1, 2, and 3 are shown in Appendix A, Figures A1–A3. Illustrating the typical convergence behavior observed across most of the models, where the generator and critic loss shows a rapid initial

increase/decrease followed by slower progression as training advance. This slowdown indicates that the critic became learned to distinguish between real and synthetic data, while the generator simultaneously learned to generalize and come up with new sequences having statistical properties similar to the real data. The complete set of training plots for all 16 machines is provided in Supplementary file S1.

Moreover, each feature on the generated data were compared with their corre-sponding feature on the real data using kernel density estimate graphs(KDE). The comparisons show exactly superimposable distributions of the features in the real and synthetic data, Appendix B, figures B1-B3 show these comparisons for Machine 0-3. The complete set for all the 16 machines is presented supplementary file S1. PCA plots were also used to visualize similarity between the synthetic and the real data in a lower dimension. Appendix C shows these comparisons for the first 3 machines.

Kolmogorov-Smirnov (K-S) tests were conducted to evaluate the goodness of fit between real and generated feature distributions for each machine component. While the K-S tests were statistically significant for all components, this does not imply poor synthetic data quality. Such tests are highly sensitive-especially in the tails and large samples—and may not reflect practical or perceived similarity. Therefore, they should be complemented with visual and model-based evaluations, which in this case support the utility of the generated data. Table 2 below reports the K-S test results for real vs. synthetic data across different machines and features.

| Machine | Feature      | K-S       | p-         |
|---------|--------------|-----------|------------|
|         |              | Statistic | value      |
| МО      | Feature<br>0 | 0.9473    | <0.00<br>1 |
|         | Feature<br>1 | 0.7622    | <0.00      |
|         | Feature<br>2 | 0.4707    | <0.00      |
| M1      | Feature<br>0 | 0.9913    | <0.00<br>1 |
|         | Feature<br>1 | 0.8177    | <0.00<br>1 |
|         | Feature<br>2 | 0.6043    | <0.00<br>1 |
| M2      | Feature<br>0 | 0.9959    | <0.00<br>1 |
|         | Feature<br>1 | 0.7128    | <0.00<br>1 |
|         | Feature<br>2 | 0.5150    | <0.00<br>1 |
| М3      | Feature<br>0 | 0.9628    | <0.00<br>1 |
|         | Feature<br>1 | 0.8274    | <0.00<br>1 |
|         | Feature<br>2 | 0.5670    | <0.00      |
| M4      | Feature<br>0 | 0.9974    | <0.00<br>1 |
|         | Feature<br>1 | 0.8405    | <0.00<br>1 |

|     | Feature<br>2 | 0.4980 | <0.00           |
|-----|--------------|--------|-----------------|
| M5  | Feature      | 0.9941 | 1<br><0.00      |
|     | 0<br>Feature | 0.7702 | 1<br><0.00      |
|     | Feature      | 0.4834 | 1<br><0.00      |
| M6  | Feature      | 0.9752 | 1<br><0.00      |
|     | Feature      | 0.8979 | 1<br><0.00<br>1 |
|     | Feature      | 0.4933 | <0.00<br>1      |
| M7  | Feature      | 0.9965 | <0.00           |
|     | Feature      | 0.8740 | 1<br><0.00      |
|     | Feature      | 0.5295 | 1<br><0.00      |
| M8  | Feature      | 0.9275 | 1<br><0.00      |
|     | Feature      | 0.8084 | 1<br><0.00      |
|     | 1<br>Feature | 0.4732 | 1<br><0.00      |
| M9  | Feature      | 0.9894 | 1<br><0.00      |
|     | Feature      | 0.7009 | 1<br><0.00      |
|     | Feature      | 0.4909 | 1<br><0.00      |
| M10 | Feature      | 0.9934 | 1<br><0.00      |
|     | Feature      | 0.7229 | <0.00           |
|     | Feature<br>2 | 0.4667 | <0.00<br>1      |
| M11 | Feature      | 0.9276 | <0.00<br>1      |
|     | Feature      | 0.8005 | <0.00<br>1      |
|     | Feature      | 0.5679 | <0.00<br>1      |
| M12 | Feature<br>0 | 0.9928 | <0.00<br>1      |
|     | Feature<br>1 | 0.7135 | <0.00           |
|     | Feature      | 0.4826 | <0.00<br>1      |
| M13 | Feature<br>0 | 0.9774 | <0.00<br>1      |
|     | Feature<br>1 | 0.8131 | <0.00<br>1      |
|     |              | 0.7242 | <0.00<br>1      |
| M14 | Feature<br>0 | 0.9454 | <0.00<br>1      |
|     | Feature<br>1 | 0.7269 | <0.00           |
|     | Feature<br>2 | 0.5262 | 1<br><0.00<br>1 |
| M15 | _            | 0.9867 | <0.00<br>1      |
|     | Feature<br>1 | 0.7558 | <0.00           |
|     | Feature      | 0.8348 | <0.00           |

2 1

Real vs.

<span id="page-15-0"></span>**Table 2.** K-S Test Results for Synthetic Data by Machine and Feature

# LSTM-Based Remaining Useful Life (RUL) Prediction Performance

For predicting Remaining Useful Life (RUL) of each component, we developed 15 different Long Short-Term Memory (LSTM) models. Hyperparameters were fine-tuned including the number of LSTM units between 32 and 256, use of single LSTM layer and stacked LSTM layers, and the optimization algorithm between Adam and RMSprop. To prevent overfitting, dropout regularization rates between 0.0 and 0.4 were also included. The models were trained with epochs ranging of up to 100. However, an early stopping callback was added to the model training to halt model training if the model validation loss does not improve for 10 consecutive epochs. Training history curves for Machines 1, 2, and 3 are shown in Appendix D, Figures D1-D3. The complete list of model training history is available on Supplementary S1. Generally, the graphs show stability of training without overfitting.

To evaluate the efficiency of the RUL prediction models, five metrics were calculated in each test set. Mean Absolute Error (MAE), Root Mean Square Error (RMSE), Median Absolute Error (Median AE), Mean Absolute Percentage Error (MAPE), and the percentage of predictions falling within  $\pm 10$  cycles of the true RUL (Within  $\pm 10$ ). To assess the impact of data sparsity and the contribution of GAN-based augmentation, model performance is reported both for models trained with synthetic data augmentation and for models trained using original data only. The results are as shown in Table 3 below:

| machi<br>ne | loss  | MAE   | МАРЕ     | MSE   | R <sup>2</sup> | RMS<br>E | Within ±10 (%) | Media<br>n AE |
|-------------|-------|-------|----------|-------|----------------|----------|----------------|---------------|
| With G      | ANs   |       |          |       |                |          |                |               |
|             | 0.000 | 0.001 |          | 0.000 | 0.999          | 0.004    |                |               |
| M0          | 0     | 2     | 42034.3  | 0     | 8              | 4        | 96.9939        | 0.0009        |
|             | 0.001 | 0.009 |          | 0.001 | 0.982          | 0.038    |                |               |
| M1          | 7     | 2     | 502903.5 | 8     | 9              | 6        | 91.6515        | 0.0058        |
|             | 0.001 | 0.013 |          | 0.001 | 0.988          | 0.033    |                |               |
| M2          | 2     | 9     | 286641.2 | 2     | 4              | 1        | 86.6526        | 0.0111        |
|             | 0.000 | 0.008 |          | 0.000 | 0.993          | 0.023    |                |               |
| М3          | 7     | 3     | 146643.6 | 7     | 3              | 7        | 92.0503        | 0.0057        |
|             | 0.000 | 0.012 |          | 0.000 | 0.991          | 0.027    |                |               |
| M4          | 9     | 4     | 190514.8 | 8     | 9              | 0        | 87.5009        | 0.0099        |
|             | 0.010 | 0.025 |          | 0.003 | 0.968          | 0.053    |                |               |
| M5          | 6     | 1     | 83693.4  | 1     | 1              | 6        | 80.8075        | 0.0154        |

|            |                                                                                                                              |                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                          | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                    |             |                                                                              |
|------------|------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|-------------|------------------------------------------------------------------------------|
| 0.374      | 0.249                                                                                                                        | 359502 9                                                                                                                                                                                                                                                        | 0.096                                                                                                                                                                                                                                                    | 0.024<br>1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 0.309                                              | 7 4971      | 0 2094                                                                       |
| 0.535      | 0.231                                                                                                                        | 333302.3                                                                                                                                                                                                                                                        | 0.070                                                                                                                                                                                                                                                    | 0.263                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 0.264                                              | 7.4371      | 0.2054                                                                       |
| 7          | 0                                                                                                                            | 423743.1                                                                                                                                                                                                                                                        | 0                                                                                                                                                                                                                                                        | 9                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 5                                                  | 7.9589      | 0.2338                                                                       |
| 0.392<br>7 | 0.270<br>8                                                                                                                   | 161375.6                                                                                                                                                                                                                                                        | 0.103                                                                                                                                                                                                                                                    | 0.028                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 0.322<br>4                                         | 3.7097      | 0.2510                                                                       |
| 0.324      | 0.307<br>4                                                                                                                   | 162346.3                                                                                                                                                                                                                                                        | 0.140<br>5                                                                                                                                                                                                                                               | 0.683                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 0.374<br>8                                         | 4.9276      | 0.2478                                                                       |
| 0.263<br>7 | 0.281                                                                                                                        | 150411.9                                                                                                                                                                                                                                                        | 0.114                                                                                                                                                                                                                                                    | 0.371                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 0.338                                              | 6.5769      | 0.2500                                                                       |
| 3          | 5                                                                                                                            | 159076.8                                                                                                                                                                                                                                                        | 8                                                                                                                                                                                                                                                        | 8                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 9                                                  |             | 0.2502                                                                       |
| 0.259<br>4 | 0.268                                                                                                                        | 151588.7                                                                                                                                                                                                                                                        | 0.101                                                                                                                                                                                                                                                    | 0.215                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 0.318                                              | 7.3714      | 0.2501                                                                       |
| 0.284<br>9 | 0.277<br>7                                                                                                                   | 131496.7                                                                                                                                                                                                                                                        | 0.111                                                                                                                                                                                                                                                    | 0.332                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 0.333                                              | 6.7622      | 0.2500                                                                       |
| 5          | 0                                                                                                                            | 136524.5                                                                                                                                                                                                                                                        | 4                                                                                                                                                                                                                                                        | 6                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 8                                                  | 7.4594      | 0.2501                                                                       |
|            |                                                                                                                              | 107602.5                                                                                                                                                                                                                                                        | 0.110<br>4                                                                                                                                                                                                                                               | 0.324<br>5                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 0.332                                              | 6.8090      | 0.2500                                                                       |
| t GAN      |                                                                                                                              |                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                    |             |                                                                              |
| 7          | O                                                                                                                            | 00                                                                                                                                                                                                                                                              | 0                                                                                                                                                                                                                                                        | 7                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 7                                                  | 5.6829      | 0.0253                                                                       |
| 0.285<br>9 | 0.198                                                                                                                        | 37222690<br>.00                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                    |             | 0.0827                                                                       |
| 0.083      | 0.178                                                                                                                        | 2203169.                                                                                                                                                                                                                                                        | 0.071                                                                                                                                                                                                                                                    | 0.837                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 0.268                                              | 2.6026      | 0.1100                                                                       |
|            |                                                                                                                              |                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                    | 3.6830      | 0.1103                                                                       |
| 1          | 4                                                                                                                            | 00                                                                                                                                                                                                                                                              | 9                                                                                                                                                                                                                                                        | 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 0                                                  | 2.6899      | 0.0883                                                                       |
| 7          | 0                                                                                                                            | 00                                                                                                                                                                                                                                                              | 9                                                                                                                                                                                                                                                        | 2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 2                                                  | 4.5455      | 0.1187                                                                       |
| 0.414<br>7 | 0.500<br>7                                                                                                                   | 521470.5                                                                                                                                                                                                                                                        | 0.391                                                                                                                                                                                                                                                    | 0.738                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 0.625                                              | 4.7288      | 0.5345                                                                       |
|            | 0.535 7 0.392 7 0.324 3 0.263 7 0.257 3 0.259 4 0.284 9 0.275 5 0.318 1 of GAN 0.015 7 0.285 9 0.083 9 0.056 1 0.080 7 0.414 | 0.535 0.231 7 0 0.392 0.270 7 8 0.324 0.307 3 4 0.263 0.281 7 0 0.257 0.281 3 5 0.259 0.268 4 0 0.275 0.267 5 0 0.318 0.277 1 0 0 t GAN 0.015 0.040 7 1 0.285 0.198 9 0.083 0.178 9 0 0.015 0.040 7 1 0.285 0.198 9 0.056 0.136 1 4 0.080 0.155 7 0 0.414 0.500 | 0 0 359502.9 0.535 0.231 7 0 423743.1  0.392 0.270 7 8 161375.6  0.324 0.307 3 4 162346.3  0.263 0.281 7 0 150411.9  0.257 0.281 3 5 159076.8  0.259 0.268 4 0 151588.7  0.284 0.277 9 7 131496.7  0.275 0.267 5 0 136524.5  0.318 0.277 1 0 107602.5  1 | 0.535 0.231 0.070 7 0 423743.1 0 0.392 0.270 0.103 7 8 161375.6 9 0.324 0.307 0.140 3 4 162346.3 5 0.263 0.281 0.114 7 0 150411.9 4 0.257 0.281 0.114 3 5 159076.8 8 0.259 0.268 0.101 4 0 151588.7 4 0.284 0.277 0.111 9 7 131496.7 1 0.275 0.267 0.100 5 0 136524.5 4 0.318 0.277 0.110 1 0 107602.5 4 0.15 0.040 7300200. 0.009 7 1 00 0 0.285 0.198 37222690 0.195 9 3 0.00 0.083 0.178 2203169. 0.071 9 8 00 0.080 0.155 3417938. 0.038 7 0 00 0.080 0.155 3417938. 0.038 7 0 00 0.0414 0.500 521470.5 0.391 | 0 0 359502.9 0 0.263 7 0 423743.1 0 9  0.392 0.270 | 0.392 0.270 | 0 0 359502.9 0 1 9 7.4971 0.535 0.231 7 0 423743.1 0 9 5 7.9589  0.392 0.270 |

|       |              |              |          |          | -     |       |         |        |
|-------|--------------|--------------|----------|----------|-------|-------|---------|--------|
|       | 0.189        | 0.327        | 313365.9 | 0.159    | 0.433 | 0.398 |         |        |
| М6    | 6            | 6            | 0        | 1        | 5     | 9     | 2.2082  | 0.3179 |
|       | 0.084        | 0.187        | 368401.3 | 0.063    | 0.532 | 0.251 |         |        |
| M7    | 6            | 1            | 0        | 1        | 0     | 2     | 5.4106  | 0.1401 |
|       |              |              |          |          | _     |       |         |        |
|       | 0.070        | 0.168        | 1604277. | 0.047    | 0.339 | 0.218 |         |        |
| M8    | 9            | 4            | 00       | 6        | 0     | 1     | 2.3810  | 0.1063 |
|       | _            |              |          |          | _     |       |         |        |
|       | 0.580        | 0.618        | 117424.0 | 0.538    | 2.217 | 0.734 |         |        |
| М9    | 2            | 2            | 0        | 7        | 4     | 0     | 1.6992  | 0.6268 |
|       | 0.031        | 0.100        | 157557.1 | 0.014    | 0.347 | 0.119 |         |        |
| M10   | 3            | 4            | 0        | 3        | 7     | 8     | 13.6528 | 0.0999 |
| 1-110 | 0.053        | 0.111        | 132848.6 | 0.017    | 0.443 | 0.131 | 15.0520 | 0.0555 |
| M11   | 0.055        | 2            | 132040.0 | 4        | 5     | 7     | 15.3597 | 0.1082 |
| IALTT | <del>-</del> | <del>-</del> | •        | =        | _     | •     | 15.5597 | 0.1062 |
|       | 0.591        | 0.627        | 345774.0 | 0.529    | 0.229 | 0.727 |         |        |
| M12   | 2            | 0            | 0        | 4        | 0     | 6     | 14.1084 | 0.6499 |
|       | 0.975        | 0.827        | 424091.2 | 0.875    | 0.176 | 0.935 |         |        |
| M13   | 6            | 2            | 0        | 3        | 2     | 6     | 15.1610 | 0.8665 |
|       | 1.453        | 0.955        | 400574.9 | 1.243    | 0.382 | 1.115 |         |        |
| M14   | 1            | 1            | 0        | 5        | 2     | 1     | 14.4018 | 0.9934 |
|       | 7.579        | 2.063        | 331461.0 | 6.539    | 0.692 | 2.557 |         |        |
| M15   | 9            | 1            | 0        | 9        | 4     | 3     | 22.3997 | 1.9799 |
|       |              |              |          | <i>J</i> |       |       |         | 1.5755 |

<span id="page-17-0"></span>**Table 3.** Evaluation Metrics for RUL Prediction Models

These results demonstrate substantial variability in predictive performance across machines and between augmented and nonaugmented training regimes. Models trained with GAN-based data augmentation generally achieve lower absolute errors, higher Within ±10 percentages, and more stable values across most components, particularly for machines with limited failure histories. In contrast, models trained without augmentation exhibit pronounced degradation in predictive performance for several machines, including inflated error metrics and negative R<sup>2</sup> values. indicating poor generalization under severe data sparsity. Elevated Mean Absolute Percentage Error (MAPE) values are observed for some components, especially those operating at large RUL scales, where small absolute deviations result in disproportionately large percentage errors. Importantly, within the proposed framework, RUL predictions are not used directly as point estimates for maintenance decisions. Instead, RUL values are normalized and transformed into a distribution-aware risk representation prior to clustering and scheduling. Consequently, downstream decisions rely on relative proximity and risk ranking rather than raw RUL magnitudes. The implications of prediction uncertainty on clustering robustness and cost-aware maintenance optimization are

further discussed

### **RUL Probability Estimation**

Following RUL prediction using the LSTM models, parametric distributions were fitted to the predicted Remaining Useful Life (RUL) values of each component in order to characterize the empirical distribution of RUL outcomes across runs. Candidate distributions were restricted to forms commonly used to model lifetime and degradation behavior, including Weibull, exponential. gamma, lognormal, inverse Gaussian, Gompertz, and fatigue-life distributions. For each component, the best-fitting distribution was selected based on the sum of squared error (SSE). Table 4 reports the selected distributions and their estimated parameters for models trained with and without GAN-based data augmentation. When trained with augmentation, the fitted distributions exhibit stable parameter estimates and consistent distributional forms components. In contrast, models trained without augmentation often result in highly skewed or extreme parameter values, reflecting the effects of severe data sparsity and limited failure observations. It is important to emphasize that these fitted distributions describe the distribution of predicted RUL values, rather than failure-time processes. As such, the estimated parameters are not interpreted directly in a reliability-theoretical sense. Instead, the fitted distributions are subsequently used to derive a normalized, CDF-based RUL risk proxy that quantifies proximity to the failure boundary. This formulation enables robust downstream clustering and maintenance optimization without relying on explicit failure-time or hazard rate assumptions. The complete list of candidate distributions and fitted parameters is provided in Supplementary File S1.

| compone<br>nt | best_distribu<br>tion | param_c  | param_loc  | param_scale | param_<br>mu | param<br>_s |
|---------------|-----------------------|----------|------------|-------------|--------------|-------------|
| With Gans     | ; /(L                 |          |            |             |              |             |
| 0             | weibu!l_min           | 2.05     | -29.19     | 267.71      |              |             |
| 1             | weibull_min           | 1.91     | -5.86      | 77.08       |              |             |
| 2             | weibull_min           | 1.77     | -8.94      | 127.52      |              |             |
| 3             | invgauss              |          | -50.92     | 504.42      | 0.2923       |             |
| 4             | weibull_min           | 1.82     | -5.55      | 192.09      |              |             |
| 5             | weibull_min           | 2.63     | -143.02    | 505.24      |              |             |
| 6             | weibull_min           | 28829.57 | -832280.17 | 832457.97   |              |             |
| 7             | lognorm               |          | -7502.50   | 7876.75     |              | 0.0093      |
| 8             | lognorm               |          | -20092.36  | 20261.05    |              | 0.0037      |
|               |                       |          |            |             |              |             |

without Gans

| 0  | gompertz    | 0.03      | 3.58              | 2.81         |          |        |
|----|-------------|-----------|-------------------|--------------|----------|--------|
| 1  | lognorm     |           | 3.89              | 1.38         | 0.420924 |        |
| 2  | weibull_min | 1.02      | 5.74              | 1.82         |          |        |
| 3  | lognorm     |           | -2.46             | 7.11         | 0.312943 |        |
| 4  | lognorm     |           | -26.40            | 38.98        | 0.3843   |        |
| 5  | expon       |           | 4.60              | 0.14         |          |        |
| 6  | weibull_min | 0.30      | 10.25             | 32.66        |          |        |
| 7  | weibull_min | 1.42      | -2.90             | 31.10        |          |        |
| 8  | invgauss    |           | -28.71            | 137.25       |          | 0.3414 |
| 9  | weibull_min | 0.97      | 33.41             | 99.20        |          |        |
|    |             | 93951780. | -<br>6371177000.0 | 6371178000.0 |          |        |
| 10 | weibull_min | 00        | 0                 | 0            |          |        |
| 11 | weibull_min | 367215.50 | -36535740.00      | 36536480.00  |          |        |
| 12 | lognorm     |           | -32198030.00      | 32199230.00  | 0.000005 |        |
| 13 | lognorm     |           | -33499010.00      | 33500700.00  | 0.000009 |        |
| 14 | lognorm     |           | -33546850.00      | 33548210.00  | 0.000012 |        |
|    |             | 210232100 | 106069800000      | 10606980000  |          |        |
| 15 | weibull_min | .00       | .00               | 0.00         |          |        |
|    |             |           |                   |              |          |        |

**Table 4.** The best distributions for each component. See supplementary file S1 for the list of all candidate distributions

### <span id="page-19-0"></span>**Maintenance Optimization Strategy**

Failure Probability Estimation To address the issues of excessive, planned and forced, as well as excessive and unplanned, maintenance costs we devised and built an efficient and optimised maintenance planning model as described in our experimental methods section:

### Stage1: RUL-Based Component Clustering

To mitigate excessive preventive maintenance as well as costly unplanned failures, an optimized maintenance planning framework was developed as described in the Experimental Methods section. The first stage of this framework groups components with similar degradation states using predicted Remaining Useful Life (RUL) information, enabling opportunistic maintenance of components with comparable health conditions. Although the dataset comprises 15 components, clustering was performed on the subset of components for which stable RUL distributions could be reliably estimated; the remaining components, affected by extreme data sparsity or unstable distribution fits, were excluded from clustering and scheduled independently. Clustering was carried out using Density-Based Spatial

Clustering of Applications with Noise (DBSCAN), applied to the median predicted RUL values. Components classified as noise—i.e., those not sufficiently close to others in RUL space—were treated as single-component clusters and scheduled independently. The maximum allowable distance between median RUL values for components within the same cluster (ε) was selected using the k-distance elbow method. Figure 3 illustrates the kdistance plots and the identified elbow points used to determine ε for both augmented (left) and non-augmented data (right). Based on this analysis, an ε value of 65.14 hours was selected for clustering. Figure 4 visualizes the resulting cluster memberships and relative proximity between components in RUL space(top panel is for augmented data), while Table [5](#page-20-0)  summarizes the final cluster compositions. When trained with GANaugmented data, components are grouped into fewer, more compact clusters with a silhouette score of 0.579, reflecting moderate but meaningful separation given the heterogeneous degradation profiles. In contrast, clustering based on the original (non-augmented) data yields more fragmented groupings, driven by sparse and uneven failure histories, resulting in a higher silhouette score (0.885) but reduced practical interpretability for coordinated maintenance actions. This higher silhouette score is primarily an artifact of exaggerated separation caused by sparse and unstable RUL estimates, rather than evidence of genuinely distinct degradation regimes. These results highlight the stabilizing affect of data augmentation on RUL-based clustering, enabling more coherent grouping of components for downstream maintenance scheduling.

![](_page_20_Figure_2.jpeg)

Optimal threshold for cluster dissimilarity (*δ*)

<span id="page-20-0"></span>

| cluster   |   | Components  |
|-----------|---|-------------|
| With Gans |   |             |
|           | 0 | {0, 4, 6,8} |
|           | 1 | { 1, 2, 3}  |
|           | 2 | { 5,7}      |

**Figure 3.**

| Silhouette    |                       |
|---------------|-----------------------|
| score:        | 0.579                 |
|               |                       |
| Original data |                       |
|               | {0, 1, 2, 3, 4, 5, 6, |
| 0             | 8, 9}                 |
| 1             | { 13,15}              |
| 2             | { 12,14}              |
| 3             | {10, 11}              |
| Silhouette    |                       |
| score:        | 0.885                 |

 **Table 5.** Clustering results

![](_page_21_Figure_3.jpeg)

 **Figure 4.** Visual representation of the clusters

### **Stage 2: Optimal Maintenance Time Selection and Sensitivity Analysis**

After clustering components based on RUL proximity, a grid search was

conducted to determine the optimal maintenance time  $t_k$  for each cluster. The objective was to minimize the expected maintenance cost while avoiding both premature preventive actions and excessive failure risk. The search domain for  $t_k$  was defined over the feasible RUL range of each cluster, with the additional constraint that the normalized failure risk proxy remained below a predefined threshold.

Expected maintenance cost was expressed as a weighted combination of preventive, failure, and downtime costs. To enable a systematic sensitivity analysis, all costs were normalized by the preventive maintenance cost  $C_p$ , such that  $C_p=1$ , while failure and downtime costs were expressed as multiples of  $C_p$  (i.e.,  $C_{pf} \in \{5,10,20,40,80\}, C_d \in \{0,2,5,10\}$ ). This normalization allows results to be interpreted independently of absolute monetary scales.

Figure 5 presents the sensitivity of the expected maintenance cost to variations in  $C_f$  and  $C_d$  across the full RUL range. The results indicate that changes in cost parameters primarily rescale the magnitude of the expected cost curves without altering their overall shape. In particular, the location of the minimum expected cost—and thus the optimal maintenance time  $t_k$  remains stable across a wide range of cost assumptions. As expected, expected cost increases monotonically as  $t_k$  decreases toward zero RUL, reflecting the rapidly increasing risk of failure when maintenance is deferred excessively.

To further interpret cost behavior, Figure 6 decomposes the expected cost into preventive, failure, and downtime components for each cluster. This decomposition confirms that variations in individual cost parameters uniformly magnify their respective contributions without changing the relative dominance or temporal ordering of cost components. Preventive cost dominates at large RUL values, while failure and downtime costs increase sharply as the system approaches the failure boundary.

An identical sensitivity analysis conducted on models trained without data augmentation produced qualitatively similar cost curve shapes and optimal maintenance times; however, the expected cost increased more steeply as RUL decreased, reflecting higher instability in risk estimates under data sparsity. See figure 7 and 8 below.

![](_page_23_Figure_1.jpeg)

![](_page_23_Figure_2.jpeg)

<span id="page-23-0"></span> **Figure 5.** Trend in cluster costs (augmented data)

![](_page_23_Figure_5.jpeg)

**Figure 6:** Decomposition of expected costs to preventive, failure and downtime costs (augmented data)

<span id="page-24-0"></span>![](_page_24_Figure_2.jpeg)

**Figure 7.** Trend in cluster costs(original data)

<span id="page-24-1"></span>![](_page_24_Figure_5.jpeg)

**Figure 8:** Decomposition of expected costs to preventive, failure and down time costs (original data)

# Stage 4: Validation-Based Comparison with Baseline Maintenance Strategies

To further evaluate the effectiveness of the proposed cluster-based maintenance strategy, a validation-based comparison was conducted against two baseline scheduling approaches: a random maintenance strategy and fixed-percentile maintenance policies. All strategies were evaluated on the validation set using normalized cost parameters, consistent with the sensitivity analysis results.

For the proposed approach, maintenance scheduling was performed by combining RUL-based clustering with grid-search optimization of the maintenance threshold

 $t_k$ , subject to a minimum survival constraint (e.g., survival proxy  $\geq$  0.3). Maintenance actions occurring before failure was recorded as preventive, while actions scheduled after failure were counted as corrective interventions.

In order to further assess the efficiency of the proposed cluster-based maintenance strategy, a validation-based comparison was made on such two baseline scheduling strategies as random maintenance strategy and fixed-percentile maintenance policies. The entire strategies were tested on the validation set based on normalized cost parameters, which is in line with the sensitivity analysis outcome.

In the case of the proposed approach, maintenance scheduling was done by implementing a composite algorithm of RUL-based clustering and grid-search optimization of the maintenance threshold.t<sub>k</sub>, with a minimum survival constraint (e.g., survival proxy  $\geq$  0.3). The process of maintenance that takes place prior to failure was noted as preventive and the one executed after failure was noted as corrective interventions. Figure 9 below compares the three strategies based on Total costs and average of total costs while figure 10 compares the three strategies, based number of maintenance actions taken as  $\theta$  changes.

<span id="page-26-0"></span>![](_page_26_Figure_1.jpeg)

**Figure 9:** left panel shows trend in realized costs across survival threshold( $\theta$ ).while left panel shows the average costs(argumented data)

<span id="page-26-1"></span>![](_page_26_Figure_3.jpeg)

**Figure 10:** Comparison between predictive and correct maintenances (data augmented)

Repeating the same evaluation using models trained without data augmentation yielded qualitatively similar trends, although the absence of augmentation resulted in higher corrective failure counts and increased cost variability. These results confirm that the proposed cluster-based strategy provides more reliable and cost-effective maintenance decisions than non-adaptive baseline policies, while remaining robust to cost scaling and modeling assumptions see appendix E for these graphs.

### **Discussion**

This study was motivated by three recurring limitations identified in the

predictive maintenance (PdM) literature: (i) the treatment of data augmentation as a tool for improving predictive accuracy rather than decision robustness, (ii) the limited use of component-level clustering for coordinated maintenance actions, and (iii) the reliance on point RUL estimates for cost-based scheduling under uncertainty. The discussion below interprets the results explicitly in relation to these strands of prior work.

### RUL prediction errors and decision robustness

Several prior studies emphasize improving RUL prediction accuracy as the primary objective of PdM models [9, 10, 33, 34]. Consistent with observations in these works, the present results show that percentage-based error metrics such as MAPE can become extremely large for small true RUL values, exceeding 300% for some components. Similar instability of relative error measures at low RUL has been noted implicitly in probabilistic prognostics studies [34], though its downstream implications are rarely discussed.

Importantly, the proposed framework does not rely on point RUL estimates for maintenance decisions. Instead, predicted RUL trajectories are aggregated and modeled probabilistically, and decisions are driven by relative degradation proximity and distribution-aware risk trends. This design directly addresses a limitation of prediction-centric PdM pipelines highlighted in [35], where errors in late-life predictions can propagate into unstable maintenance decisions. The findings indicate that although the accuracy of RUL against some components decreases, the clustering and scheduling processes are stable, which proves that the robustness of decisions can be separated without depending on the accuracy of point-prediction.

### Role of GAN-based augmentation beyond prediction accuracy

Existing GAN-based PdM studies are mainly tested on the augmentation benefits by measuring them with better predictive metrics. As an instance, Hakami et al. [12] and similar studies [18-20] prove that GANs are able to address data scarcity and imbalance in classes, contributing to an increase in model accuracy. These studies however conclude at the prediction phase and fail to investigate the impacts of augmentation on downstream maintenance choices.

The research findings of ablation demonstrate that the main advantage of GAN-based augmentation is not just the predictive accuracy, but the ability to stabilize learned RUL distributions in the case of extreme sparsity of failures. Unaugmented RUL distributions are also unstable, and tend to cluster fragments into fake clusters, and the expected cost curves have sharp gradients at the boundary of failure. Augmentation on the other hand generates more coherent clustering structures and smooth RUL distributions, facilitating the cost optimization. This directly fills the gap it has been established in the Introduction the lack of frameworks that explicitly relate augmented data to effective maintenance decision-making.

Although silhouette scores were worse with GAN-augmented

clustering, this result indicates the decrease in artificial separation due to low and patchy histories of failures instead of reduced operational relevance. As with the findings of [30-32] on maintenance clustering, the concept of operational coherence and coordinated servicing is more significant than cluster separation in geometry only.

### RUL-based clustering and opportunistic maintenance

In the maintenance setting, the concept of clustering has been applied in terms of task grouping and efficiency of planning [29-32], yet it has not been utilized in the context of PdM, with most of the research being conducted on the system-level or isolated component-level prognostics [33-35]. Independent treatment of components may result in inefficient maintenance schedules in cases where there are several components with similar degradation horizons as pointed out by [33].

The findings of the clustering in this paper provide empirical evidence of the usefulness of component-level RUL-based structuring. The framework allows opportunistic maintenance by grouping components that have a similar state of degradation and minimize redundant interventions and synchronize servicing actions of components that tend to need maintenance in a similar time range. This strategy is more realistic with regard to the heterogeneous nature of industrial systems, which is in line with the arguments that have been presented in [34, 351.

### Cost sensitivity and robustness of scheduling decisions

Several studies of PdM are based on putative parameters of costs without investigating their impact on maintenance decisions [26, 27, 34]. To overcome this drawback, the current sensitivity analysis shows that different preventive, corrective, and downtime costs mainly rescale the expected cost curves but do not change their shape and moves the optimal maintenance level. This was behavioral throughout cluster and augmentation conditions, and it implies that the overall scheduling choices are controlled by the degradation behavior and not arbitrary cost calibration.

It is interesting to note that the non-augmented models had steep gradients in the cost close to the failure boundary in that it was more unstable and susceptible to scheduling delays. This result supports the need to integrate augmentation, clustering, and probabilistic risk modeling to make sound choices in uncertainty.

### Comparison with baseline maintenance strategies

In line with previous criticisms of non-adaptive maintenance policies viewed as static [27, 34], the finding when compared to the random and fixed-percentile baselines indicates the weaknesses of non-adaptive scheduling policies. The variability of random scheduling was found to be high even with Monte Carlo averaging and fixed-percentile strategies were incapable of capturing component-specific degradation behavior.

Conversely, the proposed cluster-based approach steadily minimized

the corrective failures and lower normalized cost was obtained on validation data. These findings are empirical evidence that successful PdM must involve coordination among the components and adaptive and risk-sensitive threshold selection as opposed to fixed or prediction-based policies.

### **Conclusions**

The given work illustrates that predictive maintenance systems should be shifted to more decision-oriented designs that are not focused on predictions. The proposed framework includes data augmentation with GANs, RUL prediction, component-centric clustering, and cost-conscience scheduling to overcome the major shortcomings that were observed in the current PdM literature. The findings indicate that strong maintenance decisions can be attained even when there is extreme data unavailability and uncertainty of prediction, which offers a viable avenue to real-life implementation.

### Limitations and Future Work

Although the framework is better robust with sparse failure data, extremely limited history components were unable to provide stable distribution fits and were executed in isolation. Such components could be better incorporated in future work by using hierarchical or transfer-learning methods. Also, the suggested CDF-based risk proxy is not a actual failure-time probability but a relative risk measure, which can be enhanced further by incorporating models of survival analysis; it should be emphasized that theoretical basis may be further bolstered. The generalization of the framework into the multi-system environment and dynamic cost structures is also a potential research direction in the future.

### <span id="page-30-6"></span>References

- <span id="page-30-0"></span>Tortora, A. M. R., Di Pasquale, V., Franciosi, C., Miranda, S., and lannone, R., The Role of Maintenance Operator in Industrial Manufacturing Systems: Research Topics and Trends, Applied Sciences, vol. 11, no. 7, p. 3193, April 2021. https://www.mdpi. com/2076-3417/11/7/3193, 10.3390/app11073193.
- <span id="page-30-1"></span>2. Lee, J. and Singh, J., Intelligent Maintenance Systems and Predictive Manufacturing, ResearchGate, June 2020. https://www.researchgate.net/publication/342247340 Intelligent Maintenance Systems and Predictive Manufacturing.
- <span id="page-30-2"></span>3. Hamasha, M. M., Banilrshid, A. H., Mashaqbeh, S. A., Shwaheen, G., Qadri, L. A., Shbool, M., Muathen, D., Ababneh, M., Harfoush, S., Albedoor, Q., and Al-Bashir, A., Strategical selection of maintenance type under different conditions, Scientific Reports, vol. 13, no. 1, September 2023. https://doi.org/10.1038/s41598-023-42751-5, 10.1038/s41598-023-42751-5.
- <span id="page-30-3"></span>4. Zwoliń ska, B. and Wiercioch, J., Selection of maintenance strategies for machines in a Series-Parallel system, Sustainability vol. 14, no. 19, p. 11953, September 2022. https://doi.org/10.3390/su141911953, 10.3390/su141911953.
- <span id="page-30-4"></span> Pan, J., Gutschi, C., Furian, N., Mizelli, D., and Voessner, S., *A framework\_to\_enhance predictive maintenance\_installation in high volume production environments: A case study*, Procedia CIRP, vol. 112, pp. 134–139, January 2022.https://www.researchgate.net/publication/363778051 A framework to enhance predictive maintenance installation in high volume production environments A case study,10.1016/j.procir.2022.09.051.
- <span id="page-30-5"></span>6. Paul, A. L., Odu, A., and Oluwaseyi, J., *Predictive Maintenance: Leveraging Machine Learning for Equipment Health Monitoring*, ResearchGate, January 2024. https://www.researchgate.net/publication/377411657 Predictive Maintenance Leveraging Machine Learning for Equipment

### Health Monitoring.

- 7. Elkateb, S., M´etwalli, A., Shendy, A., and Abu-Elanien, A. E. B., *Machine learning and IoT Based predictive maintenance approach for industrial applications*, Alexandria Engineering Journal, vol. 88, pp. 298–309, January 2024. https://doi.org/10.1016/j. aej.2023.12.065.
- <span id="page-31-0"></span>8. Aminzadeh, A., Karganroudi, S. S., Majidi, S., Dabompre, C., Azaiez, K., Mitride, C., and S'en'echal, E., *A Machine Learning Implementation to Predictive Maintenance and Monitoring of Industrial Compressors*, Sensors, vol. 25, no. 4, p. 1006, February 2025. https://www.mdpi.com/1424-8220/25/4/1006.
- <span id="page-31-1"></span>9. Galar, D., Goebel, K., Sandborn, P., and Kumar, U., *Prognostics and Remaining Useful Life (RUL) Estimation*, November 2021. https://doi.org/10.1201/9781003097242.
- <span id="page-31-2"></span>10. Patel, M., Vasa, J., and Patel, B., *Predictive Maintenance: A Comprehensive Analysis and Future Outlook*, 2023 2nd International Conference on Futuristic Technologies (INCOFT), pp. 1–7, November 2023. https://doi.org/10.1109/incoft60753.2023. 10425122.
- <span id="page-31-3"></span>11. Sarker, I. H., *Machine learning: Algorithms, real-world applications and research directions*, SN Computer Science, vol. 2, no. 3, March 2021. https://doi.org/1.1007/ s42979-021-00592-x.
- <span id="page-31-4"></span>12. Hakami, A., Strategies for overcoming data scarcity, imbalance, and feature selection challenges in machine learning models for predictive maintenance, Scientific Reports, vol. 14, no. 1, April 2024. https://doi.org/10.1038/s41598-024-59958-9.
- <span id="page-31-5"></span>13. Araf, I., Idri, A., and Chairi, I., Cost-sensitive learning for imbalanced medical data: a review, Artificial Intelligence Review, vol. 57, no. 4, March 2024. https://doi.org/ 10.1007/s10462-023-10652-8.
- <span id="page-31-6"></span>14. Salmi, M., Atif, D., Oliva, D., Abraham, A., and Ventura, S., *Handling imbalanced medical datasets: review of a decade of research*, Artificial Intelligence Review, vol. 57, no. 10, Sept. 2024. https://doi.org/10.1007/s10462-024-10884-2.
- <span id="page-31-7"></span>15. Fullington, D., Yangue, E., Bappy, M. M., Liu, C., and Tian, W., Leveraging small-scale datasets for additive manufacturing process modeling and part certification: Current practice and remaining gaps, Journal of Manufacturing Systems, vol. 75, pp. 306–321, May 2024. https://doi.org/10.1016/j.jmsy.2024.04.021.
- 16. Sharif, H., Hyttinen, J., Gao, X.-Z., Hauta-Kasari, M., and Räisänen, R., *Data Aug- mentation Methods for Deep Learning Neural Networks*, Artificial Intelligence and Machine Learning, Dec. 2024. https://doi.org/10.20944/preprints202412.2343.v1.
- <span id="page-31-8"></span>17. Tian, S. I. P., Ren, Z., Venkataraj, S., et al., *Tackling data scarcity with transfer learning: a case study of thickness characterization from optical spectra of perovskite thin films*, Digital Discovery, vol. 2, no. 5, pp. 1334–1346, Jan. 2023. https://doi.org/10.1039/d2dd00149g.

- <span id="page-32-0"></span>18. Xu, C., Li, W., Cui, X., et al., *Scarcity-GAN: Scarce data augmentation for defect detection via generative adversarial nets*, Neurocomputing, vol. 566, p. 127061, Nov. 2023. https://doi.org/10.1016/j.neucom.2023.127061.
- <span id="page-32-1"></span>19. García-Esteban, J. J., Cuevas, J. C., and Bravo-Abad, J., *Generative adversarial networks for data-scarce radiative heat transfer applications*, Machine Learning Science and Technology, vol. 5, no. 1, p. 015060, Mar. 2024. https://doi.org/10.1088/ 2632-2153/ad33e1.
- <span id="page-32-2"></span>20. Vilela-P´erez, N., Heras, D. B., and Argüello, F., *EFFBAGAN: an efficient balancing GAN for earth observation in data scarcity scenarios*, IEEE J. Sel. Top. Appl. Earth Obs. Remote Sens., pp. 1–20, Jan. 2024. https://doi.org/10.1109/jstars.2024.3510859.
- <span id="page-32-3"></span>21. Ali, H., Grönlund, C., and Shah, Z., Leveraging GANs for data scarcity of COVID- 19: Beyond the hype, Proc. 2022 IEEE/CVF Conf. Comput. Vis. Pattern Recognit. Workshops (CVPRW), pp. 659–667, Jun. 2023. https://doi.org/10.1109/cvprw59228. 2023.00073.
- 22. Aeschbacher, D., Meisner, J., Miletic, M., and Sariyar, M., *Use and Evaluation of GANs for Synthetic Data Generation in Pharmacogenetics*, Studies in Health Technology and Informatics, Nov. 2024. https://doi.org/10.3233/shti241100.
- 23. Abdalla, Y., Taub, M., Hilton, E., et al., *VECT-GAN: A variationally encoded gen- erative model for overcoming data scarcity in pharmaceutical science*, arXiv preprint, Jan. 2025. http://arxiv.org/abs/2501.08995.
- <span id="page-32-4"></span>24. Mobeen, M., Afzal, A., Saeed, R., Arshad, T., and Asad, M., Leveraging GANs for synthetic tabular data generation: a platform-centric solution to data scarcity, IET Conf. Proc., vol. 2024, no. 10, pp. 242–249, Oct. 2024. https://doi.org/10.1049/icp. 2024.3311.
- <span id="page-32-5"></span>25. Yang, H., Xiang, Z., Li, X., and Zhang, W., *An improved GAN-Based data augmentation model for addressing data scarcity in SRMs*, Measurement Science and Technology, Jan. 2025. https://doi.org/10.1088/1361-6501/ada570.
- <span id="page-32-6"></span>26. Ali, B. M., Al-Musawi, T. J., Mohammed, A., et al., *Sustainable Strategies for preventive maintenance and replacement in photovolraic power systems: enhancing reliability, efficiency, and system economy*, Unconventional Resources, p. 100170, Mar. 2025. https://doi.org/10.1016/j.uncres.2025.100170.
- <span id="page-32-7"></span>27. Zhao, J., Gao, C., and Tang, T., *A review of sustainable maintenance strategies for single component and multicomponent equipment*, Sustainability, vol. 14, no. 5, p. 2992, Mar. 2022. https://doi.org/10.3390/su14052992.
- <span id="page-32-8"></span>28. Alhourani, F., Essila, J., and Farkas, B., *Preventive maintenance planning considering machines' reliability using group technology*, Journal of Quality in Mainte-nance Engineering, vol. 29, no. 1, pp. 136–154, Dec. 2021. https://doi.org/10.1108/jqme-12-2019-0118.
- <span id="page-32-9"></span>29. Ahmed, R., Nasiri, F., and Zayed, T., *Two-Stage predictive maintenance planning for hospital buildings: a Multiple-*

- *Objective Optimization-Based Clustering approach*, Journal of Performance of Constructed Facilities, vol. 36, no. 1, Oct. 2021. https://doi.org/10.1061/(asce)cf.1943-5509.0001691.
- <span id="page-33-0"></span>30. Bazeli, S., and Fallahnezhad, M. S., Clustering of Condition-Based Mainte- nance Considering Perfect and Imperfect actions, International Journal of Reli-ability Risk and Safety Theory and Application, vol. 3, no. 1, pp. 69–76, Jan. 2020. https://www.researchgate.net/publication/353179158
  Clustering of Condition-Based Maintenance Considering Perfect and Imperfect actions.
- <span id="page-33-1"></span>31. Quatrini, E., Colabianchi, S., Costantino, F., and Tronci, M., Clustering Application for Condition-Based Maintenance in Time-Varying Processes: A review using Latent Dirichlet Allocation, Applied Sciences, vol. 12, no. 2, p. 814, Jan. 2022. https://doi.org/10.3390/app12020814.
- <span id="page-33-2"></span>32. Agergaard, J. K., Sigsgaard, K. V., Mortensen, N. H., Ge, J., and Hansen, K. B., *Quantifying the impact of early-stage maintenance clustering*, Journal of Quality in Maintenance Engineering, vol. 29, no. 5, pp. 1–15, Jun. 2022. https://doi.org/10.1108/jgme-07-2021-0056.
- <span id="page-33-3"></span>33. Lv, Y., Zheng, P., Yuan, J., and Cao, X., *A Predictive maintenance Strategy for Multi-Component systems based on components' remaining useful life prediction*, Mathematics, vol. 11, no. 18, p. 3884, Sep. 2023. https://doi.org/10.3390/ math11183884.
- <span id="page-33-4"></span>34. Mitici, M., De Pater, I., Barros, A., and Zeng, Z., *Dynamic predictive maintenance for multiple components using data-driven probabilistic RUL prognostics: The case of turbofan engines*, Reliability Engineering System Safety, vol. 234, p. 109199, Feb. 2023. https://doi.org/10.1016/j.ress.2023.109199.
- <span id="page-33-5"></span>35. Feng, Q., Zhang, Y., Sun, B., Guo, X., Fan, D., Ren, Y., Song, Y., and Wang, Z., *Multi-level predictive maintenance of smart manufacturing systems driven by digital twin: A matheuristics approach*, Journal of Manufacturing Systems, vol. 68, pp. 443–454, May 2023. https://doi.org/10.1016/j.jmsy.2023.05.004

### **Acknowledgements**

The author appreciatively acknowledges the support of the Jazan Development and Investment Company to facilitate and support data collection.

### **Author contributions**

A. H. conceptualization, A.H. methodology, A.H. data curation, A.H. formal analysis, A.H. writing-review and editing. All authors have read and agreed to the published

version of the manuscript.

### **Funding**

The authors did not receive fund from any organization for the submitted work.

### **Additional information**

**Correspondence** and requests for materials should be addressed to A.H.

**Competing interests** The author declares no competing interests.

**Supplementary Information** The supplementary file S1 includes additional output data and extended results that support the findings of this study.

### **Code Availability**

The complete raw source code used for training and validation has been made publicly available at: https://github.com/AliH1409/Code.git

### **Data Availability**

The datasets used during the current study are available from the corresponding author on reasonable request.
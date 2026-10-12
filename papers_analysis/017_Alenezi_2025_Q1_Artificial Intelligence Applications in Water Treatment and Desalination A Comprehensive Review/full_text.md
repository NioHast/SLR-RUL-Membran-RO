![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_1.jpeg)

*Review*

# **Artificial Intelligence Applications in Water Treatment and Desalination: A Comprehensive Review**

**Anwur Alenezi 1,\* and Yousef Alabaiadly <sup>2</sup>**

- <sup>1</sup> Water Research Centre, Kuwait Institute for Scientific Research, Safat 13109, Kuwait
- <sup>2</sup> Studies and Research Department, Ministry of Electricity and Water, Ministries Zone 12010, Kuwait; yaalobidly@mew.gov.kw
- **\*** Correspondence: anwenezi@kisr.edu.kw; Tel.: +96-524-989-338

**Abstract:** This paper examines the application of artificial intelligence (AI) in desalination. The study explored AI techniques, including machine learning, neural networks, and genetic algorithms, to enhance system efficiency and reduce energy costs. Case studies assessed the impact of AI on desalination systems, including those powered by renewable energy sources. Key findings revealed that AI-driven systems improved water quality, reduced energy consumption by up to 50%, and enabled predictive maintenance, minimizing downtime. Challenges in integrating AI with renewable energy-powered water treatment and desalination systems were addressed by analyzing hybrid setups combining solar, wind, and battery storage with reverse osmosis (RO) and multi-stage flash (MSF) technologies. These systems demonstrated critical improvements in energy efficiency, making desalination more viable for arid and remote areas. Fault detection algorithms and predictive maintenance emerged as pivotal AI applications, significantly reducing maintenance costs and enhancing reliability. This study was concluded by identifying challenges such as the intermittent nature of renewable energy and the complexities of designing scalable hybrid AI systems. Future research should further refine AI techniques, advancing sustainable and energy-efficient water treatment solutions.

**Keywords:** artificial intelligence; desalination technologies; water treatment; renewable energy integration; process optimization; fault detection algorithm; machine learning applications; predictive maintenance; energy efficiency; hybrid AI systems

![](_page_0_Picture_10.jpeg)

Academic Editor: José Luis Sánchez-Lizaso

Received: 15 January 2025 Revised: 14 March 2025 Accepted: 15 March 2025 Published: 14 April 2025

**Citation:** Alenezi, A.; Alabaiadly, Y. Artificial Intelligence Applications in Water Treatment and Desalination: A Comprehensive Review. *Water* **2025**, *17*, 1169. [https://doi.org/10.3390/](https://doi.org/10.3390/w17081169) [w17081169](https://doi.org/10.3390/w17081169)

**Copyright:** © 2025 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license [\(https://creativecommons.org/](https://creativecommons.org/licenses/by/4.0/) [licenses/by/4.0/\)](https://creativecommons.org/licenses/by/4.0/).

# **1. Introduction**

Water is the most essential constituent of life; however, the rapid global population growth has exerted immense pressure on clean and drinkable water. Traditionally, water sources have been strained, with nearly 2 billion people (26 percent of the global population) lacking safe drinking water, according to the U.N.'s World Water Development Report 2023 [\[1\]](#page-26-0). These approaches have been proposed to address pollution issues, but they involve high energy consumption and operational costs, as well as environmental impacts. With the aim to address these problems and improve sustainability, artificial intelligence (AI) is currently being widely applied in the industry.

AI offers promising solutions to the challenges in water treatment and desalination, resulting from the ability of AI to process large datasets, to predict outcomes, and to optimize complex systems. Yet questions remain about the specific areas of AI application and the results obtained and, consequently, about their impact on these fields. Despite increasing interest in AI, research on the topic is still scattered in the literature, and the same

*Water* **2025**, *17*, 1169 2 of 28

articles often concentrate on only a small portion of AI applications, without providing an overall understanding of the role and outcomes of AI in practice.

## *1.1. Background on Water Treatment and Desalination*

Water treatment and desalination are crucial processes for utilizing other water sources that would otherwise not be suitable for use. Salts and other impurities are removed from seawater or brackish water during desalination, and the water becomes suitable for drinking or for other purposes [\[2\]](#page-26-1).

Although traditional water treatment and desalination methods have been effective, these methods have a few drawbacks. For example, reverse osmosis (RO) [\[3](#page-26-2)[,4\]](#page-26-3) and distillation [\[5](#page-26-4)[,6\]](#page-26-5) desalination are energy- and cost-intensive methods. Similar to the other processes, they also raise environmental concerns, including brine disposal [\[7–](#page-26-6)[9\]](#page-26-7) and greenhouse gas emissions [\[10–](#page-26-8)[12\]](#page-26-9). These limitations have driven the search for more efficient, cost-effective, and environmentally friendly technologies, with AI emerging as a key solution.

Given that AI is not just a buzzword, but a powerful transformative technology, the water treatment and desalination industries face increasingly complex problems that can be addressed with AI. For example, predictive modeling allows plants to predict equipment failures or when the equipment needs maintenance before it results in downtime, increasing the lifespan of expensive machinery. Fault detection systems can identify the problems before they escalate, and process optimization increases efficiency, reduces energy consumption, and enhances operations [\[13\]](#page-26-10).

These are great areas where AI's potential benefits are immense. AI can optimize processes in management, and it leads to a reduced energy usage, lower costs, and better water quality. In addition, AI can assist plants in greater resource management, reduce waste, and mitigate some environmental impacts. However, the application of AI in water treatment and desalination remains an emerging area of research, with many questions about its practical implementation, outcomes, and future prospects.

# *1.2. Research Question*

This study addresses the following research question: how has AI been utilized in desalination, and what are the outcomes? This research question guided the exploration of the current state of AI applications in these fields, focusing on the methods employed, the results achieved, and the challenges that remain.

#### *1.3. Objectives*

To address the research question, this study focused on the following specific objectives:

- 1. To review the application of AI in desalination. This involved analyzing AI techniques, such as machine learning (ML), neural networks, and genetic algorithms (GAs), as well as their use in predictive modeling, process optimization, and fault detection.
- 2. To examine the outcomes of AI applications, including reduced energy costs, improved efficiency, and enhanced water quality. This included analyzing case studies to identify real-world impacts and remaining challenges.
- 3. To identify specific desalination systems where AI has been implemented, providing insights into its application across various contexts and the results achieved.

#### *1.4. Rationale and Significance of the Study*

The need for this study was driven by the increasing importance of sustainable water management. As water scarcity worsens, particularly in arid regions, the demand for efficient and cost-effective water treatment and desalination technologies has become more *Water* **2025**, *17*, 1169 3 of 28

urgent. AI holds significant potential to address many challenges associated with these technologies, but its application remains in its infancy. By conducting a comprehensive review of the literature, this study aimed to provide a deeper understanding of the AI's current applications, achieved outcomes, and prospects in these fields.

This study is significant for several reasons. First, it contributes to the academic understanding of AI's role in desalination, addressing gaps in existing literature and establishing a foundation for future research. Second, it offers practical insights for engineers, researchers, and policymakers, enhancing their ability to leverage AI's potential while understanding its limitations. Finally, by identifying areas where AI has made substantial impacts, this study seeks to guide future investments and research efforts, ensuring the extensive utilization of AI's capabilities.

# **2. Methodology**

This review answered the question, how is AI being used in desalination, and what are the results? This section discusses some details on how the relevant literature was gathered, evaluated through checking for relevance and rigor, and synthesized.

#### *2.1. Literature Review Process*

In this work, we searched academic journals, conference papers, books, and credible online resources for information about how something could be controlled. The preference of sources was for those that had a rigorous peer review process, such as Water Research, Journal of Hydrology, and Desalination, which are highly regarded in the field. The initial search resulted in an average of 1200 potential sources that were narrowed to 150 highquality, peer-reviewed articles based on relevance, credibility, and impact factor. Journals such as Water Research, Journal of Hydrology, and Desalination were given priority and are of high reputation.

Specific keywords were developed to facilitate the search: "ML in desalination", "neural networks for water quality", and similar keywords. These 'keywords' helped in a very broad and specific search to answer the research question.

Databases such as Google Scholar, Scopus, and Web of Science were selected for their extensive indexing of academic publications. After conducting the searches, a comprehensive list of potential sources was compiled. This initial list was substantial, as expected, but required further refinement.

Each source was evaluated by skimming abstracts and conclusions to assess its relevance to this study's focus. Relevance was the primary criterion, but the credibility of authors and publications was also considered. Papers authored by recognized experts and published in high-impact journals were prioritized.

Following this filtering process, a manageable list of sources remained. To further streamline the review, these sources were categorized based on their primary focus—AI in desalination. This categorization ensured comprehensive coverage of all aspects of the research question. Figure [1](#page-2-0) illustrates this process. *Water* **2025**, *17*, x FOR PEER REVIEW 4 of 29

<span id="page-2-0"></span>![](_page_2_Figure_11.jpeg)

**Figure 1.** Literature review process. **Figure 1.** Literature review process.

Water 2025, 17, 1169 4 of 28

#### 2.2. Analytical Framework

With the literature pool established, the next step involved analyzing the content of these papers. The analysis emphasized the methods employed, key findings, and their connection to the research question. The analytical framework focused on three main areas: AI techniques, outcomes, and context, as illustrated in Figure 2.

- AI techniques: This review identified specific AI methods used in desalination, including ML algorithms, neural networks, GAs, and related technologies. Each technique's strengths and weaknesses were assessed. For instance, ML excels at making predictions based on large datasets, while neural networks model complex, non-linear relationships. Particular attention was given to how these techniques were implemented—including the type of data used, software or tools employed, and model validation methods.
- 2. Outcomes: After the relevant AI techniques were identified, the results they produced were analyzed. Key focus areas included accuracy, efficiency improvements, cost reductions, and energy savings. Broader impacts, such as enhanced water quality, reduced operational costs, and environmental sustainability, were also considered. Performance metrics were noted for each study and compared across different papers to identify patterns and trends.
- 3. Context: AI technologies function within specific contexts, which significantly influence their effectiveness. For example, AI applications in large-scale desalination plants may differ from those in small, community-based water treatment systems. Contextual factors, such as system size, complexity, data quality, and operational challenges, were effectively analyzed to interpret the results.

<span id="page-3-0"></span>![](_page_3_Figure_6.jpeg)

Figure 2. Analytical framework.

#### 2.3. Synthesis and Integration

After analyzing each study, the findings were synthesized into a coherent narrative. This process involved identifying common themes or patterns in the data, such as the prevalence of certain AI techniques in desalination. Discrepancies, such as contradictory results across studies, were also noted and discussed.

*Water* **2025**, *17*, 1169 5 of 28

# *2.4. Critical Assessment of Methodologies*

Several methodological issues were identified during the review. A common concern was the lack of transparency in reporting AI models. Many studies did not provide sufficient detail about the algorithms used, model training, or validation processes, hindering replication and comparison. Transparency is critical in AI research to ensure the validity of models and facilitate further advancements.

Another issue was the use of small datasets. Effective AI models, particularly ML and neural networks, require large datasets. Some reviewed studies relied on relatively small datasets, leading to overfitting—where the model performs well on training data but fails to generalize new data. This limitation affects the real-world applicability of such models.

Additionally, many studies focused on short-term outcomes, such as immediate efficiency gains or cost savings, while neglecting long-term impacts, such as sustainability or environmental effects. This represents a big gap in the literature and can be further explored.

Finally, the review evaluated the statistical methods used by the studies. Several studies had used older or otherwise inappropriate statistical methods, potentially compromising the reliability of their findings. This emphasizes the importance of continued education and training in statistical techniques by researchers who use AI.

# *2.5. Limitations and Challenges*

There were several methodological limitations and challenges encountered by this review. The large volume of literature on the use of AI in water treatment and desalination was one challenge. This abundance represented the field's growth, but high-quality, peerreviewed studies had to be selected. Thus, research relevant to this field might have been overlooked in less traditional outlets.

The reviewed studies were not homogeneous, which is another limitation. Much of the AI is context-specific, making it hard to draw general conclusions. Outcomes can vary differently depending on the circumstances. The diversity was enriching, but, consequently, it presented a synthesis problem.

Last, data availability was a limitation. AI research is highly data-driven, and the reviewed studies employed different quality datasets. Certain studies utilized vast and high-quality datasets, whereas the rest relied on smaller, relatively less reliable datasets. The variation altered the study outcomes and hampered cross-paper comparisons.

# **3. AI in Water Treatment**

With recent advances in AI came the ability to apply AI to water treatment to provide innovative solutions to water scarcity and pollution. AI techniques are used to optimize processes, improve water quality, decrease costs, and reduce energy consumption. In this section, we look at how AI plays a role in water treatment, focusing on key techniques such as using ML, neural networks, and GAs. In addition, case studies, performance metrics, and outcomes are reviewed regarding the effect of these technologies in real-world situations.

#### *3.1. Overview of AI Techniques in Water Treatment*

#### 3.1.1. Machine Learning Algorithms

ML involves building intelligent systems that can modify their behavior during training, depending on new information. It is a technique used for prediction or decisionmaking, using historical data without explicit programming. Moreover, ML has proven effective in predicting water quality parameters, optimizing treatment processes, and detecting contaminants. An ML framework for improving water quality in a treatment plant is illustrated in Figure [3.](#page-5-0) In total, 80% of the dataset was used to train the ML models, Water 2025, 17, 1169 6 of 28

<span id="page-5-0"></span>and the remaining 20% was used for validation. Raw water production (RWP), water turbidity, conductivity, total dissolved solids (TDSs), salinity, pH, water temperature (WT), suspended matter (SM), and oxygen levels  $(O_2)$  were used as input variables. Validation was performed using cross-validation and statistical measures, such as  $R^2$ , RMSE, and MAE.

![](_page_5_Figure_2.jpeg)

**Figure 3.** Machine learning framework designed to improve water quality in a water treatment plant. (Online monitored data from the water plant is first used to build models (random forest and deep neural networks). After validation, the model interpretation step identifies the most important operating variables and illustrates how they influence effluent parameters. This insight then informs the development of a sophisticated control strategy. Finally, the control strategy is applied to the treatment process, creating a feedback loop that continually improves water quality).

ML models were shown by Zhang et al. [14] to be able to accurately predict water quality parameters, including pH, turbidity, and dissolved oxygen levels (O<sub>2</sub>). Many stages of water treatment, from raw water intake to final distribution, have been proven to be flexible and adaptable to ML techniques.

These studies make use of the label datasets and train models using supervised learning. Support vector machines (SVM), random forests (RF), and k nearest neighbor (KNN) were already widely used as techniques. For example, Lowe et al. [15] modeled the creation of disinfection by-products (DBPs) and key parameters involved in adsorption and membrane filtration processes. Their models were evaluated by statistical measures such as correlation coefficient (R), coefficient of determination (R<sup>2</sup>), mean absolute error (MAE), mean square error (MSE), root mean square error (RMSE), and relative error (RE). To demonstrate the potential of real-time monitoring and optimization, ML was shown to have great achievement, especially when all input variables were incorporated into the models. For real-time changes, it allows operators to tune parameters, and this makes them rapid, while also saving money without any human intervention.

Bhagat et al. [16] studied copper ion removal through adsorption using the three ML models: ANN, SVM, and RF. Key input parameters were selected for initial copper concentration, adsorbent dosage, pH, contact time, and ionic strength, with 80% of the dataset being used for training and 20% for testing. An R over 0.99 was attained by RF and ANN models, compared to 0.93 for SVM's maximum. The RF and ANN models could handle the complex variable interactions and the nonlinearity of adsorption processes and thus achieved this superior performance. A comparative summary of the performance of the models is given in Table 1.

Water 2025, 17, 1169 7 of 28

| Model                              | R (Correlation Coefficient) | Best Input Set                                                                        | Accuracy  |
|------------------------------------|-----------------------------|---------------------------------------------------------------------------------------|-----------|
| Artificial Neural<br>Network (ANN) | >0.99                       | Initial copper concentration, adsorbent dosage, contact time, pH, NaNO <sub>3</sub> . | Very High |
| Support Vector<br>Machine (SVM)    | 0.93                        | Initial copper concentration, adsorbent dosage.                                       | Moderate  |
| Random Forest (RF)                 | >0.99                       | Initial copper concentration, adsorbent dosage, contact time, pH, NaNO <sub>2</sub> . | Very High |

<span id="page-6-0"></span>**Table 1.** Comparative summary of the model's performance.

RF and ANN models exhibited great predictive capabilities that enabled advanced process modeling toward efficiency without further costs. ML's potential for managing uncertainties in water treatment systems was discussed by Sundui et al. [17]. By mixing up ML algorithms with real-time sensor data, we were able to make accurate predictions of breakdowns of pipelines, bioreactors, and temperature or organic loading changes. They allowed for proactive system adjustments to become a predictive process rather than a more traditional reactive process. ML forecasts the problems and implements corrective measures that reduce downtime, reduce operational costs, and improve overall reliability.

Li et al. [18] emphasized ML's widespread use in addressing regression and classification challenges in water treatment. Predictive models developed using ML reliably estimate process parameters, including flow rate, contaminant concentration, and system pressures. For instance, in membrane filtration, ML models can predict fouling rates and adjust system pressure to mitigate fouling, extending membrane lifespan and reducing maintenance frequency. This predictive capability is vital for process optimization, cost reduction, and improved energy efficiency.

However, ML's efficiency depends on the availability of large, high-quality training datasets. In regions with limited or inadequate data, training ML models becomes challenging. Furthermore, the quality and diversity of training data significantly influence prediction accuracy.

#### 3.1.2. Neural Networks

Neural networks, inspired by the structure and function of the human brain, represent a robust AI technique used in water treatment. These networks consist of interconnected nodes (neurons) that process and transmit information, enabling the modeling of complex, non-linear relationships in water treatment processes, such as chemical dosing and filtration efficiency. Wang et al. [19] demonstrated that deep neural networks (DNNs) outperform traditional statistical methods in predicting water treatment outcomes. Figure 4 compares artificial neural network (ANN) and DNN models in predicting coagulant dosage and settled water turbidity.

Neural networks, similar to other ML models, require substantial computational resources and large datasets to achieve high accuracy. These networks are trained by adjusting the weights of connections between neurons using techniques such as backpropagation. While highly effective, neural networks are often criticized as "black boxes" due to their opaque and complex decision-making processes, posing interpretability challenges that can limit their widespread adoption in critical water treatment operations.

Khataee and Kasiri [20] discussed the use of ANNs to model the advanced oxidation processes (AOPs) that are vital for the oxidation of diverse pollutants. There are many operational parameters for these processes, so they are difficult to model using traditional linear methods. Therefore, they have been used to simulate interactions between catalyst

Water 2025, 17, 1169 8 of 28

concentration, pollutant type, and reaction time to better predict system behavior. Such models are extremely important because they may be used to scale up chemical reactors in industrial applications where tight knowledge of variable interaction is critical.

<span id="page-7-0"></span>![](_page_7_Figure_2.jpeg)

**Figure 4.** Comparing artificial and deep neural network models for predicting coagulant dosage and settled water turbidity. (First, raw data from the treatment plant is gathered and sent to the preprocessing step. Next, the cleaned data feeds into the neural networks (artificial or deep) to predict coagulant dosage and settled water turbidity. Finally, these predictions guide adjustments in the sequential treatment tanks, creating a feedback loop that continually refines water quality).

Matheri et al. [21] demonstrated the successful application of ANNs to model the relationship between chemical oxygen demand (COD) and trace metal concentrations in a wastewater treatment plant (WWTP). The ANN used a supervised learning algorithm, and R<sup>2</sup>s between 0.98 and 0.99, as well as low RMSE and MSE values were obtained. The results show that ANNs efficiently predict WWTP performance and provide a cost-effective approach to environmental management. Specifically, this capability is useful for integrating big data and emerging technologies for wastewater treatment.

This was achieved by Kulisz et al. [22] by using ANN models to predict groundwater quality with a reduced set of input parameters. They developed a highly effective model using stepwise regression to optimize and reduce the number of inputs from seven to five. Electrical conductivity and pH, as well as calcium, magnesium, and sodium ion concentrations were input parameters. The model with five input and five hidden neurons was able to achieve an R of 0.9992 and an R<sup>2</sup> of 0.9984. Table 2 highlights the model's performance metrics.

<span id="page-7-1"></span>Table 2. Key performance metrics of neural networks.

| Metric                                         | Value    |
|------------------------------------------------|----------|
| RMSE                                           | 0.651258 |
| Correlation Coefficient (R)                    | 0.9992   |
| Coefficient of Determination (R <sup>2</sup> ) | 0.9984   |

This study has shown that ANNs can predict water quality well, especially in industrial areas where contamination is common. ANN models are a reliable tool for monitoring and controlling water treatment in the industry, allowing for industrial decision-making based on the data.

#### 3.1.3. Genetic Algorithms

Optimization techniques inspired by the principles of natural selection are called GAs. In solving complex problems, especially in iterating over a refinement of candidate

Water 2025, 17, 1169 9 of 28

solutions between generations, they are particularly effective. GAs have been applied to optimize energy consumption in desalination plants, to control chemical dosages, and to improve water quality in water treatment.

<span id="page-8-0"></span>GAs are based on evolutionary processes, generating a population of potential solutions, evaluating them, and using crossover and mutation to create new solutions. Then, this process repeats many times in a series of generations to identify an optimal solution. The application of GAs in water management procedures by ML integration is shown in Figure 5.

![](_page_8_Figure_3.jpeg)

**Figure 5.** Genetic algorithm-based machine learning procedure for water management. (First, the intelligent algorithm feeds into the prediction support systems, which generate insights on water quality and quantity. Next, those predictions flow into the decision-making support systems, where incoming water, consumed water, and water distribution routes are evaluated. Label assignment and feature extraction steps further refine the data, ensuring continuous updates for each group. This creates a feedback loop that supports ongoing improvement in water management).

In practical applications, GAs have been applied to improve the design and rehabilitation of water distribution networks, to simulate groundwater quality, and to model water productivity. They are good at balancing competing objects, such as a minimization of energy use with an increase in treatment efficiency. GAs simulate evolutionary principles and are a flexible and powerful approach to solving the various challenges in modern water treatment.

Chandra et al. [23] conducted a study in this domain and found that GAs can reduce operational costs, sustaining or improving water quality. Studies analyzing GAs identify the computational time required for convergence as the main challenge with these AI techniques. This issue becomes more pronounced when GAs are implemented at a larger scale. Another key consideration is that solutions generated by GAs are not always guaranteed to be globally optimal, which can limit the efficiency of primary applications.

Walters and Savic [24] described how GAs optimize water distribution network design by determining the optimal pipe diameters for cost-effective construction while maintaining adequate pressure at various nodes. GAs help navigate the vast number of potential solutions by encoding pipe diameters as binary or integer strings (similar to chromosomes), enabling the method to explore numerous configurations. The initial random selection of designs is refined over time, and even infeasible solutions (where pressure is too low) are penalized, but not discarded. This evolutionary process has been successfully applied in multiple projects, including extending water networks in Australia, resulting in significant cost savings.

However, GAs face challenges when scaling to larger networks, as the number of variables becomes difficult to manage. To address this, Tao et al. [25] introduced the Structured Messy Genetic Algorithm (SMGA), simplifying the process by focusing only on the most critical pipes in the network. This method has proven highly effective for rehabilitation projects where limited funds necessitate selecting the most impactful improvements, such

*Water* **2025**, *17*, 1169 10 of 28

as reducing leakage and increasing pressure. The evolution process here mirrors the way simple life forms evolve into complex organisms, a compelling analogy that helps explain the power of GAs.

Pandey et al. [\[26\]](#page-27-1) demonstrated the effectiveness of GAs combined with artificial neural networks (GA-ANN) in predicting groundwater table depth (GWTD) in the region between India's Ganga and Hindon rivers. Over 21 years, they collected data on groundwater recharge and discharge. They found that hybrid GA-ANN models outperformed traditional GA models in predicting both pre-monsoon and post-monsoon water table depths. Notably, the GA-ANN models with more input variables performed better, emphasizing capturing all relevant factors when predicting groundwater levels. This method can easily be applied to similar regions worldwide, making it a valuable tool for managing groundwater resources.

Bahiraei et al. [\[27\]](#page-27-2) applied GAs to optimize the water productivity of a new nanofluidbased solar still. They used a Multi-Layer Perceptron (MLP) neural network enhanced with a GA to predict water productivity based on solar radiation, nanoparticle concentration, and various temperatures (water, glass, basin, and ambient). The GA-MLP model reduced the RMSE by 40.49% compared to a standard MLP model, demonstrating that GAs can significantly improve prediction accuracy. Interestingly, when compared to another optimization method, the Imperialist Competition Algorithm (ICA), GAs performed slightly worse but still provided a marked improvement over traditional models.

GAs have demonstrated versatility across various aspects of distribution, from optimizing complex networks to enhancing prediction models. The success of these algorithms largely depends on their ability to balance multiple variables—whether optimizing pipe diameters, predicting groundwater levels, or improving water productivity in solar stills. While the basic GA approach works well for smaller systems, more advanced methods, such as the SMGA or hybrid GA-ANN models, are necessary for larger, more complex systems. Table [3](#page-9-0) summarizes the performance of these models, including reductions in RMSE and other performance indicators, illustrating the effectiveness of GAs in these applications.

<span id="page-9-0"></span>**Table 3.** Performance of GA models.

| Study<br>Application   |                                    | Optimization Method |
|------------------------|------------------------------------|---------------------|
| Walters and Savic [24] | Water Distribution Networks        | GA                  |
| Halhal et al. [28]     | Network Rehabilitation             | SMGA                |
| Pandey et al. [26]     | Groundwater Table Depth Prediction | GA-ANN              |
| Bahiraei et al. [27]   | Water Productivity in Solar Stills | GA-MLP              |

GAs provide a powerful and flexible tool for solving complex problems in distribution. Whether designing a cost-effective pipe network, predicting seasonal groundwater levels, or optimizing a solar still's water output, GAs offer robust solutions for engineers in this field. The future of water treatment will likely involve more advanced hybrid models, where GAs are combined with other techniques to further enhance their predictive and optimization capabilities.

#### 3.1.4. Case Studies and Examples

The transformation of traditional water treatment practices by ML is particularly seen in how the optimal dosage of coagulants (CD) should be determined. The jar test is a common method in water treatment plants, but it is also expensive, time consuming, and requires particular laboratory equipment. An alternative that is more efficient for estimating coagulant dosage, without the need to perform traditional tests, is provided by ML.

*Water* **2025**, *17*, 1169 11 of 28

To predict the CD in water treatment plants, a hybrid ML model combining M5 and the Gorilla Troops Optimizer (GTO) was used as a case study [\[24\]](#page-26-21). The aim was to improve accuracy by using nine parameters: raw water production (RWP), water turbidity, conductivity, total dissolved solids (TDSs), salinity, pH, water temperature (WT), suspended matter (SM), and O2. These variables were the inputs for estimating the needed coagulant dosage.

The M5-GTO model outperformed several standard models, including multiple linear regression, ANN, and random forest (RF), in predicting coagulant dosage. For example, when compared to the least-squares support vector machine (LSSVM), the worstperforming algorithm in the test, the M5-GTO model was up to 73% more accurate based on MAE and reduced root RMSE by 55%. The M5-GTO also had an R of 0.967, demonstrating a robust fit between the predicted and observed data. To illustrate this, Table [4](#page-10-0) provides a performance comparison.

| Algorithm     | MAE   | RMSE  | Relative<br>RMSE | Normalized<br>RMSE | Correlation<br>Coefficient |
|---------------|-------|-------|------------------|--------------------|----------------------------|
| M5-GTO        | 0.562 | 1.172 | 0.257            | 0.170              | 0.967                      |
| LSSVM (worst) | 2.080 | 2.600 | 0.569            | 0.378              | 0.927                      |
| M5 (2nd rank) | 0.650 | 1.300 | 0.315            | 0.220              | 0.955                      |
| RF (3rd rank) | 0.780 | 1.420 | 0.329            | 0.235              | 0.948                      |

<span id="page-10-0"></span>**Table 4.** Performance comparison of different algorithms.

Notably, the partial dependence plots generated by the model revealed that two parameters, RWP and WT, had the most significant influence on coagulant dosage. An increase in RWP was associated with a reduction in coagulant dosage, while a rise in WT led to an increase in dosage. This is expected, as an increase in raw water production (RWP) can lead to the dilution of contaminants solely when mixing takes place within the system, minimizing the need for coagulants, while warmer water temperature (WT) can lead to an increase in chemical reactions, requiring higher dosages.

The M5-GTO algorithm has shown significant potential in modeling parameters in water treatment plants, proving to be not only more efficient but also more accurate than traditional methods. It represents a major step forward in optimizing water treatment processes, reducing reliance on labor-intensive and costly procedures, such as the jar test.

#### 3.1.5. Analysis of Outcomes

- 1. Improvements in water quality: AI has consistently demonstrated its ability to enhance water quality. Zhang et al. [\[14\]](#page-26-11) used ML models to predict turbidity levels with high accuracy, allowing operators to proactively adjust treatment processes. This resulted in consistently clearer water and fewer filter backwashes, conserving both water and energy. AI has played a significant role in monitoring and ensuring better water quality in developing regions with less advanced water treatment infrastructure. For example, simple ML models installed in rural areas in India have helped local authorities monitor water quality in real-time, leading to quicker responses to potential contamination and better public health outcomes [\[29\]](#page-27-4).
- 2. Cost reductions: One of the most significant benefits of AI in water treatment is cost reduction. By optimizing chemical dosages, energy use, and maintenance schedules, AI can lead to substantial cost savings for water treatment facilities. Pandey et al. [\[26\]](#page-27-1) demonstrated that applying GAs to enhance the chemical treatment process resulted in a 12% decrease in chemical costs. They achieved this by identifying the most efficient

*Water* **2025**, *17*, 1169 12 of 28

- combination of treatment chemicals and regulating their dosages dynamically based on real-time data.
- 3. Energy savings: Applying AI techniques in water treatment significantly contributes to energy savings of 50%. In addition to the reported 50% energy reduction, AI-driven systems have illustrated a 20% enhancement in membrane lifespan, a 15% minimization in chemical usage, and a 10% increase in freshwater production efficiency. These benefits are particularly pronounced in energy-intensive water treatment processes. This is especially true for RO systems, where neural networks have shown effectiveness in optimizing energy use [\[16,](#page-26-13)[17\]](#page-26-14). Ultimately, the energy savings achieved by incorporating AI not only reduce operational costs but also contribute to environmental sustainability by lowering the carbon footprint of key facilities.

## 3.1.6. Critical Assessment of Methodologies

Integrating AI into the water treatment processes involves diverse methodologies, ranging from supervised ML to evolutionary algorithms, such as GAs. Although each method has its strengths, it also has limitations that must be addressed for AI techniques to reach their full potential in water treatment.

One such limitation is the data requirement across all AI techniques. As noted earlier, these methods require large, high-quality datasets to operate effectively. In most cases, water treatment plants lack historical data, which are critical for training accurate models. This challenge can limit the efficacy of AI systems.

Another issue is the computational demands of AI techniques. Specifically, techniques such as neural networks and GAs require substantial computational resources, which can be a barrier for small facilities or those in developing regions.

Additionally, AI techniques face challenges related to interpretability, which need to be addressed for AI to be effective in water treatment processes. Certain AI models are called 'black boxes' and they can do only limited functionality. It is amid water treatment processes where understanding or explaining AI-driven decisions is vital for public health, and without these methods, the global use of those methods can be limited.

# 3.1.7. Conclusions

The use of AI in water treatment and desalination presents a great potential for significantly improving water quality, lowering the costs, and improving energy efficiency. Yet, to be able to be integrated into these processes, the challenges of data availability, computational demands, and model interpretability must also be addressed.

Despite many studies successfully showing the ability of AI in water treatment, there is a lack of research on the long-term effects of AI-driven optimization. Additionally, very little attention is paid to the deployment of AI in low-resource settings, where water treatment challenges are the greatest.

In the future, AI models requiring less data and computational power should be designed to be more accessible to a wider range of water treatment facilities. At the same time, we need to make the effort to make AI models more interpretable, so that they can be confidently applied in critical water treatment operations.

Finally, AI can change water treatment in general. Still, the large-scale implementation would only happen if the current limitations were overcome, and the benefits were available to everyone. This research will fill in the gap in the field and open new, novel AI use in water treatment.

*Water* **2025**, *17*, 1169 13 of 28

# **4. AI in Desalination**

AI has been widely applied in desalination across various domains. With water scarcity affecting much of the world, desalination, which involves converting saltwater into potable water, has emerged as an important innovation. However, desalination processes are energy-intensive and costly. AI can help optimize these processes, reducing operational costs and improving efficiency. Additionally, AI can reduce the environmental impact of desalination by enhancing process optimization. This section critically reviews the current and potential applications of AI in desalination, focusing on predictive modeling, process optimization, and fault detection and maintenance. Specific case studies are highlighted to demonstrate how AI has improved desalination systems, leading to better performance and energy savings.

## *4.1. Overview of Desalination Processes*

## 4.1.1. Reverse Osmosis (RO)

RO is the most common desalination process globally. The process works by forcing saltwater through a semi-permeable membrane, which removes salt and other impurities. Although effective, RO systems require regular maintenance [\[25](#page-27-0)[,26\]](#page-27-1). Challenges, such as membrane fouling, high energy consumption, and the need for precise pressure control, can be efficiently addressed using AI.

#### 4.1.2. Distillation

Distillation, particularly multi-stage flash (MSF) [\[27](#page-27-2)[,30\]](#page-27-5) and multi-effect distillation (MED) [\[31](#page-27-6)[,32\]](#page-27-7), is another widely adopted desalination method. This process involves heating seawater to generate steam, which condenses into freshwater. While effective, distillation is energy-intensive. AI can optimize the heating and condensation stages, reducing energy consumption and improving the efficiency of these desalination methods.

## *4.2. AI Techniques Applied to Desalination*

## 4.2.1. Predictive Modeling

Predictive modeling uses AI to forecast future outcomes based on past data. Desalination could involve predicting when a membrane in an RO system will need cleaning or replacement, or forecasting energy consumption under different operating conditions.

The significance of predictive modeling is highlighted in the study by Qadir et al. [\[33\]](#page-27-8), which demonstrated that predictive models can precisely forecast maintenance needs, reduce unexpected downtime, and extend the lifespan of desalination equipment. These models, employing techniques such as ML and neural networks, analyze large datasets from desalination plants. Common methods include supervised learning, where algorithms are trained on labeled datasets. These models can predict membrane fouling, energy consumption, and water quality. Effective techniques include decision trees (DTs), deep learning, and SVM. Figure [6](#page-13-0) illustrates the use of predictive models in conjunction with thermal energy storage to enhance the efficiency and sustainability of solar desalination systems.

Qadir et al. [\[33\]](#page-27-8) performed predictive modeling of nanofiltration membranes using a MATLAB program based on the Donnan Steric Pore Model (DSPM) and the Extended Nernst–Planck Equation (ENP). Traditionally, the structural parameters of membranes such as pore radius, membrane thickness, and charge density—required numerous experimental trials. However, the method described by Qadir et al. [\[33\]](#page-27-8) reduced the need for extensive lab work by analyzing solute rejection and permeation data to accurately predict membrane performance.

Water 2025, 17, 1169 14 of 28

<span id="page-13-0"></span>![](_page_13_Picture_1.jpeg)

**Figure 6.** Optimizing solar desalination by incorporating integrative predictive models with thermal energy storage for better efficiency and sustainability. (The orange arrows represent the flow of solar energy from the sun to the solar field and then into the storage tank, where heat can be stored for later use. The bidirectional orange arrows between the storage tank and the control element indicate that the system can both store and release thermal energy as needed. Meanwhile, the green arrows show the movement of water through the desalination process, benefitting from the stored heat. The integrative predictive model continuously adjusts these energy and water flows, ensuring optimized efficiency and sustainability).

For instance, the E5C1 membrane demonstrated superior salt rejection rates compared to other membranes (E5, E5C5). At a pressure of 10 bar, the E5C1 membrane rejected 60% of NaCl and 80% of CaCl<sub>2</sub> from 100 ppm solutions. Table 5 summarizes the key structural parameters of the membranes and their respective salt rejection efficiencies.

<span id="page-13-1"></span>

| Table       | <b>e 5.</b> Key structural param | eters of the membranes a | and their respective sa | alt rejection efficiencies. |
|-------------|----------------------------------|--------------------------|-------------------------|-----------------------------|
| Pore Radius | Thickness/Porosity               | Charge Density           | NaCl                    | CaCl <sub>2</sub>           |

| Membrane | Pore Radius<br>(nm) | Thickness/Porosity<br>(μm) | Charge Density (mol/m³) | NaCl<br>Rejection (%) | CaCl <sub>2</sub><br>Rejection (%) |
|----------|---------------------|----------------------------|-------------------------|-----------------------|------------------------------------|
| E5C1     | 0.5                 | 16                         | -6.04                   | 60                    | 80                                 |
| E5C5     | 0.7                 | 12                         | -5.00                   | 50                    | 65                                 |
| E5       | 1.0                 | 10                         | -4.00                   | 40                    | 55                                 |

The E5C1 membrane was shown to be the most effective, largely due to its smaller pore size and higher charge density, which better-controlled ion transport. This method allows for accurate predictions of membrane behavior with fewer experiments, saving both time and resources in membrane design.

Salem et al. [34] developed a predictive model for a hybrid desalination system powered by solar energy. Using ANNs, their study predicted the efficiency of a solar-driven desalination system that combined solar stills with air humidification and dehumidification units. A key challenge in this modeling is optimizing regression accuracy, which Salem et al. [34] addressed by implementing the Adam optimizer to enhance the performance of a standard MLP. The optimized model (OMLP) was then compared to regular MLP, DT, and Bayesian ridge regression (BRR), using metrics such as RMSE, MAE, and R². The results were impressive: OMLP outperformed other models, predicting the desalination efficiency with an RMSE ranging from 0.07171 to 8.05636 and a maximum error between 0.10108 and 14.19858.

Mahadeva et al. [35] applied a Modified Whale Optimization Algorithm (MWOA) alongside ANNs to optimize the performance of RO desalination plants. The objective

*Water* **2025**, *17*, 1169 15 of 28

was to predict permeate flux based on input variables such as the feed flow rate, salt concentration, and temperatures in the evaporator and condenser. The MWOA-ANN models (Models 1–10) were compared to existing models, such as the Response Surface Methodology (RSM) and basic ANN models. Model-6, which featured a single hidden layer with 11 nodes and 13 search agents, achieved the most accurate predictions, with an R <sup>2</sup> value of 99.1% and a mean squared error (MSE) of 0.005, showing a strong fit between predicted and actual values. The MWOA-ANN models for Model 6 have been shown by Mahadeva [\[35\]](#page-27-10) to be very effective in optimizing the process parameters of RO desalination plants, and they have been found to predict accurately, with few errors. However, the accuracy of ANN-based models using optimization algorithms such as MWOA has been found to be significantly better than that of ANN models with no optimization, and thus very useful to industrial plant designers.

Large amounts of high quality data are needed for the predictive models to be successful, but in some cases such data can also be lacking. In addition, although these models can predict well the outcomes, they do not have to offer a reasoning explaining the cause of these trends. Therefore, predictive models may not serve in cases when one needs to troubleshoot or discover the root causes of problems.

## 4.2.2. Process Optimization

The application of AI to optimize desalination process parameters for optimal process performance is known as process optimization. It could involve changing the pressure in an RO system, the temperature in a distillation process, or chemical dosages.

AI optimization of desalination systems has provided large reductions in energy (and capital) costs and energy efficiency. For instance, Zhang et al. [\[14\]](#page-26-11) showed that applying AI to pressure and flow rate optimization in an RO system led to a 15% reduction in energy usage. Nevertheless, due to the complexity of desalination processes, it is necessary to incorporate a large number of variables into the optimization process, which makes the overall optimization process computationally time-consuming and intensive.

Guided by the food–energy–water nexus principle, Di Martino et al. [\[36\]](#page-27-11) specifically proposed an optimization framework to solve the problem of RO desalination plants. It was to balance water production, energy use, and environmental impact, particularly in arid and semi-arid regions. In the first case, a surrogate model was developed to simulate desalination by different membrane modules, with different input energy, and different saline water sources. It was formulated as a mixed integer nonlinear optimization problem (MINLP) that could quickly evaluate multiple design scenarios. It offers a way to make decisions concerning desalination plant configurations by balancing energy consumption and water demand. The framework was applied to evaluate different scenarios of water production and energy usage for an instance study in South-Central Texas. By this approach, the RO plants have become more flexible to changing environmental conditions and therefore will decrease cost and resource demand in the water desalination effort.

Another emerging desalination technology is the emerging technology of capacitive deionization (CDI), which is highly energy efficient and capable of selectively removing ions. In CDI, water is driven between charged electrodes (the ions are removed by an electric field). In this regard, Al Rajabi et al. [\[37\]](#page-27-12) provided a very detailed review of CDI and its variants (MCDI and FCDI). A cost study in the form of a levelized cost of water (LCOW) was conducted for the CDI relative to other desalination methods, including RO and nanofiltration. Accordingly, their findings indicate that CDI should reduce energy consumption, particularly in areas with moderate salinity levels, thanks to its ability to remove only specific ions. Most of the optimization techniques for CDI have been directed toward the electrode and desalination cell design. Performance is influenced by the elec*Water* **2025**, *17*, 1169 16 of 28

trode composition, applied voltage, and electrolyte properties. Hybrid CDI systems may also be processed and optimized by combining them with other desalination technologies to achieve better performance, lower costs, and better sustainability. Selectively removing ions such as calcium or sodium through controlled electrode characteristics helps maintain low energy consumption while ensuring high desalination efficiency. These advancements pave the way for large-scale CDI adoption in both water-scarce and industrial regions.

Shin et al. [\[38\]](#page-27-13) focused on improving the energy efficiency of FCDI, a variant of CDI that allows for continuous operation by circumventing electrode saturation issues. The key innovation is the use of flow electrodes, which carry charged ions continuously, allowing the system to operate without stopping to recharge the electrodes. Shin et al. [\[38\]](#page-27-13) identify several optimization avenues, including electrode material selection, cell design, and operating conditions. By adjusting these variables, energy consumption can be significantly reduced, especially in low-salinity environments where FCDI is particularly effective. Furthermore, the study emphasizes the importance of process control algorithms in maintaining energy efficiency over long periods, ensuring the sustainable operation of desalination plants. AI integration into FCDI enables real-time adjustments in electrode and electrolyte configurations, reducing energy use without compromising water output. These insights are crucial for the future deployment of FCDI in desalination plants, where energy costs remain a limiting factor.

Optimization techniques in desalination can significantly improve both efficiency and sustainability. With the help of AI-driven models and algorithms, the designs of desalination plants can be optimized, which will save energy and meet the exponentially growing water demand while causing little environmental damage. However, these techniques need to continue to develop to ensure that they can help deal with water scarcity, and in particular, as the world heads toward a climate change and resource depletion reality.

## 4.2.3. Fault Detection and Maintenance

Fault detection and predictive maintenance are achieved and potential issues are identified before they cause the system to fail with the help of AI. This includes detecting leaks, membrane fouling, or component wear in desalination plants. AI methods such as anomaly detection, which identifies patterns deviating from normal operations, are commonly used in desalination plants. Neural networks and ML models have also been applied to analyze sensor data, predicting when maintenance may be needed. Figure [7](#page-16-0) illustrates the process of detecting faults and facilitating maintenance in a desalination plant.

Said and Sihem [\[39\]](#page-27-14) focused on using hybrid dynamic systems to address fault detection in desalination plants. A hybrid system combines continuous and discrete dynamics such as when water flow pressure (continuous) interacts with the opening and closing of valves (discrete). The study proposed a method that integrated hybrid automata with a neural fuzzy system to detect faults. The neural fuzzy system modeled the continuous behavior of the desalination process, capturing how factors such as water flow and pressure changed over time. Hybrid automata, in contrast, managed the discrete aspects of the system, such as detecting sudden events, e.g., valve failures or pump shutdowns. Together, these models classified and detected faults as they occurred, providing an automated method for early issue detection. Real-world application of this method in a desalination plant demonstrated its effectiveness in improving reliability, reducing maintenance costs, and minimizing downtime.

Water 2025, 17, 1169 17 of 28

<span id="page-16-0"></span>![](_page_16_Figure_1.jpeg)

**Figure 7.** Illustration of the process used to detect faults in a desalination plant. (The arrows depict how data and decisions flow through the fault detection process. First, measurements from the pumping system are scaled and used to calculate the head for a given pressure and flow rate. Next, a decision point checks if the test flow rate is lower than that of water, triggering the appropriate classification (sludge-free or with sludge). Finally, these classifications feed into the training data set, refining threshold limits and parameters for ongoing improvements in fault detection).

In RO systems, actuator faults are a common issue. Mehrad and Kargar [40] developed an integrated fault detection and fault-tolerant control system to address this challenge. In their approach, the parity space was used to estimate the actuator faults by comparing actual system behavior with expected behavior. In case of any fault, the system would adapt using model predictive control (MPC) to compensate and hence maintain stable water production by adjusting certain parameters (valve opening). The study suggests that the method can tolerate up to 90% of actuator faults, rendering the system operational even in the presence of faulty components. This robustness is important to guarantee the quality of freshwater produced by RO plants with minimal energy losses. By using a receding horizon predictive control system could anticipate the issues which are ahead and could respond. By enhancing the resilience of the desalination plants, fault detection

*Water* **2025**, *17*, 1169 18 of 28

combined with the automatic control process adjustment reduced the requirement for manual intervention.

Based on their work, Saidy et al. [\[41\]](#page-27-16) propose Maintenance with Predictive Maintenance 4.0, which is based on the use of modern digital technologies, such as the IoT, ML, and data analytics. Predictive Maintenance 4.0 is different from conventional maintenance, which deals with a reaction that takes place after a failure has already occurred. This maintenance type solves this problem by analyzing real-time data. In desalination plants, sensors continuously monitor equipment performance, such as pump efficiency, water pressure, and temperature. These data feed into ML models that predict when components are likely to fail, allowing for proactive maintenance scheduling. This approach reduces unplanned downtime, which is costly in terms of both repairs and lost productivity. Furthermore, Predictive Maintenance 4.0 can improve product lifecycle management (PLM). Continuous equipment monitoring provides feedback that can inform future desalination system designs, enhancing efficiency and reliability in new systems.

However, it is important to note that fault detection systems must be highly reliable. False positives could lead to unnecessary maintenance and operational disruptions. Moreover, the need for extensive sensor networks and data collection can be costly, particularly for smaller desalination plants.

## *4.3. Case Studies and Examples*

Specific Desalination Systems and Their AI Applications

Sayed et al. [\[42\]](#page-27-17) investigated how AI techniques could optimize the design and control of desalination systems powered by renewable energy. In arid regions, where water scarcity is persistent, renewable energy sources (e.g., solar, wind, or geothermal energy) are increasingly used to power desalination plants. However, renewable energy's unpredictable nature complicates the maintenance of a steady desalination output. In their study, Sayed et al. [\[42\]](#page-27-17) proposed integrating AI techniques such as forecasting models and optimization algorithms to address this challenge. They combined photovoltaic (PV) systems with battery energy storage and fuel cells, allowing AI algorithms to predict energy availability based on weather patterns and adjust desalination processes accordingly. The AI system optimized the operation of RO and MSF desalination technologies, ensuring stable and efficient freshwater production. Increased utilization of energy, coupled with a reduction in operational challenges, reduced integration challenges, and it maintained excellent performance even under varying energy conditions. In particular, AI algorithms were able to effectively manage different complex systems with several energy sources, where classical optimization would not work. It found that integrating AI would boost the performance and cost of renewable energy desalination plants in remote or arid regions.

Alnajdi et al. [\[43\]](#page-27-18) considered Adsorption Desorption Desalination (ADD) technology coupled with renewable energy sources for the potential creation of sustainable, decentralized water supplies. Centralized desalination plants, such as those in Saudi Arabia, rely heavily on burning fossil fuels, use significant amounts of energy, and need a lot of pipelines to transport water. Moreover, this approach is energy intensive and unsustainable in the long term. Alnajdi et al. [\[43\]](#page-27-18) assessed the feasibility of using ADD technology in a decentralized system. The low temperature of the heat source is a characteristic that makes ADD well suited for coupling to renewable energy. The authors compared ADD with the commonly used desalinization technology, seawater reverse osmosis (SWRO), and found ADD to be more energy efficient. Specifically, the energy consumption of piped and non-piped systems of four Saudi Arabia centralized desalination plants was analyzed. The energy consumption used for desalination in decentralized ADD systems was compared with those of centralized SWRO systems, resulting in an energy requirement for desalinaWater 2025, 17, 1169 19 of 28

tion of 4 to 1.38 kWh/m³ (65% reduction). Reductions in energy use and carbon emissions were due to the absence of long-distance water pipelines. Using AI for the desalination process via the ADD system, the team optimized the desalination process under local conditions and renewable energy availability. In addition to improving energy efficiency, it also improved the overall sustainability of water production in arid areas. The study showed that AI-enhanced ADD technology is a viable alternative for countries wishing to decentralize their water supply and reduce their ecological footprint. Table 6 shows a comparison of specific desalination systems.

<span id="page-18-0"></span>Table 6. Comparison of specific desalination systems.

| Technology                                  | Energy Consumption (kWh/m³) | CO <sub>2</sub> Emissions (kg/m <sup>3</sup> ) | Renewable Energy<br>Integration | AI Application              |
|---------------------------------------------|-----------------------------|------------------------------------------------|---------------------------------|-----------------------------|
| Seawater Reverse Osmosis (SWRO)             | 4.00                        | 0.75                                           | Moderate                        | Limited                     |
| Adsorption Desorption<br>Desalination (ADD) | 1.38                        | 0.25                                           | High                            | Extensive AI<br>Integration |
| Multi-Stage Flash (MSF)                     | 6.00                        | 1.25                                           | Low                             | Minimal                     |

In these case studies, it is shown how AI can be used to enhance the performance, energy consumption, and sustainability of desalination systems. For this type of case study, a hybrid desalination system powered by solar energy was studied with a feed flow rate of 10 m³/h, a salt concentration of 35,000 ppm, and operating temperatures of 25 °C for the evaporator and 15 °C for the condenser. AI is critical for controlling fluctuating supplies of energy in both renewable energy-powered and decentralized setups, as well as in optimizing desalination processes. Through the integration of intelligent control systems, forecasting models, and optimization algorithms, these studies indicate that AI has the potential to imbue a great deal of efficiency and reliability in desalination plants in arid regions suffering from water scarcity. Table 7 shows a detailed overview of AI Usage in water treatment facilities across Saudi Arabia, the USA, and China.

<span id="page-18-1"></span>**Table 7.** AI Usage in water treatment facilities.

| Location     | Capacity (m <sup>3</sup> /day) | AI Usage               | Reference |
|--------------|--------------------------------|------------------------|-----------|
| Saudi Arabia | 500,000                        | Predictive maintenance | [37]      |
| USA          | 100,000                        | Energy optimization    | [36]      |
| China        | 200,000                        | Fault detection        | [43]      |

#### 4.4. Analysis of Outcomes

#### 4.4.1. Reduction in Operational Costs

The reduction of operational costs is one of the most important benefits of using AI in desalination. AI optimizes processes and predicts when maintenance is necessary to make desalination plants function more efficiently and therefore reduces the total cost of producing water. Lowe et al. [44] and Chandra et al. [22] reported that AI-based process optimization has a significant impact on operational costs by saving energy and reducing chemical use.

#### 4.4.2. Enhancement in Process Efficiency

By fine-tuning the operating parameters in real time, AI improves the process efficiency, and the performance of the process, at lower resource consumption. This is even more important when the resource is scarce or the cost of energy is high. A practical application of this was observed in Australia, where AI was used to optimize the operation of a hybrid

*Water* **2025**, *17*, 1169 20 of 28

RO-distillation plant. This led to a significant increase in freshwater production and a noticeable reduction in energy consumption [\[43,](#page-27-18)[45\]](#page-27-20).

## 4.4.3. Environmental Impact

AI can also minimize the environmental impact of desalination. By reducing energy consumption and optimizing chemical use, AI technologies help lower the carbon footprint of desalination plants and decrease the harmful brine discharged into the ocean. Di Martino et al. [\[35\]](#page-27-10) demonstrated how AI-driven process optimization significantly reduced greenhouse gas emissions and mitigated the environmental impact of brine disposal.

Scholarly research on artificial intelligence (AI) has shown that it maximizes the desalination process on a global scale, in the USA, Europe, and China. Engineers from the Massachusetts Institute of Technology (MIT), in conjunction with Chinese researchers, have been able to develop a solar desalination system that relies on natural sunlight to heat the saltwater, cause evaporation, and then condense the resulting water into freshwater. The MIT News [\[3\]](#page-26-2) cites this innovative approach, which employs AI to improve the system's efficiency and potentially produce freshwater at a lower cost than traditional tap water.

The integration of AI and machine learning in desalination is already being achieved in Europe to determine the political areas where seawater desalination plants should be established. A research study on water resources shows that machine learning models could well forecast future sites for desalination facilities to assist strategic planning and the allocation of resources, as illustrated by Ai et al. [\[43\]](#page-27-18).

China, too, has advanced desalination technology. In the journal *Membranes*, a comprehensive review of China's desalination technologies was conducted, which focused on innovations to increase the efficiency and sustainability of water treatment processes, as illustrated by Ruan et al. [\[4\]](#page-26-3). Taken together, these studies highlight the important role of AI in the development of desalination technologies, which can change the world by solving the global water scarcity problem.

#### *4.5. Critical Assessment of Methodologies*

Different methodologies have been applied in using AI for desalination processes, such as predictive modeling, process optimization, and fault detection. These methods are effective but are not problem free.

Data requirements are one of the significant limitations. As with any of the water treatment processes, the primary application for AI techniques in desalination is in determining the training and validation datasets. Such data can be difficult to acquire, especially for new or small-scale desalination plants that may have a limited history of data.

The other limitation is that AI systems are computationally demanding. However, some AI techniques, i.e., deep learning or complex optimization, require a great amount of computational resources. There may be some limitations on their use in circumstances where resources are scarce.

The reliability and interpretability of AI models are finally critical. In critical operations such as desalination, the reliability of AI models is even more crucial. Furthermore, some AI models that have been used in desalination remain in the "black box", making it challenging to grasp or rely on the decision-making of those models, which might impede larger uptake.

## *4.6. Conclusions*

Desalination is a promising field in which AI application shows great potential to improve efficiency, decrease costs, and save the environment. Nevertheless, to achieve successful integration of AI in desalination, three challenges need to be overcome, which include data availability, computational demands, and model interpretability.

*Water* **2025**, *17*, 1169 21 of 28

The benefits of using AI in desalination are widely known, yet further research is needed on the use of AI to optimize desalination performance in the long term. Moreover, there is a need for studies on the deployment of AI in small scale or low-resource desalination settings, where its benefits could be more beneficial.

Future research should seek to design AI models with less need of data and computational power, which would make them more accessible to a greater number of desalination facilities. Additionally, the interpretability of AI models is crucial to be able to use them with confidence in critical desalination operations.

Finally, in summary, AI has great potential to change desalination; however, its mass adoption will have to address the current limitations and ensure that its benefits reach everyone. This research will fill the gap around these identified areas of research to explore new and more innovative applications of AI in mechanical engineering and specifically in desalination.

# **5. Comparative Analysis**

## *5.1. AI Applications in Water Treatment vs. Desalination*

This study finds that AI performs well in water treatment and desalination. Although these technologies are used differently in every process, the focus in the water treatment process is mainly on the optimization of processes. Included in this are adjustments in chemical dosages, monitoring the quality of the water, and prediction of possible process failures. For example, the data from sensors are analyzed using ML models in real time, so that operators can adjust their actions to increase the quality of the water and reduce chemical usage. It enhances efficiency and reduces costs.

On the other hand, AI is mostly used in desalination for predictive maintenance and energy management. Desalination is an energy-intensive process, particularly for methods such as RO. AI models predict when pumps and membranes are likely to fail, allowing maintenance to be performed proactively. This reduces downtime and extends equipment life, which is crucial for cost management. AI is also employed to optimize energy use, determining the most efficient means of operating the system under varying conditions. Table [8](#page-21-0) presents a comparative analysis of AI techniques used in desalination.

Several patterns emerged from the data. One notable observation is the clear correlation between the complexity of the AI technique used and the degree of improvement in efficiency and cost effectiveness. More advanced techniques, such as neural networks and GA, tend to yield higher savings but require more computational power and expertise to implement.

Another pattern is the difference in data types used in water treatment versus desalination. Water treatment systems rely on a broad range of data inputs, including chemical concentrations, flow rates, and water quality metrics. In contrast, desalination systems primarily focus on parameters related to membrane performance and energy use. This distinction in data types appears to influence the selection of AI techniques, with simpler models being more suitable for the diverse data of water treatment, while complex models, such as neural networks, are better suited to the high-volume, specialized data of desalination.

However, not all observations fit neatly into the patterns mentioned above. One notable anomaly is the occasional underperformance of AI models in smaller water treatment plants. In these cases, AI models did not deliver the expected cost or energy savings. Upon closer inspection, the limited availability of high-quality data in smaller plants was identified as a key issue. AI models, especially those relying on ML, require large amounts of high-quality data to function optimally. When data are scarce or of low quality, the models struggle, leading to less impressive results.

<span id="page-21-0"></span>*Water* **2025**, *17*, 1169 22 of 28

|                    | Table 8. Comparative analysis of AI techniques.                                                                                                                                                                                                                                                                                                                                                                                                                               |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AI Techniques      | In water treatment, the most commonly applied AI techniques were ML algorithms,<br>particularly support vector machines (SVMs) and decision trees (DTs). These methods were<br>employed to predict water quality outcomes based on historical data.<br>In desalination, neural networks and genetic algorithms (GAs) were more prevalent, primarily<br>used to optimize the performance of reverse osmosis (RO) membranes, which are critical to<br>the desalination process. |
| Outcomes           | In water treatment, AI models consistently demonstrated a 10–20% improvement in chemical<br>dosing accuracy, directly reducing costs and minimizing environmental impact. In<br>desalination, AI applications resulted in energy savings of up to 15% by optimizing membrane<br>operations and reducing the frequency of cleaning cycles.                                                                                                                                     |
| Energy efficiency  | AI in water treatment also helped reduce energy consumption by optimizing the operation of<br>pumps and other mechanical systems, leading to energy savings of approximately 5–10%.<br>Desalination, being more energy intensive, exhibited more significant energy savings, with<br>AI-driven optimizations cutting energy use by up to 20% in some cases.                                                                                                                   |
| Cost effectiveness | In water treatment, the overall cost reduction was approximately 10–15%, largely due to more<br>efficient chemical use and reduced energy consumption. The cost savings, however, were<br>more significant for desalination; depending on location, they were in the order of 15–25%;<br>most were attributed to reduced energy requirements and increased membrane life.                                                                                                     |

#### *5.2. Common Challenges and Limitations*

Despite the promise of AI applications in desalination, several hurdles need to be addressed. A common challenge in both fields is the quality of data. AI models are only as effective as the data they are trained on. In many studies, data issues were a recurring theme. Some systems operated with outdated sensors or incomplete data sets, leading to inaccuracies in the models. This is akin to trying to solve a puzzle with missing pieces, making it difficult to obtain a full picture.

Another challenge is the integration of AI into existing systems. Water treatment plants and desalination facilities often operate on legacy systems that were not designed with AI in mind. Retrofitting these systems to incorporate AI can be complex and costly. Additionally, operators must undergo training to effectively use AI-driven tools. While training is essential, it is often insufficient to ensure smooth implementation.

Scalability is another major issue. While AI has shown potential in pilot projects and small-scale studies, scaling these solutions to handle the demands of large water treatment or desalination plants remains a work in progress. The computational power and infrastructure needed to run AI models on a large scale can pose a barrier, particularly in regions with limited resources.

#### *5.3. Overall Impact on Energy Efficiency and Cost Effectiveness*

One of the most significant benefits of AI in water treatment and desalination is its potential to save energy and reduce costs. The data gathered in this review support this perspective, though with some caveats.

In water treatment, AI-driven process optimization has led to noticeable reductions in chemical and energy usage. By fine-tuning the treatment process in real time, AI enhances plant efficiency, resulting in lower operational costs. For example, one study found that a neural network model reduced chemical usage by 20% while maintaining water quality standards [\[46\]](#page-27-21). This represents a significant cost-saving and environmental benefit.

This trend is similarly evident in water treatment and desalination plants. AI-driven predictive maintenance has extended equipment lifespans and reduced the frequency of costly repairs. Energy management is another area where AI has made a significant impact. By optimizing the operation of pumps and other energy-intensive components, AI has

*Water* **2025**, *17*, 1169 23 of 28

helped reduce the overall energy consumption of water treatment and desalination plants. Some studies report energy savings of up to 15%, a noteworthy achievement given the energy-intensive nature of water treatment and desalination processes [\[35\]](#page-27-10).

However, while the data are promising, they are not definitive. Many of the studies reviewed were small-scale or pilot projects, and it remains uncertain whether these results can be replicated on a larger scale. Additionally, upfront costs for implementing AI solutions are an important consideration. The payback period can vary depending on specific circumstances.

# **6. Discussion**

#### *6.1. Interpretation of Findings*

In water treatment and desalination, AI has shown great promise in reducing costs, improving energy efficiency, and optimizing energy management, as well as overall efficiency. The data show that AI can achieve real-time process optimization, allow for the prediction of equipment failure, and support operators in making better decisions. These outcomes are in line with the main goals of improving water quality and making desalination more sustainable.

Nevertheless, some challenges should not be ignored. Issues such as data quality, system integration, and scalability are important and can make the difference between success and failure when AI is deployed in these fields. While the reviewed studies demonstrate that its implementation can bring impressive results, they also demonstrate that data quality, incompatibility in the system, and scalability issues can negatively impact AI's benefits.

## *6.2. Implications for the Field*

These findings are quite important for water treatment and desalination. This review provides a thorough discussion of how AI is currently being used in desalination, as well as how AI can help solve the world's water scarcity. This research provides some important information to enable engineers, researchers, and policymakers to use artificial intelligence systems for developing sustainable water management solutions. The benefits of AI can be brought to bear on these processes including cleaner water, lower operational costs, and more sustainable resource use. The significance of these advancements is heightened, given the growing world water scarcity issue.

However, the challenges indicate the fact that the path ahead is not going to be easy. Research in data quality and system integration is needed, along with efforts in related areas. However, these studies also suggest that for AI to deliver on its promise in these fields, it is going to need reliable data of high quality. In addition, scalability remains a challenge, and there is still research on how AI solutions can be expanded to scale and meet the needs of a large-scale operation.

Another implication is that collaboration is required. As AI is highly complex and its output will be used for desalination, success will depend on the involvement of several experts: data scientists, engineers, environmental scientists, and on-duty water treatment operators. These challenges must be overcome for AI to realize its full potential, and these problems necessitate this interdisciplinary approach.

#### *6.3. Potential for Future Research and Development*

Finally, several promising areas for further research and development in AI applications to water treatment and desalination are based on the results found.

1. Data quality improvement: Since AI models are highly data dependent, further research should be conducted to improve the data quality and reliability. The enhancements could be in the form of sensor technology improvement, better development of

*Water* **2025**, *17*, 1169 24 of 28

- cleaning algorithms of data, and the creation of the AI models that work well with imperfect data.
- 2. Scale studies: AI solutions have proved promising in small-scale studies; however, there still needs to be more exploration as to whether these solutions can be scaled to large-scale desalination plants. The studies should also not overlook the economic and logistical barriers to scaling, costs of scaling, and infrastructure requirements.
- 3. Challenges of integrating AI with legacy systems: Integration of AI into the existing system is a major challenge. The future research should be directed to developing strategies for smooth and economic integration. This could be designed in the form of middleware solutions to connect old technology to new technology or to build AI models that can work within the constraints of the legacy system.
- 4. AI and desalination, an environmental, economic, and social, as well as a technical challenge: Future research should focus on interdisciplinary collaboration, or collaboration among people who are experts in AI, environmental science, economics, and other fields. Thus, this may lead to more holistic solutions that incorporate energy requirements, chemical inputs, environmental impacts, and cost effectiveness.
- 5. Energy efficiency and environmental impact: In the face of the energy requirements of desalinization, there needs to be research on how AI can reduce energy use to the minimum and minimize its impact on the environment. That could include constructing AI models that have tunable parameters to optimize operations according to renewable energy availability and the possible side effects of waste products.
- 6. Regulatory and ethical issues: Even more research will be needed on how regulatory and ethical considerations will play out as AI becomes a more significant part of desalination. It might encompass exploring how to guarantee AI systems (i) are transparent (ii), accountable, and (iii) fair, and that (iv) data are protected when collecting and processing them.
- 7. A comprehensive cost–benefit analysis will be important for applying AI in desalination. In these studies, we can identify the most cost-effective AI implementations and also provide guidance on how to make the most of that investment.
- 8. Economic and scalability aspects of AI in desalination: For AI to become widely accepted in water treatment and desalination, both its economic performance and large-scale capability need assessment. AI becomes a profitable choice because its initial setup expenses result in enduring cost reductions regarding power usage and facility upkeep. The scalability challenges are related to the necessity of large datasets and computational resources, while cloud-based solutions and modular AI systems can tackle that.
- 9. Cybersecurity, training, and ease of use: Research investigating cybersecurity threats will be necessary because AI deployments in water treatment and desalination plants can face hacking risks. Water treatment and desalination require operator training along with AI interface development to ensure the successful adoption of AI technologies.

#### *6.4. Limitations of Current Studies and Gaps in the Literature*

While the findings are promising, there are notable limitations and gaps in the current body of research. Many studies were small-scale or case-specific, which indicates that they do not provide a comprehensive view of how AI will perform in diverse, real-world scenarios. There is a clear need for larger-scale studies to gain a broader perspective on AI's performance.

Another limitation is the lack of long-term data. AI is a relatively new technology in desalination, and many studies were conducted over short periods—typically months or a *Water* **2025**, *17*, 1169 25 of 28

few years. Long-term research is needed to understand how AI solutions affect equipment lifespan, maintenance costs, and overall sustainability.

There is also a gap in the literature concerning the social and ethical implications of AI in these fields. While the technical and economic aspects have been well explored, less attention has been paid to the impact of AI on the workers in water treatment and desalination, as well as the communities they serve. Future research should address these social considerations to ensure AI applications benefit society as a whole.

# **7. Conclusions**

This paper aimed to answer the research question: how has AI been utilized in desalination, and what are the outcomes? The key objectives were to review AI techniques, analyze their outcomes, and examine specific systems where AI has been applied.

First, we explored the AI techniques that are transforming desalination. Methods such as ML, neural networks, and GAs are driving improvements in predictive modeling, process optimization, and fault detection. AI models, for instance, can predict system failures before they occur, reducing downtime and improving overall reliability.

Second, we examined the outcomes of AI in these fields. The case studies revealed that AI contributes to reduced energy costs, enhanced efficiency, and improved water quality. Systems powered by renewable energy—such as solar or wind—benefit from AI's ability to manage energy supply variability, ensuring that water treatment and desalination processes run smoothly despite fluctuating conditions. Additionally, AI supports predictive maintenance, minimizing the likelihood of unexpected failures and maintenance costs. The integration of AI in water treatment and desalination systems powered by renewable energy further underscores its potential to lower energy consumption and reduce carbon footprints, which are critical outcomes, given the global energy crisis.

Finally, we reviewed specific water treatment and desalination systems where AI has been successfully incorporated. These include RO, MED, and adsorption–desorption desalination. AI techniques have optimized processes in these systems, improving operational reliability and energy efficiency. Each system faced unique challenges, but AI helped address them through smarter control systems, fault tolerance, and better forecasting of operational needs.

In answering the research question, it is evident that AI is already revolutionizing desalination. AI is transforming the management of these systems and enhancing the outcomes they deliver, such as reduced costs, increased reliability, and greater sustainability. Although challenges remain—particularly regarding scaling these solutions and managing their complexity—the potential for AI to further advance water treatment and desalination systems is significant.

Looking ahead, the future of AI in water treatment and desalination holds great promise. The implementation of AI in water treatment and desalination technology requires two main phases to reach widespread adoption by 2035: first, developing low-data AI models in 2025 and second, integrating AI with renewable energy systems by 2030. These objectives will make AI technologies accessible, sustainable, and scalable for addressing worldwide water scarcity problems. Continued innovation in AI techniques will likely lead to even more efficient and resilient systems. As technology advances, we can expect AI to become an integral component of global water management, offering solutions to growing water scarcity challenges while reducing environmental impacts. The results so far are promising, and the journey is just beginning.

**Author Contributions:** Conceptualization, A.A.; investigation, Y.A.; resources, Y.A.; supervision, A.A.; validation, A.A.; writing—original draft preparation, A.A.; writing—review and editing, A.A. and Y.A. All authors have read and agreed to the published version of the manuscript.

*Water* **2025**, *17*, 1169 26 of 28

**Funding:** This study received no external funding.

**Data Availability Statement:** The data that support the findings of this study are available from the corresponding author, A.A., upon request.

**Conflicts of Interest:** The authors declare no conflicts of interest.

# **Abbreviations**

ADD Adsorption Desorption Desalination AOPs Advanced Oxidation Processes

AI Artificial Intelligence ANNs Artificial Neural Networks BRR Bayesian Ridge Regression COD Chemical Oxygen Demand

PV Photovoltaic

R <sup>2</sup> Coefficient of Determination R Correlation Coefficient

DT Decision Trees

DNNs Deep Neural Networks DBPs Disinfection By-Products DSPM Donnan Steric Pore Model

ENP Extended Nernst-Planck Equation

GAs Genetic Algorithms

GA-ANN Genetic Algorithms Combined with Artificial Neural Networks

GTO Gorilla Troops Optimizer GWTD Groundwater Table Depth

ICA Imperialist Competition Algorithm

KNN K-Nearest Neighbors LCOW Levelized Cost of Water

LSSVM Least-squares support Vector Machine

ML Machine Learning MAE Mean Absolute Error MSE Mean Square Error

MCDI Membrane Capacitive Deionization

MPC Model Predictive Control

MINLP Mixed-Integer Nonlinear Optimization Problem MWOA Modified Whale Optimization Algorithm

MED Multi-Effect Distillation MSF Multi-Stage Flash MLP Multi-Layer Perceptron CD Optimal Dosage of Coagulants

OMLP Optimized Model

PLM Product Lifecycle Management

RF Random Forests RWP Raw Water Production RO Reverse Osmosis RMSE Root Mean Square Error SWRO Seawater Reverse Osmosis

SMGA Structured Messy Genetic Algorithm

SM Suspended Matter

SVM Support Vector Machines TDS Total Dissolved Solids WT Water Temperature

*Water* **2025**, *17*, 1169 27 of 28

WWTP Wastewater Treatment Plant O<sup>2</sup> Oxygen Levels

# **References**

<span id="page-26-0"></span>1. Omer, S. Global Water Crisis: Facts, FAQs, and How to Help. *World Vision*. 2025. Available online: [https://www.worldvision.com.](https://www.worldvision.com.au/global-water-crisis-facts?srsltid=AfmBOopQkj2iDpreh-N_KZ_u1g63rZwA3iSpOE8d3uW3VMB0HhzQLMG7) [au/global-water-crisis-facts?srsltid=AfmBOopQkj2iDpreh-N\\_KZ\\_u1g63rZwA3iSpOE8d3uW3VMB0HhzQLMG7](https://www.worldvision.com.au/global-water-crisis-facts?srsltid=AfmBOopQkj2iDpreh-N_KZ_u1g63rZwA3iSpOE8d3uW3VMB0HhzQLMG7) (accessed on 14 March 2025).

- <span id="page-26-1"></span>2. Ai, Z.; Ishihama, F.; Hanasaki, N. Mapping Current and Future Seawater Desalination Plants Globally Using Species Distribution Models. *Water Resour. Res.* **2022**, *58*, e2021WR031156. [\[CrossRef\]](https://doi.org/10.1029/2021WR031156)
- <span id="page-26-2"></span>3. Chu, J. Desalination System Could Produce Freshwater That Is Cheaper than Tap Water. Available online: [https://news.mit.edu/](https://news.mit.edu/2023/desalination-system-could-produce-freshwater-cheaper-0927) [2023/desalination-system-could-produce-freshwater-cheaper-0927](https://news.mit.edu/2023/desalination-system-could-produce-freshwater-cheaper-0927) (accessed on 14 March 2025).
- <span id="page-26-3"></span>4. Ruan, G.; Wang, M.; An, Z.; Xu, G.; Ge, Y.; Zhao, H. Progress and Perspectives of Desalination in China. *Membranes* **2021**, *11*, 206. [\[CrossRef\]](https://doi.org/10.3390/membranes11030206) [\[PubMed\]](https://www.ncbi.nlm.nih.gov/pubmed/33804227)
- <span id="page-26-4"></span>5. Gitis, V.; Hankins, N. Water Treatment Chemicals: Trends and Challenges. *J. Water Process Eng.* **2018**, *25*, 34–38. [\[CrossRef\]](https://doi.org/10.1016/j.jwpe.2018.06.003)
- <span id="page-26-5"></span>6. Darre, N.C.; Toor, G.S. Desalination of Water: A Review. *Curr. Pollut. Rep.* **2018**, *4*, 104–111. [\[CrossRef\]](https://doi.org/10.1007/s40726-018-0085-9)
- <span id="page-26-6"></span>7. Ghafoor, A.; Ahmed, T.; Munir, A.; Arslan, C.; Ahmad, S.A. Techno-Economic Feasibility of Solar Based Desalination through Reverse Osmosis. *Desalination* **2020**, *485*, 114464. [\[CrossRef\]](https://doi.org/10.1016/j.desal.2020.114464)
- 8. Chen, Z.; Li, J.; Zhou, J.; Chen, X. Photothermal Janus PPy-SiO2@PAN/F-SiO2@PVDF-HFP Membrane for High-Efficient, Low Energy and Stable Desalination through Solar Membrane Distillation. *Chem. Eng. J.* **2023**, *451*, 138473. [\[CrossRef\]](https://doi.org/10.1016/j.cej.2022.138473)
- <span id="page-26-7"></span>9. Shakib, S.E.; Amidpour, M.; Boghrati, M.; Ghafurian, M.M.; Esmaieli, A. New Approaches to Low Production Cost and Low Emissions through Hybrid MED-TVC+RO Desalination System Coupled to a Gas Turbine Cycle. *J. Clean. Prod.* **2021**, *295*, 126402. [\[CrossRef\]](https://doi.org/10.1016/j.jclepro.2021.126402)
- <span id="page-26-8"></span>10. Yadav, A.; Labhasetwar, P.K.; Shahi, V.K. Membrane Distillation Using Low-Grade Energy for Desalination: A Review. *J. Environ. Chem. Eng.* **2021**, *9*, 105818. [\[CrossRef\]](https://doi.org/10.1016/j.jece.2021.105818)
- 11. Panagopoulos, A.; Haralambous, K.-J. Environmental Impacts of Desalination and Brine Treatment Challenges and Mitigation Measures. *Mar. Pollut. Bull.* **2020**, *161*, 111773. [\[CrossRef\]](https://doi.org/10.1016/j.marpolbul.2020.111773)
- <span id="page-26-9"></span>12. Soliman, M.N.; Guen, F.Z.; Ahmed, S.A.; Saleem, H.; Khalil, M.J.; Zaidi, S.J. Energy Consumption and Environmental Impact Assessment of Desalination Plants and Brine Disposal Strategies. *Process Saf. Environ. Prot.* **2021**, *147*, 589–608. [\[CrossRef\]](https://doi.org/10.1016/j.psep.2020.12.038)
- <span id="page-26-10"></span>13. Herrera-León, S.; Cruz, C.; Negrete, M.; Chacana, J.; Cisternas, L.A.; Kraslawski, A. Impact of Seawater Desalination and Wastewater Treatment on Water Stress Levels and Greenhouse Gas Emissions: The Case of Chile. *Sci. Total Environ.* **2022**, *818*, 151853. [\[CrossRef\]](https://doi.org/10.1016/j.scitotenv.2021.151853) [\[PubMed\]](https://www.ncbi.nlm.nih.gov/pubmed/34822892)
- <span id="page-26-11"></span>14. Zhang, J.; Zhan, Z.; Lin, Y.; Chen, N.; Gong, Y.; Zhong, J.; Chung, H.S.H.; Li, Y.; Shi, Y. Evolutionary Computation Meets Machine Learning: A Survey. *IEEE Comput. Intell. Mag.* **2011**, *6*, 68–75. [\[CrossRef\]](https://doi.org/10.1109/MCI.2011.942584)
- <span id="page-26-12"></span>15. Lowe, M.; Qin, R.; Mao, X. A Review on Machine Learning, Artificial Intelligence, and Smart Technology in Water Treatment and Monitoring. *Water* **2022**, *14*, 1384. [\[CrossRef\]](https://doi.org/10.3390/w14091384)
- <span id="page-26-13"></span>16. Bhagat, S.K.; Pyrgaki, K.; Salih, S.Q.; Tiyasha, T.; Beyaztas, U.; Shahid, S.; Yaseen, Z.M. Prediction of Copper Ions Adsorption by Attapulgite Adsorbent Using Tuned-Artificial Intelligence Model. *Chemosphere* **2021**, *276*, 130162. [\[CrossRef\]](https://doi.org/10.1016/j.chemosphere.2021.130162)
- <span id="page-26-14"></span>17. Sundui, B.; Ramirez Calderon, O.A.; Abdeldayem, O.M.; Lázaro-Gil, J.; Rene, E.R.; Sambuu, U. Applications of Machine Learning Algorithms for Biological Wastewater Treatment: Updates and Perspectives. *Clean Technol. Environ. Policy* **2021**, *23*, 127–143. [\[CrossRef\]](https://doi.org/10.1007/s10098-020-01993-x)
- <span id="page-26-15"></span>18. Li, L.; Rong, S.; Wang, R.; Yu, S. Recent Advances in Artificial Intelligence and Machine Learning for Nonlinear Relationship Analysis and Process Control in Drinking Water Treatment: A Review. *Chem. Eng. J.* **2021**, *405*, 126673. [\[CrossRef\]](https://doi.org/10.1016/j.cej.2020.126673)
- <span id="page-26-16"></span>19. Wang, G.; Jia, Q.-S.; Zhou, M.; Bi, J.; Qiao, J.; Abusorrah, A. Artificial Neural Networks for Water Quality Soft-Sensing in Wastewater Treatment: A Review. *Artif. Intell. Rev.* **2022**, *55*, 565–587. [\[CrossRef\]](https://doi.org/10.1007/s10462-021-10038-8)
- <span id="page-26-17"></span>20. Khataee, A.R.; Kasiri, M.B. Artificial Neural Networks Modeling of Contaminated Water Treatment Processes by Homogeneous and Heterogeneous Nanocatalysis. *J. Mol. Catal. A Chem.* **2010**, *331*, 86–100. [\[CrossRef\]](https://doi.org/10.1016/j.molcata.2010.07.016)
- <span id="page-26-18"></span>21. Matheri, A.N.; Ntuli, F.; Ngila, J.C.; Seodigeng, T.; Zvinowanda, C. Performance Prediction of Trace Metals and Cod in Wastewater Treatment Using Artificial Neural Network. *Comput. Chem. Eng.* **2021**, *149*, 107308. [\[CrossRef\]](https://doi.org/10.1016/j.compchemeng.2021.107308)
- <span id="page-26-19"></span>22. Kulisz, M.; Kujawska, J.; Przysucha, B.; Cel, W. Forecasting Water Quality Index in Groundwater Using Artificial Neural Network. *Energies* **2021**, *14*, 5875. [\[CrossRef\]](https://doi.org/10.3390/en14185875)
- <span id="page-26-20"></span>23. Chandra, P.; Mudgal, A.; Patel, J.; Patel, V.K. Thermo-Economical Modeling and Multi-Objective Optimization of Thermal Energy Driven Multiple Effect Distillation System for Water Treatment Using NSGA-II Algorithm. *Desalination Water Treat.* **2024**, *320*, 100646. [\[CrossRef\]](https://doi.org/10.1016/j.dwt.2024.100646)
- <span id="page-26-21"></span>24. Walters, G.A.; Savic, D.A. Optimal Design of Water Systems Using Genetic Algorithms and Other Evolution Programs. *Trans. Ecol. Environ.* **1994**, *7*. [\[CrossRef\]](https://doi.org/10.2495/HY940021)

*Water* **2025**, *17*, 1169 28 of 28

<span id="page-27-0"></span>25. Tao, Y.; Yan, D.; Yang, H.; Ma, L.; Kou, C. Multi-Objective Optimization of Water Distribution Networks Based on Non-Dominated Sequencing Genetic Algorithm. *PLoS ONE* **2022**, *17*, e0277954. [\[CrossRef\]](https://doi.org/10.1371/journal.pone.0277954) [\[PubMed\]](https://www.ncbi.nlm.nih.gov/pubmed/36441704)

- <span id="page-27-1"></span>26. Pandey, K.; Kumar, S.; Malik, A.; Kuriqi, A. Artificial Neural Network Optimized with a Genetic Algorithm for Seasonal Groundwater Table Depth Prediction in Uttar Pradesh, India. *Sustainability* **2020**, *12*, 8932. [\[CrossRef\]](https://doi.org/10.3390/su12218932)
- <span id="page-27-2"></span>27. Bahiraei, M.; Nazari, S.; Moayedi, H.; Safarzadeh, H. Using Neural Network Optimized by Imperialist Competition Method and Genetic Algorithm to Predict Water Productivity of a Nanofluid-Based Solar Still Equipped with Thermoelectric Modules. *Powder Technol.* **2020**, *366*, 571–586. [\[CrossRef\]](https://doi.org/10.1016/j.powtec.2020.02.055)
- <span id="page-27-3"></span>28. Halhal, D.; Walters, G.A.; Savic, D.A.; Ouazar, D. Scheduling of Water Distribution System Rehabilitation Using Structured Messy Genetic Algorithms. *Evol. Comput.* **1999**, *7*, 311–329. [\[CrossRef\]](https://doi.org/10.1162/evco.1999.7.3.311)
- <span id="page-27-4"></span>29. Bhoi, S.K.; Mallick, C.; Mohanty, C.R. Estimating the Water Quality Class of a Major Irrigation Canal in Odisha, India: A Supervised Machine Learning Approach. *Nat. Environ. Pollut. Technol.* **2022**, *21*, 433–446. [\[CrossRef\]](https://doi.org/10.46488/NEPT.2022.v21i02.002)
- <span id="page-27-5"></span>30. Achite, M.; Farzin, S.; Elshaboury, N.; Valikhan Anaraki, M.; Amamra, M.; Toubal, A.K. Modeling the Optimal Dosage of Coagulants in Water Treatment Plants Using Various Machine Learning Models. *Environ. Dev. Sustain.* **2024**, *26*, 3395–3421. [\[CrossRef\]](https://doi.org/10.1007/s10668-022-02835-0)
- <span id="page-27-6"></span>31. Djebedjian, B.; Gad, H.; Khaled, I.; Rayan, M.M.A. Experimental and Analytical Study of a Reverse Osmosis Desalination Plant. *Mansoura Eng. J.* **2020**, *34*, 71–92. [\[CrossRef\]](https://doi.org/10.21608/bfemu.2020.126197)
- <span id="page-27-7"></span>32. Mulyawan, R.; Muarif, A. A Review Of Reverse Osmosis Membrane Fouling: Formation and Control. *Int. J. Eng. Sci. Inf. Technol.* **2021**, *1*, 110–115. [\[CrossRef\]](https://doi.org/10.52088/ijesty.v1i3.127)
- <span id="page-27-8"></span>33. Qadir, D.; Idris, A.; Nasir, R.; Abdul Mannan, H.; Sharif, R.; Mukhtar, H. Prediction of Single Salt Rejection in PES/CMS Based Membranes. *Chemosphere* **2023**, *311*, 136987. [\[CrossRef\]](https://doi.org/10.1016/j.chemosphere.2022.136987)
- <span id="page-27-9"></span>34. Salem, H.; Kabeel, A.E.; El-Said, E.M.S.; Elzeki, O.M. Predictive Modelling for Solar Power-Driven Hybrid Desalination System Using Artificial Neural Network Regression with Adam Optimization. *Desalination* **2022**, *522*, 115411. [\[CrossRef\]](https://doi.org/10.1016/j.desal.2021.115411)
- <span id="page-27-10"></span>35. Mahadeva, R.; Kumar, M.; Gupta, V.; Manik, G.; Patole, S.P. Modified Whale Optimization Algorithm Based ANN: A Novel Predictive Model for RO Desalination Plant. *Sci. Rep.* **2023**, *13*, 2901. [\[CrossRef\]](https://doi.org/10.1038/s41598-023-30099-9) [\[PubMed\]](https://www.ncbi.nlm.nih.gov/pubmed/36807398)
- <span id="page-27-11"></span>36. Di Martino, M.; Avraamidou, S.; Cook, J.; Pistikopoulos, E.N. An Optimization Framework for the Design of Reverse Osmosis Desalination Plants under Food-Energy-Water Nexus Considerations. *Desalination* **2021**, *503*, 114937. [\[CrossRef\]](https://doi.org/10.1016/j.desal.2021.114937)
- <span id="page-27-12"></span>37. AL-Rajabi, M.M.; Abumadi, F.A.; Laoui, T.; Atieh, M.A.; Khalil, K.A. Capacitive Deionization for Water Desalination: Cost Analysis, Recent Advances, and Process Optimization. *J. Water Process Eng.* **2024**, *58*, 104816. [\[CrossRef\]](https://doi.org/10.1016/j.jwpe.2024.104816)
- <span id="page-27-13"></span>38. Shin, Y.-U.; Lim, J.; Boo, C.; Hong, S. Improving the Feasibility and Applicability of Flow-Electrode Capacitive Deionization (FCDI): Review of Process Optimization and Energy Efficiency. *Desalination* **2021**, *502*, 114930. [\[CrossRef\]](https://doi.org/10.1016/j.desal.2021.114930)
- <span id="page-27-14"></span>39. Said, A.M.; Sihem, K. Methodology for Monitoring and Diagnosing Faults of Hybrid Dynamic Systems: A Case Study on a Desalination Plant. *Diagnostyka* **2020**, *21*, 27–33. [\[CrossRef\]](https://doi.org/10.29354/diag/116076)
- <span id="page-27-15"></span>40. Mehrad, R.; Kargar, S.M. Integrated Model Predictive Fault-Tolerant Control, and Fault Detection Based on the Parity Space Approach for a Reverse Osmosis Desalination Unit. *Trans. Inst. Meas. Control* **2020**, *42*, 1882–1894. [\[CrossRef\]](https://doi.org/10.1177/0142331219898942)
- <span id="page-27-16"></span>41. Saidy, C.; Valappil, S.P.; Matthews, R.M.; Bayoumi, A. Development of a Predictive Maintenance 4.0 Platform: Enhancing Product Design and Manufacturing. *Adv. Asset Manag. Cond. Monit.* **2020**, *166*, 1039–1049. [\[CrossRef\]](https://doi.org/10.1007/978-3-030-57745-2_86)
- <span id="page-27-17"></span>42. Sayed, E.T.; Olabi, A.G.; Elsaid, K.; Al Radi, M.; Semeraro, C.; Doranehgard, M.H.; Eltayeb, M.E.; Abdelkareem, M.A. Application of Artificial Intelligence Techniques for Modeling, Optimizing, and Controlling Desalination Systems Powered by Renewable Energy Resources. *J. Clean. Prod.* **2023**, *413*, 137486. [\[CrossRef\]](https://doi.org/10.1016/j.jclepro.2023.137486)
- <span id="page-27-18"></span>43. Alnajdi, O.; Wu, Y.; Kaiser Calautit, J. Toward a Sustainable Decentralized Water Supply: Review of Adsorption Desorption Desalination (ADD) and Current Technologies: Saudi Arabia (SA) as a Case Study. *Water* **2020**, *12*, 1111. [\[CrossRef\]](https://doi.org/10.3390/w12041111)
- <span id="page-27-19"></span>44. Ai, C.; Zhao, L.; Song, D.; Han, M.; Shan, Q.; Liu, S. Identifying Greenhouse Gas Emission Reduction Potentials through Large-Scale Photovoltaic-Driven Seawater Desalination. *Sci. Total Environ.* **2023**, *857*, 159402. [\[CrossRef\]](https://doi.org/10.1016/j.scitotenv.2022.159402) [\[PubMed\]](https://www.ncbi.nlm.nih.gov/pubmed/36240922)
- <span id="page-27-20"></span>45. Prajapati, M.; Shah, M.; Soni, B. A Comprehensive Review of the Geothermal Integrated Multi-Effect Distillation (MED) Desalination and Its Advancements. *Groundw. Sustain. Dev.* **2022**, *19*, 100808. [\[CrossRef\]](https://doi.org/10.1016/j.gsd.2022.100808)
- <span id="page-27-21"></span>46. Khan, Q.; Maraqa, M.A.; Mohamed, A.-M.O. Chapter 17—Inland Desalination: Techniques, Brine Management, and Environmental Concerns. In *Pollution Assessment for Sustainable Practices in Applied Sciences and Engineering*; Mohamed, A.-M.O., Paleologos, E.K., Howari, F.M., Eds.; Butterworth-Heinemann: Oxford, UK, 2021; pp. 871–918. ISBN 978-0-12-809582-9.

**Disclaimer/Publisher's Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.
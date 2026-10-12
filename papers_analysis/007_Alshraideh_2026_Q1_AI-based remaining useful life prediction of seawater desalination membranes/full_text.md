Contents lists available at [ScienceDirect](www.sciencedirect.com/science/journal/26668211)

# Chemical Engineering Journal Advances

journal homepage: [www.sciencedirect.com/journal/chemical-engineering-journal-advances](https://www.sciencedirect.com/journal/chemical-engineering-journal-advances)

![](_page_0_Picture_5.jpeg)

![](_page_0_Picture_6.jpeg)

# AI-based remaining useful life prediction of seawater desalination membranes

Hussam Alshraideh a,b,\* , Fajer Al Ali <sup>c</sup> , Mahmoud Awad <sup>a</sup> [,](https://orcid.org/0000-0003-2999-9084) Amani Al-Othman d,e

- <sup>a</sup> *Department of Industrial Engineering, American University of Sharjah, Sharjah, United Arab Emirates*
- <sup>b</sup> *Industrial Engineering Department, Jordan University of Science and Technology, Irbid 22110, Jordan*
- <sup>c</sup> *Engineering Systems Management, Department of Industrial Engineering, American University of Sharjah, Sharjah, United Arab Emirates*
- <sup>d</sup> *Department of Chemical and Biological Engineering, American University of Sharjah, PO. Box 26666, Sharjah, United Arab Emirates*
- <sup>e</sup> *Energy, Water and Sustainable Environment research center, college of Engineering, American University of Sharjah, PO. Box 26666, Sharjah, United Arab Emirates*

### ARTICLE INFO

#### *Keywords:* Reverse osmosis Predictive modelling Remaining useful life Clean-in-place Desalination

#### ABSTRACT

Remaining Useful Life (RUL) of Reverse Osmosis (RO) membranes is defined as the anticipated time until the RO membrane reaches a specified performance threshold, triggering maintenance actions to enhance system longevity and efficiency. We propose an artificial intelligence-based predictive model for modelling and estimating the RUL of RO membranes. Literature on the prediction of RUL for RO membranes is limited, solely based on historical water production data and does not incorporate operational conditions and parameters. We consider a detailed list of sensor and laboratory based system operational parameters such as Silt Density Index (SDI), water temperature, pump speed, and the water production history at the different stages of the desalination process to model and predict the membranes RUL. A case study from a local RO plant in the UAE is used to demonstrate the proposed work. Four machine learning based predictive models were examined. Random Forest algorithm demonstrated the best performance, achieving R² of 0.984, RMSE of 0.136, and MAE of 0.0997 indicating exceptional RUL prediction performance. SHapley Additive exPlanations (SHAP) importance analysis identified SDI, water temperature, pump speed, and the membrane age as the top RUL influential parameters. Understanding these key variables can provide valuable insights into optimizing operational conditions, thus extending membrane lifespan. Implementation of this AI-driven model optimizes clean-in-place scheduling maximizing the longevity and performance of membranes. Findings enhance the understanding of necessary operating conditions for effective seawater treatment and contribute to the broader literature on predictive maintenance in desalination, supporting more efficient and sustainable water production practices.

# **1. Introduction**

The increasing population is an issue that has put significant pressure on accessing and using clean water. The unreliability of the natural resources providing fresh water because of the overuse of water resources and human contamination has exacerbated this problem. The UAE experiences the issue as well. According to Alaa et al [\[1\]](#page-11-0) apart from the UAE's water scarcity and contamination, the region has relied heavily on non-conventional resources [\[1\]](#page-11-0). Desalination plays a crucial role in addressing freshwater scarcity by providing an essential source of water through water treatment plants, especially in regions with inadequate natural water resources. Electricity demand in the Gulf Cooperation Council (GCC) countries, including the UAE, is driven by sectors like

water desalination, air-conditioning, and lighting. While fossil fuels currently dominate power generation, efforts are underway to transition to cleaner energy sources like renewables. Seawater desalination, a critical process for meeting water needs, contributes significantly to electricity consumption, especially with rising demand. A rise in the water consumption has made treatment and management strategies crucial in the UAE to meet water demand among its population. Water resources in the UAE comprise both conventional (surface runoff, springs, groundwater) and non-conventional resources such as desalinated and treated sewage water. The motivation behind increasing desalination capacity stems from seawater availability and attractive tactics to meet water demand at a favourable cost as industries have shown willingness and ability to establish plants that utilize

<https://doi.org/10.1016/j.ceja.2026.101217>

<sup>\*</sup> Corresponding author: American University of Sharjah, Sharjah, United Arab Emirates. *E-mail address:* [halshraideh@aus.edu](mailto:halshraideh@aus.edu) (H. Alshraideh).

technologies to address the freshwater scarcity issue. Since the early 1970s, UAE has expanded non-conventional water resource management to bridge the gap between resources and population demand a normal practice [\[2\]](#page-11-0). Thus, UAE must maintain the ability to establish desalination plants and guarantee their resilience for water productivity and electricity generation.

The UAE combined cycle power plants use RO processes for water desalination and electricity generation. The significance of this procedure, especially through RO membranes, cannot be overemphasized since RO has become a preferred method for desalination due to its lower energy requirements [\[3\]](#page-11-0). RO is favoured for desalination due to its energy efficiency, scalability, high salt rejection, and versatility in removing contaminants. Continuous technological advancements further enhance its appeal as a preferred method for producing clean and safe drinking water from various sources. The RO pre-treatment process is an integrated technology that allows simultaneous water treatment and production of electricity in reduced time and lower energy consumption [[3](#page-11-0)]. The description pinpoints the significance of promoting the performance of RO membrane to prevent it from potential damage. The significance of promoting the performance of RO membranes lies in mitigating potential damage, particularly fouling, which can significantly impair their efficiency and lifespan. Addressing fouling issues is crucial for ensuring optimal operation and longevity of the membrane system. Further, the evidence suggests that RO membrane is the preferred technology in the UAE due to its effectiveness in desalinating water efficiently and successfully [\[4\]](#page-11-0). The preference for RO membrane technology in the UAE is largely attributed to its effectiveness in efficiently desalinating water while meeting stringent purity standards and minimizing energy requirements. This technology offers a cost-effective and sustainable solution for addressing water scarcity challenges in the region. Thus, the inclination to maximize its utilization is vital since the plant has a clean-in-place (CIP) procedure, a cleaning procedure for the RO membranes. In the principle underpinning the membrane process, the key mechanism is the selective passage of particles. The process is pressure-driven, hence requiring controlling the accumulation of particles to enforce their transportation via the membranes against the potential chemical gradient [[5](#page-11-0)]. Fig. 1 shows a typical RO system. A typical (RO) system comprises several key components: a pre-filter, a semipermeable membrane, a pressurization mechanism, a post-filter, and a storage tank. The process begins as water flows through the pre-filter, removing sediments, chlorine, and other contaminants. Then, pressurized water is forced through the semipermeable membrane, where only pure water molecules can pass through, leaving behind impurities. These impurities are diverted to the drain, while the purified water continues to the post-filter, which removes any remaining tastes or odours. Finally, the clean water is stored in a tank until it's needed. This method ensures efficient removal of contaminants, providing safe and clean drinking water for various applications.

The opportunities for desalinated water reuse should accompany efficiency in clean-in-place (CIP) optimization and scheduling. Moreover, plants should demonstrate value in terms of cost-effectiveness to meet user-end needs [\[7\]](#page-11-0). Thus, the RO membrane system should align with reliable CIP procedures to prevent membranes damage. Research can assess strategies to limit the accumulation of particles that lead to clogging. Building a predictive model provides a practical solution to this problem, helping plants predict pressure increase and hence the need for a CIP to optimize cleaning schedules. Machine learning and artificial intelligence methods has been extensively applied in the field of water desalination including the recent work of Alanazi et al[\[8\]](#page-11-0) and Ashraf et al [[9](#page-11-0)] that demonstrate superior performance of these models in designing and modelling the performance of desalination systems. A complete review of artificial intelligence models in water treatment and desalination is provided in the work of Alenezi et al [[10\]](#page-11-0). To the authors knowledge, no current work exists in the literature that addresses the prediction of the remaining useful life (RUL) of RO membranes. Novelity and contribution of this work is twofold: first, we propose an Artificial Intelligence (AI) based prediction framework to model the RUL of RO membranes; second, unlike existing literature that relies solely on laboratory results data to model and analyze CIP procedure, we combine full system operational features along with laboratory results to test and validate the proposed RUL prediction model. A case study of a local UAE seawater desalination plant is used to demonstrate the work proposed.

The rest of the papers is organized as follows. Section 2 provides a review of the related literature. In [Section 3,](#page-3-0) we discuss the proposed work methodology. Modelling and analysis results are presented and discussed in [Section 4](#page-4-0). Conclusions are provided in [Section 5](#page-8-0).

#### **2. Literature review**

The surveyed literature is organised around membrane failure mechanism, maintenance practices, and predictive models.

#### *2.1. RO membrane fouling*

Membrane-based technologies in water desalination are promising technologies but fouling limits their efficiency in improving the separation process. According to [\[11](#page-11-0)], fouling is the "deposition and accumulation of undesired materials on the surface of or inside a given host

![](_page_1_Picture_11.jpeg)

**Fig. 1.** Stages of a typical RO water desalination system, adopted from [\[6](#page-11-0)].

material such as membranes, heat exchangers, and boilers". From this perspective, it is vital that membrane-based processes integrate complexity in terms of chemical reactions since the surface of the membrane and the feed elements limit the operational efficiency of the system. The problem becomes complicated during the desalination process. The general lifespan of RO membranes typically lasts between 2 and 7 years. However, with proper maintenance and under ideal conditions, some membranes can last up to 10 years or more [[11\]](#page-11-0). Results from the study done by Eltanbouly et al [\[12](#page-11-0)], present a data-driven approach to predict the RUL of the membrane, identifying fouling as a reason that reduces the system's safety threshold. The membrane cleaning procedure can hinder its output, which is attributed to the distorted operating conditions. The immediate outcome of disrupted membrane plant operation is shortened membrane life [[12\]](#page-11-0). A solution to addressing this issue has been proposed in the form of anti-fouling surface-patterned membranes. In this context, the study by Ibrahim and Hilal, investigated the suitability of the surface-patterned membranes to improve the spacer-assisted filtration process and used diamond- and honeycomb-fabricated surface-patterned membranes [\[13](#page-11-0)]. The results reveal that the membranes are effective during the filtration process compared to the conventional feed spacer-assisted filtration in terms of higher permeability and anti-fouling operations. These findings affirm that the configuration of a membrane system remains a crucial factor in its performance based on the employed fabrication technique.

Evidence suggests that the lifespan of the RO membrane possesses antifouling and material properties that forecast the filtration cycle pattern. As indicated in [[14\]](#page-11-0), the desalination performance of RO membranes can be improved by using nano reinforcing materials since they show great suitability when synthesized in the preparation of nanocomposite aromatic polyamide and crystalline cellulose nanofiber membranes. These materials provide enhanced durability and antifouling resistance, thereby extending membrane lifespan and improving operational stability. The utilization of nano reinforcing materials enhances the desalination performance of RO membranes by augmenting their structural integrity and surface properties. This improvement is achieved through the incorporation of nanocomposite aromatic polyamide and crystalline cellulose nanofiber membranes, which exhibit increased durability and resistance to fouling, thereby ensuring prolonged membrane lifespan and sustained antifouling capabilities. Different methods of intensifying the performance of RO membranes indicate that a combination of factors increases the implementation of this desalination technique. Similarly, in the assessment of various processes to increase the useful life and reuse of the RO membrane elements, it is determined that different components are integrated with the physical fouling to boost the technical and operational features of the system in its life cycle [\[15](#page-11-0)]. The research trends on the proper selection of materials for desalination plants underscore the relationship between corrosion resistance and the smooth operations of desalination industries. A literature analysis of desalination trends identified that RO (27%) is the most explored desalination technique when compared to renewable energy desalination (26%), thermal desalination (14%), brine (14%), electrodialysis (8%), and membrane distillation (7%) [\[16](#page-11-0)]. The higher proportion of RO is associated with the critical importance of selecting materials that enhance efficiency and improve the opportunity to address the water salinity problem.

Existing academic literature reviews the parameters and contexts leading to the accumulation of particles in the RO membranes, thus hindering its efficiency and longevity. A review [[17\]](#page-11-0) explained the main factors contributing to the formation and development of particles and biological foulants and outlined corresponding mitigation strategies to address RO membrane fouling. This review is grounded in evidence showing that fouling caused by physicochemical reactions between membrane materials and water pollutants leads to the build-up of particles on the membrane surface or within its pores, lowering the efficiency of RO membranes. Similarly, a state-of-the-art review [\[18](#page-11-0)] identified the key operational parameters such as flux decline, increased

feed pressure, and varied fouling types (biological fouling and organic fouling) to curtail the operations of the RO membrane system. The analysis provides a comprehensive conclusion about the improvements in brine management and developing membranes integrating chlorine resistance and specific contaminants. Furthermore, crucial factors behind the accumulation of particles include cleaning protocols, feed water quality, operating conditions, and membrane characteristics [\[18](#page-11-0)]. Moreover, another review analyzed relevant literature concerning the usage of artificial neural networks focusing on the application of AI-based fouling prediction models to improve membrane fouling forecast [\[19](#page-11-0)]. In the paper, it is determined that artificial neural networks have great potential to optimize membrane-based procedures since they identify the underlying complex chemical reactions and physical processes in membrane fouling. Consequently, there is a need to strengthen awareness of desalination maintenance practices that effectively reduce membrane fouling and extend the useful life of the RO membrane's system.

# *2.2. RO membrane maintenance practices*

The maintenance practices of the RO membrane system primarily revolve around CIP procedures. The technique is defined as an automated cleaning protocol meant for the removal of undesirable deposits on equipment surface, such as organic fouling and scaling, using various solution types, such as acid and sanitizer, as cleaning agents. These processes illustrate CIP as an intensive industrial method for rinsing off varied effluents for sustainable wastewater treatment [\[20](#page-11-0)]. Proper and successful CIP practices ensure efficient operations and maintenance. In preserving the functional ability of the RO membrane system, CIP procedures are employed to extend the membrane's longevity by optimizing the performance of the system. Table 1 provides an overview of the main processes and functions of a typical RO plant CIP protocol.

The efficiency of RO membrane maintenance practices is well explained through typical CIP protocols. A comparison between CIP efficacy in lab-scale and full-scale RO investigated the suitability of laboratory and industrial membrane system pretreatment [\[22](#page-11-0)]. A significant difference between full-scale (9–20%) and lab-scale (~50%) was apparent. The disparity is explained by reviewing the results from the membrane fouling simulator in the lab-scale biofilms, which has a richness in polysaccharide ratio of 0.5, compared to the lab-scale membrane fouling simulator, which has full-scale modules containing polysaccharide ratio of 2.2. It is concluded that the development of CIP protocols should use synthetic feed water and fouling layers fabricated within a short period [\[22](#page-11-0)]. The relevance of CIP procedures in RO membrane systems cannot be overemphasized since they are crucial in ensuring ideal operational conditions. Moreover, a study [[23\]](#page-11-0) was performed at the Mahou-San Miguel brewing plant situated in Alovera, Spain to investigate the efficacy of CIP procedures to assist in restoring the permeability of the RO membrane system. The CIP protocol consisted of high-pressure backwash and soaking of sodium hypochlorite and hydrochloric acid dosing at 13% and 33%, respectively. The microfiltration membrane integrated sodium hypochlorite up to 3000 ppm and hydrochloric acid at 5%. Results revealed the effectiveness of using sodium hypochlorite as a cleaning agent since it restored

**Table 1**  A typical RO plant CIP process [\[21](#page-11-0)].

| Process                      | Function                                                                                                                       |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Pre-rinse<br>Low pH cleaning | Displacing feedwater and confirming the CIP flow path<br>Removing organic and biological materials from the membrane<br>system |
| High pH<br>cleaning          | Removing foulants from the membrane system                                                                                     |
| Final rinse<br>Quality rinse | Removing all cleaning chemicals<br>Confirming the product quality is within suitable operating<br>conditions                   |

<span id="page-3-0"></span>permeability within a range of 50–120% while eliminating organic matter and removed inorganic depositions, although the process incurred a high chemical cost. The inference made in these accounts implies that various parameters other than materials and costs are considered when ideal operation conditions for a CIP should be achieved for efficiency and performance.

However, a study [[24\]](#page-11-0) that assessed the efficacy of CIP protocols on whey RO membranes provided varying findings. It consisted of experiments conducted using four replicates. These results revealed that the tested CIP protocol showed limited effectiveness in cleaning membrane biofilms in the whey RO membranes. Apparently, the conditions for cleaning RO membranes necessitate combining effective CIP procedures and the use of proper materials. The claim is affirmed by a review [\[25](#page-11-0)] that summarizes CIP practices in mitigating organic fouling when using ceramic membranes in processing liquids of organic origin. Therefore, the paper recommended sodium hydroxide, strong oxidants, or acids as efficient options in cleaning irreversible fouling treatment. The RO desalination pre-treatment should be optimized in such a manner that it does not affect the filtration performance. The assertion is associated with an explanation made in the study [\[26](#page-11-0)], which identifies that membrane cleaning procedure comprises the optimization of key operational parameters, the cost-effectiveness, and sustainability of the filtration operations to remove reversible fouling through chemical cleaning so as without impairing filtration. Thus, the underlying and most practical conditions for the cleaning efficiency of CIP have been explained. In their study, [\[27](#page-11-0)] clarified that evidence was required from a practical standpoint and a scientific view to expound on the underlying regulating mechanism for long-term CIP fouling control strategy in RO membranes. Thus, for improved RO operation sustainability to mitigate fouling, the selection of CIP procedures should manifest feasibility and sustainability.

### *2.3. Remaining useful life predictive modelling*

Despite its importance, very few research studies have focused on the application of RUL concepts to RO membranes. Existing studies have explored various opportunities and challenges of RUL predictive models in promoting reliability and accuracy by utilizing collected data sets. Li et al. presented a deep learning-based RUL predictive modelling on RO membranes emphasizing weighted sequence data and proposed a method to improve accuracy and efficiency in the practical use of the distributed mechanism [\[27](#page-11-0)]. The context of the experiment encompassed the extraction of time series based on a verified commercial modular aero-propulsion system simulation (C-MAPSS) data set. The results show that the proposed method consisting of the integration of industrial sensors weights and time steps, demonstrated high accuracy and sustained efficiency in practical applications. The development of an advanced analytical procedure using RUL boosts optimality in maintenance practices. Thus, researchers [\[28](#page-11-0)] developed a novel analytical procedure that estimated the RUL of complex industrial facilities based on degradation data collected over time. They proposed an extended prognostic model to predict RUL in terms of maintenance aspects of partially repaired units. With the artificial neural network method, the RUL predictive model process was shown to yield low-cost prognostics, hence making the procedure effective in high-risk facilities since it assists in establishing optimality and satisfying necessary preventative maintenance practices. The advantage of proposing a novel modelling method is its feasibility in achieving valuable risk analysis and decision-making [\[29](#page-11-0)]. Prediction results aid in identifying and proposing a RUL model for forecasting the lifecycle of a system.

The RUL predictive modelling methods have challenges when adopting model-based data. The Wiener process-based method was introduced to address challenges attributed to the random factors within RUL prediction of an axial piston pump [[29](#page-11-0)]. This development is motivated by the idea of addressing the limited performance of a degradation model, since the Weiner process integrates a set of superior computational features and parameters to describe a random process. The experimental results revealed that the method is crucial in indicating appropriate parameters for demonstrating the status of the axial piston pump in terms of its internal wear condition. Accordingly, increasing the accuracy of the RUL predictive model improves the system's reliability [[30\]](#page-11-0). A study by Cheng et al [[31\]](#page-11-0), which developed a dual-channel long short-term memory (LSTM) neural network model to improve prediction accuracy, concluded that the experimental verification on the C-MAPSS dataset demonstrated the stability and efficiency of an advanced predictive model capable of handling RUL prediction complexity. Overcoming these challenges is a research area that continues to attract interest, since there is a necessity to build a framework that will improve the RUL predictive process. A qualitative review [\[32](#page-11-0)] explored these limitations and proposed a compact framework as a solution to the complex RUL prediction process while addressing the accuracy concern of the operational datasets is addressed. Eventually, building an integrated framework is essential when technological components are involved in managing huge datasets that are used to trigger the system through the RUL predictive model for maintenance [[32\]](#page-11-0). The evidence provides a deep insight into the measures fundamental to assist in improving the RUL predictive model within the industrial context.

Reverse Osmosis (RO) desalination plants pose significant challenges due to their highly nonlinear, multi-input-multi-output nature, which is further complicated by uncertainties, constraints, and intricate physical phenomena such as membrane fouling. Addressing these complexities requires effective control strategies, among which nonlinear model predictive control (NMPC) stands out [\[33](#page-11-0)]. However, NMPC depends heavily on the accuracy of the internal model for prediction to ensure the RO desalination plant's operational feasibility. Recurrent Neural Networks (RNNs), particularly LSTM networks, excel in capturing complex nonlinear dynamics and providing long-range predictions, even amidst disturbances. As a result, an NMPC approach for an RO desalination plant employing an LSTM as the predictive model was proposed in [[33\]](#page-11-0). The controller was designed to regulate a specified permeate flow rate and maintain permeate concentration below a defined threshold by adjusting the feed pressure. Experimental results demonstrated the efficacy of the proposed approach in achieving desired system performance [[33\]](#page-11-0).

## **3. Research methodology**

The proposed AI prediction model was developed based on data obtained from a local UAE desalination plant. Collected data comprised 2999 instances and 34 attributes, covering daily records from January 1st, 2021 to August 31st, 2025. The raw data attributes retrieved directly from the plant's records system are presented in [Table 2](#page-4-0).

From the 20 raw features presented in [Table 2](#page-4-0), additional 14 features were extracted to enhance model's prediction performance. These new features were constructed to enrich the operational data, providing a more comprehensive basis for predictive modeling. This expanded feature set helps capture additional patterns and trends within the data, ultimately contributing to a more robust and accurate predictive framework. The extracted features are presented in [Table 3.](#page-4-0) Data for features listed in [Table 2](#page-4-0) were acquired through system sensors except for permeate conductivity, feed water conductivity and feed water SDI. As sensor reading exhibited low variability within the same day, sensors data were granulated on daily basis, and the average daily readings were used to simplify the modelling process. Manual laboratory samples were taken daily at five time points to measure permeate conductivity, feed water conductivity and feed water SDI. Average daily values for those features were used as well. Throughout the data preparation steps, missing values were imputed with the median value where applicable. Incorrect entries and extreme outliers were identified and removed from the data to provide more robust models. All attributes were normalized to mitigate scale differences. The data were then randomly split into

<span id="page-4-0"></span>**Table 2**  Description of data attributes collected from the desalination plant digital records system.

| Attribute                      | Stage        | Data Description                                          |
|--------------------------------|--------------|-----------------------------------------------------------|
| Total Feed                     | RO inlet     | The flow of inlet water to the RO system (m3<br>/<br>hr)  |
| HP Pump                        | Pre-RO       | The flow of water in the high-pressure pump               |
|                                | membranes    | (m3<br>/hr)                                               |
| PX LP Inlet                    | Pre-RO       | The flow of inlet water in the pressure                   |
|                                | membranes    | exchange low-pressure pump (m3<br>/hr)                    |
| PX LP Outlet                   | Pre-RO       | The flow of outlet water in the pressure                  |
|                                | membranes    | exchange low-pressure pump (m3/hr)                        |
| Permeate Avg                   | RO inlet     | The average flow of treated permeate water<br>(m3<br>/hr) |
| Permeate Int                   | Post-RO      | The interval flow of treated permeate water               |
|                                | membranes    | (m3<br>/hr)                                               |
| Permeate                       | Post-RO      | The conductivity of permeate water (µS)                   |
| Condty                         | membranes    |                                                           |
| Feed Pressure                  | RO inlet     | Initial pressure of feed in the membrane (Bar)            |
| Pump Speed                     | Pre-RO       | Speed of the high-pressure pump (%)                       |
| HP                             | membranes    |                                                           |
| Pump Speed                     | Pre-RO       | Speed of the pressure exchange pump (%)                   |
| PX                             | membranes    |                                                           |
| DAF Flow                       | Pretreatment | The flow of inlet water to the Dissolved air              |
|                                |              | flotation tank (m3<br>/hr)                                |
| DP DMF Stage                   | Pretreatment | Change of pressure in the Dual media                      |
| 1                              |              | filtration in stage 1 tank (bar)                          |
| DP DMF Stage                   | Pretreatment | Change of pressure in the Dual media                      |
| 2                              |              | filtration in stage 2 tank (bar)                          |
| DP Cartridge                   | Pretreatment | Change of pressure in the cartridge filter (bar)          |
| Filter<br>Feed Water<br>Condty | RO inlet     | The conductivity of the RO feed water (µS)                |
| Feed Water<br>SDI              | RO inlet     | The SDI of the RO feed water                              |
| Feed Water<br>Temp             | RO inlet     | The temperature of the RO feed water ( ◦C)                |
| SW in                          | RO inlet     | The turbidity of seawater inlet (NTU)                     |
| DMF 1 out                      | Pretreatment | The turbidity of outlet water from the dual               |
|                                |              | media filtration 1st stage                                |
| DMF 2 out                      | Pretreatment | The turbidity of outlet water from the dual               |
|                                |              | media filtration 2nd stage                                |

**Table 3**  Extracted Attributes and their Description.

| Extracted Attribute | Data Description                                                |
|---------------------|-----------------------------------------------------------------|
|                     |                                                                 |
| RUL                 | The remaining useful lifetime is measured by the amount of      |
|                     | water (m3<br>) that can be produced till the next CIP           |
| Age                 | The age is measured by the amount of water (m3<br>) produced at |
|                     | the specific time since last CIP                                |
| Min Permeate        | The minimum conductivity of permeate water since the last       |
| Condty              | CIP (µS)                                                        |
| Max Permeate        | The maximum conductivity of permeate water since the last       |
| Condty              | CIP (µS)                                                        |
| Mean Permeate       | The average conductivity of permeate water since the last CIP   |
| Condty              | (µS)                                                            |
| Min Feed Water      | The minimum conductivity of feed water since the last CIP       |
| Condty              | (µS)                                                            |
| Max Feed Water      | The maximum conductivity of feed water since the last CIP       |
| Condty              | (µS)                                                            |
| Mean Feed Water     | The average conductivity of feed water since the last CIP (µS)  |
| Condty              |                                                                 |
| Min Feed Water SDI  | The minimum SDI value of the feed water since the last CIP      |
| Max Feed Water      | The maximum SDI value of the feed water since the last CIP      |
| SDI                 |                                                                 |
| Mean Feed Water     | The average SDI value of the feed water since the last CIP      |
| SDI                 |                                                                 |
| Min Feed Water      | The minimum temperature of feed water since the last CIP (      |
| Temp                | ◦C)                                                             |
| Max Feed Water      | The maximum temperature of feed water since the last CIP (      |
| Temp                | ◦C)                                                             |
| Mean Feed Water     | The average temperature of feed water since the last CIP ( ◦C)  |
| Temp                |                                                                 |

70% for training and 30% for testing. RUL is generally defined in time units until a system CIP is deemed necessary. Since different RO production plants operate as different production rates based on daily water demand and to make our work generalizable, RUL is defined in cubic meters (m3 ) that can be produced before a CIP is performed. At constant production rates, RUL in time units can be calculated as the anticipated RUL in m3 divided by the production rate (m3/unit time).

The study aims to explore and evaluate various machine learning models to construct a robust RUL predictive framework for RO desalination systems. Recent research [\[34](#page-11-0)] suggests that machine learning techniques, including Decision Trees (DTs), Random Forests (RF), and XGBoost, exhibit promising potential in optimizing seawater desalination processes. These models are adept at leveraging real-time data to enhance operational efficiency in water treatment operations. Furthermore, ANNs have demonstrated their utility in both laboratory-scale investigations and commercial desalination plants for process optimization [[35\]](#page-11-0). Following recommendations from the literature, DTs, XGBoost, RF, and LR (as the baseline and simplest ML model) algorithms were selected for evaluation. To optimize the performance of each machine learning algorithm, hyperparameters were tuned and optimized through a 10-fold cross validation procedure. All modelling and analysis steps in this work were carried through the *TidyModels* ecosystem within the R computing software package.

Following its name, DTs are non‑parametric models that partition the feature space into homogeneous regions based on splitting optimization criteria such as mean‑squared error. Terminal nodes of the tree represent predictions based on the subset of data falling within that region. Decision trees are simple, interpretable and computationally inexpensive models that can capture complex, nonlinear relationships and feature interactions. RFs extend decision trees through a data ensembling framework. It generates a large number of trees (forming a forest) using bootstrap samples of the training data and random subsets of features at each split. Predictions are obtained by averaging the outputs of individual trees. This aggregation substantially reduces variance and improves generalization performance. Being a tree-based model, RF is computationally inexpensive and simple to adopt model. Extreme Gradient Boosting model (XGBoost) is a gradient based boosting framework optimized for speed and predictive accuracy. It builds an additive ensemble of decision trees, where each successive tree is trained to correct the residual errors of the preceding tree model. XGBoost implements advanced regularization, efficient handling of missing values, and system-level optimizations such as parallelization and sparsityaware learning making it highly competitive for structured regression tasks. Although XGBoost is a tree based model, it possesses significant computational complexity due to the gradient boosting algorithm implemented. Readers interested in more details of these models are referred to the work of Ray et al [[34\]](#page-11-0) and Jawad at. al [[35\]](#page-11-0).

# **4. Results and discussion**

Summary statistics of the considered RO system features are provided in [Table 4](#page-5-0). As expected, the summary statistics indicate a rightskewed distribution of RUL with a median value of about 541,283 m<sup>3</sup> . The heatmap of correlations among the system features is depicted in [Fig. 2](#page-6-0). RUL shows significant negative correlation with feed pressure, feed water temperature (mean, maximum, minimum, and daily values), feed water SDI (mean, maximum, and daily values), and produced water since last CIP represented as the age feature. Total feed, inlet and outlet flow rate at the low pressure pump exchange, permeate average, and water flow rate at the high pressure pump are positively correlated with the RO system RUL. Significant negative correlations are also observed among the total feed, flow rate at high pressure pump, inlet and outlet flow rate at the low pressure pump exchange and permeate average as shown in the upper left block of the correlations heatmap.

Following our research methodology, data was randomly split into training (70%) and testing (30%) sets. For model performance

<span id="page-5-0"></span>**Table 4**  Summary statistics of the considered RO system features.

| Variable                | Minimum   | Mean       | Median     | Standard Deviation | Maximum     |
|-------------------------|-----------|------------|------------|--------------------|-------------|
| RUL                     | 463.50    | 658,918.28 | 541,283.13 | 522,460.46         | 2826,666.85 |
| Total Feed              | 953.00    | 1089.12    | 1086.00    | 40.72              | 1165.00     |
| HP pump                 | 52.30     | 487.47     | 489.00     | 23.80              | 541.00      |
| PX LP inlet             | 56.00     | 601.13     | 611.00     | 25.80              | 827.00      |
| PX LP outlet            | 465.00    | 618.82     | 622.00     | 22.99              | 843.00      |
| Permeate Avg            | 130.00    | 447.83     | 450.00     | 17.15              | 475.00      |
| Permeate Int            | 66.00     | 448.53     | 453.17     | 72.40              | 4170.00     |
| Permeate Condty         | 17.18     | 1247.80    | 1242.00    | 499.36             | 4898.00     |
| Feed Pressure           | 57.20     | 66.30      | 66.40      | 2.28               | 73.20       |
| Pump Speed HP           | 8.00      | 87.75      | 87.80      | 14.86              | 889.00      |
| Pump Speed PX           | 69.70     | 81.25      | 81.00      | 14.04              | 820.00      |
| DAF Flow                | 0.12      | 2342.13    | 2453.00    | 406.00             | 2696.00     |
| Dp Bar DMF Stage 1      | 0.05      | 0.47       | 0.50       | 0.12               | 0.85        |
| Dp Bar DMF Stage 2      | 0.00      | 0.30       | 0.29       | 0.83               | 32.00       |
| Dp Bar Cartridge Filter | 0.02      | 0.53       | 0.46       | 1.40               | 54.00       |
| Feed Water Condty       | 6056.00   | 58,211.31  | 58,796.50  | 2788.06            | 89,702.00   |
| Feed Water SDI          | 0.44      | 2.48       | 2.47       | 0.10               | 2.92        |
| Feed Water Temp         | 20.50     | 29.39      | 29.50      | 4.68               | 36.50       |
| SW_in                   | 0.29      | 1.11       | 0.99       | 0.72               | 11.40       |
| DMF_1_out               | 0.23      | 0.45       | 0.43       | 0.12               | 2.45        |
| DMF_2_out               | 0.20      | 0.33       | 0.32       | 0.09               | 2.60        |
| AgeM3                   | 0.00      | 642,499.53 | 527,686.35 | 522,751.04         | 2811,690.85 |
| MinPermeate_Condty      | 17.18     | 1122.38    | 1097.50    | 475.28             | 3037.00     |
| MaxPermeate_Condty      | 265.00    | 1693.25    | 1608.00    | 805.23             | 4898.00     |
| MeanPermeate_Condty     | 246.04    | 1284.03    | 1282.16    | 501.64             | 3048.00     |
| MinFeed_Water_Condty    | 6056.00   | 57,070.78  | 57,946.00  | 4356.95            | 61,386.00   |
| MaxFeed_Water_Condty    | 48,251.00 | 59,383.23  | 59,485.00  | 4249.18            | 89,702.00   |
| MeanFeed_Water_Condty   | 48,129.67 | 58,196.67  | 58,703.39  | 2348.30            | 61,505.79   |
| MinFeed_Water_SDI       | 0.44      | 2.37       | 2.38       | 0.21               | 2.69        |
| MaxFeed_Water_SDI       | 2.33      | 2.58       | 2.57       | 0.08               | 2.92        |
| MeanFeed_Water_SDI      | 2.33      | 2.48       | 2.48       | 0.05               | 2.69        |
| MinFeed_Water_Temp      | 20.50     | 27.87      | 27.90      | 4.81               | 36.20       |
| MaxFeed_Water_Temp      | 22.00     | 30.49      | 31.10      | 4.37               | 36.50       |
| MeanFeed_Water_Temp     | 21.37     | 29.07      | 29.33      | 4.55               | 36.25       |

optimization, hyperparameter tuning was performed through 10-fold cross validation using a grid-search optimization approach. Machine learning method parameters require tuning, their operational range, and optimal values are provided in [Table 5](#page-6-0). As an example, performance of the RF model as a function of the tuning parameters (Mtry and number of trees) is depicted in [Fig. 3](#page-7-0). The model performance improves as the values of Mtry and number of trees increase and plateaus at higher values of these parameters. Optimized model performance metrics for the four selected machine learning models are shown in [Table 6](#page-7-0) based on training and testing parts of the data. The RF model achieved the best performance, with an R² of 0.984 and mean absolute error (MAE) of 0.0997, indicating a highly performing prediction model. XGBoost showed similar performance to the RF model with an R2 value of 0.977, while the LR model had the worst performance with an R2 value of 0.655. CART decision tree model has shown an acceptable performance with an R2 value of 0.936. These results indicate superior performance of ensemble-based machine learning models including RF and XGBoost over classical algorithms such as LR and CART trees. It is worth mentioning here that decision trees and RF models are easy to explain and interpret compared to XGBoost. Models demonstrated comparable results across the training and testing parts of the data indicating no overfitting issues. Being a decision tree-based model, RF model is computationally inexpensive and can be easily adopted in the RO plant control system to identify and predict the system RUL.

[Fig. 4](#page-8-0) illustrates the actual RUL versus predicted values plot for the RF prediction model. Points in [Fig. 4](#page-8-0) closely align with the correlation line, indicating a high degree of correlation between the actual and predicted values. The minimal scattering of points away from the line further demonstrates the exceptional accuracy and reliability of the RF model in predicting the RO system RUL, reaffirming its suitability for predictive maintenance applications. Density plots of models' prediction errors are provided in [Fig. 5.](#page-8-0) The probability density plots indicate wellperforming prediction models with symmetrical distributions and no skewness issues. The cumulative density plots in [Fig. 5](#page-8-0) confirm the superior performance of the RF and XGBoost models over the CART and LR models.

After evaluating the performance of various models and selecting the RF algorithm as the best predictive model, it became evident that identifying the variables with the most significant impact on the RUL of RO membranes was crucial. Understanding which features most strongly influence membrane lifespan provides valuable insights into the operational conditions of the plant, allowing for informed decisions to optimize performance and extend membrane longevity.

The bar chart presented in [Fig. 6](#page-9-0) illustrates the variable importance as determined by the RF prediction model. The chart highlights the general significance of each feature, offering an overview of the factors that have the greatest impact on RUL predictions. Notably, the top five significant predictors of RUL were the maximum feed water SDI, maximum feed water temperature, speed of the pressure exchange pump, age, and minimum feed water conductivity.

Global variable importance through the SHapley Additive exPlanations (SHAP) method is depicted in [Fig. 7.](#page-9-0) The global SHAP importance graph, reveals the significance of features across the entire testing dataset, identifying which variables consistently contribute to the model's decisions. Meanwhile, the local SHAP variable importance graph in [Fig. 8,](#page-10-0) delves into individual predictions, explaining why the model made a specific decision for a particular instance. This graph is represented in dot form, where the color gradient reflects the direction and magnitude of each feature's contribution, with more influential features shown in distinct colors. Together, these visualizations offer a comprehensive understanding of the factors affecting RUL and enable targeted improvements in plant operations. Top five predictors of RUL as indicated by SHAP analysis are the maximum feed water temperature, maximum feed water SDI, membrane age, speed of the pressure

<span id="page-6-0"></span>![](_page_6_Figure_2.jpeg)

**Fig. 2.** Heatmap of features correlation.

**Table 5**  Tuning parameters for the selected machine learning models.

| Algorithm               | Tunning Parameters                                                                            | Optimal Parameter<br>Value                            |
|-------------------------|-----------------------------------------------------------------------------------------------|-------------------------------------------------------|
| Linear<br>Regression    | No Tunning                                                                                    | No Tunning                                            |
| Decision Tree<br>(CART) | 1. Cost Complexity [1e-10 to 0.1]<br>2. Tree Depth [1 to 15]                                  | 1. Cost Complexity =<br>0.00001<br>2. Tree Depth = 15 |
| XGBoost                 | 1. Mtry (number of features to try at<br>each split) [1 to 20]<br>2. No. of trees [1 to 2000] | 1. Mtry = 20<br>2. No. of trees= 1333                 |
| Random Forest           | 1. Mtry (number of features to try at<br>each split) [1 to 20]<br>2. No. of trees [1 to 2000] | 1. Mtry = 11<br>2. No. of trees= 445                  |

exchange pump, and permeate average. These results are in line with the findings of the variable importance obtained directly through the RF model in [Fig. 6](#page-9-0). Local contributions provided in [Fig. 8](#page-10-0) indicate negative relationship of RUL with maximum feed water temperature, maximum feed water SDI, membrane age and speed of the pressure exchange pump as higher values for those features are associated with low RUL values. These variables are inherently linked to the performance and degradation of the membranes, making their high influence on the RUL logical and expected. On the contrary, permeate average has shown a positive relationship with RUL with higher RUL values associated with higher permeate average values.

SDI assesses the fouling potential of the feed water by measuring the presence of suspended solids, particles, and other fouling agents that can clog membrane pores. A high SDI value typically indicates a greater risk of fouling, thereby reducing the membrane's lifespan. Water temperature also plays a critical role, as it directly affects the solubility of fouling agents and the viscosity of water. Fouling can be slowed down if feed water temperature is cooled down. Temperature fluctuations can accelerate membrane degradation, with RO membrane design limits generally ranging between 5 ◦C and 45 ◦C. Elevated temperatures can increase scaling due to salt precipitation or reduce the solubility of salts such as calcium carbonate and sulfate, thereby exacerbating fouling. While higher pump speeds can improve feed water flow and enhance turbulence across the membrane surface—helping to reduce biofouling and scaling—excessively high speeds can cause membrane compaction, which diminishes its lifespan. Membrane age, as expected, is also a strong determinant of RUL, as older membranes naturally exhibit

<span id="page-7-0"></span>![](_page_7_Figure_2.jpeg)

**Fig. 3.** Tunning parameters results for Random Forest model.

**Table 6**  Training and testing performance of the considered machine learning models for RUL prediction.

| RUL Prediction<br>Model | Performance on Training<br>Data |         | Data   | Performance on Testing |       |        |
|-------------------------|---------------------------------|---------|--------|------------------------|-------|--------|
|                         | R2                              | RMSE    | MAE    | R2                     | RMSE  | MAE    |
| Linear Regression       | 0.693                           | 0.560   | 0.438  | 0.655                  | 0.571 | 0.431  |
| Decision Tree<br>(CART) | 0.993                           | 0.0846  | 0.0592 | 0.936                  | 0.246 | 0.152  |
| XGBoost                 | 0.999                           | 0.00142 | 0.001  | 0.977                  | 0.147 | 0.0993 |
| Random Forest           | 0.997                           | 0.0592  | 0.0415 | 0.984                  | 0.136 | 0.0997 |

reduced performance and a shorter remaining lifespan due to prolonged exposure to operational stresses.

Overall, this analysis underscores the significant role operational data plays in determining membrane performance and lifespan. By monitoring and optimizing these critical variables, RO plants can operate under more stable and efficient conditions, ultimately extending membrane longevity and enhancing overall system efficiency. From an operational standpoint, feed water temperature and SDI seem to have the highest impact on the RO system's RUL. Reducing both parameters is essential for improving membrane lifespan.

To show the importance of including operational parameters in the RUL prediction model, we implement a Deep Learning based timeseries transformer with attention model as one of the state-of-the-art models for timeseries predictions. Model is trained on RUL timeseries data with no operational parameters at 64 attention heads and head size of 4. Performance of the transformer model for the test part of the data is

depicted in [Fig. 9.](#page-10-0) Model had an R2 value of 0.718, MAE value of 0.102 and RMSE value of 0.227. Results show the superiority of the developed RF model over the transformer-based model indicating the significance of operational parameters in predicting RO membranes RUL.

The developed RF model in this study is computationally lightweight once trained, enabling RUL predictions to be executed on standard industrial hardware or integrated into supervisory systems at minimal overhead cost. The model can operate at the prediction frequency required by the process supervisors that could range from almost real‑time intervals on SCADA‑connected edge devices to low frequency daily predictions on centralized database servers without violating latency constraints. As new operational data becomes available, the model can be retrained on regular cycles so it continues to reflect most recent system behavior and naturally adjusts to gradual shifts in operating conditions providing a day-to-day industrial decision support system. Due to slight differences in performance in RO desalination systems, models need to be trained at first for the specific system under consideration. Similar prediction performance is expected to the developed RF model in other RO plants is expected as the model was trained and tested on separate parts of the data following standard modelling pipelines in machine learning making its performance generalizable.

In a pressure vessel, membranes are arranged in series and experience different degradation constraints. Leading membranes face particulate fouling, while trailing membranes face scaling. This spatial heterogeneity leads to different RULs by position within the same vessel. In this work and due to the limited data, we deal with the whole RO pressure vessel as one unit and predicts when a next CIP is necessary, as this is the current practice at the RO production facility considered. When a CIP is performed, all RO membranes in the cell are cleaned to

<span id="page-8-0"></span>![](_page_8_Figure_3.jpeg)

**Fig. 4.** Actual versus predicted RUL values for the Random Forest Model.

![](_page_8_Figure_5.jpeg)

**Fig. 5.** Probability density function (Left) and cumulative probability density (Right) for the prediction errors among the four considered machine learning models.

minimize downtime. As no membrane replacement procedures are currently implemented as suggested solution to reduce CIP time and the lack of sensors data at the beginning and end of each RO membrane stage, the system was considered as one block. This points a limitation of our current work for further investigation.

# **5. Conclusion**

In this work, an artificial intelligence-based predictive model for estimating the RUL of RO membranes has been developed. Through the examination of the literature and an extensive analysis of the RO plant operational data, four primary machine learning based prediction algorithms were tested and validated: linear regression, decision tree, XGBoost, and Random Forest. Among these, the Random Forest algorithm demonstrated the best performance, achieving an impressive R2 value of 0.984 for the test set. This high level of prediction performance confirms that the Random Forest model can be effectively employed to predict the RUL of RO membranes, ultimately benefiting water treatment plants by enhancing maintenance strategies. By accurately forecasting the membrane lifespan, this predictive model can minimize unexpected failures and reduce the frequency and cost of CIP procedures, thus optimizing operational efficiency.

The development of this machine learning based predictive model is underpinned by a robust methodology that leverages both experimental and historical operational data. It addresses critical challenges in managing RO membrane performance, particularly in mitigating the impacts of pressure changes that accelerate fouling and degradation. This research not only contributes to the field of predictive maintenance in desalination but also enhances data-driven decision-making practices. Ultimately, the findings of this work have the potential to advance knowledge regarding optimal operating conditions and parameters necessary for effective seawater treatment. By leveraging machine learning in predictive maintenance, desalination plants can improve the cost-effectiveness, enhance operational reliability, and extend the

<span id="page-9-0"></span>![](_page_9_Figure_2.jpeg)

**Fig. 6.** Variable importance graph as provided by the Random Forest model.

![](_page_9_Figure_4.jpeg)

**Fig. 7.** SHAP global variable importance for the Random Forest model.

lifespan of RO membranes, thereby supporting sustainable seawater production practices.

Few recommendations for future research are warranted. First, the external validity of the prediction model can be strengthened by incorporating additional RO plant data from different operating environments and membrane types. This would enhance the generalizability and robustness of the proposed model. Second, future studies could investigate the economic and operational impacts of monitoring and controlling the most influential variables identified in this work. Such analyses would provide valuable insights into the cost–benefit

<span id="page-10-0"></span>![](_page_10_Figure_2.jpeg)

**Fig. 8.** SHAP local variable importance for the Random Forest model.

![](_page_10_Figure_4.jpeg)

**Fig. 9.** Actuals versus predicted RUL values through the Deep Learning transformed model considered. Plot is shown for test data only.

trade-offs of implementing predictive maintenance strategies and could guide decision-makers in optimizing resource allocation.

#### **Funding sources**

Article processing charges for this publication is funded through the Research Office at the American University of Sharjah.

#### **CRediT authorship contribution statement**

**Hussam Alshraideh:** Writing – review & editing, Visualization, Supervision, Resources, Project administration, Funding acquisition, Formal analysis, Data curation, Conceptualization. **Fajer Al Ali:** Writing – original draft, Visualization, Validation, Software, Methodology, Formal analysis, Data curation, Conceptualization. **Mahmoud Awad:**  Writing – review & editing, Supervision. **Amani Al-Othman:** Writing – review & editing, Methodology.

# **Declaration of competing interest**

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

### **Acknowledgment**

The authors gratefully acknowledge the financial support provided by the Office of Research at the American University of Sharjah through the open access program OAP26. This paper represents the opinions of the author(s) and does not mean to represent the position or opinions of the American University of Sharjah.

### **Data availability**

Data will be made available on request.

### <span id="page-11-0"></span>**References**

- [1] S. Alaa Abu, N. Tasmin, A. Amer, Potable water in UAE: an overview of water characteristics and sources of contamination, J. Env. Toxicol. Stud. 3 (2) (Mar. 2019) 1–4, [https://doi.org/10.16966/2576-6430.120.](https://doi.org/10.16966/2576-6430.120)
- [2] A. Alsharhan, Z. Rizk, Water resources and water demands in the UAE. Water Resources and Integrated Management of the United Arab Emirates, 2020, pp. 757–791, [https://doi.org/10.1007/978-3-030-31684-6\\_27.](https://doi.org/10.1007/978-3-030-31684-6_27)
- [3] T. Shivakumar, V. Razaviarani, An integrated approach to enhance the desalination process: coupling reverse osmosis process with microbial desalination cells in the UAE, Water Suppl. 21 (3) (2020) 1127–1143, [https://doi.org/10.2166/](https://doi.org/10.2166/ws.2020.375) [ws.2020.375](https://doi.org/10.2166/ws.2020.375).
- [4] L.V. Amma, F. Ashraf, Brine management in reverse osmosis desalination: a UAE perspective, in: 2020 Advances in Science and Engineering Technology International Conferences (ASET), Feb. 2020, [https://doi.org/10.1109/](https://doi.org/10.1109/aset48392.2020.9118335) [aset48392.2020.9118335](https://doi.org/10.1109/aset48392.2020.9118335).
- [5] B. Zolghadr-Asli, et al., A review of limitations and potentials of desalination as a sustainable source of water, Environ. Sci. Pollut. Res. (2023), [https://doi.org/](https://doi.org/10.1007/s11356-023-30662-x)  [10.1007/s11356-023-30662-x.](https://doi.org/10.1007/s11356-023-30662-x)
- [6] R. Saeed, A.H. Konsowa, M.S. Shalaby, M.S. Mansour, M.G. Eloffy, Optimization of integrated forward – reverse osmosis desalination processes for brackish water, Alex. Eng. J. 63 (2023) 89–102, <https://doi.org/10.1016/j.aej.2022.07.054>.
- [7] S. Bhattacharjee, G. Dersel, A. Shanableh, N. Darwish, M. Al-Samarai, Challenges & opportunities of wastewater reuse privatization: a case study from Sharjah, UAE, IEEE Xplore (2020). Accessed: Dec. 6, 2023 [Online]. Available at: [https://ieeexplo](https://ieeexplore.ieee.org/document/9118342)  [re.ieee.org/document/9118342](https://ieeexplore.ieee.org/document/9118342).
- [8] [M. Alanazi, T.N. Alharby, Computational evaluation using machine learning for](http://refhub.elsevier.com/S2666-8211(26)00185-7/sbref0007)  [analysis of membrane desalination process powered by solar energy, Sci. Rep. 15](http://refhub.elsevier.com/S2666-8211(26)00185-7/sbref0007)  [\(1\) \(2025\) 36384.](http://refhub.elsevier.com/S2666-8211(26)00185-7/sbref0007)
- [9] [W.M. Ashraf, M.A. Jamil, G.M. Uddin, B. Shboul, K. Ishfaq, K.C. Ng, M. Dixon, B.](http://refhub.elsevier.com/S2666-8211(26)00185-7/sbref0008)  [B. Xu, M.W. Shahzad, Machine learning assisted improved desalination pilot](http://refhub.elsevier.com/S2666-8211(26)00185-7/sbref0008) [system design and experimentation for the circular economy, J. Water. Process.](http://refhub.elsevier.com/S2666-8211(26)00185-7/sbref0008) [Eng. 63 \(2024\) 105535.](http://refhub.elsevier.com/S2666-8211(26)00185-7/sbref0008)
- [10] [A. Alenezi, Y. Alabaiadly, Artificial intelligence applications in water treatment](http://refhub.elsevier.com/S2666-8211(26)00185-7/sbref0009)  [and desalination: a comprehensive review, Water 17 \(8\) \(2025\) 1169](http://refhub.elsevier.com/S2666-8211(26)00185-7/sbref0009).
- [11] N. AlSawaftah, W. Abuwatfa, N. Darwish, G. Husseini, A comprehensive review on membrane fouling: mathematical modelling, prediction, diagnosis, and mitigation, Water 13 (9) (2021) 1–37, [https://doi.org/10.3390/w13091327.](https://doi.org/10.3390/w13091327)
- [12] S. Eltanbouly, A. Erradi, A. Tantawy, A.B. Said, K. Shaban, H. Qiblawey, LIME: long-term forecasting model for desalination membrane fouling to estimate the remaining useful life of membrane, Intern Confer Ind. Eng. Other Appl. Appl. Intell. Syst. (2023) 3–14, [https://doi.org/10.1007/978-3-031-36822-6\\_1.](https://doi.org/10.1007/978-3-031-36822-6_1)
- [13] Y. Ibrahim, N. Hilal, Enhancing ultrafiltration membrane permeability and antifouling performance through surface patterning with features resembling feed spacers, NPJ. Clean. Water. 6 (1) (2023) 1–15, [https://doi.org/10.1038/s41545-](https://doi.org/10.1038/s41545-023-00277-3) [023-00277-3.](https://doi.org/10.1038/s41545-023-00277-3)
- [14] R. Cruz-Silva, et al., Nanocomposite desalination membranes made of aromatic polyamide with cellulose nanofibers: synthesis, performance, and water diffusion study, Nanoscale 12 (38) (2020) 19628–19637, [https://doi.org/10.1039/](https://doi.org/10.1039/d0nr02915g)  [d0nr02915g.](https://doi.org/10.1039/d0nr02915g)
- [15] T. Tavares, J. Tavares, F. Leon, ´ B. Penate, ˜ A.R. Martín, Assessment of processes to increase the useful life and the reuse of reverse osmosis elements in Cape Verde and Macaronesia, Membrane 12 (6) (2022) 613, [https://doi.org/10.3390/](https://doi.org/10.3390/membranes12060613) [membranes12060613](https://doi.org/10.3390/membranes12060613), 613.
- [16] A. Zapata-Sierra, M. Cascajares, A. Alcayde, F. Manzano-Agugliaro, Worldwide research trends on desalination, Desalination 519 (2021) 115305, [https://doi.org/](https://doi.org/10.1016/j.desal.2021.115305)  [10.1016/j.desal.2021.115305](https://doi.org/10.1016/j.desal.2021.115305).
- [17] M.A. Ahmed, S. Amin, A.A. Mohamed, Fouling in reverse osmosis membranes: monitoring, characterization, mitigation strategies and future directions, Heliyon (2023) e14908, [https://doi.org/10.1016/j.heliyon.2023.e14908.](https://doi.org/10.1016/j.heliyon.2023.e14908)

- [18] M. Qasim, M. Badrelzaman, N.N. Darwish, N.A. Darwish, N. Hilal, Reverse osmosis desalination: a state-of-the-art review, Desalination 459 (2019) 59–104, [https://](https://doi.org/10.1016/j.desal.2019.02.008) [doi.org/10.1016/j.desal.2019.02.008.](https://doi.org/10.1016/j.desal.2019.02.008)
- [19] W.H. Abuwatfa, N. AlSawaftah, N. Darwish, W.G. Pitt, G.A. Husseini, A review on membrane fouling prediction using artificial neural networks (ANNs), Membranes 13 (7) (2023), <https://doi.org/10.3390/membranes13070685>.
- [20] Y. Su, C. Jacobsen, Treatment of clean in place (CIP) wastewater using microalgae: nutrient upcycling and value-added byproducts production, Sci. Total. Environ. 785 (2021) 147337, <https://doi.org/10.1016/j.scitotenv.2021.147337>.
- [21] J. Bailey, Membrane CIP (Clean in Place): a complete guide, Avis. Membr. Treat. Solut. (2022). Accessed: Dec. 6, 2023 [Online]. Available at: [https://avistamembra](https://avistamembranesolutions.com/resources/membrane-cip-clean-in-place-a-complete-guide/)  [nesolutions.com/resources/membrane-cip-clean-in-place-a-complete-guide/](https://avistamembranesolutions.com/resources/membrane-cip-clean-in-place-a-complete-guide/).
- [22] M. Jafari, et al., A comparison between chemical cleaning efficiency in lab-scale and full-scale reverse osmosis membranes: role of extracellular polymeric substances (EPS), J. Membr. Sci. 609 (2020) 118189, [https://doi.org/10.1016/j.](https://doi.org/10.1016/j.memsci.2020.118189)  [memsci.2020.118189](https://doi.org/10.1016/j.memsci.2020.118189), 118189.
- [23] M.S. Toran, et al., Membrane-based processes to obtain high-quality water from brewery wastewater, Front. Chem. Eng. 3 (2021), [https://doi.org/10.3389/](https://doi.org/10.3389/fceng.2021.734233)  [fceng.2021.734233.](https://doi.org/10.3389/fceng.2021.734233)
- [24] D. Singh, S. Anand, Efficacy of a typical clean-in-place protocol against in vitro membrane biofilms, J. Dair. Sci. (2022), [https://doi.org/10.3168/jds.2022-21712.](https://doi.org/10.3168/jds.2022-21712)
- [25] K. Gruskevica, L. Mezule, Cleaning methods for ceramic ultrafiltration membranes affected by organic fouling, Membrane 11 (2) (2021), [https://doi.org/10.3390/](https://doi.org/10.3390/membranes11020131)  [membranes11020131](https://doi.org/10.3390/membranes11020131).
- [26] S. Brover, Y. Lester, A. Brenner, E. Sahar-Hadar, Optimization of ultrafiltration as pre-treatment for seawater RO desalination, Desalination 524 (2022), [https://doi.](https://doi.org/10.1016/j.desal.2021.115478)  [org/10.1016/j.desal.2021.115478.](https://doi.org/10.1016/j.desal.2021.115478)
- [27] Y. Li, H. Wang, S. Wang, K. Xiao, X. Huang, Enzymatic cleaning mitigates polysaccharide-induced refouling of RO membrane: evidence from foulant layer structure and microbial dynamics, Env. Sci. Technol. 55 (8) (2021) 5453–5462, [https://doi.org/10.1021/acs.est.0c04735.](https://doi.org/10.1021/acs.est.0c04735)
- [28] Y. Song, S. Gao, Y. Li, L. Jia, Q. Li, F. Pang, Distributed attention-based temporal convolutional network for remaining useful life prediction, IEEe Internet. Things. J. 8 (12) (2021) 9594–9602, <https://doi.org/10.1109/jiot.2020.3004452>.
- [29] X. Wang, S. Lin, S. Wang, Z. He, C. Zhang, Remaining useful life prediction based on the Wiener process for an aviation axial piston pump, Chin. J. Aeronaut. 29 (3) (2016) 779–788, <https://doi.org/10.1016/j.cja.2015.12.020>.
- [30] M. Yan, X. Wang, B. Wang, M. Chang, and I. Muhammad, "Bearing remaining useful life prediction using support vector machine and hybrid degradation tracking model," vol. 98, pp. 471–482, 2020, [doi: https://doi.org/10.1016/j.is](https://doi.org/10.1016/j.isatra.2019.08.058) [atra.2019.08.058.](https://doi.org/10.1016/j.isatra.2019.08.058)
- [31] P. Cheng, J. Wu, Q. Wang, W. Gui, Z. Tang, Remaining useful life prediction using dual-channel LSTM with time feature and its difference, Entropy 24 (12) (2022) 1818,<https://doi.org/10.3390/e24121818>, 1818.
- [32] C. Ferreira, G. Gonçalves, Remaining useful life prediction and challenges: a literature review on the use of machine learning methods, J. Manuf. Syst. 63 (2022) 550–562, <https://doi.org/10.1016/j.jmsy.2022.05.010>.
- [33] D. Karimanzira, T. Rauschenbach, Deep learning based model predictive control for a reverse osmosis desalination plant, J. Appl. Math. Phys. 08 (12) (2020) 2713–2731, <https://doi.org/10.4236/jamp.2020.812201>.
- [34] S.S. Ray, R.K. Verma, A. Singh, M. Ganesapillai, Y.N. Kwon, A holistic review on how artificial intelligence has redefined water treatment and seawater desalination processes, Desalination 546 (2023) 116221, [https://doi.org/10.1016/j.](https://doi.org/10.1016/j.desal.2022.116221)  [desal.2022.116221](https://doi.org/10.1016/j.desal.2022.116221).
- [35] J. Jawad, A.H. Hawari, S.J. Zaidi, Artificial neural network modelling of wastewater treatment and desalination using membrane processes: a review, Chem. Engin. J. 419 (2021),<https://doi.org/10.1016/j.cej.2021.129540>.
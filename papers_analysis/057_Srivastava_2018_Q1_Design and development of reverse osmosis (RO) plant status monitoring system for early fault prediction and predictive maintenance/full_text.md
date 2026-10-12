#### **ORIGINAL ARTICLE**

![](_page_0_Picture_2.jpeg)

# **Design and development of reverse osmosis (RO) plant status monitoring system for early fault prediction and predictive maintenance**

**Satyam Srivastava<sup>1</sup> · Saikrishna Vaddadi1 · Pankaj Kumar2 · Shashikant Sadistap1**

Received: 29 January 2018 / Accepted: 12 September 2018 / Published online: 18 September 2018 © The Author(s) 2018

#### **Abstract**

Automation and reliability are the crucial elements of any advance reverse osmosis plant to meet the environmental and economic demands. Early fault indication, diagnosis and regular maintenance are the key challenges with most of the reverse osmosis plants in the Indian scenario. The present work introduces a modern reverse osmosis (RO) plant status monitoring unit to monitor diferent plant parameters in real time and early prediction for faults and maintenance. Developed RO plant status monitoring unit consists of a touch screen-based embedded monitoring unit, water quality sensors (pH, TDS), sampling chamber for controlled water fow, fow sensors, pressure and level sensors. The present system has been developed in a modular fashion so that it could be integrated with any capacity of RO plant units. Developed embedded system monitors various parameters of the plant such as input power, efciency of the plant, level of input and output water tank and also guides operator with instructions for plant operation. Other than this, a dedicated smartphone app interface has been developed for the operator to acquire data from status monitoring unit, storage on smartphone, and transfer it to the cloud. The developed smartphone-based app also provides facility to integrate plant data with Google map with location information for easy understanding and quick action. The system has also a backup facility to transfer data to the server using 2G GSM module during the unavailability of the operator. A dedicated centralized Web server has been developed for real-time visualization of all installed RO plant status monitoring units. Diferent machine learning techniques have been implemented on acquired sensors data to predict early warnings related to power failure, membrane fouling and scaling, input water shortage, pipe, tank leakage, water quality sensors damage, non-operation or wrong operation of the plant along with diferent maintenance actions such as membrane water and chemical wash. Developed RO status monitoring unit has been tested with various RO plants having capacity from 500 LPH to 2000 LPH and deployed at various nearby villages of Rajasthan.

**Keywords** Water quality sensors · Reverse osmosis · Embedded system · Early warning · Predictive maintenance

\* Satyam Srivastava satyamsrivastava@ceeri.res.in

> Saikrishna Vaddadi sai@ceeri.res.in

Pankaj Kumar pankajkumar@ceeri.res.in

Shashikant Sadistap shashikant\_s@ceeri.res.in

- <sup>1</sup> Academy of Scientifc and Innovative Research (AcSiR), CSIR-CEERI, CEERI Colony, Pilani, Jhunjhunu, Rajasthan 333031, India
- <sup>2</sup> CSIR-CEERI, CEERI Colony, Pilani, Jhunjhunu, Rajasthan 333031, India

# **Introduction**

Increasing demand for fresh potable water leads toward the requirement of diferent advance automatic water treatment solutions. Various water treatment solutions such as reverse osmosis (RO), microfltration (MF), ultra-fltration (UF), nano-fltration (NF) have been explored by diferent researchers in the past, but RO is one of the leading water treatment solutions due to its higher water purifcation capacity, energy efciency along with the capability to remove almost all toxic metals and bacteria from input water supply. The performance of RO membrane is quite sensitive and highly dependent on the quality of feed and overall plant conditions. So, RO plant needs highly accurate control and monitoring system to monitor the feed water

![](_page_0_Picture_17.jpeg)

Applied Water Science (2018) 8:159 **159** Page 2 of 10

and other plant parameters to maintain its operation close to optimum conditions. Regular maintenance of membrane and monitoring of feed water and plant parameters increase the productivity of RO plant and also reduce the chances of early membrane fouling which prolongs the life of the RO membrane and overall plant (Sobana and Rames [2011\)](#page-9-0). Several control techniques such as PID (Esfahani et al. [2016\)](#page-9-1), fuzzy (Zilouchian and Jafar [2001](#page-9-2)), ANN (Lee et al. [2009](#page-9-3)), optimal control (Gambier et al. [2006](#page-9-4)), predictive control (Abbas [2006\)](#page-9-5) have been explored to control various RO plant parameters and maintain the plant in optimum conditions. Centralized PI controllers scheme for interfacing multivariable process has been also tried by diferent researchers for RO plant parameters control using synthesis method (Kumar et al. [2012](#page-9-6)). Selection of diferent techniques to tune the controller parameters is one of the important and challenging steps and needs to be selected based on the specifc application. One of the famous techniques to tune controller parameters is the usage of compensators. Recycle compensator is one of the famous techniques to tune the controller parameters (Armbrust and Sbarbaro [2010\)](#page-9-7). Minimization of RO plant energy consumption using optimal-based control (Bartman et al. [2010\)](#page-9-8) along with alternative energy sources (Chaabene and Sellami [2013\)](#page-9-9) for RO plants also has been introduced by diferent researchers. In Indian scenario, intelligent monitoring along with event prediction for RO plants is one of the essential needs to increase the life of RO membrane and also to avoid diferent problems such as over-/undervoltage fuctuations, dry run of high pressure and booster pumps, input water pipeline leakage, empty input water tank, overfow of output water tank. Diferent monitoring control tools along with efcient control strategy have been introduced for real-time monitoring and control of RO plants, but most of them are costly and bulky and predict only limited parameters such as water quality and fow rate (Torky et al. [2009](#page-9-10)). Few of the eforts also have been seen in the direction of real-time membrane fouling monitoring and early prediction using diferent analytical techniques (Hwang et al. [2010](#page-9-11)). Several eforts have been observed in the direction of RO plant parameters monitoring and control, but still, there are various challenges such as early fault prediction of diferent events such as overvoltage and undervoltage fuctuations, membrane fouling, membrane scaling, plant efciency, water quality sensors damage which need to be addressed. Other than early fault prediction, predictive maintenance facility related to the membrane, sensors, flters maintenance for Indian RO plant operators is one of the essential needs to be tackled to increase the life of the overall plant and also maintain optimum operating conditions. The present work introduces an embedded RO plant status monitoring unit to monitor various plant parameters such as water quality (pH, TDS), input and output fow rate, input and output tank level, under- and overvoltage fuctuations along with the facility to predict diferent maintenance actions such as membrane water wash, membrane chemical wash, sensors calibration and cleaning, operation of RO plant. Other than this, a smartphone-based app interface also has been developed to acquire data from RO plant status monitoring unit using classical Bluetooth module and further transfer it to Google frebase cloud (Taherkordi and Frank [2016](#page-9-12)). An alternative data transfer scheme also has been implemented using 2G GSM module during the unavailability of RO plant operator. Day by day RO plant parameters data also store at the local memory of the embedded system and can be collected using any USB drive. The rest of the manuscript is organized as follows. Section II provides a detailed description of the proposed RO plant status monitoring scheme, and section III provides details of the developed embedded system for RO plant status monitoring. Section IV consists of the detailed description of the development procedure of smartphonebased android application along with its features and utility. Section V discusses the algorithms to predict diferent maintenance actions and events. Section VI presents testing and feld trial results of developed system installed at diferent nearby villages of Rajasthan, and Section VII discusses discussion and conclusion.

# **Proposed RO plant status monitoring scheme**

Overall idea is to monitor the critical parameters of RO plants installed at nearby villages of Rajasthan. Proposed monitoring scheme (Fig. [1\)](#page-2-0) consists of diferent layers such as at local level, supervisory level and coordinator level and fnally at the central level. Local level monitoring of various RO plants can be performed using developed embedded RO plant status monitoring unit and will be useful for diferent RO plant operators and villagers. Central level of monitoring has been performed using cloud services and could be useful for monitoring and visualization of data at any parts of the world.

Proposed scheme consists of parameters monitoring, data storage and computational algorithms at diferent levels and has fewer chances of information loss. Other than this, proposed scheme also divides overall information, models and algorithms complexity at diferent layers. Information collected at the local level using developed embedded RO plant status monitoring unit transfers to operator's smartphone using Bluetooth communication. Further, collected data with plant location information are transferred to cloud level for centralized monitoring using the developed customized android app. Google frebase has been used as a cloud platform for the initial use and also to demonstrate the proof of concept. 2G GSM module is also used as a backup option for data communication from monitoring unit to the Web

![](_page_1_Picture_6.jpeg)

![](_page_2_Figure_3.jpeg)

<span id="page-2-0"></span>**Fig. 1** Implemented RO plant status monitoring scheme for fault prediction and regular maintenance

server. Few of the layers such as supervisory and coordinator monitoring layer also can be introduced as the complexity increases with increase in the number of local RO monitoring nodes.

# **Embedded system design and development for RO plant status monitoring**

An embedded system (Fig. [3b](#page-3-0)) has been designed and developed to acquire real-time data of of-the-shelf sensors interfaced with RO plant to measure various plant parameters such as feed and product fow rate, input power, water level, feed and product pH, TDS. A customized hardware platform (Fig. [2\)](#page-3-1) has been designed to read and store data from various sensors and also to drive diferent actuators used in RO plant. Developed hardware platform has been interfaced with quad-core ARMv8 processor-based microcontroller unit for data acquisition and processing. Developed touch screenbased embedded system provides the facility for a userfriendly graphical user interface for RO plant operator to monitor real-time plant data. Further, a classical Bluetooth module has been integrated with the developed embedded system to communicate with dedicated smartphone-based app interface to store data and further transfer it to cloud with location information. Developed RO plant status monitoring unit for early fault prediction and predictive maintenance is a step toward the development of an advanced, low-cost and easy to use modular embedded for RO plant status monitoring. Detailed information about frmware and software package development is as follows.

#### **Firmware development**

RO plant status monitoring unit (Fig. [3](#page-3-0)a) has been developed in modular fashion (Fig. [4](#page-4-0)) and consists various submodules such as embedded data acquisition, monitoring and control unit along with commercial sensors with 4–20-mA current transmitters for pH and TDS sensors installed in sampling chamber for real-time feed and product water quality data collection, commercial uninterrupted power supply module (U.P.S) for power backup. The developed portable embedded system acts as a heart of the overall RO plant status monitoring unit. Embedded system consists three major sections such as dedicated designed hardware platform for sensors and actuator interfacing, an ARMv8 processorbased microcontroller unit (Raspberry pi 3) for data acquisition and processing and switch mode power supply for

![](_page_2_Picture_11.jpeg)

![](_page_3_Figure_3.jpeg)

<span id="page-3-1"></span>**Fig. 2** Functional block diagram of developed embedded RO plant status monitoring unit

![](_page_3_Picture_5.jpeg)

**Fig. 3 a** Deployed RO plant status monitoring unit and **b** developed embedded processing and control unit

<span id="page-3-0"></span>regulated power. Developed dedicated hardware module design composed of embedded circuitry, wherein PCB modules are indigenously designed, fabricated and interfaced with ARMv8 processor-based microcontroller unit. The resources used to develop dedicated hardware modules are Darlington array (ULN2003) to drive relay array, external E2 PROM (24LC1025) for data storage at local level, port expander (MCP23017) to generate additional digital input

![](_page_3_Picture_9.jpeg)

![](_page_4_Figure_2.jpeg)

<span id="page-4-0"></span>**Fig. 4** Line diagram of reverse osmosis plant status monitoring unit integrated with reverse osmosis plant

output pins, analog-to-digital converter (ADS7828) to convert sensors analog response into digital form, bufer unit for isolation (74LS244), real-time clock (DS1307) to access the real time with data, Xbee pro module for wireless data transfer and regulators (LM7805, LM1117) of diferent voltage levels (+5 v and +3.3 v). Developed hardware platform has been further interfaced with an ARMv8 processor-based microcontroller unit (Raspberry pi 3) for data acquisition,

![](_page_4_Picture_6.jpeg)

processing and control. A 7-inch touch display along with its local controller has been integrated with the developed embedded system to display the user-friendly graphical user interface.

A classical Bluetooth module has been used to transfer data from developed embedded system to smartphone-based app interface and further to cloud for future analysis. Other than this, a 2G GSM module has been used as an alternative data transfer to the server. Developed embedded system power is provided by a switched mode power supply (SMPS) that provides cleaned and fltered±12 V to all circuit modules. Developed embedded processing and control unit has been interfaced with various commercial sensors, which are already integrated with RO plant for measurement of diferent parameters.

#### **Software package development**

Various modular programs have been written in C+++with GCC compiler for the functioning of developed embedded RO plant status monitoring unit. Open-source Qtopia platform has been used for graphical user interface development for data visualization and user interaction. Developed software package provides the number of facilities for hasslefree operation and regular maintenance. Few of the major features are on-site set point window for location-specifc thresholds of pH, TDS, fow rate, real-time data visualization of various RO plant parameters, multiple data transfer options and RO plant operation steps in the local language. The main software module initializes the various water quality sensors, fow sensors, level sensors, pressure sensors, analog-to-digital converter, E2ROM, Bluetooth module, serial port, GSM module, port expander module, phase failure monitoring unit and also diagnosis of overall embedded unit. Microcontroller unit communicates with developed dedicated hardware unit using the I2C protocol to drive various actuators and also to acquire information from various sensors. Developed software package has menu-driven option with four diferent modes to operate RO plant status monitoring unit: First is data visualization mode, second is location-specifc set point mode, third is data transfer mode, and the last one is training mode. Data visualization mode provides facility to access various RO plant parameters in real time and also to drive plant in diferent modes such as process mode, rinse mode, chemical wash mode and water wash mode. Location-specifc set point mode has options to set upper and lower thresholds for critical sensors response such as pH, TDS and fow. System triggers alarm for RO plant operator as real-time sensors response crosses set points. Data transfer mode provides real-time data transfer options to cloud and server using 2G GSM module or operator's smartphone-based app interface while the training mode provides stepwise points for RO plant operation in the local language. All developed modular programs are linked to the main menu graphical user interface-based program to operate RO plant status monitoring unit for fault prediction and predictive maintenance. Raspbian Jessie OS has been ported raspberry pi-based embedded system and further developed software package transferred on raspberry pi 3-based embedded system.

# **Smartphone‑based android app and Web page‑based data visualization and analytics interface**

Data communication from embedded RO plant status monitoring unit to cloud or Web server is a challenging and diffcult task in diferent Indian remote locations. One of the major challenges faced during the installation of RO plant status monitoring units at diferent villages is the availability of network for data transfer. Initially, 2G GSM module has been used to communicate data from RO plant status monitoring system to the server, but various problems have been faced related to network availability. The strength of diferent frm's network changes from village to village. A new innovative approach of data transfer from embedded unit to the cloud has been implemented to tackle abovementioned problems. Proposed approach consists of twostep data transfer: First is from embedded RO monitoring unit to the smartphone-based android app, and second is from smartphone to cloud using operators smartphone. A dedicated smartphone-based app interface has been developed to transfer data from RO plant status monitoring unit to smartphone and further to cloud. Open-source android studio platform has been used for smartphone-based app interface development. Developed smartphone-based app interface provides a front end view to display diferent RO plant parameters such as pH, TDS, feed and product water fow, input power status, input and output tank level, input pipeline status, plant modes running status and the overall status of the plant. The developed app also provides options to transfer per minute RO plant data along with location information to Google frebase cloud. Further, a dedicated Web page has been developed to access the cloud for realtime data visualization. The developed Web page provides real-time information of all installed RO plant process variables such as feed and product pH, TDS, fow rate, pressure along with various operation modes (process mode, rinse mode, chemical wash mode and water wash mode) duration information. The user can easily access real-time data or status of any RO plant by just clicking on its location on Google map. Android app also has the ability to save per day data on smartphone memory in Excel fle format. It also provides facility to take a picture RO plant location and transfer to cloud as a backup of the location information. Android app

![](_page_5_Picture_8.jpeg)

also integrates all RO plants data with location information to Google map for easy understanding, quick judgment and action. Overall data transfer scheme (Fig. [5\)](#page-6-0) from RO plant status monitoring unit to user interface is as follows.

# **Algorithms for early fault prediction and predictive maintenance**

Reverse osmosis (RO) membrane fouling and scaling are one of the main challenges for the membrane manufactures, the scientifc community and industry professionals. Membrane fouling and scaling phenomenon have a negative efect on the RO desalination system. Predicting fouling and scaling in RO systems are the key challenges and also important to evaluate the long-term performance and cost. As membrane is one of the important and costly elements of reverse osmosis plant, continuously chemical wash and water are required to increase the life of the membrane. Regular chemical and water wash decreases the chances of early membrane fouling and scaling. Researchers have presented various techniques and methods for membrane fouling prediction for diferent water treatment methods such microfltration (Liu et al. [2009](#page-9-13); Davis [1992;](#page-9-14) Duclos-Orsello et al. [2006\)](#page-9-15), reverse osmosis (Ruiz-García et al. [2017;](#page-9-16) Yiantsios et al. [2005](#page-9-17)), but no signifcant efort has been observed in the direction of an portable embedded system development for early fault prediction and predictive maintenance for reverse osmosis plant. Developed RO plant status monitoring unit has been integrated with 2000-LPH reverse osmosis plant installed in institute campus and continuously operated six hours daily for 10 days. Real-time data from various sensors have been acquired episodically using developed RO plant status monitoring unit. Real-time fow rate, pressure and water quality sensors data of feed and product water have been acquired for 7 days continuously. Water wash process has been performed to clean the RO membrane after each day data acquisition process. It has been observed that feed water parameters are almost constant while product water parameters also change very slowly over the time period. The sampling rate for data acquisition of sensors integrated with RO plant has optimized based on the study and observation and fxed at one hour (Fig. [6\)](#page-7-0). Real-time pressure sensors (P1, P2 and P3 in Fig. [4](#page-4-0)) and fow sensors (F1, F2 in Fig. [4\)](#page-4-0) responses have been used to measure the overall fow rate of feed and product water. pH and TDS sensors responses have been used to judge the quality of feed and product water. Overall acquired data have been used to design the models to

![](_page_6_Figure_6.jpeg)

<span id="page-6-0"></span>**Fig. 5** Overall communication scheme for developed embedded RO plant status monitoring unit

![](_page_6_Picture_8.jpeg)

<span id="page-7-0"></span>**Fig. 6** Flow rate and water quality variation in feed and product water

predict membrane fouling and scaling events, and based on this information system generates an early warning and also predicts various predictive actions such as chemical wash, water wash, membrane replacement. Membrane efciency analysis (Fig. [7](#page-7-1)) has been carried out using real-time sensors data, and it has been observed that efciency of the reverse osmosis plant decreases over the time period of operation.

It also has been observed that efciency of the reverse osmosis plant depends over the membrane chemical wash, water wash and backwash frequencies. Efciency analysis

![](_page_7_Figure_7.jpeg)

<span id="page-7-1"></span>**Fig. 7** Efciency analysis of reverse osmosis membrane over the time period of 15 days

![](_page_7_Picture_9.jpeg)

can clearly indicate the membrane scaling event, as membrane efciency suddenly goes down monotonically up to 25 percent. Artifcial neural network (ANN)-based techniques have been implemented in MATLAB 2015a to predict membrane fouling and scaling event. Multi-input- and single output-based architecture has been used to predict membrane fouling and scaling event. Five plant parameters such as feed and product water fow rate, product water quality parameters (pH, TDS) and water wash frequency along with plant operation time have been used as input in input layer and predict single output membrane efciency in output layer. The optimal number of neurons in hidden layer has been achieved using trial-and-error method. Hidden layer neurons have been varied from 1 to 7, and obtained results have been compared in the context of complexity, computation time and accuracy. Two mostly explored training algorithms such as Levenberg–Marquardt and Bayesian

<span id="page-8-0"></span>**Table 1** Performance comparison of two diferent training techniques used of membrane scaling and fouling prediction

| Training algorithm  | Number of<br>neurons | Testing R2 | MSE (testing) |
|---------------------|----------------------|------------|---------------|
| Bayesian regulation | 1                    | 99.97      | 0.129687      |
| Bayesian regulation | 3                    | 99.99      | 8.8855×10−8   |
| Bayesian regulation | 5                    | 99.99      | 1.2814×10−10  |
| Bayesian regulation | 7                    | 99.99      | 4.0055×10−9   |
| Levenberg–Marquardt | 3                    | 99.952     | 0.243723      |
| Levenberg–Marquardt | 4                    | 100        | 1.1371×10−5   |
| Levenberg–Marquardt | 6                    | 99.998     | 0.028779      |
| Levenberg–Marquardt | 8                    | 100        | 0.00025786    |

regulation have been implemented in MATLAB 2015a to achieve the best results. Further, performance of both training algorithms (Table [1\)](#page-8-0) has been compared on the basis of mean square error, number of neurons and accuracy, and the fnal weight and bias values have been updated on RO plant status monitoring unit to predict plant efciency, and based on the variation in membrane efciency, system generates a silent alarm indicator to indicate the membrane fouling and scaling event.

Total samples dataset (75 samples) has been divided into three diferent datasets such as training, testing and validation. Training dataset consists of 70% of the dataset while testing and validation dataset consists of 15% each. Training process has been stopped as mean square error stops improving. Mean square with the variation in the number of neurons in the hidden layer has been analyzed for both training algorithms (Fig. [8\)](#page-8-1). Out of both training techniques, Bayesian regulation training algorithm performs the best with the lowest mean square error (1.2814×10−10), less number of neurons in hidden layer (5) and with the highest accuracy (*R*2=99.99%).

# **Testing and feld trial results**

Developed embedded RO plant status monitoring unit has been tested with RO plant installed at institute campus having a capacity of 2000 LPH. Tested RO plant status monitoring unit has been installed along with various preexisting RO plants having a capacity of 500–2000 LPH at ten diferent nearby villages of Rajasthan such as Tamkor, Googne ki Dhani, Raboodi, Mukha ka bas, Jhunjhunu to monitor

![](_page_8_Figure_9.jpeg)

<span id="page-8-1"></span>**Fig. 8** Mean square error variation with the number of neurons in hidden layer

![](_page_8_Picture_11.jpeg)

the real-time status of RO plants. It has been observed that developed RO plant status monitoring unit provides realtime data of RO plant parameters and it is also able to predict various events related to membrane behavior such as membrane scaling and fouling. System also predicts various maintenances regarding actions such as membrane chemical wash, water wash, replacement of membrane, wrong operation of RO plant, emergency power shutdown. The developed system also has autofault diagnosis capability to detect and report internal errors related to sensors and circuit damage.

# **Discussion and conclusion**

This paper reported a portable reverse osmosis status monitoring unit for early fault diagnosis and predictive maintenance. Developed systems monitor various plant parameters such as feed and product water fow rate, pressure, pH, TDS, over- and undersupply voltage, input and output water tank level. Developed system provides early fault detection related to membrane fouling, scaling, sensors damage, dry running of pumps, a wrong operation of plant and many more. The system also suggests various predictive actions to plant operator at regular interval to avoid faults. A smartphone-based app interface with various advanced features such data collection from embedded RO plant status monitoring unit further transfers it to cloud. Developed app interface also provides facility to integrate real-time plant data to the Google map with location information for quick understanding and rapid maintenance action. Diferent ANN-based algorithms have been explored to predict membrane efciency using various reverse osmosis plant parameters as input. The present idea to monitor the status of reverse osmosis plant and early predict various faults avoids the situation of non-operation of RO plant and also increases the life of the overall plant. It also guides plant operator regarding various operation steps, faults and maintenance actions at regular interval. The overall developed system is cost-efective, portable and easy to use for villagers or any unskilled person.

**Acknowledgements** Authors wanted to thank Director CEERI for allowing us to develop such technology and also to publish this work. Authors also wanted to extend their gratitude to Department of Science and Technology (DST), New Delhi, for funding such innovative project. Authors wanted to thank group members for providing their support in system testing and installation.

**Open Access** This article is distributed under the terms of the Creative Commons Attribution 4.0 International License [\(http://creativeco](http://creativecommons.org/licenses/by/4.0/) [mmons.org/licenses/by/4.0/](http://creativecommons.org/licenses/by/4.0/)), which permits unrestricted use, distribution, and reproduction in any medium, provided you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made.

### **References**

- <span id="page-9-5"></span>Abbas A (2006) Model predictive control of a reverse osmosis desalination unit. Desalination 194(1-3):268–280
- <span id="page-9-7"></span>Armbrust N, Sbarbaro D (2010) On the robust tuning of controllers with recycle compensators. IFAC Proc Vol 43(21):211–217
- <span id="page-9-8"></span>Bartman AR et al (2010) Minimizing energy consumption in reverse osmosis membrane desalination using optimization-based control. J Process Control 20(10):1261–1269
- <span id="page-9-9"></span>Chaabene AB, Sellami A (2013) A novel control of a Reverse Osmosis desalination system powered by photovoltaic generator. In: 2013 International conference on electrical engineering and software applications (ICEESA), IEEE
- <span id="page-9-14"></span>Davis RH (1992) Modeling of fouling of crossfow microfltration membranes. Sep Purif Methods 21(2):75–126
- <span id="page-9-15"></span>Duclos-Orsello C, Li W, Ho C-C (2006) A three mechanism model to describe fouling of microfltration membranes. J Membr Sci 280(1-2):856–866
- <span id="page-9-4"></span>Gambier A, Andrea W, Essameddin B (2006) Optimal control of a reverse osmosis desalination plant using multi-objective optimization. Computer aided control system design, 2006 IEEE international conference on control applications, 2006 IEEE international symposium on intelligent control, 2006 IEEE
- <span id="page-9-11"></span>Hwang T-M et al (2010) Prediction of membrane fouling rate by neural network modeling. Desalin Water Treat 15(1–3):134–140
- <span id="page-9-1"></span>Janghorban Esfahani I et al (2016) Control performance evaluation of reverse osmosis desalination system based on model predictive control and PID controllers. Desalin Water Treat 57(55):26692–26699
- <span id="page-9-6"></span>Kumar VV, Rao VSR, Chidambaram M (2012) Centralized PI controllers for interacting multivariable processes by synthesis method. ISA Trans 51(3):400–409
- <span id="page-9-3"></span>Lee YG et al (2009) Artifcial neural network model for optimizing operation of a seawater reverse osmosis desalination plant. Desalination 247(1–3):180–189
- <span id="page-9-13"></span>Liu Q-F, Kim S-H, Lee S (2009) Prediction of microfltration membrane fouling using artifcial neural network models. Sep Purif Technol 70(1):96–102
- <span id="page-9-16"></span>Ruiz-García A, Melián-Martel N, Nuez I (2017) Short review on predicting fouling in RO desalination. Membranes 7(4):62
- <span id="page-9-0"></span>Sobana S, Rames CP (2011) Identifcation, modelling, and control of continuous reverse osmosis desalination system: a review. Sep Sci Technol 46(4):551–560
- <span id="page-9-12"></span>Taherkordi A, Frank E (2016) Scalable modeling of cloud-based iot services for smart cities. Pervasive computing and communication workshops (PerCom Workshops), IEEE
- <span id="page-9-10"></span>Torky OM, Irraivan E, Hanif NHHBM (2009) PC based SCADA system for reverse osmosis desalination plants. In: 2009 IEEE student conference on research and development (SCOReD), IEEE
- <span id="page-9-17"></span>Yiantsios SG, Sioutopoulos D, Karabelas AJ (2005) Colloidal fouling of RO membranes: an overview of key issues and eforts to develop improved prediction techniques. Desalination 183(1–3):257–272
- <span id="page-9-2"></span>Zilouchian A, Jafar M (2001) Automation and process control of reverse osmosis plants using soft computing methodologies. Desalination 135(1-3):51–59

**Publisher's Note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional afliations

![](_page_9_Picture_27.jpeg)
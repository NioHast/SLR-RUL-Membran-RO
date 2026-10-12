Hindawi Publishing Corporation e Scientific World Journal Volume 2014, Article ID 807693, 11 pages http://dx.doi.org/10.1155/2014/807693

![](_page_0_Picture_2.jpeg)

# *Research Article*

# **Thermal Cycling Life Prediction of Sn-3.0Ag-0.5Cu Solder Joint Using Type-I Censored Data**

# **Jinhua Mi, Yan-Feng Li, Yuan-Jian Yang, Weiwen Peng, and Hong-Zhong Huang**

*School of Mechanical, Electronic and Industrial Engineering, University of Electronic Science and Technology of China, No. 2006, Xiyuan Avenue, West Hi-Tech Zone, Chengdu, Sichuan 611731, China*

Correspondence should be addressed to Yan-Feng Li; yanfengli@uestc.edu.cn

Received 7 February 2014; Revised 9 June 2014; Accepted 10 June 2014; Published 8 July 2014

Academic Editor: Nirupam Chakraborti

Copyright © 2014 Jinhua Mi et al. This is an open access article distributed under the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.

Because solder joint interconnections are the weaknesses of microelectronic packaging, their reliability has great influence on the reliability of the entire packaging structure. Based on an accelerated life test the reliability assessment and life prediction of lead-free solder joints using Weibull distribution are investigated. The type-I interval censored lifetime data were collected from a thermal cycling test, which was implemented on microelectronic packaging with lead-free ball grid array (BGA) and fine-pitch ball grid array (FBGA) interconnection structures. The number of cycles to failure of lead-free solder joints is predicted by using a modified Engelmaier fatigue life model and a type-I censored data processing method. Then, the Pan model is employed to calculate the acceleration factor of this test. A comparison of life predictions between the proposed method and the ones calculated directly by Matlab and Minitab is conducted to demonstrate the practicability and effectiveness of the proposed method. At last, failure analysis and microstructure evolution of lead-free solders are carried out to provide useful guidance for the regular maintenance, replacement of substructure, and subsequent processing of electronic products.

## **1. Introduction**

With the development of electronic devices, the highintegrity and portability as well as the layout design have become important features of modern electronic devices. However, they are also encountered with some challenges in the electronic industry. The potential random vibrations and thermal shocks directly affect the quality and reliability of electronic devices [1–3] during transportation process and daily usage. According to statistical analysis presented in [1], about 70 percent of the electronic product failures are packaging structural failures. Solder joints are used to transmit the electrical signal and also serve as structural support of microelectronic structures. As a weak point of the electronic packaging structures, the solder joints of electronic products often suffer from the joint effect of electricity, heat, and load. The main failures of the solder joints include thermally induced failures, mechanically induced failures, and electrochemically induced failures [2, 3].

With the increase of environmental protection awareness and the European Union (EU) legislation on restriction of the use of certain hazardous substances (RoHS) and waste electrical and electronic equipment (WEEE) [4] taken effect in July 2006, Pb solders have been gradually replaced by SnAgCu alloys which are lead-free solders. However, such materials have many limitations, such as low durability and frangibility, which emerged in the service, especially in the high strain-stress situations. Due to the coefficients of thermal expansion (CTE) mismatch among surface mount components, printed circuit boards (PCBs), and solders, the solder joints will suffer from periodic stress and strain. It can cause crack initiation and propagation in the solders and eventually lead to functional failure of entire packaging structure [5]. Over the past decades, lots of researchers have focused on improving the reliability of lead-free solders which suffer from a joint effect of load, heat, and electricity during their lifecycle [6–11]. The mechanical properties of the solders, such as mechanical fatigues, thermal fatigues, shock, and creep deformations, have raised many concerns [6–9]. There are lots of studies on electromigration of the solder joints under high current density and the mechanical properties of BGA solder joints [10, 11]. The reliability study of the solder joints possesses high academic value and good market prospect.

The fatigue life of a solder joint is a basic merit of its reliability. Several fatigue life models, including Coffin-Manson model, Engelmaier model, and Solomon model, have been proposed based on plastic strain of solders [12–14]. Darveaux presented a life prediction model with 4 correlation coefficients, which has been widely used in the solder joint life prediction [15]. There are some creep strain-based fatigue models, such as the Knecht and Fox model and the Syed model [16], which are used to predict the creep fatigue life of solder joints. When the effect of plastic and creep strain is considered, Miner's linear superposition thermo can be applied to combine the plastic strain-based model with the creep strain-based model, and it can also be used to calculate the number of cycles to failure of products [16, 17].

Generally, it is hard to obtain exact failure time of modern products, especially for electronic products with high reliability. We commonly get different kinds of censored data, such as fixed-time censoring data and fixed-number censoring data, which are separately called type-I and type-II censored data. For censored data, Chen et al. [18, 19] presented a maximum likelihood estimate (MLE) method based on several kinds of censored data with Log-normal distribution and Weibull distribution. Huang et al. [20] proposed a new Bayesian reliability analysis method for processing fuzzy lifetime data. Many works related to type-I and type-II censored data have been presented by Balakrishnan et al. [21, 22]. However, according to the literature review, there is no work related to the fatigue life prediction of lead-free solder joints with censored data gathered from accelerated life tests.

In this paper, a thermal cycling test of lead-free ball grid array (BGA) and fine-pitch ball grid array (FBGA) connection structures is conducted, and failure data are collected. A fatigue life model and a type-I interval censored data processing method are used to predict the cycles to failure of lead-free solder joints. In order to verify the practicability and effectiveness of the proposed method, the results obtained by the proposed method are compared with the ones obtained by Minitab statistical software which is based on the built-in MLE method with two-parameter Weibull distribution. The Matlab curve fitting toolbox is used to check whether the lifetime of solder joint follows the Weibull distribution.

The remainder of this paper is organized as follows. The thermal cycling tests are introduced in Section 2. Section 3 briefly reviews the modified Engelmaier model and the analysis method for Type-I censored data. In Section 4, the failure and microstructure of solder interface are analyzed first. Then, the fatigue life of solder joints based on the theory introduced in Section 3 is obtained. A comparison of predicted lifetime between the modified Engelmaier model and Matlab numerical simulation is conducted. We then conclude the paper in Section 5.

## 2. Thermal Cycling Test

2.1. Device under Test. This paper focuses on the life prediction of BGA and FBGA (Sn-3.0Ag-0.5Cu (wt.%)) packages. Figure 1(a) depicts the bottom side of a BGA package. The

perfect symmetrical distribution of the solder balls can be observed. The package dimension is  $35\times35\times3.63~\mathrm{mm}^3$  with an array of  $34\times34~\mathrm{Sn}3.0\mathrm{Ag}0.5\mathrm{Cu}$  (SAC305) solder balls, where each solder ball has a diameter of  $600~\mu\mathrm{m}$ . Ignoring the first mark point, there are 1155 solder balls, and each of them has a height of  $0.5\pm0.1~\mathrm{mm}$  and  $1~\mathrm{mm}$  pitch. The package dimension of the FBGA is  $14\times10\times1.1~\mathrm{mm}^3$  as shown in Figure 1(b). There are 136 solder balls with an array of  $8\times17$  symmetrical distribution. The height is  $0.35\pm0.05~\mathrm{mm}$  and ball pitch is  $0.8~\mathrm{mm}$ . Figure 2(a) shows the basic structure of the BGA package, and Figure 2(b) shows the detailed package structure of BGA interconnection structures.

The samples used in this paper were fabricated on printed circuit board assemblies (PCBAs) with qualified functionality, which have passed online testing, visual testing, and functional testing. Flame Retardant 4 (FR-4) substrates with Cu pads were used to assemble various components by SnAgCu solder pasted through a standard surface mounting technology (SMT) process. The  $T_g$  point (glass transition temperature) of FR-4 is from 130°C to 145°C, and it can withstand a temperature ranging from 260°C to 280°C, which makes it possible to meet the requirements of the lead-free SMT

2.2. Design of Experiment (DOE). According to the JEDEC Standard of JESD22-A104C [23], an accelerated temperature cycling (ATC) test was conducted in a thermal chamber, where the temperature ranged from -40°C to 125°C. Each cycle lasted for 1 hour, including a 15-minute dwelling at −40°C and 125°C, respectively, and 15 minutes for ramping up and cooling down, as shown in Figure 3. The cycling began by ramping from an ambient temperature (25°C) to the highest temperature (125°C). Thus, for the analysis of cycling phase, the zero strain reference temperature was set to the ambient temperature. When the thermal cycling was completed at 250, 500, 750, 1000, 1500, 2000, and 2500 cycles for the BGA solder joints and 300, 600, 800, 1000, 1400, 1800, 2200, and 2500 cycles for the FBGA solder joints, 2 samples were taken out at each observation cycle. They are prepared by cross section, dye and pry, and standard metallographic procedures (grinding, polishing, and etching). Scanning electron microscope (SEM) was used to characterize the microstructures of the prepared solder matrices. At last, failure data were collected for reliability analysis, and failure analysis was performed on the assemblies.

## 3. Basic Theories of Fatigue Life Prediction

3.1. Fatigue Theory of Lead-Free Solder Joint Life Prediction. In the Coffin-Manson fatigue life model [13], the number of cycles to failure of solder joint  $(N_f)$  can be expressed as an exponential relationship. It is established by the fatigue ductility coefficient  $(\varepsilon_f')$ , the fatigue ductility exponent (c), and the plastic strain amplitude of each cycle  $(\Delta \varepsilon_p)$ , which is given as follows:

$$\frac{\Delta \varepsilon_p}{2} = \varepsilon_f' (2N_f)^c. \tag{1}$$

8086, 2014, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2014/807693 by Nat Prov Indonesia, Wiley Online Library on [11/10/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Ceravite Commons. Licensee the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Ceravite Commons. Licensee the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Ceravite Commons. Licensee the Commons and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Ceravite Commons. Licensee the Commons and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Ceravite Commons. Licensee the Commons and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Ceravite Commons. Licensee the Commons and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of u

![](_page_2_Picture_2.jpeg)

FIGURE 1: Package dimension of the BGA and the FBGA: (a) the BGA package and (b) the FBGA package.

![](_page_2_Picture_4.jpeg)

FIGURE 2: The detail package structure of the BGA (a) basic structure and (b) the details of the BGA.

![](_page_2_Figure_6.jpeg)

FIGURE 3: ATC thermal profile.

Equation (1) is suitable for the case where the damage of solders completely depends on the plastic deformation. When some other factors, such as creep and plastic relaxation, are considered, the Coffin-Manson fatigue life model is modified as the Engelmaier fatigue model [14]. The number of cycles to failure of fatigue damage is determined by the total shear strain and the modified fatigue ductility index c. The fatigue life  $N_f(x\%)$  at a given failure probability x of surface mount solder attachment is given by [24]

$$N_f(x\%) = 0.5 \left(\frac{\Delta \gamma}{2\varepsilon_f}\right)^{1/c} \left(\frac{\ln(1 - 0.01x)}{\ln 0.5}\right)^{1/m},$$
 (2)

where  $\Delta \gamma$  is the cyclic fatigue damage (the cyclic plastic strain range),  $\varepsilon_f$  is the fatigue ductility coefficient, and m is the Weibull shape parameter. The modification of the fatigue ductility exponent c takes the effect of the temperature  $T_s$  and the cycle frequency f into account, and  $c = -0.442 - (6 \times 10^{-4})T_s + 1.74 \times 10^{-2} \ln(1+f)$ . Considering the influence of the creep fatigue, the cyclic fatigue damage  $\Delta \gamma$  used in (2) can be replaced by  $\Delta D$  which is the cycle fatigue damage parameter and contains the creep damage and plastic relaxation [25]. When plastic and creep strain is the cause for solder joints fatigue crack, according to Miner's linear superposition theorem, we can get a plastic deformation and creep based fatigue life equation by combining the Knecht and Fox creep model with the Solomon fatigue model [16, 17].

When x = 50, we can get  $\ln(1 - 0.01x) / \ln 0.5 = 1$ , and (2) can be simplified to [26]

$$N_f(50\%) = 0.5 \left(\frac{\Delta \gamma}{2\varepsilon_f}\right)^{1/c}.$$
 (3)

3.2. Type-I Censored Data Processing. In engineering practice, especially in storage reliability research, the following situation often happens. Suppose that the observation time points are denoted as  $c_1, \ldots, c_n$  and assume that the product fails at time  $c_i$ , then the result is recorded as  $\delta_i = 1$ ; otherwise,

The Scientific World Journal

it is recorded as  $\delta_i = 0$ . The results  $\delta_1, \dots, \delta_n$  can be expressed as follows [18]:

$$\delta_i = \begin{cases} 1, & x_i \le c_i \\ 0, & x_i > c_i \end{cases} \quad (i = 1, \dots, n), \tag{4}$$

where  $x_1, \ldots, x_n$  are the real fatigue life of n products. However, the values of  $x_1, \ldots, x_n$  may not be observed. We further assume that they are independently identically distributed. The Weibull distribution is used since it is one of the most commonly used distributions in reliability engineering. The distribution function of lifetime T is denoted as  $F(t,\theta)$  ( $\theta \in \Theta$ ), and its probability density function is  $f(t,\theta)$ . Here  $\Theta$  is a nonempty open set of  $R^m$ , which represents the set of distribution parameters. When the life of electronic product T follows a Weibull distribution, we have

$$P(T \le t) = F(t; \eta, m) = \begin{cases} 1 - \exp\left\{-\left(\frac{t}{\eta}\right)^m\right\}, & t > 0, \\ 0, & t \le 0, \end{cases}$$
(5)

where  $\eta$  is the scale parameter and m is the shape parameter with  $\eta > 0$  and m > 0.

The probability density function of the two-parameter Weibull distribution is  $f(t) = (m/\eta)(t/\eta)^{m-1} \exp\{-(t/\eta)^m\}$ . The failure rate function is  $\lambda(t) = (m/\eta)(t/\eta)^{m-1}$ , and the mean time to failure is MTTF =  $\eta \cdot \Gamma(1+1/m)$  [27, 28]. The reliability of products at mission time  $t_0$  can be expressed as  $R(t_0) = P(T > t_0) = \exp\{-(t/\eta)^m\}$ . The reliable life of the products having reliability of R can be obtained as  $t_R = \eta(-\ln R)^{1/m}$ .

The product life distribution function is  $F_s(t; \eta_s, m_s)$  in an actual working environment, and the lifetime T follows this distribution function in accelerated life test environment. The corresponding likelihood function of the observed data  $\delta_1, \ldots, \delta_n$  can be expressed as follows [18, 19]:

$$L(\eta, m) = \prod_{i=1}^{n} \left[ F'(c_i; \eta, m) \right]^{\delta_i} \left[ 1 - F(c_i; \eta, m) \right]^{1 - \delta_i}$$

$$= \prod_{i=1}^{n} \left[ 1 - \exp\left\{ -\left(\frac{c_i}{\eta}\right)^m \right\} \right]^{\delta_i} \left[ \exp\left\{ -\left(\frac{c_i}{\eta}\right)^m \right\} \right]^{1 - \delta_i}.$$
(6)

And the log-likelihood function is given as follows:

ln L

$$= \ln \left\{ \prod_{i=1}^{n} \left[ 1 - \exp \left\{ -\left(\frac{c_i}{\eta}\right)^m \right\} \right]^{\delta_i} \left[ \exp \left\{ -\left(\frac{c_i}{\eta}\right)^m \right\} \right]^{1 - \delta_i} \right\}$$

$$= l(\lambda, m)$$

$$= \sum_{i=1}^{n} \left[ \delta_i \ln \left( 1 - \exp \left\{ -\left(\frac{c_i}{\eta}\right)^m \right\} \right) - (1 - \delta_i) \lambda c_i^m \right], \tag{7}$$

where  $\lambda = \eta^{-m}$ . The derivative of  $\lambda$  is given as follows:

$$\frac{\partial l}{\partial \lambda} = \sum_{i=1}^{n} c_i^m - \sum_{i=1}^{n} \frac{\delta_i c_i^m}{1 - \exp\left\{-\left(c_i/\eta\right)^m\right\}}.$$
 (8)

If the range of m can be obtained as  $m \in [m_1, m_2]$  and  $0 < \sum_{i=1}^n \delta_i < n$ , then  $\partial l/\partial \lambda$  is a strict continuous increasing function. And if  $\widehat{\lambda} = \widetilde{\lambda}(\widehat{m})$ ,  $\widehat{\lambda}$  and  $\widehat{m}$  are the maximum likelihood estimation of  $\lambda$ , m, respectively.

When  $0 < \sum_{i=1}^{n} \delta_i < n$ , the following method can be used to obtain  $\widehat{\lambda}$  and  $\widehat{m}$ . If  $m_1 = m^{(1)} < m^{(2)} < \cdots < m^{(l)} = m_2$  and  $m^{(i+1)} - m^{(i)}$  are extremely small, the dichotomy method [18] can be used to solve the following formula at each  $m^{(k)}$ :

$$\sum_{i=1}^{n} \frac{\delta_{i} c_{i}^{m^{(k)}}}{1 - \exp\left\{-\lambda c_{i}^{m^{(k)}}\right\}} = \sum_{i=1}^{n} c_{i}^{m^{(k)}}.$$
 (9)

When all  $\lambda^{(k)}$  are obtained,  $k_0$  satisfies  $l(\lambda^{(k_0)}, m^{(k_0)}) = \max\{l(\lambda^{(k)}, m^{(k)}) : k = 1, 2, \dots, l\}$ . Then, the corresponding  $\lambda^{(k_0)}$  and  $m^{(k_0)}$  can be determined.

3.3. Acceleration Factor Modeling. In order to extrapolate the normal life characteristics, the life characteristics under a high stress should be used. There are four commonly used acceleration models, that is, the Arrhenius model, the inverse power law model, the Eyring model, and the temperature-humidity model. The acceleration factor (AF) is an important parameter used in the accelerated life testing. It is the ratio from the normal stress life characteristics to the life characteristics under a high stress level.

An extension has been developed by Norris and Landzberg [29]. The computation of the acceleration factor  $AF_{NL}$  for SnPb eutectic can be expressed as [30]

$$AF_{NL} = \frac{N_0}{N_t} = \left(\frac{\Delta T_t}{\Delta T_0}\right)^{1.9} \left(\frac{f_0}{f_t}\right)^{0.333} \times \exp\left\{1414\left(\frac{1}{T_{\max,0}} - \frac{1}{T_{\max,t}}\right)\right\}.$$
(10)

The calculation of the AF depends on the temperature difference between the  $\Delta T_0$  and the  $\Delta T_t$ , the cycle frequencies  $f_0$  and  $f_t$ , and the maximum temperatures  $T_{\max,0}$  and  $T_{\max,t}(\mathbf{K})$ . An alternative modification of the Norris and Landzberg (NL) model was introduced by Pan et al. [31]. It accounts for the dwell time  $t_0$  and  $t_t$  instead of the cycle frequency as it affects the creep damage the most. The Pan model (modified NL model) can be expressed as follows:

$$AF_{\text{Pan}} = \frac{N_0}{N_t} = \left(\frac{\Delta T_t}{\Delta T_0}\right)^{2.65} \left(\frac{t_t}{t_0}\right)^{0.136} \times \exp\left\{2185 \left(\frac{1}{T_{\text{max},0}} - \frac{1}{T_{\text{max},t}}\right)\right\},$$
(11)

where  $N_0$  and  $N_t$  represent the numbers of cycles to failure at a service condition and a test condition, respectively.

5

The Scientific World Journal

#### 4. Results and Discussions

4.1. Failure Analysis and Microstructure Evolution. Figure 4 shows the dye and pry images of the BGA solder joints under normal and polarized lights after 2500 cycles. The edge of every solder ball has been dyed seriously, and the dyed area of some solder joints reaches 100% in BGA side. Figure 5 is cross section images of the solders after 2500 thermal cycles. Cracks occur firstly at the interface of solder and Cu pad and have a tendency to extend along with the intermetallic compounds (IMC) layer. This test shows that the fatigue fracture of lead-free solder joints under the thermal cycling test is creep fracture, where the crack initiation always occurs in external edges of solders. The cracks are more obvious at the four corners of solders and devices under the maximal load as shown in Figure 5(b).

Figures 6(a) and 6(b) show the cross section SEM images of solder joints after 2500 thermal cycles. The interfaces of the solder joints are mainly composed of scallop-type Cu<sub>6</sub>Sn<sub>5</sub> after reflowing, and the mixtures of Ag<sub>3</sub>Cu and Cu<sub>6</sub>Sn<sub>5</sub> form some white particles around IMC layer. With the increase of thermal cycles, the IMC layers of solder joints are gradually formed by Cu<sub>6</sub>Sn<sub>5</sub> and Cu<sub>3</sub>Sn; then a layer of Cu<sub>3</sub>Sn grows up between Cu pad and Cu<sub>6</sub>Sn<sub>5</sub>. This is because the chemical reaction of atom Cu and Sn generates Cu<sub>3</sub>Sn and then Cu<sub>3</sub>Sn layer keeps growing with thermal cycles, which makes the scallop-type of IMC layer turn into flat-type. The area around the SnAgCu/Cu interface has become the weak point of the solder ball, because the increasing Cu<sub>3</sub>Sn layer has obvious fragility and low strength. This will cause crack initiation and propagation in the solders and further reduce the reliability of the solder joints.

#### 4.2. Test Data Processing Based on Previous Methods

4.2.1. Life Prediction Based on Engelmaier Model. Prior to the use of the Engelmaier fatigue model for life prediction of solder joints, the three parameters in (3) must be determined, where the creep fatigue is not considered in the Engelmaier fatigue model. According to the previous results [32], the fatigue ductility coefficient  $\varepsilon_f=0.325$  was used for a eutectic tin-lead solder. The fatigue ductility exponent c can be calculated by

$$c = -0.442 - \left(6 \times 10^{-4}\right) T_{SJ} + 1.74 \times 10^{-2} \ln\left(1 + \frac{360}{t_d}\right),\tag{12}$$

where  $T_{\rm SJ}$  is a mean cyclic solder joint temperature during accelerated temp cycling (°C),  $t_d$  is a half cycle dwell time (minutes), and  $360/t_d$  represents the cyclic frequency and  $1 \le 360/t_d \le 1000$  cycles/day [32]. The cyclic fatigue damage  $\Delta \gamma$  for a lead-free solder can be written as follows:

$$\Delta \gamma = F\left(\frac{L_D}{h}\right) \Delta \alpha \Delta T_e = F\left(\frac{L_D}{h}\right) \left(\alpha_s \Delta T_s - \alpha_c \Delta T_c\right), \quad (13)$$

where h is the nominal height of the solder joint,  $2L_D$  is the maximum distance between the solder joints of component,  $\alpha_s$ ,  $\alpha_c$ ,  $\Delta T_s$ , and  $\Delta T_c$  are coefficients of thermal expansions

(CTE) and the cyclic temperatures of substrate and component, respectively, and  $\Delta\alpha$  represents the absolute difference between CTE of component and substrate (CTE mismatch). F is an empirical correction factor under idealized assumptions. The value of F varies from 0.5 to 1.5 and is set to 1 for lead-free solder SnAgCu [33]. It is assumed that temperature variation is relatively slow, and the temperature is evenly distributed in the component and the substrate. As a result,  $\Delta T_s$  equals c=-0.57 and further results in  $\Delta T_e=\Delta T_s=\Delta T_c$  [24]

The parameters of the Engelmaier fatigue model for (3), (12), and (13) are listed in Table 1. The zero stress reference temperature  $T_0$  has no effect on the analysis result of cyclical loading. With the ambient temperature  $T_0=25^{\circ}\mathrm{C}$ , based on the defined package assembly architecture in Table 1, the cycles to failure caused by the thermal cycle are calculated by using (2) and (3). The parameter c=-0.401 is then determined. The fatigue lives for BGA and FBGA solder joints at 50% failure probability are  $N_f(50\%)_{\mathrm{BGA}}=2146.2$  and  $N_f(50\%)_{\mathrm{FBGA}}=2375$ , respectively [34].

According to the previous studies, the fatigue ductility exponent c is within the range from -0.5 to -0.7 for common engineering metals [26]. For SnPb solder, c = -0.442, and SnAgCu solder, c = -0.57. The Engelmaier fatigue prediction method is applied. A comparison of predicted fatigue life between the two exponents with the fatigue ductility exponent in this paper that c = -0.401 is depicted in Figure 7. From this figure, we can conclude that the cyclic fatigue damage changes with the number of cycles to failure at different fatigue ductility exponents.

The result shown in Figure 7 indicates that the cyclic fatigue damage  $\Delta \gamma$  (the cyclic plastic strain range) is decreasing as the test cycles at a different fatigue ductility exponent are increasing. The change of the fatigue ductility exponent c has a great influence on the mean number of cycles to failure at a fixed  $\Delta \gamma$ .

4.2.2. Life Prediction Based on Type-I Censored Data. Solder joint fails when its dyed area reaches up to 30% or the number of failed solder joints is no less than 10 percent of the total number at observation time  $c_k$ . The connection structure is considered as failure, which means  $\delta_k=1$ . According to Section 3, the collected type-I interval censored data are tabulated in Table 2. They are the inputs from (6) to (9) for calculating the scale parameter  $\eta$  and shape parameter m of the Weibull distribution. Based on these data, we have obtained that  $\eta_1=3104.5, m_1=1.1$  for BGA and  $\eta_2=3185, m_2=1.44$  for FBGA, respectively.

In the case of Weibull distribution, Minitab statistical software is used to analyze the experiment data (for BGA and FBGA) and calculate m using a built-in MLE method. The input data of Minitab are collected and settled in Table 3 [35]. The slope of the line, the  $\eta$ , the characteristic life, and the point at which 63.2% of the items in the data set have failed can be calculated. At last, with the aid of Minitab internal functions, the probability plot of cycles to failure is obtained by using the MLE method and it is shown in Figure 8, where the x-axis is the observation time and the

![](_page_5_Picture_3.jpeg)

FIGURE 4: Optical images (200x) of dye penetration and dye rate. (a) 45%, (b) 100%, (c) 50% under polarized light, (d) 100% under polarized light.

![](_page_5_Figure_5.jpeg)

FIGURE 5: Crack image after 2500 thermal cycles. (a) A complete solder joint and (b) a corner of BGA side.

*y*-axis is the cumulative failure probability. Figure 9 shows the cumulative failure plot of cycles to failure of the BGA and FBGA solder joints on 95% confidence interval; the scale parameter and the shape parameterof BGA solder are  $\eta_1' = 3002.4$  and  $m_1' = 1.7113$ , respectively. For FBGA, these two parameters are  $\eta_2' = 3052$  and  $m_2' = 1.8617$ .

At the same time, Matlab curve fitting toolbox is used to analyze the data from this experiment. The fitted curves of the Weibull distribution for the BGA and FBGA solder joints are shown in Figure 10, and the 95% prediction bounds of fitted Weibull distribution are plotted in Figure 11. The shape parameters and scale parameters of the BGA and FBGA

8086, 2014, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2014/807693 by Nat Prov Indonesia, Wiley Online Library on [11/10/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Ceravite Commons. Licensee the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Ceravite Commons. Licensee the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Ceravite Commons. Licensee the Commons and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Ceravite Commons. Licensee the Commons and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Ceravite Commons. Licensee the Commons and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Ceravite Commons. Licensee the Commons and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of use of u

![](_page_6_Figure_2.jpeg)

![](_page_6_Figure_3.jpeg)

FIGURE 6: SEM image of the solder joint interface at the BGA side after 2500 thermal cycles.

TABLE 1: The parameters for the Engelmaier fatigue model.

| Parameters       | Explanation                                                                | BGA (SAC305) | FBGA (SAC305) |
|------------------|----------------------------------------------------------------------------|--------------|---------------|
| $\overline{L_D}$ | $2L_D$ is the maximum distance between the solder joints of component (mm) | 23.3345      | 7.7666        |
| h                | The nominal height of the solder joint (mm)                                | 0.42         | 0.25          |
| $\Delta T$       | Cyclic temperature $\Delta T_e = \Delta T_s = \Delta T_c$ (°C)             | 165          | 165           |
| F                | Empirical correction factor ([0.5, 1.5])                                   | 1            | 1             |
| $\varepsilon_f$  | Fatigue ductility coefficient                                              | 0.325        | 0.325         |
| $T_0$            | Zero stress reference temperature (°C)                                     | 25           | 25            |
| $t_d$            | A half cycle dwell time (mins)                                             | 15           | 15            |

TABLE 2: Type-I interval censored data of ATC.

| $C_i$      | 0                       | 250                                                                                               | 500                                                                                           | 750                                                                                                                                                                 | 1000                                                 | 1500                                        | 2000                                                 | 2500                                                  |
|------------|-------------------------|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|---------------------------------------------|------------------------------------------------------|-------------------------------------------------------|
| $\delta_i$ | 0                       | 0                                                                                                 | 1                                                                                             | 0                                                                                                                                                                   | 0                                                    | 1                                           | 1                                                    | 0                                                     |
| $C_i$      | 0                       | 250                                                                                               | 500                                                                                           | 750                                                                                                                                                                 | 1000                                                 | 1500                                        | 2000                                                 | 2500                                                  |
| $\delta_i$ | 0                       |                                                                                                   |                                                                                               |                                                                                                                                                                     |                                                      |                                             |                                                      | 1                                                     |
| $c_i$      | 300                     | 600                                                                                               | 800                                                                                           | 1000                                                                                                                                                                | 1400                                                 | 1800                                        | 2200                                                 | 2500                                                  |
| $\delta_i$ | 0                       | 0                                                                                                 | 0                                                                                             | 1                                                                                                                                                                   | 0                                                    | 0                                           | 1                                                    | 0                                                     |
| $C_i$      | 300                     | 600                                                                                               | 800                                                                                           | 1000                                                                                                                                                                | 1400                                                 | 1800                                        | 2200                                                 | 2500                                                  |
| $\delta_i$ | 0                       | 0                                                                                                 | 0                                                                                             | 0                                                                                                                                                                   | 1                                                    | 0                                           | 0                                                    | 1                                                     |
|            | $S_i$ $S_i$ $S_i$ $S_i$ | $ \begin{array}{ccc} S_i & 0 \\ \varepsilon_i & 0 \\ S_i & 0 \\ \varepsilon_i & 300 \end{array} $ | $S_i = 0 = 0$ $c_i = 0 = 250$ $S_i = 0 = 0$ $c_i = 300 = 600$ $S_i = 0 = 0$ $c_i = 300 = 600$ | $\begin{array}{llll} S_i & 0 & 0 & 1 \\ c_i & 0 & 250 & 500 \\ S_i & 0 & 0 & 0 \\ c_i & 300 & 600 & 800 \\ S_i & 0 & 0 & 0 \\ c_i & 300 & 600 & 800 \\ \end{array}$ | $\begin{array}{cccccccccccccccccccccccccccccccccccc$ | $S_i$ 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 | $\begin{array}{cccccccccccccccccccccccccccccccccccc$ | $ \begin{array}{cccccccccccccccccccccccccccccccccccc$ |

 $m_1''$ ,  $\eta_1''$ ,  $m_2''$ , and  $\eta_2''$ , as well as the three other parameters, the sum of squares due to an error of the fitted curve (SSE), the R-square coefficient of determination, and the root mean square error (RMSE), which characterize the goodness of fit, are obtained and listed in Table 4. The comparison of the fatigue life predicted by using Engelmaier fatigue model and type-I interval censored data processing method with the ones obtained for SAC305 BGA and FBGA solder joints using Matlab and Minitab is shown in Figure 12.

4.2.3. Acceleration Factor Estimation. Since the Coffin-Manson is more conservative than the NL model and the Pan model in terms of estimating the acceleration factor, the activation energy of the NL model is calibrated for SnPb solder alloys. In this paper, for SnAgCu solder alloys, the Pan model is used to calculate the acceleration factor for predicting field life. The test condition and parameters of (11) are listed in Table 5. Then the acceleration factor under the Pan model is obtained:

$$AF_{\text{Pan}} = \frac{N_0}{N_t}$$

$$= \left(\frac{\Delta T_t}{\Delta T_0}\right)^{2.65} \left(\frac{t_t}{t_0}\right)^{0.136}$$

$$\times \exp\left\{2185 \left(\frac{1}{T_{\text{max},0}} - \frac{1}{T_{\text{max},t}}\right)\right\}$$

$$= \left(\frac{165}{60}\right)^{2.65} \left(\frac{1}{0.25}\right)^{0.136} \exp\left\{2185 \left(\frac{1}{353} - \frac{1}{398}\right)\right\}$$

$$= 35.5.$$
(14)

It means that the Pan acceleration factor of this thermal cycling test is approximated to be 35.5.

|                       | BG                       | A                    |                              | FBGA                  |                          |                      |                              |  |
|-----------------------|--------------------------|----------------------|------------------------------|-----------------------|--------------------------|----------------------|------------------------------|--|
| Initial time (cycles) | Inspection time (cycles) | Failure<br>frequency | Cumulative failure prob. (%) | Initial time (cycles) | Inspection time (cycles) | Failure<br>frequency | Cumulative failure prob. (%) |  |
| 0                     | 250                      | 0                    | 0                            | 0                     | 300                      | 0                    | 0                            |  |
| 250                   | 500                      | 5                    | 0                            | 300                   | 600                      | 5                    | 3.68                         |  |
| 500                   | 750                      | 71                   | 0.43                         | 600                   | 800                      | 9                    | 10.29                        |  |
| 750                   | 1000                     | 129                  | 6.58                         | 800                   | 1000                     | 4                    | 13.24                        |  |
| 1000                  | 1500                     | 168                  | 17.75                        | 1000                  | 1400                     | 10                   | 20.59                        |  |
| 1500                  | 2000                     | 74                   | 32.29                        | 1400                  | 1800                     | 17                   | 33.09                        |  |
| 2000                  | 2500                     | 123                  | 41.3                         | 1800                  | 2200                     | 14                   | 43.38                        |  |
| 2500                  | *                        | 556                  | 51.95                        | 2200                  | 2500                     | 8                    | 49.26                        |  |

2500

TABLE 3: The input data of Minitab.

TABLE 4: The results obtained by using Matlab.

| Parameters | m"                   | $\eta''$ | SSE     | R-square | RMSE   |
|------------|----------------------|----------|---------|----------|--------|
| BGA        | 1.658 (1.087, 2.229) | 2919     | 0.0059  | 0.9709   | 0.0385 |
| FBGA       | 1.769 (1.762, 1.776) | 3073     | 0.00096 | 0.9947   | 0.0126 |

TABLE 5: Parameters for acceleration factor calculations.

| Parameters      | T <sub>max</sub> (°C) | T <sub>min</sub> (°C) | ΔT (°C) | Cycles<br>per hour | Dwell time (mins) |
|-----------------|-----------------------|-----------------------|---------|--------------------|-------------------|
| Test condition  | 125                   | -40                   | 165     | 1                  | 15                |
| Field condition | 80                    | 20                    | 60      | 0.25               | 360               |

4.3. Discussions. The failure analysis and microstructure evolution of the solder joints in this test show that the fatigue fracture of the lead-free solder joints under thermal cycling test is creep fracture. The crack initiation always occurs in external edges of solders. Cracks are mainly grown at the interface of solder and Cu pad and have a tendency to extend along with the intermetallic compounds (IMC) layer. With the increase of thermal cycles, the IMC layers of solder joints are gradually divided into two layers, namely, Cu<sub>6</sub>Sn<sub>5</sub> layer and Cu<sub>3</sub>Sn layer. Because of the obvious fragility caused by the increase of IMC layer and holes in solders, SnAgCu/Cu interface becomes the weak point of the whole solders with a low strength.

Figure 12 compares the predicted life of the BGA and FBGA lead-free solder joints obtained using the modified Engelmaier fatigue model and the Type-I interval censored data processing method with the results obtained using Matlab curve fitting and Minitab statistical software. For the BGA solders, the median life obtained by using the modified Engelmaier fatigue model is 2146.2 cycles, the life got from type-I interval censored data processing method is 3002.4 cycles, and the characteristic life calculated by Matlab and Minitab software is 2919.4 cycles. For FBGA solder joints, these four predictions of life are 2375, 3185, 3052, and 3073 cycles, respectively.

The basic theory of Matlab curve fitting toolbox is Powell's Dogleg Method, which is a hybrid algorithm originating from the Levenberg-Marquardt method and the Newton-steepest

![](_page_7_Figure_12.jpeg)

69

FIGURE 7: The predictions of Engelmaier fatigue model.

descent method. Powell's Dogleg Method is an excellent algorithm for nonlinear curve fitting, and the fitting results have high credibility [36]. If the parameter of SSE is close to 0, it is indicated that the model fitting is good, and the data prediction is credible. The coefficient of determination, Rsquare, characterizes the quality of the curve fitting through data changing. If R-square is close to 1, it means that the variable of the equation has strong ability to explain the function and this model fits the data well. Minitab statistical software, which is based on the built-in maximum likelihood estimation (MLE) method, is used to estimate the Weibull parameters. It adopts similar principle with type-I interval censored data processing method which is introduced in Section 3. Matlab and Minitab are used to analyze the experimental data, respectively. The results obtained using those two prediction methods can represent the experiment condition approximately.

From Table 4, we know that for the BGA,  $SSE_1 = 0.005943$  and R-square<sub>1</sub> = 0.9709 and for the FBGA,  $SEE_2 = 0.000957$ 

![](_page_8_Figure_2.jpeg)

![](_page_8_Figure_3.jpeg)

Variable

→ Initial time (BGA)

-- Initial time (FBGA)

FIGURE 8: The probability plot of cycles to failure.

![](_page_8_Figure_6.jpeg)

FIGURE 9: The cumulative failure plot of cycles to failure.

and R-square<sub>2</sub> = 0.9947. Both SSEs are close to 0 and both R-squares are close to 1, which mean the curve fitting by Matlab is effective and accurate. All of these predictions match the experimental results with a high confidence, and the methods used in this paper are applicable for lead-free solder joint life prediction. In Section 4.2, the shape and scale parameters for the BGA using Matlab curve fitting toolbox are m=1.658 and  $\eta=2919.4$ , respectively. The acceleration factor of this test is nearly 35.5, and the number of cycles to failure under the normal operating condition can be estimated easily. Using

![](_page_8_Figure_9.jpeg)

FIGURE 10: The fitting curve of Weibull distribution (the BGA and the FBGA).

![](_page_8_Figure_11.jpeg)

FIGURE 11: Analysis of two-parameter Weibull distribution fitting (the BGA and the FBGA).

the equations in Section 3, the reliability characteristics of SAC305 lead-free solder joint including MTTF,  $R(t_0)$ , and  $t_R$  can be calculated.

Using the modified Engelmaier fatigue model to predict solder joint fatigue life (cycles to failure) is only associated with the total shear strain and the modified fatigue ductility exponent, where these two parameters can be obtained easily. Therefore, without considering other effect factors, this model is an effective method for the solder joint lifetime prediction. The results obtained in this paper show that the type-I interval censored data processing method which is applicable for censored data generated from accelerated life

![](_page_9_Figure_3.jpeg)

FIGURE 12: A comparison of the BGA and the FBGA solders fatigue life obtained using different methods.

tests is an effective method to predict fatigue life of lead-free solder joints.

#### 5. Conclusions

The modified Engelmaier fatigue model is a reasonable and effective method for estimating the fatigue life of solder interconnects. However, this model is more conservative than other models. Through the analyses of the censored lifetime data of thermal cycling tests, it is found that the type-I censored data processing method is an effective method to predict the life of solder joint. The comparison study carried out using Minitab indicates that the type-I interval censored data processing method can predict the failure life of leadfree solder joint effectively. This study shows that the fatigue fracture of lead-free solder joint under thermal cycling test is creep fracture, and the crack initiation always occurs at the interface of solder and Cu pad. The IMC layer is gradually divided into Cu<sub>6</sub>Sn<sub>5</sub> and Cu<sub>3</sub>Sn layers, and the area close to SnAgCu/Cu interface has become the weak point of the whole solder because of the fragility introduced by the increase of IMC layer and holes in solders. Being the weaknesses of microelectronic packaging, the reliability of solder joint interconnections affects the reliability of the entire structure. The prediction of the solder joint life can offer suggestions for regular maintenance, replacement of substructure, and subsequent processing of electronics.

#### **Conflict of Interests**

The authors declare that there is no conflict of interests regarding the publication of this paper.

## **Acknowledgments**

This research is partially supported by the National Natural Science Foundation of China under the Contract no. 11272082 and the Fundamental Research Funds for the Central Universities under the Contract no. YBXSZC20131040. The authors would like to express special thanks to the cooperation of Regional Technology Center located in Flextronics Zhu

Hai Industry Park (B15) and Mr. BY Wu, Mr. C Huang in Flextronics, and Miss ZM Cao in Chongqing University for their helpful discussions. Last, the authors appreciate the reviewers for their constructive comments on this paper.

#### References

- [1] D. S. Steinberg, Vibration Analysis for Electronic Equipment, John Wiley & Sons, 2nd edition, 1988.
- [2] D. Chicot, K. Tilkin, K. Jankowski, and A. Wymysłowski, "Reliability analysis of solder joints due to creep and fatigue in microelectronic packaging using microindentation technique," *Microelectronics Reliability*, vol. 53, no. 5, pp. 761–766, 2013.
- [3] X. Zhou, Board level lead-free solder joints reliability analysis under drop shock loading [M. S. dissertation], Shanghai Jiao Tong University, 2007.
- [4] Directive 2002/96/EC of the European Parliament and of the Council of January 2003 on Waste Electronic and Electrical Equipment (WEEE), p. 15, 2003.
- [5] Y. X. Ning, K. L. Pan, and N. Li, "Failure analysis of solder joints in electronic assemblies," *Equipment for Electronic Products Manufacturing*, vol. 36, no. 9, pp. 46–50, 2007.
- [6] Q. K. Zhang, Q. S. Zhu, H. F. Zou, and Z. F. Zhang, "Fatigue fracture mechanisms of Cu/lead-free solders interfaces," *Materials Science and Engineering A*, vol. 527, no. 6, pp. 1367–1376, 2010.
- [7] T. Tsai, C. Yeh, Y. Lai, and R. Chen, "Transient submodeling analysis for board-level drop tests of electronic packages," *IEEE Transactions on Electronics Packaging Manufacturing*, vol. 30, no. 1, pp. 54–62, 2007.
- [8] J. Varghese and A. Dasgupta, "An experimental approach to characterize rate-dependent failure envelopes and failure site transitions in surface mount assemblies," *Microelectronics Reliability*, vol. 47, no. 7, pp. 1095–1102, 2007.
- [9] P. Arulvanan, Z. Zhong, and X. Shi, "Effects of process conditions on reliability, microstructure evolution and failure modes of SnAgCu solder joints," *Microelectronics Reliability*, vol. 46, no. 2–4, pp. 432–439, 2006.
- [10] F. L. Sun, J. B. Wang, Y. Liu, and G. J. Wang, "Electromigration of SnAgCu-Bi-Ni Pb-free micro solder joints," *Journal of Harbin University Science and Technology*, vol. 17, no. 3, pp. 1–4, 2012.
- [11] A. S. G. Andrae and O. Andersen, "Life cycle assessment of integrated circuit packaging technologies," *The International Journal of Life Cycle Assessment*, vol. 16, no. 3, pp. 258–267, 2011.
- [12] W. Engelmaier, "Fatigue life of leadless chip carrier solder joint during power cycling," *IEEE transactions on components*, hybrids, and manufacturing technology, vol. 6, no. 3, pp. 232–237, 1983.
- [13] W. Engelmaier, "Solder attachment reliability, accelerated testing, and result evaluation," in *Solder Joint Reliability—Theory and Applications*, J. H. Lau, Ed., pp. 545–587, Van Nostrand Reinhold of ITP, New York, NY, USA, 1991.
- [14] W. Engelmaier, "Generic reliability figures of merit design tools for surface mount solder attachments," *IEEE Transactions on Components, Hybrids, and Manufacturing Technology*, vol. 16, no. 1, pp. 103–112, 1993.
- [15] R. Darveaux, "Solder joint fatigue life model in design and reliability of solders and solder interconnections," in *The Minerals, Metals and Materials Society*, pp. 213–218, Metals and Materials Society, Orlando, Fla, USA, 1997.

8086, 2014, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/2014/807693 by Nat Prov Indonesia, Wiley Online Library on [11/10/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

- [16] W. W. Lee, L. T. Nguyen, and G. S. Selvaduray, "Solder joint fatigue models: review and applicability to chip scale packages," *Microelectronics Reliability*, vol. 40, no. 2, pp. 231–244, 2000.
- [17] L. Zhang, S. Xue, F. Lu, Z. Han, S. Yu, and Z. Lai, "Fatigue life prediction for fine pitch device soldered joints based on creep model," *Journal of Mechanical Engineering*, vol. 45, no. 9, pp. 279–284, 2009.
- [18] J. D. Chen and X. Z. Fang, "The reliability evaluation in the case of Weibull or log-normal distributions," *Jouranl of Application Statistics and Management*, vol. 31, no. 5, pp. 835–848, 2012.
- [19] J. D. Chen, *Survival Analysis and Reliability*, Peking University Press, Beijing, China, 2005.
- [20] H. Z. Huang, M. J. Zuo, and Z. Q. Sun, "Bayesian reliability analysis for fuzzy lifetime data," *Fuzzy Sets and Systems*, vol. 157, no. 12, pp. 1674–1686, 2006.
- [21] N. Balakrishnan, D. Han, and G. Iliopoulos, "Exact inference for progressively Type-I censored exponential failure data," *Metrika*, vol. 73, no. 3, pp. 335–358, 2011.
- [22] N. Balakrishnan, H. K. T. Ng, and J. Navarro, "Linear inference for type-II censored lifetime data of reliability systems with known signatures," *IEEE Transactions on Reliability*, vol. 60, no. 2, pp. 426–440, 2011.
- [23] JEDEC Solid State Technology Association, JESD22-A104C. Temperature cycling, 2005.
- [24] J. Sarkk ¨ a, ¨ *A novel method for hazard rate estimates of the second level interconnections in infrastructure electronics [Academic Dissertation]*, University of Oulu, 2008.
- [25] X. Li and Y. Yan, "Reliability and life prediction methodologies for solder joints of electronic packages," *Journal of Mechanical Strength*, vol. 27, no. 4, pp. 470–479, 2005.
- [26] N. Blattau and C. Hillman, "A comparison of the isothermal fatigue behavior of SnAgCu to SnPb solder," in *Proceedings of the International Annual Conference on Surface Mount Technology Association (SMTA '05)*, pp. 884–890, Chicago, Ill, USA, September 2005.
- [27] X. J. Tian, "Cooling fan reliability: failure criteria, accelerated life testing, modeling and qualification," in *Proceedings of the Annual Reliability and Maintainability Symposium (RAMS '06)*, pp. 380–384, January 2006.
- [28] H. Li, Z. Zhang, Y. Hu, and D. Zheng, "Maximum likelihood estimation of weibull distribution based on random censored data and its application," in *Proceedings of the 8th International Conference on Reliability, Maintainability and Safety (ICRMS '09)*, pp. 302–304, July 2009.
- [29] K. C. Norris and A. H. Landzberg, "Reliability of controlled collapse interconnections," *IBM Journal of Research and Development*, vol. 13, no. 3, pp. 266–271, 1969.
- [30] J. Reichelt, P. Gromala, and S. Rzepka, "Accelerating the temperature cycling tests of FBGA memory components with leadfree solder joints without changing the damage mechanism," in *Proceedings of the European Microelectronics and Packaging Conference (EMPC '09)*, June 2009.
- [31] N. Pan, G. A. Henshall, F. Billaut et al., "An acceleration model for Sn-Ag-Cu solder joint reliability under various thermal cycle conditions," in *Proceedings of the MTA International Conference*, pp. 876–883, 2006.
- [32] R. D. Gerke and G. B. Kromann, "Solder joint reliability of high I/O ceramic-ball-grid arrays and ceramic quad-flat-packs in computer environments: the PowerPC 603TM and PowerPC 604TM microprocessors," *IEEE Transactions on Components and Packaging Technologies*, vol. 22, no. 4, pp. 488–496, 1999.

- [33] H. Qi, M. Osterman, and M. Pecht, "A rapid life-prediction approach for PBGA solder joints under combined thermal cycling and vibration loading conditions," *IEEE Transactions on Components and Packaging Technologies*, vol. 32, no. 2, pp. 283– 292, 2009.
- [34] K. C. Otiaba, R. S. Bhatti, N. N. Ekere, S. Mallik, and M. Ekpu, "Finite element analysis of the effect of silver content for Sn-Ag-Cu alloy compositions on thermal cycling reliability of solder die attach," *Engineering Failure Analysis*, vol. 28, pp. 192–207, 2013.
- [35] C. Huang, *Reliability research on SAC305 lead-free solder joint under thermal and mechanical stress [M.S. thesis]*, Guilin University of Electronic Technology, 2013.
- [36] J. Nocedal and S. J. Wrignt, *Numerical Optimization*, pp. 258– 278, Springer, Berlin, Germany, 2006.
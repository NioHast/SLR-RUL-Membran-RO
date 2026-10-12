![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_1.jpeg)

Case Report

# Numerical Modelling Assisted Design of a Compact Ultrafiltration (UF) Flat Sheet Membrane Module

Mokgadi F Bopape <sup>1,2,\*</sup>, Tim Van Geel <sup>1,\*</sup>, Abhishek Dutta <sup>3</sup>, Bart Van der Bruggen <sup>1,2</sup> and Maurice Stephen Onyango <sup>2</sup>

- Department of Chemical Engineering, KU Leuven, Celestijnenlaan 200F, B-3001 Leuven, Belgium; bart.vanderbruggen@kuleuven.be
- Department of Chemical, Metallurgical and Materials Engineering, Tshwane University of Technology (TUT), Private Bag X680, Pretoria 0001, South Africa; OnyangoMS@tut.ac.za
- Department of Chemical Engineering, Izmir Institute of Technology, Gülbahçe Campus, Urla, Izmir 35430, Turkey; abhishekdutta@iyte.edu.tr
- \* Correspondence: mokgadifredericka.bopape@kuleuven.be (M.F.B.); tim.vangeel@kuleuven.be (T.V.G.)

Abstract: The increasing adoption of ultra-low pressure (ULP) membrane systems for drinking water treatment in small rural communities is currently hindered by a limited number of studies on module design. Detailed knowledge on both intrinsic membrane transport properties and fluid hydrodynamics within the module is essential in understanding ULP performance prediction, mass transfer analysis for scaling-up between lab-scale and industrial scale research. In comparison to hollow fiber membranes, flat sheet membranes present certain advantages such as simple manufacture, sheet replacement for cleaning, moderate packing density and low to moderate energy usage. In the present case study, a numerical model using computational fluid dynamics (CFD) of a novel custom flat sheet membrane module has been designed in 3D to predict fluid flow conditions. The permeate flux through the membrane decreased with an increase in spacer curviness from 2.81 L/m²h for no (0%) curviness to 2.73 L/m²h for full (100%) curviness. A parametric analysis on configuration variables was carried out to determine the optimum design variables and no significant influence of spacer inflow or outflow thickness on the fluid flow were observed. The numerical model provides the necessary information on the role of geometrical and operating parameters for fabricating a module prototype where access to technical expertise is limited.

**Keywords:** ultra-low pressure (ULP); ultrafiltration (UF); simulation; computational fluid dynamics (CFD); flat sheet membrane module

# check for updates

Citation: Bopape, M.F.; Van Geel, T.; Dutta, A.; Van der Bruggen, B.; Onyango, M.S. Numerical Modelling Assisted Design of a Compact Ultrafiltration (UF) Flat Sheet Membrane Module. *Membranes* 2021, 11, 54. https://doi.org/membranes

Received: 25 October 2020 Accepted: 11 January 2021 Published: 14 January 2021

**Publisher's Note:** MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](_page_0_Picture_15.jpeg)

Copyright: © 2021 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https://creativecommons.org/licenses/by/4.0/).

## 1. Introduction

Access to drinking water is a basic human right and providing access has become an international goal as envisaged in the Sustainable Development Goals (SDGs) [1,2]. Within the South African context, the percentage of the population using safely managed drinking water services has remained constant at around 91% between 2014 and 2016 as reported in the South African SDG baseline report [3]. Approximately 26% of the population in the Mutale local municipality (Limpopo province, Venda) have poor access to municipal services (piped drinking water), leading to relatively bad access to clean drinking water [4,5]. Tsaande B, also known as Tshaanda village, is located in the Mutale Local Municipality (GPS coordinates: 22.6857 S, 30.4189 E) within the Limpopo province, South Africa [6]. With aims to combat issues related to poor water quality and supply and consequently, failure of centralized reliable water distribution networks, a pilot-scale decentralized Ultrafiltration (UF) membrane plant was installed for provision of drinking water. The plant comprised a commercial hollow fibre UF membrane (Multibore membrane housed in a dizzer XL 1.5 MB 40) for removal of bacteria, viruses, suspended particles and colloids. Moreover, the ultimate goal was to demonstrate the feasibility of membrane

*Membranes* **2021**, *11*, 54 2 of 18

technology to provide drinking water in a rural area [\[6\]](#page-15-5). The system operation started in 2014 and although the UF pilot plant could produce safe drinking water, much work was still required before this technology could be rolled-out countrywide. Successive research expansion was to include evidence of sustained use on water quality over extended periods, operation and maintenance, cost-effectiveness, system performance and optimization (considering seasonal variations), and water quality monitoring [\[6\]](#page-15-5). Up until now, no follow-up evaluation has been made. Furthermore, the dependence of the system on a commercial membrane module presented opportunities to develop a custom membrane module producible on a local scale, to lower capital cost requirements.

The development of membrane module design, fabrication and optimization on operating conditions is built on a wide range of prior arts and practical experiences. In general, the criteria for membrane module configurations include two types: namely, flat sheet and tubular membrane modules [\[7\]](#page-15-6). Numerous studies [\[8–](#page-15-7)[12\]](#page-15-8) have explored the design of the hollow-fibre (tubular) configuration [\[13\]](#page-15-9), spiral wound [\[14\]](#page-15-10) due to competitive benefits; however, the design and fabrication of hollow fibre modules is a complicated process that involves different disciplines and requires a thorough understanding of the intended application, particularly for decentralized water treatment systems [\[13](#page-15-9)[,15\]](#page-15-11). Nonetheless, a study by Oka et al. [\[16\]](#page-15-12) explored the operation of a submerged hollow-fibre UF system for drinking water for application in small/remote communities. However, the complexity of the system on auxiliary fouling control measures including backwashing, air sparging and chemical cleaning prove to be costly. Furthermore, three different configurations of bench-scale commercial submerged hollow-fibre membrane systems were used, adding more cost to the overall costs of the system. Pillay et al. [\[17\]](#page-15-13) presented a technical report on the development of a capillary ultrafiltration (CUF) system for a small-scale potable water treatment system for rural and peri-urban areas. Periodically, the information from the technical evaluations was combined with the information of sustainability needs. Once again, a commercial membrane module was used. Consequently, a guidebook on the selection of small water treatment systems for drinking water supply to small communities was published [\[18\]](#page-15-14). Although the merits and drawbacks of the different configurations can be argued, the plate and frame configuration may offer certain advantages over other module configurations, particularly for decentralized membrane water plants in small/remote communities [\[19–](#page-15-15)[21\]](#page-15-16). Flat sheet plate and frame membranes offer benefits in simplicity, better flow control on both the permeate and feed side [\[22\]](#page-15-17), ease of sheet replacement, less fouling tendency over tubular configurations (excessive fouling and membrane integrity problems) [\[7](#page-15-6)[,23\]](#page-15-18), while also being easier to prototype in a laboratory environment.

Computational fluid dynamics (CFD) is a widely integrated tool for process optimisation [\[24](#page-15-19)[,25\]](#page-16-0) and design of UF water and wastewater treatment systems to achieve a desired system performance [\[26–](#page-16-1)[35\]](#page-16-2). The fundamental characteristics of membrane module design comprises minimizing the cost per amount of mass transferred and maximizing the system performance through optimized flow geometry and operating conditions [\[9\]](#page-15-20). Moreover, other aspects in water treatment plant design may include: (1) meeting water quality standards and requirements; (2) minimizing overall project costs; and (3) controlling ongoing operating costs and maintenance requirements. Successfully achieving these objectives is dependent upon proper design and optimization of the treatment water flow systems within the plant. Numerous studies [\[35](#page-16-2)[–40\]](#page-16-3) have employed CFD tools to gain an insight into the phenomena taking place inside membrane modules [\[33](#page-16-4)[,41–](#page-16-5)[44\]](#page-16-6) and to improve the overall performance of modules. As an analysis tool, CFD provides the ability to modify operating conditions, fluid properties and geometric characteristics of the flow channels in a flexible but defined way [\[31\]](#page-16-7). For example [\[45\]](#page-16-8), the presented results on the design of a thin channel cross-flow module were for the characterization of flat ceramic membranes, with a primary objective ensuring uniform flow characteristics over the permeating area. Boundary conditions were imposed such that the flow non-uniformity was taken as the normalized standard deviation of the velocity field above the permeating area, while the pressure drops considered were those across the inlet plenum and across the permeating

*Membranes* **2021**, *11*, 54 3 of 18

area normalized with respect to the outlet pressure. Similarly [\[46\]](#page-16-9), the presented results of CFD modelling of flow within the SEPA CF flat sheet membrane filtration cell operated at low recoveries. As expected, the goal of the study was to characterize uniform flow distribution within the cell. The common Navier–Stokes governing equation was applied, with all the walls set at a no-slip boundary including the membrane. Results revealed stagnation areas in dead ends of the inlet and outlet tubes and in the channel areas behind duct entries as well as local regions of high shear in duct-channel transition areas (the flow was unidirectional over most of the channel area with exception of the corners of the channel). Another example was presented by [\[33\]](#page-16-4), who performed CFD studies on a circular cross-flow NF laboratory test cell with an aim to improve the design of the cell and to increase the filtration performance. Design variables considered were the feed chamber thickness, number and distribution of the inlet/outlet pipes, sequential mode inlets and the addition of grooves on the top surface of the cell. The two dimensional (2D) study demonstrated that the groove size and the groove interval play a significant role. Therefore, for small bench-scale cells when the use of retentate spacers is not convenient, the alternative would be to add grooves opposite to the membrane side in order to create velocity fluctuations [\[33](#page-16-4)[,47\]](#page-16-10). In general, a membrane performance is significantly influenced by the operating pressure and velocity within a membrane module; therefore, it is crucial to obtain and maintain uniform fluid flow hydrodynamic (pressure and velocity) conditions over the membrane surface [\[10,](#page-15-21)[16\]](#page-15-12). Commercially available codes are well suited for the types of simulations required to advance water and wastewater component system designs; however, each code has individual strengths and weaknesses to be considered.

To characterize the performance of a custom membrane module, this study evaluated the design, development, and modelling of fluid flow through a flat sheet plate and frame module prototype, using CFD techniques, to identify the geometry (spacer geometry, spacer thickness, inlet and outlet diameter, inlet and outlet length) and membrane parameters (permeability, membrane thickness, membrane area) that may influence the module's overall performance. Moreover, the aim of the study was to design a membrane module with uniform flow characteristics over the permeating area. Da costa et al. [\[48\]](#page-16-11) and Saeed et al. [\[43\]](#page-16-12) acknowledged that the spacer geometry is critical in module performance as it directly relates the hydrodynamics and solute transport. Therefore, the type of the spacer used will strongly influence the resulting flow and ultimately, the performance of the module [\[48](#page-16-11)[–51\]](#page-16-13). The development of a model that can be used to simulate the module prototype may give an insight [\[52\]](#page-16-14) into whether lab-scale performance corresponds with pilot scale performance, reducing the need for experiments during its optimization process and effectively reducing optimization costs. Subsequently, the model can be validated using experimental data.

# **2. Materials and Methods**

*2.1. Proposed Module Design and Fabrication* Design Dimensions and Variables

The design and development of the proposed module prototype in the present study was achieved using AutoCAD 2D as a drawing tool. Additionally, the design was based on local process conditions collected but flexible enough to be applied in a different region. The module housing consisted of two Perspex glass closing holders (thickness 20 mm), five tortuous spacers (thickness 2 mm), used for flow channelling and sealing of the stack with corresponding gaskets (thickness 2 mm). The thickness of the spacers was based on the required flow velocity on the membrane surface and their quantity was based on the membrane flux. The overall dimensions of the unit were 20 cm × 20 cm × 25 cm, while the effective membrane surface was 0.01 m<sup>2</sup> . The significance of the tortuous (plugflow) permeate spacer design was to bring about high flow velocity over the membrane (membranes arranged horizontally), to enable cleaning of the membrane surface while under operation and support the membrane sheets mechanically. No mesh in the feed side was used to avoid the possibility of heavier total suspended solid load accumulating in the

Membranes 2021, 11, 54 4 of 18

feed side. The inlet and outlet ducts were configured by etching the Perspex holder (etching depth of 1.5 mm). Valves and fittings are also important for the stack operation and thus they were designed in such a way that they are quick to connect and disconnect from tubes and completely waterproof, and most importantly, provide resistance against corrosion. Three speed controllers as quick connectors to outlet diameters were also included, to control flow and then lock to sustain the desired flow.

#### 2.2. Development of the CFD Modelling

Numerical simulation platform ANSYS® 19.2 (ANSYS Inc., Canonsburg, PA, USA) was used to model and simulate the membrane module. The geometry was designed using an ANSYS Design Modeler, while ANSYS Meshing was used to create the required grids for pre-processing. ANSYS Fluent was used to set up and solve the actual model and ANSYS CFD Post was used for post-processing tools. Simulations were carried out on two computer systems: an MSI Aegis X3 desktop computer, with 16 GB of RAM and a quad core 4.2 GHz Intel Core i7-7700K processor, overclocked to 4.5 GHz, and a MSI GE63 Raider laptop computer, with 16 GB of RAM and a hexa core 2.2 GHz Intel Core i7-8750H processor, overclocked to 4.1 GHz. A brief description of the steps followed within the ANSYS workbench GUI to set-up a CFD model, i.e., the creation of a geometry, formation of a grid (mesh), and set-up of the model by combining different models for hydrodynamics and turbulence is presented.

# 2.2.1. Geometry and Grid Creation

The geometry simulated in this study is illustrated in Figure 1. A three-dimensional (3-D) mathematical model was developed by reversing the set-up of the geometry (technical drawings), i.e., the flow path was constructed in ANSYS Design Modeler, not on the surrounding materials.

<span id="page-3-0"></span>![](_page_3_Picture_6.jpeg)

Figure 1. Top-down view of the simulated geometry. Top side is the inlet and bottom side is the outlet.

Three distinct zones in the geometry were created: an inflow zone, outlet zone and membrane zone. The inflow zone represents the inlet of the module connected to the flow path through a spacer and a retentate outlet, the outflow zone, found on the other side of the membrane zone and a membrane zone, found at the other side of the spacer when compared to the inlet as shown in Figure 2.

<span id="page-3-1"></span>![](_page_3_Picture_9.jpeg)

**Figure 2.** Side view of a part of the simulated geometry near the inlet. Visible are inlet of the inflow zone (grey), the very thin membrane zone (orange) and the outflow zone (green).

*Membranes* **2021**, *11*, 54 5 of 18

Given the sharp corners of the spacer, the spacer "curviness" was used as a measure of the roundedness of the corners of the flow field through the spacer and calculated using Equation (1) as demonstrated in Figure 3.

$$C = \frac{r_{qc}}{r_{qc, max}} \tag{1}$$

where  $r_{qc}$  is the radius of a quarter-circle replacing the corners of the flow path and  $r_{qc,max}$  is the maximal value possible for this radius within the width of the flow channels.

<span id="page-4-0"></span>![](_page_4_Picture_4.jpeg)

**Figure 3.** Graphical overview to how the "curviness" parameter ( $r_{qc}$ —green and  $r_{qc,max}$ —blue) is calculated (left) at the different corners of the spacer geometry (right). The fluid flow path within the spacer is shown in red.

The quality of a CFD solution is highly dependent on the quality of the grid (mesh). Several grids were created to run the computational domain and each grid had structured multigrid of hexahedral [53,54] cells, to reduce computational time and thus speed up convergence. In all simulation cases, the outflow zone was coarsely meshed as illustrated in Figure 4, while the membrane and the spacer zone were finely meshed, as shown in Figure 5.

<span id="page-4-1"></span>![](_page_4_Picture_7.jpeg)

**Figure 4.** Close-up view of the structured multigrid. Below the membrane is the outflow zone, meshed finely in the direction of the flow.

<span id="page-4-2"></span>![](_page_4_Picture_9.jpeg)

Figure 5. Zoomed-in side view of the membrane zone (orange) and the outflow zone (grey) grid.

To test the quality of the size of the grid cells on the simulation solution, a grid analysis was carried out. Five grids were generated, varying from coarse to fine, with

*Membranes* **2021**, *11*, 54 6 of 18

250,000, 500,000, 1,000,000, 1,500,000, and 2,000,000 cells. Based on the assumption that finer meshes typically lead to an accurate solution, but with higher computational costs, a balance between computational costs and solution accuracy is paramount. Therefore, a parametric sensitivity analysis on the geometrical parameters was conducted.

#### 2.2.2. Governing Equations

The fluid was assumed to be isothermal, incompressible, and Newtonian and a steady-state flow was formulated in the three-dimensional (3D) domain. The modelling was based on a single-phase flow and pure water flux was modelled through the module. The simulation was implemented by solving hydrodynamic Navier–Stokes governing equations, including mass and momentum conservation equations. In general, the mass and momentum conservation equations [35,55] can be expressed as follows:

$$\frac{\partial_p}{\partial_t} + \nabla \cdot (\rho v) = 0 \tag{2}$$

$$\frac{\partial(\rho v)}{\partial_t} + \nabla \cdot (\rho v \mu) = -\frac{\partial P}{\partial_y} + \nabla \cdot (\mu \nabla v) + SM_y \tag{3}$$

where  $\rho$  is the density of the fluid (kg/ m<sup>3</sup>), v is the component of the fluid velocity in the x direction (m/s),  $\mu$  is the fluid viscosity (Pa s), P is the pressure (Pa), t is time (s), and  $SM_y$  is a source term in the y direction (kg/ m<sup>2</sup> s<sup>2</sup>). For constant density fluids, the continuity equation states that the velocity field is non-divergent [31] as expressed in Equation (4).

$$\nabla \cdot v = 0 \tag{4}$$

#### 2.2.3. Solution Method

The commercial package ANSYS® 19.2 (ANSYS Inc., Canonsburg, PA, USA), based on a finite element method (FEM), was used to simulate the laminar flow in the module prototype. At the inlet, a normal inflow velocity boundary condition (i.e., imposed uniform velocity profile) was given. At the outlet, a zero-gauge pressure was set since fluid flows out of the computational domain. At all wall boundaries, even at the membrane surface on the bottom of the cell, the no-slip condition was imposed. The expressions were discretized by the Semi-Implicit Method for Pressure-Linked Equations (SIMPLE) algorithm [56], coupled with velocity to pressure in the system to solve the flow field. An iterative geometric multigrid (coarse, medium, and fine) solver was chosen. The membrane was defined as a porous zone and the pure water flux through the membrane was defined by Darcy's Law [57], calculated using Equation (5).

$$J = \frac{k}{u} \frac{\Delta p}{\Delta x} \tag{5}$$

where J is the flux (L/m²·h), k is the intrinsic permeability of the membrane (m²),  $\Delta p$  is the transmembrane pressure (TMP) over the membrane (Pa),  $\mu$  is the dynamic viscosity of the fluid passing through the membrane (Pa·s) and  $\Delta x$  is the thickness of the membrane (m). Consequently, the pores were not modelled individually, instead the membrane was regarded as a black box with a value for the intrinsic permeability inserted into Darcy's law. The intrinsic permeability for the reference case was chosen as  $4.167 \times 10^{-17}$  m², which corresponds to a permeability of 100 L/m².h.bar, when the thickness of the membrane is 150  $\mu$ m and the water viscosity is  $1 \times 10^{-3}$  Pa·s, as calculated using Equation (6),

$$K = \frac{k}{\mu \Delta x} \tag{6}$$

where *K* is the permeance, *k* is the intrinsic permeability (m<sup>2</sup>),  $\mu$  is the dynamic viscosity (Pa·s) and  $\Delta x$  the membrane thickness (m<sup>2</sup>). If a membrane with this permeability value

*Membranes* **2021**, *11*, 54 7 of 18

is used at a constant transmembrane pressure of 20,000 Pa (0.20 bar), a constant flux of 20 L/m2h can be achieved. To achieve a water flux of 5000 L of clean water per day, ca. 260 membranes of 20 cm by 20 cm are required. However, this value assumes a constant TMP, for which it cannot be achieved in a crossflow system with a spacer due to pressure drop and a complete use of the membrane area due to the spacer. To validate the performance of the model, the intrinsic permeability *k*, the transmembrane pressure (TMP) ∆*P*, the inlet pressure and the membrane thickness ∆*x* were varied in a sensitivity analysis presented in Table [1.](#page-6-0) During simulation of these parameters, only pure water flux was considered, and no fouling or concentration polarization phenomena were considered in the model.

<span id="page-6-0"></span>**Table 1.** Overview of operational parameters values used in a sensitivity analysis.

| Parameter                             |       |       |       | Value   |       |       |       |
|---------------------------------------|-------|-------|-------|---------|-------|-------|-------|
| Intrinsic Permeability (10−17 m2<br>) | 1.042 | 2.084 | 3.125 | 4.167 1 | 5.209 | 6.251 | 7.292 |
| Membrane thickness (µm)               | 50    | 100   | 150 1 | 200     | 250   | 300   | 350   |
| Inlet pressure (bar)                  | 0.05  | 0.10  | 0.15  | 0.20 1  | 0.25  | 0.30  | 0.35  |

<sup>1</sup> Values for the reference case.

# **3. Results and Discussion**

# *3.1. Grid Sensitivity Analysis*

To analyze the influence of the grid on the simulation solution quality, the cell count of the grid was varied.

# 3.1.1. Grid Cell Count Quality

Generally, it may be assumed that as the number of cells within a grid increases, the quality of the computational solution increases due to the fineness of the grid, because as the grid is refined, the numerical discretization error is reduced and the solution approaches convergence (continuous profile). Figure [6](#page-7-0) shows how the transmembrane pressure (TMP) develops throughout the spacer flow path by plotting its value along a centreline, i.e., a line drawn in the middle of the spacer flow path, at 5 mm distance from the spacer walls. The most significant differences between the five grid cells occur very close to the inlet, where pressure and velocity gradients are largest. Evidently, the pressure drops throughout the system, starting from a gauge pressure of 20,000 Pa (equal to the inlet pressure of 0.2 bar) to 0 Pa, close to the retentate outlet. This pressure drop can be related to both the lengthening of the flow path and spacer due to the frictional forces caused by the resistance to flow. Additionally, slight pressure spikes and drops around corners of the flow path defined by the spacer can be seen. This may be regarded as flow "hitting" into the walls of the spacer due to the viscous shear stresses. The pressure drop approaches linear, towards the retentate outlet, where the flow is nearly fully developed, as expected. With an assumption that increasing grid cells improves the simulation resolution (i.e., 2,000,000 grid cells), a slight difference was observed between grids with 250,000 and 500,000 cells on the one hand, and the 2,000,000-cell grid reference case on the other hand. The pressure profiles for both cases lie below the reference case. The 1,000,000 cell grid has a profile lying slightly above the reference profile, while the pressure profile for the grid with 1,500,000 cells almost entirely overlap with the pressure profile for the 2,000,000 cell grid. The difference in pressure drop from the coarse grid to the fine grid is less than 10%. Subsequently, results from the sensitivity analysis study were compared with results found for the grid with 2,000,000 cells, and in choosing the optimal grid for further simulations, a grid with 1,500,000 cells was chosen as a balance between accuracy and computational cost.

Membranes 2021, 11, 54 8 of 18

<span id="page-7-0"></span>![](_page_7_Figure_1.jpeg)

**Figure 6.** Development of the transmembrane pressure profile along the centreline in the flow path for the five grid cell counts.

#### 3.1.2. Inclusion of an Outflow Zone

The transmembrane pressure (TMP) profile along the centreline within the spacer flow path with 1,500,000 cell grid, both for an outflow zone and no outflow zone is shown in Figure 7. A distinct difference for both cases could not be established, due to the reference and outflow zone pressure profiles overlapping, inferring that TMP has no significant effect when either an outflow zone is included or when it is not, therefore removing the outflow zone could be a valid approach.

<span id="page-7-1"></span>![](_page_7_Figure_5.jpeg)

**Figure 7.** Development of TMP along the spacer flow path centreline for the 1,500,000 cell grid with an outflow zone (reference) and without an outflow zone.

The velocity contours for the spacer flow path right above the membrane are shown in Figure 8. As can be seen, the flow distribution remains uniform as the grid is refined and does not differ when either an outflow zone is included or an outflow zone is excluded, validating the assumption of excluding the outflow zone, as it does not significantly affect the simulation solution. However, the mean velocity in the system was found to decrease as the cell grid count increased. Although the pressure drop varied by a few percent as the grid is refined, the flow field remained close to zero near the spacer curviness due to the no-slip condition. Nonetheless, solutions obtained with coarse grids (250,000 and 500,000 cells) are not representative of reality due to poor quality solution.

Membranes **2021**, 11, 54 9 of 18

<span id="page-8-0"></span>![](_page_8_Figure_1.jpeg)

**Figure 8.** Velocity contour plots for the inflow path through the spacer next to the membrane, for cases with an outflow zone (upper figures) and without an outflow zone (lower figures) grids; (a) 250,000 cells, (b) 500,000 cells, (c) 1,000,000 cells, (d) 1,500,000 cells and (e) 2,000,000 cells.

# 3.2. Parametric Sensitivity Study on Geometrical Variables

Multiple geometrical parameters were varied in a series of simulations, to test the sensitivity of the model to changes in the geometry of the membrane module. The purpose was to establish optimum conditions and configurations to yield a module design with maximum performance. Table 2 lists the parameters.

<span id="page-8-1"></span>**Table 2.** Overview of geometrical parameters values used in a sensitivity analysis.

| Parameter             |     |                |     | Value    |     |     |                 |
|-----------------------|-----|----------------|-----|----------|-----|-----|-----------------|
| Spacer thickness (mm) | 0.5 | 1 <sup>2</sup> | 1.5 | 2.0      | 2.5 | 3.0 |                 |
| Spacer curviness (%)  | 02  | 20             | 40  | 60       | 80  | 100 |                 |
| Inlet length (mm)     | 10  | 15             | 20  | $25^{2}$ | 30  | 35  | 40              |
| Outlet length (mm)    | 10  | 15             | 20  | $25^{2}$ | 30  | 35  | 40              |
| Inlet diameter (mm)   | 5   | 6              | 7   | 8        | 9   | 10  | 11 <sup>2</sup> |
| Outlet diameter (mm)  | 5   | 6              | 7   | 8        | 9   | 10  | 11 <sup>2</sup> |

<sup>&</sup>lt;sup>2</sup> Values for the reference case.

#### 3.2.1. Spacer Thickness (Inflow Zone) and the Outflow Zone

The influence of the spacer thickness, i.e., the thickness of the inflow zone, on the transmembrane pressure (TMP) profile was varied with different spacer thickness values. As the spacer thickness decreases, the transmembrane pressure develops a smooth profile. When the thickness increases, the pressure drops and peaks around the corners of the spacer. This may be attributed to the thick spacer, as when the fluid flow resistance increases, it leads to high pressure drops, particularly around the spacer corners. The subsequent pressure increase, when the bend in the spacer is rounded, also increases with the thickness

Membranes **2021**, 11, 54 10 of 18

of the spacer. To characterize the influence of the spacer inflow or outflow thickness on the fluid flow, the relationship between the permeate flux and reference value is not shown, as no significant effect was found on the simulation solution.

#### 3.2.2. Spacer Curviness

The effect of the spacer curviness was varied through six simulations (i.e., 0%, 20%, 40%, 60%, 80% and 100%) and results are shown in Figure 9. No singularity was found between the pressure field profiles along the centreline within the spacer flow path for different values of curviness (insert image). However, by replacing the "blocky" geometry of the spacer with a more curved geometry, the pressure profile slightly smoothed-out. Schwinge et al. [58] characterized a zigzag spacer for ultrafiltration in spiral wound modules for water treatment applications. The zigzag spacer is thought not to be easily plugged (free from any obstacles) in the flow direction, but the tortuous channel promotes turbulence effects [58]. From the simulation solution, it was observed that when the spacer curviness percentage increased, the pressure drop was less as the pressure profile smoothed-out (stabilized). An increase in the spacer curviness percentage was found to reduce the turbulence-promoting properties of the spacer and may offer localized dead spots with poor mass transfer that encourage fouling. Nonetheless, the zigzag (tortuous) spacer with reasonable curviness may be used in the module prototype to produce a high and stable water quality over a long time frame due to lower associated pressure drop, leading to lower operational costs.

<span id="page-9-0"></span>![](_page_9_Figure_4.jpeg)

Figure 9. Development of TMP along the centerline in the flow path at different spacer curviness values.

The velocity contour profiles for flow through the spacer inflow path are shown in Figure 10. Although the flow distribution remains uniform in all six cases, the spacer curviness was found to slightly influence the progression (change) of the pressure as the fluid flows through the spacer. As the spacer curviness increases, the flow velocity developed a smoothed-out profile with values of the velocity perpendicular to the flow direction, showing an increase on the wall shear stress and thus the flow evenly distributed over the width of the pipes, especially in the bends of the geometry. This trend also illustrated that the turbulence-promoting properties of the spacer are reduced when the curviness of the spacer geometry increases, which may lead to an onset of fouling and concentration polarization (CP) phenomena when the module is in operation. To study whether this may be the case, mass transfer phenomena investigations are required.

*Membranes* **2021**, *11*, 54 11 of 18

<span id="page-10-0"></span>![](_page_10_Figure_1.jpeg)

**Figure 10.** Velocity contour plots for the inflow through the spacer next to the membrane for all curviness cases: (a) 0%, (b) 20%, (c) 40%, (d) 60%, (e) 80%, and (f) 100%.

The water flux through the module as a function of the percentage of the reference value for the curviness is shown in Figure 11. To be able to plot the other values of curviness, the percentage of the reference value as shown on the horizontal axis was defined as the value of the curviness subtracted from the 100% value for the reference, i.e., 100% corresponds to 0% curviness, 80% corresponds to 20% curviness, and so on. As can be seen, the permeate flux through the membrane slightly decreases with an increase in spacer curviness, albeit a slight decrease (from 2.81 L/m²h for 0% curviness to 2.73 L/m²h for 100% curviness). It is well acknowledged that the main parameter for predicting permeate flux is the pressure and velocity upon the membrane [38], where the pressure field depends significantly on the fluid flow pattern. Therefore, the fluid pattern played a significant role in the decrease of the permeate flux with an increased spacer curviness.

<span id="page-10-1"></span>![](_page_10_Figure_4.jpeg)

**Figure 11.** Total permeate flux leaving the module plotted as a function of the percentage of the reference value (100% corresponds to 0% curviness, 80% to 20% curviness, 60% to 40% curviness, 40% to 60% curviness, 20% to 40% curviness).

#### 3.2.3. Inlet and Outlet Pipe Length

The inlet and the retentate outlet pipe length was varied individually in two case studies consisting of seven simulations each (i.e., 10 mm, 15 mm, 20 mm, 25 mm, 30 mm, 35 mm and 40 mm). The reference value for both lengths was 25 mm. No significant pressure differences were found between the transmembrane pressure (TMP) along the length of the centreline, and therefore these profiles are not provided. A similar observation

Membranes **2021**, 11, 54 12 of 18

was also found for the permeate flux and the TMP profiles. Overall, these parameters remained uniform regardless of the inlet pipe or the outlet pipe length. For variation in the inlet length, an average value for the pure water flux through the module, taken over all cases, was  $2.822 \text{ L/m}^2\text{h}$ , with a standard deviation ( $\sigma$ ) of  $0.010 \text{ L/m}^2\text{h}$ . Similarly, the average flux value taken over all cases where the outlet length was varied, was equal to  $2.822 \text{ L/m}^2\text{h}$ , with  $\sigma = 0.011 \text{ L/m}^2\text{h}$ . Both these values are very small when compared to their corresponding average value (0.34% and 0.41% of the average value for the inlet length variation and the outlet length variation), leading to the assumption that the permeate flux does not depend on either the inlet length or the outlet length. When the TMP was averaged over the results of all cases for the inlet length, a value of 9412.7 Pa was found, with  $\sigma = 50.9 \text{ Pa}$ . The average value for the TMP for the outlet length was 9397.1 Pa, with  $\sigma = 49.5 \text{ Pa}$ . The standard deviations were 0.54% and 0.53% respectively of their corresponding average values. Similarly, these values are relatively small, and thus it may be assumed that the TMP does not depend on inlet or outlet length.

# 3.2.4. Inlet and Outlet Pipe Diameter

Two case studies were carried out in which the influence of the inlet and retentate outlet diameter was studied, with seven different values for each respective case study (i.e., 5 mm, 6 mm, 7 mm, 8 mm, 9 mm, 10 mm and 11 mm). Figure 12 shows the pure water flux as a function of the reference value (11 mm). As can be seen, a slight decrease in the permeate flux was found when the retentate outlet diameter increased. When the inlet diameter increases, a slight increase in the permeate flux was observed. This observation can be attributed to that with an increase in the inlet diameter, more water at a hydrostatic pressure of 0.2 bar is allowed to enter the membrane module at once, allowing the inlet pressure to be maintained further along the spacer flow path, and effectively reducing the pressure drop between the inlet and the retentate outlet.

<span id="page-11-0"></span>![](_page_11_Figure_4.jpeg)

**Figure 12.** Total permeate flux leaving the module plotted as a function of the percentage of the reference value.

3.3. Sensitivity Analysis on Membrane Properties and Operating Conditions

#### 3.3.1. Membrane Permeability

The influence of the intrinsic membrane permeability on the model was tested by carrying out seven different simulations with different values (i.e.,  $1.042 \times 10^{-17}$  m<sup>2</sup>,  $2.048 \times 10^{-17}$  m<sup>2</sup>,  $3.125 \times 10^{-17}$  m<sup>2</sup>,  $4.167 \times 10^{-17}$  m<sup>2</sup>,  $5.209 \times 10^{-17}$  m<sup>2</sup>,  $6.251 \times 10^{-17}$  m<sup>2</sup> and  $7.292 \times 10^{-17}$  m<sup>2</sup>). Membrane permeability, membrane thickness and inlet pressure are all important and often interdependent factors. The intrinsic membrane permeability data were compared to the relationship between the total pure water permeate flux leaving the system and the reference inlet pressure of 0.20 bar, and results are shown in Figure 13.

*Membranes* **2021**, *11*, 54 13 of 18

<span id="page-12-0"></span>![](_page_12_Figure_1.jpeg)

**Figure 13.** Relationship between intrinsic membrane permeability, total pure water flux leaving the module and membrane thickness.

As a first step of the experimental work, the system was operated in a dead-end mode to establish the flow regime and membrane resistance. For this purpose, the outlet pressure was set to be equal to the atmospheric pressure. In order to validate the CFD simulation to predict permeate flux by neglecting the membrane resistance, a linear relationship between the flux and the transmembrane pressure are obtained, which proves that the *Rc* is zero. Otherwise, due to the blocking effect of the cake, a non-linear relationship between the flux and the transmembrane is expected.

#### 3.3.2. Membrane Thickness

The membrane thickness was varied between 50  $\mu$ m, 100  $\mu$ m, 150  $\mu$ m, 200  $\mu$ m, 250  $\mu$ m, 300  $\mu$ m and 350  $\mu$ m, respectively. The pressure profile development through the spacer zone, the membrane zone and the outflow zone, found in the middle of the centreline, for each of these simulations, is shown in Figure 14. Evidently, the pressure drops throughout the membrane zone. Due to the varying membrane thickness, the slope in the decrease of the pressure in the membrane zone decreases with an increase in thickness. This occurs because transmembrane pressure remains nearly constant for all simulations, while the membrane thickness does not, and since the intrinsic permeability was defined as a constant through the entire membrane zone, (the membrane resistance was neglected), a linear relationship was found over the membrane thickness to obey Darcy's Law.

<span id="page-12-1"></span>![](_page_12_Figure_6.jpeg)

**Figure 14.** Development of the pressure profile through the spacer zone, the membrane zone and the outflow zone at different membrane thickness values.

Membranes **2021**, 11, 54 14 of 18

#### 3.3.3. Membrane Surface Area

For simulation purposes, it is desirable to have a uniform flow and fluid properties over the permeating area. Six simulations were carried out with membrane squares of 16 cm, 17 cm, 18 cm, 19 cm, 20 cm and 21 cm respectively, corresponding to area sizes of  $0.026~\text{m}^2$ ,  $0.029~\text{m}^2$ ,  $0.032~\text{m}^2$ ,  $0.036~\text{m}^2$ ,  $0.040~\text{m}^2$  and  $0.044~\text{m}^2$  respectively. The flux declined with an increase in membrane area size as shown in Figure 15, while no significant effects can be distinguished on the transmembrane pressure profile with an increase in the membrane area size. This flux decline may be attributed to that; the effective membrane area is determined by the spacer on the retentate side of the membrane. Therefore, the spacer should approximately be of the same dimensions as the membrane to obtain an optimum flux.

<span id="page-13-0"></span>![](_page_13_Figure_3.jpeg)

**Figure 15.** Total permeate flux leaving the module plotted as a function of the percentage of the reference value for surface area.

#### 3.3.4. Inlet Pressure

The relationship between the total pure water permeate flux leaving the system and the percentage of the reference value (0.20 bar) was given in Figure 13. As described before, a linear dependency was found between the inlet pressure and the permeate flux. These observations obey the Darcy's Law, where an increase in transmembrane pressure leads to a proportional increase in the permeate flux. The law was properly added to the model and simulated within the confines of the geometry and the grid.

#### 3.3.5. Overview of the Parametric Sensitivity Analysis

The overall aim of the sensitivity analysis for both the geometry and operating conditions was to define parameters that may influence the module prototype design, relating the flux through the module and the transmembrane pressure profiles (uniform fluid flow conditions). The spacer geometry and inlet diameter played a significant role in obtaining uniform permeating (flow distribution and transmembrane pressure) conditions, ultimately reducing the overall pressure drop. Table 3 lists the operational parameters comprising the inlet pressure, membrane permeability, membrane thickness and area size. All were found to have a significant influence on the permeate flux. A significant influence on the transmembrane pressure profile was found for the inlet pressure, in addition, the spacer thickness and the outlet pipe diameter also showed a significant influence on the transmembrane pressure profile. No singularity was found between the thickness of the outflow zone, the length of the inlet pipe and the length of the outlet pipe on either the permeate flux or the transmembrane pressure, while the membrane area had a significant impact on the transmembrane pressure.

*Membranes* **2021**, *11*, 54 15 of 18

| Parameter                     | Permeate Flux | Transmembrane Pressure |  |  |
|-------------------------------|---------------|------------------------|--|--|
| Spacer curviness              | ↓             | ↓                      |  |  |
| Thickness of the spacer       | ↓↓            | ↓↓                     |  |  |
| Thickness of the outflow zone | –             | –                      |  |  |
| Length of the inlet pipe      | –             | –                      |  |  |
| Length of the outlet pipe     | –             | –                      |  |  |
| Diameter of the inlet pipe    | ↑             | ↑                      |  |  |
| Diameter of the outlet pipe   | ↓↓↓           | ↓↓↓                    |  |  |
| Inlet pressure                | ↑↑↑↑          | ↑↑↑↑                   |  |  |
| Membrane permeability         | ↑↑↑↑          | ↓                      |  |  |
| Membrane thickness            | ↓↓↓↓          | ↑                      |  |  |
| Membrane area size            | ↓↓↓↓          | –                      |  |  |

<span id="page-14-0"></span>**Table 3.** Qualitative overview of several sensitivity analysis parameters on the permeate flux and the transmembrane pressure.

# **4. Conclusions**

This study presented the results from a computational fluid dynamics (CFD) numerical study on a compact membrane module prototype intended for decentralized UF drinking water purification, by characterizing the proposed design geometry and predicting the performance of the module prototype. 3D simulations on several geometry parameters were analysed within a parametric and sensitivity study. The main findings were;

- 1. The numerical simulation solution could predict permeate flux with a reasonable error. The pressure distribution upon the membrane was found to depend on the fluid flow pattern on the membrane.
- 2. A parametric analysis on configuration variables was carried out to determine the optimum design variables. The spacer geometry (tortuous spacer) with reasonable curviness was found to impact the permeating conditions and thus, may be used to produce a high and stable water quality over a long-time frame due to the lower associated pressure drop, leading to lower operational costs. The inlet diameter also showed a significant influence on the pressure drop within the system.
- 3. The sensitivity analysis on membrane properties and operating conditions revealed that the inlet pressure, membrane permeability, membrane thickness and membrane area have a significant impact on the total permeate flux.
- 4. The membrane area size provided useful information for optimization purposes: by reducing the membrane area to the size of the spacer, more, smaller membranes can be combined to obtain a higher flux.

# *Future Work*

To validate the simulation model and optimize the module design, experimental data of the pressure drop in the retentate or permeate channels with a spacer needs to be determined. This is because in module and plant design and optimization studies, permeate pressure drop is a design variable which cannot be ignored. Concentration polarization (CP) is another important factor that limits separation performance in nearly all membrane filtration processes. Thus, accurate prediction of CP and fouling phenomena is also critical for design and optimization processes.

**Author Contributions:** Conceptualization, Investigation, Methodology, Formal analysis, Data curation, Visualization, Writing—Original Draft, Writing—Review and Editing, M.F.B. and T.V.G. Supervision, Resources, Conceptualization, Visualization, Formal analysis, Writing—Review and Editing, A.D., B.V.d.B. and M.S.O. All authors have read and agreed to the published version of the manuscript.

**Funding:** This research was funded by the National Research Fund (NRF), South Africa on Freestanding Doctoral and Postdoctoral Abroad, grant number SFH150720127975.

<sup>↑</sup>: increase of either the flux or the transmembrane pressure with an increase of the parameter; ↓: decrease; –: no clear dependency between either the flux or the transmembrane pressure and the sensitivity analysis parameter.

*Membranes* **2021**, *11*, 54 16 of 18

**Institutional Review Board Statement:** Not applicable.

**Informed Consent Statement:** Not applicable.

**Data Availability Statement:** Not applicable.

**Acknowledgments:** The authors gratefully acknowledge the Tshwane University of Technology and the Nanotechnology and Water Sustainability Research Unit of the University of South Africa for permitting to use their laboratory facilities. Beyond Automatic Solutions (Pty) Ltd. is greatly thanked for fabricating the module prototype. The authors are also grateful to the reviewers and the editor for their helpful comments.

**Conflicts of Interest:** The authors declare no conflict of interest.

# **References**

<span id="page-15-0"></span>1. Watkins, K. *Human Development Report 2006-Beyond Scarcity: Power, Poverty and the Global Water Crisis. UNDP Human Development Reports 2006*; United Nations Development Programme: New York, NY, USA, 2006.

- <span id="page-15-1"></span>2. Arnal, J.; García-Fayos, B.; Sancho, M.; Verdú, G.; Lora, J. Design and installation of a decentralized drinking water system based on ultrafiltration in Mozambique. *Desalination* **2010**, *250*, 613–617. [\[CrossRef\]](http://doi.org/10.1016/j.desal.2009.09.035)
- <span id="page-15-2"></span>3. Stats, S.A. *Sustainable Development Goals: Baseline Report 2017*; Statistics South Africa: Pretoria, South Africa, 2017.
- <span id="page-15-3"></span>4. Statistics South Africa. Sustainable Development Goals: Indicator Baseline Report, Stats SA. 2017. Available online: [http:](http://www.statssa.gov.za/MDG/SDG_Baseline_Report_2017.pdf) [//www.statssa.gov.za/MDG/SDG\\_Baseline\\_Report\\_2017.pdf](http://www.statssa.gov.za/MDG/SDG_Baseline_Report_2017.pdf) (accessed on 18 August 2019).
- <span id="page-15-4"></span>5. Stats, S.A. Statistics South Africa Census 2011 Statistical Release—P0301.4/Statistics. 2012. Available online: [http://www.statssa.](http://www.statssa.gov.za/Publications/P03014/P030142011.Pdf) [gov.za/Publications/P03014/P030142011.Pdf](http://www.statssa.gov.za/Publications/P03014/P030142011.Pdf) (accessed on 19 August 2019).
- <span id="page-15-5"></span>6. Molelekwa, G.F.; Mukhola, M.S.; Van Der Bruggen, B.; Luis, P. Preliminary Studies on Membrane Filtration for the Production of Potable Water: A Case of Tshaanda Rural Village in South Africa. *PLoS ONE* **2014**, *9*, e105057. [\[CrossRef\]](http://doi.org/10.1371/journal.pone.0105057)
- <span id="page-15-6"></span>7. Caro, J. Basic Principles of Membrane Technology. *Z. Phys. Chem.* **1998**, *203*, 263. [\[CrossRef\]](http://doi.org/10.1524/zpch.1998.203.Part_1_2.263)
- <span id="page-15-7"></span>8. Li, D.; Wang, R.; Chung, T.-S. Fabrication of lab-scale hollow fiber membrane modules with high packing density. *Sep. Purif. Technol.* **2004**, *40*, 15–30. [\[CrossRef\]](http://doi.org/10.1016/j.seppur.2003.12.019)
- <span id="page-15-20"></span>9. Fane, A.G.; Chang, S.; Chardon, E. Submerged hollow fibre membrane module—Design options and operational considerations. *Desalination* **2002**, *146*, 231–236. [\[CrossRef\]](http://doi.org/10.1016/S0011-9164(02)00478-2)
- <span id="page-15-21"></span>10. Buer, T.; Cumin, J. MBR module design and operation. *Desalination* **2010**, *250*, 1073–1077. [\[CrossRef\]](http://doi.org/10.1016/j.desal.2009.09.111)
- 11. Marriott, J.; Sørensen, E.; Bogle, I. Detailed mathematical modelling of membrane modules. *Comput. Aided Chem. Eng.* **2000**, *8*, 523–528. [\[CrossRef\]](http://doi.org/10.1016/s1570-7946(00)80089-9)
- <span id="page-15-8"></span>12. Marriott, J.; Sørensen, E. A general approach to modelling membrane modules. *Chem. Eng. Sci.* **2003**, *58*, 4975–4990. [\[CrossRef\]](http://doi.org/10.1016/j.ces.2003.07.005)
- <span id="page-15-9"></span>13. Wan, C.F.; Yang, T.; Lipscomb, G.G.; Stookey, D.J.; Chung, T.-S. Design and fabrication of hollow fiber membrane modules. *J. Membr. Sci.* **2017**, *538*, 96–107. [\[CrossRef\]](http://doi.org/10.1016/j.memsci.2017.05.047)
- <span id="page-15-10"></span>14. Kostoglou, M.; Karabelas, A.J. Comprehensive simulation of flat-sheet membrane element performance in steady state desalination. *Desalination* **2013**, *316*, 91–102. [\[CrossRef\]](http://doi.org/10.1016/j.desal.2013.01.033)
- <span id="page-15-11"></span>15. Yang, X.; Wang, R.; Fane, A.G.; Tang, C.Y.; Wenten, I.G. Membrane module design and dynamic shear-induced techniques to enhance liquid separation by hollow fiber modules: A review. *Desalin. Water Treat.* **2013**, *51*, 3604–3627. [\[CrossRef\]](http://doi.org/10.1080/19443994.2012.751146)
- <span id="page-15-12"></span>16. Oka, P.; Khadem, N.; Bérubé, P. Operation of passive membrane systems for drinking water treatment. *Water Res.* **2017**, *115*, 287–296. [\[CrossRef\]](http://doi.org/10.1016/j.watres.2017.02.065) [\[PubMed\]](http://www.ncbi.nlm.nih.gov/pubmed/28285238)
- <span id="page-15-13"></span>17. Jacobs, P.E.; Pillay, V.L. The Development of Small-Scale Ultrafiltration Systems for Potable. 2004. Available online: [http:](http://www.wrc.org.za/wp-content/uploads/mdocs/1070-1-041.pdf) [//www.wrc.org.za/wp-content/uploads/mdocs/1070-1-041.pdf](http://www.wrc.org.za/wp-content/uploads/mdocs/1070-1-041.pdf) (accessed on 7 March 2019).
- <span id="page-15-14"></span>18. Swartz, C. Guidebook for the Selection of Small Water Treatment Systems for Potable Water Supply to Small Communities. 2007. Available online: <http://www.wrc.org.za/wp-content/uploads/mdocs/TT319-07.pdf> (accessed on 19 August 2019).
- <span id="page-15-15"></span>19. Peter-Varbanets, M.; Zurbrügg, C.; Swartz, C.; Pronk, W. Decentralized systems for potable water and the potential of membrane technology. *Water Res.* **2009**, *43*, 245–265. [\[CrossRef\]](http://doi.org/10.1016/j.watres.2008.10.030)
- 20. Boulestreau, M.; Hoa, E.; Peter-Verbanets, M.; Pronk, W.; Rajagopaul, R.; Lesjean, B. Operation of gravity-driven ultrafiltration prototype for decentralised water supply. *Desalin. Water Treat.* **2012**, *42*, 125–130. [\[CrossRef\]](http://doi.org/10.1080/19443994.2012.683073)
- <span id="page-15-16"></span>21. Pronk, W.; Ding, A.; Morgenroth, E.; Derlon, N.; Desmond, P.; Burkhardt, M.; Wu, B.; Fane, A.G. Gravity-driven membrane filtration for water and wastewater treatment: A review. *Water Res.* **2019**, *149*, 553–565. [\[CrossRef\]](http://doi.org/10.1016/j.watres.2018.11.062)
- <span id="page-15-17"></span>22. Baker, R.W. Membrane Technology and Applications—Richard W. Baker—Google Books. 2004. Available online: [https://books.google.co.za/books/about/Membrane\\_Technology\\_and\\_Applications.html?id=FhtBKUq4rL8C&printsec=](https://books.google.co.za/books/about/Membrane_Technology_and_Applications.html?id=FhtBKUq4rL8C&printsec=frontcover&source=kp_read_button&redir_esc=y#v=onepage&q&f=false) [frontcover&source=kp\\_read\\_button&redir\\_esc=y#v=onepage&q&f=false](https://books.google.co.za/books/about/Membrane_Technology_and_Applications.html?id=FhtBKUq4rL8C&printsec=frontcover&source=kp_read_button&redir_esc=y#v=onepage&q&f=false) (accessed on 21 August 2020).
- <span id="page-15-18"></span>23. Gu, B.; Kim, D.; Kim, J.; Yang, D.R. Mathematical model of flat sheet membrane modules for FO process: Plate-and-frame module and spiral-wound module. *J. Membr. Sci.* **2011**, *379*, 403–415. [\[CrossRef\]](http://doi.org/10.1016/j.memsci.2011.06.012)
- <span id="page-15-19"></span>24. Jardón-Pérez, L.E.; González-Rivera, C.; Ramirez-Argaez, M.A.; Dutta, A. Numerical Modeling of Equal and Differentiated Gas Injection in Ladles: Effect on Mixing Time and Slag Eye. *Processes* **2020**, *8*, 917. [\[CrossRef\]](http://doi.org/10.3390/pr8080917)

*Membranes* **2021**, *11*, 54 17 of 18

<span id="page-16-0"></span>25. Hoang, Q.N.; Ramírez-Argáez, M.A.; Conejo, A.N.; Blanpain, B.; Dutta, D. Numerical Modeling of Liquid—Liquid Mass Transfer and the Influence of Mixing in Gas-Stirred Ladles. *JOM* **2018**, *70*, 2109–2118. [\[CrossRef\]](http://doi.org/10.1007/s11837-018-3056-0)

- <span id="page-16-1"></span>26. Laurent, J.; Samstag, R.W.; Ducoste, J.M.; Griborio, A.; Nopens, I.; Batstone, D.J.; Wicks, J.D.; Saunders, S.; Potier, O. A protocol for the use of computational fluid dynamics as a supportive tool for wastewater treatment plant modelling. *Water Sci. Technol.* **2014**, *70*, 1575–1584. [\[CrossRef\]](http://doi.org/10.2166/wst.2014.425)
- 27. Samstag, R.W.; Ducoste, J.J.; Griborio, A.; Nopens, I.; Batstone, D.J.; Wicks, J.D.; Saunders, S.; Wicklein, E.A.; Kenny, G.; Laurent, J. CFD for wastewater treatment: An overview. *Water Sci. Technol.* **2016**, *74*, 549–563. [\[CrossRef\]](http://doi.org/10.2166/wst.2016.249)
- 28. Zhang, J.; Huck, P.M.; Anderson, W.B.; Stubley, G.D. A Computational Fluid Dynamics Based Integrated Disinfection Design Approach for Improvement of Full-scale Ozone Contactor Performance. *Ozone Sci. Eng.* **2007**, *29*, 451–460. [\[CrossRef\]](http://doi.org/10.1080/01919510701613420)
- 29. Meister, M.; Winkler, D.; Rezavand, M.; Rauch, W. Integrating hydrodynamics and biokinetics in wastewater treatment modelling by using smoothed particle hydrodynamics. *Comput. Chem. Eng.* **2017**, *99*, 1–12. [\[CrossRef\]](http://doi.org/10.1016/j.compchemeng.2016.12.020)
- 30. Goula, A.M.; Kostoglou, M.; Karapantsios, T.D.; Zouboulis, A.I. A CFD methodology for the design of sedimentation tanks in potable water treatment. *Chem. Eng. J.* **2008**, *140*, 110–121. [\[CrossRef\]](http://doi.org/10.1016/j.cej.2007.09.022)
- <span id="page-16-7"></span>31. Fimbres-Weihs, G.; Wiley, D.E. Review of 3D CFD modeling of flow and mass transfer in narrow spacer-filled channels in membrane modules. *Chem. Eng. Process. Process Intensif.* **2010**, *49*, 759–781. [\[CrossRef\]](http://doi.org/10.1016/j.cep.2010.01.007)
- 32. Glucina, K.; Derekx, Q.; Langlais, C.; Laîné, J.-M. Use of advanced CFD tool to characterize hydrodynamic of commercial UF membrane module. *Desalin. Water Treat.* **2009**, *9*, 253–258. [\[CrossRef\]](http://doi.org/10.5004/dwt.2009.814)
- <span id="page-16-4"></span>33. Cortés-Juan, F.; Balannec, B.; Renouard, T. CFD-assisted design improvement of a bench-scale nanofiltration cell. *Sep. Purif. Technol.* **2011**, *82*, 177–184. [\[CrossRef\]](http://doi.org/10.1016/j.seppur.2011.09.010)
- 34. Haddadi, B.; Jordan, C.; Miltner, M.; Harasek, M. Membrane modeling using CFD: Combined evaluation of mass transfer and geometrical influences in 1D and 3D. *J. Membr. Sci.* **2018**, *563*, 199–209. [\[CrossRef\]](http://doi.org/10.1016/j.memsci.2018.05.040)
- <span id="page-16-2"></span>35. Keir, G.; Jegatheesan, V. A review of computational fluid dynamics applications in pressure-driven membrane filtration. *Rev. Environ. Sci. Bio/Technol.* **2014**, *13*, 183–201. [\[CrossRef\]](http://doi.org/10.1007/s11157-013-9327-x)
- 36. Completo, C.; Semiao, V.; Geraldes, V. Efficient CFD-based method for designing cross-flow nanofiltration small devices. *J. Membr. Sci.* **2016**, *500*, 190–202. [\[CrossRef\]](http://doi.org/10.1016/j.memsci.2015.11.012)
- 37. Saeed, A.; Vuthaluru, R.; Vuthaluru, H.B. Investigations into the effects of mass transport and flow dynamics of spacer filled membrane modules using CFD. *Chem. Eng. Res. Des.* **2015**, *93*, 79–99. [\[CrossRef\]](http://doi.org/10.1016/j.cherd.2014.07.002)
- <span id="page-16-16"></span>38. Parvareh, A.; Rahimi, M.; Madaeni, S.; Alsairafi, A. Experimental and CFD Study on the Role of Fluid Flow Pattern on Membrane Permeate Flux. *Chin. J. Chem. Eng.* **2011**, *19*, 18–25. [\[CrossRef\]](http://doi.org/10.1016/S1004-9541(09)60171-3)
- 39. Ren, J.; Chowdhury, M.R.; Xia, L.; Ma, C.; Bollas, G.M.; McCutcheon, J. A computational fluid dynamics model to predict performance of hollow fiber membrane modules in forward osmosis. *J. Membr. Sci.* **2020**, *603*, 117973. [\[CrossRef\]](http://doi.org/10.1016/j.memsci.2020.117973)
- <span id="page-16-3"></span>40. Bucs, S.S.; Linares, R.V.; Marston, J.; Radu, A.I.; Vrouwenvelder, J.S.; Picioreanu, C. Experimental and numerical characterization of the water flow in spacer-filled channels of spiral-wound membranes. *Water Res.* **2015**, *87*, 299–310. [\[CrossRef\]](http://doi.org/10.1016/j.watres.2015.09.036) [\[PubMed\]](http://www.ncbi.nlm.nih.gov/pubmed/26433778)
- <span id="page-16-5"></span>41. Lotfiyan, H.; Ashtiani, F.Z.; Fouladitajar, A.; Armand, S.B. Computational fluid dynamics modeling and experimental studies of oil-in-water emulsion microfiltration in a flat sheet membrane using Eulerian approach. *J. Membr. Sci.* **2014**, *472*, 1–9. [\[CrossRef\]](http://doi.org/10.1016/j.memsci.2014.08.036)
- 42. Wang, J.; Gao, X.; Ji, G.; Gu, X. CFD simulation of hollow fiber supported NaA zeolite membrane modules. *Sep. Purif. Technol.* **2019**, *213*, 1–10. [\[CrossRef\]](http://doi.org/10.1016/j.seppur.2018.12.017)
- <span id="page-16-12"></span>43. Saeed, A.; Vuthaluru, R.; Yang, Y.; Vuthaluru, H.B. Effect of feed spacer arrangement on flow dynamics through spacer filled membranes. *Desalination* **2012**, *285*, 163–169. [\[CrossRef\]](http://doi.org/10.1016/j.desal.2011.09.050)
- <span id="page-16-6"></span>44. Feron, P.; Van Heuven, J.; Akkerhuis, J.; Van Der Welle, R. Design and development of a membrane testcell with uniform mass transfer: Application to characterisation of high flux gas separation membranes. *J. Membr. Sci.* **1993**, *80*, 157–164. [\[CrossRef\]](http://doi.org/10.1016/0376-7388(93)85140-R)
- <span id="page-16-8"></span>45. Darcovich, K.; Dal-Cin, M.; Ballèvre, S.; Wavelet, J.-P. CFD-assisted thin channel membrane characterization module design. *J. Membr. Sci.* **1997**, *124*, 181–193. [\[CrossRef\]](http://doi.org/10.1016/S0376-7388(96)00192-5)
- <span id="page-16-9"></span>46. Tarabara, V.V.; Wiesner, M.R. Computational fluid dynamics modeling of the flow in a laboratory membrane filtration cell operated at low recoveries. *Chem. Eng. Sci.* **2003**, *58*, 239–246. [\[CrossRef\]](http://doi.org/10.1016/S0009-2509(02)00436-0)
- <span id="page-16-10"></span>47. Balannec, B.; Cortès-Juan, F.; Renouard, T. Design Improvement of a Bench-scale Nanofiltration Device by CFD, Comsol.Ch. 2010. Available online: [https://www.comsol.ch/paper/download/63180/balannec\\_paper.pdf](https://www.comsol.ch/paper/download/63180/balannec_paper.pdf) (accessed on 21 August 2020).
- <span id="page-16-11"></span>48. Da Costa, A.; Fane, A.; Wiley, D. Spacer characterization and pressure drop modelling in spacer-filled channels for ultrafiltration. *J. Membr. Sci.* **1994**, *87*, 79–98. [\[CrossRef\]](http://doi.org/10.1016/0376-7388(93)E0076-P)
- 49. Gu, B.; Adjiman, C.S.; Xu, X.Y. The effect of feed spacer geometry on membrane performance and concentration polarisation based on 3D CFD simulations. *J. Membr. Sci.* **2017**, *527*, 78–91. [\[CrossRef\]](http://doi.org/10.1016/j.memsci.2016.12.058)
- 50. Kawachale, N.; Kirpalani, D.M.; Kumar, A. A mass transport and hydrodynamic evaluation of membrane separation cell. *Chem. Eng. Process. Process Intensif.* **2010**, *49*, 680–688. [\[CrossRef\]](http://doi.org/10.1016/j.cep.2009.08.001)
- <span id="page-16-13"></span>51. Ranade, V.V.; Kumar, A. Fluid dynamics of spacer filled rectangular and curvilinear channels. *J. Membr. Sci.* **2006**, *271*, 1–15. [\[CrossRef\]](http://doi.org/10.1016/j.memsci.2005.07.013)
- <span id="page-16-14"></span>52. Wiley, D.E.; Fletcher, D.F. Techniques for computational fluid dynamics modelling of flow in membrane channels. *J. Membr. Sci.* **2003**, *211*, 127–137. [\[CrossRef\]](http://doi.org/10.1016/S0376-7388(02)00412-X)
- <span id="page-16-15"></span>53. Vinchurkar, S.; Longest, P.W. Evaluation of hexahedral, prismatic and hybrid mesh styles for simulating respiratory aerosol dynamics. *Comput. Fluids* **2008**, *37*, 317–331. [\[CrossRef\]](http://doi.org/10.1016/j.compfluid.2007.05.001)

*Membranes* **2021**, *11*, 54 18 of 18

<span id="page-17-0"></span>54. Bracci, M.; Tarini, M.; Pietroni, N.; Livesu, M.; Cignoni, P. HexaLab.net: An online viewer for hexahedral meshes. *Comput. Des.* **2019**, *110*, 24–36. [\[CrossRef\]](http://doi.org/10.1016/j.cad.2018.12.003)

- <span id="page-17-1"></span>55. Blažek, J. *Governing Equations*; Elsevier BV: Amsterdam, The Netherlands, 2015; pp. 7–27.
- <span id="page-17-2"></span>56. Vasquez, S. A Phase Coupled Method for Solving Multiphase Problems on Unstructured Mesh. In Proceedings of the 2000 ASME Fluids Engineering Division Summer Meeting, Boston, MA, USA, 11–15 June 2000.
- <span id="page-17-3"></span>57. Singh, R.; Purkait, M.K. Microfiltration Membranes. In *Membrane Separation Principles and Applications*; Elsevier: Amsterdam, The Netherlands, 2019; pp. 111–146.
- <span id="page-17-4"></span>58. Schwinge, J. Characterization of a zigzag spacer for ultrafiltration. *J. Membr. Sci.* **2000**, *172*, 19–31. [\[CrossRef\]](http://doi.org/10.1016/S0376-7388(00)00312-4)
![](_page_0_Picture_0.jpeg)

MDPI

Article

# Multiscale Analysis of Permeable and Impermeable Wall Models for Seawater Reverse Osmosis Desalination

Qingqing Yang <sup>1</sup>, Yi Heng <sup>2,3,4</sup>, Ying Jiang <sup>2,3,4</sup> and Jiu Luo <sup>2,3,4,\*</sup>

- <sup>1</sup> School of Materials Science and Engineering, Sun Yat-sen University, Guangzhou 510006, China
- <sup>2</sup> School of Computer Science and Engineering, Sun Yat-sen University, Guangzhou 510006, China
- <sup>3</sup> National Supercomputing Center in Guangzhou (NSCC-GZ), Guangzhou 510006, China
- <sup>4</sup> Guangdong Province Key Laboratory of Computational Science, Guangzhou 510006, China
- \* Correspondence: luojiu@mail.sysu.edu.cn

Abstract: In recent years, high permeability membranes (HPMs) have attracted wide attention in seawater reverse osmosis (SWRO) desalination. However, the limitation of hydrodynamics and mass transfer characteristics for conventional spiral wound modules defeats the advantage of HPMs. Feed spacer design is one of the effective ways to improve module performance by enhancing permeation flux and mitigating membrane fouling. Herein, we propose a multiscale modeling framework that integrates a three-dimensional multi-physics model with a permeable wall and an impermeable wall, respectively, at a sub-millimeter scale and a system-level model at a meter scale. Using the proposed solution framework, a thorough quantitative analysis at different scales is conducted and it indicates that the average errors of the friction coefficient and the Sherwood number using the impermeable wall model are less than 2% and 9%, respectively, for commercial SWRO membrane (water permeability  $1 \text{ L m}^{-2} \text{ h}^{-1} \text{ bar}^{-1}$ ) and HPMs ( $3 \text{ L m}^{-2} \text{ h}^{-1} \text{ bar}^{-1}$ ,  $5 \text{ L m}^{-2} \text{ h}^{-1} \text{ bar}^{-1}$  and 10 L m<sup>-2</sup> h<sup>-1</sup> bar<sup>-1</sup>) systems, compared to the predictions using the permeable wall model. Using both the permeable and impermeable wall models, the system-level simulations, e.g., specific energy consumption, average permeation flux, and the maximum concentration polarization factor at the system inlet are basically the same (error < 2%), while the impermeable wall model has a significant advantage in computational efficiency. The multiscale framework coupling the impermeable wall model can be used to guide the efficient and accurate optimal spacer design and system design for HPMs using, e.g., a machine learning approach.

**Keywords:** multiscale modeling; impermeable and permeable wall models; high permeability membranes; feed spacer; reverse osmosis desalination

![](_page_0_Picture_12.jpeg)

check for

Citation: Yang, Q.; Heng, Y.; Jiang, Y.; Luo, J. Multiscale Analysis of Permeable and Impermeable Wall Models for Seawater Reverse Osmosis Desalination. *Separations* 2023, 10, 134. https://doi.org/ 10.3390/separations10020134

Academic Editor: Juan Jose Baeza Baeza

Received: 23 January 2023 Revised: 7 February 2023 Accepted: 10 February 2023 Published: 15 February 2023

![](_page_0_Picture_16.jpeg)

Copyright: © 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https://creativecommons.org/licenses/by/4.0/).

## 1. Introduction

Membrane-based separation technologies, such as micro- [1,2], ultra- [3,4], or nanofiltration (NF) [5,6], reverse osmosis (RO) [7,8], electrodialysis [9,10] and membrane distillation [11,12], have increasingly attracted extensive attention in industry and academia. Due to its energy-saving and cost-competitiveness, RO is one of the most advanced membrane-based technologies and has widespread applications in desalination [13,14], wastewater treatment [15,16], pharmaceutical production [17,18], electronics industries [19,20] etc. Scaling and fouling are common challenging problems in RO, especially in the condition of high flux (e.g., more than 50 L m $^{-2}$  h $^{-1}$  [21]) with the use of a high permeability membrane (HPM). Spacer design in spiral wound membrane (SWM) modules has wide application prospects to mitigate membrane scaling and fouling and improve the performance of a SWM module [22].

Lin et al. [23] summarized the research development on feed spacer in the last twenty years and emphasized that it is critical for feed spacer design to balance the feed channel pressure drop and mass transfer on the membrane surfaces. Among these works, the computational fluid dynamics (CFD) simulation technology was widely applied to capture

Separations 2023, 10, 134 2 of 15

the local fluid flow and transport phenomena in membrane-based processes. The CFD models in a spacer-filled channel are divided into a permeable wall model and an impermeable (or impermeable-dissolving) wall model [24], according to the type of boundary conditions enforced on the membrane walls. For the permeable wall model, Angi et al. [25] adopted the three-dimensional (3D) CFD technology to estimate the effect of the angle  $(\alpha = 60^{\circ}, 90^{\circ}, 120^{\circ})$  between the spacer filaments and the Reynolds numbers (100, 400, 800). The results indicate that increasing crossflow contributes to enhance mass transfer, and reducing the angle  $\alpha$  will decrease the friction loss. The experimental and simulation results by Lin et al. [26] showed that the feed spacer geometries with non-uniform filament have a significant effect on both anti-fouling performance and hydraulics. The study by Foo et al. [27] showed that the mass transfer in the spacer-filled channel can be markedly enhanced by an unsteady forced-slip combined with a spacer design. In this case, the optimization of the geometrical parameters can greatly affect the resonant frequency and thereby reduce the concentration polarization (CP). The study by Singh et al. [28] showed that the feed spacer configurations with the higher water permeation are accompanied with a higher flow resistance. Li et al. [29] proposed a hybrid model that couples a CFD model at a small-scale and a system level model for brackish water RO (BWRO) desalination. The simulated results fit well with the measurements from industry. Lin et al. [30] designed a novel membrane module with a diagonal-flow feed channel. The CFD simulations and experimental results indicate that the novel membrane module has better performance (e.g., higher permeation flux and higher salt rejection) compared to the conventional membrane module. This is because the former one has a higher average cross-flow in the feed channel, which can reduce CP and mitigate membrane scaling. Apart from the RO process, spacer design also has widespread applications in other membrane-based processes, such membrane distillation [31].

However, the typical used permeable wall model is fully coupled and is computationally expensive. Because the cross velocity is several orders of magnitude higher than the permeation flux, the boundary condition on the membrane surface barely affects the fluid flow and solute transport. Some researchers used impermeable wall boundary conditions to obtain reasonable simulation results in their CFD simulations [32–37]. The impermeable wall model is a one-way coupling that greatly reduces the nonlinear effect compared with the commonly used permeable wall model. Geraldes and Afonso [38] proposed a generalized correction factor to correct the mass transfer coefficients at impermeable walls with an average error of 3.6% compared with the CFD predictions with a permeable wall, which is independent of the flow regime and feed spacer geometry. The predicted results using the impermeable wall model are in good agreement with the experimental data [32,33] with an error of approximately 10%. Toh et al. [37] presented a multi-scale model that couples an impermeable wall model at a small-scale and a large-scale model for RO desalination. The simulated results for BWRO and SWRO systems with the use of an advanced feed spacer and HPMs showed that the significance of improving the spacer performance is even greater than increasing the membrane permeability in terms of cost-effectiveness. Luo et al. [39] proposed a heuristic optimization framework based on a field synergy principle and a high throughput computing strategy for BWRO systems. Using the optimized feed spacer, the axial pressure drop for the entire system is negligibly small compared to a commercial feed spacer. Chen et al. [40] further developed several novel feed spacers based on triply periodic minimal surfaces, and the average water permeation flux can be enhanced by about 8.6% in comparison to a conventional feed spacer. Gu et al. [41] used a multilayer artificial neural network to establish a surrogate pressure drop model for spacer-filled channels in BWRO desalination that enables a quantitative description between the axial pressure drop and design parameters, including feed spacer geometry and inlet velocity magnitude. The surrogate model can be guided to the optimal design of feed spacer. Recently, Luo et al. [42] further proposed a supercomputing-based machine learning-driven multiscale optimization design framework for SWRO desalination systems with HPMs. Using the optimization framework, the specific energy consumption (SEC) and

Separations 2023, 10, 134 3 of 15

the required membrane area for a designed two-stage SWRO system reduced by 27.5% (to  $1.66 \text{ kWh m}^{-3}$ ) and 37.2%, respectively, under typical conditions (feed salinity 35,000 ppm, recovery rate 50%). By spacer optimization and system design, the CP at the system inlet could be suppressed to no more than 1.20.

Although both the permeable and impermeable wall models have been widely applied in membrane-based processes, the quantitative analyses at different scales for both models were rarely reported, especially in the conditions of high flux with the use of HPMs. In this paper, we establish a multiscale modeling framework that integrates the permeable and impermeable wall models (Section 2.1), respectively, with a system-level model (Section 2.3) by using relations of the friction factor and the Sherwood number with respect to various Reynolds numbers (Section 2.2). A thorough quantitative analysis of the framework is conducted for CFD simulations at a sub-millimeter scale (Section 3.1) and system-level simulations at a meter scale (Section 3.2).

## 2. Mathematical Modeling

In spacer-filled RO channels, the "periodic fully-developed" transport phenomena were confirmed in previous work [29,43] using CFD techniques, which makes it possible to estimate the cell average mass transfer coefficient at different locations along the axis of the SWM module by changing the average inlet velocity in the CFD model. Here, we present a multiscale modeling framework that integrates the permeable wall model and the impermeable wall model, respectively, as shown in Figure 1.

<span id="page-2-1"></span>![](_page_2_Figure_5.jpeg)

**Figure 1.** The multiscale modeling framework for SWRO desalination that integrates the permeable wall model and the impermeable wall model.

#### <span id="page-2-0"></span>2.1. The Permeable and Impermeable Wall Models at a Sub-Millimeter Scale

#### 2.1.1. Problem Description

Both the permeable and impermeable wall models in the SWRO desalination consider fluid flow and solute transport, which can be mathematically formulated below [42].

$$\begin{cases}
\rho(\mathbf{u} \cdot \nabla)\mathbf{u} = \nabla \cdot \left[ -P\mathbf{I} + \mu \left( \nabla \mathbf{u} + (\nabla \mathbf{u})^{\mathrm{T}} \right) \right], & \text{in } \Omega, \\
\rho \nabla \cdot \mathbf{u} = 0, & \text{in } \Omega, \\
D_s \nabla^2 c = \mathbf{u} \cdot \nabla c, & \text{in } \Omega, \\
\mathbf{u}_{\text{in}} = \mathbf{u}_{\text{out}}, (\nabla \mathbf{u})_{\text{in}} = (\nabla \mathbf{u})_{\text{out}}, \overline{u} = U, & \text{on } \Gamma_{\mathrm{I}}, \\
(\nabla P)_{\text{in}} = (\nabla P)_{\text{out}}, c = c_0, & \text{on } \Gamma_{\mathrm{I}}, \\
P = 0, -\mathbf{n} \cdot D_s \nabla c = 0, & \text{on } \Gamma_{\mathrm{O}}, \\
J_{\mathrm{W}} = w = \mathcal{G}_1(L_{\mathrm{P}}, P, c), J_{\mathrm{S}} = \mathcal{G}_2(B, J_{\mathrm{W}}, c), & \text{on } \Gamma_{\mathrm{U}} \cup \Gamma_{\mathrm{B}}, \\
\mathbf{u}_{\mathrm{L}} = \mathbf{u}_{\mathrm{R}}, P_{\mathrm{L}} = P_{\mathrm{R}}, c_{\mathrm{L}} = c_{\mathrm{R}}, & \text{on } \Gamma_{\mathrm{L}} \cup \Gamma_{\mathrm{R}},
\end{cases}$$
(1)

Separations **2023**, 10, 134 4 of 15

<span id="page-3-0"></span>where the governing equations, the Navier–Stokes (N–S) equation, the continuity equation under a laminar flow condition and the convection–diffusion equation are defined in a 3D computational domain ( $\Omega$ ), or a narrow spacer-filled channel (Figure 2). The variables consist of the velocity vector  $\mathbf{u} \equiv (u, v, w)$ , hydraulic pressure (P) and molar concentration (c). The density ( $\rho$ ) and viscosity ( $\mu$ ) of fluid and the diffusivity ( $D_s$ ) of salt are assumed as constants [42]. $D_s$  and  $D_s$  denote water permeability and salt permeability, respectively.

![](_page_3_Figure_2.jpeg)

**Figure 2.** (a) Spacer sheet; (b) The computational domain (spacer-filled channel); (c) A spacer unit; (d) Filament A; and (e) Filament B.

#### 2.1.2. Boundary and Initial Conditions

For the permeable wall model, the permeation flux of water, or water flux ( $J_W$ ), is proportional to the difference ( $\Delta P - \Delta \pi$ ) between the transmembrane pressure ( $\Delta P = \Delta P_0 - \Delta P_c$ ) and transmembrane osmotic pressure ( $\Delta \pi$ ). The specific value is  $L_P$ .  $\Delta \pi$  is the function of the local concentration on the membrane surfaces. For the impermeable wall model, the permeation flux of water is assumed as zero, and a constant concentration boundary condition is applied on the membrane surfaces. Thus,  $J_W$  can be expressed as

$$J_{W} = \mathcal{G}_{1}(L_{P}, P, c) = \begin{cases} L_{P}[\Delta P_{0} - \Delta P_{c} - \Delta \pi(c)], & \textit{for permeable wall modeo} \\ 0, & \textit{for impermeable wall modeo} \end{cases}$$
 (2)

where  $\Delta P_0$  is the inlet transmembrane pressure. The pressure drop ( $\Delta P_c$ ) along the feed direction (x-direction, see Figure 2b) is the difference of the average pressures at the inlet ( $\Gamma_{\rm I}$ ) and outlet ( $\Gamma_{\rm O}$ ), respectively. In the convection–diffusion equation, the boundary conditions for a permeable flux of salt ( $J_{\rm S}$ ) and a constant concentration ( $c_{\rm w,0}$ ) are enforced on the membrane walls ( $\Gamma_{\rm U} \cup \Gamma_{\rm B}$ ) for the permeable wall model and impermeable wall model, respectively, as below.

$$\begin{cases} \mathcal{G}_2(B, J_W, c) = \mathbf{n} \cdot (-D_s \nabla c + c \mathbf{u}) = J_W c_w (1 - R_{\text{salt}}), & \textit{for permeable wall model} \\ c_w = c_{w,0}. & \textit{for impermeable wall model} \end{cases}$$
(3)

 $c_{\rm w}$  is the concentration on the membrane walls. The salt rejection ( $R_{\rm salt}$ ) is defined by

$$R_{\text{salt}} = \frac{J_W}{I_W + B}. (4)$$

Separations **2023**, 10, 134 5 of 15

A fully developed boundary condition with an average velocity magnitude and a constant concentration boundary condition ( $c=c_0$ ) are applied at the inlet boundary ( $\Gamma_I$ ) for both the permeable and impermeable wall models. The periodic boundary conditions are applied at the lateral boundaries ( $\Gamma_L \cup \Gamma_R$ ), which are commonly used in numerical simulation involving structural repeating units (see Figure 2a). For the impermeable wall model, the N–S equation and continuity equation are solved first. The initial velocity and pressure conditions are assumed as constants. The obtained velocity and pressure profiles are used to further calculate the concentration profile by solving the convection– diffusion equation. For the permeable wall model, the calculated velocity, pressure and concentration profiles are solved simultaneously. The simulated results for Case 1 (Commercial SWRO membrane:  $L_P = 1$  L m<sup>-2</sup> h<sup>-1</sup> bar<sup>-1</sup>) are considered as the appropriate initial results to accelerate the solutions for Cases 2–4 (HPMs:  $L_P = 3$  L m<sup>-2</sup> h<sup>-1</sup> bar<sup>-1</sup>; 5 L m<sup>-2</sup> h<sup>-1</sup> bar<sup>-1</sup>; 10 L m<sup>-2</sup> h<sup>-1</sup> bar<sup>-1</sup>).

#### <span id="page-4-0"></span>2.2. The Relations Coupling the CFD Model and System-Level Model

After solving Equations (1)–(4), the 3D velocity, pressure and concentration profiles in the spacer-filled channel ( $\Omega$ ) can be estimated for both the permeable and impermeable wall models. The relations of the friction factor (f), Sherwood number (Sh) and Reynolds numbers ( $Re = \frac{D_H \bar{u} p}{u}$ ) are obtained by the fitting curves (f-Re, Sh-Re), namely,

$$\begin{cases} f_{\text{per}} = k_1 R e^{t_1}, & \text{for permeable wall model} \\ Sh_{\text{per}} = k_2 R e^{t_2}, & \text{for permeable wall model} \end{cases}$$
 (5)

and

$$\begin{cases} f_{\text{imp}} = k'_1 \text{Re}^{t'_1}, & \text{for impermeable wall model} \\ Sh_{\text{imp}} = k'_2 \text{Re}^{t'_2}. & \text{for impermeable wall model} \end{cases}$$
 (6)

The friction factor  $(f_i)$  and Sherwood number  $(Sh_i)$  are calculated by

$$f_{\rm i} = -\frac{\Delta P_{c,\,\rm i}}{L} D_{\rm H} / \left(\frac{1}{2} \overline{u}^2\right), \quad i = \text{per, imp}$$
 (7)

and

$$Sh_{i} = \frac{\overline{k}_{m, i}D_{H}}{D_{S}},$$
  $i = per, imp$  (8)

respectively. For a given spacer geometry, the hydraulic diameter ( $D_{\rm H}$ ) can be identified [29]. Then the pressure drop per unit length along the feed direction (x-direction, see Figure 2b can be calculated by

$$-\frac{\Delta P_{c,i}}{L} = \frac{\overline{P}(x=0) - \overline{P}(x=L)}{L}, \qquad i = \text{per, imp}$$
 (9)

 $\overline{P}(x=L)$  and  $\overline{P}(x=0)$  denote the average pressure at the inlet (x=0) and outlet (x=L). The cell average mass transfer coefficient  $(\overline{k}_{m,i})$  is calculated by

$$\bar{k}_{\text{m, i}} = \frac{\int_0^L dx \int_0^W \left(\frac{-D_s}{c_r - c_w} \cdot \frac{\partial c}{\partial z} \Big|_{z=H/2}\right) dy}{\int_0^L dx \int_0^W dy}, \qquad i = \text{per, imp}$$
(10)

L, W and H denote the length (x-direction), width (y-direction) and height (z-direction) of the computational domain (Figure 2b). It should be pointed out that the estimated Sherwood number using the impermeable wall model ( $\bar{k}_{m, imp}$ ) needs to be corrected using the reported relations [38]

$$\bar{k}_{\text{m, per}} = \bar{k}_{\text{m, imp}} \left[ \psi + \left( 1 + 0.26 \psi^{1.4} \right)^{-1.7} \right], \quad (\psi < 20)$$
 (11)

Separations 2023, 10, 134 6 of 15

$$\psi = \frac{J_W}{\bar{k}_{\text{m, imp}}},\tag{12}$$

in which  $J_W$  is calculated using the system-level model, Equations (13)–(15).

### <span id="page-5-0"></span>2.3. The System-Level Model for SWRO Desalination at a Meter Scale

Furthermore, we established a system-level model [36,37] that enables us to quantify the effect of spacer geometry on the entire performance of RO desalination.

$$\begin{cases} \frac{dQ}{dX} = -J_{W} \cdot A_{\text{tot}} & X = 0, \ Q = Q_{0}, \\ \frac{d(\Delta P)}{dX} = -\frac{\rho \overline{u}^{2}}{2D_{H}} f \cdot (n_{\text{mem}} l_{x}) & X = 0, \ \Delta P = \Delta P_{0}, \\ \frac{dw_{b}}{dX} = J_{W} \cdot \frac{A_{\text{tot}}}{Q} (w_{b} - w_{p}) & X = 0, \ w_{b} = w_{b, 0}, \\ J_{W} = L_{P}(\Delta P - \sigma \cdot \varphi R_{\text{salt}} w_{w}) \\ Q = N_{PV} n_{\text{sp}} H l_{y} \varepsilon \overline{u}, \end{cases}$$

$$(13)$$

where Q,  $\Delta P$  and  $J_{\rm W}$  are the flow rate, transmembrane pressure and water flux, respectively.  $N_{\rm PV}$ ,  $n_{\rm mem}$  and  $n_{\rm sp}$  denote the number of pressure vessels, the number of membrane module per pressure vessel and the number of feed spacers per membrane module, respectively.  $l_x$  and  $l_y$  are the module length parallel to flow and the module length perpendicular to flow, respectively. The porosity,  $\varepsilon$  is calculated by the formula in previous work [29]. In this paper, the average inlet velocity ( $U_0$ ) is considered as a constant.  $w_b$ ,  $w_p$  and  $w_w$  denote bulk salinity, permeate salinity and salinity on the membrane walls, respectively. These variables change with respect to various dimensionless length,  $X = \frac{x}{n_{\rm mem}l_x}$ . The total membrane area,  $A_{\rm tot}$ , is calculated by  $A_{\rm tot} = N_{\rm PV}n_{\rm mem}A_0$  ( $A_0$ : membrane area per membrane module).  $\sigma$  and  $\varphi$  denote the reflection coefficient and osmotic pressure coefficient, respectively. The salinity on the membrane walls ( $w_w$ ) is calculated by

$$w_{\rm w} = \frac{w_{\rm p}}{1 - R_{\rm salt}},\tag{14}$$

in which  $w_p$  can be expressed by

$$w_{\rm p} = w_{\rm b} / \left[ \exp \left( \ln \frac{J_{\rm W}}{B} - \frac{J_{\rm W}}{\overline{k}_{\rm m, per}} \right) + 1 \right]. \tag{15}$$

A more detailed derivation for Equation (15) can be found in our latest work [42].

#### 3. Results and Discussion

## <span id="page-5-1"></span>3.1. CFD Simulations

In this paper, the detailed geometry parameters of the feed spacer are listed in Table 1 that are referred to previous literature [44]. The spacer thickness is about 34 mil (863 µm). The number of spatial discrete elements is 1,477,393 (Figure 3), which has comparable precision compared with our previous work [39]. The detailed mesh independence analysis was reported there. Based on the finite element method, Comsol Multiphysics was used to establish and solve the CFD models in this paper. More detailed model parameters can be found in our latest work [42]. The calculated velocity magnitude distributions using the permeable wall model (Figure 4a) and impermeable wall model (Figure 4b) demonstrate that the effect of the permeation flux of water (or water flux) on the cross velocity in the spacer-filled channel is negligible. This is because the water flux ( $\approx 10^{-5}$  m/s, see Figure 5a) is much smaller than the cross velocity in the feed channel (Figure 4a), which is consistent with the reported literature [29]. Even for the HPMs systems (e.g.,  $L_P = 5$  L m<sup>-2</sup> h<sup>-1</sup> bar<sup>-1</sup>, Figure 5b), this conclusion still holds true. Similarly, the calculated pressure magnitude distribution is basically the same using the permeable wall model (Figure 6a) and impermeable wall model (Figure 6b).

Separations **2023**, 10, 134 7 of 15

<span id="page-6-0"></span>

| Table 1. The | detailed ge | ometrical param | eters of the CFD | models [44] | l. |
|--------------|-------------|-----------------|------------------|-------------|----|
|--------------|-------------|-----------------|------------------|-------------|----|

| Geometric            | Value                                   |        |  |
|----------------------|-----------------------------------------|--------|--|
|                      | L <sub>1, A</sub> (μm)                  | 234    |  |
|                      | $L_{2, A}$ ( $\mu$ m)                   | 389    |  |
|                      | $L_{3, A}$ ( $\mu$ m)                   | 500    |  |
|                      | $L_{4, A}$ ( $\mu$ m)                   | 696    |  |
|                      | $L_{5, A}$ ( $\mu$ m)                   | 566    |  |
|                      | $L_{1, B}$ ( $\mu$ m)                   | 281    |  |
|                      | $L_{2, B}$ ( $\mu$ m)                   | 535    |  |
| Spacer unit          | $L_{3, B}$ ( $\mu$ m)                   | 92     |  |
| Spacer unit          | $L_{4, B}$ ( $\mu$ m)                   | 878    |  |
|                      | $L_{5, B}$ ( $\mu$ m)                   | 599    |  |
|                      | $D_{1, A}$ ( $\mu$ m)                   | 422    |  |
|                      | $D_{2, A}$ ( $\mu$ m)                   | 223    |  |
|                      | $D_{1,B}$ ( $\mu$ m)                    | 445    |  |
|                      | $D_{2, B}$ ( $\mu$ m)                   | 223    |  |
|                      | $D_{\mathrm{tot}}$ ( $\mu \mathrm{m}$ ) | 863    |  |
|                      | α (°)                                   | 90     |  |
|                      | Length, L (mm)                          | 16.864 |  |
|                      | Width, W (mm)                           | 3.3729 |  |
| Computational domain | Height, H (mm)                          | 0.853  |  |
|                      | Porosity, $\varepsilon$ (-)             | 0.90   |  |
|                      | Hydraulic diameter, $D_{\rm H}$ (mm)    | 1.058  |  |

<span id="page-6-1"></span>![](_page_6_Picture_3.jpeg)

**Figure 3.** The geometric model discretization for **(a)** the computational domain and **(b)** the zoomed spacer section.

<span id="page-6-2"></span>![](_page_6_Figure_5.jpeg)

**Figure 4.** The velocity magnitude distributions with an inlet average velocity magnitude of 0.15 m s<sup>-1</sup> using (**a**) the permeable wall model (Case 1:  $L_P = 1$  L m<sup>-2</sup> h<sup>-1</sup> bar<sup>-1</sup>) and (**b**) the impermeable wall model.

Separations **2023**, 10, 134 8 of 15

<span id="page-7-0"></span>![](_page_7_Figure_1.jpeg)

**Figure 5.** The water flux with inlet average velocity magnitude of 0.15 m s<sup>-1</sup> using the permeable wall model for (**a**) the commercial membrane ( $L_P = 1 \text{ L m}^{-2} \text{ h}^{-1} \text{ bar}^{-1}$ ) and (**b**) the HPM ( $L_P = 5 \text{ L m}^{-2} \text{ h}^{-1} \text{ bar}^{-1}$ ) systems.

<span id="page-7-1"></span>![](_page_7_Figure_3.jpeg)

**Figure 6.** The pressure magnitude distributions with an inlet average velocity magnitude of  $0.15 \text{ m s}^{-1}$  using (a) the permeable wall model and (b) the impermeable wall model.

Using the permeable and impermeable wall models, the calculated friction coefficient (f) and Sherwood number (Sh) are shown in Figures 7a–d and 7e–h, respectively, with the use of a commercial SWRO membrane (Case 1:  $L_p = 1 \text{ L m}^{-2} \text{ h}^{-1} \text{ bar}^{-1}$ ) and HPMs (Case 2:  $L_p = 3 \text{ L m}^{-2} \text{ h}^{-1} \text{ bar}^{-1}$ ; Case 3:  $L_p = 5 \text{ L m}^{-2} \text{ h}^{-1} \text{ bar}^{-1}$ ); Case 4:  $L_p = 10 \text{ L m}^{-2} \text{ h}^{-1}$ bar 1). It should be noted that the calculated Sherwood number using the impermeable wall model in Figure 7e-h is corrected using Equations (11)-(15). The average errors of the calculated friction coefficient using the impermeable wall model are 0.12%, 0.44%, 0.69% and 1.17%, respectively, for Cases 1-4 compared with that of using the permeable wall model. Correspondingly, the average errors of the estimated Sherwood number are 6.47%, 7.96%, 7.39% and 8.46%, which basically coincide with the reported results in previous work [38]. In an RO system, it is more likely that fouling will occur in the lead elements [45], especially in the condition of high flux. Therefore, we further evaluated the Sherwood number using the impermeable wall model at the system inlet with the errors of 4.25%, 0.27%, 3.49% and 9.51%, respectively. Overall, the accuracy of the impermeable wall model is comparable and acceptable on the prediction of the friction coefficient and Sherwood number versus the permeable wall model. In computational time, the latter one (77.8 h) for each case is about three times than that of the former one (25.3 h). It should be emphasized that the impermeable wall model is only associated with the spacer geometry and inlet velocity, and is independent of other parameters, such as water permeability and operating pressure. Therefore, the Sherwood number with respect to various water permeabilities (Cases 1-4) can be directly calculated using Equations (11)-(15) based on the obtained relations  $(f_{\text{imp}} - Re, Sh_{\text{imp}} - Re)$ . However, the permeable wall model must be recalculated to obtain the Sherwood number when the water permeability or the other conditions change. Thus, the impermeable wall model has a significant advantage in computational efficiency in comparison to the permeable wall model, which can greatly reduce the computational cost, and can be used for the optimal design of the feed spacer.

Separations **2023**, 10, 134 9 of 15

<span id="page-8-1"></span>![](_page_8_Figure_1.jpeg)

**Figure 7.** The friction coefficient (f) and and Sherwood number (Sh) with respect to various Reynolds numbers (Re) using the impermeable wall model and the permeable wall model for Case 1 (a,e) ( $L_P = 1 \text{ L m}^{-2} \text{ h}^{-1} \text{ bar}^{-1}$ ), (b,f) Case 2 ( $L_P = 3 \text{ L m}^{-2} \text{ h}^{-1} \text{ bar}^{-1}$ ), (c,g) Case 3 ( $L_P = 5 \text{ L m}^{-2} \text{ h}^{-1} \text{ bar}^{-1}$ ) and (d,d) Case 4 ( $L_P = 10 \text{ L m}^{-2} \text{ h}^{-1} \text{ bar}^{-1}$ ).

## <span id="page-8-0"></span>3.2. Performance Evaluations at a System-Level

Using the system-level model, Equations (13)–(15) coupled with the permeable wall model, Equations (1)–(5), (7)–(10) and the impermeable wall model, Equations (1)–(4), (6)–(12) respectively, the effect of both CFD models on the RO system performance was evaluated. The input parameters for the SWRO system model (Cases 1-4) are listed in Table 2. The simulated transmembrane pressure  $(\Delta P)$ , flow rate (Q), brine salinity  $(w_b)$ , permeate salinity  $(w_p)$ , permeation flux of water  $(J_W)$  and CPF along the dimensionless length (X) (Inlet: X = 0; Outlet: X = 1) for Cases 1–4 are shown in Figure 8a–f, Figure 9a–f, Figures 10a-f and 11a-f, respectively. Obviously, the simulated results at a system-level based on the impermeable wall model are highly consistent with that of the permeable wall model, even for the HPMs systems. Furthermore, the errors of the calculated average permeate salinity  $(\overline{w}_p)$ , average permeation flux  $(J_w)$ , maximum CP factor, (max (CPF)), recovery rate  $(R_r)$ , permeate rate  $(Q_D)$  and SEC are all less than 2% using both the permeable and impermeable wall models. More detailed results are listed in Table 3. As the water permeability increases from  $1 L m^{-2} h^{-1} bar^{-1}$  to  $10 L m^{-2} h^{-1} bar^{-1}$ , the maximum CP factor at the system inlet can reach up to about 1.50, which will intensify the membrane fouling. Therefore, it is crucial to enhance the mass transfer with a pressure loss penalty when the SWRO system is operated at higher flux. To achieve this, the spacer design and improvement of the cross velocity or unsteady-state shear technologies [46] are alternative methods.

Separations **2023**, 10, 134

<span id="page-9-0"></span>

| Table 2. The | input parame | ters for SWRO s | ystems in Cases 1–4. |
|--------------|--------------|-----------------|----------------------|
|--------------|--------------|-----------------|----------------------|

|                            | Value                                                                                                                                                                                                                                                     |                                                        |  |  |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|--|--|
| Operating conditions       | Inlet transmembrane pressure, $\Delta P_0$ (bar)<br>Inlet average velocity magnitude, $U_0$ (m s <sup>-1</sup> )                                                                                                                                          | 60<br>0.2                                              |  |  |
| Properties of feed solute  | Feed salinity, $w_{b, 0}$ (ppm) Density, $\rho$ (kg m <sup>-3</sup> ) Viscosity, $\mu$ (Pa s) Diffusion coefficient, $D_{\rm s}$ (m <sup>2</sup> s <sup>-1</sup> ) Reflection coefficient, $\sigma$ ( $-$ ) Osmotic pressure coefficient, $\varphi$ (bar) | 35,000 1021 9.41 × 10-4 1.45 × 10-9 1 805.1            |  |  |
| Membrane properties        | Water permeability, $L_P$ (L m <sup>-2</sup> h <sup>-1</sup> bar <sup>-1</sup> )<br>Salt permeability, $B$ (L m <sup>-2</sup> h <sup>-1</sup> )                                                                                                           | 1 (Case1); 3 (Case 2); 5 (Case 3); 10 (Case 4)<br>0.05 |  |  |
| Membrane module parameters | Module length parallel to flow, $l_x$ (m)<br>Module length perpendicular to flow, $l_y$ (m)<br>Number of feed spacers per element, $n_{\rm sp}$<br>Membrane area per membrane module, $A_0$ (m <sup>2</sup> )                                             | 1<br>1<br>23<br>37.2                                   |  |  |
| Module configurations      | Number of membrane elements per pressure vessel, $n_{\rm mem}$<br>Number of pressure vessels, $N_{\rm pv}$                                                                                                                                                | 8 (Case1); 5 (Case 2); 3 (Case 3); 2 (Case 4)<br>30    |  |  |
| Efficiencies               | Efficiency of high-pressure pump, $\eta_{\text{pump}}$ (–)<br>Efficiency of energy recovery device, $\eta_{\text{R}}$ (–)                                                                                                                                 | 0.85<br>0.95                                           |  |  |

<span id="page-9-1"></span>![](_page_9_Figure_3.jpeg)

**Figure 8.** The simulated results at the system level using the impermeable and permeable wall models with the feed salinity ( $\overline{w}_{b, 0} = 35,000 \text{ ppm}$ ), water recovery ( $R_{r, 0} = 50\%$ ), pump efficiency (0.85), energy recovery device efficiency (0.95) and water permeability ( $L_p = 1 \text{ L m}^{-2} \text{ h}^{-1} \text{ bar}^{-1}$ ). (a) Transmembrane pressure,  $\Delta P$  (bar), (b) Flow rate, Q (m<sup>3</sup> h<sup>-1</sup>), (c) Brine salinity,  $w_b$  (ppm), (d) Permeate salinity,  $w_p$  (ppm), (e) Permeation flux of water,  $J_W$  (L m<sup>-2</sup> h<sup>-1</sup>), (f) CP factor, CPF (–) along the dimensionless length (X).

Separations **2023**, 10, 134

<span id="page-10-0"></span>![](_page_10_Figure_1.jpeg)

**Figure 9.** The simulated results at the system level using the impermeable and permeable wall models with the feed salinity ( $\overline{w}_{b, 0} = 35,000 \text{ ppm}$ ), water recovery ( $R_{r, 0} = 50\%$ ), pump efficiency (0.85), energy recovery device efficiency (0.95) and water permeability ( $L_p = 3 \text{ L m}^{-2} \text{ h}^{-1} \text{ bar}^{-1}$ ). (a) Transmembrane pressure,  $\Delta P$  (bar), (b) Flow rate, Q (m<sup>3</sup> h<sup>-1</sup>), (c) Brine salinity,  $w_b$  (ppm), (d) Permeate salinity,  $w_p$  (ppm), (e) Permeation flux of water,  $J_W$  (L m<sup>-2</sup> h<sup>-1</sup>), (f) CP factor, CPF (–) along the dimensionless length (X).

<span id="page-10-1"></span>![](_page_10_Figure_3.jpeg)

Figure 10. The simulated results at the system level using the impermeable and permeable wall models with the feed salinity ( $\overline{w}_{b,\,0} = 35,000$  ppm), water recovery ( $R_{r,\,0} = 50\%$ ), pump efficiency (0.85), energy recovery device efficiency (0.95) and water permeability ( $L_p = 5 \text{ L m}^{-2} \text{ h}^{-1} \text{ bar}^{-1}$ ). (a) Transmembrane pressure, $\Delta P$  (bar), (b) Flow rate, Q (m³ h<sup>-1</sup>), (c) Brine salinity,  $w_b$  (ppm), (d) Permeate salinity,  $w_p$  (ppm), (e) Permeation flux of water,  $J_W$  (L m<sup>-2</sup> h<sup>-1</sup>), (f) CP factor, CPF (–) along the dimensionless length (X).

Separations **2023**, 10, 134

<span id="page-11-0"></span>![](_page_11_Figure_1.jpeg)

**Figure 11.** The simulated results at the system level using the impermeable and permeable wall models with the feed salinity ( $\overline{w}_{b,\,0} = 35,000$  ppm), water recovery ( $R_{r,\,0} = 50\%$ ), pump efficiency (0.85), energy recovery device efficiency (0.95) and water permeability ( $L_p = 10 \text{ L m}^{-2} \text{ h}^{-1} \text{ bar}^{-1}$ ). (a) Transmembrane pressure,ΔP (bar), (b) Flow rate, Q (  $m^3 h^{-1}$ ), (c) Brine salinity,  $w_b$  (ppm), (d) Permeate salinity,  $w_p$  (ppm), (e) Permeation flux of water,  $J_W$  (L  $m^{-2} h^{-1}$ ), (f) CP factor, CPF (–) along the dimensionless length (X).

<span id="page-11-1"></span>**Table 3.** Output results and errors analysis at the system-level coupling with the impermeable wall model (M2) compared with that of using the permeable wall model (M1) with respect to Case 1 ( $L_P = 1 \text{ L m}^{-2} \text{ h}^{-1} \text{ bar}^{-1}$ ), Case 2 ( $L_P = 3 \text{ L m}^{-2} \text{ h}^{-1} \text{ bar}^{-1}$ ), Case 3 ( $L_P = 5 \text{ L m}^{-2} \text{ h}^{-1} \text{ bar}^{-1}$ ) and Case 4 ( $L_P = 10 \text{ L m}^{-2} \text{ h}^{-1} \text{ bar}^{-1}$ ).

|                                             |                   |      |       |        |      | Va     | lue  |        |       |      |      |       |
|---------------------------------------------|-------------------|------|-------|--------|------|--------|------|--------|-------|------|------|-------|
| <b>Output Results</b>                       | tt Results Case 1 |      |       | Case 2 |      | Case 3 |      | Case 4 |       |      |      |       |
|                                             | M1                | M2   | Error | M1     | M2   | Error  | M1   | M2     | Error | M1   | M2   | Error |
| $\overline{w}_{p}$ (ppm)                    | 138               | 139  | 0.55% | 88     | 89   | 0.79%  | 56   | 56     | 1.22% | 40   | 40   | 1.47% |
| $\bar{J}_{W}$ ( $\bar{L}  m^{-2}  h^{-1}$ ) | 18.4              | 18.3 | 0.38% | 34.1   | 33.9 | 0.64%  | 54.5 | 54.0   | 0.99% | 81.0 | 79.9 | 1.26% |
| max ( <i>CPF</i> ) (–)                      | 1.08              | 1.08 | 0.32% | 1.21   | 1.21 | 0.04%  | 1.32 | 1.31   | 0.65% | 1.50 | 1.48 | 1.86% |
| $R_{\rm r}\left(-\right)$                   | 0.43              | 0.43 | 0.38% | 0.50   | 0.49 | 0.64%  | 0.48 | 0.47   | 0.99% | 0.47 | 0.47 | 1.26% |
| $Q_{\rm p} \ ({\rm m}^3 \ {\rm h}^{-1})$    | 164               | 164  | 0.38% | 190    | 189  | 0.64%  | 182  | 181    | 0.99% | 181  | 178  | 1.26% |
| SEC (kWh m <sup>-3</sup> )                  | 2.17              | 2.17 | 0.06% | 2.11   | 2.11 | 0.08%  | 2.12 | 2.12   | 0.12% | 2.11 | 2.12 | 0.14% |

### 4. Conclusions and Outlook

In this paper, we propose a multiscale model framework that couples the CFD models with a permeable wall and an impermeable wall, respectively, and the SWRO model at the system level. The simulated results indicate that the CFD simulations (e.g., velocity, pressure) and the system simulations (e.g., SEC, average permeation flux) using the permeable and impermeable wall models are basic unanimous (error < 2%). The error of the estimated Sherwood number at the system inlet using both models is smaller than 10%, even under extremely high-flux conditions ( $\approx$ 200 L m<sup>-2</sup> h<sup>-1</sup> at system inlet). Furthermore, the impermeable wall model is one-way coupled, which can greatly reduce the computational time compared to the fully coupled permeable wall model. The proposed multiscale framework coupling the impermeable wall model enables the feed spacer design and system design simultaneously for high permeability RO/NF membrane systems. Nevertheless, the im-

*Separations* **2023**, *10*, 134 13 of 15

permeable wall model still has some limitations. On the one hand, it cannot accurately predict the local CP due to the assumed constant concentration boundary condition on membrane walls. On the other hand, the correct relations from *k*m, imp to *k*m, per must satisfy the condition of *J*W/*k*m, imp < 20.

**Author Contributions:** Q.Y.: Methodology, Software, Validation, Formal analysis, Investigation, Visualization, Writing-original draft. Y.H.: Methodology, Writing-review and editing, Supervision, Resources. Y.J.: Methodology, Writing-review and editing. J.L.: Conceptualization, Methodology, Visualization, Writing-original draft, Supervision, Date curation. All authors have read and agreed to the published version of the manuscript.

**Funding:** The author Prof. Dr. Yi Heng acknowledges support provided by Key-Area Research and Development Program of Guangdong Province (No.2021B0101190003), Natural Science Foundation of Guangdong Province (No. 2022A1515011514) and Zhujiang Talent Program of Guangdong Province (2017GC010576). The corresponding author Dr. Jiu Luo thanks support by the project funded by China Postdoctoral Science Foundation (2022M723674).

**Institutional Review Board Statement:** Not applicable.

**Informed Consent Statement:** Not applicable.

**Data Availability Statement:** The data that support the findings of this study are available from the corresponding author (Jiu Luo) upon reasonable request.

**Conflicts of Interest:** All authors in this paper declare no competing interests.

## **References**

<span id="page-12-0"></span>1. Anis, S.; Hashaikeh, R.; Hilal, N. Microfiltration membrane processes: A review of research trends over the past decade. *J. Water Process. Eng.* **2019**, *32*, 100941. [\[CrossRef\]](http://doi.org/10.1016/j.jwpe.2019.100941)

- <span id="page-12-1"></span>2. Mouiya, M.; Abourriche, A.; Bouazizi, A.; Benhammou, A.; El Hafiane, Y.; Abouliatim, Y.; Nibou, L.; Oumam, M.; Ouammou, M.; Smith, A.; et al. Flat ceramic microfiltration membrane based on natural clay and Moroccan phosphate for desalination and industrial wastewater treatment. *Desalination* **2018**, *427*, 42–50. [\[CrossRef\]](http://doi.org/10.1016/j.desal.2017.11.005)
- <span id="page-12-2"></span>3. Al Aani, S.; Mustafa, T.; Hilal, N. Ultrafiltration membranes for wastewater and water process engineering: A comprehensive statistical review over the past decade. *J. Water Process. Eng.* **2020**, *35*, 101241. [\[CrossRef\]](http://doi.org/10.1016/j.jwpe.2020.101241)
- <span id="page-12-3"></span>4. Brover, S.; Lester, Y.; Brenner, A.; Sahar-Hadar, E. Optimization of ultrafiltration as pre-treatment for seawater RO desalination. *Desalination* **2022**, *524*, 115478. [\[CrossRef\]](http://doi.org/10.1016/j.desal.2021.115478)
- <span id="page-12-4"></span>5. Zhou, D.; Zhu, L.; Fu, Y.; Zhu, M.; Xue, L. Development of lower cost seawater desalination processes using nanofiltration technologies—A review. *Desalination* **2015**, *376*, 109–116. [\[CrossRef\]](http://doi.org/10.1016/j.desal.2015.08.020)
- <span id="page-12-5"></span>6. Wafi, M.; Hussain, N.; Abdalla, O.E.-S.; Al-Far, M.; Al-Hajaj, N.; Alzonnikah, K. Nanofiltration as a cost-saving desalination process. *SN Appl. Sci.* **2019**, *1*, 751. [\[CrossRef\]](http://doi.org/10.1007/s42452-019-0775-y)
- <span id="page-12-6"></span>7. Qasim, M.; Badrelzaman, M.; Darwish, N.; Darwish, N.; Hilal, N. Reverse osmosis desalination: A state-of-the-art review. *Desalination* **2019**, *459*, 59–104. [\[CrossRef\]](http://doi.org/10.1016/j.desal.2019.02.008)
- <span id="page-12-7"></span>8. Lim, Y.; Goh, K.; Kurihara, M.; Wang, R. Seawater desalination by reverse osmosis: Current development and future challenges in membrane fabrication—A review. *J. Membr. Sci.* **2021**, *629*, 119292. [\[CrossRef\]](http://doi.org/10.1016/j.memsci.2021.119292)
- <span id="page-12-8"></span>9. Galama, A.; Saakes, M.; Bruning, H.; Rijnaarts, H.; Post, J. Seawater predesalination with electrodialysis. *Desalination* **2014**, *342*, 61–69. [\[CrossRef\]](http://doi.org/10.1016/j.desal.2013.07.012)
- <span id="page-12-9"></span>10. Al-Amshawee, S.; Yunus, M.; Azoddein, A.; Hassell, D.; Dakhil, I.; Hasan, H. Electrodialysis desalination for water and wastewater: A review. *Chem. Eng. J.* **2020**, *380*, 122231. [\[CrossRef\]](http://doi.org/10.1016/j.cej.2019.122231)
- <span id="page-12-10"></span>11. Yadav, A.; Labhasetwar, P.; Shahi, V. Membrane distillation using low-grade energy for desalination: A review. *J. Environ. Chem. Eng.* **2021**, *9*, 105818. [\[CrossRef\]](http://doi.org/10.1016/j.jece.2021.105818)
- <span id="page-12-11"></span>12. Yadav, A.; Patel, R.; Singh, C.; Labhasetwar, P.; Shahi, V. Experimental study and numerical optimization for removal of methyl orange using polytetrafluoroethylene membranes in vacuum membrane distillation process. *Colloids Surf. A Physicochem. Eng. Asp.* **2022**, *635*, 128070. [\[CrossRef\]](http://doi.org/10.1016/j.colsurfa.2021.128070)
- <span id="page-12-12"></span>13. Feinberg, B.; Ramon, G.; Hoek, E. Thermodynamic analysis of osmotic energy recovery at a reverse osmosis desalination plant. *Environ. Sci. Technol.* **2013**, *47*, 2982–2989. [\[CrossRef\]](http://doi.org/10.1021/es304224b) [\[PubMed\]](http://www.ncbi.nlm.nih.gov/pubmed/23331042)
- <span id="page-12-13"></span>14. Lim, Y.; Ma, Y.; Chew, J.; Wang, R. Assessing the potential of highly permeable reverse osmosis membranes for desalination: Specific energy and footprint analysis. *Desalination* **2022**, *533*, 115771. [\[CrossRef\]](http://doi.org/10.1016/j.desal.2022.115771)
- <span id="page-12-14"></span>15. Zhang, Z.; Wu, Y.; Luo, L.; Li, G.; Li, Y.; Hu, H. Application of disk tube reverse osmosis in wastewater treatment: A review. *Sci. Total Environ.* **2021**, *792*, 148291. [\[CrossRef\]](http://doi.org/10.1016/j.scitotenv.2021.148291) [\[PubMed\]](http://www.ncbi.nlm.nih.gov/pubmed/34146802)

*Separations* **2023**, *10*, 134 14 of 15

<span id="page-13-0"></span>16. Colla, V.; Branca, T.; Rosito, F.; Lucca, C.; Vivas, B.; Delmiro, V. Sustainable Reverse Osmosis application for wastewater treatment in the steel industry. *J. Clean. Prod.* **2016**, *130*, 103–115. [\[CrossRef\]](http://doi.org/10.1016/j.jclepro.2015.09.025)

- <span id="page-13-1"></span>17. Licona, K.; Geaquinto, L.; Nicolini, J.; Figueiredo, N.; Chiapetta, S.; Habert, A.; Yokoyama, L. Assessing potential of nanofiltration and reverse osmosis for removal of toxic pharmaceuticals from water. *J. Water Process. Eng.* **2018**, *25*, 195–204. [\[CrossRef\]](http://doi.org/10.1016/j.jwpe.2018.08.002)
- <span id="page-13-2"></span>18. Lin, Y.; Chiou, J.; Lee, C. Effect of silica fouling on the removal of pharmaceuticals and personal care products by nanofiltration and reverse osmosis membranes. *J. Hazard. Mater.* **2014**, *277*, 102–109. [\[CrossRef\]](http://doi.org/10.1016/j.jhazmat.2014.01.023)
- <span id="page-13-3"></span>19. Bejaoui, I.; Mnif, A.; Hamrouni, B. Performance of Reverse Osmosis and Nanofiltration in the Removal of Fluoride from Model Water and Metal Packaging Industrial Effluent. *Sep. Sci. Technol.* **2014**, *49*, 1135–1145. [\[CrossRef\]](http://doi.org/10.1080/01496395.2013.878956)
- <span id="page-13-4"></span>20. Ndiaye, P.; Moulin, P.; Dominguez, L.; Millet, J.; Charbit, F. Removal of fluoride from electronic industrial effluent by RO membrane separation. *Desalination* **2005**, *173*, 25–32. [\[CrossRef\]](http://doi.org/10.1016/j.desal.2004.07.042)
- <span id="page-13-5"></span>21. Zhao, D.; Japip, S.; Zhang, Y.; Weber, M.; Maletzko, C.; Chung, T. Emerging thin-film nanocomposite (TFN) membranes for reverse osmosis: A review. *Water Res.* **2020**, *173*, 115557. [\[CrossRef\]](http://doi.org/10.1016/j.watres.2020.115557)
- <span id="page-13-6"></span>22. Rahmawati, R.; Bilad, M.; Nawi, N.; Wibisono, Y.; Suhaimi, H.; Shamsuddin, N.; Arahman, N. Engineered spacers for fouling mitigation in pressure driven membrane processes: Progress and projection. *J. Environ. Chem. Eng.* **2021**, *9*, 106285. [\[CrossRef\]](http://doi.org/10.1016/j.jece.2021.106285)
- <span id="page-13-7"></span>23. Lin, W.; Zhang, Y.; Li, D.; Wang, X.; Huang, X. Roles and performance enhancement of feed spacer in spiral wound membrane modules for water treatment: A 20-year review on research evolvement. *Water Res.* **2021**, *198*, 117146. [\[CrossRef\]](http://doi.org/10.1016/j.watres.2021.117146)
- <span id="page-13-8"></span>24. Fimbres-Weihs, G.; Wiley, D. Review of 3D CFD modeling of flow and mass transfer in narrow spacer-filled channels in membrane modules. *Chem. Eng. Process.* **2010**, *49*, 759–781. [\[CrossRef\]](http://doi.org/10.1016/j.cep.2010.01.007)
- <span id="page-13-9"></span>25. Anqi, A.; Alkhamis, N.; Oztekin, A. Computational study of desalination by reverse osmosis—Three-dimensional analyses. *Desalination* **2016**, *388*, 38–49. [\[CrossRef\]](http://doi.org/10.1016/j.desal.2016.03.017)
- <span id="page-13-10"></span>26. Lin, W.; Shao, R.; Wang, X.; Huang, X. Impacts of non-uniform filament feed spacers characteristics on the hydraulic and anti-fouling performances in the spacer-filled membrane channels: Experiment and numerical simulation. *Water Res.* **2020**, *185*, 116251. [\[CrossRef\]](http://doi.org/10.1016/j.watres.2020.116251) [\[PubMed\]](http://www.ncbi.nlm.nih.gov/pubmed/32771564)
- <span id="page-13-11"></span>27. Foo, K.; Liang, Y.; Weihs, G. CFD study of the effect of SWM feed spacer geometry on mass transfer enhancement driven by forced transient slip velocity. *J. Membr. Sci.* **2020**, *597*, 117643. [\[CrossRef\]](http://doi.org/10.1016/j.memsci.2019.117643)
- <span id="page-13-12"></span>28. Singh, C.; Yadav, A.; Kumar, A. Numerical simulations of the effect of spacer filament geometry and orientation on the performance of the reverse osmosis process. *Colloid. Surface A* **2022**, *650*, 129664. [\[CrossRef\]](http://doi.org/10.1016/j.colsurfa.2022.129664)
- <span id="page-13-13"></span>29. Li, M.; Bui, T.; Chao, S. Three-dimensional CFD analysis of hydrodynamics and concentration polarization in an industrial RO feed channel. *Desalination* **2016**, *397*, 194–204. [\[CrossRef\]](http://doi.org/10.1016/j.desal.2016.07.005)
- <span id="page-13-14"></span>30. Lin, W.; Lei, J.; Wang, Q.; Wang, X.-m.; Huang, X. Performance enhancement of spiral-wound reverse osmosis membrane elements with novel diagonal-flow feed channels. *Desalination* **2022**, *523*, 115447. [\[CrossRef\]](http://doi.org/10.1016/j.desal.2021.115447)
- <span id="page-13-15"></span>31. Yadav, A.; Singh, C.; Patel, R.; Kumar, A.; Labhasetwar, P. Investigations on the effect of spacer in direct contact and air gap membrane distillation using computational fluid dynamics. *Colloids Surf. A Physicochem. Eng. Asp.* **2022**, *654*, 130111. [\[CrossRef\]](http://doi.org/10.1016/j.colsurfa.2022.130111)
- <span id="page-13-16"></span>32. Koutsou, C.; Yiantsios, S.; Karabelas, A. A numerical and experimental study of mass transfer in spacer-filled channels: Effects of spacer geometrical characteristics and Schmidt number. *J. Membr. Sci.* **2009**, *326*, 234–251. [\[CrossRef\]](http://doi.org/10.1016/j.memsci.2008.10.007)
- <span id="page-13-19"></span>33. Completo, C.; Semiao, V.; Geraldes, V. Efficient CFD-based method for designing cross-flow nanofiltration small devices. *J. Membr. Sci.* **2016**, *500*, 190–202. [\[CrossRef\]](http://doi.org/10.1016/j.memsci.2015.11.012)
- 34. Fimbres-Weihs, G.; Wiley, D. Numerical study of mass transfer in three-dimensional spacer-filled narrow channels with steady flow. *J. Membr. Sci.* **2007**, *306*, 228–243. [\[CrossRef\]](http://doi.org/10.1016/j.memsci.2007.08.043)
- 35. Shakaib, M.; Hasani, S.; Mahmood, M. CFD modeling for flow and mass transfer in spacer-obstructed membrane feed channels. *J. Membr. Sci.* **2009**, *326*, 270–284. [\[CrossRef\]](http://doi.org/10.1016/j.memsci.2008.09.052)
- <span id="page-13-25"></span>36. Liang, Y.; Toh, K.; Weihs, G.F. 3D CFD study of the effect of multi-layer spacers on membrane performance under steady flow. *J. Membr. Sci.* **2019**, *580*, 256–267. [\[CrossRef\]](http://doi.org/10.1016/j.memsci.2019.02.015)
- <span id="page-13-17"></span>37. Toh, K.; Liang, Y.; Lau, W.; Weihs, G. The techno-economic case for coupling advanced spacers to high-permeance RO membranes for desalination. *Desalination* **2020**, *491*, 114534. [\[CrossRef\]](http://doi.org/10.1016/j.desal.2020.114534)
- <span id="page-13-18"></span>38. Geraldes, V.; Afonso, M. Generalized mass-transfer correction factor for nanofiltration and reverse osmosis. *AIChE J.* **2006**, *52*, 3353–3362. [\[CrossRef\]](http://doi.org/10.1002/aic.10968)
- <span id="page-13-20"></span>39. Luo, J.; Li, M.; Heng, Y. A hybrid modeling approach for optimal design of non-woven membrane channels in brackish water reverse osmosis process with high-throughput computation. *Desalination* **2020**, *489*, 114463. [\[CrossRef\]](http://doi.org/10.1016/j.desal.2020.114463)
- <span id="page-13-21"></span>40. Chen, Q.; Luo, J.; Heng, Y. High-Throughput Optimal Design of Spacers Using Triply Periodic Minimal Surfaces in BWRO. *Separations* **2022**, *9*, 62. [\[CrossRef\]](http://doi.org/10.3390/separations9030062)
- <span id="page-13-22"></span>41. Gu, J.; Luo, J.; Li, M.; Huang, C.; Heng, Y. Modeling of pressure drop in reverse osmosis feed channels using multilayer artificial neural networks. *Chem. Eng. Res. Des.* **2020**, *159*, 146–156. [\[CrossRef\]](http://doi.org/10.1016/j.cherd.2020.04.019)
- <span id="page-13-23"></span>42. Luo, J.; Li, M.; Hoek, E.; Heng, Y. Supercomputing and machine learning-aided optimal design of high permeability seawater reverse osmosis membrane systems. *Sci. Bull.* **2023**, in press. [\[CrossRef\]](http://doi.org/10.1016/j.scib.2023.01.039) [\[PubMed\]](http://www.ncbi.nlm.nih.gov/pubmed/36774298)
- <span id="page-13-24"></span>43. Li, F.; Meindersma, W.; Haan, A.; Reith, T. Optimization of commercial net spacers in spiral wound membrane modules. *J. Membr. Sci.* **2002**, *208*, 289–302. [\[CrossRef\]](http://doi.org/10.1016/S0376-7388(02)00307-1)

*Separations* **2023**, *10*, 134 15 of 15

<span id="page-14-0"></span>44. Bucs, S.; Radu, A.; Lavric, V.; Vrouwenvelder, J.; Picioreanu, C. Effect of different commercial feed spacers on biofouling of reverse osmosis membrane systems: A numerical study. *Desalination* **2014**, *343*, 26–37. [\[CrossRef\]](http://doi.org/10.1016/j.desal.2013.11.007)

- <span id="page-14-1"></span>45. Al-Amoudi, A.; Lovitt, R. Fouling strategies and the cleaning system of NF membranes and factors affecting cleaning efficiency. *J. Membr. Sci.* **2007**, *303*, 4–28. [\[CrossRef\]](http://doi.org/10.1016/j.memsci.2007.06.002)
- <span id="page-14-2"></span>46. Zamani, F.; Chew, J.; Akhondi, E.; Krantz, W.; Fane, A. Unsteady-state shear strategies to enhance mass-transfer for the implementation of ultrapermeable membranes in reverse osmosis: A review. *Desalination* **2015**, *356*, 328–348. [\[CrossRef\]](http://doi.org/10.1016/j.desal.2014.10.021)

**Disclaimer/Publisher's Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.
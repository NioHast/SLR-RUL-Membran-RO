![](_page_0_Figure_2.jpeg)

## **OPEN**

# **Physics-informed machine learning for cross-study prediction of oil– water membrane fouling**

**Carine LourencoAlves1,2,3, Silvio EdegarWeschenfelder4, Maria Alice Prado Cechinel1,2, Mariane Carolina Proner1,2, Regina de Fátima1, Peralta Muniz Moreira1, AlanAmbrosi2, Marco Di Luccio2 & Sergio Yesid GómezGonzález3**

**Performance decay driven by coupled transport, accumulation, and removal processes remains a central challenge in many chemical engineering systems. Membrane fouling in oil–water separation is examined here as a representative case. While numerical and empirical models can capture specific cases, their predictive performance across independent studies remains limited. In this work, we combine a reduced-order finite-element model of transport and fouling resistance with a data-driven framework that maps experimental metadata to flux-decline behavior across 112 datasets involving various membranes, oils, and operating conditions. The reduced representation reproduces flux–time trajectories with high fidelity (average R2 ≈0.95). Mapping experimental metadata to curve descriptors enables stage-resolved prediction of normalized flux, yielding mean absolute errors of 0.08–0.14 under grouped cross-validation. External validation using publication-level holdouts shows that differences between studies, rather than model capacity, limit predictive performance, highlighting the need for data standardization. The analysis indicates links between crossflow and pressure and early-stage fouling, while porosity and permeance relate to steady-state flux. Based on these results, we propose a minimal checklist of parameters needed for reproducible fouling models. The results quantify the impact of metadata completeness on model transferability and provide a reproducible framework for cross-study analysis of time-dependent membrane performance.**

Membrane fouling[1](#page-17-0) remains a major limitation in oil–water separation processes, leading to progressive flux decline and reduced operational efficiency. Although the mechanisms governing fouling, such as pore blocking, surface deposition, and shear-induced removal are qualitatively well understood, predictive models often remain system-specific and difficult to generalize across different membranes, feed compositions, and operating conditions[2](#page-17-1)[–4](#page-17-2) .

Rapid growth in the global economy and the oil sector has intensified the generation of domestic and industrial oily wastewater streams[5,](#page-17-3)[6](#page-17-4) . Treating this wastewater is not only crucial for environmental protection and resource recovery but also aligns directly with *UN Sustainable Development Goal 6 (clean water and sanitation)*[7](#page-17-5) . Achieving this goal requires innovative, energy-efficient, and sustainable technologies capable of treating complex industrial effluents while minimizing environmental impact. Traditional oil–water separation techniques, such as centrifugation, flocculation, and air flotation, are often effective for bulk-phase separation but may struggle to remove stable emulsions, particularly those containing surfactants[8](#page-17-6) . In contrast, membrane separation technologies offer advantages in handling finely dispersed and emulsified oil–water mixtures. While membrane processes are generally more energy-efficient than thermal separation methods, their energy consumption and operational costs can be comparable to or higher than conventional mechanical separation techniques, depending on operating conditions and fouling behavior. Their main advantage lies in their ability to achieve high separation efficiency for stable emulsions under relatively compact and controllable operating conditions[1](#page-17-0) . This technology can also effectively handle a wide variety of oil-water mixtures. Because

<sup>1</sup>Laboratory of Energy and Environment – LEMA, Department of Chemical and Food Engineering, Federal University of Santa Catarina, Florianópolis 88040-970, SC, Brazil. 2Laboratory of Membrane Processes – LABSEM, Department of Chemical and Food Engineering, Federal University of Santa Catarina, Florianópolis 88040-970, SC, Brazil. 3Laboratory of Mass Transfer, Department of Chemical and Food Engineering, Numerical Simulation of Chemical Systems – LABSIN-LABMASSA, Federal University of Santa Catarina, Florianópolis 88040- 970, SC, Brazil. 4Petrobras Research Center – CENPES, Rio de Janeiro 21941-915, RJ, Brazil. email: [carine.lourenco.alves@gmail.com](mailto:carine.lourenco.alves@gmail.com)

of its adaptability, membrane separation technology has broad applications for treating oily wastewater and is considered one of the most effective methods available 9-11.

Advanced membrane technologies, such as nanofiltration and reactive membranes, are increasingly critical for achieving higher flux, superior separation, and sustainability goals and targets in water treatment. While these advances create new opportunities, they also introduce significant complexity to the design and scale-up processes<sup>12</sup>. A key technological obstacle in membrane separation is the reduction of permeate flow. This is caused by resistance to transmembrane flow, which occurs when pores are blocked and when molecules adsorb onto the membrane surface and within the porous media during the microfiltration process<sup>13</sup>. Beyond this, challenges with scalability, cost, and maintenance remain significant hurdles, as outlined by Sutrisna et al.<sup>9</sup>. The issues of fouling, scaling, and the durability of membranes—especially in harsh environments- have therefore become the central focus of research on ceramic membranes for oil-water separation<sup>14-17</sup>.

Other membrane technologies, such as reverse osmosis (RO), are also frequently used in treating produced water, especially when total dissolved solids (TDS) levels are high <sup>18,19</sup>. That said, the main fouling mechanisms in RO systems are distinct from those in MF/UF systems, in which osmotic effects, concentration polarization, and scaling are more influential, whereas pore blocking and surface deposition are less dominant <sup>20</sup>. Consequently, the current framework is centered on MF/UF-type systems, where the decline in flux is mainly driven by fouling from particulates and emulsions. Adapting this approach to RO systems would require adding further transport and physicochemical parameters that account for high-pressure and high-salinity environments.

Advances in computer science have enabled the use of numerical simulation methods, such as computational fluid dynamics (CFD), Monte Carlo (MC) simulations, and artificial neural networks (ANNs), for modeling membrane fouling<sup>21–25</sup>. While these tools can capture specific scenarios more richly than classical theory, they have struggled to generalize across studies due to heterogeneous materials, operating conditions, and oil chemistry. Yang et al. emphasized that, despite the critical need to understand fouling mechanisms, fouling characteristics, and fouling control measures, few studies have been published that provide an overview of fouling modeling, particularly for numerical simulation of fouling<sup>21</sup>. This gap is even wider for oil–in–water applications.

Recent reviews have highlighted the increasing use of machine learning in membrane fouling prediction and desalination processes, while also emphasizing challenges related to model selection, descriptor definition, and data consistency across studies<sup>3,16,26</sup>. While simulations can describe specific operating conditions, their ability to generalize across studies is limited by variations in membrane materials, operating parameters, and feed compositions reported in the literature. In this context, the present work focuses on analyzing this lack of transferability by combining a reduced-order finite-element model (ROM) with a data-driven analysis of experimental datasets. Rather than developing a new predictive model in isolation, the approach examines how experimental metadata relates to flux-decline behavior across heterogeneous studies.

The framework quantifies between-study heterogeneity as a primary limitation for predictive modeling and evaluates how experimental metadata can be used to reconstruct flux-decline behavior across heterogeneous datasets. The results show that predictive performance is primarily constrained by metadata completeness rather than model capacity, highlighting the need for more consistent reporting to enable transferable fouling models. Within the scope of this study, the framework provides a reproducible approach to analyzing time-dependent fouling behavior across independent studies and directly supports global clean water initiatives, such as the United Nations Sustainable Development Goal 6. This work provides (i) a transferable physics-informed learning framework, (ii) a quantitative measure of cross-study generalization loss, and (iii) a minimal metadata standard required for reproducible fouling prediction.

#### Results

Model agreement was high across the compiled dataset, with the reduced-order finite element method implemented in Python yielding an average R<sup>2</sup> of 0.95 (Fig. 1a).

The normal probability plot of R² values (Fig. 1a) and histogram distribution of R² (Fig. 1b) are used to qualitatively illustrate the distribution of model performance across the dataset rather than to infer strict statistical normality. The distribution of R² values across all fitted cases shows that most simulations achieve high goodness-of-fit, with values clustered near unity. This indicates that the reduced-order formulation provides a consistent representation of flux decline behaviour across most experimental conditions. A small number of lower R² values are observed, reflecting cases where the simplified functional forms are less representative, which is expected given the heterogeneity of fouling mechanisms in the compiled dataset. The distribution of selected model forms (Fig. 1b) shows that the hybrid formulation is most frequently identified as the best representation, followed by logistic and exponential forms, indicating the prevalence of multistage fouling behaviour across the compiled dataset.

Among the tested functional forms (power-law, exponential, logistic, and hybrid; see Table 4), the hybrid model achieved the highest predictive performance for most datasets (Fig. 1b). The hybrid formulation combines an early-time exponential decay with a late-time algebraic relaxation and allows for a non-zero asymptotic resistance. This structure provided improved flexibility in capturing both the rapid initial flux decline and the slower long-time behavior observed in the compiled experimental trajectories.

Pairwise correlations were evaluated between experimental metadata (e.g., pressure, pore size, and cleanwater permeability  $J_{wh}$ ) and canonical flux features derived from the fitted normalized curves. The extracted descriptors included terminal normalized flux level ( $J_{\infty}^{\rm n}$ ), a half time ( $t_{50}$ ), initial slope ( $J_0'$ ), early- time throughput based on the initial 10% ( $AUC_{0-10}$ ) and the early-time throughput based on the initial 30% ( $AUC_{0-30}$ ). To account for non-Gaussian distributions and heterogeneous sampling across studies, Spearman's rank correlation with two-sided p-values was employed 27,28.

<span id="page-2-0"></span>![](_page_2_Figure_1.jpeg)

**Fig. 1.** Agreement of the proposed reduced order FEM method (a) Normal probability of the obtained  $R^2$  agreement (b) Histogram (c) Frequency percentage of the best agreement models for the time-dependent fouling resistance.

<span id="page-2-1"></span>![](_page_2_Figure_3.jpeg)

**Fig. 2.** (a) Spearman correlation matrix between experimental metadata ( $\mathbb{R}^2$ , NRMSE, pore size, pressure,  $J_{wh}$ ), and canonical features of the normalized flux curve ( $J_{\infty}^n$ ,  $t_{50}$ ,  $J_0'$ ,  $AUC_{0-10}$  and  $AUC_{0-30}$ ). Correlation between P1 and (**b**) pressure, (**c**) oil rejection, (**d**) pore size, and (**e**) porosity.

Pairwise correlation analysis revealed that early-time throughput metrics  $(AUC_{0-10}, AUC_{0-30})$  were positively associated with the terminal normalized flux  $(J_{\infty}^n)$  and half-time  $(t_{50})$  (Fig. 2a). The initial slope  $(J_0')$  became increasingly negative for cases with lower AUC values, indicating a steeper initial flux decline. Larger pore sizes were generally associated with higher  $J_{\infty}^n$  and  $t_{50}$ , whereas higher pressure was associated with lower  $t_{50}$ , consistent with faster fouling.

The fitted coding parameters (P1-P3), derived from the fouling-resistance models, were further examined for correlations with processing conditions and oil rejection (Fig. [2](#page-2-1)(b-e)). Across the compiled dataset, no consistent monotonic relationships were observed between these parameters and individual operational or structural variables. Additional correlations for P2 and P3 are provided in the Supplementary Information.

A parallel analysis was conducted to evaluate the extent to which normalized flux trajectories encode information about experimental metadata. Features were extracted from the curves using two complementary representations: convolution-based features (MiniRocket[\)29](#page-17-23) and physically interpretable shape descriptors (e.g., AUCs, segment slopes, and variability). Model performance was assessed using each representation individually and in combination to determine how different feature types capture information relevant to the underlying process conditions.

Two combination strategies were evaluated. In the first, feature vectors were concatenated after their respective preprocessing steps. In the second, a logarithmic transformation log(1 + *x*) was applied to the concatenated features to account for skewed distributions. Model performance for numeric targets was quantified using mean absolute error (MAE), while categorical targets (membrane material and oil type) were evaluated using macro-F1 and accuracy. Results are summarized in Fig. [3a](#page-3-0)-c, respectively.

Under publication-level GroupKFold, shape-based features consistently outperformed convolution-based features (MiniRocket) for categorical targets. For membrane material, shape features achieved a macro-F1 of 0.41 (accuracy=0.49), compared to 0.08 for MiniRocket (Fig. [3c](#page-3-0)). For oil type, macro-F1 reached 0.20 (accuracy=0.54) for shape features versus 0.07 for MiniRocket (Fig. [3b](#page-3-0)). Combining feature sets increased accuracy (0.50 for membrane material and 0.63 for oil type) but reduced macro-F1, indicating sensitivity to class imbalance and uneven representation across studies.

For numerical targets, the recoverable signal was limited but measurable. Applying a logarithmic transformation improved prediction accuracy, with the most reliable estimates obtained for crossflow, cleanwater flux (Jwh), oil concentration, pressure, and porosity. In contrast, pore size and salt concentration were more difficult to infer quantitatively from the flux trajectories, indicating weaker regression performance.

When analysed from a classification and time-localized perspective, however, certain variables such as crossflow velocity and pore size exhibited consistent and detectable signals within specific time segments of the

<span id="page-3-0"></span>![](_page_3_Figure_7.jpeg)

**Fig. 3**. Performance evaluation across feature sets (**a**) Numeric and Macro F1-score for categorical classifications. (**b**) Classification performance for oil types (c) Classification performance for materials.

flux trajectory (Fig. [4](#page-4-0)a–c). This indicates that, while these variables may be difficult to recover accurately in a global regression sense, they still leave identifiable signatures in the temporal structure of the flux decline.

Figure [4](#page-4-0) combines prediction performance, uncertainty quantification, and time-window importance to provide a comprehensive view of model behaviour. For clarity, these components are discussed sequentially below. First, predictive performance is evaluated across key variables to assess model accuracy and generalization. Second, time-window importance is analysed to identify when specific physical parameters influence flux decline, providing insight into the temporal evolution of fouling mechanisms.

. The normalized flux trajectory was divided into six equal segments (S1–S6) along the time axis. Segment S1 corresponds to the initial phase immediately after the onset of filtration, when flux remains close to its initial value and changes are minimal. As a result, S1 provides limited discriminatory information and is not emphasized in the analysis, whereas subsequent segments (S2–S6) capture the evolution of fouling dynamics across the early, transition, and late stages. Segments S2–S3 represent early-stage fouling, S4 corresponds to transition behavior, and S5–S6 capture late-stage resistance stabilization.

Time-window permutation analysis revealed that the information content is not uniformly distributed along the normalized time axis. Crossflow was most influential in early segments (S2), whereas porosity and cleanwater permeance contributed more strongly to the late segments (S5–S6). Pore size showed peak importance in the mid-time region (S4), while oil type exhibited comparatively weaker and more diffuse contributions (Fig. [4d](#page-4-0)). These temporal patterns are consistent with the expected roles of operating conditions and membrane properties during different stages of fouling. This temporal decomposition provides a direct link between statistical importance and physically interpretable fouling stages. The observed importance patterns were stable across repeated permutations, indicating that the temporal trends are robust with respect to random shuffling variability. The relative importance across segments (S2–S6) highlights that different physical variables dominate distinct fouling stages, reinforcing the multistage interpretation of flux decline dynamics.

Classification of membrane material and oil type directly from normalized flux curves using shape features yielded a macro-F1 score of 0.196 [95% CI: 0.119–0.262] for membrane material (9 classes), exceeding both majority and uniform baseline models. In contrast, classification performance for oil type was close to baseline levels, indicating limited discriminative information in the flux trajectories for this variable.

Models were trained to map experimental metadata to curve descriptors derived from normalized flux trajectories, using publication-grouped cross-validation to prevent cross-study leakage. A PCA basis fitted to the normalized curves captured approximately 99.3% of the total variance, indicating that the flux trajectories can be represented in a low-dimensional space. This suggests that prediction errors are more likely to be associated with estimating the corresponding coefficients from metadata rather than with limitations in the curve representation itsel[f30](#page-17-24)[–32](#page-17-25).

The regression model was evaluated using two complementary validation schemes (Fig. [5](#page-5-0)a). Grouped crossvalidation represents within-study prediction, in which training and test samples originate from the same

<span id="page-4-0"></span>![](_page_4_Figure_8.jpeg)

**Fig. 4**. Bidirectional reliability and feature relevance of the ML model. Prediction-interval reliability for the metadata prediction from flux curves for (**a**) crossflow velocity, (**b**) oil type, and (**c**) pore size. (**d**) Normalized feature importance aggregated across cross-validated surrogates (S2–S6).

<span id="page-5-0"></span>![](_page_5_Figure_1.jpeg)

**Fig. 5**. Cross-study generalization and metadata-based prediction of fouling behaviour. (**a**) Mean absolute error (MAE) for flux-curve prediction using membrane and foulant metadata, evaluated under Grouped CV (within-study), Publication Hold-out (unseen studies), and grouping by oil type. (**b**) Normalized feature importance for the prediction model. (**c**–**d**) Representative experimental and predicted flux decline curves under the publication hold-out scheme, comparing model predictions (red dashed line) with experimental data (black solid line) for two different membranes.

experimental dataset. In contrast, publication hold-out evaluation excludes entire studies from training and therefore reflects true generalization across independent experimental conditions and therefore represent outof-distribution predictions.

The resulting mean absolute errors (MAE) in normalized-flux units were 0.079±0.01, 0.14±0.02, and 0.14±0.02 for the early, mid-, and late-time segments, respectively. For clarity, the early-, mid-, and late-time regions correspond to the previously defined segmented windows: early-stage (S2–S3), mid-stage (S4), and latestage (S5–S6), while S1 represents the initial near-constant flux region. When transitioning from grouped crossvalidation to publication hold-out, the MAE increased by approximately a factor of two, providing a quantitative measure of cross-study domain shift. The uncertainty bars further indicate increasing variability at longer times.

Global SHAP analysis (Fig. [5](#page-5-0)b), aggregated over the latent Principal Components (PCs) and projected back onto the flux trajectory, identifies porosity as the dominant contributor to curve shape, followed by pore size and crossflow. Secondary but systematic effects are attributed to droplet size, salt concentration, and clean-water flux.

Representative predictions under publication hold-out conditions are shown Fig. [5](#page-5-0)c-d. These examples illustrate the model's performance when applied to unseen studies, where it captures the general shape of the flux decline but exhibits deviations that become more pronounced in the mid- and late-time regions. These deviations reflect the impact of heterogeneous experimental conditions and incomplete metadata rather than model inconsistency.

Figure [5](#page-5-0) is structured to provide a unified view of model behaviour: panel (a) quantifies predictive performance, panel (b) identifies the dominant influencing variables, and panels (c–d) illustrate how these factors translate into prediction accuracy at the curve level. While predictive accuracy decreases under crossstudy conditions, the framework retains value as a diagnostic and comparative tool, capturing dominant fouling trends while explicitly identifying the limits of generalization.

The calibration plot (Fig. [6a](#page-6-0)) shows that the predicted flux trajectories are well aligned with the measured behavior, with the average observed flux closely following the 1:1 line across time bins. This indicates that the regression model is well calibrated and provides quantitatively consistent predictions. The calibration analysis shown in Fig. [6](#page-6-0)a is based on predictions obtained under the publication hold-out scheme, ensuring that the

<span id="page-6-0"></span>![](_page_6_Figure_4.jpeg)

$$NMRSE_{y0} = \frac{RMSE}{J_0}$$

$$NMRSE_{range} = \frac{RMSE}{J_{max} - J_{min}}$$

![](_page_6_Figure_9.jpeg)

**Fig. 6**. Information–reliability tradeoff and physical drivers of curve reconstruction (**a**) Calibration plot comparing predicted and observed normalized flux values. The red dashed line represents the ideal 1:1 agreement, while markers indicate binned averages across the dataset. Flux values are expressed in normalized units (J/J₀). (**b**) Decomposition of the error metric with metadata fields (c) SHAP feature ranking for most influential parameters controlling the reconstructed flux-decay shape.

observed agreement reflects generalization across unseen studies rather than interpolation within the training data.

The effect of metadata richness is shown in Fig. [6b](#page-6-0), where the median NRMSE decreases as additional physical descriptors are progressively included, reaching a stable minimum at approximately 10–12 parameters. This trend suggests that improved prediction accuracy is driven primarily by the availability of more complete and informative metadata rather than by increased model complexity. While increasing the number of descriptors improves accuracy, a reduced subset of dominant descriptors (e.g., porosity, pore size, and crossflow) captures most of the predictive signal, with additional variables providing diminishing improvements.

Feature importance analysis (Fig. [6c](#page-6-0)) identifies porosity as the dominant contributor to curve reconstruction, followed by oil concentration and water flux. In contrast to Fig. [5](#page-5-0)b, which reflects feature influence through latent principal components, Fig. [6](#page-6-0)c represents the direct contribution of experimental variables within the regression model predicting normalized flux trajectories. As such, Fig. [6](#page-6-0)c provides the most direct basis for interpretation in terms of experimental relevance, as it quantifies how individual physical descriptors influence predictive accuracy. In this context, the dominance of porosity and oil concentration highlights their central role in shaping fouling dynamics, while the reduced contribution of additional variables suggests diminishing returns when expanding descriptor sets beyond a core subset. Together, these analyses provide complementary perspectives, in which Fig. [5](#page-5-0)b captures how variables influence the learned latent structure of flux behaviour, while Fig. [6](#page-6-0)c translates these effects into directly interpretable contributions at the level of experimental parameters.

Pairwise correlation analysis revealed strong associations between porosity and clean-water permeance, as well as between pore size and permeance, indicating partial redundancy among structural descriptors in the compiled dataset.

Alternative representations of the flux trajectories using image-based encodings (pyts) were also explored. When combined with shape-based descriptors, these features led to small but consistent improvements in prediction performance.

Incorporating these features into the combined representation resulted in modest error reductions for several numerical targets after applying a log(1+x) transformation, as well as slight improvements in material classification (schematized in Fig. [7](#page-7-0)a). The overall agreement with experimental data improved marginally,

<span id="page-7-0"></span>![](_page_7_Figure_7.jpeg)

**Fig. 7**. (**a**) Integration of pyts- based time-correlation[33](#page-17-26) encoding into the ML pipeline for flux prediction and interpretability (**b**) Representative GAF maps from different fouling regimes.

while the main conclusions regarding cross-study variability and metadata limitations remained unchanged. However, these gains depend not only on the inclusion of pyts features but also on the feature transformation and combination strategy. In particular, the log(1+x) scaling and the stacking of complementary feature sets both contribute to the observed improvements. Therefore, the performance increase cannot be attributed solely to the pyts representations, but rather to the interaction between representation, transformation, and model structure.

The corresponding GAF maps provide a qualitative visualization of temporal patterns in the flux trajectories, with distinct textures reflecting differences in fouling behavior (s. Figure [8](#page-8-0)b).

This clustering behavior confirms the temporal relationships identified by the permutation importance analysis: early-stage factors, such as crossflow and pressure, define the initial phase, while late-stage factors, such as porosity and clean-water permeance, dictate the late-term behavior. The proposed model was further validated by laboratory experiments, yielding high agreement (R2=0.98; s. Figure [8\)](#page-8-0). The experimental validation, however, is limited to dead-end conditions and therefore does not capture shear-induced removal mechanisms typical of crossflow systems. These experiments therefore provide validation of the model structure under simplified conditions, while highlighting the need for further validation under crossflow regimes.

Three main findings can be highlighted. First, normalized flux trajectories are intrinsically low-dimensional and can be accurately reconstructed using reduced-order representations. Second, predictive performance degrades significantly under publication-level hold-out, demonstrating that cross-study variability and incomplete metadata are the primary limitations for generalization. Finally, the temporal analysis reveals that different physical parameters govern distinct stages of fouling, with structural descriptors (e.g., porosity) dominating late behavior, while operational parameters (e.g., crossflow) influence early-stage dynamics. These findings indicate that the main barrier to predictive modeling in membrane fouling is not model complexity; rather, cross-study variability and limited metadata availability constrain predictive performance. This performance degradation is referred to here as a cross-study generalization penalty, arising from heterogeneous experimental reporting.

#### **Discussion**

The reduced-order framework achieved high agreement across the compiled dataset, with an average R² of approximately 0.95. The performance of the hybrid formulation can be attributed to its structural flexibility, which combines early exponential decay with late-time algebraic relaxation and an optional nonzero asymptote.

This functional form is consistent with multistage fouling behavior, in which an initially rapid and partially reversible decline transitions into slower, history-dependent growth of resistance. Such behavior aligns with pore-blocking and cake-formation mechanisms described in classical fouling models, including Hermia-type frameworks and fractional relaxation approaches, where early-time responses resemble exponential decay and long-time behavior follows algebraic trends [34](#page-17-27)–[36](#page-17-28). The inclusion of an asymptotic resistance further captures the residual irreversible contribution typically captured in resistance-in-series descriptions.

It is worth noting that the compiled datasets span a range of fouling regimes that may not be equally well represented by the hybrid functional form. Systems dominated by biofouling may exhibit lag–growth behavior, while scaling processes can involve induction periods followed by accelerated deposition. These dynamics may deviate from the monotonic decay patterns captured by the present formulation, potentially leading to reduced agreement in specific cases. Such deviations reflect additional physicochemical processes not explicitly represented in the reduced-order description and highlight the limitations of applying a single functional form across heterogeneous datasets.

<span id="page-8-0"></span>![](_page_8_Figure_9.jpeg)

**Fig. 8**. Summary of model validation and minimal metadata framework (**a**) Experimental validation of the predictive model for two representative tubular membranes (**b**) Minimal physical descriptor set for transferable modeling outlining the essential metadata required for reproducible and transferable fouling prediction.

The observed associations between early-time AUC metrics and both terminal flux level and half-time further support the multistage interpretation of fouling dynamics. Systems exhibiting a steeper initial decline tend to sustain lower long-term normalized flux, indicating coupling between early deposition kinetics and subsequent resistance buildup. This behaviour is consistent with classical blocking and cake-growth mechanisms in membrane filtration.

Several of the extracted descriptors (e.g., AUC, initial slope, half-time, and terminal flux) are derived from the same fitted flux trajectory and are therefore not statistically independent. As a result, some of the observed correlations among these features reflect inherent mathematical coupling rather than independent physical relationships. In contrast, correlations between these descriptors and external experimental variables (e.g., pore size, pressure, or crossflow conditions) provide more meaningful insight into the underlying transport and fouling mechanisms. This distinction is important when interpreting the correlation structure, as it separates intrinsic curve properties from physically driven associations.

The correlations observed between curve descriptors and external experimental variables provide insight into the dominant mechanisms governing fouling dynamics. For example, the association between larger pore sizes and higher terminal flux or longer characteristic times (t₅₀) suggests reduced susceptibility to rapid pore blocking, consistent with a transition toward cake-dominated filtration regimes [36](#page-17-28). Similarly, the influence of operating pressure on early-time descriptors reflects its role in accelerating initial deposition rates, which may enhance pore blocking or compaction effects depending on the system.

Crossflow-related trends, when present, are consistent with shear-mediated mitigation of fouling, particularly in early stages where particle transport and deposition are most dynami[c3](#page-17-18)[,37](#page-17-29). While these relationships do not provide direct predictive rules due to cross-study variability, they indicate that the extracted descriptors capture physically meaningful signatures of transport and fouling behaviour. As such, they can support comparative analysis across systems and guide the interpretation of fouling dynamics under varying membrane properties and operating conditions. These trends are consistent with established fouling theory but should be interpreted qualitatively due to cross-study variability.

Despite the descriptive accuracy of the reduced-order fits, the mapping between the fitted parameters ( P1-P3) and experimental metadata did not reveal stable monotonic relationships. Screening across pressure, pore size, droplet size, oil concentration, crossflow velocity, porosity, and clean water permeance showed that no single parameter could consistently explain the fitted coefficients. This absence of clear univariate trends suggests that fouling dynamics within the compiled dataset are governed by multivariate interactions rather than isolated experimental factors.

Consequently, although the reduced-order model accurately reconstructs individual flux trajectories, it does not directly generalize to unseen conditions without recalibration. The fitted coefficients, therefore, function primarily as descriptive representations of observed behavior, rather than predictive descriptors directly linked to explicit processing variables.

The comparative analysis further indicates that normalized flux trajectories encode measurable information about certain operational and structural parameters. Shape-based descriptors consistently outperformed convolution-based representations under publication-level validation, suggesting that physically interpretable curve features capture more robust signals across heterogeneous studies. In contrast, MiniRocke[t29](#page-17-23) features appear more sensitive to distribution shifts between publications.

The greater recoverability of the membrane material relative to the oil type reflects differences in how structural and chemical descriptors are expressed in flux decline behavior. Membrane material and porosity directly influence hydraulic resistance and permeance, leading to persistent signatures across both early and late stages of filtration. In contrast, the effects of oil chemistry depend strongly on interfacial properties, such as droplet size distribution, surfactant content, and oil–membrane affinity, which were inconsistently reported across studies. As a result, oil type alone acts as an incomplete surrogate for the underlying physicochemical interactions governing fouling dynamics.

Time-window permutation analysis further revealed distinct temporal patterns in how different parameters influence the flux trajectory. Crossflow exhibited its strongest influence in the early stage (S2), indicating that the initial flux decline is highly sensitive to shear condition[s36.](#page-17-28) Pressure showed a bimodal contribution (S3 and S6), consistent with both an early acceleration of fouling and a later influence on the terminal flux. In contrast, porosity was most influential in the late stage (S6), reflecting its control over steady-state resistance once the fouling layer is established [38](#page-17-30). Pore-size peaks in the mid-time regime (S4), highlighting the transition phase in which pore-scale mechanisms interact with forming cake layers. Clean-water permeance (Jwh) is late-weighted (S5–S6), matching its influence on the asymptote/throughput after fouling sets in. Finally, the oil type is weak overall, with only a small mid-time signal (S4), suggesting that chemistry leaves a modest, diffuse signature in the trajectory. These results highlight that the interpretability of flux trajectories is inherently limited by the level of detail in the reported experimental descriptors.

The influence of membrane material and oil type on the "process identity" encoded in the flux trajectory was analyzed by classifying both targets directly from normalized curves using shape-based features. For the membrane material (9 classes), the classifier outperformed baseline models, achieving a macro-F1 score of 0.196 [95% CI: 0.119–0.262] and an accuracy of 0.188 [95% CI: 0.116–0.259], compared to a majority baseline of approximately 0.053 and a uniform random baseline of 0.120. In contrast, classification performance for oil type was close to baseline levels, indicating limited discriminative information in the flux trajectories for this variable.

It is worth noting that this difference reflects how structural and chemical descriptors manifest in fouling behavior. Membrane material and porosity directly influence hydraulic resistance and permeance, producing consistent signatures across the flux trajectory. In contrast, oil chemistry depends on interfacial properties, such as droplet size distribution, surfactant content, and oil–membrane affinity, which were sparsely and inconsistently reported across studies. As a result, oil type alone acts as an incomplete surrogate for the underlying physicochemical interactions governing fouling dynamics. These findings indicate that, while flux trajectories encode information related to membrane structure and permeability [39](#page-17-31)[–42,](#page-17-32) their ability to resolve oil-specific mechanisms is fundamentally constrained by cross-study variability and incomplete metadata, rather than by limitations of the modeling approach. This further supports the interpretation that structural descriptors leave more persistent and recoverable signatures in flux decline than chemical descriptors under heterogeneous reporting conditions.

This interpretation is subject to several limitations, including inconsistent publication identifiers (which precluded strict GroupKFold validation), class imbalance, and inherent label noise. In particular, the "material" label often conflates base polymer type with surface modifications (e.g., coatings, grafting, or fillers), which likely contributes to the observed reduction in macro-F1 performance. These factors indicate that incorporating richer and more consistently reported metadata, as well as increasing sample size, would improve model robustness and classification performance.

The high variance retention achieved by PCA (99.3%) indicates that normalized flux trajectories are intrinsically low-dimensional. This suggests that the observed behavior can be effectively represented in a compact latent space, and that residual reconstruction errors are primarily due to estimating the corresponding coefficients from metadata rather than to limitations in the representation itself [30–](#page-17-24)[32](#page-17-25). Consequently, the degradation in predictive performance under cross-study conditions is more likely driven by incomplete or heterogeneous metadata than by insufficient model expressiveness. This distinction is critical for interpreting predictive performance in heterogeneous datasets, as it shifts the focus from model development toward data quality and reporting practices.

The approximately twofold increase in MAE under publication hold-out highlights the sensitivity of the model to cross-study heterogeneity. While grouped cross-validation evaluates interpolation within comparable experimental settings, publication hold-out probes generalization across differing membrane materials, operating ranges, and reporting practices. The observed performance degradation, therefore, reflects domain shift rather than overfitting.

Given the low-dimensional representation of the flux trajectories established earlier, this degradation is unlikely to arise from limitations in the modeling framework. Instead, it indicates that incomplete or inconsistently reported metadata restricts the model's ability to infer the correct mapping under unseen conditions. In this context, cross-publication variability emerges as a primary constraint on predictive transferability.

The calibration results further show that, within the bounds of available metadata, the regression models provide quantitatively consistent predictions. The widening of uncertainty bands during periods of rapid flux decline suggests coherent uncertainty propagation rather than random dispersion, supporting the interpretability of the predicted trajectories.

The reduction in NRMSE with increasing metadata dimensionality highlights the importance of descriptor richness. The plateau observed at approximately 10–12 parameters suggests that a minimum set of physical descriptors is required to constrain flux-decline dynamics. Below this threshold, under-specified models struggle to capture the multivariate interactions governing fouling.

Feature-importance analysis identifies porosity as the dominant structural determinant of curve reconstruction, consistent with its role in setting baseline hydraulic resistance and influencing late-stage behavior. Crossflow and pore size follow as influential parameters, while droplet size, salt concentration, and clean-water flux exhibit secondary but systematic effects. Oil concentration and clean-water flux primarily contribute to early- and mid-stage dynamics, whereas crossflow exerts its strongest influence in the initial phase. The consistency between global importance metrics and SHAP-based directional analysis supports a physically coherent hierarchy of parameter influence. These rankings quantify influence on predictive reconstruction rather than direct mechanistic causation. The remaining degradation in publication hold-out performance further highlights the limitations imposed by incomplete metadata, as key parameters influencing fouling kinetics are not consistently reported across studies.

Collectively, these results indicate that predictive performance is primarily constrained by metadata completeness and cross-study variability rather than by limitations of the modeling framework. This finding underscores the need for more consistent and comprehensive reporting practices and motivates the standardized metadata checklist proposed in this work to improve reproducibility and cross-study transferability in membrane fouling modeling.

The remaining limitations in cross-study generalization are expected to decrease with the inclusion of more descriptive and consistently reported metadata (e.g., emulsifier chemistry, temperature, and pre-treatment history) and with larger, more diverse datasets. The observed collinearity between porosity, pore size, and clean water permeance reflects their shared physical basis in governing intrinsic membrane permeability. As a result, once porosity and pore size are included, clean water permeance contributes a limited additional predictive signal. This explains its reduced relative importance in SHAP analysis despite its well-established experimental relevance.

Alternative representations of the flux trajectories using image-based encodings (GAF/MTF) were also explored. These representations preserve temporal correlations and provide a qualitative view of the flux-decay patterns, capturing differences in early-stage decline and long-term behavior. Incorporating these features into the combined model improved agreement with experimental data, particularly for targets sensitive to subtle changes in curve shape. However, these improvements did not change the main conclusions, which remain governed by metadata availability and cross-study variability.

The temporal alignment between clustering behavior and permutation importance reinforces the mechanistic coherence of the framework. Early-time dominance of crossflow and pressure reflects their influence on incipient deposition and shear-mediated removal, whereas porosity and clean-water permeance exert stronger control over late-stage resistance stabilization. The agreement between statistical feature importance and physically interpretable parameters indicates that the learned representations capture structured transport dynamics rather than arbitrary correlations.

Experimental validation further shows that the reduced-order model reproduces flux-decline trends under controlled laboratory conditions. The strong agreement observed across distinct tubular geometries suggests that the reduced-order representation retains sufficient physical structure to remain consistent under moderate variations in configuration.

From an operational perspective, these results highlight the limitations of predictive fouling models when applied across heterogeneous datasets. They emphasize that reliable model-based analysis depends strongly on the availability and consistency of experimental metadata. This type of predictive capability is consistent with previous work on fouling-informed process optimization.

The key outcome of this study is outlined in Fig. [8](#page-8-0). The proposed model reproduces experimental fluxdecline trends across different membrane geometries (Fig. [8](#page-8-0)a), while the accompanying metadata framework (Fig. [8b](#page-8-0)) defines a minimal set of descriptors required for reproducible and comparable modeling. These include intrinsic membrane properties (e.g., porosity, pore size), feed characteristics (e.g., oil concentration, type), and operational variables (e.g., crossflow velocity, pressure), which together provide the basis for transferable predictions of fouling behavior.

Although demonstrated here for oil–water membrane filtration, the proposed framework may be applicable to other transport-limited systems exhibiting time-dependent growth in resistance, provided that sufficiently detailed and consistent datasets are available. Its broader applicability is therefore expected to depend on the availability and quality of experimental metadata across studies. From an engineering perspective, these results provide practical insight into the limitations of predictive fouling models across studies. They show that model performance is strongly constrained by the availability and consistency of experimental descriptors, rather than by model formulation alone. This has direct implications for experimental design, data reporting, and the reliability of model-based analysis in membrane processes. These results indicate that reliable fouling prediction for process optimization is fundamentally limited by the availability of metadata, implying that improvements in data reporting may yield greater gains than increasing model complexity.

#### **Methods**

The conceptual framework integrates physical modeling, reduced-order abstraction, and machine learning, as illustrated in Fig. [9](#page-11-0):

Figure [9](#page-11-0) illustrates the overall conceptual workflow of the proposed framework. This schematic is intended to provide a high-level overview rather than a detailed mathematical formulation. The process is organized into three main stages. In the first stage (physical modelling), the system is defined through operating conditions, including feed streams, crossflow, and boundary conditions. In the second stage (reduced-order model abstraction), the governing transport processes (advection, diffusion, and Darcy-based flow) are used to construct a simplified representation of the system, from which key descriptors of flux decline are extracted and reduced using techniques such as principal component analysis (PCA). In the final stage (machine learning integration), these descriptors, together with experimental metadata, are used to train models for prediction and classification tasks. The workflow enables reconstruction of flux trajectories and prediction of fouling behaviour under unseen conditions. The schematic elements in the lower part of the figure illustrate the transformation from the physical system representation to reduced descriptors and finally to predicted flux curves.

<span id="page-11-0"></span>![](_page_11_Figure_9.jpeg)

**Fig. 9**. Conceptual framework (membrane CAD modelled by SolidEdge <https://solidedge.siemens.com> ).

<span id="page-12-0"></span>

| Membrane<br>geometry |              | Membrane materials |                 | Oil type |               |
|----------------------|--------------|--------------------|-----------------|----------|---------------|
| Label                |              | Label              |                 | Label    |               |
| 1                    | Tubular      | 1                  | Mullite         | 1        | Synthetic oil |
| 2                    | Disk         | 2                  | Alumina         | 2        | Kerosene      |
| 3                    | Hollow Fibre | 3                  | Clay            | 3        | Crude oil     |
|                      |              | 4                  | Zirconium oxide | 4        | Mineral oil   |
|                      |              | 5                  | Kaolin          | 5        | Soybean oil   |
|                      |              | 6                  | Coal            | 6        | Pump oil      |
|                      |              | 7                  | Titanium oxide  | 7        | Chloroform    |
|                      |              | 8                  | Polymeric       | 8        | Hexacane      |
|                      |              | 9                  | Bentonite       | 9        | Hexacadene    |
|                      |              | 10                 | Spinel-based    | 10       | Diesel        |

**Table 1**. Different membrane geometries, materials and oil types applied.

<span id="page-12-1"></span>

| Operation conditions           | Range          |
|--------------------------------|----------------|
| Transmembrane pressure [bar]   | 0.1–5.35       |
| Crossflow velocity [m/s]       | 0–2.5          |
| Temperature[°C]                | 25–60          |
| Salt concentration [ppm]       | 0–150          |
| Area [m²]                      | 0.00159–0.0275 |
| Porosity [%]                   | 23–75          |
| Nominal pore size [nm]         | 7.92–970       |
| Oil concentration [ppm]        | 100–8630       |
| Droplet size [nm]              | 0.6–6.928      |
| Pure water permeate flux [LMH] | 18- 3157       |

**Table 2**. Different operation conditions and applied ranges.

A database was assembled from peer-reviewed studies on oil–water separation by membranes [43](#page-17-33)[–53](#page-18-0), published from 1998 to 2025. The compiled dataset consists of 112 standardized flux–time curves gathered from ten separate published studies on oil–water membrane filtration. Inorganic (ceramic) microfiltration and ultrafiltration membranes make up most of the data, which aligns with their common application in producedwater treatment and their frequent use in longer-term, high-pressure experiments documented in the literature. Polymeric membranes are underrepresented, mainly because of scarce high-resolution flux-time data and insufficiently detailed operational and material information needed for cross-study comparisons. Consequently, the current framework is assessed chiefly within the scope of inorganic membrane systems, and the influence of material type is directly addressed during the discussion. The size and composition of the dataset reflect the current state of the literature, where consistent time-resolved flux data with complete metadata remain limited.

For each experiment, operating conditions (transmembrane pressure, crossflow velocity, temperature, salt concentration), feed descriptors (oil type/chemistry, oil concentration, droplet size), and membrane properties (material, geometry, porosity, nominal pore size), together with performance metrics (permeate flux, oil rejection), were extracted and incorporated in meta-variables set. All records were de-duplicated, units were harmonized (e.g., pressure in bar, flux in LMH), categorical fields were standardized (controlled vocabularies for oil type and membrane material), and water flux values ( *Jw*) were collected to enable water-normalized analysis

(given by the flux ratio *<sup>J</sup>* / *<sup>J</sup><sup>w</sup>* ). To ensure data integrity, any missing or unclear data points were flagged and removed from the database. The final dataset is suitable for both standard statistical modelling and time-series analysis. The different membrane materials and geometries, as well as oil types, are summarized in Table [1](#page-12-0).

Table [2](#page-12-1) summarizes the experimental condition ranges reported across the analyzed literature:

Flux data were collected over time for each literature experiment, generating a total of 112 datasets. The machine learning model was experimentally validated in the laboratory under two distinct operating conditions for the tubular membrane described in Table [3.](#page-13-0) These runs were entirely excluded from model training to serve as independent external validations, verifying that the framework generalizes beyond literature data.

#### **Reduced-order finite element method (ROM) in python**

A Python workflow was implemented to analyze fouling dynamics over time across all experiments. The geometries were drawn using SolidWorks according to the described conditions, including channel width/ height, fiber radius, length, and other geometry details [43–](#page-17-33)[53.](#page-18-0) To prevent over-parameterization, principal component analysis (PCA) was applied to the geometric descriptors. This process identified and retained a

<span id="page-13-0"></span>

| Operation conditions           | Experiment 1 (Exp 1) | Experiment 2 (Exp 2) |
|--------------------------------|----------------------|----------------------|
| Transmembrane pressure [bar]   | 0.2                  | 0.6                  |
| Crossflow velocity [m/s]       | 0                    | 0                    |
| Temperature[°C]                | 60                   | 60                   |
| Salt concentration [ppm]       | 100                  | 100                  |
| Area [m²]                      | 0.00792              | 0.00867              |
| Porosity [%]                   | 40                   | 40                   |
| Nominal pore size [nm]         | 100                  | 100                  |
| Oil concentration [ppm]        | 114                  | 667                  |
| Droplet size [nm]              | 1.01                 | 2.04                 |
| Pure water permeate flux [LMH] | 905                  | 990                  |

Table 3. Laboratory operating conditions for model validation.

compact set of orthogonal components that captured the variation most relevant to flux. These reduced features were incorporated into our low-dimensional model, improving computational efficiency while preserving the critical information needed for accurate simulation.

The objective of the reduced-order model is to provide a physics-consistent, low-dimensional representation of established membrane transport and fouling concepts that can be used across heterogeneous datasets in literature. In this sense, the formulation is grounded in classical advection—diffusion transport, Darcy-type permeation, resistance-in-series reasoning, and the balance between foulant deposition and hydrodynamic removal, as widely discussed in the membrane fouling literature2,37. The novelty lies not in the governing equations themselves, but in their integration into a reduced-order, transferable representation compatible with heterogeneous datasets from the literature.

Detailed interfacial phenomena, such as oil—membrane affinity, interfacial tension, and surfactant-mediated interactions, are not explicitly resolved in the ROM, as the corresponding parameters (e.g., contact angle, droplet size distributions, surface energies) are reported sparsely and inconsistently across the literature.

Instead, their aggregate influence is implicitly reflected through the observed flux-time trajectories and associated operating metadata. In this sense, the ROM provides a physics-informed but deliberately reduced representation that constrains the learning problem while enabling transferable analysis across heterogeneous experimental datasets. Parameter bounds were constrained to physically admissible ranges to avoid non-identifiable solutions and overfitting of empirical functional forms.

Several assumptions were carried. First, it is assumed that the emulsion is a diluted water-oil emulsion with high oil rejection typical of MF/UF produced-water filtration. It is also assumed that bulk transport is governed by advection-diffusion, while permeate flow through the membrane wall is described by Darcy's Law 54,55. Fouling was represented through a time-dependent resistance term,  $R_f(t)$ , that accounts in reduced form for the combined effects of pore blocking and surface deposition, together with shear-mediated removal under crossflow conditions. Considering x to be streamwise and y wall-normal (membrane at y=0 and bulk at y=h). For an oil concentration field C(x,y,t), the concentration is given by:

$$\frac{\partial C}{\partial t} + u(y)\frac{\partial C}{\partial x} = \frac{\partial^2 C}{\partial y^2} \tag{1}$$

where u is the velocity, and C is the concentration. Axial diffusion is neglected under the assumption of a high Péclet number:

$$Pe_x = U_{mean} \frac{L}{D} \gg 1 \tag{2}$$

where L is the membrane length and D is the diameter, so streamwise transport is dominated by advection. Consequently, under laminar crossflow, it is possible to model the flow using a simplified laminar Poiseuille profile:

$$u(y) = 6U_{mean} \frac{y}{h} \left( 1 - \frac{y}{h} \right), \ \tau_w = \mu \left. \frac{\partial u}{\partial y} \right|_{y=0} = \frac{6\mu U_{mean}}{h}$$
 (3)

<span id="page-13-1"></span>in which  $U_{mean}$  is the measured/controlled crossflow, and  $\mu$  is the viscosity.  $\tau_w$  is the corresponding wall shear stress, which is directly related to the foulant deposition/removal kinetics. The volumetric permeate flux  $J_v(t)$  follows Darcy 54–56:

$$J_{v}\left(t\right) = \frac{\Delta P}{\mu \left[R_{m} + R_{f}\left(t\right)\right]} \tag{4}$$

with the  $R_m$  being the clean membrane hydraulic resistance and  $R_f(t)$  being the time-dependent fouling resistance. This representation is consistent with standard resistance-based descriptions of membrane flux decline.

<span id="page-14-0"></span>

| Model             | Expression                 | Coding parameter         | Reference                                          |
|-------------------|----------------------------|--------------------------|----------------------------------------------------|
| Power Law Decay   | J∗ = At∗−c                 | P1= A<br>P2= c           | Bowen et al.57                                     |
| Exponential Decay | J∗ = exp (−kt∗)            | P1= R0<br>P2= k          | Bhattacharya et al., Sutzkover-Gutman et al.,58,59 |
| Logistic Model    | 1<br>J∗ =<br>1+a• exp(bt∗) | P1= R0<br>P2= a<br>P3= b | Boerlage et al.60                                  |
| Hybrid model      | J∗ = (1 + t∗)−cexp (bt∗)   | P1= R0<br>P2= b<br>P3= c | Hwang et al.,<br>Abdulsalam et al.3,61             |

**Table 4**. Empirical and reduced-order functional forms used to represent normalized flux or resistance trajectories in fouling studies.

As *R<sup>f</sup>* (*t*) increases, *Jv* decreases, which thickens the concentration boundary layer and further promotes deposition, i.e., a two-way coupling between the transport equation and fouling dynamics. In crossflow operation ( *Umean >* 0), the advection term is active and contributes to shear-induced removal of deposited material. In contrast, under dead-end filtration conditions ( *u* (*y*)=0), the governing transport equation reduces to a onedimensional transient diffusion problem. In the absence of crossflow, the concentration boundary layer grows rapidly, leading to accelerated fouling[1](#page-17-0)[,56.](#page-18-3)

In oil–water filtration, *R<sup>f</sup>* (*t*) is modelled as the superposition of two dominant contributions: (i) porescale blocking/adsorption driven by droplet–pore interactions and near-surface constrictions, and (ii) surface deposition (cake/aggregate layer) arising from droplet deposition, coalescence, and accumulation at the membrane surface.

For interpretability, the fouling contribution was decomposed into two reduced components:

$$R_f(t) = R_{blk}(t) + R_{cake}(t)$$
(5)

representing, in an aggregated sense, pore blocking/adsorption and surface deposition/cake buildup, respectivel[y20.](#page-17-15) The temporal evolution of each fouling contribution is represented through a net balance between deposition/formation and hydrodynamic removal, consistent with the role of crossflow shear in produced-water filtration. This partitioning serves as a reduced-order method for depicting the curve, rather than a breakdown into uniquely defined mechanistic parts. The temporal evolution of these components was expressed through generic deposition–removal balances in which formation scales with effective foulant loading and transport to the membrane, whereas removal increases with wall shear stress. Conceptually, this corresponds to kinetics of the forms:

$$\frac{dR_{blk}}{dt} = \kappa_{blk}\phi \ (oil, \ pores) - \kappa_{rem,blk}\psi \ (\tau_w)$$
 (6)

$$\frac{dR_{cake}}{dt} = \kappa_{cake} \Gamma \left( oil \ transport \right) - \kappa_{rem,cake} \psi \left( \tau_{w} \right) \tag{7}$$

where *τ <sup>w</sup>*denotes wall shear stress and Φ *,* Γ *,* Ψ are intentionally reduced functions parameterized through model calibration. While the present framework does not explicitly resolve interfacial parameters such as contact angle or interfacial tension (often unavailable across studies), the model structure ensures that the resistance growth arises from deposition and blocking, and increased crossflow strengthens shear removal, thereby moderating fouling. In this way, the reduced-order formulation constrains the learning problem to mechanisms consistent with crossflow filtration theory, while remaining transferable across heterogeneous experimental datasets.

This two-dimensional formulation was adopted to reduce computational complexity while retaining the dominant mechanisms of streamwise transport, wall-normal diffusion, permeation resistance, and wall shear effects. This reduced description enables a common physical framework for analyzing heterogeneous literature datasets and linking them to the subsequent machine-learning stage. Table [4](#page-14-0) summarizes the functional forms used as reduced-order descriptors for normalized resistance and flux trajectories, enabling cross-study comparison. These are not intended to replace or supersede classical mechanistic fouling models.

where *J<sup>∗</sup>* (*t*) = *J* (*t*) */J*0and *t <sup>∗</sup>* = *t/t*ref, with *t*ref being the characteristic fouling timescale, i.e., the total filtration time specific for each dataset.

The power-law models a single dominant fouling mechanism over a given time window. Resistance (or normalized flux) evolves as a scale factor times, where *A* sets the amplitude and *n >* 0 is a dimensionless decay exponent; larger *n* means faster early deterioration with a slow late-time tail. The exponential form assumes a single characteristic time scale. Starting from an initial level *R*0, the trajectory relaxes as exp (*−kt*) , with *k >* 0 a constant rate, which captures systems that approach a new steady state without a heavy late-tail memory. The logistic model, however, describes processes with two regimes—an initial induction/conditioning period followed by rapid fouling and saturation. It uses a growth rate *b* and a shift (or loading) parameter *a* to place the inflection point; the curve transitions smoothly from the initial state toward a plateau as *t* crosses *a*

. Conventionally, for coding purposes, the model parameters are referenced generically as P1, P2, and P3. Their physical interpretations vary with the chosen model, as shown in Table 3.

The hybrid model combines short-time exponential decay with late-time algebraic (power-law) relaxation and optionally enforces a non-zero asymptote. In the normalized-flux version used, the parameter b>0 controls the rapid early drop, c>0 governs the slower tail, and  $R_0\in[0,1]$  sets the lower plateau. This form is especially useful when data show an immediate decline followed by a persistent, slowly decaying regime that a single-timescale model cannot fit.

It is emphasized that the expressions summarized in Table 4 are empirical or reduced-order representations of normalized flux or resistance trajectories, rather than first principles fouling laws. Classical fouling theory describes resistance growth through mechanistic balances involving pore blocking, cake formation, and removal processes, whose analytical solutions depend on filtration mode and operating conditions2,20. In the present framework, normalized representations are adopted to enable cross-study comparison and to constrain the learning task, while preserving monotonic fouling behavior and dimensional consistency.

The parameters for each resistance model were determined through constrained nonlinear least-squares fitting of the model predictions (Eq. (4)) to the experimental flux–time data. A bounded optimization routine (fminsearchbnd) was employed to ensure physically admissible parameter values and to avoid non-identifiable solutions.

The hybrid model was implemented in its standard form as reported in the literature, without modification of its mathematical structure, and used here as a reduced-order representation for fitting normalized flux trajectories across heterogeneous datasets.

The coefficient of determination ( $\mathbb{R}^2$ ) was used to select the best-performing model for each dataset. The average computational time for fitting a single flux curve was approximately 158 s.

#### Machine learning time series regression

The objective of the data-driven component is not to develop a new machine learning methodology, but to evaluate how experimental metadata relates to flux-decline behavior across heterogeneous studies and to quantify the limits of predictive transferability. The literature dataset was separated into two components: (i) a metadata table detailing experimental conditions and membrane characteristics, and (ii) a curve table containing flux-time extracted from the cited studies.

For the metadata prediction analysis, following data integration, each flux curve was pre-processed to ensure consistency and comparability across datasets (Fig. 1). This included enforcing monotonic behavior through a cumulative minimum transformation and normalizing the flux by its initial value to obtain a scale-independent representation62,63. Each permeate flux curve  $J_v(t)$  was resampled to a fixed length L=60 on a normalized time axis [0,1] and transformed into a normalized curve  $J_v(t)/J_v(0)$ . A row-wise cumulative minimum filter was then applied to enforce the physically expected non-increasing trend. From each normalized curve, a set of physically interpretable descriptors was extracted and used as targets for the machine learning models. Terminal level ( $J_{\infty}^{\infty}$ ), including the average of the last 10% of points64:

- 1. Half-time ( $t_{50}$ ), time to reach  $(1 + J_{\infty}^{n})/2$  with linear interpolation;
- 2. Initial slope  $(J'_0)$ ;
- 3. Early-time throughput based on trapezoidal area on the initial 10% (  $\mathrm{AUC}_{0-10}$ );
- 4. Early-time throughput based on trapezoidal area on the initial 30% (AUC $_{0-30}$ ).

For visualization, compact curve summaries and predictive features, the standardized curve matrix was compressed via PCA. The PCA basis retained more than 99% of the variance, providing compact latent codes for each curve suitable for efficient subsequent modeling. Metadata included transmembrane pressure, pore size, porosity, crossflow, droplet and solute concentrations, clean-water flux, membrane material, and oil type. For continuous parameters with varying scales (e.g., transmembrane pressure, crossflow velocity, porosity), the data were discretized into three quantile bins, thereby transforming the task into a multi-class classification problem to improve model stability. Model selection and performance are evaluated using a *GroupKFold* cross-validation strategy65,66, with publication as the grouping variable. All transformers are fitted exclusively on the training folds. Performance is quantified using out-of-fold predictions, specifically *macro-F1* and accuracy. Time-window permutation importance was also computed by permuting one-sixth segments (S1.S6) of the normalized curve to pinpoint when in time the most informative data reside, measuring the drop in *macro-F1* as a metric of importance67,68. The permutation procedure was repeated across multiple random shuffling realizations to ensure that the observed importance patterns were consistent and not driven by a single permutation instance.

The supervised model maps from experimental metadata to fouling curves using three regressors: RidgeCV69, Kernel Ridge (RBF)70, and Random Forest71. To stabilize targets, a Yeo–Johnson transform was fitted on the training fold and inverted at prediction, and the outputs were clipped to physical ranges72,73. The predicted descriptors were converted back into full flux curves using a hybrid function that combines a smooth early-time exponential decay with a late-time logistic relaxation. For the model evaluation, due to the publication-level hold-out evaluation, the classical R² metric becomes unstable under distribution shift and can be negative even with moderate absolute errors. The segment-wise mean absolute error (MAE) is consequently reported as the primary metric, and cross-validation is included for completeness. To prevent leakage across publications, GroupKFold was applied with publication as the grouping variable, fitting all preprocessing transformers (standardization, PCA) and the regressor only on the training folds74. To assess early and late segments, time-weighted losses were also evaluated, along with tail-only metrics (the last 40% of time). An optional ensemble of the three regressors is tuned to the chosen metric (early- or late-weighted) and used to evaluate if it improves

robustness. Additionally, to understand the global feature importance for the curve prediction from metadata, a Shap global SHAP (SHapley Additive exPlanations) analysis was carried ou[t75,](#page-18-22)[76](#page-18-23).

To predict discrete metadata directly from the time series while avoiding leakage, two complementary feature sets are extracted from the normalized curves. Convolution-based features (MiniRocket)[29](#page-17-23) were extracted to capture temporal patterns in the flux trajectories. These features were then simplified and compressed to maintain efficiency using *TruncatedSVD*[77](#page-18-24)[,78](#page-18-25) before standardization. The second set included shape statistics, including measurements of the curve's profile, such as the total area under the curve (AUC), the steepness (slope) across early, mid, and late sections, and measures of global variability. A logistic-regression classifier was trained and evaluated with GroupKFold by publication, and performance was reported as macro-F1 and accuracy on outof-fold predictions. To localize informative time regions, time-window permutation importance was applied, shuffling one-sixth segments (S1…S6 ) and measuring the drop in macro-F1.

In addition to scalar descriptors, image-based representations of the normalized curves (Gramian Angular Fields and Markov Transition Fields) were explored to capture temporal patterns[33](#page-17-26). These features were used as auxiliary inputs and slightly improved prediction accuracy without altering the main conclusions. Specifically, Gramian Angular Fields were applied to capture late-range shape and phase dependencies, and Markov Transition Fields (MTF) to model short-range transition dynamics. Before encoding, the curves were z-normalized, in which fitting was restricted to the training fold. Each curve was then mapped to a fixed-size 64×64 image. When used as features, these images were compressed using TruncatedSV[D77](#page-18-24) to a small set of components (16–32) before concatenation with the metadata. All encoders and reducers were fitted inside the training fold to avoid leakage. These pyts images served not only to visualize curve structures that are hard to see in 1D but also as auxiliary features that modestly improved robustness by including global shape information that local metrics (like slopes or AUCs) failed to capture.

All models were implemented in Python 3.11 using scikit-learn 1.x. Random seeds were fixed to ensure reproducibility.

#### **Conclusion**

A hybrid workflow combining a reduced-order 2D finite element model (ROM) with a data-driven mapping approach was developed to analyze flux decline during membrane oil–water separation. The ROM showed high agreement with individual experiments, achieving an average R<sup>2</sup> of 0.95. PCA demonstrated that normalized flux trajectories are intrinsically low-dimensional, with more than 99% of the variance retained. This indicates that prediction errors arise primarily from estimating model coefficients from experimental metadata rather than from limitations in the curve representation itself.

Under grouped cross-validation, the model achieved segment-wise MAEs of approximately 0.08 (early) and 0.14 (mid and late). These errors increased significantly under publication hold-out, demonstrating that crossstudy heterogeneity, rather than model expressiveness, is the primary limitation on predictive performance.

Feature importance and temporal analyses provided physically consistent insights: crossflow dominates earlystage behavior, pressure influences both early- and late-stage behavior, porosity and clean-water permeance govern long-term response, and pore size contributes to the mid-time regime. In addition, flux trajectories encoded more information about membrane structure than about oil chemistry, reflecting the limited and heterogeneous reporting of interfacial descriptors across studies.

These results show that predictive performance is primarily constrained by metadata completeness and crossstudy variability rather than by the modeling framework itself. The proposed approach provides a structured way to analyze fouling behavior, combining reduced-order physical constraints with data-driven analysis to improve interpretability and assess transferability across heterogeneous datasets.

Although demonstrated here for membrane fouling, the framework may be applicable to other transportlimited systems exhibiting time-dependent growth in resistance, provided that sufficiently detailed and consistent datasets are available. Its broader applicability, therefore, depends on the availability and quality of experimental metadata across studies.

More broadly, this work demonstrates how combining reduced-order physical constraints with data-driven analysis can improve the interpretability and transferability of fouling models across heterogeneous studies. The results emphasize that consistent, sufficiently detailed metadata are essential for reliable predictive modeling, shifting the focus of fouling prediction from model development toward data standardization as the primary enabler of transferable, engineering-relevant predictions.

#### **Data availability**

All curated datasets generated or analysed during this study are available in the authors' public GitHub repository ([https://github.com/CarineLourencoAlves/Physics-informed-machine-learning-for-cross-study-predictio](https://github.com/CarineLourencoAlves/Physics-informed-machine-learning-for-cross-study-prediction-of-oil-water-membrane-fouling) [n-of-oil-water-membrane-fouling](https://github.com/CarineLourencoAlves/Physics-informed-machine-learning-for-cross-study-prediction-of-oil-water-membrane-fouling)). A version of the dataset will additionally be registered and preserved in the SINOVA research data platform at UFSC.

#### **Code availability**

Complete Python scripts implementing the reduced-order model and machine-learning pipeline are provided under an open-source license in the authors' GitHub repository. A curated version of the codebase will also be deposited in SINOVA (UFSC).

Received: 17 February 2026; Accepted: 18 May 2026

### **References**

- <span id="page-17-0"></span>1. Li, Z., Jin, R., Gong, J., Liu, W. & Li, J. Recent advances in anti-fouling oil–water separation membranes: a review focusing on active and passive anti-fouling strategies. *J. Mater. Chem. Mater.* **13**, 23418–23438 (2025).
- <span id="page-17-1"></span>2. Field, R. W., Wu, D., Howell, J. A. & Gupta, B. B. Critical flux concept for microfiltration fouling. *J. Memb. Sci.* **100**, 259–272 (1995).
- <span id="page-17-18"></span>3. Abdulsalam, A. et al. A review of fouling prediction techniques in membrane desalination: From empirical to intelligent models. *Desalination* **616**, 119363 (2025).
- <span id="page-17-2"></span>4. Doaa Salim Musallam Samhan Al-Kathiri. Membrane Fouling Prediction and Control Using AI and Machine Learning: A Comprehensive Review. *J. Environ. Earth Sci.* **7**, 315–350 (2025).
- <span id="page-17-3"></span>5. Choi, M. et al. Highly durable and sustainable heterogeneous fabric using in-and-out fluorinated urethane coating for elimination of bacteria and oil–water separation. *NPJ Clean. Water*. **5**, 48 (2022).
- <span id="page-17-4"></span>6. You, X. et al. Multifunctional porous nanofibrous membranes with superior antifouling properties for oil-water separation and photocatalytic degradation. *J. Memb. Sci.* **668**, 121245 (2023).
- <span id="page-17-5"></span>7. United Nations, D. & Affairs, S. of E. and Transforming our world: The 2030 Agenda for Sustainable Development. (2015). [https:/](https://sdgs.un.org/goals/goal6) [/sdgs.un.org/goals/goal6](https://sdgs.un.org/goals/goal6)
- <span id="page-17-6"></span>8. Xiang, Q. et al. A universal strategy for efficient separation from single emulsion separation to oil-in-water and water-in-oil mixed emulsions. *Sep. Purif. Technol.* **354**, 129517 (2025).
- <span id="page-17-7"></span>9. Sutrisna, P. D., Khoiruddin, K., Mustika, P. C. W. B., Ismadji, S. & Wenten I. G. Advancements in ceramic membranes for robust oil-water separation. *J. Environ. Chem. Eng.* **12**, 113658 (2024).
- 10. Li, B., Qi, B., Guo, Z., Wang, D. & Jiao, T. Recent developments in the application of membrane separation technology and its challenges in oil-water separation: A review. *Chemosphere* **327**, 138528 (2023).
- <span id="page-17-8"></span>11. Sholl, D. S. & Lively, R. P. Seven chemical separations to change the world. *Nature* **532**, 435–437 (2016).
- <span id="page-17-9"></span>12. Huang, J. et al. Sustainable nanofiltration membranes enable ultrafast water purification. *Nat. Water*. **3**, 1048–1056 (2025).
- <span id="page-17-10"></span>13. Cunha, A. L. et al. MEMBRANE MODULE: A NUMERICAL INVESTIGATION. *Brazilian J. Petroleum Gas*. **10**, 205–219 (2016). WATER-OIL SEPARATION PROCESS USING A CONCENTRIC TUBULAR CERAMIC.
- <span id="page-17-11"></span>14. Weschenfelder, S. E., Fonseca, M. J. C., Borges, C. P. & Campos, J. C. Application of ceramic membranes for water management in offshore oil production platforms: Process design and economics. *Sep. Purif. Technol.* **171**, 214–220 (2016).
- 15. Omar, N. M. A. et al. Overcoming challenges in water purification by nanocomposite ceramic membranes: A review of limitations and technical solutions. *J. Water Process. Eng.* **57**, 104613 (2024).
- <span id="page-17-19"></span>16. Zhang, H., Duan, Y., Elimelech, M. & Wang, Y. Scalable catalytic nanofiltration membranes for advanced water treatment. *Nat. Water*. **3**, 1038–1047 (2025).
- <span id="page-17-12"></span>17. Baig, N., Abdulazeez, I. & Aljundi, I. H. Low-pressure-driven special wettable graphene oxide-based membrane for efficient separation of water-in-oil emulsions. *NPJ Clean. Water*. **6**, 40 (2023).
- <span id="page-17-13"></span>18. Ahmed, M. A., Amin, S. & Mohamed, A. A. Fouling in reverse osmosis membranes: monitoring, characterization, mitigation strategies and future directions. *Heliyon* **9**, e14908 (2023).
- <span id="page-17-14"></span>19. Pandey, S. R., Jegatheesan, V., Baskaran, K. & Shu, L. Fouling in reverse osmosis (RO) membrane in water recovery from secondary effluent: a review. *Rev. Environ. Sci. Biotechnol.* **11**, 125–145 (2012).
- <span id="page-17-15"></span>20. Belfort, G., Davis, R. H. & Zydney, A. L. The behavior of suspensions and macromolecular solutions in crossflow microfiltration. *J.*
- <span id="page-17-16"></span>*Memb. Sci.* **96**, 1–58 (1994). 21. Yang, H. et al. A Concise Review of Theoretical Models and Numerical Simulations of Membrane Fouling. *Water (Basel)*. **14**, 3537 (2022).
- 22. CHEN, J., ELIMELECH, M. & KIM, A. Monte Carlo simulation of colloidal membrane filtration: Model development with application to characterization of colloid phase transition. *J. Memb. Sci.* **255**, 291–305 (2005).
- 23. Keir, G. & Jegatheesan, V. A review of computational fluid dynamics applications in pressure-driven membrane filtration. *Rev. Environ. Sci. Biotechnol.* **13**, 183–201 (2014).
- 24. Liu, Y. et al. Millionfold accelerated AI solver for 3D multi-physical simulations of ultrapermeable membranes. *NPJ Clean. Water*. **8**, 59 (2025).
- <span id="page-17-17"></span>25. Wang, Y. Q. et al. Knowledge embedding and interpretable machine learning optimize comprehensive benefits for water treatment. *NPJ Clean. Water*. **8**, 81 (2025).
- <span id="page-17-20"></span>26. Ignacz, G. et al. Machine learning for the advancement of membrane science and technology: A critical review. *J. Memb. Sci.* **713**, 123256 (2025).
- <span id="page-17-21"></span>27. Gauthier, T. Detecting Trends Using Spearman's Rank Correlation Coefficient. *Environ. Forensics*. **2**, 359–362 (2001).
- <span id="page-17-22"></span>28. Liu, Q., Li, C., Wanga, V. & Shepherd, B. E. Covariate-adjusted Spearman's Rank Correlation with Probability-scale Residuals. *Biometrics* **74**, 595–605 (2018).
- <span id="page-17-23"></span>29. Dempster, A., Schmidt, D. F., Webb, G. I. & MiniRocket: A Very Fast (Almost) Deterministic Transform for Time Series Classification. in *Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining* 248–257Association for Computing Machinery, (2021).<https://doi.org/10.1145/3447548.3467231>
- <span id="page-17-24"></span>30. Ghojogh, B., Crowley, M., Karray, F. & Ghodsi, A. Principal Component Analysis. in *Elements of Dimensionality Reduction and Manifold Learning* 123–154Springer International Publishing, Cham, (2023). [https://doi.org/10.1007/978-3-031-10602-6\\_5](https://doi.org/10.1007/978-3-031-10602-6_5)
- 31. Greenacre, M. et al. Principal component analysis. *Nat. Reviews Methods Primers*. **2**, 100 (2022).
- <span id="page-17-25"></span>32. Jolliffe, I. T. & Cadima, J. Principal component analysis: a review and recent developments. *Philosophical Trans. Royal Soc. A: Math. Phys. Eng. Sci.* **374**, 20150202 (2016).
- <span id="page-17-26"></span>33. Faouzi, J. Pyts: A Python Package for Time Series Classification. *Journal Mach. Learn. Research* **21** (2020). [https://github.com/joh](https://github.com/johannfaouzi/pyts) [annfaouzi/pyts](https://github.com/johannfaouzi/pyts)
- <span id="page-17-27"></span>34. Hermia, J. Blocking Filtration. Application to Non-Newtonian Fluids. in Mathematical Models and Design Methods in Solid-Liquid Separation 83–89 (Springer Netherlands, Dordrecht, doi:[https://doi.org/10.1007/978-94-009-5091-7\\_5](https://doi.org/10.1007/978-94-009-5091-7_5). (1985).
- 35. Pereira, G. L. D., Cardozo-Filho, L., Jegatheesan, V. & Guirardello, R. Generalization and Expansion of the Hermia Model for a Better Understanding of Membrane Fouling. *Membr. (Basel)*. **13**, 290 (2023).
- <span id="page-17-28"></span>36. Kirschner, A. Y., Cheng, Y. H., Paul, D. R., Field, R. W. & Freeman, B. D. Fouling mechanisms in constant flux crossflow ultrafiltration. *J. Memb. Sci.* **574**, 65–75 (2019).
- <span id="page-17-29"></span>37. Gu, W. et al. Treating PFOA emulsified oil in membrane distillation: Relationship between membrane fouling and surface properties. *Journal Water Process. Engineering* **77**, (2025).
- <span id="page-17-30"></span>38. Salahi, A., Abbasi, M. & Mohammadi, T. Permeate flux decline during UF of oily wastewater: Experimental and modeling. *Desalination* **251**, 153–160 (2010).
- <span id="page-17-31"></span>39. Hu, B. & Scott, K. Microfiltration of water in oil emulsions and evaluation of fouling mechanism. *Chem. Eng. J.* **136**, 210–220 (2008).
- 40. Virga, E., Field, R. W., Biesheuvel, P. M. & de Vos, W. M. Theory of oil fouling for microfiltration and ultrafiltration membranes in produced water treatment. *J. Colloid Interface Sci.* **621**, 431–439 (2022).
- 41. Chakrabarty, B., Ghoshal, A. K. & Purkait, M. K. Ultrafiltration of oil-in-water emulsion: Analysis of fouling mechanism. *Membrane Water Treat.* **1**, 297–316 (2010).
- <span id="page-17-32"></span>42. Roehl, E. A. et al. Modeling fouling in a large RO system with artificial neural networks. *J. Memb. Sci.* **552**, 95–106 (2018).
- <span id="page-17-33"></span>43. Cairone, S. et al. Integrating artificial intelligence modeling and membrane technologies for advanced wastewater treatment: Research progress and future perspectives. *Sci. Total Environ.* **944**, 173999 (2024).

- 44. Shahouni, R., Abbasi, M., Dibaj, M. & Akrami, M. Utilising Artificial Intelligence to Predict Membrane Behaviour in Water Purification and Desalination. *Water (Basel)*. **16**, 2940 (2024).
- 45. Abbasi, M., Mirfendereski, M., Nikbakht, M., Golshenas, M. & Mohammadi, T. Performance study of mullite and mullite–alumina ceramic MF membranes for oily wastewaters treatment. *Desalination* **259**, 169–178 (2010).
- 46. Chen, M., Rietveld, L. C. & Heijman, S. G. J. Evaluation of membrane fouling at constant flux and constant transmembrane pressure conditions: Implications for membrane modification. *J Environ. Chem. Eng* **13**, (2025).
- 47. Eom, J. H., Kim, Y. W., Yun, S. H. & Song, I. H. Low-cost clay-based membranes for oily wastewater treatment. *J. Ceram. Soc. Jpn.* **122**, 788–794 (2014).
- 48. Gao, N., Fan, Y., Quan, X., Cai, Y. & Zhou, D. Modified ceramic membranes for low fouling separation of water-in-oil emulsions. *J. Mater. Sci.* **51**, 6379–6388 (2016).
- 49. Nandi, B. K., Moparthi, A., Uppaluri, R. & Purkait, M. K. Treatment of oily wastewater using low cost ceramic membrane: Comparative assessment of pore blocking and artificial neural network models. *Chem. Eng. Res. Des.* **88**, 881–892 (2010).
- 50. Song, C., Wang, T., Pan, Y. & Qiu, J. Preparation of coal-based microfiltration carbon membrane and application in oily wastewater treatment. *Sep. Purif. Technol.* **51**, 80–84 (2006).
- 51. Suresh, K. & Pugazhenthi, G. Cross flow microfiltration of oil-water emulsions using clay based ceramic membrane support and TiO2 composite membrane. *Egypt. J. Petroleum*. **26**, 679–694 (2017).
- 52. Vasanth, D., Pugazhenthi, G. & Uppaluri, R. Cross-flow microfiltration of oil-in-water emulsions using low cost ceramic membranes. *Desalination* **320**, 86–95 (2013).
- <span id="page-18-0"></span>53. Yang, C., Zhang, G., Xu, N. & Shi, J. Preparation and application in oil–water separation of ZrO2/α-Al2O3 MF membrane. *J. Memb. Sci.* **142**, 235–243 (1998).
- <span id="page-18-1"></span>54. Zheng, W. et al. Ultra-Antifouling Liquid-Like Surfaces for Sustainable Viscous Water-in-Oil Emulsions Separation and Oil Recovery. *Advanced Materials* **37**, (2025).
- <span id="page-18-2"></span>55. Kwon, H. W. et al. Effective oil-in-water emulsion separation by self-cleaning superoleophobic hydrogel membrane composite with hierarchical structure. *NPJ Clean. Water* **8**, (2025).
- <span id="page-18-3"></span>56. Field, R. W. & Wu, J. J. Modelling of permeability loss in membrane filtration: Re-examination of fundamental fouling equations and their link to critical flux. *Desalination* **283**, 68–74 (2011).
- <span id="page-18-4"></span>57. Motin, A., Tarabara, V. V. & Bénard, A. Numerical investigation of the performance and hydrodynamics of a rotating tubular membrane used for liquid–liquid separation. *J. Memb. Sci.* **473**, 245–255 (2015).
- <span id="page-18-5"></span>58. BOLTON, G., LACASSE, D. & KURIYEL, R. Combined models of membrane fouling: Development and application to microfiltration and ultrafiltration of biological fluids. *J. Memb. Sci.* **277**, 75–84 (2006).
- <span id="page-18-6"></span>59. Mousa, H. M., Fahmy, H. S., Ali, G. A. M., Abdelhamid, H. N. & Ateia, M. Membranes for Oil/Water Separation: A Review. *Adv Mater. Interfaces* **9**, (2022).
- <span id="page-18-7"></span>60. Bowen, W. R. & Welfoot, J. S. Modelling the performance of membrane nanofiltration—critical assessment and model development. *Chem. Eng. Sci.* **57**, 1121–1137 (2002).
- <span id="page-18-8"></span>61. Bhattacharya, P., Dutta, S., Ghosh, S., Vedajnananda, S. & Bandyopadhyay, S. Crossflow microfiltration using ceramic membrane for treatment of sulphur black effluent from garment processing industry. *Desalination* **261**, 67–72 (2010).
- <span id="page-18-9"></span>62. Sutzkover-Gutman, I., Hasson, D. & Semiat, R. Humic substances fouling in ultrafiltration processes. *Desalination* **261**, 218–231 (2010).
- <span id="page-18-10"></span>63. Boerlage, S. F. E., Kennedy, M. D., Dickson, M. R., El-Hodali, D. E. Y. & Schippers, J. C. The modified fouling index using ultrafiltration membranes (MFI-UF): characterisation, filtration mechanisms and proposed reference membrane. *J. Memb. Sci.* **197**, 1–21 (2002).
- <span id="page-18-11"></span>64. Hwang, T. M. et al. Development of a statistical and mathematical hybrid model to predict membrane fouling and performance. *Desalination* **247**, 210–221 (2009).
- <span id="page-18-12"></span>65. de Leeuw, J., Hornik, K. & Mair, P. Isotone Optimization in *R*: Pool-Adjacent-Violators Algorithm (PAVA) and Active Set Methods. *J Stat. Softw* **32**, (2009).
- <span id="page-18-13"></span>66. Busing, F. M. T. A. & Monotone Regression A Simple and Fast O(n) PAVA Implementation. *J Stat. Softw* **102**, (2022).
- <span id="page-18-14"></span>67. Radišić-Aberger, O., Burggräf, P., Steinberg, F., Becher, A. & Weißer, T. Evaluating early predictive performance of machine learning approaches for engineering change schedule – A case study using predictive process monitoring techniques. *Supply Chain Analytics*. **8**, 100087 (2024).
- <span id="page-18-15"></span>68. Roberts, D. R. et al. Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure. *Ecography* **40**, 913–929 (2017).
- <span id="page-18-16"></span>69. Varma, S. & Simon, R. Bias in error estimation when using cross-validation for model selection. *BMC Bioinform.* **7**, 91 (2006).
- <span id="page-18-17"></span>70. Khan, A., Ali, A., Khan, J., Ullah, F. & Faheem, M. Using Permutation-Based Feature Importance for Improved Machine Learning Model Performance at Reduced Costs. *IEEE Access.* **13**, 36421–36435 (2025).
- <span id="page-18-18"></span>71. Molnar, C., König, G., Bischl, B. & Casalicchio, G. Model-agnostic feature importance and effects with dependent features: a conditional subgroup approach. *Data Min. Knowl. Discov*. **38**, 2903–2941 (2024).
- <span id="page-18-19"></span>72. Rajan, M. P. An Efficient Ridge Regression Algorithm with Parameter Estimation for Data Analysis in Machine Learning. *SN Comput. Sci.* **3**, 171 (2022).
- <span id="page-18-20"></span>73. Kuo, B. C., Ho, H. H., Li, C. H., Hung, C. C. & Taur, J. S. A Kernel-Based Feature Selection Method for SVM With RBF Kernel for Hyperspectral Image Classification. *IEEE J. Sel. Top. Appl. Earth Obs Remote Sens.* **7**, 317–326 (2014).
- <span id="page-18-21"></span>74. Breiman, L. Random Forests. *Mach. Learn.* **45**, 5–32 (2001).
- <span id="page-18-22"></span>75. Sameera Abdulsalam Othman & Haithem Taha Mohammed Ali. On the Use of Yeo-Johnson Transformation in the Functional Multivariate Time Series. *Stat. Optim. Inform. Comput.* **13**, 2634–2646 (2025).
- <span id="page-18-23"></span>76. Liu, B. H., Zhang, L. W., Wei, Y. Q. & Chen, C. Dual Power Transformation and Yeo–Johnson Techniques for Static and Dynamic Reliability Assessments. *Buildings* **14**, 3625 (2024).
- <span id="page-18-24"></span>77. Alves, C. L., Kuhnert, K., Rodrigues, F. A. & Moeckel, M. Harnessing multi-output machine learning approach and dynamical observables from network structure to optimize COVID-19 intervention strategies. *Biol Methods Protoc* **10**, (2025).
- <span id="page-18-25"></span>78. Li, Q., Ji, Y., Zhu, M., Zhu, X. & Sun, L. Unsupervised feature selection using chronological fitting with Shapley Additive explanation (SHAP) for industrial time-series anomaly detection. *Appl. Soft Comput.* **155**, 111426 (2024).
- 79. Sallum, L. F. et al. Revealing patterns in major depressive disorder with machine learning and networks. Preprint at (2024). [https:](https://doi.org/10.1101/2024.06.07.24308619) [//doi.org/10.1101/2024.06.07.24308619](https://doi.org/10.1101/2024.06.07.24308619)
- 80. Deng, H. et al. Fast Updating Truncated SVD for Representation Learning with Sparse Matrices. (2024). [http://arxiv.org/abs/2401](http://arxiv.org/abs/2401.09703) [.09703](http://arxiv.org/abs/2401.09703)
- 81. Saibaba, A. K., Kilmer, M., Miller, E. & Fantini, S. Fast algorithms for hyperspectral Diffuse Optical Tomography. (2014). [http://ar](http://arxiv.org/abs/1410.0986) [xiv.org/abs/1410.0986](http://arxiv.org/abs/1410.0986)

#### **Acknowledgements**

The authors would like to thank the financial support from Petróleo Brasileiro S/A (PETROBRAS) – Project EO&M, Process: 2023/00226-0, and the Brazilian National Council for Scientific and Technological Development – CNPq (process no. 315722/2025-8). CAPES. The authors would also like to thank Dr. Caroline Lourenco Alves for the methodology assistance and for the inputs given during the development of the research.

### **Author contributions**

C.L.A. and S.Y.G.G. developed the scientific methodology, performed model validation, and wrote the original draft of the manuscript. M.P. and M.P.C. conducted the experimental work under the supervision of R.F.P.M.M. A.A., M.L., and S.E.W. provided overall supervision and contributed to validation of the results. All authors reviewed, edited, and approved the final manuscript.

#### **Funding**

The authors would like to thank the financial support from Petróleo Brasileiro S/A (PETROBRAS) – Project EO&M, Process: 2023/00226-0, and the Brazilian National Council for Scientific and Technological Development – CNPq (process no. 315722/2025-8).

#### **Declarations**

#### **Competing interests**

The authors declare no competing interests.

#### **Additional information**

**Correspondence** and requests for materials should be addressed to C.L.A.

**Reprints and permissions information** is available at [www.nature.com/reprints.](www.nature.com/reprints)

**Publisher's note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

**Open Access** This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit [http://creativecommo](http://creativecommons.org/licenses/by-nc-nd/4.0/) [ns.org/licenses/by-nc-nd/4.0/.](http://creativecommons.org/licenses/by-nc-nd/4.0/)

© The Author(s) 2026
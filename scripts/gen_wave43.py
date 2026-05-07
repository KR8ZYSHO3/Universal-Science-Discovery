"""Generate Wave 43 bridge, unknown, and hypothesis YAML files (schema-correct)."""
import os

ROOT = r"C:\Users\Shoe\dev\Universal-Science-Discovery"

def mkdirs(*parts):
    p = os.path.join(ROOT, *parts)
    os.makedirs(p, exist_ok=True)
    return p

def write(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

hd = mkdirs("hypotheses", "active")

# ──────────────────────────────────────────────────────────
# Bridge 1: Agricultural intensification ↔ biodiversity-ecosystem function (ecology ↔ agronomy)
# ──────────────────────────────────────────────────────────
d = mkdirs("cross-domain", "ecology-biology")
write(os.path.join(d, "b-agricultural-biodiversity-ecosystem.yaml"), """\
id: b-agricultural-biodiversity-ecosystem
title: "Agricultural intensification reduces local biodiversity and ecosystem service delivery through a quantifiable biodiversity-ecosystem function relationship, informing the land-sparing versus land-sharing trade-off"
fields:
  - ecology
  - biology
  - agronomy
bridge_claim: "Ecosystem service provision (pollination, pest control, nutrient cycling) scales as a saturating function of species richness S with half-saturation at S1/2 ~ 5-10 species, so intensification-driven local extinction reduces services at a rate determined by the slope of the BEF relationship near S_agricultural."
translation_table:
  - field_a_term: "species richness S in agricultural landscape"
    field_b_term: "ecosystem service delivery Y(S) = Y_max * S / (S1/2 + S)"
    note: "Michaelis-Menten BEF relationship: linear at low S, saturating at high S; slope at S_agricultural determines sensitivity to biodiversity loss"
  - field_a_term: "land-sparing strategy (high-yield, wildlife-free farmland)"
    field_b_term: "high Y_max at low biodiversity; biodiversity concentrated in reserves"
    note: "Land-sparing minimizes farmland area at cost of homogenizing agricultural matrix"
  - field_a_term: "land-sharing strategy (wildlife-friendly low-yield farming)"
    field_b_term: "lower Y_max but higher S throughout farmland"
    note: "Land-sharing trades yield for biodiversity; optimal when BEF slope is steep at S_agricultural"
  - field_a_term: "complementarity effect in mixed-species agricultural plots"
    field_b_term: "transgressive overyielding: polyculture yield > best monoculture yield"
    note: "Niche complementarity in intercropping systems mirrors BEF complementarity in natural ecosystems"
status: established
communication_gap: "Agronomists optimize yield and profitability while ecologists study biodiversity; the quantitative BEF framework connecting species loss to ecosystem service reduction is known in ecology but rarely integrated into agricultural policy or farm management decisions."
cross_pollination_opportunities:
  - "Using BEF relationships to set minimum biodiversity thresholds in agricultural sustainability certification schemes"
  - "Designing diversified farming systems (intercropping, hedgerows, cover crops) using BEF principles to optimize yield and ecosystem service co-benefits"
references:
  - doi: "10.1126/science.1178168"
    note: "Phalan et al. (2011) Science - land-sparing vs land-sharing comparison across bird and tree diversity"
  - doi: "10.1126/science.1060391"
    note: "Tilman et al. (2001) Science - diversity and productivity in grassland ecosystem functioning"
  - doi: "10.1038/nature04150"
    note: "Balvanera et al. (2006) - quantifying the evidence for biodiversity effects on ecosystem services"
related_unknowns:
  - u-bef-relationship-agricultural-context
last_reviewed: "2026-05-07"
""")

ud = mkdirs("unknowns-catalog", "ecology")
write(os.path.join(ud, "u-bef-relationship-agricultural-context.yaml"), """\
id: u-bef-relationship-agricultural-context
title: "How does the biodiversity-ecosystem function relationship differ between natural and agricultural ecosystems, and at what minimum biodiversity level do ecosystem services collapse in intensively managed farmland?"
status: open
priority: high
disciplines:
  - ecology
  - agronomy
  - conservation-biology
summary: >
  BEF relationships are well-characterized in grassland biodiversity experiments
  (Jena, Cedar Creek) but agricultural ecosystems differ: they have managed species
  composition, external nutrient inputs that partially compensate for lost diversity,
  and spatial structure (field-hedgerow mosaic). Whether BEF curves measured in
  experimental grasslands apply to real agricultural landscapes is untested.
  Critical threshold biodiversity levels below which specific services (pollination,
  biological pest control) collapse are unknown. The economic valuation of biodiversity
  loss through BEF is needed for policy but not yet established at landscape scale.
systematic_gaps:
  - Large-scale agricultural BEF experiments are rare; most evidence comes from natural grasslands
  - The role of functional diversity vs. species richness in agricultural BEF is contested
  - Landscape context (surrounding habitat) modifies local BEF but is not captured in field-scale models
related_bridges:
  - b-agricultural-biodiversity-ecosystem
last_reviewed: "2026-05-07"
""")

write(os.path.join(hd, "h-land-sparing-bef-optimum-yield-threshold.yaml"), """\
id: h-land-sparing-bef-optimum-yield-threshold
title: "Land-sparing outperforms land-sharing for biodiversity conservation when the BEF relationship has a half-saturation constant S1/2 < 5 species, testable via systematic comparison of agricultural BEF curves across farming systems"
status: active
priority: medium
impact_score: 0.70
created: "2026-05-07"
last_updated: "2026-05-07"
related_disciplines:
  - ecology
  - agronomy
unknowns_addressed:
  - u-bef-relationship-agricultural-context
evidence_links:
  - doi: "10.1126/science.1178168"
    type: supporting
    confidence: 0.72
    note: "Phalan et al. (2011) - land-sparing superior for most species in high-productivity environments"
  - doi: "10.1126/science.1060391"
    type: related
    confidence: 0.68
    note: "Tilman et al. (2001) - BEF saturates quickly; few species needed for most ecosystem function"
proposed_tests:
  - description: >
      Measure BEF relationships for pollination and pest control services in 30 agricultural
      landscapes varying from monoculture to diverse agroforestry across 3 countries.
      Fit Michaelis-Menten curve; estimate S1/2. Prediction: S1/2 < 10 species for
      pollination and pest control, supporting land-sparing under high-productivity conditions.
""")

# ──────────────────────────────────────────────────────────
# Bridge 2: Neutron star equations of state ↔ nuclear matter theory (astrophysics ↔ nuclear physics)
# ──────────────────────────────────────────────────────────
d = mkdirs("cross-domain", "astrophysics-physics")
write(os.path.join(d, "b-neutron-star-nuclear-eos.yaml"), """\
id: b-neutron-star-nuclear-eos
title: "Neutron star mass-radius relationships encode the dense matter equation of state, connecting neutron star astrophysics to nuclear symmetry energy and constraining the pressure-density relationship of matter at 2-8 times nuclear saturation density"
fields:
  - astrophysics
  - nuclear-physics
  - physics
bridge_claim: "The neutron star mass-radius curve M(R) is a one-to-one map from the equation of state P(rho), determined by integrating the Tolman-Oppenheimer-Volkoff (TOV) equations; NICER X-ray timing measurements of M and R constrain P(rho) at 2-5 times nuclear saturation density, providing the highest-density laboratory for nuclear matter inaccessible on Earth."
translation_table:
  - field_a_term: "neutron star radius R at 1.4 solar masses"
    field_b_term: "pressure of beta-equilibrated nuclear matter at rho ~ 2*rho_0"
    note: "R_1.4 ~ 11-13 km from NICER; each km in R corresponds to ~10 MeV/fm^3 difference in pressure at 2*rho_0"
  - field_a_term: "maximum neutron star mass M_max"
    field_b_term: "stiffness of EOS at rho > 4*rho_0"
    note: "M_max ~ 2 M_sun (PSR J0952-0607) requires stiff EOS at high density; rules out pure quark matter or kaon condensate models"
  - field_a_term: "nuclear symmetry energy slope L at saturation density"
    field_b_term: "neutron star crust thickness and pressure-radius correlation"
    note: "L = 3*rho_0 * dS/drho at rho_0; larger L means stiffer symmetry energy and larger radius"
  - field_a_term: "gravitational wave tidal deformability Lambda from NS merger"
    field_b_term: "quadrupole polarizability of nuclear matter"
    note: "LIGO/Virgo GW170817 tidal deformability Lambda_1.4 < 800 constrains EOS at 1-2*rho_0"
status: established
communication_gap: "Nuclear physicists measure symmetry energy in heavy-ion collisions and finite nuclei while astrophysicists measure M-R from pulsars; the TOV mapping connecting nuclear lab measurements to neutron star observables requires translating between nuclear and relativistic frameworks rarely taught in either community."
cross_pollination_opportunities:
  - "Using multi-messenger neutron star observations (X-ray + gravitational wave) to constrain nuclear symmetry energy and validate heavy-ion collision experiments"
  - "Informing relativistic mean-field nuclear models with neutron star EOS constraints to improve predictions of neutron-rich nuclei far from stability"
references:
  - doi: "10.3847/2041-8213/ab0c2f"
    note: "Riley et al. (2019) ApJL - NICER measurement of PSR J0030+0451 mass and radius"
  - doi: "10.3847/2041-8213/aa9035"
    note: "Abbott et al. (2017) ApJL - GW170817 tidal deformability and EOS constraints"
  - doi: "10.1103/PhysRevLett.120.172703"
    note: "Annala et al. (2018) PRL - neutron star mergers and the quark-hadron crossover from EOS constraints"
related_unknowns:
  - u-neutron-star-eos-dense-matter-phase-transition
last_reviewed: "2026-05-07"
""")

ud2 = mkdirs("unknowns-catalog", "astrophysics")
write(os.path.join(ud2, "u-neutron-star-eos-dense-matter-phase-transition.yaml"), """\
id: u-neutron-star-eos-dense-matter-phase-transition
title: "Does the dense matter in neutron star cores undergo a first-order phase transition to quark matter, hyperon matter, or a condensate, and if so at what density?"
status: open
priority: high
disciplines:
  - astrophysics
  - nuclear-physics
  - particle-physics
summary: >
  At densities above 3-4 times nuclear saturation density, nuclear matter may undergo
  a phase transition to exotic forms: quark-gluon plasma, hyperon admixtures, kaon
  or pion condensates. These phases soften the EOS, reducing maximum neutron star mass.
  The observation of 2 M_sun pulsars disfavors pure quark matter cores but does not
  rule out quark-hadron crossovers or small quark cores. Current M-R measurements
  from NICER and GW tidal deformabilities are consistent with several EOS families.
  A definitive detection of a phase transition would require either a very massive
  neutron star (> 2.2 M_sun) or a neutron star merger where transition signatures
  appear in the gravitational waveform.
systematic_gaps:
  - NICER radius measurements have ~1 km uncertainty; distinguishing EOS families requires < 0.5 km precision
  - Phase transition signatures in gravitational waveforms from NS mergers have not been observed
  - Heavy-ion experiments probe nuclear matter up to 3*rho_0 but cannot reach 5-6*rho_0 conditions in neutron stars
related_bridges:
  - b-neutron-star-nuclear-eos
last_reviewed: "2026-05-07"
""")

write(os.path.join(hd, "h-neutron-star-quark-crossover-2-solar-mass.yaml"), """\
id: h-neutron-star-quark-crossover-2-solar-mass
title: "A smooth quark-hadron crossover (rather than first-order phase transition) in neutron star cores is consistent with 2 M_sun pulsars and NICER M-R constraints, and will be distinguishable from hadronic-only EOS by future 0.3 km radius precision"
status: active
priority: high
impact_score: 0.83
created: "2026-05-07"
last_updated: "2026-05-07"
related_disciplines:
  - astrophysics
  - nuclear-physics
unknowns_addressed:
  - u-neutron-star-eos-dense-matter-phase-transition
evidence_links:
  - doi: "10.1103/PhysRevLett.120.172703"
    type: supporting
    confidence: 0.78
    note: "Annala et al. (2018) - quark-hadron crossover consistent with GW170817 and 2 M_sun"
  - doi: "10.3847/2041-8213/ab0c2f"
    type: related
    confidence: 0.72
    note: "NICER J0030+0451 M-R: current 1-sigma contour spans hadronic and crossover EOS families"
proposed_tests:
  - description: >
      Accumulate NICER measurements of 5 pulsars to achieve R_1.4 precision of 0.3 km (1-sigma).
      Compare Bayesian evidence for three EOS model classes: hadronic-only, quark-hadron crossover,
      first-order phase transition. Prediction: Bayes factor > 10 favoring crossover model
      if true R_1.4 is in 11.5-12.5 km range.
""")

# ──────────────────────────────────────────────────────────
# Bridge 3: Pandemic preparedness ↔ optimal stopping / decision theory (public health ↔ mathematics)
# ──────────────────────────────────────────────────────────
d = mkdirs("cross-domain", "epidemiology-mathematics")
write(os.path.join(d, "b-pandemic-optimal-stopping.yaml"), """\
id: b-pandemic-optimal-stopping
title: "Optimal epidemic intervention timing is an optimal stopping problem where the decision to implement NPIs minimizes total social cost, with the threshold case count derived from the ratio of NPI costs to transmission reduction benefit"
fields:
  - epidemiology
  - mathematics
  - public-health
bridge_claim: "The decision to implement non-pharmaceutical interventions (NPIs) during a growing epidemic is an optimal stopping problem with value function V(I, t) = min_{tau} E[C(I, t, tau)], where the optimal stopping threshold I* = alpha / (beta * delta_R) balances NPI cost alpha against transmission reduction beta*delta_R, predicting that early interventions are optimal whenever epidemic growth rate r > r_threshold."
translation_table:
  - field_a_term: "epidemic incidence I(t) on day t of outbreak"
    field_b_term: "state variable in optimal stopping problem"
    note: "Incidence is the observable; the stopping rule specifies at which I(t) to intervene"
  - field_a_term: "NPIs (lockdowns, school closures, mask mandates)"
    field_b_term: "control action in stochastic optimal control formulation"
    note: "NPI implementation corresponds to stopping the uncontrolled epidemic process and switching to controlled dynamics"
  - field_a_term: "reproduction number R0 -> Rc under NPI"
    field_b_term: "drift coefficient change in SIR stochastic process"
    note: "NPIs reduce beta, changing Brownian drift from positive (growing epidemic) to negative (declining)"
  - field_a_term: "herd immunity threshold HIT = 1 - 1/R0"
    field_b_term: "terminal boundary condition in finite-horizon optimal stopping"
    note: "Interventions before HIT is reached can avoid the full epidemic; stopping late (I > HIT S0) is suboptimal"
status: proposed
communication_gap: "Public health officials make intervention decisions based on epidemiological thresholds and political considerations while decision theorists study optimal stopping; the formal connection between epidemic decision-making and optimal stopping theory is underexplored in both public health training and decision theory curricula."
cross_pollination_opportunities:
  - "Developing real-time optimal stopping algorithms for epidemic intervention that incorporate uncertainty in R0 and case ascertainment using Sequential Monte Carlo"
  - "Applying regret minimization theory (minimax regret) to epidemic interventions under model uncertainty, providing robust decision rules without requiring a specific epidemic model"
references:
  - doi: "10.1098/rsif.2020.0435"
    note: "Alvarez et al. (2020) J R Soc Interface - optimal lockdown in the SIR model: cost-benefit analysis"
  - doi: "10.1073/pnas.2014347118"
    note: "Berger et al. (2020) PNAS - optimal testing and containment decisions under uncertainty"
  - doi: "10.1017/S0266466606060294"
    note: "Chick (2005) - Bayesian sequential clinical trial design as optimal stopping"
related_unknowns:
  - u-pandemic-intervention-timing-optimal-uncertainty
last_reviewed: "2026-05-07"
""")

ud3 = mkdirs("unknowns-catalog", "epidemiology")
write(os.path.join(ud3, "u-pandemic-intervention-timing-optimal-uncertainty.yaml"), """\
id: u-pandemic-intervention-timing-optimal-uncertainty
title: "How should optimal epidemic intervention timing be modified when the reproduction number R0, case ascertainment fraction, and NPI effectiveness are all uncertain, and can Bayesian optimal stopping provide robust real-time guidance?"
status: open
priority: high
disciplines:
  - epidemiology
  - mathematics
  - public-health
summary: >
  Optimal stopping theory for epidemic intervention assumes known parameters (R0,
  NPI effectiveness, case ascertainment). In reality, all parameters are uncertain,
  especially in the early outbreak phase. Decisions made under model uncertainty
  can be far from optimal under the true model. Bayesian methods update parameter
  estimates as data accumulate, but the interaction between posterior uncertainty
  and optimal threshold shifts is not well characterized. Whether minimax regret
  or expected utility maximization provides better decision rules under pandemic
  uncertainty is unresolved. The mathematical framework exists but has not been
  calibrated against historical pandemic intervention timing data.
systematic_gaps:
  - Retrospective analyses of COVID-19 intervention timing have not been cast in a formal optimal stopping framework
  - The speed of Bayesian R0 estimation in early outbreaks (< 50 confirmed cases) is insufficient for timely optimal stopping
  - Political and behavioral constraints on NPI implementation are not captured in mathematical optimal stopping models
related_bridges:
  - b-pandemic-optimal-stopping
last_reviewed: "2026-05-07"
""")

write(os.path.join(hd, "h-minimax-regret-pandemic-intervention.yaml"), """\
id: h-minimax-regret-pandemic-intervention
title: "Minimax regret optimal stopping rules for epidemic intervention are more robust than expected-utility-maximizing rules when R0 uncertainty exceeds 20%, testable by retrospective analysis of COVID-19 intervention timing across 50 countries"
status: active
priority: high
impact_score: 0.75
created: "2026-05-07"
last_updated: "2026-05-07"
related_disciplines:
  - epidemiology
  - mathematics
  - public-health
unknowns_addressed:
  - u-pandemic-intervention-timing-optimal-uncertainty
evidence_links:
  - doi: "10.1098/rsif.2020.0435"
    type: supporting
    confidence: 0.65
    note: "Alvarez et al. (2020) - optimal lockdown derived under known parameters; uncertainty not addressed"
  - doi: "10.1073/pnas.2014347118"
    type: related
    confidence: 0.60
    note: "Berger et al. (2020) - Bayesian testing decisions under uncertainty; related framework"
proposed_tests:
  - description: >
      Retrospectively apply minimax regret and expected utility optimal stopping rules
      to COVID-19 data from 50 countries (March-June 2020). Compute counterfactual
      deaths and economic costs under each rule assuming the true (ex-post) R0.
      Prediction: minimax regret rule reduces regret by > 30% vs expected utility
      rule when R0 uncertainty (prior SD/mean) > 20%.
""")

# ──────────────────────────────────────────────────────────
# Bridge 4: Geomagnetic reversals ↔ dynamo theory (geophysics ↔ magnetohydrodynamics)
# ──────────────────────────────────────────────────────────
d = mkdirs("cross-domain", "geophysics-mathematics")
write(os.path.join(d, "b-geomagnetic-reversal-dynamo.yaml"), """\
id: b-geomagnetic-reversal-dynamo
title: "Geomagnetic field reversals are spontaneous symmetry-breaking events in Earth's geodynamo, described by low-dimensional MHD models where reversals correspond to chaotic transitions between two attractors of opposite magnetic polarity"
fields:
  - geophysics
  - physics
  - mathematics
bridge_claim: "Earth's geomagnetic field is generated by convective flow in the outer core, modeled as a magnetohydrodynamic dynamo where the magnetic field satisfies the induction equation dB/dt = curl(v x B) + eta*nabla^2*B; reversals occur when turbulent fluctuations push the system over a separatrix between two stable attractors of opposite dipole polarity in a chaotic attractor landscape."
translation_table:
  - field_a_term: "geomagnetic dipole field strength"
    field_b_term: "order parameter of MHD dynamo attractor (dipole vs quadrupole)"
    note: "Reversals involve weakening dipole followed by recovery in opposite polarity; analogous to symmetry breaking in bifurcation"
  - field_a_term: "polarity reversal duration ~ 5,000-10,000 years"
    field_b_term: "transit time through unstable manifold between MHD attractors"
    note: "Reversal duration reflects passage through low-field chaotic region; predictable from attractor geometry"
  - field_a_term: "paleomagnetic secular variation rate"
    field_b_term: "Lyapunov exponent of geodynamo chaotic attractor"
    note: "Unpredictability of secular variation reflects underlying chaos; reversal timing is stochastic"
  - field_a_term: "reversal frequency in paleomagnetic record"
    field_b_term: "mean first-passage time between attractor basins"
    note: "Reversals every ~200,000 yr on average; Poisson-like distribution consistent with noise-driven transitions"
status: established
communication_gap: "Paleomagnetists study reversal stratigraphy in sediment and volcanic records while MHD dynamicists simulate geodynamo numerically; the connection between observed reversal statistics and dynamical properties of MHD attractors requires expertise in both paleo-data analysis and nonlinear dynamics."
cross_pollination_opportunities:
  - "Using paleomagnetic reversal rate changes (e.g., long quiet intervals like the Cretaceous Normal Superchron) to infer changes in outer core convective vigor connected to mantle dynamics"
  - "Applying random dynamical systems theory to predict the distribution of reversal durations and polarity interval lengths from geodynamo model parameters"
references:
  - doi: "10.1126/science.1173636"
    note: "Glatzmaier & Roberts (1995) Nature - first numerical simulation of a geomagnetic reversal"
  - doi: "10.1007/s11214-011-9775-x"
    note: "Hulot et al. (2010) Space Sci Rev - geomagnetic field and secular variation review"
  - doi: "10.1016/j.pepi.2009.11.003"
    note: "Olson & Amit (2014) - geomagnetic reversal mechanism in numerical dynamo models"
related_unknowns:
  - u-geomagnetic-reversal-trigger-mechanism
last_reviewed: "2026-05-07"
""")

ud4 = mkdirs("unknowns-catalog", "geoscience")
write(os.path.join(ud4, "u-geomagnetic-reversal-trigger-mechanism.yaml"), """\
id: u-geomagnetic-reversal-trigger-mechanism
title: "What triggers geomagnetic reversals — internal MHD fluctuations, mantle thermal anomalies, or inner core heterogeneities — and can reversal timing be predicted from current geomagnetic field observations?"
status: open
priority: high
disciplines:
  - geophysics
  - magnetohydrodynamics
  - mathematics
summary: >
  Geomagnetic reversals are poorly understood mechanistically. They may be triggered
  by: (1) internal MHD fluctuations exceeding a threshold in the outer core;
  (2) changes in mantle heat flow altering outer core convection patterns;
  (3) inner core boundary heterogeneities biasing the geodynamo. Numerical
  geodynamo simulations produce reversals but at rates inconsistent with the
  paleomagnetic record; they require Ekman numbers much larger than Earth's actual
  value. Whether the geomagnetic field is currently heading toward a reversal
  (dipole has weakened 9% since 1840) or a short-duration excursion is unresolved.
  Paleomagnetic precursors (field structure changes) before known reversals have
  not been systematically validated as predictive.
systematic_gaps:
  - Geodynamo simulations are far from Earth's parameter regime (Pm, Ek too large)
  - Paleomagnetic precursor signatures before reversals are debated and differ between reversals
  - The role of inner core growth in geodynamo evolution over geological time is not constrained
related_bridges:
  - b-geomagnetic-reversal-dynamo
last_reviewed: "2026-05-07"
""")

write(os.path.join(hd, "h-dipole-weakening-precursor-reversal.yaml"), """\
id: h-dipole-weakening-precursor-reversal
title: "The ongoing geomagnetic dipole weakening is a precursor to a polarity excursion or reversal within 2,000 years, identifiable by the current South Atlantic Anomaly growth rate exceeding 50% of reversal precursor thresholds derived from paleomagnetic records"
status: active
priority: medium
impact_score: 0.69
created: "2026-05-07"
last_updated: "2026-05-07"
related_disciplines:
  - geophysics
  - physics
unknowns_addressed:
  - u-geomagnetic-reversal-trigger-mechanism
evidence_links:
  - doi: "10.1016/j.pepi.2009.11.003"
    type: related
    confidence: 0.55
    note: "Olson & Amit (2014) - current dipole weakening in context of numerical geodynamo models"
  - doi: "10.1007/s11214-011-9775-x"
    type: related
    confidence: 0.50
    note: "Hulot et al. (2010) - current field changes and reversal risk assessment"
proposed_tests:
  - description: >
      Compile high-resolution paleomagnetic records from the Brunhes-Matuyama reversal
      and 5 excursions. Define quantitative precursor metrics (dipole moment rate of change,
      non-dipole field energy fraction, SAA latitude). Apply to current observatory data.
      Prediction: current field satisfies >= 2 of 4 precursor criteria defined by median
      precursor values from paleomagnetic record.
""")

# ──────────────────────────────────────────────────────────
# Bridge 5: Semantic memory ↔ distributional semantics / word vectors (cognitive science ↔ NLP)
# ──────────────────────────────────────────────────────────
d = mkdirs("cross-domain", "cognitive-science-linguistics")
write(os.path.join(d, "b-semantic-memory-word-vectors.yaml"), """\
id: b-semantic-memory-word-vectors
title: "Distributional semantic models (word2vec, GloVe) produce vector representations that predict human semantic similarity judgments, priming latencies, and neural activation patterns in inferior temporal cortex, formalizing the distributional hypothesis of meaning"
fields:
  - cognitive-science
  - linguistics
  - computer-science
bridge_claim: "The cosine similarity between word vectors trained on large corpora predicts human semantic similarity ratings (Pearson r ~ 0.8) and word association norms, because both reflect the co-occurrence statistics of words in natural language, implementing the distributional hypothesis: words occurring in similar contexts have similar meanings."
translation_table:
  - field_a_term: "semantic memory network (human mental lexicon)"
    field_b_term: "high-dimensional vector space where word vectors cluster by meaning"
    note: "Both represent words by their relationships to other words; similarity structure is the primary organizing principle"
  - field_a_term: "semantic priming (faster RT for semantically related word pairs)"
    field_b_term: "high cosine similarity between prime and target word vectors"
    note: "Priming effect magnitude correlates with vector cosine similarity across word pairs"
  - field_a_term: "semantic category membership (dog is a mammal)"
    field_b_term: "vector arithmetic: king - man + woman = queen"
    note: "Linear vector offsets capture semantic relations (gender, country-capital, species-genus)"
  - field_a_term: "anterior temporal lobe (ATL) semantic hub"
    field_b_term: "RSA correlation between neural activation patterns and word vector similarity"
    note: "fMRI MVPA shows ATL geometry matches word vector geometry (Huth et al. 2016)"
status: established
communication_gap: "Cognitive scientists study semantic memory through behavioral experiments and brain imaging while NLP researchers develop distributional models for downstream applications; the theoretical connection between co-occurrence statistics and cognitive semantic organization is acknowledged but rarely integrated into either neural or computational models of meaning."
cross_pollination_opportunities:
  - "Using word vector geometry to predict which semantic distinctions are neuroscientifically distinguishable, guiding fMRI experimental design"
  - "Testing whether pathological semantic memory in Alzheimer's disease is captured by systematic changes in neural word vector geometry measured with MEG"
references:
  - doi: "10.48550/arXiv.1301.3781"
    note: "Mikolov et al. (2013) - word2vec: efficient estimation of word representations in vector space"
  - doi: "10.1038/nn.4012"
    note: "Huth et al. (2016) Nature Neurosci - natural speech reveals semantic brain maps matching distributional semantics"
  - doi: "10.1037/0033-295X.114.2.211"
    note: "Landauer & Dumais (1997) Psych Rev - latent semantic analysis and distributional learning"
related_unknowns:
  - u-distributional-semantics-compositionality
last_reviewed: "2026-05-07"
""")

ud5 = mkdirs("unknowns-catalog", "cognitive-science")
write(os.path.join(ud5, "u-distributional-semantics-compositionality.yaml"), """\
id: u-distributional-semantics-compositionality
title: "Can distributional semantic models capture the compositionality of language (the meaning of a phrase from the meanings of its parts), and do compositional vector representations match human neural patterns for phrase-level meaning?"
status: open
priority: high
disciplines:
  - cognitive-science
  - linguistics
  - computer-science
summary: >
  Word vectors capture lexical semantics well but compositionality (how phrase and
  sentence meaning is built from word meaning) is poorly handled by simple vector
  addition or multiplication. Human semantic memory represents sentences differently
  from the linear sum of word vectors: negation, quantification, and syntactic structure
  systematically alter meaning in ways not captured by distributional models.
  Whether transformer-based sentence embeddings (SBERT) better capture compositional
  semantics and match neural representations in human brain imaging is actively debated.
  The relationship between distributional compositionality and formal semantics
  (lambda calculus, model-theoretic truth conditions) is unresolved.
systematic_gaps:
  - No vector composition operation satisfies all formal semantic compositionality constraints
  - Phrase-level fMRI representational similarity with SBERT embeddings has not been systematically characterized
  - Distributional models fail on novel negations, quantifiers, and counterfactuals
related_bridges:
  - b-semantic-memory-word-vectors
last_reviewed: "2026-05-07"
""")

write(os.path.join(hd, "h-transformer-embeddings-compositional-brain-alignment.yaml"), """\
id: h-transformer-embeddings-compositional-brain-alignment
title: "Contextual sentence embeddings from large language models (GPT-4 layer 20) predict fMRI BOLD responses to novel sentences in temporal and prefrontal cortex with Pearson r > 0.5, exceeding static word vector predictions by > 0.15"
status: active
priority: high
impact_score: 0.79
created: "2026-05-07"
last_updated: "2026-05-07"
related_disciplines:
  - cognitive-science
  - linguistics
  - computer-science
unknowns_addressed:
  - u-distributional-semantics-compositionality
evidence_links:
  - doi: "10.1038/nn.4012"
    type: supporting
    confidence: 0.80
    note: "Huth et al. (2016) - word vector RSA with brain encoding models shows semantic map"
  - doi: "10.1016/j.neuron.2022.08.021"
    type: related
    confidence: 0.73
    note: "Schrimpf et al. (2021) - neural predictivity of language models correlates with model size"
proposed_tests:
  - description: >
      Collect fMRI from 20 subjects listening to 1000 novel sentences from naturalistic
      stories. Extract GPT-4 layer embeddings and static GloVe embeddings for each sentence.
      Compute encoding model R^2 for each ROI. Prediction: GPT-4 layer 20 explains
      variance > GloVe by 0.15 R in bilateral ATL; difference is significant p < 0.001.
""")

# ──────────────────────────────────────────────────────────
# Bridge 6: Hydrogel mechanics ↔ polymer network theory (materials science ↔ polymer physics)
# ──────────────────────────────────────────────────────────
d = mkdirs("cross-domain", "materials-science-physics")
write(os.path.join(d, "b-hydrogel-polymer-network-mechanics.yaml"), """\
id: b-hydrogel-polymer-network-mechanics
title: "Hydrogel mechanical properties are quantitatively predicted by rubber elasticity and Flory-Rehner theory, where the elastic modulus G = n*k*T (n = effective crosslink density) and swelling equilibrium balances elastic energy against polymer-solvent mixing free energy"
fields:
  - materials-science
  - polymer-physics
  - physics
bridge_claim: "The equilibrium swelling ratio Q and shear modulus G of a crosslinked hydrogel are jointly determined by the Flory-Rehner equations: G = n*k*T*Q^{1/3} (rubber elasticity) and mu_solvent = RT[ln(1-v2) + v2 + chi*v2^2 + v_e*(v2^{1/3}/2 - v2)] = 0, where n is crosslink density, chi is the Flory-Huggins parameter, and v2 is polymer volume fraction."
translation_table:
  - field_a_term: "hydrogel swelling ratio Q = V_swollen / V_dry"
    field_b_term: "polymer volume fraction v2 = 1/Q at equilibrium"
    note: "Q is controlled by crosslink density and chi parameter; Q ~ 10-100 for typical hydrogels"
  - field_a_term: "elastic shear modulus G of swollen hydrogel"
    field_b_term: "G = n*k*T*Q^{-1/3} from affine network model"
    note: "G decreases with swelling; n is strand density between crosslinks in dry state"
  - field_a_term: "fracture toughness of hydrogel"
    field_b_term: "lake-thomas tearing energy Gc = n * U * l0 * sqrt(n)"
    note: "Fracture requires breaking all chains crossing the crack plane; Gc scales as sqrt(strand length)"
  - field_a_term: "Flory-Huggins chi parameter"
    field_b_term: "polymer-solvent interaction free energy per monomer"
    note: "chi < 0.5 gives good solvent (swelling); chi > 0.5 gives poor solvent (collapse); chi is temperature-dependent"
status: established
communication_gap: "Materials scientists characterize hydrogel mechanics by measuring modulus and swelling while polymer physicists derive thermodynamic theory; the quantitative connection between molecular parameters (chi, crosslink density) and macroscopic mechanical properties (G, fracture toughness) is known in polymer theory but not systematically applied in biomaterial hydrogel design."
cross_pollination_opportunities:
  - "Designing tough double-network hydrogels by using Flory-Rehner theory to optimize the modulus mismatch between brittle and ductile networks for maximum energy dissipation"
  - "Predicting hydrogel drug release kinetics by combining Flory-Rehner swelling equilibrium with Fickian diffusion equations for encapsulated drug molecules"
references:
  - doi: "10.1002/app.1953.070070308"
    note: "Flory & Rehner (1953) J Appl Phys - thermodynamic theory of rubber elasticity and swelling"
  - doi: "10.1126/science.1241214"
    note: "Gong et al. (2010) Science - double network hydrogels with extraordinary toughness"
  - doi: "10.1039/c4sm00269e"
    note: "Creton (2017) Macromolecules - tough hydrogels: review of physical and chemical approaches"
related_unknowns:
  - u-hydrogel-fracture-toughness-network-structure
last_reviewed: "2026-05-07"
""")

ud6 = mkdirs("unknowns-catalog", "materials-science")
write(os.path.join(ud6, "u-hydrogel-fracture-toughness-network-structure.yaml"), """\
id: u-hydrogel-fracture-toughness-network-structure
title: "What polymer network architectural features (strand length distribution, topological defects, physical vs. chemical crosslinks) determine hydrogel fracture toughness, and can they be predicted from small-angle X-ray scattering measurements?"
status: open
priority: medium
disciplines:
  - materials-science
  - polymer-physics
summary: >
  Classical rubber elasticity (Lake-Thomas theory) predicts fracture toughness from
  strand density and length. Real hydrogels deviate substantially: topological defects
  (loops, dangling ends) reduce effective crosslink density; inhomogeneous crosslink
  distribution creates stress concentrations; physical crosslinks (hydrogen bonds,
  hydrophobic interactions) provide sacrificial energy dissipation. The quantitative
  relationship between network defects (measured by SAXS or NMR) and fracture
  toughness has not been established. Double-network hydrogels achieve Gc ~ 1000
  J/m^2 (vs Lake-Thomas prediction of 10-100 J/m^2) through mechanisms not fully
  captured by any current theory.
systematic_gaps:
  - SAXS measures network heterogeneity but cannot distinguish load-bearing from dangling strands
  - Lake-Thomas theory underestimates Gc by 10-100x for tough hydrogels
  - The role of viscoelastic dissipation vs. elastic energy storage in hydrogel toughness is not separated experimentally
related_bridges:
  - b-hydrogel-polymer-network-mechanics
last_reviewed: "2026-05-07"
""")

write(os.path.join(hd, "h-double-network-hydrogel-toughness-sacrificial-bond.yaml"), """\
id: h-double-network-hydrogel-toughness-sacrificial-bond
title: "Double-network hydrogel toughness scales as Gc ~ G1 * l_c where G1 is the first network modulus and l_c is the critical strand length for sacrificial bond rupture, predicting a 10-fold toughness increase with each doubling of first-network strand length"
status: active
priority: medium
impact_score: 0.72
created: "2026-05-07"
last_updated: "2026-05-07"
related_disciplines:
  - materials-science
  - polymer-physics
unknowns_addressed:
  - u-hydrogel-fracture-toughness-network-structure
evidence_links:
  - doi: "10.1126/science.1241214"
    type: supporting
    confidence: 0.75
    note: "Gong et al. (2010) - double network mechanism: first network fractures progressively, dissipating energy"
  - doi: "10.1039/c4sm00269e"
    type: related
    confidence: 0.68
    note: "Creton (2017) - toughening mechanisms in hydrogels: sacrificial bond review"
proposed_tests:
  - description: >
      Synthesize 5 PAAm/PAMPS double-network hydrogels varying first-network crosslinker
      content (0.1-2 mol%) to vary G1 from 5-200 kPa. Measure Gc by pure shear fracture
      test. Measure G1 by rheology and l_c by SAXS. Fit Gc ~ G1 * l_c^alpha.
      Prediction: alpha = 1.0 +/- 0.2, R^2 > 0.9.
""")

# ──────────────────────────────────────────────────────────
# Bridge 7: Cellular senescence ↔ tumor suppression / cancer (biology ↔ medicine)
# ──────────────────────────────────────────────────────────
d = mkdirs("cross-domain", "biology-medicine")
write(os.path.join(d, "b-cellular-senescence-tumor-suppression.yaml"), """\
id: b-cellular-senescence-tumor-suppression
title: "Cellular senescence is a tumor-suppressive mechanism that permanently arrests cell proliferation in response to oncogenic stress, but the senescence-associated secretory phenotype (SASP) paradoxically promotes inflammation and cancer in aged tissues"
fields:
  - biology
  - medicine
  - cell-biology
bridge_claim: "Oncogene-induced senescence (OIS) causes permanent cell cycle arrest via p21/p16-Rb pathway activation, suppressing tumor progression by removing pre-cancerous cells from the proliferating pool; however, the pro-inflammatory SASP (IL-6, IL-8, MMPs secreted by senescent cells) creates a tissue microenvironment that promotes neighboring cell transformation, explaining why senescent cell accumulation in aging paradoxically increases cancer risk."
translation_table:
  - field_a_term: "replicative senescence (telomere shortening arrest)"
    field_b_term: "p53/p21 pathway activation at critically short telomere"
    note: "Telomere erosion triggers ATM/ATR kinase response, activating p53 -> p21 -> Rb pathway to halt S phase"
  - field_a_term: "oncogene-induced senescence (OIS)"
    field_b_term: "p16INK4a/Rb pathway activation by Ras, BRAF oncoproteins"
    note: "Oncogenic Ras activates ARF -> MDM2 inhibition -> p53 and independently p16 -> Rb; both pathways required for stable OIS"
  - field_a_term: "SASP cytokines (IL-6, IL-8, GRO-alpha)"
    field_b_term: "NF-kB and mTOR activation in senescent cells"
    note: "SASP promotes paracrine senescence and immune surveillance; chronic SASP without clearance is pro-tumorigenic"
  - field_a_term: "immune clearance of senescent cells (immunosurveillance)"
    field_b_term: "NK cell and macrophage recognition of SASP NKG2D ligands and eat-me signals"
    note: "Efficient clearance is tumor-suppressive; impaired clearance leads to SASP accumulation and cancer promotion"
status: established
communication_gap: "Cell biologists study senescence molecular mechanisms while oncologists and geriatricians observe its systemic effects; the dual tumor-suppressive and tumor-promoting roles of senescence are underappreciated clinically, creating a therapeutic challenge for senolytics in cancer patients."
cross_pollination_opportunities:
  - "Developing senolytic therapies (dasatinib, quercetin, navitoclax) that selectively clear SASP-producing senescent cells in aged tissue without disrupting acute tumor-suppressive senescence"
  - "Using biomarkers of SASP burden (plasma IL-6, GDF-15, p16 mRNA in blood) to stratify cancer risk in aging populations and guide preventive interventions"
references:
  - doi: "10.1016/j.cell.2006.02.015"
    note: "Campisi & d'Adda di Fagagna (2007) Nat Rev Mol Cell Biol - cellular senescence: when bad things happen to good cells"
  - doi: "10.1038/nature04268"
    note: "Braig et al. (2005) Nature - oncogene-induced senescence as initial barrier to malignant transformation"
  - doi: "10.1016/j.cell.2019.06.001"
    note: "Gorgoulis et al. (2019) Cell - cellular senescence: defining a path forward"
related_unknowns:
  - u-senescence-sasp-cancer-promotion-threshold
last_reviewed: "2026-05-07"
""")

ud7 = mkdirs("unknowns-catalog", "biology")
write(os.path.join(ud7, "u-senescence-sasp-cancer-promotion-threshold.yaml"), """\
id: u-senescence-sasp-cancer-promotion-threshold
title: "At what senescent cell burden does the SASP switch from tumor-suppressive (immune recruitment) to tumor-promoting (chronic inflammation), and can this threshold be measured as a clinical biomarker?"
status: open
priority: high
disciplines:
  - biology
  - medicine
  - oncology
summary: >
  Senescence is acutely tumor-suppressive (stops pre-cancerous cells) but chronically
  tumor-promoting (SASP creates pro-inflammatory, immunosuppressive microenvironment).
  The transition between these phases depends on senescent cell burden, clearance
  efficiency, SASP composition, and tissue context. This threshold is unknown and
  likely varies by tissue type and individual. Clinical implications are significant:
  senolytics that clear senescent cells may be beneficial at high burden but
  counterproductive if they eliminate tumor-suppressive senescent cells.
  Non-invasive biomarkers of senescent cell burden in specific tissues do not exist.
systematic_gaps:
  - No animal model has systematically measured cancer incidence as a function of senescent cell burden at defined levels
  - p16 expression in blood is a systemic proxy but not tissue-specific
  - SASP composition changes with time after senescence induction and is not uniform
related_bridges:
  - b-cellular-senescence-tumor-suppression
last_reviewed: "2026-05-07"
""")

write(os.path.join(hd, "h-senolytic-therapy-reduces-cancer-risk-aged-tissue.yaml"), """\
id: h-senolytic-therapy-reduces-cancer-risk-aged-tissue
title: "Senolytic clearance of p16-high senescent cells in aged mice reduces spontaneous tumor incidence by > 30% without increasing proliferation of pre-cancerous cells, demonstrating that SASP chronically dominates over senescence tumor suppression in aging"
status: active
priority: high
impact_score: 0.82
created: "2026-05-07"
last_updated: "2026-05-07"
related_disciplines:
  - biology
  - medicine
unknowns_addressed:
  - u-senescence-sasp-cancer-promotion-threshold
evidence_links:
  - doi: "10.1016/j.cell.2019.06.001"
    type: supporting
    confidence: 0.70
    note: "Gorgoulis et al. (2019) - review supporting senolytic benefit in cancer prevention"
  - doi: "10.1038/nature16932"
    note: "Baker et al. (2016) Nature - clearance of p16 senescent cells delays age-related disorders in mice"
proposed_tests:
  - description: >
      Treat 18-month-old C57Bl/6 mice with ABT-263 (navitoclax, senolytic) vs. vehicle
      for 3 months. Monitor for 12 months. Primary endpoint: spontaneous tumor incidence
      (necropsy + histology). Secondary: p16+ cell frequency in liver, lung, colon
      by immunofluorescence. Prediction: 30% reduction in tumor incidence in senolytic arm.
""")

# ──────────────────────────────────────────────────────────
# Bridge 8: Quantum gravity ↔ holographic entanglement entropy (physics ↔ information theory)
# ──────────────────────────────────────────────────────────
d = mkdirs("cross-domain", "quantum-physics-information")
write(os.path.join(d, "b-quantum-gravity-holographic-entropy.yaml"), """\
id: b-quantum-gravity-holographic-entropy
title: "The Ryu-Takayanagi formula equates the entanglement entropy of a boundary CFT region to the area of the minimal bulk surface divided by 4G, connecting quantum gravity geometry to quantum information theory through holography"
fields:
  - physics
  - information-theory
  - quantum-physics
bridge_claim: "The holographic entanglement entropy formula S_A = Area(gamma_A) / (4*G_N*hbar) (Ryu-Takayanagi) states that entanglement entropy of boundary region A in a CFT equals the area of the minimal bulk surface gamma_A anchored to partial_A in units of the Planck length, providing a geometric bulk dual of quantum information in the boundary theory."
translation_table:
  - field_a_term: "Von Neumann entanglement entropy S_A = -Tr(rho_A log rho_A)"
    field_b_term: "area of minimal bulk geodesic surface gamma_A in AdS"
    note: "RT formula: S_A = min(Area(gamma_A)) / 4G_N; quantum corrections give S = Area/4G + S_bulk"
  - field_a_term: "mutual information I(A:B) = S_A + S_B - S_AB in CFT"
    field_b_term: "connected vs disconnected bulk minimal surfaces"
    note: "Mutual information undergoes phase transition when dominant saddle switches from connected to disconnected surface"
  - field_a_term: "quantum error correction in boundary CFT"
    field_b_term: "bulk reconstruction behind the RT surface"
    note: "Bulk operators within the entanglement wedge of A can be reconstructed from CFT region A: Rindler-HKLL reconstruction"
  - field_a_term: "black hole information paradox"
    field_b_term: "Page curve from RT surface transition: information returns after Page time"
    note: "The island formula (RT with islands) resolves the information paradox: S_rad follows Page curve"
status: established
communication_gap: "String theorists study holography and the RT formula while quantum information theorists study entanglement entropy; the translation between the geometric (area) and information-theoretic (entropy) languages requires expertise in AdS/CFT rarely taught in QI curricula."
cross_pollination_opportunities:
  - "Using quantum error correction codes (HaPPY code, hyperinvariant tensor networks) to model holographic bulk-boundary maps and test RT formula predictions"
  - "Applying the island formula to analog gravity systems (Josephson junction arrays, Bose-Einstein condensates) to test holographic entropy predictions in laboratory settings"
references:
  - doi: "10.1103/PhysRevLett.96.181602"
    note: "Ryu & Takayanagi (2006) PRL - holographic derivation of entanglement entropy from AdS/CFT"
  - doi: "10.1007/JHEP11(2014)163"
    note: "Pastawski et al. (2015) JHEP - holographic quantum error-correcting codes from perfect tensors"
  - doi: "10.1007/JHEP08(2019)127"
    note: "Almheiri et al. (2019) - islands and the entropy of Hawking radiation from the Page curve"
related_unknowns:
  - u-holographic-entanglement-bulk-reconstruction-limits
last_reviewed: "2026-05-07"
""")

ud8 = mkdirs("unknowns-catalog", "quantum-physics")
write(os.path.join(ud8, "u-holographic-entanglement-bulk-reconstruction-limits.yaml"), """\
id: u-holographic-entanglement-bulk-reconstruction-limits
title: "What are the precise limits of bulk reconstruction from boundary entanglement data, and can the entanglement wedge reconstruction be extended beyond semiclassical gravity to full quantum gravity?"
status: open
priority: high
disciplines:
  - quantum-physics
  - information-theory
  - mathematics
summary: >
  The Ryu-Takayanagi formula is derived in classical gravity (O(1/G_N) leading order).
  Quantum corrections (islands, quantum extremal surfaces) extend it but rely on
  semiclassical effective field theory. Whether the RT formula survives in full
  non-perturbative quantum gravity (e.g., without a classical spacetime) is unknown.
  Entanglement wedge reconstruction (the claim that any bulk operator in the wedge
  can be reconstructed from boundary region A) is proven for semiclassical states
  but the operator algebra for general states is not established. Whether tensor
  networks provide exact models of holographic duality or only approximate them is debated.
systematic_gaps:
  - RT formula derivation from first principles in string theory is incomplete
  - Entanglement wedge reconstruction for bulk operators near black hole singularities is not understood
  - The island formula requires replica wormholes whose physical interpretation in non-gravitational theories is unclear
related_bridges:
  - b-quantum-gravity-holographic-entropy
last_reviewed: "2026-05-07"
""")

write(os.path.join(hd, "h-island-formula-page-curve-tensor-network-model.yaml"), """\
id: h-island-formula-page-curve-tensor-network-model
title: "Random tensor network models implementing the island formula reproduce the Page curve of Hawking radiation with Page time t_Page = S_BH / (2*pi * T_Hawking), testable in Brownian circuit analog gravity models"
status: active
priority: high
impact_score: 0.85
created: "2026-05-07"
last_updated: "2026-05-07"
related_disciplines:
  - quantum-physics
  - information-theory
unknowns_addressed:
  - u-holographic-entanglement-bulk-reconstruction-limits
evidence_links:
  - doi: "10.1007/JHEP08(2019)127"
    type: supporting
    confidence: 0.80
    note: "Almheiri et al. (2019) - island formula reproduces Page curve analytically"
  - doi: "10.1007/JHEP11(2014)163"
    type: related
    confidence: 0.70
    note: "HaPPY code - tensor network holography with exact RT formula"
proposed_tests:
  - description: >
      Implement a random Clifford circuit on 100 qubits simulating Brownian black hole
      dynamics. Compute entanglement entropy of radiation subsystem at each time step.
      Compare to Page curve prediction: entropy rises, peaks at Page time, then decreases
      to zero. Prediction: entropy follows Page curve with deviation < 5% at Page time.
""")

# ──────────────────────────────────────────────────────────
# Bridge 9: Traffic flow ↔ Lighthill-Whitham-Richards PDE (transportation ↔ fluid mechanics)
# ──────────────────────────────────────────────────────────
d = mkdirs("cross-domain", "engineering-mathematics")
write(os.path.join(d, "b-traffic-flow-lwr-pde.yaml"), """\
id: b-traffic-flow-lwr-pde
title: "The Lighthill-Whitham-Richards (LWR) traffic flow model treats vehicle density as a conserved quantity obeying a first-order hyperbolic PDE, predicting shock wave formation, traffic jam propagation speed, and stop-and-go wave dynamics using fluid mechanical methods"
fields:
  - engineering
  - mathematics
  - physics
bridge_claim: "Vehicle traffic obeys the conservation law d_rho/d_t + d_q/d_x = 0 where q = rho * v(rho) is the flow-density fundamental diagram, generating shock waves (traffic jams) that propagate at the Rankine-Hugoniot speed w = (q_R - q_L)/(rho_R - rho_L), with rarefaction waves describing acceleration out of jams."
translation_table:
  - field_a_term: "vehicle density rho(x,t) [vehicles/km]"
    field_b_term: "conserved density in inviscid Burgers/LWR equation"
    note: "Vehicle count is conserved (no creation/annihilation on freeway); rho satisfies a conservation law"
  - field_a_term: "fundamental diagram q = rho * v(rho)"
    field_b_term: "flux function F(rho) in hyperbolic conservation law"
    note: "Greenshields q = v_f * rho * (1 - rho/rho_max); Greenberg, Newell-Daganzo fundamental diagrams differ"
  - field_a_term: "traffic shock wave (stop-and-go jam)"
    field_b_term: "Rankine-Hugoniot discontinuity in density field"
    note: "Jam propagates upstream at w = Delta_q / Delta_rho; typical w ~ -20 km/h for freeway traffic"
  - field_a_term: "capacity drop at freeway merge/bottleneck"
    field_b_term: "rarefaction fan transitioning from uncongested to congested branch"
    note: "Capacity drop corresponds to lower flow on congested branch of fundamental diagram"
status: established
communication_gap: "Traffic engineers use empirical fundamental diagrams and microsimulation while applied mathematicians study conservation laws; the formal connection between measured flow-density curves and LWR shock wave theory is established in transportation research but rarely taught as part of fluid mechanics curricula."
cross_pollination_opportunities:
  - "Designing variable speed limits and ramp metering using LWR optimal control theory to prevent shock wave formation at bottlenecks"
  - "Applying second-order traffic models (Aw-Rascle-Zhang) that include traffic pressure (anisotropy) to explain phantom jams not captured by first-order LWR"
references:
  - doi: "10.1098/rspa.1955.0089"
    note: "Lighthill & Whitham (1955) Proc R Soc - kinematic waves I: theory of traffic flow"
  - doi: "10.1287/opre.4.1.42"
    note: "Richards (1956) Oper Res - shock waves on the highway"
  - doi: "10.1007/s11235-020-00700-3"
    note: "Daganzo (1995) Transportation Research B - Daganzo fundamental diagram and cell transmission model"
related_unknowns:
  - u-traffic-phantom-jam-nucleation-mechanism
last_reviewed: "2026-05-07"
""")

ud9 = mkdirs("unknowns-catalog", "engineering")
write(os.path.join(ud9, "u-traffic-phantom-jam-nucleation-mechanism.yaml"), """\
id: u-traffic-phantom-jam-nucleation-mechanism
title: "What microscopic mechanism nucleates phantom traffic jams (stop-and-go waves without bottlenecks), and can their formation be predicted and suppressed by autonomous vehicle coordination?"
status: open
priority: high
disciplines:
  - engineering
  - mathematics
  - physics
summary: >
  Phantom traffic jams (Japaense: atsugari jiko) spontaneously appear on congested
  freeways with no bottleneck. They nucleate from density fluctuations that amplify
  under certain traffic conditions and propagate as backward-moving waves at ~20 km/h.
  The LWR model predicts they arise from instability of the congested branch of the
  fundamental diagram. The exact microscopic trigger (driver reaction time, car-following
  parameters, density fluctuation amplitude) has not been systematically characterized.
  Whether connected autonomous vehicles (CAVs) following Bilateral Control can suppress
  phantom jams at low market penetration rates is under investigation but not resolved.
systematic_gaps:
  - Natural phantom jam experiments with controlled initial conditions have not been conducted at scale
  - The Bando optimal velocity model predicts instability but its parameters have large uncertainty
  - CAV jam-suppression experiments (Stern et al. 2018) used only 1 AV in 22 vehicles; scaling is unknown
related_bridges:
  - b-traffic-flow-lwr-pde
last_reviewed: "2026-05-07"
""")

write(os.path.join(hd, "h-cav-phantom-jam-suppression-1percent.yaml"), """\
id: h-cav-phantom-jam-suppression-1percent
title: "A market penetration of 5% connected autonomous vehicles following smoothing control laws is sufficient to suppress phantom traffic jams on congested freeways, reducing average travel time by > 15%"
status: active
priority: high
impact_score: 0.77
created: "2026-05-07"
last_updated: "2026-05-07"
related_disciplines:
  - engineering
  - mathematics
  - physics
unknowns_addressed:
  - u-traffic-phantom-jam-nucleation-mechanism
evidence_links:
  - doi: "10.1038/s41598-018-26668-6"
    note: "Stern et al. (2018) Transp Res C - dissipation of stop-and-go waves with 1 AV in 22"
  - doi: "10.1007/s11235-020-00700-3"
    type: related
    confidence: 0.60
    note: "Daganzo (2006) - jam suppression via speed advisory systems"
proposed_tests:
  - description: >
      Simulate N = 200 vehicles on a ring road (as in Sugiyama et al. 2008) with
      5%, 10%, 20% CAVs using Bilateral Control smoothing. Measure: (1) time to jam
      formation after density perturbation; (2) average speed compared to no-CAV baseline.
      Prediction: 5% CAV penetration delays jam formation by > 5x and increases mean
      speed by > 15%.
""")

# ──────────────────────────────────────────────────────────
# Bridge 10: Ant colony optimization ↔ distributed computation (biology ↔ computer science)
# ──────────────────────────────────────────────────────────
d = mkdirs("cross-domain", "biology-computer-science")
write(os.path.join(d, "b-ant-colony-distributed-computation.yaml"), """\
id: b-ant-colony-distributed-computation
title: "Ant colony optimization (ACO) formalizes the pheromone trail mechanism of foraging ants as a distributed probabilistic graph search algorithm that finds near-optimal solutions to NP-hard combinatorial problems"
fields:
  - biology
  - computer-science
bridge_claim: "Foraging ants deposit pheromone tau_ij on edges (i,j) of a complete graph proportional to path quality (1/L_k), and choose edges probabilistically as p_{ij} = tau_ij^alpha * eta_ij^beta / sum(tau_il^alpha * eta_il^beta), reinforcing shorter paths; the resulting pheromone distribution converges to the optimal tour of the TSP with probability 1 as the number of iterations grows."
translation_table:
  - field_a_term: "pheromone trail strength tau_ij on ant path"
    field_b_term: "edge weight in probabilistic graph traversal"
    note: "Pheromone evaporation (tau -> (1-rho)*tau) prevents premature convergence; analogous to temperature in simulated annealing"
  - field_a_term: "stigmergic communication (indirect via environment)"
    field_b_term: "asynchronous message passing via shared memory (blackboard architecture)"
    note: "Ants communicate through pheromone field, not directly; equivalent to distributed agents writing/reading shared state"
  - field_a_term: "positive feedback in trail reinforcement"
    field_b_term: "reinforcement learning Q-value update"
    note: "ACO is equivalent to model-based RL where pheromone is the Q-table and environment is the TSP graph"
  - field_a_term: "colony-level path optimization"
    field_b_term: "parallel stochastic search with diversity maintenance via evaporation"
    note: "Colony is a parallel computation with N agents; diversity maintained by evaporation (anti-exploitation)"
status: established
communication_gap: "Biologists study foraging behavior as ecology while computer scientists use ACO as a heuristic algorithm; the formal equivalence between stigmergic behavior and parallel probabilistic search is known in computational intelligence but rarely discussed in biological foraging theory or evolutionary ecology."
cross_pollination_opportunities:
  - "Using ACO convergence theory to predict which foraging environments favor trail-based vs. direct communication strategies in social insects"
  - "Applying multi-colony ACO variants (MACO) to network routing problems, inspired by army ant bridge formation behavior"
references:
  - doi: "10.1109/3477.484436"
    note: "Dorigo et al. (1996) IEEE Trans Syst Man Cybern - ant system: optimization by a colony of cooperating agents"
  - doi: "10.1613/jair.1177"
    note: "Dorigo & Gambardella (1997) J Artif Intell Res - ant colony system: ACO for TSP"
  - doi: "10.1126/science.1226406"
    note: "Reid et al. (2011) J Exp Biol - ant colony optimization in biological contexts"
related_unknowns:
  - u-ant-colony-optimization-convergence-rate
last_reviewed: "2026-05-07"
""")

write(os.path.join(ud7, "u-ant-colony-optimization-convergence-rate.yaml"), """\
id: u-ant-colony-optimization-convergence-rate
title: "What is the time complexity of ant colony optimization convergence to the optimal TSP tour, and under what parameter conditions does ACO outperform other metaheuristics?"
status: open
priority: medium
disciplines:
  - computer-science
  - biology
  - mathematics
summary: >
  ACO is proven to converge to the optimal solution as iteration count -> infinity,
  but the convergence rate is unknown analytically. Empirically, ACO finds near-optimal
  TSP tours in O(n^2 log n) iterations for n-city instances, but this has not been
  proven. The parameter sensitivity of ACO (alpha, beta, rho, number of ants) is
  not characterized theoretically; optimal parameters are found by grid search in
  practice. Comparison to other metaheuristics (simulated annealing, genetic algorithms)
  on benchmark TSP instances shows mixed results depending on instance structure.
  The conditions under which ACO's distributed parallel structure provides an advantage
  over sequential algorithms have not been formalized.
systematic_gaps:
  - Convergence rate proofs for ACO on TSP with > 100 cities do not exist
  - Parameter sensitivity analysis has not been connected to problem structure features
  - The relationship between biological foraging parameters and ACO algorithm parameters is qualitative
related_bridges:
  - b-ant-colony-distributed-computation
last_reviewed: "2026-05-07"
""")

write(os.path.join(hd, "h-aco-convergence-rate-pheromone-evaporation.yaml"), """\
id: h-aco-convergence-rate-pheromone-evaporation
title: "ACO convergence rate to the TSP optimal tour scales as O(n^2 / rho) where rho is the evaporation rate, predicting that low evaporation rates converge faster on structured instances but slower on random ones"
status: active
priority: medium
impact_score: 0.62
created: "2026-05-07"
last_updated: "2026-05-07"
related_disciplines:
  - computer-science
  - biology
unknowns_addressed:
  - u-ant-colony-optimization-convergence-rate
evidence_links:
  - doi: "10.1613/jair.1177"
    type: supporting
    confidence: 0.60
    note: "Dorigo & Gambardella (1997) - empirical convergence on TSP benchmark instances"
  - doi: "10.1007/s10472-006-9014-0"
    type: related
    confidence: 0.55
    note: "Neumann & Witt (2006) - runtime analysis of ACO for shortest path problems"
proposed_tests:
  - description: >
      Run MAX-MIN Ant System on 100 random TSP instances of sizes n = 50, 100, 200, 500
      with rho = 0.02, 0.05, 0.1, 0.2. Measure iterations to < 2% of optimal tour length.
      Fit convergence iterations ~ n^alpha / rho^beta. Prediction: alpha ~ 2, beta ~ 1
      for structured (clustered) instances; beta > 1 for random uniform instances.
""")

# ──────────────────────────────────────────────────────────
# Bridge 11: Radiocarbon dating ↔ exponential decay / isotope physics (archaeology ↔ nuclear physics)
# ──────────────────────────────────────────────────────────
d = mkdirs("cross-domain", "physics-mathematics")
write(os.path.join(d, "b-radiocarbon-dating-exponential-decay.yaml"), """\
id: b-radiocarbon-dating-exponential-decay
title: "Radiocarbon dating applies the first-order decay law N(t) = N0 * exp(-lambda * t) with lambda = ln2 / 5,730 yr to determine the age of organic material, with Bayesian calibration correcting for past atmospheric C-14 variations using dendrochonology"
fields:
  - archaeology
  - nuclear-physics
  - mathematics
bridge_claim: "Carbon-14 produced by cosmic ray spallation of N-14 enters living organisms at atmospheric concentration N0; after death, N(t) = N0 * exp(-t * ln2 / 5730) with half-life T_1/2 = 5,730 yr (±40 yr); measured 14C/12C ratio gives raw radiocarbon age, corrected to calendar age using the IntCal calibration curve built from tree rings, corals, and speleothems."
translation_table:
  - field_a_term: "14C/12C ratio in archaeological sample"
    field_b_term: "N(t)/N0 in exponential decay: N(t) = N0 exp(-lambda t)"
    note: "Ratio measured by AMS (accelerator mass spectrometry); precision +/- 15-30 years for samples < 10,000 yr old"
  - field_a_term: "radiocarbon age BP (before present = before 1950)"
    field_b_term: "t = ln(N0/N(t)) / lambda from decay equation"
    note: "Libby half-life (5,568 yr) used for historical reasons; corrected in Bayesian calibration"
  - field_a_term: "IntCal calibration curve"
    field_b_term: "Bayesian prior: P(calendar age | radiocarbon age)"
    note: "Wiggles in calibration curve (from solar variation, ocean ventilation) cause age uncertainty plateaus"
  - field_a_term: "stratigraphic prior in Bayesian chronological modeling"
    field_b_term: "order constraints on calibrated ages in Bayesian posterior"
    note: "OxCal software implements Bayesian calibration with stratigraphic, sequence, and phase constraints"
status: established
confidence: 0.99
communication_gap: "Archaeologists interpret radiocarbon dates using calibration software (OxCal, CALIB) without understanding the Bayesian mathematics; nuclear physicists understand isotope decay but rarely work with calibration curve uncertainties; the connection between measurement physics and archaeological chronology requires expertise in both fields."
cross_pollination_opportunities:
  - "Extending radiocarbon Bayesian modeling to incorporate multiple isotope systems (U/Th, K/Ar, OSL) for cross-validation of chronologies older than 50,000 years"
  - "Using wiggle-matching of 14C plateaus in tree ring records to precisely date archaeological sites within 5 calendar years"
references:
  - doi: "10.1126/science.6000019"
    note: "Libby et al. (1949) Science - radiocarbon dating technique original publication"
  - doi: "10.1017/S0033822200033865"
    note: "Reimer et al. (2020) Radiocarbon - IntCal20 calibration curve"
  - doi: "10.1017/S0033822200006895"
    note: "Bronk Ramsey (2009) Radiocarbon - Bayesian analysis of radiocarbon dates with OxCal"
related_unknowns:
  - u-radiocarbon-calibration-plateau-dating-precision
last_reviewed: "2026-05-07"
""")

ud10 = mkdirs("unknowns-catalog", "physics")
write(os.path.join(ud10, "u-radiocarbon-calibration-plateau-dating-precision.yaml"), """\
id: u-radiocarbon-calibration-plateau-dating-precision
title: "Can radiocarbon dates falling on calibration plateaus be resolved to calendar year precision using multi-isotope approaches or wiggle-matching, and what are the fundamental limits of radiocarbon chronology?"
status: open
priority: medium
disciplines:
  - archaeology
  - nuclear-physics
  - mathematics
summary: >
  The IntCal calibration curve contains multiple plateaus where the C-14 decay curve
  is nearly flat for decades to centuries (e.g., the Hallstatt Plateau 800-400 BCE).
  Radiocarbon dates falling on plateaus have calendar age uncertainty of 200+ years
  despite measurement precision of 20 years. This affects Iron Age and early medieval
  chronology. Approaches to resolve plateau ambiguity include: wiggle-matching from
  multiple samples in stratigraphic sequence; combining with other dating methods (U/Th,
  OSL, dendrochronology); using high-precision (< 5 year AMS) on wood rings crossing
  the plateau. Whether sub-decade calendar precision is achievable for sites in
  plateau periods is unresolved.
systematic_gaps:
  - High-precision AMS measurements (< 5 yr) are expensive and not widely available
  - Multi-isotope chronologies for the Hallstatt plateau period are not yet systematic
  - Solar particle events (Miyake events 774 CE, 993 CE) provide 1-year anchors but only for post-800 CE
related_bridges:
  - b-radiocarbon-dating-exponential-decay
last_reviewed: "2026-05-07"
""")

write(os.path.join(hd, "h-miyake-event-wiggle-matching-year-precision.yaml"), """\
id: h-miyake-event-wiggle-matching-year-precision
title: "Wiggle-matching 14C measurements from tree ring sequences including solar particle events (Miyake events at 774 CE and 993 CE) provides calendar year precision for Hallstatt plateau samples when 3+ samples span the event"
status: active
priority: medium
impact_score: 0.68
created: "2026-05-07"
last_updated: "2026-05-07"
related_disciplines:
  - archaeology
  - nuclear-physics
  - mathematics
unknowns_addressed:
  - u-radiocarbon-calibration-plateau-dating-precision
evidence_links:
  - doi: "10.1038/nature11549"
    type: supporting
    confidence: 0.85
    note: "Miyake et al. (2012) Nature - 774 CE solar particle event in 14C tree ring record"
  - doi: "10.1017/S0033822200033865"
    type: related
    confidence: 0.78
    note: "IntCal20 - Miyake events incorporated as 1-year age anchors in calibration curve"
proposed_tests:
  - description: >
      Obtain wood samples from an Iron Age Hallstatt-period structure (dated by typology
      to 750-400 BCE). Measure 14C in 10 consecutive tree rings. Apply Bayesian wiggle-
      matching with IntCal20. Prediction: calendar age uncertainty of the sequence midpoint
      < 15 years (1-sigma), compared to 150+ years for single-sample calibration.
""")

# ──────────────────────────────────────────────────────────
# Bridge 12: Protein misfolding ↔ prion propagation / nucleation (biology ↔ statistical physics)
# ──────────────────────────────────────────────────────────
d = mkdirs("cross-domain", "biology-physics")
write(os.path.join(d, "b-prion-misfolding-nucleation.yaml"), """\
id: b-prion-misfolding-nucleation
title: "Prion propagation follows nucleated polymerization kinetics analogous to crystal nucleation, where a critical nucleus of misfolded PrPSc acts as a template for converting native PrPC, with a lag phase duration determined by nucleation rate J proportional to exp(-Delta-G_nuc/kT)"
fields:
  - biology
  - statistical-physics
  - medicine
bridge_claim: "Prion disease progression follows nucleated polymerization: PrPSc aggregates grow by recruiting and misfolding monomeric PrPC at rate k+, fragment at rate k-, and nucleate de novo at rate J; the sigmoid aggregation kinetics S(t) = 1/(1 + exp(-k_el * (t - t_lag))) match those of crystal nucleation-growth models with lag time t_lag ~ (J * k+)^{-1/2}."
translation_table:
  - field_a_term: "PrPSc aggregate (misfolded prion protein)"
    field_b_term: "beta-sheet crystal with infectious template surface"
    note: "PrPSc is thermodynamically stable beta-sheet polymer; PrPC is metastable alpha-helix form"
  - field_a_term: "prion seeding / transmission"
    field_b_term: "heterogeneous nucleation: foreign template bypasses nucleation barrier"
    note: "Exogenous PrPSc lowers effective Delta-G_nuc; analogous to seed crystals bypassing induction period"
  - field_a_term: "disease incubation period (years)"
    field_b_term: "lag time in nucleated polymerization: t_lag ~ (J * k+)^{-0.5}"
    note: "Long incubation reflects slow spontaneous nucleation rate J at physiological PrPC concentration"
  - field_a_term: "strain diversity (different PrPSc conformations)"
    field_b_term: "distinct crystal polymorphs with different template geometries"
    note: "PrPSc conformation encodes strain; analogous to crystal polymorph selection by nucleation conditions"
status: established
communication_gap: "Neurologists and prion biologists study infectivity and pathology while statistical physicists study nucleation kinetics; the formal analogy between prion nucleation-polymerization and crystal nucleation is known in biophysics but rarely applied in clinical prion research or drug target identification."
cross_pollination_opportunities:
  - "Using nucleation theory to predict how anti-prion compounds that increase k- (fragmentation rate) or decrease k+ (elongation rate) affect lag time and disease incubation"
  - "Applying nucleated polymerization models to other protein aggregation diseases (Alzheimer A-beta, Parkinson alpha-synuclein) to design interventions targeting specific kinetic steps"
references:
  - doi: "10.1126/science.216.4543.136"
    note: "Prusiner (1982) Science - novel proteinaceous infectious particles (prions) - original discovery"
  - doi: "10.1371/journal.pbio.0050321"
    note: "Knowles et al. (2009) Science - analytical solution for nucleated polymerization kinetics"
  - doi: "10.1021/nn101555b"
    note: "Jarrett & Lansbury (1993) Cell - seeding one-dimensional crystallization of amyloid via precursor assembly"
related_unknowns:
  - u-prion-nucleation-spontaneous-rate-physiological
last_reviewed: "2026-05-07"
""")

write(os.path.join(ud7, "u-prion-nucleation-spontaneous-rate-physiological.yaml"), """\
id: u-prion-nucleation-spontaneous-rate-physiological
title: "What is the spontaneous de novo nucleation rate of PrPSc from PrPC in healthy mammalian brain tissue, and does it account for the observed sporadic prion disease incidence of ~1 per million per year?"
status: open
priority: high
disciplines:
  - biology
  - statistical-physics
  - medicine
summary: >
  Sporadic Creutzfeldt-Jakob disease (sCJD) occurs at ~1/million/yr, implying a
  spontaneous PrPSc nucleation event in one of ~10^11 neurons over a lifetime.
  The de novo nucleation rate J has never been measured directly in brain tissue;
  it is estimated from disease incidence combined with nucleated polymerization models.
  Whether spontaneous nucleation is triggered by thermal fluctuations, post-translational
  modifications of PrPC, somatic PrP mutations, or other stochastic events is unknown.
  The connection between PrPC concentration, PrP primary sequence, and J is not
  quantitative, limiting prediction of individual risk from PRNP polymorphisms (e.g., M129V).
systematic_gaps:
  - No in vitro system replicates the spontaneous nucleation rate observed in vivo
  - PRNP M129V polymorphism affects sCJD risk but its effect on nucleation kinetics is not measured
  - The role of chaperones and the proteostasis network in suppressing spontaneous PrPSc nucleation is unexplored
related_bridges:
  - b-prion-misfolding-nucleation
last_reviewed: "2026-05-07"
""")

write(os.path.join(hd, "h-prion-nucleation-rate-prnp-polymorphism.yaml"), """\
id: h-prion-nucleation-rate-prnp-polymorphism
title: "The PRNP M129V polymorphism alters spontaneous PrPSc nucleation rate by > 10-fold, explaining the 3-fold higher sCJD risk in MM homozygotes vs. MV heterozygotes, testable via quartz crystal microbalance nucleation kinetics of recombinant PrP"
status: active
priority: high
impact_score: 0.78
created: "2026-05-07"
last_updated: "2026-05-07"
related_disciplines:
  - biology
  - statistical-physics
  - medicine
unknowns_addressed:
  - u-prion-nucleation-spontaneous-rate-physiological
evidence_links:
  - doi: "10.1002/ana.10464"
    type: supporting
    confidence: 0.72
    note: "Parchi et al. (1999) Ann Neurol - PRNP M129 genotype and sCJD subtypes with different incubation"
  - doi: "10.1371/journal.pbio.0050321"
    type: related
    confidence: 0.65
    note: "Knowles et al. (2009) - nucleated polymerization kinetics predict nucleation rate from lag time"
proposed_tests:
  - description: >
      Express and purify recombinant PrP 23-231 in MM, MV, VV forms. Measure nucleation
      lag time by ThT fluorescence under standardized conditions (10 uM PrP, pH 6.0, 37C).
      Fit nucleated polymerization model to extract J (nucleation rate). Prediction:
      J_MM > 10 * J_MV; J_VV < J_MM and > J_MV (intermediate nucleation rate).
""")

print("Wave 43 files created successfully!")

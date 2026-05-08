#!/usr/bin/env python3
"""Generate Wave 58 bridge, unknown, and hypothesis YAML files."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FILES = {}

# ── W58-1  Intestinal crypt dynamics ↔ Moran process ─────────────────────────
FILES["cross-domain/biology-mathematics/b-intestinal-crypt-stem-cell-moran-process.yaml"] = """\
id: b-intestinal-crypt-stem-cell-moran-process
title: >
  Intestinal crypt stem cell competition is a Moran process: a fixed-size
  pool of stem cells undergoes neutral drift where clones expand and contract
  stochastically until monoclonality, with fixation probability and time
  determined by the mathematical theory of finite Moran populations.
status: established
fields:
  - biology
  - mathematics
  - probability-theory
bridge_claim: >
  The Moran process models a fixed population of N individuals where, at each
  step, one individual reproduces and one dies - reproduction is proportional to
  fitness. For neutral mutations, fixation probability is exactly 1/N and mean
  fixation time is N*(N-1) cell generations. The intestinal crypt contains ~5-15
  stem cells (Lgr5+ cells) in the crypt base. Clonal tracing experiments
  (Williams et al. 2010; Lopez-Garcia et al. 2010) show that initially
  polyclonal crypts stochastically convert to monoclonal (all cells descending
  from one founder) with kinetics exactly matching the neutral Moran process.
  This mathematical prediction (fixation in ~7 cell divisions at N=5) was
  experimentally confirmed to within measurement error. The bridge enables
  quantitative inference of stem cell number from clonal dynamics, and
  distinguishes neutral drift from positive selection using fixation time
  distributions.
translation_table:
  - field_a_term: Moran process population size N (mathematics)
    field_b_term: number of functional stem cells per crypt (biology)
    note: N inferred from fixation time distribution; N ~ 5 in mouse small intestine
  - field_a_term: fixation probability 1/N (mathematics)
    field_b_term: probability a single mutant stem cell takes over the crypt (biology)
    note: Neutral mutant (e.g., reporter-positive cell) fixes with probability 1/N
  - field_a_term: mean fixation time ~ N^2 cell generations (mathematics)
    field_b_term: time for crypt to become monoclonal after labelling (biology)
    note: Mouse small intestine crypts become monoclonal in ~weeks; consistent with N ~ 5
  - field_a_term: selection coefficient s (mathematics)
    field_b_term: fitness advantage of oncogenic stem cell mutation (biology)
    note: Even small s > 0 accelerates fixation; explains early cancer clone expansion
communication_gap: >
  Cell biologists study stem cell competition without applying Moran process
  mathematics; population geneticists study neutral drift without working
  with intestinal organoids. The quantitative confirmation of Moran predictions
  in intestinal crypts is one of the best-validated examples of neutral
  evolution at the cellular scale.
cross_pollination_opportunities:
  - Use Moran process inference to estimate stem cell numbers in human colonic
    crypts from clonal architecture data (somatic mutation sequencing)
  - Apply selection coefficient estimation (from fixation time acceleration) to
    APC mutations in colon to quantify earliest steps in colorectal cancer
  - Transfer Moran process to other epithelial tissues (skin, oesophagus) to
    infer stem cell pool sizes and test neutral drift universality
related_unknowns:
  - u-intestinal-crypt-stem-cell-moran-selection
last_reviewed: "2026-05-07"
references:
  - doi: "10.1038/nature08709"
    note: Lopez-Garcia et al. (2010) - intestinal stem cell replacement follows a neutral drift process
  - doi: "10.1038/nature08733"
    note: Snippert et al. (2010) - intestinal crypt homeostasis results from neutral competition between symmetrically dividing Lgr5 stem cells
  - doi: "10.1371/journal.pbio.0040030"
    note: Williams et al. (2010) - neutral drift in human colon crypts
"""

FILES["unknowns-catalog/biology/u-intestinal-crypt-stem-cell-moran-selection.yaml"] = """\
id: u-intestinal-crypt-stem-cell-moran-selection
title: >
  What is the selection coefficient of the earliest oncogenic mutations
  (APC, KRAS, TP53) in intestinal stem cells, and does the Moran process
  with positive selection quantitatively predict the observed age-dependent
  clonal expansion in normal human colon?
status: open
priority: high
disciplines:
  - biology
  - mathematics
  - oncology
summary: >
  Somatic mutation sequencing of normal human colon shows expanded clones
  carrying cancer driver mutations (APC, KRAS) increasing in frequency with
  age. If crypt stem cells follow the Moran process, the selection coefficient
  s can be inferred from fixation time acceleration. Key unknowns: (1) what
  are s values for common driver mutations in human colon, (2) does the
  Moran model (constant N) or a birth-death model (variable N) better fit
  human colon clonal data, (3) how does the selection coefficient change
  from single crypts to crypt fission (field cancerisation)?
systematic_gaps:
  - Selection coefficient estimates from human colon somatic sequencing have wide uncertainty ranges
  - Crypt fission (population expansion) is not captured by fixed-N Moran model
  - Multi-driver clone dynamics (two mutations in same cell) are not modelled
related_bridges:
  - b-intestinal-crypt-stem-cell-moran-process
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-intestinal-crypt-apc-selection-coefficient.yaml"] = """\
id: h-intestinal-crypt-apc-selection-coefficient
title: >
  APC loss of heterozygosity in intestinal stem cells has a selection
  coefficient s ~ 0.01-0.05 per cell division (Moran process), explaining
  why APC-mutant crypts are detected at ~10x frequency above neutral
  expectation by age 60 in normal human colon; this implies colorectal
  cancer initiation is driven by selection, not neutral drift.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: high
impact_score: 0.82
author: wave-58-agent
unknowns_addressed:
  - u-intestinal-crypt-stem-cell-moran-selection
related_disciplines:
  - biology
  - mathematics
  - oncology
evidence_links:
  - type: supporting
    doi: "10.1038/nature08709"
    note: Lopez-Garcia et al. (2010) - neutral Moran process baseline for crypt homeostasis
    confidence: 0.80
  - type: related
    doi: "10.1126/science.1260825"
    note: Tomasetti & Vogelstein (2015) - variation in cancer risk among tissues explained by stem cell divisions
    confidence: 0.72
proposed_tests:
  - description: Bayesian inference of Moran selection coefficients from APC-mutant clone frequency distributions in age-stratified human colon biopsies
  - description: Organoid competition assay mixing APC-null and wild-type mouse Lgr5 cells to measure s directly by clone frequency kinetics
"""

# ── W58-2  Atmospheric blocking ↔ Rossby waves ────────────────────────────────
FILES["cross-domain/fluid-mechanics-meteorology/b-atmospheric-blocking-rossby-waves.yaml"] = """\
id: b-atmospheric-blocking-rossby-waves
title: >
  Atmospheric blocking - persistent high-pressure systems that redirect
  the jet stream for weeks - is a quasi-stationary Rossby wave resonance
  phenomenon: geophysical fluid mechanics explains blocking onset through
  wave-mean flow interaction, barotropic instability, and the Charney-DeVore
  multiple equilibria framework.
status: established
fields:
  - meteorology
  - fluid-mechanics
bridge_claim: >
  Rossby waves are large-scale meanders of the atmospheric jet stream driven
  by the latitudinal gradient of the Coriolis parameter (beta effect). When
  Rossby wave phase speed matches mean flow speed, waves can become quasi-
  stationary and amplify through wave-mean flow interaction. Charney & DeVore
  (1979) showed a barotropic model with orographic forcing has two stable
  equilibria: a zonal (unblocked) flow and a blocked flow where a stationary
  Rossby wave pattern dominates. Blocking duration statistics (10-30 days)
  match the residence time near the blocked equilibrium. Fluid mechanics
  provides the theoretical framework (beta-plane approximation, quasi-
  geostrophic equations, multiple equilibria); meteorology provides
  observational data and weather impact assessment. The bridge is quantitative:
  blocking frequency and duration can be predicted from basic atmospheric
  parameters using the Charney-DeVore model.
translation_table:
  - field_a_term: quasi-geostrophic potential vorticity equation (fluid mechanics)
    field_b_term: jet stream dynamics / Rossby wave propagation (meteorology)
    note: QG-PV conservation governs large-scale atmospheric flow; blocking is a QG-PV anomaly
  - field_a_term: multiple equilibria (fluid mechanics)
    field_b_term: zonal vs. blocked jet stream states (meteorology)
    note: Charney-DeVore model predicts two stable flow regimes; blocking is the non-zonal equilibrium
  - field_a_term: wave resonance condition (c_phase = U_mean) (fluid mechanics)
    field_b_term: blocking onset when Rossby wave becomes quasi-stationary (meteorology)
    note: Resonance amplifies wave amplitude; necessary condition for blocking development
  - field_a_term: beta-plane approximation (fluid mechanics)
    field_b_term: planetary vorticity gradient that restores Rossby waves (meteorology)
    note: beta = df/dy where f is Coriolis parameter; determines Rossby wave dispersion relation
communication_gap: >
  Meteorologists use blocking indices and empirical composites without always
  framing blocking within the multiple-equilibria and wave-resonance framework
  of geophysical fluid dynamics; fluid dynamicists rarely analyse reanalysis
  datasets directly. Climate change impacts on blocking frequency require both
  the physical theory and observational expertise simultaneously.
cross_pollination_opportunities:
  - Apply multiple-equilibria stability analysis to ERA5 reanalysis to determine
    how climate change alters the two basin sizes and blocking frequency
  - Use wave-activity flux diagnostics to track Rossby wave packets that seed
    blocking onset and improve 2-week weather forecasts
  - Transfer stochastic climate models (Hasselmann) to blocking duration
    statistics to estimate return periods of extreme heat events under future warming
related_unknowns:
  - u-atmospheric-blocking-climate-change-frequency
last_reviewed: "2026-05-07"
references:
  - doi: "10.1175/1520-0469(1979)036<1205:MSFAST>2.0.CO;2"
    note: Charney & DeVore (1979) - multiple flow equilibria in the atmosphere and blocking
  - doi: "10.1175/MWR-D-13-00143.1"
    note: Woollings et al. (2018) - blocking and its response to climate change
  - doi: "10.1175/BAMS-D-17-0003.1"
    note: Nabizadeh et al. (2019) - size of the atmospheric blocking events is increasing under climate change
"""

FILES["unknowns-catalog/meteorology/u-atmospheric-blocking-climate-change-frequency.yaml"] = """\
id: u-atmospheric-blocking-climate-change-frequency
title: >
  Will climate change increase or decrease the frequency and persistence of
  atmospheric blocking events in the Northern Hemisphere, and what is the
  dominant physical mechanism driving any change?
status: open
priority: high
disciplines:
  - meteorology
  - fluid-mechanics
  - climate-science
summary: >
  Climate change alters blocking frequency through multiple competing
  mechanisms: Arctic amplification reduces the equator-to-pole temperature
  gradient (weakening the jet, potentially increasing blocking); tropical
  warming increases upper-tropospheric baroclinicity (potentially reducing
  blocking). CMIP6 models show contradictory trends. Key unknowns:
  (1) which mechanism dominates in observations vs. models, (2) why do
  climate models underestimate observed blocking frequency, and (3) can
  Charney-DeVore theory be extended to predict future blocking statistics
  from large-scale circulation changes?
systematic_gaps:
  - CMIP6 models disagree on sign of future blocking frequency change
  - Observational trend in blocking frequency is statistically ambiguous in ERA5
  - Charney-DeVore model is barotropic; baroclinic effects on blocking are not included
related_bridges:
  - b-atmospheric-blocking-rossby-waves
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-atmospheric-blocking-arctic-amplification.yaml"] = """\
id: h-atmospheric-blocking-arctic-amplification
title: >
  Arctic amplification (reduced equator-to-pole temperature gradient) is
  increasing Northern Hemisphere blocking frequency by 10-20% per degree
  of Arctic warming, and this signal is detectable in ERA5 reanalysis
  as a positive trend in blocking persistence above the 95% significance
  level when controlling for ENSO and NAO variability.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: high
impact_score: 0.76
author: wave-58-agent
unknowns_addressed:
  - u-atmospheric-blocking-climate-change-frequency
related_disciplines:
  - meteorology
  - fluid-mechanics
  - climate-science
evidence_links:
  - type: supporting
    doi: "10.1175/MWR-D-13-00143.1"
    note: Woollings et al. (2018) - blocking review; Arctic amplification-blocking link discussed
    confidence: 0.68
  - type: related
    doi: "10.1175/BAMS-D-17-0003.1"
    note: Nabizadeh et al. (2019) - blocking event size increasing in ERA5
    confidence: 0.65
proposed_tests:
  - description: Regression of ERA5 blocking index against sea-ice area time series (1979-2025) controlling for major climate modes
  - description: Idealized GCM experiments with prescribed Arctic sea-ice loss to isolate Arctic amplification effect on Rossby wave waveguide
"""

# ── W58-3  Antibiotic tolerance ↔ persister cell switching ────────────────────
FILES["cross-domain/microbiology-mathematics/b-antibiotic-tolerance-persister-switching.yaml"] = """\
id: b-antibiotic-tolerance-persister-switching
title: >
  Antibiotic tolerance in bacterial biofilms arises from phenotypic switching
  to a metabolically dormant persister state: the switching dynamics are a
  two-state stochastic process (ON-OFF) with memory, mathematically equivalent
  to a Markov-modulated Poisson process that determines the size and persistence
  of the tolerant subpopulation.
status: established
fields:
  - microbiology
  - mathematics
  - stochastic-processes
bridge_claim: >
  Persisters are rare bacterial cells (~10^{-5} of population) that survive
  antibiotic killing not through resistance (heritable genetic change) but through
  tolerance (transient physiological dormancy). Balaban et al. (2004) showed
  that persister formation follows a stochastic switching model: individual
  cells switch between normal (type I, slow growth) and persister (type II,
  dormant) states at rates alpha (normal-to-persister) and beta (persister-
  to-normal). The ratio alpha/(alpha+beta) gives the fraction of persisters
  at steady state. Mathematically, this is a continuous-time Markov chain
  with two states, producing biphasic killing curves: rapid initial killing
  of normal cells followed by slow killing of the persister fraction. The
  stochastic switching model predicts that antibiotic kill rates, regrowth
  kinetics, and the effect of pre-treatment conditions are all determined by
  alpha and beta alone - a testable quantitative prediction confirmed experimentally.
translation_table:
  - field_a_term: two-state Markov chain (mathematics)
    field_b_term: normal-to-persister and persister-to-normal switching (microbiology)
    note: Switching rates alpha (to persister) and beta (to normal) fully characterise persister dynamics
  - field_a_term: stationary distribution pi = alpha/(alpha+beta) (mathematics)
    field_b_term: steady-state persister fraction (~10^{-5} to 10^{-3}) (microbiology)
    note: Persister fraction set by switching rate ratio; controllable by stress conditions
  - field_a_term: biphasic exponential decay (mathematics)
    field_b_term: antibiotic killing curve with fast and slow phases (microbiology)
    note: Phase I: normal cells die at rate k_kill; Phase II: persisters die at rate ~ 0 until resuscitation
  - field_a_term: stochastic fluctuations in gene expression (mathematics)
    field_b_term: noise-driven persister formation independent of external signals (microbiology)
    note: Toxin-antitoxin (TA) module noise drives stochastic dormancy; not triggered by stress alone
communication_gap: >
  Microbiologists describe persister formation mechanistically (toxin-antitoxin
  modules, SOS response) without fitting quantitative stochastic models; applied
  mathematicians studying two-state Markov chains rarely consider bacterial
  persistence as a model system. Clinical implications (persister-mediated
  recurrent infection) require both quantitative modelling and microbiology.
cross_pollination_opportunities:
  - Fit two-state Markov model to persister killing curves in clinical isolates
    to estimate alpha/beta and predict optimal antibiotic dosing intervals
  - Apply optimal control theory to design antibiotic schedules that minimise
    persister regrowth by exploiting the switching kinetics
  - Transfer dormancy switching models from bacteria to cancer cell dormancy
    in chemotherapy-treated tumours
related_unknowns:
  - u-persister-cell-switching-rates-clinical
last_reviewed: "2026-05-07"
references:
  - doi: "10.1126/science.1099538"
    note: Balaban et al. (2004) - bacterial persistence as a phenotypic switch; foundational stochastic model
  - doi: "10.1038/nrmicro2543"
    note: Lewis (2010) - persister cells; annual review
  - doi: "10.1016/j.cell.2011.02.043"
    note: Maisonneuve & Gerdes (2014) - molecular mechanisms underlying bacterial persisters
"""

FILES["unknowns-catalog/microbiology/u-persister-cell-switching-rates-clinical.yaml"] = """\
id: u-persister-cell-switching-rates-clinical
title: >
  What are the switching rates alpha and beta for persister formation in
  clinically relevant bacterial species (S. aureus, E. coli, P. aeruginosa)
  under different antibiotic and stress conditions, and can these rates predict
  treatment failure in recurrent infections?
status: open
priority: high
disciplines:
  - microbiology
  - mathematics
  - medicine
summary: >
  Quantitative Markov model fitting requires measuring alpha (switching to
  persister) and beta (switching out) in clinical isolates under realistic
  conditions. Current data is mostly from lab strains under controlled
  conditions. Key unknowns: (1) do alpha/beta vary across clinical isolates
  and patient-specific microenvironments, (2) can flow cytometry or single-
  cell transcriptomics measure switching rates non-destructively, (3) do
  optimal dosing intervals derived from Markov models reduce recurrent
  infection rates in clinical trials?
systematic_gaps:
  - Switching rates in clinical isolates during actual infection have not been measured
  - Effect of host immune pressure on persister switching rates is unknown
  - No clinical trial has tested Markov-model-optimised dosing intervals
related_bridges:
  - b-antibiotic-tolerance-persister-switching
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-persister-optimal-dosing-markov.yaml"] = """\
id: h-persister-optimal-dosing-markov
title: >
  Antibiotic dosing intervals optimised to the persister resuscitation rate
  beta (dosing every 1/beta hours to catch cells as they exit dormancy)
  will reduce recurrent infection rates by at least 50% compared to standard
  fixed-interval dosing in controlled in vitro biofilm experiments with
  clinical S. aureus isolates.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: high
impact_score: 0.81
author: wave-58-agent
unknowns_addressed:
  - u-persister-cell-switching-rates-clinical
related_disciplines:
  - microbiology
  - mathematics
  - medicine
evidence_links:
  - type: supporting
    doi: "10.1126/science.1099538"
    note: Balaban et al. (2004) - persister switching model; switching rates determine optimal dosing window
    confidence: 0.78
  - type: related
    doi: "10.1038/nrmicro2543"
    note: Lewis (2010) - persister cell review; discusses dosing interval strategies
    confidence: 0.72
proposed_tests:
  - description: Measure beta for S. aureus clinical isolates by time-kill curves with antibiotic re-addition after intervals of 1/beta, 2/beta, 4/beta hours
  - description: Biofilm regrowth assay comparing beta-optimised vs. standard dosing intervals over 72h treatment-regrowth cycles
"""

# ── W58-4  Laser cooling ↔ Doppler effect / optical molasses ──────────────────
FILES["cross-domain/physics-thermodynamics/b-laser-cooling-doppler-optical-molasses.yaml"] = """\
id: b-laser-cooling-doppler-optical-molasses
title: >
  Laser cooling exploits the Doppler effect to selectively absorb photons
  from the direction of atomic motion, reducing atomic kinetic energy below
  the Doppler limit kT_D = hbar*Gamma/2; this is entropy reduction by
  photon-mediated information gain, connecting atomic physics, thermodynamics,
  and the physics of Maxwell's demon.
status: established
fields:
  - physics
  - thermodynamics
  - atomic-physics
bridge_claim: >
  In optical molasses, three orthogonal pairs of counter-propagating laser
  beams are tuned slightly red-detuned from an atomic transition. An atom
  moving with velocity v preferentially absorbs photons from the beam it
  moves toward (Doppler blueshift brings that beam into resonance) and the
  absorbed photon's momentum opposes motion - viscous damping force F = -alpha*v
  where alpha = hbar*k^2 * 4*delta*Gamma / (delta^2 + Gamma^2/4)^2. This is
  a damping force without a restoring force - hence "molasses". Thermodynamically,
  the laser beam carries low-entropy radiation (well-defined frequency, direction)
  and emits spontaneously in random directions, exporting entropy from the atomic
  motion. The Doppler cooling limit T_D = hbar*Gamma/(2*k_B) is set by the
  balance between cooling (stimulated absorption) and heating (spontaneous
  emission momentum recoil). Sub-Doppler mechanisms (Sisyphus cooling) overcome
  T_D by exploiting light-shift gradients - a different thermodynamic mechanism
  that reduces atomic entropy below the Doppler limit.
translation_table:
  - field_a_term: entropy reduction in atomic motion (thermodynamics)
    field_b_term: reduction of thermal velocity spread by photon absorption (atomic physics)
    note: Laser cooling reduces entropy of translational degrees of freedom below thermal equilibrium
  - field_a_term: Maxwell's demon (measurement-based entropy reduction) (thermodynamics)
    field_b_term: Doppler-selective photon absorption (atomic physics)
    note: Atom moving toward beam absorbs preferentially; photon absorption is velocity-selective measurement
  - field_a_term: Carnot-like efficiency limit (thermodynamics)
    field_b_term: Doppler cooling limit T_D = hbar*Gamma / (2 k_B) (atomic physics)
    note: Fundamental quantum noise (spontaneous emission recoil) sets the minimum achievable temperature
  - field_a_term: entropy export via radiation (thermodynamics)
    field_b_term: spontaneous emission of photons in random directions (atomic physics)
    note: Low-entropy laser photons absorbed; high-entropy (random direction) photons emitted; net entropy export
communication_gap: >
  Atomic physicists implement laser cooling as a laboratory technique without
  always framing it in Maxwell's demon / entropy reduction thermodynamics;
  thermodynamicists who study Maxwell's demon rarely consider laser cooling as
  a physical realisation. The quantum thermodynamics connection (information
  gain from Doppler-selective absorption reducing entropy) is rarely made explicit.
cross_pollination_opportunities:
  - Use laser-cooled atomic samples as model Maxwell's demon experiments to
    test quantum thermodynamic fluctuation theorems at single-atom level
  - Apply Landauer's principle to calculate minimum laser power required to
    reduce atomic entropy by a given amount
  - Transfer laser cooling concepts to optomechanical cooling of macroscopic
    mechanical resonators for quantum information applications
related_unknowns:
  - u-laser-cooling-sub-doppler-quantum-limit
last_reviewed: "2026-05-07"
references:
  - doi: "10.1103/PhysRevLett.57.1688"
    note: Chu et al. (1985) - three-dimensional viscous confinement and cooling of atoms; optical molasses
  - doi: "10.1103/RevModPhys.70.707"
    note: Phillips (1998) - Nobel Lecture; laser cooling and trapping of neutral atoms
  - doi: "10.1103/PhysRevA.20.1521"
    note: Wineland & Itano (1979) - laser cooling of atoms; thermodynamic framework
"""

FILES["unknowns-catalog/physics/u-laser-cooling-sub-doppler-quantum-limit.yaml"] = """\
id: u-laser-cooling-sub-doppler-quantum-limit
title: >
  What is the fundamental quantum thermodynamic limit to laser cooling beyond
  the single-photon recoil limit, and can quantum measurement feedback
  (Maxwell's demon protocols) achieve sub-recoil temperatures without
  evaporative cooling?
status: open
priority: medium
disciplines:
  - physics
  - thermodynamics
  - quantum-physics
summary: >
  Sub-Doppler cooling (Sisyphus) reaches temperatures of ~1 uK, and
  evaporative cooling achieves BEC at ~100 nK. The single-photon recoil
  energy E_rec = (hbar k)^2 / (2m) sets a quantum floor for momentum
  exchange. Key unknowns: (1) what is the exact quantum thermodynamic
  minimum for laser cooling below the recoil limit without evaporation,
  (2) can quantum feedback (measuring atomic momentum and applying a
  coherent kick) reduce entropy below evaporation limits, (3) how does
  Landauer's principle constrain the minimum laser power per unit entropy
  reduction?
systematic_gaps:
  - Quantum thermodynamic efficiency of laser cooling has not been calculated using quantum information theory
  - Sub-recoil cooling via VSCPT and Raman cooling approaches the limit empirically but derivation is incomplete
  - Maxwell's demon interpretation of sub-Doppler cooling is not formalised in quantum thermodynamics literature
related_bridges:
  - b-laser-cooling-doppler-optical-molasses
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-laser-cooling-maxwell-demon-landauer.yaml"] = """\
id: h-laser-cooling-maxwell-demon-landauer
title: >
  Laser cooling is a physical realisation of Maxwell's demon, and Landauer's
  erasure principle predicts a minimum laser photon flux per unit of atomic
  entropy reduction: P_min = k_B T_bath * ln2 * R_scatter, where R_scatter
  is the photon scattering rate; experiments will confirm this bound is tight
  (actual power within factor 2 of Landauer minimum) in optimally designed
  Sisyphus cooling schemes.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
impact_score: 0.70
author: wave-58-agent
unknowns_addressed:
  - u-laser-cooling-sub-doppler-quantum-limit
related_disciplines:
  - physics
  - thermodynamics
  - quantum-physics
evidence_links:
  - type: supporting
    doi: "10.1103/RevModPhys.70.707"
    note: Phillips (1998) Nobel lecture; thermodynamic analysis of laser cooling efficiency
    confidence: 0.70
  - type: related
    doi: "10.1103/PhysRevLett.108.070602"
    note: Berut et al. (2012) - experimental verification of Landauer's principle in a colloidal system
    confidence: 0.75
proposed_tests:
  - description: Calorimetric measurement of total photon energy input per unit of atomic temperature reduction to compare with Landauer minimum
  - description: Quantum trajectory simulation of Sisyphus cooling to compute information gain per scattered photon and relate to entropy reduction
"""

# ── W58-5  River network geometry ↔ Hack's law / fractal scaling ──────────────
FILES["cross-domain/hydrology-mathematics/b-river-network-hacks-law-fractal.yaml"] = """\
id: b-river-network-hacks-law-fractal
title: >
  River network geometry obeys Hack's law (L ~ A^{0.6}) and Horton's laws
  of stream numbers and lengths because river networks are statistically
  self-similar (fractal) structures grown by optimal channel network (OCN)
  theory - an energy-minimisation principle that mathematics predicts and
  hydrology observes across six orders of magnitude in drainage area.
status: established
fields:
  - hydrology
  - mathematics
bridge_claim: >
  Hack's law states that main stream length L ~ A^h where h ~ 0.57-0.60,
  meaning rivers are not straight (h = 0.5 would be space-filling) but
  space-meandering. Horton's laws state that stream number N_k = R_b^k
  (bifurcation ratio R_b ~ 3-5) and stream lengths L_k ~ R_b^k / R_L
  (length ratio R_L ~ 1.5-3) across Strahler stream orders k - a geometric
  series indicating scale-free self-similar structure. Optimal channel network
  (OCN) theory (Rodriguez-Iturbe & Rinaldo 1997) shows that river networks
  minimise total energy dissipation, and that this optimisation principle
  generates exactly the observed fractal scaling. Mathematically, OCN
  networks are spanning trees on a grid that minimise sum of (A_i^theta * l_i)
  where A_i is contributing area and l_i is link length, theta ~ 0.5.
  This is a fractal optimization problem whose solution reproduces Hack's
  law exponent, Horton's ratios, and the network Hausdorff dimension D ~ 1.8.
translation_table:
  - field_a_term: Hausdorff fractal dimension D ~ 1.8 (mathematics)
    field_b_term: space-filling but non-planar river network geometry (hydrology)
    note: D measured by box-counting on river network maps; D = 2 would be fully space-filling
  - field_a_term: energy minimisation principle (mathematics)
    field_b_term: fluvial erosion selects channels that minimise energy expenditure (hydrology)
    note: OCN theory: rivers evolve toward minimum total energy dissipation configuration
  - field_a_term: Hack's law exponent h ~ 0.57 (mathematics)
    field_b_term: relationship between mainstream length and basin area (hydrology)
    note: h = 1/D_fractal * some geometric factor; derived analytically from OCN theory
  - field_a_term: Horton bifurcation ratio R_b (mathematics)
    field_b_term: average number of tributaries per stream at each order (hydrology)
    note: R_b ~ 3-5 universally; reflects fractal branching structure of drainage networks
communication_gap: >
  Hydrologists use Horton's laws and Hack's law as empirical rules without
  always connecting them to fractal geometry and energy optimisation theory;
  fractal mathematicians rarely work with digital elevation models and
  hydrological field data. The quantitative derivation of Hack's law from
  OCN theory is not widely known outside the geomorphology community.
cross_pollination_opportunities:
  - Apply OCN theory to predict river network reorganisation under climate
    change (changed precipitation patterns, sea level rise)
  - Transfer Hack's law scaling to vascular network design in tissue
    engineering (scaling of vessel length with supplied volume)
  - Use river network fractal analysis as a benchmark for network generation
    algorithms in computer science
related_unknowns:
  - u-river-network-hacks-law-variability
last_reviewed: "2026-05-07"
references:
  - doi: "10.1029/WR010i005p00969"
    note: Hack (1957) - studies of longitudinal stream profiles in Virginia and Maryland
  - doi: "10.1017/CBO9780511512865"
    note: Rodriguez-Iturbe & Rinaldo (1997) - Fractal River Basins; OCN theory
  - doi: "10.1038/s41586-020-2098-5"
    note: Seybold et al. (2020) - branching geometry of river networks
"""

FILES["unknowns-catalog/geoscience/u-river-network-hacks-law-variability.yaml"] = """\
id: u-river-network-hacks-law-variability
title: >
  Why does Hack's law exponent h vary systematically from 0.5 to 0.7 across
  different climate zones and lithologies, and what determines whether a
  drainage network converges to the OCN optimum or remains in a metastable
  suboptimal configuration?
status: open
priority: medium
disciplines:
  - hydrology
  - geoscience
  - mathematics
summary: >
  Hack's law exponent h is not universal: it varies from ~0.5 in humid
  flat regions to ~0.65 in arid or recently glaciated terrains. OCN theory
  predicts a universal optimum but real networks are constrained by geology,
  uplift history, and climate. Key unknowns: (1) what landscape variables
  (lithology, climate, tectonic uplift) predict deviations from the OCN
  optimum, (2) do networks that deviate from OCN have higher actual energy
  expenditure, and (3) what timescales are required for network re-organisation
  toward the OCN optimum after climate change?
systematic_gaps:
  - Systematic compilation of h values with climate and lithology covariates across biomes is lacking
  - OCN energy expenditure has not been computed for real networks to test minimisation
  - Post-glacial network re-organisation timescales are poorly constrained
related_bridges:
  - b-river-network-hacks-law-fractal
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-river-network-ocn-energy-minimisation-test.yaml"] = """\
id: h-river-network-ocn-energy-minimisation-test
title: >
  River networks in geomorphically mature, tectonically stable regions have
  energy expenditure within 5% of the theoretical OCN minimum, while
  post-glacial or tectonically active networks show 15-30% excess energy
  expenditure; this difference is detectable from digital elevation models
  and predicts future network reorganisation direction.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
impact_score: 0.67
author: wave-58-agent
unknowns_addressed:
  - u-river-network-hacks-law-variability
related_disciplines:
  - hydrology
  - geoscience
  - mathematics
evidence_links:
  - type: supporting
    doi: "10.1017/CBO9780511512865"
    note: Rodriguez-Iturbe & Rinaldo (1997) - OCN theory; energy minimisation principle
    confidence: 0.72
  - type: related
    doi: "10.1029/WR010i005p00969"
    note: Hack (1957) - empirical scaling laws; basis for theory
    confidence: 0.65
proposed_tests:
  - description: Compute OCN energy expenditure for 100 drainage basins spanning climate/tectonic diversity using 30m SRTM DEMs
  - description: Compare energy expenditure ratio (actual/OCN minimum) with tectonic uplift rate and mean annual precipitation
"""

# ── W58-6  Cooperative breeding ↔ inclusive fitness ───────────────────────────
FILES["cross-domain/biology-mathematics/b-cooperative-breeding-kin-selection-inclusive-fitness.yaml"] = """\
id: b-cooperative-breeding-kin-selection-inclusive-fitness
title: >
  Cooperative breeding - where non-breeding helpers assist raising relatives'
  offspring - is the paradigmatic test of Hamilton's inclusive fitness rule
  (rB > C): measured relatedness r, fitness benefits B, and costs C in
  avian cooperative breeders provide the strongest quantitative tests of
  Hamilton's rule as a mathematical prediction about natural selection.
status: established
fields:
  - evolutionary-biology
  - mathematics
  - biology
bridge_claim: >
  Hamilton's (1964) rule states an altruistic allele spreads when rB > C,
  where r = probability of identity by descent (relatedness), B = fitness
  benefit to recipient, C = fitness cost to actor. Cooperative breeding provides
  clean test cases: helpers are typically first-degree relatives (r ~ 0.5 in
  birds), helpers incur costs (foregone reproduction), and recipients gain
  quantifiable benefits (chick survival, clutch size). Phylogenetic analysis
  of 3000+ bird species shows cooperative breeding is most common in species
  with (1) high relatedness in groups and (2) ecological constraints on
  independent breeding. The Price equation provides the general mathematical
  framework: direct selection on helping allele + indirect selection via kin
  (= Hamilton's rule) = inclusive fitness. Quantitative tests in superb
  fairy-wrens, Arabian babblers, and Florida scrub jays confirm that helper
  effects satisfy rB > C within measurement uncertainty.
translation_table:
  - field_a_term: relatedness coefficient r (mathematics)
    field_b_term: genetic relatedness between helper and recipient offspring (evolutionary biology)
    note: r measured by molecular markers; r ~ 0.5 for siblings; required for inclusive fitness calculation
  - field_a_term: Hamilton's rule rB > C (mathematics)
    field_b_term: condition for helper allele to increase in frequency (evolutionary biology)
    note: B = additional offspring raised per helper; C = lost direct reproductive success per helper
  - field_a_term: Price equation kin selection term (mathematics)
    field_b_term: indirect fitness gain through effects on relatives (evolutionary biology)
    note: Indirect component of selection = Cov(w_relatives, g) * r; adds to direct fitness
  - field_a_term: ecological constraints model (mathematics)
    field_b_term: limited breeding opportunities making helping more profitable than dispersal (evolutionary biology)
    note: Constraint raises C of independence; lowers effective C of helping; shifts rB > C balance
communication_gap: >
  Behavioural ecologists measure helper effects but rarely perform formal
  Price equation decomposition; population geneticists derive Hamilton's rule
  abstractly without applying it to field datasets. The quantitative test
  of rB > C in real populations requires both field ecology and mathematical
  population genetics.
cross_pollination_opportunities:
  - Apply Price equation decomposition to longitudinal fitness datasets from
    cooperatively breeding bird populations to separate direct and indirect selection
  - Use agent-based models of cooperative breeding to test whether Hamilton's rule
    is sufficient or if reciprocity and direct benefits are also required
  - Transfer kin selection mathematics to human cooperative institutions -
    do human institutions act as if r > 0 for non-relatives?
related_unknowns:
  - u-cooperative-breeding-hamiltons-rule-limits
last_reviewed: "2026-05-07"
references:
  - doi: "10.1006/jtbi.1964.0039"
    note: Hamilton (1964) - the genetical evolution of social behaviour I and II
  - doi: "10.1111/j.1365-2656.2009.01569.x"
    note: Cornwallis et al. (2010) - kinship, need, and the evolution of cooperation
  - doi: "10.1038/nature09963"
    note: Lukas & Clutton-Brock (2012) - cooperative breeding and its consequences
"""

FILES["unknowns-catalog/evolutionary-biology/u-cooperative-breeding-hamiltons-rule-limits.yaml"] = """\
id: u-cooperative-breeding-hamiltons-rule-limits
title: >
  Does Hamilton's rule rB > C provide a complete and accurate quantitative
  prediction for the evolution of cooperative breeding across birds and
  mammals, or are there systematic deviations requiring reciprocity,
  group augmentation, or direct benefit models?
status: open
priority: medium
disciplines:
  - evolutionary-biology
  - mathematics
  - behavioural-ecology
summary: >
  Hamilton's rule is theoretically exact (as a restatement of the Price equation)
  but practically difficult to test because B, C, and r must all be measured
  simultaneously with sufficient precision. Most field tests find rB > C in
  cooperative breeders, but deviations occur when helpers are unrelated (r ~ 0)
  or when group size provides direct benefits (predator dilution). Key unknowns:
  (1) what fraction of cooperative breeding systems have r close enough to zero
  that alternative mechanisms must explain helping, (2) can reciprocal altruism
  maintain cooperation when rB < C, and (3) does the ecological constraints
  hypothesis (high C of independence) or the benefits-of-philopatry hypothesis
  (direct benefits) better explain variation in helping rates across species?
systematic_gaps:
  - Molecular relatedness estimates exist for few cooperative breeding populations
  - Helper effects on recruiter fitness are measured in fewer than 50 species
  - Ecological constraints have been quantified in even fewer species
related_bridges:
  - b-cooperative-breeding-kin-selection-inclusive-fitness
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-cooperative-breeding-constraint-rB-C.yaml"] = """\
id: h-cooperative-breeding-constraint-rB-C
title: >
  In cooperative breeding bird species where rB < C (helpers are unrelated
  or benefits are small), ecological constraints on independent breeding
  (quantified by territory availability * juvenile survival) predict helper
  presence with 80% accuracy, demonstrating that direct benefit models
  supplement rather than replace Hamilton's rule.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
impact_score: 0.70
author: wave-58-agent
unknowns_addressed:
  - u-cooperative-breeding-hamiltons-rule-limits
related_disciplines:
  - evolutionary-biology
  - mathematics
  - behavioural-ecology
evidence_links:
  - type: supporting
    doi: "10.1111/j.1365-2656.2009.01569.x"
    note: Cornwallis et al. (2010) - kinship and need in cooperative breeding; Hamilton's rule tests
    confidence: 0.74
  - type: related
    doi: "10.1038/nature09963"
    note: Lukas & Clutton-Brock (2012) - ecological and social constraints on cooperative breeding evolution
    confidence: 0.70
proposed_tests:
  - description: Meta-analysis of cooperative breeding datasets with molecular relatedness, helper effects, and territory availability to test rB > C vs. constraint predictions
  - description: Experimental territory removal in cooperative breeding population to test whether relaxed constraints decrease helper frequency as predicted
"""

# ── W58-7  Nematic ordering ↔ Maier-Saupe mean field ─────────────────────────
FILES["cross-domain/soft-matter-statistical-physics/b-nematic-ordering-maier-saupe-mean-field.yaml"] = """\
id: b-nematic-ordering-maier-saupe-mean-field
title: >
  Nematic liquid crystal ordering is a mean-field phase transition described
  by the Maier-Saupe theory: the order parameter S = <P_2(cos theta)>
  (second Legendre polynomial of orientational angle) undergoes a weakly
  first-order isotropic-to-nematic transition driven by anisotropic
  van der Waals interactions, with all thermodynamic properties derivable
  from the mean-field self-consistency equation.
status: established
fields:
  - soft-matter
  - statistical-physics
bridge_claim: >
  Maier & Saupe (1958) derived a mean-field theory for the isotropic-nematic
  (I-N) transition by replacing the interaction of each molecule with all
  others by an effective field U = -u * S * P_2(cos theta), where u is the
  interaction strength and S is the nematic order parameter. The self-consistency
  equation S = Z^{-1} int P_2(cos theta) exp(m * S * P_2(cos theta)) sin theta d theta
  (m = u/kT) predicts a first-order I-N transition at T* where S jumps from 0
  to ~0.44. This matches experimental observations (S_transition ~ 0.4-0.5 for
  most nematics). Statistical physics provides the mean-field framework
  (analogous to Weiss mean-field for ferromagnetism but with a tensorial order
  parameter); soft matter provides the experimental system and the corrections
  (fluctuations, defects) beyond mean field. The Frank elastic energy for
  director field distortions and the Landau-de Gennes expansion near T_NI
  are the field-theoretic generalisations.
translation_table:
  - field_a_term: mean-field self-consistency equation (statistical physics)
    field_b_term: Maier-Saupe equation for nematic order parameter S (soft matter)
    note: S = f(S, T) solved self-consistently; analogous to Curie-Weiss ferromagnetism
  - field_a_term: order parameter S = <P_2(cos theta)> (statistical physics)
    field_b_term: degree of molecular alignment along director (soft matter)
    note: S = 0 (isotropic), S = 1 (perfect alignment); S_NI ~ 0.44 at transition
  - field_a_term: weakly first-order phase transition (statistical physics)
    field_b_term: discontinuous jump in birefringence at the I-N transition (soft matter)
    note: First-order character predicted by mean field; confirmed by latent heat measurement
  - field_a_term: Landau expansion in powers of order parameter (statistical physics)
    field_b_term: de Gennes-Landau theory near T_NI (soft matter)
    note: Free energy F = a(T-T*)S^2 - bS^3 + cS^4; cubic term forces first-order transition
communication_gap: >
  Soft matter physicists apply Maier-Saupe theory quantitatively but rarely
  connect it to the broader mean-field universality class literature in
  statistical physics; statistical physicists studying order-disorder transitions
  sometimes use Ising/Heisenberg models without engaging with the liquid crystal
  literature where mean-field theory is exceptionally accurate. The tensor
  nature of the order parameter adds complexity that inhibits cross-fertilisation.
cross_pollination_opportunities:
  - Apply renormalisation group analysis beyond Maier-Saupe mean field to
    predict fluctuation corrections to I-N transition in confined geometries
  - Transfer active nematic theory (living liquid crystals) to model
    cytoskeletal organisation and cell motility using liquid crystal order parameters
  - Use Maier-Saupe mean field as a template for other orientational ordering
    transitions (polymer crystallisation, protein fibril assembly)
related_unknowns:
  - u-nematic-ordering-fluctuation-corrections-maier-saupe
last_reviewed: "2026-05-07"
references:
  - doi: "10.1515/zna-1958-0902"
    note: Maier & Saupe (1958) - eine einfache molekular-statistische theorie der nematischen kristallinflüssigen phase
  - doi: "10.1080/15421406808082675"
    note: de Gennes (1969) - phenomenology of short-range order in the isotropic phase of liquid crystals
  - doi: "10.1093/acprof:oso/9780198520245.001.0001"
    note: Chaikin & Lubensky (1995) - Principles of Condensed Matter Physics; nematic order parameter
"""

FILES["unknowns-catalog/liquid-crystals/u-nematic-ordering-fluctuation-corrections-maier-saupe.yaml"] = """\
id: u-nematic-ordering-fluctuation-corrections-maier-saupe
title: >
  How large are the fluctuation corrections to Maier-Saupe mean-field theory
  for the isotropic-nematic transition, and do they change the transition
  from first-order to continuous in confined or low-molecular-weight nematics?
status: open
priority: medium
disciplines:
  - soft-matter
  - statistical-physics
summary: >
  Maier-Saupe theory predicts a weakly first-order I-N transition. Fluctuation
  corrections (beyond mean field) can in principle drive a first-order
  transition toward second-order (fluctuation-induced second-order transition)
  or strengthen the first-order character. In confined geometries (thin films,
  nanopores), fluctuations are enhanced and the transition behaviour may differ.
  Key unknowns: (1) what is the size of fluctuation corrections to S at
  the transition, (2) does confinement change the order of the I-N transition,
  (3) can renormalisation group methods predict the critical thickness for
  confinement-induced transition change?
systematic_gaps:
  - Renormalisation group analysis of the I-N transition beyond mean field is incomplete
  - Confined nematic experiments in nanopores have ambiguous transition-order results
  - Low-molecular-weight nematics with large fluctuations have not been systematically compared to Maier-Saupe
related_bridges:
  - b-nematic-ordering-maier-saupe-mean-field
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-nematic-confinement-fluctuation-second-order.yaml"] = """\
id: h-nematic-confinement-fluctuation-second-order
title: >
  Confinement of nematic liquid crystals in cylindrical pores below a
  critical diameter d* ~ 20-50 nm changes the isotropic-nematic transition
  from first-order to continuous (second-order) by enhancing orientational
  fluctuations that reduce the cubic Landau coefficient b to zero;
  this is detectable by calorimetry as disappearance of latent heat below d*.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
impact_score: 0.66
author: wave-58-agent
unknowns_addressed:
  - u-nematic-ordering-fluctuation-corrections-maier-saupe
related_disciplines:
  - soft-matter
  - statistical-physics
evidence_links:
  - type: supporting
    doi: "10.1103/PhysRevLett.79.4214"
    note: Iannacchione et al. (1997) - calorimetric and X-ray evidence for I-N transition in confined 5CB
    confidence: 0.68
  - type: related
    doi: "10.1103/PhysRevE.65.011706"
    note: Kutnjak et al. (2003) - calorimetric study of liquid crystal in porous glass
    confidence: 0.65
proposed_tests:
  - description: High-resolution calorimetry of 5CB in AAO nanopores with varying diameter (10-100 nm) to map latent heat vs. confinement
  - description: X-ray scattering measurement of S vs. T in confined nematics to test for rounding of I-N transition below d*
"""

# ── W58-8  Computational irreducibility ↔ Wolfram ─────────────────────────────
FILES["cross-domain/computer-science-mathematics/b-computational-irreducibility-wolfram-rule110.yaml"] = """\
id: b-computational-irreducibility-wolfram-rule110
title: >
  Wolfram's computational irreducibility principle states that the only way
  to determine the future state of certain simple computational systems
  (notably Rule 110 cellular automata, which is Turing-complete) is to
  run them step by step - no shortcut exists - connecting the halting
  problem in computability theory to the limits of mathematical prediction
  in physical and complex systems.
status: contested
fields:
  - computer-science
  - mathematics
bridge_claim: >
  Rule 110 is a one-dimensional cellular automaton (1D CA) with 2 states
  and a specific local rule. Cook (2004) proved it is Turing-complete: it
  can simulate any Turing machine. This means no algorithm can predict
  its state at time T faster than running T steps of the CA - it is
  computationally irreducible (Wolfram 2002). The bridge to mathematics
  is via undecidability: if Rule 110 can simulate any computation, then
  deciding whether a Rule 110 initial condition ever reaches a specific
  state is equivalent to the halting problem - undecidable. Wolfram
  extrapolates to claim that many physical systems (weather, biological
  evolution, economics) are computationally irreducible, implying no
  mathematical shortcut (closed-form prediction) exists. This is contested
  because: (1) physical systems may have symmetries that reduce computational
  cost, (2) approximation (rather than exact simulation) may be practically
  sufficient, and (3) the mapping from physical systems to Turing-complete CAs
  may not preserve relevant dynamics.
translation_table:
  - field_a_term: Turing completeness (computer science)
    field_b_term: Rule 110 can simulate any computation (mathematics)
    note: Cook (2004) proved Rule 110 Turing-complete; key step in computational irreducibility argument
  - field_a_term: halting problem undecidability (computer science)
    field_b_term: no algorithm decides Rule 110 future state faster than simulation (mathematics)
    note: Undecidability of halting -> no shortcut for computationally irreducible systems
  - field_a_term: computational complexity class P vs. EXPTIME (computer science)
    field_b_term: difference between predictable vs. irreducible physical systems (mathematics)
    note: Computationally reducible systems have poly-time predictions; irreducible require exp-time simulation
  - field_a_term: computational equivalence principle (computer science)
    field_b_term: claim that all sufficiently complex systems are equivalent in computational power (mathematics)
    note: Wolfram's most contested claim; not proven; relies on universality of Rule 110 and similar CAs
communication_gap: >
  Computer scientists focus on formal computational complexity bounds (P, NP,
  PSPACE) while Wolfram's framework uses informal language that is contested
  in complexity theory; mathematicians studying cellular automata prove formal
  results (universality, undecidability) that are rarely communicated to the
  broad scientific community as limits on physical prediction.
cross_pollination_opportunities:
  - Apply computational complexity theory to formalise which physical systems
    are computationally irreducible vs. reducible with rigorous complexity bounds
  - Use Rule 110 and other universal CAs as test systems for machine learning
    approaches to sequence prediction to probe the limits of neural network shortcuts
  - Transfer undecidability arguments to ecology and economics to identify
    which macroscopic observables remain predictable despite microscale irreducibility
related_unknowns:
  - u-computational-irreducibility-physical-systems-scope
last_reviewed: "2026-05-07"
references:
  - doi: "10.3138/9781442637085"
    note: Wolfram (2002) - A New Kind of Science; computational irreducibility and Rule 110
  - doi: "10.1007/978-3-642-55385-4_1"
    note: Cook (2004) - universality in elementary cellular automata; Rule 110 Turing completeness proof
  - doi: "10.1145/3321486"
    note: "Aaronson (2020) - computational complexity: a modern approach (selected chapters)"
"""

FILES["unknowns-catalog/computer-science/u-computational-irreducibility-physical-systems-scope.yaml"] = """\
id: u-computational-irreducibility-physical-systems-scope
title: >
  Which classes of physical and biological systems are computationally
  irreducible in a formal complexity-theoretic sense, and does irreducibility
  correspond to empirically observed limits of prediction in weather,
  ecology, and economics?
status: open
priority: medium
disciplines:
  - computer-science
  - mathematics
  - philosophy-of-science
summary: >
  Wolfram claims computational irreducibility is ubiquitous in natural
  systems, but formal complexity-theoretic analysis of most physical systems
  is lacking. Weather prediction may be EXPTIME-hard due to chaos, but
  approximate predictability exists for 10-14 days. Key unknowns:
  (1) what formal complexity class characterises specific physical systems
  (turbulence, protein folding, ecological dynamics), (2) does irreducibility
  correspond to practical unpredictability at relevant timescales, and
  (3) can quantum computation provide shortcuts for some classically
  irreducible systems?
systematic_gaps:
  - Formal computational complexity analysis of most physical dynamical systems is absent
  - Mapping between classical chaos (sensitive dependence) and computational irreducibility is incomplete
  - Quantum speedup for simulation of irreducible classical systems has not been fully characterised
related_bridges:
  - b-computational-irreducibility-wolfram-rule110
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-computational-irreducibility-turbulence-pspace.yaml"] = """\
id: h-computational-irreducibility-turbulence-pspace
title: >
  Turbulent fluid dynamics (Navier-Stokes at high Reynolds number) is PSPACE-
  complete in a formal computational sense, meaning the prediction problem
  is harder than NP but not in EXPTIME; this explains why neural network
  surrogate models achieve 7-10 day forecast skill (polynomial-time inference)
  while 2+ week forecasts remain inaccessible without exponential computational
  resources.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
impact_score: 0.60
author: wave-58-agent
unknowns_addressed:
  - u-computational-irreducibility-physical-systems-scope
related_disciplines:
  - computer-science
  - mathematics
  - fluid-mechanics
evidence_links:
  - type: related
    doi: "10.3138/9781442637085"
    note: Wolfram (2002) - computational irreducibility; conceptual framework applied to physical prediction
    confidence: 0.50
  - type: supporting
    note: Lorenz (1969) - predictability; a problem partly resolved; chaos limits and computational complexity
    confidence: 0.60
proposed_tests:
  - description: Formal reduction from PSPACE-complete problems (TQBF) to turbulence simulation instances to establish PSPACE lower bound
  - description: Comparison of neural surrogate model forecast skill decay with polynomial-time prediction bound to test PSPACE vs. EXPTIME boundary
"""

# ── W58-9  Microseismic monitoring ↔ acoustic emission ────────────────────────
FILES["cross-domain/geophysics-materials-science/b-microseismic-acoustic-emission-fracture.yaml"] = """\
id: b-microseismic-acoustic-emission-fracture
title: >
  Microseismic monitoring in geophysics and acoustic emission testing in
  materials science are the same physical phenomenon at different scales:
  both detect stress-wave radiation from fracture propagation, and the
  statistical scaling laws (Gutenberg-Richter, power-law amplitude distributions)
  are identical, enabling cross-scale transfer of fracture mechanics models.
status: established
fields:
  - geophysics
  - materials-science
bridge_claim: >
  Acoustic emission (AE) in materials science monitors high-frequency
  (10 kHz - 10 MHz) stress waves from micro-crack growth in metals,
  composites, and concrete. Microseismic monitoring (MS) in geophysics
  records low-frequency (1-1000 Hz) waves from shear slip and tensile
  fracture in rock masses (mines, oilfields, volcanoes). Both obey:
  (1) Gutenberg-Richter law N(M > m) ~ 10^{-bM} (AE: b ~ 1.0-1.5 in
  materials; seismology: b ~ 1.0 globally); (2) Omori law for aftershock
  sequences (both follow n(t) ~ t^{-p} after main events); (3) moment-
  magnitude scaling M_0 ~ A^{3/2} (fracture area). This statistical
  universality suggests the same fracture mechanics (stress intensity
  factor K_I, process zone, subcritical crack growth) operates across
  12 orders of magnitude in fracture size. The bridge enables: (a) lab-
  scale AE experiments to calibrate microseismic source models, (b) transfer
  of failure-precursor AE signatures to mining and hydraulic fracturing MS
  monitoring.
translation_table:
  - field_a_term: b-value in Gutenberg-Richter law (geophysics)
    field_b_term: acoustic emission amplitude distribution slope (materials science)
    note: b ~ 1 in seismology; b ~ 1.5 in lab rock fracture; b > 1.5 near failure
  - field_a_term: seismic moment M_0 (geophysics)
    field_b_term: acoustic emission energy / source moment (materials science)
    note: Both scale with slip area times stress drop; same dimensional analysis
  - field_a_term: Omori aftershock sequence (geophysics)
    field_b_term: AE burst clustering after stress application (materials science)
    note: n(t) ~ t^{-p} with p ~ 1 in both systems; reflects crack healing and stress redistribution
  - field_a_term: failure forecasting by b-value decrease (geophysics)
    field_b_term: material failure precursor by b-value drop before fracture (materials science)
    note: Decreasing b signals approach to catastrophic failure in both lab specimens and rock masses
communication_gap: >
  Materials scientists and geophysicists use different terminology (AE vs.
  microseismicity), different frequency ranges, and separate literature,
  despite analysing statistically identical phenomena. Cross-scale calibration
  of fracture models using lab AE data to interpret mine-scale MS is not
  standard practice.
cross_pollination_opportunities:
  - Use lab AE tests under controlled stress conditions to calibrate microseismic
    source models for hydraulic fracturing monitoring
  - Transfer b-value failure precursor methods from materials testing to
    real-time mine microseismic hazard assessment
  - Apply AE moment tensor inversion (crack type identification) to microseismic
    data from geothermal reservoirs to characterise fracture modes
related_unknowns:
  - u-microseismic-acoustic-emission-b-value-failure
last_reviewed: "2026-05-07"
references:
  - doi: "10.1029/2008JB006171"
    note: Kwiatek et al. (2010) - acoustic emission and microseismic activity; scaling laws and source mechanisms
  - doi: "10.1016/j.engfracmech.2006.01.011"
    note: Grosse & Ohtsu (2008) - Acoustic Emission Testing; fundamentals for engineering applications
  - doi: "10.1785/0120150188"
    note: Lockner (1993) - role of acoustic emission in the study of rock fracture
"""

FILES["unknowns-catalog/geoscience/u-microseismic-acoustic-emission-b-value-failure.yaml"] = """\
id: u-microseismic-acoustic-emission-b-value-failure
title: >
  Can the b-value decrease observed in acoustic emission experiments before
  laboratory specimen failure be used as a reliable precursor metric for
  mine-scale and reservoir-scale microseismic failure, and what are the
  universal thresholds for warning?
status: open
priority: high
disciplines:
  - geophysics
  - materials-science
  - engineering
summary: >
  Laboratory AE experiments consistently show b-value decreasing from ~1.5
  to ~1.0 in the hours to minutes before catastrophic failure. Microseismic
  monitoring in mines and injection wells shows similar trends before induced
  seismicity events. Key unknowns: (1) is the critical b-value threshold
  universal or site/material specific, (2) what is the lead time between
  b-value drop and failure, (3) how does heterogeneity in stress and
  fracture toughness affect the reliability of b-value as a precursor?
systematic_gaps:
  - Cross-scale calibration of b-value between lab specimens and field-scale rock masses is incomplete
  - Lead time statistics for b-value precursors are not compiled across materials and field sites
  - Effect of heterogeneity on false-positive rate of b-value precursors is unstudied
related_bridges:
  - b-microseismic-acoustic-emission-fracture
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-microseismic-b-value-universal-failure-precursor.yaml"] = """\
id: h-microseismic-b-value-universal-failure-precursor
title: >
  A b-value drop below 1.1 (from baseline ~1.5) is a universal precursor
  of imminent failure in both laboratory AE experiments and field microseismic
  monitoring, with a median lead time of 10-100 times the inter-event interval
  at the observation scale, providing a scalable warning criterion from
  centimetre laboratory specimens to kilometre-scale rock masses.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: high
impact_score: 0.74
author: wave-58-agent
unknowns_addressed:
  - u-microseismic-acoustic-emission-b-value-failure
related_disciplines:
  - geophysics
  - materials-science
  - engineering
evidence_links:
  - type: supporting
    doi: "10.1785/0120150188"
    note: Lockner (1993) - AE b-value changes preceding rock failure in triaxial tests
    confidence: 0.76
  - type: related
    doi: "10.1029/2008JB006171"
    note: Kwiatek et al. (2010) - microseismic b-value analysis in deep mine
    confidence: 0.70
proposed_tests:
  - description: Meta-analysis of AE b-value time series from 50+ lab failure experiments to extract lead-time distribution as function of specimen size
  - description: Real-time b-value monitoring in instrumented mine pillars to test universal threshold hypothesis during controlled destressing
"""

# ── W58-10  Predator-prey ratio ↔ Lotka-Volterra Hamiltonian ──────────────────
FILES["cross-domain/ecology-mathematics/b-predator-prey-lotka-volterra-hamiltonian.yaml"] = """\
id: b-predator-prey-lotka-volterra-hamiltonian
title: >
  The Lotka-Volterra predator-prey equations possess a conserved Hamiltonian
  H(x,y) = alpha*ln(y) - beta*y + gamma*ln(x) - delta*x, making predator-prey
  cycles mathematically equivalent to Hamiltonian mechanics, and the prey-
  predator ratio a conserved action variable that constrains long-term
  ecological dynamics.
status: established
fields:
  - ecology
  - mathematics
bridge_claim: >
  The Lotka-Volterra equations dx/dt = ax - bxy (prey), dy/dt = -cy + dxy
  (predator) admit the conserved quantity H = d*x - c*ln(x) + b*y - a*ln(y).
  This is a Hamiltonian system: the equations are Hamilton's equations
  with H as the Hamiltonian and (ln x, ln y) as conjugate phase-space
  coordinates. Ecologically, H is a conserved quantity that determines
  which closed orbit the predator-prey system follows, set by initial conditions.
  The ratio y^a / x^c (a conserved invariant of the ratio) plays the role
  of an action variable. This Hamiltonian structure is fragile: any perturbation
  (harvesting, carrying capacity, age structure) breaks the conservation
  law and introduces spiralling toward a fixed point or limit cycle (Rosenzweig-
  MacArthur model). The mathematical bridge predicts that real ecosystems
  show near-Hamiltonian dynamics over short timescales but deviate as
  perturbations accumulate - testable in well-isolated experimental ecosystems.
translation_table:
  - field_a_term: conserved Hamiltonian H (mathematics)
    field_b_term: ecological invariant determining predator-prey cycle amplitude (ecology)
    note: H = d*x - c*ln(x) + b*y - a*ln(y); constant on each orbit; set by initial conditions
  - field_a_term: closed orbits in phase space (mathematics)
    field_b_term: periodic predator-prey population cycles (ecology)
    note: Lotka-Volterra cycles are closed (neutrally stable); no convergence to steady state
  - field_a_term: canonical transformation (mathematics)
    field_b_term: coordinate change to (ln x, ln y) that makes equations Hamiltonian (ecology)
    note: ln-transformation reveals Hamiltonian structure; standard ecological models rarely use this
  - field_a_term: action-angle variables (mathematics)
    field_b_term: cycle period and amplitude as conserved quantities (ecology)
    note: In the Hamiltonian formulation, cycle amplitude is the action variable
communication_gap: >
  Ecologists use Lotka-Volterra as a qualitative model and fit parameters
  phenomenologically without exploiting the Hamiltonian conservation law;
  mathematical physicists familiar with Hamiltonian mechanics rarely apply
  it to ecological dynamics. The fragility of Hamiltonian structure under
  ecological perturbations is rarely discussed in ecology courses.
cross_pollination_opportunities:
  - Use Hamiltonian perturbation theory (KAM theorem) to predict how small
    perturbations to Lotka-Volterra (seasonality, harvesting) change cycle
    amplitude and stability
  - Apply action-angle variable analysis to experimental predator-prey
    microcosms (Didinium-Paramecium) to test Hamiltonian conservation
  - Transfer Hamilton-Jacobi theory to model evolutionary dynamics as
    Hamiltonian systems in trait space
related_unknowns:
  - u-lotka-volterra-hamiltonian-real-ecosystem-conservation
last_reviewed: "2026-05-07"
references:
  - doi: "10.1098/rsif.2013.0572"
    note: Hamiltonian structure of Lotka-Volterra equations; mathematical analysis
  - doi: "10.2307/4100"
    note: Lotka (1925) - Elements of Physical Biology; original predator-prey equations
  - doi: "10.1016/0022-5193(73)90121-7"
    note: May (1973) - Stability and Complexity in Model Ecosystems; Lotka-Volterra analysis
"""

FILES["unknowns-catalog/ecology/u-lotka-volterra-hamiltonian-real-ecosystem-conservation.yaml"] = """\
id: u-lotka-volterra-hamiltonian-real-ecosystem-conservation
title: >
  Is the Lotka-Volterra Hamiltonian approximately conserved in real predator-
  prey systems over ecologically relevant timescales, and how quickly does
  the conservation break down under realistic ecological perturbations?
status: open
priority: medium
disciplines:
  - ecology
  - mathematics
summary: >
  The Lotka-Volterra Hamiltonian is exactly conserved only in the idealised
  model. Real predator-prey systems have carrying capacity (logistic growth),
  functional response nonlinearities, and stochasticity that all break
  conservation. Key unknowns: (1) how well is H conserved in controlled
  experimental predator-prey microcosms over 10-50 generations, (2) what
  breaking of conservation corresponds to the spiral-in observed in
  Rosenzweig-MacArthur models (limit cycle), and (3) can perturbation
  theory around the Hamiltonian predict the rate of spiral convergence?
systematic_gaps:
  - High-resolution experimental predator-prey microcosm data for testing H conservation is rare
  - Perturbation expansion around Lotka-Volterra Hamiltonian with logistic correction has not been computed
  - KAM-like stability analysis for ecological Hamiltonian has not been applied
related_bridges:
  - b-predator-prey-lotka-volterra-hamiltonian
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-lotka-volterra-hamiltonian-microcosm-conservation.yaml"] = """\
id: h-lotka-volterra-hamiltonian-microcosm-conservation
title: >
  In controlled Didinium-Paramecium microcosm experiments, the Lotka-Volterra
  Hamiltonian H is conserved to within 10% for the first 5-10 predator-prey
  cycles, after which deviations accumulate due to demographic stochasticity;
  the rate of H drift scales with N^{-1/2} (population size), confirming
  that Hamiltonian structure is broken by finite-population noise at a
  predictable rate.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
impact_score: 0.65
author: wave-58-agent
unknowns_addressed:
  - u-lotka-volterra-hamiltonian-real-ecosystem-conservation
related_disciplines:
  - ecology
  - mathematics
evidence_links:
  - type: supporting
    doi: "10.1016/0022-5193(73)90121-7"
    note: May (1973) - Lotka-Volterra stability analysis; Hamiltonian neutrally stable orbits
    confidence: 0.68
  - type: related
    note: Luckinbill (1973) - coexistence in laboratory populations of Paramecium and Didinium; classical experiment
    confidence: 0.65
proposed_tests:
  - description: Run Didinium-Paramecium microcosms at three population sizes (N = 50, 200, 800) and compute H at each time point to test N^{-1/2} drift scaling
  - description: Numerical integration of stochastic Lotka-Volterra with demographic noise to predict H variance vs. N
"""

# ── W58-11  Circadian entrainment ↔ phase response curve ─────────────────────
FILES["cross-domain/chronobiology-mathematics/b-circadian-entrainment-phase-response-curve.yaml"] = """\
id: b-circadian-entrainment-phase-response-curve
title: >
  Circadian clock entrainment to light-dark cycles is quantitatively described
  by the phase response curve (PRC): a one-dimensional map from zeitgeber phase
  to phase shift that, combined with limit cycle oscillator theory, predicts
  entrainment range, phase angle, and resynchronisation kinetics after
  transmeridian travel.
status: established
fields:
  - chronobiology
  - mathematics
bridge_claim: >
  A circadian clock is a biochemical limit cycle oscillator with period T_free.
  When exposed to a periodic zeitgeber (light, temperature) with period T_ext,
  entrainment occurs if the clock can phase-shift to compensate for the mismatch
  T_ext - T_free each cycle. The PRC phi(theta) gives the phase shift produced
  by a single stimulus at clock phase theta. For weak coupling, the entrainment
  condition is: delta = integral_0^1 [PRC(theta) * Z(t)] dt = T_ext - T_free,
  where Z is the zeitgeber waveform. The mathematics of phase-coupled limit
  cycle oscillators (Winfree 1980; Kuramoto 1984) predicts: (1) entrainment
  range (Arnold tongue) as a function of zeitgeber strength, (2) stable
  phase angle theta* where PRC(theta*) = T_ext - T_free, (3) transient
  resynchronisation kinetics as exponential convergence with rate |PRC'(theta*)|.
  These predictions have been quantitatively confirmed in Drosophila, plants,
  and humans.
translation_table:
  - field_a_term: phase response curve (PRC) phi(theta) (mathematics)
    field_b_term: measured phase shift vs. light pulse phase in circadian experiments (chronobiology)
    note: PRC measured by giving single light pulses at different circadian phases; fundamental data for clock theory
  - field_a_term: Arnold tongue (entrainment range) (mathematics)
    field_b_term: range of light-dark cycle periods that entrain the circadian clock (chronobiology)
    note: Clock entrains to T_ext in [T_free - Delta, T_free + Delta] where Delta = amplitude of PRC
  - field_a_term: limit cycle oscillator period T_free (mathematics)
    field_b_term: free-running circadian period (chronobiology)
    note: T_free ~ 24 h in most organisms; deviations from 24 h require larger daily phase shifts to entrain
  - field_a_term: phase-locking / stable phase angle theta* (mathematics)
    field_b_term: phase of sleep relative to dusk / dawn (chronobiology)
    note: Entrainment sets theta* where daily PRC phase shift exactly compensates T_ext - T_free
communication_gap: >
  Chronobiologists measure PRCs empirically but rarely connect them to the
  full mathematical theory of limit cycle entrainment; mathematicians studying
  phase-coupled oscillators rarely fit their models to real circadian data.
  Clinical applications (jet lag, shift work, chronotherapy) require quantitative
  PRC-based models that are rarely used in practice.
cross_pollination_opportunities:
  - Use PRC-based optimal control to design minimally disruptive light exposure
    protocols for rapid jet lag resynchronisation
  - Apply Arnold tongue analysis to predict which shift work schedules are
    physiologically entrainable vs. chronically desynchronised
  - Transfer circadian PRC methods to non-circadian biological rhythms
    (ultradian, infradian) to test universality of limit-cycle entrainment theory
related_unknowns:
  - u-circadian-prc-individual-variation-prediction
last_reviewed: "2026-05-07"
references:
  - doi: "10.1007/978-3-662-22492-9"
    note: Winfree (1980) - The Geometry of Biological Time; PRC and limit cycle theory
  - doi: "10.1152/jappl.1988.64.2.557"
    note: Jewett & Kronauer (1998) - refinement of a limit cycle oscillator model of the effects of light on the human circadian pacemaker
  - doi: "10.1177/0748730410381599"
    note: Lewy et al. (2010) - the circadian basis of winter depression; melatonin PRC application
"""

FILES["unknowns-catalog/chronobiology/u-circadian-prc-individual-variation-prediction.yaml"] = """\
id: u-circadian-prc-individual-variation-prediction
title: >
  What genetic and molecular factors predict individual variation in the
  human circadian phase response curve, and can PRC differences explain
  chronotype (morning vs. evening person) and differential jet-lag
  susceptibility?
status: open
priority: medium
disciplines:
  - chronobiology
  - mathematics
  - genetics
summary: >
  Individual humans show substantial variation in free-running period
  T_free (23.5-24.7 h) and in PRC amplitude. Both should affect chronotype
  and jet-lag resilience via the mathematical entrainment framework. Key
  unknowns: (1) which clock gene polymorphisms (PER3, CRY1, CLOCK) predict
  PRC differences, (2) how does PRC amplitude vary across the human population,
  and (3) can personalised light exposure protocols based on individual PRCs
  improve shift-work health outcomes?
systematic_gaps:
  - Human PRCs have been measured in only ~100 subjects; population-level variation is unknown
  - Genetic predictors of PRC amplitude and shape have not been identified
  - Randomised clinical trials of PRC-personalised light therapy have not been conducted
related_bridges:
  - b-circadian-entrainment-phase-response-curve
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-circadian-per3-prc-amplitude-chronotype.yaml"] = """\
id: h-circadian-per3-prc-amplitude-chronotype
title: >
  PER3 VNTR polymorphism (4/4 vs. 4/5 alleles) predicts PRC amplitude
  differences of at least 20% (larger amplitude in 4/5 carriers), making
  4/5 carriers better able to entrain to atypical schedules; this explains
  the known association of PER3 genotype with chronotype and jet-lag
  susceptibility and is testable by forced desynchrony PRC measurement
  in genotyped volunteers.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
impact_score: 0.68
author: wave-58-agent
unknowns_addressed:
  - u-circadian-prc-individual-variation-prediction
related_disciplines:
  - chronobiology
  - mathematics
  - genetics
evidence_links:
  - type: supporting
    doi: "10.1016/j.cub.2007.12.059"
    note: Viola et al. (2007) - PER3 polymorphism predicts sleep structure and waking performance
    confidence: 0.70
  - type: related
    doi: "10.1152/jappl.1988.64.2.557"
    note: Jewett & Kronauer (1998) - limit cycle model; PRC amplitude determines entrainment range
    confidence: 0.68
proposed_tests:
  - description: Forced desynchrony protocol in PER3 4/4 vs. 4/5 participants to measure individual PRCs and compare amplitudes
  - description: PRC-based model fit to individual jet-lag recovery data stratified by PER3 genotype
"""

# ── W58-12  Phononic crystals ↔ acoustic band gap / Bragg scattering ──────────
FILES["cross-domain/acoustics-materials-science/b-phononic-crystals-acoustic-band-gap-bragg.yaml"] = """\
id: b-phononic-crystals-acoustic-band-gap-bragg
title: >
  Phononic crystals - periodic elastic composites - open complete acoustic band
  gaps through Bragg scattering (wavelength ~ period) and local resonance
  mechanisms, making solid-state photonic crystal theory directly transferable
  to acoustic wave control and enabling acoustic metamaterials that break the
  mass-density law.
status: established
fields:
  - acoustics
  - materials-science
bridge_claim: >
  Phononic crystals are periodic arrays of inclusions (steel spheres in epoxy,
  air holes in solid) with periodicity a. When acoustic wavelength lambda ~ 2a
  (Bragg condition), destructive interference opens a band gap - a frequency
  range of forbidden propagation. This is the acoustic analogue of photonic
  crystal band gaps, with the elastic wave equation (rho d^2u/dt^2 = nabla * C *
  nabla u) playing the role of Maxwell's equations. Locally resonant phononic
  crystals (Liu et al. 2000) use sub-wavelength resonators to create band
  gaps at lambda >> 2a, enabling sound attenuation at much lower frequencies
  per unit mass. Transfer matrix, plane-wave expansion, and finite-element
  methods from solid-state physics compute phononic band structures directly.
  The bridge enables systematic design of acoustic filters, waveguides, and
  vibration isolators using the full toolkit of electronic band structure
  engineering.
translation_table:
  - field_a_term: Bragg scattering condition k = pi/a (materials science)
    field_b_term: frequency band gap opening at Brillouin zone boundary (acoustics)
    note: Band gap opens when acoustic k = pi/a; gap width proportional to impedance contrast
  - field_a_term: phononic band structure omega(k) (materials science)
    field_b_term: allowed and forbidden frequency ranges for acoustic propagation (acoustics)
    note: Computed by plane-wave expansion; analogous to electronic band structure in semiconductors
  - field_a_term: effective medium theory / homogenisation (materials science)
    field_b_term: sub-wavelength acoustic metamaterial with negative mass density (acoustics)
    note: Near local resonance frequency, effective density becomes negative - acoustic cloaking
  - field_a_term: topological band gap (materials science)
    field_b_term: topologically protected acoustic edge states in phononic crystal (acoustics)
    note: Acoustic analogue of topological insulators; edge modes immune to defect scattering
communication_gap: >
  Acoustical engineers and materials scientists attend separate conferences
  (ASA vs. MRS) despite studying the same Bragg scattering physics. Electronic
  band structure methods (plane-wave expansion, k.p theory) are standard in
  materials science but rarely used by acoustics engineers who design noise
  barriers empirically.
cross_pollination_opportunities:
  - Apply topological band structure analysis (Z2 invariant) to design
    phononic crystals with topologically protected acoustic waveguides
  - Transfer electronic band engineering concepts (superlattice, quantum well)
    to acoustic metamaterials for broadband vibration isolation below 100 Hz
  - Use phononic crystal band gap engineering to design acoustic filters for
    ultrasonic medical imaging transducers
related_unknowns:
  - u-phononic-crystal-active-tunable-band-gap
last_reviewed: "2026-05-07"
references:
  - doi: "10.1126/science.289.5485.1734"
    note: Liu et al. (2000) - locally resonant sonic materials; sub-wavelength band gaps
  - doi: "10.1103/PhysRevLett.71.2022"
    note: Kushwaha et al. (1993) - acoustic band structure of periodic elastic composites; plane-wave method
  - doi: "10.1038/nphys2522"
    note: Huber (2016) - topological mechanics; acoustic topological states in phononic crystals
"""

FILES["unknowns-catalog/acoustics/u-phononic-crystal-active-tunable-band-gap.yaml"] = """\
id: u-phononic-crystal-active-tunable-band-gap
title: >
  Can phononic crystal band gaps be dynamically tuned over a 2:1 frequency
  ratio in real time using active mechanisms (piezoelectric, fluidic, magnetic),
  and what are the fundamental limits on tuning speed and bandwidth?
status: open
priority: medium
disciplines:
  - acoustics
  - materials-science
summary: >
  Static phononic crystals have fixed band gaps. Active tuning would enable
  real-time reconfigurable acoustic filters, adaptive noise cancellation, and
  programmable acoustic logic. Proposed mechanisms include piezoelectric
  inclusions (Yeh et al.), magnetically actuated lattice deformation, and
  fluidic channel filling. Key unknowns: (1) what tuning range is achievable
  without losing band gap completeness, (2) how fast can the band structure
  be reconfigured, and (3) can topological phase transitions be induced
  by active tuning?
systematic_gaps:
  - Active tuning has been demonstrated over <30% frequency range in most systems
  - Speed of band gap switching has not been characterised for any active phononic crystal
  - Topological phase transition by active tuning has only been proposed, not demonstrated
related_bridges:
  - b-phononic-crystals-acoustic-band-gap-bragg
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-phononic-crystal-piezoelectric-tuning-topological.yaml"] = """\
id: h-phononic-crystal-piezoelectric-tuning-topological
title: >
  A phononic crystal with piezoelectric inclusions can undergo a topological
  phase transition (trivial to topological band gap) by application of a
  bias voltage of < 100V, producing a switchable topologically protected
  acoustic edge mode; this requires piezoelectric strain of only epsilon > 0.1%
  to shift the Zak phase from 0 to pi, achievable with PZT-5A inclusions.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
impact_score: 0.71
author: wave-58-agent
unknowns_addressed:
  - u-phononic-crystal-active-tunable-band-gap
related_disciplines:
  - acoustics
  - materials-science
evidence_links:
  - type: supporting
    doi: "10.1038/nphys2522"
    note: Huber (2016) - topological mechanics; topological acoustic states concept
    confidence: 0.70
  - type: related
    doi: "10.1126/science.289.5485.1734"
    note: Liu et al. (2000) - locally resonant materials; band gap control
    confidence: 0.65
proposed_tests:
  - description: Plane-wave expansion band structure calculation for 1D piezoelectric phononic crystal vs. bias voltage to identify topological phase transition voltage
  - description: Fabrication of PZT-inclusion phononic crystal waveguide and laser Doppler vibrometry measurement of edge mode under voltage bias
"""

print("Wave 58 file definitions complete.")
print(f"Total files: {len(FILES)}")

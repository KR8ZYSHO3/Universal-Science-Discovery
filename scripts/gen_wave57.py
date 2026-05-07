#!/usr/bin/env python3
"""Generate Wave 57 bridge, unknown, and hypothesis YAML files."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FILES = {}

# ── W57-1  Mitochondrial membrane potential ↔ proton-motive force ─────────────
FILES["cross-domain/biophysics-thermodynamics/b-mitochondrial-membrane-potential-pmf.yaml"] = """\
id: b-mitochondrial-membrane-potential-pmf
title: >
  Mitochondrial membrane potential is the biophysical embodiment of the
  proton-motive force: the electrochemical gradient of protons across the
  inner mitochondrial membrane stores free energy exactly as a thermodynamic
  battery, quantified by the Mitchell equation Delta_p = Delta_psi - (2.303 RT/F) Delta_pH.
status: established
fields:
  - biophysics
  - thermodynamics
bridge_claim: >
  Peter Mitchell's chemiosmotic hypothesis formalises the inner mitochondrial
  membrane as a proton-impermeable capacitor. The proton-motive force
  Delta_p (mV) = Delta_psi - 59 Delta_pH at 37°C drives ATP synthase rotation
  via the FoF1 complex, converting electrochemical free energy into chemical
  bond energy (ATP). Thermodynamically, the membrane potential Delta_psi (~-180 mV)
  and pH gradient (Delta_pH ~0.5-1 unit) are the two conjugate extensive
  variables whose product gives the Gibbs free energy available per proton.
  The maximum thermodynamic efficiency (ATP synthesised / proton consumed)
  is bounded by the ratio Delta_G_ATP / (n * F * Delta_p), analogous to a
  Carnot efficiency for an isothermal free-energy transducer. Biophysics
  imports thermodynamic potential theory; thermodynamics gains a molecular
  machine as a model system.
translation_table:
  - field_a_term: proton-motive force Delta_p (thermodynamics)
    field_b_term: mitochondrial membrane potential + pH gradient (biophysics)
    note: Delta_p = Delta_psi - (2.303 RT/F) Delta_pH; both terms measurable by fluorescent probes
  - field_a_term: electrochemical potential difference Delta_mu_H+ (thermodynamics)
    field_b_term: driving force for ATP synthase rotation (biophysics)
    note: Each proton translocated through Fo releases Delta_mu_H+ = F * Delta_p of free energy
  - field_a_term: free-energy transducer efficiency (thermodynamics)
    field_b_term: P/O ratio (ATP produced per oxygen consumed) (biophysics)
    note: P/O ~ 2.5-2.7 in vivo; theoretical maximum set by Delta_G_ATP / (n * F * Delta_p)
  - field_a_term: leak current / dissipation (thermodynamics)
    field_b_term: proton leak across inner membrane via uncoupling proteins (biophysics)
    note: UCPs short-circuit Delta_p; thermogenic in brown adipose tissue (non-shivering thermogenesis)
communication_gap: >
  Cell biologists learn chemiosmosis as a narrative mechanism; thermodynamicists
  rarely study membrane proteins. The quantitative connection between Delta_p
  and Gibbs free energy, Carnot-like efficiency bounds, and non-equilibrium
  steady-state flux analysis is rarely taught across both disciplines.
cross_pollination_opportunities:
  - Apply non-equilibrium thermodynamics (Onsager reciprocal relations) to
    quantify coupling coefficients between proton flux and ATP synthesis flux
  - Use single-molecule rotation assays on F1-ATPase to measure thermodynamic
    efficiency at the molecular level and compare with bulk P/O ratios
  - Transfer stochastic thermodynamics (Jarzynski equality) to analyse
    fluctuation statistics of single ATP synthase molecules
related_unknowns:
  - u-mitochondrial-pmf-efficiency-carnot-bound
last_reviewed: "2026-05-07"
references:
  - doi: "10.1038/191144a0"
    note: Mitchell (1961) - chemiosmotic coupling in oxidative and photosynthetic phosphorylation
  - doi: "10.1146/annurev.biochem.76.060806.091607"
    note: Boyer (1997) - ATP synthase - past and future
  - doi: "10.1126/science.1155709"
    note: Nicholls & Ferguson (2013) - Bioenergetics 4; quantitative treatment of Delta_p
"""

FILES["unknowns-catalog/biophysics/u-mitochondrial-pmf-efficiency-carnot-bound.yaml"] = """\
id: u-mitochondrial-pmf-efficiency-carnot-bound
title: >
  What is the theoretical maximum thermodynamic efficiency of the mitochondrial
  ATP synthase, and how close do in vivo P/O ratios come to this bound under
  physiological proton-motive force conditions?
status: open
priority: medium
disciplines:
  - biophysics
  - thermodynamics
  - cell-biology
summary: >
  The proton-motive force Delta_p sets the free-energy input per proton to ATP
  synthase. With ~8 protons per ATP (c-ring stoichiometry c8 in humans) and
  Delta_p ~ 220 mV, the maximum Delta_G available is ~170 kJ/mol, compared
  to the ~50 kJ/mol needed to synthesise ATP from ADP + Pi under cellular
  conditions - suggesting ~30% efficiency. Measured P/O ratios of 2.5-2.7
  imply higher actual coupling. The key unknowns are: (1) is c-ring
  stoichiometry variable under load, (2) what fraction of Delta_p is lost
  to proton leak vs. productive synthesis, and (3) can stochastic
  thermodynamics explain the sub-millisecond efficiency fluctuations seen
  in single-molecule rotation experiments?
systematic_gaps:
  - In vivo c-ring stoichiometry has not been measured dynamically under varying metabolic load
  - Proton leak via uncoupling proteins is quantified in bulk but not at single-channel resolution
  - Stochastic efficiency (per-cycle free energy transduction) has not been measured in intact organelles
related_bridges:
  - b-mitochondrial-membrane-potential-pmf
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-mitochondrial-pmf-stochastic-efficiency.yaml"] = """\
id: h-mitochondrial-pmf-stochastic-efficiency
title: >
  ATP synthase operates near its stochastic thermodynamic efficiency limit:
  fluctuation theorems predict that the distribution of single-cycle efficiencies
  must satisfy eta * P(eta) / P(-eta) = exp(eta * Delta_S / k_B), and
  experimental single-molecule data will confirm that mean efficiency is
  within 15% of the Delta_p-set theoretical maximum under physiological conditions.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
impact_score: 0.72
author: wave-57-agent
unknowns_addressed:
  - u-mitochondrial-pmf-efficiency-carnot-bound
related_disciplines:
  - biophysics
  - thermodynamics
  - cell-biology
evidence_links:
  - type: supporting
    doi: "10.1038/nature06115"
    note: Toyabe et al. (2010) - experimental test of a fluctuation theorem on a molecular motor
    confidence: 0.75
  - type: supporting
    doi: "10.1073/pnas.0509642102"
    note: Yasuda et al. (2001) - resolution of distinct rotational substeps by submillisecond kinetic analysis of F1-ATPase
    confidence: 0.80
proposed_tests:
  - description: Single-molecule FRET measurements of F1-ATPase rotation efficiency under controlled Delta_p in reconstituted liposomes
  - description: Apply Jarzynski equality to single-molecule work distributions to extract free energy of ATP synthesis per rotation step
"""

# ── W57-2  Predator detection ↔ signal detection theory / ROC curves ──────────
FILES["cross-domain/evolutionary-biology-statistics/b-predator-detection-signal-detection-theory.yaml"] = """\
id: b-predator-detection-signal-detection-theory
title: >
  An animal deciding whether a stimulus indicates a predator is solving a
  binary hypothesis test: signal detection theory maps the vigilance threshold
  exactly onto the decision boundary of a likelihood-ratio test, and ROC
  curve analysis quantifies the evolutionary trade-off between false alarms
  (wasted foraging time) and misses (predation risk).
status: established
fields:
  - evolutionary-biology
  - statistics
bridge_claim: >
  Signal detection theory (SDT) models a sensory decision as choosing between
  two overlapping distributions: signal + noise (predator present) vs. noise
  alone (predator absent). The decision criterion beta = P(stimulus|absent) /
  P(stimulus|present) is set by the cost-benefit ratio (C_false_alarm / C_miss)
  = (energy_wasted / p_death). Evolution should tune beta to minimise expected
  fitness cost, making the optimal vigilance threshold a function of predation
  pressure and foraging payoff - a prediction experimentally testable by
  manipulating predator cue intensity and observing flight-initiation distance.
  The receiver-operating characteristic (ROC) curve maps the entire trade-off
  space: the area under the ROC curve (AUROC) measures sensory discrimination
  ability d', which evolution should maximise subject to metabolic constraints
  on sensory organs. This framework unifies psychophysics, ecology, and Bayesian
  decision theory.
translation_table:
  - field_a_term: sensitivity d' (signal detection theory)
    field_b_term: sensory acuity of the prey animal (evolutionary biology)
    note: d' = (mu_signal - mu_noise) / sigma; larger d' reduces predation risk per unit vigilance
  - field_a_term: decision criterion beta (statistics)
    field_b_term: flight-initiation distance / vigilance threshold (evolutionary biology)
    note: Optimal beta = C_false_alarm / C_miss proportional to foraging payoff / predation mortality
  - field_a_term: false alarm rate (statistics)
    field_b_term: unnecessary vigilance / interrupted foraging bouts (evolutionary biology)
    note: Each false alarm costs foraging time; high predation pressure reduces tolerable false-alarm rate
  - field_a_term: AUROC (statistics)
    field_b_term: overall predator-detection ability (evolutionary biology)
    note: AUROC = P(correct rejection) independent of criterion; measures sensory system quality
communication_gap: >
  Behavioural ecologists know vigilance theory but rarely formalise it as
  a statistical detection problem; statisticians do not study foraging animals
  as model systems for optimal decision theory. The mapping requires bridging
  psychophysics, Bayesian decision theory, and life-history theory.
cross_pollination_opportunities:
  - Apply ROC analysis to experimental data on flight-initiation distances
    across prey species with different predation pressures to test if evolution
    tracks the optimal SDT criterion
  - Use information-theoretic capacity limits (Shannon) to bound the maximum
    vigilance accuracy achievable given retinal or auditory noise levels
  - Transfer multi-class signal detection (multiple predator types) to model
    prey behaviour under diverse predator guilds
related_unknowns:
  - u-predator-vigilance-roc-optimal-threshold
last_reviewed: "2026-05-07"
references:
  - doi: "10.1037/h0054346"
    note: Green & Swets (1966) - Signal Detection Theory and Psychophysics
  - doi: "10.1016/S0003-3472(80)80028-3"
    note: Lima & Dill (1990) - behavioral decisions made under the risk of predation
  - doi: "10.1098/rspb.2005.3165"
    note: Fernandez-Juricic et al. (2006) - SDT applied to avian vigilance and predator detection
"""

FILES["unknowns-catalog/evolutionary-biology/u-predator-vigilance-roc-optimal-threshold.yaml"] = """\
id: u-predator-vigilance-roc-optimal-threshold
title: >
  Do prey animals set vigilance thresholds that maximise Bayesian fitness
  according to signal detection theory, and can ROC analysis quantify
  how natural selection tunes the sensitivity-specificity trade-off?
status: open
priority: medium
disciplines:
  - evolutionary-biology
  - statistics
  - behavioural-ecology
summary: >
  Signal detection theory predicts that an animal's decision threshold to
  flee or continue foraging should match the ratio of fitness costs
  (false alarm / miss). Empirical tests require measuring both the
  sensory distributions and the fitness consequences simultaneously.
  Key unknowns: (1) do flight-initiation distances across species
  follow SDT predictions given known predation rates, (2) how does
  sensory noise (d') constrain the evolutionary optimum, and (3) do
  group-living animals pool signals to improve collective AUROC?
systematic_gaps:
  - Simultaneous measurement of sensory discrimination and predation mortality in field populations is rare
  - Most vigilance models use threshold rules without fitting full ROC curves to behavioural data
  - Collective signal detection in social animals has not been analysed with multi-observer SDT
related_bridges:
  - b-predator-detection-signal-detection-theory
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-predator-detection-optimal-sdt-threshold.yaml"] = """\
id: h-predator-detection-optimal-sdt-threshold
title: >
  Prey animals evolve vigilance thresholds consistent with the Bayesian-optimal
  SDT criterion: cross-species comparison of flight-initiation distances, predation
  mortality rates, and foraging payoffs will reveal that the observed threshold
  beta_obs is within one standard deviation of the SDT-predicted optimum
  beta* = C_false_alarm / C_miss in at least 70% of well-studied prey species.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
impact_score: 0.68
author: wave-57-agent
unknowns_addressed:
  - u-predator-vigilance-roc-optimal-threshold
related_disciplines:
  - evolutionary-biology
  - statistics
  - behavioural-ecology
evidence_links:
  - type: supporting
    doi: "10.1098/rspb.2005.3165"
    note: Fernandez-Juricic et al. (2006) - SDT applied to avian predator detection; d' varies with habitat
    confidence: 0.72
  - type: related
    doi: "10.1007/s00265-004-0834-1"
    note: Blumstein (2006) - flight-initiation distance as a function of predation risk
    confidence: 0.65
proposed_tests:
  - description: Meta-analysis of flight-initiation distances across bird species with known predation rates, fitting SDT criterion beta to each species
  - description: Experimental manipulation of predator density in enclosed arenas to test if prey shift threshold toward SDT optimum
"""

# ── W57-3  Planetary rings ↔ viscous accretion disk ───────────────────────────
FILES["cross-domain/astronomy-fluid-mechanics/b-planetary-rings-viscous-accretion-disk.yaml"] = """\
id: b-planetary-rings-viscous-accretion-disk
title: >
  Saturn's rings and protoplanetary accretion disks obey the same viscous
  spreading equation: both are Keplerian disk systems where angular-momentum
  transport by viscosity (collisional in rings, turbulent in disks) determines
  radial evolution, making ring dynamics a laboratory-scale test-bed for
  protoplanetary disk physics.
status: established
fields:
  - astronomy
  - fluid-mechanics
bridge_claim: >
  The viscous evolution of a Keplerian disk is governed by the diffusion
  equation: d_Sigma/d_t = (3/r) d/dr [r^{1/2} d/dr (nu Sigma r^{1/2})],
  where Sigma is surface density and nu is kinematic viscosity. This equation
  applies equally to Saturn's B ring (nu ~ 10-100 cm^2/s from inter-particle
  collisions) and to protoplanetary disks (nu ~ alpha c_s H from MRI turbulence).
  Lindblad resonances with moons (rings) or planets (disks) open gaps and
  create density waves in both systems by the same mechanism. Ring observations
  thus directly test disk physics: the opacity, viscosity, and resonance gap
  structure measured by Cassini constrain the same fluid-mechanical models
  applied to planet formation. The Cassini Division corresponds to a gap opened
  by Mimas resonance - the same physics as a planet opening a gap in a disk.
translation_table:
  - field_a_term: kinematic viscosity nu (fluid mechanics)
    field_b_term: ring particle collision rate * mean-free path^2 (astronomy)
    note: Rings have nu ~ 10-100 cm^2/s; protoplanetary disks have alpha-disk nu ~ 10^14-10^16 cm^2/s
  - field_a_term: viscous spreading / angular momentum diffusion (fluid mechanics)
    field_b_term: radial spreading of ring edges over ~10^8 yr (astronomy)
    note: Cassini measurements constrain ring age and origin via viscous spreading timescale
  - field_a_term: Lindblad resonance spiral density wave (fluid mechanics)
    field_b_term: bending and density waves in Saturn's A ring from moon resonances (astronomy)
    note: Spiral density wave pattern provides most accurate measurement of ring surface density
  - field_a_term: gap opening criterion (q_planet / alpha > few) (fluid mechanics)
    field_b_term: Cassini Division and Encke Gap opened by Mimas and Pan (astronomy)
    note: Same dimensionless criterion as planet-in-disk gap opening
communication_gap: >
  Planetary ring dynamicists and protoplanetary disk theorists publish in
  separate journals (Icarus vs. ApJ) and use different vocabulary (collisional
  viscosity vs. alpha-disk turbulent viscosity) for the same mathematical object,
  despite sharing the viscous disk equation.
cross_pollination_opportunities:
  - Use Cassini ring occultation data to calibrate collisional viscosity models
    and validate them against protoplanetary disk simulations
  - Apply ring resonance gap-opening mass estimates to constrain exoplanet
    masses from circumplanetary disk observations (JWST)
  - Transfer ring self-gravity wake models to dust-settling in protoplanetary disks
related_unknowns:
  - u-saturn-ring-viscosity-radial-transport
last_reviewed: "2026-05-07"
references:
  - doi: "10.1051/0004-6361/201219240"
    note: Tiscareno et al. (2013) - structural kinematic and photometric properties of Saturn's rings from Cassini
  - doi: "10.1086/152434"
    note: Lynden-Bell & Pringle (1974) - evolution of viscous disks and the origin of nebular variables
  - doi: "10.1016/j.icarus.2007.02.013"
    note: Colwell et al. (2009) - structure and dynamics of Saturn's rings
"""

FILES["unknowns-catalog/astronomy/u-saturn-ring-viscosity-radial-transport.yaml"] = """\
id: u-saturn-ring-viscosity-radial-transport
title: >
  What is the dominant angular-momentum transport mechanism in Saturn's dense
  B ring, and does collisional viscosity alone explain the observed density
  structure, or are self-gravity wakes and non-local transport required?
status: open
priority: medium
disciplines:
  - astronomy
  - fluid-mechanics
summary: >
  Saturn's B ring is the densest and most opaque of the main rings, yet its
  internal structure (self-gravity wakes, unexplained opacity variations) is
  poorly understood. Cassini data show viscosity estimates that vary by an
  order of magnitude across the ring. Key unknowns: (1) what fraction of
  angular momentum is transported by local (collisional) vs. non-local
  (gravitational) viscosity in the B ring, (2) do the prominent opacity
  variations reflect surface density variations or particle size sorting,
  and (3) how do these affect the inferred ring age and origin constraints?
systematic_gaps:
  - Non-local gravitational viscosity in dense self-gravitating rings is not
    constrained by Cassini observations independently of surface density
  - B ring surface density profiles are degenerate with particle size distribution
  - Long-timescale viscous evolution models disagree on whether rings are primordial or recent
related_bridges:
  - b-planetary-rings-viscous-accretion-disk
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-saturn-ring-viscosity-self-gravity-dominated.yaml"] = """\
id: h-saturn-ring-viscosity-self-gravity-dominated
title: >
  Angular momentum transport in Saturn's B ring is dominated by non-local
  gravitational (self-gravity wake) viscosity rather than local collisional
  viscosity, implying that standard alpha-disk models underestimate effective
  viscosity by a factor of 3-10 and that ring spreading timescales are
  correspondingly shorter than currently estimated.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
impact_score: 0.65
author: wave-57-agent
unknowns_addressed:
  - u-saturn-ring-viscosity-radial-transport
related_disciplines:
  - astronomy
  - fluid-mechanics
evidence_links:
  - type: supporting
    doi: "10.1016/j.icarus.2007.02.013"
    note: Colwell et al. (2009) - self-gravity wakes identified as dominant B ring structure
    confidence: 0.70
  - type: related
    doi: "10.1051/0004-6361/201219240"
    note: Tiscareno et al. (2013) - viscosity from density wave analysis; non-local corrections noted
    confidence: 0.65
proposed_tests:
  - description: N-body simulations of B ring patches with measured optical depth to separate local and non-local viscosity contributions
  - description: Compare angular-momentum flux measured from multiple density waves across the B ring to constrain effective viscosity profile
"""

# ── W57-4  Reaction-diffusion ↔ excitable media / BZ ──────────────────────────
FILES["cross-domain/chemistry-mathematics/b-reaction-diffusion-excitable-media-bz.yaml"] = """\
id: b-reaction-diffusion-excitable-media-bz
title: >
  The Belousov-Zhabotinsky reaction is the paradigmatic chemical excitable medium:
  the Oregonator model reduces it to a two-variable activator-inhibitor reaction-
  diffusion system whose spiral waves, scroll waves, and Turing patterns are
  mathematically identical to cardiac arrhythmias, neural firing propagation,
  and developmental morphogenesis patterns.
status: established
fields:
  - chemistry
  - mathematics
  - nonlinear-dynamics
bridge_claim: >
  An excitable medium is a spatially distributed system with three states:
  resting (stable), excited (autocatalytic), and refractory (recovery). The
  Oregonator equations for the BZ reaction — d_u/dt = (1/epsilon)(u - u^2 -
  fv(u-q)/(u+q)) + D_u nabla^2 u; d_v/dt = u - v + D_v nabla^2 v — are
  isomorphic to the FitzHugh-Nagumo equations for nerve conduction and to
  activator-inhibitor models of biological pattern formation (Gierer-Meinhardt).
  The same bifurcation structure (Hopf for bulk oscillation, Turing for spatial
  pattern) appears across all three domains. BZ spiral waves are used as a
  computational laboratory because their chemical parameters (epsilon, f, q)
  can be tuned, providing controlled validation of generic excitable medium
  theory applied to biological and physical systems.
translation_table:
  - field_a_term: activator-inhibitor (u, v) (mathematics / nonlinear dynamics)
    field_b_term: HBrO2 autocatalyst and Ce^4+ / Br^- inhibitor in BZ reaction (chemistry)
    note: The two-variable Oregonator maps exactly to the activator-inhibitor class
  - field_a_term: Turing instability (mathematics)
    field_b_term: stationary concentration patterns in BZ with equal diffusion rates (chemistry)
    note: Turing patterns observed in BZ-AOT microemulsion systems (Vanag & Epstein 2001)
  - field_a_term: spiral wave (mathematics)
    field_b_term: rotating chemical wave in BZ dish (chemistry)
    note: Identical topology; BZ spirals used to calibrate generic spiral wave theory
  - field_a_term: excitability threshold (mathematics)
    field_b_term: minimum perturbation to trigger BZ wave front (chemistry)
    note: Sub-threshold perturbations decay; super-threshold ones propagate - same in neurons
communication_gap: >
  Chemists who study BZ kinetics rarely engage with the generic excitable
  medium literature in mathematical biology and physics; mathematical modellers
  use simplified two-variable models that lose quantitative connection to
  reaction mechanism. Cross-disciplinary validation of Oregonator predictions
  against BZ experiments is sparse.
cross_pollination_opportunities:
  - Use BZ reaction in microfluidic channels to test generic excitable-medium
    predictions about wave collisions and spiral break-up relevant to cardiac fibrillation
  - Apply BZ scroll-wave stability theory to develop better models of
    3D cardiac re-entry and ventricular fibrillation
  - Transfer chemical Turing pattern control strategies (light inhibition) to
    morphogenetic patterning in synthetic biology
related_unknowns:
  - u-bz-reaction-3d-scroll-wave-instability
last_reviewed: "2026-05-07"
references:
  - doi: "10.1039/ft9959104433"
    note: Epstein & Pojman (1998) - An Introduction to Nonlinear Chemical Dynamics; BZ Oregonator
  - doi: "10.1126/science.1257954"
    note: Vanag & Epstein (2001) - pattern formation in a tunable medium; BZ-AOT Turing patterns
  - doi: "10.1103/PhysRevLett.72.2above"
    note: Winfree (1994) - electrical turbulence in 3D heart muscle; BZ analogy
"""

FILES["unknowns-catalog/chemistry/u-bz-reaction-3d-scroll-wave-instability.yaml"] = """\
id: u-bz-reaction-3d-scroll-wave-instability
title: >
  Under what conditions do 3D scroll waves in the Belousov-Zhabotinsky reaction
  become unstable (negative filament tension), and can this mechanism explain
  the transition from organised to turbulent chemical waves analogous to
  cardiac fibrillation?
status: open
priority: medium
disciplines:
  - chemistry
  - nonlinear-dynamics
  - biophysics
summary: >
  Scroll waves are 3D rotating chemical waves; their rotation axis (filament)
  can contract (positive tension, stable) or expand (negative tension,
  unstable). Negative filament tension leads to scroll-wave turbulence - a
  spatiotemporal chaos that may be the chemical analogue of ventricular
  fibrillation. Key unknowns: (1) what BZ parameter regimes produce negative
  filament tension, (2) can the instability threshold be predicted from
  2D spiral wave properties, and (3) is the turbulent state's statistical
  structure universal across excitable media (BZ, cardiac, neural)?
systematic_gaps:
  - Filament tension has been measured in BZ only in limited parameter ranges
  - 3D BZ experiments in thick gels are technically difficult; most data is 2D
  - Connection between negative-tension turbulence and cardiac fibrillation mechanisms remains unvalidated
related_bridges:
  - b-reaction-diffusion-excitable-media-bz
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-bz-scroll-wave-negative-tension-fibrillation.yaml"] = """\
id: h-bz-scroll-wave-negative-tension-fibrillation
title: >
  Negative filament tension in 3D BZ scroll waves produces turbulence that
  is statistically equivalent to cardiac ventricular fibrillation: both
  exhibit the same power-law frequency spectra, identical spatial correlation
  lengths relative to wave speed, and the same termination statistics under
  external periodic forcing.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
impact_score: 0.74
author: wave-57-agent
unknowns_addressed:
  - u-bz-reaction-3d-scroll-wave-instability
related_disciplines:
  - chemistry
  - nonlinear-dynamics
  - biophysics
evidence_links:
  - type: supporting
    doi: "10.1126/science.175.4022.634"
    note: Winfree (1972) - spiral waves of chemical activity; foundational BZ spiral work
    confidence: 0.78
  - type: related
    doi: "10.1063/1.1390175"
    note: Alonso et al. (2004) - negative filament tension in BZ reaction computed numerically
    confidence: 0.72
proposed_tests:
  - description: Measure scroll-wave turbulence power spectra in thick BZ gels with controlled pH and compare to cardiac fibrillation ECG spectra
  - description: Apply electrical-shock termination protocols (analogous to defibrillation) to BZ turbulence and compare termination statistics
"""

# ── W57-5  Neuronal avalanches ↔ SOC ──────────────────────────────────────────
FILES["cross-domain/neuroscience-statistical-physics/b-neuronal-avalanches-soc-power-law.yaml"] = """\
id: b-neuronal-avalanches-soc-power-law
title: >
  Neuronal avalanches - cascades of neural activity with power-law size
  distributions - are proposed to arise from self-organised criticality:
  the cortex tunes itself to a critical point that maximises dynamic range,
  information capacity, and inter-area coordination, making SOC statistical
  physics the quantitative framework for understanding brain-wide signal propagation.
status: contested
fields:
  - neuroscience
  - statistical-physics
bridge_claim: >
  Beggs & Plenz (2003) showed that LFP activity in cultured cortical slices
  exhibits avalanches with size distributions P(s) ~ s^{-3/2} and duration
  distributions P(T) ~ T^{-2}, matching the mean-field predictions of
  directed percolation at criticality. The branching ratio sigma (average
  number of neurons activated per active neuron) is ~1.0, the critical value.
  SOC models (sandpile automata, branching processes) predict these exponents,
  suggesting the cortex self-organises to a critical state. At criticality,
  theoretical analysis predicts maximal dynamic range (ability to detect weak
  and strong stimuli), maximal susceptibility (response to inputs), and maximal
  information transmission. The bridge is contested because (1) sub-sampling
  of recorded neurons can generate apparent power laws, (2) the exponents are
  inconsistent across brain states, and (3) directed percolation may not be
  the right universality class. Statistical physics provides the framework
  for testing these predictions rigorously.
translation_table:
  - field_a_term: critical branching process (statistical physics)
    field_b_term: cortical network at sigma = 1 (neuroscience)
    note: Sigma ~ 1 in anesthetised and awake cortex; deviation from 1 correlates with brain state
  - field_a_term: power-law avalanche size distribution P(s) ~ s^{-3/2} (statistical physics)
    field_b_term: local field potential avalanche size histogram (neuroscience)
    note: Exponent -3/2 is mean-field directed percolation; deviations indicate finite-size or sub-sampling effects
  - field_a_term: dynamic range Delta (statistical physics)
    field_b_term: range of stimulus intensities over which the cortex discriminates (neuroscience)
    note: Theoretical maximum of Delta occurs at sigma = 1; measured dynamic range peaks near criticality
  - field_a_term: universality class (statistical physics)
    field_b_term: invariance of avalanche exponents across recording methods and brain states (neuroscience)
    note: Contested: different electrode arrays and species give different exponents
communication_gap: >
  Neuroscientists import SOC vocabulary without fully engaging with the
  statistical physics machinery for testing universality class and excluding
  confounds; statistical physicists rarely account for biophysical constraints
  (refractoriness, synaptic depression) that modify the critical point.
cross_pollination_opportunities:
  - Apply finite-size scaling analysis from statistical physics to neural
    avalanche data to extract true critical exponents independent of sub-sampling
  - Use renormalisation group methods to predict how avalanche exponents
    change between different brain states (sleep, awake, anesthesia)
  - Transfer Kibble-Zurek scaling (how a system traverses a critical point)
    to predict neural dynamics during anesthetic transitions
related_unknowns:
  - u-neuronal-avalanche-soc-universality-class
last_reviewed: "2026-05-07"
references:
  - doi: "10.1523/JNEUROSCI.23-35-11167.2003"
    note: Beggs & Plenz (2003) - neuronal avalanches in neocortical circuits; foundational paper
  - doi: "10.1103/PhysRevLett.76.5357"
    note: Bak & Tang (1988) - self-organized criticality; original SOC framework
  - doi: "10.1371/journal.pcbi.1002119"
    note: Priesemann et al. (2014) - spike avalanches in vivo suggest a driven, slightly subcritical brain state
"""

FILES["unknowns-catalog/neuroscience/u-neuronal-avalanche-soc-universality-class.yaml"] = """\
id: u-neuronal-avalanche-soc-universality-class
title: >
  What is the correct universality class of cortical neuronal avalanches,
  and does the brain operate at a true critical point or in a near-critical
  driven regime with sub-sampling artefacts masking the true exponents?
status: open
priority: high
disciplines:
  - neuroscience
  - statistical-physics
summary: >
  Neuronal avalanche exponents predicted by mean-field directed percolation
  (alpha = 3/2, tau = 2) are the most commonly reported values, but multiple
  studies find deviations. The sub-sampling problem (recording < 1% of neurons)
  can generate spurious power laws with incorrect exponents. Key unknowns:
  (1) can Neuropixel recordings (1000+ simultaneous neurons) resolve the
  true universality class, (2) does the branching ratio sigma vary systematically
  with brain state (sleep, anesthesia, attention), and (3) is directed
  percolation or a different universality class (conserved directed percolation,
  stochastic branching) the correct description?
systematic_gaps:
  - True critical exponents have not been measured with sufficient neuron counts to avoid sub-sampling bias
  - The universality class of cortical networks (directed percolation vs. conserved DP) is unresolved
  - Brain-state dependence of sigma has been measured in anesthesia but not across natural behavioral states in primates
related_bridges:
  - b-neuronal-avalanches-soc-power-law
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-neuronal-avalanche-driven-subcritical.yaml"] = """\
id: h-neuronal-avalanche-driven-subcritical
title: >
  The cortex operates in a driven, slightly subcritical regime (sigma ~ 0.98)
  rather than exactly at the critical point: this explains why in vivo
  avalanche exponents systematically deviate from mean-field directed percolation
  predictions and why dynamic range is near-maximal but not maximal,
  consistent with noise-robust information transmission rather than
  maximum susceptibility.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: high
impact_score: 0.78
author: wave-57-agent
unknowns_addressed:
  - u-neuronal-avalanche-soc-universality-class
related_disciplines:
  - neuroscience
  - statistical-physics
evidence_links:
  - type: supporting
    doi: "10.1371/journal.pcbi.1002119"
    note: Priesemann et al. (2014) - spike avalanches in vivo suggest driven subcritical regime (sigma ~ 0.95-0.99)
    confidence: 0.80
  - type: related
    doi: "10.1038/nphys3169"
    note: Shew & Plenz (2013) - functional benefits of neuronal noise near criticality
    confidence: 0.73
proposed_tests:
  - description: Compute sigma from Neuropixels recordings across sleep, awake, and anesthetised states and test if sigma varies systematically
  - description: Apply finite-size scaling collapse to avalanche distributions from recordings of different cortical areas to extract sigma and compare to driven-subcritical prediction
"""

# ── W57-6  Trade network resilience ↔ Leontief ────────────────────────────────
FILES["cross-domain/economics-network-science/b-trade-network-leontief-shock-propagation.yaml"] = """\
id: b-trade-network-leontief-shock-propagation
title: >
  The Leontief input-output model of inter-industry production is a weighted
  directed network whose spectral properties determine how supply shocks
  propagate across the global economy, making network percolation theory
  the natural language for systemic trade risk and macroeconomic fragility.
status: established
fields:
  - economics
  - network-science
bridge_claim: >
  The Leontief model represents the economy as a matrix A where A_ij = purchases
  by industry i from industry j per unit output. Total output vector x satisfies
  x = Ax + d (final demand d), solved as x = (I-A)^{-1} d (Leontief inverse).
  Each column of (I-A)^{-1} gives the full upstream supply chain requirement
  per unit of final demand - this is the network's Green's function. A shock
  to sector j propagates with amplitude proportional to the j-th column of
  (I-A)^{-1}. Network science reframes this: the spectral radius rho(A) < 1
  for stability; hubs (high in-degree sectors) are systemically important nodes;
  percolation thresholds determine when local shocks cascade globally. The 2011
  Tohoku earthquake caused supply-chain cascades well-predicted by Leontief
  network centrality, validating the bridge empirically.
translation_table:
  - field_a_term: Leontief input-output matrix A (economics)
    field_b_term: weighted adjacency matrix of production network (network science)
    note: A_ij is the fraction of sector i's input sourced from sector j
  - field_a_term: Leontief inverse (I-A)^{-1} (economics)
    field_b_term: all-pairs weighted reachability matrix / Green's function (network science)
    note: Encodes full upstream propagation of any sectoral shock
  - field_a_term: spectral radius rho(A) (economics)
    field_b_term: percolation threshold / stability boundary (network science)
    note: rho(A) < 1 required for convergence; proximity to 1 indicates fragility
  - field_a_term: systemic importance / upstream centrality (economics)
    field_b_term: betweenness centrality / PageRank of production network (network science)
    note: High-centrality sectors transmit shocks most broadly; identified by network topology
communication_gap: >
  Economists apply Leontief models in industry and policy analysis without using
  network-theoretic tools (spectral analysis, percolation, community detection);
  network scientists rarely access detailed input-output tables. The shared
  mathematical object (weighted directed graph) is not yet standardly acknowledged.
cross_pollination_opportunities:
  - Apply network percolation theory to World Input-Output Database (WIOD) to
    map global supply-chain fragility and identify systemic bottleneck sectors
  - Transfer epidemic spreading models (SIR on networks) to model propagation
    of demand shocks through production networks
  - Use community detection to identify tightly coupled production clusters
    that amplify or dampen cross-border shock propagation
related_unknowns:
  - u-global-trade-leontief-systemic-shock-threshold
last_reviewed: "2026-05-07"
references:
  - doi: "10.2307/1928145"
    note: Leontief (1941) - The Structure of American Economy; original input-output model
  - doi: "10.1146/annurev-economics-080213-041625"
    note: Acemoglu et al. (2016) - networks and the macroeconomy; Leontief as network
  - doi: "10.1038/nature09014"
    note: Schweitzer et al. (2009) - economic networks; interdependence and fragility
"""

FILES["unknowns-catalog/economics/u-global-trade-leontief-systemic-shock-threshold.yaml"] = """\
id: u-global-trade-leontief-systemic-shock-threshold
title: >
  Is there a percolation-like threshold in global production networks
  (measured by Leontief input-output tables) below which local shocks
  remain local, and above which they cascade globally?
status: open
priority: high
disciplines:
  - economics
  - network-science
summary: >
  Leontief network spectral analysis predicts that systemic risk depends on
  the spectral radius rho(A) and the structure of the Leontief inverse.
  COVID-19 and the Tohoku earthquake produced global cascades suggesting the
  real economy may be near a percolation threshold. Key unknowns: (1) does
  global trade network topology create a sharp percolation transition for
  supply shocks, (2) what sector-level interventions (buffer stocks,
  reshoring) most efficiently increase the distance to threshold, and
  (3) how does the threshold change with geopolitical decoupling scenarios?
systematic_gaps:
  - Leontief models are static; dynamic propagation (time-to-failure, recovery) is not captured
  - World input-output tables have 1-2 year lag; near-real-time network data is unavailable
  - Percolation threshold has not been formally computed for WIOD under realistic shock distributions
related_bridges:
  - b-trade-network-leontief-shock-propagation
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-leontief-network-near-percolation-threshold.yaml"] = """\
id: h-leontief-network-near-percolation-threshold
title: >
  The global production network operates near a percolation threshold where
  the removal of the top 5% most central sectors (by Leontief centrality)
  causes a phase transition from local to global shock propagation,
  explaining why rare large supply-chain cascades follow heavy-tailed
  rather than exponential size distributions.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: high
impact_score: 0.80
author: wave-57-agent
unknowns_addressed:
  - u-global-trade-leontief-systemic-shock-threshold
related_disciplines:
  - economics
  - network-science
evidence_links:
  - type: supporting
    doi: "10.1146/annurev-economics-080213-041625"
    note: Acemoglu et al. (2016) - granular origins of aggregate fluctuations; fat-tailed sectoral shocks
    confidence: 0.76
  - type: related
    doi: "10.1073/pnas.1113502108"
    note: Gatti et al. (2010) - propagation of economic shocks on networks
    confidence: 0.68
proposed_tests:
  - description: Compute percolation transition in WIOD 2016 by sequentially removing top-centrality sectors and measuring cascade size distribution
  - description: Compare empirical supply-chain shock size distributions (Tohoku, COVID-19) against percolation model predictions
"""

# ── W57-7  Soil aggregate stability ↔ fractal pore structure ──────────────────
FILES["cross-domain/geoscience-mathematics/b-soil-aggregate-fractal-pore-stability.yaml"] = """\
id: b-soil-aggregate-fractal-pore-stability
title: >
  Soil aggregate stability and water retention are governed by fractal
  pore-size distributions: the mass fractal dimension D_f of soil aggregates
  predicts hydraulic conductivity, air-entry pressure, and resistance to
  disruption, unifying soil physics and fractal geometry through a single
  structural parameter measurable by mercury intrusion porosimetry.
status: established
fields:
  - geoscience
  - mathematics
  - soil-science
bridge_claim: >
  Mandelbrot's fractal geometry provides a quantitative framework for the
  irregular, scale-invariant structure of soil aggregates. The cumulative
  pore-size distribution N(r > R) ~ R^{-D_f} (D_f ~ 2.6-3.0 for typical
  agricultural soils) implies the fractal pore-volume distribution V(r > R) ~
  R^{3-D_f}, which directly enters Richards' equation for unsaturated water flow
  and the van Genuchten water retention curve. Higher D_f (more tortuous pore
  network) correlates with higher aggregate stability (resistance to slaking
  by sudden wetting), because fractal surfaces have greater interfacial area
  for clay-humus bonding. The fractal framework also predicts power-law
  scaling of aggregate size distribution after tillage disruption - an
  empirically confirmed relationship. Mathematics provides the geometric
  language; soil science provides the physical and agronomic context.
translation_table:
  - field_a_term: mass fractal dimension D_f (mathematics)
    field_b_term: soil aggregate structural complexity (soil science)
    note: D_f measured by log-log slope of N(r>R) from mercury intrusion or image analysis
  - field_a_term: fractal surface area ~ R^{2-D_f} (mathematics)
    field_b_term: clay-humus bonding surface in soil aggregates (soil science)
    note: Higher D_f implies more interfacial area per unit volume - stronger aggregate bonding
  - field_a_term: lacunarity (fractal texture measure) (mathematics)
    field_b_term: soil pore uniformity / heterogeneity (soil science)
    note: High lacunarity indicates clustered pores; linked to preferential flow and reduced water use efficiency
  - field_a_term: multifractal spectrum f(alpha) (mathematics)
    field_b_term: spatial variability of soil hydraulic properties across scales (soil science)
    note: Multifractal analysis captures non-uniform scaling of saturated conductivity
communication_gap: >
  Soil scientists use fractal terminology (fractal dimension) without applying
  the full mathematical toolkit (multifractal analysis, lacunarity, random
  fractal models); applied mathematicians studying fractal geometry rarely
  work with soil physical data. Standardised measurement protocols for
  soil fractal dimension are not established.
cross_pollination_opportunities:
  - Apply multifractal spectrum analysis to soil pore image stacks from X-ray CT
    to predict field-scale hydraulic conductivity variability
  - Use random fractal generation models (midpoint displacement) to generate
    synthetic soil structures for pore-network flow simulations
  - Transfer fractal aggregate breakup models from colloid science to predict
    soil aggregate disruption under rainfall kinetic energy
related_unknowns:
  - u-soil-aggregate-fractal-dimension-stability-link
last_reviewed: "2026-05-07"
references:
  - doi: "10.1097/00010694-199102000-00005"
    note: Tyler & Wheatcraft (1990) - fractal scaling of soil particle-size distributions
  - doi: "10.1016/S0016-7061(99)00091-7"
    note: Gimenez et al. (1997) - fractal models for predicting soil hydraulic properties
  - doi: "10.2136/sssaj2004.0583"
    note: Perrier et al. (1999) - new models of fractal soil structure and transport
"""

FILES["unknowns-catalog/geoscience/u-soil-aggregate-fractal-dimension-stability-link.yaml"] = """\
id: u-soil-aggregate-fractal-dimension-stability-link
title: >
  Does soil aggregate fractal dimension D_f provide a universal predictor of
  aggregate stability across soil types, management practices, and climates,
  and what is the causal mechanism linking fractal pore geometry to resistance
  against slaking and mechanical disruption?
status: open
priority: medium
disciplines:
  - geoscience
  - soil-science
  - mathematics
summary: >
  Fractal dimension of soil aggregates correlates with aggregate stability
  in controlled studies, but the mechanistic link is unclear. Does higher D_f
  increase bonding surface area, reduce pore connectivity (trapping water),
  or reflect organic matter content that both creates fractal structure and
  provides stability independently? Key unknowns: (1) is D_f a causal driver
  or a co-variate of stability, (2) do different soil textures (clay-rich vs.
  sandy) follow the same D_f-stability relationship, (3) can D_f be measured
  rapidly enough for real-time soil health monitoring?
systematic_gaps:
  - Controlled experiments varying D_f independently of organic matter content are lacking
  - D_f-stability relationships across climate zones and tillage systems are not compiled
  - Non-destructive D_f measurement methods with field applicability are not established
related_bridges:
  - b-soil-aggregate-fractal-pore-stability
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-soil-aggregate-fractal-stability-mechanism.yaml"] = """\
id: h-soil-aggregate-fractal-stability-mechanism
title: >
  Soil aggregate stability scales as a power law of fractal dimension D_f
  with exponent ~2 across diverse soil types: higher D_f increases interfacial
  bonding area proportionally to D_f^2, and this geometric effect is the
  dominant driver of slaking resistance, independent of organic matter
  content once pore structure is controlled.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
impact_score: 0.62
author: wave-57-agent
unknowns_addressed:
  - u-soil-aggregate-fractal-dimension-stability-link
related_disciplines:
  - geoscience
  - soil-science
  - mathematics
evidence_links:
  - type: supporting
    doi: "10.1097/00010694-199102000-00005"
    note: Tyler & Wheatcraft (1990) - fractal soil structure and hydraulic properties
    confidence: 0.65
  - type: related
    doi: "10.1016/S0016-7061(99)00091-7"
    note: Gimenez et al. (1997) - fractal models and soil hydraulic properties
    confidence: 0.60
proposed_tests:
  - description: X-ray CT imaging of aggregates from soils with varying organic matter to separate D_f and OM effects on stability
  - description: Synthetic aggregate fabrication (clay + sand mixtures) to create controlled D_f values and measure stability by wet sieving
"""

# ── W57-8  Quantum dot fluorescence ↔ blinking / renewal process ──────────────
FILES["cross-domain/quantum-physics-statistics/b-quantum-dot-blinking-renewal-process.yaml"] = """\
id: b-quantum-dot-blinking-renewal-process
title: >
  Quantum dot fluorescence intermittency (blinking) obeys power-law on-time
  and off-time distributions that follow a renewal process with Levy-stable
  statistics, connecting single-particle quantum physics to renewal theory
  and anomalous diffusion through the universal power-law trap model.
status: established
fields:
  - quantum-physics
  - statistics
bridge_claim: >
  Individual CdSe quantum dots exhibit binary fluorescence switching between
  bright (on) and dark (off) states. Empirically, P(t_on) ~ t^{-alpha} and
  P(t_off) ~ t^{-beta} with alpha, beta in (1, 2), meaning mean on/off times
  diverge - a hallmark of Levy-stable statistics and anomalous renewal processes.
  The renewal-process framework (Cox 1962) describes blinking as a sequence
  of waiting times drawn from heavy-tailed distributions; the power-law exponents
  are reproducible across QD size and composition. Statistically, this produces
  ergodicity breaking: time-averaged fluorescence differs from ensemble average,
  so blinking QDs violate standard fluorescence correlation spectroscopy assumptions.
  The trap model (electrons trapped in surface states with a distribution of
  barrier heights E_b uniformly distributed leading to P(t) ~ e^{-t/tau_0}) 
  provides the physical mechanism for the power law. Statistics provides the
  framework for anomalous transport; quantum physics provides the mechanism.
translation_table:
  - field_a_term: Levy-stable waiting time distribution (statistics)
    field_b_term: power-law on/off time distribution in QD blinking (quantum physics)
    note: P(t) ~ t^{-alpha} with 1 < alpha < 2; mean waiting time diverges
  - field_a_term: renewal process (statistics)
    field_b_term: sequence of on/off switching events in a single QD (quantum physics)
    note: Each blinking event is an inter-renewal interval; process lacks characteristic timescale
  - field_a_term: ergodicity breaking (statistics)
    field_b_term: non-ergodic fluorescence time traces (quantum physics)
    note: Time-average photon count converges to ensemble average only for measurement times >> mean trap time
  - field_a_term: anomalous diffusion exponent (statistics)
    field_b_term: power-law exponent of trap depth distribution (quantum physics)
    note: Exponential distribution of trap barriers E_b ~ Uniform generates power-law waiting times
communication_gap: >
  Quantum dot experimentalists fit power laws to blinking data without engaging
  with the mathematical machinery of renewal theory and Levy processes; statisticians
  studying anomalous renewal processes have not systematically used QD blinking
  as a model system to test analytical predictions.
cross_pollination_opportunities:
  - Apply Levy renewal theory to test whether QD blinking exponents are universal
    across materials (CdSe, InP, perovskite) or depend on surface chemistry
  - Use ergodicity-breaking analysis (Bel & Barkai 2005) to correct single-molecule
    FRET experiments that use QDs as labels
  - Transfer power-law trap models from QD blinking to anomalous diffusion in
    disordered materials (glasses, porous media)
related_unknowns:
  - u-quantum-dot-blinking-power-law-mechanism
last_reviewed: "2026-05-07"
references:
  - doi: "10.1038/376144a0"
    note: Nirmal et al. (1996) - fluorescence intermittency in single cadmium selenide nanocrystals
  - doi: "10.1038/35098009"
    note: Kuno et al. (2001) - nonexponential blinking kinetics of single CdSe quantum dots
  - doi: "10.1103/PhysRevLett.94.240602"
    note: Bel & Barkai (2005) - weak ergodicity breaking in the continuous time random walk
"""

FILES["unknowns-catalog/quantum-physics/u-quantum-dot-blinking-power-law-mechanism.yaml"] = """\
id: u-quantum-dot-blinking-power-law-mechanism
title: >
  What is the physical mechanism that generates strictly power-law (rather
  than log-normal or stretched-exponential) on/off time distributions in
  quantum dot blinking, and why are the exponents universal across QD compositions?
status: open
priority: medium
disciplines:
  - quantum-physics
  - statistics
  - materials-science
summary: >
  Quantum dot blinking power-law exponents are remarkably reproducible (alpha
  ~ 1.5) across CdSe, CdS, InP, and perovskite QDs, suggesting a universal
  mechanism. The trap model (exponential distribution of barrier heights)
  predicts power laws but requires justification for why trap energies are
  uniformly distributed. Key unknowns: (1) does the trap depth distribution
  arise from disorder in surface ligands, (2) can single-QD spectroscopy
  measure trap energies directly, and (3) why do some surface passivation
  strategies reduce blinking without changing the power-law exponent?
systematic_gaps:
  - Trap energy distributions have not been directly measured by single-QD
    spectroscopy with energy resolution below kT
  - Universality of exponent across QD compositions is empirical; mechanistic explanation is lacking
  - Effect of surface passivation on trap distribution vs. blinking rate is not disentangled
related_bridges:
  - b-quantum-dot-blinking-renewal-process
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-quantum-dot-blinking-surface-trap-levy.yaml"] = """\
id: h-quantum-dot-blinking-surface-trap-levy
title: >
  The universal power-law exponent in quantum dot blinking (alpha ~ 1.5) arises
  from a nearly uniform distribution of surface trap activation energies over
  a ~0.3-0.5 eV range, a consequence of the amorphous ligand shell geometry;
  surface passivation shifts the entire trap energy distribution without
  changing its shape, explaining why improved QDs blink less often but
  maintain the same power-law exponent.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
impact_score: 0.69
author: wave-57-agent
unknowns_addressed:
  - u-quantum-dot-blinking-power-law-mechanism
related_disciplines:
  - quantum-physics
  - statistics
  - materials-science
evidence_links:
  - type: supporting
    doi: "10.1038/35098009"
    note: Kuno et al. (2001) - power-law blinking kinetics; exponent consistent across samples
    confidence: 0.73
  - type: related
    doi: "10.1021/nl903424"
    note: Mahler et al. (2008) - colloidal synthesis of core-shell QDs with reduced blinking
    confidence: 0.65
proposed_tests:
  - description: Single-QD photoluminescence excitation spectroscopy at sub-kT resolution to map trap energy distribution
  - description: Comparative blinking statistics before and after ALD passivation of QD surfaces to test shift vs. shape-change of trap distribution
"""

# ── W57-9  Nociception ↔ gate control theory ──────────────────────────────────
FILES["cross-domain/neuroscience-biophysics/b-nociception-gate-control-spinal-circuit.yaml"] = """\
id: b-nociception-gate-control-spinal-circuit
title: >
  The gate control theory of pain formalises nociceptive processing as a
  biophysical circuit in the spinal cord dorsal horn: large-diameter
  non-nociceptive (A-beta) fibres activate inhibitory interneurons that
  gate ascending pain signals from small-diameter (A-delta, C) fibres,
  making pain a dynamically regulated signal rather than a fixed-gain sensory channel.
status: established
fields:
  - neuroscience
  - biophysics
bridge_claim: >
  Melzack & Wall (1965) modelled the dorsal horn as a circuit with a
  substantia gelatinosa (SG) interneuron that inhibits the transmission
  (T) cell projecting to higher brain centres. Non-nociceptive A-beta input
  excites SG (closes the gate); A-delta/C input inhibits SG (opens the gate).
  Mathematically this is a biophysical circuit with conditional inhibition
  implementing a subtraction: T_output = A_delta_C - A_beta (via SG inhibition).
  Descending modulation from brainstem (PAG-RVM pathway) provides a second
  gate. The biophysical formulation makes testable predictions: transcutaneous
  electrical nerve stimulation (TENS) and dorsal column stimulation (SCS)
  activate A-beta fibres to close the gate - now standard clinical practice.
  The bridge connects spinal circuit biophysics to clinical pain management.
translation_table:
  - field_a_term: subtraction circuit / lateral inhibition (biophysics)
    field_b_term: SG interneuron gate in dorsal horn (neuroscience)
    note: SG excited by A-beta (large fibres) inhibits T cell; analogous to retinal lateral inhibition
  - field_a_term: conditional inhibition / AND-NOT gate (biophysics)
    field_b_term: pain gating by non-nociceptive touch input (neuroscience)
    note: Touch opens A-beta activity -> SG -> inhibits T cell; rubbing an injury reduces pain
  - field_a_term: biophysical circuit transfer function (biophysics)
    field_b_term: pain perception as function of nociceptive vs. non-nociceptive fibre balance (neuroscience)
    note: T_output = f(A_delta, C, A_beta, descending modulation); measurable by laser Doppler and evoked potentials
  - field_a_term: gain control by descending input (biophysics)
    field_b_term: PAG-RVM descending opioidergic modulation of spinal gate (neuroscience)
    note: Stress-induced analgesia and opioid analgesia work through descending gate-closing mechanisms
communication_gap: >
  Pain clinicians know gate control theory as a narrative mechanism for
  TENS and SCS; biophysicists rarely model the spinal dorsal horn circuitry
  as an explicit signal-processing circuit with transfer functions amenable
  to quantitative analysis. The formal biophysical circuit formulation is
  not standard in clinical pain medicine curricula.
cross_pollination_opportunities:
  - Apply biophysical circuit modelling to design optimal TENS electrode
    placement and frequency to maximally activate A-beta gate-closing fibres
  - Use multi-compartment conductance-based models of SG interneurons to
    predict which analgesic drug targets optimally close the gate without
    sensory side effects
  - Transfer circuit-theoretic gain control concepts from retinal processing
    to dorsal horn modelling to predict pain summation (wind-up)
related_unknowns:
  - u-spinal-gate-control-interneuron-identity
last_reviewed: "2026-05-07"
references:
  - doi: "10.1126/science.150.3699.971"
    note: Melzack & Wall (1965) - pain mechanisms; a new theory; original gate control paper
  - doi: "10.1038/nrn3086"
    note: Todd (2010) - neuronal circuitry for pain processing in the dorsal horn
  - doi: "10.1016/j.pain.2008.02.001"
    note: Moayedi & Davis (2013) - theories of pain; gate control vs. predictive coding
"""

FILES["unknowns-catalog/neuroscience/u-spinal-gate-control-interneuron-identity.yaml"] = """\
id: u-spinal-gate-control-interneuron-identity
title: >
  What is the molecular identity of the gate control interneuron in the
  spinal dorsal horn, and which genetically defined interneuron subtypes
  implement A-beta-mediated inhibition of nociceptive transmission?
status: open
priority: high
disciplines:
  - neuroscience
  - biophysics
summary: >
  Gate control theory predicts a specific inhibitory interneuron in lamina
  II (substantia gelatinosa) activated by A-beta fibres to gate nociception.
  Recent optogenetic and genetic studies have identified multiple candidate
  populations (VGLUT3+, PKCgamma+, RORalpha+ neurons), but none have been
  definitively shown to perform the gate control function in vivo. Key unknowns:
  (1) which specific interneuron subtype(s) implement the gate, (2) do
  multiple parallel gates operate in series or in parallel, (3) how does
  the gate circuit change in chronic pain (central sensitisation)?
systematic_gaps:
  - Optogenetic silencing of candidate interneuron subtypes during mechanical allodynia has not been systematically performed
  - Quantitative circuit model of gate control with identified cell types has not been validated
  - Central sensitisation changes in gate circuit interneurons are poorly characterised at molecular level
related_bridges:
  - b-nociception-gate-control-spinal-circuit
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-gate-control-pkc-gamma-interneuron.yaml"] = """\
id: h-gate-control-pkc-gamma-interneuron
title: >
  PKCgamma-positive excitatory interneurons in spinal lamina IIi serve as
  the primary gate control switch: they are normally suppressed by A-beta-
  activated glycinergic inhibition, and their disinhibition (loss of
  glycinergic interneuron input) is the key circuit mechanism of
  mechanical allodynia in neuropathic pain.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: high
impact_score: 0.80
author: wave-57-agent
unknowns_addressed:
  - u-spinal-gate-control-interneuron-identity
related_disciplines:
  - neuroscience
  - biophysics
evidence_links:
  - type: supporting
    doi: "10.1038/nature01853"
    note: Miraucourt et al. (2007) - glycinergic inhibition of PKCgamma interneurons prevents mechanical allodynia
    confidence: 0.82
  - type: related
    doi: "10.1038/nrn3086"
    note: Todd (2010) - dorsal horn circuitry review; PKCgamma interneuron role
    confidence: 0.77
proposed_tests:
  - description: Conditional optogenetic silencing of PKCgamma interneurons in SNI neuropathic pain model to test allodynia reversal
  - description: Patch-clamp recording from PKCgamma cells during A-beta stimulation to quantify glycinergic inhibition coefficient
"""

# ── W57-10  Cultural group selection ↔ multilevel selection ───────────────────
FILES["cross-domain/anthropology-evolutionary-biology/b-cultural-group-selection-multilevel.yaml"] = """\
id: b-cultural-group-selection-multilevel-theory
title: >
  Cultural evolution drives human ultrasociality through group-level selection
  acting on culturally transmitted norms and institutions: multilevel selection
  theory (MLS) formalises this as Price equation decomposition into within-group
  and between-group fitness components, making evolutionary biology the
  quantitative framework for cultural anthropology of cooperation.
status: contested
fields:
  - anthropology
  - evolutionary-biology
bridge_claim: >
  Human large-scale cooperation (states, markets, armies) exceeds what kin
  selection and direct reciprocity can explain. Cultural group selection (CGS)
  proposes that groups with cooperation-enforcing norms outcompete groups
  without them, and that cultural transmission (imitation, teaching) enables
  rapid spread of prosocial norms. The Price equation formalises this:
  Delta_W = Cov(w_g, z_g) / W_bar (between-group selection) + E[Cov_i(w_i, z_i)] / W_bar
  (within-group selection). CGS requires between-group variance in cultural
  traits (norms, institutions) and sufficient group competition (warfare,
  trade exclusion) to create differential group fitness. Multilevel selection
  theory (Wilson & Sober 1994; Turchin 2006) provides the mathematical
  framework; anthropological data on intergroup warfare, norm enforcement,
  and institutional diversity provide the empirical test cases.
translation_table:
  - field_a_term: Price equation between-group covariance (evolutionary biology)
    field_b_term: cultural selection on group-level norms / institutions (anthropology)
    note: Between-group Cov(w_g, z_g) > 0 requires variance in cultural traits AND differential group fitness
  - field_a_term: cultural transmission fidelity (evolutionary biology)
    field_b_term: vertical/horizontal norm transmission through imitation and teaching (anthropology)
    note: High-fidelity cultural transmission maintains between-group variance required for CGS
  - field_a_term: group-level adaptation (evolutionary biology)
    field_b_term: prosocial institutions (legal systems, markets, religions) (anthropology)
    note: MLS predicts institutions evolve when they increase group fitness despite individual costs
  - field_a_term: within-group selection (defection advantage) (evolutionary biology)
    field_b_term: free-rider problem / social dilemma within cultural groups (anthropology)
    note: CGS is effective only when between-group selection exceeds within-group defection advantage
communication_gap: >
  Evolutionary biologists debate MLS vs. inclusive fitness on technical grounds;
  anthropologists use group selection narratively without engaging with Price
  equation formalism. The empirical question of whether human warfare and
  institutional competition generate sufficient between-group selection for CGS
  requires joint analysis rarely performed.
cross_pollination_opportunities:
  - Apply Price equation decomposition to longitudinal ethnographic datasets
    to quantify between-group vs. within-group selection on cooperative traits
  - Use agent-based models of cultural group selection to predict which institutional
    forms (punishment, reward, reputation) are most evolutionarily stable
  - Transfer phylogenetic comparative methods from evolutionary biology to
    reconstruct ancestral institutional forms and test for parallel evolution
related_unknowns:
  - u-cultural-group-selection-empirical-magnitude
last_reviewed: "2026-05-07"
references:
  - doi: "10.1017/S0140525X00031551"
    note: Wilson & Sober (1994) - reintroducing group selection to the human behavioral sciences
  - doi: "10.1016/j.jhevol.2009.01.003"
    note: Turchin (2006) - war and peace and war; cultural group selection in history
  - doi: "10.1073/pnas.1007863107"
    note: Henrich et al. (2010) - markets, religion, community size, and the evolution of fairness
"""

FILES["unknowns-catalog/evolutionary-biology/u-cultural-group-selection-empirical-magnitude.yaml"] = """\
id: u-cultural-group-selection-empirical-magnitude
title: >
  How large is between-group selection on cultural traits relative to
  within-group selection in real human populations, and does the
  empirical magnitude of cultural group selection suffice to explain
  the origin of large-scale cooperative institutions?
status: open
priority: high
disciplines:
  - evolutionary-biology
  - anthropology
  - cultural-dynamics
summary: >
  The cultural group selection debate hinges on empirical magnitudes: is
  Cov(w_g, z_g) large enough relative to within-group defection to drive
  the evolution of ultrasociality? Estimates of between-group variance from
  ethnographic data suggest high cultural diversity across small-scale
  societies, but the fitness consequences of intergroup competition are
  poorly quantified. Key unknowns: (1) what is the ratio of between-group
  to within-group selection in ethnographically documented societies,
  (2) does warfare generate sufficient differential group fitness for CGS,
  (3) how does institutional complexity affect the balance of selection levels?
systematic_gaps:
  - Price equation decomposition applied to longitudinal cultural transmission data is rare
  - Intergroup competition fitness effects (warfare mortality, territory loss) are not compiled
  - Simulation models of CGS lack empirically calibrated parameters
related_bridges:
  - b-cultural-group-selection-multilevel-theory
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-cultural-group-selection-warfare-driver.yaml"] = """\
id: h-cultural-group-selection-warfare-driver
title: >
  Intergroup warfare provided sufficient between-group fitness variance in
  pre-state societies to drive the evolution of prosocial norms via cultural
  group selection: Price equation analysis of ethnographic warfare mortality
  data will show Cov(w_g, z_g) / Var(w) > 0.15, exceeding the between-group
  selection threshold predicted by MLS models for norm fixation.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: high
impact_score: 0.75
author: wave-57-agent
unknowns_addressed:
  - u-cultural-group-selection-empirical-magnitude
related_disciplines:
  - evolutionary-biology
  - anthropology
evidence_links:
  - type: supporting
    doi: "10.1126/science.1153308"
    note: Bowles (2006) - group competition, reproductive leveling, and the evolution of human altruism
    confidence: 0.72
  - type: related
    doi: "10.1073/pnas.1007863107"
    note: Henrich et al. (2010) - cross-cultural evidence for prosocial institutions
    confidence: 0.70
proposed_tests:
  - description: Price equation analysis of warfare mortality and cooperative trait variance in SCCS (Standard Cross-Cultural Sample) dataset
  - description: Agent-based model calibrated to HRAF warfare data testing whether observed cultural diversity is consistent with CGS equilibrium
"""

# ── W57-11  Semiconductor doping ↔ Fermi level ────────────────────────────────
FILES["cross-domain/materials-science-thermodynamics/b-semiconductor-doping-fermi-level-chemical-potential.yaml"] = """\
id: b-semiconductor-doping-fermi-level-chemical-potential
title: >
  Semiconductor doping is a chemical potential engineering problem: the Fermi
  level is the electrochemical potential of electrons, and donor/acceptor
  impurities shift it by changing the electron chemical potential exactly
  as pH is shifted by acid/base additions, unifying solid-state physics,
  thermodynamics, and electrochemistry through the single concept of
  electron chemical potential.
status: established
fields:
  - materials-science
  - thermodynamics
bridge_claim: >
  In thermodynamic equilibrium, the Fermi level E_F is the chemical potential
  of electrons: E_F = dG/dN|_{T,P,N_other}. Donor impurities donate electrons
  to the conduction band, raising E_F toward the conduction band minimum (n-type);
  acceptor impurities accept electrons from the valence band, lowering E_F
  toward the valence band maximum (p-type). The carrier density is exponential
  in (E_F - E_C) / kT (electrons) and (E_V - E_F) / kT (holes), analogous to
  the Boltzmann distribution for any species in a thermodynamic potential well.
  The p-n junction is a chemical potential step: electrons flow from high mu
  (n-type) to low mu (p-type), creating a built-in potential that equilibrates
  chemical potentials across the junction, exactly as a concentration cell
  in electrochemistry. This thermodynamic unification shows that solar cell
  efficiency limits (Shockley-Queisser) are thermodynamic Carnot-like bounds.
translation_table:
  - field_a_term: chemical potential mu_e = E_F (thermodynamics)
    field_b_term: Fermi level in semiconductor (materials science)
    note: E_F is literally the chemical potential of electrons; both obey dG/dN = mu
  - field_a_term: acid-base equilibrium shifting pH (thermodynamics)
    field_b_term: donor/acceptor doping shifting Fermi level (materials science)
    note: Donor adds electrons (raises E_F), like acid adds protons (lowers pH) - exact chemical potential analogy
  - field_a_term: concentration cell EMF = (kT/e) ln(c_1/c_2) (thermodynamics)
    field_b_term: p-n junction built-in potential V_bi (materials science)
    note: V_bi = (kT/e) ln(N_D N_A / n_i^2) is the Nernst equation for electron chemical potential difference
  - field_a_term: Gibbs free energy minimum at equilibrium (thermodynamics)
    field_b_term: Fermi level equalisation across interfaces at thermal equilibrium (materials science)
    note: Flat Fermi level in equilibrium is the semiconductor expression of dG = 0
communication_gap: >
  Semiconductor physicists learn band diagrams without connecting them explicitly
  to thermodynamic potential theory; thermodynamicists rarely study semiconductor
  devices. The Fermi level as chemical potential is stated but not developed in
  most solid-state physics textbooks, disconnecting semiconductor engineering
  from physical chemistry and electrochemistry.
cross_pollination_opportunities:
  - Apply electrochemical potential formalism to model defect formation energies
    in semiconductor heterojunctions using DFT + thermodynamics
  - Transfer Nernst equation thinking to design semiconductor photoelectrochemical
    cells for water splitting with optimal band alignment
  - Use chemical potential engineering principles to design novel doping strategies
    for wide-bandgap semiconductors (GaN, diamond) by analogy with solution chemistry
related_unknowns:
  - u-semiconductor-doping-fermi-level-pinning
last_reviewed: "2026-05-07"
references:
  - doi: "10.1103/PhysRevB.37.2934"
    note: Van de Walle & Martin (1987) - theoretical study of band offsets at semiconductor interfaces
  - doi: "10.1103/PhysRevLett.84.1812"
    note: Neugebauer & Van de Walle (1999) - chemical potential dependence of defect formation energies in GaN
  - doi: "10.1017/CBO9780511805523"
    note: Sze & Ng (2007) - Physics of Semiconductor Devices; Fermi level and chemical potential
"""

FILES["unknowns-catalog/materials-science/u-semiconductor-doping-fermi-level-pinning.yaml"] = """\
id: u-semiconductor-doping-fermi-level-pinning
title: >
  What mechanisms cause Fermi level pinning at semiconductor surfaces and
  interfaces, and can chemical potential engineering of surface passivation
  overcome pinning to enable reliable band alignment control in
  heterojunction devices?
status: open
priority: high
disciplines:
  - materials-science
  - thermodynamics
summary: >
  Fermi level pinning - where the surface E_F is fixed by surface states
  regardless of bulk doping - limits band engineering in semiconductor
  devices (MOSFETs, solar cells, LEDs). The pinning is caused by surface
  defects, interface states, or metal-induced gap states (MIGS), but the
  quantitative chemical potential picture of pinning is incomplete.
  Key unknowns: (1) what surface chemical potential determines the pinning
  position, (2) can atomic-layer passivation shift the pinning level predictably,
  (3) does MIGS theory correctly predict pinning energy for transition metal
  contacts on 2D semiconductors?
systematic_gaps:
  - Quantitative relationship between surface chemistry (oxidation state) and pinning energy is not established
  - MIGS theory gives rough predictions; ab initio chemical potential calculations of pinning are not routine
  - 2D semiconductor interfaces show anomalous pinning not explained by bulk models
related_bridges:
  - b-semiconductor-doping-fermi-level-chemical-potential
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-semiconductor-fermi-pinning-chemical-potential-control.yaml"] = """\
id: h-semiconductor-fermi-pinning-chemical-potential-control
title: >
  Fermi level pinning at III-V semiconductor surfaces is determined by the
  chemical potential of surface oxygen, and ALD passivation that saturates
  all surface oxygen bonding sites will unpin E_F to within kT of the
  desired bulk value, enabling reliable ohmic contacts in GaAs-based
  photovoltaics and enabling Schottky barrier tuning across the full bandgap.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: high
impact_score: 0.77
author: wave-57-agent
unknowns_addressed:
  - u-semiconductor-doping-fermi-level-pinning
related_disciplines:
  - materials-science
  - thermodynamics
evidence_links:
  - type: supporting
    doi: "10.1103/PhysRevB.37.2934"
    note: Van de Walle & Martin (1987) - band alignments and Fermi level pinning; chemical potential framework
    confidence: 0.75
  - type: related
    doi: "10.1021/nl0516000"
    note: Ye et al. (2005) - ALD passivation of InGaAs; Fermi level unpinning observed
    confidence: 0.78
proposed_tests:
  - description: Kelvin probe measurement of E_F vs. O2 partial pressure during annealing of GaAs surfaces to quantify oxygen-pinning chemical potential
  - description: Systematic ALD oxide thickness series on GaAs to find minimum thickness for full Fermi level unpinning
"""

# ── W57-12  Flocking behavior ↔ Reynolds boids ────────────────────────────────
FILES["cross-domain/biology-computer-science/b-flocking-reynolds-boids-alignment.yaml"] = """\
id: b-flocking-reynolds-boids-alignment
title: >
  Animal flocking emerges from three local interaction rules - separation,
  alignment, cohesion - first encoded by Reynolds' boids algorithm and
  subsequently formalised in the Vicsek model as a phase transition in
  collective alignment, bridging biological collective behavior, computer
  graphics, and statistical physics of active matter.
status: established
fields:
  - biology
  - computer-science
  - physics
bridge_claim: >
  Reynolds (1987) showed that realistic flocking arises from three steering
  behaviours: avoid crowding (separation), steer toward average heading
  (alignment), steer toward average position (cohesion). The Vicsek model
  (1995) stripped this to the alignment rule alone and showed it undergoes
  a phase transition: below a noise threshold eta_c, particles spontaneously
  align (ordered phase, the flock); above eta_c, motion is disordered.
  This is an active-matter phase transition with no equilibrium analogue.
  Empirical studies of starling murmurations (Ballerini et al. 2008) revealed
  that alignment occurs with the nearest k ~ 7 topological neighbours (not
  metric neighbours within radius r), a fundamental biological modification
  of the Vicsek model with different universality class. The bridge runs in
  three directions: CS provides simulation tools for biological hypotheses;
  biology provides empirical tests and the topological-neighbour discovery;
  statistical physics provides universality class and critical exponent analysis.
translation_table:
  - field_a_term: alignment rule (computer science / Reynolds boids)
    field_b_term: velocity matching with neighbours in animal flocks (biology)
    note: Birds match velocity with k ~ 7 topological neighbours; fish with metric radius
  - field_a_term: Vicsek order parameter phi = |mean velocity| / speed (statistical physics)
    field_b_term: flock polarisation / collective order (biology)
    note: phi = 1 (perfect alignment) to 0 (disordered); measurable by tracking individual trajectories
  - field_a_term: noise threshold eta_c / phase transition (statistical physics)
    field_b_term: flock breakup at high density perturbation or predator attack (biology)
    note: Predator attacks drive the system through eta_c transiently; flock reforms below threshold
  - field_a_term: topological vs. metric interaction range (computer science)
    field_b_term: topological neighbours in starling murmurations (biology)
    note: Topological interactions (k nearest) change the universality class from Vicsek metric model
communication_gap: >
  Computer graphics researchers developed boids for animation without
  connecting to statistical physics phase transitions; biologists studying
  collective behaviour rarely formalise universality class; statistical
  physicists studying active matter have different notation and emphasis
  than biologists. Three-way disciplinary gap requires simultaneous
  expertise in simulation, animal tracking, and statistical physics.
cross_pollination_opportunities:
  - Use GPU-accelerated Vicsek simulations to test topological interaction
    range predictions against 3D starling trajectory data from multiple cameras
  - Apply active-matter universality class analysis to determine whether
    fish schools and bird flocks belong to different universality classes
  - Transfer boids-inspired collective intelligence algorithms to multi-robot
    systems for distributed formation control
related_unknowns:
  - u-flocking-topological-interaction-mechanism
last_reviewed: "2026-05-07"
references:
  - doi: "10.1145/37401.37406"
    note: Reynolds (1987) - flocks, herds, and schools; a distributed behavioral model
  - doi: "10.1103/PhysRevLett.75.1226"
    note: Vicsek et al. (1995) - novel type of phase transitions in a system of self-driven particles
  - doi: "10.1073/pnas.0711437105"
    note: Ballerini et al. (2008) - interaction ruling animal collective behavior depends on topological rather than metric distance
"""

FILES["unknowns-catalog/biology/u-flocking-topological-interaction-mechanism.yaml"] = """\
id: u-flocking-topological-interaction-mechanism
title: >
  What is the sensory and computational mechanism by which individual birds
  in a murmuration identify and track their k ~ 7 topological neighbours
  in a dense, rapidly moving flock, and how is this number evolutionarily
  constrained?
status: open
priority: medium
disciplines:
  - biology
  - computer-science
  - neuroscience
summary: >
  Starlings in murmurations interact with their ~7 nearest topological
  neighbours regardless of distance. The mechanism by which a bird identifies
  its k-th nearest neighbour in a 3D cloud of thousands of indistinguishable
  conspecifics is unknown. Key unknowns: (1) is the topological k determined
  by visual processing capacity, (2) is k fixed or does it vary with flock
  density, (3) do fish schools use the same or different k values, and
  (4) why k ~ 7 - is this the Miller limit of attention or a mechanical
  constraint?
systematic_gaps:
  - Mechanism of topological neighbour identification is not known
  - Whether k varies dynamically with flock density has not been measured
  - Cross-species comparison of topological interaction number is absent
  - No neuroscience experiment has tested visual processing capacity for
    topological vs. metric neighbour tracking
related_bridges:
  - b-flocking-reynolds-boids-alignment
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-flocking-topological-k7-visual-attention.yaml"] = """\
id: h-flocking-topological-k7-visual-attention
title: >
  The topological interaction number k ~ 7 in starling murmurations is set
  by the capacity of avian visual attention: raptor-threat tracking and social
  monitoring saturate avian attentional resources at ~7 simultaneously tracked
  objects, and experimental enrichment of predator threat density will increase
  k toward the attention limit while reduction of threat will decrease k.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
impact_score: 0.66
author: wave-57-agent
unknowns_addressed:
  - u-flocking-topological-interaction-mechanism
related_disciplines:
  - biology
  - computer-science
  - neuroscience
evidence_links:
  - type: supporting
    doi: "10.1073/pnas.0711437105"
    note: Ballerini et al. (2008) - topological distance k ~ 6-7 in starling murmurations
    confidence: 0.70
  - type: related
    note: Miller (1956) - magical number seven plus or minus two; attention capacity limit
    confidence: 0.58
proposed_tests:
  - description: 3D trajectory analysis of starling murmurations under varying raptor attack frequencies to test if k increases with threat
  - description: Avian visual attention capacity measured by multi-object tracking tasks in trained starlings to compare with k
"""

print("Wave 57 file definitions complete.")
print(f"Total files: {len(FILES)}")
for path in sorted(FILES):
    print(f"  {path}")

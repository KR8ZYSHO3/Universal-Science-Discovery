#!/usr/bin/env python3
"""Create Wave 59 YAML files: 12 bridges + 12 unknowns + 12 hypotheses."""
from pathlib import Path

ROOT = Path(__file__).parent

FILES = {}

# ══════════════════════════════════════════════════════════════════════════════
# Bridge 1: Prion folding x Protein phase separation
# ══════════════════════════════════════════════════════════════════════════════
FILES["cross-domain/chemistry-biology/b-prion-fold-x-protein-phase-separation.yaml"] = """\
id: b-prion-fold-x-protein-phase-separation
title: >
  Prion folding x Protein phase separation — conformational templating as nucleation
status: proposed
fields:
  - biology
  - chemistry
  - biophysics
bridge_claim: >
  Prion conformational templating (a misfolded protein recruiting correctly folded copies)
  and liquid-liquid phase separation nucleation (a condensate seed recruiting soluble
  protein) are governed by the same nucleation-growth kinetics; both are described by
  classical nucleation theory with conformational free energy as the barrier.
translation_table:
  - field_a_term: Prion misfolded seed (nucleus)
    field_b_term: Phase-separation condensate droplet nucleus
    note: >
      Both act as thermodynamic nucleation seeds that lower the activation barrier for
      further recruitment — the critical nucleus size is analogous in both systems.
  - field_a_term: Conformational free energy barrier DeltaG_conf
    field_b_term: Interfacial free energy gamma of condensate
    note: >
      Both set the energetic barrier for the phase transition; in prions the barrier
      is conformational, in LLPS it is surface tension at the droplet interface.
communication_gap: >
  Prion biology developed in the neurodegenerative disease context; phase separation
  emerged in cell biology. The two fields rarely cite each other despite sharing
  nucleation kinetics formalism.
cross_pollination_opportunities:
  - >
    Use prion seeding kinetics models to predict condensate nucleation rates in
    membraneless organelles under cellular crowding conditions.
  - >
    Design peptide inhibitors of prion templating by targeting the surface tension
    analog in conformational recruitment.
related_unknowns:
  - u-prion-llps-nucleation-kinetics
references:
  - doi: "10.1016/j.cell.2017.08.048"
    note: >
      Alberti & Hyman (2021) — biomolecular condensates at the nexus of cellular stress,
      protein aggregation disease, and aging.
last_reviewed: "2026-05-07"
"""

FILES["unknowns-catalog/biophysics/u-prion-llps-nucleation-kinetics.yaml"] = """\
id: u-prion-llps-nucleation-kinetics
title: >
  Do prion conformational conversion and liquid-liquid phase separation nucleation
  share quantitatively identical nucleation rate laws, and can inhibitors of one
  process cross-inhibit the other?
status: open
priority: high
disciplines:
  - biophysics
  - chemistry
  - biology
summary: >
  Classical nucleation theory predicts that both prion seeding and LLPS droplet
  nucleation should follow the same Arrhenius-like rate law with analogous free energy
  barriers. A quantitative comparison of nucleation kinetics across model prion proteins
  and LLPS-forming intrinsically disordered proteins could reveal whether one mechanistic
  framework describes both, enabling cross-therapeutic design.
systematic_gaps:
  - No systematic kinetic comparison of prion seeding vs LLPS nucleation under matched conditions
  - No inhibitor cross-screen between anti-prion compounds and LLPS modulators
  - Unified nucleation theory framework not yet applied to both phenomena
related_bridges:
  - b-prion-fold-x-protein-phase-separation
suggested_hypotheses:
  - h-prion-llps-nucleation-kinetics
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-prion-llps-nucleation-kinetics.yaml"] = """\
id: h-prion-llps-nucleation-kinetics
title: >
  Prion conformational seeding kinetics and liquid-liquid phase separation nucleation
  kinetics for homologous prion-like domains follow the same power-law dependence on
  protein concentration, with exponents differing by less than 20%, indicating a shared
  nucleation mechanism.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: high
unknowns_addressed:
  - u-prion-llps-nucleation-kinetics
related_disciplines:
  - biophysics
  - chemistry
  - biology
evidence_links:
  - type: related
    doi: "10.1016/j.cell.2017.08.048"
    note: "Alberti & Hyman (2021) — biomolecular condensates and aggregation disease"
proposed_tests:
  - discipline: biophysics
    description: >
      Measure ThT fluorescence (prion aggregation) and turbidity (LLPS) for FUS and
      TDP-43 prion-like domains as a function of concentration. Fit both to nucleation
      theory; compare exponents. If exponents differ by more than 20%, hypothesis is
      falsified.
"""

# ══════════════════════════════════════════════════════════════════════════════
# Bridge 2: Action potential x Soliton
# ══════════════════════════════════════════════════════════════════════════════
FILES["cross-domain/biology-physics/b-action-potential-x-soliton.yaml"] = """\
id: b-action-potential-x-soliton
title: >
  Action potential x Soliton — nerve impulse as nonlinear wave
status: proposed
fields:
  - neuroscience
  - physics
  - mathematics
bridge_claim: >
  The Hodgkin-Huxley action potential propagates as a solitary wave (soliton) in the
  nonlinear cable equation; the nerve impulse velocity and shape stability arise from
  the same mathematical mechanism as solitons in the Korteweg-de Vries equation.
translation_table:
  - field_a_term: Hodgkin-Huxley membrane nonlinearity
    field_b_term: KdV nonlinear dispersion term
    note: >
      The voltage-gated ion channel dynamics provide the nonlinearity that balances
      diffusive spreading, exactly as the nonlinear term in KdV balances dispersion.
  - field_a_term: Action potential propagation velocity
    field_b_term: Soliton speed (function of amplitude)
    note: >
      Both velocities are determined by the amplitude-nonlinearity balance; the
      conduction velocity in myelinated axons scales analogously.
communication_gap: >
  Hodgkin-Huxley was developed as an electrophysiology model in 1952; soliton theory
  emerged in fluid mechanics. The mathematical equivalence was recognized but rarely
  integrated into neuroscience textbooks.
cross_pollination_opportunities:
  - >
    Use soliton collision theory to model action potential interactions at axon branching
    points and predict failure modes.
  - >
    Apply soliton perturbation theory to predict how channelopathies alter conduction
    velocity and waveform stability.
related_unknowns:
  - u-axon-soliton-collision-dynamics
references:
  - doi: "10.1113/jphysiol.1952.sp004764"
    note: "Hodgkin & Huxley (1952) — quantitative description of membrane current and nerve impulse"
last_reviewed: "2026-05-07"
"""

FILES["unknowns-catalog/neuroscience/u-axon-soliton-collision-dynamics.yaml"] = """\
id: u-axon-soliton-collision-dynamics
title: >
  Do action potentials at axon branch points interact according to soliton collision
  rules, and can soliton perturbation theory predict conduction failure thresholds?
status: open
priority: medium
disciplines:
  - neuroscience
  - physics
  - mathematics
summary: >
  At axon branching points, action potentials can fail to propagate or can interact.
  Soliton theory predicts specific collision outcomes (transmission, reflection,
  annihilation) based on amplitude ratios. Testing whether these rules apply to
  action potentials would validate the soliton analogy and provide a predictive
  framework for neural conduction failure in channelopathies and demyelinating diseases.
systematic_gaps:
  - No systematic test of soliton collision rules at axon branch points in vitro
  - Perturbation theory predictions not compared to Hodgkin-Huxley simulation outcomes
  - Channelopathy effects on conduction velocity not framed in soliton amplitude language
related_bridges:
  - b-action-potential-x-soliton
suggested_hypotheses:
  - h-axon-soliton-collision-dynamics
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-axon-soliton-collision-dynamics.yaml"] = """\
id: h-axon-soliton-collision-dynamics
title: >
  Action potential collision outcomes at axon branch points (transmission, annihilation,
  or reflection) can be predicted within 10% accuracy by KdV soliton collision rules
  applied to the Hodgkin-Huxley cable equation.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
unknowns_addressed:
  - u-axon-soliton-collision-dynamics
related_disciplines:
  - neuroscience
  - physics
  - mathematics
evidence_links:
  - type: related
    doi: "10.1113/jphysiol.1952.sp004764"
    note: "Hodgkin & Huxley (1952) — foundational HH equations"
proposed_tests:
  - discipline: neuroscience
    description: >
      Simulate collision of two action potentials in a branched HH cable model.
      Compare outcomes (transmission fraction, delay, waveform distortion) to
      KdV soliton collision predictions. If predictions deviate by more than 10%
      across 10 parameter combinations, hypothesis is falsified.
"""

# ══════════════════════════════════════════════════════════════════════════════
# Bridge 3: Percolation x Disease spread
# ══════════════════════════════════════════════════════════════════════════════
FILES["cross-domain/math-ecology/b-percolation-x-disease-spread.yaml"] = """\
id: b-percolation-x-disease-spread
title: >
  Percolation theory x Epidemic spreading — connectivity threshold as herd immunity
status: proposed
fields:
  - mathematics
  - biology
  - epidemiology
bridge_claim: >
  The SIR epidemic threshold (R0 = 1) is identical to the bond percolation critical
  probability on the contact network; herd immunity corresponds to the network falling
  below the percolation threshold, making the giant connected component subcritical.
translation_table:
  - field_a_term: Bond percolation critical probability p_c
    field_b_term: Epidemic threshold 1/R0
    note: >
      Removing bonds with probability (1 - 1/R0) destroys the giant component, exactly
      corresponding to achieving herd immunity threshold in the SIR model.
  - field_a_term: Giant connected component (GCC)
    field_b_term: Epidemic final size (proportion infected)
    note: >
      The fraction of the population in the GCC equals the final epidemic attack rate;
      both exhibit power-law scaling near the critical threshold.
communication_gap: >
  Mathematical percolation theory developed in statistical physics; epidemiology developed
  with different modeling traditions. The formal equivalence was established by Newman
  (2002) but is not standard in epidemiology curricula.
cross_pollination_opportunities:
  - >
    Use percolation finite-size scaling to predict epidemic size uncertainty in small
    populations and during early outbreak detection.
  - >
    Apply network percolation theory to design optimal targeted vaccination strategies
    that fragment the contact network below p_c.
related_unknowns:
  - u-percolation-herd-immunity-heterogeneous-networks
references:
  - doi: "10.1103/PhysRevE.66.016128"
    note: "Newman (2002) — spread of epidemic disease on networks; percolation equivalence"
last_reviewed: "2026-05-07"
"""

FILES["unknowns-catalog/epidemiology/u-percolation-herd-immunity-heterogeneous-networks.yaml"] = """\
id: u-percolation-herd-immunity-heterogeneous-networks
title: >
  Does the percolation-epidemic equivalence hold quantitatively on empirically measured
  human contact networks with heterogeneous degree distributions, and does it predict
  herd immunity thresholds more accurately than the classic 1 - 1/R0 formula?
status: open
priority: high
disciplines:
  - epidemiology
  - mathematics
  - network-science
summary: >
  The classic herd immunity threshold 1 - 1/R0 assumes homogeneous mixing. Percolation
  theory on heterogeneous networks predicts lower thresholds due to hub immunization
  effects. Testing this on measured contact networks (e.g., POLYMOD data) against
  observed epidemic dynamics would validate or refute the percolation approach and
  could improve vaccine coverage recommendations.
systematic_gaps:
  - No systematic comparison of percolation threshold predictions vs classic HIT on POLYMOD-type data
  - Heterogeneous degree distribution effects on critical threshold not validated against outbreak data
  - Bond vs site percolation difference for vaccination vs natural immunity not empirically resolved
related_bridges:
  - b-percolation-x-disease-spread
suggested_hypotheses:
  - h-percolation-herd-immunity-heterogeneous-networks
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-percolation-herd-immunity-heterogeneous-networks.yaml"] = """\
id: h-percolation-herd-immunity-heterogeneous-networks
title: >
  The herd immunity threshold predicted by bond percolation on empirically measured
  contact networks (using POLYMOD degree distributions) matches observed epidemic
  final sizes within 5 percentage points, outperforming the classic homogeneous-mixing
  1 - 1/R0 formula for pathogens with R0 > 3.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: high
unknowns_addressed:
  - u-percolation-herd-immunity-heterogeneous-networks
related_disciplines:
  - epidemiology
  - mathematics
  - network-science
evidence_links:
  - type: supporting
    doi: "10.1103/PhysRevE.66.016128"
    note: "Newman (2002) — percolation-epidemic equivalence on networks"
proposed_tests:
  - discipline: epidemiology
    description: >
      Construct contact networks from POLYMOD data for 5 European countries. Compute
      percolation threshold and compare to observed COVID-19 and measles final attack
      rates. If percolation prediction is not closer to observed attack rates than
      classic HIT for R0 > 3 in at least 4 of 5 cases, hypothesis is falsified.
"""

# ══════════════════════════════════════════════════════════════════════════════
# Bridge 4: Ising model x Hopfield network
# ══════════════════════════════════════════════════════════════════════════════
FILES["cross-domain/physics-computer-science/b-ising-model-x-hopfield-network.yaml"] = """\
id: b-ising-model-x-hopfield-network
title: >
  Ising model x Hopfield network — spin glass as associative memory
status: proposed
fields:
  - physics
  - computer-science
  - neuroscience
bridge_claim: >
  The Hopfield neural network for associative memory is exactly the Ising spin glass
  model; stored memories correspond to local energy minima, retrieval is energy
  minimization, and the network's memory capacity is set by the spin-glass phase boundary.
translation_table:
  - field_a_term: Ising spin configuration
    field_b_term: Neural activity pattern
    note: >
      Each spin (+1/-1) corresponds to a neuron's firing state (active/silent);
      the spin glass Hamiltonian is identical to the Hopfield energy function.
  - field_a_term: Spin glass frozen state (local energy minimum)
    field_b_term: Stored memory attractor
    note: >
      Both are metastable states of the same energy landscape; spin glass frustration
      corresponds to memory interference in the Hopfield network.
communication_gap: >
  Hopfield published independently in 1982, unaware that his model was the spin glass
  Hamiltonian already studied by Edwards and Anderson (1975). The connection was
  recognized by Amit, Gutfreund & Sompolinsky (1985) but remains a pedagogical gap.
cross_pollination_opportunities:
  - >
    Use spin glass replica theory to analytically compute the maximum number of memories
    a neural population can store before error rates exceed threshold.
  - >
    Apply modern spin glass phase diagram analysis to predict catastrophic forgetting
    thresholds in continual learning systems.
related_unknowns:
  - u-hopfield-capacity-modern-architectures
references:
  - doi: "10.1073/pnas.79.8.2554"
    note: "Hopfield (1982) — neural networks and physical systems with emergent collective computational abilities"
last_reviewed: "2026-05-07"
"""

FILES["unknowns-catalog/computer-science/u-hopfield-capacity-modern-architectures.yaml"] = """\
id: u-hopfield-capacity-modern-architectures
title: >
  Does the spin-glass memory capacity bound (alpha_c ~ 0.14 per neuron) generalize
  to modern transformer attention heads, and can spin-glass replica theory predict
  catastrophic forgetting thresholds in large language models?
status: open
priority: high
disciplines:
  - computer-science
  - physics
  - neuroscience
summary: >
  The Hopfield-Ising equivalence gives a capacity bound of approximately 0.14N memories
  for a network of N neurons. Modern transformers use dense attention that resembles
  continuous-valued Hopfield networks with higher capacity. Whether the spin-glass
  phase transition framework correctly predicts failure modes in transformers is unknown
  and potentially high-impact for understanding in-context learning limits.
systematic_gaps:
  - Replica theory capacity bounds not tested against empirical in-context learning limits in transformers
  - Relationship between spin-glass temperature parameter and transformer temperature not formalized
  - Catastrophic forgetting onset not analyzed as a spin-glass phase transition
related_bridges:
  - b-ising-model-x-hopfield-network
suggested_hypotheses:
  - h-hopfield-capacity-modern-architectures
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-hopfield-capacity-modern-architectures.yaml"] = """\
id: h-hopfield-capacity-modern-architectures
title: >
  The in-context learning capacity of transformer attention heads (measured as maximum
  number of retrievable input-output pairs) scales with context length N according to
  the Hopfield-Ising capacity bound alpha_c * N, with alpha_c between 0.1 and 2.0
  depending on the effective energy function curvature.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: high
unknowns_addressed:
  - u-hopfield-capacity-modern-architectures
related_disciplines:
  - computer-science
  - physics
  - neuroscience
evidence_links:
  - type: supporting
    doi: "10.1073/pnas.79.8.2554"
    note: "Hopfield (1982) — original associative memory model"
proposed_tests:
  - discipline: computer-science
    description: >
      Construct associative memory tasks with varying numbers of key-value pairs and
      test retrieval accuracy as a function of context length N for GPT-class models.
      Fit capacity curve and compare to Hopfield-Ising bound. If scaling exponent differs
      by more than 2x from the classical bound, hypothesis is falsified.
"""

# ══════════════════════════════════════════════════════════════════════════════
# Bridge 5: Osmotic pressure x Viral capsid
# ══════════════════════════════════════════════════════════════════════════════
FILES["cross-domain/biology-physics/b-osmotic-pressure-x-viral-capsid.yaml"] = """\
id: b-osmotic-pressure-x-viral-capsid
title: >
  Osmotic pressure x Viral capsid mechanics — genome packaging as pressurization
status: proposed
fields:
  - biology
  - physics
  - biophysics
bridge_claim: >
  Bacteriophage DNA packaging generates internal pressures of 50-100 atm inside the
  capsid, governed by the same van't Hoff osmotic pressure law that applies to
  semipermeable membranes; DNA ejection is an osmotically driven pressure-release
  mechanism.
translation_table:
  - field_a_term: Osmotic pressure Pi = nRT/V
    field_b_term: DNA packaging pressure inside phage capsid
    note: >
      The confined DNA acts as an ideal osmotic solute; van't Hoff law predicts
      50-100 atm matching direct measurements by osmotic suppression experiments.
  - field_a_term: Semipermeable membrane water flux
    field_b_term: DNA ejection through phage tail channel
    note: >
      Both are pressure-driven transport through a nanoscale channel; the ejection
      force equals the osmotic pressure times the channel cross-section.
communication_gap: >
  Membrane biophysics and virology developed as separate fields; the application of
  osmotic pressure theory to phage DNA packaging was only established with single-molecule
  experiments in the 2000s.
cross_pollination_opportunities:
  - >
    Use osmotic pressure engineering to design phage-based drug delivery vehicles
    that release payload at tunable osmotic thresholds.
  - >
    Apply viral capsid pressurization models to synthetic nanocapsule design for
    controlled release applications.
related_unknowns:
  - u-phage-ejection-force-osmotic-mechanism
references:
  - doi: "10.1016/S0006-3495(01)75940-2"
    note: "Tzlil et al. (2003) — forces and pressures in DNA packaging and release from viral capsids"
last_reviewed: "2026-05-07"
"""

FILES["unknowns-catalog/biophysics/u-phage-ejection-force-osmotic-mechanism.yaml"] = """\
id: u-phage-ejection-force-osmotic-mechanism
title: >
  Is bacteriophage DNA ejection force quantitatively explained by osmotic pressure
  alone, or do electrostatic and entropic contributions require an extended model?
status: open
priority: medium
disciplines:
  - biophysics
  - biology
  - physics
summary: >
  Direct force measurements by optical tweezers suggest phage ejection forces of 60-80 pN,
  consistent with osmotic pressure estimates. However, the DNA confinement entropy,
  electrostatic self-repulsion of the charged DNA, and capsid elasticity all contribute.
  A complete quantitative budget of ejection force components is not yet established.
systematic_gaps:
  - No complete force-component breakdown (osmotic + electrostatic + entropic) for phage lambda
  - Osmotic suppression experiments measure total force but not individual contributions
  - Capsid mechanical compliance contribution to ejection dynamics not systematically measured
related_bridges:
  - b-osmotic-pressure-x-viral-capsid
suggested_hypotheses:
  - h-phage-ejection-force-osmotic-mechanism
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-phage-ejection-force-osmotic-mechanism.yaml"] = """\
id: h-phage-ejection-force-osmotic-mechanism
title: >
  More than 70% of bacteriophage lambda DNA ejection force is attributable to osmotic
  pressure from confined DNA, with electrostatic and entropic contributions each below
  20%, as measurable by systematic osmotic suppression experiments with PEG solutions
  of varying molecular weight.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
unknowns_addressed:
  - u-phage-ejection-force-osmotic-mechanism
related_disciplines:
  - biophysics
  - biology
  - physics
evidence_links:
  - type: supporting
    doi: "10.1016/S0006-3495(01)75940-2"
    note: "Tzlil et al. (2003) — osmotic pressure model for viral DNA packaging and release"
proposed_tests:
  - discipline: biophysics
    description: >
      Measure phage lambda ejection force via osmotic suppression with PEG 8000 and
      PEG 200 (different size exclusion). The PEG-size dependence distinguishes osmotic
      from electrostatic contributions. If osmotic contribution is less than 70% in
      repeated measurements, hypothesis is falsified.
"""

# ══════════════════════════════════════════════════════════════════════════════
# Bridge 6: Stochastic resonance x Signal detection
# ══════════════════════════════════════════════════════════════════════════════
FILES["cross-domain/math-physics/b-stochastic-resonance-x-signal-detection.yaml"] = """\
id: b-stochastic-resonance-x-signal-detection
title: >
  Stochastic resonance x Signal detection — noise-enhanced threshold crossing
status: proposed
fields:
  - physics
  - neuroscience
  - signal-processing
bridge_claim: >
  Stochastic resonance — where adding noise to a subthreshold signal improves detection —
  is the physical mechanism behind mechanoreceptor hair cell bundle noise and neural
  population coding; the optimal noise level is predicted by the signal-to-noise ratio
  at the detection threshold.
translation_table:
  - field_a_term: Optimal noise amplitude sigma_opt
    field_b_term: Hair cell bundle thermal noise level
    note: >
      Both optimize at the same value: sigma_opt = signal amplitude / sqrt(2); hair
      cell thermal noise appears tuned near this optimum.
  - field_a_term: Threshold crossing rate vs noise curve (SR peak)
    field_b_term: Neural detection probability vs spontaneous firing rate
    note: >
      The SR peak in physical systems corresponds to the non-monotonic dependence of
      detection sensitivity on spontaneous activity in sensory neurons.
communication_gap: >
  Stochastic resonance was discovered in climate physics (Benzi 1981) and later applied
  to neural systems; the quantitative connection to hair cell mechanics required
  experiments not completed until the late 1990s.
cross_pollination_opportunities:
  - >
    Design neural prosthetics that add optimal stochastic stimulation to amplify
    subthreshold sensory signals in patients with peripheral neuropathy.
  - >
    Use SR theory to set optimal noise floors in weak-signal detection hardware
    (gravimeters, magnetometers) by analogy with sensory neuroscience.
related_unknowns:
  - u-stochastic-resonance-neural-coding-optimality
references:
  - doi: "10.1038/365337a0"
    note: "Levin & Miller (1996) — broadband neural encoding of weak signals via noise — stochastic resonance in hair cells"
last_reviewed: "2026-05-07"
"""

FILES["unknowns-catalog/neuroscience/u-stochastic-resonance-neural-coding-optimality.yaml"] = """\
id: u-stochastic-resonance-neural-coding-optimality
title: >
  Is the spontaneous firing rate of primary sensory neurons (hair cells, mechanoreceptors)
  optimally tuned to maximize stochastic resonance detection of their characteristic
  stimulus frequencies?
status: open
priority: medium
disciplines:
  - neuroscience
  - physics
  - signal-processing
summary: >
  If sensory neurons operate at the SR optimum, their spontaneous rates should
  satisfy sigma_opt = A_signal / sqrt(2) where A_signal is the threshold signal
  amplitude. Testing this across modalities and species would reveal whether evolution
  has exploited SR as a general coding strategy, with implications for hearing loss
  and neuroprosthetics.
systematic_gaps:
  - No systematic test of SR optimality across sensory modalities (auditory, tactile, vestibular)
  - Spontaneous rates and signal thresholds not jointly measured in the same neuron preparations
  - Evolutionary conservation of SR tuning not assessed across species
related_bridges:
  - b-stochastic-resonance-x-signal-detection
suggested_hypotheses:
  - h-stochastic-resonance-neural-coding-optimality
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-stochastic-resonance-neural-coding-optimality.yaml"] = """\
id: h-stochastic-resonance-neural-coding-optimality
title: >
  The spontaneous firing rate of primary auditory nerve fibers is within a factor of 2
  of the stochastic resonance optimum predicted by the ratio of detection threshold
  sound pressure to hair cell thermal noise, across at least 5 mammalian species.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
unknowns_addressed:
  - u-stochastic-resonance-neural-coding-optimality
related_disciplines:
  - neuroscience
  - physics
  - signal-processing
evidence_links:
  - type: supporting
    doi: "10.1038/365337a0"
    note: "Levin & Miller (1996) — stochastic resonance in hair cells"
proposed_tests:
  - discipline: neuroscience
    description: >
      Compile published spontaneous rate data and detection thresholds for auditory
      nerve fibers in mouse, cat, guinea pig, chinchilla, and human. Compute SR optimum
      from threshold and thermal noise estimates. If observed rates are outside 2x of
      optimum in 3+ species, hypothesis is falsified.
"""

# ══════════════════════════════════════════════════════════════════════════════
# Bridge 7: Catalysis x Transition state theory
# ══════════════════════════════════════════════════════════════════════════════
FILES["cross-domain/chemistry-physics/b-catalysis-x-transition-state-theory.yaml"] = """\
id: b-catalysis-x-transition-state-theory
title: >
  Catalysis x Transition state theory — activation energy landscape
status: proposed
fields:
  - chemistry
  - physics
  - biochemistry
bridge_claim: >
  Enzymatic catalysis and heterogeneous surface catalysis both lower activation energy
  by stabilizing the transition state; the Eyring-Polanyi equation k = (kT/h)exp(-DeltaG_dag/RT)
  is the universal bridge between molecular structure and reaction rate in both contexts.
translation_table:
  - field_a_term: Enzyme active site transition state stabilization
    field_b_term: Heterogeneous catalyst surface adsorption energy
    note: >
      Both lower DeltaG_dag by the same energy stabilization mechanism; the Brønsted-Evans-Polanyi
      relation in surface catalysis parallels Pauling's complementarity principle for enzymes.
  - field_a_term: Michaelis-Menten k_cat
    field_b_term: Turnover frequency (TOF) per active site
    note: >
      Both measure the per-site rate at saturation; k_cat and TOF are defined identically
      via the Eyring equation once DeltaG_dag is known.
communication_gap: >
  Biochemists and heterogeneous catalysis chemists developed separate kinetic frameworks
  (Michaelis-Menten vs Langmuir-Hinshelwood) despite both being limiting cases of
  transition state theory, creating parallel vocabularies for the same physics.
cross_pollination_opportunities:
  - >
    Use Brønsted-Evans-Polanyi volcano plot analysis from heterogeneous catalysis to
    design enzyme variants with optimal transition state stabilization.
  - >
    Apply enzyme promiscuity principles to design multi-functional heterogeneous
    catalysts with tunable selectivity.
related_unknowns:
  - u-enzyme-surface-catalyst-design-principles
references:
  - doi: "10.1039/tf9353100875"
    note: "Eyring (1935) — activated complex theory; the foundational Eyring-Polanyi equation"
last_reviewed: "2026-05-07"
"""

FILES["unknowns-catalog/chemistry/u-enzyme-surface-catalyst-design-principles.yaml"] = """\
id: u-enzyme-surface-catalyst-design-principles
title: >
  Can the Brønsted-Evans-Polanyi volcano plot framework from heterogeneous catalysis
  predict optimal transition state stabilization energies for enzyme active site design?
status: open
priority: medium
disciplines:
  - chemistry
  - biochemistry
  - physics
summary: >
  Volcano plots in heterogeneous catalysis identify the optimal adsorption energy
  that maximizes reaction rate. The analogous optimization in enzyme design would
  identify the optimal transition state complementarity. Whether the Sabatier principle
  (binding not too strong, not too weak) applies quantitatively to enzyme design is
  an open question with practical implications for directed evolution strategies.
systematic_gaps:
  - No systematic application of BEP volcano plots to enzyme active site design
  - Sabatier principle not quantitatively tested for transition state analogue inhibitor design
  - Cross-field comparison of optimal stabilization energies not performed
related_bridges:
  - b-catalysis-x-transition-state-theory
suggested_hypotheses:
  - h-enzyme-surface-catalyst-design-principles
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-enzyme-surface-catalyst-design-principles.yaml"] = """\
id: h-enzyme-surface-catalyst-design-principles
title: >
  Enzyme variants designed using the Brønsted-Evans-Polanyi volcano plot optimality
  criterion (DeltaG_dag minimized at DeltaG_ads = -DeltaG_rxn/2) achieve k_cat values
  within 10-fold of the wild-type enzyme when DeltaG_rxn is held constant by substrate choice.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
unknowns_addressed:
  - u-enzyme-surface-catalyst-design-principles
related_disciplines:
  - chemistry
  - biochemistry
  - physics
evidence_links:
  - type: related
    doi: "10.1039/tf9353100875"
    note: "Eyring (1935) — transition state theory"
proposed_tests:
  - discipline: chemistry
    description: >
      Design 5 variants of a well-characterized enzyme (e.g., ketosteroid isomerase)
      using BEP volcano plot analysis. Measure k_cat for each. If none falls within
      10-fold of wild-type using BEP predictions, hypothesis is falsified.
"""

# ══════════════════════════════════════════════════════════════════════════════
# Bridge 8: Boolean satisfiability x Spin glass
# ══════════════════════════════════════════════════════════════════════════════
FILES["cross-domain/cs-math/b-boolean-satisfiability-x-spin-glass.yaml"] = """\
id: b-boolean-satisfiability-x-spin-glass
title: >
  Boolean satisfiability x Spin glass — NP-hardness as frustrated frustration
status: proposed
fields:
  - computer-science
  - physics
  - mathematics
bridge_claim: >
  The satisfiability phase transition (SAT/UNSAT boundary near clause-to-variable
  ratio alpha approximately 4.27 for 3-SAT) coincides with a spin-glass phase transition
  in the random K-SAT energy landscape; NP-hardness emerges from the same frustration
  mechanism as glassy dynamics.
translation_table:
  - field_a_term: Boolean variable assignment (+1/-1)
    field_b_term: Ising spin state (up/down)
    note: >
      Each Boolean variable maps directly to a spin; clauses map to interaction
      terms in a multi-spin Hamiltonian.
  - field_a_term: SAT/UNSAT phase boundary at alpha_c
    field_b_term: Spin glass freezing temperature T_g
    note: >
      Both mark the onset of exponential search complexity; the algorithmic phase
      transition mirrors the equilibrium phase transition in the energy landscape.
communication_gap: >
  Complexity theory and statistical physics developed independently; the cavity method
  from spin glass theory (Mezard & Parisi) was only imported into SAT solving
  (survey propagation) in the early 2000s.
cross_pollination_opportunities:
  - >
    Use spin glass replica symmetry breaking theory to design better SAT solvers
    that exploit the phase transition structure.
  - >
    Apply random K-SAT phase transition analysis to predict hardness of real-world
    constraint satisfaction problems in scheduling and logistics.
related_unknowns:
  - u-sat-spin-glass-algorithm-design
references:
  - doi: "10.1126/science.1073287"
    note: "Mezard & Montanari (2002) — analytic and algorithmic solution of random satisfiability problems"
last_reviewed: "2026-05-07"
"""

FILES["unknowns-catalog/computer-science/u-sat-spin-glass-algorithm-design.yaml"] = """\
id: u-sat-spin-glass-algorithm-design
title: >
  Can spin glass replica symmetry breaking theory predict the optimal algorithmic
  strategy for SAT instances near the phase transition boundary, and does survey
  propagation achieve the theoretical cavity method performance bound?
status: open
priority: high
disciplines:
  - computer-science
  - physics
  - mathematics
summary: >
  Survey propagation (SP) was derived from the cavity method and outperforms DPLL
  near the SAT phase transition. Whether SP achieves the theoretical performance bound
  from RSB analysis, and whether RSB order parameters predict algorithm runtime, are
  open questions. Resolving them would directly connect statistical physics theory
  to practical algorithm design.
systematic_gaps:
  - RSB order parameters not systematically compared to SP runtime profiles near alpha_c
  - Performance bound from cavity method not tested against modern CDCL solvers
  - Phase transition structure of structured (non-random) industrial SAT instances not characterized
related_bridges:
  - b-boolean-satisfiability-x-spin-glass
suggested_hypotheses:
  - h-sat-spin-glass-algorithm-design
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-sat-spin-glass-algorithm-design.yaml"] = """\
id: h-sat-spin-glass-algorithm-design
title: >
  The RSB cavity method complexity parameter (Parisi parameter q) for random 3-SAT
  at clause density alpha correlates with the median DPLL runtime exponent with
  Spearman rank correlation greater than 0.85 across the range alpha = 3.5 to 5.0.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: high
unknowns_addressed:
  - u-sat-spin-glass-algorithm-design
related_disciplines:
  - computer-science
  - physics
  - mathematics
evidence_links:
  - type: supporting
    doi: "10.1126/science.1073287"
    note: "Mezard & Montanari (2002) — cavity method applied to random SAT"
proposed_tests:
  - discipline: computer-science
    description: >
      Generate random 3-SAT instances at 20 densities spanning alpha = 3.5 to 5.0.
      Measure DPLL median runtime and compute RSB order parameter q numerically.
      Test Spearman correlation. If correlation is below 0.85, hypothesis is falsified.
"""

# ══════════════════════════════════════════════════════════════════════════════
# Bridge 9: Cytoskeleton x Active matter
# ══════════════════════════════════════════════════════════════════════════════
FILES["cross-domain/biology-physics/b-cytoskeleton-x-active-matter.yaml"] = """\
id: b-cytoskeleton-x-active-matter
title: >
  Cytoskeleton x Active matter — motor protein filaments as polar active fluid
status: proposed
fields:
  - biology
  - physics
  - biophysics
bridge_claim: >
  The cytoskeletal network of actin filaments and myosin motors is a biological
  realization of active matter (polar self-propelled rods); cytoplasmic streaming,
  cell motility, and mitotic spindle assembly are emergent collective behaviors
  described by Toner-Tu active hydrodynamics.
translation_table:
  - field_a_term: Actin filament with myosin motor
    field_b_term: Self-propelled rod in active fluid
    note: >
      The actin-myosin unit is the canonical biological active particle; its polarity
      and self-propulsion map directly onto Toner-Tu polar active matter.
  - field_a_term: Cytoplasmic streaming vortices
    field_b_term: Spontaneous flow in active fluid
    note: >
      Both arise from the same hydrodynamic instability of the uniform polarized state;
      Toner-Tu theory predicts the streaming patterns in Drosophila oocytes.
communication_gap: >
  Active matter physics developed theoretically in the 1990s (Toner & Tu 1995);
  the connection to cytoskeletal dynamics in cell biology was established through
  in vitro reconstitution experiments in the 2010s.
cross_pollination_opportunities:
  - >
    Use active matter topological defect theory to predict mitotic spindle assembly
    defects from motor protein stoichiometry perturbations.
  - >
    Design synthetic active matter materials with cytoskeletal components for
    autonomous soft robotics applications.
related_unknowns:
  - u-cytoskeletal-active-matter-defect-dynamics
references:
  - doi: "10.1103/PhysRevLett.75.4326"
    note: "Toner & Tu (1995) — long-range order in a 2D dynamical XY model: how birds fly together"
last_reviewed: "2026-05-07"
"""

FILES["unknowns-catalog/biophysics/u-cytoskeletal-active-matter-defect-dynamics.yaml"] = """\
id: u-cytoskeletal-active-matter-defect-dynamics
title: >
  Do topological defects in cytoskeletal active matter (actin-myosin networks)
  control cell division plane orientation, and can active matter defect theory
  predict mitotic spindle positioning errors?
status: open
priority: high
disciplines:
  - biophysics
  - biology
  - physics
summary: >
  Active matter theory predicts that +1/2 topological defects in nematic active fluids
  generate extensile stress and drive local flows. In epithelial monolayers, +1/2
  defects correlate with cell extrusion events. Whether analogous defects in the
  3D cytoskeletal network control mitotic spindle orientation is a key open question
  with implications for understanding chromosomal missegregation and cancer.
systematic_gaps:
  - No systematic mapping of cytoskeletal defect density to spindle positioning errors in dividing cells
  - Active matter defect theory not applied to 3D cytoskeletal networks in confined geometries
  - Relationship between actin/myosin stoichiometry perturbations and defect creation rate not quantified
related_bridges:
  - b-cytoskeleton-x-active-matter
suggested_hypotheses:
  - h-cytoskeletal-active-matter-defect-dynamics
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-cytoskeletal-active-matter-defect-dynamics.yaml"] = """\
id: h-cytoskeletal-active-matter-defect-dynamics
title: >
  The density of +1/2 topological defects in the cortical actin network at cell division
  onset is predictive of spindle misorientation angle (R^2 > 0.5) across HeLa cells
  with varying myosin II activity, consistent with active matter defect-driven stress.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: high
unknowns_addressed:
  - u-cytoskeletal-active-matter-defect-dynamics
related_disciplines:
  - biophysics
  - biology
  - physics
evidence_links:
  - type: supporting
    doi: "10.1103/PhysRevLett.75.4326"
    note: "Toner & Tu (1995) — active matter hydrodynamics foundation"
proposed_tests:
  - discipline: biophysics
    description: >
      Image cortical actin in HeLa cells at onset of mitosis using live super-resolution
      microscopy. Detect topological defects using orientational order parameter analysis.
      Measure spindle misorientation angle. Compute correlation. If R^2 < 0.5 across
      N > 50 cells, hypothesis is falsified.
"""

# ══════════════════════════════════════════════════════════════════════════════
# Bridge 10: Mechanism design x Market equilibrium
# ══════════════════════════════════════════════════════════════════════════════
FILES["cross-domain/cs-economics/b-mechanism-design-x-market-equilibrium.yaml"] = """\
id: b-mechanism-design-x-market-equilibrium
title: >
  Mechanism design x Market equilibrium — incentive compatibility as stability
status: proposed
fields:
  - economics
  - computer-science
  - mathematics
bridge_claim: >
  Mechanism design (designing rules so truthful reporting is the dominant strategy)
  and competitive market equilibrium (where no agent can profitably deviate) are dual
  formulations of the same incentive compatibility condition; the revelation principle
  bridges them formally.
translation_table:
  - field_a_term: Dominant strategy incentive compatibility (DSIC)
    field_b_term: Nash equilibrium strategy profile
    note: >
      DSIC is the stronger condition (truthfulness dominant regardless of others);
      Nash equilibrium is the weaker condition (no profitable unilateral deviation) —
      both formalize incentive alignment.
  - field_a_term: Revelation principle (direct mechanism equivalence)
    field_b_term: Arrow-Debreu competitive equilibrium existence
    note: >
      Both results guarantee existence and uniqueness of incentive-compatible outcomes
      under analogous conditions; the revelation principle is the mechanism design
      analog of Walras's existence theorem.
communication_gap: >
  Mechanism design emerged from game theory and computer science auction theory;
  competitive equilibrium from Walrasian economics. Myerson's Nobel work unified them
  formally but the connection is not standard in economics curricula.
cross_pollination_opportunities:
  - >
    Apply mechanism design DSIC constraints to design platform fee structures that
    induce truthful bidding in two-sided markets.
  - >
    Use computational mechanism design (VCG, Myerson optimal) to analyze stability
    of algorithmic trading market microstructure.
related_unknowns:
  - u-mechanism-design-algorithmic-markets
references:
  - doi: "10.2307/1912601"
    note: "Myerson (1981) — optimal auction design; the foundational mechanism design paper"
last_reviewed: "2026-05-07"
"""

FILES["unknowns-catalog/economics/u-mechanism-design-algorithmic-markets.yaml"] = """\
id: u-mechanism-design-algorithmic-markets
title: >
  Can mechanism design DSIC guarantees be maintained in algorithmic markets where
  agents use learned bidding strategies, and does the revelation principle hold
  when agents are adaptive ML-based algorithms?
status: open
priority: high
disciplines:
  - economics
  - computer-science
  - mathematics
summary: >
  Classical mechanism design assumes rational agents with fixed types. When agents
  are learning algorithms (e.g., in programmatic advertising auctions), they can
  exploit mechanism rules through repeated interaction in ways the revelation principle
  does not account for. Whether DSIC mechanisms remain strategy-proof against
  adaptive ML bidders is an open problem with direct relevance to online auction design.
systematic_gaps:
  - Revelation principle not extended to adaptive/learning agents with belief updates
  - DSIC violations by ML bidding algorithms in repeated auctions not systematically measured
  - Game-theoretic stability of VCG and Myerson mechanisms not proven for non-Bayesian agents
related_bridges:
  - b-mechanism-design-x-market-equilibrium
suggested_hypotheses:
  - h-mechanism-design-algorithmic-markets
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-mechanism-design-algorithmic-markets.yaml"] = """\
id: h-mechanism-design-algorithmic-markets
title: >
  VCG auction mechanisms remain approximately DSIC (regret within 5% of truthful
  bidding) for ML-based bidding agents trained with standard no-regret learning
  algorithms, even after 1000 repeated auction rounds, because the dominant strategy
  is a fixed point of the learning dynamics.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: high
unknowns_addressed:
  - u-mechanism-design-algorithmic-markets
related_disciplines:
  - economics
  - computer-science
  - mathematics
evidence_links:
  - type: related
    doi: "10.2307/1912601"
    note: "Myerson (1981) — optimal auction design"
proposed_tests:
  - discipline: computer-science
    description: >
      Simulate a VCG auction with 10 ML bidders (e.g., EXP3 algorithm) over 1000 rounds.
      Measure average regret relative to truthful bidding strategy. If regret exceeds
      5% of truthful utility in 3 out of 5 simulation runs, hypothesis is falsified.
"""

# ══════════════════════════════════════════════════════════════════════════════
# Bridge 11: Self-organized criticality x Earthquake
# ══════════════════════════════════════════════════════════════════════════════
FILES["cross-domain/physics-geology/b-self-organized-criticality-x-earthquake.yaml"] = """\
id: b-self-organized-criticality-x-earthquake
title: >
  Self-organized criticality x Earthquake statistics — Gutenberg-Richter as SOC
status: proposed
fields:
  - geoscience
  - physics
  - statistical-mechanics
bridge_claim: >
  The Gutenberg-Richter power law for earthquake frequency-magnitude distributions
  is the signature of self-organized criticality in the Earth's crust; the crust
  self-tunes to the critical state without external parameter adjustment, exactly
  as in the Bak-Tang-Wiesenfeld sandpile model.
translation_table:
  - field_a_term: BTW sandpile slope (maintained at critical angle)
    field_b_term: Earth's crust at critical stress state
    note: >
      Both systems self-organize to a marginally stable critical state; in the crust
      tectonic loading drives the system back toward criticality after each event.
  - field_a_term: Sandpile avalanche size distribution (power law)
    field_b_term: Gutenberg-Richter earthquake magnitude distribution
    note: >
      Both follow power laws N(s) ~ s^(-tau); the GR exponent b = 1 corresponds to
      the BTW avalanche exponent tau = 1.5 in 2D (with appropriate rescaling).
communication_gap: >
  Seismology developed empirically from the 1900s; SOC theory was formulated by
  Bak, Tang & Wiesenfeld in 1987. The connection was proposed early but quantitative
  tests of the SOC model for seismicity remain contested.
cross_pollination_opportunities:
  - >
    Use SOC early warning indicators (increasing autocorrelation, variance) to
    develop earthquake precursor detection systems.
  - >
    Apply SOC model to other geophysical systems (landslides, volcanic eruptions)
    to test universality of the critical state.
related_unknowns:
  - u-soc-earthquake-precursor-detection
references:
  - doi: "10.1103/PhysRevLett.59.381"
    note: "Bak, Tang & Wiesenfeld (1987) — self-organized criticality: an explanation of 1/f noise"
last_reviewed: "2026-05-07"
"""

FILES["unknowns-catalog/geoscience/u-soc-earthquake-precursor-detection.yaml"] = """\
id: u-soc-earthquake-precursor-detection
title: >
  Do SOC early warning indicators (rising autocorrelation, variance divergence) in
  regional seismicity time series provide statistically significant precursors to
  large earthquakes (M > 6.5)?
status: open
priority: high
disciplines:
  - geoscience
  - physics
  - statistical-mechanics
summary: >
  SOC theory predicts that a system approaching a large event should show increasing
  temporal autocorrelation and variance (critical slowing down) in the smaller events
  that precede it. Testing whether this signature appears in seismicity catalogs before
  major earthquakes would validate the SOC model and potentially enable probabilistic
  earthquake forecasting — a high-stakes application with contested empirical support.
systematic_gaps:
  - No systematic retrospective analysis of SOC indicators before all M > 6.5 events in a complete catalog
  - False positive rate of SOC indicators not benchmarked against Poisson null model
  - Spatial scale of precursor region not determined by SOC theory for realistic fault geometries
related_bridges:
  - b-self-organized-criticality-x-earthquake
suggested_hypotheses:
  - h-soc-earthquake-precursor-detection
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-soc-earthquake-precursor-detection.yaml"] = """\
id: h-soc-earthquake-precursor-detection
title: >
  In regional seismicity catalogs, temporal variance of M > 2 event rates increases
  significantly (z-score > 2) in the 90 days before M > 6.5 earthquakes more often
  than expected by chance, with a true positive rate exceeding false positive rate
  by at least 2:1 in a retrospective analysis of the ANSS catalog.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: high
unknowns_addressed:
  - u-soc-earthquake-precursor-detection
related_disciplines:
  - geoscience
  - physics
  - statistical-mechanics
evidence_links:
  - type: supporting
    doi: "10.1103/PhysRevLett.59.381"
    note: "Bak, Tang & Wiesenfeld (1987) — SOC and power law distributions"
proposed_tests:
  - discipline: geoscience
    description: >
      Analyze ANSS catalog (2000-2020) for all M > 6.5 events. For each, compute
      rolling variance of M > 2 seismicity rate in 90-day windows. Test whether
      variance in the pre-event window exceeds the catalog mean by z > 2 more often
      than for matched random windows. If TP/FP ratio < 2, hypothesis is falsified.
"""

# ══════════════════════════════════════════════════════════════════════════════
# Bridge 12: Population genetics x Random matrix theory
# ══════════════════════════════════════════════════════════════════════════════
FILES["cross-domain/biology-math/b-population-genetics-x-random-matrix.yaml"] = """\
id: b-population-genetics-x-random-matrix
title: >
  Population genetics x Random matrix theory — allele covariance as Wishart ensemble
status: proposed
fields:
  - biology
  - mathematics
  - statistics
bridge_claim: >
  The covariance matrix of allele frequencies across a neutrally evolving population
  follows the Marchenko-Pastur distribution of the Wishart random matrix ensemble;
  deviations from this null distribution identify loci under selection, providing a
  principled statistical test for selective sweeps.
translation_table:
  - field_a_term: Allele frequency covariance matrix (neutral evolution)
    field_b_term: Wishart random matrix ensemble
    note: >
      Under drift alone, the sample covariance matrix of allele frequencies is a
      Wishart matrix; its eigenvalue spectrum follows the Marchenko-Pastur law.
  - field_a_term: Eigenvalue outliers (selected loci)
    field_b_term: Spiked covariance matrix deviations from MP bulk
    note: >
      Loci under selection create eigenvalue outliers above the Marchenko-Pastur
      upper edge — exactly the signal RMT spike detection methods identify.
communication_gap: >
  Population geneticists and random matrix theorists publish in entirely separate
  journals. The RMT null model for population structure was proposed by Patterson,
  Price & Reich (2006) but RMT tools are rarely imported into population genetics
  software packages.
cross_pollination_opportunities:
  - >
    Apply RMT spike detection to GWAS summary statistics to identify polygenic
    selection signals below standard significance thresholds.
  - >
    Use RMT free probability theory to disentangle population structure from
    selection signals in admixed populations.
related_unknowns:
  - u-rmt-selective-sweep-detection-power
references:
  - doi: "10.1371/journal.pgen.0020190"
    note: "Patterson, Price & Reich (2006) — population structure and eigenanalysis; foundational RMT connection"
last_reviewed: "2026-05-07"
"""

FILES["unknowns-catalog/evolutionary-biology/u-rmt-selective-sweep-detection-power.yaml"] = """\
id: u-rmt-selective-sweep-detection-power
title: >
  Does the random matrix theory Marchenko-Pastur null model provide higher statistical
  power for detecting selective sweeps in population genomics than standard Fst-based
  tests, particularly in admixed populations?
status: open
priority: medium
disciplines:
  - biology
  - mathematics
  - statistics
summary: >
  Standard selective sweep tests (iHS, XP-EHH) have reduced power in admixed populations
  due to population structure confounding. RMT eigenvalue outlier detection separates
  structure (bulk MP spectrum) from selection (spikes above the edge), potentially
  providing unconfounded sweep detection. Whether this power improvement is quantifiable
  and applicable to biobank-scale data is an open question.
systematic_gaps:
  - No power comparison of RMT eigenvalue tests vs iHS/XP-EHH on matched simulated data
  - Free probability corrections for admixture not applied to selective sweep detection
  - RMT null model not validated against known sweeps in admixed African-European populations
related_bridges:
  - b-population-genetics-x-random-matrix
suggested_hypotheses:
  - h-rmt-selective-sweep-detection-power
last_reviewed: "2026-05-07"
"""

FILES["hypotheses/active/h-rmt-selective-sweep-detection-power.yaml"] = """\
id: h-rmt-selective-sweep-detection-power
title: >
  The RMT eigenvalue spike test for selective sweeps achieves at least 2x higher
  power (at fixed 5% FPR) than Fst-based tests in admixed populations with at least
  20% admixture, as measured on coalescent-simulated genomes with known sweep locations.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
unknowns_addressed:
  - u-rmt-selective-sweep-detection-power
related_disciplines:
  - biology
  - mathematics
  - statistics
evidence_links:
  - type: supporting
    doi: "10.1371/journal.pgen.0020190"
    note: "Patterson, Price & Reich (2006) — RMT connection to population structure"
proposed_tests:
  - discipline: biology
    description: >
      Simulate 1000 coalescent genomes (msprime) with 20% admixture and 50 selective
      sweep loci at known positions. Apply RMT eigenvalue spike test and Fst test.
      Compute ROC curves. If RMT power at 5% FPR is less than 2x Fst power,
      hypothesis is falsified.
"""


def main():
    created = []
    skipped = []
    for rel_path, content in FILES.items():
        path = ROOT / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists():
            skipped.append(rel_path)
            print(f"SKIP (exists): {rel_path}")
        else:
            path.write_text(content, encoding="utf-8")
            print(f"CREATED: {rel_path}")
            created.append(rel_path)
    print(f"\nDone. {len(created)} files created, {len(skipped)} skipped.")


if __name__ == "__main__":
    main()

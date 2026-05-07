"""Write 12 unknowns and 12 hypotheses for wave-28 bridges."""
import os

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# ─── Unknowns ───

# Bridge A unknown
write('unknowns-catalog/biophysics/u-eis-channel-gating-mechanistic-link.yaml', """\
id: u-eis-channel-gating-mechanistic-link
title: Can electrochemical impedance spectroscopy non-invasively extract Hodgkin-Huxley channel gating parameters (activation/inactivation time constants, channel density) from intact excitable cell layers?
status: open
priority: medium
disciplines:
  - biophysics
  - chemistry
  - electrophysiology
summary: >
  EIS measures the frequency-dependent impedance of cell monolayers and tissues,
  which in principle encodes the kinetics of voltage-gated ion channels as
  frequency-dependent impedance elements. However, the inverse problem — extracting
  individual channel parameters (g_Na, g_K, activation/inactivation time constants tau_m,
  tau_h, tau_n) from multi-frequency EIS measurements on intact cell cultures — has not
  been systematically solved. The difficulty is that the impedance spectrum reflects
  an ensemble of channels at varying membrane potentials and activation states, and the
  equivalent circuit model must distinguish channel kinetics from passive cell geometry
  (cell-substrate contact area, cleft resistance).
systematic_gaps:
  - Multi-frequency EIS at sub-millisecond time resolution needed to capture fast Na channel gating has not been demonstrated on intact mammalian excitable cell layers.
  - The mapping from HH parameters to EIS Nyquist plot features is known analytically only for linearized (small-signal) channel models around a fixed operating point.
  - Drug-induced channel block creates characteristic EIS signatures that have not been systematically catalogued for ion channel pharmacology screening.
last_reviewed: "2026-05-06"
""")

# Bridge B unknown
write('unknowns-catalog/social-science/u-matching-markets-dynamic-stability.yaml', """\
id: u-matching-markets-dynamic-stability
title: Does the Gale-Shapley stable matching persist under dynamic entry/exit of agents, and what mechanism design principles govern real-time matching platforms (gig economy, ride-sharing)?
status: open
priority: high
disciplines:
  - social-science
  - mathematics
  - economics
  - mechanism-design
summary: >
  The classical Gale-Shapley deferred acceptance algorithm operates on a static set of
  agents with fixed preference lists. In real markets — gig-economy platforms (Uber,
  TaskRabbit), organ exchange (kidney paired donation), and online job boards — agents
  arrive and depart dynamically and preferences may be stochastic or revealed gradually.
  Whether a stable matching exists and can be computed efficiently in dynamic settings
  is an open theoretical problem. Dynamic matching may require accepting temporary
  instability to achieve long-run efficiency, and the appropriate stability concept
  for dynamic markets has not been settled.
systematic_gaps:
  - No polynomial-time algorithm is known for stable matching with dynamic arrivals under general preference structures.
  - The welfare impact of dynamic vs. static mechanisms in real labor markets (NRMP, teacher placement) has not been empirically identified.
  - Incentive compatibility in dynamic settings (where agents can strategically delay reporting preferences) has not been fully characterized.
last_reviewed: "2026-05-06"
""")

# Bridge C unknown
write('unknowns-catalog/biophysics/u-capsid-assembly-kinetic-intermediates.yaml', """\
id: u-capsid-assembly-kinetic-intermediates
title: What are the structures and stabilities of transient oligomeric intermediates during viral capsid nucleation, and can they be targeted for antiviral intervention?
status: open
priority: high
disciplines:
  - biophysics
  - structural-biology
  - virology
  - biochemistry
summary: >
  The Zlotnick nucleation-elongation model predicts a slow nucleation step involving
  a critical nucleus of approximately 5 subunits, but the structure and stability of
  these early oligomeric intermediates (dimers, trimers, pentamers) remain poorly
  characterized experimentally. Cryo-electron microscopy captures assembled capsids
  at near-atomic resolution but not the transient, disordered nucleation intermediates.
  Native mass spectrometry and hydrogen-deuterium exchange can detect these species
  but the stoichiometry and geometry of the critical nucleus remains uncertain for
  most viruses (HBV, HIV, picornaviruses). The antiviral opportunity is significant:
  molecules that stabilize off-pathway intermediates (CAM drugs for HBV) already
  demonstrate proof-of-concept, but rational design requires structural knowledge
  of the target intermediates.
systematic_gaps:
  - Cryo-EM structures of pre-nucleation oligomers below pentamer size do not exist for any major human pathogen.
  - The relationship between critical nucleus size, subunit concentration dependence of the lag phase, and the effective CAC has not been measured for HIV or influenza capsids.
  - Whether the nucleation pathway is unique or whether multiple parallel assembly pathways coexist remains unresolved.
last_reviewed: "2026-05-06"
""")

# Bridge D unknown
write('unknowns-catalog/urban-science/u-smart-city-equity-algorithmic-routing.yaml', """\
id: u-smart-city-equity-algorithmic-routing
title: How can smart city traffic and resource optimization algorithms be designed to satisfy both system efficiency objectives and distributional equity constraints across neighborhoods?
status: open
priority: high
disciplines:
  - urban-science
  - engineering
  - social-science
  - computer-science
summary: >
  Model predictive control and system-optimal traffic assignment algorithms minimize
  aggregate metrics (total vehicle delay, energy consumption) that may externalize
  costs onto specific neighborhoods — routing trucks through residential areas, directing
  commuter traffic through low-income districts, deploying air quality sensors unevenly.
  Current smart city deployments rarely include distributional constraints, and there
  is no consensus on the appropriate equity metric (neighborhood exposure, demographic
  disparity, Rawlsian worst-case). The mathematical challenge is incorporating
  distributional constraints into MPC optimization without excessive computational cost,
  and the political challenge is determining which equity definition is democratically
  legitimate.
systematic_gaps:
  - No published smart city deployment has prospectively measured demographic distributional impacts of algorithmic traffic routing at fine spatial resolution.
  - The tradeoff between system efficiency and equity (Pareto frontier) has not been empirically characterized for any real urban network.
  - Participatory mechanisms for residents to express preferences and constraints within city optimization frameworks do not exist at production scale.
last_reviewed: "2026-05-06"
""")

# Bridge E unknown
write('unknowns-catalog/physics/u-lorenz-attractor-universality-class.yaml', """\
id: u-lorenz-attractor-universality-class
title: Is the Lorenz attractor in a distinct universality class from other strange attractors, and what determines the route to chaos (period-doubling vs. intermittency vs. quasiperiodicity) in physical fluid systems?
status: open
priority: medium
disciplines:
  - physics
  - mathematics
  - nonlinear-dynamics
  - fluid-dynamics
summary: >
  The Lorenz attractor arises from a specific 3-mode Galerkin truncation of the Bénard
  equations and has a fractal dimension of approximately 2.06 and a specific Lyapunov
  exponent spectrum. However, it is unknown whether the Lorenz system represents a
  universal route to chaos for convection-like systems or whether the three-mode
  truncation introduces artifacts not present in the full PDE. The physical Rayleigh-
  Bénard system exhibits multiple routes to chaos (period-doubling in narrow-gap cells,
  intermittency in other parameter regimes) and the theoretical prediction of which
  route a given fluid system will take from its governing equations remains an unsolved
  problem. The renormalization group approach (Feigenbaum universality for period-doubling)
  applies to 1D maps but its extension to PDE fluid systems is incomplete.
systematic_gaps:
  - No rigorous proof exists that the physical Rayleigh-Bénard system (PDE) exhibits the Lorenz attractor in any parameter regime — the truncation may be qualitatively misleading.
  - The universality class of the Lorenz attractor (critical exponents, dimension) relative to other strange attractors is not fully classified.
  - Predicting the route to chaos (period-doubling vs. intermittency) from fluid parameters (Prandtl number, aspect ratio) without simulation remains an open theoretical problem.
last_reviewed: "2026-05-06"
""")

# Bridge F unknown
write('unknowns-catalog/ecology/u-red-queen-molecular-clock-arms-race.yaml', """\
id: u-red-queen-molecular-clock-arms-race
title: Can molecular evolutionary rate analysis (dN/dS ratios at interacting protein interfaces) quantitatively detect and measure the pace of ongoing coevolutionary arms races in wild populations?
status: open
priority: medium
disciplines:
  - ecology
  - evolutionary-biology
  - molecular-biology
  - population-genetics
summary: >
  The life-dinner principle (Dawkins and Krebs 1979) predicts elevated molecular
  evolutionary rates (dN/dS > 1, positive selection) in prey receptor genes relative
  to predator ligand genes. This prediction has been tested in TTX resistance (Nav1.4
  in snakes), host immune genes vs. pathogen surface antigens, and plant resistance
  genes vs. pathogen effectors. However, quantitatively linking geographic variation
  in coevolutionary selection intensity (hot spots vs. cold spots in Thompson's mosaic)
  to local dN/dS values in wild populations requires dense geographic sampling and
  long-term time-series data that do not yet exist for most systems. The temporal
  scale of arms races (generations to millennia) also complicates inference.
systematic_gaps:
  - No system has both sufficient geographic sampling of dN/dS variation and sufficient ecological data on local selection intensity to test Thompson's mosaic theory quantitatively at the molecular level.
  - Whether molecular co-evolutionary clocks run at rates predicted by measured selection coefficients from field experiments has not been tested.
  - The contribution of horizontal gene transfer vs. de novo mutation to rapid coevolutionary response in host-microbe systems is poorly quantified.
last_reviewed: "2026-05-06"
""")

# Bridge G unknown
write('unknowns-catalog/mathematics/u-neural-network-loss-landscape-global-structure.yaml', """\
id: u-neural-network-loss-landscape-global-structure
title: What is the global topological and geometric structure of neural network loss landscapes, and does the absence of spurious local minima hold for realistic architectures beyond shallow networks?
status: open
priority: high
disciplines:
  - mathematics
  - machine-learning
  - computer-science
  - optimization
summary: >
  Dauphin et al. (2014) showed empirically that saddle points dominate local minima in
  high-dimensional neural network loss landscapes, and theoretical results prove no
  spurious local minima exist for linear networks and two-layer networks with specific
  activation functions under overparameterization. However, the global structure of
  loss landscapes for deep ResNets, transformers, and other architectures used in
  practice is unknown. Whether the empirical success of SGD implies the absence of
  problematic local minima or merely that SGD avoids them for other reasons (implicit
  regularization, flat minima generalization) has not been resolved. The lottery ticket
  hypothesis implies the existence of sparse subnetworks within the loss landscape,
  but their geometric arrangement relative to the landscape structure is unclear.
systematic_gaps:
  - No rigorous proof that deep transformers or ResNets have no spurious local minima; theoretical results cover shallow networks only.
  - The relationship between implicit SGD regularization (edge of stability, catapult phase) and the geometric structure of flat minima is not understood mathematically.
  - Whether winning lottery tickets occupy special geometric positions in loss landscape (e.g., near global minimum manifold) has not been tested.
last_reviewed: "2026-05-06"
""")

# Bridge H unknown
write('unknowns-catalog/neuroscience/u-prion-like-spread-neurodegeneration-circuit-specificity.yaml', """\
id: u-prion-like-spread-neurodegeneration-circuit-specificity
title: What determines the circuit-specific vulnerability and spreading pattern of prion-like protein aggregates in neurodegeneration — connectivity, local protein expression, or regional metabolic activity?
status: open
priority: high
disciplines:
  - neuroscience
  - molecular-biology
  - cell-biology
  - neuropathology
summary: >
  Braak staging shows that misfolded alpha-synuclein and tau spread along stereotyped
  anatomical trajectories in Parkinson's and Alzheimer's disease respectively. Three
  competing explanations for the circuit specificity are: (1) connectome-based propagation
  — aggregates spread along axonal projections from highly connected hub regions;
  (2) protein expression vulnerability — neurons with high SNCA or MAPT expression
  accumulate aggregates faster; (3) metabolic vulnerability — high-activity neurons
  (dopaminergic substantia nigra neurons fire tonically at 3-4 Hz) accumulate
  oxidative stress that accelerates misfolding. Distinguishing these mechanisms requires
  interventions that decouple connectivity, expression, and activity — not yet achieved.
  The cell-to-cell transfer mechanism (exosome vs. tunneling nanotube vs. synaptic
  release) also remains contested.
systematic_gaps:
  - No study has simultaneously mapped connectome, SNCA/MAPT expression, metabolic activity, and Lewy body burden in the same brains at cellular resolution.
  - The route of cell-to-cell alpha-synuclein transfer (exosome, tunneling nanotube, lysosomal exocytosis) has not been uniquely determined in vivo.
  - Whether impeding axonal transport (e.g., by disrupting dynein) slows or accelerates Braak-staging progression has not been tested in a primate model.
last_reviewed: "2026-05-06"
""")

# Bridge I unknown
write('unknowns-catalog/social-science/u-opioid-prescribing-policy-chemistry-disconnect.yaml', """\
id: u-opioid-prescribing-policy-chemistry-disconnect
title: Why does pharmacological evidence about opioid receptor pharmacokinetics and tolerance mechanisms fail to translate into evidence-based prescribing policy, and how can this science-policy gap be closed?
status: open
priority: high
disciplines:
  - social-science
  - pharmacology
  - chemistry
  - public-health
summary: >
  The pharmacology of opioid tolerance, dependence, and overdose risk is well
  understood at the receptor level (mu-opioid receptor downregulation, arrestin
  signaling, respiratory depression mediated by different receptor populations than
  analgesia). However, prescribing guidelines for pain management have historically
  ignored this evidence — the OxyContin "abuse-deterrent" formulation was approved
  despite evidence that the reformulation (ER coating) does not prevent misuse in
  determined users. The FDA approval pathway, DEA scheduling, and clinical prescribing
  guidelines are each governed by different institutional actors with different
  evidentiary standards, creating multiple disconnects between receptor pharmacology
  and clinical practice. The mechanisms by which industry funding of medical education
  overrides pharmacological evidence in prescribing behavior are not quantitatively
  characterized.
systematic_gaps:
  - Quantitative models linking receptor pharmacology (tolerance rate, respiratory depression threshold) to population prescribing outcomes have not been validated against epidemic data.
  - The relative contributions of physician incentives, patient demand, and regulatory failure to opioid overprescribing have not been causally identified.
  - Evidence-based criteria for Schedule I classification (grounded in receptor pharmacology and epidemiology) have never been formally operationalized in U.S. drug law.
last_reviewed: "2026-05-06"
""")

# Bridge J unknown
write('unknowns-catalog/biology/u-whale-song-information-content-localization.yaml', """\
id: u-whale-song-information-content-localization
title: What is the information content and function of whale song — mate attraction, individual identification, group coordination, or SOFAR-channel navigation — and can passive acoustic methods resolve whale positions at basin scale?
status: open
priority: medium
disciplines:
  - biology
  - physics
  - acoustics
  - marine-biology
summary: >
  Humpback whale song is one of the most complex animal vocalizations, with hierarchical
  structure (units, phrases, themes, songs, sessions) and cultural transmission across
  ocean basins. Yet the function of song remains debated: male-only singing during breeding
  season supports mate attraction, but playback experiments yield inconsistent female
  responses. Individual identification is possible from call structure for some cetaceans
  but not systematically studied for humpback song. Blue and fin whale calls propagate
  through the SOFAR channel at basin scale (>1000 km), raising the possibility that
  low-frequency calls serve navigational or population coordination functions. Passive
  acoustic monitoring networks (hydrophone arrays) can triangulate call positions using
  time-difference-of-arrival (TDOA), but the resolution degrades at basin scale due to
  multipath propagation and uncertain sound-speed profiles.
systematic_gaps:
  - No information-theoretic analysis has quantified the Shannon entropy of humpback whale song and compared it to other communication systems.
  - The spatial resolution of passive TDOA triangulation for blue whale calls in the SOFAR channel has not been empirically characterized using simultaneous satellite tracking.
  - Whether humpbacks actively adjust call frequency for SOFAR channel propagation optimization (analogous to bat Doppler compensation) has not been tested.
last_reviewed: "2026-05-06"
""")

# Bridge K unknown
write('unknowns-catalog/mathematical-physics/u-non-abelian-aharonov-bohm-observable-consequences.yaml', """\
id: u-non-abelian-aharonov-bohm-observable-consequences
title: What experimentally observable consequences distinguish the non-Abelian Aharonov-Bohm effect (SU(2) gauge holonomy) from the Abelian U(1) case, and can they be measured in condensed matter systems?
status: open
priority: medium
disciplines:
  - mathematical-physics
  - physics
  - quantum-physics
  - topology
summary: >
  The Abelian Aharonov-Bohm effect (U(1) gauge theory) produces a scalar phase
  phi = (e/hbar) ∮ A·dl that shifts interference fringes — experimentally confirmed
  to high precision. For non-Abelian gauge theories (SU(2), SU(3)), the holonomy
  ∮ A is a matrix rather than a scalar, and the order of travel around different
  loops matters (non-commutative). The non-Abelian AB effect has been proposed as
  a mechanism for topological quantum computation (braiding non-Abelian anyons in
  fractional quantum Hall states), but experimental realization remains elusive.
  Whether the non-Abelian holonomy produces measurable signatures beyond what Abelian
  theory predicts — and how to disentangle these from other quantum interference
  effects in realistic condensed matter systems — has not been established.
systematic_gaps:
  - No condensed matter experiment has unambiguously demonstrated non-Abelian AB holonomy (as opposed to other non-Abelian topological effects like braiding statistics).
  - The relationship between non-Abelian AB phase and observable interference pattern in multi-path electron interferometers has not been computed for realistic device geometries.
  - Whether topological quantum computing proposals based on non-Abelian anyons require the full non-Abelian AB effect or only non-Abelian braiding statistics has not been clarified.
last_reviewed: "2026-05-06"
""")

# Bridge L unknown
write('unknowns-catalog/engineering/u-spider-silk-recombinant-production-mechanical-parity.yaml', """\
id: u-spider-silk-recombinant-production-mechanical-parity
title: Why does recombinant spider silk produced in bacteria or yeast consistently underperform native spider silk in toughness and tensile strength, and what spinning process parameters close this gap?
status: open
priority: high
disciplines:
  - engineering
  - materials-science
  - biochemistry
  - biology
summary: >
  Native spider silk achieves toughness modulus ~160 MJ/m³ through a precisely controlled
  spinning process: protein solution (dope) at ~50% concentration transitions from liquid
  crystal phase to solid fiber through ion exchange (Na+/K+ for H+), pH drop (7.2 to 6.0),
  and extensional flow in the spinning duct. Recombinant silk proteins expressed in E. coli,
  yeast, tobacco, or transgenic goats can be spun into fibers by post-spinning in methanol
  or water vapor, but consistently produce fibers with toughness 50-80% of native silk.
  The molecular weight of recombinant proteins (limited by expression system to ~100 kDa vs.
  ~300-400 kDa native) and the absence of replication of the native spinning duct chemistry
  are leading candidates for the performance gap. Whether any synthetic spinning process
  can replicate native silk mechanics is an open engineering question.
systematic_gaps:
  - The critical molecular weight threshold above which recombinant silk achieves native-equivalent toughness has not been determined.
  - The relative contributions of spinning duct pH gradient, ion exchange, and extensional flow rate to beta-sheet nanocrystal alignment have not been independently varied in a systematic factorial experiment.
  - Whether native silk toughness requires the full-length spidroin sequence or only specific domain arrangements has not been determined by domain-deletion mutagenesis.
last_reviewed: "2026-05-06"
""")

print("All 12 unknowns written.")

# ─── Hypotheses ───

# Bridge A hypothesis
write('hypotheses/active/h-eis-hodgkin-huxley-parameter-extraction.yaml', """\
id: h-eis-hodgkin-huxley-parameter-extraction
title: >
  Multi-frequency EIS measurements on voltage-clamped excitable cell monolayers can
  extract Hodgkin-Huxley channel gating parameters (g_Na, g_K, tau_m, tau_h) with
  accuracy comparable to patch-clamp, enabling label-free high-throughput ion channel
  pharmacology screening.
status: active
created: "2026-05-06"
last_updated: "2026-05-06"
priority: medium
related_disciplines:
  - biophysics
  - chemistry
  - electrophysiology
  - pharmacology
unknowns_addressed:
  - u-eis-channel-gating-mechanistic-link
evidence_links:
  - type: supporting
    note: >
      Lindner et al. (2013) demonstrated that frequency-resolved impedance measurements
      can distinguish passive membrane resistance from active voltage-gated conductance
      contributions in cardiomyocyte monolayers — proof of concept for parameter extraction.
  - type: supporting
    note: >
      RTCA (Roche Applied Science) platform detects hERG channel block at 10 kHz
      impedance frequency as a reduction in cell-electrode coupling resistance,
      demonstrating that channel pharmacology is detectable by EIS.
  - type: contradicting
    note: >
      The ill-posedness of the HH-parameter inverse problem from EIS: without voltage
      control, measured impedance is a nonlinear convolution of channel kinetics, membrane
      potential distribution, and cell geometry that may not be uniquely invertible.
proposed_tests:
  - discipline: biophysics
    description: >
      Culture HL-1 cardiomyocytes (constitutively active Na/K channels) on gold RTCA
      electrodes. Perform simultaneous EIS (0.1 Hz to 100 kHz, 10 mV RMS AC) and
      whole-cell patch clamp under voltage clamp. Fit the EIS spectrum to an HH-
      equivalent circuit model and compare extracted tau_m, tau_h, g_Na with patch-
      clamp values. Repeat with TTX (Na channel blocker) and 4-AP (K channel blocker)
      to validate parameter sensitivity.
  - discipline: pharmacology
    description: >
      Screen 50 known hERG channel blockers (varying potency) against RTCA EIS
      measurements. Test whether the EIS-derived channel resistance change
      (Delta R_channel) correlates with patch-clamp IC50 values across 3 orders of
      magnitude of potency — validating EIS as a pharmacological screening surrogate.
""")

# Bridge B hypothesis
write('hypotheses/active/h-da-mechanism-welfare-improving-redesign.yaml', """\
id: h-da-mechanism-welfare-improving-redesign
title: >
  Redesigning real-world matching mechanisms from immediate-acceptance (Boston) to
  deferred-acceptance produces measurable welfare improvements for the proposing side
  without reducing stability, replicating the NRMP result in school-choice and
  teacher-placement markets.
status: active
created: "2026-05-06"
last_updated: "2026-05-06"
priority: high
related_disciplines:
  - economics
  - social-science
  - mathematics
  - mechanism-design
unknowns_addressed:
  - u-matching-markets-dynamic-stability
evidence_links:
  - type: supporting
    doi: "10.1086/261272"
    note: >
      Roth (1984) documented that the NRMP switch to worker-proposing DA improved
      resident welfare — the canonical empirical demonstration of mechanism redesign benefit.
  - type: supporting
    note: >
      Abdulkadiroglu & Sonmez (2003) formally showed Boston mechanism is manipulable
      and proposed DA for school choice; Boston adopted DA in 2006 with subsequent
      welfare analysis showing improvement for strategic sophistication subgroups.
  - type: contradicting
    note: >
      Pathak & Sonmez (2008) showed that in some markets, manipulable mechanisms
      benefit unsophisticated students who happen to prefer their first-choice schools
      — DA may disadvantage students with non-strategic preferences in specific market structures.
proposed_tests:
  - discipline: economics
    description: >
      Use regression discontinuity on the Boston school-choice mechanism switch (2006)
      to estimate the causal effect on student assignment quality (distance to school,
      school quality ranking). Compare outcomes for students at the margin of mechanism
      manipulation vs. those well within their preferred school's capacity.
  - discipline: social-science
    description: >
      Survey new medical residents across NRMP-participating and non-participating
      specialties about satisfaction with match outcomes, controlling for specialty
      competitiveness. Test whether DA-matched residents report higher satisfaction
      with match outcome than those in specialties using informal signaling and
      non-DA matching.
""")

# Bridge C hypothesis
write('hypotheses/active/h-rna-electrostatic-packaging-signal-design.yaml', """\
id: h-rna-electrostatic-packaging-signal-design
title: >
  The electrostatic interaction between RNA packaging signals and positively charged
  coat protein N-terminal tails can be computationally redesigned to create artificial
  virus-like particles (VLPs) that self-assemble around arbitrary RNA cargo with
  T-number selectivity, enabling programmable RNA delivery vectors.
status: active
created: "2026-05-06"
last_updated: "2026-05-06"
priority: high
related_disciplines:
  - biology
  - physics
  - structural-biology
  - bioengineering
unknowns_addressed:
  - u-capsid-assembly-kinetic-intermediates
evidence_links:
  - type: supporting
    note: >
      Comas-Garcia et al. (2014) showed that alfalfa mosaic virus coat protein
      assembles around heterologous RNA in vitro when the RNA contains packaging
      signal stem-loops — demonstrating programmability of electrostatic co-assembly.
  - type: supporting
    doi: "10.1038/35098134"
    note: >
      Smith et al. (2001) phi29 packaging motor can encapsidate foreign dsDNA
      when provided in linearized form — demonstrates that packaging motors are
      not absolutely sequence-specific.
  - type: contradicting
    note: >
      Packaging signal specificity in RNA viruses (MS2, hepatitis B) is sequence-
      specific, not purely electrostatic — redesigned RNA sequences that match
      charge but not sequence fail to package efficiently in these systems.
proposed_tests:
  - discipline: structural-biology
    description: >
      Express 3 variants of cowpea chlorotic mottle virus (CCMV) coat protein with
      N-terminal tails of varying charge (+4, +8, +12). Mix with eGFP mRNA and
      incubate under assembly conditions. Quantify assembly yield (DLS, SEC-MALS),
      RNA packaging efficiency (RNase protection assay), and T-number distribution
      (cryo-EM) as a function of tail charge and RNA length.
  - discipline: bioengineering
    description: >
      Test VLP delivery of a therapeutic RNA (siRNA against VEGF) assembled using
      redesigned coat protein in an in vitro tumor spheroid model. Compare knockdown
      efficiency and cell viability to lipid nanoparticle delivery. Assess VLP
      stability in serum (t½) as a function of coat protein modification.
""")

# Bridge D hypothesis
write('hypotheses/active/h-differential-privacy-urban-analytics-accuracy-threshold.yaml', """\
id: h-differential-privacy-urban-analytics-accuracy-threshold
title: >
  A privacy budget of epsilon ≤ 1 (strong differential privacy) is sufficient to
  produce accurate city-scale traffic flow models from cellular mobility data, with
  model error below 10% for flows aggregated at 500-meter spatial resolution —
  resolving the accuracy-privacy tradeoff at operationally useful precision.
status: active
created: "2026-05-06"
last_updated: "2026-05-06"
priority: medium
related_disciplines:
  - engineering
  - social-science
  - computer-science
  - urban-planning
unknowns_addressed:
  - u-smart-city-equity-algorithmic-routing
evidence_links:
  - type: supporting
    note: >
      Mir et al. (2013) showed that differentially private traffic flow queries
      with epsilon=1 achieve <15% mean absolute error for highway segment counts
      at hourly aggregation — close to the 10% threshold at coarser spatial resolution.
  - type: supporting
    note: >
      Duchi et al. (2014) established minimax optimal rates for local differential
      privacy, showing that accuracy scales as sqrt(n) / epsilon — larger populations
      permit stronger privacy with fixed accuracy, suggesting city-scale data
      (millions of probes) can sustain epsilon ≤ 1.
  - type: contradicting
    note: >
      The Laplace mechanism noise scales with sensitivity / epsilon; for fine-grained
      OD (origin-destination) matrix estimation (n² cells for n zones), the sensitivity
      may be too high for epsilon=1 to achieve useful accuracy at small zone granularity.
proposed_tests:
  - discipline: computer-science
    description: >
      Use the Microsoft Research open dataset of cellular mobility traces (Cabspotting,
      or equivalent) to simulate DP noise injection at epsilon in [0.1, 0.5, 1, 2, 10].
      Fit a gravity model traffic flow prediction to the noisy data. Measure mean absolute
      percentage error (MAPE) of flow predictions against ground-truth counts at 500m,
      1km, and 2km spatial resolutions. Identify the epsilon threshold at which MAPE
      drops below 10% for each resolution.
  - discipline: urban-planning
    description: >
      Survey city transportation planners in 5 cities to establish their minimum
      acceptable prediction accuracy for traffic signal timing decisions. Benchmark
      this against the achievable accuracy at epsilon ≤ 1 to determine whether
      strong DP is compatible with operational planning requirements.
""")

# Bridge E hypothesis
write('hypotheses/active/h-rayleigh-benard-turbulence-bifurcation-cascade.yaml', """\
id: h-rayleigh-benard-turbulence-bifurcation-cascade
title: >
  The transition to turbulence in Rayleigh-Bénard convection follows a finite sequence
  of identifiable bifurcations (pitchfork, Hopf, torus, chaos) whose order and
  critical Ra values can be predicted from a low-dimensional center-manifold reduction
  without full DNS, enabling efficient turbulence onset prediction for engineering heat
  transfer applications.
status: active
created: "2026-05-06"
last_updated: "2026-05-06"
priority: medium
related_disciplines:
  - physics
  - mathematics
  - fluid-dynamics
  - nonlinear-dynamics
unknowns_addressed:
  - u-lorenz-attractor-universality-class
evidence_links:
  - type: supporting
    note: >
      Libchaber and Maurer (1982) experimental observation of period-doubling route to
      chaos in liquid helium Rayleigh-Bénard convection — confirmed Feigenbaum
      universality in a physical fluid system.
  - type: supporting
    note: >
      Manneville and Pomeau (1979) identified the intermittency route to chaos
      as an alternative to period-doubling — both routes occur in Bénard convection
      depending on Prandtl number and aspect ratio, consistent with bifurcation theory.
  - type: contradicting
    note: >
      At high Ra (Ra >> Ra_c), turbulence is fully developed and the bifurcation
      cascade picture breaks down — no low-dimensional description captures turbulent
      convection, and the route-to-chaos prediction fails for large aspect ratio cells.
proposed_tests:
  - discipline: physics
    description: >
      Run DNS of Rayleigh-Bénard convection in a small-aspect-ratio cell (Gamma = 1)
      at Prandtl number Pr = 0.7 for Ra from 1.5*Ra_c to 100*Ra_c. At each Ra,
      compute the Floquet multipliers of the periodic orbit to identify bifurcation
      type. Compare onset Ra values for each bifurcation to predictions from a
      Galerkin-reduced model truncated at 10 modes.
  - discipline: mathematics
    description: >
      Apply normal form theory (center manifold reduction) to the Oberbeck-Boussinesq
      equations near Ra_c to derive the amplitude equation for convective rolls.
      Extend to second bifurcation using equivariant bifurcation theory (symmetry
      breaking from D4 to D2). Test whether the predicted Hopf bifurcation Ra matches
      the DNS value.
""")

# Bridge F hypothesis
write('hypotheses/active/h-geographic-mosaic-coevolution-trait-variance.yaml', """\
id: h-geographic-mosaic-coevolution-trait-variance
title: >
  Thompson's geographic mosaic theory predicts higher among-population variance in
  coevolving traits (TTX level in newts, resistance in snakes) than in non-coevolving
  traits in the same species — a signature detectable by comparing population-level
  trait variance across hot-spot and cold-spot populations.
status: active
created: "2026-05-06"
last_updated: "2026-05-06"
priority: medium
related_disciplines:
  - ecology
  - evolutionary-biology
  - population-genetics
unknowns_addressed:
  - u-red-queen-molecular-clock-arms-race
evidence_links:
  - type: supporting
    doi: "10.1111/j.0014-3820.2002.tb01373.x"
    note: >
      Brodie et al. (2002) documented geographic variation in TTX resistance in T.
      sirtalis populations correlated with local Taricha TTX levels — consistent with
      hot-spot/cold-spot mosaic prediction.
  - type: supporting
    note: >
      Zangerl & Berenbaum (2003) plant-insect coevolution: wild parsnip furanocoumarin
      levels and parsnip webworm resistance show correlated geographic variation
      across 20 populations — direct test of geographic mosaic.
  - type: contradicting
    note: >
      Gene flow between populations may homogenize coevolving traits even when local
      selection differs, obscuring the predicted hot-spot/cold-spot pattern — the
      geographic mosaic signal requires sufficiently low migration relative to selection.
proposed_tests:
  - discipline: ecology
    description: >
      Sample 30 T. sirtalis populations across the Pacific Northwest at sites with
      known Taricha TTX levels (hot spots vs. cold spots classified by Brodie lab data).
      Measure TTX resistance (Nav1.4 resistance allele frequency by genotyping) and
      TTX level (HPLC) for 20 individuals per population. Test whether among-population
      variance in resistance allele frequency is higher in hot-spot populations and
      whether it correlates with local TTX level after controlling for population
      structure (FST correction).
""")

# Bridge G hypothesis
write('hypotheses/active/h-lottery-ticket-sparse-subnetwork-universality.yaml', """\
id: h-lottery-ticket-sparse-subnetwork-universality
title: >
  Winning lottery ticket subnetworks are not random sparse subsets of the full network
  but occupy a specific geometric region of the loss landscape — near a flat manifold
  of global minima — and the same winning tickets emerge independently across multiple
  training runs with different random seeds, demonstrating reproducibility of sparsity
  structure.
status: active
created: "2026-05-06"
last_updated: "2026-05-06"
priority: medium
related_disciplines:
  - mathematics
  - machine-learning
  - computer-science
unknowns_addressed:
  - u-neural-network-loss-landscape-global-structure
evidence_links:
  - type: supporting
    note: >
      Frankle et al. (2020) showed that winning tickets identified by iterative
      magnitude pruning are consistent across multiple random seeds when using
      late rewinding (resetting weights to their values at a late iteration of
      training, not initialization) — suggesting convergence to a common sparse structure.
  - type: supporting
    note: >
      Morcos et al. (2019) demonstrated that winning tickets generalize across
      datasets (from CIFAR-10 to CIFAR-100) and across related architectures,
      suggesting a universal sparse structure not specific to one training distribution.
  - type: contradicting
    note: >
      Frankle & Carlin (2019) original paper showed winning tickets at initialization
      are fragile and require rewinding for large networks — the geometric interpretation
      at initialization is unclear; winning tickets may be a property of the optimization
      trajectory rather than the initial landscape.
proposed_tests:
  - discipline: machine-learning
    description: >
      Train ResNet-50 on ImageNet with 10 different random seeds. Apply iterative
      magnitude pruning (80% sparsity) to each. Compute pairwise Jaccard similarity
      of the surviving weight masks. Test whether the mean Jaccard similarity significantly
      exceeds 0.5 (random expectation) — if so, winning tickets are convergent
      across seeds rather than seed-specific.
  - discipline: mathematics
    description: >
      Map the loss landscape in the vicinity of winning ticket subnetwork solutions
      using 2D loss surface visualization (Li et al. 2018 method). Measure the
      flatness (Hessian trace) at winning ticket minima vs. random pruned network
      minima. Test whether winning tickets systematically occupy flatter regions,
      consistent with residing on a wide flat manifold.
""")

# Bridge H hypothesis
write('hypotheses/active/h-tau-propagation-circuit-connectivity-determines-staging.yaml', """\
id: h-tau-propagation-circuit-connectivity-determines-staging
title: >
  Tau propagation in Alzheimer's disease follows the structural connectome hierarchy
  (entorhinal → hippocampal → association cortex) because cell-to-cell transfer rate
  is proportional to synaptic connection strength, and disrupting the entorhinal-CA1
  projection with targeted connectivity interruption will slow Braak staging progression
  in mouse models.
status: active
created: "2026-05-06"
last_updated: "2026-05-06"
priority: high
related_disciplines:
  - neuroscience
  - cell-biology
  - molecular-biology
unknowns_addressed:
  - u-prion-like-spread-neurodegeneration-circuit-specificity
evidence_links:
  - type: supporting
    doi: "10.1126/science.1072994"
    note: >
      Hardy & Selkoe (2002) amyloid cascade hypothesis positions Abeta as initiator
      and tau as propagating effector — implies tau propagation is downstream of
      and mechanistically separable from Abeta accumulation.
  - type: supporting
    note: >
      De Calignon et al. (2012) Science: tau pathology spreads from entorhinal cortex
      to hippocampus in rTgTauEC mice (entorhinal-specific tau expression) — direct
      evidence for transneuronal tau propagation along anatomical connections.
  - type: contradicting
    note: >
      Cope et al. (2018) found that tau propagation is not strictly connectivity-
      dependent in some mouse models — vulnerable neurons show early tau even without
      direct synaptic input from seeded regions, suggesting vulnerability-intrinsic
      factors (local protein expression, metabolic activity) also contribute.
proposed_tests:
  - discipline: neuroscience
    description: >
      Inject AAV-tau-P301L into entorhinal cortex of 3 mouse groups: intact controls,
      chemogenetic silencing of entorhinal-CA1 axons (DREADD-Gi, chronic), and
      axon ablation (diphtheria toxin receptor expressed in entorhinal projections).
      Measure tau burden by immunohistochemistry in CA1, CA3, dentate gyrus, and
      association cortex at 3, 6, and 12 months. Test whether silencing or ablation
      of the projection slows tau spread to CA1 proportional to the reduction in
      synaptic activity.
""")

# Bridge I hypothesis
write('hypotheses/active/h-psilocybin-rescheduling-neuroplasticity-evidence.yaml', """\
id: h-psilocybin-rescheduling-neuroplasticity-evidence
title: >
  Psilocybin's antidepressant efficacy comparable to SSRIs (Carhart-Harris 2021)
  derives from 5-HT2A-mediated BDNF upregulation and rapid dendritic spine growth
  (neuroplasticity), and this mechanistic evidence satisfies the pharmacological
  criteria for removal from Schedule I — providing a scientifically tractable basis
  for rescheduling that is distinct from political arguments.
status: active
created: "2026-05-06"
last_updated: "2026-05-06"
priority: high
related_disciplines:
  - pharmacology
  - social-science
  - chemistry
  - neuroscience
unknowns_addressed:
  - u-opioid-prescribing-policy-chemistry-disconnect
evidence_links:
  - type: supporting
    doi: "10.1056/NEJMoa2032994"
    note: >
      Carhart-Harris et al. (2021) NEJM RCT: psilocybin vs. escitalopram in major
      depressive disorder — no significant difference in primary outcome (QIDS-SR-16)
      with psilocybin showing superiority on secondary measures.
  - type: supporting
    note: >
      Ly et al. (2018) Cell Reports: psilocybin promotes structural and functional
      plasticity of human cortical neurons — BDNF upregulation, dendritic spine
      density increase within 24 hours at psychedelic doses.
  - type: contradicting
    note: >
      Schedule I criteria include "high potential for abuse" — psilocybin does not
      produce physical dependence and has low addiction liability by standard metrics,
      but its scheduling is also based on historical and political factors (Controlled
      Substances Act 1970) that may require legislative rather than purely scientific action.
proposed_tests:
  - discipline: pharmacology
    description: >
      Systematic review and meta-analysis of all psilocybin clinical trials published
      through 2026 (depression, OCD, addiction, end-of-life anxiety). Compute pooled
      effect sizes vs. placebo and active comparators. Cross-reference with the DEA
      scheduling criteria checklist (abuse potential, safety profile, accepted medical
      use). Assess whether the pharmacological evidence profile satisfies the legal
      standard for Schedule II or III classification.
  - discipline: neuroscience
    description: >
      MRI-based dendritic density mapping (diffusion MRI NODDI) in psilocybin-treated
      patients vs. escitalopram-treated patients. Test whether psilocybin produces
      greater increases in neurite orientation dispersion index (ODI) in prefrontal
      cortex — a proxy for dendritic spine density — and whether ODI changes correlate
      with antidepressant response, providing a biomarker for the neuroplasticity mechanism.
""")

# Bridge J hypothesis
write('hypotheses/active/h-bat-echolocation-neural-matched-filter-implementation.yaml', """\
id: h-bat-echolocation-neural-matched-filter-implementation
title: >
  The inferior colliculus of echolocating bats implements a neural matched filter
  optimally tuned to the species-specific FM sweep waveform — neurons with delay-
  tuned delay-period responses functionally equivalent to radar matched filters —
  and this implementation is sufficient to account for the 2-3 mm range resolution
  measured behaviorally.
status: active
created: "2026-05-06"
last_updated: "2026-05-06"
priority: medium
related_disciplines:
  - neuroscience
  - physics
  - sensory-biology
unknowns_addressed:
  - u-whale-song-information-content-localization
evidence_links:
  - type: supporting
    doi: "10.1126/science.441058"
    note: >
      Simmons (1979) showed that big brown bat range discrimination of 0.75 mm
      approaches the physical limit for FM sweep bandwidth — consistent with matched
      filter processing achieving delta_R = c/2B.
  - type: supporting
    note: >
      Suga & O'Neill (1979) Science: FM-FM neurons in mustached bat auditory cortex
      are tuned to specific echo delays relative to emitted pulse — direct neural
      correlate of delay-line coincidence detection, analogous to Jeffress ITD detector.
  - type: contradicting
    note: >
      Some bat behaviors (target glint discrimination, object shape encoding) exceed
      what a simple matched filter can achieve — suggesting additional neural processing
      beyond the matched filter (possibly involving two-glint interference or spectral
      analysis of FM echoes).
proposed_tests:
  - discipline: neuroscience
    description: >
      Record from inferior colliculus neurons in big brown bat (Eptesicus fuscus)
      during playback of FM sweeps matched to natural calls vs. spectrally reversed
      (anti-chirp) sweeps. Test whether response magnitude and latency are higher
      for the natural chirp — consistent with matched filter tuning. Compute the
      theoretical matched filter output for each waveform and compare to measured
      neural response to assess whether neurons approach optimal detection.
  - discipline: physics
    description: >
      Model the bat auditory periphery (basilar membrane filter bank) as a bank of
      bandpass filters. Compute the output of each filter for natural FM sweeps.
      Show analytically that the delay between peak filter responses encodes target
      range with resolution delta_R = c/2B. Compare to published neural delay
      tuning data from mustached bat IC to test quantitative agreement.
""")

# Bridge K hypothesis
write('hypotheses/active/h-chern-simons-theory-topological-quantum-computation.yaml', """\
id: h-chern-simons-theory-topological-quantum-computation
title: >
  Chern-Simons gauge theory at level k provides the mathematical framework for
  topological quantum computation via anyons in the fractional quantum Hall state
  at filling fraction nu = 1/(2k+1), and the non-Abelian case (nu = 5/2) supports
  universal quantum gates through braiding operations that are exponentially
  protected from local decoherence.
status: active
created: "2026-05-06"
last_updated: "2026-05-06"
priority: high
related_disciplines:
  - mathematical-physics
  - quantum-physics
  - topology
  - quantum-computing
unknowns_addressed:
  - u-non-abelian-aharonov-bohm-observable-consequences
evidence_links:
  - type: supporting
    note: >
      Witten (1989) showed that Chern-Simons theory produces knot invariants (Jones
      polynomial) and predicts the statistics of anyons in fractional quantum Hall
      states — the mathematical foundation for topological quantum computation.
  - type: supporting
    note: >
      Nayak et al. (2008) Reviews of Modern Physics: comprehensive review of non-Abelian
      anyons and topological quantum computation — establishes that braiding operations
      of Fibonacci anyons (predicted in nu=12/5 FQH state) can implement universal
      quantum gates.
  - type: contradicting
    note: >
      Experimental realization of non-Abelian anyons at nu = 5/2 remains contested —
      some experiments support Ising anyon statistics (sufficient for some gates but
      not universal), and the topological protection advantage over conventional
      error-corrected qubits has not been demonstrated.
proposed_tests:
  - discipline: quantum-physics
    description: >
      Perform anyon interferometry experiment in GaAs/AlGaAs 2DEG at nu = 5/2.
      Insert a quantum point contact to create an anyon interferometer. Measure
      the Aharonov-Bohm oscillation period as a function of enclosed anyons to
      determine whether the charge is e/4 (non-Abelian Ising anyon) or e/2 (Abelian).
      Compare oscillation visibility as a function of temperature to predictions of
      Chern-Simons theory at k = 2.
  - discipline: mathematical-physics
    description: >
      Compute the braid group representation matrices for Fibonacci anyons (nu = 12/5)
      using the R and F matrices from Chern-Simons theory at k = 3. Verify computationally
      that the resulting braid matrices generate a dense subgroup of SU(2^n) for n anyons,
      confirming universal quantum computation by braiding alone.
""")

# Bridge L hypothesis
write('hypotheses/active/h-biomimicry-design-convergence-performance-ceiling.yaml', """\
id: h-biomimicry-design-convergence-performance-ceiling
title: >
  Biomimicry-derived designs converge on performance ceilings set by the underlying
  physical constraints — not by evolutionary history — so that lotus-inspired surfaces,
  whale-tubercle blades, and spider-silk analogs will asymptotically approach but not
  surpass the physical limits for superhydrophobicity, stall delay, and toughness
  respectively, confirming natural selection as an effective but not omniscient optimizer.
status: active
created: "2026-05-06"
last_updated: "2026-05-06"
priority: medium
related_disciplines:
  - ecology
  - engineering
  - materials-science
  - physics
unknowns_addressed:
  - u-spider-silk-recombinant-production-mechanical-parity
evidence_links:
  - type: supporting
    doi: "10.1002/jmor.1052250106"
    note: >
      Fish & Battle (1995) tubercle geometry analysis: leading-edge wavelength and
      amplitude are within 10% of values predicted to maximize stall angle delay
      from thin-airfoil theory — suggesting near-optimal geometric tuning by evolution.
  - type: supporting
    note: >
      Cassie-Baxter superhydrophobic surfaces (contact angle 180° = total non-wetting)
      are physically achievable; lotus leaf achieves ~160° — there is a measurable gap
      from the physical limit, suggesting room for engineering improvement beyond biology.
  - type: contradicting
    note: >
      The physical constraint framing may be too simple: biological materials are
      multifunctional (lotus leaf is also gas-exchanging, light-harvesting, and self-
      repairing) so the biological optimum is a multi-objective compromise, not a
      single-metric optimum. Engineering designs optimized for a single metric may
      legitimately surpass biological performance on that metric while sacrificing others.
proposed_tests:
  - discipline: materials-science
    description: >
      Fabricate a systematic series of superhydrophobic surfaces (SiO2 nanopillar arrays)
      with varying pillar height (h), diameter (d), and pitch (p), sweeping the full
      parameter space from lotus-geometry to optimal Cassie-Baxter geometry. Measure
      contact angle, roll-off angle, and durability (abrasion resistance). Identify the
      geometry that maximizes contact angle while maintaining durability comparable to
      the lotus surface. Compare this optimum to the lotus geometry to test whether
      biology is at the engineering optimum or has multi-functional constraints.
  - discipline: engineering
    description: >
      Systematic CFD parameter sweep of tubercle wavelength (lambda) and amplitude (A)
      on NACA 0012 airfoil at Reynolds number 500,000. Map the stall angle and maximum
      CL as a function of lambda/c and A/c (chord fractions). Identify the CFD optimum
      and compare to the humpback whale geometry. Test whether the whale geometry lies
      within 5% of the CFD optimum or whether engineering optimization could substantially
      improve on the biological design.
""")

print("All 12 hypotheses written.")

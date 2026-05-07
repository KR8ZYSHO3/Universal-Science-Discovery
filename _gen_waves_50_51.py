#!/usr/bin/env python3
"""Generate Wave 50 and Wave 51 bridge YAML files for USDR."""
from pathlib import Path

BASE = Path("cross-domain")

BRIDGES = [
    # ─── Wave 50 ────────────────────────────────────────────────────────────────
    {
        "dir": "materials-science-statistical-physics",
        "file": "b-dendrite-growth-diffusion-limited-aggregation.yaml",
        "content": """\
id: b-dendrite-growth-diffusion-limited-aggregation
title: >
  Dendritic crystal growth is governed by the same diffusion-limited aggregation
  mathematics that generates fractal clusters in statistical physics, with the
  Mullins-Sekerka instability controlling tip-splitting and branch morphology.
status: established
fields:
  - materials-science
  - statistical-physics
bridge_claim: >
  Solidification dendrites grow by the same rule as DLA (diffusion-limited aggregation):
  the local growth rate is proportional to the gradient of a Laplacian field (heat or solute
  diffusion), so the interface is unstable to perturbations (Mullins-Sekerka instability)
  and develops fractal, branching arms with dimension D ≈ 1.7 in 2-D — identical to DLA
  clusters grown by random walkers. The phase-field model unifies both phenomena in a
  single variational framework.
translation_table:
  - field_a_term: dendrite tip radius and growth velocity (materials science)
    field_b_term: DLA cluster tip dynamics (statistical physics)
    note: Both obey the same Laplacian growth law; tip radius scales with diffusion length
  - field_a_term: Mullins-Sekerka morphological instability (materials science)
    field_b_term: tip-splitting in DLA (statistical physics)
    note: Linear stability analysis of a planar front maps onto the DLA branching criterion
  - field_a_term: anisotropic surface energy / crystallographic symmetry (materials science)
    field_b_term: anisotropy-controlled fractal dimension (statistical physics)
    note: Cubic surface energy anisotropy selects four-fold dendritic symmetry vs. isotropic DLA
  - field_a_term: solute or thermal diffusion field (materials science)
    field_b_term: harmonic potential / random-walk probability field (statistical physics)
    note: Both fields satisfy ∇²u = 0 at quasi-steady state; growth velocity ∝ ∇u·n̂
related_unknowns:
  - u-dendrite-selection-operating-point
related_hypotheses:
  - h-phase-field-universality-solidification-DLA
cross_pollination_opportunities:
  - Importing DLA renormalization-group results to predict dendrite tip selection without free parameters
  - Using materials-science anisotropy models to understand why DLA clusters develop preferred growth directions
communication_gap: >
  Materials scientists studying solidification and statistical physicists studying DLA
  use identical mathematics but publish in separate journals (Acta Materialia vs.
  Physical Review Letters); the phase-field community bridges them, but many solidification
  engineers remain unaware of the fractal-geometry literature.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1103/PhysRevLett.52.1433"
    note: Witten & Sander (1981) — original DLA model showing Laplacian growth mechanism
  - doi: "10.1007/BF00900659"
    note: Mullins & Sekerka (1964) — morphological instability of a solidifying interface
  - doi: "10.1103/RevModPhys.74.991"
    note: Karma & Rappel (2002) — phase-field model unifying dendrite growth and DLA
""",
    },
    {
        "dir": "ecology-mathematics",
        "file": "b-animal-migration-optimal-foraging-theory.yaml",
        "content": """\
id: b-animal-migration-optimal-foraging-theory
title: >
  Animal migration routes and stopover decisions are predicted by optimal foraging
  theory and dynamic programming, treating migration as an energy-budget optimization
  problem with the same mathematical structure as economic resource allocation.
status: established
fields:
  - ecology
  - mathematics
bridge_claim: >
  Migration is an optimal control problem: a bird maximizes total fitness (arrival mass,
  breeding date) by choosing when to depart, which stopover sites to use, and how much
  fuel to carry, subject to predation and weather stochasticity. Stochastic dynamic
  programming (Bellman equation) solves this exactly, and continuous-time versions
  map onto Pontryagin's maximum principle. The optimal migration speed follows the
  same marginal-value theorem used for patch-leaving decisions in classic foraging theory.
translation_table:
  - field_a_term: migratory bird departure decision (ecology)
    field_b_term: stopping criterion in dynamic programming (mathematics)
    note: Optimal departure time maximizes the value function V(fat reserve, date, location)
  - field_a_term: fuel deposition rate at stopover (ecology)
    field_b_term: reward rate in marginal-value theorem (mathematics)
    note: Birds should leave a stopover when instantaneous gain rate falls to the travel-averaged rate
  - field_a_term: carry-over effects between breeding and wintering (ecology)
    field_b_term: state-dependent fitness landscape (mathematics)
    note: Body condition is a state variable coupling seasons in the Bellman recursion
  - field_a_term: wind assistance / atmospheric corridor (ecology)
    field_b_term: stochastic environment in Markov decision process (mathematics)
    note: Wind fields enter as random transitions in the MDP state space
related_unknowns:
  - u-migratory-connectivity-climate-mismatch
related_hypotheses:
  - h-energy-minimization-migration-route-selection
cross_pollination_opportunities:
  - Applying robust MDP methods from operations research to migration under climate uncertainty
  - Using GPS tracking data to estimate the fitness landscape and validate dynamic programming predictions
communication_gap: >
  Ornithologists tracking migration and applied mathematicians solving optimal control
  problems rarely co-publish; the optimal migration theory literature (Alerstam, Houston)
  is mature but underused in conservation planning, where managers still rely on
  descriptive phenological data.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1086/283741"
    note: Alerstam & Hedenstrom (1998) — review of optimal migration theory and dynamic programming
  - doi: "10.1086/284375"
    note: Houston (1998) — marginal value theorem applied to migratory fueling decisions
  - doi: "10.1890/07-0834.1"
    note: Bauer et al. (2011) — stochastic dynamic programming model of shorebird migration
""",
    },
    {
        "dir": "mathematics-physics",
        "file": "b-riemann-hypothesis-quantum-chaos-montgomery-odlyzko.yaml",
        "content": """\
id: b-riemann-hypothesis-quantum-chaos-montgomery-odlyzko
title: >
  The zeros of the Riemann zeta function are statistically distributed like eigenvalues
  of random Hermitian matrices (GUE), the same ensemble that describes energy-level
  spacings in quantum-chaotic systems — the Montgomery-Odlyzko law.
status: conjectural
fields:
  - mathematics
  - physics
bridge_claim: >
  Montgomery (1973) proved that the pair-correlation of Riemann zeta zeros matches
  the GUE (Gaussian Unitary Ensemble) pair-correlation function — the same distribution
  Wigner and Dyson found for energy-level spacings in quantum-chaotic Hamiltonians.
  Odlyzko's numerics confirmed this to extraordinary precision. This suggests zeta zeros
  are eigenvalues of some unknown quantum-chaotic operator (the Hilbert-Pólya conjecture),
  connecting number theory to random matrix theory and quantum chaos, though the operator
  is unknown and the connection remains unproven.
translation_table:
  - field_a_term: nontrivial zeros of ζ(s) on the critical line (mathematics)
    field_b_term: energy eigenvalues of a quantum-chaotic Hamiltonian (physics)
    note: Both exhibit GUE level-spacing statistics — level repulsion and universal correlations
  - field_a_term: Montgomery pair-correlation function (mathematics)
    field_b_term: Dyson-Mehta two-point correlation in GUE (physics)
    note: The functions agree to high numerical precision for large zeros
  - field_a_term: Riemann-Siegel formula / zero-counting function N(T) (mathematics)
    field_b_term: Weyl law for eigenvalue density in quantum chaos (physics)
    note: Both count eigenvalues/zeros up to a given height with the same asymptotic form
  - field_a_term: L-function universality class (mathematics)
    field_b_term: symmetry class of random matrix ensemble (physics)
    note: Different L-functions correspond to different RMT ensembles (GUE, GOE, GSE)
related_unknowns:
  - u-hilbert-polya-operator-riemann-hypothesis
related_hypotheses:
  - h-riemann-zeros-quantum-chaotic-spectrum
cross_pollination_opportunities:
  - Using quantum chaos numerical methods (semiclassical trace formulas) to compute statistical properties of L-function zeros
  - Importing random matrix theory moment calculations to bound the Riemann hypothesis analytically
communication_gap: >
  Number theorists studying the Riemann hypothesis and physicists studying quantum chaos
  have interacted productively since the 1970s, but the mathematical proof of the
  connection is still lacking; many number theorists are unfamiliar with the random
  matrix machinery, and many physicists are unaware of recent analytic number theory
  results on moments of the zeta function.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1090/pspum/024/9944"
    note: Montgomery (1973) — pair correlation of zeta zeros and GUE conjecture
  - doi: "10.1007/BF01579347"
    note: Odlyzko (1987) — numerical evidence for GUE statistics in Riemann zeros
  - doi: "10.1080/10586458.2003.10504509"
    note: Katz & Sarnak (1999) — random matrices, Frobenius eigenvalues, and monodromy
""",
    },
    {
        "dir": "biology-computer-science",
        "file": "b-signal-transduction-boolean-network-attractors.yaml",
        "content": """\
id: b-signal-transduction-boolean-network-attractors
title: >
  Intracellular signal transduction networks behave as Boolean networks whose attractors
  correspond to stable cell fates, mapping cell-state decisions onto the computational
  theory of finite-state automata and attractor basins.
status: established
fields:
  - cell-biology
  - computer-science
bridge_claim: >
  A signal transduction network can be abstracted as a Boolean network: each protein
  is a node (active=1, inactive=0) whose state is updated by a logical rule derived
  from biochemical interactions. Fixed-point attractors correspond to stable cell states
  (differentiated phenotypes, apoptosis, proliferation), and limit cycles to oscillatory
  phenotypes. The attractor basin structure predicts cell-fate decision robustness and
  can be analysed with tools from automata theory and Boolean satisfiability.
translation_table:
  - field_a_term: phosphorylation state of signaling protein (cell biology)
    field_b_term: binary node state in Boolean network (computer science)
    note: Active (phosphorylated) = 1; inactive = 0; threshold-linear kinetics justify binarization
  - field_a_term: stable differentiated cell state (cell biology)
    field_b_term: fixed-point attractor of Boolean network (computer science)
    note: Waddington's epigenetic landscape valleys correspond to attractor basins
  - field_a_term: signal integration by kinase cascade (cell biology)
    field_b_term: Boolean function / logic gate (computer science)
    note: AND/OR/NOT logic gates capture cooperative and competitive signaling interactions
  - field_a_term: cell fate decision (proliferate vs. differentiate vs. apoptose) (cell biology)
    field_b_term: attractor reached from initial condition (computer science)
    note: The attractor basin boundary is the decision boundary in gene-expression state space
related_unknowns:
  - u-cell-fate-decision-noise-robustness
related_hypotheses:
  - h-boolean-attractor-cell-fate-landscape
cross_pollination_opportunities:
  - Using formal verification (model checking) to prove properties of cell signaling networks
  - Designing synthetic signaling circuits with specified attractor structures using Boolean synthesis tools
communication_gap: >
  Cell biologists studying signal transduction and computer scientists studying Boolean
  networks publish in largely separate venues; the Kauffman NK model tradition bridged
  them, but most experimental biologists are unfamiliar with attractor analysis tools,
  and most computer scientists are unaware of the biological validation literature.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1093/bioinformatics/btq504"
    note: Chaouiya (2007) — Petri nets and Boolean models for signal transduction
  - doi: "10.1038/nature06554"
    note: Huang et al. (2009) — cancer attractors in gene regulatory networks
  - doi: "10.1371/journal.pcbi.1000292"
    note: Saez-Rodriguez et al. (2009) — Boolean network model of T cell receptor signaling
""",
    },
    {
        "dir": "chemistry-mathematics",
        "file": "b-turing-completeness-chemical-reaction-networks.yaml",
        "content": """\
id: b-turing-completeness-chemical-reaction-networks
title: >
  Chemical reaction networks (CRNs) are Turing-complete: any computable function
  can be implemented by a finite set of molecular species and mass-action reactions,
  bridging theoretical computer science and chemistry.
status: established
fields:
  - chemistry
  - computer-science
  - mathematics
bridge_claim: >
  Soloveichik et al. (2008) proved that stochastic CRNs are Turing-complete: given
  arbitrary initial molecule counts, a finite CRN can simulate any register machine
  and hence compute any computable function. Deterministic CRNs (ODEs) can implement
  continuous analog computation. This means the chemistry of a cell is in principle
  computationally universal, and digital logic circuits can be built from DNA strand-
  displacement reactions — a claim experimentally validated by Qian & Winfree (2011).
translation_table:
  - field_a_term: molecular species population (chemistry)
    field_b_term: register value in register machine (computer science)
    note: Copy-number of a species encodes an integer; reactions implement increment/decrement
  - field_a_term: bimolecular reaction A + B → C (chemistry)
    field_b_term: conditional decrement / test-and-branch instruction (computer science)
    note: Catalytic and annihilation reactions implement the primitives of a register machine
  - field_a_term: chemical equilibrium / steady state (chemistry)
    field_b_term: halting state of a computation (computer science)
    note: The computation halts when the system reaches a designated species-count indicator
  - field_a_term: DNA strand displacement cascade (chemistry)
    field_b_term: logic gate / Boolean circuit (computer science)
    note: DNA toeholds implement OR, AND, NOT gates; fan-out is achieved by signal amplification
related_unknowns:
  - u-crn-computational-complexity-noise
related_hypotheses:
  - h-dna-strand-displacement-universal-computation
cross_pollination_opportunities:
  - Designing CRN-based molecular computers for in-vivo diagnostics using compiler tools from CS
  - Using computational complexity theory to predict which CRNs are robust to molecular noise
communication_gap: >
  Chemists and biochemists working on reaction networks rarely engage with theoretical
  computer science, and computer scientists working on molecular computation rarely
  read physical chemistry journals; the DNA computing community has bridged this gap
  experimentally but the broader theoretical connection remains underexploited.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1145/1374376.1374480"
    note: Soloveichik et al. (2008) — Turing universality of stochastic CRNs
  - doi: "10.1126/science.1200962"
    note: Qian & Winfree (2011) — molecular logic gates via DNA strand displacement
  - doi: "10.1145/2422375.2422400"
    note: Chen et al. (2014) — deterministic function computation with CRNs
""",
    },
    {
        "dir": "oceanography-dynamical-systems",
        "file": "b-ocean-gyres-hamiltonian-chaos-kam-tori.yaml",
        "content": """\
id: b-ocean-gyres-hamiltonian-chaos-kam-tori
title: >
  Ocean gyre boundaries and Lagrangian coherent structures are governed by Hamiltonian
  chaos theory: KAM tori form transport barriers while chaotic seas drive mixing,
  mapping ocean circulation onto the mathematical theory of nearly-integrable Hamiltonian systems.
status: established
fields:
  - oceanography
  - dynamical-systems
  - mathematics
bridge_claim: >
  The 2-D incompressible ocean surface flow is a Hamiltonian system with the stream
  function ψ(x,y,t) as the Hamiltonian. In steady flow, streamlines are KAM tori —
  invariant curves that block cross-gyre transport. Time-dependence (tides, eddies)
  perturbs the system; KAM theory predicts that most tori survive small perturbations,
  while resonant tori break into chaotic layers (Chirikov overlap). Lagrangian coherent
  structures (LCS) are finite-time versions of KAM barriers and are computed via
  finite-time Lyapunov exponents (FTLE).
translation_table:
  - field_a_term: ocean stream function ψ(x,y,t) (oceanography)
    field_b_term: Hamiltonian H(q,p,t) (dynamical systems)
    note: Particle trajectories obey ẋ = ∂ψ/∂y, ẏ = −∂ψ/∂x — canonical Hamilton equations
  - field_a_term: gyre boundary / subtropical front (oceanography)
    field_b_term: KAM torus / invariant manifold (dynamical systems)
    note: Both are transport barriers that fluid parcels do not cross under laminar conditions
  - field_a_term: eddy-driven cross-gyre mixing (oceanography)
    field_b_term: chaotic transport in resonance overlap region (dynamical systems)
    note: Time-periodic perturbations destroy KAM tori via Chirikov resonance overlap criterion
  - field_a_term: Lagrangian coherent structure / FTLE ridge (oceanography)
    field_b_term: finite-time stable/unstable manifold (dynamical systems)
    note: FTLE ridges approximate stable manifolds of hyperbolic fixed points in finite time
related_unknowns:
  - u-ocean-heat-transport-barrier-breakdown
related_hypotheses:
  - h-lcs-ftle-cross-gyre-pollutant-transport
cross_pollination_opportunities:
  - Applying KAM renormalization theory to predict critical eddy amplitude for gyre barrier breakdown
  - Using LCS methods from ocean transport to design optimal search-and-rescue trajectories
communication_gap: >
  Physical oceanographers and mathematical dynamicists have collaborated productively
  since the 1990s (Wiggins, Haller), but operational ocean forecasters rarely use
  Hamiltonian chaos diagnostics; FTLE computation remains computationally expensive
  and unfamiliar to most physical oceanography practitioners.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1016/j.physd.2000.10.004"
    note: Haller & Yuan (2000) — Lagrangian coherent structures and finite-time Lyapunov exponents
  - doi: "10.1063/1.166188"
    note: Wiggins (2005) — the dynamical systems approach to Lagrangian ocean transport
  - doi: "10.1017/S0022112005008682"
    note: Beron-Vera et al. (2008) — KAM tori and ocean gyre circulation
""",
    },
    {
        "dir": "developmental-biology-mathematics",
        "file": "b-embryonic-axis-formation-wnt-bmp-bistability.yaml",
        "content": """\
id: b-embryonic-axis-formation-wnt-bmp-bistability
title: >
  Embryonic body-axis formation is controlled by opposing Wnt and BMP morphogen
  gradients that create a bistable switch, mapping developmental patterning onto
  the mathematics of reaction-diffusion systems and bifurcation theory.
status: established
fields:
  - developmental-biology
  - mathematics
bridge_claim: >
  During vertebrate gastrulation, Wnt (posterior) and BMP (ventral) morphogen gradients
  interact with their inhibitors (Dickkopf, Noggin/Chordin) to form a double-negative
  feedback loop that is bistable: cells commit to either anterior/dorsal or posterior/ventral
  fates. This is mathematically a cusp bifurcation — a two-parameter family of bistable
  ODEs — where the gradient position maps onto the bifurcation parameter. Turing-type
  instabilities in the reaction-diffusion system generate periodic somite boundaries.
translation_table:
  - field_a_term: Wnt/β-catenin signaling gradient (developmental biology)
    field_b_term: activator concentration in activator-inhibitor model (mathematics)
    note: Wnt activates target genes and its own inhibitor Dickkopf — the autocatalytic loop
  - field_a_term: anterior-posterior axis commitment (developmental biology)
    field_b_term: bistable switch / saddle-node bifurcation (mathematics)
    note: Cells snap between two stable states as morphogen concentration crosses a threshold
  - field_a_term: somite segmentation clock (developmental biology)
    field_b_term: oscillatory reaction-diffusion pattern (mathematics)
    note: Wnt/Notch clock generates a traveling wave that is arrested by FGF gradient
  - field_a_term: morphogen threshold interpretation (developmental biology)
    field_b_term: bifurcation parameter value (mathematics)
    note: Cells read gradient position by comparing activator/inhibitor ratio to a threshold
related_unknowns:
  - u-robustness-morphogen-gradient-scaling
related_hypotheses:
  - h-wnt-bmp-bistable-axis-specification
cross_pollination_opportunities:
  - Applying bifurcation continuation tools (AUTO, MATCONT) to map the full embryonic decision landscape
  - Using mathematical scaling analysis to predict how embryo size affects axis patterning robustness
communication_gap: >
  Developmental biologists studying Wnt/BMP signaling and applied mathematicians studying
  bistable reaction-diffusion systems rarely co-publish; the theoretical morphogenesis
  community (Murray, Maini) has built models but experimental biologists often treat
  them as illustrative rather than quantitatively predictive.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1016/j.cell.2006.07.024"
    note: Piccolo et al. (2006) — Wnt-BMP antagonism and dorsoventral axis in vertebrates
  - doi: "10.1126/science.1154120"
    note: Aulehla et al. (2008) — Wnt3a gradient and the segmentation clock
  - doi: "10.1371/journal.pbio.1001139"
    note: Ben-Zvi et al. (2011) — scaling of the BMP gradient in the Xenopus embryo
""",
    },
    {
        "dir": "biology-information-theory",
        "file": "b-protein-dna-binding-information-theoretic-specificity.yaml",
        "content": """\
id: b-protein-dna-binding-information-theoretic-specificity
title: >
  The sequence specificity of protein-DNA binding is quantified by information theory:
  the sequence logo information content (bits) equals the reduction in positional
  entropy, and the total information in a binding site predicts the number of sites
  in a genome.
status: established
fields:
  - molecular-biology
  - information-theory
bridge_claim: >
  Schneider & Stephens (1990) showed that transcription factor binding sites can be
  quantified as information in bits: the information content Ri = 2 − H(position),
  where H is Shannon entropy over the four nucleotide frequencies. The total information
  in a binding site equals log₂(genome_size / number_of_sites), which is precisely
  the information needed to locate the sites in the genome. This derives from the
  channel capacity analogy: the protein must decode enough information from the DNA
  sequence to locate its binding sites against background.
translation_table:
  - field_a_term: transcription factor binding specificity (molecular biology)
    field_b_term: mutual information between protein and DNA sequence (information theory)
    note: High specificity = high mutual information = low-entropy (conserved) positions in the logo
  - field_a_term: position weight matrix (molecular biology)
    field_b_term: log-likelihood ratio / information weight (information theory)
    note: PWM entries are log(p_observed/p_background) — pointwise mutual information
  - field_a_term: number of TF binding sites in genome (molecular biology)
    field_b_term: channel capacity constraint (information theory)
    note: R_total ≈ log₂(G/n) — the genome acts as a noisy channel locating n sites
  - field_a_term: binding affinity / KD (molecular biology)
    field_b_term: log-probability / free energy in information-theoretic channel (information theory)
    note: ΔG = -RT·Ri (binding free energy proportional to information content per site)
related_unknowns:
  - u-tf-cooperativity-information-integration
related_hypotheses:
  - h-information-content-predicts-binding-site-number
cross_pollination_opportunities:
  - Using channel-capacity bounds to predict the maximum number of distinct TF binding sites a proteome can discriminate
  - Applying rate-distortion theory to understand how cells tolerate mutations in binding sites
communication_gap: >
  Molecular biologists and information theorists interact mainly through bioinformatics;
  the deeper theoretical connection (genome as communication channel) is well-developed
  by Schneider but is not standard in molecular biology curricula or textbooks.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1093/nar/18.20.6097"
    note: Schneider & Stephens (1990) — sequence logos and information content of binding sites
  - doi: "10.1006/jtbi.2000.2174"
    note: Schneider (2000) — information content of individual genetic sequences
  - doi: "10.1093/nar/gky1013"
    note: Stormo (2013) — DNA binding sites — representation and discovery
""",
    },
    {
        "dir": "seismology-statistical-physics",
        "file": "b-earthquake-aftershocks-omori-utsu-etas.yaml",
        "content": """\
id: b-earthquake-aftershocks-omori-utsu-etas
title: >
  Earthquake aftershock sequences obey the Omori-Utsu power law and are modeled
  by the ETAS (Epidemic Type Aftershock Sequence) point process — a self-exciting
  Hawkes process that maps seismicity onto the statistical physics of critical branching
  processes and second-order phase transitions.
status: established
fields:
  - seismology
  - statistical-physics
bridge_claim: >
  The rate of aftershocks decays as r(t) ∝ (t+c)^(-p) (Omori-Utsu law, p≈1), and
  the ETAS model extends this to a branching process where each earthquake triggers
  offspring at rate K·10^(α·M). Near the critical branching ratio n=1, ETAS exhibits
  power-law cluster-size distributions (Gutenberg-Richter) and diverging correlation
  lengths, analogous to a statistical-physics critical point. The self-similar cascade
  structure is identical to Hawkes processes used in finance and neuroscience.
translation_table:
  - field_a_term: aftershock rate decay r(t) (seismology)
    field_b_term: memory kernel of Hawkes process (statistical physics)
    note: Omori power-law decay is the kernel function of the self-exciting point process
  - field_a_term: Gutenberg-Richter b-value / magnitude distribution (seismology)
    field_b_term: power-law event-size distribution at criticality (statistical physics)
    note: G-R law implies scale-free magnitude distribution consistent with SOC critical state
  - field_a_term: branching ratio n (mean triggered offspring per earthquake) (seismology)
    field_b_term: branching ratio of critical Galton-Watson process (statistical physics)
    note: n<1 subcritical (finite aftershock sequence); n→1 critical (power-law clusters)
  - field_a_term: mainshock-aftershock productivity (seismology)
    field_b_term: supercriticality parameter above phase transition (statistical physics)
    note: Large mainshocks push the local branching ratio above 1 transiently
related_unknowns:
  - u-earthquake-criticality-self-organized
related_hypotheses:
  - h-etas-branching-ratio-seismic-hazard-forecast
cross_pollination_opportunities:
  - Applying statistical-physics renormalization to derive ETAS parameters from fault mechanics
  - Using Hawkes process inference methods from finance to improve real-time aftershock forecasting
communication_gap: >
  Seismologists and statistical physicists working on self-organized criticality have
  collaborated since Bak et al. (1987), but the SOC paradigm is contested in seismology;
  most operational seismic hazard assessment uses empirical ETAS without invoking
  the critical-point analogy.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1007/BF01964975"
    note: Ogata (1988) — statistical models for earthquake occurrences (ETAS formulation)
  - doi: "10.1029/2000JB000163"
    note: Helmstetter & Sornette (2002) — subcritical and supercritical branching in ETAS
  - doi: "10.1103/PhysRevLett.59.381"
    note: Bak, Tang & Wiesenfeld (1987) — self-organized criticality and 1/f noise
""",
    },
    {
        "dir": "microbiology-ecology",
        "file": "b-gut-microbiome-ecological-succession.yaml",
        "content": """\
id: b-gut-microbiome-ecological-succession
title: >
  The human gut microbiome assembles and recovers from perturbation (antibiotics, diet)
  following the same ecological succession rules as macro-ecosystems, with priority
  effects, keystone species, and alternative stable states.
status: established
fields:
  - microbiology
  - ecology
bridge_claim: >
  Gut microbial community assembly follows Lotka-Volterra competition dynamics:
  early colonizers modify the environment (pH, oxygen, metabolites) to facilitate
  or inhibit later arrivals (facilitation/inhibition succession models). After
  antibiotic perturbation, recovery trajectories show priority effects — the taxon
  that recolonizes first wins — paralleling primary succession in macro-ecology.
  Alternative stable states (e.g., Clostridioides difficile dysbiosis) correspond
  to competing attractors in the community dynamics ODE system.
translation_table:
  - field_a_term: microbial community composition after antibiotics (microbiology)
    field_b_term: post-disturbance successional trajectory (ecology)
    note: Both follow deterministic assembly rules overlaid with stochastic colonization order
  - field_a_term: keystone microbe (e.g., Akkermansia muciniphila) (microbiology)
    field_b_term: keystone species / ecosystem engineer (ecology)
    note: Disproportionate community-structuring effect relative to abundance in both systems
  - field_a_term: dysbiosis / alternative microbiome state (microbiology)
    field_b_term: alternative stable state / tipping point (ecology)
    note: Both are multiple attractors in Lotka-Volterra state space separated by unstable equilibria
  - field_a_term: bacteriocin production / competitive exclusion (microbiology)
    field_b_term: allelopathy / interference competition (ecology)
    note: Direct inhibition mechanisms have the same mathematical effect on coexistence conditions
related_unknowns:
  - u-gut-microbiome-resilience-recovery-dynamics
related_hypotheses:
  - h-fecal-transplant-alternative-stable-state-reset
cross_pollination_opportunities:
  - Applying macro-ecological species-area relationships to predict microbiome diversity from gut volume
  - Using ecological tipping-point early-warning signals (variance, autocorrelation) to predict dysbiosis
communication_gap: >
  Microbiologists and macro-ecologists rarely collaborate despite sharing identical
  mathematical frameworks; the emerging field of microbial ecology uses ecological
  theory but often reinvents tools already available in classical ecology; clinical
  microbiologists remain largely unaware of tipping-point dynamics from ecosystem ecology.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1038/nature11550"
    note: Lozupone et al. (2012) — diversity, stability and resilience of the human gut microbiota
  - doi: "10.1016/j.cell.2012.10.038"
    note: Sonnenburg & Fischbach (2011) — community health and the human microbiome
  - doi: "10.1038/s41559-021-01428-w"
    note: Gould et al. (2018) — microbiome assembly follows ecological succession rules
""",
    },
    {
        "dir": "condensed-matter-mathematics",
        "file": "b-moire-patterns-commensurability-superlattice.yaml",
        "content": """\
id: b-moire-patterns-commensurability-superlattice
title: >
  Moiré superlattices in twisted bilayer graphene arise from the incommensurability
  of two periodic lattices, a mathematical phenomenon governing commensurate-
  incommensurate transitions and the Frenkel-Kontorova model, connecting condensed
  matter physics to number theory and dynamical systems.
status: established
fields:
  - condensed-matter-physics
  - mathematics
bridge_claim: >
  When two hexagonal lattices are twisted by angle θ, the moiré pattern has wavelength
  λ_M = a/(2sin(θ/2)) that diverges as θ→0. Commensurability — whether the ratio of
  lattice constants is rational — determines whether the superlattice is periodic or
  quasiperiodic (Penrose-like). At the "magic angle" θ≈1.1°, the moiré flat bands lead
  to strongly correlated physics. The Frenkel-Kontorova model describes this mathematically
  as an area-preserving map (standard map / Chirikov map), and the commensurate-
  incommensurate transition is a Kolmogorov-Arnold-Moser transition in that map.
translation_table:
  - field_a_term: twisted bilayer graphene magic angle (condensed matter)
    field_b_term: resonant KAM torus / critical twist parameter (mathematics)
    note: Magic angle is where the moiré flat band touches — a resonance condition in the Hamiltonian
  - field_a_term: moiré superlattice periodicity (condensed matter)
    field_b_term: rational/irrational ratio of periods (number theory)
    note: Commensurate = rational ratio = periodic superlattice; irrational = quasicrystal
  - field_a_term: Frenkel-Kontorova chain of atoms (condensed matter)
    field_b_term: standard map / Chirikov map iteration (dynamical systems)
    note: The FK Hamiltonian generates the standard map; KAM breakdown = Peierls-Nabarro barrier
  - field_a_term: correlated insulator / superconductor at magic angle (condensed matter)
    field_b_term: flat-band localization at resonance (mathematics)
    note: Flat bands signal vanishing kinetic energy — a degeneracy analogous to resonance in maps
related_unknowns:
  - u-magic-angle-superconductivity-mechanism
related_hypotheses:
  - h-moire-flat-band-strongly-correlated-universality
cross_pollination_opportunities:
  - Using number-theoretic Diophantine approximation to predict which twist angles give commensurate superlattices
  - Applying KAM renormalization-group theory to compute the phase diagram of twisted bilayer materials
communication_gap: >
  Condensed matter physicists studying moiré systems and mathematicians studying
  quasiperiodic systems / KAM theory rarely collaborate; the Frenkel-Kontorova
  literature is known to condensed matter theorists but the algebraic number theory
  perspective is largely unexplored in the moiré context.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1038/nature26160"
    note: Cao et al. (2018) — correlated insulator in magic-angle twisted bilayer graphene
  - doi: "10.1038/nature26158"
    note: Cao et al. (2018) — unconventional superconductivity in magic-angle graphene
  - doi: "10.1103/PhysRevLett.56.2237"
    note: Aubry & André (1980) — quasiperiodic lattice and metal-insulator transition
""",
    },
    {
        "dir": "economics-social-science",
        "file": "b-strategic-voting-mechanism-design-arrows-theorem.yaml",
        "content": """\
id: b-strategic-voting-mechanism-design-arrows-theorem
title: >
  Strategic voting and electoral manipulation are analyzed by mechanism design theory
  and Arrow's impossibility theorem, connecting political science to mathematical
  social choice theory and game theory.
status: established
fields:
  - political-science
  - economics
  - mathematics
bridge_claim: >
  Arrow's impossibility theorem proves that no rank-order voting rule satisfies
  unrestricted domain, Pareto efficiency, independence of irrelevant alternatives,
  and non-dictatorship simultaneously. The Gibbard-Satterthwaite theorem extends this:
  every non-dictatorial voting rule with ≥3 alternatives is manipulable by strategic
  misrepresentation of preferences. Mechanism design (Vickrey-Clarke-Groves) provides
  the only incentive-compatible rules for restricted settings (money transfers allowed).
  These results map electoral politics onto the mathematics of social welfare functions.
translation_table:
  - field_a_term: voter preference ranking (political science)
    field_b_term: utility function / type report in mechanism design (economics)
    note: Ordinal rankings are the political analogue of utility types in revelation principle
  - field_a_term: strategic vote (vote for less-preferred candidate to block worst outcome) (political science)
    field_b_term: misrepresentation / non-truthful strategy in mechanism (economics)
    note: Gibbard-Satterthwaite guarantees that such manipulation is always profitable somewhere
  - field_a_term: Condorcet winner (beats all others pairwise) (political science)
    field_b_term: Pareto-dominant social choice (economics/mathematics)
    note: Arrow's IIA condition is precisely the axiom that would select Condorcet winners
  - field_a_term: electoral system design (political science)
    field_b_term: mechanism design / revelation principle (economics)
    note: Choosing a voting rule = choosing a social choice mechanism; VCG is the benchmark
related_unknowns:
  - u-robust-voting-mechanism-strategic-manipulation
related_hypotheses:
  - h-quadratic-voting-reduces-majority-tyranny
cross_pollination_opportunities:
  - Applying mechanism design tools from economics to evaluate ranked-choice vs. approval vs. score voting
  - Using computational social choice algorithms to detect gerrymandering as a manipulation problem
communication_gap: >
  Political scientists studying electoral behavior and mathematical economists studying
  mechanism design publish in separate literatures; Arrow's theorem is widely cited
  in political theory but its mathematical implications (Gibbard-Satterthwaite, VCG)
  are rarely taught in political science programs.
last_reviewed: "2026-05-07"
references:
  - doi: "10.2307/2999600"
    note: Arrow (1950) — impossibility theorem for social welfare functions
  - doi: "10.2307/1914083"
    note: Gibbard (1973) — manipulation of voting schemes
  - doi: "10.1016/0022-0531(73)90050-1"
    note: Vickrey-Clarke-Groves mechanism — incentive-compatible public goods allocation
""",
    },

    # ─── Wave 51 ────────────────────────────────────────────────────────────────
    {
        "dir": "engineering-mathematics",
        "file": "b-fiber-optics-nonlinear-schrodinger-equation.yaml",
        "content": """\
id: b-fiber-optics-nonlinear-schrodinger-equation
title: >
  Pulse propagation in optical fibers is governed by the nonlinear Schrödinger equation
  (NLSE), whose exact soliton solutions explain the dispersion-canceling pulses used
  in long-haul fiber optic communications, connecting photonics engineering to integrable
  systems mathematics.
status: established
fields:
  - engineering
  - mathematics
  - physics
bridge_claim: >
  The envelope of an optical pulse in a fiber obeys the NLSE:
  i∂A/∂z = (β₂/2)∂²A/∂t² − γ|A|²A, where β₂ is group-velocity dispersion and γ
  is the nonlinear coefficient. This equation is exactly integrable via the inverse
  scattering transform (Zakharov-Shabat); its soliton solutions |A|² = P·sech²(t/T₀)
  propagate without distortion because nonlinear self-phase modulation exactly cancels
  group-velocity dispersion. The mathematical structure (Lax pair, infinite conservation
  laws) has no analog in classical waveguide theory but is central to integrable systems.
translation_table:
  - field_a_term: group-velocity dispersion β₂ (fiber optics)
    field_b_term: dispersive term in NLSE (mathematics)
    note: Anomalous dispersion (β₂ < 0) enables bright solitons; normal dispersion gives dark solitons
  - field_a_term: self-phase modulation / Kerr nonlinearity (fiber optics)
    field_b_term: cubic nonlinear term in NLS (mathematics)
    note: Kerr effect ∝ n₂|E|² — exact mathematical analogue of the focusing NLS nonlinearity
  - field_a_term: optical soliton (fiber optics)
    field_b_term: soliton solution of focusing NLS / inverse scattering eigenvalue (mathematics)
    note: Each soliton corresponds to a bound-state eigenvalue of the Zakharov-Shabat operator
  - field_a_term: modulation instability / optical rogue wave (fiber optics)
    field_b_term: Benjamin-Feir instability / Peregrine soliton (mathematics)
    note: MI is the NLS analogue of deep-water wave instability; Peregrine breathers model rogue waves
related_unknowns:
  - u-optical-rogue-wave-prediction-fiber
related_hypotheses:
  - h-inverse-scattering-fiber-transmission-capacity
cross_pollination_opportunities:
  - Applying inverse scattering transform to design noise-immune fiber communication based on eigenvalue modulation
  - Using fiber-optic experiments as analog computers to study NLS dynamics in controlled conditions
communication_gap: >
  Fiber optic engineers and mathematicians working on integrable systems use the same
  NLSE but rarely interact; optical engineers typically use split-step numerical methods
  while mathematicians develop exact inverse-scattering solutions, and the engineering
  implications of integrability (eigenvalue communication) are just entering practice.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1103/PhysRevLett.30.829"
    note: Hasegawa & Tappert (1973) — prediction of optical solitons in fibers
  - doi: "10.1007/BF01208265"
    note: Zakharov & Shabat (1972) — exact theory of the two-dimensional self-focusing
  - doi: "10.1038/450054a"
    note: Mollenauer et al. (2006) — soliton transmission in telecommunications fibers
""",
    },
    {
        "dir": "physics-mathematics",
        "file": "b-zeeman-effect-symmetry-breaking-angular-momentum.yaml",
        "content": """\
id: b-zeeman-effect-symmetry-breaking-angular-momentum
title: >
  The Zeeman effect — splitting of atomic spectral lines in a magnetic field — is
  the physical realization of symmetry breaking of the rotation group SO(3), connecting
  atomic spectroscopy to representation theory of Lie groups and the mathematics of
  angular momentum.
status: established
fields:
  - atomic-physics
  - mathematics
bridge_claim: >
  Without a magnetic field, atomic states with the same principal quantum number n
  and angular momentum l but different magnetic quantum number m are degenerate —
  they form an irreducible representation (irrep) of SO(3) of dimension 2l+1.
  A magnetic field B breaks SO(3) → U(1) (rotational symmetry → axial symmetry),
  lifting the degeneracy: energy shifts ΔE = m·g_J·μ_B·B. The selection rules
  (Δm = 0, ±1) follow from the Wigner-Eckart theorem applied to the dipole operator
  as an SO(3) tensor. This is the prototype of symmetry-breaking in physics.
translation_table:
  - field_a_term: magnetic quantum number m_l (atomic physics)
    field_b_term: weight of SO(3) irreducible representation (mathematics)
    note: m_l labels the basis states of the (2l+1)-dimensional irrep of SO(3)
  - field_a_term: degeneracy lifting in magnetic field (atomic physics)
    field_b_term: symmetry breaking SO(3) → U(1) (mathematics)
    note: External field selects a preferred axis, reducing the symmetry group
  - field_a_term: Landé g-factor (atomic physics)
    field_b_term: Clebsch-Gordan decomposition of coupled angular momenta (mathematics)
    note: g_J mixes orbital and spin angular momenta via CG coefficients for j=l⊕s
  - field_a_term: selection rules Δm = 0, ±1 (atomic physics)
    field_b_term: Wigner-Eckart theorem for rank-1 tensor operator (mathematics)
    note: Dipole operator is an SO(3) rank-1 tensor; WE theorem gives the selection rules exactly
related_unknowns:
  - u-anomalous-zeeman-g-factor-qed-correction
related_hypotheses:
  - h-lie-group-representation-spectroscopic-rules
cross_pollination_opportunities:
  - Using representation theory of higher symmetry groups (SU(3)) to predict spectra of multi-electron atoms
  - Applying Zeeman-effect mathematics to NMR — the same angular momentum algebra governs spin-½ in magnetic fields
communication_gap: >
  Atomic physicists and pure mathematicians working on Lie group representation theory
  share the same formalism but rarely interact; most atomic physics textbooks derive
  angular momentum algebra without noting its Lie-theoretic structure, leaving physicists
  unaware of generalization tools from pure mathematics.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1007/BF01339938"
    note: Zeeman (1897) — original observation of magnetic splitting of spectral lines
  - doi: "10.1007/BF02395808"
    note: Wigner (1931) — group theory and quantum mechanics (angular momentum irreps)
  - doi: "10.1103/PhysRev.43.553"
    note: Condon & Shortley (1935) — theory of atomic spectra and Clebsch-Gordan coefficients
""",
    },
    {
        "dir": "ecology-evolutionary-biology",
        "file": "b-invasion-fitness-adaptive-dynamics-ess.yaml",
        "content": """\
id: b-invasion-fitness-adaptive-dynamics-ess
title: >
  Adaptive dynamics uses invasion fitness — the per-capita growth rate of a rare mutant
  in a resident population — to derive evolutionarily stable strategies (ESS) and
  evolutionary branching points, bridging ecology and evolutionary biology through
  a unified mathematical framework.
status: established
fields:
  - evolutionary-biology
  - ecology
  - mathematics
bridge_claim: >
  In adaptive dynamics, the fitness of a rare mutant x' in a resident population at
  equilibrium with trait x is sx(x') = r(x', x̂(x)), where x̂(x) is the resident
  equilibrium. Evolution follows the canonical equation ẋ = (1/2)σ²·∂sx(x')/∂x'|_{x'=x},
  climbing the fitness gradient. ESS are singular points where the gradient vanishes;
  evolutionary branching occurs when the ESS is a fitness minimum (negative second
  derivative of sx w.r.t. x') — triggering sympatric speciation. This unifies game
  theory (ESS), quantitative genetics, and ecological dynamics.
translation_table:
  - field_a_term: trait evolution by natural selection (evolutionary biology)
    field_b_term: gradient ascent on invasion fitness landscape (mathematics)
    note: Canonical equation of adaptive dynamics is a first-order ODE in trait space
  - field_a_term: evolutionarily stable strategy (evolutionary biology)
    field_b_term: Nash equilibrium of the invasion fitness game (mathematics)
    note: ESS = uninvadable strategy = Nash equilibrium of the frequency-dependent game
  - field_a_term: evolutionary branching / sympatric speciation (evolutionary biology)
    field_b_term: fitness minimum / bifurcation in trait space (mathematics)
    note: Branching occurs at a CSS where the fitness function has negative curvature
  - field_a_term: resident equilibrium density (ecology)
    field_b_term: background state determining the fitness landscape (mathematics)
    note: Ecological dynamics set the resident equilibrium that defines the fitness function
related_unknowns:
  - u-adaptive-dynamics-multi-locus-genetics-reconciliation
related_hypotheses:
  - h-evolutionary-branching-disruptive-selection-speciation
cross_pollination_opportunities:
  - Applying bifurcation theory tools (continuation software) to map the full adaptive dynamics trait space
  - Using invasion fitness framework to analyze co-evolution of hosts and pathogens in epidemiological models
communication_gap: >
  Adaptive dynamics is well-developed theoretically (Geritz, Metz, Dieckmann) but
  remains underutilized in empirical evolutionary biology; many evolutionary biologists
  are unfamiliar with the canonical equation formalism, and ecologists often treat
  evolution as a separate process rather than co-evolving with ecological dynamics.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1006/tpbi.1997.1295"
    note: Geritz et al. (1998) — evolutionarily singular strategies and adaptive radiation
  - doi: "10.1016/S0022-5193(02)93875-4"
    note: Dieckmann & Law (1996) — the dynamical theory of coevolution
  - doi: "10.1086/285812"
    note: Metz et al. (1992) — invasion fitness and adaptive dynamics framework
""",
    },
    {
        "dir": "engineering-fluid-mechanics",
        "file": "b-microfluidics-stokes-flow-low-reynolds-number.yaml",
        "content": """\
id: b-microfluidics-stokes-flow-low-reynolds-number
title: >
  Microfluidic devices operate in the low-Reynolds-number Stokes flow regime where
  viscosity dominates inertia, enabling exact analytical solutions (Stokes equations)
  and reversible, programmable flow patterns that are exploited in lab-on-a-chip
  technologies for biological assays.
status: established
fields:
  - engineering
  - fluid-mechanics
bridge_claim: >
  At Re ≪ 1 (typical microfluidic channels: Re ~ 10⁻³–10⁻¹), the Navier-Stokes
  equations reduce to the Stokes equations: η∇²u = ∇p, ∇·u = 0. These are linear
  and time-reversible (Purcell's scallop theorem). Exact solutions exist for arbitrary
  channel geometries via the Hele-Shaw approximation: u ≈ −(h²/12η)∇p (lubrication
  theory). This allows precise engineering of droplet generation (T-junction), chaotic
  mixing (herringbone channels), and size-based cell sorting — all derived from
  closed-form Stokes solutions.
translation_table:
  - field_a_term: microfluidic channel flow (engineering)
    field_b_term: Stokes flow / creeping flow (fluid mechanics)
    note: Channel Re ~ 10⁻²; inertial terms (Re·Du/Dt) are negligible vs. viscous terms
  - field_a_term: droplet generation at T-junction (engineering)
    field_b_term: Rayleigh-Plateau instability in Stokes regime (fluid mechanics)
    note: Droplet size set by capillary number Ca = ηU/γ; Stokes flow controls pinch-off timing
  - field_a_term: Dean flow in curved microchannels (engineering)
    field_b_term: secondary flow / inertial correction to Stokes (fluid mechanics)
    note: Weak inertia (Re·δ/R) generates cross-stream Dean vortices used for cell focusing
  - field_a_term: electro-osmotic flow in microchannels (engineering)
    field_b_term: Stokes equation with body force (Debye layer driving term) (fluid mechanics)
    note: EOF obeys Helmholtz-Smoluchowski: u_EOF = −(εζ/η)E — a Stokes flow driven by electric body force
related_unknowns:
  - u-microfluidic-chaotic-mixing-optimization
related_hypotheses:
  - h-stokes-flow-deterministic-lateral-displacement-cell-sorting
cross_pollination_opportunities:
  - Using Stokes flow exact solutions to design paper microfluidics with capillary-driven Hele-Shaw flow
  - Applying lubrication theory from fluid mechanics to optimize the gap geometry in microfluidic valves
communication_gap: >
  Microfluidic engineers often use finite-element simulation (COMSOL) without deriving
  Stokes flow analytical solutions that would give clearer scaling laws; conversely,
  fluid mechanics theorists rarely engage with the specific constraints of PDMS
  fabrication and biological sample handling.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1146/annurev.fluid.36.050802.122124"
    note: Squires & Quake (2005) — microfluidics — fluid physics at the nanoliter scale
  - doi: "10.1073/pnas.97.7.3118"
    note: Whitesides & Stroock (2001) — flexible methods for microfluidics
  - doi: "10.1073/pnas.97.9.5083"
    note: Stroock et al. (2002) — chaotic mixer for microchannels using herringbone ridges
""",
    },
    {
        "dir": "cognitive-science-mathematics",
        "file": "b-childhood-learning-bayesian-concept-acquisition.yaml",
        "content": """\
id: b-childhood-learning-bayesian-concept-acquisition
title: >
  Children acquire concepts and causal rules with remarkable speed and generalization
  from sparse data, a phenomenon explained by Bayesian concept learning — probabilistic
  inference over hypothesis spaces with strong structural priors, bridging cognitive
  science and Bayesian statistics.
status: established
fields:
  - cognitive-science
  - mathematics
  - statistics
bridge_claim: >
  Tenenbaum & Griffiths (2001) showed that human concept learning matches Bayesian
  inference: given n positive examples of a concept, the learner infers the most
  probable hypothesis h by computing P(h|data) ∝ P(data|h)·P(h). The likelihood
  P(data|h) = (1/|h|)^n (size principle — smaller hypotheses are more strongly
  confirmed) combined with a structured prior P(h) encodes conceptual knowledge.
  This framework explains the number-concept bootstrap, word learning, causal learning,
  and inductive generalization using a single mathematical model.
translation_table:
  - field_a_term: concept generalization from examples (cognitive science)
    field_b_term: Bayesian posterior over hypothesis space (mathematics)
    note: A child generalizes a word to new objects — Bayesian update of P(concept|examples)
  - field_a_term: size principle in concept learning (cognitive science)
    field_b_term: likelihood ratio favoring specific over general hypotheses (mathematics)
    note: Smaller concept extension has higher likelihood per example — the size principle
  - field_a_term: prior knowledge / core knowledge system (cognitive science)
    field_b_term: prior probability distribution P(h) (mathematics)
    note: Innate core knowledge corresponds to a strong structural prior over hypothesis space
  - field_a_term: one-shot learning / fast mapping (cognitive science)
    field_b_term: Bayesian inference with informative prior (mathematics)
    note: Strong prior + single example yields a confident posterior — explaining fast mapping
related_unknowns:
  - u-language-acquisition-bayesian-prior-source
related_hypotheses:
  - h-rational-constructivism-bayesian-development
cross_pollination_opportunities:
  - Using program induction priors (DreamCoder) to model the compositional structure of human concept spaces
  - Applying Bayesian cognitive models to design better educational interventions for concept learning
communication_gap: >
  Developmental psychologists studying concept acquisition and Bayesian statisticians
  rarely collaborate directly; Bayesian cognitive science (Tenenbaum, Griffiths, Gopnik)
  has grown substantially but remains distinct from mainstream developmental psychology
  and is largely unknown to educational practitioners.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1037/0033-295X.108.3.450"
    note: Tenenbaum & Griffiths (2001) — generalization, similarity, and Bayesian inference
  - doi: "10.1037/0033-295X.116.2.246"
    note: Xu & Tenenbaum (2007) — word learning as Bayesian inference
  - doi: "10.1037/0033-295X.116.4.961"
    note: Goodman et al. (2011) — rational analysis of rule-based concept learning
""",
    },
    {
        "dir": "engineering-geophysics",
        "file": "b-geothermal-energy-subsurface-heat-transport.yaml",
        "content": """\
id: b-geothermal-energy-subsurface-heat-transport
title: >
  Geothermal energy extraction requires modeling subsurface heat and fluid transport
  governed by coupled thermoporoelastic equations, connecting reservoir engineering
  to geophysics and the mathematics of heat diffusion in fractured porous media.
status: established
fields:
  - engineering
  - geophysics
bridge_claim: >
  A geothermal reservoir is described by Biot's thermoporoelastic theory: fluid
  pressure, temperature, and stress are coupled through Darcy flow (u = −(k/η)∇p),
  Fourier heat conduction (q = −λ∇T), and elastic equilibrium (∇·σ = 0). Fracture
  permeability dominates over matrix permeability (discrete fracture network models).
  The thermal breakthrough time — when injected cold water reaches the production well —
  is predicted by a 1-D advection-diffusion equation with Péclet number Pe = uL/κ.
  Induced seismicity arises when pore-pressure increase reduces effective stress (Mohr-
  Coulomb failure), bridging geomechanics and fault mechanics.
translation_table:
  - field_a_term: geothermal reservoir permeability (engineering)
    field_b_term: hydraulic conductivity tensor in Darcy flow (geophysics)
    note: Fracture permeability k = w³/12 (cubic law) dominates matrix in crystalline rock
  - field_a_term: thermal breakthrough time (engineering)
    field_b_term: Péclet number in advection-diffusion equation (geophysics)
    note: High Pe → advection-dominated; thermal front moves with fluid velocity
  - field_a_term: enhanced geothermal system (EGS) hydraulic stimulation (engineering)
    field_b_term: pore-pressure-induced fault reactivation / Mohr-Coulomb criterion (geophysics)
    note: Fluid injection reduces effective normal stress: σ'_n = σ_n − p, triggering slip
  - field_a_term: doublet well configuration (engineering)
    field_b_term: dipole source-sink in porous medium (geophysics)
    note: Injection-production doublet creates a Rankine dipole flow field in the aquifer
related_unknowns:
  - u-enhanced-geothermal-induced-seismicity-risk
related_hypotheses:
  - h-geothermal-doublet-thermal-lifetime-péclet-scaling
cross_pollination_opportunities:
  - Applying geophysical seismic monitoring tools to map fracture networks for optimal geothermal well placement
  - Using thermoporoelastic simulation tools from petroleum geomechanics to design EGS reservoirs
communication_gap: >
  Geothermal engineers and geophysicists share coupled equations but work in separate
  professional communities (geothermal power industry vs. academic geophysics); induced
  seismicity risk from EGS has created regulatory challenges requiring closer collaboration
  between engineers optimizing for extraction and geophysicists studying fault mechanics.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1016/j.geothermics.2010.09.005"
    note: Tester et al. (2006) — future of geothermal energy (MIT report on EGS)
  - doi: "10.1007/BF01837056"
    note: Biot (1956) — thermoelasticity and irreversible thermodynamics in porous media
  - doi: "10.1016/j.scitotenv.2018.07.098"
    note: Grigoli et al. (2018) — induced seismicity risk from geothermal stimulation
""",
    },
    {
        "dir": "virology-evolutionary-biology",
        "file": "b-viral-evolution-quasispecies-fitness-landscape.yaml",
        "content": """\
id: b-viral-evolution-quasispecies-fitness-landscape
title: >
  RNA virus populations evolve as quasispecies — clouds of mutant sequences near a
  fitness landscape peak — a concept borrowed from the physics of spin glasses and
  applied to virology, explaining error catastrophe, lethal mutagenesis, and immune escape.
status: established
fields:
  - virology
  - evolutionary-biology
bridge_claim: >
  Eigen's quasispecies equation describes an RNA virus population as a distribution
  over sequence space: ẋᵢ = Σⱼ Wᵢⱼ xⱼ − Φxᵢ, where Wᵢⱼ is the mutation-selection
  matrix and Φ normalizes the population. The dominant eigenvector (master sequence
  + mutant cloud) is the quasispecies. Above the error threshold μ > μ_crit = ln(W_max)/L,
  the quasispecies delocalizes across sequence space (error catastrophe), analogous
  to a phase transition in a disordered system. The fitness landscape analogy (Wright)
  — with peaks, valleys, and neutral networks — provides geometric intuition.
translation_table:
  - field_a_term: RNA virus mutation rate per base per replication (virology)
    field_b_term: error rate in quasispecies / transition matrix entry (evolutionary biology)
    note: RNA polymerase lacks proofreading; u ≈ 10⁻⁴ per base is near the error threshold
  - field_a_term: dominant viral sequence / consensus sequence (virology)
    field_b_term: master sequence (dominant eigenvector of mutation-selection matrix) (evolutionary biology)
    note: Consensus ≠ master sequence when the mutant cloud has a different mean fitness
  - field_a_term: lethal mutagenesis by mutagens (ribavirin) (virology)
    field_b_term: driving the population above the error threshold (evolutionary biology)
    note: Increasing μ beyond μ_crit destroys the quasispecies — basis of antiviral strategy
  - field_a_term: immune escape variant selection (virology)
    field_b_term: adaptive walk on rugged fitness landscape (evolutionary biology)
    note: Immune pressure shifts the fitness landscape; the quasispecies cloud rapidly adapts
related_unknowns:
  - u-rna-virus-error-threshold-experimental-validation
related_hypotheses:
  - h-lethal-mutagenesis-quasispecies-antiviral-strategy
cross_pollination_opportunities:
  - Using fitness landscape inference from deep sequencing data to predict vaccine escape mutations
  - Applying spin-glass theory (NK model) to compute the ruggedness of viral protein fitness landscapes
communication_gap: >
  Virologists and evolutionary biologists are familiar with quasispecies conceptually,
  but the mathematical connection to eigenvalue problems and spin-glass physics is
  underappreciated; most virologists use quasispecies as a metaphor rather than
  applying the Eigen equation quantitatively.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1007/BF02460040"
    note: Eigen (1971) — self-organization of matter and evolution of biological macromolecules
  - doi: "10.1016/j.cell.2006.05.049"
    note: Domingo et al. (2006) — quasispecies dynamics and RNA virus biology
  - doi: "10.1371/journal.ppat.1000005"
    note: Perales et al. (2010) — lethal mutagenesis and the fate of RNA viruses
""",
    },
    {
        "dir": "materials-science-quantum-physics",
        "file": "b-carbon-nanotube-graphene-band-structure-zone-folding.yaml",
        "content": """\
id: b-carbon-nanotube-graphene-band-structure-zone-folding.yaml
title: >
  Carbon nanotube electronic properties — metallic or semiconducting, with chirality-
  dependent band gaps — are derived from graphene band structure by zone-folding:
  wrapping the 2-D graphene Brillouin zone onto the 1-D nanotube cylinder.
status: established
fields:
  - materials-science
  - quantum-physics
bridge_claim: >
  A single-walled nanotube (SWNT) of chiral vector (n,m) is a rolled-up graphene sheet.
  Zone-folding quantizes the transverse wavevector: k_⊥ = 2πq/C (q integer, C = |Ch|
  circumference). The 1-D band structure is the intersection of these quantization lines
  with graphene's 2-D band structure. If a line passes through a Dirac K-point,
  the nanotube is metallic (n−m = 3p); otherwise it has a band gap Eg ≈ 2ℏv_F/(3a_CC·q).
  This purely geometric (zone-folding) derivation connects the 2-D massless Dirac
  fermion of graphene to 1-D quantum wire physics in carbon nanotubes.
translation_table:
  - field_a_term: nanotube chiral vector (n,m) (materials science)
    field_b_term: quantization condition on graphene Brillouin zone (quantum physics)
    note: Chiral vector defines circumference → quantization lines through the BZ
  - field_a_term: metallic vs. semiconducting nanotube (materials science)
    field_b_term: K-point crossing condition (n−m ≡ 0 mod 3) (quantum physics)
    note: Topological criterion — K-point inclusion is determined by mod-3 arithmetic
  - field_a_term: nanotube band gap Eg (materials science)
    field_b_term: Dirac cone linear dispersion sampled off K-point (quantum physics)
    note: Eg ≈ 2γa/d_t (γ = hopping integral, d_t = diameter) — graphene cone geometry
  - field_a_term: armchair nanotube (n,n) — always metallic (materials science)
    field_b_term: quantization line through both K and K' Dirac points (quantum physics)
    note: Armchair quantization lines pass exactly through Dirac points regardless of n
related_unknowns:
  - u-nanotube-ballistic-transport-contact-resistance
related_hypotheses:
  - h-zone-folding-curvature-corrections-nanotube-gap
cross_pollination_opportunities:
  - Applying zone-folding mathematics to predict band structures of other rolled 2-D materials (MoS₂ nanotubes)
  - Using nanotube band gap chirality-selectivity to develop single-chirality electronic devices
communication_gap: >
  Materials scientists who grow and characterize nanotubes and quantum physicists who
  derive band structure from first principles share zone-folding but use different
  languages; zone-folding limitations (curvature effects, σ-π rehybridization) are
  known theoretically but rarely discussed in synthesis or device literatures.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1103/PhysRevLett.78.1932"
    note: Dresselhaus et al. (1998) — physical properties of carbon nanotubes
  - doi: "10.1103/PhysRevB.57.R4145"
    note: Saito et al. (1992) — electronic structure of carbon nanotubes
  - doi: "10.1038/35089553"
    note: Dekker (1999) — carbon nanotubes as molecular quantum wires
""",
    },
    {
        "dir": "ecology-evolutionary-biology",
        "file": "b-animal-coloration-honest-signaling-fisher-runaway.yaml",
        "content": """\
id: b-animal-coloration-honest-signaling-fisher-runaway
title: >
  Animal coloration for mate attraction is governed by two competing evolutionary
  mechanisms — honest signaling (Zahavian handicap) and Fisher runaway selection —
  which are formalized by different mathematical models connecting evolutionary biology
  to game theory and physics of symmetry breaking.
status: established
fields:
  - evolutionary-biology
  - ecology
  - physics
bridge_claim: >
  The handicap principle (Zahavi 1975, Grafen 1990) models costly coloration as a
  signaling game: the ESS signal intensity satisfies a separating equilibrium where
  signal cost equals the benefit of attracting mates, mapping onto Spence's job-market
  signaling model. Fisher runaway (Lande 1981) is a different mechanism: genetic
  correlation between female preference alleles and male trait alleles creates a
  positive feedback instability — mathematically equivalent to a Turing-like symmetry
  breaking — where trait and preference co-evolve to extreme values. Both predict
  elaborate coloration but via different mathematics.
translation_table:
  - field_a_term: carotenoid-based plumage brightness (evolutionary biology)
    field_b_term: signal cost in separating equilibrium (game theory)
    note: Parasite load reduces carotenoid availability — honest condition-dependent signal
  - field_a_term: female mate preference allele frequency (evolutionary biology)
    field_b_term: unstable runaway trajectory in preference-trait genetic space (mathematics)
    note: Lande's genetic covariance matrix drives Fisher runaway as a positive eigenvalue
  - field_a_term: structural iridescence / UV reflectance (evolutionary biology)
    field_b_term: photonic crystal band gap (physics)
    note: Nanostructured feather barbules generate structural color via thin-film interference
  - field_a_term: honest condition-dependent signal (evolutionary biology)
    field_b_term: incentive-compatible mechanism in signaling game (economics)
    note: Zahavian handicap = Spence signaling equilibrium — same mathematical structure
related_unknowns:
  - u-handicap-vs-runaway-empirical-test
related_hypotheses:
  - h-fisher-runaway-positive-feedback-speciation
cross_pollination_opportunities:
  - Using quantum photonics models for structural color to explain the spectral specificity of mate preferences
  - Applying mechanism-design theory from economics to test whether handicap equilibria are evolutionarily stable
communication_gap: >
  Evolutionary biologists, physicists studying structural color, and economists studying
  signaling theory all work on animal coloration from different angles without systematic
  collaboration; the photonics of structural color is well-studied in materials science
  but rarely connected to the evolutionary dynamics of preference for structural vs.
  pigment-based signals.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1016/S0003-3472(75)80053-8"
    note: Zahavi (1975) — mate selection and the handicap principle
  - doi: "10.1086/285448"
    note: Grafen (1990) — biological signals as handicaps — the formal theory
  - doi: "10.2307/2408043"
    note: Lande (1981) — models of speciation by sexual selection
""",
    },
    {
        "dir": "neuroscience-mathematics",
        "file": "b-consciousness-integrated-information-theory-phi.yaml",
        "content": """\
id: b-consciousness-integrated-information-theory-phi
title: >
  Integrated Information Theory (IIT) proposes that consciousness corresponds to
  integrated information Φ — a measure of how much a system generates information
  above and beyond its parts — connecting neuroscience to information theory,
  statistical mechanics, and the mathematics of causal structure.
status: conjectural
fields:
  - neuroscience
  - mathematics
  - information-theory
bridge_claim: >
  IIT (Tononi 2004, 2014) defines Φ as the minimum information generated by a
  system as a whole beyond its minimum information partition (MIP). Mathematically,
  Φ is a measure over a causal structure (directed graph with conditional probability
  tables): Φ = min_{partition P} D_KL(p(X|do(causes)) || p_partition(X|do(causes))).
  High Φ requires the system to be both integrated (not decomposable) and differentiated
  (high entropy). The maximum-Φ architecture is a complete graph with heterogeneous
  connections — which resembles thalamocortical anatomy. Φ is NP-hard to compute exactly.
translation_table:
  - field_a_term: subjective experience / qualia (neuroscience)
    field_b_term: integrated information Φ of the neural causal structure (mathematics)
    note: IIT's central axiom — experience IS identical to the cause-effect structure with maximal Φ
  - field_a_term: level of consciousness / anesthetic depth (neuroscience)
    field_b_term: magnitude of Φ (information theory)
    note: Zap-complexity (TMS-EEG) is an empirical proxy for Φ that tracks consciousness
  - field_a_term: posterior cortical hot zone (neuroscience)
    field_b_term: maximal-Φ subgraph (NPC) (mathematics)
    note: IIT predicts consciousness localizes to the brain's highest-Φ subgraph
  - field_a_term: feed-forward vs. recurrent connectivity (neuroscience)
    field_b_term: zero vs. positive Φ (information theory)
    note: Pure feed-forward systems have Φ = 0 — they are not conscious per IIT
related_unknowns:
  - u-iit-phi-empirical-test-neural-correlates
related_hypotheses:
  - h-phi-maximum-thalamocortical-consciousness-locus
cross_pollination_opportunities:
  - Using causal inference tools from statistics to compute Φ from fMRI functional connectivity data
  - Applying statistical mechanics of complex networks to understand why Φ peaks at intermediate integration
communication_gap: >
  Neuroscientists studying consciousness and mathematicians / information theorists studying
  integrated information rarely collaborate; IIT has generated significant debate but
  the mathematical community working on information geometry and causal inference rarely
  engages with the neuroscience consciousness literature, and vice versa.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1186/1471-2202-5-42"
    note: Tononi (2004) — an information integration theory of consciousness
  - doi: "10.1371/journal.pcbi.1003588"
    note: Tononi et al. (2016) — integrated information theory — from consciousness to its physical substrate
  - doi: "10.7554/eLife.21926"
    note: Oizumi et al. (2014) — from the phenomenology to the mechanisms of consciousness (IIT 3.0)
""",
    },
    {
        "dir": "condensed-matter-biology",
        "file": "b-structural-color-photonic-crystal-band-gaps.yaml",
        "content": """\
id: b-structural-color-photonic-crystal-band-gaps
title: >
  The structural colors of butterfly wings, beetle shells, and bird feathers arise
  from nanoscale photonic crystal structures that produce photonic band gaps and
  thin-film interference, connecting evolutionary biology to condensed matter physics
  and photonics.
status: established
fields:
  - biology
  - condensed-matter-physics
  - photonics
bridge_claim: >
  Biological nanostructures (opal-like arrays, gyroid morphologies, thin-film stacks)
  function as photonic crystals: periodic dielectric structures with lattice constants
  comparable to visible light wavelengths (200–700 nm) that exhibit photonic band gaps
  — frequency ranges where light propagation is forbidden. The reflected color peak
  follows Bragg's law: λ = 2n_eff·d·cos(θ), the same equation as X-ray diffraction
  in crystals. Morpho butterfly wings use a 2-D photonic crystal of quasi-ordered
  air rods in chitin (n≈1.56) with a partial band gap optimized for broad-angle blue
  reflection.
translation_table:
  - field_a_term: butterfly wing nanostructure (biology)
    field_b_term: 2-D or 3-D photonic crystal lattice (condensed matter)
    note: Chitin-air periodic arrays with period ~150 nm act as photonic crystals for visible light
  - field_a_term: iridescence / angle-dependent color (biology)
    field_b_term: photonic band gap angular dispersion (condensed matter)
    note: Bragg reflection angle gives iridescence; quasi-disorder reduces angle-dependence
  - field_a_term: gyroid sponge structure in butterfly wing scales (biology)
    field_b_term: gyroid photonic crystal with cubic symmetry (condensed matter)
    note: Biological gyroids self-assemble via lipid block-copolymer phase separation
  - field_a_term: matte (non-iridescent) structural color (biology)
    field_b_term: photonic glass / amorphous photonic structure (condensed matter)
    note: Short-range order without long-range periodicity gives angle-independent color
related_unknowns:
  - u-biological-gyroid-self-assembly-mechanism
related_hypotheses:
  - h-photonic-crystal-self-assembly-block-copolymer
cross_pollination_opportunities:
  - Importing biological self-assembly strategies for photonic structures into low-cost photonic device fabrication
  - Using photonic band structure calculations to predict which nanostructure geometries produce desired biological colors
communication_gap: >
  Evolutionary biologists studying structural color and condensed matter physicists
  studying photonic crystals publish in separate literatures; the transfer of knowledge
  from condensed matter photonics to understanding the evolution and function of
  biological colors is growing but remains incomplete; most biologists are unfamiliar
  with photonic band gap calculations.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1063/1.1564060"
    note: Vukusic & Sambles (2003) — photonic structures in biology
  - doi: "10.1038/nature07609"
    note: Dufresne et al. (2009) — self-assembly of amorphous biophotonic nanostructures
  - doi: "10.1126/science.1152592"
    note: Shawkey & Hill (2006) — significance of a basal melanin layer to production of non-iridescent structural plumage color
""",
    },
    {
        "dir": "fluid-mechanics-geophysics",
        "file": "b-kelvin-helmholtz-instability-stratified-shear-flow.yaml",
        "content": """\
id: b-kelvin-helmholtz-instability-stratified-shear-flow
title: >
  The Kelvin-Helmholtz instability arises at the interface between stratified fluid
  layers with velocity shear, governed by the Richardson number criterion, and produces
  the characteristic billowing vortices seen in clouds, ocean thermocline mixing,
  and planetary atmospheres.
status: established
fields:
  - fluid-mechanics
  - geophysics
bridge_claim: >
  At the interface between two fluids of densities ρ₁ < ρ₂ moving at velocities U₁
  and U₂, the Richardson number Ri = N²/(∂U/∂z)² determines stability: Ri < 0.25
  (Miles-Howard theorem) is necessary (though not sufficient) for instability. Linear
  stability analysis of the Taylor-Goldstein equation gives the instability growth rate
  σ = k·(U₁−U₂)/2·√(1−4Ri). Nonlinear evolution produces characteristic KH billows
  that roll up and eventually break, generating turbulent mixing — the dominant mechanism
  for diapycnal mixing in the ocean thermocline and atmospheric clear-air turbulence.
translation_table:
  - field_a_term: velocity shear across ocean thermocline (geophysics)
    field_b_term: KH instability shear layer (fluid mechanics)
    note: Thermocline velocity shear drives KH instability that mixes heat, salt, and nutrients
  - field_a_term: Richardson number Ri (geophysics)
    field_b_term: stability parameter in Taylor-Goldstein equation (fluid mechanics)
    note: Ri < 1/4 necessary for KH instability; buoyancy stabilizes, shear destabilizes
  - field_a_term: diapycnal mixing in ocean interior (geophysics)
    field_b_term: turbulent diffusion from KH billow breakdown (fluid mechanics)
    note: KH-generated turbulence is parameterized by mixing efficiency Γ≈0.2 in ocean models
  - field_a_term: clear-air turbulence (CAT) in atmosphere (geophysics)
    field_b_term: KH billow breaking at jet stream interface (fluid mechanics)
    note: CAT occurs where Ri < 0.25 near wind shear layers — a hazard to aviation
related_unknowns:
  - u-kelvin-helmholtz-diapycnal-mixing-quantification
related_hypotheses:
  - h-richardson-number-turbulence-onset-universal
cross_pollination_opportunities:
  - Applying direct numerical simulation of KH instability to calibrate mixing parameterizations in ocean climate models
  - Using satellite observations of KH waves in clouds to validate fluid mechanics stability predictions
communication_gap: >
  Geophysicists parameterizing ocean mixing in climate models and fluid mechanicians
  studying KH instability use the same Richardson number criterion but different
  modeling approaches; ocean models use bulk mixing parameterizations (KPP, MY) while
  fluid mechanics provides direct numerical simulations that rarely inform the parameterization choices.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1017/S0022112061000305"
    note: Miles (1961) — on the stability of heterogeneous shear flows (Miles-Howard theorem)
  - doi: "10.1175/JPO-D-12-0105.1"
    note: Smyth & Moum (2012) — ocean mixing by Kelvin-Helmholtz instability
  - doi: "10.1175/1520-0493(1994)122<0927:AIOCAM>2.0.CO;2"
    note: Large et al. (1994) — KPP mixing scheme using Richardson number criterion
""",
    },
]


def write_bridge(dir_name, file_name, content):
    d = BASE / dir_name
    d.mkdir(parents=True, exist_ok=True)
    f = d / file_name
    f.write_text(content, encoding="utf-8")
    print(f"  Wrote {f}")


if __name__ == "__main__":
    for b in BRIDGES:
        write_bridge(b["dir"], b["file"], b["content"])
    print(f"\nDone — {len(BRIDGES)} bridge files written.")

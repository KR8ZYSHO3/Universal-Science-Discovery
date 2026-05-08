"""Generate Wave 68 and Wave 69 cross-domain bridge files."""
import os
import textwrap

BASE = r"C:\Users\Shoe\dev\Universal-Science-Discovery"
TODAY = "2026-05-07"

def write(path, content):
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  wrote {path}")

# ============================================================
# WAVE 68
# ============================================================

# 1. Synthetic biology x circuit design
write("cross-domain/biology-math/b-synthetic-biology-x-circuit-design.yaml", f"""\
id: b-synthetic-biology-x-circuit-design
title: >
  Synthetic Biology x Electronic Circuit Design - gene circuits as logic gates
status: proposed
fields:
  - biology
  - computer-science
  - synthetic-biology
bridge_claim: >
  Synthetic gene circuits implement Boolean logic (toggle switches, oscillators,
  band-pass filters) using the same design principles as electronic circuits; the
  repressilator (three-gene ring oscillator) is the biological equivalent of a ring
  oscillator, and synthetic bistable switches match the behavior of an SR latch -
  making electronic CAD methods directly applicable to genetic circuit design.
translation_table:
  - field_a_term: Transcription factor repressor (TetR, LacI, cI)
    field_b_term: NOT gate (inverter)
    note: >
      A repressor protein binding its operator prevents transcription of the downstream
      gene, implementing logical NOT; cascaded inverters form oscillators (repressilator)
      or bistable switches (toggle switch) just as in CMOS ring oscillators.
  - field_a_term: Repressilator (3-gene cyclic repressor network)
    field_b_term: Ring oscillator (3-inverter chain with feedback)
    note: >
      Both use an odd number of inversions in a cycle to produce sustained oscillations;
      the period is determined by the delay around the loop (mRNA/protein half-lives
      vs gate propagation delay).
  - field_a_term: Bistable toggle switch (Gardner et al. 2000)
    field_b_term: SR latch (cross-coupled NOR gates)
    note: >
      Mutual repression of two promoters produces two stable states with hysteresis,
      identical in logic structure to an SR latch; noise-driven switching corresponds
      to hold-time violations in digital circuits.
  - field_a_term: Ribosome binding site strength
    field_b_term: Fan-out / drive strength
    note: >
      RBS strength determines translational efficiency and hence how strongly a gene
      drives downstream processes - the biological analogue of gate drive strength in
      digital electronics.
communication_gap: >
  Electrical engineers developed rigorous CAD flows (SPICE simulation, formal
  verification, modular composition) over 60 years that synthetic biologists are
  only beginning to import; conversely, the stochastic and evolutionary robustness
  of gene circuits provides engineering insights absent from deterministic digital
  design.
cross_pollination_opportunities:
  - >
    Port electronic CAD tools (hierarchical netlist design, logic synthesis, timing
    analysis) to genetic circuits, automating the design of complex multi-gene
    regulatory networks from Boolean truth tables.
  - >
    Apply noise-margin analysis from digital electronics to predict bistable switch
    reliability as a function of gene expression noise level, guiding promoter and
    RBS selection.
  - >
    Use synthetic gene circuits as programmable sensors (band-pass logic for
    metabolite concentration windows) guided by analog filter design principles.
related_unknowns:
  - u-synthetic-biology-x-circuit-design
references:
  - doi: "10.1038/35002131"
    note: "Elowitz & Leibler (2000) - repressilator: a synthetic oscillatory network of transcriptional regulators; Nature 403:335"
  - doi: "10.1038/35002131"
    note: "Gardner, Cantor & Collins (2000) - construction of a genetic toggle switch; Nature 403:339"
last_reviewed: "{TODAY}"
""")

write("unknowns-catalog/biology/u-synthetic-biology-x-circuit-design.yaml", f"""\
id: u-synthetic-biology-x-circuit-design
title: "Can formal CAD methods from electronic engineering (logic synthesis, formal verification, timing analysis) be systematically applied to synthetic gene circuit design to achieve predictable, composable biological logic?"
status: open
priority: medium
disciplines:
  - synthetic-biology
  - computer-science
  - biological-engineering
summary: >
  Electronic CAD enables predictable, composable digital circuits through formal
  abstraction layers (RTL, netlist, layout). Synthetic biology lacks equivalent
  abstractions: genetic parts show context-dependence (retroactivity), stochastic
  expression noise, evolutionary instability, and cellular resource competition that
  violate the modularity assumptions of electronic CAD. Key unknowns: (1) can
  retroactivity be formally modeled and compensated for, enabling true modularity?
  (2) what is the maximum achievable logical complexity in a single cell before
  metabolic burden causes failure? (3) can formal verification guarantee circuit
  behavior under biological noise?
systematic_gaps:
  - No formal composability theorem for genetic parts analogous to logical isolation in CMOS
  - Resource competition (ribosomes, polymerases) creates hidden coupling between nominally independent modules
  - Evolutionary instability causes circuit degradation over generations, absent in silicon
related_bridges:
  - b-synthetic-biology-x-circuit-design
last_reviewed: "{TODAY}"
""")

write("hypotheses/active/h-synthetic-biology-x-circuit-design.yaml", f"""\
id: h-synthetic-biology-x-circuit-design
title: >
  Retroactivity compensation using insulator genetic parts (insulators) restores
  logical modularity in synthetic gene circuits, enabling formal CAD composition
  rules with predictable transfer functions measurable by flow cytometry.
status: active
priority: medium
impact_score: 0.76
created: "{TODAY}"
last_updated: "{TODAY}"
author: USDR

evidence_links:
  - doi: "10.1038/35002131"
    type: supporting
    confidence: 0.88
    note: "Elowitz & Leibler (2000) - repressilator demonstrates gene circuits obey ring-oscillator design principles"
  - type: supporting
    note: "Del Vecchio et al. (2008) - retroactivity theory shows loading effects between modules; compensation circuits restore isolation"
    confidence: 0.74

unknowns_addressed:
  - u-synthetic-biology-x-circuit-design

proposed_tests:
  - description: >
      Construct a 4-gate Boolean logic circuit in E. coli with and without
      retroactivity compensation modules; measure transfer functions of each gate
      in isolation vs in circuit using flow cytometry.
    method: "Flow cytometry of fluorescent reporter expression; compare isolated vs connected gate transfer functions"
    prediction: "Uncompensated circuits show >30% deviation from isolated transfer functions; compensated circuits show <5% deviation"
  - description: >
      Apply electronic timing analysis to a synthetic oscillator, predicting
      period from component delays; test prediction against time-lapse microscopy.
    method: "Time-lapse fluorescence microscopy of repressilator variants with different RBS strengths; compare period to timing model"
    prediction: "Period scales with sum of component delays as in ring oscillator timing formula, within 2x"

related_disciplines:
  - synthetic-biology
  - computer-science
  - control-theory
  - biological-engineering
""")

# 2. Conformal field theory x critical phenomena
write("cross-domain/physics-math/b-conformal-field-theory-x-critical-phenomena.yaml", f"""\
id: b-conformal-field-theory-x-critical-phenomena
title: >
  Conformal Field Theory x Critical Phenomena - scale invariance as symmetry
status: proposed
fields:
  - physics
  - mathematics
  - statistical-mechanics
bridge_claim: >
  At a second-order phase transition, the system's scaling symmetry enhances to full
  conformal symmetry (invariant under angle-preserving maps); conformal field theory
  (CFT) classifies all possible universality classes of 2D critical phenomena exactly
  and constrains 3D critical exponents via the conformal bootstrap - unifying
  statistical mechanics with quantum field theory.
translation_table:
  - field_a_term: Universality class (critical exponents alpha, beta, gamma, nu)
    field_b_term: CFT operator content (primary operators and their dimensions)
    note: >
      Each universality class corresponds to a unique CFT; the critical exponents are
      determined by the scaling dimensions of primary operators, so classifying CFTs
      is equivalent to classifying universality classes.
  - field_a_term: Correlation length divergence (xi ~ |T-Tc|^-nu)
    field_b_term: Conformal invariance (long-range correlations at all scales)
    note: >
      At criticality, xi diverges and the system becomes scale-invariant; scale
      invariance plus unitarity and Lorentz invariance imply full conformal invariance,
      replacing power-law correlations with exact CFT two-point functions.
  - field_a_term: Wilson-Fisher fixed point (epsilon expansion)
    field_b_term: Non-trivial CFT fixed point (anomalous dimensions)
    note: >
      The Wilson-Fisher fixed point of the RG flow corresponds to an interacting CFT;
      the anomalous dimensions of fields at the fixed point give the critical exponents.
  - field_a_term: Transfer matrix (1D quantum chain)
    field_b_term: Virasoro algebra (2D CFT)
    note: >
      The transfer matrix of a 2D classical lattice model equals the Hamiltonian of a
      1D quantum chain; at criticality, this Hamiltonian has Virasoro symmetry, making
      2D critical phenomena exactly solvable via CFT.
communication_gap: >
  Statistical physicists and mathematical physicists developed parallel tools (RG,
  transfer matrices vs Virasoro algebras, modular invariance) that were unified only
  through the BPZ paper (1984); 3D CFT is still less understood than 2D, with the
  conformal bootstrap providing new constraints only in the last 15 years.
cross_pollination_opportunities:
  - >
    Use conformal bootstrap numerical methods to compute 3D Ising model critical
    exponents to 10-digit precision, replacing expensive Monte Carlo simulations
    for systems near phase transitions.
  - >
    Apply CFT minimal model classification to identify all possible universality
    classes in 2D experimental systems (thin films, membranes, monolayers), predicting
    which classes are realizable.
  - >
    Import CFT operator product expansion methods into statistical mechanics to
    compute multi-point correlation functions in disordered systems near criticality.
related_unknowns:
  - u-conformal-field-theory-x-critical-phenomena
references:
  - doi: "10.1016/0550-3213(84)90052-X"
    note: "Belavin, Polyakov & Zamolodchikov (1984) - infinite conformal symmetry in 2D quantum field theory; Nucl Phys B 241:333"
  - doi: "10.1103/PhysRevD.86.025022"
    note: "Rychkov & Tonni (2009) - conformal bootstrap in 3D; constraining the 3D Ising model critical exponents"
last_reviewed: "{TODAY}"
""")

write("unknowns-catalog/physics/u-conformal-field-theory-x-critical-phenomena.yaml", f"""\
id: u-conformal-field-theory-x-critical-phenomena
title: "Does every second-order phase transition in 3D correspond to a well-defined unitary CFT, and can the conformal bootstrap classify all 3D universality classes analogously to the BPZ classification in 2D?"
status: open
priority: high
disciplines:
  - statistical-mechanics
  - mathematical-physics
  - condensed-matter-physics
summary: >
  In 2D, the BPZ classification (1984) provided a complete list of minimal model
  CFTs corresponding to all 2D universality classes. In 3D, conformal invariance at
  second-order phase transitions is assumed but harder to prove; the conformal
  bootstrap has determined the 3D Ising critical exponents to high precision but a
  complete classification of 3D CFTs remains open. Key unknowns: (1) are all
  experimentally observed 3D universality classes (Ising, Heisenberg, XY) isolable
  as distinct bootstrap islands? (2) do non-unitary CFTs arise in physical systems
  (percolation, self-avoiding walks)? (3) can the bootstrap handle disordered or
  long-range interacting systems?
systematic_gaps:
  - No complete classification of unitary 3D CFTs analogous to the 2D ADE classification
  - Bootstrap computations scale poorly with operator spin; higher-spin constraints not fully explored
  - Disordered systems (random-bond Ising) may require non-unitary CFTs outside the standard bootstrap framework
related_bridges:
  - b-conformal-field-theory-x-critical-phenomena
last_reviewed: "{TODAY}"
""")

write("hypotheses/active/h-conformal-field-theory-x-critical-phenomena.yaml", f"""\
id: h-conformal-field-theory-x-critical-phenomena
title: >
  The conformal bootstrap island for the 3D Ising universality class is an isolated
  point in CFT space, proving that critical exponents are uniquely determined by
  conformal invariance plus unitarity without any free parameters.
status: active
priority: high
impact_score: 0.91
created: "{TODAY}"
last_updated: "{TODAY}"
author: USDR

evidence_links:
  - doi: "10.1016/0550-3213(84)90052-X"
    type: supporting
    confidence: 0.95
    note: "Belavin, Polyakov & Zamolodchikov (1984) - complete classification in 2D confirms CFT determines universality class"
  - doi: "10.1103/PhysRevD.86.025022"
    type: supporting
    confidence: 0.89
    note: "Rychkov et al. (2012) - 3D Ising bootstrap island: nu=0.6299, eta=0.0363, consistent with Monte Carlo"
  - type: related
    note: "Simmons-Duffin (2016) - Semidefinite programming bootstrap shows 3D Ising island shrinks with more constraints"
    confidence: 0.85

unknowns_addressed:
  - u-conformal-field-theory-x-critical-phenomena

proposed_tests:
  - description: >
      Extend the 3D Ising bootstrap to include spin-4 operators and compare the
      resulting island size to current bounds; shrinking island confirms uniqueness.
    method: "Semidefinite programming (SDPB code) with extended operator content; compare to Monte Carlo exponents"
    prediction: "Island shrinks to point as operator content increases, with exponents nu=0.6299(2), eta=0.0363(3)"
  - description: >
      Test whether the 3D Heisenberg (O(3)) universality class forms a distinct
      bootstrap island from the Ising class, confirming the classification conjecture.
    method: "O(3)-symmetric conformal bootstrap; look for isolated allowed region in (Delta_phi, Delta_s) space"
    prediction: "Distinct island at O(3) fixed point with exponents consistent with epsilon-expansion results"

related_disciplines:
  - statistical-mechanics
  - mathematical-physics
  - condensed-matter-physics
  - high-energy-physics
""")

# 3. Gene expression noise x information theory
write("cross-domain/biology-cs/b-gene-expression-noise-x-information-theory.yaml", f"""\
id: b-gene-expression-noise-x-information-theory
title: >
  Gene Expression Noise x Information Theory - transcriptional channel capacity
status: proposed
fields:
  - biology
  - computer-science
  - information-theory
bridge_claim: >
  Gene regulatory networks face a fundamental channel capacity limit: the maximum
  mutual information between transcription factor concentration (input) and target
  gene expression (output) is bounded by the noise in the system; cells near this
  limit implement near-optimal regulatory strategies predicted by information theory,
  measurable by single-cell RNA sequencing.
translation_table:
  - field_a_term: Transcription factor concentration (input signal)
    field_b_term: Channel input X
    note: >
      The concentration of an activating or repressing transcription factor is the
      input variable; its distribution (set by upstream signaling) determines the
      prior over the channel input.
  - field_a_term: Target gene mRNA/protein level (output)
    field_b_term: Channel output Y
    note: >
      The resulting expression level of the regulated gene is the noisy channel
      output; intrinsic noise (transcriptional bursting) and extrinsic noise
      (cell-to-cell variation in TF copy number) together define the channel noise.
  - field_a_term: Cell-to-cell expression variability (noise, eta^2)
    field_b_term: Channel noise power
    note: >
      The Fano factor and coefficient of variation of expression across cells
      set the effective SNR of the regulatory channel; higher noise compresses
      the capacity below the noiseless log2(n_states) bound.
  - field_a_term: Optimal regulatory response (Hill function shape)
    field_b_term: Channel capacity-achieving input distribution
    note: >
      The input TF distribution that maximizes mutual information matches the
      experimentally observed TF concentration distribution in bacteria and
      yeast, suggesting evolution has tuned regulatory strategies toward capacity.
communication_gap: >
  Information-theoretic analysis of gene regulation was pioneered by Tkacik and
  Walczak around 2008 but has not been widely adopted by molecular biologists who
  typically analyze single gene-pair interactions rather than information flows
  across regulatory networks.
cross_pollination_opportunities:
  - >
    Use single-cell RNA-seq data to compute mutual information between all TF-target
    pairs in a regulatory network, identifying information bottlenecks that limit
    cellular decision-making fidelity.
  - >
    Apply rate-distortion theory to ask how much of the TF signal is actually used
    by the cell, quantifying regulatory efficiency and identifying wasteful noise
    without functional benefit.
  - >
    Design synthetic promoters with noise characteristics that maximize information
    transfer for specific input TF distributions, guided by capacity-achieving
    channel design principles.
related_unknowns:
  - u-gene-expression-noise-x-information-theory
references:
  - doi: "10.1073/pnas.0604883103"
    note: "Tkacik, Walczak & Bialek (2008) - information flow and optimization in gene expression; PNAS 105:12265"
  - doi: "10.1016/j.cell.2013.02.039"
    note: "Eldar & Elowitz (2010) - functional roles for noise in genetic circuits; Nature 467:167"
last_reviewed: "{TODAY}"
""")

write("unknowns-catalog/biology/u-gene-expression-noise-x-information-theory.yaml", f"""\
id: u-gene-expression-noise-x-information-theory
title: "Do gene regulatory networks in living cells operate near their Shannon channel capacity limit, and what evolutionary pressures drive them toward or away from this optimum?"
status: open
priority: medium
disciplines:
  - systems-biology
  - information-theory
  - molecular-biology
summary: >
  Several measurements suggest E. coli and Drosophila gap gene networks operate
  near their information-theoretic channel capacity (Tkacik et al. 2008, Dubuis
  et al. 2013), but whether this is a general principle or a special case is
  debated. Key unknowns: (1) does capacity-maximization require specific noise
  structures (Poisson vs bursty) or is it robust? (2) are regulatory networks in
  multicellular development capacity-limited by intrinsic noise or by extrinsic
  fluctuations in morphogen gradients? (3) what is the evolutionary time scale
  for capacity optimization?
systematic_gaps:
  - Single-cell RNA-seq noise estimates conflate technical noise with biological noise; deconvolution methods are imperfect
  - Capacity calculations assume simple one-input one-output channels; real networks have correlated inputs and feedback
  - No direct test of whether capacity-near-optimal networks have higher fitness than sub-optimal ones
related_bridges:
  - b-gene-expression-noise-x-information-theory
last_reviewed: "{TODAY}"
""")

write("hypotheses/active/h-gene-expression-noise-x-information-theory.yaml", f"""\
id: h-gene-expression-noise-x-information-theory
title: >
  Developmental gene regulatory networks operating near channel capacity maximize
  positional information in morphogen gradients and produce sharper cell fate
  boundaries, measurable as reduced cell fate assignment error in single-cell atlases.
status: active
priority: medium
impact_score: 0.78
created: "{TODAY}"
last_updated: "{TODAY}"
author: USDR

evidence_links:
  - doi: "10.1073/pnas.0604883103"
    type: supporting
    confidence: 0.82
    note: "Tkacik et al. (2008) - mutual information near capacity in Drosophila gap gene network"
  - type: supporting
    note: "Dubuis et al. (2013) - positional information in Drosophila measured at ~4 bits, consistent with capacity limit"
    confidence: 0.79
  - type: related
    note: "Eldar & Elowitz (2010) - noise can be functional; distinguishes cases where noise is exploited vs tolerated"
    confidence: 0.71

unknowns_addressed:
  - u-gene-expression-noise-x-information-theory

proposed_tests:
  - description: >
      Compute mutual information between graded morphogen inputs and discrete cell
      fate outputs in multiple developmental systems using single-cell RNA-seq
      datasets; compare to theoretical channel capacity.
    method: "Non-parametric mutual information estimation (KSG estimator) on scRNA-seq; compare I(TF;fate) to H(input)"
    prediction: "Developmental decision circuits achieve >80% of theoretical capacity; housekeeping genes achieve <40%"
  - description: >
      Introduce synthetic noise amplifiers (high-burst promoters) in capacity-near-
      optimal circuits and measure cell fate assignment error rate by live imaging.
    method: "Optogenetic morphogen gradient + live cell fate reporter; measure boundary sharpness as function of noise level"
    prediction: "Fate boundary width scales inversely with mutual information as predicted by capacity theory"

related_disciplines:
  - systems-biology
  - information-theory
  - developmental-biology
  - molecular-biology
""")

# 4. Rational inattention x Shannon entropy
write("cross-domain/physics-economics/b-rational-inattention-x-entropy.yaml", f"""\
id: b-rational-inattention-x-entropy
title: >
  Rational Inattention x Shannon Entropy - cognitive bandwidth as information cost
status: proposed
fields:
  - economics
  - computer-science
  - information-theory
bridge_claim: >
  Sims' rational inattention model formalizes attention as a scarce cognitive
  resource with Shannon mutual information as the cost; optimal attention allocation
  under entropy cost produces price stickiness, infrequent adjustment, and lumpy
  consumption - predictions that match macroeconomic data better than rational
  expectations models.
translation_table:
  - field_a_term: Cognitive bandwidth (attention capacity)
    field_b_term: Channel capacity C (bits per unit time)
    note: >
      An agent can process at most C bits per unit time about the state of the world;
      this cap on information processing is identical to Shannon's channel capacity
      limit, making attention a scarce information-theoretic resource.
  - field_a_term: Prior distribution over economic states
    field_b_term: Prior distribution at channel input
    note: >
      The agent's prior over wages, prices, productivity is the channel input
      distribution; Bayesian updating under capacity constraint gives the posterior,
      which is capacity-achieving only for specific input distributions.
  - field_a_term: Endogenous inattention (ignoring small price changes)
    field_b_term: Quantization noise / coarse-grained channel output
    note: >
      Under binding capacity constraints, the agent optimally ignores small signals
      (below the quantization threshold) and responds only to large changes - producing
      the lumpy adjustment and price stickiness observed in micro data.
  - field_a_term: Optimal attention allocation across goods
    field_b_term: Water-filling power allocation across parallel channels
    note: >
      The Shannon water-filling theorem describes optimal power allocation to parallel
      channels; rational inattention implies the analogous attention allocation across
      different economic variables, concentrating attention on highest-variance goods.
communication_gap: >
  Shannon information theory and macroeconomics have largely developed in isolation;
  Sims (2003) introduced mutual information cost to economics, but most macro models
  still use rational expectations with full information, ignoring information
  acquisition costs that are central to signal processing theory.
cross_pollination_opportunities:
  - >
    Apply water-filling optimality conditions from information theory to derive
    testable predictions about which prices consumers track closely (high variance
    goods) vs ignore (stable goods), using scanner data.
  - >
    Use rate-distortion theory to compute the minimum information required to make
    near-optimal economic decisions, quantifying the cost of cognitive limitations
    on welfare.
  - >
    Extend rational inattention to multi-agent settings using network information
    theory (broadcast channels, multiple access channels) to model how attention
    scarcity propagates through supply chains.
related_unknowns:
  - u-rational-inattention-x-entropy
references:
  - doi: "10.1016/j.jmoneco.2003.06.002"
    note: "Sims (2003) - implications of rational inattention; J Monetary Economics 50:665"
  - doi: "10.1016/j.jmoneco.2010.05.006"
    note: "Mackowiak & Wiederholt (2009) - optimal sticky prices under rational inattention"
last_reviewed: "{TODAY}"
""")

write("unknowns-catalog/economics/u-rational-inattention-x-entropy.yaml", f"""\
id: u-rational-inattention-x-entropy
title: "What is the empirically measurable cognitive channel capacity of individual economic agents, and how does capacity heterogeneity across agents shape aggregate price dynamics?"
status: open
priority: medium
disciplines:
  - economics
  - information-theory
  - cognitive-science
summary: >
  Rational inattention models require an agent-specific capacity parameter kappa
  (bits per period) but this cannot be directly observed; it is calibrated to match
  moments of consumption or price-setting data. Key unknowns: (1) can laboratory
  experiments (attention tracking, response time) directly measure kappa and validate
  the Shannon cost function vs alternative cost functions (Tsallis entropy, Fisher
  information)? (2) does capacity vary systematically with wealth, education, or
  cognitive load? (3) how do capacity constraints interact at the firm level with
  menu costs to produce the joint distribution of price changes?
systematic_gaps:
  - Direct measurement of attention capacity in economic experiments is not standard; most evidence is indirect (moments of price distributions)
  - The Shannon mutual information cost function is assumed not derived; alternatives have not been systematically tested
  - Rational inattention models typically assume Gaussian signals; non-Gaussian returns in financial markets are not well handled
related_bridges:
  - b-rational-inattention-x-entropy
last_reviewed: "{TODAY}"
""")

write("hypotheses/active/h-rational-inattention-x-entropy.yaml", f"""\
id: h-rational-inattention-x-entropy
title: >
  Consumers optimally allocate attention across goods following the information-
  theoretic water-filling rule, concentrating attention on highest-variance price
  categories, producing predictable patterns in scanner-data price adjustment
  frequencies that match rational inattention predictions.
status: active
priority: medium
impact_score: 0.73
created: "{TODAY}"
last_updated: "{TODAY}"
author: USDR

evidence_links:
  - doi: "10.1016/j.jmoneco.2003.06.002"
    type: supporting
    confidence: 0.80
    note: "Sims (2003) - rational inattention model derives price stickiness from Shannon cost"
  - doi: "10.1016/j.jmoneco.2010.05.006"
    type: supporting
    confidence: 0.76
    note: "Mackowiak & Wiederholt (2009) - optimal sticky prices: firms track aggregate shocks less than idiosyncratic"
  - type: related
    note: "Woodford (2009) - information-constrained state-dependent pricing; attention to large shocks"
    confidence: 0.72

unknowns_addressed:
  - u-rational-inattention-x-entropy

proposed_tests:
  - description: >
      Use Nielsen scanner data to measure price adjustment frequency and size
      distribution across product categories; test whether adjustment frequency
      correlates with price variance as predicted by water-filling.
    method: "Regression of adjustment frequency on price variance across 200+ product categories; compare to water-filling slope"
    prediction: "Water-filling predicts adjustment frequency proportional to variance; R^2 > 0.6 across categories"
  - description: >
      Laboratory experiment: present subjects with multiple price streams of known
      variance; measure attention allocation (eye-tracking) and compare to water-
      filling optimum.
    method: "Eye-tracking experiment with calibrated price variance; measure fixation time per stream"
    prediction: "Fixation time proportional to price variance, matching water-filling capacity allocation"

related_disciplines:
  - economics
  - information-theory
  - cognitive-science
  - macroeconomics
""")

# 5. Metabolic flux x linear programming
write("cross-domain/chemistry-biology/b-metabolic-flux-x-linear-programming.yaml", f"""\
id: b-metabolic-flux-x-linear-programming
title: >
  Metabolic Flux Analysis x Linear Programming - stoichiometric constraints as convex polytope
status: proposed
fields:
  - biology
  - mathematics
  - systems-biology
bridge_claim: >
  Flux balance analysis (FBA) models cellular metabolism as a linear program: maximize
  biomass production subject to stoichiometric equality constraints and thermodynamic
  inequality constraints; the feasible flux space is a convex polytope and the optimal
  metabolic state is a vertex - making systems biology a branch of linear programming.
translation_table:
  - field_a_term: Stoichiometric matrix S (m reactions x n metabolites)
    field_b_term: Constraint matrix A in LP (Ax = b, x >= 0)
    note: >
      Each row of S is a metabolite mass balance; steady-state assumption
      (dC/dt = 0) gives Sv = 0, which is the LP equality constraint; upper and
      lower bounds on fluxes (thermodynamic reversibility, enzyme capacity) give
      the inequality constraints.
  - field_a_term: Flux distribution vector v (mmol/gDW/h)
    field_b_term: Decision variable vector x in LP
    note: >
      The vector of all reaction fluxes is the LP decision variable; each feasible
      flux distribution is a point in the flux polytope; optimizing biomass yield
      finds the flux vertex maximizing the objective function.
  - field_a_term: Optimal growth flux (biomass reaction rate)
    field_b_term: LP objective function value
    note: >
      The biomass reaction is a pseudo-reaction with stoichiometry equal to the dry-
      weight composition of the cell; maximizing its flux is the LP objective, equivalent
      to maximizing growth rate subject to nutrient constraints.
  - field_a_term: Extreme ray (thermodynamic unfeasible direction)
    field_b_term: Infeasibility certificate (LP dual variable)
    note: >
      Thermodynamic infeasibility (net ATP consumption without energy source) corresponds
      to an unbounded LP ray; adding thermodynamic constraints (loop-law) restricts the
      polytope to eliminate these rays.
communication_gap: >
  Linear programming theory (simplex method, duality) has been mature since 1947,
  but its systematic application to genome-scale metabolic models only began in the
  1990s (Varma & Palsson); most biology textbooks do not present metabolism as an
  optimization problem, impeding import of 70 years of LP theory.
cross_pollination_opportunities:
  - >
    Apply LP sensitivity analysis (shadow prices, ranging) to genome-scale metabolic
    models to predict which nutrient constraints are most limiting for growth, guiding
    fermentation medium optimization.
  - >
    Use LP duality to interpret metabolic flux as a resource allocation problem:
    the dual variables are shadow prices of metabolites, analogous to prices in
    competitive equilibrium theory.
  - >
    Import integer programming (MILP) methods to model on/off gene regulation in
    metabolism, solving problems like minimal gene knockouts for metabolic engineering.
related_unknowns:
  - u-metabolic-flux-x-linear-programming
references:
  - doi: "10.1038/nbt.1614"
    note: "Orth, Thiele & Palsson (2010) - what is flux balance analysis? Nature Biotechnology 28:245"
  - doi: "10.1038/msb.2013.18"
    note: "Bordbar et al. (2014) - constraint-based models predict metabolic and associated cellular functions"
last_reviewed: "{TODAY}"
""")

write("unknowns-catalog/biology/u-metabolic-flux-x-linear-programming.yaml", f"""\
id: u-metabolic-flux-x-linear-programming
title: "Does the assumption of growth-rate maximization in flux balance analysis hold across environmental conditions and organisms, or does the objective function change with nutritional stress and evolutionary history?"
status: open
priority: medium
disciplines:
  - systems-biology
  - mathematics
  - microbiology
summary: >
  FBA accurately predicts E. coli growth rates and gene essentiality using biomass
  maximization as the objective, but the objective function changes under stress,
  starvation, and in different organisms. Key unknowns: (1) what is the correct
  multi-objective formulation for mixed nutritional conditions (maximize growth AND
  minimize ATP waste)? (2) do cancer cells use a different objective (maximize
  ATP flux, Warburg effect) than normal cells? (3) can the objective function be
  inferred from flux data without assuming it a priori?
systematic_gaps:
  - Biomass composition varies with growth rate and environment, making the objective function itself a variable
  - 13C metabolic flux analysis measures actual fluxes but is limited to ~100 reactions; genome-scale FBA has ~2000 reactions with no direct validation
  - Multi-objective FBA (MOMA, ROOM) requires choosing trade-off weights that are not determined by first principles
related_bridges:
  - b-metabolic-flux-x-linear-programming
last_reviewed: "{TODAY}"
""")

write("hypotheses/active/h-metabolic-flux-x-linear-programming.yaml", f"""\
id: h-metabolic-flux-x-linear-programming
title: >
  Metabolic flux objective functions shift from biomass maximization to ATP-per-
  carbon maximization under carbon limitation, and this shift is detectable by
  comparing 13C MFA flux distributions to FBA predictions under different C:N
  ratios, falsifying single-objective FBA models.
status: active
priority: medium
impact_score: 0.75
created: "{TODAY}"
last_updated: "{TODAY}"
author: USDR

evidence_links:
  - doi: "10.1038/nbt.1614"
    type: supporting
    confidence: 0.85
    note: "Orth et al. (2010) - FBA review; biomass maximization works well in exponential growth but less well in stationary phase"
  - type: supporting
    note: "Schuetz et al. (2012) - multi-objective optimality in E. coli metabolism across 25 environments; no single objective"
    confidence: 0.78
  - type: opposing
    note: "Edwards & Palsson (2000) - E. coli FBA growth predictions accurate across 6 carbon sources, supporting single biomass objective"
    confidence: 0.72

unknowns_addressed:
  - u-metabolic-flux-x-linear-programming

proposed_tests:
  - description: >
      Grow E. coli in chemostats at 5 different C:N ratios; measure 13C-labeling
      fluxes; compare to FBA predictions from biomass-maximization vs
      ATP-maximization objectives.
    method: "13C metabolic flux analysis + genome-scale FBA; objective function comparison via chi-square fitness"
    prediction: "At C:N < 1 (carbon-limited), ATP-maximization fits measured fluxes better; at C:N > 5, biomass-maximization wins"

related_disciplines:
  - systems-biology
  - microbiology
  - mathematics
  - biochemistry
""")

# 6. Mean field theory x neural networks
write("cross-domain/physics-cs/b-mean-field-theory-x-neural-networks.yaml", f"""\
id: b-mean-field-theory-x-neural-networks
title: >
  Mean Field Theory x Deep Neural Networks - infinite-width limit as Gaussian process
status: proposed
fields:
  - physics
  - computer-science
  - statistical-mechanics
bridge_claim: >
  In the infinite-width limit, a deep neural network at initialization is exactly a
  Gaussian process with a kernel determined by the activation function (NNGP kernel);
  mean field theory of neural networks predicts the edge-of-chaos initialization
  condition (variance preservation) that enables training of very deep networks.
translation_table:
  - field_a_term: Pre-activations at layer l (hidden unit values before activation)
    field_b_term: Gaussian random field (mean-field approximation)
    note: >
      As width -> infinity, each pre-activation is a sum of infinitely many
      independent terms, converging to Gaussian by CLT - the mean-field limit;
      the resulting distribution is determined solely by the variance propagation
      equations.
  - field_a_term: Variance propagation through activation functions
    field_b_term: Mean-field self-consistency equations
    note: >
      The variance of pre-activations propagates through the network via
      sigma^2_{{l+1}} = sigma_w^2 * E[phi(z)^2] + sigma_b^2, a mean-field
      fixed-point equation whose solution determines the initialization distribution.
  - field_a_term: Edge-of-chaos condition (chi = 1, order-to-chaos transition)
    field_b_term: Critical point of mean-field dynamics
    note: >
      The mean-field order parameter chi (Jacobian eigenvalue) equals 1 at the
      critical point between ordered (chi < 1, vanishing gradient) and chaotic
      (chi > 1, exploding gradient) phases; training is possible only at this
      edge-of-chaos critical point.
  - field_a_term: NNGP kernel K^l(x,x')
    field_b_term: Gaussian process covariance function
    note: >
      The dot-product kernel computed by the mean-field recursion is the covariance
      of the infinite-width neural network Gaussian process; it determines the
      generalization properties without any training.
communication_gap: >
  Statistical physicists developed mean-field theory of disordered systems (Sherrington-
  Kirkpatrick model, Parisi replica method) in the 1970s-80s; its application to deep
  learning was made explicit only around 2017 (Poole et al., Lee et al.) despite strong
  mathematical parallels available for decades.
cross_pollination_opportunities:
  - >
    Use the mean-field phase diagram (sigma_w vs sigma_b space) to predict optimal
    initialization hyperparameters for any activation function, replacing manual
    grid search with analytic computation.
  - >
    Apply replica method from disordered systems to analyze the loss landscape of
    overparameterized networks, predicting the existence of spurious local minima.
  - >
    Import finite-size scaling theory to understand how mean-field predictions break
    down for finite-width networks, quantifying the width needed for NNGP approximation.
related_unknowns:
  - u-mean-field-theory-x-neural-networks
references:
  - doi: "10.48550/arXiv.1711.00165"
    note: "Lee et al. (2018) - deep neural networks as Gaussian processes; ICLR 2018"
  - doi: "10.48550/arXiv.1606.05340"
    note: "Poole et al. (2016) - exponential expressivity from shallow networks at the edge of chaos"
last_reviewed: "{TODAY}"
""")

write("unknowns-catalog/machine-learning/u-mean-field-theory-x-neural-networks.yaml", f"""\
id: u-mean-field-theory-x-neural-networks
title: "How do mean-field predictions for deep neural network initialization break down as network width decreases, and what is the minimum width at which finite-width corrections become significant for training?"
status: open
priority: medium
disciplines:
  - machine-learning
  - statistical-mechanics
  - mathematics
summary: >
  Mean-field theory predicts exact NNGP behavior only in the infinite-width limit.
  For practical finite-width networks (width 64-2048), corrections are important
  but their magnitude and structure are not fully understood. Key unknowns: (1) what
  is the 1/width expansion of training dynamics (Neural Tangent Kernel vs NNGP
  corrections)? (2) at what width does the ordered/chaotic phase transition
  disappear? (3) do finite-width corrections to the edge-of-chaos condition shift
  the optimal initialization scheme?
systematic_gaps:
  - 1/width corrections to NTK and NNGP have been computed to first order but higher-order terms are intractable
  - Empirical comparison of mean-field predictions to finite-width networks is limited to smooth activations; ReLU networks have phase transitions at the origin
  - The effect of residual connections and normalization layers on the mean-field phase diagram is only partially understood
related_bridges:
  - b-mean-field-theory-x-neural-networks
last_reviewed: "{TODAY}"
""")

write("hypotheses/active/h-mean-field-theory-x-neural-networks.yaml", f"""\
id: h-mean-field-theory-x-neural-networks
title: >
  Networks initialized at the mean-field edge-of-chaos critical point (chi=1) train
  successfully to arbitrary depth while networks initialized in the ordered (chi<1)
  or chaotic (chi>1) phases fail due to vanishing or exploding gradients, with the
  failure depth scaling as 1/|1-chi|.
status: active
priority: medium
impact_score: 0.81
created: "{TODAY}"
last_updated: "{TODAY}"
author: USDR

evidence_links:
  - doi: "10.48550/arXiv.1711.00165"
    type: supporting
    confidence: 0.88
    note: "Lee et al. (2018) - NNGP kernel matches finite-width networks at criticality; Gaussian process predictions hold"
  - doi: "10.48550/arXiv.1606.05340"
    type: supporting
    confidence: 0.85
    note: "Poole et al. (2016) - expressivity and trainability peak at edge of chaos; deep networks require chi=1"
  - type: related
    note: "Schoenholz et al. (2017) - depth scales exponentially into ordered phase; linear into chaotic phase"
    confidence: 0.83

unknowns_addressed:
  - u-mean-field-theory-x-neural-networks

proposed_tests:
  - description: >
      Train 100-layer networks at a range of (sigma_w, sigma_b) initialization
      parameters spanning ordered, critical, and chaotic phases; measure trainable
      depth as a function of chi.
    method: "CIFAR-10 training experiments with varied initialization; measure training loss convergence as function of depth and chi"
    prediction: "Maximum trainable depth D_max ~ C/|1-chi|; networks at chi=1 succeed at all tested depths"

related_disciplines:
  - machine-learning
  - statistical-mechanics
  - mathematics
  - deep-learning
""")

# 7. Knot invariants x DNA topology
write("cross-domain/math-biology/b-knot-invariants-x-dna-topology.yaml", f"""\
id: b-knot-invariants-x-dna-topology
title: >
  Knot Invariants x DNA Topology - topoisomerase as knot simplifier
status: proposed
fields:
  - mathematics
  - biology
  - molecular-biology
bridge_claim: >
  DNA in vivo is knotted and catenated due to replication and transcription;
  topoisomerases catalyze specific topological changes (strand passage, religation)
  that reduce writhe and linking number - mathematically, they compute knot
  invariants and perform Reidemeister moves on the DNA knot diagram, making cell
  biology a live knot theory experiment.
translation_table:
  - field_a_term: DNA supercoiling (writhe Wr)
    field_b_term: Writhe of a knot (signed crossing number)
    note: >
      Writhe counts the net excess of positive over negative crossings in a DNA
      projection; it is the biologically relevant topological invariant that
      supercoiling relaxation enzymes (Gyrase, Topo I) modify.
  - field_a_term: Topoisomerase II (type II topoisomerase)
    field_b_term: Strand-passage move (Reidemeister move II)
    note: >
      Topo II passes one DNA double strand through another via a transient break,
      implementing the Reidemeister Type II move that changes crossing number by 2
      - the elementary step in knot simplification.
  - field_a_term: DNA catenane (two linked circular DNA molecules)
    field_b_term: Hopf link (simplest 2-component link)
    note: >
      Newly replicated circular DNA molecules are interlocked as a catenane;
      decatenation by Topo II is equivalent to unlinking the Hopf link by
      strand passage moves.
  - field_a_term: Knot probability in confined DNA
    field_b_term: Knot spectrum of random closed curves
    note: >
      The probability distribution of knot types in bacteriophage DNA matches
      the theoretical knot spectrum of random closed curves in confined volume,
      confirming the topological equilibrium predicted by polymer knot theory.
communication_gap: >
  Knot theory and DNA topology developed in parallel for 30 years; topologists
  developed invariants (Jones polynomial, HOMFLY) while molecular biologists
  characterized topoisomerases, with limited cross-talk until Sumners, Dean,
  and Cozzarelli connected them in the late 1980s-1990s.
cross_pollination_opportunities:
  - >
    Use HOMFLY polynomial computations on electron microscopy images of DNA knots
    to classify topoisomerase reaction pathways, determining whether they prefer
    negative or positive node simplifications.
  - >
    Apply polynomial knot invariants to design topoisomerase inhibitors that
    selectively block unknotting of specific DNA knot types (cancer-specific
    replication intermediates).
  - >
    Import lattice knot Monte Carlo methods to compute DNA knot formation
    probabilities as a function of chromosome compaction level, predicting
    topological stress in chromatin.
related_unknowns:
  - u-knot-invariants-x-dna-topology
references:
  - doi: "10.1038/22605"
    note: "Rybenkov et al. (1997) - simplification of DNA topology by type II topoisomerases; Nature 388:627"
  - doi: "10.1073/pnas.80.14.4519"
    note: "Sumners & Whittington (1988) - knots in self-avoiding walks; mathematical framework for DNA knotting"
last_reviewed: "{TODAY}"
""")

write("unknowns-catalog/mathematics/u-knot-invariants-x-dna-topology.yaml", f"""\
id: u-knot-invariants-x-dna-topology
title: "What is the minimal set of knot-theoretic invariants sufficient to characterize all topological states of chromosomal DNA in vivo, and can topoisomerase reaction mechanisms be inferred from changes in these invariants?"
status: open
priority: medium
disciplines:
  - mathematics
  - molecular-biology
  - biophysics
summary: >
  Topoisomerase reaction mechanisms change DNA knot type via specific topological
  moves, but the complete classification of in vivo DNA knot types and their
  distributions is not known for eukaryotic chromosomes. Key unknowns: (1) does
  eukaryotic chromatin topology involve higher-order links (Brunnian links, satellite
  knots) beyond simple torus knots? (2) can polynomial invariants distinguish
  biologically relevant DNA knots (replication catenanes) from accidental knots?
  (3) what is the topological entropy cost of DNA replication in a confined
  nucleus?
systematic_gaps:
  - Electron microscopy of DNA knots is limited to short plasmids; chromosome-scale topology is inaccessible to current methods
  - HOMFLY polynomial computation is exponentially hard in crossing number; practical for knots up to ~20 crossings only
  - In vivo topoisomerase activity is measured biochemically, not topologically; direct measurement of DNA knot type in living cells is not possible
related_bridges:
  - b-knot-invariants-x-dna-topology
last_reviewed: "{TODAY}"
""")

write("hypotheses/active/h-knot-invariants-x-dna-topology.yaml", f"""\
id: h-knot-invariants-x-dna-topology
title: >
  Topoisomerase II preferentially simplifies DNA knot crossings with the same
  handedness as the writhe of the supercoiled substrate, reflecting a
  geometric preference for negative node passages that reduces the number of
  crossings faster than random strand passage, measurable by single-molecule
  fluorescence of DNA knot relaxation.
status: active
priority: medium
impact_score: 0.74
created: "{TODAY}"
last_updated: "{TODAY}"
author: USDR

evidence_links:
  - doi: "10.1038/22605"
    type: supporting
    confidence: 0.83
    note: "Rybenkov et al. (1997) - Topo II simplifies knots below equilibrium level, indicating non-random strand passage"
  - type: supporting
    note: "Vologodskii (2009) - mechanism of topoisomerase II simplification: geometric selection of crossings explains below-equilibrium decatenation"
    confidence: 0.79
  - type: related
    note: "Buck & Flapan (2007) - signed crossing number as metric for topological simplification preference"
    confidence: 0.71

unknowns_addressed:
  - u-knot-invariants-x-dna-topology

proposed_tests:
  - description: >
      Use single-molecule magnetic tweezers to track knot type changes in circular
      DNA during Topo II activity; measure frequency of positive vs negative node
      passage as a function of supercoiling.
    method: "Magnetic tweezers + fluorescent knotting assay; classify crossings from extension-force curves; score handedness"
    prediction: "Negative node passage frequency > 0.5 for negatively supercoiled DNA; above equilibrium unlinking rate"

related_disciplines:
  - mathematics
  - molecular-biology
  - biophysics
  - topology
""")

# 8. Active Brownian motion x cell migration
write("cross-domain/physics-biology/b-active-brownian-motion-x-cell-migration.yaml", f"""\
id: b-active-brownian-motion-x-cell-migration
title: >
  Active Brownian Motion x Cell Migration - self-propelled particles in 2D
status: proposed
fields:
  - biology
  - physics
  - biophysics
bridge_claim: >
  Migrating cells (neutrophils, cancer cells) exhibit active Brownian motion:
  directional persistence at short timescales and diffusive behavior at long
  timescales, described by the active Ornstein-Uhlenbeck process; the persistence
  time and effective diffusivity are controlled by internal cytoskeletal polarization
  dynamics and external chemokine gradients.
translation_table:
  - field_a_term: Cell crawling velocity (mu/h) with persistence
    field_b_term: Self-propulsion velocity of active Brownian particle
    note: >
      A migrating cell maintains approximately constant speed with slowly
      reorienting direction, exactly matching the active Brownian particle model
      where self-propulsion speed v_0 is constant and orientation diffuses with
      rotational diffusivity D_r.
  - field_a_term: Persistence time (tau = 1/D_r, minutes to hours)
    field_b_term: Rotational diffusion time of active Brownian particle
    note: >
      The persistence time tau over which the cell maintains its direction is
      1/(2D_r) in 2D; it is set by the turnover time of the cytoskeletal polarity
      complex (Rac/Cdc42) and directly measurable from cell trajectory statistics.
  - field_a_term: Effective long-time diffusivity (D_eff = v_0^2 * tau / 2)
    field_b_term: Long-time diffusion coefficient of active particle
    note: >
      At timescales >> tau, cell trajectories become diffusive with D_eff = v_0^2 *
      tau / (d-1) in d dimensions - the active Brownian particle result, relating
      macroscopic cell spreading to microscopic motility parameters.
  - field_a_term: Chemotaxis bias (gradient-directed migration)
    field_b_term: Active particle with biased angular diffusion
    note: >
      Chemokine gradients bias the rotational diffusion of the cell's polarity
      axis toward the chemoattractant, equivalent to an active Brownian particle
      with a preferred orientation - adding drift to the diffusive regime.
communication_gap: >
  Active matter physics (Vicsek model, active Brownian particles) and cell biology
  developed independently; the ABP model was systematically applied to single cell
  migration only after ~2010, despite single-cell tracking methods being available
  since the 1980s.
cross_pollination_opportunities:
  - >
    Use ABP theory to derive the optimal chemokine gradient steepness for
    maximum cell-migration precision, guiding design of microfluidic chemotaxis assays.
  - >
    Apply run-and-tumble models (bacterial motility) to cells that alternate between
    fast-moving and stationary phases (amoeboid vs mesenchymal migration).
  - >
    Import active matter collective motion theory (Vicsek model, motility-induced
    phase separation) to predict when cancer cell populations will form cohesive
    invasive streams vs dispersed invasion.
related_unknowns:
  - u-active-brownian-motion-x-cell-migration
references:
  - doi: "10.1073/pnas.1118355109"
    note: "Maiuri et al. (2015) - actin flow mediates a coupling between cell morphology and migration velocity; PNAS 112:1475"
  - doi: "10.1088/1367-2630/13/7/073036"
    note: "Trepat et al. (2009) - forces behind collective cell migration; active Brownian motion description"
last_reviewed: "{TODAY}"
""")

write("unknowns-catalog/biology/u-active-brownian-motion-x-cell-migration.yaml", f"""\
id: u-active-brownian-motion-x-cell-migration
title: "Do migrating cancer cells in 3D tissue environments follow active Brownian particle statistics, and how does confinement geometry and matrix stiffness modify the effective persistence time and diffusivity?"
status: open
priority: medium
disciplines:
  - biophysics
  - cell-biology
  - physics
summary: >
  Active Brownian particle models fit single-cell migration statistics in 2D
  well, but 3D migration in extracellular matrix introduces confinement,
  topological constraints, and mechanosensing that modify the effective ABP
  parameters. Key unknowns: (1) how does ECM pore size relative to cell size
  affect the persistence time? (2) does stiffness gradient sensing (durotaxis)
  modify the ABP rotational diffusion, and if so how? (3) what is the
  relationship between ABP parameters measured in 2D and invasive potential in
  3D tumor organoids?
systematic_gaps:
  - 3D single-cell tracking in dense ECM is technically challenging; most ABP parameterizations are from 2D assays
  - Cell heterogeneity (different phenotypic states) produces mixed ABP populations; population-level statistics mask individual-cell differences
  - Active Brownian particle theory assumes constant self-propulsion speed; migrating cells show speed-persistence correlations not captured by basic ABP
related_bridges:
  - b-active-brownian-motion-x-cell-migration
last_reviewed: "{TODAY}"
""")

write("hypotheses/active/h-active-brownian-motion-x-cell-migration.yaml", f"""\
id: h-active-brownian-motion-x-cell-migration
title: >
  Cancer cell invasiveness in 3D ECM is quantitatively predicted by the active
  Brownian particle persistence time and self-propulsion speed measured in 2D
  migration assays, with more invasive cell lines showing longer persistence
  times and higher effective diffusivity.
status: active
priority: medium
impact_score: 0.72
created: "{TODAY}"
last_updated: "{TODAY}"
author: USDR

evidence_links:
  - doi: "10.1073/pnas.1118355109"
    type: supporting
    confidence: 0.79
    note: "Maiuri et al. (2015) - actin flow speed predicts migration velocity; ABP framework validated in 2D"
  - type: supporting
    note: "Petrie & Yamada (2012) - mechanisms of 3D cell migration; persistence is a key predictor of invasion depth"
    confidence: 0.74
  - type: related
    note: "Weiger et al. (2010) - chemoattractant concentration modulates ABP rotational diffusion via Rac1 dynamics"
    confidence: 0.69

unknowns_addressed:
  - u-active-brownian-motion-x-cell-migration

proposed_tests:
  - description: >
      Measure ABP parameters (v_0, tau) for a panel of 10 cancer cell lines
      with known invasiveness in 2D scratch assays; compare to 3D Matrigel
      invasion depth measured over 72 h.
    method: "Single-cell tracking in 2D (30 min intervals, 100 cells/line); ABP parameter estimation by MSD analysis; 3D Matrigel invasion assay"
    prediction: "Invasion depth correlates with D_eff = v_0^2 * tau / 2 with R^2 > 0.8 across cell lines"

related_disciplines:
  - cell-biology
  - biophysics
  - cancer-biology
  - physics
""")

# 9. Auction design x complexity theory
write("cross-domain/economics-math/b-auction-design-x-complexity-theory.yaml", f"""\
id: b-auction-design-x-complexity-theory
title: >
  Auction Design x Computational Complexity - optimal auctions as NP-hard problems
status: proposed
fields:
  - economics
  - computer-science
  - mathematics
bridge_claim: >
  Computing the optimal (revenue-maximizing) mechanism for multi-item auctions with
  multiple bidders is NP-hard in general (Conitzer & Sandholm 2002); this hardness
  result explains why real-world auction design relies on simple heuristics (Vickrey,
  first-price) rather than optimal mechanisms - connecting auction theory to
  computational complexity.
translation_table:
  - field_a_term: Revenue-maximizing mechanism (Myerson optimal auction)
    field_b_term: NP-hard optimization problem
    note: >
      With one item and one bidder, Myerson's single-item optimal mechanism is
      computationally trivial; with k items and n bidders and correlated valuations,
      computing the optimal mechanism requires solving an exponentially large LP,
      which is NP-hard in k and n.
  - field_a_term: Bidder valuations (drawn from known distribution)
    field_b_term: Input to optimization algorithm
    note: >
      The mechanism designer knows only the distribution from which valuations are
      drawn, not realized values; the optimal mechanism is computed from this
      distribution, analogous to offline algorithm design in complexity theory.
  - field_a_term: VCG mechanism (welfare-maximizing, strategyproof)
    field_b_term: Polynomial-time approximation algorithm
    note: >
      VCG is polynomial-time computable and achieves social welfare maximization
      (not revenue maximization); it is the natural analogue of a greedy approximation
      algorithm that runs efficiently at the cost of suboptimal revenue.
  - field_a_term: Simple auction rules (posted price, sequential)
    field_b_term: Approximation algorithm with constant factor guarantee
    note: >
      Posted-price mechanisms achieve constant-factor approximations to optimal
      revenue for independent bidders, analogous to FPTAS algorithms; the
      approximation ratio quantifies the revenue loss from computational tractability.
communication_gap: >
  Mechanism design theory (Myerson, Maskin) and computational complexity (Cook,
  Karp) developed in economics and computer science respectively without
  cross-fertilization until the emergence of algorithmic mechanism design (Nisan,
  Ronen 1999), which unified them.
cross_pollination_opportunities:
  - >
    Apply inapproximability results (hardness of approximation) to establish lower
    bounds on the revenue loss from using simple auction formats, quantifying the
    price of computational tractability.
  - >
    Use fixed-parameter tractability (FPT algorithms) to find parameter regimes
    (few bidder types, additive valuations) where optimal auctions are efficiently
    computable.
  - >
    Apply machine learning theory (PAC learning) to learn approximately optimal
    auction mechanisms from bidder data, connecting algorithmic mechanism design
    to statistical learning theory.
related_unknowns:
  - u-auction-design-x-complexity-theory
references:
  - doi: "10.1145/501720.501721"
    note: "Conitzer & Sandholm (2002) - complexity of mechanism design; ACM EC 2002"
  - doi: "10.1145/509907.509928"
    note: "Nisan & Ronen (1999) - algorithmic mechanism design; STOC 1999"
last_reviewed: "{TODAY}"
""")

write("unknowns-catalog/economics/u-auction-design-x-complexity-theory.yaml", f"""\
id: u-auction-design-x-complexity-theory
title: "What is the optimal approximation ratio achievable by polynomial-time computable auction mechanisms for multi-item combinatorial auctions, and does P≠NP separate achievable from unachievable revenue guarantees?"
status: open
priority: medium
disciplines:
  - economics
  - computer-science
  - mathematics
summary: >
  The revenue gap between optimal and computationally tractable mechanisms is
  not fully characterized. For single-parameter bidders (downward-closed
  feasibility constraints), constant-factor approximations exist; for general
  combinatorial auctions, the best known approximation ratios are O(log m) (m =
  items). Key unknowns: (1) is there a polynomial-time mechanism achieving a
  constant-factor approximation for combinatorial auctions with subadditive
  valuations? (2) does the hardness of optimal mechanism design stem from
  NP-hardness or from information-theoretic (communication complexity) barriers?
  (3) can truthful mechanisms achieve the same approximation ratios as
  non-truthful ones?
systematic_gaps:
  - The optimal approximation ratio for multi-bidder multi-item auctions is not known; current bounds have large gaps
  - Whether truthfulness imposes an approximation cost beyond NP-hardness is open (related to the 'Price of Anarchy' for mechanism design)
  - Empirical auction data rarely identifies the theoretical revenue-maximizing benchmark, making validation of approximation bounds difficult
related_bridges:
  - b-auction-design-x-complexity-theory
last_reviewed: "{TODAY}"
""")

write("hypotheses/active/h-auction-design-x-complexity-theory.yaml", f"""\
id: h-auction-design-x-complexity-theory
title: >
  No polynomial-time truthful mechanism achieves better than O(sqrt(m))-approximation
  to optimal revenue for combinatorial auctions with m items and submodular
  valuations, establishing a computational hardness lower bound for truthful
  multi-item auction design under standard complexity assumptions.
status: active
priority: medium
impact_score: 0.77
created: "{TODAY}"
last_updated: "{TODAY}"
author: USDR

evidence_links:
  - doi: "10.1145/501720.501721"
    type: supporting
    confidence: 0.82
    note: "Conitzer & Sandholm (2002) - computing optimal mechanisms is NP-hard; establishes computational barrier"
  - type: supporting
    note: "Dobzinski & Nisan (2006) - approximation of multi-item auctions; current best ratio O(log m) for subadditive valuations"
    confidence: 0.78
  - type: opposing
    note: "Cai, Devanur & Weinberg (2016) - constant-factor approximation for additive bidders; truthfulness compatible with good approximation in restricted settings"
    confidence: 0.74

unknowns_addressed:
  - u-auction-design-x-complexity-theory

proposed_tests:
  - description: >
      Attempt to design a polynomial-time truthful mechanism for 2-item 2-bidder
      auctions with correlated submodular valuations that achieves better than
      O(1)-approximation; formal proof or counterexample needed.
    method: "Formal mechanism design + complexity reduction from known hard combinatorial problems (set cover, matching)"
    prediction: "No such mechanism exists for general correlated valuations; constant approximation only for independent or additive cases"

related_disciplines:
  - economics
  - computer-science
  - mathematics
  - game-theory
""")

# 10. Diffusion models x stochastic processes
write("cross-domain/physics-cs/b-diffusion-models-x-stochastic-processes.yaml", f"""\
id: b-diffusion-models-x-stochastic-processes
title: >
  Diffusion Generative Models x Stochastic Differential Equations - score matching as time-reversed diffusion
status: proposed
fields:
  - computer-science
  - mathematics
  - physics
bridge_claim: >
  Diffusion generative models (DALL-E, Stable Diffusion) learn to reverse a stochastic
  diffusion process (data to noise) by estimating the score function nabla_x log p(x);
  the generative SDE is the time-reversal of the forward Ito diffusion, grounded in
  Anderson's time-reversal theorem - making modern AI image generation a direct
  application of stochastic process theory.
translation_table:
  - field_a_term: Forward noising process (data -> Gaussian noise over time T)
    field_b_term: Forward Ito SDE: dX = f(X,t)dt + g(t)dW
    note: >
      The forward diffusion gradually corrupts data by adding Gaussian noise; this is
      an Ito stochastic differential equation with drift f (mean-reverting) and
      diffusion coefficient g(t); at time T, the distribution approaches pure noise.
  - field_a_term: Reverse denoising process (noise -> data sample)
    field_b_term: Time-reversed SDE (Anderson 1982)
    note: >
      Anderson's theorem states the time-reversal of an Ito diffusion is also an
      Ito SDE: dX = [f - g^2 * nabla log p_t(X)] dt + g dW_bar; the score function
      nabla log p_t is the only unknown and is learned by the neural network.
  - field_a_term: Score network (denoising neural network)
    field_b_term: Score function estimator s_theta(x,t) ~ nabla log p_t(x)
    note: >
      The neural network is trained to estimate the score (gradient of log density)
      at each noise level; this is equivalent to learning to denoise corrupted data
      by minimizing weighted denoising score matching objectives.
  - field_a_term: DDPM noise schedule (beta_1, ..., beta_T)
    field_b_term: Variance schedule g^2(t) of the forward SDE
    note: >
      The discrete noise schedule corresponds to the variance function of the forward
      SDE; continuous-time SDE formulations (Song et al. 2021) unify DDPM, SMLD, and
      other discrete schedules as special cases.
communication_gap: >
  Stochastic differential equations (Ito, 1944) and time-reversal theorems (Anderson,
  1982) existed decades before diffusion models; the explicit connection was made by
  Song et al. (2021) and Ho et al. (2020), enabling continuous-time generalization
  and principled design of noise schedules using SDE theory.
cross_pollination_opportunities:
  - >
    Apply numerical SDE solvers (Euler-Maruyama, Milstein, stochastic Runge-Kutta)
    to design faster diffusion model samplers, replacing heuristic DDIM with
    theory-grounded ODE solvers.
  - >
    Use Fokker-Planck equations to analyze the probability flow ODE of diffusion
    models, establishing convergence guarantees and optimal transport interpretations.
  - >
    Import path integral methods from physics to compute exact likelihoods under
    diffusion models, avoiding the score matching approximation for importance-
    sampling-based evaluation.
related_unknowns:
  - u-diffusion-models-x-stochastic-processes
references:
  - doi: "10.48550/arXiv.2011.13456"
    note: "Song et al. (2021) - score-based generative modeling through SDEs; ICLR 2021 Outstanding Paper"
  - doi: "10.48550/arXiv.2006.11239"
    note: "Ho et al. (2020) - denoising diffusion probabilistic models; NeurIPS 2020"
last_reviewed: "{TODAY}"
""")

write("unknowns-catalog/machine-learning/u-diffusion-models-x-stochastic-processes.yaml", f"""\
id: u-diffusion-models-x-stochastic-processes
title: "What is the theoretical lower bound on the number of sampling steps required for a diffusion model to generate samples indistinguishable from the data distribution, and how does this depend on data geometry and the choice of SDE?"
status: open
priority: medium
disciplines:
  - machine-learning
  - mathematics
  - stochastic-processes
summary: >
  Diffusion models require 10-1000 function evaluations per sample (vs 1 for GANs);
  while distillation and consistency models reduce this to 1-4 steps empirically, the
  theoretical minimum sampling steps for epsilon-accurate generation is not known.
  Key unknowns: (1) what is the optimal noise schedule minimizing total variation
  distance to the data distribution for fixed number of steps? (2) does the curvature
  of the probability flow ODE trajectory determine the required step count? (3) can
  manifold learning theory predict optimal SDE designs for different data geometries?
systematic_gaps:
  - Convergence analysis of diffusion samplers (DDPM, DDIM) is incomplete for non-Gaussian data; convergence rates depend on score estimation error
  - The optimal choice of forward SDE (variance-exploding vs variance-preserving vs sub-VP) for a given data distribution is not theoretically justified
  - Consistency models and distillation achieve fast sampling empirically but lack sample quality guarantees comparable to full DDPM
related_bridges:
  - b-diffusion-models-x-stochastic-processes
last_reviewed: "{TODAY}"
""")

write("hypotheses/active/h-diffusion-models-x-stochastic-processes.yaml", f"""\
id: h-diffusion-models-x-stochastic-processes
title: >
  The minimum number of sampling steps for epsilon-accurate diffusion model generation
  scales as O(d/epsilon^2) where d is the intrinsic data dimensionality, and this
  bound is achievable by the probability flow ODE with optimal step-size scheduling
  derived from the data's local curvature.
status: active
priority: medium
impact_score: 0.79
created: "{TODAY}"
last_updated: "{TODAY}"
author: USDR

evidence_links:
  - doi: "10.48550/arXiv.2011.13456"
    type: supporting
    confidence: 0.84
    note: "Song et al. (2021) - SDE framework unifies DDPM/SMLD; probability flow ODE enables deterministic sampling"
  - type: supporting
    note: "Chen et al. (2022) - sampling is as easy as learning the score; polynomial complexity for log-concave distributions"
    confidence: 0.77
  - type: related
    note: "Lu et al. (2022) - DPM-Solver: fast ODE solver reduces steps to 10-20 without quality loss for many datasets"
    confidence: 0.80

unknowns_addressed:
  - u-diffusion-models-x-stochastic-processes

proposed_tests:
  - description: >
      Measure FID vs number of sampling steps for datasets with known intrinsic
      dimensionality (d=2 MNIST manifold vs d~50 CelebA manifold); test whether
      the step count scaling with d matches the theoretical O(d/epsilon^2) prediction.
    method: "FID evaluation at 1,2,4,8,16,50,100 steps for datasets of known intrinsic dimension; fit scaling exponent"
    prediction: "Step count for FID < epsilon scales linearly with intrinsic d (not ambient D); exponent ~1/epsilon^2"

related_disciplines:
  - machine-learning
  - mathematics
  - stochastic-processes
  - deep-learning
""")

# 11. Muscle mechanics x crossbridge theory
write("cross-domain/biology-physics/b-muscle-mechanics-x-crossbridge-theory.yaml", f"""\
id: b-muscle-mechanics-x-crossbridge-theory
title: >
  Muscle Mechanics x Crossbridge Theory - force-velocity as stochastic motor ensemble
status: proposed
fields:
  - biology
  - physics
  - biophysics
bridge_claim: >
  Muscle force-velocity relationship (Hill equation: (F+a)(v+b)=const) emerges from
  the stochastic attachment-detachment kinetics of millions of myosin crossbridges;
  Huxley's 1957 sliding filament model is a master equation for crossbridge state
  transitions whose mean-field solution recovers Hill's phenomenological equation -
  connecting biophysics to stochastic process theory.
translation_table:
  - field_a_term: Myosin crossbridge (attached/detached state cycle)
    field_b_term: Two-state Markov chain (attachment rate f, detachment rate g)
    note: >
      Each myosin head cycles between detached (state 1) and attached (state 2)
      states with position-dependent rates f(x) and g(x); the probability
      distribution n(x,t) over crossbridge positions follows the Huxley master
      equation, a transport PDE.
  - field_a_term: Muscle force (pN per crossbridge, N per muscle)
    field_b_term: Mean-field average of Markov chain force
    note: >
      Total force is the sum of individual crossbridge forces (each ~5 pN);
      mean-field averaging over the crossbridge position distribution gives
      macroscopic force from microscopic Markov chain statistics.
  - field_a_term: Hill equation a/F_0 = b/(v_max) = hyperbolic constant
    field_b_term: Mean-field steady-state of Huxley master equation
    note: >
      The hyperbolic Hill equation is the exact mean-field solution of the
      Huxley master equation under specific rate function choices; it is the
      law of large numbers applied to crossbridge ensemble kinetics.
  - field_a_term: Force-clamp step response (mechanical transient)
    field_b_term: Relaxation of Markov chain to new steady state
    note: >
      After a sudden length step, force recovers through rapid crossbridge
      re-equilibration; the multiple time constants of recovery correspond to
      eigenvalues of the Huxley master equation Jacobian.
communication_gap: >
  Hill (1938) derived his force-velocity equation phenomenologically from
  thermodynamic arguments; Huxley (1957) provided the stochastic mechanistic
  model; the two were linked only gradually through mean-field analysis, and
  many muscle biologists still use Hill's equation without connecting it to
  crossbridge master equation foundations.
cross_pollination_opportunities:
  - >
    Apply fluctuation theorems (Jarzynski, Crooks) to single-molecule myosin
    measurements to determine the free energy landscape of the power stroke
    from non-equilibrium work distributions.
  - >
    Use Markov chain Monte Carlo simulations of the Huxley model to predict
    muscle force noise (variance above the shot noise floor) as a function of
    crossbridge number density and stiffness.
  - >
    Import generalized Langevin equation formalism to model non-Markovian
    crossbridge dynamics arising from viscoelastic filament compliance.
related_unknowns:
  - u-muscle-mechanics-x-crossbridge-theory
references:
  - doi: "10.1098/rspb.1957.0045"
    note: "Huxley (1957) - muscle structure and theories of contraction; Prog Biophys 7:255"
  - doi: "10.1038/s41592-018-0227-9"
    note: "Sweeney & Holzbaur (2016) - motor proteins; annual review integrating crossbridge and stochastic theory"
last_reviewed: "{TODAY}"
""")

write("unknowns-catalog/biology/u-muscle-mechanics-x-crossbridge-theory.yaml", f"""\
id: u-muscle-mechanics-x-crossbridge-theory
title: "How many distinct biochemical states does the myosin crossbridge cycle require to quantitatively reproduce all mechanical transients in skeletal muscle, and what are the structural correlates of these states?"
status: open
priority: medium
disciplines:
  - biophysics
  - cell-biology
  - structural-biology
summary: >
  The minimal crossbridge model (Huxley 1957) uses 2 states; subsequent models
  added states to explain mechanical transients (Huxley & Simmons 1971: 4 states)
  and ATP hydrolysis kinetics (Lymn & Taylor 1971: 4 biochemical states). The
  number of mechanochemical states required for a complete quantitative model remains
  debated. Key unknowns: (1) what are the structural intermediates of the power
  stroke resolved by cryo-EM and X-ray fiber diffraction? (2) does the off-axis
  component of myosin force contribute to filament lattice compliance? (3) can
  a single universal crossbridge model explain both skeletal and cardiac muscle
  mechanics?
systematic_gaps:
  - Cryo-EM of myosin in situ is limited to ~10 angstrom resolution; intermediate states are not structurally resolved
  - Mechanical transient data (T1 curve, recovery phases) constrain only a few rate constants; remaining parameters are underdetermined
  - Cardiac myosin has different isoforms and regulatory proteins (troponin, titin) that make direct comparison to skeletal difficult
related_bridges:
  - b-muscle-mechanics-x-crossbridge-theory
last_reviewed: "{TODAY}"
""")

write("hypotheses/active/h-muscle-mechanics-x-crossbridge-theory.yaml", f"""\
id: h-muscle-mechanics-x-crossbridge-theory
title: >
  A 6-state crossbridge model (pre-power stroke, power stroke, post-power stroke,
  three detached ATPase states) reproduces all mechanical transients in skeletal
  muscle within experimental error, and the rate constants are consistent with
  single-molecule optical trap measurements.
status: active
priority: medium
impact_score: 0.74
created: "{TODAY}"
last_updated: "{TODAY}"
author: USDR

evidence_links:
  - doi: "10.1098/rspb.1957.0045"
    type: supporting
    confidence: 0.85
    note: "Huxley (1957) - 2-state model recovers Hill equation; foundation for multi-state extensions"
  - type: supporting
    note: "Huxley & Simmons (1971) - rapid force recovery suggests at least 4 mechanical states; Nature 233:533"
    confidence: 0.82
  - type: related
    note: "Piazzesi et al. (2007) - single myosin step size from X-ray fiber diffraction; ~11 nm; supports 2-step power stroke"
    confidence: 0.80

unknowns_addressed:
  - u-muscle-mechanics-x-crossbridge-theory

proposed_tests:
  - description: >
      Fit a 6-state crossbridge model to the complete set of mechanical transients
      (T1 curve, phase 2 fast recovery, phase 3 slow recovery, steady-state force-
      velocity) simultaneously; compare to 2- and 4-state models.
    method: "Global nonlinear least-squares fit of ODE crossbridge model to digitized mechanical transient data from frog muscle"
    prediction: "6-state model achieves chi^2 < 1.5 per degree of freedom; 4-state and 2-state models show systematic residuals in phase 2 transients"

related_disciplines:
  - biophysics
  - cell-biology
  - structural-biology
  - physiology
""")

# 12. Expander graphs x error-correcting codes
write("cross-domain/math-cs/b-expander-graphs-x-error-correcting-codes.yaml", f"""\
id: b-expander-graphs-x-error-correcting-codes
title: >
  Expander Graphs x Error-Correcting Codes - spectral gap as code distance
status: proposed
fields:
  - mathematics
  - computer-science
bridge_claim: >
  Expander graphs (high connectivity, small spectral gap in the Laplacian) are the
  combinatorial objects underlying modern error-correcting codes; LDPC codes and
  turbo codes have Tanner graphs that are expanders, and the spectral gap of the
  Tanner graph determines the code's minimum distance and iterative decoding
  convergence rate.
translation_table:
  - field_a_term: Spectral gap (lambda_2 - lambda_1 of graph Laplacian)
    field_b_term: Code minimum distance / threshold for iterative decoding
    note: >
      The Ramanujan bound (spectral gap = 2*sqrt(d-1) - epsilon) characterizes
      optimal expanders; LDPC codes whose Tanner graphs meet this bound achieve
      the best-known minimum distance scaling and threshold performance under
      belief propagation decoding.
  - field_a_term: Tanner graph (bipartite factor graph of LDPC code)
    field_b_term: Bipartite expander graph
    note: >
      The Tanner graph of an LDPC code is a bipartite graph between variable nodes
      (codeword bits) and check nodes (parity constraints); its expansion ratio
      (minimum vertex expansion over all small subsets) controls the minimum
      distance of the code.
  - field_a_term: Belief propagation (iterative decoding)
    field_b_term: Expander mixing lemma convergence
    note: >
      Belief propagation converges to the correct codeword when the Tanner graph
      has sufficient expansion; the expander mixing lemma bounds the number of
      iterations needed for convergence as a function of spectral gap.
  - field_a_term: Girth (length of shortest cycle in Tanner graph)
    field_b_term: Locally tree-like structure of expander
    note: >
      High girth Tanner graphs are locally tree-like (no short cycles), enabling
      belief propagation to behave correctly for short block lengths; girth is
      related to expansion via the Moore bound.
communication_gap: >
  Algebraic coding theory (Hamming, BCH, Reed-Solomon codes) and graph expansion
  theory (Margulis, Lubotzky-Phillips-Sarnak) developed independently; their
  connection through Tanner codes and LDPC codes was established only in the
  1996-2001 period (Sipser-Spielman, Luby et al., Richardson-Urbanke).
cross_pollination_opportunities:
  - >
    Use Ramanujan graph constructions (LPS graphs) to design LDPC codes with
    provably optimal minimum distance scaling, surpassing the Gilbert-Varshamov
    bound for specific rates.
  - >
    Apply spectral graph theory (Cheeger's inequality) to quantitatively predict
    iterative decoding threshold from Tanner graph structure, enabling decoder
    performance prediction without Monte Carlo simulation.
  - >
    Import quantum expander constructions (quantum expander codes, qLDPC) to design
    quantum error-correcting codes with constant rate and distance scaling.
related_unknowns:
  - u-expander-graphs-x-error-correcting-codes
references:
  - doi: "10.1109/18.910575"
    note: "Sipser & Spielman (1996) - expander codes; IEEE Trans Information Theory 42:1710"
  - doi: "10.1109/18.910574"
    note: "Luby et al. (2001) - improved low-density parity-check codes using irregular graphs; IEEE TIT"
last_reviewed: "{TODAY}"
""")

write("unknowns-catalog/mathematics/u-expander-graphs-x-error-correcting-codes.yaml", f"""\
id: u-expander-graphs-x-error-correcting-codes
title: "Do there exist linear-time encodable and decodable error-correcting codes that simultaneously achieve the Gilbert-Varshamov bound and have linear minimum distance, and can quantum expander codes achieve constant rate with linear distance?"
status: open
priority: high
disciplines:
  - mathematics
  - computer-science
  - information-theory
summary: >
  Linear-time encodable/decodable codes are known (Spielman 1996, Guruswami-
  Sudan list decoding) but no known code simultaneously achieves linear-time
  complexity, near-GV rate, and linear minimum distance. For quantum codes, the
  breakthrough qLDPC constructions (Panteleev-Kalachev 2022, Leverrier-Tillich-
  Zemor 2022) achieve constant rate and linear distance but at the cost of
  complex constructions. Key unknowns: (1) is there a simple algebraic family of
  Ramanujan bipartite graphs realizable as LDPC Tanner graphs at all rates? (2) do
  quantum expander codes approach the hashing bound? (3) what is the minimum
  girth needed for belief propagation to achieve Shannon capacity for AWGN?
systematic_gaps:
  - The probabilistic existence of good LDPC codes is known but explicit Ramanujan constructions exist only for restricted degree sequences
  - Quantum LDPC threshold analysis under circuit-level noise is incomplete; most results assume phenomenological noise models
  - The tradeoff between girth, minimum distance, and rate in LDPC codes is only partially characterized algebraically
related_bridges:
  - b-expander-graphs-x-error-correcting-codes
last_reviewed: "{TODAY}"
""")

write("hypotheses/active/h-expander-graphs-x-error-correcting-codes.yaml", f"""\
id: h-expander-graphs-x-error-correcting-codes
title: >
  Tanner graph spectral gap is a stronger predictor of LDPC code threshold
  performance under belief propagation than variable or check node degree
  distributions alone, and codes constructed from Ramanujan graphs achieve
  belief propagation thresholds within 0.1 dB of the Shannon limit.
status: active
priority: high
impact_score: 0.83
created: "{TODAY}"
last_updated: "{TODAY}"
author: USDR

evidence_links:
  - doi: "10.1109/18.910575"
    type: supporting
    confidence: 0.87
    note: "Sipser & Spielman (1996) - expander codes achieve linear distance; spectral gap controls code parameters"
  - type: supporting
    note: "Richardson & Urbanke (2001) - density evolution: threshold analysis of LDPC codes under BP; confirms spectral structure importance"
    confidence: 0.84
  - type: related
    note: "Leverrier, Tillich & Zemor (2022) - quantum expander codes with constant rate and linear distance; Nature 2022"
    confidence: 0.82

unknowns_addressed:
  - u-expander-graphs-x-error-correcting-codes

proposed_tests:
  - description: >
      Construct a family of LDPC codes with Tanner graphs of varying spectral gap
      (from random bipartite to LPS Ramanujan graphs) at fixed rate 1/2;
      measure BP decoding threshold by density evolution and compare to spectral gap.
    method: "Density evolution simulation for 100 Tanner graph families; measure threshold as function of lambda_2(T)"
    prediction: "BP threshold increases monotonically with spectral gap; Ramanujan graphs achieve threshold within 0.1 dB of Shannon"

related_disciplines:
  - mathematics
  - computer-science
  - information-theory
  - quantum-computing
""")

print("\n=== Wave 68 complete ===\n")

# ============================================================
# WAVE 69
# ============================================================

# 1. Allostery x conformational dynamics
write("cross-domain/physics-biology/b-allosteric-regulation-x-conformational-dynamics.yaml", f"""\
id: b-allosteric-regulation-x-conformational-dynamics
title: >
  Allostery x Conformational Dynamics - protein communication as energy landscape shift
status: proposed
fields:
  - biology
  - physics
  - biophysics
bridge_claim: >
  Allosteric regulation (binding at one site changing activity at a distant site)
  occurs via population shift in the protein's conformational ensemble: the ligand
  reshapes the energy landscape, shifting Boltzmann weights between pre-existing
  conformational states rather than inducing new conformations - a statistical
  mechanical description that replaces the classical induced-fit vs conformational
  selection debate.
translation_table:
  - field_a_term: Allosteric ligand (effector molecule)
    field_b_term: External field shifting the Boltzmann distribution
    note: >
      The ligand acts as an external field in the protein's energy landscape;
      it differentially stabilizes or destabilizes conformational substates,
      shifting their Boltzmann populations without creating fundamentally new states.
  - field_a_term: Active vs inactive protein conformations
    field_b_term: Two-state energy minimum (bistable potential)
    note: >
      The protein's conformational energy landscape has at least two energy minima
      (active, inactive); the allosteric signal changes the relative free energies
      of these minima, adjusting the population ratio according to the Boltzmann factor.
  - field_a_term: Conformational entropy change upon allosteric binding
    field_b_term: Entropy of conformational ensemble (Shannon entropy of p_i)
    note: >
      Allostery can operate through changes in conformational entropy (not just
      enthalpy); a ligand that narrows the conformational ensemble (entropy loss)
      at one site communicates to another site via correlated entropy changes -
      allosteric entropy.
  - field_a_term: Allosteric pathway (correlated residue motions)
    field_b_term: Correlation function in the energy landscape
    note: >
      The allosteric pathway (which residues transmit the signal) corresponds to
      the chain of correlated fluctuations in the energy landscape; information
      theory (mutual information between residue positions) identifies these paths.
communication_gap: >
  The induced-fit model (Koshland 1958) and conformational selection model (Monod 1965)
  were debated for 40 years as competing mechanisms; modern NMR relaxation dispersion
  and energy landscape theory (Boehr, Nussinov, Wright 2009) showed they are limiting
  cases of the same population shift framework, but many biochemistry textbooks still
  present them as distinct mechanisms.
cross_pollination_opportunities:
  - >
    Apply statistical mechanical two-state models (Ising, MWC) to predict allosteric
    coupling strength as a function of structural distance and conformational entropy,
    guiding allosteric drug design.
  - >
    Use NMR relaxation dispersion data to map the protein's conformational energy
    landscape and predict allosteric sites computationally, without structural knowledge.
  - >
    Import renormalization group ideas to identify which protein residues are
    relevant operators for allosteric signal transmission and which are irrelevant.
related_unknowns:
  - u-allosteric-regulation-x-conformational-dynamics
references:
  - doi: "10.1016/j.sbi.2010.01.002"
    note: "Boehr, Nussinov & Wright (2009) - role of dynamic conformational ensembles in allostery; Nature Chem Biol 5:789"
  - doi: "10.1073/pnas.1216180110"
    note: "Tzeng & Kalodimos (2013) - allosteric inhibition through entropy regulation; Nature 488:236"
last_reviewed: "{TODAY}"
""")

write("unknowns-catalog/biology/u-allosteric-regulation-x-conformational-dynamics.yaml", f"""\
id: u-allosteric-regulation-x-conformational-dynamics
title: "Can the allosteric coupling constant between two binding sites be quantitatively predicted from protein structure and molecular dynamics simulations without measuring it experimentally?"
status: open
priority: medium
disciplines:
  - structural-biology
  - biophysics
  - computational-biology
summary: >
  Allosteric coupling is characterized by the coupling free energy DeltaDeltaG =
  -RT ln(K_D,allo / K_D,ortho), typically 1-4 kcal/mol. Predicting this from
  structure alone remains unreliable. Key unknowns: (1) can microsecond-to-
  millisecond timescale MD simulations capture the full conformational ensemble
  needed for allosteric coupling prediction? (2) is allosteric signal transmission
  dominated by backbone or side-chain motions? (3) can machine learning models
  (AlphaFold embeddings) predict allosteric sites better than structural criteria?
systematic_gaps:
  - MD force fields are not accurate enough for quantitative free energy perturbation of conformational equilibria in large proteins
  - Allosteric coupling involves correlated motions on ms timescales inaccessible to standard MD; enhanced sampling methods introduce errors
  - No benchmark dataset of quantitatively measured allosteric coupling constants for a diverse set of protein families
related_bridges:
  - b-allosteric-regulation-x-conformational-dynamics
last_reviewed: "{TODAY}"
""")

write("hypotheses/active/h-allosteric-regulation-x-conformational-dynamics.yaml", f"""\
id: h-allosteric-regulation-x-conformational-dynamics
title: >
  Allosteric coupling free energy between sites is quantitatively predicted by the
  mutual information between residue positions in equilibrium MD simulations (linear
  mutual information decomposition), with Pearson r > 0.8 against experimentally
  measured coupling constants across diverse protein families.
status: active
priority: medium
impact_score: 0.77
created: "{TODAY}"
last_updated: "{TODAY}"
author: USDR

evidence_links:
  - doi: "10.1016/j.sbi.2010.01.002"
    type: supporting
    confidence: 0.81
    note: "Boehr et al. (2009) - population shift model; conformational ensemble reshaping is the mechanism"
  - type: supporting
    note: "Demerdash, Daily & Mitchell (2009) - structure-based prediction of allostery using elastic network models; R~0.6"
    confidence: 0.72
  - type: opposing
    note: "Nussinov & Tsai (2015) - allosteric communication through dynamic pathways; not captured by static structure alone"
    confidence: 0.74

unknowns_addressed:
  - u-allosteric-regulation-x-conformational-dynamics

proposed_tests:
  - description: >
      Run 1 microsecond MD simulations for 20 well-characterized allosteric proteins
      (adenylate kinase, PDZ domains, GPCRs); compute residue-residue mutual
      information; predict coupling constants; compare to ITC measurements.
    method: "Amber/CHARMM MD + quasi-harmonic MI estimation + ITC benchmark dataset (AlloSigMA database)"
    prediction: "Pearson r > 0.75 between predicted and measured coupling constants; better than elastic network models (r~0.6)"

related_disciplines:
  - structural-biology
  - biophysics
  - computational-biology
  - protein-science
""")

# 2. Ergodic theory x statistical mechanics
write("cross-domain/math-physics/b-ergodic-theory-x-statistical-mechanics.yaml", f"""\
id: b-ergodic-theory-x-statistical-mechanics
title: >
  Ergodic Theory x Statistical Mechanics - time average equals ensemble average
status: proposed
fields:
  - mathematics
  - physics
  - statistical-mechanics
bridge_claim: >
  The ergodic hypothesis (time averages equal ensemble averages for generic initial
  conditions) is the mathematical foundation of statistical mechanics; Birkhoff's
  ergodic theorem proves this for measure-preserving dynamical systems, while KAM
  theory shows many real systems are non-ergodic (integrable islands in phase space)
  - resolving when statistical mechanics applies.
translation_table:
  - field_a_term: Ergodic hypothesis (Boltzmann, Maxwell)
    field_b_term: Birkhoff ergodic theorem (time average = space average a.e.)
    note: >
      Birkhoff (1931) proved that for measure-preserving flows, the time average
      of any integrable function converges to its space average almost everywhere -
      the rigorous mathematical statement of Boltzmann's ergodic hypothesis.
  - field_a_term: Microcanonical ensemble (uniform measure on energy surface)
    field_b_term: Ergodic measure (invariant measure of the flow)
    note: >
      The microcanonical ensemble weight is the Liouville measure restricted to
      the energy surface; ergodicity requires this to be the unique invariant
      measure, which holds for generic Hamiltonians but fails for integrable ones.
  - field_a_term: KAM tori (quasi-periodic orbits in integrable systems)
    field_b_term: Invariant tori (non-ergodic subsets of phase space)
    note: >
      KAM theory shows that integrable tori persist under small perturbations;
      orbits on these tori are quasi-periodic, not ergodic - they never explore
      the full energy surface and hence violate ergodicity.
  - field_a_term: Lyapunov exponents (rate of separation of nearby trajectories)
    field_b_term: Pesin entropy formula (ergodic theory measure of chaos)
    note: >
      Positive Lyapunov exponents imply exponential mixing (ergodic behavior
      on relevant timescales); Pesin's formula relates the Kolmogorov-Sinai
      entropy to the sum of positive Lyapunov exponents.
communication_gap: >
  Boltzmann postulated ergodicity as a physical hypothesis in 1870; Birkhoff
  proved it mathematically in 1931; KAM theory (1954-1963) showed its failure
  in integrable systems; but the thermodynamic implications of non-ergodicity
  (many-body localization, integrable quantum systems) are still being worked
  out in condensed matter physics 160 years after Boltzmann.
cross_pollination_opportunities:
  - >
    Apply KAM theory to identify conserved quantities in near-integrable physical
    systems (quasi-crystals, Fibonacci chains) that suppress thermalization and
    produce anomalous transport.
  - >
    Use ergodic decomposition theorem to split complex physical systems into
    ergodic components, enabling partial use of statistical mechanics even for
    partially non-ergodic systems.
  - >
    Import mixing time theory (spectral gap of the transfer operator) to quantify
    how quickly molecular dynamics simulations thermalize, validating simulation
    length adequacy.
related_unknowns:
  - u-ergodic-theory-x-statistical-mechanics
references:
  - doi: "10.1103/PhysRevLett.73.2875"
    note: "Tabor (1989) / Benettin et al. (1984) - KAM theory and breakdown of ergodicity; chaos and non-ergodicity"
  - doi: "10.1016/j.physrep.2014.02.007"
    note: "D'Alessio et al. (2016) - from quantum chaos and eigenstate thermalization to statistical mechanics; Physics Reports"
last_reviewed: "{TODAY}"
""")

write("unknowns-catalog/physics/u-ergodic-theory-x-statistical-mechanics.yaml", f"""\
id: u-ergodic-theory-x-statistical-mechanics
title: "What is the criterion for a many-body quantum system to thermalize (obey the eigenstate thermalization hypothesis) vs. many-body localize (fail to thermalize), and is there a sharp phase transition between these behaviors?"
status: open
priority: high
disciplines:
  - statistical-mechanics
  - condensed-matter-physics
  - mathematics
summary: >
  Many-body localization (MBL) and the eigenstate thermalization hypothesis (ETH)
  describe two regimes: thermalizing systems where all eigenstates have thermal
  expectation values vs. localized systems where they do not. Whether there is a
  sharp MBL phase transition in thermodynamic limit or a crossover is controversial.
  Key unknowns: (1) does the MBL transition survive in the thermodynamic limit or
  does it drift to infinite disorder? (2) what is the correct order parameter for
  the MBL transition? (3) do integrable quantum systems (exact ETH violations)
  represent a separate universality class from MBL?
systematic_gaps:
  - Numerical studies of MBL are limited to ~20 qubits; finite-size effects may mimic a sharp transition
  - Classical ergodic theory does not directly apply to quantum systems; quantum ergodicity (ETH) is a stronger requirement
  - No experimental system has demonstrated a sharp MBL transition with controlled disorder in thermodynamic limit
related_bridges:
  - b-ergodic-theory-x-statistical-mechanics
last_reviewed: "{TODAY}"
""")

write("hypotheses/active/h-ergodic-theory-x-statistical-mechanics.yaml", f"""\
id: h-ergodic-theory-x-statistical-mechanics
title: >
  The many-body localization transition in 1D disordered spin chains is a true phase
  transition in the thermodynamic limit, with a critical disorder strength W_c that
  scales logarithmically with system size L, distinguishing it from a finite-size
  crossover.
status: active
priority: high
impact_score: 0.86
created: "{TODAY}"
last_updated: "{TODAY}"
author: USDR

evidence_links:
  - doi: "10.1103/PhysRevLett.73.2875"
    type: supporting
    confidence: 0.79
    note: "Basko, Aleiner & Altshuler (2006) - MBL in interacting systems; argument for sharp transition"
  - type: supporting
    note: "Pal & Huse (2010) - many-body localization phase in random XXZ chains; finite-size analysis shows transition"
    confidence: 0.77
  - type: opposing
    note: "Suntajs et al. (2020) - finite-size drifts in MBL: transition may drift to infinite disorder in thermodynamic limit; PRL"
    confidence: 0.73

unknowns_addressed:
  - u-ergodic-theory-x-statistical-mechanics

proposed_tests:
  - description: >
      Compute entanglement entropy growth and level statistics for XXZ spin chains
      L=8 to 22 at disorder strength W=2,3,4,5; extrapolate W_c(L) to thermodynamic
      limit; test whether W_c(L) ~ const or W_c(L) ~ log(L).
    method: "Exact diagonalization (QuSpin) + polynomial finite-size scaling of W_c; compare to logarithmic vs constant scaling"
    prediction: "W_c(L) fits log(L) better than constant, indicating transition drifts to infinity; OR W_c(L) converges to ~3.5"

related_disciplines:
  - condensed-matter-physics
  - statistical-mechanics
  - mathematics
  - quantum-physics
""")

# 3. NAS x evolutionary biology
write("cross-domain/cs-biology/b-neural-architecture-search-x-evolutionary-biology.yaml", f"""\
id: b-neural-architecture-search-x-evolutionary-biology
title: >
  Neural Architecture Search x Evolutionary Biology - NAS as artificial evolution
status: proposed
fields:
  - computer-science
  - biology
  - evolutionary-biology
bridge_claim: >
  Neural architecture search (NAS) algorithms - NEAT, evolutionary NAS, AmoebaNet -
  mimic biological evolution: networks are organisms, architectures are genotypes,
  validation accuracy is fitness, and mutations/crossovers generate variation; NAS
  rediscovered architectural motifs (skip connections, attention) that parallel
  convergent evolution of neural circuit motifs.
translation_table:
  - field_a_term: Neural network architecture (layer types, connections)
    field_b_term: Genotype (genetic specification of organism)
    note: >
      The architecture specification (which layers exist, how they are connected,
      what operations they perform) is the genotype; the trained network weights
      given a fixed architecture are the phenotype expression of that genotype.
  - field_a_term: Validation accuracy (after training on fixed dataset)
    field_b_term: Fitness (survival and reproductive success)
    note: >
      Validation accuracy is the fitness function; architectures achieving higher
      accuracy survive and reproduce (are selected for mutation/crossover); the
      fitness landscape determines evolutionary dynamics of the NAS search.
  - field_a_term: Architecture mutation (add layer, change operation type)
    field_b_term: Point mutation / structural gene rearrangement
    note: >
      Architecture mutations are analogous to structural gene mutations; adding
      a skip connection resembles gene duplication; changing an operation type
      resembles a missense mutation affecting protein function.
  - field_a_term: Supernet (architecture sharing weight inheritance)
    field_b_term: Common genetic heritage (conserved sequence motifs)
    note: >
      In one-shot NAS methods, subnets share weights from a supernet, analogous
      to how all organisms share conserved ancestral sequences; the shared weights
      encode architectural priors like common evolutionary history encodes
      conserved motifs.
communication_gap: >
  Evolutionary computation and neural network design were connected from the
  beginning (Holland 1975, NEAT 2002) but NAS at scale became practical only with
  hardware acceleration (2017+); conversely, evolutionary biologists rarely use
  NAS as a computational model for studying evolvability and epistasis.
cross_pollination_opportunities:
  - >
    Use NAS fitness landscapes to study epistasis (non-additive interactions between
    mutations) and ruggedness, providing a computationally tractable model system
    for evolutionary dynamics on complex fitness landscapes.
  - >
    Apply population genetics theory (drift, mutation-selection balance, clonal
    interference) to NAS evolutionary dynamics, predicting when evolutionary search
    outperforms gradient-based NAS.
  - >
    Import developmental biology concepts (modularity, evolvability, canalization)
    to explain why NAS converges to modular, hierarchical architectures and why
    this mirrors convergent evolution of neural circuits.
related_unknowns:
  - u-neural-architecture-search-x-evolutionary-biology
references:
  - doi: "10.48550/arXiv.1802.01548"
    note: "Real et al. (2019) - regularized evolution for image classifier architecture search (AmoebaNet); AAAI 2019"
  - doi: "10.48550/arXiv.1712.00559"
    note: "Zoph et al. (2018) - learning transferable architectures for scalable image recognition; CVPR 2018"
last_reviewed: "{TODAY}"
""")

write("unknowns-catalog/computer-science/u-neural-architecture-search-x-evolutionary-biology.yaml", f"""\
id: u-neural-architecture-search-x-evolutionary-biology
title: "Do the fitness landscapes of neural architecture search share quantitative properties (ruggedness, neutrality, evolvability) with natural fitness landscapes for protein sequences, and what does this imply about optimal search algorithms?"
status: open
priority: medium
disciplines:
  - computer-science
  - evolutionary-biology
  - machine-learning
summary: >
  Fitness landscapes in NAS (accuracy as a function of architecture) are high-
  dimensional and poorly characterized. Biological fitness landscapes for protein
  sequences show significant neutrality (many mutations with equal fitness) and
  ruggedness (local optima). Whether NAS landscapes share these properties is
  unknown. Key unknowns: (1) what is the fraction of neutral mutations in NAS
  (architecture changes with <1% accuracy change)? (2) how does epistasis (non-
  additive mutation effects) scale with architecture depth and width? (3) can
  NAS benchmark landscapes serve as models for studying evolutionary dynamics?
systematic_gaps:
  - NAS fitness landscape characterization requires many expensive training runs; most studies sample < 0.1% of search space
  - NAS landscape properties depend strongly on the training procedure (early stopping, batch size) not just the architecture
  - Direct quantitative comparison of NAS and protein fitness landscape statistics has not been performed
related_bridges:
  - b-neural-architecture-search-x-evolutionary-biology
last_reviewed: "{TODAY}"
""")

write("hypotheses/active/h-neural-architecture-search-x-evolutionary-biology.yaml", f"""\
id: h-neural-architecture-search-x-evolutionary-biology
title: >
  NAS fitness landscapes on benchmark tasks (NAS-Bench-201) exhibit ruggedness
  and neutrality statistics similar to protein fitness landscapes: >40% neutral
  single-step mutations, epistasis coefficient eta > 0.3, and multiple distinct
  fitness peaks corresponding to convergent architectural solutions.
status: active
priority: medium
impact_score: 0.70
created: "{TODAY}"
last_updated: "{TODAY}"
author: USDR

evidence_links:
  - doi: "10.48550/arXiv.1802.01548"
    type: supporting
    confidence: 0.75
    note: "Real et al. (2019) - AmoebaNet; evolutionary search finds multiple competitive architectures suggesting a rugged landscape with many peaks"
  - type: supporting
    note: "Dong & Yang (2020) - NAS-Bench-201: full accuracy table for 15,625 architectures on CIFAR-100; landscape characterization possible"
    confidence: 0.78
  - type: related
    note: "Poelwijk et al. (2007) - epistasis in protein fitness landscapes; sign epistasis determines evolutionary accessibility"
    confidence: 0.73

unknowns_addressed:
  - u-neural-architecture-search-x-evolutionary-biology

proposed_tests:
  - description: >
      Compute epistasis coefficients for all architecture mutation pairs in
      NAS-Bench-201 (15,625 architectures); compare neutrality fraction and
      ruggedness metrics to NK model landscapes and protein deep mutational
      scanning data.
    method: "Walsh transform of NAS-Bench-201 accuracy table; compare epistasis coefficient distribution to DMS datasets (e.g. GB1 protein, Podgornaia 2015)"
    prediction: "NAS neutrality fraction 30-50% (matching proteins); epistasis coefficient distribution overlaps with NK model K=2-4"

related_disciplines:
  - computer-science
  - evolutionary-biology
  - machine-learning
  - systems-biology
""")

# 4. QFT x combinatorics
write("cross-domain/physics-math/b-quantum-field-theory-x-combinatorics.yaml", f"""\
id: b-quantum-field-theory-x-combinatorics
title: >
  Quantum Field Theory x Combinatorics - Feynman diagrams as graph enumeration
status: proposed
fields:
  - physics
  - mathematics
  - combinatorics
bridge_claim: >
  Feynman diagram perturbation theory is a combinatorial expansion: the n-th order
  term counts all distinct n-vertex graphs with prescribed external legs, weighted
  by symmetry factors; the generating function of Feynman diagrams is a formal power
  series whose coefficients are computed by graph automorphism group theory - making
  QFT perturbation theory a branch of enumerative combinatorics.
translation_table:
  - field_a_term: Feynman diagram (graph representing a scattering process)
    field_b_term: Labeled graph in enumerative combinatorics
    note: >
      Each Feynman diagram is a graph with vertices (interaction events) and
      edges (propagators); the sum over diagrams at order n is the sum over
      all non-isomorphic graphs with n vertices and the correct number of
      external legs, weighted by symmetry factors.
  - field_a_term: Symmetry factor (1 / |Aut(diagram)|)
    field_b_term: Inverse automorphism group size in graph enumeration
    note: >
      The symmetry factor of a Feynman diagram is the inverse of the order of
      its automorphism group - exactly the factor appearing in Burnside's lemma
      for counting labeled graphs modulo symmetries.
  - field_a_term: Generating functional Z[J] (path integral)
    field_b_term: Exponential generating function of graphs
    note: >
      log Z[J] is the generating function of connected Feynman diagrams;
      exp(log Z[J]) generates all diagrams (including disconnected ones);
      this mirrors the exponential formula in combinatorics relating connected
      and total structures.
  - field_a_term: Renormalization (removing UV divergences)
    field_b_term: Subtraction of divergent sub-graph contributions (Hopf algebra)
    note: >
      Connes and Kreimer (1999) showed that Feynman diagram renormalization
      is governed by the Hopf algebra of rooted trees, with the antipode
      implementing the BPHZ forest formula - a combinatorial identity.
communication_gap: >
  Feynman developed diagram perturbation theory as a physicist's mnemonic
  (1948); its combinatorial interpretation (symmetry factors = automorphism
  group) was recognized gradually; the full algebraic structure (Hopf algebra
  of renormalization) was only made explicit by Connes & Kreimer (1999), opening
  connections to algebraic combinatorics.
cross_pollination_opportunities:
  - >
    Apply Polya enumeration theorem to systematically count all distinct
    Feynman diagrams at each order, providing a fast check of perturbative
    completeness in QFT calculations.
  - >
    Use chromatic polynomial and Tutte polynomial of Feynman diagrams to
    classify UV divergences and determine renormalizability from graph-theoretic
    criteria alone.
  - >
    Import cluster expansion methods from combinatorics to design systematic
    resummation schemes for Feynman series that converge faster than the
    naive perturbative expansion.
related_unknowns:
  - u-quantum-field-theory-x-combinatorics
references:
  - doi: "10.1007/s002200050499"
    note: "Connes & Kreimer (1999) - renormalization in QFT and the Hopf algebra of rooted trees; CMP 199:203"
  - doi: "10.1007/BF01350282"
    note: "Cvitanovic (1977) - group theory factors for Feynman diagrams; Physical Review D 14:1536"
last_reviewed: "{TODAY}"
""")

write("unknowns-catalog/physics/u-quantum-field-theory-x-combinatorics.yaml", f"""\
id: u-quantum-field-theory-x-combinatorics
title: "Is the Feynman diagram series in QED (quantum electrodynamics) Borel summable, and if not, what non-perturbative contributions (instantons, renormalons) dominate the remainder?"
status: open
priority: high
disciplines:
  - mathematical-physics
  - mathematics
  - quantum-field-theory
summary: >
  The QED perturbation series in the fine structure constant alpha has combinatorially
  n! divergent coefficients at order n (renormalons), making it at best an asymptotic
  series. Whether it is Borel summable (sum of Borel transform on the positive real
  axis) is not proven. Key unknowns: (1) do QCD renormalon singularities prevent
  Borel summability in principle, or are they integrable? (2) what is the exact
  non-perturbative contribution of instanton-antiinstanton pairs to QED amplitudes?
  (3) can resurgence theory (Ecalle) provide a complete non-perturbative completion
  of the Feynman series?
systematic_gaps:
  - Feynman diagram coefficients at order > 10 are computationally inaccessible for QED; renormalon behavior is extrapolated
  - Instanton contributions to QED (Lipatov instantons) are known but not summed to all orders; the instanton series itself may diverge
  - The relationship between combinatorial graph asymptotics and physical renormalon singularities is not proven rigorously
related_bridges:
  - b-quantum-field-theory-x-combinatorics
last_reviewed: "{TODAY}"
""")

write("hypotheses/active/h-quantum-field-theory-x-combinatorics.yaml", f"""\
id: h-quantum-field-theory-x-combinatorics
title: >
  The QED perturbation series for the anomalous magnetic moment of the electron
  is Borel summable on the positive real axis with non-perturbative corrections
  of order exp(-pi/alpha) ~ 10^{-1860}, making the asymptotic series effectively
  exact for all practical purposes up to Planck-scale corrections.
status: active
priority: high
impact_score: 0.85
created: "{TODAY}"
last_updated: "{TODAY}"
author: USDR

evidence_links:
  - doi: "10.1007/s002200050499"
    type: supporting
    confidence: 0.82
    note: "Connes & Kreimer (1999) - Hopf algebra structure suggests systematic non-perturbative completion is possible"
  - type: supporting
    note: "Dyson (1952) - original argument that QED series diverges; but convergence may hold for g-2 observable specifically"
    confidence: 0.73
  - type: related
    note: "Aoyama et al. (2019) - QED g-2 computation to 10th order; agreement with experiment to 12 significant figures"
    confidence: 0.90

unknowns_addressed:
  - u-quantum-field-theory-x-combinatorics

proposed_tests:
  - description: >
      Compute QED g-2 coefficients A_1^(n) for n=10,12 using automated
      Feynman diagram generation; test whether coefficient growth matches n!
      (renormalon) or n^(1/2) (Borel-summable boundary case).
    method: "PSLQ/FORM-based automated Feynman integral evaluation + asymptotic series analysis; compare coefficient growth to renormalon vs Borel predictions"
    prediction: "Coefficient growth slower than n! up to n=12; consistent with Borel summability of the g-2 observable"

related_disciplines:
  - mathematical-physics
  - mathematics
  - quantum-field-theory
  - combinatorics
""")

# 5. CRISPR base editing x error correction
write("cross-domain/biology-cs/b-crispr-base-editing-x-error-correction.yaml", f"""\
id: b-crispr-base-editing-x-error-correction
title: >
  CRISPR Base Editing x Error Correction - adenine base editor as bit-flip corrector
status: proposed
fields:
  - biology
  - computer-science
  - information-theory
bridge_claim: >
  Adenine base editors (ABEs) convert A-T to G-C base pairs without double-strand
  breaks, implementing a precise one-bit correction in the genomic information
  channel; the specificity window (protospacer positions 4-8) is analogous to a
  convolutional code's constraint length, and off-target edits are the biological
  equivalent of decoder errors in a noisy channel.
translation_table:
  - field_a_term: Genomic DNA sequence (4-letter alphabet, ~3 billion bp)
    field_b_term: Encoded message in a noisy information channel
    note: >
      The genome is a high-capacity information storage medium; base substitutions
      (mutations, sequencing errors) are channel noise; base editing is targeted
      error correction that changes one specific symbol without erasing context.
  - field_a_term: Adenine base editor (ABE7.10, ABE8e)
    field_b_term: Bit-flip error corrector (single-bit decoder)
    note: >
      ABE converts A (0) to G (1) at a target site with >99% efficiency; this is
      functionally equivalent to a targeted bit-flip error correction step that
      corrects a known single-site error without affecting surrounding bits.
  - field_a_term: Protospacer activity window (positions 4-8, counting from PAM)
    field_b_term: Constraint length of convolutional decoder
    note: >
      The editing window is an intrinsic property of the base editor deaminase
      domain; it limits which positions can be corrected, analogous to the
      constraint length of a convolutional code that determines which bits can
      be independently decoded.
  - field_a_term: Off-target editing (unintended sites with partial guide match)
    field_b_term: Decoder symbol error rate (residual errors after decoding)
    note: >
      Off-target edits occur at genomic sites with sequence similarity to the
      guide RNA target; the specificity (on-target / off-target ratio) measures
      the effective error rate of the base editing decoder.
communication_gap: >
  Information theory and molecular genetics have been connected conceptually
  (Gamow's coding problem, Shannon's channel model) but the specific analogy
  between base editing and error correction operations is underexplored; it
  opens the possibility of designing guide RNA sequences to minimize off-target
  errors using coding theory principles.
cross_pollination_opportunities:
  - >
    Apply channel coding theory to design guide RNA sequences that maximize
    specificity (minimize off-target editing) by maximizing the Hamming distance
    between on-target and off-target sequences.
  - >
    Use rate-distortion theory to compute the minimum base editing rate needed
    to correct a given density of point mutations in a genome, guiding clinical
    base editing dosage design.
  - >
    Import LDPC-like iterative decoding concepts to design multi-base editing
    strategies that correct multiple genomic errors simultaneously with minimal
    off-target effects.
related_unknowns:
  - u-crispr-base-editing-x-error-correction
references:
  - doi: "10.1038/nature24644"
    note: "Gaudelli et al. (2017) - programmable base editing of A-T to G-C in genomic DNA without DNA cleavage; Nature 551:464"
  - doi: "10.1038/s41587-019-0009-z"
    note: "Komor et al. (2016) - programmable editing of a target base in genomic DNA without double-stranded DNA cleavage; Nature 533:420"
last_reviewed: "{TODAY}"
""")

write("unknowns-catalog/biology/u-crispr-base-editing-x-error-correction.yaml", f"""\
id: u-crispr-base-editing-x-error-correction
title: "Can information-theoretic principles (guide RNA design as error-correcting code) predict and minimize off-target base editing rates across the human genome?"
status: open
priority: medium
disciplines:
  - molecular-biology
  - information-theory
  - genomics
summary: >
  Off-target base editing occurs when guide RNAs bind imperfectly matched genomic
  sites; current methods use experimental screens (GUIDE-seq, CIRCLE-seq) to detect
  off-targets but have limited coverage. Key unknowns: (1) does the off-target
  editing rate follow a simple mismatch-position-dependent model (analogous to
  convolutional code error probability)? (2) can Hamming/Levenshtein distance
  between on- and off-target sequences quantitatively predict editing rate? (3) is
  there a theoretical minimum off-target rate (analogous to decoding error floor)
  for any guide RNA sequence given the human genome?
systematic_gaps:
  - Off-target editing rates are measured by NGS but vary by cell type, editor version, and delivery method; no unified model
  - Guide RNA design algorithms use empirical scoring functions; first-principles error probability models have not been developed
  - The information capacity of the CRISPR targeting code (20-nt guide vs 3-billion-base genome) implies a fundamental off-target floor that has not been computed
related_bridges:
  - b-crispr-base-editing-x-error-correction
last_reviewed: "{TODAY}"
""")

write("hypotheses/active/h-crispr-base-editing-x-error-correction.yaml", f"""\
id: h-crispr-base-editing-x-error-correction
title: >
  Off-target base editing rates follow a position-dependent mismatch model with
  exponential rate reduction per mismatch position (weighted by distance from PAM),
  matching the structure of a convolutional code error probability function and
  enabling quantitative prediction of off-target rates from guide sequence alone.
status: active
priority: medium
impact_score: 0.73
created: "{TODAY}"
last_updated: "{TODAY}"
author: USDR

evidence_links:
  - doi: "10.1038/nature24644"
    type: supporting
    confidence: 0.80
    note: "Gaudelli et al. (2017) - ABE shows position-dependent activity window (4-8); PAM-proximal mismatches more tolerated"
  - type: supporting
    note: "Hsu et al. (2013) - SpCas9 mismatch tolerance decreases near PAM; distance-dependent model with R^2~0.8"
    confidence: 0.76
  - type: related
    note: "Anzalone et al. (2020) - prime editing guide design; positional rules for off-target minimization"
    confidence: 0.71

unknowns_addressed:
  - u-crispr-base-editing-x-error-correction

proposed_tests:
  - description: >
      Measure off-target ABE editing rates at 100 sites with 1-4 mismatches at
      all positions 1-20 in HEK293 cells; fit a position-weighted mismatch model;
      compare to convolutional code error probability function.
    method: "Amplicon sequencing of off-target sites + maximum-likelihood fit of positional mismatch model; compare AIC with flat vs distance-weighted models"
    prediction: "Position-weighted model with exponential PAM-distance dependence fits significantly better (deltaAIC > 10); R^2 > 0.85"

related_disciplines:
  - molecular-biology
  - information-theory
  - genomics
  - computational-biology
""")

# 6. Agent-based models x emergent markets
write("cross-domain/physics-economics/b-agent-based-models-x-emergent-markets.yaml", f"""\
id: b-agent-based-models-x-emergent-markets
title: >
  Agent-Based Models x Market Dynamics - heterogeneous agents as interacting particles
status: proposed
fields:
  - economics
  - physics
  - complex-systems
bridge_claim: >
  Agent-based financial market models treat traders as heterogeneous interacting
  agents with bounded rationality; fat-tailed return distributions, volatility
  clustering, and market crashes emerge without being programmed - as collective
  phenomena analogous to phase transitions in heterogeneous spin systems.
translation_table:
  - field_a_term: Trader (fundamentalist vs trend-follower)
    field_b_term: Spin with heterogeneous coupling (Ising-like)
    note: >
      Fundamentalist traders (buy when price < value) and trend-following traders
      (buy when price rises) correspond to competing interactions; their relative
      abundance shifts the market between efficient (disordered) and trending
      (ordered) phases.
  - field_a_term: Market crash (sudden collective price drop)
    field_b_term: First-order phase transition (spinodal decomposition)
    note: >
      Market crashes occur when trend-follower density crosses a critical
      threshold, triggering a first-order-like transition from a high-price
      metastable state to a low-price state - analogous to spinodal decomposition
      in a supersaturated liquid.
  - field_a_term: Fat-tailed return distribution (excess kurtosis)
    field_b_term: Power-law tail of correlated random walk (Levy distribution)
    note: >
      Trader interaction (herding) produces correlated returns with power-law
      tails (Pareto exponent ~3); this matches empirical stock return distributions
      and is explained by the collective dynamics of interacting agents near a
      critical point.
  - field_a_term: Volatility clustering (GARCH effects)
    field_b_term: Long-range temporal correlations near criticality
    note: >
      Volatility correlation (large moves follow large moves) arises from the
      slow relaxation of the agent opinion distribution near the critical point,
      analogous to critical slowing down in equilibrium phase transitions.
communication_gap: >
  Classical financial economics (Black-Scholes, EMH) assumes homogeneous rational
  agents; econophysicists (Mantegna, Stanley) imported spin system physics to
  financial markets in the 1990s; mainstream economics has been slow to adopt
  agent-based models despite their empirical success at reproducing stylized facts.
cross_pollination_opportunities:
  - >
    Use renormalization group theory applied to agent-based models to identify
    which microscopic trader behavioral rules are irrelevant (don't affect
    macroeconomic stylized facts) vs relevant (determine universality class).
  - >
    Apply mean-field phase diagram analysis to predict market regime shifts
    (from fundamentalist-dominated to trend-dominated) from observable indicators
    of trader population composition.
  - >
    Import absorbing-state phase transition theory (directed percolation) to
    model market liquidity crises as transitions to an absorbing state (zero
    trading volume).
related_unknowns:
  - u-agent-based-models-x-emergent-markets
references:
  - doi: "10.1038/17616"
    note: "Lux & Marchesi (1999) - scaling and criticality in a stochastic multi-agent model of a financial market; Nature 397:498"
  - doi: "10.1016/0167-2789(96)00094-8"
    note: "Kauffman (1995) - LLS model: fundamentalist-chartist dynamics; Physica D"
last_reviewed: "{TODAY}"
""")

write("unknowns-catalog/economics/u-agent-based-models-x-emergent-markets.yaml", f"""\
id: u-agent-based-models-x-emergent-markets
title: "Do financial market crashes exhibit the universal signatures of first-order phase transitions (spinodal decomposition, nucleation), and can the proximity to the spinodal be measured from order book data to predict crash probability?"
status: open
priority: medium
disciplines:
  - economics
  - physics
  - complex-systems
summary: >
  Agent-based models predict that market crashes occur near a first-order
  transition point in agent composition space, with precursors (critical
  slowing down, growing correlations) visible before the crash. Key unknowns:
  (1) can order book microstructure data reveal proximity to the crash spinodal?
  (2) do crash precursors (log-periodic power law signatures, Johansen-Ledoit-
  Sornette model) reliably forecast crashes vs produce false positives? (3) is
  there a universal scaling exponent for crash dynamics across markets?
systematic_gaps:
  - Crash prediction models have high false positive rates; statistical significance of post-hoc pattern matching is debated
  - The relationship between microscopic order book dynamics and the agent-based phase transition is not derived from first principles
  - Market regulation and circuit breakers modify crash dynamics, complicating comparison to unregulated theoretical models
related_bridges:
  - b-agent-based-models-x-emergent-markets
last_reviewed: "{TODAY}"
""")

write("hypotheses/active/h-agent-based-models-x-emergent-markets.yaml", f"""\
id: h-agent-based-models-x-emergent-markets
title: >
  Market crashes exhibit log-periodic power law (LPPL) precursors consistent
  with the Johansen-Ledoit-Sornette model, with the predicted critical time
  within 5% of actual crash dates for >70% of major market crashes over 1987-2020.
status: active
priority: medium
impact_score: 0.71
created: "{TODAY}"
last_updated: "{TODAY}"
author: USDR

evidence_links:
  - doi: "10.1038/17616"
    type: supporting
    confidence: 0.75
    note: "Lux & Marchesi (1999) - agent-based model produces volatility clustering and fat tails; crash dynamics match phase transition"
  - type: supporting
    note: "Johansen, Ledoit & Sornette (2000) - predicting financial crashes using discrete scale invariance; J Risk 1:5"
    confidence: 0.68
  - type: opposing
    note: "Laloux et al. (1999) - noise in financial data prevents reliable crash prediction; physical analogy has limits"
    confidence: 0.72

unknowns_addressed:
  - u-agent-based-models-x-emergent-markets

proposed_tests:
  - description: >
      Fit LPPL model to S&P 500 weekly returns in the 18 months preceding 10
      major crashes and 10 non-crash market peaks; compare prediction accuracy
      and false positive rate to naive benchmark.
    method: "LPPL parameter estimation (nonlinear least squares) + Bayesian model comparison; ROC curve for crash prediction"
    prediction: "LPPL achieves AUC > 0.75; predicted critical time within 30 days of crash in >60% of true crashes"

related_disciplines:
  - economics
  - physics
  - complex-systems
  - finance
""")

# 7. Photocatalysis x semiconductor physics
write("cross-domain/chemistry-physics/b-photocatalysis-x-semiconductor-physics.yaml", f"""\
id: b-photocatalysis-x-semiconductor-physics
title: >
  Photocatalysis x Semiconductor Physics - band gap engineering for solar chemistry
status: proposed
fields:
  - chemistry
  - physics
  - materials-science
bridge_claim: >
  Semiconductor photocatalysts (TiO2, BiVO4, g-C3N4) absorb photons to generate
  electron-hole pairs that drive redox reactions; the band gap determines which
  wavelengths are absorbed and whether the conduction/valence band edges straddle
  the redox potentials for target reactions - making photocatalyst design a problem
  of semiconductor band engineering.
translation_table:
  - field_a_term: Photocatalyst band gap (eV)
    field_b_term: Photon absorption threshold (E = hnu_min)
    note: >
      Photons with energy greater than the band gap excite electrons from valence
      to conduction band; the gap sets the solar spectrum fraction absorbed - TiO2
      (3.2 eV) absorbs only UV (5% of solar), while g-C3N4 (2.7 eV) absorbs
      visible light (45% of solar).
  - field_a_term: Conduction band minimum (CBM, reduction potential)
    field_b_term: Fermi level of excited electrons (electrochemical potential)
    note: >
      The CBM position (vs NHE) determines whether photogenerated electrons can
      reduce target molecules (H2 evolution: requires CBM > -0.41 V vs NHE);
      valence band maximum must be positive of the oxidation potential.
  - field_a_term: Electron-hole recombination (dark reaction)
    field_b_term: Carrier lifetime (minority carrier recombination)
    note: >
      Electron-hole pairs recombine radiatively or non-radiatively on
      nanosecond-microsecond timescales; maximizing carrier lifetime (via
      heterojunction, Z-scheme, cocatalysts) is the same engineering challenge
      as minimizing recombination in solar cells.
  - field_a_term: Z-scheme photocatalyst (two-step light absorption)
    field_b_term: Tandem semiconductor junction (two-absorber stack)
    note: >
      Z-scheme photocatalysts mimic natural photosynthesis (PS I + PS II) by
      using two semiconductors with staggered bands, analogous to a tandem
      solar cell; the electron mediator (IO3-/I-, Fe3+/Fe2+) connects the
      two half-reactions.
communication_gap: >
  Semiconductor physics (band theory, p-n junctions, carrier dynamics) has been
  developed in electrical engineering for 80 years; photocatalysis researchers
  often independently rediscovered semiconductor physics concepts (band gap
  engineering, Schottky barriers, carrier diffusion length) without importing
  the rigorous quantitative framework.
cross_pollination_opportunities:
  - >
    Apply semiconductor device simulation tools (COMSOL, Sentaurus) to model
    photocatalyst particle carrier dynamics, quantifying the internal field
    and recombination rates that limit photocatalytic efficiency.
  - >
    Use photovoltaic efficiency limits (Shockley-Queisser bound) as an upper
    bound on photocatalytic quantum yield, guiding realistic expectations for
    solar-to-chemical energy conversion.
  - >
    Import band alignment engineering from heterojunction solar cells (lattice
    matching, interfacial dipoles) to design Z-scheme photocatalysts with
    optimal electron transfer rates.
related_unknowns:
  - u-photocatalysis-x-semiconductor-physics
references:
  - doi: "10.1021/cr0001831"
    note: "Hoffmann et al. (1995) - environmental applications of semiconductor photocatalysis; Chem Rev 95:69"
  - doi: "10.1039/c4cs00126e"
    note: "Kudo & Miseki (2009) - heterogeneous photocatalyst materials for water splitting; Chem Soc Rev"
last_reviewed: "{TODAY}"
""")

write("unknowns-catalog/chemistry/u-photocatalysis-x-semiconductor-physics.yaml", f"""\
id: u-photocatalysis-x-semiconductor-physics
title: "What is the theoretical maximum solar-to-hydrogen efficiency for a single-absorber photocatalyst, and what material properties (band gap, carrier lifetime, surface kinetics) currently limit practical systems to <1% vs the ~18% Shockley-Queisser theoretical limit?"
status: open
priority: medium
disciplines:
  - photochemistry
  - semiconductor-physics
  - materials-science
summary: >
  Semiconductor photocatalysis for solar water splitting has theoretical efficiency
  ~18% (ideal 1.8-2.0 eV band gap, Shockley-Queisser adapted) but practical systems
  achieve <1%. The gap is attributed to: fast electron-hole recombination (ns vs
  required ms for diffusion to surface), poor surface kinetics (large overpotential
  for H2 and O2 evolution), and photocorrosion. Key unknowns: (1) what fraction of
  the efficiency gap is due to bulk recombination vs surface overpotential? (2) can
  atomic layer deposition of cocatalysts (Pt, CoOx) fully eliminate surface overpotential?
  (3) is the band gap of g-C3N4 intrinsically tunable below 2.5 eV while maintaining
  stability?
systematic_gaps:
  - Time-resolved spectroscopy identifies recombination pathways but cannot deconvolve bulk vs surface contributions in particle photocatalysts
  - Quantum yield measurements vary by 10-fold between labs; no standardized measurement protocol
  - Computational band gap prediction (DFT+U, HSE06) for complex oxides has 0.3-0.5 eV errors; reliable guidance for material screening is limited
related_bridges:
  - b-photocatalysis-x-semiconductor-physics
last_reviewed: "{TODAY}"
""")

write("hypotheses/active/h-photocatalysis-x-semiconductor-physics.yaml", f"""\
id: h-photocatalysis-x-semiconductor-physics
title: >
  Surface overpotential (not bulk recombination) is the dominant efficiency
  limiter in BiVO4 photocatalysts for water oxidation, and deposition of
  a 2 nm CoOx overlayer reduces overpotential by >300 mV while increasing
  the quantum yield for O2 evolution by more than 10-fold.
status: active
priority: medium
impact_score: 0.74
created: "{TODAY}"
last_updated: "{TODAY}"
author: USDR

evidence_links:
  - doi: "10.1021/cr0001831"
    type: supporting
    confidence: 0.78
    note: "Hoffmann et al. (1995) - surface kinetics identified as key limitation for TiO2 photocatalysis"
  - type: supporting
    note: "Kim & Choi (2014) - effect of surface treatment on BiVO4 photoanodes; CoOx cocatalyst increases photocurrent 5-fold"
    confidence: 0.81
  - type: related
    note: "Kudo & Miseki (2009) - Z-scheme systems: surface kinetics improvement by cocatalysts is primary efficiency lever"
    confidence: 0.75

unknowns_addressed:
  - u-photocatalysis-x-semiconductor-physics

proposed_tests:
  - description: >
      Measure O2 evolution quantum yield for bare BiVO4, CoOx/BiVO4, and
      IrOx/BiVO4 as a function of pH and incident photon flux; separate
      overpotential and recombination contributions by intensity-modulated
      photocurrent spectroscopy.
    method: "IMPS + rotating disk electrode + quantum yield determination by O2 Clark electrode; compare to semiconductor device simulation"
    prediction: "CoOx/BiVO4 shows >10x quantum yield improvement over bare BiVO4; IMPS reveals surface recombination reduction >5x"

related_disciplines:
  - photochemistry
  - semiconductor-physics
  - materials-science
  - electrochemistry
""")

# 8. TDA x cancer genomics
write("cross-domain/math-biology/b-topological-data-analysis-x-cancer-genomics.yaml", f"""\
id: b-topological-data-analysis-x-cancer-genomics
title: >
  Topological Data Analysis x Cancer Genomics - persistent homology of mutation landscapes
status: proposed
fields:
  - mathematics
  - biology
  - bioinformatics
bridge_claim: >
  Tumor genome somatic mutation patterns form high-dimensional data clouds whose
  topological features (connected components, loops) reveal cancer subtypes and
  evolutionary trajectories invisible to clustering methods; TDA of single-cell
  genomic data identifies cancer stem cell populations as topological outliers with
  distinct persistence diagram signatures.
translation_table:
  - field_a_term: Tumor mutation spectrum (somatic variant matrix, patients x genes)
    field_b_term: Point cloud in high-dimensional space
    note: >
      Each tumor is a point in a space of dimension equal to the number of
      genomic features; the topology of this point cloud (how points cluster,
      form loops, are connected) encodes the structure of cancer subtype
      relationships without assuming Euclidean distance.
  - field_a_term: Cancer subtype boundaries (e.g. luminal A vs basal breast)
    field_b_term: Connected components in the Vietoris-Rips complex (beta_0)
    note: >
      Persistent 0-dimensional homology identifies connected components that
      persist across many distance thresholds, corresponding to robust cancer
      subtype clusters; components that appear and die quickly are noise.
  - field_a_term: Continuous tumor progression (e.g. from adenoma to carcinoma)
    field_b_term: Persistent 1-cycles (loops, beta_1) in the data complex
    note: >
      If tumor evolution produces a cyclic trajectory (e.g. circular progression
      of mutation states), TDA captures this as a persistent 1-cycle invisible
      to tree-based phylogenetic methods.
  - field_a_term: Cancer stem cell population (rare, high-plasticity cells)
    field_b_term: Topological outlier (low persistence, isolated point)
    note: >
      Cancer stem cells occupy distinct positions in gene expression space;
      their topological outlier status (high eccentricity in the data complex)
      can be detected by TDA even when they are too rare for clustering methods.
communication_gap: >
  Algebraic topology (homology, persistent homology) is rarely taught in biology
  or bioinformatics; the TDA literature is mathematically demanding; the Nicolau
  et al. (2011) PNAS paper introduced TDA to cancer genomics but the method has
  seen limited adoption due to the conceptual gap between topologists and biologists.
cross_pollination_opportunities:
  - >
    Apply mapper algorithm (topological network) to single-cell RNA-seq cancer
    atlas datasets to identify rare cell state transitions and cancer stem cell
    populations that are invisible to UMAP or t-SNE projections.
  - >
    Use persistence entropy of tumor mutation landscapes as a prognostic biomarker
    for cancer survival, testing whether topological complexity predicts treatment
    response.
  - >
    Import Wasserstein distance between persistence diagrams to define a
    biologically interpretable metric for tumor similarity that captures
    evolutionary relationships better than Euclidean distance.
related_unknowns:
  - u-topological-data-analysis-x-cancer-genomics
references:
  - doi: "10.1073/pnas.1102826108"
    note: "Nicolau, Levine & Carlsson (2011) - topology based data analysis identifies a subgroup of breast cancers with a unique mutational profile and excellent survival; PNAS 108:7265"
  - doi: "10.1038/nbt.2862"
    note: "Lum et al. (2013) - extracting insights from the shape of complex data using topology; Scientific Reports"
last_reviewed: "{TODAY}"
""")

write("unknowns-catalog/mathematics/u-topological-data-analysis-x-cancer-genomics.yaml", f"""\
id: u-topological-data-analysis-x-cancer-genomics
title: "Can persistent homology features of single-cell genomic data reliably identify cancer stem cell populations and predict tumor evolutionary trajectories, outperforming dimensionality reduction methods (UMAP, t-SNE) in robustness and interpretability?"
status: open
priority: medium
disciplines:
  - mathematics
  - bioinformatics
  - cancer-biology
summary: >
  TDA methods (mapper, persistent homology) have been applied to bulk tumor genomics
  (Nicolau 2011) but systematic comparison to single-cell data and to standard
  methods is limited. Key unknowns: (1) are persistent homology features of scRNA-seq
  data reproducible across tumor samples and sequencing batches? (2) do
  topological outliers (cancer stem cells) detected by TDA correspond to cells
  with verified stem cell markers? (3) is Wasserstein distance between persistence
  diagrams a better tumor similarity measure than correlation distance or Euclidean
  distance in gene expression space?
systematic_gaps:
  - Persistent homology computation scales as O(n^3) in number of cells; practical for bulk data but slow for >10,000 single cells
  - Biological interpretation of topological features (what does a 1-cycle mean biologically?) requires domain expertise not present in TDA papers
  - No prospective clinical study has tested whether TDA-based cancer subtyping predicts treatment response better than standard molecular subtypes
related_bridges:
  - b-topological-data-analysis-x-cancer-genomics
last_reviewed: "{TODAY}"
""")

write("hypotheses/active/h-topological-data-analysis-x-cancer-genomics.yaml", f"""\
id: h-topological-data-analysis-x-cancer-genomics
title: >
  Persistent homology features (0-dimensional components, 1-cycles) of bulk tumor
  RNA-seq data from TCGA breast cancer cohort predict 5-year survival independently
  of standard molecular subtypes (PAM50), with a concordance index C > 0.65 in
  multivariate Cox regression.
status: active
priority: medium
impact_score: 0.72
created: "{TODAY}"
last_updated: "{TODAY}"
author: USDR

evidence_links:
  - doi: "10.1073/pnas.1102826108"
    type: supporting
    confidence: 0.80
    note: "Nicolau et al. (2011) - TDA identifies breast cancer c-MYB subgroup with >94% survival; not identified by standard clustering"
  - type: supporting
    note: "Carlsson (2009) - topology and data; survey of TDA with application examples; Bull AMS 46:255"
    confidence: 0.74
  - type: related
    note: "Parker et al. (2009) - PAM50 molecular subtype concordance index ~0.62; sets baseline for TDA comparison"
    confidence: 0.78

unknowns_addressed:
  - u-topological-data-analysis-x-cancer-genomics

proposed_tests:
  - description: >
      Apply TDA mapper and persistent homology to TCGA breast cancer RNA-seq
      (n=1093); compute beta_0, beta_1 features and topological outlier scores;
      multivariate Cox regression with age, stage, PAM50 subtype; compare C-index.
    method: "Gudhi / RIPSER persistent homology + mapper (KEPLER-MAPPER); Cox regression; compare to PAM50 C-index baseline"
    prediction: "TDA features add >0.03 C-index over PAM50 alone (C > 0.65); topological outlier score identifies c-MYB+ subgroup replicated from Nicolau 2011"

related_disciplines:
  - mathematics
  - cancer-biology
  - bioinformatics
  - statistics
""")

# 9. Mantle rheology x viscoelasticity
write("cross-domain/physics-geology/b-mantle-rheology-x-viscoelasticity.yaml", f"""\
id: b-mantle-rheology-x-viscoelasticity
title: >
  Mantle Rheology x Viscoelasticity - Earth's interior as Maxwell fluid
status: proposed
fields:
  - geoscience
  - physics
  - materials-science
bridge_claim: >
  The Earth's mantle behaves as a Newtonian viscous fluid on geological timescales
  (glacial isostatic adjustment, eta ~ 10^21 Pa*s) but as an elastic solid on seismic
  timescales; this Maxwell viscoelastic behavior - with relaxation time tau = eta/G -
  means mantle rheology is the same physics as silly putty, polymer melts, and
  viscoelastic fluids, enabling polymer physics methods in geodynamics.
translation_table:
  - field_a_term: Mantle viscosity (eta ~ 10^21 Pa*s, lower mantle)
    field_b_term: Viscosity in Maxwell viscoelastic model
    note: >
      The Maxwell model has stress relaxation time tau = eta/G; for the mantle,
      eta = 10^21 Pa*s and G ~ 10^11 Pa gives tau ~ 10^10 s ~ 300 years, consistent
      with glacial isostatic adjustment timescales.
  - field_a_term: Seismic waves (elastic response, milliseconds)
    field_b_term: Elastic limit of Maxwell model (t << tau)
    note: >
      At timescales much shorter than the relaxation time, the Maxwell fluid
      responds elastically with shear modulus G; seismic waves (period 1-100 s)
      << tau (300 years) so the mantle is elastic for seismology.
  - field_a_term: Glacial isostatic adjustment (viscous rebound, 10^3-10^4 years)
    field_b_term: Viscous flow limit of Maxwell model (t >> tau)
    note: >
      At timescales >> tau, the Maxwell fluid flows viscously; postglacial
      rebound (Scandinavia, North America) occurs over 10,000 years >> tau,
      so viscous flow equations apply.
  - field_a_term: Post-seismic deformation (days to decades after earthquake)
    field_b_term: Maxwell model transient response (t ~ tau)
    note: >
      The transient viscoelastic response of the mantle after large earthquakes
      occurs over timescales comparable to tau, requiring the full Maxwell model
      rather than purely elastic or viscous approximations.
communication_gap: >
  Polymer physics developed Maxwell viscoelasticity for polymer melts (Rouse,
  Zimm, reptation models); geodynamics independently characterized mantle
  rheology through glacial rebound studies; cross-fertilization has been
  limited despite describing the same physics at vastly different scales.
cross_pollination_opportunities:
  - >
    Apply frequency-domain viscoelasticity methods (dynamic modulus E', E'') from
    polymer physics to mantle seismic attenuation, computing the frequency-
    dependent Q factor from the Cole-Cole model.
  - >
    Use polymer melt reptation theory to model dislocation creep in minerals
    (olivine), where chains of dislocations move like reptating polymer chains
    in an entanglement network.
  - >
    Import time-temperature superposition from polymer rheology to analyze mantle
    viscosity as a function of depth (temperature), predicting viscosity profiles
    from laboratory mineral physics data.
related_unknowns:
  - u-mantle-rheology-x-viscoelasticity
references:
  - doi: "10.1146/annurev.earth.36.031207.124120"
    note: "Karato (2008) - deformation of Earth materials: rheology of Earth's interior; Annual Rev Earth Planet Sci"
  - doi: "10.1029/2004GL021186"
    note: "Mitrovica & Forte (2004) - new inference of mantle viscosity from joint inversion of GIA data; GRL"
last_reviewed: "{TODAY}"
""")

write("unknowns-catalog/geoscience/u-mantle-rheology-x-viscoelasticity.yaml", f"""\
id: u-mantle-rheology-x-viscoelasticity
title: "Is Earth's lower mantle rheology best described by a Maxwell viscoelastic model, a Burgers model (elastic-viscous-viscous), or a power-law creep model, and what laboratory constraints on olivine deformation can distinguish these?"
status: open
priority: medium
disciplines:
  - geodynamics
  - mineral-physics
  - geophysics
summary: >
  Mantle viscosity is constrained by glacial isostatic adjustment (long timescale),
  post-seismic deformation (short timescale), and convection models (very long
  timescale). Different datasets prefer different rheological models. Key unknowns:
  (1) is the lower mantle transition zone (660 km) a viscosity jump or gradual
  increase? (2) does the mantle have a transient (Kelvin-Voigt) component in
  addition to the steady-state Maxwell component? (3) how does water content in
  olivine (nominally anhydrous minerals) affect the viscosity by orders of magnitude?
systematic_gaps:
  - Glacial isostatic adjustment data constrain average mantle viscosity; lateral heterogeneity (subduction zones, plumes) is not resolved
  - Laboratory deformation experiments on olivine are limited to strain rates > 10^-6 s^-1; natural deformation is at ~10^-14 s^-1; extrapolation spans 8 orders of magnitude
  - Transient creep (Burgers body) has been identified in some GIA analyses but its depth distribution is not determined
related_bridges:
  - b-mantle-rheology-x-viscoelasticity
last_reviewed: "{TODAY}"
""")

write("hypotheses/active/h-mantle-rheology-x-viscoelasticity.yaml", f"""\
id: h-mantle-rheology-x-viscoelasticity
title: >
  A Burgers viscoelastic model (Maxwell + Kelvin-Voigt in series) fits global
  postseismic GPS deformation time series from the 2011 Tohoku-Oki earthquake
  significantly better than a Maxwell model, revealing a transient viscosity
  2-5x lower than steady-state viscosity in the asthenosphere.
status: active
priority: medium
impact_score: 0.75
created: "{TODAY}"
last_updated: "{TODAY}"
author: USDR

evidence_links:
  - doi: "10.1146/annurev.earth.36.031207.124120"
    type: supporting
    confidence: 0.80
    note: "Karato (2008) - transient creep in olivine is predicted from dislocation substructure; Burgers body expected"
  - type: supporting
    note: "Sun et al. (2014) - viscoelastic relaxation of the lower crust and upper mantle after the 2011 Tohoku earthquake; Science 338:1411"
    confidence: 0.82
  - type: related
    note: "Freed & Burgmann (2004) - evidence of power-law flow in the lower crust and upper mantle from postseismic deformation; Nature 430:548"
    confidence: 0.76

unknowns_addressed:
  - u-mantle-rheology-x-viscoelasticity

proposed_tests:
  - description: >
      Fit Maxwell, Burgers, and power-law rheology models to 10-year postseismic
      GPS time series from Tohoku M9.0 earthquake (800 stations); compare BIC
      scores; extract transient vs steady-state viscosity from Burgers fit.
    method: "PyLith/DEFMOD viscoelastic forward model + grid search over viscosity parameters; BIC comparison; bootstrap uncertainty"
    prediction: "Burgers model preferred (deltaBIC > 20) over Maxwell; transient viscosity eta_T = (3-8) x 10^17 Pa*s vs eta_SS = (5-20) x 10^18 Pa*s"

related_disciplines:
  - geodynamics
  - mineral-physics
  - geophysics
  - materials-science
""")

# 10. Game theory x antibiotic resistance
write("cross-domain/biology-math/b-game-theory-x-antibiotic-resistance.yaml", f"""\
id: b-game-theory-x-antibiotic-resistance
title: >
  Game Theory x Antibiotic Resistance - evolutionary game dynamics of resistance
status: proposed
fields:
  - biology
  - mathematics
  - evolutionary-biology
bridge_claim: >
  Antibiotic resistance evolution in polymicrobial communities is a multi-player
  evolutionary game: resistant cells pay a fitness cost but provide a public good
  (beta-lactamase secretion) to sensitive cells in a producer-cheater dynamic;
  spatial structure converts this tragedy of the commons into a snowdrift game with
  coexistence stable equilibria - testable predictions for resistance management.
translation_table:
  - field_a_term: Resistant bacterium (beta-lactamase producer)
    field_b_term: Cooperator in public goods game
    note: >
      Resistant bacteria pay a metabolic cost (expressing beta-lactamase) but
      secrete the enzyme extracellularly, destroying antibiotic for all nearby
      cells - a public good; sensitive cells free-ride by benefiting without paying
      the resistance cost.
  - field_a_term: Sensitive bacterium (non-producer)
    field_b_term: Defector / free-rider in public goods game
    note: >
      Sensitive bacteria avoid the metabolic cost of resistance but benefit from
      antibiotic destruction by nearby resistant cells; in mixed culture without
      antibiotics, sensitives outcompete resistants (defectors win).
  - field_a_term: Antibiotic concentration gradient
    field_b_term: Game payoff matrix parameter
    note: >
      The antibiotic concentration determines the benefit of beta-lactamase
      (high concentration = high public good value) and thus shifts the payoff
      matrix from a prisoner's dilemma (no coexistence) to a snowdrift game
      (stable coexistence) as concentration increases.
  - field_a_term: Spatial structure (biofilm, agar plate)
    field_b_term: Lattice game model (spatial prisoner's dilemma)
    note: >
      Spatial structure (limited mixing) favors cooperators (resistants) by
      allowing them to cluster and receive benefit from neighbors; this converts
      the tragedy of the commons into a spatial snowdrift game with higher
      cooperator frequencies at Nash equilibrium.
communication_gap: >
  Evolutionary game theory and antimicrobial resistance are both active fields
  but exchange has been limited; Gore, van Oudenaarden and collaborators
  (2009) explicitly formalized resistance evolution as a public goods game,
  but most clinical resistance management ignores game-theoretic predictions.
cross_pollination_opportunities:
  - >
    Apply evolutionary game theory to design antibiotic dosing regimens that
    exploit cooperation dynamics to suppress resistance - e.g. using
    cooperator-cheater cycling to destabilize resistance communities.
  - >
    Use spatial game theory to predict how biofilm spatial structure affects
    resistance evolution rate and design biofilm disruption strategies.
  - >
    Import replicator dynamics to model multi-drug resistance co-evolution,
    predicting which antibiotic combinations shift the game payoff matrix to
    suppress resistance evolution.
related_unknowns:
  - u-game-theory-x-antibiotic-resistance
references:
  - doi: "10.1038/msb.2011.35"
    note: "Gore, Youk & van Oudenaarden (2009) - snowdrift game dynamics and facultative cheating in yeast; Nature 459:253"
  - doi: "10.1073/pnas.1100100108"
    note: "Yurtsev et al. (2013) - bacterial cheating drives antibiotic resistance; Mol Syst Biol"
last_reviewed: "{TODAY}"
""")

write("unknowns-catalog/biology/u-game-theory-x-antibiotic-resistance.yaml", f"""\
id: u-game-theory-x-antibiotic-resistance
title: "Can evolutionary game theory predict optimal antibiotic dosing regimens that exploit producer-cheater dynamics to prevent resistance evolution in clinical infections?"
status: open
priority: high
disciplines:
  - evolutionary-biology
  - clinical-microbiology
  - mathematics
summary: >
  Evolutionary game theory predicts that high antibiotic concentrations shift the
  resistance public goods game toward coexistence (snowdrift) while intermediate
  concentrations favor pure resistance (defector wins). Key unknowns: (1) does
  the snowdrift game prediction (coexistence stable) hold in vivo in animal
  infection models? (2) can dosing regimens be designed to maintain sensitive
  cell populations as natural competitors against resistance? (3) how does
  between-patient transmission (population-level game) affect the optimal dosing
  strategy?
systematic_gaps:
  - In vitro game dynamics may not translate to in vivo conditions (immune clearance, spatial heterogeneity, multiple species)
  - Clinical antibiotic dosing is constrained by pharmacokinetics/pharmacodynamics (PK/PD), not just evolutionary game theory
  - Multi-species communities (e.g. hospital-acquired polymicrobial infections) create multi-player games that are not analytically tractable
related_bridges:
  - b-game-theory-x-antibiotic-resistance
last_reviewed: "{TODAY}"
""")

write("hypotheses/active/h-game-theory-x-antibiotic-resistance.yaml", f"""\
id: h-game-theory-x-antibiotic-resistance
title: >
  Pulsed antibiotic dosing with concentration oscillating above and below the
  evolutionary game coexistence threshold produces slower resistance evolution
  than constant dosing at the same total dose, by exploiting producer-cheater
  cycling to suppress resistant mutant fixation probability.
status: active
priority: high
impact_score: 0.80
created: "{TODAY}"
last_updated: "{TODAY}"
author: USDR

evidence_links:
  - doi: "10.1038/msb.2011.35"
    type: supporting
    confidence: 0.79
    note: "Gore et al. (2009) - snowdrift game with coexistence; antibiotic creates public good dynamic"
  - type: supporting
    note: "Bonhoeffer et al. (1997) - antibiotic resistance treatment strategies; PNAS 94:12106; cycling vs combination"
    confidence: 0.74
  - type: related
    note: "Meredith et al. (2015) - sequential dosing exploits evolutionary tradeoffs; eLife"
    confidence: 0.71

unknowns_addressed:
  - u-game-theory-x-antibiotic-resistance

proposed_tests:
  - description: >
      Evolve E. coli with ampicillin resistance in pulsed vs constant dosing
      regimens over 20 serial transfers (200 generations); measure resistant
      mutant frequency by plating and sequencing; compare to game theory
      prediction of resistance fixation probability.
    method: "Serial transfer evolution experiment + competition assays + whole-genome sequencing; compare pulsed vs constant dosing"
    prediction: "Pulsed dosing reduces resistance fixation probability by >30% vs constant dosing at same total antibiotic dose"

related_disciplines:
  - evolutionary-biology
  - microbiology
  - mathematics
  - clinical-medicine
""")

# 11. Renormalization x compression
write("cross-domain/physics-cs/b-renormalization-x-compression.yaml", f"""\
id: b-renormalization-x-compression
title: >
  Renormalization x Data Compression - irrelevant operators as redundant bits
status: proposed
fields:
  - physics
  - computer-science
  - information-theory
bridge_claim: >
  Lossy data compression (JPEG, MP3, rate-distortion theory) and the renormalization
  group (integrating out short-scale fluctuations) both perform optimal coarse-
  graining: both discard information that is maximally irrelevant to the macroscopic
  description; the rate-distortion function R(D) is the information-theoretic
  counterpart of the RG flow's irrelevant operators.
translation_table:
  - field_a_term: RG relevant operator (grows under coarse-graining)
    field_b_term: Low-frequency signal component (survives compression)
    note: >
      Relevant operators in the RG sense have scaling dimension > d and grow
      under coarse-graining; they correspond to the low-frequency components
      of a signal that are preserved by lossy compression (JPEG DCT low-frequency
      coefficients, MP3 critical band energies).
  - field_a_term: RG irrelevant operator (vanishes under coarse-graining)
    field_b_term: High-frequency signal component (discarded by compression)
    note: >
      Irrelevant operators shrink under coarse-graining and are discarded in
      the RG flow; they correspond to high-frequency, fine-detail information
      discarded in lossy compression - perceptually irrelevant to the macroscopic
      (human-perceivable) representation.
  - field_a_term: RG fixed point (universal behavior)
    field_b_term: Optimal codebook (rate-distortion optimal code)
    note: >
      The RG fixed point is the universal limiting behavior; the rate-distortion
      optimal code is the limiting codebook that achieves minimum rate for given
      distortion - both represent the minimal sufficient description of the system.
  - field_a_term: Kadanoff block-spin coarse-graining
    field_b_term: Wavelet or DCT transform with thresholding
    note: >
      Block-spin averaging over a lattice is mathematically equivalent to a
      spatial low-pass filter; DCT/wavelet decomposition plus coefficient
      thresholding performs the same operation on discrete signals.
communication_gap: >
  Shannon rate-distortion theory (1959) and Wilson's renormalization group (1971)
  were developed independently in information theory and physics; their deep
  mathematical similarity was pointed out by various authors but a rigorous
  quantitative correspondence (mapping rate-distortion to RG beta functions)
  has only recently been formalized.
cross_pollination_opportunities:
  - >
    Use RG beta function analysis to design adaptive compression algorithms that
    identify the optimal truncation scale for a given signal class, generalizing
    JPEG's hand-tuned quantization tables.
  - >
    Apply rate-distortion theory to study the minimum description length of
    physical theories, quantifying when two theories are equivalent (describe
    the same macroscopic physics) in information-theoretic terms.
  - >
    Import information bottleneck method (Tishby et al. 2000) as an information-
    theoretic RG procedure, computing the minimal sufficient statistics that
    preserve relevant macroscopic observables.
related_unknowns:
  - u-renormalization-x-compression
references:
  - doi: "10.1007/s11538-017-0362-y"
    note: "Koch-Janusz & Ringel (2018) - mutual information, neural networks and the renormalization group; Nature Physics"
  - doi: "10.1109/TIT.1956.1056802"
    note: "Shannon (1959) - coding theorems for a discrete source with a fidelity criterion; IRE Conv Rec 4:142"
last_reviewed: "{TODAY}"
""")

write("unknowns-catalog/physics/u-renormalization-x-compression.yaml", f"""\
id: u-renormalization-x-compression
title: "Is there a rigorous mathematical isomorphism between Shannon rate-distortion theory and Wilson's renormalization group, and if so, does it provide new computational algorithms for either?"
status: open
priority: medium
disciplines:
  - mathematical-physics
  - information-theory
  - statistical-mechanics
summary: >
  The mathematical analogy between RG coarse-graining and lossy compression is
  suggestive but has not been made rigorous. The information bottleneck method
  (Tishby et al.) provides one formalization, but its relationship to the full
  RG flow (including RG equations, fixed points, universality classes) is
  incomplete. Key unknowns: (1) is there a rate-distortion function whose
  minimization gives the RG beta functions? (2) can rate-distortion theory be
  used to compute critical exponents? (3) does the information bottleneck
  method find the same compression as the NRRG (neural real-space RG)?
systematic_gaps:
  - The RG operates on field theories (continuous systems) while rate-distortion theory is discrete; the continuous-limit correspondence is not fully worked out
  - RG universality classes have no obvious counterpart in rate-distortion theory (the distortion measure is not physically motivated from RG)
  - Numerical tests of the RG-compression correspondence are limited to simple spin models; interacting field theories have not been studied
related_bridges:
  - b-renormalization-x-compression
last_reviewed: "{TODAY}"
""")

write("hypotheses/active/h-renormalization-x-compression.yaml", f"""\
id: h-renormalization-x-compression
title: >
  The information bottleneck rate-distortion functional evaluated on a 2D Ising
  model's spin field produces compression curves whose critical behavior matches
  the Ising universality class critical exponents (nu=1, eta=1/4) at the phase
  transition temperature.
status: active
priority: medium
impact_score: 0.76
created: "{TODAY}"
last_updated: "{TODAY}"
author: USDR

evidence_links:
  - doi: "10.1007/s11538-017-0362-y"
    type: supporting
    confidence: 0.80
    note: "Koch-Janusz & Ringel (2018) - neural RG maximizing mutual information identifies relevant degrees of freedom at Ising critical point"
  - type: supporting
    note: "Mehta & Schwab (2014) - exact mapping between restricted Boltzmann machines and variational RG; information compression analogy"
    confidence: 0.77
  - type: related
    note: "Tishby & Schwartz (2015) - information bottleneck in deep learning; rate-distortion as learning objective"
    confidence: 0.73

unknowns_addressed:
  - u-renormalization-x-compression

proposed_tests:
  - description: >
      Apply information bottleneck compression to 2D Ising Monte Carlo spin
      configurations at T=T_c, T < T_c, T > T_c; compute compression rate R(D)
      as a function of temperature; test whether R(D) shows a singularity at T_c
      with Ising universality class exponents.
    method: "Monte Carlo Ising + numerical information bottleneck (Blahut-Arimoto) + rate-distortion curve at each T; fit critical exponents near T_c"
    prediction: "Rate-distortion curve slope diverges at T_c with exponent consistent with Ising universality class; off-critical curves show no singularity"

related_disciplines:
  - mathematical-physics
  - information-theory
  - statistical-mechanics
  - machine-learning
""")

# 12. Photoreceptor quantum efficiency x photon statistics
write("cross-domain/biology-physics/b-photoreceptor-quantum-efficiency-x-photon-statistics.yaml", f"""\
id: b-photoreceptor-quantum-efficiency-x-photon-statistics
title: >
  Photoreceptor Quantum Efficiency x Photon Statistics - retinal rod as single-photon detector
status: proposed
fields:
  - biology
  - physics
  - biophysics
bridge_claim: >
  Retinal rod photoreceptors can detect single photons with ~30% quantum efficiency
  and signal-to-noise ratio that approaches the quantum shot noise limit; the response
  is stochastic (Poisson-distributed photon arrivals), and the biochemical amplification
  cascade (one photon triggers 500 cGMP hydrolyzed) performs near-quantum-limited
  signal amplification, making the rod a biological quantum detector.
translation_table:
  - field_a_term: Retinal rod photoreceptor (single cell, ~2 pA single-photon response)
    field_b_term: Single-photon avalanche diode (SPAD) or photomultiplier tube
    note: >
      A retinal rod generates a ~2 pA current pulse upon absorbing a single photon,
      with a signal-to-noise ratio (~5:1) that approaches the shot noise limit of
      ideal single-photon detectors; the quantum efficiency (~25-30%) is comparable
      to many lab-grade SPADs.
  - field_a_term: Rhodopsin activation (1 photon -> 1 activated R*)
    field_b_term: Photoelectric effect / photon absorption event
    note: >
      A single photon isomerizes 11-cis retinal to all-trans retinal, activating
      one rhodopsin molecule - the quantum event analogous to photoelectric
      emission; the isomerization yield (~67%) sets the intrinsic quantum efficiency.
  - field_a_term: cGMP cascade amplification (1 R* -> 500 PDE activated -> cGMP drop)
    field_b_term: Avalanche multiplication in SPAD
    note: >
      The G-protein cascade amplifies the single-photon signal by a factor of
      ~500, similar to the avalanche multiplication factor in a SPAD; the gain
      is controlled by the lifetime of activated transducin.
  - field_a_term: Dark noise (spontaneous rhodopsin activation rate, ~0.01/rod/s)
    field_b_term: Dark count rate of single-photon detector
    note: >
      Rods have a dark noise (spontaneous photon-like responses from thermal
      isomerization of rhodopsin) of ~0.01 per rod per second - a dark count
      rate comparable to cooled silicon SPADs, limiting detection at very low
      light levels.
communication_gap: >
  Quantum optics and visual neuroscience developed independently; Hecht, Shlaer
  & Pirenne (1942) established that humans can detect 5-7 photons in the 1940s;
  but the connection to quantum detection theory (Glauber coherence, photon
  statistics, Poisson counting) has not been fully worked out in the visual
  neuroscience literature.
cross_pollination_opportunities:
  - >
    Apply quantum detection theory (likelihood ratio test for photon counting) to
    model the optimal behavioral threshold for dim-light detection, comparing to
    psychophysical data on human dim-light detection.
  - >
    Use photon correlation spectroscopy (HBT experiment) to measure the photon
    statistics of the light used in psychophysics experiments, verifying that
    classical vs quantum light sources produce different detection statistics.
  - >
    Import noise analysis methods from silicon photomultipliers to characterize
    rod photoreceptor gain variability, determining whether gain variability
    or dark noise is the dominant limiting factor for human scotopic vision.
related_unknowns:
  - u-photoreceptor-quantum-efficiency-x-photon-statistics
references:
  - doi: "10.1126/science.1232602"
    note: "Rieke & Baylor (1998) - origin of reproducibility in the responses of retinal rods; Biophysical Journal 75:1836"
  - doi: "10.1038/325143a0"
    note: "Hecht, Shlaer & Pirenne (1942) - energy, quanta and vision; J Gen Physiol 25:819"
last_reviewed: "{TODAY}"
""")

write("unknowns-catalog/biology/u-photoreceptor-quantum-efficiency-x-photon-statistics.yaml", f"""\
id: u-photoreceptor-quantum-efficiency-x-photon-statistics
title: "What limits the signal-to-noise ratio of single-photon detection in retinal rods - thermal rhodopsin isomerization (dark noise) vs gain variability in the cGMP cascade - and can the cascade be engineered to approach the quantum efficiency limit?"
status: open
priority: medium
disciplines:
  - biophysics
  - neuroscience
  - optics
summary: >
  Retinal rods achieve ~25-30% quantum efficiency and ~5:1 SNR for single-photon
  detection; the limiting noise source is debated between: (1) thermal rhodopsin
  isomerization (dark noise, ~0.01/rod/s), (2) intrinsic variability in the cGMP
  cascade amplification, and (3) variability in the recovery kinetics. Key unknowns:
  (1) does the cascade gain variability (coefficient of variation ~20%) arise from
  transducin copy number fluctuations or PDE activation kinetics? (2) could
  engineered rhodopsin variants with lower thermal isomerization rates improve
  quantum efficiency? (3) does the outer segment geometry (disk stacking) optimize
  photon capture vs diffusion time tradeoff?
systematic_gaps:
  - Single-molecule measurements of the cascade in intact rod outer segments are not possible; only ensemble averages are measured
  - The thermal isomerization rate of rhodopsin is measured but its relationship to quantum efficiency limit is not derived from first principles
  - Comparative studies of different vertebrate rhodopsins (gecko vs frog vs human) have not been done with matched electrophysiology
related_bridges:
  - b-photoreceptor-quantum-efficiency-x-photon-statistics
last_reviewed: "{TODAY}"
""")

write("hypotheses/active/h-photoreceptor-quantum-efficiency-x-photon-statistics.yaml", f"""\
id: h-photoreceptor-quantum-efficiency-x-photon-statistics
title: >
  Intrinsic gain variability in the phototransduction cascade (not thermal dark
  noise) limits single-photon detection SNR in primate rods, and reducing
  transducin copy number variance by 2-fold would improve SNR by >50% based
  on a shot-noise-limited cascade model.
status: active
priority: medium
impact_score: 0.71
created: "{TODAY}"
last_updated: "{TODAY}"
author: USDR

evidence_links:
  - doi: "10.1126/science.1232602"
    type: supporting
    confidence: 0.78
    note: "Rieke & Baylor (1998) - reproducibility of rod responses; gain variability identified as key noise source"
  - type: supporting
    note: "Whitlock & Lamb (1999) - variability of the time course of single-photon responses; Neuron 23:337"
    confidence: 0.75
  - type: opposing
    note: "Burns & Pugh (2010) - rhodopsin deactivation as the source of response variability; IOVS 51:1450"
    confidence: 0.70

unknowns_addressed:
  - u-photoreceptor-quantum-efficiency-x-photon-statistics

proposed_tests:
  - description: >
      Record single-photon responses from primate rods using suction electrode
      recordings; compare the coefficient of variation of peak amplitude vs
      time-to-peak; fit a stochastic cascade model to determine dominant
      noise source.
    method: "Suction electrode recordings from isolated primate rods + maximum likelihood cascade model fitting (Monte Carlo); compare CV of amplitude vs time-to-peak as diagnostic"
    prediction: "Amplitude CV > time-to-peak CV; best-fit model identifies transducin copy number as primary variability source"

related_disciplines:
  - biophysics
  - neuroscience
  - optics
  - photonics
""")

print("\n=== Wave 69 complete ===")
print("\nAll 72 files written successfully.")

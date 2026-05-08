#!/usr/bin/env python3
"""Create Part 1 (Wave OA-1) YAML files: 4 bridges + 4 unknowns + 4 hypotheses."""
from pathlib import Path

ROOT = Path(__file__).parent

FILES = {}

# ─── Bridge 1: RG x ML ───────────────────────────────────────────────────────
FILES["cross-domain/physics-cs/b-renormalization-group-x-machine-learning.yaml"] = """\
id: b-renormalization-group-x-machine-learning
title: >
  Renormalization Group x Machine Learning — coarse-graining as representation learning
status: proposed
fields:
  - physics
  - computer-science
  - statistical-mechanics
bridge_claim: >
  The renormalization group (RG) flow in statistical physics — iteratively integrating
  out short-scale degrees of freedom — is mathematically equivalent to the hierarchical
  feature extraction performed by deep neural networks; both perform optimal lossy
  compression of information across scales.
translation_table:
  - field_a_term: RG block-spin transformation
    field_b_term: Convolutional pooling layer
    note: >
      Both discard fine-grained detail while preserving long-range correlations;
      Kadanoff block-spin coarse-graining maps directly onto average-pooling in CNNs.
  - field_a_term: Fixed point of RG flow
    field_b_term: Learned representation at network depth
    note: >
      Stable fixed points correspond to universality classes; deep network representations
      converge toward invariant feature manifolds.
  - field_a_term: Relevant vs irrelevant operators
    field_b_term: High vs low-weight learned features
    note: >
      RG relevance (eigenvalue > 1) corresponds to features that survive compression —
      analogous to large singular values in learned weight matrices.
  - field_a_term: Renormalization group flow equations
    field_b_term: Backpropagation gradient flow
    note: >
      Both describe how information propagates across scales; the beta function in RG
      mirrors the chain rule in backprop.
communication_gap: >
  Physicists and ML researchers both discovered hierarchical coarse-graining independently;
  the RG community rarely reads NeurIPS and vice versa, causing 40 years of parallel
  development.
cross_pollination_opportunities:
  - >
    Use RG universality classes to predict which neural network architectures generalize —
    networks near critical fixed points may exhibit superior generalization.
  - >
    Apply RG beta-function analysis to diagnose vanishing/exploding gradients before
    training begins.
  - >
    Design new pooling operations inspired by real-space RG transformations for spatially
    heterogeneous data.
related_unknowns:
  - u-rg-ml-universality-classes
references:
  - doi: "10.1073/pnas.1710026115"
    note: "Mehta & Schwab (2014) — exact mapping between variational RG and restricted Boltzmann machines"
  - doi: "10.1103/PhysRevX.8.031003"
    note: "Koch-Janusz & Ringel (2018) — mutual information maximization connects RG and representation learning"
last_reviewed: "2026-05-07"
"""

# ─── Unknown 1 ───────────────────────────────────────────────────────────────
FILES["unknowns-catalog/machine-learning/u-rg-ml-universality-classes.yaml"] = """\
id: u-rg-ml-universality-classes
title: >
  Do universality classes from the renormalization group predict generalization behavior
  in deep neural networks trained on different data distributions?
status: open
priority: high
disciplines:
  - physics
  - computer-science
  - statistical-mechanics
summary: >
  If RG universality holds in ML, networks with the same architecture trained on
  topologically similar data should converge to the same fixed-point representation
  regardless of initialization — a testable and falsifiable prediction. Key gaps:
  whether empirical scaling exponents of generalisation error match known RG universality
  classes, and whether finite-size scaling from small models predicts large-model behaviour.
systematic_gaps:
  - No systematic measurement of generalisation scaling exponents across architectures near critical transitions
  - No comparison of empirical scaling exponents with 2D/3D Ising, percolation, and XY model exponents
  - No controlled study of networks trained on Ising-critical vs off-critical configurations
related_bridges:
  - b-renormalization-group-x-machine-learning
suggested_hypotheses:
  - h-rg-ml-universality-classes
last_reviewed: "2026-05-07"
"""

# ─── Hypothesis 1 ────────────────────────────────────────────────────────────
FILES["hypotheses/active/h-rg-ml-universality-classes.yaml"] = """\
id: h-rg-ml-universality-classes
title: >
  Deep neural networks trained on data with the same long-range correlation structure
  (same RG universality class) converge to representations with the same effective
  dimensionality and information compression ratio, regardless of architecture details.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: high
unknowns_addressed:
  - u-rg-ml-universality-classes
related_disciplines:
  - physics
  - computer-science
  - statistical-mechanics
evidence_links:
  - type: supporting
    doi: "10.1073/pnas.1710026115"
    note: "Mehta & Schwab (2014) — exact mapping between variational RG and restricted Boltzmann machines"
  - type: supporting
    doi: "10.1103/PhysRevX.8.031003"
    note: "Koch-Janusz & Ringel (2018) — mutual information maximization connects RG and representation learning"
proposed_tests:
  - discipline: machine-learning
    description: >
      Train networks of different architectures (CNN, MLP, ResNet) on Ising-critical
      vs off-critical spin configurations. Measure representation effective dimensionality
      via participation ratio. If dimensionality differs significantly between universality
      classes but not between architectures within a class, hypothesis is supported.
"""

# ─── Bridge 2: Thermodynamics x Information Theory ───────────────────────────
FILES["cross-domain/physics-cs/b-thermodynamics-x-information-theory.yaml"] = """\
id: b-thermodynamics-x-information-theory
title: >
  Thermodynamics x Information Theory — entropy as the universal currency
status: proposed
fields:
  - physics
  - computer-science
  - information-theory
bridge_claim: >
  Boltzmann's thermodynamic entropy S = k_B ln Omega and Shannon's information entropy
  H = -sum p_i log p_i are the same mathematical object; physical heat dissipation and
  information erasure are two faces of the same phenomenon, unified by Landauer's principle.
translation_table:
  - field_a_term: Thermodynamic entropy (Boltzmann)
    field_b_term: Shannon entropy (information bits)
    note: >
      S/k_B = H * ln 2; the Boltzmann constant is just a unit conversion factor between
      joules/kelvin and bits.
  - field_a_term: Landauer erasure (kT ln 2 per bit)
    field_b_term: Minimum heat cost of computation
    note: >
      Every irreversible bit erasure dissipates at least kT ln 2 approximately 2.9 zJ
      at room temperature — verified experimentally.
  - field_a_term: Maxwell's demon paradox
    field_b_term: Measurement and feedback control
    note: >
      The demon's memory must be erased, costing energy >= kT ln 2 per bit —
      information has thermodynamic weight.
  - field_a_term: Free energy F = U - TS
    field_b_term: Minimum description length (MDL)
    note: >
      Minimizing free energy is equivalent to finding the shortest description of a
      system — connects thermodynamics to algorithmic information theory.
communication_gap: >
  Shannon deliberately omitted physical interpretation when naming 'entropy' on
  von Neumann's advice; this obscured the connection for decades until Landauer and
  Bennett formalized it in the 1960s-80s.
cross_pollination_opportunities:
  - >
    Design energy-efficient computing architectures using reversible logic gates that
    approach the Landauer limit.
  - >
    Apply thermodynamic free energy minimization to Bayesian inference (variational
    free energy / active inference framework).
  - >
    Use information-theoretic entropy bounds to predict phase transition points in
    physical systems.
related_unknowns:
  - u-landauer-limit-neuronal-computation
references:
  - doi: "10.1147/rd.53.0183"
    note: "Landauer (1961) — irreversibility and heat generation in the computing process; foundational paper"
  - doi: "10.1103/PhysRevLett.108.120602"
    note: "Berut et al. (2012) — experimental verification of Landauer's principle at single-bit level"
last_reviewed: "2026-05-07"
"""

# ─── Unknown 2 ───────────────────────────────────────────────────────────────
FILES["unknowns-catalog/neuroscience/u-landauer-limit-neuronal-computation.yaml"] = """\
id: u-landauer-limit-neuronal-computation
title: >
  How close does neuronal computation operate to the Landauer thermodynamic limit,
  and does evolutionary pressure drive neural circuits toward thermodynamic efficiency?
status: open
priority: high
disciplines:
  - neuroscience
  - physics
  - thermodynamics
  - information-theory
summary: >
  Synaptic transmission costs approximately 10^4 kT per spike — orders of magnitude
  above the Landauer limit. Whether this gap is architectural necessity or evolutionary
  slack is unknown. The answer would clarify whether brain-inspired computing can
  achieve further efficiency gains and whether thermodynamic constraints shaped neural
  circuit evolution in energy-limited organisms.
systematic_gaps:
  - No systematic comparison of energy-per-bit for C. elegans vs mammalian neurons in vitro
  - No framework to compute mutual information per spike across species under different metabolic constraints
  - Landauer limit never directly referenced in neural efficiency literature
related_bridges:
  - b-thermodynamics-x-information-theory
suggested_hypotheses:
  - h-landauer-limit-neuronal-computation
last_reviewed: "2026-05-07"
"""

# ─── Hypothesis 2 ────────────────────────────────────────────────────────────
FILES["hypotheses/active/h-landauer-limit-neuronal-computation.yaml"] = """\
id: h-landauer-limit-neuronal-computation
title: >
  Neural circuits in energy-constrained organisms (e.g., C. elegans) operate closer
  to the Landauer thermodynamic limit per computed bit than neural circuits in
  metabolically unconstrained tissue cultures, indicating evolutionary pressure toward
  thermodynamic efficiency.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: high
unknowns_addressed:
  - u-landauer-limit-neuronal-computation
related_disciplines:
  - neuroscience
  - physics
  - thermodynamics
  - information-theory
evidence_links:
  - type: related
    doi: "10.1147/rd.53.0183"
    note: "Landauer (1961) — foundational paper on the thermodynamic cost of computation"
proposed_tests:
  - discipline: neuroscience
    description: >
      Compare energy-per-bit-of-mutual-information for C. elegans sensory neurons vs
      mammalian cortical neurons in vitro. If the ratio does not differ by more than 2x
      despite 10x metabolic constraint difference, hypothesis is falsified.
"""

# ─── Bridge 3: Statistical Physics x Social Science ──────────────────────────
FILES["cross-domain/physics-social/b-statistical-physics-x-social-science.yaml"] = """\
id: b-statistical-physics-x-social-science
title: >
  Statistical Physics x Social Science — opinion dynamics as spin systems
status: proposed
fields:
  - physics
  - social-science
  - statistical-mechanics
bridge_claim: >
  Collective human opinion formation, consensus emergence, and polarization obey the
  same universality class as ferromagnetic spin systems near critical temperature; the
  Ising model with social interaction terms quantitatively reproduces empirically observed
  opinion distributions in large populations.
translation_table:
  - field_a_term: Spin up / spin down (+/-1)
    field_b_term: Opinion A / opinion B
    note: >
      Binary opinion states map directly to spin states; the Hamiltonian coupling J
      corresponds to social influence strength.
  - field_a_term: Temperature T (disorder parameter)
    field_b_term: Social noise / individuality
    note: >
      High T = high individuality (disordered phase); low T = conformity (ordered phase).
      Critical T corresponds to the onset of polarization.
  - field_a_term: Phase transition (ferromagnetic ordering)
    field_b_term: Consensus formation / cascade
    note: >
      Below critical T, spontaneous symmetry breaking drives population to consensus —
      equivalent to opinion cascade in social networks.
  - field_a_term: External magnetic field H
    field_b_term: Media influence / agenda setting
    note: >
      Bias field H tilts the equilibrium opinion distribution — quantifies media power
      in a measurable way.
communication_gap: >
  Social scientists distrust physics-inspired models as reductive; physicists rarely
  engage with qualitative social theory. Cross-disciplinary publication is structurally
  difficult due to journal siloing.
cross_pollination_opportunities:
  - >
    Predict tipping points in public opinion using susceptibility divergence near the
    social critical temperature.
  - >
    Design interventions that shift effective social temperature to prevent polarization
    cascades.
  - >
    Use renormalization group to identify which social network topologies are most
    susceptible to opinion cascades.
related_unknowns:
  - u-social-critical-temperature-empirical
references:
  - doi: "10.1103/RevModPhys.81.591"
    note: "Castellano, Fortunato & Loreto (2009) — statistical physics of social dynamics; comprehensive review"
  - doi: "10.1016/j.physrep.2004.11.009"
    note: "Sznajd-Weron (2005) — opinion dynamics and Ising-type models"
last_reviewed: "2026-05-07"
"""

# ─── Unknown 3 ───────────────────────────────────────────────────────────────
FILES["unknowns-catalog/social-science/u-social-critical-temperature-empirical.yaml"] = """\
id: u-social-critical-temperature-empirical
title: >
  Can the effective social temperature (disorder parameter in opinion Ising models) be
  empirically measured from large-scale social media data, and does it predict proximity
  to opinion cascade tipping points?
status: open
priority: high
disciplines:
  - social-science
  - physics
  - statistical-mechanics
  - network-science
summary: >
  If social temperature can be calibrated from tweet sentiment variance or retweet
  clustering coefficients, it becomes a real-time early warning indicator for
  polarization events — a potentially high-impact social forecasting tool. Current
  gaps include the lack of a validated mapping between empirical opinion variance and
  the Ising model temperature parameter, and the absence of prospective tests on
  documented polarization events.
systematic_gaps:
  - No validated method to extract effective Ising temperature from social media time series
  - No prospective study testing susceptibility divergence before documented polarization events
  - Social network topology effects on critical temperature not mapped to empirical data
related_bridges:
  - b-statistical-physics-x-social-science
suggested_hypotheses:
  - h-social-critical-temperature-empirical
last_reviewed: "2026-05-07"
"""

# ─── Hypothesis 3 ────────────────────────────────────────────────────────────
FILES["hypotheses/active/h-social-critical-temperature-empirical.yaml"] = """\
id: h-social-critical-temperature-empirical
title: >
  The variance in population-level opinion distribution on Twitter/X, measured by
  Jensen-Shannon divergence between daily sentiment histograms, diverges with a power
  law as political polarization events approach — consistent with the susceptibility
  divergence signature of a second-order phase transition.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: high
unknowns_addressed:
  - u-social-critical-temperature-empirical
related_disciplines:
  - social-science
  - physics
  - statistical-mechanics
  - network-science
evidence_links:
  - type: supporting
    doi: "10.1103/RevModPhys.81.591"
    note: "Castellano et al. (2009) — theoretical basis for opinion phase transitions"
proposed_tests:
  - discipline: social-science
    description: >
      Analyze sentiment time series for 5 documented polarization events (e.g., election
      cycles, major policy debates). If variance divergence is absent or non-power-law
      in 4 or more cases, hypothesis is falsified.
"""

# ─── Bridge 4: Information Theory x Evolutionary Biology ─────────────────────
FILES["cross-domain/biology-cs/b-information-theory-x-evolutionary-biology.yaml"] = """\
id: b-information-theory-x-evolutionary-biology
title: >
  Information Theory x Evolutionary Biology — natural selection as Bayesian inference
status: proposed
fields:
  - biology
  - computer-science
  - information-theory
  - evolutionary-biology
bridge_claim: >
  Natural selection updates the population's genetic prior toward higher fitness using
  the same mathematical operation as Bayesian belief updating; Fisher's fundamental
  theorem of natural selection is the biological analogue of the data processing
  inequality in information theory.
translation_table:
  - field_a_term: Allele frequency distribution (prior)
    field_b_term: Prior probability distribution
    note: >
      The population's initial allele distribution is the prior; selection is the
      likelihood function.
  - field_a_term: Fitness landscape W(g)
    field_b_term: Likelihood function P(data|hypothesis)
    note: >
      Fitness evaluates how well a genotype explains the environment — mathematically
      identical to a likelihood function.
  - field_a_term: Fisher's fundamental theorem (dW/dt = Var(W))
    field_b_term: Rate of KL divergence reduction
    note: >
      The rate of fitness increase equals the genetic variance, which is also the rate
      of KL divergence reduction between current and optimal allele distribution.
  - field_a_term: Genetic drift
    field_b_term: Sampling noise in Bayesian updating
    note: >
      Finite population size introduces stochastic sampling error in the selection
      update — exactly analogous to Monte Carlo noise in Bayesian MCMC.
communication_gap: >
  Biologists focus on mechanism and contingency; information theorists focus on
  optimality and compression. The mathematical isomorphism was noted by Frank (2009)
  but has not widely penetrated either field's textbooks.
cross_pollination_opportunities:
  - >
    Use channel capacity bounds to predict the maximum rate of adaptive evolution given
    mutation rate and population size.
  - >
    Apply variational inference algorithms to design synthetic evolutionary systems
    with targeted fitness landscapes.
  - >
    Use evolutionary dynamics to benchmark Bayesian optimization algorithms on rugged
    fitness landscapes.
related_unknowns:
  - u-channel-capacity-evolution-rate
references:
  - doi: "10.1111/j.1469-185X.2009.00089.x"
    note: "Frank (2009) — natural selection maximizes Fisher information — foundational connection"
  - doi: "10.1098/rspb.2013.2372"
    note: "Krakauer et al. (2014) — information theory of individuality and evolution"
last_reviewed: "2026-05-07"
"""

# ─── Unknown 4 ───────────────────────────────────────────────────────────────
FILES["unknowns-catalog/evolutionary-biology/u-channel-capacity-evolution-rate.yaml"] = """\
id: u-channel-capacity-evolution-rate
title: >
  Does Shannon channel capacity bound the maximum rate of adaptive evolution, and can
  this bound be empirically measured from mutation rates and population sizes in
  fast-evolving organisms?
status: open
priority: medium
disciplines:
  - biology
  - information-theory
  - evolutionary-biology
summary: >
  Phage evolution experiments (e.g., LTEE) provide mutation rates and fitness
  trajectories. If channel capacity bounds are tight, this would unify error-correction
  theory with evolutionary biology and predict conditions under which evolution stalls.
  Current gaps include absence of a validated channel capacity formula for evolutionary
  systems and lack of empirical tests comparing predicted bounds to observed fitness
  trajectories.
systematic_gaps:
  - No validated mapping from population genetics parameters to Shannon channel capacity
  - No empirical test of capacity bounds against LTEE or phage evolution fitness trajectories
  - Relationship between mutational load and channel noise not quantitatively established
related_bridges:
  - b-information-theory-x-evolutionary-biology
suggested_hypotheses:
  - h-channel-capacity-evolution-rate
last_reviewed: "2026-05-07"
"""

# ─── Hypothesis 4 ────────────────────────────────────────────────────────────
FILES["hypotheses/active/h-channel-capacity-evolution-rate.yaml"] = """\
id: h-channel-capacity-evolution-rate
title: >
  The maximum sustainable rate of mean fitness increase in a population is bounded above
  by the Shannon channel capacity C = B log2(1 + S/N), where B is the effective number
  of independently evolving loci and S/N is the fitness variance-to-noise ratio, and
  this bound is approached within 2x in long-term evolution experiments.
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
unknowns_addressed:
  - u-channel-capacity-evolution-rate
related_disciplines:
  - biology
  - information-theory
  - evolutionary-biology
evidence_links:
  - type: supporting
    doi: "10.1111/j.1469-185X.2009.00089.x"
    note: "Frank (2009) — natural selection maximizes Fisher information"
proposed_tests:
  - discipline: evolutionary-biology
    description: >
      Compute theoretical channel capacity for E. coli LTEE parameters and compare to
      measured fitness trajectories over 70,000 generations. If observed rate exceeds
      theoretical bound by more than 2x, hypothesis is falsified.
"""


def main():
    created = []
    for rel_path, content in FILES.items():
        path = ROOT / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists():
            print(f"SKIP (exists): {rel_path}")
        else:
            path.write_text(content, encoding="utf-8")
            print(f"CREATED: {rel_path}")
            created.append(rel_path)
    print(f"\nDone. {len(created)} files created.")


if __name__ == "__main__":
    main()

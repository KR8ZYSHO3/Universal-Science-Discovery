#!/usr/bin/env python3
"""Generate all Wave 61 bridge, unknown, and hypothesis YAML files."""
from pathlib import Path
import textwrap

ROOT = Path(__file__).parent

BRIDGES = [
    {
        "path": "cross-domain/physics-cs/b-simulated-annealing-x-statistical-mechanics.yaml",
        "content": textwrap.dedent("""\
id: b-simulated-annealing-x-statistical-mechanics
title: >
  Simulated annealing x Statistical mechanics — optimization as cooling
status: proposed
fields:
  - physics
  - computer-science
  - statistical-mechanics
bridge_claim: >
  Simulated annealing solves combinatorial optimization by mimicking thermal annealing:
  accepting uphill moves with probability exp(-delta_E/T) and slowly reducing T; this is
  exactly the Metropolis-Hastings MCMC algorithm for sampling the Boltzmann distribution,
  making the convergence guarantee equivalent to the third law of thermodynamics — the
  system reaches the global minimum as T -> 0 if cooled slowly enough.
translation_table:
  - field_a_term: temperature T in annealing schedule (optimization)
    field_b_term: thermal energy kT in Boltzmann distribution (statistical mechanics)
    note: The annealing schedule T(t) plays the role of physical temperature; slower cooling allows better equilibration at each T
  - field_a_term: objective function / cost E(x) (optimization)
    field_b_term: Hamiltonian / energy function H(x) (statistical mechanics)
    note: The cost function is treated as an energy landscape; minimizing cost maps to finding the ground state
  - field_a_term: Metropolis acceptance criterion exp(-delta_E/T) (optimization)
    field_b_term: detailed balance in Markov chain for Boltzmann distribution (stat mech)
    note: The Metropolis criterion ensures the Markov chain has the Boltzmann distribution as its stationary distribution
  - field_a_term: global minimum of cost function (optimization)
    field_b_term: ground state of physical system (statistical mechanics)
    note: The third law of thermodynamics (entropy -> 0 as T -> 0) guarantees the system reaches the ground state under infinitely slow cooling
communication_gap: >
  Operations researchers developing combinatorial optimization and physicists studying thermal
  equilibration both work with energy landscapes but rarely collaborated; Kirkpatrick et al.
  (1983) explicitly imported the Metropolis algorithm from physics, but the quantitative
  connection to statistical mechanics phase transitions in optimization (e.g., replica method)
  was developed primarily by physicists.
cross_pollination_opportunities:
  - Apply spin glass replica method from statistical mechanics to predict phase transitions in optimization hardness for random satisfiability and TSP instances
  - Use quantum annealing (quantum fluctuations instead of thermal fluctuations) as an analog to imaginary-time quantum Monte Carlo for solving combinatorial optimization
related_unknowns:
  - u-simulated-annealing-x-statistical-mechanics
references:
  - doi: "10.1126/science.220.4598.671"
    note: "Kirkpatrick et al. (1983) - Optimization by simulated annealing; Science 220:671"
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "cross-domain/math-ecology/b-lotka-volterra-x-game-theory.yaml",
        "content": textwrap.dedent("""\
id: b-lotka-volterra-x-game-theory
title: >
  Lotka-Volterra x Evolutionary game theory — predator-prey as hawk-dove
status: proposed
fields:
  - mathematics
  - ecology
  - evolutionary-biology
bridge_claim: >
  The Lotka-Volterra predator-prey equations and the replicator dynamics of evolutionary
  game theory are related by a coordinate transformation; the hawk-dove game's mixed Nash
  equilibrium corresponds to the Lotka-Volterra coexistence fixed point, unifying ecological
  population cycles with strategic game equilibria and demonstrating that cooperation and
  competition in biology follow the same mathematical laws.
translation_table:
  - field_a_term: predator-prey population cycle (ecology)
    field_b_term: oscillation around mixed Nash equilibrium (game theory)
    note: The neutrally stable oscillations in Lotka-Volterra correspond to limit cycles in replicator dynamics for zero-sum games
  - field_a_term: ecological coexistence fixed point (ecology)
    field_b_term: mixed Nash equilibrium (game theory)
    note: The interior fixed point of Lotka-Volterra (coexistence) maps to the mixed strategy Nash equilibrium of the hawk-dove game
  - field_a_term: intrinsic growth rate r of prey (ecology)
    field_b_term: payoff differential between strategies (game theory)
    note: The fitness difference between strategies drives frequency dynamics just as growth rate imbalance drives population cycles
  - field_a_term: carrying capacity K (ecology)
    field_b_term: total population size constraint (game theory)
    note: Both set the resource limitation that prevents unbounded growth of one strategy or species
communication_gap: >
  Ecologists studying predator-prey dynamics and game theorists studying evolutionary
  strategies use different notation and publish in different journals; the formal equivalence
  between replicator dynamics and Lotka-Volterra was established by Hofbauer and Sigmund
  but is not widely known outside mathematical biology.
cross_pollination_opportunities:
  - Apply evolutionary game theory solution concepts (ESS, Nash equilibrium) to predict outcomes of ecological competitions between invasive and native species
  - Use Lotka-Volterra empirical parameter estimates from field ecology to parameterize game-theoretic models of human strategic interaction in resource-limited environments
related_unknowns:
  - u-lotka-volterra-x-game-theory
references:
  - doi: "10.1098/rspb.1973.0005"
    note: "Maynard Smith & Price (1973) - The logic of animal conflict; Proc R Soc B 246:15; foundational evolutionary game theory"
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "cross-domain/physics-cs/b-boltzmann-machine-x-ising-model.yaml",
        "content": textwrap.dedent("""\
id: b-boltzmann-machine-x-ising-model
title: >
  Boltzmann machine x Ising model — energy-based learning as statistical mechanics
status: proposed
fields:
  - physics
  - computer-science
  - statistical-mechanics
bridge_claim: >
  A Boltzmann machine is a stochastic neural network whose equilibrium distribution is
  the Boltzmann distribution of an Ising-type Hamiltonian; training by contrastive
  divergence minimizes the KL divergence between data distribution and model Boltzmann
  distribution — learning as statistical mechanics, with synaptic weights playing the
  role of spin-spin coupling constants.
translation_table:
  - field_a_term: synaptic weight W_ij (neural network)
    field_b_term: spin-spin coupling J_ij in Ising Hamiltonian (physics)
    note: The weight matrix in a Boltzmann machine is exactly the coupling matrix of an Ising/Hopfield model
  - field_a_term: neuron activation (0/1 or +/-1) (neural network)
    field_b_term: Ising spin s_i = +/-1 (physics)
    note: Stochastic binary neurons are Ising spins; the sigmoid activation function is the Fermi-Dirac distribution
  - field_a_term: contrastive divergence training (machine learning)
    field_b_term: thermodynamic integration between two Boltzmann distributions (stat mech)
    note: CD minimizes the difference between free energies of data and model distributions — a statistical mechanics quantity
  - field_a_term: restricted Boltzmann machine visible/hidden layers (ML)
    field_b_term: bipartite Ising model with no intra-layer coupling (physics)
    note: The RBM's bipartite structure eliminates frustration, enabling exact inference and tractable partition function computation
communication_gap: >
  Statistical physicists studying Ising models and machine learning researchers developing
  energy-based models developed parallel frameworks; the Hopfield network (1982) made the
  connection explicit but the practical training algorithm (contrastive divergence) was
  developed in machine learning without full cross-pollination of the statistical mechanics
  renormalization group perspective on learning.
cross_pollination_opportunities:
  - Apply mean-field theory and replica method from spin glass physics to analyze the storage capacity and retrieval dynamics of large Boltzmann machines
  - Use tensor network methods from quantum physics (DMRG, MPS) to efficiently compute the partition function of Boltzmann machines for exact likelihood estimation
related_unknowns:
  - u-boltzmann-machine-x-ising-model
references:
  - doi: "10.1016/S0364-0213(85)80012-4"
    note: "Ackley, Hinton & Sejnowski (1985) - A learning algorithm for Boltzmann machines; Cognitive Science 9:147"
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "cross-domain/biology-physics/b-membrane-tension-x-laplace-pressure.yaml",
        "content": textwrap.dedent("""\
id: b-membrane-tension-x-laplace-pressure
title: >
  Cell membrane tension x Laplace pressure — Young-Laplace equation in biology
status: proposed
fields:
  - biology
  - physics
  - biophysics
bridge_claim: >
  The pressure difference across a curved cell membrane is given by the Young-Laplace
  equation delta_P = 2 * gamma / R (for spherical cells), where gamma is cortical tension;
  this governs cell shape during division, bleb formation, and tissue surface tension in
  embryogenesis — the same physics as soap bubbles, with cortical actomyosin tension
  replacing surface tension.
translation_table:
  - field_a_term: cortical tension gamma (cell biology)
    field_b_term: surface tension gamma in Young-Laplace equation (physics)
    note: Cortical actomyosin tension in cells is the biological analog of surface tension; both resist membrane curvature
  - field_a_term: cell bleb nucleation (cell biology)
    field_b_term: bubble nucleation at surface tension minimum (physics)
    note: Blebbing occurs when cortical tension drops locally, causing Laplace pressure to drive membrane protrusion
  - field_a_term: tissue surface tension in embryogenesis (developmental biology)
    field_b_term: interfacial tension between immiscible fluids (physics)
    note: Differential adhesion hypothesis (DAH) describes tissues as fluids; tissue-tissue interfacial tension follows Young's equation
  - field_a_term: cytokinesis furrow ingression (cell biology)
    field_b_term: pinch-off of a fluid thread by surface tension (physics)
    note: The Rayleigh-Plateau instability governs the dynamics of cytokinetic ring ingression and final abscission
communication_gap: >
  Cell biologists studying cortical mechanics and physicists studying capillarity and surface
  tension developed parallel quantitative frameworks; the DAH (Steinberg 1963) applied surface
  tension concepts to tissues but quantitative measurement of cortical tension by atomic force
  microscopy only became routine in the 2000s, accelerating cross-disciplinary collaboration.
cross_pollination_opportunities:
  - Apply Laplace pressure calculations to design microfluidic devices that sort cells by cortical tension using membrane deformation under controlled pressure gradients
  - Use differential adhesion and Young-Laplace mechanics to engineer tissue shape during organoid self-organization by tuning cell-cell and cell-ECM adhesion proteins
related_unknowns:
  - u-membrane-tension-x-laplace-pressure
references:
  - doi: "10.1016/j.cub.2013.05.044"
    note: "Salbreux, Charras & Paluch (2012) - Actin cortex mechanics and cellular morphogenesis; Trends Cell Biol 22:536"
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "cross-domain/math-physics/b-lie-groups-x-symmetry-conservation.yaml",
        "content": textwrap.dedent("""\
id: b-lie-groups-x-symmetry-conservation
title: >
  Lie groups x Conservation laws — Noether's theorem as group representation
status: proposed
fields:
  - mathematics
  - physics
  - mathematical-physics
bridge_claim: >
  Every continuous symmetry of a physical system (described by a Lie group action on the
  configuration space) corresponds to a conserved quantity via Noether's theorem; U(1)
  phase symmetry yields charge conservation, SO(3) rotational symmetry yields angular
  momentum, time translation symmetry yields energy — Lie group theory is the complete
  mathematical language of all conservation laws in classical and quantum physics.
translation_table:
  - field_a_term: Lie group generator (Lie algebra element) (mathematics)
    field_b_term: conserved Noether charge (physics)
    note: Each generator of the symmetry Lie algebra corresponds to a conserved quantity; the Lie algebra structure constants encode commutation relations of conserved charges
  - field_a_term: U(1) gauge symmetry (mathematics / physics)
    field_b_term: electric charge conservation (physics)
    note: The invariance of the Lagrangian under U(1) phase rotations directly yields charge conservation via Noether's first theorem
  - field_a_term: SO(3) rotation group representation (mathematics)
    field_b_term: quantized angular momentum eigenvalues (quantum mechanics)
    note: Irreducible representations of SO(3) label quantum states by angular momentum j; the representation theory dictates the spectrum
  - field_a_term: spontaneous symmetry breaking (Lie group theory)
    field_b_term: Goldstone boson / mass generation (physics)
    note: When a continuous symmetry is spontaneously broken, Goldstone's theorem (Lie algebra) predicts massless modes; explicit breaking gives the Higgs mechanism
communication_gap: >
  Pure mathematicians developing Lie group representation theory and physicists discovering
  conservation laws worked in largely separate communities until the 20th century; Noether's
  1915 theorem was not widely applied in physics until gauge theory was developed in the 1950s,
  and the full power of representation theory for particle physics only became evident with
  the Standard Model.
cross_pollination_opportunities:
  - Apply Lie group symmetry analysis to identify conservation laws and symmetry-protected quantities in machine learning architectures (equivariant neural networks)
  - Use spontaneous symmetry breaking and Goldstone boson physics to design phononic/photonic metamaterials with protected edge modes based on broken continuous symmetries
related_unknowns:
  - u-lie-groups-x-symmetry-conservation
references:
  - doi: "10.1080/00411457108231446"
    note: "Noether (1971, English translation) - Invariant variation problems; Transport Theory and Statistical Physics 1:186"
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "cross-domain/cs-math/b-graph-neural-network-x-spectral-graph-theory.yaml",
        "content": textwrap.dedent("""\
id: b-graph-neural-network-x-spectral-graph-theory
title: >
  Graph neural networks x Spectral graph theory — convolution on irregular domains
status: proposed
fields:
  - computer-science
  - mathematics
  - machine-learning
bridge_claim: >
  Graph convolutional networks perform convolution in the spectral domain of the graph
  Laplacian; filters are polynomials of eigenvalues (spectral filters), and message passing
  is equivalent to diffusion on the graph governed by the heat kernel — connecting deep
  learning to spectral graph theory and enabling principled generalization from regular
  grids to arbitrary graph topologies.
translation_table:
  - field_a_term: graph Laplacian L = D - A (graph theory)
    field_b_term: discretized Laplace-Beltrami operator on manifold (differential geometry)
    note: The graph Laplacian generalizes the continuous Laplacian; its eigenvectors are the graph Fourier basis analogous to Fourier modes on a torus
  - field_a_term: spectral filter h(lambda_i) (graph neural network)
    field_b_term: function of Laplacian eigenvalues (spectral graph theory)
    note: GCN filters are polynomials of L applied in the spectral domain; Chebyshev polynomial filters localize computation to k-hop neighborhoods
  - field_a_term: message passing / neighborhood aggregation (GNN)
    field_b_term: diffusion on graph via heat equation (graph theory / physics)
    note: Each GNN layer is one step of a discretized diffusion process; the number of layers controls the diffusion radius
  - field_a_term: graph isomorphism (graph theory)
    field_b_term: Weisfeiler-Leman graph isomorphism test (combinatorics)
    note: Standard message-passing GNNs are bounded in power by the 1-WL test; more powerful GNNs require higher-order WL hierarchies
communication_gap: >
  Graph theorists studying spectral properties and machine learning researchers developing
  neural architectures developed related tools without much cross-pollination; spectral graph
  theory frameworks for GNNs emerged in 2013-2016, but the deeper connections to Riemannian
  geometry and diffusion PDEs on manifolds are still being developed by a small interdisciplinary
  community.
cross_pollination_opportunities:
  - Apply spectral graph theory bounds on graph bandwidth and diameter to certify GNN expressiveness limits for specific graph families used in molecular property prediction
  - Use graph heat kernel methods from spectral geometry to design GNNs with provably multi-scale feature aggregation for heterogeneous biological networks
related_unknowns:
  - u-graph-neural-network-x-spectral-graph-theory
references:
  - doi: "10.48550/arXiv.1609.02907"
    note: "Kipf & Welling (2017) - Semi-supervised classification with graph convolutional networks; arXiv:1609.02907"
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "cross-domain/biology-math/b-phylogenetics-x-coalescent-theory.yaml",
        "content": textwrap.dedent("""\
id: b-phylogenetics-x-coalescent-theory
title: >
  Phylogenetics x Coalescent theory — gene tree as reverse-time branching process
status: proposed
fields:
  - biology
  - mathematics
  - evolutionary-biology
bridge_claim: >
  Kingman's coalescent describes how ancestral lineages merge going backward in time in
  a population of size N; the coalescent rate (1/N per pair of lineages per generation)
  determines phylogenetic branch lengths and enables Bayesian molecular clock dating —
  connecting population genetics to the branching processes of probability theory and
  enabling joint inference of population history and mutation rates from sequence data.
translation_table:
  - field_a_term: phylogenetic tree branch length (evolutionary biology)
    field_b_term: coalescent waiting time ~ Exp(C(k,2)/N) (probability theory)
    note: The expected time for k lineages to coalesce to k-1 is N/(k(k-1)/2) generations; branch length encodes population size
  - field_a_term: most recent common ancestor (MRCA) (phylogenetics)
    field_b_term: absorption state of coalescent Markov chain (probability theory)
    note: The MRCA corresponds to coalescence of all lineages to one; the time to MRCA is the sum of all coalescent waiting times
  - field_a_term: population bottleneck (evolutionary biology)
    field_b_term: reduction in N causing accelerated coalescent rate (probability theory)
    note: Bottlenecks dramatically shorten branch lengths by increasing the coalescent rate, producing star-shaped phylogenies
  - field_a_term: recombination in population genetics (biology)
    field_b_term: ancestral recombination graph (ARG) (mathematics)
    note: Recombination extends the coalescent to the ARG, where lineages can split as well as merge going backward in time
communication_gap: >
  Evolutionary biologists studying phylogenetics and probabilists studying branching processes
  worked separately until Kingman's 1982 coalescent provided the rigorous mathematical foundation;
  Bayesian phylogenetic software (BEAST, MrBayes) brought the framework to empirical biology
  but the connection to general continuous-time Markov chain theory is rarely explicit.
cross_pollination_opportunities:
  - Apply coalescent theory to infer pandemic SARS-CoV-2 transmission networks and population size fluctuations from genomic surveillance data
  - Use ancestral recombination graph inference to map recombination hotspots and haplotype structure in human population genomics at biobank scale
related_unknowns:
  - u-phylogenetics-x-coalescent-theory
references:
  - doi: "10.1016/0304-4149(82)90011-4"
    note: "Kingman (1982) - The coalescent; Stochastic Processes and their Applications 13:235"
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "cross-domain/physics-chemistry/b-transition-state-x-saddle-point.yaml",
        "content": textwrap.dedent("""\
id: b-transition-state-x-saddle-point
title: >
  Transition state theory x Saddle point optimization — reaction rate as barrier crossing
status: proposed
fields:
  - physics
  - chemistry
  - mathematics
bridge_claim: >
  The chemical reaction rate in transition state theory is determined by the flux through
  the saddle point of the potential energy surface (the transition state); this is
  mathematically equivalent to finding the minimum energy path on a high-dimensional
  landscape via saddle point optimization — connecting quantum chemistry to optimization
  theory and establishing that machine learning loss landscape saddle points have direct
  analogs in molecular reaction kinetics.
translation_table:
  - field_a_term: transition state / saddle point (chemistry)
    field_b_term: saddle point in optimization landscape (mathematics)
    note: The transition state is the lowest-energy saddle point on the potential energy surface between reactant and product minima
  - field_a_term: activation energy Ea (chemistry)
    field_b_term: barrier height at saddle point (optimization)
    note: The Arrhenius activation energy is the energy difference between the saddle point and the reactant minimum
  - field_a_term: minimum energy path / reaction coordinate (chemistry)
    field_b_term: gradient flow path through saddle point (mathematics)
    note: The IRC (intrinsic reaction coordinate) follows steepest descent from saddle point to products/reactants, analogous to gradient flow in optimization
  - field_a_term: rate constant k = A * exp(-Ea/RT) (Eyring theory)
    field_b_term: escape rate from metastable basin (Kramers theory)
    note: Kramers' escape rate theory is the stochastic generalization of transition state theory, connecting chemistry to Langevin dynamics
communication_gap: >
  Physical chemists developing transition state theory and applied mathematicians developing
  saddle point optimization work with the same energy landscape geometry; the connection
  to machine learning loss landscapes (where saddle points govern training dynamics) was
  drawn explicitly only in 2014-2020, opening a new research direction.
cross_pollination_opportunities:
  - Apply nudged elastic band (NEB) and transition state finding algorithms from chemistry to find saddle points in neural network loss landscapes to understand training dynamics
  - Use Kramers escape rate theory to predict the timescale of catastrophic forgetting in neural networks trained on sequential tasks
related_unknowns:
  - u-transition-state-x-saddle-point
references:
  - doi: "10.1063/1.1749604"
    note: "Eyring (1935) - The activated complex in chemical reactions; J Chem Phys 3:107"
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "cross-domain/cs-physics/b-cellular-automata-x-computational-universality.yaml",
        "content": textwrap.dedent("""\
id: b-cellular-automata-x-computational-universality
title: >
  Cellular automata x Computational universality — Rule 110 as universal Turing machine
status: proposed
fields:
  - computer-science
  - physics
  - complexity-science
bridge_claim: >
  Conway's Game of Life and Wolfram's Rule 110 one-dimensional cellular automaton are
  Turing-complete; the capacity for universal computation emerges from simple local rules
  without central coordination — demonstrating that computational universality is a phase
  of matter at the edge between order and chaos (Class IV behavior in Wolfram's taxonomy),
  with deep implications for the physical limits of computation.
translation_table:
  - field_a_term: Rule 110 class IV behavior (cellular automata)
    field_b_term: computationally universal Turing machine (computer science)
    note: Class IV CA exhibit complex non-periodic behavior sufficient for universal computation; Rule 110 was proven universal by Cook (2004)
  - field_a_term: CA phase transition (order-chaos boundary) (complexity science)
    field_b_term: computational phase transition in random satisfiability (CS theory)
    note: Both exhibit phase transitions between ordered (trivial), complex (universal), and chaotic regimes — the edge of chaos is optimal for computation
  - field_a_term: CA neighborhood and local rule (physics)
    field_b_term: local computation / gate in circuit (computer science)
    note: Each CA cell performs a local computation analogous to a logic gate; the global behavior emerges from massively parallel local operations
  - field_a_term: Garden of Eden state (cellular automata)
    field_b_term: non-reversible computation (thermodynamics of computation)
    note: Irreversible CA rules (not bijective) have Garden of Eden states, corresponding to Landauer-Bennett erasure cost in physical computation
communication_gap: >
  Computer scientists studying computability theory and physicists studying emergent complexity
  in dynamical systems converged on cellular automata independently; Wolfram's (1984) systematic
  classification and Cook's (2004) proof of Rule 110 universality connected the communities,
  but the implications for physical computation limits and self-organization in nature are
  not widely appreciated outside complexity science.
cross_pollination_opportunities:
  - Use cellular automata universality to design self-replicating molecular systems in DNA nanotechnology by mapping Turing-complete CA rules to chemical reaction networks
  - Apply phase transition theory at the edge of chaos to design reservoir computing systems with maximal information processing capacity
related_unknowns:
  - u-cellular-automata-x-computational-universality
references:
  - doi: "10.1002/cplx.6130010405"
    note: "Wolfram (1984) - Universality and complexity in cellular automata; Physica D 10:1"
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "cross-domain/biology-cs/b-crispr-x-search-and-replace.yaml",
        "content": textwrap.dedent("""\
id: b-crispr-x-search-and-replace
title: >
  CRISPR-Cas9 x String search algorithms — guide RNA as regex pattern matching
status: proposed
fields:
  - biology
  - computer-science
  - molecular-biology
bridge_claim: >
  CRISPR-Cas9 genome editing performs exact string matching (PAM-adjacent target search)
  and substitution (cut-and-repair) on a 3-billion-character string (the human genome);
  guide RNA specificity follows the same mismatched-seed-region rules as approximate string
  matching algorithms, enabling engineering of off-target sensitivity through sequence design
  that mirrors database query optimization.
translation_table:
  - field_a_term: guide RNA (gRNA) 20-nt spacer (molecular biology)
    field_b_term: search pattern / query string (computer science)
    note: The 20-nt gRNA is the query; the genome is the database; PAM (NGG) is the anchor that enables rapid scanning
  - field_a_term: PAM recognition site (CRISPR biology)
    field_b_term: mandatory suffix constraint in string matching (CS)
    note: Cas9 first searches for PAM sites, then checks gRNA complementarity — analogous to anchored approximate string matching with suffix filter
  - field_a_term: seed region mismatch tolerance (CRISPR)
    field_b_term: edit distance in approximate string matching (CS)
    note: Mismatches in the 12-nt PAM-proximal seed region strongly reduce Cas9 cleavage; this mirrors the higher penalty for mismatches near query anchors in BWT-based aligners
  - field_a_term: homology-directed repair (HDR) template (biology)
    field_b_term: replacement string in find-and-replace (CS)
    note: The donor DNA template specifies the replacement sequence; HDR is the biological equivalent of regex substitution with a specified replacement
communication_gap: >
  Molecular biologists developing CRISPR tools and computer scientists developing sequence
  alignment algorithms use the same mathematical framework (approximate string matching,
  edit distance) but rarely cite each other; off-target prediction tools (Cas-OFFinder,
  CRISPOR) implement bioinformatics algorithms but are not designed with formal string
  matching complexity bounds in mind.
cross_pollination_opportunities:
  - Apply FM-index and BWT string matching algorithms to CRISPR off-target prediction to achieve O(n + m) time complexity for genome-wide PAM-adjacent search
  - Use CRISPR-based DNA data storage systems that encode binary data as nucleotide strings and use guide RNA sequence matching to retrieve specific data segments
related_unknowns:
  - u-crispr-x-search-and-replace
references:
  - doi: "10.1126/science.1225829"
    note: "Jinek et al. (2012) - A programmable dual-RNA-guided DNA endonuclease in adaptive bacterial immunity; Science 337:816"
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "cross-domain/physics-biology/b-diffusion-limited-aggregation-x-fractal-growth.yaml",
        "content": textwrap.dedent("""\
id: b-diffusion-limited-aggregation-x-fractal-growth
title: >
  Diffusion-limited aggregation x Fractal biological growth — DLA as dendritic morphogenesis
status: proposed
fields:
  - physics
  - biology
  - mathematics
bridge_claim: >
  Diffusion-limited aggregation (DLA) generates fractal cluster morphologies with fractal
  dimension D approximately 1.71 in 2D; branching patterns in snowflakes, lightning,
  coral, and lung bronchial trees all exhibit the same fractal dimension, indicating that
  DLA is the universal growth law for systems where tip growth is diffusion-limited and
  providing a mathematical explanation for fractal biology.
translation_table:
  - field_a_term: diffusion field around DLA cluster (physics)
    field_b_term: morphogen/nutrient gradient around growing biological structure (biology)
    note: Branching morphogenesis is driven by diffusion of signaling molecules or nutrients toward growth tips — the same physics as DLA
  - field_a_term: DLA fractal dimension D = 1.71 in 2D (physics)
    field_b_term: fractal dimension of biological branching networks (biology)
    note: Lung airways, retinal vasculature, and neuronal dendrites exhibit fractal dimensions close to DLA predictions
  - field_a_term: tip instability in DLA (physics)
    field_b_term: lateral inhibition in branching morphogenesis (biology)
    note: DLA tips grow preferentially due to enhanced diffusion field; biological tips are stabilized by lateral inhibition signals (BMP, FGF) creating the same instability
  - field_a_term: DLA cluster growth rate proportional to grad(phi) (physics)
    field_b_term: chemotaxis velocity proportional to morphogen gradient (biology)
    note: Cells grow toward higher morphogen concentration just as DLA clusters grow proportional to the local diffusion flux
communication_gap: >
  Physicists studying DLA since the Witten-Sander (1981) paper and biologists studying
  branching morphogenesis both produce fractal structures but rarely cite each other; the
  connection was made explicit in the 1990s but quantitative comparison of fractal dimensions
  between physical DLA and biological systems is not systematic.
cross_pollination_opportunities:
  - Apply DLA simulation algorithms to predict the fractal dimension of disease-altered vascular networks (diabetic retinopathy, tumor angiogenesis) for diagnostic imaging biomarkers
  - Use DLA universality class theory to identify which biological branching systems are diffusion-limited vs reaction-limited, guiding targeted drug delivery to branch tips
related_unknowns:
  - u-diffusion-limited-aggregation-x-fractal-growth
references:
  - doi: "10.1103/PhysRevLett.47.1400"
    note: "Witten & Sander (1981) - Diffusion-limited aggregation, a kinetic critical phenomenon; Phys Rev Lett 47:1400"
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "cross-domain/math-economics/b-auction-theory-x-mechanism-design.yaml",
        "content": textwrap.dedent("""\
id: b-auction-theory-x-mechanism-design
title: >
  Auction theory x Mechanism design — revenue equivalence as envelope theorem
status: proposed
fields:
  - mathematics
  - economics
  - game-theory
bridge_claim: >
  The revenue equivalence theorem proves that all standard auction formats (English, Dutch,
  sealed-bid first-price, second-price Vickrey) yield the same expected revenue given
  symmetric independent private values; this is a consequence of the envelope theorem in
  mechanism design, connecting auction theory to the calculus of incentive-compatible
  mechanisms and showing that revenue depends only on the allocation rule, not the
  payment rule.
translation_table:
  - field_a_term: second-price (Vickrey) auction (economics)
    field_b_term: incentive-compatible (strategy-proof) mechanism (mechanism design)
    note: Truthful bidding is a dominant strategy in Vickrey auctions; this is the defining property of a strategy-proof direct revelation mechanism
  - field_a_term: bidder's private value v_i (auction theory)
    field_b_term: type in mechanism design (mathematics)
    note: The bidder's private value is their type; mechanism design studies optimal mechanisms over the distribution of types
  - field_a_term: revenue equivalence theorem (auction theory)
    field_b_term: envelope theorem in calculus of variations (mathematics)
    note: Revenue equivalence follows from the envelope theorem applied to the bidder's indirect utility function; only the allocation rule determines expected revenue
  - field_a_term: optimal auction / Myerson auction (economics)
    field_b_term: virtual value function phi(v) = v - (1-F(v))/f(v) (mathematics)
    note: Myerson's optimal auction uses virtual values to characterize the revenue-maximizing allocation rule — a pure mathematical object
communication_gap: >
  Economists developing auction theory and mathematicians developing mechanism design
  and optimal control theory use the same mathematical tools (envelope theorem, revelation
  principle, calculus of variations) but the connection between Myerson's virtual value
  formula and the Pontryagin maximum principle from optimal control theory is rarely
  made explicit in economics textbooks.
cross_pollination_opportunities:
  - Apply mechanism design theory to design truthful resource allocation protocols for cloud computing markets and spectrum auctions with multi-dimensional bidder types
  - Use auction theory revenue equivalence to analyze matching market outcomes (school choice, kidney exchange) and predict when different matching mechanisms yield equivalent outcomes
related_unknowns:
  - u-auction-theory-x-mechanism-design
references:
  - doi: "10.2307/1911865"
    note: "Myerson (1981) - Optimal auction design; Mathematics of Operations Research 6:58"
last_reviewed: "2026-05-07"
"""),
    },
]

UNKNOWNS = [
    {
        "path": "unknowns-catalog/physics/u-simulated-annealing-x-statistical-mechanics.yaml",
        "content": textwrap.dedent("""\
id: u-simulated-annealing-x-statistical-mechanics
title: >
  What cooling schedule guarantees that quantum annealing finds the global optimum faster
  than classical simulated annealing, and for which problem classes does quantum tunneling
  provide exponential speedup?
status: open
priority: high
disciplines:
  - physics
  - computer-science
  - statistical-mechanics
summary: >
  Classical simulated annealing requires logarithmically slow cooling for convergence
  guarantees; quantum annealing uses quantum tunneling instead of thermal fluctuations and
  may escape local minima exponentially faster for certain problem classes. Unknown: what
  is the exact class of optimization problems where quantum tunneling provides provable
  exponential speedup over thermal annealing, what is the optimal annealing schedule for
  quantum devices (adiabatic gap vs diabatic shortcuts), and how do hardware imperfections
  (decoherence, crosstalk) affect the effective quantum advantage?
systematic_gaps:
  - No provable exponential quantum speedup over classical SA has been demonstrated for practical optimization problems
  - Optimal annealing schedule depends on the spectral gap of the problem Hamiltonian, which is generically intractable to compute
  - Threshold theorems for quantum annealing convergence analogous to the classical SA convergence proof are not established
related_bridges:
  - b-simulated-annealing-x-statistical-mechanics
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "unknowns-catalog/mathematics/u-lotka-volterra-x-game-theory.yaml",
        "content": textwrap.dedent("""\
id: u-lotka-volterra-x-game-theory
title: >
  When do multi-species ecological communities admit a Nash equilibrium description,
  and what evolutionary game dynamics predict community assembly and stability?
status: open
priority: medium
disciplines:
  - mathematics
  - ecology
  - evolutionary-biology
summary: >
  Lotka-Volterra and replicator dynamics are equivalent for two-species/two-strategy cases,
  but multi-species communities with complex interaction networks (omnivory, mutualism,
  intransitive competition) do not always map to game-theoretic equilibria. Unknown: what
  is the game-theoretic analog of feasibility and stability conditions in multi-species LV
  systems, can evolutionary game theory predict community assembly trajectories, and how
  does environmental stochasticity affect Nash equilibrium predictions in ecological
  communities?
systematic_gaps:
  - Conditions for existence of evolutionary stable strategies (ESS) in games with more than two strategies and continuous trait spaces are not fully characterized
  - Relationship between LV community matrix eigenvalues and game-theoretic stability conditions is not established in general
  - Empirical tests of replicator dynamics predictions in natural multi-species communities are rare
related_bridges:
  - b-lotka-volterra-x-game-theory
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "unknowns-catalog/physics/u-boltzmann-machine-x-ising-model.yaml",
        "content": textwrap.dedent("""\
id: u-boltzmann-machine-x-ising-model
title: >
  What is the maximum expressive power of energy-based models trained by contrastive
  divergence, and how does the spin glass phase structure of the Ising model constrain
  the representational capacity of deep Boltzmann machines?
status: open
priority: medium
disciplines:
  - physics
  - computer-science
  - statistical-mechanics
summary: >
  The Boltzmann machine training landscape is determined by the free energy landscape of
  the corresponding Ising model; spin glass phases (replica symmetry breaking) create
  exponentially many metastable states that trap contrastive divergence training. Unknown:
  what is the storage capacity of deep Boltzmann machines as a function of architecture
  depth (analogous to Hopfield capacity), at what temperature/hidden unit density does
  the spin glass transition occur, and can renormalization group methods from stat mech
  be used to design better training algorithms?
systematic_gaps:
  - Theoretical storage capacity of deep Boltzmann machines has not been derived analytically
  - Phase structure of the training landscape (glassy vs paramagnetic vs ferromagnetic) is not characterized for modern architectures
  - Connection between replica symmetry breaking and overfitting / memorization in deep learning has not been rigorously established
related_bridges:
  - b-boltzmann-machine-x-ising-model
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "unknowns-catalog/biology/u-membrane-tension-x-laplace-pressure.yaml",
        "content": textwrap.dedent("""\
id: u-membrane-tension-x-laplace-pressure
title: >
  How do cells coordinate cortical tension anisotropy during mitosis to ensure symmetric
  division, and what is the quantitative relationship between cortical tension gradients
  and cleavage furrow positioning?
status: open
priority: medium
disciplines:
  - biology
  - physics
  - biophysics
summary: >
  The Young-Laplace equation predicts cell shape from cortical tension, but during mitosis
  cells must generate precise tension gradients to position the cleavage furrow at the
  equator; the molecular mechanisms that couple spindle pole geometry to cortical tension
  asymmetry are incompletely known. Unknown: what signaling pathways create the equatorial
  cortical tension maximum, how does cell geometry feedback on spindle positioning through
  Laplace pressure, and can the cleavage furrow position be predicted from cortical tension
  measurements?
systematic_gaps:
  - Quantitative measurement of cortical tension spatial distribution during mitosis is limited by resolution of current probes
  - Feedback loop between spindle orientation and cortical tension asymmetry is not fully characterized
  - Effect of cell substrate geometry and confinement on division plane selection is not fully predicted by Laplace pressure theory
related_bridges:
  - b-membrane-tension-x-laplace-pressure
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "unknowns-catalog/mathematics/u-lie-groups-x-symmetry-conservation.yaml",
        "content": textwrap.dedent("""\
id: u-lie-groups-x-symmetry-conservation
title: >
  What are the conservation laws and symmetry structures of non-equilibrium systems, and
  how do Lie group methods extend to time-irreversible and dissipative physical systems?
status: open
priority: medium
disciplines:
  - mathematics
  - physics
  - mathematical-physics
summary: >
  Noether's theorem applies to Lagrangian (time-reversible) systems; non-equilibrium
  systems (dissipative structures, active matter) break time-reversal symmetry and do not
  have standard Noether conservation laws. Unknown: what is the generalization of Noether's
  theorem to dissipative systems (using Onsager reciprocal relations, GENERIC formalism),
  what Lie group structures govern the symmetries of non-equilibrium steady states, and
  how do anomalous symmetries (quantum anomalies) manifest in classical field theories?
systematic_gaps:
  - GENERIC formalism generalizes Noether to dissipative systems but its group-theoretic foundations are not fully developed
  - Classification of symmetry-protected topological phases in non-equilibrium (Floquet) systems using Lie group methods is incomplete
  - Quantum anomalies (chiral anomaly, conformal anomaly) in condensed matter systems lack a complete Lie group classification
related_bridges:
  - b-lie-groups-x-symmetry-conservation
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "unknowns-catalog/computer-science/u-graph-neural-network-x-spectral-graph-theory.yaml",
        "content": textwrap.dedent("""\
id: u-graph-neural-network-x-spectral-graph-theory
title: >
  What is the expressive power of spectral GNNs for distinguishing non-isomorphic graphs,
  and how do spectral filters on graphs generalize to dynamic and hypergraphs?
status: open
priority: medium
disciplines:
  - computer-science
  - mathematics
  - machine-learning
summary: >
  Standard message-passing GNNs are bounded by the 1-WL graph isomorphism test; spectral
  GNNs that use all Laplacian eigenvalues can distinguish more graph pairs but at higher
  computational cost. Unknown: what is the minimal spectral information needed to distinguish
  all non-isomorphic graphs (complete graph spectrum), how do spectral methods generalize
  to dynamic graphs and temporal networks, and can the graph Fourier transform be defined
  consistently for directed and weighted graphs?
systematic_gaps:
  - Expressiveness hierarchy between spectral GNNs (full spectrum) and higher-order WL tests (k-WL) is not fully established
  - Efficient spectral GNN for large graphs requires approximate eigendecomposition; approximation error's effect on expressiveness is not bounded
  - Spectral graph theory for directed graphs lacks a unique canonical Laplacian definition, creating ambiguity in GNN design
related_bridges:
  - b-graph-neural-network-x-spectral-graph-theory
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "unknowns-catalog/biology/u-phylogenetics-x-coalescent-theory.yaml",
        "content": textwrap.dedent("""\
id: u-phylogenetics-x-coalescent-theory
title: >
  How do ancestral recombination graphs (ARGs) scale computationally to whole-genome
  biobank data, and what population history features are identifiable from ARGs but
  not from summary statistics?
status: open
priority: high
disciplines:
  - biology
  - mathematics
  - evolutionary-biology
summary: >
  The coalescent with recombination produces an ancestral recombination graph (ARG) that
  encodes all genealogical relationships across the genome; ARG inference from sequence
  data is computationally expensive and approximate. Unknown: what is the minimum ARG
  complexity (number of recombination events) needed to explain observed haplotype
  patterns, what population history features (bottlenecks, admixture, selection) leave
  distinct ARG signatures, and can ARG inference be made tractable for millions of
  individuals?
systematic_gaps:
  - ARG inference algorithms (ARG-Weaver, Relate, tsinfer) scale poorly beyond 10^4 individuals
  - Statistical tests for distinguishing selective sweeps from neutral demographic events using ARG topology are not established
  - Minimum description length of ARG for given sequence data is not known, limiting compression and inference efficiency
related_bridges:
  - b-phylogenetics-x-coalescent-theory
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "unknowns-catalog/chemistry/u-transition-state-x-saddle-point.yaml",
        "content": textwrap.dedent("""\
id: u-transition-state-x-saddle-point
title: >
  Can machine learning potentials accurately predict transition states and reaction rates
  for chemical reactions not represented in training data, and what training strategies
  ensure extrapolation to high-energy configurations?
status: open
priority: high
disciplines:
  - chemistry
  - physics
  - mathematics
summary: >
  Transition state theory requires accurate potential energy surface (PES) near saddle
  points; machine learning interatomic potentials (MLIPs) trained on equilibrium
  configurations may fail near transition states due to distribution shift. Unknown:
  what active learning strategies ensure MLIP coverage of saddle point regions, how
  can transfer learning from high-level quantum chemistry be used to improve saddle
  point accuracy, and what is the theoretical lower bound on PES error needed for
  accurate rate constant prediction?
systematic_gaps:
  - Active learning protocols for saddle point sampling are not standardized across MLIP frameworks
  - Error propagation from PES uncertainty to rate constant uncertainty is not systematically characterized
  - Transferability of MLIP transition state predictions to new reaction classes is not benchmarked
related_bridges:
  - b-transition-state-x-saddle-point
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "unknowns-catalog/computer-science/u-cellular-automata-x-computational-universality.yaml",
        "content": textwrap.dedent("""\
id: u-cellular-automata-x-computational-universality
title: >
  What is the minimum computational resource (space-time complexity) for a cellular
  automaton to be universal, and are there self-replicating CA rules that are
  computationally simpler than von Neumann's construction?
status: open
priority: medium
disciplines:
  - computer-science
  - physics
  - complexity-science
summary: >
  Von Neumann's self-replicating automaton uses a 29-state rule; simpler universal CAs
  exist (Game of Life, Rule 110) but their self-replication efficiency is unknown.
  Unknown: what is the minimum number of states (alphabet size) for a CA to be Turing
  complete with self-replication, can computationally universal CAs be realized in
  physical systems (reaction-diffusion, molecular arrays), and what is the Kolmogorov
  complexity of the simplest universal CA rule?
systematic_gaps:
  - Minimum state complexity for Turing-complete self-replicating CA is unknown; best known lower bounds are not tight
  - Physical implementation of universal CAs in molecular systems (DNA computing, chemical reaction networks) is not demonstrated
  - Relationship between CA computational universality and the physical notion of computational substrate (Landauer principle) is not formalized
related_bridges:
  - b-cellular-automata-x-computational-universality
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "unknowns-catalog/biology/u-crispr-x-search-and-replace.yaml",
        "content": textwrap.dedent("""\
id: u-crispr-x-search-and-replace
title: >
  What is the theoretical minimum off-target cleavage rate achievable by any CRISPR
  system given the genome size and guide RNA length, and can this bound be achieved
  by engineered Cas variants?
status: open
priority: high
disciplines:
  - biology
  - computer-science
  - molecular-biology
summary: >
  The 20-nt guide RNA can theoretically distinguish a target from all off-targets in a
  3 Gb genome (4^20 >> 3x10^9), but mismatches, RNA secondary structure, and chromatin
  accessibility reduce specificity. Unknown: what is the information-theoretic lower bound
  on off-target cleavage probability for a 20-nt guide in a 3 Gb genome, can multi-guide
  or anti-sense strategies achieve sub-one-in-genome specificity, and how do epigenetic
  marks (DNA methylation, chromatin openness) affect the effective search space?
systematic_gaps:
  - Information-theoretic minimum off-target rate has not been calculated for realistic mismatch tolerance models
  - Off-target sites in heterochromatin are systematically undersampled by current detection methods (GUIDE-seq, CIRCLE-seq)
  - Effect of guide RNA secondary structure on PAM search kinetics is not incorporated in off-target prediction models
related_bridges:
  - b-crispr-x-search-and-replace
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "unknowns-catalog/physics/u-diffusion-limited-aggregation-x-fractal-growth.yaml",
        "content": textwrap.dedent("""\
id: u-diffusion-limited-aggregation-x-fractal-growth
title: >
  Is the fractal dimension of DLA clusters in 3D exactly 2.5, and how does adding
  surface tension or noise to DLA change the universality class of biological
  branching structures?
status: open
priority: medium
disciplines:
  - physics
  - biology
  - mathematics
summary: >
  DLA in 2D has fractal dimension D ≈ 1.71 and in 3D approximately 2.5, but neither
  value has been proven analytically; biological systems deviate from pure DLA due to
  surface tension effects (dendritic solidification), anisotropy (crystalline), and
  reaction-limited growth. Unknown: what is the exact DLA fractal dimension in 2D and
  3D (is it a simple fraction?), how do biological growth modifiers (surface tension,
  anisotropy, feedback) shift the fractal dimension, and can fractal dimension measurements
  diagnose diffusion-limited vs reaction-limited growth in biological tissues?
systematic_gaps:
  - Analytical proof of DLA fractal dimension does not exist; only numerical estimates with ~1% error
  - Crossover between DLA and Eden (reaction-limited) growth universality classes in biological systems is not quantified
  - Effect of flow (advection) on DLA fractal dimension is known to change universality class but biological analogs have not been systematically studied
related_bridges:
  - b-diffusion-limited-aggregation-x-fractal-growth
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "unknowns-catalog/economics/u-auction-theory-x-mechanism-design.yaml",
        "content": textwrap.dedent("""\
id: u-auction-theory-x-mechanism-design
title: >
  What is the optimal mechanism for multi-item auctions with budget-constrained bidders
  and correlated values, and can the Myerson optimal auction be extended to these settings?
status: open
priority: medium
disciplines:
  - mathematics
  - economics
  - game-theory
summary: >
  Myerson's optimal auction applies to single-item auctions with independent private
  values; multi-item settings (spectrum auctions, ad markets) with budget constraints and
  correlated values are much harder. Unknown: what is the revenue-maximizing mechanism for
  multi-item auctions with correlated values (Cremer-McLean requires exponential payments),
  how do budget constraints change the virtual value formula, and can combinatorial auction
  mechanisms be computed in polynomial time?
systematic_gaps:
  - Optimal multi-item mechanism design is computationally intractable in general; best known results are approximate
  - Budget constraints fundamentally break revenue equivalence; optimal budget-feasible mechanisms are not known beyond simple cases
  - Empirical validation of mechanism design predictions in real markets (FCC spectrum auctions, Google ad auctions) is limited by data access
related_bridges:
  - b-auction-theory-x-mechanism-design
last_reviewed: "2026-05-07"
"""),
    },
]

HYPOTHESES = [
    {
        "path": "hypotheses/active/h-simulated-annealing-x-statistical-mechanics.yaml",
        "content": textwrap.dedent("""\
id: h-simulated-annealing-x-statistical-mechanics
title: >
  Quantum annealing on D-Wave hardware achieves polynomial speedup over classical
  simulated annealing for frustrated Ising spin glass problems with chimera graph
  connectivity, detectable through scaling of time-to-solution with problem size
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: high
impact_score: 0.82
author: wave-61-agent
unknowns_addressed:
  - u-simulated-annealing-x-statistical-mechanics
related_disciplines:
  - physics
  - computer-science
  - statistical-mechanics
evidence_links:
  - type: supporting
    doi: "10.1126/science.220.4598.671"
    note: "Kirkpatrick et al. (1983) - Optimization by simulated annealing; foundational SA paper"
    confidence: 0.78
  - type: related
    note: "Boixo et al. (2014) - Evidence for quantum annealing with more than one hundred qubits; Nature Physics 10:218; doi:10.1038/nphys2900"
    confidence: 0.72
proposed_tests:
  - description: Benchmark D-Wave quantum annealer vs parallel tempering simulated annealing on random frustrated Ising problems with chimera connectivity and measure time-to-solution scaling exponent
  - description: Test whether quantum tunneling path in D-Wave quantum annealing corresponds to imaginary-time evolution of Ising Hamiltonian using process tomography on small instances
"""),
    },
    {
        "path": "hypotheses/active/h-lotka-volterra-x-game-theory.yaml",
        "content": textwrap.dedent("""\
id: h-lotka-volterra-x-game-theory
title: >
  Rock-paper-scissors intransitive competition between three bacterial species follows
  replicator dynamics with oscillation period predicted by Lotka-Volterra cycle frequency,
  and spatial structure extends coexistence time beyond well-mixed predictions
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
impact_score: 0.73
author: wave-61-agent
unknowns_addressed:
  - u-lotka-volterra-x-game-theory
related_disciplines:
  - mathematics
  - ecology
  - evolutionary-biology
evidence_links:
  - type: supporting
    doi: "10.1098/rspb.1973.0005"
    note: "Maynard Smith & Price (1973) - The logic of animal conflict; foundational evolutionary game theory"
    confidence: 0.75
  - type: related
    note: "Kerr et al. (2002) - Local dispersal promotes biodiversity in a real-life game of rock-paper-scissors; Nature 418:171; doi:10.1038/nature00823"
    confidence: 0.82
proposed_tests:
  - description: Culture three E. coli strains (toxin producer, resistant, sensitive) in well-mixed and structured (patch) environments and measure oscillation period against Lotka-Volterra cycle time prediction
  - description: Verify that the interior equilibrium of a three-species intransitive system matches the mixed Nash equilibrium of the corresponding rock-paper-scissors game matrix
"""),
    },
    {
        "path": "hypotheses/active/h-boltzmann-machine-x-ising-model.yaml",
        "content": textwrap.dedent("""\
id: h-boltzmann-machine-x-ising-model
title: >
  Restricted Boltzmann machines trained on natural images will develop effective coupling
  constants that exhibit a spin glass phase transition as network size increases,
  with the glass transition temperature inversely related to dataset diversity
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
impact_score: 0.71
author: wave-61-agent
unknowns_addressed:
  - u-boltzmann-machine-x-ising-model
related_disciplines:
  - physics
  - computer-science
  - statistical-mechanics
evidence_links:
  - type: supporting
    doi: "10.1016/S0364-0213(85)80012-4"
    note: "Ackley, Hinton & Sejnowski (1985) - A learning algorithm for Boltzmann machines"
    confidence: 0.72
  - type: related
    note: "Tubiana & Monasson (2017) - Emergence of compositional representations in restricted Boltzmann machines; Phys Rev Lett 118:138301; doi:10.1103/PhysRevLett.118.138301"
    confidence: 0.78
proposed_tests:
  - description: Train RBMs of increasing size on CIFAR-10 and measure the distribution of effective couplings W_ij; test for replica symmetry breaking signature using the Edwards-Anderson order parameter
  - description: Measure the free energy landscape of trained RBMs using parallel tempering and identify glass transition temperature as a function of number of hidden units and dataset size
"""),
    },
    {
        "path": "hypotheses/active/h-membrane-tension-x-laplace-pressure.yaml",
        "content": textwrap.dedent("""\
id: h-membrane-tension-x-laplace-pressure
title: >
  Cortical tension asymmetry during cell division follows the Young-Laplace equation
  quantitatively, and the cleavage furrow position can be predicted from cortical tension
  measurements to within 10% of cell diameter in rounded HeLa cells
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
impact_score: 0.74
author: wave-61-agent
unknowns_addressed:
  - u-membrane-tension-x-laplace-pressure
related_disciplines:
  - biology
  - physics
  - biophysics
evidence_links:
  - type: supporting
    doi: "10.1016/j.cub.2013.05.044"
    note: "Salbreux et al. (2012) - Actin cortex mechanics and cellular morphogenesis"
    confidence: 0.78
  - type: related
    note: "Stewart et al. (2011) - Hydrostatic pressure and the actomyosin cortex drive mitotic cell rounding; Nature 469:226; doi:10.1038/nature09642"
    confidence: 0.80
proposed_tests:
  - description: Measure cortical tension distribution in dividing HeLa cells using atomic force microscopy and compare equatorial-to-polar tension ratio with Young-Laplace furrow position prediction
  - description: Laser ablate the mitotic spindle and measure how cortical tension distribution and cleavage furrow position change, testing whether spindle-cortex tension coupling follows Laplace mechanics
"""),
    },
    {
        "path": "hypotheses/active/h-lie-groups-x-symmetry-conservation.yaml",
        "content": textwrap.dedent("""\
id: h-lie-groups-x-symmetry-conservation
title: >
  Equivariant neural networks that enforce Lie group symmetries will generalize to
  out-of-distribution examples related by symmetry transformations from training data,
  and their generalization gap will scale as the inverse of the group order
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
impact_score: 0.75
author: wave-61-agent
unknowns_addressed:
  - u-lie-groups-x-symmetry-conservation
related_disciplines:
  - mathematics
  - physics
  - mathematical-physics
evidence_links:
  - type: supporting
    doi: "10.1080/00411457108231446"
    note: "Noether (1971 translation) - Invariant variation problems; foundational symmetry-conservation law theorem"
    confidence: 0.80
  - type: related
    note: "Cohen & Welling (2016) - Group equivariant convolutional networks; ICML 2016; arXiv:1602.07576"
    confidence: 0.77
proposed_tests:
  - description: Train SE(3)-equivariant and standard CNNs on molecular property prediction (QM9) with systematic rotation augmentation and measure test performance on rotated vs unrotated molecules
  - description: Measure generalization gap of equivariant networks as a function of symmetry group order (cyclic groups C_n) and test inverse-order scaling prediction
"""),
    },
    {
        "path": "hypotheses/active/h-graph-neural-network-x-spectral-graph-theory.yaml",
        "content": textwrap.dedent("""\
id: h-graph-neural-network-x-spectral-graph-theory
title: >
  GNNs using learned spectral filters over the full graph Laplacian spectrum will
  outperform spatial message-passing GNNs on molecular property prediction tasks
  requiring long-range electronic effects (HOMO-LUMO gap, ionization potential)
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
impact_score: 0.72
author: wave-61-agent
unknowns_addressed:
  - u-graph-neural-network-x-spectral-graph-theory
related_disciplines:
  - computer-science
  - mathematics
  - machine-learning
evidence_links:
  - type: supporting
    doi: "10.48550/arXiv.1609.02907"
    note: "Kipf & Welling (2017) - Semi-supervised classification with GCN; arXiv:1609.02907"
    confidence: 0.75
  - type: related
    note: "Kreuzer et al. (2021) - Rethinking graph transformers with spectral attention; NeurIPS 2021; arXiv:2106.03893"
    confidence: 0.76
proposed_tests:
  - description: Train spectral GNN (using top-k Laplacian eigenvectors as positional encodings) vs spatial MPNN on QM9 molecular dataset and measure MAE for HOMO-LUMO gap prediction
  - description: Analyze learned spectral filter response functions in trained GNNs and verify that long-range properties (dipole moment, HOMO-LUMO) require low-frequency Laplacian modes
"""),
    },
    {
        "path": "hypotheses/active/h-phylogenetics-x-coalescent-theory.yaml",
        "content": textwrap.dedent("""\
id: h-phylogenetics-x-coalescent-theory
title: >
  Ancestral recombination graph inference from UK Biobank whole-genome sequences will
  reveal a European population bottleneck during the Last Glacial Maximum (~20,000 years
  ago) with effective population size below 1,000 individuals, detectable as an
  acceleration in coalescent rate
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
impact_score: 0.74
author: wave-61-agent
unknowns_addressed:
  - u-phylogenetics-x-coalescent-theory
related_disciplines:
  - biology
  - mathematics
  - evolutionary-biology
evidence_links:
  - type: supporting
    doi: "10.1016/0304-4149(82)90011-4"
    note: "Kingman (1982) - The coalescent; Stochastic Processes and their Applications 13:235"
    confidence: 0.82
  - type: related
    note: "Kelleher et al. (2019) - Inferring whole-genome histories in large population datasets; Nature Genetics 51:1330; doi:10.1038/s41588-019-0483-y"
    confidence: 0.78
proposed_tests:
  - description: Apply tsinfer+tsdate to 10,000 UK Biobank whole genomes and measure effective population size trajectory over 100,000 years; compare to PSMC estimates
  - description: Test whether coalescent rate acceleration at LGM is detectable as a significant excess of coalescent events in the 15,000-25,000 year time window relative to flanking periods
"""),
    },
    {
        "path": "hypotheses/active/h-transition-state-x-saddle-point.yaml",
        "content": textwrap.dedent("""\
id: h-transition-state-x-saddle-point
title: >
  Machine learning interatomic potentials trained with active learning on transition state
  configurations will predict reaction rate constants within a factor of 2 of gold-standard
  CCSD(T) calculations for a benchmark set of 20 gas-phase reactions
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: high
impact_score: 0.80
author: wave-61-agent
unknowns_addressed:
  - u-transition-state-x-saddle-point
related_disciplines:
  - chemistry
  - physics
  - mathematics
evidence_links:
  - type: supporting
    doi: "10.1063/1.1749604"
    note: "Eyring (1935) - The activated complex in chemical reactions; foundational TST"
    confidence: 0.80
  - type: related
    note: "Batatia et al. (2022) - MACE: Higher order equivariant message passing neural networks for fast and accurate force fields; NeurIPS 2022; arXiv:2206.07697"
    confidence: 0.77
proposed_tests:
  - description: Train MACE MLIP on DFT reference data augmented by transition state configurations found via NEB algorithm; evaluate on CCSD(T) reaction rate benchmark (BH9 dataset)
  - description: Measure correlation between MLIP potential energy at transition state and CCSD(T) activation energy for diverse reaction classes (H-abstraction, cyclization, elimination)
"""),
    },
    {
        "path": "hypotheses/active/h-cellular-automata-x-computational-universality.yaml",
        "content": textwrap.dedent("""\
id: h-cellular-automata-x-computational-universality
title: >
  A 3-state 1D cellular automaton with a local neighborhood of 3 cells is sufficient
  for Turing universality with self-replication, establishing a new lower bound on
  the minimum computational complexity for physical self-replication
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
impact_score: 0.70
author: wave-61-agent
unknowns_addressed:
  - u-cellular-automata-x-computational-universality
related_disciplines:
  - computer-science
  - physics
  - complexity-science
evidence_links:
  - type: supporting
    doi: "10.1002/cplx.6130010405"
    note: "Wolfram (1984) - Universality and complexity in cellular automata; Physica D 10:1"
    confidence: 0.75
  - type: related
    note: "Cook (2004) - Universality in elementary cellular automata; Complex Systems 15:1"
    confidence: 0.82
proposed_tests:
  - description: Systematically search all 3-state 3-neighbor 1D CA rules for self-replicating patterns using automated evolutionary search and identify rules exhibiting unbounded complexity
  - description: Map any identified 3-state universal CA to a chemical reaction network to establish physical realizability and compute minimal molecular implementation
"""),
    },
    {
        "path": "hypotheses/active/h-crispr-x-search-and-replace.yaml",
        "content": textwrap.dedent("""\
id: h-crispr-x-search-and-replace
title: >
  Designing guide RNAs with maximum Levenshtein distance from all off-target sites in
  the human genome using FM-index string matching will reduce off-target cleavage by
  at least 10-fold compared to guides designed by conventional seed-region matching alone
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: high
impact_score: 0.79
author: wave-61-agent
unknowns_addressed:
  - u-crispr-x-search-and-replace
related_disciplines:
  - biology
  - computer-science
  - molecular-biology
evidence_links:
  - type: supporting
    doi: "10.1126/science.1225829"
    note: "Jinek et al. (2012) - A programmable dual-RNA-guided DNA endonuclease; founding CRISPR-Cas9 paper"
    confidence: 0.82
  - type: related
    note: "Hsu et al. (2013) - DNA targeting specificity of RNA-guided Cas9 nucleases; Nature Biotechnology 31:827; doi:10.1038/nbt.2647"
    confidence: 0.79
proposed_tests:
  - description: Design 10 guide RNAs targeting VEGFA using FM-index maximum-distance criterion and compare off-target cleavage frequency to seed-match guides by GUIDE-seq in HEK293 cells
  - description: Verify that FM-index search identifies all GUIDE-seq-validated off-target sites and test whether Levenshtein distance to the nearest off-target site correlates with observed cleavage frequency
"""),
    },
    {
        "path": "hypotheses/active/h-diffusion-limited-aggregation-x-fractal-growth.yaml",
        "content": textwrap.dedent("""\
id: h-diffusion-limited-aggregation-x-fractal-growth
title: >
  The fractal dimension of retinal vasculature in diabetic retinopathy will decrease
  measurably from the healthy DLA baseline (D ≈ 1.71) in proportion to the severity
  of vascular regression, providing a non-invasive diagnostic biomarker
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: high
impact_score: 0.78
author: wave-61-agent
unknowns_addressed:
  - u-diffusion-limited-aggregation-x-fractal-growth
related_disciplines:
  - physics
  - biology
  - mathematics
evidence_links:
  - type: supporting
    doi: "10.1103/PhysRevLett.47.1400"
    note: "Witten & Sander (1981) - Diffusion-limited aggregation; foundational DLA paper"
    confidence: 0.78
  - type: related
    note: "Daxer (1993) - The fractal geometry of proliferative diabetic retinopathy; Invest Ophthalmol Vis Sci 34:2197"
    confidence: 0.74
proposed_tests:
  - description: Measure fractal dimension of retinal vasculature in 100 diabetic and 100 healthy subjects by box-counting of fundus photographs and test for correlation with HbA1c and retinopathy grade
  - description: Compare fractal dimension trajectories over 5-year follow-up between patients with progressive vs stable retinopathy to test whether D decrease precedes clinical diagnosis
"""),
    },
    {
        "path": "hypotheses/active/h-auction-theory-x-mechanism-design.yaml",
        "content": textwrap.dedent("""\
id: h-auction-theory-x-mechanism-design
title: >
  Second-price combinatorial auctions with item complementarities will achieve at least
  63% of optimal social welfare in polynomial time via the greedy algorithm, and this
  bound is tight for submodular valuation functions
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
impact_score: 0.72
author: wave-61-agent
unknowns_addressed:
  - u-auction-theory-x-mechanism-design
related_disciplines:
  - mathematics
  - economics
  - game-theory
evidence_links:
  - type: supporting
    doi: "10.2307/1911865"
    note: "Myerson (1981) - Optimal auction design; Mathematics of Operations Research 6:58"
    confidence: 0.80
  - type: related
    note: "Lehmann et al. (2002) - Truth revelation in approximately efficient combinatorial auctions; J ACM 49:577; doi:10.1145/585265.585267"
    confidence: 0.75
proposed_tests:
  - description: Implement greedy combinatorial auction with posted prices and measure realized social welfare ratio on spectrum auction instances from FCC CBRS band data
  - description: Generate 1000 random submodular valuation instances and measure the empirical welfare ratio distribution, testing whether the 1-1/e = 0.632 bound is achieved on average
"""),
    },
]


def write_file(path_str: str, content: str) -> None:
    path = ROOT / path_str
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"  wrote {path_str}")


if __name__ == "__main__":
    print("Writing Wave 61 bridges...")
    for item in BRIDGES:
        write_file(item["path"], item["content"])
    print("Writing Wave 61 unknowns...")
    for item in UNKNOWNS:
        write_file(item["path"], item["content"])
    print("Writing Wave 61 hypotheses...")
    for item in HYPOTHESES:
        write_file(item["path"], item["content"])
    print(f"Done: {len(BRIDGES)} bridges, {len(UNKNOWNS)} unknowns, {len(HYPOTHESES)} hypotheses")

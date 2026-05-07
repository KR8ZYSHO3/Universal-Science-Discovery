#!/usr/bin/env python3
"""Generate all Wave 60 bridge, unknown, and hypothesis YAML files."""
from pathlib import Path
import textwrap

ROOT = Path(__file__).parent

BRIDGES = [
    {
        "path": "cross-domain/physics-cs/b-quantum-error-correction-x-topological-codes.yaml",
        "content": textwrap.dedent("""\
id: b-quantum-error-correction-x-topological-codes
title: >
  Quantum error correction x Topological codes — anyons as logical qubits
status: proposed
fields:
  - physics
  - computer-science
  - quantum-information
bridge_claim: >
  Topological quantum error correction (surface codes, toric codes) encodes logical qubits
  in the global topology of anyon configurations; logical errors require macroscopic anyon
  movement, making decoherence exponentially suppressed in system size — the same topological
  protection that makes quantum Hall edge states robust against local perturbations.
translation_table:
  - field_a_term: anyon braiding (condensed matter physics)
    field_b_term: logical gate on topological qubit (quantum computing)
    note: Non-abelian anyon worldline braids implement fault-tolerant quantum gates without external control pulses
  - field_a_term: topological ground state degeneracy (physics)
    field_b_term: logical qubit Hilbert space (quantum computing)
    note: The 2^k-fold degenerate ground state of a toric code encodes k logical qubits protected by the energy gap
  - field_a_term: anyon pair creation energy gap Δ (physics)
    field_b_term: code distance d (quantum error correction)
    note: The energy gap suppresses thermal anyon creation; code distance quantifies how many physical errors must occur for a logical error
  - field_a_term: quantum Hall edge state (condensed matter)
    field_b_term: topologically protected logical channel (quantum computing)
    note: Both are immune to local perturbations by virtue of topological invariance of the bulk
communication_gap: >
  Condensed matter physicists studying fractional quantum Hall states and computer scientists
  designing fault-tolerant quantum algorithms share mathematics (topological field theory,
  category theory of anyons) but publish in disjoint journals (Physical Review Letters vs
  Quantum Information & Computation), causing slow cross-pollination of experimental insights.
cross_pollination_opportunities:
  - Leverage fractional quantum Hall material engineering to realize physical anyon platforms for topological quantum computers
  - Apply quantum error correction distance bounds to estimate minimum system sizes required for observable non-abelian anyon statistics in condensed matter experiments
related_unknowns:
  - u-quantum-error-correction-x-topological-codes
references:
  - doi: "10.1103/RevModPhys.80.1083"
    note: "Nayak et al. (2008) - Non-abelian anyons and topological quantum computation; Rev Mod Phys 80:1083"
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "cross-domain/biology-math/b-developmental-gradient-x-pde.yaml",
        "content": textwrap.dedent("""\
id: b-developmental-gradient-x-pde
title: >
  Developmental gradients x Reaction-diffusion PDE — morphogen as chemical wave
status: proposed
fields:
  - biology
  - mathematics
  - developmental-biology
bridge_claim: >
  Turing's reaction-diffusion mechanism (1952) generates spatial patterns in morphogen
  concentration gradients that specify body axis patterning in embryos; stripe width, spot
  size, and axis polarity are determined by the ratio of diffusion coefficients and reaction
  rates — a purely mathematical prediction later confirmed in Drosophila Bicoid gradients
  and zebrafish pigmentation.
translation_table:
  - field_a_term: morphogen gradient (developmental biology)
    field_b_term: activator-inhibitor concentration field (mathematics)
    note: The morphogen acts as an activator whose local production is balanced by a faster-diffusing inhibitor, producing stable spatial patterns
  - field_a_term: body axis specification (biology)
    field_b_term: symmetry breaking in reaction-diffusion PDE (mathematics)
    note: A homogeneous steady state becomes unstable to spatial perturbations (Turing instability) at a critical diffusion ratio, selecting a preferred wavelength
  - field_a_term: stripe or spot pattern wavelength (biology)
    field_b_term: dominant unstable mode of linearized PDE (mathematics)
    note: Pattern scale is set by sqrt(D_inhibitor/D_activator) times reaction rate constants — a purely mathematical prediction
communication_gap: >
  Developmental biologists working on morphogenesis and applied mathematicians studying PDEs
  share the Turing framework but the experimental confirmation of Turing patterns in vertebrate
  development came 60 years after the 1952 prediction, partly due to disciplinary siloing.
cross_pollination_opportunities:
  - Use PDE parameter estimation from measured morphogen profiles to infer biophysical parameters (diffusion rates, reaction kinetics) in living embryos
  - Design synthetic genetic circuits that implement tunable reaction-diffusion modules for programmable tissue patterning in bioengineering
related_unknowns:
  - u-developmental-gradient-x-pde
references:
  - doi: "10.1098/rstb.1952.0012"
    note: "Turing (1952) - The chemical basis of morphogenesis; Phil Trans R Soc B 237:37"
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "cross-domain/cs-math/b-compressed-sensing-x-sparse-recovery.yaml",
        "content": textwrap.dedent("""\
id: b-compressed-sensing-x-sparse-recovery
title: >
  Compressed sensing x Sparse signal recovery — underdetermined systems and L1 minimization
status: proposed
fields:
  - computer-science
  - mathematics
  - signal-processing
bridge_claim: >
  Compressed sensing proves that a sparse signal in R^n can be exactly recovered from
  O(k log n) random linear measurements (far fewer than n) by L1 minimization; this connects
  the restricted isometry property (RIP) of random matrices to convex optimization geometry,
  enabling MRI acceleration by 10x and single-pixel camera architectures.
translation_table:
  - field_a_term: sparsity k in signal space (signal processing)
    field_b_term: number of non-zero coefficients in a basis (mathematics)
    note: A signal is k-sparse if at most k of its n basis coefficients are nonzero; sparsity is the key structural assumption
  - field_a_term: random measurement matrix Φ (compressed sensing)
    field_b_term: random linear map satisfying RIP (mathematics)
    note: Gaussian or Bernoulli random matrices satisfy the RIP with overwhelming probability, guaranteeing recovery
  - field_a_term: L1 minimization / LASSO (optimization)
    field_b_term: convex relaxation of L0 sparse constraint (mathematics)
    note: L1 is the tightest convex surrogate for sparsity; the L1 ball's geometry causes solutions to be corner-sparse
communication_gap: >
  Signal processing engineers and pure mathematicians studying convex geometry worked in
  isolation until Candès, Romberg, and Tao (2006) and Donoho (2006) simultaneously showed
  that L1 minimization achieves exact sparse recovery — a result with implications neither
  community had fully anticipated.
cross_pollination_opportunities:
  - Apply compressed sensing theory to accelerate MRI protocols by designing non-Cartesian k-space sampling patterns that satisfy RIP conditions
  - Use sparse recovery algorithms to solve inverse problems in tomography, seismology, and astronomical imaging where measurement budgets are limited
related_unknowns:
  - u-compressed-sensing-x-sparse-recovery
references:
  - doi: "10.1109/TIT.2006.871582"
    note: "Candès & Tao (2006) - Near-optimal signal recovery from random projections; IEEE Trans Inf Theory 52:5406"
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "cross-domain/chemistry-biology/b-enzyme-kinetics-x-michaelis-menten.yaml",
        "content": textwrap.dedent("""\
id: b-enzyme-kinetics-x-michaelis-menten
title: >
  Enzyme kinetics x Michaelis-Menten — substrate saturation as queueing theory
status: proposed
fields:
  - chemistry
  - biology
  - mathematics
bridge_claim: >
  The Michaelis-Menten enzyme saturation curve is mathematically identical to an M/M/1
  queueing model where the enzyme is the server, substrate molecules are customers, and
  kcat is the service rate; enzyme inhibition kinetics map to different queueing disciplines
  (priority queues for competitive inhibition), unifying biochemistry with operations research.
translation_table:
  - field_a_term: enzyme active site (biochemistry)
    field_b_term: server in M/M/1 queue (queueing theory)
    note: The enzyme processes one substrate at a time; Km is the dissociation constant analogous to the arrival-to-service rate ratio
  - field_a_term: Km (Michaelis constant, biochemistry)
    field_b_term: traffic intensity ρ = λ/μ (queueing theory)
    note: Km sets the substrate concentration for half-maximal velocity, equivalent to the load factor at which the queue becomes saturated
  - field_a_term: competitive inhibition (biochemistry)
    field_b_term: priority queueing discipline (queueing theory)
    note: Competitive inhibitor occupies the active site with higher priority than substrate, blocking service — exactly a priority queue
  - field_a_term: kcat/Km (catalytic efficiency, biochemistry)
    field_b_term: throughput per unit load (operations research)
    note: Diffusion-limited enzymes achieve kcat/Km near 10^8-10^9 M^-1 s^-1, the theoretical queueing throughput maximum
communication_gap: >
  Biochemists derive the Michaelis-Menten equation from chemical kinetics (rapid equilibrium
  or steady-state assumptions) without recognizing the isomorphism to queueing theory; operations
  researchers are unaware that their algorithms have direct biochemical analogs, blocking
  potential cross-fertilization in metabolic engineering and network pharmacology.
cross_pollination_opportunities:
  - Apply queueing network theory to model metabolic flux in multi-enzyme pathways as a network of coupled queues, enabling bottleneck identification
  - Use enzyme kinetics parameter estimation techniques to fit queueing models in biological systems such as ribosomes translating mRNA
related_unknowns:
  - u-enzyme-kinetics-x-michaelis-menten
references:
  - doi: "10.1111/j.1432-1033.1994.tb18811.x"
    note: "Heinrich & Schuster (1994) - The regulation of cellular systems; European J Biochemistry"
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "cross-domain/physics-math/b-topological-defects-x-homotopy.yaml",
        "content": textwrap.dedent("""\
id: b-topological-defects-x-homotopy
title: >
  Topological defects x Homotopy groups — vortices classified by pi_1
status: proposed
fields:
  - physics
  - mathematics
  - condensed-matter-physics
bridge_claim: >
  The classification of topological defects in ordered media (vortices in superfluids,
  dislocations in crystals, monopoles in spin textures) is governed by the homotopy groups
  of the order parameter space; pi_1 classifies line defects (vortices), pi_2 classifies
  point defects (hedgehogs), and pi_3 classifies textures (skyrmions) — a complete
  mathematical taxonomy from algebraic topology.
translation_table:
  - field_a_term: vortex in superfluid (physics)
    field_b_term: element of first homotopy group pi_1(S^1) = Z (mathematics)
    note: A superfluid vortex carries quantized circulation; the winding number is an integer element of pi_1
  - field_a_term: magnetic monopole or hedgehog defect (physics)
    field_b_term: element of pi_2(S^2) = Z (mathematics)
    note: A hedgehog point defect in a 3D vector field has integer topological charge classified by pi_2
  - field_a_term: topological stability of defect (physics)
    field_b_term: non-trivial element of homotopy group (mathematics)
    note: A defect is topologically stable if and only if it corresponds to a non-identity element of the relevant homotopy group
  - field_a_term: defect annihilation (physics)
    field_b_term: group multiplication to identity in pi_n (mathematics)
    note: Two defects can annihilate if and only if their homotopy group elements multiply to the identity
communication_gap: >
  Condensed matter physicists discovering vortex quantization and topological defects in the
  1960s-70s were largely unaware of the existing homotopy theory in mathematics; the Kibble-Zurek
  mechanism and defect topology were developed independently before Mermin's 1979 review
  unified the framework.
cross_pollination_opportunities:
  - Use homotopy group calculations to predict and catalog all possible topological defect types in newly discovered ordered phases (topological semimetals, magnetic skyrmion lattices)
  - Apply topological defect classification to design defect-tolerant materials where controlled defect populations enable functional properties
related_unknowns:
  - u-topological-defects-x-homotopy
references:
  - doi: "10.1103/RevModPhys.51.591"
    note: "Mermin (1979) - The topological theory of defects in ordered media; Rev Mod Phys 51:591"
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "cross-domain/biology-physics/b-hair-cell-bundle-x-hopf-bifurcation.yaml",
        "content": textwrap.dedent("""\
id: b-hair-cell-bundle-x-hopf-bifurcation
title: >
  Hair cell bundle x Hopf bifurcation — auditory amplification at the edge of oscillation
status: proposed
fields:
  - neuroscience
  - physics
  - biophysics
bridge_claim: >
  The inner ear hair cell bundle operates at a Hopf bifurcation point, producing active
  mechanical amplification with a characteristic 1/3 power compression and sharp frequency
  selectivity; this is the same nonlinear dynamics as a laser at threshold and is responsible
  for the ear's extraordinary sensitivity (~1 Angstrom displacement detection) and spontaneous
  otoacoustic emissions.
translation_table:
  - field_a_term: hair cell bundle spontaneous oscillation (neuroscience)
    field_b_term: limit cycle near Hopf bifurcation point (nonlinear dynamics)
    note: The bundle oscillates spontaneously below threshold; this is the hallmark of a system at a supercritical Hopf bifurcation
  - field_a_term: 1/3 power compression in auditory response (auditory neuroscience)
    field_b_term: cube-root response of driven Hopf oscillator (dynamical systems)
    note: Driven at a Hopf bifurcation, amplitude scales as stimulus^(1/3) — the mathematical origin of auditory compression
  - field_a_term: frequency selectivity / Q factor (auditory physics)
    field_b_term: sharpness of resonance at bifurcation (nonlinear dynamics)
    note: The Hopf bifurcation maximally sharpens frequency tuning while maintaining amplitude sensitivity simultaneously
communication_gap: >
  Auditory neuroscientists measuring hair cell mechanics and physicists studying nonlinear
  oscillator theory developed parallel frameworks; the identification of the Hopf bifurcation
  as the operating principle of hearing occurred in 2000 and cross-disciplinary collaboration
  between biophysicists and nonlinear dynamicists remains limited.
cross_pollination_opportunities:
  - Design artificial cochlea sensors that exploit Hopf bifurcation dynamics for broadband frequency-selective mechanosensing at low power
  - Apply Hopf bifurcation theory to understand how hearing loss (hair cell damage) shifts the operating point away from the critical point, degrading compression
related_unknowns:
  - u-hair-cell-bundle-x-hopf-bifurcation
references:
  - doi: "10.1073/pnas.97.7.3183"
    note: "Camalet et al. (2000) - Auditory sensitivity provided by self-tuned critical oscillations of hair cells; PNAS 97:3183"
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "cross-domain/cs-biology/b-genetic-algorithm-x-natural-selection.yaml",
        "content": textwrap.dedent("""\
id: b-genetic-algorithm-x-natural-selection
title: >
  Genetic algorithms x Natural selection — evolution as optimization
status: proposed
fields:
  - computer-science
  - biology
  - evolutionary-biology
bridge_claim: >
  Genetic algorithms (mutation, crossover, selection on fitness) are a direct mathematical
  abstraction of natural selection; Holland's schema theorem proves that GAs implicitly
  sample an exponential number of schemata simultaneously (building block hypothesis),
  explaining why evolution efficiently searches high-dimensional fitness landscapes that
  are intractable for gradient-based methods.
translation_table:
  - field_a_term: chromosome / binary string (genetic algorithm)
    field_b_term: genome / DNA sequence (evolutionary biology)
    note: The GA chromosome encodes a solution; the biological genome encodes a phenotype — both are subject to heritable variation
  - field_a_term: fitness function f(x) (genetic algorithm)
    field_b_term: reproductive fitness W (biology)
    note: Selection pressure in both cases preferentially propagates high-fitness individuals; the fitness landscape concept is shared
  - field_a_term: crossover / recombination operator (GA)
    field_b_term: sexual recombination / meiosis (biology)
    note: Both shuffle genetic material between parent solutions, generating novel combinations unexplored by single-parent variation
  - field_a_term: schema / building block (GA theory)
    field_b_term: linkage disequilibrium / epistatic block (population genetics)
    note: Schemata with above-average fitness grow exponentially; analogous to favorable haplotype blocks spreading in a population
communication_gap: >
  Computer scientists developing GAs from the 1960s-70s drew explicit inspiration from
  biology but the mathematical formalism (schema theorem, No Free Lunch) diverged from
  population genetics (Price equation, Fisher's fundamental theorem); cross-disciplinary
  collaboration between EC researchers and evolutionary biologists is growing but remains
  fragmented.
cross_pollination_opportunities:
  - Apply GA schema theory to identify minimal functional gene modules in synthetic biology circuits that are robust to mutational perturbation
  - Use population genetics' coalescent theory to analyze convergence and diversity maintenance in large-scale evolutionary computation
related_unknowns:
  - u-genetic-algorithm-x-natural-selection
references:
  - doi: "10.1016/0004-3702(94)90132-5"
    note: "Mitchell et al. (1994) - When will a genetic algorithm outperform hill climbing? A survey; AI Journal"
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "cross-domain/physics-economics/b-blackscholes-x-diffusion-equation.yaml",
        "content": textwrap.dedent("""\
id: b-blackscholes-x-diffusion-equation
title: >
  Black-Scholes x Heat diffusion equation — option pricing as Brownian motion
status: proposed
fields:
  - economics
  - physics
  - mathematics
bridge_claim: >
  The Black-Scholes partial differential equation for option pricing is mathematically
  identical to the heat diffusion equation after a change of variables; option price maps
  to temperature, log-price maps to position, and volatility squared maps to thermal
  diffusivity — enabling physicists' Green's function methods and Fourier analysis to
  price financial derivatives analytically.
translation_table:
  - field_a_term: option price C(S,t) (finance)
    field_b_term: temperature field T(x,t) (heat equation)
    note: After the substitution tau = T-t, x = ln(S/K), the Black-Scholes PDE becomes the standard heat equation
  - field_a_term: volatility sigma (finance)
    field_b_term: sqrt(2 * thermal diffusivity) (physics)
    note: Volatility sets the rate at which the probability distribution of log-prices spreads, exactly as thermal diffusivity spreads heat
  - field_a_term: risk-neutral pricing measure Q (finance)
    field_b_term: Feynman-Kac path integral (physics)
    note: The risk-neutral expectation of discounted payoff is the path-integral solution to the heat equation with appropriate boundary conditions
  - field_a_term: Black-Scholes delta hedge (finance)
    field_b_term: gradient of temperature field (physics)
    note: The delta (dC/dS) plays the role of the temperature gradient in the heat equation formulation
communication_gap: >
  Financial economists derived Black-Scholes in 1973 using Ito calculus without recognizing
  the heat equation equivalence; physicists independently applied diffusion theory to finance
  (econophysics) from the 1990s, creating a second derivation tradition that financial
  professionals were slow to adopt despite its computational advantages.
cross_pollination_opportunities:
  - Apply physics heat kernel methods (Green's functions for complex geometries) to price path-dependent options with barriers and complex payoff structures
  - Use statistical physics of non-equilibrium systems to model fat-tailed return distributions beyond Black-Scholes Gaussian assumptions
related_unknowns:
  - u-blackscholes-x-diffusion-equation
references:
  - doi: "10.1086/260062"
    note: "Black & Scholes (1973) - The pricing of options and corporate liabilities; J Political Economy 81:637"
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "cross-domain/math-physics/b-random-walk-x-brownian-motion.yaml",
        "content": textwrap.dedent("""\
id: b-random-walk-x-brownian-motion
title: >
  Random walk x Brownian motion — discrete to continuum limit
status: proposed
fields:
  - mathematics
  - physics
  - probability-theory
bridge_claim: >
  The continuum limit of a symmetric random walk on a lattice is Brownian motion (Wiener
  process); Donsker's invariance principle (functional central limit theorem) proves that
  this convergence holds universally for any finite-variance step distribution, unifying
  discrete combinatorics with continuous stochastic calculus and underlying polymer physics,
  financial modeling, and diffusion-limited aggregation.
translation_table:
  - field_a_term: random walk step on lattice (combinatorics)
    field_b_term: Wiener process increment dW_t (stochastic calculus)
    note: In the limit of small step size and time, the random walk distribution converges to the Gaussian distribution of Brownian increments
  - field_a_term: number of steps N (combinatorics)
    field_b_term: continuous time t (stochastic calculus)
    note: Rescaling by N^(1/2) in space and N in time yields the continuum limit; this is Donsker's theorem
  - field_a_term: Pascal's triangle / binomial distribution (combinatorics)
    field_b_term: Gaussian heat kernel / Green's function (PDE theory)
    note: The binomial distribution of random walk positions converges to the Gaussian under CLT, which is the fundamental solution of the diffusion equation
  - field_a_term: self-avoiding random walk (combinatorics / polymer physics)
    field_b_term: excluded volume polymer conformation statistics (physics)
    note: Self-avoiding walk exponent nu = 3/5 (Flory) deviates from nu = 1/2 for Brownian motion, capturing polymer swelling
communication_gap: >
  Probabilists studying random walks and physicists studying Brownian motion developed
  parallel mathematical frameworks; Donsker's 1951 theorem providing the rigorous convergence
  proof was not widely cited in physics literature until the development of stochastic calculus
  in finance made the connection essential.
cross_pollination_opportunities:
  - Apply functional central limit theorem universality to prove that mesoscopic physical systems (colloidal particles, polymer chains) obey Brownian motion despite microscopic details
  - Use random walk lattice algorithms to compute Green's functions for diffusion problems in complex geometries that are intractable analytically
related_unknowns:
  - u-random-walk-x-brownian-motion
references:
  - doi: "10.1090/S0002-9947-1951-0040613-0"
    note: "Donsker (1951) - An invariance principle for certain probability limit theorems; Mem AMS 6:1"
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "cross-domain/biology-cs/b-neural-spike-coding-x-information-compression.yaml",
        "content": textwrap.dedent("""\
id: b-neural-spike-coding-x-information-compression
title: >
  Neural spike coding x Information compression — retinal ganglion cells as efficient encoders
status: proposed
fields:
  - neuroscience
  - computer-science
  - information-theory
bridge_claim: >
  Retinal ganglion cell spike trains are efficient codes in the information-theoretic sense;
  center-surround receptive fields implement a whitening filter that removes spatial redundancy
  in natural images, maximizing mutual information per spike — a biological implementation of
  principal component analysis that inspired sparse coding and ICA algorithms in machine learning.
translation_table:
  - field_a_term: center-surround receptive field (retinal neuroscience)
    field_b_term: whitening / decorrelation filter (signal processing)
    note: The difference-of-Gaussians RF profile is the optimal linear filter for removing second-order spatial correlations in natural images
  - field_a_term: retinal ganglion cell spike rate (neuroscience)
    field_b_term: efficient code / compressed representation (information theory)
    note: Ganglion cells allocate more spikes to unexpected (high-information) features; sparse coding maximizes mutual information per action potential
  - field_a_term: lateral inhibition in retina (neuroscience)
    field_b_term: redundancy reduction (information theory)
    note: Lateral inhibition suppresses responses to spatially correlated (redundant) inputs, implementing Barlow's efficient coding hypothesis
communication_gap: >
  Neurophysiologists studying retinal circuits and information theorists studying source
  coding developed parallel frameworks; Barlow's efficient coding hypothesis (1961) bridged
  them conceptually but quantitative testing required natural image statistics measurements
  that became practical only in the 1990s.
cross_pollination_opportunities:
  - Design artificial retinal prostheses whose spike coding schemes are optimized for natural image statistics rather than uniform sampling grids
  - Apply efficient neural coding principles to design energy-efficient edge AI sensors that transmit only informative events (event cameras)
related_unknowns:
  - u-neural-spike-coding-x-information-compression
references:
  - doi: "10.1038/381520a0"
    note: "Olshausen & Field (1996) - Emergence of simple-cell receptive field properties by learning a sparse code for natural images; Nature 381:607"
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "cross-domain/physics-biology/b-liquid-crystal-x-cell-membrane.yaml",
        "content": textwrap.dedent("""\
id: b-liquid-crystal-x-cell-membrane
title: >
  Liquid crystals x Cell membranes — lipid bilayer as smectic-A phase
status: proposed
fields:
  - physics
  - biology
  - biophysics
bridge_claim: >
  The lipid bilayer cell membrane is a biological realization of a smectic-A liquid crystal;
  membrane fluidity, phase transitions (lipid rafts, gel-to-fluid transition), and curvature
  elasticity are all governed by the same Frank elastic energy that describes liquid crystal
  defects and alignments — making liquid crystal physics the natural framework for membrane
  mechanics and cell shape.
translation_table:
  - field_a_term: smectic-A layered order (liquid crystal physics)
    field_b_term: lipid bilayer lamellar structure (cell biology)
    note: The bilayer's two leaflets correspond to the smectic-A layers; amphiphile self-assembly is driven by the same hydrophobic packing that drives smectic order
  - field_a_term: Frank elastic constants K1, K2, K3 (liquid crystal physics)
    field_b_term: Helfrich bending modulus kappa (membrane biophysics)
    note: Membrane curvature elasticity is the biological analog of Frank elastic energy; kappa ~ 10-20 kBT is the bending rigidity
  - field_a_term: liquid crystal phase transition (Tc) (physics)
    field_b_term: lipid raft formation / gel-fluid transition (cell biology)
    note: Lipid phase separation into ordered (Lo) and disordered (Ld) domains mirrors liquid crystal isotropic-nematic transitions
  - field_a_term: topological defects in liquid crystal (physics)
    field_b_term: membrane curvature singularities / buds (biology)
    note: Defects in membrane lipid order correspond to sites of curvature generation (endocytosis, filopodia)
communication_gap: >
  Liquid crystal physicists and membrane biophysicists use identical mathematical frameworks
  (Frank elastic energy, order parameter fields) but publish in different journals; the field
  of active matter has begun bridging them, but quantitative cross-disciplinary experiments
  remain rare.
cross_pollination_opportunities:
  - Apply liquid crystal defect engineering principles to design biomimetic membranes with programmable curvature patterns for synthetic cell manufacturing
  - Use liquid crystal optical microscopy techniques (polarized light, fluorescence anisotropy) to quantify lipid order parameters in living cell membranes
related_unknowns:
  - u-liquid-crystal-x-cell-membrane
references:
  - doi: "10.1103/RevModPhys.46.617"
    note: "de Gennes (1974) - The physics of liquid crystals; Rev Mod Phys 46:617"
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "cross-domain/math-cs/b-fourier-transform-x-signal-processing.yaml",
        "content": textwrap.dedent("""\
id: b-fourier-transform-x-signal-processing
title: >
  Fourier transform x Signal processing — frequency domain as dual representation
status: proposed
fields:
  - mathematics
  - computer-science
  - signal-processing
bridge_claim: >
  The discrete Fourier transform (DFT) and its fast algorithm (FFT) provide an exact dual
  representation of any finite signal in the frequency domain; the convolution theorem
  (multiplication in frequency = convolution in time) reduces O(n^2) correlation to O(n log n)
  FFT — the mathematical backbone of all digital signal processing, communications, and
  numerical PDE solvers.
translation_table:
  - field_a_term: DFT frequency bin X[k] (signal processing)
    field_b_term: Fourier coefficient in orthonormal basis expansion (mathematics)
    note: The DFT decomposes a signal into complex exponential basis functions; this is an exact isometry (Parseval's theorem)
  - field_a_term: convolution in time domain (signal processing)
    field_b_term: pointwise multiplication in frequency domain (mathematics)
    note: The convolution theorem is the mathematical fact that the Fourier transform diagonalizes convolution operators
  - field_a_term: FFT butterfly algorithm (computer science)
    field_b_term: divide-and-conquer factorization of DFT matrix (mathematics)
    note: The FFT exploits the factorization of the DFT matrix into sparse factors using roots of unity, reducing O(n^2) to O(n log n)
  - field_a_term: Nyquist sampling theorem (signal processing)
    field_b_term: Paley-Wiener theorem / bandlimited functions (mathematics)
    note: Shannon's sampling theorem is a consequence of the Paley-Wiener theorem; band-limiting in frequency implies exact reconstruction from samples at 2B Hz
communication_gap: >
  Pure mathematicians studying Fourier analysis and electrical engineers developing signal
  processing algorithms developed the same theory independently; Cooley and Tukey's 1965
  FFT paper was not recognized as rediscovering Gauss's 1805 algorithm until the history
  was researched afterward, illustrating how disciplinary separation delays algorithm diffusion.
cross_pollination_opportunities:
  - Apply noncommutative Fourier analysis on groups to design signal processing algorithms for non-Euclidean domains (graphs, spheres, manifolds) in geometric deep learning
  - Use number-theoretic transforms (NTT, FFT over finite fields) to accelerate polynomial multiplication in post-quantum cryptography implementations
related_unknowns:
  - u-fourier-transform-x-signal-processing
references:
  - doi: "10.1090/S0025-5718-1965-0178586-1"
    note: "Cooley & Tukey (1965) - An algorithm for the machine calculation of complex Fourier series; Math Comp 19:297"
last_reviewed: "2026-05-07"
"""),
    },
]

UNKNOWNS = [
    {
        "path": "unknowns-catalog/physics/u-quantum-error-correction-x-topological-codes.yaml",
        "content": textwrap.dedent("""\
id: u-quantum-error-correction-x-topological-codes
title: >
  What physical platforms can host non-abelian anyons at scales sufficient for fault-tolerant
  topological quantum computation, and what is the minimum system size needed to achieve
  meaningful logical error rate suppression?
status: open
priority: high
disciplines:
  - physics
  - quantum-information
  - condensed-matter-physics
summary: >
  Topological quantum error correction requires physical anyons or their effective analogs;
  leading candidate platforms (fractional quantum Hall systems, Kitaev honeycomb model,
  Majorana-based nanowires) each face barriers in achieving the necessary coherence, system
  size, and anyon manipulation fidelity at the same time. Key unknowns: what is the
  minimum code distance needed for below-threshold operation in realistic noise models,
  which material platform will first achieve controllable non-abelian anyons, and how
  do finite-size corrections affect the topological protection gap?
systematic_gaps:
  - No experimental demonstration of non-abelian anyon braiding with sufficient fidelity for logical gate implementation
  - Theoretical threshold theorems assume idealized noise models that may not match realistic correlated noise in solid-state systems
  - Relationship between bulk energy gap and logical error rate in finite-size topological codes is not precisely known
related_bridges:
  - b-quantum-error-correction-x-topological-codes
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "unknowns-catalog/biology/u-developmental-gradient-x-pde.yaml",
        "content": textwrap.dedent("""\
id: u-developmental-gradient-x-pde
title: >
  How do embryos robustly maintain morphogen gradient precision despite noise in gene
  expression, cell number variability, and tissue growth during development?
status: open
priority: high
disciplines:
  - biology
  - developmental-biology
  - mathematics
summary: >
  Turing reaction-diffusion models predict specific pattern wavelengths but are sensitive
  to parameter variation; real embryos achieve remarkable reproducibility (Drosophila
  Bicoid gradient has <10% positional error) despite stochastic gene expression.
  Unknown: what feedback mechanisms (self-organized criticality, tissue mechanics, cell
  polarity) buffer the Turing instability against noise, and how do growing tissues
  maintain stable patterns as cell number increases?
systematic_gaps:
  - Quantitative measurement of morphogen diffusion coefficients in vivo remains difficult due to limited temporal resolution of imaging
  - Mechanisms that scale pattern wavelength with organism size (embryo scaling) are not fully understood
  - Role of mechanical feedback (tissue tension, cell rearrangement) in pattern robustness is uncharacterized
related_bridges:
  - b-developmental-gradient-x-pde
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "unknowns-catalog/mathematics/u-compressed-sensing-x-sparse-recovery.yaml",
        "content": textwrap.dedent("""\
id: u-compressed-sensing-x-sparse-recovery
title: >
  What are the fundamental limits of compressed sensing recovery for non-sparse but
  approximately sparse signals, and how do these limits change under adversarial or
  structured noise?
status: open
priority: medium
disciplines:
  - mathematics
  - computer-science
  - signal-processing
summary: >
  Classical compressed sensing theory assumes exact sparsity and sub-Gaussian measurement
  noise; real applications involve approximately sparse signals (compressible), structured
  noise (quantization, clipping), and adversarial perturbations. Unknown: what is the
  optimal measurement design for approximately sparse signals under L_inf noise, how does
  the RIP constant degrade under structured measurement matrices, and can compressed
  sensing be extended to union-of-subspace models with optimal sample complexity?
systematic_gaps:
  - Tight information-theoretic lower bounds for compressed sensing with structured (non-i.i.d.) noise are not known
  - Sample complexity of compressed sensing for group-sparse or low-rank matrix recovery with dependent measurements is open
  - Computational vs statistical tradeoffs in compressed sensing (SDP relaxations vs greedy algorithms) are not fully characterized
related_bridges:
  - b-compressed-sensing-x-sparse-recovery
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "unknowns-catalog/chemistry/u-enzyme-kinetics-x-michaelis-menten.yaml",
        "content": textwrap.dedent("""\
id: u-enzyme-kinetics-x-michaelis-menten
title: >
  How do multi-enzyme metabolic pathways coordinate kinetics to avoid toxic intermediate
  accumulation, and what determines the optimal Km/Vmax ratio for each enzyme in a pathway?
status: open
priority: medium
disciplines:
  - chemistry
  - biology
  - biochemistry
summary: >
  Michaelis-Menten kinetics describes single enzymes, but in metabolic pathways enzymes
  operate in series/parallel with substrate channeling and allosteric regulation; the
  conditions for stable flux through branched networks without toxic intermediate buildup
  are not fully understood. Unknown: what is the optimal distribution of enzyme Km values
  along a metabolic pathway for robust flux, how does enzyme co-localization (metabolon
  formation) affect effective kinetics, and can queueing theory predict metabolic
  bottlenecks?
systematic_gaps:
  - In vivo Km values differ significantly from in vitro measurements due to macromolecular crowding
  - Substrate channeling efficiency between consecutive enzymes in metabolons is not quantified
  - Stochastic fluctuations in enzyme copy number affect pathway flux in ways not captured by deterministic Michaelis-Menten models
related_bridges:
  - b-enzyme-kinetics-x-michaelis-menten
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "unknowns-catalog/physics/u-topological-defects-x-homotopy.yaml",
        "content": textwrap.dedent("""\
id: u-topological-defects-x-homotopy
title: >
  What is the complete classification of topological defects in active matter and
  non-equilibrium ordered phases where homotopy theory applies only approximately?
status: open
priority: medium
disciplines:
  - physics
  - mathematics
  - condensed-matter-physics
summary: >
  Homotopy group classification of topological defects applies rigorously to equilibrium
  ordered phases with well-defined order parameters; active matter systems (bacterial
  suspensions, cytoskeletal networks) exhibit topological defect dynamics but lack
  equilibrium order parameters. Unknown: how do activity-induced fluctuations modify
  defect stability, what is the role of non-Abelian homotopy groups in frustrated magnets
  with competing order parameters, and can topological defects be used as functional
  elements in programmable materials?
systematic_gaps:
  - Homotopy classification does not account for defect dynamics and kinetics in driven systems far from equilibrium
  - Non-Abelian defect fusion rules have not been experimentally verified in accessible condensed matter systems
  - Topological defects in systems with multiple competing order parameters (spin-orbit coupled magnets) remain poorly classified
related_bridges:
  - b-topological-defects-x-homotopy
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "unknowns-catalog/neuroscience/u-hair-cell-bundle-x-hopf-bifurcation.yaml",
        "content": textwrap.dedent("""\
id: u-hair-cell-bundle-x-hopf-bifurcation
title: >
  How does the inner ear maintain tuning of individual hair cells at the Hopf bifurcation
  across the full auditory frequency range (20 Hz to 20 kHz), and what active feedback
  mechanisms set the bifurcation parameter?
status: open
priority: high
disciplines:
  - neuroscience
  - physics
  - biophysics
summary: >
  Hair cell bundles operate near a Hopf bifurcation for maximal sensitivity and frequency
  selectivity, but maintaining this precise operating point across four decades of frequency
  in a non-uniform cochlea requires active feedback. Unknown: what molecular motors (myosin
  1c, prestin) and ion channels set and maintain the bifurcation parameter, how does the
  operating point change with sound level adaptation, and what is the feedback delay that
  allows active amplification without instability?
systematic_gaps:
  - Molecular identity of the adaptation motor maintaining the Hopf bifurcation point is debated (myosin vs Ca2+-gating)
  - Quantitative measurement of the bifurcation parameter in vivo is limited by accessibility of the mammalian cochlea
  - Interaction between the traveling wave and individual hair cell Hopf oscillators is not fully modeled
related_bridges:
  - b-hair-cell-bundle-x-hopf-bifurcation
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "unknowns-catalog/computer-science/u-genetic-algorithm-x-natural-selection.yaml",
        "content": textwrap.dedent("""\
id: u-genetic-algorithm-x-natural-selection
title: >
  Under what fitness landscape structures do genetic algorithms outperform gradient-based
  optimization, and how can evolutionary computation borrow population genetics theory
  to design better crossover operators?
status: open
priority: medium
disciplines:
  - computer-science
  - biology
  - evolutionary-biology
summary: >
  No Free Lunch theorems prove that no algorithm outperforms random search on all problems;
  GAs excel on deceptive, multimodal, or noisy landscapes but the precise landscape
  properties that favor evolutionary search are not characterized. Unknown: what landscape
  statistics (epistasis, ruggedness, neutrality) predict GA vs gradient method advantage,
  how can recombination operators be designed to exploit linkage structure (analogous to
  sexual recombination), and can population genetics' diffusion theory predict GA
  population diversity dynamics?
systematic_gaps:
  - Fitness landscape statistics for real combinatorial optimization problems (TSP, protein folding) are not well characterized
  - Optimal crossover operator design for preserving building blocks depends on unknown problem structure
  - Theory of GA population diversity maintenance (niching, speciation) lacks quantitative predictive power
related_bridges:
  - b-genetic-algorithm-x-natural-selection
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "unknowns-catalog/economics/u-blackscholes-x-diffusion-equation.yaml",
        "content": textwrap.dedent("""\
id: u-blackscholes-x-diffusion-equation
title: >
  How should the Black-Scholes diffusion equation be modified to capture fat-tailed
  return distributions, jumps, and stochastic volatility observed in real financial markets?
status: open
priority: high
disciplines:
  - economics
  - physics
  - mathematics
summary: >
  Black-Scholes assumes log-normal returns (Gaussian diffusion) but real markets exhibit
  heavy tails (kurtosis > 3), volatility clustering, and occasional jumps; models such as
  Heston (stochastic volatility), Merton (jump-diffusion), and Levy process models modify
  the diffusion equation but lack analytical tractability. Unknown: what is the correct
  generalization of the diffusion equation for financial returns that is both analytically
  tractable and empirically accurate, and how do extreme events (crashes) fit into the
  diffusion framework?
systematic_gaps:
  - No consensus model captures all statistical properties of financial returns (tail index, volatility autocorrelation, leverage effect) simultaneously
  - Calibration of stochastic volatility models to options data is numerically unstable and non-unique
  - Extreme event (crash) statistics are inherently non-Gaussian and may not be captured by any diffusion framework
related_bridges:
  - b-blackscholes-x-diffusion-equation
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "unknowns-catalog/mathematics/u-random-walk-x-brownian-motion.yaml",
        "content": textwrap.dedent("""\
id: u-random-walk-x-brownian-motion
title: >
  What is the universality class of the scaling limit for random walks in random environments,
  and when does the Brownian motion limit break down?
status: open
priority: medium
disciplines:
  - mathematics
  - physics
  - probability-theory
summary: >
  Donsker's theorem establishes Brownian motion as the universal scaling limit for i.i.d.
  steps with finite variance; random walks in random environments (RWRE), correlated walks,
  and heavy-tailed walks have different scaling limits. Unknown: what are the universality
  classes for RWRE in 2D (Sinai diffusion, subdiffusion), when does the KPZ universality
  class apply, and can the functional CLT be extended to non-Markovian and non-stationary
  increment processes?
systematic_gaps:
  - Scaling limit for random walk in 2D random environment is not rigorously established
  - Universality class crossover between diffusive and subdiffusive behavior in correlated random walks is not characterized
  - Extension of Donsker's theorem to infinite-variance (Levy flight) steps requires stable distribution theory not yet fully applied in physics
related_bridges:
  - b-random-walk-x-brownian-motion
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "unknowns-catalog/neuroscience/u-neural-spike-coding-x-information-compression.yaml",
        "content": textwrap.dedent("""\
id: u-neural-spike-coding-x-information-compression
title: >
  How does the brain maintain efficient coding of natural scenes across adaptation,
  attention, and changes in stimulus statistics, and what plasticity rules implement
  online information maximization?
status: open
priority: high
disciplines:
  - neuroscience
  - computer-science
  - information-theory
summary: >
  Efficient coding theory predicts that neural representations should match the statistics
  of natural inputs, but real brains must adapt coding efficiency to changing environments
  (e.g., adaptation from bright to dim light) while maintaining discriminability. Unknown:
  what Hebbian learning rules implement information-maximizing adaptation in real neural
  circuits, how do higher cortical areas encode non-Gaussian higher-order statistics, and
  what is the energy-information tradeoff in spike coding?
systematic_gaps:
  - Information-theoretic measurement of neural coding efficiency requires knowledge of the complete stimulus distribution, which is unknown for complex natural stimuli
  - Role of spike timing (temporal codes) vs rate coding in information transmission is debated
  - Energy cost of neural computation is not integrated into efficient coding models
related_bridges:
  - b-neural-spike-coding-x-information-compression
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "unknowns-catalog/physics/u-liquid-crystal-x-cell-membrane.yaml",
        "content": textwrap.dedent("""\
id: u-liquid-crystal-x-cell-membrane
title: >
  How do lipid raft phase separation and curvature coupling in cell membranes influence
  protein sorting, signaling, and membrane-mediated interactions between proteins?
status: open
priority: high
disciplines:
  - physics
  - biology
  - biophysics
summary: >
  Liquid crystal theory predicts that lipid composition phase transitions (Lo/Ld separation)
  should create ordered membrane microdomains (rafts) that concentrate certain proteins; but
  raft size, lifetime, and signaling function in living cells are contested. Unknown: what
  is the equilibrium phase diagram of plasma membrane lipids, how does membrane curvature
  couple to lipid phase separation (curvature sorting), and what is the quantitative
  relationship between membrane liquid crystal order parameters and signaling protein
  diffusion?
systematic_gaps:
  - In vivo raft size is below optical diffraction limit (~10-200 nm) and hard to measure directly
  - The role of cytoskeleton-membrane coupling in defining raft domains is not quantified
  - Curvature-composition coupling constants are not measured in biological membranes
related_bridges:
  - b-liquid-crystal-x-cell-membrane
last_reviewed: "2026-05-07"
"""),
    },
    {
        "path": "unknowns-catalog/mathematics/u-fourier-transform-x-signal-processing.yaml",
        "content": textwrap.dedent("""\
id: u-fourier-transform-x-signal-processing
title: >
  What are the optimal time-frequency representations for non-stationary signals,
  and how do Fourier and wavelet transforms generalize to non-Euclidean domains?
status: open
priority: medium
disciplines:
  - mathematics
  - computer-science
  - signal-processing
summary: >
  The Fourier transform is optimal for stationary signals but non-stationary signals
  (speech, EEG, financial time series) require time-frequency representations (STFT,
  wavelet transform, EMD); no single representation is optimal for all non-stationary
  signals. Unknown: what is the optimal time-frequency atom for a given signal class,
  how does the uncertainty principle limit joint time-frequency resolution, and how do
  Fourier-like transforms generalize to signals on graphs, manifolds, and non-Euclidean
  spaces?
systematic_gaps:
  - No unified theory of optimal time-frequency representation for arbitrary non-stationary processes
  - Graph Fourier transform (eigendecomposition of graph Laplacian) lacks the shift-invariance and fast algorithm of classical FFT
  - Quantum Fourier transform speedup for classical signal processing problems is not fully characterized
related_bridges:
  - b-fourier-transform-x-signal-processing
last_reviewed: "2026-05-07"
"""),
    },
]

HYPOTHESES = [
    {
        "path": "hypotheses/active/h-quantum-error-correction-x-topological-codes.yaml",
        "content": textwrap.dedent("""\
id: h-quantum-error-correction-x-topological-codes
title: >
  Majorana-based topological qubits in semiconductor nanowire networks will achieve below-threshold
  logical error rates when system size exceeds a critical length determined by the topological gap
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: high
impact_score: 0.88
author: wave-60-agent
unknowns_addressed:
  - u-quantum-error-correction-x-topological-codes
related_disciplines:
  - physics
  - quantum-information
  - condensed-matter-physics
evidence_links:
  - type: supporting
    doi: "10.1103/RevModPhys.80.1083"
    note: "Nayak et al. (2008) - Non-abelian anyons and topological quantum computation; theoretical foundation"
    confidence: 0.82
  - type: related
    note: "Kitaev (2003) - Fault-tolerant quantum computation by anyons; arXiv:quant-ph/9707021"
    confidence: 0.85
proposed_tests:
  - description: Measure anyon braiding statistics in fractional quantum Hall nu=5/2 state by interferometry and verify non-abelian phase accumulation
  - description: Demonstrate logical qubit coherence time scaling exponentially with nanowire network size in Majorana-based devices
"""),
    },
    {
        "path": "hypotheses/active/h-developmental-gradient-x-pde.yaml",
        "content": textwrap.dedent("""\
id: h-developmental-gradient-x-pde
title: >
  The robustness of embryonic morphogen gradient interpretation is maintained by a
  feedforward incoherent loop that implements derivative control, reducing sensitivity
  to absolute morphogen levels
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
impact_score: 0.75
author: wave-60-agent
unknowns_addressed:
  - u-developmental-gradient-x-pde
related_disciplines:
  - biology
  - developmental-biology
  - mathematics
evidence_links:
  - type: supporting
    doi: "10.1098/rstb.1952.0012"
    note: "Turing (1952) - The chemical basis of morphogenesis; foundational reaction-diffusion theory"
    confidence: 0.78
  - type: related
    note: "Eldar et al. (2003) - Robustness of the BMP morphogen gradient in Drosophila embryonic patterning; Nature 419:304; doi:10.1038/nature01061"
    confidence: 0.81
proposed_tests:
  - description: Perturb morphogen production rate in Drosophila embryos by 2-fold and measure positional error of target gene expression boundary by live imaging
  - description: Construct synthetic gene circuit implementing incoherent feedforward loop and measure gradient robustness to input perturbation in E. coli
"""),
    },
    {
        "path": "hypotheses/active/h-compressed-sensing-x-sparse-recovery.yaml",
        "content": textwrap.dedent("""\
id: h-compressed-sensing-x-sparse-recovery
title: >
  Deep neural networks implicitly implement compressed sensing by learning measurement
  matrices that satisfy the RIP for the natural signal manifold, explaining their
  sample efficiency relative to classical sparse recovery
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
impact_score: 0.72
author: wave-60-agent
unknowns_addressed:
  - u-compressed-sensing-x-sparse-recovery
related_disciplines:
  - mathematics
  - computer-science
  - signal-processing
evidence_links:
  - type: supporting
    doi: "10.1109/TIT.2006.871582"
    note: "Candès & Tao (2006) - Near-optimal signal recovery; foundational compressed sensing theory"
    confidence: 0.80
  - type: related
    note: "Bora et al. (2017) - Compressed sensing using generative models; arXiv:1703.03208"
    confidence: 0.74
proposed_tests:
  - description: Measure the RIP constant of trained neural network feature layers for natural image patches and compare to theoretical bounds for random Gaussian matrices
  - description: Compare sample complexity of compressed sensing with learned vs random measurement matrices on MRI reconstruction benchmarks
"""),
    },
    {
        "path": "hypotheses/active/h-enzyme-kinetics-x-michaelis-menten.yaml",
        "content": textwrap.dedent("""\
id: h-enzyme-kinetics-x-michaelis-menten
title: >
  Metabolic pathway enzymes are evolutionarily tuned so that their Km values match
  physiological substrate concentrations, placing each enzyme in the linear (unsaturated)
  regime to minimize resource waste and maximize pathway control coefficient
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
impact_score: 0.70
author: wave-60-agent
unknowns_addressed:
  - u-enzyme-kinetics-x-michaelis-menten
related_disciplines:
  - chemistry
  - biology
  - biochemistry
evidence_links:
  - type: supporting
    doi: "10.1111/j.1432-1033.1994.tb18811.x"
    note: "Heinrich & Schuster (1994) - The regulation of cellular systems; metabolic control analysis"
    confidence: 0.73
  - type: related
    note: "Bar-Even et al. (2011) - The moderately efficient enzyme: evolutionary and physicochemical trends; Biochemistry 50:4402; doi:10.1021/bi2002289"
    confidence: 0.76
proposed_tests:
  - description: Systematically compare measured in vivo metabolite concentrations with enzyme Km values across E. coli central metabolism and test for the predicted Km ~ [S] correlation
  - description: Engineer E. coli strains with Km values shifted 10-fold from wild-type and measure pathway flux and growth rate to test optimality hypothesis
"""),
    },
    {
        "path": "hypotheses/active/h-topological-defects-x-homotopy.yaml",
        "content": textwrap.dedent("""\
id: h-topological-defects-x-homotopy
title: >
  Active matter systems (bacterial suspensions, cytoskeletal networks) exhibit topological
  defect coarsening dynamics governed by the same homotopy group fusion rules as equilibrium
  liquid crystals, but with activity-renormalized defect mobility
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
impact_score: 0.73
author: wave-60-agent
unknowns_addressed:
  - u-topological-defects-x-homotopy
related_disciplines:
  - physics
  - mathematics
  - condensed-matter-physics
evidence_links:
  - type: supporting
    doi: "10.1103/RevModPhys.51.591"
    note: "Mermin (1979) - The topological theory of defects in ordered media; homotopy classification"
    confidence: 0.82
  - type: related
    note: "Sanchez et al. (2012) - Spontaneous motion in hierarchically assembled active matter; Nature 491:431; doi:10.1038/nature11591"
    confidence: 0.75
proposed_tests:
  - description: Image topological defect dynamics in active nematic microtubule-kinesin system and measure defect velocity as function of ATP concentration (activity parameter)
  - description: Verify that defect annihilation events in active nematics obey pi_1 fusion rules and are suppressed by topological charge conservation
"""),
    },
    {
        "path": "hypotheses/active/h-hair-cell-bundle-x-hopf-bifurcation.yaml",
        "content": textwrap.dedent("""\
id: h-hair-cell-bundle-x-hopf-bifurcation
title: >
  Sensorineural hearing loss shifts individual hair cell bundles away from the Hopf
  bifurcation point toward the stable fixed point regime, reducing amplification gain
  and auditory sensitivity quantitatively predictable from the bifurcation distance parameter
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: high
impact_score: 0.80
author: wave-60-agent
unknowns_addressed:
  - u-hair-cell-bundle-x-hopf-bifurcation
related_disciplines:
  - neuroscience
  - physics
  - biophysics
evidence_links:
  - type: supporting
    doi: "10.1073/pnas.97.7.3183"
    note: "Camalet et al. (2000) - Auditory sensitivity provided by self-tuned critical oscillations of hair cells"
    confidence: 0.83
  - type: related
    note: "Hudspeth (2008) - Making an effort to listen: mechanical amplification in the ear; Neuron 59:530; doi:10.1016/j.neuron.2008.07.012"
    confidence: 0.79
proposed_tests:
  - description: Measure spontaneous oscillation amplitude and frequency of individual hair cell bundles in ototoxin-damaged cochleae and compare to Hopf bifurcation theory predictions
  - description: Apply sub-threshold sinusoidal mechanical stimulation to damaged and healthy hair cells and measure the power law response exponent (predicted 1/3 for Hopf, 1 for sub-threshold linear)
"""),
    },
    {
        "path": "hypotheses/active/h-genetic-algorithm-x-natural-selection.yaml",
        "content": textwrap.dedent("""\
id: h-genetic-algorithm-x-natural-selection
title: >
  Genetic algorithms searching protein sequence space will outperform gradient-based
  directed evolution methods when the fitness landscape has high epistasis (>50% of
  beneficial mutations are conditionally beneficial), due to crossover's ability to
  combine building blocks
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
impact_score: 0.71
author: wave-60-agent
unknowns_addressed:
  - u-genetic-algorithm-x-natural-selection
related_disciplines:
  - computer-science
  - biology
  - evolutionary-biology
evidence_links:
  - type: supporting
    doi: "10.1016/0004-3702(94)90132-5"
    note: "Mitchell et al. (1994) - When will a genetic algorithm outperform hill climbing; AI survey"
    confidence: 0.72
  - type: related
    note: "Romero & Arnold (2009) - Exploring protein fitness landscapes by directed evolution; Nature Rev Mol Cell Biol 10:866; doi:10.1038/nrm2805"
    confidence: 0.75
proposed_tests:
  - description: Measure epistasis fraction in TEM-1 beta-lactamase fitness landscape using combinatorial mutagenesis library and correlate with GA vs gradient method optimization advantage
  - description: Compare GA with sexual recombination (crossover) vs asexual mutation-only search on NK landscape models as a function of K (epistasis parameter)
"""),
    },
    {
        "path": "hypotheses/active/h-blackscholes-x-diffusion-equation.yaml",
        "content": textwrap.dedent("""\
id: h-blackscholes-x-diffusion-equation
title: >
  Financial return distributions are well-described by a fractional diffusion equation
  with a Levy stable index alpha < 2 that accounts for fat tails, and this index is
  stable across market regimes and asset classes
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: high
impact_score: 0.76
author: wave-60-agent
unknowns_addressed:
  - u-blackscholes-x-diffusion-equation
related_disciplines:
  - economics
  - physics
  - mathematics
evidence_links:
  - type: supporting
    doi: "10.1086/260062"
    note: "Black & Scholes (1973) - The pricing of options and corporate liabilities; foundational model"
    confidence: 0.70
  - type: related
    note: "Mantegna & Stanley (1994) - Stochastic process with ultraslow convergence to a Gaussian; Phys Rev Lett 73:2946; doi:10.1103/PhysRevLett.73.2946"
    confidence: 0.74
proposed_tests:
  - description: Fit fractional diffusion equation to daily S&P 500 return distributions over 1990-2025 and test stability of Levy index alpha across sub-periods including crises
  - description: Compare option prices computed from fractional diffusion model to Black-Scholes prices and market prices for far out-of-the-money options (tail sensitivity test)
"""),
    },
    {
        "path": "hypotheses/active/h-random-walk-x-brownian-motion.yaml",
        "content": textwrap.dedent("""\
id: h-random-walk-x-brownian-motion
title: >
  Anomalous diffusion of proteins on cell membranes follows a fractional Brownian motion
  scaling law with Hurst exponent H < 0.5 (subdiffusion) due to macromolecular crowding,
  transitioning to normal diffusion at long times when confinement domains are escaped
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
impact_score: 0.74
author: wave-60-agent
unknowns_addressed:
  - u-random-walk-x-brownian-motion
related_disciplines:
  - mathematics
  - physics
  - biophysics
evidence_links:
  - type: supporting
    doi: "10.1090/S0002-9947-1951-0040613-0"
    note: "Donsker (1951) - Invariance principle for probability limit theorems; foundational random walk theory"
    confidence: 0.75
  - type: related
    note: "Saxton & Jacobson (1997) - Single-particle tracking: applications to membrane dynamics; Annu Rev Biophys Biomol Struct 26:373; doi:10.1146/annurev.biophys.26.1.373"
    confidence: 0.78
proposed_tests:
  - description: Measure single-molecule diffusion of GPI-anchored proteins by single-particle tracking in live cells and fit mean-squared displacement to fractional Brownian motion model
  - description: Test whether confinement hop diffusion (confined subdiffusion punctuated by escapes) accounts for the anomalous exponent by depleting membrane cytoskeleton
"""),
    },
    {
        "path": "hypotheses/active/h-neural-spike-coding-x-information-compression.yaml",
        "content": textwrap.dedent("""\
id: h-neural-spike-coding-x-information-compression
title: >
  Retinal ganglion cell receptive field shapes are optimally tuned to the statistics
  of the specific natural scenes encountered during early visual development, and this
  tuning is lost when visual experience is restricted during the critical period
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: high
impact_score: 0.78
author: wave-60-agent
unknowns_addressed:
  - u-neural-spike-coding-x-information-compression
related_disciplines:
  - neuroscience
  - computer-science
  - information-theory
evidence_links:
  - type: supporting
    doi: "10.1038/381520a0"
    note: "Olshausen & Field (1996) - Emergence of simple-cell receptive fields by learning a sparse code for natural images"
    confidence: 0.82
  - type: related
    note: "Atick & Redlich (1992) - What does the retina know about natural scenes; Neural Comp 4:196; doi:10.1162/neco.1992.4.2.196"
    confidence: 0.79
proposed_tests:
  - description: Raise ferrets in structured visual environments with altered spatial frequency statistics and measure adult ganglion cell receptive field sizes vs normal controls
  - description: Train convolutional neural network on natural scene statistics and verify that learned first-layer filters match retinal ganglion cell center-surround profiles
"""),
    },
    {
        "path": "hypotheses/active/h-liquid-crystal-x-cell-membrane.yaml",
        "content": textwrap.dedent("""\
id: h-liquid-crystal-x-cell-membrane
title: >
  Lipid raft microdomains in the plasma membrane are described by the two-dimensional
  Ising model near a miscibility critical point, and their size distribution follows
  critical fluctuation scaling laws with measurable critical exponents
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: high
impact_score: 0.77
author: wave-60-agent
unknowns_addressed:
  - u-liquid-crystal-x-cell-membrane
related_disciplines:
  - physics
  - biology
  - biophysics
evidence_links:
  - type: supporting
    doi: "10.1103/RevModPhys.46.617"
    note: "de Gennes (1974) - The physics of liquid crystals; foundational liquid crystal theory"
    confidence: 0.75
  - type: related
    note: "Veatch & Keller (2005) - Seeing spots: complex phase behavior in simple membranes; Biochim Biophys Acta 1746:172; doi:10.1016/j.bbamcr.2005.06.010"
    confidence: 0.80
proposed_tests:
  - description: Measure lipid domain size distribution in giant plasma membrane vesicles by fluorescence microscopy and test for power-law scaling consistent with 2D Ising critical exponents
  - description: Apply temperature-controlled membrane phase behavior measurements to map the miscibility phase diagram and identify the critical point coordinates
"""),
    },
    {
        "path": "hypotheses/active/h-fourier-transform-x-signal-processing.yaml",
        "content": textwrap.dedent("""\
id: h-fourier-transform-x-signal-processing
title: >
  Graph neural networks that incorporate spectral graph Fourier transforms will outperform
  spatial message-passing GNNs on tasks requiring long-range frequency-dependent features,
  due to the ability to apply frequency-selective filters to graph signals
status: active
created: "2026-05-07"
last_updated: "2026-05-07"
priority: medium
impact_score: 0.70
author: wave-60-agent
unknowns_addressed:
  - u-fourier-transform-x-signal-processing
related_disciplines:
  - mathematics
  - computer-science
  - signal-processing
evidence_links:
  - type: supporting
    doi: "10.1090/S0025-5718-1965-0178586-1"
    note: "Cooley & Tukey (1965) - An algorithm for the machine calculation of complex Fourier series"
    confidence: 0.72
  - type: related
    note: "Defferrard et al. (2016) - Convolutional neural networks on graphs with fast localized spectral filtering; NeurIPS; arXiv:1606.09375"
    confidence: 0.75
proposed_tests:
  - description: Compare spectral GNN vs spatial GNN performance on graph signal processing benchmarks with known frequency structure (filtering, denoising) across graph topologies
  - description: Analyze learned spectral filters in trained GNNs and verify that they correspond to meaningful frequency bands in the graph Laplacian spectrum
"""),
    },
]


def write_file(path_str: str, content: str) -> None:
    path = ROOT / path_str
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"  wrote {path_str}")


if __name__ == "__main__":
    print("Writing Wave 60 bridges...")
    for item in BRIDGES:
        write_file(item["path"], item["content"])
    print("Writing Wave 60 unknowns...")
    for item in UNKNOWNS:
        write_file(item["path"], item["content"])
    print("Writing Wave 60 hypotheses...")
    for item in HYPOTHESES:
        write_file(item["path"], item["content"])
    print(f"Done: {len(BRIDGES)} bridges, {len(UNKNOWNS)} unknowns, {len(HYPOTHESES)} hypotheses")

"""Write all 12 wave-28 bridge files, unknowns, and hypotheses."""
import os

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# ─── Bridge A: Chemistry ↔ Physics — Electrochemical Impedance and Biological Membranes ───
write('cross-domain/chemistry-physics/b-electrochemical-impedance-membranes.yaml', """\
id: b-electrochemical-impedance-membranes
title: >
  Electrochemical impedance spectroscopy maps directly onto equivalent-circuit models
  of biological membranes — the Hodgkin-Huxley ionic conductances are impedance
  elements, enabling label-free biosensing of living cells with the same formalism
  used to study corroding metal electrodes.
status: established
fields:
  - chemistry
  - physics
  - biophysics
  - neuroscience
bridge_claim: >
  Electrochemical impedance spectroscopy (EIS) applies a small AC voltage
  V(omega) = V0 exp(i*omega*t) and measures complex impedance Z(omega) = Z' + iZ''.
  The Nyquist plot (Z'' vs Z') displays a semicircle whose radius equals the
  charge-transfer resistance R_ct and whose high-frequency intercept gives solution
  resistance R_s.

  Biological membranes are precisely described by the same equivalent-circuit language:
  membrane capacitance C_m ≈ 1 μF/cm², membrane resistance R_m ≈ 10⁴ Ω·cm², and
  voltage-gated channel conductances that are frequency-dependent. The Hodgkin-Huxley
  (1952) model translates directly: ionic conductances g_Na, g_K, g_L are impedance
  elements whose frequency response encodes channel gating kinetics.

  This equivalence is operationally exploited in impedance-based biosensors (RTCA
  platform, Giaever and Keese 1991): changes in cell adhesion or cytoskeletal
  integrity shift Z(omega) measurably within minutes. Brain electrocorticography
  (ECoG) uses impedance spectra of cortical tissue correlated with neural activity.

  The bridge is non-trivial because electrochemists developed EIS for corroding metal
  electrodes, while electrophysiologists independently derived the HH model from
  voltage-clamp experiments — both solved the same mathematical problem (frequency-
  domain response of RC networks with nonlinear elements) without recognising the
  shared formalism.
translation_table:
  - field_a_term: charge-transfer resistance R_ct
    field_b_term: membrane ion-channel resistance R_m
    note: Both represent resistive impedance to ion flow across an interface
  - field_a_term: double-layer capacitance C_dl
    field_b_term: membrane capacitance C_m (~1 μF/cm²)
    note: Lipid bilayer acts as a parallel-plate capacitor just as the electric double layer does
  - field_a_term: Warburg impedance (diffusion-limited, ~sqrt(i*omega) dependence)
    field_b_term: diffusion-limited ion transport through cytoplasm or cell-substrate cleft
    note: Identical frequency dependence in both systems
  - field_a_term: Nyquist semicircle radius
    field_b_term: membrane resistance R_m (inversely proportional to channel open probability)
    note: Drug toxicity or channel blockade shifts semicircle radius measurably
  - field_a_term: high-frequency intercept R_s
    field_b_term: extracellular solution resistance
    note: Sets baseline; used to normalize cell-substrate impedance measurements
related_unknowns:
  - u-eis-channel-gating-mechanistic-link
related_hypotheses:
  - h-eis-hodgkin-huxley-parameter-extraction
cross_pollination_opportunities:
  - >
    Real-time cell analysis (RTCA) could be extended to map Hodgkin-Huxley parameters
    (g_Na activation/inactivation time constants) from multi-frequency impedance sweeps
    on excitable cell lines without patch clamp.
  - >
    EIS of cortical organoids could non-invasively track maturation of voltage-gated
    channel expression and network synchronisation as a drug-screening readout.
communication_gap: >
  EIS was developed by the electrochemical corrosion community and remains primarily
  published in electrochemistry journals (J Electrochem Soc, Electrochim Acta). The
  Hodgkin-Huxley tradition publishes in physiology and neuroscience journals. Both use
  circuit analogies but rarely cite each other. Biosensor researchers who bridge both
  communities are a small, specialized group.
last_reviewed: "2026-05-06"
references:
  - note: "Macdonald (1987) Impedance Spectroscopy — Wiley; foundational EIS reference"
  - doi: "10.1113/jphysiol.1952.sp004764"
    note: "Hodgkin & Huxley (1952) J Physiol 117:500 — quantitative model of membrane conductances"
  - doi: "10.1073/pnas.88.17.7896"
    note: "Giaever & Keese (1991) PNAS 88:7896 — impedance-based cell biosensing"
  - note: "Cole (1972) Membranes, Ions and Impulses — University of California Press"
""")

# ─── Bridge B: Mathematics ↔ Social Science — Matching Theory and Labor Markets ───
write('cross-domain/mathematics-social-science/b-matching-theory-labor-markets.yaml', """\
id: b-matching-theory-labor-markets
title: >
  The Gale-Shapley deferred acceptance algorithm solves stable matching in O(n²) and
  directly describes real labor market clearing mechanisms — medical residency match,
  school choice, and kidney exchange — making market design a branch of applied
  combinatorics.
status: established
fields:
  - mathematics
  - social-science
  - economics
  - game-theory
bridge_claim: >
  Stable matching (Gale-Shapley 1962): given preference lists of n workers and n firms,
  the deferred acceptance (DA) algorithm produces a stable matching — one in which no
  worker-firm pair mutually prefer each other over their current assignments — in O(n²)
  steps. Worker-proposing DA is worker-optimal; firm-proposing DA is firm-optimal.

  Roth's insight (Nobel Prize 2012): real markets use matching mechanisms that can be
  evaluated for stability, incentive-compatibility, and efficiency. The National Residency
  Matching Program (NRMP) for medical residency was mathematically equivalent to the
  firm-proposing DA algorithm before Roth's analysis — and switching to worker-proposing
  DA improved resident welfare with no loss of stability.

  School choice: the Boston mechanism (immediate acceptance) is not strategy-proof —
  students have incentives to misreport preferences. Deferred acceptance is strategy-
  proof for students (reporting truthfully is a dominant strategy), making it preferable
  on incentive-compatibility grounds even when it does not maximize efficiency.

  Kelso and Crawford (1982): labor markets with complementarities require the gross
  substitutes condition for competitive equilibrium to exist. The Shapley-Shubik (1972)
  assignment game shows that with transferable utility, the set of competitive equilibria
  equals the core of the cooperative game — a deep duality between competitive and
  cooperative solution concepts.

  Monopsony: when a single firm is the only buyer of labor, the wage falls below the
  marginal product and employment below the efficient level — a market structure whose
  prevalence in local labor markets (hospitals, school districts) matches the predictions
  of matching models with limited outside options.
translation_table:
  - field_a_term: stable matching (no blocking pair)
    field_b_term: labor market equilibrium (no mutually beneficial unsatisfied worker-firm pair)
    note: Stability is the market-design analog of Nash equilibrium for matching problems
  - field_a_term: deferred acceptance algorithm, O(n²)
    field_b_term: NRMP residency match, school assignment mechanism
    note: Real institutions implement a mathematical algorithm — often without knowing it
  - field_a_term: strategy-proof mechanism (truthful reporting is dominant strategy)
    field_b_term: incentive-compatible market design
    note: DA is strategy-proof for the proposing side; Boston mechanism is not
  - field_a_term: gross substitutes condition (Kelso-Crawford)
    field_b_term: condition for competitive equilibrium existence with worker complementarities
    note: Violated when firms value workers as complements — equilibrium may not exist
  - field_a_term: Shapley-Shubik assignment game core
    field_b_term: set of competitive equilibrium wages
    note: Core = competitive equilibria — cooperative and competitive concepts coincide
  - field_a_term: monopsony (single buyer)
    field_b_term: wage below marginal product, employment below efficient level
    note: Predicts observed wage suppression in geographically isolated labor markets
related_unknowns:
  - u-matching-markets-dynamic-stability
related_hypotheses:
  - h-da-mechanism-welfare-improving-redesign
cross_pollination_opportunities:
  - >
    Dynamic matching markets (workers and firms arrive and depart over time) require
    generalizing the static Gale-Shapley framework — an open mathematical problem with
    direct relevance to gig-economy platform design and real-time ride-sharing assignment.
  - >
    Algorithmic fairness in school choice: measuring demographic disparities in
    assignment outcomes across different matching mechanisms using tools from
    combinatorics and social-choice theory.
communication_gap: >
  Gale and Shapley published in the American Mathematical Monthly as a mathematical
  puzzle (1962). The economic significance was recognized only by Roth (1984), who
  connected it to real NRMP data. Mathematicians rarely read economics journals, and
  economists rarely read combinatorics literature. The 2012 Nobel Prize substantially
  raised mutual awareness but the two communities still publish in separate venues.
last_reviewed: "2026-05-06"
references:
  - doi: "10.2307/2312726"
    note: "Gale & Shapley (1962) Am Math Mon 69:9 — deferred acceptance algorithm"
  - doi: "10.1086/261272"
    note: "Roth (1984) J Polit Econ 92:991 — NRMP as stable matching"
  - doi: "10.2307/1913392"
    note: "Kelso & Crawford (1982) Econometrica 50:1483 — labor markets with complementarities"
  - doi: "10.1007/BF01753437"
    note: "Shapley & Shubik (1972) Int J Game Theory 1:111 — assignment game"
""")

# ─── Bridge C: Biology ↔ Physics — Viral Self-Assembly and Capsid Physics ───
write('cross-domain/biology-physics/b-viral-self-assembly-capsid-physics.yaml', """\
id: b-viral-self-assembly-capsid-physics
title: >
  Viral capsids self-assemble from identical protein subunits into icosahedral shells
  whose geometry is fully predicted by Caspar-Klug triangulation theory, and whose
  thermodynamics and cooperative kinetics are quantitatively described by nucleation-
  elongation models from polymer physics.
status: established
fields:
  - biology
  - physics
  - structural-biology
  - biophysics
bridge_claim: >
  Caspar and Klug (1962) showed that icosahedral capsids can be indexed by the
  triangulation number T = h² + hk + k² (h, k non-negative integers), giving 60T
  protein subunits per capsid. Most plant viruses have T=3 (180 subunits); adenovirus
  has T=25 (1500 subunits); bacteriophage HK97 has T=7. This purely geometric
  prediction matches observed capsid structures to high accuracy.

  Assembly thermodynamics: ΔG_assembly = ΔH_subunit-subunit - T·ΔS_translational.
  The favorable enthalpy from protein-protein contacts at quasi-equivalent interfaces
  drives assembly; the entropic cost of immobilizing subunits must be overcome.
  At equilibrium, a critical assembly concentration (CAC) analogous to the CMC for
  micelles sets the threshold below which free subunits predominate.

  The Zlotnick nucleation-elongation model (1994): assembly proceeds via a slow
  nucleation step (forming a critical nucleus of ~5 subunits) followed by rapid
  elongation. This produces the characteristic sigmoidal kinetics with a concentration-
  dependent lag phase — identical in form to protein fibril nucleation and polymer
  crystallization.

  Viral genome packaging motors (bacteriophage phi29): one of the most powerful
  molecular motors known, generating >50 pN of compressive force to pack dsDNA
  against osmotic and electrostatic repulsion inside the capsid. Single-molecule
  optical tweezers measurements (Smith et al. 2001) directly measured the force-
  velocity relationship of this motor.

  RNA viruses exploit electrostatic co-assembly: positively charged N-terminal tails
  of coat proteins condense the negatively charged RNA genome, lowering the free
  energy of assembly and providing specificity (packaging signal recognition).
translation_table:
  - field_a_term: triangulation number T = h² + hk + k²
    field_b_term: geometrical tiling index for icosahedral surfaces
    note: Pure geometry predicts subunit count 60T and quasi-equivalence of subunit environments
  - field_a_term: critical assembly concentration (CAC)
    field_b_term: critical micelle concentration (CMC) analog
    note: Below CAC, subunits remain as monomers; above CAC, capsids dominate
  - field_a_term: nucleation lag phase
    field_b_term: nucleation in crystallization and fibril assembly — identical kinetic form
    note: Zlotnick model parameters map onto classical nucleation theory
  - field_a_term: phi29 packaging motor force (>50 pN)
    field_b_term: molecular motor mechanics — F-V curve, stall force
    note: Measured by optical tweezers; surpasses myosin and kinesin force generation
  - field_a_term: electrostatic co-assembly (RNA-capsid)
    field_b_term: polyelectrolyte condensation by multivalent cations
    note: Analogous to DNA compaction by histones — charge neutralization drives condensation
related_unknowns:
  - u-capsid-assembly-kinetic-intermediates
related_hypotheses:
  - h-rna-electrostatic-packaging-signal-design
cross_pollination_opportunities:
  - >
    Caspar-Klug theory predicts allowable T numbers but not which T a given coat protein
    will adopt. Coarse-grained molecular dynamics simulations with physics-based
    interaction potentials can now predict T number from sequence — a direct bridge
    between sequence space and geometric outcome.
  - >
    Antiviral strategies targeting the nucleation step: small molecules that
    accelerate aberrant capsid assembly (mis-assembly into non-icosahedral forms)
    can block viral replication — a physics-based drug design principle (e.g., CAM
    drugs against HBV).
communication_gap: >
  Caspar and Klug published in Cold Spring Harbor Symposia (structural biology), while
  the nucleation-elongation kinetics literature is primarily in biophysics and soft-
  matter physics journals. Virologists focused on genetics and replication rarely
  engage with the quantitative assembly physics literature. Single-molecule
  biophysicists and structural virologists have begun to converge, but the broader
  communities remain siloed by journal and conference culture.
last_reviewed: "2026-05-06"
references:
  - doi: "10.1101/SQB.1962.027.001.008"
    note: "Caspar & Klug (1962) Cold Spring Harb Symp Quant Biol 27:1 — triangulation theory"
  - doi: "10.1006/jmbi.1994.1318"
    note: "Zlotnick (1994) J Mol Biol 241:59 — nucleation-elongation capsid assembly model"
  - doi: "10.1038/35098134"
    note: "Smith et al. (2001) Nature 413:748 — phi29 packaging motor optical tweezers"
  - note: "Hagan (2014) Adv Chem Phys 155:1 — theory of viral capsid assembly"
""")

# ─── Bridge D: Engineering ↔ Social Science — Smart Cities and Urban Data Analytics ───
write('cross-domain/engineering-social-science/b-smart-cities-urban-data-analytics.yaml', """\
id: b-smart-cities-urban-data-analytics
title: >
  Smart city platforms bridge engineering control theory and social science: IoT sensor
  networks feed model predictive control for traffic and energy optimization, while
  differential privacy mechanisms address the fundamental tension between urban
  data utility and individual rights.
status: established
fields:
  - engineering
  - social-science
  - computer-science
  - urban-planning
bridge_claim: >
  Smart city platforms aggregate IoT sensor data (traffic flow, air quality, energy
  consumption, pedestrian density) for real-time urban management. The data pipeline
  runs from edge computing (latency <10 ms for local decisions) through fog-layer
  aggregation to cloud ML inference for city-scale optimization.

  Traffic signal optimization using model predictive control (MPC): formulate the
  intersection as a dynamical system, solve a receding-horizon optimal control problem
  to minimize total vehicle delay. Empirical deployments reduce average travel delay
  20-40% versus fixed-timing plans (Zheng et al. 2014). The optimization is a form
  of linear programming with flow-conservation constraints.

  Energy demand response: ML forecasting of building thermal loads combined with
  real-time grid price signals enables HVAC schedule optimization that reduces peak
  demand 15% without comfort degradation. This closes the loop between energy
  engineering and behavioral economics (demand elasticity).

  The fundamental social-science tension: aggregate mobility data (cellphone GPS
  traces) enables accurate population flow modeling but is individually re-identifiable
  even after naive anonymization. Differential privacy (Dwork 2006) adds calibrated
  Laplace or Gaussian noise with privacy budget epsilon (ε-DP), providing a
  mathematically rigorous bound on information leakage — but the accuracy-privacy
  tradeoff is stark at fine spatial resolution.

  Equity concerns: algorithmic traffic routing through disadvantaged neighborhoods
  (to minimize system-wide delay) imposes noise, pollution, and safety costs on
  politically marginalized communities — a concrete instance where engineering
  optimization ignores distributional social welfare.
translation_table:
  - field_a_term: model predictive control (MPC) receding horizon
    field_b_term: sequential social decision-making under uncertainty
    note: MPC formalizes the engineering intuition of rolling planning; social planners face the same structure
  - field_a_term: IoT sensor network data stream
    field_b_term: behavioral trace data (mobility, consumption, social interaction)
    note: The same data stream is simultaneously an engineering input and a social surveillance concern
  - field_a_term: differential privacy parameter epsilon (ε)
    field_b_term: privacy-utility tradeoff — social norm boundary
    note: ε is an engineering parameter but its acceptable value is a social/political choice
  - field_a_term: peak demand reduction 15% (HVAC optimization)
    field_b_term: demand elasticity — behavioral response to dynamic pricing
    note: Engineering optimization requires a social-science model of occupant behavior
  - field_a_term: system-optimal traffic assignment (Wardrop second principle)
    field_b_term: social welfare maximization vs. Nash equilibrium (user equilibrium)
    note: System-optimal routing requires coordination that individual drivers do not spontaneously produce
related_unknowns:
  - u-smart-city-equity-algorithmic-routing
related_hypotheses:
  - h-differential-privacy-urban-analytics-accuracy-threshold
cross_pollination_opportunities:
  - >
    Federated learning on distributed urban IoT data: train city-wide models without
    centralizing sensitive data — bridges ML engineering with privacy law compliance
    (GDPR, CCPA) in a technically rigorous way.
  - >
    Participatory sensing platforms that give residents control over their data
    contribution could resolve the equity-efficiency tension while generating richer
    behavioral data for urban planners.
communication_gap: >
  Smart city engineering is dominated by computer science and control engineering
  conferences (IEEE, ACM) while the equity, privacy, and governance implications
  are studied in urban planning, sociology, and law journals. Privacy engineers and
  civil society organizations occupy different professional worlds. The differential
  privacy literature (theory CS) is rarely read by urban planners, and vice versa.
last_reviewed: "2026-05-06"
references:
  - note: "Batty (2013) The New Science of Cities. MIT Press"
  - note: "Zheng et al. (2014) ACM Trans Intell Syst Technol 5:29 — urban computing survey"
  - note: "Dwork (2006) ICALP LNCS 4052:1 — differential privacy definition"
  - note: "Albino et al. (2015) Cities 45:1 — smart city concepts review"
""")

# ─── Bridge E: Physics ↔ Mathematics — Fluid Instabilities and Bifurcation Theory ───
write('cross-domain/physics-mathematics/b-fluid-instabilities-bifurcation.yaml', """\
id: b-fluid-instabilities-bifurcation
title: >
  Fluid instabilities — Rayleigh-Bénard convection, Kelvin-Helmholtz, Plateau-Rayleigh
  — are physical realizations of mathematical bifurcations: the transition from laminar
  to convective flow is a pitchfork bifurcation at Ra_c = 1708, and Lorenz's three-mode
  truncation of the Bénard equations produced the first mathematical proof of deterministic
  chaos.
status: established
fields:
  - physics
  - mathematics
  - fluid-dynamics
  - nonlinear-dynamics
bridge_claim: >
  Rayleigh-Bénard convection: a fluid heated from below and cooled from above undergoes
  a transition from pure conduction to convective rolls when the Rayleigh number
  Ra = g*alpha*DeltaT*L³/(nu*kappa) exceeds the critical value Ra_c = 1708 (from
  linear stability analysis). This transition is a supercritical pitchfork bifurcation
  in the mathematical sense: the conduction state loses stability and two mirror-symmetric
  convective roll states emerge continuously.

  At higher Ra, a Hopf bifurcation occurs — the stationary rolls give way to oscillating
  convection (time-periodic solution). Further Ra increase leads to torus bifurcations
  and eventually chaos through the Ruelle-Takens-Newhouse route.

  Lorenz (1963): truncating the Bénard equations to three Fourier modes (X, Y, Z) yields
  the Lorenz system: dX/dt = sigma(Y-X), dY/dt = X(r-Z)-Y, dZ/dt = XY-bZ. For
  sigma=10, b=8/3, r=28, this system exhibits the Lorenz strange attractor — bounded,
  aperiodic, fractal dimension ~2.06, positive Lyapunov exponent lambda>0. This was
  the first mathematical demonstration of deterministic chaos (sensitive dependence on
  initial conditions — the butterfly effect).

  Kelvin-Helmholtz instability: velocity shear at a fluid interface with density
  difference grows at rate proportional to k*DeltaU (wavenumber times velocity jump).
  In bifurcation language, this is a linear instability that saturates in vortex roll-up
  — a secondary bifurcation from the shear-flow base state.

  Plateau-Rayleigh instability: a liquid jet of radius R breaks into droplets when
  perturbation wavelength lambda > 2*pi*R (surface-tension-driven). This is a linear
  instability with growth rate sigma ~ (kR)²(1-(kR)²)/... — again described by linear
  stability theory followed by nonlinear saturation (droplet formation).

  All these phenomena are unified by the bifurcation theory of dynamical systems:
  linear stability analysis identifies the onset, weakly nonlinear theory gives the
  bifurcation type, and center manifold reduction captures the essential dynamics near
  threshold.
translation_table:
  - field_a_term: Rayleigh number Ra_c = 1708
    field_b_term: bifurcation parameter value at pitchfork bifurcation point
    note: Ra plays the role of the control parameter mu in the normal form X' = mu*X - X³
  - field_a_term: convective rolls (stationary pattern)
    field_b_term: stable fixed points emerging at supercritical pitchfork bifurcation
    note: Amplitude of rolls scales as sqrt(Ra - Ra_c) — classic bifurcation scaling
  - field_a_term: oscillating convection onset
    field_b_term: Hopf bifurcation — limit cycle emerges from fixed point
    note: Period of oscillation is set by the imaginary part of eigenvalues at criticality
  - field_a_term: Lorenz strange attractor
    field_b_term: chaotic attractor with positive Lyapunov exponent, fractal dimension
    note: First mathematical proof that deterministic ODEs can produce unpredictable trajectories
  - field_a_term: Plateau-Rayleigh jet breakup at lambda > 2*pi*R
    field_b_term: linear instability threshold — fastest-growing mode sets droplet size
    note: Droplet spacing predicted by maximizing growth rate sigma(k)
related_unknowns:
  - u-lorenz-attractor-universality-class
related_hypotheses:
  - h-rayleigh-benard-turbulence-bifurcation-cascade
cross_pollination_opportunities:
  - >
    Machine learning identification of bifurcation structure from fluid simulation data:
    sparse identification of nonlinear dynamics (SINDy) can reconstruct the Lorenz system
    from trajectory data — a bridge between data-driven ML and dynamical systems theory.
  - >
    Climate tipping points as bifurcations: AMOC slowdown, Arctic sea-ice loss, and
    Amazon dieback may be saddle-node bifurcations — critical slowing down (diverging
    return time) provides early-warning indicators detectable in observational data.
communication_gap: >
  Fluid dynamicists publishing in Journal of Fluid Mechanics and Physics of Fluids
  largely overlap with mathematicians working in nonlinear dynamics, but the connection
  is not universal. Applied mathematicians familiar with bifurcation theory sometimes
  lack physical intuition for fluid instabilities, while experimentalists focus on
  pattern selection without engaging the underlying mathematical framework. Chaos theory
  (Strogatz 1994 textbook) has helped bridge this gap for students.
last_reviewed: "2026-05-06"
references:
  - doi: "10.1080/14786441608635602"
    note: "Rayleigh (1916) Philos Mag 32:529 — linear stability analysis of convection"
  - doi: "10.1175/1520-0469(1963)020<0130:DNF>2.0.CO;2"
    note: "Lorenz (1963) J Atmos Sci 20:130 — deterministic nonperiodic flow, strange attractor"
  - note: "Drazin & Reid (2004) Hydrodynamic Stability. Cambridge University Press"
  - note: "Strogatz (1994) Nonlinear Dynamics and Chaos. Perseus Books"
""")

# ─── Bridge F: Ecology ↔ Biology — Coevolution and Arms Races ───
write('cross-domain/ecology-biology/b-coevolution-arms-races.yaml', """\
id: b-coevolution-arms-races
title: >
  Coevolution between interacting species drives reciprocal evolutionary arms races —
  the Red Queen hypothesis (Van Valen 1973) — whose dynamics are quantitatively
  described by the community interaction matrix and eigenvalue analysis, unifying
  evolutionary biology and ecological stability theory.
status: established
fields:
  - ecology
  - biology
  - evolutionary-biology
  - population-genetics
bridge_claim: >
  Coevolution is reciprocal evolutionary change in interacting species. The Red Queen
  hypothesis (Van Valen 1973): species must continually evolve just to maintain fitness
  relative to coevolving partners — constant selection pressure with no stable equilibrium.
  Named for the Red Queen in Through the Looking-Glass: "it takes all the running you
  can do, to keep in the same place."

  Predator-prey arms races: cheetah speed coevolves with gazelle speed; dorsal coloration
  in polymorphic prey coevolves with predator search images. The toxin resistance case
  is the most quantitatively studied: garter snakes (Thamnophis sirtalis) have evolved
  tetrodotoxin (TTX) resistance through convergent amino acid substitutions in Nav1.4
  voltage-gated sodium channels (the same TTX resistance as puffer fish — independent
  evolution of identical molecular solutions). Resistance level correlates geographically
  with local rough-skinned newt (Taricha) TTX levels (Brodie et al. 2002).

  Thompson's geographic mosaic theory (2005): coevolution is spatially structured with
  "hot spots" (where both species exert reciprocal selection) and "cold spots" (where
  only one species drives selection). The geographic mosaic predicts trait diversity
  across populations and explains why arms races are not globally synchronous.

  The mathematical bridge: at ecological equilibrium, the community interaction matrix
  J_{ij} = ∂f_i/∂x_j encodes how species i's growth rate responds to changes in
  species j's density. The eigenvalues of J determine stability; when coevolution drives
  the interaction coefficients, the eigenvalues track along trajectories in complex
  space — stable coexistence requires all eigenvalues to have negative real part, while
  Red Queen dynamics correspond to eigenvalues with nonzero imaginary part (oscillatory
  coevolution).

  Dawkins and Krebs (1979) formalized the asymmetry of arms races: prey must win every
  time (one failure = death), predators need only win occasionally (one success = meal).
  This "life-dinner principle" predicts faster evolution in prey — testable via
  substitution rate analysis of interacting proteins.
translation_table:
  - field_a_term: Red Queen (constant coevolution, no equilibrium)
    field_b_term: eigenvalues of J with nonzero imaginary part — oscillatory dynamics
    note: Persistent oscillation in trait space rather than convergence to equilibrium
  - field_a_term: TTX resistance level in garter snakes
    field_b_term: quantitative trait matching coevolving partner trait
    note: Resistance tracks local newt TTX production level — geographic mosaic prediction confirmed
  - field_a_term: geographic hot spot / cold spot
    field_b_term: spatially variable selection coefficient s
    note: s > 0 at hot spots drives reciprocal change; s ≈ 0 at cold spots does not
  - field_a_term: life-dinner principle (asymmetric selection)
    field_b_term: asymmetric fitness landscape — faster molecular evolution in prey proteins
    note: Substitution rate d_N/d_S elevated in prey receptor genes vs. predator toxin genes
  - field_a_term: community interaction matrix J_{ij}
    field_b_term: coevolutionary dynamics as flow on the J matrix landscape
    note: Eigen-analysis of J predicts whether coevolution leads to stability or Red Queen cycling
related_unknowns:
  - u-red-queen-molecular-clock-arms-race
related_hypotheses:
  - h-geographic-mosaic-coevolution-trait-variance
cross_pollination_opportunities:
  - >
    Genomic signatures of arms races: comparing d_N/d_S ratios in receptor genes
    (prey) versus ligand/toxin genes (predator/parasite) across the geographic mosaic
    could quantitatively test the life-dinner principle at the molecular level.
  - >
    Host-pathogen coevolution (MHC diversity, influenza antigenic drift, HIV escape)
    can be modeled with the same community matrix framework, connecting evolutionary
    ecology with immunology and vaccinology.
communication_gap: >
  Evolutionary ecology journals (Evolution, American Naturalist) and molecular biology
  journals rarely cross-cite on this topic. The mathematical community-matrix framework
  for stability is known to theoretical ecologists but rarely applied to coevolutionary
  dynamics. Van Valen's original paper was rejected by major journals and published in
  his own journal (Evolutionary Theory) — indicating disciplinary resistance to the idea.
last_reviewed: "2026-05-06"
references:
  - note: "Van Valen (1973) Evol Theory 1:1 — Red Queen hypothesis"
  - doi: "10.1111/j.0014-3820.2002.tb01373.x"
    note: "Brodie et al. (2002) Evolution 56:2067 — TTX resistance geographic coevolution"
  - note: "Thompson (2005) The Geographic Mosaic of Coevolution. University of Chicago Press"
  - doi: "10.1098/rspb.1979.0081"
    note: "Dawkins & Krebs (1979) Proc R Soc B 205:489 — arms races and the life-dinner principle"
""")

# ─── Bridge G: Mathematics ↔ Engineering — Optimization Theory and Machine Learning ───
write('cross-domain/mathematics-engineering/b-optimization-theory-machine-learning.yaml', """\
id: b-optimization-theory-machine-learning
title: >
  Convex optimization theory (KKT conditions, strong duality, convergence rates for
  gradient descent) provides the mathematical foundation for machine learning training,
  while empirical ML discoveries — the dominance of saddle points over local minima in
  high dimensions and the lottery ticket hypothesis — require extending classical theory
  beyond convexity.
status: established
fields:
  - mathematics
  - engineering
  - computer-science
  - machine-learning
bridge_claim: >
  Convex optimization: minimize f(x) subject to x in C (convex set). The Lagrangian
  L(x,lambda,mu) = f(x) + lambda^T h(x) + mu^T g(x) and dual function g(lambda,mu) =
  inf_x L satisfy strong duality (primal = dual) under Slater's condition.
  KKT conditions are necessary and sufficient: stationarity, primal feasibility, dual
  feasibility, complementary slackness.

  Gradient descent convergence: for L-smooth, mu-strongly convex f, the iterates satisfy
  ||x_t - x*||² ≤ (1 - mu/L)^t ||x_0 - x*||² — geometric convergence rate determined
  by the condition number kappa = L/mu. Momentum (Nesterov) achieves the optimal rate
  O(1/t²) for smooth convex problems.

  The Adam optimizer (Kingma and Ba 2015): adaptive learning rates for each parameter
  (scaled by EMA of squared gradients) plus momentum. Convergence on non-convex
  stochastic objectives is not guaranteed by classical theory — Adam converges on
  smooth non-convex functions at rate O(1/sqrt(T)) to a stationary point, not necessarily
  a global minimum.

  Neural network loss landscapes: in high dimensions (millions of parameters), local
  minima are almost non-existent — instead, saddle points dominate (Dauphin et al. 2014).
  At a saddle point, the Hessian has both positive and negative eigenvalues; gradient
  descent escapes saddle points when perturbed by noise (SGD noise helps). This empirical
  discovery explains why SGD works despite non-convexity — the loss landscape is not
  the adversarial non-convex case that classical theory fears.

  Lottery ticket hypothesis (Frankle and Carlin 2019): randomly initialized dense neural
  networks contain sparse subnetworks (winning tickets) that can be trained in isolation
  to full accuracy. This suggests neural networks are dramatically over-parameterized and
  that the true solution structure is sparse — connecting to compressed sensing and
  L1 regularization theory.
translation_table:
  - field_a_term: KKT stationarity condition
    field_b_term: zero-gradient condition at neural network training convergence
    note: KKT is necessary at any local minimum; sufficient only for convex problems
  - field_a_term: condition number kappa = L/mu
    field_b_term: learning rate sensitivity — large kappa requires small learning rate for stability
    note: Adam mitigates large kappa by adapting per-parameter learning rates
  - field_a_term: Lagrange multiplier lambda
    field_b_term: regularization coefficient (L2 regularization = Lagrange constraint on norm)
    note: L2 regularization is equivalent to adding a quadratic constraint to the primal
  - field_a_term: saddle point (indefinite Hessian)
    field_b_term: dominant critical point type in high-dimensional neural network loss landscape
    note: Dauphin (2014): fraction of negative Hessian eigenvalues tracks loss value
  - field_a_term: L1 regularization (sparse solution)
    field_b_term: winning ticket subnetwork (sparse trained-in-isolation subnetwork)
    note: Lottery ticket hypothesis has connections to compressed sensing and L1-induced sparsity
related_unknowns:
  - u-neural-network-loss-landscape-global-structure
related_hypotheses:
  - h-lottery-ticket-sparse-subnetwork-universality
cross_pollination_opportunities:
  - >
    Non-convex optimization guarantees for neural networks: can manifold-structure
    assumptions on the loss landscape (e.g., benign non-convexity, no spurious local
    minima) be proved for specific architectures (two-layer networks, transformers)?
    This is an active mathematical frontier.
  - >
    Quantum optimization algorithms (QAOA, VQE) for ML training: quantum annealing
    may escape saddle points more efficiently than gradient-based methods — a potential
    speedup if quantum hardware scales.
communication_gap: >
  Convex optimization was developed by operations research and applied mathematics
  communities (Boyd and Vandenberghe textbook published 2004) largely before deep
  learning became dominant. Deep learning practitioners rarely use classical
  optimization convergence proofs in practice. The theoretical ML community has
  tried to bridge this gap but key questions (why does SGD generalize well? what
  is the correct convergence notion for non-convex neural networks?) remain open,
  keeping the communities somewhat separated.
last_reviewed: "2026-05-06"
references:
  - note: "Boyd & Vandenberghe (2004) Convex Optimization. Cambridge University Press"
  - note: "Kingma & Ba (2015) ICLR — Adam optimizer"
  - note: "Dauphin et al. (2014) NeurIPS 27 — saddle points in high-dimensional optimization"
  - note: "Frankle & Carlin (2019) ICLR — lottery ticket hypothesis"
""")

# ─── Bridge H: Neuroscience ↔ Biology — Neurodegeneration and Protein Aggregation ───
write('cross-domain/neuroscience-biology/b-neurodegeneration-protein-aggregation.yaml', """\
id: b-neurodegeneration-protein-aggregation
title: >
  All major neurodegenerative diseases — Parkinson's (alpha-synuclein), Alzheimer's
  (Abeta, tau), and prion diseases — are protein aggregation disorders with nucleation-
  elongation kinetics identical to protein crystallization, and they spread through
  neural circuits by prion-like templated misfolding.
status: established
fields:
  - neuroscience
  - biology
  - biochemistry
  - molecular-biology
bridge_claim: >
  Parkinson's disease: alpha-synuclein (SNCA gene product) misfolds from its natively
  unstructured form into beta-sheet-rich oligomers and then into Lewy body inclusions.
  The aggregation kinetics follow nucleation-elongation theory: a slow lag phase
  (nucleation of a critical oligomeric nucleus) followed by exponential elongation and
  saturation — identical in form to protein crystallization and amyloid fibril growth.
  The same kinetic equations describe both benign protein crystals and pathological
  amyloid fibrils.

  Prion-like propagation (Braak staging): Braak and Braak (1991) showed that Lewy
  pathology in Parkinson's follows a stereotyped anatomical progression from the
  enteric nervous system and brainstem (Braak stage 1-2) through the midbrain (stage 3-4)
  to the neocortex (stage 5-6). Misfolded alpha-synuclein acts as a template that
  converts native protein in adjacent neurons — prion-like propagation along neural
  circuit connections, spreading over decades.

  Alzheimer's disease: two protein aggregation processes proceed in parallel — extracellular
  amyloid-beta (Abeta) plaques and intracellular tau neurofibrillary tangles. The amyloid
  cascade hypothesis (Hardy and Selkoe 2002): Abeta accumulation is the initiating event
  that drives downstream tau pathology and neurodegeneration. Tau also spreads in a
  prion-like pattern following the entorhinal-hippocampal-neocortical circuit hierarchy
  (Braak tau staging).

  Prusiner's prion hypothesis (Nobel 1997): the prion protein PrP^C misfolds into PrP^Sc,
  which catalytically converts PrP^C — pure protein-based infectious agent with no
  nucleic acid. The same conformational templating mechanism is now recognized in all
  major neurodegenerative diseases, turning them from distinct pathologies into a
  unified class of prion-like proteinopathies.

  The common quantitative framework: all these systems obey nucleation-elongation kinetics
  with rate constants k_n (nucleation), k_+ (elongation), k_- (disaggregation), and
  critical concentration analogous to CMC. Therapeutic strategy follows: inhibit nucleation
  (anti-aggregation small molecules), accelerate clearance (immunotherapy), or prevent
  prion-like spread (antibodies targeting extracellular seeds).
translation_table:
  - field_a_term: nucleation lag phase (critical nucleus)
    field_b_term: slow initiation of Lewy body / plaque formation in early disease
    note: Lag phase duration is concentration-dependent; explains decades of silent progression
  - field_a_term: elongation rate constant k_+
    field_b_term: rate of amyloid fibril growth by monomer addition
    note: Amenable to inhibition by small molecules or antibodies targeting fibril ends
  - field_a_term: prion-like templated misfolding
    field_b_term: prion mechanism applied to Parkinson's, Alzheimer's, ALS
    note: Braak staging is the anatomical manifestation of prion-like circuit propagation
  - field_a_term: amyloid cascade hypothesis (Abeta initiates tau, tau drives death)
    field_b_term: upstream-downstream causal chain in disease progression
    note: Hardy & Selkoe (2002) — tested by anti-Abeta immunotherapy trials
  - field_a_term: critical aggregation concentration
    field_b_term: threshold alpha-synuclein or Abeta concentration for aggregation onset
    note: Explains why gene dosage (triplication vs. duplication) matters for age of onset
related_unknowns:
  - u-prion-like-spread-neurodegeneration-circuit-specificity
related_hypotheses:
  - h-tau-propagation-circuit-connectivity-determines-staging
cross_pollination_opportunities:
  - >
    Cryo-electron microscopy structures of alpha-synuclein and tau filaments from
    patient brains reveal that different diseases produce different fibril polymorphs
    (strains) — explaining why Parkinson's, DLB, and MSA have different alpha-synuclein
    strains. This connects structural biology to clinical heterogeneity.
  - >
    Glymphatic clearance failure (sleep disruption → Abeta accumulation) connects
    neurodegenerative biology to sleep medicine — a therapeutic opportunity targeting
    glymphatic flow augmentation during sleep.
communication_gap: >
  Neurodegeneration research is historically siloed by disease (Alzheimer's researchers
  vs. Parkinson's researchers) despite the mechanistic commonality. Protein biophysicists
  who study nucleation-elongation kinetics rarely collaborate with neurologists who treat
  patients. The prion-like framing was initially controversial among disease-specific
  communities. The Braak staging papers (neuropathology) took years to be absorbed by
  the molecular biology and drug development communities.
last_reviewed: "2026-05-06"
references:
  - doi: "10.1126/science.1072994"
    note: "Hardy & Selkoe (2002) Science 297:353 — amyloid cascade hypothesis"
  - doi: "10.1007/BF00308809"
    note: "Braak & Braak (1991) Acta Neuropathol 82:239 — Parkinson's staging"
  - doi: "10.1073/pnas.95.23.13363"
    note: "Prusiner (1998) PNAS 95:13363 — prion hypothesis"
  - doi: "10.1038/388839a0"
    note: "Spillantini et al. (1997) Nature 388:839 — alpha-synuclein in Lewy bodies"
""")

# ─── Bridge I: Social Science ↔ Chemistry — Drug Policy and Pharmacoepidemiology ───
write('cross-domain/social-science-chemistry/b-drug-policy-pharmacoepidemiology.yaml', """\
id: b-drug-policy-pharmacoepidemiology
title: >
  Pharmacoepidemiology bridges the molecular pharmacology of opioid receptor binding
  and the social epidemiology of the opioid crisis — harm reduction policies (naloxone
  distribution, methadone maintenance) derive their evidence base from both mu-receptor
  pharmacokinetics and population-level randomized trial data.
status: established
fields:
  - social-science
  - chemistry
  - pharmacology
  - epidemiology
bridge_claim: >
  Pharmacoepidemiology studies drug effects at the population level, connecting molecular
  pharmacology to public health policy. The opioid epidemic illustrates this bridge at
  scale: prescription opioid deaths triggered heroin substitution which triggered illicit
  fentanyl (100x more potent than morphine) — an epidemiological cascade driven by
  manufacturer-funded physician incentive structures (Purdue Pharma) and regulatory failure.

  Naloxone (Narcan): a competitive mu-opioid receptor antagonist with Ki ≈ 1 nM,
  reversing opioid overdose within 2-5 minutes. Its pharmacokinetics (t½ ≈ 60-90 min,
  shorter than many opioid agonists) create a re-narcotization risk requiring repeated
  dosing. Population-level naloxone distribution is cost-effective at approximately
  $438/QALY (Coffin and Sullivan 2013) — below the standard US threshold of $50,000-
  100,000/QALY.

  Methadone maintenance treatment (MMT): methadone's long half-life (24-36h) prevents
  withdrawal and reduces cravings via sustained mu-receptor occupancy. Cochrane meta-
  analysis (Mattick et al. 2009): MMT reduces illicit opioid use 50-70% and crime
  40-60%, and decreases HIV transmission among PWID. Buprenorphine (partial agonist,
  ceiling effect) is equally effective with lower overdose risk.

  Drug scheduling controversy: the Controlled Substances Act Schedule I classification
  (high abuse potential, no medical use) for cannabis and psilocybin is contested by
  pharmacological evidence. Carhart-Harris et al. (2021) NEJM trial: psilocybin
  produces significant antidepressant effect comparable to SSRIs, with a single
  molecule producing neuroplasticity through 5-HT2A receptor agonism and BDNF upregulation.
  The evidence mismatch between pharmacology and policy is a direct social-science /
  chemistry divide.

  Harm reduction framework: policy interventions graded by risk (abstinence >
  medication-assisted treatment > supervised consumption sites > needle exchange >
  drug checking services). Each rung is evidence-based from clinical pharmacology
  but politically contested — the science-policy translation gap is primarily social.
translation_table:
  - field_a_term: mu-opioid receptor binding affinity (Ki)
    field_b_term: overdose reversal efficacy and required naloxone dose
    note: Higher-potency opioids (fentanyl Ki < 1 nM) may require higher or repeated naloxone doses
  - field_a_term: drug half-life (t½)
    field_b_term: dosing interval in treatment protocols — methadone once daily vs. heroin multiple times daily
    note: Pharmacokinetics directly determines adherence burden and diversion risk
  - field_a_term: 5-HT2A receptor agonism (psilocybin mechanism)
    field_b_term: antidepressant effect — schedule I classification vs. clinical evidence
    note: Molecular mechanism supports rescheduling; regulatory barrier is policy not pharmacology
  - field_a_term: harm reduction continuum
    field_b_term: public health policy ranking by risk-benefit ratio
    note: Policy tiers map onto pharmacological risk profiles — each tier has molecular rationale
  - field_a_term: opioid epidemic cascade (Rx → heroin → fentanyl)
    field_b_term: pharmacological substitution driven by market and regulatory incentives
    note: Fentanyl proliferation is partly driven by its greater potency-to-weight ratio (smuggling efficiency)
related_unknowns:
  - u-opioid-prescribing-policy-chemistry-disconnect
related_hypotheses:
  - h-psilocybin-rescheduling-neuroplasticity-evidence
cross_pollination_opportunities:
  - >
    Drug checking services: fentanyl test strips and mass spectrometry identification
    of novel psychoactive substances (NPS) could give PWID real-time pharmacological
    information — a direct chemistry-to-social-policy intervention.
  - >
    Precision addiction medicine: pharmacogenomics of mu-opioid receptor variants
    (OPRM1 A118G) predicts naltrexone treatment response — individual molecular variation
    can inform population-level policy targeting.
communication_gap: >
  Drug policy is primarily debated in political science, sociology, law, and public
  health literatures. Molecular pharmacologists who understand receptor binding and
  metabolism rarely engage in policy advocacy. The DEA scheduling process does not
  systematically integrate pharmacological evidence — it is primarily a legal and
  political process. The psilocybin scheduling controversy has helped bridge this gap
  by forcing explicit comparison of pharmacological evidence with scheduling criteria.
last_reviewed: "2026-05-06"
references:
  - doi: "10.1097/01.jom.0000479702.28107.52"
    note: "Kolodny et al. (2015) J Opioid Manag 11:5 — opioid epidemic drivers"
  - note: "Mattick et al. (2009) Cochrane Database — methadone maintenance effectiveness"
  - doi: "10.1056/NEJMoa2032994"
    note: "Carhart-Harris et al. (2021) N Engl J Med 384:1402 — psilocybin vs. escitalopram"
  - doi: "10.1016/S0140-6736(10)61462-6"
    note: "Nutt et al. (2010) Lancet 376:1558 — drug harms ranking"
""")

# ─── Bridge J: Physics ↔ Biology — Bioacoustics and Sound Production ───
write('cross-domain/physics-biology/b-bioacoustics-sound-production.yaml', """\
id: b-bioacoustics-sound-production
title: >
  Animal sound production and hearing are direct applications of acoustic physics —
  the Helmholtz resonator equation governs birdsong and vocal tract resonance, bat
  echolocation achieves near-physical-limit range resolution, and barn owl sound
  localization exploits interaural time differences with microsecond precision.
status: established
fields:
  - physics
  - biology
  - neuroscience
  - sensory-biology
bridge_claim: >
  Sound production in animals implements physical acoustic principles. Crickets
  stridulate by scraping a plectrum across file teeth — the resonant frequency is
  determined by file tooth spacing and wing membrane compliance, acting as a driven
  resonator. Frogs use vocal sac resonance to amplify calls; whales produce sound
  via laryngeal membranes coupled to complex nasal resonant chambers.

  The Helmholtz resonator equation f₀ = (c/2pi) * sqrt(A / (V*L)) where A is neck
  cross-sectional area, V is cavity volume, and L is effective neck length governs
  both engineering resonators and biological vocal structures. Bird syrinx resonance
  and human vocal tract formants are Helmholtz resonators tuned by muscular adjustment.

  Bat echolocation: frequency-modulated (FM) sweeps from 25-100 kHz provide range
  resolution delta_R = c / (2B) where B is bandwidth (c = 340 m/s, B ≈ 75 kHz gives
  delta_R ≈ 2.3 mm). Constant-frequency (CF) bats (horseshoe bats, Rhinolophus) adjust
  their emitted frequency to compensate for Doppler shift from their own flight speed,
  keeping the echo within the "acoustic fovea" (sharply tuned basilar membrane region)
  — Doppler compensation with precision ~0.1 Hz.

  Sound localization: the auditory brainstem computes interaural time difference (ITD)
  and interaural level difference (ILD) to locate sound sources. The barn owl (Tyto alba)
  achieves ITD resolution of ~1-2 microseconds — near the theoretical limit set by
  neural spike timing jitter. The nucleus laminaris (avian homolog of the medial
  superior olive) implements a delay-line coincidence detector exactly as proposed by
  Jeffress (1948) — a physical model (delay line + coincidence detector) realized in
  neural hardware.

  Green's function for sound propagation in the ocean: whale song propagates thousands
  of kilometers via the SOFAR channel (sound-fixing and ranging — minimum sound velocity
  at ~1000m depth), which acts as an acoustic waveguide. Blue whale B calls at 15-40 Hz
  can be detected at basin scales.
translation_table:
  - field_a_term: Helmholtz resonator f₀ = (c/2pi) sqrt(A/VL)
    field_b_term: vocal tract formant frequencies — F1, F2 shaped by tongue and lip position
    note: Human vowel production is Helmholtz resonator theory applied to a time-varying cavity
  - field_a_term: radar range resolution delta_R = c / (2B)
    field_b_term: bat echolocation range resolution delta_R ≈ 2-3 mm
    note: Bats achieve near-physical-limit range discrimination through wide-bandwidth FM sweeps
  - field_a_term: Doppler shift f_echo = f_emit * (c + v_target) / (c - v_bat)
    field_b_term: horseshoe bat Doppler compensation — adjusts call frequency to null own velocity
    note: CF bats maintain echo frequency in acoustic fovea; measured to 0.1 Hz precision
  - field_a_term: interaural time difference (ITD) — binaural cue
    field_b_term: barn owl 1-2 microsecond ITD resolution — near spike-timing limit
    note: Jeffress model delay-line coincidence detector implemented in nucleus laminaris
  - field_a_term: SOFAR channel (ocean acoustic waveguide)
    field_b_term: whale long-range communication — basin-scale song propagation
    note: Sound velocity minimum at ~1000m depth creates a waveguide confining low-frequency sound
related_unknowns:
  - u-whale-song-information-content-localization
related_hypotheses:
  - h-bat-echolocation-neural-matched-filter-implementation
cross_pollination_opportunities:
  - >
    Bioinspired sonar: bat echolocation algorithms (FM sweep + autocorrelation processing,
    CF Doppler compensation) could improve autonomous vehicle radar/lidar by incorporating
    active Doppler compensation and acoustic fovea-like selective frequency attention.
  - >
    Passive acoustic monitoring: automated bat call classification using ML trained on
    species-specific FM sweep signatures could replace expensive manual survey effort
    — directly applying echolocation physics to biodiversity monitoring.
communication_gap: >
  Bioacoustics spans physics (acoustics, signal processing), biology (animal behavior,
  neuroscience), and engineering (sonar design). Acoustical Society of America publishes
  across all three areas but researchers from each discipline primarily attend their
  own conferences. Bat echolocation researchers (Animal Behaviour, J Exp Biol) and
  radar/sonar engineers (IEEE) overlap far less than the physics would suggest.
last_reviewed: "2026-05-06"
references:
  - note: "Greenewalt (1968) Bird Song: Acoustics and Physiology. Smithsonian Institution Press"
  - doi: "10.1126/science.441058"
    note: "Simmons (1979) Science 204:1336 — bat echolocation target ranging"
  - doi: "10.1126/science.644324"
    note: "Knudsen & Konishi (1978) Science 200:795 — barn owl sound localization"
  - note: "Au (1993) The Sonar of Dolphins. Springer"
""")

# ─── Bridge K: Mathematics ↔ Physics — Differential Forms and Maxwell's Equations ───
write('cross-domain/mathematics-physics/b-differential-forms-maxwell.yaml', """\
id: b-differential-forms-maxwell
title: >
  Maxwell's equations expressed in differential form notation — dF = 0 and d*F = J —
  reveal that classical electromagnetism is a U(1) gauge theory, the Aharonov-Bohm
  effect is a purely topological phenomenon, and Chern-Weil theory connects curvature
  forms to topological invariants, unifying differential geometry with physics.
status: established
fields:
  - mathematics
  - physics
  - differential-geometry
  - topology
bridge_claim: >
  Maxwell's equations in classical vector notation (div B = 0, curl E = -dB/dt, div D = rho,
  curl H = J + dD/dt) are rewritten in the language of differential forms on 4-dimensional
  spacetime as two equations: dF = 0 and d*F = J, where F is the electromagnetic field
  strength 2-form, *F is its Hodge dual, and J is the 4-current 1-form.

  The equation dF = 0 (Bianchi identity) encodes both Faraday's law and the absence
  of magnetic monopoles. Since d(dA) = 0, we write F = dA where A is the electromagnetic
  potential 1-form — gauge freedom is the freedom to replace A by A + df for any scalar
  function f (exact form, no physical effect since d(df) = 0).

  The Hodge decomposition theorem: any k-form omega on a compact Riemannian manifold
  decomposes uniquely as omega = d*alpha + delta*beta + gamma, where d*alpha is exact,
  delta*beta is coexact, and gamma is harmonic (d*gamma = delta*gamma = 0). This is the
  geometric generalization of the Helmholtz decomposition of vector fields.

  The Aharonov-Bohm effect (1959): an electron traveling around a solenoid carrying
  magnetic flux Phi accumulates a quantum phase phi = (e/hbar) * ∮ A·dl even where
  B = curl A = 0 outside the solenoid. This is a purely topological effect — the line
  integral of A around the loop equals the enclosed flux by Stokes' theorem, but the
  local field vanishes. Experimentally confirmed by Chambers (1960) and subsequent
  electron interference experiments — topology directly affects physics.

  Chern-Weil theory: characteristic classes (Chern classes, Pontryagin classes) of
  fiber bundles are represented by closed differential forms constructed from the
  curvature of a connection. The first Chern class c1(L) = (1/2pi)[F] — the cohomology
  class of the field strength 2-form — classifies the topology of the line bundle.
  In physics: c1 counts the Dirac monopole charge; the second Chern class gives the
  instanton number in Yang-Mills theory.

  This framework is the natural language of modern gauge theory: the standard model
  of particle physics is a U(1) x SU(2) x SU(3) gauge theory, all expressed in
  terms of connection forms and curvature.
translation_table:
  - field_a_term: differential 2-form F = dA
    field_b_term: electromagnetic field tensor F_{mu nu} = partial_mu A_nu - partial_nu A_mu
    note: Form language makes coordinate independence manifest; tensor components are frame-dependent
  - field_a_term: Bianchi identity dF = 0
    field_b_term: no magnetic monopoles (div B = 0) + Faraday's law (curl E = -dB/dt)
    note: Two Maxwell equations unified into one topological identity
  - field_a_term: Hodge dual *F
    field_b_term: electric-magnetic duality (E <-> B under *F in vacuum)
    note: Hodge dual exchanges field strength with its dual — duality symmetry of vacuum Maxwell equations
  - field_a_term: Aharonov-Bohm phase (e/hbar) ∮ A·dl
    field_b_term: holonomy of the U(1) connection around a loop — topological invariant
    note: Phase is a Wilson loop — fundamental observable in gauge theory
  - field_a_term: first Chern class c1 in H²(M, Z)
    field_b_term: magnetic monopole charge (Dirac quantization condition)
    note: Topology quantizes charge — Dirac's heuristic derivation follows from c1 being integral
related_unknowns:
  - u-non-abelian-aharonov-bohm-observable-consequences
related_hypotheses:
  - h-chern-simons-theory-topological-quantum-computation
cross_pollination_opportunities:
  - >
    Topological insulators and topological superconductors: band topology classified by
    Chern numbers (2D) and Z₂ invariants (3D) — the mathematics of characteristic classes
    directly predicts protected surface states and is now central to condensed matter physics.
  - >
    Non-Abelian gauge theories (QCD, electroweak) expressed in terms of curvature forms:
    the Yang-Mills instanton (self-dual curvature F = *F) is characterized by the second
    Chern class, connecting topology to the QCD vacuum structure and CP violation.
communication_gap: >
  The differential forms approach to electromagnetism is standard in mathematical physics
  (Misner-Thorne-Wheeler, Nakahara) but is rarely taught in undergraduate physics courses
  that use Jackson (classical vector notation). Mathematics graduate students learning
  differential geometry do not typically see the Maxwell equations example until they
  encounter gauge theory. The Aharonov-Bohm effect, though over 60 years old, is still
  not in most undergraduate physics curricula despite being one of the cleanest
  demonstrations that topology enters physics directly.
last_reviewed: "2026-05-06"
references:
  - note: "Misner, Thorne & Wheeler (1973) Gravitation. W.H. Freeman — chapters on differential forms"
  - doi: "10.1103/PhysRev.115.485"
    note: "Aharonov & Bohm (1959) Phys Rev 115:485 — topological phase effect"
  - note: "Nakahara (2003) Geometry, Topology and Physics. IOP Publishing"
  - note: "Frankel (2012) The Geometry of Physics. Cambridge University Press"
""")

# ─── Bridge L: Ecology ↔ Engineering — Biomimicry and Sustainable Design ───
write('cross-domain/ecology-engineering/b-biomimicry-sustainable-design.yaml', """\
id: b-biomimicry-sustainable-design
title: >
  Biomimicry applies 3.8 billion years of evolutionary R&D to engineering design:
  lotus superhydrophobicity, kingfisher-beak aerodynamics, whale-tubercle lift
  enhancement, spider-silk mechanics, and termite-mound passive ventilation each
  solve engineering problems through biological principles refined by natural selection.
status: established
fields:
  - ecology
  - engineering
  - materials-science
  - sustainable-design
bridge_claim: >
  Biomimicry (Benyus 1997): natural selection has acted as a design engineer for
  3.8 billion years, solving mechanical, thermal, optical, and chemical challenges
  under constraints of material efficiency, scalability, and self-repair that human
  engineering rarely achieves.

  Lotus effect (superhydrophobicity): the lotus leaf surface has hierarchical micro-
  nano structures (papillae 10-20 μm with wax crystalloids 1-2 nm) that produce
  contact angle >150° and contact angle hysteresis <10° — water droplets bead and
  roll off carrying dirt particles (self-cleaning). Barthlott and Neinhuis (1997)
  characterized this surface and inspired Sto Lotusan paint and Gore-Tex textiles.
  The physics: the Cassie-Baxter state traps air pockets reducing solid-liquid contact
  area; the Wenzel state (complete wetting) is avoided by the dual-scale roughness.

  Kingfisher beak → Shinkansen bullet train nose: the kingfisher (Alcedo atthis)
  dives from air into water with minimal splash by having a beak that transitions
  smoothly between media of very different impedance (air Z≈415 Pa·s/m, water
  Z≈1.5x10⁶ Pa·s/m). The tapered beak profile minimizes pressure shock. The Shinkansen
  500 series nose (designed by Eiji Nakatsu, a birdwatcher) reduces tunnel boom by
  30%, decreases electricity use ~15%, and enables higher speeds.

  Whale flipper tubercles: leading-edge tubercles on humpback whale (Megaptera novaeangliae)
  pectoral fins act as passive vortex generators that delay stall and increase maximum
  lift angle. Fish and Battle (1995) characterized the tubercle geometry; WhalePower
  Corporation applied it to wind turbine blades achieving ~10% efficiency improvement
  and quieter operation.

  Spider silk: tensile strength 1.0-1.3 GPa (comparable to high-strength steel by
  weight), failure strain 40% (much greater than steel or Kevlar), toughness modulus
  ~160 MJ/m³ — greater than any known natural or synthetic fiber. The mechanical
  properties arise from beta-sheet nanocrystals embedded in an amorphous network
  (Gosline et al. 1999). Recombinant spider silk from transgenic goat milk (Nexia
  BioTechnologies) and E. coli expression systems are engineering this into scalable
  production.

  Termite mound ventilation: Macrotermes michaelseni termites maintain internal nest
  temperature ~30±1°C in a 40°C external environment using a passive ventilation
  system of surface flue chimneys and basal tunnels driven by thermal buoyancy —
  no fans, no A/C. The Eastgate Centre in Zimbabwe (architect Mick Pearce) implements
  this principle, using 85% less energy than a conventional air-conditioned building
  of similar size.
translation_table:
  - field_a_term: lotus leaf dual-scale roughness (papillae + wax nanocrystals)
    field_b_term: Cassie-Baxter superhydrophobic surface — contact angle >150°
    note: Hierarchical structure is essential; single-scale roughness achieves partial effect only
  - field_a_term: kingfisher beak impedance-matching taper
    field_b_term: Shinkansen nose profile — minimizes tunnel boom, reduces drag
    note: Bio-inspired aerodynamic profile derived from studying diving behavior
  - field_a_term: whale tubercle passive vortex generators
    field_b_term: wind turbine blade stall delay — lift angle +5°, efficiency +10%
    note: Tubercles disrupt laminar boundary layer; delay stall without active control
  - field_a_term: spider silk beta-sheet nanocrystal network
    field_b_term: high-toughness fiber — tensile strength 1.3 GPa, strain 40%
    note: Outperforms Kevlar in toughness (area under stress-strain curve) due to large failure strain
  - field_a_term: termite mound thermal buoyancy ventilation
    field_b_term: passive building ventilation — 85% energy savings vs. conventional A/C
    note: Eastgate Centre demonstrates scalability; requires no external energy input
related_unknowns:
  - u-spider-silk-recombinant-production-mechanical-parity
related_hypotheses:
  - h-biomimicry-design-convergence-performance-ceiling
cross_pollination_opportunities:
  - >
    Structural color from photonic nanostructures (morpho butterfly wings): iridescent
    structural color without pigment dye could inspire energy-efficient display and
    coloring technologies with no bleaching or environmental contamination.
  - >
    Bioinspired adhesion (gecko setae): Van der Waals adhesion from hierarchical seta
    arrays (spatulae 200 nm wide) produces dry adhesion ~10 N/cm² — inspiration for
    reversible surgical adhesives and climbing robots (Stanford Gecko Glove).
communication_gap: >
  Biomimicry is promoted in popular science (Benyus 1997, TED talks) but the engineering
  translation requires deep expertise in both the biological system (morphology,
  mechanics, physics of the biological solution) and the engineering application. Most
  engineers lack the biology background to identify relevant biological examples; most
  biologists lack the engineering background to extract design principles. Dedicated
  biomimicry research centers (e.g., Biomimicry Institute, AskNature database) have
  partially bridged this, but systematic translation remains rare.
last_reviewed: "2026-05-06"
references:
  - note: "Benyus (1997) Biomimicry: Innovation Inspired by Nature. William Morrow"
  - doi: "10.1007/PL00008818"
    note: "Barthlott & Neinhuis (1997) Planta 202:1 — lotus effect superhydrophobicity"
  - doi: "10.1002/jmor.1052250106"
    note: "Fish & Battle (1995) J Morphol 225:51 — humpback whale tubercle geometry"
  - doi: "10.1242/jeb.202.23.3295"
    note: "Gosline et al. (1999) J Exp Biol 202:3295 — mechanical properties of spider silk"
""")

print("All 12 bridge files written successfully.")

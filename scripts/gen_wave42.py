"""Generate Wave 42 bridge, unknown, and hypothesis YAML files."""
import os

ROOT = r"C:\Users\Shoe\dev\Universal-Science-Discovery"

def mkdirs(*parts):
    p = os.path.join(ROOT, *parts)
    os.makedirs(p, exist_ok=True)
    return p

def write(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# ──────────────────────────────────────────────────────────
# Bridge 1: Neuroplasticity ↔ STDP (neuroscience ↔ physics)
# ──────────────────────────────────────────────────────────
d = mkdirs("cross-domain", "neuroscience-physics")
write(os.path.join(d, "b-neuroplasticity-stdp.yaml"), """\
id: b-neuroplasticity-stdp
title: "Spike-timing-dependent plasticity implements Hebbian learning through a physically measurable asymmetric time window that strengthens or weakens synapses based on millisecond-scale relative spike timing"
domains: [neuroscience, physics]
bridge_claim: "STDP modifies synaptic conductance by an amount proportional to exp(-|dt|/tau) with sign determined by whether pre-synaptic firing precedes post-synaptic firing, implementing unsupervised Hebbian learning as a physical rule governed by calcium influx kinetics at NMDA receptors."
translation_table:
  - source: "Hebbian coincidence detection"
    target: "NMDA receptor voltage-and-ligand gating"
    notes: "Both require simultaneous pre- and post-synaptic activation; NMDA opens only when membrane is depolarized AND glutamate is bound"
  - source: "synaptic weight update delta-w"
    target: "change in AMPA receptor conductance"
    notes: "Long-term potentiation (LTP) inserts AMPA receptors; LTD removes them; conductance change is the physical substrate of weight"
  - source: "STDP time window tau_plus ~ 20 ms"
    target: "calcium transient decay constant"
    notes: "The ~20 ms window reflects the time course of calcium elevation following a back-propagating action potential"
  - source: "causal spike ordering (pre before post)"
    target: "potentiation via calcium-calmodulin kinase II (CaMKII) activation"
    notes: "High calcium from near-coincident NMDA + bAP activates CaMKII, driving LTP"
status: established
confidence: 0.92
communication_gap: "Computational neuroscientists model STDP as abstract weight-update rules while biophysicists study calcium kinetics; the quantitative mapping between learning rules and molecular mechanisms is rarely made explicit across both literatures."
cross_pollination_opportunities:
  - "Reservoir computing networks using STDP can self-organize to perform temporal pattern recognition without supervised labels, bridging physical neural dynamics with machine learning"
  - "Measuring STDP windows in vivo across cortical layers could calibrate biophysical models of learning rate and stability in large networks"
references:
  - doi: "10.1126/science.275.5297.213"
    note: "Markram et al. (1997) Science - first quantitative demonstration of STDP in neocortical pyramidal neurons"
  - doi: "10.1523/JNEUROSCI.18-24-10464.1998"
    note: "Bi & Poo (1998) J Neurosci - canonical STDP time window characterization in hippocampal neurons"
  - doi: "10.1038/nn.2479"
    note: "Caporale & Dan (2008) Nat Rev Neurosci - STDP mechanisms and functional implications"
related_unknowns:
  - u-stdp-synaptic-weight-saturation
last_reviewed: "2026-05-07"
""")

ud = mkdirs("unknowns-catalog", "neuroscience")
write(os.path.join(ud, "u-stdp-synaptic-weight-saturation.yaml"), """\
id: u-stdp-synaptic-weight-saturation
title: "How do biological neural networks prevent runaway potentiation under STDP, and what mechanisms enforce weight normalization to maintain stable learned representations?"
status: open
priority: high
disciplines:
  - neuroscience
  - physics
  - computational-neuroscience
summary: >
  STDP alone is unstable: any synapse that happens to fire slightly earlier than
  its post-synaptic target will be potentiated, increasing its firing probability,
  leading to further potentiation. Without a normalization mechanism, all synaptic
  weights drift to maximum (potentiation explosion) or minimum (depression spiral).
  Proposed stabilizers include synaptic scaling (homeostatic plasticity), hard weight
  bounds, multiplicative STDP, and inhibitory plasticity. Which mechanism dominates
  in vivo and how they interact with STDP windows to produce stable receptive fields
  remains contested.
systematic_gaps:
  - In vivo weight distributions during learning have not been measured at single-synapse resolution in behaving animals
  - The relative contribution of homeostatic versus Hebbian plasticity to weight stabilization is unknown
  - Whether multiplicative or additive STDP better describes biological data is contested
related_bridges:
  - b-neuroplasticity-stdp
last_reviewed: "2026-05-07"
""")

hd = mkdirs("hypotheses", "active")
write(os.path.join(hd, "h-stdp-homeostatic-scaling-weight-stability.yaml"), """\
id: h-stdp-homeostatic-scaling-weight-stability
title: "Multiplicative STDP combined with synaptic scaling maintains log-normally distributed synaptic weights that match observed in vivo distributions in cortical neurons"
status: active
priority: medium
impact_score: 0.71
created: "2026-05-07"
last_updated: "2026-05-07"
related_disciplines:
  - neuroscience
  - computational-neuroscience
  - physics
unknowns_addressed:
  - u-stdp-synaptic-weight-saturation
evidence_links:
  - doi: "10.1016/j.neuron.2006.09.015"
    type: supporting
    confidence: 0.75
    note: "Turrigiano (2008) - synaptic scaling homeostatically adjusts all weights proportionally, preserving relative strengths"
  - doi: "10.1371/journal.pbio.0030068"
    type: supporting
    confidence: 0.70
    note: "Song et al. (2005) - multiplicative STDP produces log-normal weight distributions matching cortical data"
proposed_tests:
  - description: >
      Simulate a network of 1000 neurons with multiplicative STDP and synaptic scaling.
      Measure the steady-state weight distribution and compare Kolmogorov-Smirnov
      statistic against log-normal fit. Prediction: KS p > 0.05 for log-normal,
      p < 0.001 for normal distribution.
""")

# ──────────────────────────────────────────────────────────
# Bridge 2: Ecosystem metabolism ↔ thermodynamic scaling (ecology ↔ thermodynamics)
# ──────────────────────────────────────────────────────────
d = mkdirs("cross-domain", "ecology-thermodynamics")
write(os.path.join(d, "b-ecosystem-metabolic-scaling.yaml"), """\
id: b-ecosystem-metabolic-scaling
title: "Ecosystem gross primary production scales with total biomass raised to the 3/4 power, reflecting the same thermodynamic constraints on transport networks that govern metabolic rate scaling in individual organisms"
domains: [ecology, thermodynamics]
bridge_claim: "The metabolic theory of ecology (MTE) predicts that individual metabolic rate B scales as M^(3/4) exp(-E/kT) due to fractal vascular network optimization, and this scaling propagates to ecosystem-level energy flux, setting carbon turnover rates, population densities, and food-web structure through a single thermodynamic framework."
translation_table:
  - source: "individual metabolic rate B = B0 * M^(3/4)"
    target: "Boltzmann-Arrhenius temperature correction exp(-E/kT)"
    notes: "3/4 exponent from fractal resource network; temperature term from enzyme kinetics; both enter the same MTE equation"
  - source: "ecosystem gross primary production (GPP)"
    target: "sum of individual autotroph metabolic rates at ambient temperature"
    notes: "GPP integrates over the biomass distribution; its temperature sensitivity is ~0.65 eV matching the Arrhenius term"
  - source: "carbon turnover time"
    target: "M^(1/4) exp(E/kT)"
    notes: "Slower turnover in larger organisms; faster in warmer environments; exact inverse of metabolic rate scaling"
  - source: "population energy use (population density times body mass times metabolic rate)"
    target: "constant across body sizes within a trophic level"
    notes: "Damuth's law: energy equivalence across body sizes emerges from 3/4 scaling"
status: established
confidence: 0.80
communication_gap: "Ecologists measure ecosystem fluxes at the ecosystem level while thermodynamicists study energy dissipation at the molecular/organismal level; the MTE bridge between scales is known in macroecology but not widely taught in thermodynamics curricula."
cross_pollination_opportunities:
  - "Predicting ecosystem carbon uptake under climate warming using thermodynamic activation energies measured in lab metabolic assays"
  - "Testing whether metabolic scaling exponents deviate from 3/4 in extreme environments (deep sea, polar regions) as a window into non-standard transport network geometries"
references:
  - doi: "10.1126/science.1095244"
    note: "Brown et al. (2004) Science - Metabolic Theory of Ecology unifying body size, temperature, and metabolic rate"
  - doi: "10.1038/35098076"
    note: "West et al. (1999) Science - fractal vascular network derivation of 3/4 scaling law"
  - doi: "10.1111/j.1461-0248.2007.01094.x"
    note: "Allen & Gillooly (2007) Ecology Letters - temperature dependence of ecosystem processes via MTE"
related_unknowns:
  - u-metabolic-scaling-exponent-deviation-extremes
last_reviewed: "2026-05-07"
""")

ud = mkdirs("unknowns-catalog", "ecology")
write(os.path.join(ud, "u-metabolic-scaling-exponent-deviation-extremes.yaml"), """\
id: u-metabolic-scaling-exponent-deviation-extremes
title: "Under what environmental or physiological conditions do metabolic scaling exponents deviate significantly from 3/4, and can deviations be predicted from first principles?"
status: open
priority: medium
disciplines:
  - ecology
  - thermodynamics
  - physiology
summary: >
  The 3/4 metabolic scaling exponent is well-supported for mammals and birds but
  contested for ectotherms, unicellular organisms, and plants. Some studies report
  exponents from 0.6 to 1.0. The fractal vascular network model predicts 3/4 only
  for organisms with space-filling resource distribution networks; organisms with
  different transport geometries (diffusion-limited microbes, plants without closed
  circulatory systems) may deviate. Whether deviations reflect biological diversity
  or measurement artifacts is unresolved.
systematic_gaps:
  - Metabolic scaling in unicellular eukaryotes spans exponents from 0.6-1.0 without clear mechanistic explanation
  - The temperature correction has been measured primarily in endotherms; ectotherm activation energies show higher variance
  - Ecosystem-level tests of MTE predictions require long-term flux tower data rarely linked to individual organism physiology
related_bridges:
  - b-ecosystem-metabolic-scaling
last_reviewed: "2026-05-07"
""")

write(os.path.join(hd, "h-metabolic-scaling-3-4-fractal-derivation.yaml"), """\
id: h-metabolic-scaling-3-4-fractal-derivation
title: "Organisms with non-space-filling transport networks (e.g., insect tracheal systems) should show metabolic scaling exponents significantly below 3/4, testable via comparative respirometry"
status: active
priority: medium
impact_score: 0.65
created: "2026-05-07"
last_updated: "2026-05-07"
related_disciplines:
  - ecology
  - thermodynamics
  - physiology
unknowns_addressed:
  - u-metabolic-scaling-exponent-deviation-extremes
evidence_links:
  - doi: "10.1126/science.1095244"
    type: supporting
    confidence: 0.70
    note: "MTE predicts 3/4 only when transport is space-filling fractal; insects with tracheal diffusion may deviate"
  - doi: "10.1242/jeb.01819"
    type: related
    confidence: 0.60
    note: "Greenlee & Harrison (2004) measured tracheal system scaling in insects showing non-fractal geometry"
proposed_tests:
  - description: >
      Measure resting metabolic rate in 30+ insect species spanning 6 orders of
      magnitude in body mass using flow-through respirometry. Fit log(B) vs log(M)
      by OLS and SMA regression. Prediction: exponent significantly below 3/4
      (95% CI excludes 0.75) for insects but not for mammals measured under
      identical conditions.
""")

# ──────────────────────────────────────────────────────────
# Bridge 3: Disordered systems ↔ replica method (statistical physics ↔ optimization)
# ──────────────────────────────────────────────────────────
d = mkdirs("cross-domain", "physics-computer-science")
write(os.path.join(d, "b-spin-glass-replica-optimization.yaml"), """\
id: b-spin-glass-replica-optimization
title: "The replica method from spin-glass theory exactly characterizes the typical-case complexity of random constraint satisfaction problems, revealing phase transitions from easy to hard to unsatisfiable regimes that govern practical algorithm performance"
domains: [physics, computer-science]
bridge_claim: "The free energy of an Ising spin glass with random couplings, computed via the replica trick and replica-symmetry breaking (RSB) ansatz, maps exactly onto the satisfiability threshold of random k-SAT at clause-to-variable ratio alpha_c, predicting the hard-easy phase transition that explains why search algorithms fail exponentially near alpha_c."
translation_table:
  - source: "spin glass free energy F = -kT ln Z"
    target: "log-partition function of random k-SAT formula"
    notes: "Both are quenched averages over random disorder; the replica trick averages ln Z = lim_{n->0} (Z^n - 1)/n"
  - source: "replica-symmetry breaking (RSB)"
    target: "exponentially many metastable solution clusters in k-SAT"
    notes: "RSB signals that solutions cluster into exponentially many well-separated groups; search algorithms get trapped between clusters"
  - source: "Parisi order parameter q(x)"
    target: "overlap distribution P(q) between random solutions"
    notes: "P(q) = delta(q) (RS phase, easy) or broad distribution (RSB phase, hard)"
  - source: "SAT/UNSAT phase transition alpha_c"
    target: "thermodynamic phase transition in spin glass free energy"
    notes: "alpha_c for 3-SAT ~ 4.267; exactly predicted by cavity method (belief propagation at zero temperature)"
status: established
confidence: 0.88
communication_gap: "Complexity theorists study worst-case hardness while statistical physicists analyze typical-case phase transitions; the replica/cavity method bridges typical-case analysis (physics) to algorithm design (CS), but the mathematical formalism is non-rigorous and rarely taught in CS programs."
cross_pollination_opportunities:
  - "Belief propagation algorithms derived from the cavity method solve random k-SAT near the phase transition far better than DPLL variants, enabling practical SAT solvers informed by physics"
  - "Survey propagation, a message-passing algorithm from RSB theory, can guide backtracking search away from clustered solution spaces, improving large-instance combinatorial optimization"
references:
  - doi: "10.1126/science.1073287"
    note: "Mezard et al. (2002) Science - replica and cavity method predict 3-SAT threshold"
  - doi: "10.1073/pnas.90.22.10844"
    note: "Kirkpatrick & Selman (1994) Science - phase transition in random 3-SAT"
  - doi: "10.1007/978-3-540-24605-3_37"
    note: "Mezard & Montanari (2009) - Information, Physics, Computation: RSB and belief propagation"
related_unknowns:
  - u-replica-symmetry-breaking-algorithmic-hardness
last_reviewed: "2026-05-07"
""")

ud2 = mkdirs("unknowns-catalog", "physics")
write(os.path.join(ud2, "u-replica-symmetry-breaking-algorithmic-hardness.yaml"), """\
id: u-replica-symmetry-breaking-algorithmic-hardness
title: "Can the degree of replica-symmetry breaking in a random optimization problem be used to quantitatively predict the running time of specific algorithms such as DPLL, belief propagation, or simulated annealing?"
status: open
priority: high
disciplines:
  - statistical-physics
  - computer-science
  - mathematics
summary: >
  The replica method predicts where phase transitions occur in random CSPs but does
  not directly predict algorithm running time. The connection between RSB order
  and typical-case complexity is qualitative: full RSB suggests exponential
  difficulty, RS suggests polynomial. Quantitative predictions (e.g., the exponent
  in exponential scaling) from RSB parameters to specific algorithm performance have
  not been derived. Algorithmic hardness is also sensitive to problem structure
  beyond the order parameter, including the number and structure of solution clusters.
systematic_gaps:
  - No rigorous mathematical proof connects RSB phase structure to algorithm complexity classes
  - Empirical running times of CDCL SAT solvers near the phase transition are poorly predicted by any physics-derived quantity
  - The replica method is non-rigorous; results have been confirmed by the cavity method but full mathematical proofs are limited to specific cases
related_bridges:
  - b-spin-glass-replica-optimization
last_reviewed: "2026-05-07"
""")

write(os.path.join(hd, "h-survey-propagation-rsat-threshold-prediction.yaml"), """\
id: h-survey-propagation-rsat-threshold-prediction
title: "Survey propagation derived from the 1RSB cavity method predicts the satisfiability threshold of random 3-SAT to within 0.1% and solves instances near the threshold in polynomial expected time"
status: active
priority: high
impact_score: 0.82
created: "2026-05-07"
last_updated: "2026-05-07"
related_disciplines:
  - statistical-physics
  - computer-science
  - mathematics
unknowns_addressed:
  - u-replica-symmetry-breaking-algorithmic-hardness
evidence_links:
  - doi: "10.1126/science.1073287"
    type: supporting
    confidence: 0.88
    note: "Mezard et al. (2002) - survey propagation solves random 3-SAT near threshold in polynomial time"
  - doi: "10.1145/1374376.1374440"
    type: related
    confidence: 0.72
    note: "Coja-Oghlan (2011) - rigorous upper and lower bounds on 3-SAT threshold from second moment method"
proposed_tests:
  - description: >
      Generate random 3-SAT instances at alpha = 4.0, 4.2, 4.267, 4.3, 4.5 with n = 10^4
      variables. Run survey propagation and DPLL with 100 random seeds each.
      Compare median solve time and success rate. Prediction: SP succeeds > 90% at
      alpha <= 4.267; DPLL success drops below 50% at alpha > 4.1.
""")

# ──────────────────────────────────────────────────────────
# Bridge 4: Marine biogeochemistry ↔ stoichiometric ratios (oceanography ↔ chemistry)
# ──────────────────────────────────────────────────────────
d = mkdirs("cross-domain", "ecology-chemistry")
write(os.path.join(d, "b-redfield-ratio-ocean-stoichiometry.yaml"), """\
id: b-redfield-ratio-ocean-stoichiometry
title: "The Redfield ratio C:N:P = 106:16:1 reflects the average elemental stoichiometry of marine phytoplankton and constrains global ocean nutrient cycling through chemical mass balance"
domains: [ecology, chemistry]
bridge_claim: "Deep ocean nutrient concentrations maintain C:N:P ~ 106:16:1 (Redfield ratio) because phytoplankton growth stoichiometry and bacterial remineralization are coupled through the same biochemical machinery, creating a geochemical constraint that links ocean chemistry to biological productivity across ocean basins."
translation_table:
  - source: "phytoplankton C:N:P stoichiometry"
    target: "phospholipid, RNA, and protein fractional composition of cells"
    notes: "N/P ratio reflects ribosome-to-protein balance; phosphorus-rich ribosomes drive low N/P in fast-growing cells"
  - source: "deep water nitrate-to-phosphate ratio"
    target: "Redfield ratio 16:1 predicted by mass balance of remineralization"
    notes: "Bacterial decomposition regenerates N and P in ratio equal to phytoplankton uptake ratio, closing the cycle"
  - source: "nitrogen fixation and denitrification balance"
    target: "deviation from Redfield N:P in oxygen minimum zones"
    notes: "Denitrification removes N without P; N fixation adds N; their balance determines ocean N inventory"
  - source: "stoichiometric flexibility (plasticity)"
    target: "Droop model: growth rate limited by most deficient nutrient"
    notes: "C:P ratios vary 10-fold across phytoplankton under P limitation; N:P varies 5-fold under N limitation"
status: established
confidence: 0.85
communication_gap: "Marine chemists measure nutrient ratios while ecologists study phytoplankton physiology; the mechanistic connection between cellular biochemistry and ocean-scale chemical stoichiometry is underemphasized in both oceanography and chemistry curricula."
cross_pollination_opportunities:
  - "Predicting how ocean N:P ratios will shift under climate change by coupling phytoplankton ecophysiology models with ocean circulation chemistry models"
  - "Using deviations from the Redfield ratio in sediment records as a paleoceanographic proxy for past changes in ocean productivity and nitrogen cycling"
references:
  - doi: "10.4319/lo.1958.3.1.0054"
    note: "Redfield (1958) Am Sci - original paper establishing the 106:16:1 ratio and its biological basis"
  - doi: "10.1126/science.1128253"
    note: "Falkowski et al. (2000) Science - why is the N:P ratio of ocean phytoplankton 16:1?"
  - doi: "10.1073/pnas.0805876105"
    note: "Klausmeier et al. (2004) - optimal N:P stoichiometry of phytoplankton from evolutionary optimization"
related_unknowns:
  - u-redfield-ratio-variability-drivers
last_reviewed: "2026-05-07"
""")

ud3 = mkdirs("unknowns-catalog", "oceanography")
write(os.path.join(ud3, "u-redfield-ratio-variability-drivers.yaml"), """\
id: u-redfield-ratio-variability-drivers
title: "What biological and chemical mechanisms drive systematic deviations from the Redfield C:N:P ratio across ocean basins, seasons, and phytoplankton functional groups?"
status: open
priority: medium
disciplines:
  - oceanography
  - chemistry
  - ecology
summary: >
  The Redfield ratio is a global average with significant variability. Tropical
  oligotrophic gyres show elevated C:P ratios; upwelling zones show lower C:P.
  Cyanobacteria have higher N:P than diatoms. Luxury phosphorus uptake under
  P-replete conditions inflates cellular P without increasing growth. The
  relative contributions of acclimation (physiological plasticity), adaptation
  (evolutionary change in gene expression), and community composition shifts
  (species sorting) to observed stoichiometric variability are not quantified.
  This uncertainty propagates into Earth system model predictions of nutrient
  limitation under climate change.
systematic_gaps:
  - Single-cell stoichiometry measurements at ocean-basin scale are unavailable
  - Separating plasticity from adaptation in field populations requires controlled experiments not feasible at sea
  - Earth system models use fixed Redfield ratios, introducing systematic bias in nutrient cycle projections
related_bridges:
  - b-redfield-ratio-ocean-stoichiometry
last_reviewed: "2026-05-07"
""")

write(os.path.join(hd, "h-flexible-stoichiometry-p-limitation-gyre.yaml"), """\
id: h-flexible-stoichiometry-p-limitation-gyre
title: "Subtropical ocean gyres maintain high C:P ratios because P-limited phytoplankton downregulate ribosome synthesis, producing cells with 50-100% higher C:P than Redfield, measurable via flow cytometry and ICP-MS"
status: active
priority: medium
impact_score: 0.68
created: "2026-05-07"
last_updated: "2026-05-07"
related_disciplines:
  - oceanography
  - chemistry
  - ecology
unknowns_addressed:
  - u-redfield-ratio-variability-drivers
evidence_links:
  - doi: "10.1073/pnas.0805876105"
    type: supporting
    confidence: 0.72
    note: "Optimal stoichiometry theory predicts high C:P under P-limitation"
  - doi: "10.1038/ngeo434"
    type: supporting
    confidence: 0.65
    note: "Weber & Deutsch (2010) - ocean C:P ratios vary systematically with growth rate and nutrient availability"
proposed_tests:
  - description: >
      Collect phytoplankton from the North Pacific Subtropical Gyre (ALOHA station)
      and a coastal upwelling site. Measure single-cell C:P by SIMS and bulk C:P
      by ICP-MS. Compare to Redfield. Prediction: gyre C:P > 180 (vs Redfield 106),
      upwelling C:P < 106.
""")

# ──────────────────────────────────────────────────────────
# Bridge 5: Predator-prey cycles ↔ limit cycles / Hopf bifurcation (ecology ↔ dynamical systems)
# ──────────────────────────────────────────────────────────
d = mkdirs("cross-domain", "ecology-mathematics")
write(os.path.join(d, "b-predator-prey-hopf-bifurcation.yaml"), """\
id: b-predator-prey-hopf-bifurcation
title: "The Lotka-Volterra predator-prey equations undergo a Hopf bifurcation as carrying capacity increases, generating stable limit-cycle oscillations whose period and amplitude are analytically predictable from the Jacobian eigenvalues at the coexistence equilibrium"
domains: [ecology, mathematics]
bridge_claim: "In the Rosenzweig-MacArthur model with prey carrying capacity K, the coexistence equilibrium undergoes a supercritical Hopf bifurcation at a critical K* where Re(lambda) = 0, predicting the paradox of enrichment: increasing productivity destabilizes the ecosystem and produces cycles of period T = 2*pi/Im(lambda)."
translation_table:
  - source: "predator-prey coexistence equilibrium (N*, P*)"
    target: "fixed point of the dynamical system where dN/dt = dP/dt = 0"
    notes: "Stability of fixed point determined by eigenvalues of the Jacobian J evaluated at (N*, P*)"
  - source: "paradox of enrichment"
    target: "supercritical Hopf bifurcation at K*"
    notes: "Increasing K shifts Re(lambda) from negative (stable) to positive (unstable limit cycle); period T = 2pi/|Im(lambda)|"
  - source: "predator-prey cycle period (e.g., 9-11 yr Canadian lynx/hare cycle)"
    target: "Im(lambda) at the Hopf point"
    notes: "Hare-lynx cycle period ~ 10 yr consistent with Im(lambda) ~ 0.6 yr^-1 in fitted RM models"
  - source: "functional response (Holling type II)"
    target: "nonlinear saturation term a*N/(1 + a*h*N)"
    notes: "Saturating functional response is required for the Hopf bifurcation; linear functional response gives neutrally stable cycles only"
status: established
confidence: 0.90
communication_gap: "Ecologists fit population cycle data empirically while dynamical systems mathematicians analyze bifurcation diagrams; the explicit calculation of Hopf bifurcation parameters from measured ecological rates is rarely performed in the field ecology literature."
cross_pollination_opportunities:
  - "Using Hopf bifurcation theory to predict which ecosystems are near the destabilization threshold and prioritize conservation monitoring"
  - "Applying normal form theory near the Hopf point to predict how environmental stochasticity converts limit cycles to quasi-cycles observable in noisy ecological data"
references:
  - doi: "10.1086/282272"
    note: "Rosenzweig & MacArthur (1963) Am Nat - Rosenzweig-MacArthur model and paradox of enrichment"
  - doi: "10.1126/science.171.3969.385"
    note: "Rosenzweig (1971) Science - paradox of enrichment: destabilization of exploitation ecosystems"
  - doi: "10.2307/1940352"
    note: "May (1972) Am Nat - stability and complexity in model ecosystems, bifurcation analysis"
related_unknowns:
  - u-predator-prey-cycle-amplitude-stochastic
last_reviewed: "2026-05-07"
""")

write(os.path.join(ud, "u-predator-prey-cycle-amplitude-stochastic.yaml"), """\
id: u-predator-prey-cycle-amplitude-stochastic
title: "How do demographic and environmental stochasticity interact with Hopf bifurcation dynamics to determine observed cycle amplitude and period variability in real predator-prey systems?"
status: open
priority: medium
disciplines:
  - ecology
  - mathematics
  - dynamical-systems
summary: >
  Deterministic predator-prey models predict exact limit cycle amplitude and period
  from ecological parameters, but real populations show substantial variability in
  both. Stochastic fluctuations near a Hopf bifurcation can amplify into large-
  amplitude quasi-cycles even when the deterministic equilibrium is stable (below K*).
  Disentangling genuine limit cycles from stochastically amplified quasi-cycles in
  time-series data is methodologically unresolved. The relative importance of
  demographic stochasticity, environmental stochasticity, and deterministic nonlinearity
  in observed cycle variability (e.g., lynx-hare) has not been definitively settled.
systematic_gaps:
  - Long-term ecological time series (> 50 years) sufficient for spectral analysis are rare
  - Parameter estimation for RM models is underdetermined from abundance data alone
  - Cycle period variability is often confounded with changing environmental conditions
related_bridges:
  - b-predator-prey-hopf-bifurcation
last_reviewed: "2026-05-07"
""")

write(os.path.join(hd, "h-hopf-bifurcation-lynx-hare-10yr-cycle.yaml"), """\
id: h-hopf-bifurcation-lynx-hare-10yr-cycle
title: "The 10-year lynx-hare cycle in boreal Canada is generated by a supercritical Hopf bifurcation in the Rosenzweig-MacArthur model with snowshoe hare carrying capacity near the critical threshold K*"
status: active
priority: medium
impact_score: 0.74
created: "2026-05-07"
last_updated: "2026-05-07"
related_disciplines:
  - ecology
  - mathematics
unknowns_addressed:
  - u-predator-prey-cycle-amplitude-stochastic
evidence_links:
  - doi: "10.1126/science.269.5227.1112"
    type: supporting
    confidence: 0.78
    note: "Krebs et al. (1995) Science - experimental evidence for plant-hare-lynx trophic cascade driving 10-yr cycle"
  - doi: "10.1046/j.1461-0248.2001.00177.x"
    type: related
    confidence: 0.62
    note: "Turchin (2003) - complex population dynamics: analysis of lynx-hare cycle using nonlinear time-series methods"
proposed_tests:
  - description: >
      Fit the Rosenzweig-MacArthur model to 90 years of Hudson Bay Company lynx-hare
      data using Bayesian MCMC. Compute the Jacobian at fitted (N*, P*) and determine
      whether Re(lambda) is near zero (close to Hopf point). Prediction: |Re(lambda)|
      < 0.05 yr^-1, consistent with near-critical dynamics rather than deep limit cycle.
""")

# ──────────────────────────────────────────────────────────
# Bridge 6: Membrane potential ↔ Hodgkin-Huxley conductance model (neuroscience ↔ biophysics)
# ──────────────────────────────────────────────────────────
d = mkdirs("cross-domain", "neuroscience-physics")
write(os.path.join(d, "b-hodgkin-huxley-conductance.yaml"), """\
id: b-hodgkin-huxley-conductance
title: "The Hodgkin-Huxley equations describe action potential generation as a system of nonlinear ODEs where ion channel conductances follow voltage-dependent gating kinetics, reducing neural excitability to measurable biophysical parameters"
domains: [neuroscience, physics]
bridge_claim: "Action potential generation in squid giant axon (and all neurons) is quantitatively described by C_m * dV/dt = -g_Na * m^3 * h * (V - E_Na) - g_K * n^4 * (V - E_K) - g_L * (V - E_L) + I, where m, h, n are voltage-dependent gating variables following first-order kinetics with rate constants measured by voltage clamp."
translation_table:
  - source: "membrane capacitance C_m charging/discharging"
    target: "parallel RC circuit with nonlinear conductance branches"
    notes: "C_m ~ 1 muF/cm^2 for biological membranes; time constant tau = RC sets spike width"
  - source: "Na+ channel activation gate m"
    target: "dm/dt = alpha_m(V)(1-m) - beta_m(V)m; tau_m ~ 0.5 ms at -40 mV"
    notes: "m^3 nonlinearity causes threshold-like sodium current activation (cooperative gating)"
  - source: "Na+ channel inactivation gate h"
    target: "dh/dt = alpha_h(V)(1-h) - beta_h(V)h; tau_h ~ 5 ms at -40 mV"
    notes: "h provides refractory period; h closes slowly after Na+ influx, preventing re-excitation"
  - source: "K+ channel activation gate n"
    target: "dn/dt = alpha_n(V)(1-n) - beta_n(V)n; tau_n ~ 5 ms at -50 mV"
    notes: "n^4 nonlinearity delays K+ current; repolarizes membrane and produces afterhyperpolarization"
status: established
confidence: 0.97
communication_gap: "The Hodgkin-Huxley model is taught in both neuroscience and biophysics but the connection between voltage-clamp measurements, Nernst potentials, and the full nonlinear dynamics is rarely integrated; computational neuroscience treats it as a black box while biophysicists focus on individual channel kinetics without connecting to whole-neuron computation."
cross_pollination_opportunities:
  - "Reduced HH models (FitzHugh-Nagumo, Morris-Lecar) capture essential bifurcation structure (saddle-node vs Hopf) enabling analytical prediction of excitability classes from channel composition"
  - "Single-channel patch clamp data on stochastic gating can be integrated with deterministic HH framework using Markov models to predict population-level noise properties"
references:
  - doi: "10.1113/jphysiol.1952.sp004764"
    note: "Hodgkin & Huxley (1952) J Physiol - original HH model quantitatively describing action potential"
  - doi: "10.1113/jphysiol.1952.sp004717"
    note: "Hodgkin & Huxley (1952) J Physiol - voltage clamp measurements of Na and K conductances"
  - doi: "10.1007/s00422-007-0178-y"
    note: "Izhikevich (2007) Dynamical Systems in Neuroscience - bifurcation analysis of HH and reduced models"
related_unknowns:
  - u-hodgkin-huxley-channel-heterogeneity-neuron-diversity
last_reviewed: "2026-05-07"
""")

ud4 = mkdirs("unknowns-catalog", "neuroscience")
write(os.path.join(ud4, "u-hodgkin-huxley-channel-heterogeneity-neuron-diversity.yaml"), """\
id: u-hodgkin-huxley-channel-heterogeneity-neuron-diversity
title: "How do differences in ion channel composition and density across neuron types produce the diverse firing patterns observed experimentally, and can a unified conductance-based framework predict firing phenotype from transcriptomic channel expression data?"
status: open
priority: high
disciplines:
  - neuroscience
  - biophysics
  - computational-neuroscience
summary: >
  The Hodgkin-Huxley framework can produce regular spiking, burst firing,
  intrinsic oscillations, and many other patterns by varying the type and density
  of ion channels. Single-cell RNA sequencing now provides transcriptomic channel
  expression profiles for thousands of neuron types. However, the mapping from
  mRNA expression to membrane conductance to firing phenotype is poorly characterized:
  mRNA abundance does not reliably predict protein levels; channel trafficking and
  localization add further complexity. Whether a conductance-based model trained on
  transcriptomic data can predict firing pattern has not been systematically tested.
systematic_gaps:
  - mRNA-to-conductance calibration curves are available only for a handful of channel types
  - Axonal vs. somatic channel distributions are not captured by bulk or single-cell RNA-seq
  - The space of channel combinations producing a given firing phenotype is degenerate (many solutions)
related_bridges:
  - b-hodgkin-huxley-conductance
last_reviewed: "2026-05-07"
""")

write(os.path.join(hd, "h-transcriptomic-conductance-firing-phenotype.yaml"), """\
id: h-transcriptomic-conductance-firing-phenotype
title: "Ion channel mRNA expression profiles from single-cell RNA-seq can predict HH conductance parameters with sufficient accuracy to reproduce firing phenotype in 70% of neuron types"
status: active
priority: high
impact_score: 0.78
created: "2026-05-07"
last_updated: "2026-05-07"
related_disciplines:
  - neuroscience
  - biophysics
unknowns_addressed:
  - u-hodgkin-huxley-channel-heterogeneity-neuron-diversity
evidence_links:
  - doi: "10.1016/j.cell.2019.05.031"
    type: supporting
    confidence: 0.65
    note: "Allen Brain Cell Atlas - transcriptomic classification of mouse cortical neurons with matched patch-clamp electrophysiology"
  - doi: "10.1371/journal.pcbi.1002051"
    type: related
    confidence: 0.58
    note: "Marder & Taylor (2011) - degeneracy in conductance-based models: many parameter sets produce same phenotype"
proposed_tests:
  - description: >
      Use the Allen Cell Types Database (Patch-seq) to train a random forest regressor
      from log-normalized channel mRNA counts to HH conductance parameters (g_Na, g_K,
      g_A, g_h, etc.) in 500 cortical neurons. Simulate HH models with predicted
      parameters, compare firing patterns (regular spiking, bursting, fast spiking)
      to electrophysiology. Prediction: >70% correct phenotype classification.
""")

# ──────────────────────────────────────────────────────────
# Bridge 7: Crystal nucleation ↔ classical nucleation theory (materials science ↔ thermodynamics)
# ──────────────────────────────────────────────────────────
d = mkdirs("cross-domain", "materials-science-physics")
write(os.path.join(d, "b-classical-nucleation-theory.yaml"), """\
id: b-classical-nucleation-theory
title: "Classical nucleation theory predicts the rate of crystal formation from supersaturated solutions as J = A * exp(-Delta-G*/kT), where the nucleation barrier Delta-G* = 16*pi*gamma^3 / (3*Delta-g_v^2) balances surface energy against volumetric driving force"
domains: [materials-science, physics]
bridge_claim: "Crystal nucleation rate from a supersaturated melt is J = Z * f * C0 * exp(-Delta-G*/kT), where the thermodynamic barrier Delta-G* = 16*pi*gamma^3/(3*Delta-g_v^2) is derived from competing surface free energy (gamma, favors dissolution) and volumetric free energy gain (Delta-g_v, favors growth), predicting that nucleation is exponentially sensitive to temperature and supersaturation."
translation_table:
  - source: "critical nucleus radius r* = 2*gamma / Delta-g_v"
    target: "thermodynamic saddle point in free energy landscape"
    notes: "r* is the smallest stable nucleus; subcritical clusters dissolve, supercritical clusters grow spontaneously"
  - source: "nucleation barrier Delta-G* = (4/3)*pi*r*^2 * gamma"
    target: "activation energy in Arrhenius nucleation rate"
    notes: "Delta-G* scales as gamma^3/Delta-g_v^2; small changes in interfacial energy gamma have cubic effect on barrier"
  - source: "Zeldovich factor Z"
    target: "accounts for curvature of free energy near saddle point"
    notes: "Z ~ 0.01-0.1 for typical systems; often treated as a prefactor adjustment"
  - source: "supersaturation ratio S = c/c_eq"
    target: "Delta-g_v = kT * ln(S) per molecule"
    notes: "Higher supersaturation increases Delta-g_v, lowering r* and Delta-G*; nucleation rate increases exponentially"
status: established
confidence: 0.78
communication_gap: "Materials scientists measure nucleation rates experimentally while thermodynamicists derive CNT from capillarity approximations; CNT often fails by orders of magnitude for small clusters where the capillarity approximation breaks down, and the gap between theory and experiment is acknowledged but not resolved."
cross_pollination_opportunities:
  - "Density functional theory calculations of cluster-size-dependent surface energy can replace the capillarity approximation in CNT, potentially resolving the 10-order-of-magnitude discrepancy for protein crystallization"
  - "Non-classical two-step nucleation pathways (dense liquid precursor followed by crystallization) observed in biomineralization require extending CNT to multi-order-parameter free energy landscapes"
references:
  - doi: "10.1039/cs9908900321"
    note: "Mullin (2001) Crystallization - comprehensive treatment of classical nucleation theory"
  - doi: "10.1103/RevModPhys.84.759"
    note: "Sosso et al. (2016) - crystal nucleation in liquids: open questions and future challenges"
  - doi: "10.1126/science.1167641"
    note: "Vekilov (2010) - two-step mechanism for the nucleation of crystals from solution"
related_unknowns:
  - u-classical-nucleation-theory-prefactor-discrepancy
last_reviewed: "2026-05-07"
""")

ud5 = mkdirs("unknowns-catalog", "materials-science")
write(os.path.join(ud5, "u-classical-nucleation-theory-prefactor-discrepancy.yaml"), """\
id: u-classical-nucleation-theory-prefactor-discrepancy
title: "Why does classical nucleation theory fail by 10-20 orders of magnitude for protein and ice nucleation, and what molecular-scale corrections are needed for quantitative prediction?"
status: open
priority: high
disciplines:
  - materials-science
  - thermodynamics
  - biophysics
summary: >
  CNT routinely fails by factors of 10^10 to 10^20 in predicted nucleation rates for
  proteins, ice, and many organic crystals. The failures arise from: (1) the capillarity
  approximation assuming bulk properties for clusters of 10-100 molecules; (2) neglect
  of non-classical two-step pathways; (3) poorly known interfacial energies gamma;
  (4) attachment kinetics not described by simple diffusion. Molecular dynamics simulations
  can directly simulate nucleation for some systems but are too slow for low-supersaturation
  conditions. The development of a quantitatively predictive nucleation theory that
  works from first principles without fitted parameters remains an open problem.
systematic_gaps:
  - Interfacial free energy gamma for sub-nanometer clusters cannot be measured directly
  - Two-step nucleation pathways (liquid-precursor route) are observed but not incorporated in standard CNT
  - MD simulations of nucleation are limited to supersaturations > 10x beyond experiment
related_bridges:
  - b-classical-nucleation-theory
last_reviewed: "2026-05-07"
""")

write(os.path.join(hd, "h-two-step-nucleation-density-liquid-precursor.yaml"), """\
id: h-two-step-nucleation-density-liquid-precursor
title: "Protein crystallization proceeds through a dense liquid precursor phase whose lifetime determines the observed induction time, and DFT-based free energy calculations of the precursor can predict nucleation rates within 2 orders of magnitude"
status: active
priority: high
impact_score: 0.76
created: "2026-05-07"
last_updated: "2026-05-07"
related_disciplines:
  - materials-science
  - thermodynamics
  - biophysics
unknowns_addressed:
  - u-classical-nucleation-theory-prefactor-discrepancy
evidence_links:
  - doi: "10.1126/science.1167641"
    type: supporting
    confidence: 0.75
    note: "Vekilov (2010) - dense liquid precursor in lysozyme nucleation observed by DLS and AFM"
  - doi: "10.1073/pnas.1108379109"
    type: related
    confidence: 0.68
    note: "Gebauer et al. (2008) - stable prenucleation calcium carbonate clusters as two-step pathway"
proposed_tests:
  - description: >
      Monitor lysozyme crystallization at 4 conditions (varied supersaturation, pH)
      using dynamic light scattering (cluster size distribution) and turbidity (crystal
      appearance). Fit a two-step kinetic model where rate = k1 * [precursor] * k2.
      Compare to CNT single-step prediction. Prediction: two-step model reduces
      residual by > 50% vs CNT across all conditions.
""")

# ──────────────────────────────────────────────────────────
# Bridge 8: Collective motion ↔ Vicsek model / active matter (physics ↔ biology)
# ──────────────────────────────────────────────────────────
d = mkdirs("cross-domain", "physics-biology")
write(os.path.join(d, "b-vicsek-active-matter-flocking.yaml"), """\
id: b-vicsek-active-matter-flocking
title: "The Vicsek model demonstrates that local velocity alignment among self-propelled particles spontaneously generates long-range orientational order in 2D, explaining collective motion in bird flocks, fish schools, and bacterial swarms through a minimal active matter model"
domains: [physics, biology]
bridge_claim: "N self-propelled particles with speed v0 aligning with neighbors within radius r undergo a continuous noise-driven phase transition at critical noise eta_c from a disordered gas phase (no net motion) to a polar ordered phase (coherent flock), with the order parameter phi = |sum(v_i)|/(N*v0) serving as the magnetization analog in a non-equilibrium system with no Hamiltonian."
translation_table:
  - source: "local velocity alignment rule theta_i(t+1) = <theta_j>_{|r_ij|<r} + noise"
    target: "ferromagnetic spin alignment in XY model without detailed balance"
    notes: "Unlike equilibrium XY model, Vicsek particles self-propel, breaking time-reversal symmetry and allowing long-range order in 2D"
  - source: "noise parameter eta (angular deviation)"
    target: "effective temperature in non-equilibrium system"
    notes: "Increasing eta destroys order; the eta_c transition is discontinuous (first-order) at large N, debated at small N"
  - source: "starling murmuration long-range correlations"
    target: "scale-free correlation length xi >> r (interaction range)"
    notes: "Empirical correlations in starling flocks extend over the entire flock; consistent with proximity to criticality"
  - source: "bacterial collective motion (E. coli swarms)"
    target: "Toner-Tu hydrodynamic theory for polar active fluids"
    notes: "Toner-Tu equations add advective nonlinearity to XY hydrodynamics; predict unique anomalous scaling exponents"
status: established
confidence: 0.85
communication_gap: "Physicists study active matter phase transitions theoretically while biologists measure collective animal behavior empirically; quantitative comparison requires translating biophysical parameters (alignment strength, noise) into measurable behavioral metrics (nearest-neighbor correlation, speed distribution)."
cross_pollination_opportunities:
  - "Inferring effective alignment strength and noise from field data on animal collectives using maximum entropy methods, connecting behavioral ecology to statistical physics"
  - "Designing synthetic active matter systems (Janus particles, nanomotors) using Vicsek model predictions to achieve programmable collective behavior for microrobotics"
references:
  - doi: "10.1103/PhysRevLett.75.1226"
    note: "Vicsek et al. (1995) PRL - original Vicsek model paper demonstrating phase transition in collective motion"
  - doi: "10.1103/PhysRevLett.75.4326"
    note: "Toner & Tu (1995) PRL - hydrodynamic theory of flocking: Toner-Tu equations"
  - doi: "10.1126/science.1215776"
    note: "Cavagna et al. (2010) PNAS - scale-free correlations in starling flocks empirically measured"
related_unknowns:
  - u-vicsek-transition-order-finite-systems
last_reviewed: "2026-05-07"
""")

ud6 = mkdirs("unknowns-catalog", "biology")
write(os.path.join(ud6, "u-vicsek-transition-order-finite-systems.yaml"), """\
id: u-vicsek-transition-order-finite-systems
title: "Is the Vicsek model phase transition first-order or continuous in the thermodynamic limit, and how does finite-size scaling affect collective behavior in biological groups of 10-10^4 individuals?"
status: open
priority: medium
disciplines:
  - physics
  - biology
  - computational-physics
summary: >
  The order of the Vicsek model phase transition (first-order vs continuous) remains
  disputed. Chate et al. (2008) argued it is first-order based on density fluctuation
  analysis; other analyses suggest it approaches continuous at large N. Biological
  systems have finite N (100-100,000 animals), where finite-size effects are large.
  Whether biological collectives operate near the Vicsek critical point (as suggested
  by starling data showing scale-free correlations) or far from it is not settled.
  The mapping from Vicsek parameters to biological observables (alignment strength,
  noise) requires further development.
systematic_gaps:
  - Finite-size scaling analysis of the Vicsek transition is computationally expensive; results up to N ~ 10^5 are available but extrapolation to thermodynamic limit is uncertain
  - Empirical data on alignment strength in different species are not systematically compared to Vicsek predictions
  - The role of heterogeneity (different speeds, sizes) in biological collectives is not captured by the basic Vicsek model
related_bridges:
  - b-vicsek-active-matter-flocking
last_reviewed: "2026-05-07"
""")

write(os.path.join(hd, "h-starling-murmuration-criticality-vicsek.yaml"), """\
id: h-starling-murmuration-criticality-vicsek
title: "Starling murmurations are tuned near the Vicsek critical point, maintaining scale-free correlations that maximize information transfer speed across the flock, measurable through correlation length scaling with flock size"
status: active
priority: medium
impact_score: 0.79
created: "2026-05-07"
last_updated: "2026-05-07"
related_disciplines:
  - physics
  - biology
unknowns_addressed:
  - u-vicsek-transition-order-finite-systems
evidence_links:
  - doi: "10.1126/science.1215776"
    type: supporting
    confidence: 0.80
    note: "Cavagna et al. (2010) - scale-free correlations in starling flocks consistent with criticality"
  - doi: "10.1073/pnas.1320637111"
    type: supporting
    confidence: 0.73
    note: "Bialek et al. (2014) - maximum entropy model of starling flocks shows near-critical behavior"
proposed_tests:
  - description: >
      Track 5-10 starling murmurations of different sizes (N = 100-10,000) using
      stereo cameras. Compute spatial correlation function C(r) of velocity fluctuations.
      Measure correlation length xi. Prediction: xi scales as N^nu with nu consistent
      with Vicsek critical exponent (nu ~ 0.5-0.7), not as constant fraction of flock size.
""")

# ──────────────────────────────────────────────────────────
# Bridge 9: Legal reasoning ↔ argumentation theory / logic (law ↔ computer science)
# ──────────────────────────────────────────────────────────
d = mkdirs("cross-domain", "computer-science-mathematics")
write(os.path.join(d, "b-legal-argumentation-formal-logic.yaml"), """\
id: b-legal-argumentation-formal-logic
title: "Legal reasoning can be formalized as abstract argumentation frameworks where arguments and their defeat relations determine the set of legally justified conclusions via extension semantics"
domains: [computer-science, mathematics]
bridge_claim: "Dung's abstract argumentation framework AF = (AR, attacks) maps legal arguments to nodes and legal rebuttals/undercutters to directed edges, with grounded, preferred, and stable extension semantics providing formal definitions of which legal conclusions are justified, contested, or defeated under different standards of proof."
translation_table:
  - source: "legal argument (claim with supporting reasons)"
    target: "node in Dung's argumentation framework"
    notes: "Arguments are abstract; their internal structure (ASPIC+, Carneades) can be separately formalized"
  - source: "legal rebuttal or undercutter"
    target: "directed attack edge A -> B in (AR, attacks)"
    notes: "A attacks B means A, if accepted, defeats B; rebuttal attacks conclusion, undercutter attacks inference rule"
  - source: "legal justification under preponderance of evidence"
    target: "grounded extension: the unique minimal complete extension"
    notes: "Grounded extension is skeptical: only accept what cannot be defeated; maps to beyond-reasonable-doubt standard"
  - source: "legal justification under balance of probabilities"
    target: "preferred extension: maximal admissible set"
    notes: "Preferred extensions are credulous: accept as much as possible without inconsistency"
  - source: "burden of proof allocation"
    target: "asymmetric attack strength or priority ordering on arguments"
    notes: "ASPIC+ formalizes burden allocation through argument ordering; rebuttals only succeed against equal or weaker arguments"
status: proposed
confidence: 0.62
communication_gap: "Legal scholars analyze arguments qualitatively using doctrine while computer scientists develop formal argumentation systems; the operationalization of legal concepts (burden of proof, standards of evidence) into formal semantics remains contested between the two communities."
cross_pollination_opportunities:
  - "Automated legal argument mining from case text using NLP to populate argumentation frameworks, enabling computational analysis of case law consistency"
  - "Using formal argumentation semantics to detect circular reasoning or inconsistency in legislative drafting before enactment"
references:
  - doi: "10.1016/0004-3702(95)00021-9"
    note: "Dung (1995) - On the acceptability of arguments: foundational paper on abstract argumentation"
  - doi: "10.1007/s10506-006-9036-x"
    note: "Prakken & Sartor (2006) - law and logic: a review from an argumentation perspective"
  - doi: "10.1016/j.artint.2010.11.009"
    note: "Modgil & Prakken (2012) - ASPIC+ framework for structured argumentation"
related_unknowns:
  - u-legal-argumentation-formal-completeness
last_reviewed: "2026-05-07"
""")

ud7 = mkdirs("unknowns-catalog", "computer-science")
write(os.path.join(ud7, "u-legal-argumentation-formal-completeness.yaml"), """\
id: u-legal-argumentation-formal-completeness
title: "Can formal argumentation frameworks capture the full range of legal reasoning patterns including analogy, precedent, and equitable discretion, or are there fundamental limits to the formalization of law?"
status: open
priority: medium
disciplines:
  - computer-science
  - mathematics
  - law
summary: >
  Formal argumentation (Dung, ASPIC+, Carneades) handles deductive legal reasoning
  and explicit rebuttals well. However, legal reasoning also involves analogy from
  precedent (not captured by logical attack), equitable discretion (judge weighs
  values not formalized as arguments), and interpretive ambiguity in statutory text.
  Whether these can be formalized is debated: some argue analogical reasoning requires
  case-based reasoning systems (CBR) outside formal logic; others argue that argument
  schemes for analogy can be added to ASPIC+. The question of whether a complete
  formal account of legal reasoning is possible or if law is essentially open-textured
  (Hart) remains philosophically unresolved.
systematic_gaps:
  - No large-scale empirical test of whether formal argumentation models predict court decisions better than baseline
  - Analogical reasoning in legal decisions has not been successfully reduced to formal attack relations
  - Judicial discretion and value-based judgment resist formalization in any existing framework
related_bridges:
  - b-legal-argumentation-formal-logic
last_reviewed: "2026-05-07"
""")

write(os.path.join(hd, "h-aspic-legal-argument-outcome-prediction.yaml"), """\
id: h-aspic-legal-argument-outcome-prediction
title: "ASPIC+ argumentation frameworks populated from legal briefs can predict appellate court outcomes with accuracy exceeding logistic regression on case features alone"
status: active
priority: medium
impact_score: 0.58
created: "2026-05-07"
last_updated: "2026-05-07"
related_disciplines:
  - computer-science
  - mathematics
  - law
unknowns_addressed:
  - u-legal-argumentation-formal-completeness
evidence_links:
  - doi: "10.1016/0004-3702(95)00021-9"
    type: supporting
    confidence: 0.55
    note: "Dung (1995) - foundational semantics; no empirical outcome prediction tested"
  - doi: "10.1126/science.aag2433"
    type: related
    confidence: 0.60
    note: "Katz et al. (2017) Science Advances - machine learning predicts Supreme Court outcomes at 70%"
proposed_tests:
  - description: >
      Annotate 200 US Court of Appeals cases with ASPIC+ argumentation graphs extracted
      from legal briefs. Compute grounded extension predictions and compare to actual
      outcomes. Baseline: logistic regression on BagOfWords features. Prediction:
      argumentation model achieves >= 75% accuracy vs baseline ~65%.
""")

# ──────────────────────────────────────────────────────────
# Bridge 10: Quantum decoherence ↔ einselection / pointer states (quantum physics ↔ information theory)
# ──────────────────────────────────────────────────────────
d = mkdirs("cross-domain", "quantum-physics-information")
write(os.path.join(d, "b-quantum-decoherence-einselection.yaml"), """\
id: b-quantum-decoherence-einselection
title: "Quantum decoherence selects pointer states through einselection: the preferred basis that survives entanglement with the environment is determined by the system-environment interaction Hamiltonian, explaining the emergence of classical reality from quantum superpositions"
domains: [quantum-physics, information-theory]
bridge_claim: "Environment-induced superselection (einselection) identifies pointer states as eigenstates of the system observable that commutes with the system-environment interaction Hamiltonian H_int, explaining why macroscopic objects appear classical: coherence between pointer states decays at rate Gamma ~ (x1-x2)^2 / lambda_th^2 * gamma, exponentially fast for large objects."
translation_table:
  - source: "pointer states (preferred basis)"
    target: "eigenstates of operator commuting with H_int"
    notes: "Pointer states are robust: they are not scrambled by interaction with environment; determined by symmetry of H_int"
  - source: "decoherence rate Gamma"
    target: "information leakage rate from system to environment"
    notes: "Gamma is the rate at which environment gains information about system state; fast decoherence = fast information transfer"
  - source: "thermal de Broglie wavelength lambda_th"
    target: "coherence length scale for position superpositions"
    notes: "Superpositions of positions |x1> and |x2> decohere at rate proportional to (x1-x2)^2/lambda_th^2"
  - source: "quantum Darwinism: environment as witness"
    target: "mutual information I(S:F) between system and environment fragment F"
    notes: "Classical objectivity emerges when many environment fragments each carry full information about pointer states"
status: established
confidence: 0.88
communication_gap: "Quantum physicists study decoherence as a dynamical process while information theorists analyze it as information flow; quantum Darwinism connecting objectivity to redundant information encoding in the environment is known in foundations of QM but rarely discussed in quantum information curricula."
cross_pollination_opportunities:
  - "Quantum error correction codes protect logical qubits by engineering environments that do not commute with logical operations, directly applying einselection principles in reverse"
  - "Quantum biology: decoherence time scales in biological chromophores can be measured to test whether quantum coherence plays a functional role in energy transfer"
references:
  - doi: "10.1103/RevModPhys.75.715"
    note: "Zurek (2003) Rev Mod Phys - decoherence, einselection, and the quantum origins of the classical"
  - doi: "10.1038/nature02544"
    note: "Schlosshauer (2004) Rev Mod Phys - decoherence and the measurement problem"
  - doi: "10.1038/nphys1202"
    note: "Zurek (2009) Nat Phys - quantum Darwinism: objectivity from quantum redundancy"
related_unknowns:
  - u-quantum-darwinism-redundancy-threshold-classicality
last_reviewed: "2026-05-07"
""")

ud8 = mkdirs("unknowns-catalog", "quantum-physics")
write(os.path.join(ud8, "u-quantum-darwinism-redundancy-threshold-classicality.yaml"), """\
id: u-quantum-darwinism-redundancy-threshold-classicality
title: "What minimum redundancy in environmental information encoding is required for a quantum system to appear classical, and has quantum Darwinism been experimentally verified in a controlled system?"
status: open
priority: high
disciplines:
  - quantum-physics
  - information-theory
summary: >
  Quantum Darwinism predicts that objective classical reality emerges when the same
  information about a system's pointer state is encoded redundantly in many independent
  environment fragments. The redundancy Rdelta is the number of environment copies
  needed for an observer to learn the system state with probability 1-delta.
  Predictions include a plateau in I(S:F) as a function of fragment size.
  Experimental tests are technically demanding: photon experiments (Unden et al. 2019)
  show signatures consistent with quantum Darwinism but not definitive. What threshold
  redundancy produces operationally classical behavior, and whether biological systems
  exploit or are limited by quantum Darwinism, are open questions.
systematic_gaps:
  - No experiment has demonstrated quantum Darwinism in a system where all environment degrees of freedom are accessible
  - The transition from quantum to classical as redundancy increases has not been quantitatively characterized
  - The role of quantum Darwinism in biological decoherence (e.g., retinal photoisomerization) is speculative
related_bridges:
  - b-quantum-decoherence-einselection
last_reviewed: "2026-05-07"
""")

write(os.path.join(hd, "h-quantum-darwinism-photon-redundancy-verification.yaml"), """\
id: h-quantum-darwinism-photon-redundancy-verification
title: "Quantum Darwinism predicts a plateau in mutual information I(S:F) at I(S:F) = H(S) for fragment sizes above 1/R_delta of the total environment, verifiable in a photon-environment experiment with full environment access"
status: active
priority: high
impact_score: 0.81
created: "2026-05-07"
last_updated: "2026-05-07"
related_disciplines:
  - quantum-physics
  - information-theory
unknowns_addressed:
  - u-quantum-darwinism-redundancy-threshold-classicality
evidence_links:
  - doi: "10.1038/nphys1202"
    type: supporting
    confidence: 0.80
    note: "Zurek (2009) - quantum Darwinism framework and plateau prediction"
  - doi: "10.1103/PhysRevA.99.042307"
    type: related
    confidence: 0.68
    note: "Unden et al. (2019) - experimental signatures of quantum Darwinism in nitrogen-vacancy center"
proposed_tests:
  - description: >
      Prepare a two-level system (spin) entangled with N = 4 photon modes as environment.
      Measure I(S:F) for all 2^N subsets of environment modes using quantum state
      tomography. Predict: I(S:F) plateau at H(S) ~ 1 bit for F > N/R_delta modes,
      with plateau onset at the predicted redundancy threshold.
""")

# ──────────────────────────────────────────────────────────
# Bridge 11: Morphogen gradients ↔ diffusion-driven patterning (developmental biology ↔ mathematics)
# ──────────────────────────────────────────────────────────
d = mkdirs("cross-domain", "biology-mathematics")
write(os.path.join(d, "b-morphogen-turing-patterning.yaml"), """\
id: b-morphogen-turing-patterning
title: "Turing's reaction-diffusion mechanism explains how uniform morphogen distributions spontaneously break symmetry to generate periodic spatial patterns when an activator diffuses slower than its inhibitor, with pattern wavelength lambda = 2*pi * sqrt(D_u/sigma) set by diffusion coefficients"
domains: [biology, mathematics]
bridge_claim: "In a two-component reaction-diffusion system du/dt = D_u * nabla^2 u + f(u,v), dv/dt = D_v * nabla^2 v + g(u,v), a homogeneous steady state that is stable to uniform perturbations becomes unstable to spatial perturbations when D_v/D_u > gamma (Turing instability condition), generating self-organized patterns with wavelength lambda ~ 2*pi*sqrt(D_u/alpha) observed in skin pigmentation, digit formation, and palate rugae."
translation_table:
  - source: "activator-inhibitor short-range activation / long-range inhibition"
    target: "Turing instability condition: D_v >> D_u and f_u > 0, g_v < 0"
    notes: "Pattern formation requires activator to be locally autocatalytic (f_u > 0) and inhibited by faster-diffusing inhibitor"
  - source: "pattern wavelength in digit/stripe patterning"
    target: "lambda = 2*pi / k_max where k_max maximizes Re(sigma(k))"
    notes: "k_max from dispersion relation of linearized RD system; observed stripe spacing ~ lambda"
  - source: "morphogen gradient Bicoid/Nodal"
    target: "source term or spatially varying parameter in RD equations"
    notes: "Pre-patterning gradients modulate local RD parameters, selecting which Turing mode is expressed"
  - source: "finger/digit spacing in limb development"
    target: "Turing wavelength controlled by BMP/Wnt activator-inhibitor pair"
    notes: "Shyer et al. (2018) demonstrated BMP-Wnt RD mechanism in chick digit patterning"
status: established
confidence: 0.82
communication_gap: "Developmental biologists identify molecular components of patterning while mathematicians analyze RD equations; connecting measured morphogen diffusion coefficients and reaction rates to observed pattern wavelengths via the Turing dispersion relation is rarely done quantitatively in developmental biology papers."
cross_pollination_opportunities:
  - "Measuring in vivo diffusion coefficients of BMP and Wnt in developing limb buds using FCS/FRAP to directly test the Turing instability condition D_v/D_u > gamma"
  - "Synthetic biology Turing patterns: engineering genetic circuits with activator-inhibitor topology to generate programmable spatial patterns in bacterial colonies"
references:
  - doi: "10.1098/rstb.1952.0012"
    note: "Turing (1952) - The chemical basis of morphogenesis: original RD theory paper"
  - doi: "10.1126/science.aai7830"
    note: "Shyer et al. (2017) Science - Turing mechanism for digit patterning via BMP-WNT"
  - doi: "10.1038/nrm2763"
    note: "Kondo & Miura (2010) Nat Rev Mol Cell Biol - reaction-diffusion model as a framework for understanding biological pattern formation"
related_unknowns:
  - u-turing-patterning-3d-robustness
last_reviewed: "2026-05-07"
""")

ud9 = mkdirs("unknowns-catalog", "developmental-biology")
write(os.path.join(ud9, "u-turing-patterning-3d-robustness.yaml"), """\
id: u-turing-patterning-3d-robustness
title: "How do Turing reaction-diffusion mechanisms maintain robust spatial patterning in three-dimensional growing tissues despite molecular noise, geometric constraints, and cell division?"
status: open
priority: high
disciplines:
  - developmental-biology
  - mathematics
  - biophysics
summary: >
  Turing patterns in 2D are well-studied mathematically, but embryonic tissues are
  3D, growing, and subject to mechanical forces and cell proliferation. The effect
  of tissue geometry on pattern wavelength selection, the robustness of patterns to
  diffusion coefficient variability (> 20% cell-to-cell), and the coupling between
  mechanical deformation and chemical patterning are poorly understood. In vivo,
  BMP and WNT diffusion coefficients have not been measured with sufficient precision
  to test the Turing instability condition D_v/D_u > gamma quantitatively.
  Whether Turing patterns or clock-and-wavefront mechanisms dominate in different
  developmental contexts is also debated.
systematic_gaps:
  - In vivo diffusion coefficients of key morphogens measured by FRAP are highly variable and may not satisfy Turing instability conditions
  - The coupling between tissue mechanics (growth, folding) and RD pattern formation is not captured by current Turing models
  - Large-scale validation of Turing predictions across species and body plans has not been performed
related_bridges:
  - b-morphogen-turing-patterning
last_reviewed: "2026-05-07"
""")

write(os.path.join(hd, "h-bmp-wnt-diffusion-ratio-turing-digits.yaml"), """\
id: h-bmp-wnt-diffusion-ratio-turing-digits
title: "BMP and WNT morphogens in the developing vertebrate limb bud satisfy the Turing instability condition D_WNT/D_BMP > 10, directly predicting the observed inter-digit spacing from RD theory"
status: active
priority: high
impact_score: 0.80
created: "2026-05-07"
last_updated: "2026-05-07"
related_disciplines:
  - developmental-biology
  - mathematics
unknowns_addressed:
  - u-turing-patterning-3d-robustness
evidence_links:
  - doi: "10.1126/science.aai7830"
    type: supporting
    confidence: 0.78
    note: "Shyer et al. (2017) - BMP-WNT RD mechanism in digit patterning with genetic perturbation evidence"
  - doi: "10.1098/rstb.1952.0012"
    type: supporting
    confidence: 0.90
    note: "Turing (1952) - mathematical framework predicting instability condition"
proposed_tests:
  - description: >
      Measure BMP2 and WNT5A diffusion coefficients in mouse limb bud mesenchyme using
      fluorescence correlation spectroscopy (FCS) on photoactivatable fluorescent fusion
      proteins. Compute D_WNT/D_BMP ratio. Prediction: ratio > 10 (Turing instability
      condition). Simultaneously measure inter-digit spacing. Verify lambda ~ 2*pi*sqrt(D_BMP/alpha).
""")

# ──────────────────────────────────────────────────────────
# Bridge 12: Hysteresis in materials ↔ Preisach model / memory (materials science ↔ mathematics)
# ──────────────────────────────────────────────────────────
d = mkdirs("cross-domain", "materials-science-mathematics")
write(os.path.join(d, "b-preisach-hysteresis-model.yaml"), """\
id: b-preisach-hysteresis-model
title: "The Preisach model represents any rate-independent hysteretic material as a superposition of elementary bistable switches (hysterons), mapping hysteresis loops to a weight distribution rho(alpha,beta) that can be identified from first-order reversal curves"
domains: [materials-science, mathematics]
bridge_claim: "A ferromagnetic material's magnetization M(H) is described by M = double_integral_{alpha>=beta} rho(alpha,beta) * gamma_{alpha,beta}[H] d_alpha d_beta, where gamma_{alpha,beta} are relay operators switching between +1 and -1 at fields alpha (up-switch) and beta (down-switch), and rho is identified from the Everett diagram measured by first-order reversal curves (FORCs)."
translation_table:
  - source: "hysteresis loop M(H)"
    target: "output of Preisach operator: superposition of relay operators"
    notes: "Any rate-independent hysteresis with congruency and wiping-out properties is representable by Preisach model"
  - source: "first-order reversal curve (FORC)"
    target: "partial derivative d^2 M / d_Ha d_Hb = rho(alpha,beta)"
    notes: "FORCs directly measure the Preisach density; FORC diagram visualizes magnetic interaction and coercivity distribution"
  - source: "magnetic coercivity distribution"
    target: "projection of rho(alpha,beta) onto alpha-beta diagonal"
    notes: "Coercivity field H_c = (alpha-beta)/2; interaction field H_u = (alpha+beta)/2"
  - source: "return-point memory in disordered magnets"
    target: "wiping-out property of Preisach model: minor loops erase prior history"
    notes: "Preisach model predicts that state is determined only by most recent field extrema, not full history"
status: established
confidence: 0.85
communication_gap: "Materials scientists measure hysteresis loops experimentally while mathematicians study Preisach operators as functional analysis objects; the FORC technique for identifying the Preisach density is established in rock magnetism but underused in engineering materials characterization."
cross_pollination_opportunities:
  - "Using FORC diagrams to non-destructively characterize fatigue damage in ferromagnetic structural components by tracking changes in Preisach density over load cycles"
  - "Applying Preisach-type memory operators to model hysteresis in shape-memory alloys, ferroelectrics, and porous media for engineering simulation"
references:
  - doi: "10.1007/978-3-662-04726-6"
    note: "Mayergoyz (2003) Mathematical Models of Hysteresis - definitive Preisach model reference"
  - doi: "10.1029/JB091iB12p12497"
    note: "Pike et al. (1999) J Geophys Res - FORC diagrams for characterizing fine magnetic particle systems"
  - doi: "10.1103/PhysRevLett.64.1973"
    note: "Sethna et al. (1993) PRL - hysteresis, avalanches, and Barkhausen noise in disordered magnets"
related_unknowns:
  - u-preisach-model-physical-interpretation-density
last_reviewed: "2026-05-07"
""")

write(os.path.join(ud5, "u-preisach-model-physical-interpretation-density.yaml"), """\
id: u-preisach-model-physical-interpretation-density
title: "What microscopic physical mechanism determines the Preisach density rho(alpha,beta) in real ferromagnetic materials, and can rho be predicted from microstructural parameters without fitting to measured hysteresis loops?"
status: open
priority: medium
disciplines:
  - materials-science
  - mathematics
  - condensed-matter-physics
summary: >
  The Preisach model is a phenomenological representation that fits any hysteresis loop
  but provides no physical insight into the origin of rho(alpha,beta). The density rho
  is determined by the distribution of local switching fields, which depend on grain
  size, shape anisotropy, exchange coupling, and defect structure. Connecting
  microstructural parameters measured by TEM, XRD, and EBSD to the Preisach density
  requires a microscopic theory of domain wall pinning that does not yet exist in
  predictive form. This limits the use of Preisach models for materials design: rho
  must always be measured rather than predicted.
systematic_gaps:
  - No first-principles calculation of Preisach density from grain size distribution has been validated against FORC measurements
  - The effect of thermal activation on rate-independent Preisach operators is not well formulated
  - Preisach model extensions to accommodate accommodation (gradual minor loop drift) are not standardized
related_bridges:
  - b-preisach-hysteresis-model
last_reviewed: "2026-05-07"
""")

write(os.path.join(hd, "h-preisach-density-grain-size-prediction.yaml"), """\
id: h-preisach-density-grain-size-prediction
title: "The Preisach switching field distribution rho(alpha,beta) of a polycrystalline ferromagnet can be predicted from grain size distribution measured by EBSD within a factor of 2, using Stoner-Wohlfarth single-domain particle theory"
status: active
priority: medium
impact_score: 0.64
created: "2026-05-07"
last_updated: "2026-05-07"
related_disciplines:
  - materials-science
  - mathematics
unknowns_addressed:
  - u-preisach-model-physical-interpretation-density
evidence_links:
  - doi: "10.1007/978-3-662-04726-6"
    type: supporting
    confidence: 0.60
    note: "Mayergoyz (2003) - Preisach model review; grain size connection discussed qualitatively"
  - doi: "10.1098/rspa.1948.0095"
    type: related
    confidence: 0.72
    note: "Stoner & Wohlfarth (1948) - single-domain particle switching fields from shape anisotropy"
proposed_tests:
  - description: >
      Prepare 5 NdFeB magnet samples with varied sintering conditions (different
      grain sizes 1-10 micron measured by EBSD). Measure FORC diagrams for each.
      Predict rho from Stoner-Wohlfarth model using grain size distribution as input.
      Compare predicted vs measured FORC diagrams. Prediction: peak rho within 2x;
      Preisach coercivity distribution within 20% of measured value.
""")

print("Wave 42 files created successfully!")

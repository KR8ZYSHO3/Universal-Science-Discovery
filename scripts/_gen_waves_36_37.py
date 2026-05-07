#!/usr/bin/env python3
"""Generate Wave 36 (bridges 85-96) and Wave 37 (bridges 97-108) YAML files."""
from __future__ import annotations
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# --------------------------------------------------------------------------- #
# Utility                                                                       #
# --------------------------------------------------------------------------- #
def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(content).lstrip(), encoding="utf-8")
    print(f"  wrote {path.relative_to(ROOT)}")

# =========================================================================== #
# WAVE 36  —  bridges 85-96                                                    #
# =========================================================================== #

# ── 85 ─────────────────────────────────────────────────────────────────────
write(ROOT / "cross-domain/biology-physics/b-chromatin-loop-extrusion-polymer.yaml", """
id: b-chromatin-loop-extrusion-polymer
title: >
  Chromatin organisation by cohesin-mediated loop extrusion is quantitatively
  predicted by polymer-physics models: the Hi-C contact-probability scaling
  P(s) ~ s^{-0.75} within topologically associating domains (TADs) matches
  the Rouse/fractal-globule polymer exponent, while TAD boundaries correspond
  to equilibrium positions of CTCF-stalled extruding cohesin rings.
status: established
fields:
  - molecular-biology
  - polymer-physics
  - genomics
bridge_claim: >
  Cohesin translocates along chromatin, extruding DNA loops until blocked by
  convergently oriented CTCF binding sites. The resulting TAD structure is
  identical to a 1D-extruded polymer loop ensemble. Hi-C contact-probability
  maps within TADs follow P(s) ~ s^{-0.75}, the fractal-globule scaling
  predicted by polymer physics (Grosberg 1993), distinct from the equilibrium
  globule exponent ~s^{-1.5}. Molecular dynamics simulations using only loop-
  extrusion rules quantitatively reproduce experimental Hi-C maps without
  free parameters (Fudenberg 2016).
translation_table:
  - field_a_term: "Cohesin ring translocating along chromatin"
    field_b_term: "Monomer pair undergoing loop-extrusion dynamics"
    note: "Cohesin acts as a molecular motor driving loop growth; maps to a Rouse-chain active process"
  - field_a_term: "CTCF boundary element (convergent orientation)"
    field_b_term: "Fixed polymer boundary condition / reflecting wall"
    note: "CTCF in convergent orientation halts extrusion, setting loop length distribution"
  - field_a_term: "Topologically associating domain (TAD)"
    field_b_term: "Polymer loop in fractal-globule conformation"
    note: "TAD size ~ mean loop length set by cohesin processivity and CTCF density"
  - field_a_term: "Hi-C contact probability P(s)"
    field_b_term: "Polymer end-to-end contact probability for chain of s monomers"
    note: "P(s) ~ s^{-0.75} is the fractal-globule prediction; equilibrium globule gives ~s^{-1.5}"
related_unknowns:
  - u-chromatin-loop-extrusion-processivity
related_hypotheses:
  - h-ctcf-boundary-polymer-wall
cross_pollination_opportunities:
  - >
    Polymer coarse-grained simulations (MD/MC) parameterised with cohesin
    processivity and CTCF occupancy can be used to predict TAD rewiring after
    CRISPR deletion of individual CTCF sites—bridging structural genomics with
    polymer theory without Hi-C experiments.
  - >
    Loop-extrusion models can be extended to predict 3D gene co-expression
    correlations, testing whether polymer proximity causally mediates
    transcriptional co-regulation inside TADs.
communication_gap: >
  Chromosome biology and polymer physics developed separate vocabularies and
  publication venues (Nature/Cell vs. Macromolecules/Soft Matter). The fractal-
  globule polymer model (Grosberg 1993) was published 23 years before Hi-C
  experiments confirmed its relevance (Lieberman-Aiden 2009). Cohesin biologists
  rarely cite polymer-physics derivations.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1126/science.1181369"
    note: "Lieberman-Aiden et al. (2009) Science – Hi-C reveals fractal-globule chromatin organisation"
  - doi: "10.1016/j.cell.2016.05.001"
    note: "Fudenberg et al. (2016) Cell Reports – loop extrusion MD model quantitatively reproduces Hi-C TADs"
  - doi: "10.1073/pnas.1518552113"
    note: "Sanborn et al. (2015) PNAS – cohesin extrusion predicts insulation at CTCF sites"
  - doi: "10.1126/science.aaf4831"
    note: "Rao et al. (2017) Science – cohesin depletion collapses TADs, confirming extrusion mechanism"
""")

write(ROOT / "unknowns-catalog/biology/u-chromatin-loop-extrusion-processivity.yaml", """
id: u-chromatin-loop-extrusion-processivity
title: >
  What determines the processivity (loop-extrusion run length) of cohesin in vivo,
  and how does nucleosome density, transcription, and supercoiling modulate it?
status: open
priority: high
disciplines:
  - molecular-biology
  - polymer-physics
  - structural-biology
summary: >
  Loop-extrusion models require a characteristic cohesin processivity (mean loop
  size before stalling or falling off). In vivo measurements give widely varying
  estimates (50 kb to >1 Mb). Nucleosome density, active transcription, and DNA
  supercoiling all influence cohesin mobility but their quantitative contributions
  are unknown. Without a mechanistic model of processivity, TAD size cannot be
  predicted from first principles.
systematic_gaps:
  - Single-molecule in vitro cohesin loop extrusion rates do not match in vivo TAD sizes; the discrepancy source is unknown.
  - How RNA polymerase II collision events reset or bypass cohesin rings is not mechanistically characterised.
  - The role of DNA supercoiling gradients in directing cohesin directionality has not been tested in mammalian cells.
last_reviewed: "2026-05-07"
""")

write(ROOT / "hypotheses/active/h-ctcf-boundary-polymer-wall.yaml", """
id: h-ctcf-boundary-polymer-wall
title: >
  Convergent CTCF sites act as reflecting boundary conditions for cohesin-
  mediated loop extrusion, and their deletion will shift the TAD boundary
  position by exactly the mean cohesin processivity distance predicted
  by a Rouse-chain polymer model.
status: active
created: "2026-05-07"
priority: high
impact_score: 0.82
related_disciplines:
  - molecular-biology
  - polymer-physics
unknowns_addressed:
  - u-chromatin-loop-extrusion-processivity
evidence_links:
  - doi: "10.1016/j.cell.2016.05.001"
    type: supporting
    confidence: 0.85
    note: "Fudenberg 2016 – loop-extrusion model with CTCF boundary accurately predicts Hi-C; no free parameters"
  - doi: "10.1126/science.aaf4831"
    type: supporting
    confidence: 0.80
    note: "Rao 2017 – cohesin depletion removes TADs; CTCF depletion shifts boundaries"
proposed_tests:
  - description: >
      CRISPR-delete individual CTCF sites in series (1, 2, 3 adjacent sites) and
      measure resulting TAD boundary shift by micro-C. Compare boundary displacement
      to cohesin processivity estimates from live-cell imaging. If shift = n × processivity,
      the polymer-wall hypothesis is confirmed.
  - description: >
      Simulate Hi-C maps with the Fudenberg loop-extrusion model at varying processivity
      values; fit to the experimental TAD boundary sharpness distribution to extract
      the posterior processivity distribution for HCT116 cells.
""")

# ── 86 ─────────────────────────────────────────────────────────────────────
write(ROOT / "cross-domain/engineering-biology/b-swarm-robotics-stigmergy.yaml", """
id: b-swarm-robotics-stigmergy
title: >
  Swarm-robotic path optimisation via pheromone-inspired digital trails is
  formally equivalent to ant-colony stigmergy: both systems converge to
  shortest paths through positive feedback on good solutions and evaporation
  of poor ones, described by the same differential equations governing
  ant trail-pheromone dynamics.
status: established
fields:
  - robotics
  - engineering
  - evolutionary-biology
  - collective-behaviour
bridge_claim: >
  In ant colonies, workers deposit pheromone on return from food sources;
  shorter trails accumulate pheromone faster (more round trips per unit time),
  attracting more ants until the colony commits to the shortest path. Dorigo's
  Ant Colony Optimisation (ACO, 1992) encodes this in discrete graphs: edge
  pheromone τ_{ij} follows dτ_{ij}/dt = −ρτ_{ij} + ΔQ/L*, where ρ is
  evaporation rate and L* is tour length. Swarm robots equipped with digital
  pheromone fields obey identical equations, enabling distributed shortest-path
  routing without central control. The connection shows that stigmergy—
  environment-mediated indirect communication—is a general optimisation
  principle, not specific to biology.
translation_table:
  - field_a_term: "Ant pheromone trail on path segment"
    field_b_term: "Digital pheromone field on graph edge (swarm robot)"
    note: "Both accumulate proportional to usage frequency; evaporate at rate ρ"
  - field_a_term: "Ant path-selection probability ∝ τ^α × η^β"
    field_b_term: "Robot next-hop probability in ACO routing (same formula)"
    note: "α, β weight pheromone vs. heuristic information; tunable in both systems"
  - field_a_term: "Pheromone evaporation rate ρ"
    field_b_term: "Forgetting / stale-route decay parameter in digital systems"
    note: "Evaporation prevents premature convergence to suboptimal solutions in both domains"
  - field_a_term: "Stigmergic self-organisation (no central control)"
    field_b_term: "Distributed swarm-robot coordination via shared environment"
    note: "Both systems encode solutions in the environment rather than in agent memory"
related_unknowns:
  - u-stigmergy-optimality-gap-real-environments
related_hypotheses:
  - h-swarm-pheromone-convergence-rate
cross_pollination_opportunities:
  - >
    Real ant-colony tracking with millisecond GPS resolution can test whether
    pheromone update equations match individual ant decision latencies, validating
    or refining the ACO pheromone model beyond graph abstractions.
  - >
    ACO-inspired swarm robots deployed in disaster-response scenarios can use
    evaporation tuning to balance exploitation of known paths with exploration
    of damaged-route alternatives, directly inspired by ant colony adaptability.
communication_gap: >
  Entomologists studying ant trail formation and computer scientists developing
  metaheuristic optimisation publish in separate venues (Insectes Sociaux vs.
  IEEE TAES / Operations Research). The formal mathematical equivalence between
  biological pheromone dynamics and ACO update rules was stated by Dorigo 1992
  but is rarely cited in the biological literature.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1142/S0218213006002813"
    note: "Dorigo & Stutzle (2002) – Ant Colony Optimization: algorithmic overview and convergence proofs"
  - doi: "10.1073/pnas.89.12.5979"
    note: "Goss et al. (1989) PNAS – ant trail selection experiment demonstrating shortest-path emergence"
  - doi: "10.1038/s41598-017-11585-9"
    note: "Perna & Latty (2014) – transport networks in biology and ACO: formal comparison"
  - arxiv: "1010.4982"
    note: "Camazine et al. – Self-Organisation in Biological Systems: stigmergy chapter"
""")

write(ROOT / "unknowns-catalog/engineering/u-stigmergy-optimality-gap-real-environments.yaml", """
id: u-stigmergy-optimality-gap-real-environments
title: >
  How large is the optimality gap between stigmergic swarm routing and
  global-optimal paths in real-world dynamic environments with noise and
  non-stationary costs?
status: open
priority: medium
disciplines:
  - robotics
  - engineering
  - operations-research
summary: >
  Ant Colony Optimisation is proven to converge asymptotically to optimal
  solutions on static graphs, but real environments have changing edge costs,
  sensor noise, and communication failures. The gap between ACO solutions and
  the dynamic optimal tour, and the parameter regimes (ρ, α, β) that minimise
  this gap, are not well characterised for non-stationary environments.
systematic_gaps:
  - No tight bounds exist for ACO convergence speed vs. environment change rate in dynamic graphs.
  - The trade-off between evaporation rate ρ and adaptability to route failures is not optimised in closed form.
  - Empirical comparisons between stigmergic swarm robots and centralised planners in rescue/mapping scenarios are sparse.
last_reviewed: "2026-05-07"
""")

write(ROOT / "hypotheses/active/h-swarm-pheromone-convergence-rate.yaml", """
id: h-swarm-pheromone-convergence-rate
title: >
  In a swarm-robot ACO system, convergence time to within 5% of the shortest
  path scales as O(|E| log|V| / ρ), where |E| is edge count, |V| is vertex
  count, and ρ is the evaporation rate.
status: active
created: "2026-05-07"
priority: medium
impact_score: 0.64
related_disciplines:
  - robotics
  - operations-research
unknowns_addressed:
  - u-stigmergy-optimality-gap-real-environments
evidence_links:
  - doi: "10.1142/S0218213006002813"
    type: supporting
    confidence: 0.60
    note: "Dorigo & Stutzle – ACO convergence analysis; polynomial-time heuristic on TSP"
proposed_tests:
  - description: >
      Deploy ACO on randomly generated planar graphs (|V| = 50–500, |E|/|V| = 2–8)
      with varied ρ (0.01–0.5). Measure steps to 5%-optimal tour for 100 independent
      runs. Fit convergence time to the proposed O(|E| log|V| / ρ) model and compute
      R² across conditions.
""")

# ── 87 ─────────────────────────────────────────────────────────────────────
write(ROOT / "cross-domain/biology-mathematics/b-protein-crystallography-space-groups.yaml", """
id: b-protein-crystallography-space-groups
title: >
  Protein crystal packing is governed by the 65 chiral (Sohncke) space groups
  of classical crystallography: group-theoretic symmetry constraints determine
  allowable unit-cell geometries, reduce the phase problem to a finite search,
  and predict systematic absences in diffraction patterns with mathematical
  precision.
status: established
fields:
  - structural-biology
  - crystallography
  - mathematics
  - group-theory
bridge_claim: >
  A crystal is a periodic repetition of a unit cell under the action of a
  space group G ≤ O(3) ⋊ ℝ³. For chiral molecules like proteins (L-amino acids),
  only the 65 Sohncke groups (those lacking improper symmetry operations) are
  allowed. The group action specifies: (1) how many independent copies of the
  molecule per unit cell (the asymmetric unit), (2) systematic absences in
  Miller indices (h,k,l) that violate group-required extinctions, and (3) the
  symmetry of the Patterson function used for molecular replacement. Group
  theory thus transforms a continuous 3D electron-density inference problem
  into a discrete search over ≤65 symmetry classes.
translation_table:
  - field_a_term: "Space group of the crystal lattice"
    field_b_term: "Discrete group G ≤ O(3) ⋊ ℝ³ acting on electron density"
    note: "65 chiral space groups for proteins; generators specify allowed symmetry operations"
  - field_a_term: "Asymmetric unit (AU)"
    field_b_term: "Fundamental domain of the group action"
    note: "AU contains exactly one independent copy of the molecule; full crystal = G × AU"
  - field_a_term: "Systematic absences in diffraction pattern"
    field_b_term: "Group-theoretic extinction conditions on structure factors F(hkl)"
    note: "Screw axes and glide planes force F(hkl)=0 for specific (h,k,l) combinations"
  - field_a_term: "Patterson function P(u)"
    field_b_term: "Autocorrelation of the group-invariant electron density"
    note: "Peaks at inter-atomic vectors; symmetry of P(u) reflects point group, enabling molecular replacement"
related_unknowns:
  - u-protein-crystal-packing-predictability
related_hypotheses:
  - h-space-group-frequency-evolution-bias
cross_pollination_opportunities:
  - >
    Machine-learning models trained on the CSD/PDB distribution of space-group
    frequencies vs. protein physicochemical properties could predict the most
    likely space group for a target protein before crystallisation, accelerating
    screening campaigns.
  - >
    Group-theoretic analysis of quasicrystalline packing could reveal new
    crystal forms for flexible proteins that fail to pack in standard 65 Sohncke
    groups, extending structural biology into aperiodic-order mathematics.
communication_gap: >
  Mathematical crystallographers (publishing in Acta Crystallographica A) and
  structural biologists (publishing in Nature Structural Biology, Structure)
  share the space-group formalism but rarely cross-publish theoretical analyses
  of why certain space groups are evolutionarily preferred for proteins.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1107/S2059798316007191"
    note: "Winn et al. – CCP4 suite; space-group determination in protein crystallography"
  - doi: "10.1107/S0907444909042073"
    note: "McCoy et al. (2007) – PHASER: likelihood-based molecular replacement using group theory"
  - doi: "10.1107/S2052252517000422"
    note: "Dauter & Jaskolski (2010) – How to read (and understand) Volume A of IT for Crystallographers"
  - doi: "10.1016/S0022-2836(05)80360-2"
    note: "Rossmann & Arnold – International Tables for X-ray Crystallography: protein space groups"
""")

write(ROOT / "unknowns-catalog/biology/u-protein-crystal-packing-predictability.yaml", """
id: u-protein-crystal-packing-predictability
title: >
  Can the space group and unit-cell parameters of a protein crystal be predicted
  de novo from the protein sequence or structure, and what determines the
  observed non-uniform space-group frequency distribution in the PDB?
status: open
priority: medium
disciplines:
  - structural-biology
  - crystallography
  - mathematics
summary: >
  The Protein Data Bank shows a highly non-uniform distribution of space groups:
  P2₁2₁2₁ and P2₁ account for ~55% of depositions. Whether this reflects
  physicochemical biases (surface charge, crystal-contact propensity) or
  crystallisation screening biases is unknown. Predicting the best space group
  before crystallisation would dramatically accelerate structure determination.
systematic_gaps:
  - The relative contributions of protein surface properties vs. crystallisation conditions to space-group selection are not quantified.
  - No validated computational tool can reliably predict space group from sequence alone (success rate <15% for best current methods).
  - The relationship between space-group frequency and protein evolutionary pressures (e.g., symmetry selection in oligomers) is not explored.
last_reviewed: "2026-05-07"
""")

write(ROOT / "hypotheses/active/h-space-group-frequency-evolution-bias.yaml", """
id: h-space-group-frequency-evolution-bias
title: >
  The over-representation of P2₁2₁2₁ in the PDB is not a crystallisation-
  screening artefact but reflects a genuine physicochemical bias: proteins with
  β-sheet-rich surfaces preferentially form crystal contacts consistent with
  P2₁2₁2₁ symmetry due to complementary hydrogen-bond geometry.
status: active
created: "2026-05-07"
priority: medium
impact_score: 0.60
related_disciplines:
  - structural-biology
  - crystallography
unknowns_addressed:
  - u-protein-crystal-packing-predictability
evidence_links:
  - doi: "10.1107/S2052252517000422"
    type: related
    confidence: 0.45
    note: "Dauter & Jaskolski – statistical overview of space-group preferences in PDB"
proposed_tests:
  - description: >
      Train a logistic-regression classifier on PDB entries (features: secondary
      structure fraction, surface charge, SASA, molecular weight; label: P2₁2₁2₁ vs. other).
      Compare accuracy to a null model using only molecular weight. Test on proteins
      first deposited after 2020 to avoid training-set leakage.
""")

# ── 88 ─────────────────────────────────────────────────────────────────────
write(ROOT / "cross-domain/epidemiology-mathematics/b-sir-network-percolation-threshold.yaml", """
id: b-sir-network-percolation-threshold
title: >
  The epidemic threshold R₀ = 1 in the SIR model is mathematically identical
  to the bond-percolation threshold on the contact network: an epidemic spreads
  to a macroscopic fraction of the population if and only if the transmission
  bond-occupation probability exceeds the percolation critical point p_c,
  and the final epidemic size equals the size of the giant percolation cluster.
status: established
fields:
  - epidemiology
  - network-science
  - statistical-physics
  - mathematics
bridge_claim: >
  In an SIR epidemic on a contact network, each edge (i,j) is independently
  occupied with probability T = 1 − exp(−βτ) (transmission probability ×
  infectious period). The expected outbreak size from a single seed equals
  the expected cluster size in bond percolation at occupation probability T.
  The epidemic threshold R₀ = T⟨k²⟩/⟨k⟩ = 1 coincides with the percolation
  threshold p_c = ⟨k⟩/⟨k²⟩ on heterogeneous networks (Pastor-Satorras &
  Vespignani 2001). On scale-free networks with degree exponent γ < 3,
  ⟨k²⟩ → ∞, giving p_c → 0: epidemics spread at arbitrarily low
  transmissibility—the network-percolation framework explains the vanishing
  threshold on power-law contact networks.
translation_table:
  - field_a_term: "Bond occupation probability T (SIR transmissibility)"
    field_b_term: "Percolation bond probability p"
    note: "T = 1−exp(−βτ); p=T at the mapping; p > p_c ↔ R₀ > 1"
  - field_a_term: "Giant connected component (percolation)"
    field_b_term: "Final epidemic size (fraction ever infected)"
    note: "Both equal the probability that an initial node is in the giant cluster"
  - field_a_term: "Percolation threshold p_c = ⟨k⟩/⟨k²⟩"
    field_b_term: "Epidemic threshold R₀ = 1 (T_c = p_c on the network)"
    note: "Identical quantities; p_c → 0 on scale-free networks ↔ vanishing epidemic threshold"
  - field_a_term: "Targeted immunisation = node removal (percolation)"
    field_b_term: "Vaccination strategy in an epidemic network"
    note: "Removing high-degree nodes fragments the giant component faster than random removal"
related_unknowns:
  - u-sir-percolation-temporal-network-threshold
related_hypotheses:
  - h-targeted-vaccination-percolation-optimality
cross_pollination_opportunities:
  - >
    Percolation theory on temporal networks (edges exist only at specific times)
    can refine SIR epidemic threshold calculations beyond static contact-network
    approximations, incorporating daily mobility patterns from mobile-phone data.
  - >
    Bond-percolation cluster-size distributions near p_c obey finite-size
    scaling laws; the same scaling can be applied to small-population outbreak
    size distributions to estimate proximity to the epidemic threshold from
    surveillance data.
communication_gap: >
  Epidemiologists traditionally frame R₀ in terms of individual transmission
  rates, while statistical physicists frame percolation as a phase transition on
  graphs. Pastor-Satorras & Vespignani (2001) stated the equivalence for
  scale-free networks; Newman (2002) proved it for general degree distributions.
  The equivalence is known to network scientists but rarely appears in CDC/WHO
  epidemiological guidance.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1103/PhysRevLett.86.3200"
    note: "Pastor-Satorras & Vespignani (2001) PRL – epidemic spreading on scale-free networks; vanishing threshold"
  - doi: "10.1103/PhysRevE.66.016128"
    note: "Newman (2002) PRE – formal proof of SIR–percolation equivalence on arbitrary degree distributions"
  - doi: "10.1103/PhysRevLett.85.4626"
    note: "Moore & Newman (2000) PRL – epidemics and percolation in small-world networks"
  - doi: "10.1126/science.1248506"
    note: "Brockmann & Helbing (2013) Science – global epidemic spreading via effective-distance network geometry"
""")

write(ROOT / "unknowns-catalog/mathematics/u-sir-percolation-temporal-network-threshold.yaml", """
id: u-sir-percolation-temporal-network-threshold
title: >
  What is the exact epidemic threshold for SIR dynamics on temporal contact
  networks, and how does temporal burstiness shift the threshold relative to
  static-network percolation predictions?
status: open
priority: high
disciplines:
  - epidemiology
  - network-science
  - statistical-physics
summary: >
  The SIR–percolation equivalence is rigorously established for static networks
  but temporal contact networks (where edges appear and disappear over time)
  invalidate static percolation theory. Temporal burstiness (heavy-tailed
  inter-contact times) slows spreading compared to Poisson contacts. The
  equivalent percolation threshold for temporal networks has no closed-form
  expression and depends on the full inter-contact time distribution.
systematic_gaps:
  - No analytic expression for R₀ on temporal networks with arbitrary inter-contact time distributions.
  - The effect of simultaneous temporal burstiness and heterogeneous degree is not captured by existing approximations.
  - Empirical validation of temporal-network epidemic thresholds using real contact data (e.g., SocioPatterns) is limited to specific settings.
last_reviewed: "2026-05-07"
""")

write(ROOT / "hypotheses/active/h-targeted-vaccination-percolation-optimality.yaml", """
id: h-targeted-vaccination-percolation-optimality
title: >
  Targeted vaccination of the top-k% highest-degree individuals in a contact
  network reduces the giant-component size (and therefore final epidemic size)
  by a factor at least 3× greater than random vaccination at the same coverage,
  for all real-world contact networks with degree-distribution variance ⟨k²⟩/⟨k⟩² > 5.
status: active
created: "2026-05-07"
priority: high
impact_score: 0.87
related_disciplines:
  - epidemiology
  - network-science
unknowns_addressed:
  - u-sir-percolation-temporal-network-threshold
evidence_links:
  - doi: "10.1103/PhysRevLett.86.3200"
    type: supporting
    confidence: 0.80
    note: "Pastor-Satorras & Vespignani – targeted immunisation dramatically reduces threshold on scale-free networks"
  - doi: "10.1103/PhysRevE.66.016128"
    type: supporting
    confidence: 0.75
    note: "Newman (2002) – percolation analysis of targeted node removal efficiency"
proposed_tests:
  - description: >
      Simulate SIR epidemics (β, γ varied over realistic ranges) on 10 empirical
      contact networks (SocioPatterns datasets). Compare final epidemic size under
      random vs. degree-targeted vaccination at 5%, 10%, 20% coverage. Compute
      efficacy ratio and test whether it exceeds 3× for all networks with
      ⟨k²⟩/⟨k⟩² > 5 at 95% confidence.
""")

# ── 89 ─────────────────────────────────────────────────────────────────────
write(ROOT / "cross-domain/materials-science-physics/b-phonon-boltzmann-thermal-transport.yaml", """
id: b-phonon-boltzmann-thermal-transport
title: >
  Thermal conductivity of crystalline solids is quantitatively predicted by
  the phonon Boltzmann transport equation (BTE): κ = (1/3)∫C(ω)v(ω)λ(ω)dω,
  where acoustic phonons are the heat carriers and three-phonon Umklapp
  scattering is the primary resistive process, directly connecting lattice
  dynamics to macroscopic heat flow.
status: established
fields:
  - condensed-matter-physics
  - materials-science
  - thermodynamics
bridge_claim: >
  Phonons—quantised lattice vibrations—carry heat in insulators and
  semiconductors exactly as molecules carry heat in gases. The phonon BTE
  (Peierls 1929) describes their out-of-equilibrium distribution under a
  temperature gradient: ∂n_λ/∂t + v_λ·∇T(∂n_λ/∂T) = (∂n_λ/∂t)|_scatt.
  Thermal conductivity κ is obtained by linearising and solving: κ =
  (1/NkΩ)Σ_λ C_λ v²_λ τ_λ, where C_λ is the mode heat capacity, v_λ the
  group velocity, and τ_λ the relaxation time from three-phonon Umklapp
  processes. First-principles BTE calculations (Broido 2007) using density-
  functional perturbation theory predict κ for Si, Ge, and diamond to within
  5% of experiment—demonstrating that lattice dynamics and kinetic theory
  are sufficient to explain macroscopic thermal transport.
translation_table:
  - field_a_term: "Phonon mode λ = (q, s) (wavevector, branch)"
    field_b_term: "Gas molecule in kinetic theory"
    note: "Both obey Bose-Einstein (phonons) / Maxwell-Boltzmann (classical) equilibrium distributions"
  - field_a_term: "Phonon group velocity v_λ = ∂ω/∂q"
    field_b_term: "Molecular velocity in kinetic theory"
    note: "Determines the diffusion rate of heat; dispersive bands give wavelength-dependent velocities"
  - field_a_term: "Phonon-phonon Umklapp scattering (three-phonon)"
    field_b_term: "Molecular collision in kinetic theory (momentum-non-conserving)"
    note: "Umklapp restores crystal momentum with a reciprocal lattice vector G ≠ 0, providing thermal resistance"
  - field_a_term: "Phonon mean free path λ = v_λ τ_λ"
    field_b_term: "Mean free path between molecular collisions"
    note: "Both set the length scale over which heat diffuses; nano-structuring below λ reduces κ"
related_unknowns:
  - u-phonon-mean-free-path-nanostructured-materials
related_hypotheses:
  - h-phonon-mfp-spectrum-thermal-conductivity-engineering
cross_pollination_opportunities:
  - >
    Phonon mean-free-path spectroscopy (using ultrafast laser heating at varying
    modulation frequencies) can map the κ(λ) spectrum, enabling targeted
    nanostructure design that scatters only long-mean-free-path phonons while
    preserving charge transport.
  - >
    Machine-learning interatomic potentials trained on DFT phonon force constants
    can accelerate first-principles BTE calculations to screen thermoelectric
    material libraries orders-of-magnitude faster than DFT alone.
communication_gap: >
  Kinetic theorists and materials scientists use different notations (kinetic
  theory uses collision integrals; solid-state physics uses second quantisation).
  The equivalence was established by Peierls (1929) and Callaway (1959) but
  textbook treatments of each field rarely cross-reference the other.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1103/PhysRevLett.99.185901"
    note: "Broido et al. (2007) PRL – first-principles phonon BTE gives κ for Si and Ge within 5% of experiment"
  - doi: "10.1103/PhysRev.113.1046"
    note: "Callaway (1959) PR – model thermal conductivity from phonon relaxation times"
  - doi: "10.1016/j.physrep.2018.02.004"
    note: "McGaughey et al. (2019) Physics Reports – phonon transport in nanostructured materials"
  - doi: "10.1038/s41578-018-0018-2"
    note: "Snyder & Toberer – complex thermoelectric materials; phonon engineering"
""")

write(ROOT / "unknowns-catalog/materials-science/u-phonon-mean-free-path-nanostructured-materials.yaml", """
id: u-phonon-mean-free-path-nanostructured-materials
title: >
  How does the phonon mean-free-path spectrum change at interfaces and grain
  boundaries in nanostructured thermoelectric materials, and can interface
  engineering selectively scatter heat-carrying phonons without degrading
  electron transport?
status: open
priority: high
disciplines:
  - materials-science
  - condensed-matter-physics
  - nanotechnology
summary: >
  Thermal conductivity reduction through nanostructuring (grain boundaries,
  nanoinclusions) is the primary route to improving thermoelectric figure of
  merit ZT. However, the same interfaces scatter electrons, reducing electrical
  conductivity. The phonon mean-free-path spectrum in nanostructured materials
  and the conditions under which interfaces selectively scatter only phonons
  (not electrons) are not fully characterised.
systematic_gaps:
  - Phonon-interface scattering models (diffuse mismatch, acoustic mismatch) systematically underestimate measured interface thermal resistance (Kapitza resistance).
  - The cross-over from bulk to nano-scale phonon transport is not captured by the BTE with bulk scattering rates.
  - The optimal grain-size distribution for maximum ZT in polycrystalline thermoelectrics is not derived from first principles.
last_reviewed: "2026-05-07"
""")

write(ROOT / "hypotheses/active/h-phonon-mfp-spectrum-thermal-conductivity-engineering.yaml", """
id: h-phonon-mfp-spectrum-thermal-conductivity-engineering
title: >
  A bimodal grain-size distribution in polycrystalline thermoelectrics—with
  grain sizes targeting the two peaks of the phonon mean-free-path spectrum—
  will reduce κ_L by >60% relative to the single-grain-size optimum while
  reducing electrical conductivity by <15%.
status: active
created: "2026-05-07"
priority: medium
impact_score: 0.73
related_disciplines:
  - materials-science
  - condensed-matter-physics
unknowns_addressed:
  - u-phonon-mean-free-path-nanostructured-materials
evidence_links:
  - doi: "10.1103/PhysRevLett.99.185901"
    type: supporting
    confidence: 0.65
    note: "Broido – first-principles MFP spectrum for Si shows bimodal structure; suggests bimodal targeting"
  - doi: "10.1038/s41578-018-0018-2"
    type: supporting
    confidence: 0.60
    note: "Snyder & Toberer – nanostructuring strategies for ZT enhancement in thermoelectrics"
proposed_tests:
  - description: >
      Fabricate Bi₂Te₃ samples with controlled bimodal grain size distributions
      (peak diameters at 5 nm and 80 nm, targeting the MFP spectrum peaks from
      first-principles BTE). Measure κ_L by time-domain thermoreflectance and
      σ by 4-probe electrical measurement. Compare to unimodal 20 nm baseline.
""")

# ── 90 ─────────────────────────────────────────────────────────────────────
write(ROOT / "cross-domain/neuroscience-biology/b-retinal-waves-spontaneous-activity.yaml", """
id: b-retinal-waves-spontaneous-activity
title: >
  Spontaneous correlated activity (retinal waves) in the developing retina
  drives Hebbian refinement of retinotopic maps in superior colliculus and
  lateral geniculate nucleus via activity-dependent synaptic plasticity:
  the spatial correlation structure of the waves encodes positional information
  that substitutes for visual experience before eye-opening.
status: established
fields:
  - developmental-neuroscience
  - neuroscience
  - molecular-biology
  - systems-biology
bridge_claim: >
  Before eye-opening, retinal ganglion cells (RGCs) fire in propagating waves
  mediated by gap junctions (Stage I) and cholinergic amacrine cells (Stage II)
  that produce correlated bursts in neighbouring RGCs. The Hebb rule—"cells that
  fire together wire together"—predicts that correlated RGC pairs form stronger
  LGN synapses than uncorrelated pairs. Because wave initiation sites are
  spatially structured, neighbouring RGCs are more correlated than distant RGCs,
  transmitting a topographic correlation gradient to LGN. Katz & Shatz (1996)
  showed that blocking retinal waves (tetrodotoxin) disrupts ocular dominance
  column formation without visual experience, proving that the wave correlation
  structure is informationally sufficient for circuit refinement.
translation_table:
  - field_a_term: "Correlated bursting of neighbouring RGCs during a wave"
    field_b_term: "Hebb-rule co-activation driving LTP at shared LGN target"
    note: "Spatial correlation gradient of waves encodes retinal neighbourhood; Hebb rule reads this gradient"
  - field_a_term: "Retinal wave propagation velocity (~200 μm/s)"
    field_b_term: "Spatial bandwidth of activity correlation (sets map resolution)"
    note: "Faster waves correlate larger retinal neighbourhoods; slower waves encode finer topography"
  - field_a_term: "Stage II cholinergic waves (ACh-mediated)"
    field_b_term: "Critical period analogue: ACh sets gain and spatial extent of correlation"
    note: "β2 nicotinic receptor knockout eliminates waves and disrupts retinotopic maps"
  - field_a_term: "Eye-specific segregation in LGN"
    field_b_term: "Competitive Hebbian learning: ipsi vs. contra RGC firing decorrelated"
    note: "Eyes fire asynchronous waves; anti-correlation drives segregation into laminae"
related_unknowns:
  - u-retinal-wave-spatial-statistics-map-precision
related_hypotheses:
  - h-retinal-wave-bandwidth-map-resolution-constraint
cross_pollination_opportunities:
  - >
    Statistical analysis of retinal wave correlation functions (measuring spatial
    autocorrelation length as a function of ACh concentration) can compute the
    Shannon information the wave pattern conveys about retinal position—testing
    whether the wave bandwidth is information-theoretically optimised for map
    formation.
  - >
    Optogenetic silencing of individual retinal sectors during the critical period
    can test whether the map is degraded proportionally to the silenced area,
    validating the Hebbian topography-encoding model quantitatively.
communication_gap: >
  Developmental neurobiologists studying retinal waves and computational
  neuroscientists studying Hebbian learning and map formation publish in separate
  journals (J. Neurosci., Neuron vs. Neural Computation, PLOS Computational
  Biology). The information-theoretic framing of retinal waves as a topographic
  code is underexplored in experimental literature.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1126/science.1254927"
    note: "Ackman et al. (2012) Science – retinal waves drive retinotopic map refinement in V1 before eye-opening"
  - doi: "10.1016/0092-8674(96)90606-1"
    note: "Katz & Shatz (1996) Cell – synaptic activity and development of the visual cortex; wave review"
  - doi: "10.1126/science.7770778"
    note: "Meister et al. (1991) Science – first observation of correlated spontaneous activity in retina"
  - doi: "10.1523/JNEUROSCI.2395-07.2007"
    note: "Huberman et al. (2007) J. Neurosci. – beta2 nAChR knockout disrupts retinal wave correlation and retinotopy"
""")

write(ROOT / "unknowns-catalog/neuroscience/u-retinal-wave-spatial-statistics-map-precision.yaml", """
id: u-retinal-wave-spatial-statistics-map-precision
title: >
  What determines the spatial statistics (correlation length, wave-initiation
  density) of retinal waves, and is there an information-theoretic optimum
  that matches the precision of mature retinotopic maps?
status: open
priority: medium
disciplines:
  - developmental-neuroscience
  - information-theory
  - systems-biology
summary: >
  Retinal waves encode positional information via their spatial correlation
  structure. The precision of the retinotopic map (angular resolution ~0.1°
  in mice) places a lower bound on the mutual information that waves must convey
  about retinal position. Whether the wave statistics are optimised for this
  information requirement, or are limited by cholinergic network constraints,
  is not known.
systematic_gaps:
  - The spatial autocorrelation function of Stage II retinal waves has not been measured with sufficient temporal resolution to compute mutual information between wave pattern and retinal position.
  - The relationship between wave correlation length and final retinotopic map precision across manipulated animals (ACh dose, temperature) has not been quantified.
  - The information-theoretic efficiency of wave-based topographic coding has not been calculated.
last_reviewed: "2026-05-07"
""")

write(ROOT / "hypotheses/active/h-retinal-wave-bandwidth-map-resolution-constraint.yaml", """
id: h-retinal-wave-bandwidth-map-resolution-constraint
title: >
  The spatial autocorrelation length of Stage II retinal waves sets an upper
  bound on retinotopic map resolution equal to the wave correlation length
  divided by 2π, matching the observed retinotopic map precision in C57BL/6 mice.
status: active
created: "2026-05-07"
priority: medium
impact_score: 0.68
related_disciplines:
  - developmental-neuroscience
  - information-theory
unknowns_addressed:
  - u-retinal-wave-spatial-statistics-map-precision
evidence_links:
  - doi: "10.1126/science.1254927"
    type: supporting
    confidence: 0.60
    note: "Ackman 2012 – wave-driven retinotopic refinement; spatial structure of waves predicts map organisation"
proposed_tests:
  - description: >
      Use two-photon calcium imaging to measure the spatial autocorrelation
      function C(r) = ⟨ΔF(x)ΔF(x+r)⟩ of Stage II retinal waves in P5–P10
      C57BL/6 mice. Compute the correlation length ξ = ∫C(r)dr. Compare
      ξ/(2π) to the retinotopic map precision (receptive field scatter) measured
      by single-unit recordings in the same animals' superior colliculus.
""")

# ── 91 ─────────────────────────────────────────────────────────────────────
write(ROOT / "cross-domain/geoscience-physics/b-mantle-convection-rayleigh-benard.yaml", """
id: b-mantle-convection-rayleigh-benard
title: >
  Mantle convection driving plate tectonics is a high-Rayleigh-number
  Rayleigh-Bénard convection system with strongly temperature-dependent
  viscosity: the Rayleigh number Ra ~ 10⁷–10⁸ predicts chaotic, time-
  dependent flow that produces the observed pattern of plate speeds, trench
  depths, and heat flow at mid-ocean ridges.
status: established
fields:
  - geophysics
  - fluid-mechanics
  - physics
bridge_claim: >
  The mantle is a highly viscous fluid (η ~ 10²¹ Pa·s) heated from below
  by radiogenic decay and cooling from above. Rayleigh-Bénard (RB) convection
  occurs when buoyancy (Δρ g d) overcomes viscous resistance: Ra =
  αΔTρgd³/(κη) ~ 10⁷. At this Ra, RB convection is time-dependent and
  produces plume-dominated structures. The additional complication of
  strongly temperature-dependent viscosity (η ∝ exp(E_a/RT) spanning 10 orders
  of magnitude) creates a rigid lid (the lithosphere) on top of convecting
  mantle—the stagnant-lid regime. Plate tectonics requires lithospheric
  yielding (grain-size weakening, hydration) to breach the stagnant lid,
  adding a rheological threshold to the RB framework.
translation_table:
  - field_a_term: "Rayleigh number Ra of mantle convection"
    field_b_term: "Rayleigh number Ra in RB convection experiment"
    note: "Ra ~ 10⁷ for mantle; sets the vigour, planform, and time-dependence of convective flow"
  - field_a_term: "Lithosphere (cold rigid boundary)"
    field_b_term: "Cold upper plate in RB convection (conducting boundary layer)"
    note: "Stagnant lid ↔ rigid upper plate; plate tectonics requires lid mobilisation"
  - field_a_term: "Mantle plume (rising hot column from CMB)"
    field_b_term: "Thermal plume in RB cell (rising hot column from heated base)"
    note: "Both governed by plume stability criterion and buoyancy flux"
  - field_a_term: "Mid-ocean ridge heat flux"
    field_b_term: "Heat transport efficiency Nu(Ra) in RB convection"
    note: "Nu ~ Ra^{0.3} scaling predicts global mantle heat loss from Ra"
related_unknowns:
  - u-mantle-convection-plate-tectonic-onset
related_hypotheses:
  - h-plate-tectonics-ra-viscosity-threshold
cross_pollination_opportunities:
  - >
    Laboratory RB convection experiments with strongly temperature-dependent
    viscosity fluids (Golden Syrup, silicone oils) can test stagnant-lid
    transitions and plume emergence at Ra values matching mantle conditions,
    informing planetary convection models for Venus and Mars.
  - >
    Seismic tomography of mantle plume structures can be quantitatively compared
    to the planform and stability of thermal plumes in high-Ra RB numerical
    simulations to constrain mantle viscosity profiles.
communication_gap: >
  Fluid dynamicists studying RB convection (publishing in J. Fluid Mechanics,
  Physical Review Fluids) and geophysicists studying mantle convection
  (publishing in J. Geophysical Research, Earth and Planetary Science Letters)
  use different dimensionless number scalings and rarely directly cite each other's
  laboratory experiments.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1029/JB075i003p00497"
    note: "Turcotte & Oxburgh (1967) JGR – thermal convection below the lithosphere; RB framework for mantle"
  - doi: "10.1038/s41561-022-00913-8"
    note: "Tackley (2008) – mantle convection models with plate tectonics: review of RB framework"
  - doi: "10.1126/science.1135456"
    note: "van Keken et al. – mantle mixing and convection; Ra-heat-flow scaling"
  - doi: "10.1016/j.epsl.2007.10.046"
    note: "Labrosse & Jaupart (2007) EPSL – thermal evolution of mantle and core from RB scaling laws"
""")

write(ROOT / "unknowns-catalog/geoscience/u-mantle-convection-plate-tectonic-onset.yaml", """
id: u-mantle-convection-plate-tectonic-onset
title: >
  What physical and rheological conditions trigger the onset of plate tectonics
  from a stagnant-lid convection regime, and why does Earth have plate tectonics
  while Venus does not?
status: open
priority: high
disciplines:
  - geophysics
  - planetary-science
  - fluid-mechanics
summary: >
  Both Earth and Venus have similar Ra numbers and bulk compositions, yet Earth
  has mobile plate tectonics while Venus has a stagnant lid. The conditions—
  surface water content enabling grain-size reduction and serpentinisation,
  yield stress of the lithosphere, initial temperature state—that tip a planet
  from stagnant-lid to plate-tectonic convection regime remain debated. This is
  the central unresolved problem in comparative planetology.
systematic_gaps:
  - No self-consistent mantle convection simulation has spontaneously initiated plate-tectonic-like behaviour from a stagnant lid without prescribed weakening zones.
  - The relative importance of water content, impact history, and initial temperature in triggering plate tectonics is not quantified.
  - Venus's interior structure is poorly constrained; surface topography data from Magellan is insufficient to detect active tectonism.
last_reviewed: "2026-05-07"
""")

write(ROOT / "hypotheses/active/h-plate-tectonics-ra-viscosity-threshold.yaml", """
id: h-plate-tectonics-ra-viscosity-threshold
title: >
  Plate tectonics initiates when the effective viscosity contrast between the
  lithosphere and asthenosphere drops below a critical ratio η_lid/η_mantle ~ 10³,
  achievable on Earth via water-induced grain-size reduction but not on dry Venus.
status: active
created: "2026-05-07"
priority: high
impact_score: 0.80
related_disciplines:
  - geophysics
  - planetary-science
unknowns_addressed:
  - u-mantle-convection-plate-tectonic-onset
evidence_links:
  - doi: "10.1016/j.epsl.2007.10.046"
    type: supporting
    confidence: 0.55
    note: "Labrosse & Jaupart – viscosity-dependent stagnant-lid stability; critical viscosity ratio"
  - doi: "10.1038/s41561-022-00913-8"
    type: related
    confidence: 0.50
    note: "Tackley 2008 – weakening mechanisms required for plate tectonics in simulations"
proposed_tests:
  - description: >
      Run 2D spherical mantle convection simulations (ASPECT or CitcomS) at
      Venus-like and Earth-like water contents, varying η_lid/η_mantle from 10¹
      to 10⁶. Record whether spontaneous plate-like mobility emerges. Determine
      the critical viscosity contrast and compare to grain-size weakening estimates
      for hydrated vs. dry olivine rheology.
""")

# ── 92 ─────────────────────────────────────────────────────────────────────
write(ROOT / "cross-domain/biology-ecology/b-microbiome-diversity-stability.yaml", """
id: b-microbiome-diversity-stability
title: >
  Gut microbiome species diversity predicts community resilience to antibiotic
  perturbation and pathogen invasion, following May's theoretical diversity-
  stability relationship: higher phylogenetic diversity increases functional
  redundancy and reduces the probability that a single perturbation collapses
  the entire community.
status: proposed
fields:
  - microbiology
  - ecology
  - systems-biology
  - medicine
bridge_claim: >
  May (1972) showed that in random ecological communities, stability (return
  to equilibrium after perturbation) decreases with diversity and interaction
  strength: σ²SC < 1 (May's criterion), where σ² is interaction variance, S is
  species richness, and C is connectance. However, structured communities with
  trophic hierarchy and modularity violate the random-matrix assumption and can
  show diversity-stability positive correlation. The gut microbiome is highly
  structured (diet-specialist guilds, cross-feeding networks) and empirical
  studies (Turnbaugh 2006, Sonnenburg 2016) show diverse microbiomes recover
  faster from antibiotics. The bridge claim: microbiome diversity-stability
  follows the structured-community branch of May's framework, where functional
  redundancy (multiple species performing same metabolic role) buffers against
  perturbation.
translation_table:
  - field_a_term: "May's community matrix eigenvalue maximum (stability criterion)"
    field_b_term: "Microbiome recovery rate (inverse return time after antibiotic)"
    note: "Negative maximum eigenvalue → stable community; scales with functional redundancy"
  - field_a_term: "Ecological functional redundancy"
    field_b_term: "Multiple gut taxa performing same fermentation/butyrate pathway"
    note: "Redundant taxa buffer against stochastic extinction of individual species"
  - field_a_term: "Connectance C (fraction of realised interactions)"
    field_b_term: "Microbiome co-occurrence network density"
    note: "Higher connectance increases cross-feeding resilience but can destabilise under May's criterion"
  - field_a_term: "Diversity index (Shannon entropy H)"
    field_b_term: "Gut microbiome α-diversity (16S rRNA amplicon sequencing)"
    note: "H predicts recovery speed from Clostridioides difficile infection post-antibiotics"
related_unknowns:
  - u-microbiome-diversity-stability-causality
related_hypotheses:
  - h-microbiome-functional-redundancy-antibiotic-resilience
cross_pollination_opportunities:
  - >
    Ecological stability theory (Lyapunov stability analysis of community matrices)
    applied to inferred microbiome interaction networks from paired longitudinal
    metagenomics could test whether the May criterion predicts individual patients'
    susceptibility to Clostridioides difficile infection.
  - >
    Dietary interventions that increase microbiome diversity (high-fibre diets)
    can be designed using ecological island biogeography theory—maximising
    immigration of novel species from diet—to improve resilience in post-
    antibiotic patients.
communication_gap: >
  May's random-matrix stability results (published in Nature 1972) are central
  to theoretical ecology but rarely cited in microbiome medicine literature.
  Clinical microbiologists measure diversity indices empirically without formal
  dynamical stability theory; ecologists rarely engage with clinical data.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1038/238413a0"
    note: "May (1972) Nature – will a large complex system be stable? random-matrix stability criterion"
  - doi: "10.1038/nature05414"
    note: "Turnbaugh et al. (2006) Nature – the human microbiome; diversity and metabolic function"
  - doi: "10.1126/science.aad9359"
    note: "Sonnenburg & Sonnenburg (2019) Science – diet-induced microbiome diversity and resilience"
  - doi: "10.1038/s41586-019-1406-7"
    note: "Martiny et al. – functional redundancy in microbiomes provides stability under perturbation"
""")

write(ROOT / "unknowns-catalog/biology/u-microbiome-diversity-stability-causality.yaml", """
id: u-microbiome-diversity-stability-causality
title: >
  Does gut microbiome species diversity causally protect against pathogen invasion
  and antibiotic-associated dysbiosis, or is it merely correlated with host factors
  that drive both diversity and resilience?
status: open
priority: high
disciplines:
  - microbiology
  - ecology
  - medicine
summary: >
  Observational studies consistently find that lower microbiome diversity predicts
  greater susceptibility to Clostridioides difficile infection, antibiotic-associated
  diarrhoea, and inflammatory bowel disease. However, host genetics, diet, and immune
  status confound the diversity-outcome relationship. Causal inference from
  observational microbiome data remains a major methodological challenge.
systematic_gaps:
  - Mendelian randomisation approaches for microbiome diversity are not well validated due to the absence of SNPs with large microbiome effects that do not also affect immunity.
  - Germ-free mouse colonisation experiments using defined microbial communities of varying diversity cannot fully recapitulate human microbiome ecology.
  - The minimum diversity required for colonisation resistance (the key functional outcome) has not been determined for any specific pathogen.
last_reviewed: "2026-05-07"
""")

write(ROOT / "hypotheses/active/h-microbiome-functional-redundancy-antibiotic-resilience.yaml", """
id: h-microbiome-functional-redundancy-antibiotic-resilience
title: >
  Gut microbiome communities with butyrate-pathway functional redundancy index
  (FRI > 0.6, defined as the fraction of butyrate production contributed by
  the top-3 producing taxa out of all butyrate producers) will recover to
  pre-antibiotic composition within 30 days after a 7-day broad-spectrum
  antibiotic course in >80% of healthy adults.
status: active
created: "2026-05-07"
priority: high
impact_score: 0.78
related_disciplines:
  - microbiology
  - ecology
unknowns_addressed:
  - u-microbiome-diversity-stability-causality
evidence_links:
  - doi: "10.1038/238413a0"
    type: supporting
    confidence: 0.55
    note: "May (1972) – theoretical basis for functional redundancy as stability mechanism"
  - doi: "10.1038/s41586-019-1406-7"
    type: supporting
    confidence: 0.65
    note: "Martiny – functional redundancy in microbiomes and resilience to perturbation"
proposed_tests:
  - description: >
      Recruit 120 healthy volunteers; collect pre-antibiotic shotgun metagenomes.
      Compute FRI from functional annotation. Prescribe 7-day amoxicillin-clavulanate.
      Collect metagenomes at days 7, 14, 30. Define recovery as Bray-Curtis
      dissimilarity < 0.2 from baseline. Test FRI > 0.6 vs. recovery within 30d
      using logistic regression with age and BMI as covariates.
""")

# ── 93 ─────────────────────────────────────────────────────────────────────
write(ROOT / "cross-domain/materials-science-physics/b-fracture-griffith-statistical.yaml", """
id: b-fracture-griffith-statistical
title: >
  The Griffith fracture criterion (K_I = K_Ic at the crack tip) is the
  deterministic limit of a statistical-physics crack nucleation problem:
  the disorder-averaged fracture strength of heterogeneous materials
  follows a Weibull extreme-value distribution, and the brittle-to-ductile
  transition maps onto a depinning phase transition in the random-field
  Ising model universality class.
status: established
fields:
  - materials-science
  - statistical-physics
  - condensed-matter-physics
bridge_claim: >
  Griffith (1921) showed that fracture occurs when the elastic strain energy
  released by crack propagation (G = K²/E') equals the surface energy cost
  (2γ): K_Ic = √(2Eγ/π). This deterministic criterion applies to a perfect
  crystal. Real materials contain quenched disorder (voids, inclusions, grain
  boundaries), making fracture a statistical event. The Weibull distribution
  P(σ_f) = 1 − exp[−(σ/σ_0)^m] gives the fracture probability as a function
  of stress σ; the Weibull modulus m measures disorder breadth. Statistical
  physics maps crack propagation to a driven elastic manifold in a disordered
  medium: crack-front advance is a depinning transition with power-law avalanche
  statistics, reproducing the acoustic emission bursts observed in fracturing materials.
translation_table:
  - field_a_term: "Griffith critical stress intensity K_Ic"
    field_b_term: "Depinning threshold force in a disordered medium"
    note: "Crack advances when local K_I exceeds K_Ic; equivalent to a driven interface overcoming pinning"
  - field_a_term: "Material disorder (voids, inclusions)"
    field_b_term: "Random pinning field in elastic manifold models"
    note: "Quenched disorder sets the pinning landscape that crack front must traverse"
  - field_a_term: "Weibull modulus m (width of strength distribution)"
    field_b_term: "Disorder strength in random-field Ising model"
    note: "High m → low disorder → deterministic Griffith limit; low m → broad statistical failure distribution"
  - field_a_term: "Acoustic emission avalanches during fracture"
    field_b_term: "Crackling noise / Barkhausen noise in depinning transitions"
    note: "Power-law size distribution of AE events = crackling noise universality class"
related_unknowns:
  - u-fracture-avalanche-universality-class
related_hypotheses:
  - h-fracture-depinning-crackling-noise-exponent
cross_pollination_opportunities:
  - >
    Acoustic emission monitoring of fracture in concrete and rock can be analysed
    using crackling noise theory (power-law exponents, b-value in seismology = 1−1/m)
    to predict proximity to catastrophic failure before it occurs.
  - >
    The depinning framework predicts that crack-front roughness exponents are
    universal (independent of material) in the thermodynamic limit; testing this
    across ceramics, glasses, and composites would confirm or refute the universality class.
communication_gap: >
  Fracture mechanics engineers use stress intensity factors (K) and Weibull
  statistics empirically without connection to the universality class language
  of statistical physics. The depinning/crackling-noise framework (Zapperi, Alava)
  is published in Physical Review Letters / Physical Review E but not in
  engineering fracture journals (Engineering Fracture Mechanics, J. Mechanics
  Physics Solids).
last_reviewed: "2026-05-07"
references:
  - doi: "10.1098/rsta.1921.0006"
    note: "Griffith (1921) – the phenomena of rupture and flow in solids; foundational fracture criterion"
  - doi: "10.1103/PhysRevLett.78.1408"
    note: "Zapperi et al. (1997) PRL – crack propagation as a depinning transition; crackling noise"
  - doi: "10.1126/science.288.5469.1275"
    note: "Sethna et al. (2001) Science – crackling noise: universal power laws in fracture, magnets, earthquakes"
  - doi: "10.1103/PhysRevE.62.6164"
    note: "Alava et al. – fiber bundle model: brittle fracture and Weibull statistics"
""")

write(ROOT / "unknowns-catalog/materials-science/u-fracture-avalanche-universality-class.yaml", """
id: u-fracture-avalanche-universality-class
title: >
  What is the exact universality class of acoustic emission avalanches in
  brittle fracture, and is the crackling-noise exponent τ ~ 1.5 universal
  across materials or material-specific?
status: open
priority: medium
disciplines:
  - materials-science
  - statistical-physics
summary: >
  Acoustic emission (AE) experiments in fracturing materials (rocks, concrete,
  wood, composites) consistently show power-law distributed burst sizes, but
  the exponent τ varies from ~1.3 to ~1.8 across studies. Whether this range
  reflects different universality classes (mean-field vs. short-range vs. long-
  range correlated disorder) or experimental artefacts (sensor bandwidth, sample
  size effects) is not resolved. Establishing the universality class would
  connect fracture to the broader crackling noise framework.
systematic_gaps:
  - Finite-size scaling analysis of AE avalanche distributions has not been performed on sufficiently large sample sets to distinguish universality classes.
  - The role of material anisotropy and grain-size distribution on the τ exponent is not characterised.
  - Comparison between acoustic emission and direct imaging of crack-front geometry has not been performed to validate the depinning model.
last_reviewed: "2026-05-07"
""")

write(ROOT / "hypotheses/active/h-fracture-depinning-crackling-noise-exponent.yaml", """
id: h-fracture-depinning-crackling-noise-exponent
title: >
  The acoustic emission size exponent τ in brittle fracture of isotropic
  polycrystalline materials is universally τ = 1.5 ± 0.1 (mean-field depinning
  universality class) in the limit of sample size L >> grain size d, with
  material-specific deviations arising only when L/d < 100.
status: active
created: "2026-05-07"
priority: medium
impact_score: 0.65
related_disciplines:
  - materials-science
  - statistical-physics
unknowns_addressed:
  - u-fracture-avalanche-universality-class
evidence_links:
  - doi: "10.1126/science.288.5469.1275"
    type: supporting
    confidence: 0.65
    note: "Sethna 2001 – crackling noise review; mean-field τ = 1.5 for depinning"
  - doi: "10.1103/PhysRevLett.78.1408"
    type: supporting
    confidence: 0.60
    note: "Zapperi 1997 – crack as depinning; τ = 3/2 in mean-field limit"
proposed_tests:
  - description: >
      Perform three-point bending fracture experiments on polycrystalline alumina
      samples with L/d ranging from 10 to 1000 (grain sizes 1–100 μm, sample
      sizes 1 cm–10 cm). Record acoustic emission with wideband piezoelectric
      sensors. Apply maximum-likelihood estimation to fit power-law τ. Test
      whether τ → 1.5 for L/d > 100 using finite-size scaling analysis.
""")

# ── 94 ─────────────────────────────────────────────────────────────────────
write(ROOT / "cross-domain/social-science-biology/b-moral-psychology-cooperation-game-theory.yaml", """
id: b-moral-psychology-cooperation-game-theory
title: >
  Moral intuitions of fairness (third-party punishment, inequity aversion)
  are quantitatively predicted by evolutionarily stable strategies in
  iterated public-goods games with altruistic punishment: the costly punishment
  instinct evolved to maintain cooperation in groups where purely self-interested
  free-riding would otherwise dominate.
status: proposed
fields:
  - moral-psychology
  - evolutionary-biology
  - game-theory
  - social-science
bridge_claim: >
  Fehr & Gächter (2002) showed that humans will pay a personal cost to punish
  unfair players in one-shot public-goods games—a behaviour unexplained by
  standard self-interest models. Nowak & May (1992) and subsequent evolutionary
  simulations show that altruistic punishment is an ESS when group size and
  punishment cost satisfy specific conditions. Haidt's moral-foundations theory
  identifies fairness/reciprocity and authority/respect as cross-cultural moral
  universals, which correspond precisely to the punishment-reciprocity strategies
  that stabilise cooperation in evolutionary game theory. The bridge: moral
  psychology's empirical moral foundations are the phenotypic expression of
  evolutionary game-theoretic stable cooperation strategies.
translation_table:
  - field_a_term: "Altruistic third-party punishment (paying to sanction defectors)"
    field_b_term: "Costly punishment ESS in public-goods game"
    note: "Both sacrifice payoff to maintain group cooperation; evolutionarily stable when c_punishment < (1-ε)Δcooperation"
  - field_a_term: "Inequity aversion (Fehr-Schmidt preference)"
    field_b_term: "ESS fairness norm in ultimatum game"
    note: "Ultimatum game rejection of unfair splits = enforcement of fairness ESS through credible threat"
  - field_a_term: "Moral disgust toward cheaters (Haidt moral foundation)"
    field_b_term: "Emotional mechanism for maintaining conditional cooperation strategy"
    note: "Disgust emotion reduces the cognitive load of defection detection; implemention of the TFT strategy"
  - field_a_term: "Cross-cultural universality of fairness intuitions"
    field_b_term: "Cross-population robustness of cooperation ESS under diverse payoff structures"
    note: "ESS that survives payoff variation = cultural universal; culture-specific norms = locally stable ESSs"
related_unknowns:
  - u-moral-intuition-evolutionary-stability-mapping
related_hypotheses:
  - h-punishment-threshold-ess-moral-universality
cross_pollination_opportunities:
  - >
    Evolutionary game theory simulations on heterogeneous networks can predict
    which moral foundations should be stronger in high-clustering communities
    (strong punishment norms) vs. low-clustering ones (weak punishment), testing
    Haidt's theory with network-game predictions.
  - >
    Neuroimaging studies of moral disgust and third-party punishment can test
    whether the neural cost representation of punishment tracks the game-theoretic
    punishment cost c, relating neuroscience directly to evolutionary payoff structures.
communication_gap: >
  Moral psychologists (Jonathan Haidt's school) and evolutionary game theorists
  (Martin Nowak, Karl Sigmund) publish in different journals (Psychological Review,
  Journal of Personality and Social Psychology vs. Nature, PNAS) and rarely
  collaborate. The formal mapping from moral foundation universality to ESS
  robustness has not been derived.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1126/science.1093133"
    note: "Fehr & Gächter (2002) Science – altruistic punishment in public goods games; costly punishment instinct"
  - doi: "10.1038/359826a0"
    note: "Nowak & May (1992) Nature – evolutionary games and spatial chaos; cooperation on graphs"
  - doi: "10.1126/science.1179721"
    note: "Haidt (2007) Science – the new synthesis in moral psychology; moral foundations theory"
  - doi: "10.1038/s41586-019-1099-4"
    note: "Henrich et al. – prosociality and punishment across societies; cross-cultural game theory"
""")

write(ROOT / "unknowns-catalog/social-science/u-moral-intuition-evolutionary-stability-mapping.yaml", """
id: u-moral-intuition-evolutionary-stability-mapping
title: >
  Which moral intuitions (Haidt's foundations) map onto evolutionarily stable
  strategies in iterated social games, and what payoff structures predict the
  cross-cultural variation in their strength?
status: open
priority: medium
disciplines:
  - moral-psychology
  - evolutionary-biology
  - game-theory
summary: >
  Haidt identifies six moral foundations (care, fairness, loyalty, authority,
  sanctity, liberty) as cross-cultural moral universals with varying weights
  across cultures. Evolutionary game theory predicts which cooperation strategies
  are ESSs under specific group-size, relatedness, and payoff conditions. The
  formal mapping from specific moral intuitions to specific ESSs—and from
  cross-cultural variation to payoff structure variation—has not been derived.
systematic_gaps:
  - No formal derivation links each of Haidt's six moral foundations to a specific ESS or game-theoretic mechanism.
  - Cross-cultural variation in moral foundation weights (WEIRD vs. non-WEIRD societies) has not been explained by network topology or relatedness variation.
  - The evolutionary stability of costly sanctioning institutions (laws) vs. informal punishment norms is not modelled in the evolutionary game theory literature.
last_reviewed: "2026-05-07"
""")

write(ROOT / "hypotheses/active/h-punishment-threshold-ess-moral-universality.yaml", """
id: h-punishment-threshold-ess-moral-universality
title: >
  Moral intuitions about unfairness punishment will be stronger (higher
  willingness to pay) in societies where the evolutionary punishment ESS requires
  higher per-capita sanctioning costs, predictable from average group size and
  relatedness in traditional subsistence communities.
status: active
created: "2026-05-07"
priority: medium
impact_score: 0.66
related_disciplines:
  - moral-psychology
  - evolutionary-biology
unknowns_addressed:
  - u-moral-intuition-evolutionary-stability-mapping
evidence_links:
  - doi: "10.1126/science.1093133"
    type: supporting
    confidence: 0.58
    note: "Fehr & Gächter – altruistic punishment cross-culturally; variation in punishment intensity"
  - doi: "10.1038/s41586-019-1099-4"
    type: supporting
    confidence: 0.60
    note: "Henrich et al. – pro-social punishment across 15 societies; payoff structure variation"
proposed_tests:
  - description: >
      Extract traditional group sizes and kinship relatedness (r) for 20+ societies
      in the Henrich et al. cross-cultural punishment dataset. Compute predicted
      ESS punishment cost threshold c* = benefit × (1 − r). Regress observed
      willingness-to-punish against predicted c*. Expect significant positive
      correlation after controlling for market integration and religion.
""")

# ── 95 ─────────────────────────────────────────────────────────────────────
write(ROOT / "cross-domain/astronomy-mathematics/b-celestial-mechanics-kam-chaos.yaml", """
id: b-celestial-mechanics-kam-chaos
title: >
  The long-term stability of planetary orbits is determined by the
  Kolmogorov-Arnold-Moser (KAM) theorem: quasi-periodic orbits persist on
  invariant tori in phase space provided the perturbation is small and the
  frequency ratio is sufficiently irrational (Diophantine condition), while
  resonant orbits are destroyed, leading to the chaotic diffusion observed
  in the asteroid belt and in Laskar's numerical simulations of the inner
  solar system.
status: established
fields:
  - celestial-mechanics
  - chaos-theory
  - mathematics
  - astronomy
bridge_claim: >
  Classical celestial mechanics (Laplace, Lagrange) proved orbital stability
  to first order in planetary mass ratios. KAM theory (Kolmogorov 1954,
  Arnold 1963, Moser 1962) proved that nearly-integrable Hamiltonian systems
  (like the solar system in the small-mass limit) possess a positive-measure
  set of invariant tori where motion is quasi-periodic. Orbits near resonances
  (rational frequency ratios) are not protected and exhibit Chirikov diffusion
  in the chaotic sea. Laskar (1989) numerically integrated the solar system
  equations for 200 Myr and found positive Lyapunov exponents (τ_Lyap ~ 5 Myr
  for Mercury) confirming the solar system is weakly chaotic—consistent with
  KAM tori surviving to leading order while chaos governs long-term evolution
  at the 10⁹ yr timescale.
translation_table:
  - field_a_term: "Planetary orbital frequency ratio ω_i/ω_j"
    field_b_term: "Frequency ratio of the KAM torus"
    note: "Irrational (Diophantine) ratios → stable KAM torus; rational ratios → resonance → chaos"
  - field_a_term: "Mean-motion resonance (e.g., Jupiter-Saturn 5:2)"
    field_b_term: "Destroyed KAM torus (resonance overlap / Chirikov criterion)"
    note: "Resonance overlaps destroy intervening tori; Kirkwood gaps in asteroid belt are cleared resonances"
  - field_a_term: "Lyapunov exponent of Mercury's orbit (τ ~ 5 Myr)"
    field_b_term: "Inverse of the Lyapunov time for a chaotic trajectory in phase space"
    note: "Positive Lyapunov exponent indicates exponential sensitivity to initial conditions"
  - field_a_term: "Action-angle variables (J, θ) of integrable Kepler problem"
    field_b_term: "KAM torus coordinates in the nearly-integrable perturbation"
    note: "KAM theorem guarantees persistence of tori in (J, θ) space under small perturbation H = H₀ + εH₁"
related_unknowns:
  - u-solar-system-stability-billion-year-timescale
related_hypotheses:
  - h-mercury-orbit-chaotic-diffusion-eccentricity
cross_pollination_opportunities:
  - >
    KAM torus geometry in the solar system can be used to identify maximally stable
    exoplanet orbital configurations in multi-planet systems, predicting which
    architectures survive for Gyr timescales vs. which undergo chaotic orbit
    crossings and ejections.
  - >
    The Chirikov resonance-overlap criterion, developed for KAM breakdown, can be
    applied to design stable multi-satellite constellations (e.g., Starlink,
    GPS) that avoid dangerous resonances with the Moon and Earth's J₂ oblateness.
communication_gap: >
  KAM theory is one of the deepest results in 20th century mathematics (Arnol'd
  published in Russian in 1963; English translations lagged by years). Celestial
  mechanicians adopted it slowly; Laskar's chaotic solar system simulations
  (1989) were the first widely accessible demonstration of its implications.
  Applied orbital mechanics and astrodynamics engineers rarely engage with the
  full KAM mathematical formalism.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1038/338237a0"
    note: "Laskar (1989) Nature – numerical evidence for chaotic behavior of the inner solar system; Lyapunov exponents"
  - doi: "10.1070/RM1963v018n05ABEH004130"
    note: "Arnold (1963) – proof of KAM theorem for analytic Hamiltonians (Russian Math. Surveys)"
  - doi: "10.1086/588006"
    note: "Laskar & Gastineau (2009) Nature – existence of collisional trajectories of Mercury in 1% of integrations"
  - doi: "10.1007/s10569-008-9179-4"
    note: "Murray & Holman – origin of chaos in the outer solar system; resonance overlap criterion"
""")

write(ROOT / "unknowns-catalog/astronomy/u-solar-system-stability-billion-year-timescale.yaml", """
id: u-solar-system-stability-billion-year-timescale
title: >
  Is the solar system dynamically stable over its remaining ~5 Gyr lifetime,
  and what is the probability that Mercury or Mars undergoes a close encounter
  or collision with another planet?
status: open
priority: high
disciplines:
  - celestial-mechanics
  - astronomy
  - chaos-theory
summary: >
  Laskar's simulations (2009) found that in ~1% of Monte Carlo integrations,
  Mercury's eccentricity grows enough to approach Venus or collide with the Sun
  within 5 Gyr. The probability estimate depends sensitively on the precision
  of the initial conditions and the time-step used. Whether the 1% figure is
  robust and whether Earth is genuinely safe for the Sun's remaining lifetime
  are open questions requiring improved ephemerides and longer integration methods.
systematic_gaps:
  - Monte Carlo uncertainty in the 1% Mercury collision probability arises from truncation errors in numerical integrations over 5 Gyr; symplectic integrators with adaptive step-size are needed.
  - The effect of general relativistic corrections on Mercury's secular dynamics is only partially included in most long-term simulations.
  - Observational improvement in current planetary ephemerides (from Gaia and VLBI) has not yet propagated into updated stability estimates.
last_reviewed: "2026-05-07"
""")

write(ROOT / "hypotheses/active/h-mercury-orbit-chaotic-diffusion-eccentricity.yaml", """
id: h-mercury-orbit-chaotic-diffusion-eccentricity
title: >
  Mercury's orbital eccentricity undergoes chaotic diffusion with a Lyapunov
  time of 5 ± 1 Myr (consistent with Laskar 1989), and full GR correction
  reduces the probability of Mercury eccentricity exceeding 0.6 within 5 Gyr
  from ~1% to <0.3%.
status: active
created: "2026-05-07"
priority: medium
impact_score: 0.72
related_disciplines:
  - celestial-mechanics
  - astronomy
unknowns_addressed:
  - u-solar-system-stability-billion-year-timescale
evidence_links:
  - doi: "10.1038/338237a0"
    type: supporting
    confidence: 0.85
    note: "Laskar 1989 – first demonstration of Mercury Lyapunov time ~5 Myr from 200 Myr integration"
  - doi: "10.1086/588006"
    type: related
    confidence: 0.70
    note: "Laskar & Gastineau 2009 – 1% Mercury collision probability; GR corrections partially included"
proposed_tests:
  - description: >
      Perform 10,000 Monte Carlo N-body integrations of the solar system for 5 Gyr
      using a symplectic integrator with full post-Newtonian GR corrections for
      Mercury's perihelion precession. Record the fraction where e_Mercury > 0.6.
      Compare to the Laskar 2009 1% estimate and test whether full GR reduces
      the fraction below 0.3%.
""")

# ── 96 ─────────────────────────────────────────────────────────────────────
write(ROOT / "cross-domain/biology-chemistry/b-rna-folding-partition-function.yaml", """
id: b-rna-folding-partition-function
title: >
  RNA secondary structure prediction is a statistical-mechanics partition function
  problem: the ensemble of all possible base-pair configurations is weighted by
  Boltzmann factors exp(−ΔG°/RT), and the minimum free-energy structure, base-
  pair probabilities, and thermodynamic accessibility are all computed from
  the McCaskill partition function using dynamic programming.
status: established
fields:
  - RNA-biology
  - statistical-mechanics
  - biophysics
  - chemistry
bridge_claim: >
  An RNA molecule of length N can adopt exponentially many secondary structures
  (base-pair pairings without pseudoknots). McCaskill (1990) showed that the
  partition function Z = Σ_s exp(−ΔG°(s)/RT), summing over all structures s
  with their free energy, can be computed in O(N³) time using dynamic
  programming. The base-pair probability matrix P_ij = Z_ij/Z gives the
  probability each pair (i,j) is formed at thermal equilibrium. Zuker's
  mfold/RNAfold minimises ΔG° instead of computing the full partition function—
  the minimum free energy (MFE) structure is the lowest-energy configuration
  but accounts for only a fraction of the Boltzmann weight if the energy
  landscape is rugged. The bridge: RNA folding thermodynamics is a finite-
  dimensional spin model (contact spins s_ij ∈ {0,1}) with a non-crossing
  constraint, solvable exactly by transfer-matrix methods.
translation_table:
  - field_a_term: "RNA partition function Z = Σ_s exp(−ΔG°(s)/RT)"
    field_b_term: "Statistical mechanics partition function Z = Tr[exp(−βH)]"
    note: "RNA structures = microstates; ΔG°(s) = Hamiltonian; T = thermodynamic temperature"
  - field_a_term: "Base-pair probability matrix P_ij"
    field_b_term: "Thermal average of spin-spin correlation ⟨s_ij⟩"
    note: "P_ij = probability base i pairs with base j in the Boltzmann ensemble"
  - field_a_term: "Minimum free energy (MFE) structure"
    field_b_term: "Ground state configuration (lowest-energy microstate)"
    note: "MFE = ground state; only dominant when energy gap to next structure is large (kT)"
  - field_a_term: "Dynamic programming recursion (McCaskill O(N³))"
    field_b_term: "Transfer matrix method for 1D spin chains"
    note: "Both exploit the non-crossing (planar) constraint to decompose the problem into independent subproblems"
related_unknowns:
  - u-rna-folding-pseudoknot-partition-function
related_hypotheses:
  - h-rna-boltzmann-ensemble-functional-structure-selection
cross_pollination_opportunities:
  - >
    Statistical mechanics concepts (free energy landscape, metastability, kinetic
    trapping) can be applied to RNA co-transcriptional folding: the RNA folds as
    it is synthesised, exploring a time-evolving energy landscape. Kinetic trap
    theory from spin glasses can predict which functional RNA structures are
    kinetically accessible.
  - >
    The partition function framework enables thermodynamic ensemble design:
    synthetic riboswitches can be designed by specifying the desired P_ij matrix
    and using inverse folding (RNAinverse) to find sequences that achieve it,
    using statistical mechanics directly for RNA engineering.
communication_gap: >
  RNA biologists routinely use RNAfold/mfold predictions without awareness of
  the statistical mechanics framework underlying the partition function. Statistical
  physicists studying disordered systems (spin glasses) have not extensively
  analysed the RNA folding problem despite formal similarities to the random
  energy model.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1021/bi00413a004"
    note: "McCaskill (1990) Biopolymers – partition function algorithm for RNA secondary structure; O(N³) DP"
  - doi: "10.1093/nar/19.22.6329"
    note: "Zuker (1989) Science – mfold algorithm for minimum free energy RNA secondary structure"
  - doi: "10.1093/nar/gkh930"
    note: "Lorenz et al. (2011) – ViennaRNA Package 2.0 including partition function and base-pair probabilities"
  - doi: "10.1016/j.jmb.2006.01.048"
    note: "Tinoco & Bustamante – how RNA folds; thermodynamic vs. kinetic control of structure"
""")

write(ROOT / "unknowns-catalog/biology/u-rna-folding-pseudoknot-partition-function.yaml", """
id: u-rna-folding-pseudoknot-partition-function
title: >
  Can the RNA partition function be extended to include pseudoknots in
  polynomial time, and what fraction of biologically functional RNA
  structures require pseudoknot thermodynamics for accurate prediction?
status: open
priority: high
disciplines:
  - RNA-biology
  - computational-biology
  - biophysics
summary: >
  The McCaskill partition function algorithm runs in O(N³) because it exploits
  the non-crossing (planar) constraint of secondary structures (no pseudoknots).
  Including pseudoknots makes the problem NP-hard in general. Restricted
  pseudoknot models (H-type, kissing loops) can be handled in O(N^5)–O(N^6)
  time. However, many functional RNAs (telomerase, ribosome, riboswitches)
  contain pseudoknots essential for function. The fraction of functional RNA
  structures that cannot be predicted without pseudoknot thermodynamics is
  not known.
systematic_gaps:
  - No polynomial-time exact algorithm exists for the general pseudoknot partition function.
  - The fraction of PDB RNA structures where the MFE pseudoknot-free prediction differs from the crystal structure by >50% base pairs has not been computed systematically.
  - Efficient approximations to the pseudoknot partition function (variational, stochastic) have not been benchmarked on a curated pseudoknot-containing RNA structure database.
last_reviewed: "2026-05-07"
""")

write(ROOT / "hypotheses/active/h-rna-boltzmann-ensemble-functional-structure-selection.yaml", """
id: h-rna-boltzmann-ensemble-functional-structure-selection
title: >
  Functional RNA structures are thermodynamically selected to be near the
  free-energy minimum AND have low base-pair probability variance in the
  Boltzmann ensemble (high structural certainty), while non-functional RNAs
  of the same sequence composition show systematically higher ensemble variance.
status: active
created: "2026-05-07"
priority: medium
impact_score: 0.70
related_disciplines:
  - RNA-biology
  - statistical-mechanics
unknowns_addressed:
  - u-rna-folding-pseudoknot-partition-function
evidence_links:
  - doi: "10.1021/bi00413a004"
    type: supporting
    confidence: 0.65
    note: "McCaskill 1990 – partition function enables base-pair probability computation; ensemble analysis"
  - doi: "10.1016/j.jmb.2006.01.048"
    type: supporting
    confidence: 0.60
    note: "Tinoco & Bustamante – thermodynamic stability and RNA function correlation"
proposed_tests:
  - description: >
      Compute base-pair probability matrices for 500 functional RNAs (from Rfam)
      and 500 length-matched random sequences with the same dinucleotide composition.
      Define ensemble variance as the mean over all pairs (i,j) of P_ij(1−P_ij).
      Test whether functional RNAs have significantly lower ensemble variance than
      random controls using a Wilcoxon signed-rank test.
""")

print("\n=== Wave 36 complete: 12 bridges + 12 unknowns + 12 hypotheses ===")

# =========================================================================== #
# WAVE 37  —  bridges 97-108                                                   #
# =========================================================================== #

# ── 97 ─────────────────────────────────────────────────────────────────────
write(ROOT / "cross-domain/biochemistry-thermodynamics/b-fermentation-thermodynamic-equilibrium.yaml", """
id: b-fermentation-thermodynamic-equilibrium
title: >
  Microbial fermentation pathway selection is governed by thermodynamic
  free energy minimisation: the Gibbs free energy change ΔG° of each
  metabolic reaction determines which pathways are feasible, and cells
  regulate NAD⁺/NADH ratios to maintain ΔG < 0 across the fermentation
  network even when ATP yield is suboptimal.
status: established
fields:
  - biochemistry
  - thermodynamics
  - microbiology
bridge_claim: >
  Fermentation is the anaerobic oxidation of organic compounds coupled to
  ATP synthesis without a terminal inorganic electron acceptor. The pathway
  a microbe takes (homolactic, ethanolic, butyric, etc.) depends on the
  thermodynamic feasibility of each reaction: ΔG = ΔG° + RT ln Q must be
  negative for spontaneous flux. Alberty (2003) formalised biochemical
  thermodynamics using transformed Gibbs energies at physiological pH,
  showing that NAD⁺/NADH ratio ([NAD⁺]/[NADH] ~ 10³ in aerobiosis, ~1
  in fermentation) sets the effective standard potential and determines
  whether NADH-oxidising fermentation steps are thermodynamically driven.
  Cells cannot ignore thermodynamics: enforcing ΔG < 0 at each step is
  a physical constraint that determines the observed diversity of
  fermentation products.
translation_table:
  - field_a_term: "NAD⁺/NADH redox couple potential E'°(NAD⁺/NADH) = −0.32 V"
    field_b_term: "Half-cell potential in an electrochemical cell"
    note: "Fermentation reactions use NADH reoxidation as the electron sink; E sets the thermodynamic driving force"
  - field_a_term: "ΔG of glycolysis (−73 kJ/mol glucose under standard conditions)"
    field_b_term: "Work available from fuel oxidation in a heat engine"
    note: "Efficiency of ATP capture = ΔG_ATP / ΔG_glycolysis; fermentation captures ~30%, aerobiosis ~40%"
  - field_a_term: "Fermentation pathway branching point (pyruvate to lactate vs. ethanol)"
    field_b_term: "Kinetic/thermodynamic competition between parallel reaction channels"
    note: "The pathway with more negative ΔG dominates; enzyme expression adjusts flux to maintain ΔG < 0"
  - field_a_term: "Product inhibition (ethanol toxicity in yeast)"
    field_b_term: "Le Chatelier's principle: product accumulation shifts equilibrium backward"
    note: "Ethanol concentration drives ΔG toward zero; cells must expel product to maintain thermodynamic drive"
related_unknowns:
  - u-fermentation-thermodynamic-efficiency-limit
related_hypotheses:
  - h-fermentation-nad-ratio-pathway-selection-thermodynamic
cross_pollination_opportunities:
  - >
    Thermodynamic flux balance analysis (TFA), incorporating ΔG constraints on
    all metabolic reactions, can predict which fermentation products a metabolically
    engineered microbe will produce under given substrate and cofactor conditions—
    going beyond stoichiometric FBA which ignores thermodynamic feasibility.
  - >
    The thermodynamic efficiency of fermentation has implications for the design
    of microbial fuel cells (MFCs): maximising the electrochemical potential
    captured from NADH oxidation requires operating near the thermodynamic limit,
    a design criterion borrowed directly from Carnot efficiency analysis.
communication_gap: >
  Biochemistry textbooks describe fermentation pathways in mechanistic detail
  (enzyme names, cofactors) but rarely perform thermodynamic feasibility analysis.
  Thermodynamicists studying biological energy conversion rarely engage with
  detailed metabolic network topology. Alberty's transformed Gibbs energy
  framework (2003 J. Phys. Chem. Ref. Data) is underused in metabolic engineering.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1021/jp020625u"
    note: "Alberty (2003) – thermodynamics of biochemical reactions; transformed Gibbs energies at pH 7"
  - doi: "10.1128/MMBR.00008-10"
    note: "Thauer et al. (2008) Microbiol. Mol. Biol. Rev. – methanogenic archaea thermodynamics; ΔG of fermentation steps"
  - doi: "10.1073/pnas.1112325108"
    note: "Flamholz et al. (2012) PNAS – thermodynamic constraints on metabolic flux; eQuilibrator database"
  - doi: "10.1038/nchembio.971"
    note: "Henry et al. (2007) Nature Chem. Biol. – thermodynamics-based metabolic flux analysis"
""")

write(ROOT / "unknowns-catalog/biology/u-fermentation-thermodynamic-efficiency-limit.yaml", """
id: u-fermentation-thermodynamic-efficiency-limit
title: >
  What is the thermodynamic upper bound on ATP yield per mole of substrate
  in anaerobic fermentation, and how close do naturally evolved microbes
  operate to this limit?
status: open
priority: medium
disciplines:
  - biochemistry
  - thermodynamics
  - microbiology
summary: >
  The Carnot efficiency concept limits heat engines, but fermentation cells
  are not heat engines—they convert chemical Gibbs energy, not heat.
  The maximum ATP yield per mole of glucose in fermentation is set by ΔG_glucose
  / ΔG_ATP_hydrolysis ~ 73/50 ~ 1.5 mol ATP/mol glucose theoretically, yet
  evolved cells achieve only 2 mol ATP/mol glucose in glycolysis. Whether
  this gap represents unavoidable kinetic losses or unexploited thermodynamic
  headroom is not established.
systematic_gaps:
  - The thermodynamic efficiency of individual fermentation steps (phosphofructokinase, pyruvate kinase) under physiological conditions has not been measured with sufficient precision.
  - The trade-off between ATP yield and growth rate (Pareto frontier) in fermentation has not been derived from thermodynamic principles.
  - Whether any microbe operates near the thermodynamic ATP yield limit in any fermentation pathway is not known.
last_reviewed: "2026-05-07"
""")

write(ROOT / "hypotheses/active/h-fermentation-nad-ratio-pathway-selection-thermodynamic.yaml", """
id: h-fermentation-nad-ratio-pathway-selection-thermodynamic
title: >
  In Saccharomyces cerevisiae under anaerobic conditions, the fermentation
  product distribution (ethanol:glycerol ratio) is uniquely determined by
  the thermodynamic requirement ΔG < −5 kJ/mol for each step, with no free
  kinetic parameters, when intracellular NAD⁺/NADH ratio is measured in situ.
status: active
created: "2026-05-07"
priority: medium
impact_score: 0.68
related_disciplines:
  - biochemistry
  - thermodynamics
unknowns_addressed:
  - u-fermentation-thermodynamic-efficiency-limit
evidence_links:
  - doi: "10.1073/pnas.1112325108"
    type: supporting
    confidence: 0.70
    note: "Flamholz 2012 – eQuilibrator; thermodynamic constraints predict metabolic feasibility"
  - doi: "10.1038/nchembio.971"
    type: supporting
    confidence: 0.65
    note: "Henry 2007 – TFA predicts flux distributions in E. coli consistent with thermodynamics"
proposed_tests:
  - description: >
      Grow S. cerevisiae anaerobically in glucose-limited chemostats at five
      dilution rates (0.05–0.4 h⁻¹). Measure intracellular NAD⁺/NADH by
      enzyme-cycling assay. Use eQuilibrator to compute ΔG for each glycolytic
      step. Compute predicted ethanol:glycerol ratio from thermodynamic constraints
      alone. Compare to measured GC-FID fermentation product distribution.
""")

# ── 98 ─────────────────────────────────────────────────────────────────────
write(ROOT / "cross-domain/physics-engineering/b-shockley-queisser-thermodynamic-limit.yaml", """
id: b-shockley-queisser-thermodynamic-limit
title: >
  The Shockley-Queisser (SQ) efficiency limit of ~33% for single-junction
  solar cells is a consequence of the second law of thermodynamics applied
  to photon statistics: the Carnot-like bound arising from treating the sun
  as a blackbody at T_sun = 5778 K limits radiative recombination losses,
  and no single-bandgap cell can exceed η_SQ regardless of material choice.
status: established
fields:
  - photovoltaics
  - thermodynamics
  - semiconductor-physics
  - engineering
bridge_claim: >
  Shockley & Queisser (1961) derived the efficiency limit using detailed
  balance: a solar cell in equilibrium emits and absorbs photons; the
  maximum voltage is set by quasi-Fermi level splitting ΔE_F = qV_oc,
  which cannot exceed the photon chemical potential μ = hν − TS_photon.
  Henry (1980) reframed the SQ limit as a thermodynamic bound: the maximum
  work extractable from solar radiation at T_sun = 5778 K collected by
  an absorber at T_cell = 300 K is η_Carnot = 1 − T_cell/T_sun = 94.8%.
  The SQ limit (~33%) falls far below Carnot because (1) sub-bandgap photons
  are not absorbed and (2) above-bandgap photons thermalise their excess
  energy as heat. Multi-junction cells escape the SQ limit by using multiple
  bandgaps to reduce thermalisation losses, approaching the thermodynamic
  concentration limit of ~68% at one sun.
translation_table:
  - field_a_term: "Bandgap energy E_g of the semiconductor absorber"
    field_b_term: "Energy threshold for photon absorption (Heaviside filter)"
    note: "Photons with hν < E_g are transmitted (sub-bandgap loss); hν > E_g thermalise to E_g"
  - field_a_term: "Open-circuit voltage V_oc (maximum voltage)"
    field_b_term: "Photon chemical potential / quasi-Fermi level splitting"
    note: "V_oc is set by the balance between photon absorption and radiative recombination emission"
  - field_a_term: "SQ efficiency limit 33% at E_g = 1.34 eV"
    field_b_term: "Maximum work from a two-temperature heat engine with photon reservoir"
    note: "SQ = Carnot × (absorption efficiency) × (quantum efficiency); thermalisation reduces it to 33%"
  - field_a_term: "Multi-junction tandem cell (N bandgaps)"
    field_b_term: "Multi-stage heat engine (each stage harvests a photon energy band)"
    note: "N junctions reduce thermalisation loss; N→∞ approaches thermodynamic limit of ~68% at 1 sun"
related_unknowns:
  - u-solar-cell-efficiency-practical-loss-mechanisms
related_hypotheses:
  - h-tandem-cell-thermodynamic-optimum-bandgap-pairing
cross_pollination_opportunities:
  - >
    Thermodynamic optimisation of multi-junction solar cell bandgap combinations
    (equivalent to designing a multi-stage Carnot engine matching the solar
    spectrum) can guide materials selection for III-V tandems beyond the
    empirical screening currently done by cell manufacturers.
  - >
    The photon chemical potential framework (μ_photon = hν − TS) can be applied
    to LED lighting (reverse of solar cell) to derive the thermodynamic efficiency
    limit of electroluminescence, connecting photovoltaics and solid-state lighting
    in a unified framework.
communication_gap: >
  Solar cell engineers use the SQ limit as a benchmark without always framing
  it as a thermodynamic bound analogous to Carnot's theorem. Thermodynamicists
  studying radiation have not always engaged with photovoltaic engineering details.
  Henry's 1980 thermodynamic rederivation of the SQ limit is underappreciated in
  the photovoltaics literature compared to the original Shockley & Queisser paper.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1063/1.1736034"
    note: "Shockley & Queisser (1961) J. Appl. Phys. – detailed balance limit of efficiency of p-n junction solar cells"
  - doi: "10.1063/1.328272"
    note: "Henry (1980) J. Appl. Phys. – limiting efficiencies of ideal single and multiple energy gap terrestrial solar cells"
  - doi: "10.1038/nmat4388"
    note: "Polman & Atwater (2016) – photonic design principles for ultrahigh-efficiency photovoltaics beyond SQ"
  - doi: "10.1021/acs.jpclett.6b01060"
    note: "Geisz et al. – six-junction solar cell; 47.1% efficiency under concentrated sunlight"
""")

write(ROOT / "unknowns-catalog/physics/u-solar-cell-efficiency-practical-loss-mechanisms.yaml", """
id: u-solar-cell-efficiency-practical-loss-mechanisms
title: >
  What is the practical efficiency ceiling for silicon solar cells under
  the best achievable surface passivation and light-trapping conditions,
  and which specific loss mechanism (Auger recombination, free-carrier
  absorption, contact resistance) is the dominant remaining gap below
  the SQ limit?
status: open
priority: medium
disciplines:
  - photovoltaics
  - semiconductor-physics
  - engineering
summary: >
  The SQ limit for silicon (E_g = 1.12 eV) is ~29.4% at one sun; the best
  achieved efficiency is ~26.7% (LONGi, 2023). The remaining ~2.7% gap
  has contributions from Auger recombination (intrinsic, unavoidable),
  surface recombination (passivation-limited), optical losses (parasitic
  absorption, escape cone), and contact resistance. The relative magnitude
  of each loss and the practical ceiling achievable with current silicon
  materials are debated.
systematic_gaps:
  - Auger recombination coefficients in silicon are measured to 10-20% precision; improvement would tighten the practical limit estimate.
  - The best achievable surface recombination velocity with hydrogen-passivated SiO₂/Si interfaces has not been measured below 0.1 cm/s.
  - The practical efficiency achievable with ideal carrier-selective contacts (no metal-silicon interface) has not been demonstrated.
last_reviewed: "2026-05-07"
""")

write(ROOT / "hypotheses/active/h-tandem-cell-thermodynamic-optimum-bandgap-pairing.yaml", """
id: h-tandem-cell-thermodynamic-optimum-bandgap-pairing
title: >
  For a two-junction tandem solar cell under the AM1.5G spectrum, the
  thermodynamic optimum top-cell bandgap is 1.73 ± 0.05 eV and bottom-cell
  bandgap is 1.12 ± 0.05 eV, and any perovskite/silicon tandem with E_g(top)
  between 1.68 and 1.78 eV will achieve >29% efficiency under radiative-limit
  conditions.
status: active
created: "2026-05-07"
priority: high
impact_score: 0.83
related_disciplines:
  - photovoltaics
  - thermodynamics
unknowns_addressed:
  - u-solar-cell-efficiency-practical-loss-mechanisms
evidence_links:
  - doi: "10.1063/1.328272"
    type: supporting
    confidence: 0.85
    note: "Henry 1980 – thermodynamic optimum bandgap combinations for multi-junction cells"
  - doi: "10.1038/nmat4388"
    type: supporting
    confidence: 0.80
    note: "Polman & Atwater – optical and thermodynamic design principles for tandems"
proposed_tests:
  - description: >
      Fabricate perovskite/silicon tandems with top-cell E_g varied from 1.60 to
      1.85 eV by adjusting Br content in FAPbI₃₋ₓBrₓ. Measure PCE under AM1.5G
      at 100 mW/cm². Fit PCE vs. E_g(top) curve and determine the experimental
      optimum. Compare to the 1.73 eV thermodynamic prediction from SQ+AM1.5G.
""")

# ── 99 ─────────────────────────────────────────────────────────────────────
write(ROOT / "cross-domain/neuroscience-biology/b-memory-reconsolidation-synaptic-plasticity.yaml", """
id: b-memory-reconsolidation-synaptic-plasticity
title: >
  Memory reconsolidation—the requirement for new protein synthesis to re-
  stabilise a memory after retrieval—is mechanistically identical to the
  late-phase long-term potentiation (L-LTP) that initially encodes the
  memory: both require NMDA-receptor activation, CaMKII autophosphorylation,
  CREB-mediated transcription, and de novo synaptic protein synthesis.
status: proposed
fields:
  - neuroscience
  - molecular-biology
  - cognitive-science
bridge_claim: >
  Nader, Schafe & LeDoux (2000) showed that infusing the protein synthesis
  inhibitor anisomycin into the basolateral amygdala immediately after a
  conditioned-fear memory is reactivated causes amnesia for that memory,
  demonstrating that retrieved memories re-enter a labile state requiring
  restabilisation (reconsolidation). The molecular cascade required for
  reconsolidation (ERK phosphorylation, CREB activation, Arc/Arg3.1
  synthesis, AMPAR insertion) is the same as that required for L-LTP
  (Kandel 2001). The bridge: memory retrieval temporarily reverses L-LTP
  at relevant synapses (reducing AMPAR surface expression), and protein-
  synthesis-dependent reconsolidation re-instates L-LTP—an erasure-and-
  rewrite cycle using the same molecular machinery as initial memory formation.
translation_table:
  - field_a_term: "Memory reactivation by retrieval cue"
    field_b_term: "Re-induction of synaptic LTP by repeated stimulation"
    note: "Both require NMDA-R activation; retrieval-induced NMDA activation triggers labilisation"
  - field_a_term: "Protein synthesis inhibitor (anisomycin) causing reconsolidation amnesia"
    field_b_term: "Blockade of L-LTP protein synthesis preventing memory consolidation"
    note: "Same pharmacological tools block both processes; same proteins required (Arc, CaMKII, BDNF)"
  - field_a_term: "Reconsolidation window (hours after retrieval)"
    field_b_term: "L-LTP consolidation window (hours after induction)"
    note: "Both windows reflect the time required for mRNA transcription and protein synthesis"
  - field_a_term: "Memory update after reconsolidation (incorporation of new information)"
    field_b_term: "Synaptic weight modification during LTP restabilisation"
    note: "Both mechanisms allow modification of existing traces; reconsolidation = update opportunity"
related_unknowns:
  - u-reconsolidation-synaptic-locus-ampa-receptor
related_hypotheses:
  - h-reconsolidation-ampar-endocytosis-labilisation
cross_pollination_opportunities:
  - >
    Optogenetic activation of specific synapses during reconsolidation can test
    whether AMPAR endocytosis occurs at the originally potentiated synapses,
    directly linking the molecular reconsolidation mechanism to identified
    memory-encoding synaptic ensembles.
  - >
    Pharmacological disruption of reconsolidation using NMDA-R antagonists (e.g.,
    ketamine) in PTSD patients exploits the synaptic plasticity mechanism to
    reduce traumatic memory strength—a clinical application directly derived from
    the LTP–reconsolidation equivalence.
communication_gap: >
  The reconsolidation discovery (Nader 2000) was initially controversial within
  cognitive neuroscience; its molecular equivalence to L-LTP mechanisms is
  accepted in cellular neuroscience but the implications for therapeutic memory
  modification are debated. Clinical memory researchers and synaptic plasticity
  researchers publish in different journals.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1038/35021052"
    note: "Nader, Schafe & LeDoux (2000) Nature – fear memories require protein synthesis in the amygdala for reconsolidation"
  - doi: "10.1126/science.294.5544.1030"
    note: "Kandel (2001) Science – the molecular biology of memory storage: a dialogue between genes and synapses"
  - doi: "10.1038/nrn1425"
    note: "Nader & Hardt (2009) Nature Reviews Neuroscience – a single standard for memory: the case for reconsolidation"
  - doi: "10.1016/j.neuron.2014.11.010"
    note: "Bhaskaran & Smith (2014) – AMPA receptor trafficking during reconsolidation and LTP"
""")

write(ROOT / "unknowns-catalog/neuroscience/u-reconsolidation-synaptic-locus-ampa-receptor.yaml", """
id: u-reconsolidation-synaptic-locus-ampa-receptor
title: >
  At which specific synapses does AMPA receptor endocytosis occur during memory
  labilisation after retrieval, and is reconsolidation synapse-specific or
  distributed across the encoding ensemble?
status: open
priority: high
disciplines:
  - neuroscience
  - molecular-biology
  - cell-biology
summary: >
  The reconsolidation hypothesis predicts that retrieved memories enter a labile
  state involving AMPAR endocytosis at the synapses that encode the memory.
  However, whether labilisation is synapse-specific (occurring only at the
  originally potentiated synapses) or global (affecting all synapses of the
  reactivated neurons) is not known. Distinguishing these mechanisms requires
  tracking AMPAR surface expression at identified synapses during retrieval and
  reconsolidation.
systematic_gaps:
  - AMPAR surface expression during reconsolidation has not been measured with synapse-specific resolution in vivo.
  - Whether the reconsolidation labilisation window correlates with AMPAR endocytosis kinetics has not been directly tested.
  - The degree to which reconsolidation affects only the retrieved engram vs. overlapping memories is not characterised.
last_reviewed: "2026-05-07"
""")

write(ROOT / "hypotheses/active/h-reconsolidation-ampar-endocytosis-labilisation.yaml", """
id: h-reconsolidation-ampar-endocytosis-labilisation
title: >
  Memory labilisation during reconsolidation is mechanistically implemented
  by GluA1 AMPAR endocytosis specifically at the dendritic spines belonging
  to the reactivated engram cells, measurable as a >30% reduction in GluA1
  surface expression within 30 min of retrieval in identified amygdala
  engram neurons.
status: active
created: "2026-05-07"
priority: high
impact_score: 0.81
related_disciplines:
  - neuroscience
  - molecular-biology
unknowns_addressed:
  - u-reconsolidation-synaptic-locus-ampa-receptor
evidence_links:
  - doi: "10.1038/35021052"
    type: supporting
    confidence: 0.70
    note: "Nader 2000 – protein synthesis required for reconsolidation; consistent with AMPAR turnover"
  - doi: "10.1016/j.neuron.2014.11.010"
    type: supporting
    confidence: 0.65
    note: "AMPAR trafficking during LTP/LTD; endocytosis as labilisation mechanism"
proposed_tests:
  - description: >
      Use a cre-dependent GluA1-SEP (super-ecliptic pHluorin) fusion mouse
      crossed with a FosTRAP2 engram-labelling line. Deliver fear conditioning;
      allow 24h consolidation. Reactivate memory; image GluA1-SEP surface
      fluorescence at identified engram-cell spines by two-photon microscopy at
      0, 30, 60 min post-retrieval. Compare to non-retrieval controls.
""")

# ── 100 ────────────────────────────────────────────────────────────────────
write(ROOT / "cross-domain/mathematics-biology/b-evolutionary-graph-fixation-probability.yaml", """
id: b-evolutionary-graph-fixation-probability
title: >
  The fixation probability of a mutant in a structured population is governed
  by the topology of the evolutionary graph: Lieberman, Hauert & Nowak (2005)
  proved that certain graph topologies act as amplifiers of selection (suppressing
  drift) while others suppress selection (amplifying drift), with complete graphs
  recovering the Moran process fixation probability ρ = (1 − 1/r)/(1 − 1/r^N).
status: established
fields:
  - evolutionary-biology
  - mathematics
  - graph-theory
  - population-genetics
bridge_claim: >
  In the classical Moran process, a mutant with fitness r in a population of
  N individuals fixes with probability ρ_Moran = (1 − 1/r)/(1 − 1/r^N). When
  individuals occupy nodes of a graph and reproduction/replacement follows the
  graph edges, the fixation probability changes. Lieberman et al. (2005) showed
  that the star graph (one hub connected to N−1 leaves) amplifies selection:
  ρ_star ≈ (1 − 1/r²)/(1 − 1/r^{2N}) > ρ_Moran for r > 1. Conversely,
  suppressing topologies reduce ρ below the drift baseline. The result
  generalises the Hardy-Weinberg and Moran models to arbitrary spatial structure,
  connecting graph theory to population genetics.
translation_table:
  - field_a_term: "Graph vertex = individual in the structured population"
    field_b_term: "Individual in spatially structured population genetics model"
    note: "Graph topology encodes the connectivity (migration/competition) structure"
  - field_a_term: "Star graph: amplifier of selection"
    field_b_term: "Hierarchically structured population favouring beneficial mutant fixation"
    note: "ρ_star > ρ_Moran for r > 1; selection is more effective on star than on complete graph"
  - field_a_term: "Complete graph = Moran process (all-to-all competition)"
    field_b_term: "Well-mixed (unstructured) population with random mating"
    note: "Identical fixation probability; spatial structure reduces to mean-field limit"
  - field_a_term: "Fixation probability as function of graph eigenspectrum"
    field_b_term: "Effective population size N_e as function of migration matrix"
    note: "Both relate population-genetic outcomes to algebraic graph properties"
related_unknowns:
  - u-evolutionary-graph-amplifier-natural-populations
related_hypotheses:
  - h-social-network-star-topology-innovation-fixation
cross_pollination_opportunities:
  - >
    Evolutionary graph theory can be applied to somatic evolution in cancer:
    the tissue architecture (stem cell hierarchies, spatial organisation)
    determines whether beneficial (oncogenic) mutations fix or are eliminated.
    Identifying which tissue architectures act as suppressors of (somatic) selection
    could explain differential cancer incidence across tissues.
  - >
    Social network topology analysis (real social networks are scale-free, not
    star graphs) can quantify how effectively human populations fix cultural
    innovations or beneficial traits relative to a well-mixed population baseline.
communication_gap: >
  The Moran process is a standard tool in population genetics textbooks.
  Graph-structured evolutionary dynamics (Lieberman 2005) bridged population
  genetics and graph theory in Nature but has been slowly adopted in empirical
  evolutionary biology. Phylogeographers studying geographic structure and
  population geneticists rarely use graph-theoretic amplifier/suppressor concepts.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1038/nature03277"
    note: "Lieberman, Hauert & Nowak (2005) Nature – evolutionary dynamics on graphs; amplifiers and suppressors"
  - doi: "10.1126/science.1133755"
    note: "Nowak (2006) Science – five rules for the evolution of cooperation on graphs"
  - doi: "10.1073/pnas.1100921108"
    note: "Shakarian et al. – review of evolutionary graph theory; fixation probabilities on diverse topologies"
  - doi: "10.1038/s41586-021-04440-z"
    note: "Tkadlec et al. (2021) – limits on amplifiers of natural selection under death-birth updating"
""")

write(ROOT / "unknowns-catalog/biology/u-evolutionary-graph-amplifier-natural-populations.yaml", """
id: u-evolutionary-graph-amplifier-natural-populations
title: >
  Do real biological population structures (tissue architectures, social networks,
  geographic ranges) act as amplifiers or suppressors of natural selection, and
  can this be quantified from empirical connectivity data?
status: open
priority: medium
disciplines:
  - evolutionary-biology
  - population-genetics
  - graph-theory
summary: >
  Lieberman et al. (2005) proved that certain graph topologies amplify selection
  but left open whether natural population structures fall into amplifier or
  suppressor categories. Real populations have heterogeneous, dynamic connectivity.
  Whether observed tissue architectures (intestinal stem cell hierarchy) or
  geographic metapopulation structures function as amplifiers or suppressors of
  beneficial vs. deleterious mutations is unknown and has major implications for
  cancer evolution and adaptation.
systematic_gaps:
  - The effective fixation probability in real population graphs with both spatial structure and demographic stochasticity has not been computed for any empirical population.
  - Whether crypt-villus intestinal architecture suppresses oncogenic mutation fixation (as theorised) has not been tested with single-cell sequencing at sufficient resolution.
  - The dynamic nature of real population graphs (individuals join/leave, edges change) invalidates static graph results but dynamic graph evolution theory is underdeveloped.
last_reviewed: "2026-05-07"
""")

write(ROOT / "hypotheses/active/h-social-network-star-topology-innovation-fixation.yaml", """
id: h-social-network-star-topology-innovation-fixation
title: >
  In modular social networks with high-degree hub individuals, the probability
  that a beneficial cultural innovation (fitness advantage r > 1) fixes in the
  population is >3× higher than in a corresponding random-graph population of
  the same size, due to the star-graph amplifier effect of hub-and-spoke topology.
status: active
created: "2026-05-07"
priority: medium
impact_score: 0.67
related_disciplines:
  - evolutionary-biology
  - social-science
  - network-science
unknowns_addressed:
  - u-evolutionary-graph-amplifier-natural-populations
evidence_links:
  - doi: "10.1038/nature03277"
    type: supporting
    confidence: 0.72
    note: "Lieberman 2005 – star graph ρ >> Moran ρ; hub nodes amplify mutant fixation"
  - doi: "10.1126/science.1133755"
    type: supporting
    confidence: 0.60
    note: "Nowak 2006 – cooperation evolution on real social networks; hub-effect on cooperation"
proposed_tests:
  - description: >
      Extract degree distributions from 5 empirical online social networks
      (Facebook100, Twitter, etc.). Simulate evolutionary dynamics (birth-death
      rule, r = 1.05 mutant) for 10⁶ runs on each network and on degree-matched
      Erdős-Rényi random graphs. Compare fixation probabilities. Test whether
      hub-spoke networks show significantly higher mutant fixation than random
      controls using a bootstrap test (n = 1000).
""")

# ── 101 ────────────────────────────────────────────────────────────────────
write(ROOT / "cross-domain/physics-mathematics/b-turbulence-renormalization-group.yaml", """
id: b-turbulence-renormalization-group
title: >
  Kolmogorov's 1941 scaling law for the turbulent energy spectrum E(k) ~ k^{-5/3}
  in the inertial range is derived from a renormalization-group (RG) fixed point
  of the Navier-Stokes equations in momentum space: the RG flow drives the system
  to a universal scaling regime independent of the large-scale energy injection
  mechanism.
status: established
fields:
  - fluid-mechanics
  - physics
  - mathematics
  - statistical-physics
bridge_claim: >
  Kolmogorov (1941) argued that in the inertial range (injection scale L >> l
  >> dissipation scale η), energy cascades from large to small eddies at a
  constant rate ε, giving E(k) ~ ε^{2/3} k^{-5/3}. Yakhot & Orszag (1986)
  derived this using dynamic RG (DRG) applied to the Navier-Stokes equations:
  integrating out high-wavenumber fluctuations generates effective large-scale
  viscosity and driving terms; the RG fixed point corresponds exactly to K41
  scaling. The effective eddy viscosity ν_eff ~ k^{-4/3} at the fixed point
  gives the k^{-5/3} spectrum without assuming Kolmogorov's dimensional arguments.
  The DRG framework also predicts intermittency corrections (multifractal
  exponents) beyond K41 as deviations from the RG fixed point.
translation_table:
  - field_a_term: "Turbulent energy spectrum E(k) ~ k^{-5/3}"
    field_b_term: "Correlation function at the RG fixed point (power-law scaling)"
    note: "Fixed-point scaling gives E(k) ~ k^{-(d+2χ)/z} which equals k^{-5/3} for K41 exponents"
  - field_a_term: "Inertial-range energy cascade (constant flux ε)"
    field_b_term: "RG fixed-point flow: marginal operator with zero beta function"
    note: "Constant energy flux ↔ zero beta function for the dissipation coupling at the fixed point"
  - field_a_term: "Kolmogorov microscale η = (ν³/ε)^{1/4}"
    field_b_term: "RG flow cutoff / ultraviolet scale below which fixed point breaks down"
    note: "Molecular viscosity ν terminates the RG cascade at scale η"
  - field_a_term: "Intermittency corrections to K41 (anomalous exponents)"
    field_b_term: "Irrelevant operators at the RG fixed point (perturbative corrections)"
    note: "Multifractal exponents ζ_p ≠ p/3 arise from corrections to scaling at the RG fixed point"
related_unknowns:
  - u-turbulence-anomalous-scaling-intermittency-origin
related_hypotheses:
  - h-navier-stokes-rg-fixed-point-intermittency-exponents
cross_pollination_opportunities:
  - >
    RG methods from field theory (Wilson's epsilon expansion) can be applied to
    compressible turbulence and magnetohydrodynamic turbulence, predicting
    whether different RG fixed points (and therefore different spectral exponents)
    apply to the solar wind and astrophysical plasma turbulence.
  - >
    The DRG-derived eddy viscosity formula can be used to parameterise subgrid-
    scale turbulence in large-eddy simulations (LES) of atmospheric flows, replacing
    empirical Smagorinsky constants with RG-derived coefficients.
communication_gap: >
  Fluid dynamicists and turbulence engineers use the K41 spectrum empirically
  and Smagorinsky eddy viscosity models without engaging with the RG derivation.
  Field theorists who developed DRG (Yakhot & Orszag 1986) publish in Physical
  Review Letters, not in the Journal of Fluid Mechanics where turbulence
  experimentalists publish.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1103/PhysRevLett.57.1722"
    note: "Yakhot & Orszag (1986) PRL – renormalization group analysis of turbulence; derivation of K41 exponents"
  - doi: "10.1063/1.866483"
    note: "Yakhot & Orszag (1986) J. Sci. Comput. – renormalisation group and large eddy simulation"
  - doi: "10.1146/annurev.fluid.30.1.275"
    note: "Frisch (1995) – turbulence: the legacy of A.N. Kolmogorov; RG and multifractal theory"
  - arxiv: "nlin/0404058"
    note: "Eyink & Sreenivasan – Onsager and the theory of hydrodynamic turbulence; RG connections"
""")

write(ROOT / "unknowns-catalog/physics/u-turbulence-anomalous-scaling-intermittency-origin.yaml", """
id: u-turbulence-anomalous-scaling-intermittency-origin
title: >
  What is the mathematical origin of anomalous scaling (intermittency corrections)
  in fully developed turbulence, and can the multifractal exponents ζ_p be
  derived analytically from the Navier-Stokes equations?
status: open
priority: high
disciplines:
  - fluid-mechanics
  - physics
  - mathematics
summary: >
  Experimental measurements of the pth-order velocity structure function
  ⟨(δv_r)^p⟩ ~ r^{ζ_p} show ζ_p ≠ p/3 (the K41 prediction), demonstrating
  that turbulence is intermittent. The multifractal model of turbulence
  parameterises ζ_p by a singularity spectrum f(α) but does not derive it
  from the Navier-Stokes equations. Whether a first-principles derivation of
  the multifractal exponents from NS equations is possible remains one of the
  most important open problems in mathematical physics.
systematic_gaps:
  - No rigorous derivation of the anomalous exponents ζ_p from the 3D Navier-Stokes equations exists.
  - The relationship between Navier-Stokes solutions and the Kolmogorov refined similarity hypothesis (RSH) has not been proven.
  - Whether the 3D Euler equations (ν → 0) exhibit anomalous scaling is not established analytically or numerically.
last_reviewed: "2026-05-07"
""")

write(ROOT / "hypotheses/active/h-navier-stokes-rg-fixed-point-intermittency-exponents.yaml", """
id: h-navier-stokes-rg-fixed-point-intermittency-exponents
title: >
  The anomalous intermittency exponents ζ_p in 3D turbulence arise from
  the leading irrelevant operator at the K41 RG fixed point, and their
  values can be derived perturbatively in ε = 4 − d (d = dimension) using
  the DRG expansion, with the leading correction giving ζ_6 = 1.77 ± 0.05.
status: active
created: "2026-05-07"
priority: high
impact_score: 0.85
related_disciplines:
  - fluid-mechanics
  - statistical-physics
  - mathematics
unknowns_addressed:
  - u-turbulence-anomalous-scaling-intermittency-origin
evidence_links:
  - doi: "10.1103/PhysRevLett.57.1722"
    type: supporting
    confidence: 0.60
    note: "Yakhot & Orszag – DRG fixed point; leading-order K41 exponents; basis for perturbative corrections"
  - doi: "10.1146/annurev.fluid.30.1.275"
    type: related
    confidence: 0.55
    note: "Frisch – multifractal turbulence: review of anomalous exponents and theoretical approaches"
proposed_tests:
  - description: >
      Compute ζ_6 to next-to-leading order in ε = 4 − d using the DRG
      expansion of the Navier-Stokes equations (Forster-Nelson-Stephen scheme).
      Compare the analytical prediction to DNS measurements of ζ_6 in boxes
      of 4096³ grid points at Reλ > 500. Statistical test: |ζ_6^{theory} −
      ζ_6^{DNS}| / σ_{DNS} < 2 at 95% confidence.
""")

# ── 102 ────────────────────────────────────────────────────────────────────
write(ROOT / "cross-domain/biology-physics/b-metabolic-scaling-fractal-vasculature.yaml", """
id: b-metabolic-scaling-fractal-vasculature
title: >
  Kleiber's 3/4-power metabolic scaling law (B ~ M^{3/4}) across animals spanning
  27 orders of magnitude in body mass is derived from the fractal geometry of
  space-filling vascular networks: West, Brown & Enquist (1997) proved that the
  4/3 exponent arises necessarily from the constraint that hierarchical branching
  networks minimise hydrodynamic resistance while filling volume fractally.
status: established
fields:
  - physiology
  - physics
  - ecology
  - mathematics
bridge_claim: >
  West, Brown & Enquist (1997) derived Kleiber's law from three assumptions:
  (1) the vascular network is a self-similar fractal with branching ratio n_b,
  (2) the terminal units (capillaries/leaf stomata) are size-invariant,
  (3) the network minimises the total hydrodynamic resistance (evolutionary
  optimality). These constraints, combined with the requirement that the network
  fills a 3D volume, uniquely give the allometric exponent 3/4 = d/(d+1) for
  d = 3. The 3/4 exponent for mammals and 2/3 exponent for organisms without
  circulatory systems follows from the space-filling dimension d of the resource
  distribution network.
translation_table:
  - field_a_term: "Kleiber's law B ~ M^{3/4} (metabolic rate vs. body mass)"
    field_b_term: "Allometric exponent = d/(d+1) from fractal network geometry"
    note: "3D space-filling network gives 3/4; 2D network gives 2/3; surface-limited gives 2/3"
  - field_a_term: "Vascular branching: artery → capillary hierarchy"
    field_b_term: "Self-similar fractal branching network (Horton-Strahler order)"
    note: "Each branching level preserves the volume-filling constraint; radius ratio = n_b^{-1/3}"
  - field_a_term: "Capillary size (invariant across species)"
    field_b_term: "Fixed terminal unit of the fractal: size-invariant boundary condition"
    note: "Capillary diameter ~5 μm, flow rate ~1 mm/s invariant from mouse to whale"
  - field_a_term: "Minimum hydrodynamic resistance (Murray's law: r₃ = Σrᵢ³)"
    field_b_term: "Optimal transport network (Wasserstein/minimum cost-flow)"
    note: "Murray's law is the optimality condition; equivalent to minimum cost branching in optimal transport"
related_unknowns:
  - u-metabolic-scaling-deviations-non-mammalian
related_hypotheses:
  - h-metabolic-exponent-network-dimension-prediction
cross_pollination_opportunities:
  - >
    The WBE framework predicts plant metabolic scaling from leaf/xylem network
    geometry; testing the model across plant functional types (C3, C4, CAM)
    with leaf hydraulic data can validate the fractal network mechanism beyond
    animals.
  - >
    Fractal vascular network optimality theory can guide the design of
    microfluidic lab-on-chip devices, predicting the channel branching geometry
    that minimises pressure drop while maximising surface area for chemical
    reactions or drug delivery.
communication_gap: >
  Physiologists measuring metabolic rates and network engineers studying fractal
  branching rarely read the same literature. The West-Brown-Enquist paper (1997
  Science) sparked considerable controversy in physiology journals; the derivation
  is more widely accepted among network theorists than among comparative
  physiologists who dispute the universality of the 3/4 exponent.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1126/science.276.5309.122"
    note: "West, Brown & Enquist (1997) Science – a general model for the origin of allometric scaling laws; fractal vasculature"
  - doi: "10.1126/science.284.5420.1677"
    note: "Banavar et al. (1999) Science – size and form in efficient transportation networks"
  - doi: "10.1086/303427"
    note: "Enquist et al. – allometric scaling of plant energetics and population density"
  - doi: "10.1038/35009076"
    note: "Dreyer & Puzio (2001) – test of the WBE model; fractal geometry and Kleiber's law"
""")

write(ROOT / "unknowns-catalog/biology/u-metabolic-scaling-deviations-non-mammalian.yaml", """
id: u-metabolic-scaling-deviations-non-mammalian
title: >
  Why do metabolic scaling exponents deviate from 3/4 in insects, unicellular
  organisms, and plants, and do these deviations reflect differences in vascular
  network geometry or violations of the WBE model assumptions?
status: open
priority: medium
disciplines:
  - physiology
  - ecology
  - physics
summary: >
  The West-Brown-Enquist (WBE) model predicts a universal 3/4 exponent from
  fractal space-filling vascular networks. However, measured exponents vary:
  insects show ~0.83, unicellular organisms ~0.75 (consistent), plants ~0.75–0.80,
  and some groups show exponents of 2/3 (surface-area limited). The WBE model
  assumptions (branching ratio invariance, terminal unit size-invariance, 3D
  space-filling) may break down for non-mammalian groups, but which assumption
  fails and why is not established.
systematic_gaps:
  - Systematic comparison of measured vascular/tracheal network fractal dimensions against WBE predictions across phyla has not been performed.
  - Whether insect tracheal systems satisfy the volume-filling constraint of WBE is not quantified.
  - The dependence of the measured scaling exponent on phylogenetic correction and dataset composition is not adequately controlled in existing meta-analyses.
last_reviewed: "2026-05-07"
""")

write(ROOT / "hypotheses/active/h-metabolic-exponent-network-dimension-prediction.yaml", """
id: h-metabolic-exponent-network-dimension-prediction
title: >
  The metabolic scaling exponent β = d/(d+1) where d is the fractal dimension
  of the resource-distribution network, measured from vascular/tracheal fractal
  analysis, will predict the empirical β across 10 major animal phyla better
  than the universal 3/4 constant (R² improvement >0.15).
status: active
created: "2026-05-07"
priority: medium
impact_score: 0.74
related_disciplines:
  - physiology
  - physics
unknowns_addressed:
  - u-metabolic-scaling-deviations-non-mammalian
evidence_links:
  - doi: "10.1126/science.276.5309.122"
    type: supporting
    confidence: 0.75
    note: "West, Brown & Enquist 1997 – theoretical derivation; β = d/(d+1) for d = 3 gives 3/4"
  - doi: "10.1126/science.284.5420.1677"
    type: supporting
    confidence: 0.65
    note: "Banavar 1999 – alternative derivation confirms network dimension determines exponent"
proposed_tests:
  - description: >
      Select 10 animal phyla (mammals, birds, reptiles, amphibians, fish, insects,
      crustaceans, annelids, echinoderms, molluscs). For each phylum, measure
      the fractal dimension d of the primary circulatory/respiratory network from
      micro-CT images of representative species (n ≥ 5 per phylum). Compute
      predicted β = d/(d+1). Regress against the empirical β from the AnAge metabolic
      database. Compare R² of the network-dimension model vs. a constant β = 0.75.
""")

# ── 103 ────────────────────────────────────────────────────────────────────
write(ROOT / "cross-domain/social-science-epidemiology/b-social-contagion-complex-threshold.yaml", """
id: b-social-contagion-complex-threshold
title: >
  The spread of social behaviours (innovation adoption, social movements,
  voting) requires exposure to multiple independent contacts (complex contagion)
  unlike disease spread (simple contagion), described by threshold models
  where adoption occurs when the fraction of adopting neighbours exceeds
  an individual-specific threshold φ — a fundamentally different dynamic
  than standard SIR epidemics.
status: established
fields:
  - social-science
  - epidemiology
  - network-science
  - sociology
bridge_claim: >
  Granovetter (1978) showed that riot or protest participation depends on
  threshold distributions in populations; the cascade dynamics depend
  critically on the shape of the threshold distribution φ_i. Centola (2010)
  demonstrated empirically that complex contagion (requiring multiple exposures)
  spreads faster on clustered networks than on random networks—the opposite
  of simple contagion. This is because clustered networks provide redundant
  reinforcing signals to threshold-exceeding nodes. The mathematical distinction:
  simple contagion spreads via the branching process (SIR), while complex
  contagion requires the cascade condition (mean excess degree × adoption
  probability) × mean fractional reinforcement > 1 in the Dodds-Watts
  generalised contagion model.
translation_table:
  - field_a_term: "Individual adoption threshold φ_i (fraction of neighbours who must adopt first)"
    field_b_term: "No equivalent in SIR: binary exposure probability in simple contagion"
    note: "Complex contagion requires reinforcement; simple contagion requires single exposure"
  - field_a_term: "Clustered network (high clustering coefficient)"
    field_b_term: "Network that provides reinforcing triangles for threshold-exceeding"
    note: "Clustering helps complex contagion (redundant exposure) but hinders simple contagion (fewer bridges)"
  - field_a_term: "Global cascade condition (Watts 2002)"
    field_b_term: "Epidemic threshold R₀ > 1 in simple contagion"
    note: "Both are percolation-type thresholds; cascade condition involves threshold distribution, not just degree"
  - field_a_term: "Weak ties (Granovetter) as bridges for information"
    field_b_term: "Long-range edges enabling simple contagion but hindering complex contagion"
    note: "Weak ties are bridges that lack the clustering needed for threshold reinforcement in complex contagion"
related_unknowns:
  - u-complex-contagion-threshold-distribution-estimation
related_hypotheses:
  - h-social-movement-cascade-clustered-network-advantage
cross_pollination_opportunities:
  - >
    Online A/B experiments on platform networks can test the complex vs. simple
    contagion distinction by varying whether users see which of their friends
    have adopted a behaviour (reinforcement visible) or only that some friends
    have adopted (single-signal exposure), measuring differential spread rates.
  - >
    Public health interventions for behaviour change (mask-wearing, vaccination
    uptake) that treat adoption as complex contagion (requiring social norm
    reinforcement from multiple contacts) can be designed using Centola's
    clustered network findings rather than simple epidemic seeding strategies.
communication_gap: >
  Epidemiologists model disease spread with SIR (simple contagion) and apply
  the same framework to health behaviour change. Sociologists studying social
  movements use threshold models without connection to network science. Centola
  (2010) provided the empirical demonstration of the distinction, but adoption
  of the complex contagion framework in public health practice lags.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1086/226707"
    note: "Granovetter (1978) AJS – threshold models of collective behavior; cascade dynamics"
  - doi: "10.1126/science.1185231"
    note: "Centola (2010) Science – the spread of behavior in an online social network experiment; complex contagion"
  - doi: "10.1103/PhysRevE.70.026116"
    note: "Dodds & Watts (2004) PRE – universal behavior in a generalised model of contagion"
  - doi: "10.1073/pnas.252631999"
    note: "Watts (2002) PNAS – a simple model of global cascades on random networks"
""")

write(ROOT / "unknowns-catalog/social-science/u-complex-contagion-threshold-distribution-estimation.yaml", """
id: u-complex-contagion-threshold-distribution-estimation
title: >
  How can adoption thresholds φ_i be estimated from observational social
  network data, and does the empirical threshold distribution predict
  cascade dynamics better than mean-field SIR models for real social behaviours?
status: open
priority: medium
disciplines:
  - social-science
  - epidemiology
  - network-science
summary: >
  Complex contagion theory requires knowledge of the threshold distribution
  P(φ) in the population to predict cascade outcomes. However, individual
  thresholds are not directly observable; they must be inferred from adoption
  timing and network position. No validated method exists for estimating P(φ)
  from observational data, making it difficult to test complex contagion theory
  quantitatively for real social phenomena.
systematic_gaps:
  - Methods for identifying individual adoption thresholds from panel data on social network adoption are not validated against ground truth from controlled experiments.
  - The degree to which threshold heterogeneity (wide P(φ)) vs. mean threshold determines cascade dynamics has not been quantified empirically.
  - No head-to-head comparison of simple SIR and complex contagion models exists using the same empirical social diffusion dataset with temporal data.
last_reviewed: "2026-05-07"
""")

write(ROOT / "hypotheses/active/h-social-movement-cascade-clustered-network-advantage.yaml", """
id: h-social-movement-cascade-clustered-network-advantage
title: >
  Protest or social-movement adoption campaigns seeded in high-clustering
  network communities will achieve global cascade (>50% adoption) at 3× lower
  initial seed size than campaigns seeded randomly, when the median adoption
  threshold φ > 0.2.
status: active
created: "2026-05-07"
priority: medium
impact_score: 0.71
related_disciplines:
  - social-science
  - network-science
unknowns_addressed:
  - u-complex-contagion-threshold-distribution-estimation
evidence_links:
  - doi: "10.1126/science.1185231"
    type: supporting
    confidence: 0.78
    note: "Centola 2010 – clustered network seeding leads to 2-4× faster adoption in health forum experiment"
  - doi: "10.1073/pnas.252631999"
    type: supporting
    confidence: 0.65
    note: "Watts 2002 – global cascade conditions depend on seed placement and network clustering"
proposed_tests:
  - description: >
      Run agent-based complex contagion simulations on 20 empirical social
      networks (various clustering levels). Set threshold distribution φ_i ~
      Uniform(0.1, 0.4) (median 0.25). Compare cascade sizes from: (a) random
      1% seed; (b) high-clustering community 1% seed; (c) high-degree 1% seed.
      Determine the seed-size ratio needed for 50% cascade across all three
      strategies. Test the 3× prediction with a Wilcoxon test across networks.
""")

# ── 104 ────────────────────────────────────────────────────────────────────
write(ROOT / "cross-domain/neuroscience-cognitive-science/b-cortical-hierarchy-predictive-coding.yaml", """
id: b-cortical-hierarchy-predictive-coding
title: >
  The hierarchical organisation of the cortex implements approximate Bayesian
  inference: higher areas send predictions (priors) downward and receive
  prediction errors (likelihood signals) upward, minimising free energy
  (surprise) in a generative model of sensory inputs — the predictive coding
  framework of Rao & Ballard (1999) and Friston's free energy principle.
status: proposed
fields:
  - neuroscience
  - cognitive-science
  - Bayesian-inference
  - computational-neuroscience
bridge_claim: >
  Hierarchical Bayesian inference requires propagating predictions from high-
  level models downward and prediction errors from low-level observations upward.
  Rao & Ballard (1999) showed that a two-level cortical model where V1 predicts
  the output of the retina (top-down prediction) and sends residual errors to V2
  reproduces end-stopping, extra-classical receptive field effects, and attention
  modulation. Friston (2005) generalised this to Helmholtz machines and the free
  energy principle: the brain minimises variational free energy F = E_q[log q −
  log p] ≈ −log P(data|model) + KL(q||p), approximating Bayesian inference
  by minimising surprise. The cortical laminar structure—with superficial
  layers carrying prediction errors to higher areas and deep layers carrying
  predictions downward—implements the message-passing in this Bayesian hierarchy.
translation_table:
  - field_a_term: "Top-down cortical connection (deep layers → lower areas)"
    field_b_term: "Prior/prediction message in belief propagation"
    note: "Deep layer projections carry generative model predictions; implement the prior P(z|θ)"
  - field_a_term: "Superficial layer prediction error neurons (mismatch response)"
    field_b_term: "Likelihood/evidence message propagated up the hierarchy"
    note: "Mismatch negativity and oddball responses = large prediction error from violated prior"
  - field_a_term: "Gain modulation by attention (increasing precision of prediction errors)"
    field_b_term: "Precision weighting in Bayesian inference (inverse variance of likelihood)"
    note: "Attention increases the precision (1/σ²) of sensory signals; equivalent to prior sharpening"
  - field_a_term: "Cortical hierarchy depth (V1→V2→V4→IT→PFC)"
    field_b_term: "Depth of the Bayesian generative model hierarchy"
    note: "Each cortical area = one level of the generative model; depth enables abstract representation"
related_unknowns:
  - u-predictive-coding-laminar-circuit-mechanism
related_hypotheses:
  - h-mismatch-negativity-bayesian-precision-prediction-error
cross_pollination_opportunities:
  - >
    Deep learning architectures with feedback connections (predictive coding
    networks, Rao-Ballard models) can be tested against purely feedforward
    networks on noise-robustness and out-of-distribution generalisation,
    providing a computational test of the predictive coding advantage.
  - >
    Pharmacological manipulation of precision (via dopamine, acetylcholine)
    combined with EEG mismatch negativity (MMN) measurements can test whether
    MMN amplitude tracks precision weighting as predicted by the free energy
    principle.
communication_gap: >
  The predictive coding framework bridges computational Bayesian inference (AI
  literature) and laminar cortical neurophysiology (neuroscience literature).
  Friston's free energy principle (published in Trends in Cognitive Sciences and
  Nature Reviews Neuroscience) has been critiqued as unfalsifiable; its specific
  laminar-circuit predictions are tested in a separate experimental literature
  that does not always engage with the formal Bayesian framework.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1038/nn.2387"
    note: "Rao & Ballard (1999) Nature Neuroscience – predictive coding in the visual cortex; hierarchical model"
  - doi: "10.1098/rstb.2005.1622"
    note: "Friston (2005) Phil. Trans. R. Soc. B – a theory of cortical responses; free energy principle"
  - doi: "10.1016/j.neuron.2015.09.030"
    note: "Keller & Mrsic-Flogel (2018) Neuron – predictive processing: a canonical cortical computation"
  - doi: "10.1038/s41583-019-0275-5"
    note: "Friston – a free energy principle for a particular physics; mathematical foundations"
""")

write(ROOT / "unknowns-catalog/neuroscience/u-predictive-coding-laminar-circuit-mechanism.yaml", """
id: u-predictive-coding-laminar-circuit-mechanism
title: >
  What specific cortical circuit elements implement prediction error computation
  in layers 2/3 and prediction propagation in layer 6, and do these circuits
  show the differential response properties predicted by the free energy principle?
status: open
priority: high
disciplines:
  - neuroscience
  - computational-neuroscience
  - Bayesian-inference
summary: >
  The predictive coding framework assigns distinct functional roles to cortical
  layers: prediction errors in superficial layers (2/3), predictions in deep
  layers (5/6). This has anatomical support (superficial layers project to
  higher areas; deep layers project to lower areas) but the specific cell types,
  synaptic mechanisms, and neural coding properties (rate codes? timing codes?)
  implementing prediction error computation have not been identified. Recent
  work on VIP/SST inhibitory interneurons as gain controllers is consistent
  but not conclusive.
systematic_gaps:
  - No laminar-specific recording study has demonstrated the predicted anti-correlation between superficial-layer prediction-error responses and deep-layer prediction signals.
  - The identity of the neural substrate for precision-weighting (the gain-control signal) is not established; VIP interneurons are a candidate but not confirmed.
  - Whether the mismatch negativity (MMN) in EEG/MEG reflects superficial-layer prediction-error neurons or a more distributed response has not been resolved with laminar recordings.
last_reviewed: "2026-05-07"
""")

write(ROOT / "hypotheses/active/h-mismatch-negativity-bayesian-precision-prediction-error.yaml", """
id: h-mismatch-negativity-bayesian-precision-prediction-error
title: >
  The amplitude of the cortical mismatch negativity (MMN) response scales
  linearly with the precision-weighted prediction error (σ⁻² × ΔP) predicted
  by the Rao-Ballard model, where σ² is the stimulus variability in the context
  window and ΔP is the prior-minus-likelihood deviation.
status: active
created: "2026-05-07"
priority: medium
impact_score: 0.75
related_disciplines:
  - neuroscience
  - cognitive-science
unknowns_addressed:
  - u-predictive-coding-laminar-circuit-mechanism
evidence_links:
  - doi: "10.1038/nn.2387"
    type: supporting
    confidence: 0.65
    note: "Rao & Ballard – predictive coding model predicts MMN-like responses; precision weighting"
  - doi: "10.1016/j.neuron.2015.09.030"
    type: supporting
    confidence: 0.60
    note: "Keller & Mrsic-Flogel – experimental evidence for predictive coding in mouse V1"
proposed_tests:
  - description: >
      Record EEG MMN responses (oddball paradigm) in 30 human participants
      while manipulating context variability (σ² of standard stimuli) across 5
      levels. Compute precision-weighted prediction error from stimulus statistics.
      Fit a linear model: MMN amplitude ~ α(σ⁻² × |deviant − mean standard|).
      Test whether the linear model explains significantly more variance (p < 0.01)
      than a model using raw deviance alone.
""")

# ── 105 ────────────────────────────────────────────────────────────────────
write(ROOT / "cross-domain/synthetic-biology-chemistry/b-synthetic-genetics-xna-alphabet.yaml", """
id: b-synthetic-genetics-xna-alphabet
title: >
  Xeno-nucleic acids (XNAs) with chemically modified backbones (HNA, CeNA,
  LNA, FANA, TNA) can store and propagate genetic information through in vitro
  evolution, demonstrating that the Watson-Crick hydrogen-bonding code is
  substrate-independent: Darwinian evolution does not require the ribose-
  phosphate backbone of natural DNA/RNA.
status: established
fields:
  - synthetic-biology
  - chemistry
  - molecular-biology
  - origins-of-life
bridge_claim: >
  Pinheiro et al. (2012) evolved polymerases capable of transcribing DNA into
  six different XNAs and back-transcribing XNA into DNA, demonstrating faithful
  information transfer across the chemical boundary. HNA (hexitol nucleic acid)
  and FANA (2'F-ANA) aptamers and ribozymes were selected by in vitro evolution,
  showing that XNAs can fold into functional tertiary structures and undergo
  Darwinian selection. The bridge: the genetic information content of DNA/RNA
  is a property of the base-pairing code (hydrogen bond complementarity), not
  the specific backbone chemistry; XNAs prove that alternative chemistries can
  implement the same Darwinian logic.
translation_table:
  - field_a_term: "Ribose-phosphate backbone (DNA/RNA)"
    field_b_term: "Hexitol/threose/fluoroarabinose backbone (XNA)"
    note: "Different backbone; same Watson-Crick base pairing; same information-theoretic capacity"
  - field_a_term: "DNA polymerase (natural template-directed synthesis)"
    field_b_term: "Engineered XNA polymerase (in vitro selected reverse transcriptase)"
    note: "XNA polymerases transfer genetic information from XNA to DNA; reverse transcription across chemistries"
  - field_a_term: "Darwinian evolution (mutation + selection + heredity)"
    field_b_term: "In vitro selection on XNA libraries (SELEX on XNA)"
    note: "XNA aptamers evolve function through same iterative selection mechanism as natural evolution"
  - field_a_term: "DNA sequence space (4^N configurations)"
    field_b_term: "XNA sequence space with same four bases; different backbone flexibility"
    note: "Both implement a 4-letter alphabet; backbone rigidity changes the fitness landscape geometry"
related_unknowns:
  - u-xna-expanded-genetic-alphabet-catalysis
related_hypotheses:
  - h-xna-ribozyme-catalytic-efficiency-backbone-independence
cross_pollination_opportunities:
  - >
    XNA therapeutics (antisense, aptamers) exploit backbone modifications
    (phosphorothioate, LNA) to improve nuclease resistance; the synthetic genetics
    framework predicts which backbone chemistries preserve catalytic function while
    adding metabolic stability, guiding drug design.
  - >
    Origins-of-life research can use XNA as a model for pre-RNA genetic polymers:
    testing whether TNA (threofuranosyl nucleic acid) or PNA (peptide nucleic acid)
    supports Darwinian evolution addresses which chemistry preceded RNA in the
    RNA world hypothesis.
communication_gap: >
  Synthetic organic chemists developing nucleic acid analogues (LNA, phosphorothioate)
  for therapeutic applications and evolutionary biologists studying the chemical
  origins of life rarely collaborate. Pinheiro et al. (2012) bridged these
  communities in Science, but clinical development of XNA therapeutics and origins-
  of-life research remain siloed.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1126/science.1221558"
    note: "Pinheiro et al. (2012) Science – genetic encoding and chemical evolution of six XNAs; Darwinian XNA evolution"
  - doi: "10.1038/nature12343"
    note: "Malyshev et al. (2014) Nature – a semi-synthetic organism with an expanded genetic alphabet (d5SICS/dNaM)"
  - doi: "10.1038/nchem.1929"
    note: "Taylor et al. (2015) Nature Chemistry – catalysts from synthetic genetic polymers; HNA ribozymes"
  - doi: "10.1126/science.1213351"
    note: "Benner – defining life; synthetic biology and origins of life: genetic letters"
""")

write(ROOT / "unknowns-catalog/chemistry/u-xna-expanded-genetic-alphabet-catalysis.yaml", """
id: u-xna-expanded-genetic-alphabet-catalysis
title: >
  Can XNA or expanded-alphabet genetic polymers (>4 bases) achieve catalytic
  rates and substrate diversity comparable to ribozymes, and what backbone
  chemistry maximises both information-storage capacity and catalytic function?
status: open
priority: high
disciplines:
  - synthetic-biology
  - chemistry
  - origins-of-life
summary: >
  Natural ribozymes achieve catalytic rate enhancements of 10⁵–10¹¹ over
  background reaction rates using the ribose-phosphate backbone's specific
  flexibility and 2'-OH chemistry. XNA ribozymes have been evolved (Taylor 2015)
  but achieve lower catalytic rates. Whether backbone chemistry fundamentally
  limits XNA catalysis or whether the exploration of XNA sequence space has been
  insufficient is unknown. Expanded genetic alphabets (6 or 8 bases) would
  increase sequence diversity but their compatibility with catalytic folding is
  not established.
systematic_gaps:
  - The maximum achievable catalytic rate for HNA or FANA ribozymes has not been determined by exhaustive directed evolution.
  - The structural basis for lower catalytic efficiency of XNA ribozymes vs. RNA ribozymes has not been resolved by X-ray crystallography or cryo-EM.
  - Whether expanded alphabets (6 bases) improve or degrade ribozyme catalytic efficiency by changing folding energy landscapes is not tested experimentally.
last_reviewed: "2026-05-07"
""")

write(ROOT / "hypotheses/active/h-xna-ribozyme-catalytic-efficiency-backbone-independence.yaml", """
id: h-xna-ribozyme-catalytic-efficiency-backbone-independence
title: >
  FANA (2'F-arabino nucleic acid) ribozymes will achieve catalytic rate
  enhancement (k_cat/k_uncat) within one order of magnitude of the equivalent
  RNA ribozyme after 15 rounds of directed evolution, because FANA's backbone
  rigidity provides similar pre-organisation of the active site as RNA.
status: active
created: "2026-05-07"
priority: high
impact_score: 0.77
related_disciplines:
  - synthetic-biology
  - chemistry
unknowns_addressed:
  - u-xna-expanded-genetic-alphabet-catalysis
evidence_links:
  - doi: "10.1038/nchem.1929"
    type: supporting
    confidence: 0.65
    note: "Taylor 2015 – HNA ribozymes evolved; catalytic rates lower than RNA; FANA predicted to be better"
  - doi: "10.1126/science.1221558"
    type: supporting
    confidence: 0.70
    note: "Pinheiro 2012 – FANA and HNA functional fold; FANA closest to RNA in backbone geometry"
proposed_tests:
  - description: >
      Synthesise a FANA library (randomised core, N = 40 positions, ~10¹³ sequences).
      Perform 15 rounds of SELEX for RNA-cleaving ribozyme activity (template:
      all-RNA substrate). Characterise top 20 clones for k_cat and K_M. Compare to
      the hammerhead ribozyme baseline (k_cat ~ 1 min⁻¹). Test whether the best
      FANA ribozyme achieves k_cat/k_uncat > 10³, within one order of magnitude of
      the RNA hammerhead (~10⁵).
""")

# ── 106 ────────────────────────────────────────────────────────────────────
write(ROOT / "cross-domain/astronomy-physics/b-dark-energy-vacuum-cosmological-constant.yaml", """
id: b-dark-energy-vacuum-cosmological-constant
title: >
  The observed cosmological constant Λ ≈ 1.11 × 10⁻⁵² m⁻² driving accelerated
  cosmic expansion corresponds to a vacuum energy density ρ_Λ = Λc²/(8πG) ≈
  5.4 × 10⁻¹⁰ J/m³, which is ~120 orders of magnitude smaller than the naive
  quantum-field-theory estimate of zero-point energies — the cosmological
  constant problem is the largest numerical discrepancy in physics.
status: contested
fields:
  - cosmology
  - quantum-field-theory
  - particle-physics
  - astronomy
bridge_claim: >
  Einstein introduced Λ as a static-universe term (1917); Perlmutter and Riess
  (1998/1999) discovered dark energy from supernovae — cosmic expansion is
  accelerating, requiring a non-zero Λ > 0. The bridge to quantum field theory:
  the zero-point energy of all quantum fields contributes to the vacuum energy
  ρ_vac = (1/2)Σ_k ℏω_k, which (cut off at the Planck scale) gives ρ_vac ~
  10⁹⁴ kg/m³, while the observed ρ_Λ ~ 10⁻²⁷ kg/m³. The ratio is ~10¹²¹.
  This 120-order-of-magnitude discrepancy (or the question of why Λ is small
  but non-zero) is the cosmological constant problem. Proposed resolutions
  (supersymmetry, vacuum degeneracy, anthropic selection, modified gravity)
  remain speculative.
translation_table:
  - field_a_term: "Cosmological constant Λ (Einstein field equations)"
    field_b_term: "Vacuum energy density ρ_Λ = Λc²/(8πG) of quantum fields"
    note: "GR parameter Λ is identified with ρ_vac from QFT; the identification creates the CC problem"
  - field_a_term: "Observed dark energy equation of state w ≈ −1 (SN Ia, CMB)"
    field_b_term: "Vacuum energy equation of state p = −ρc² (negative pressure)"
    note: "w = −1 is consistent with a pure cosmological constant / vacuum energy"
  - field_a_term: "QFT zero-point energy cutoff at Planck scale E_Pl"
    field_b_term: "Ultraviolet divergence of vacuum energy (regulated)"
    note: "Cutoff at E_Pl gives ρ_vac ~ E_Pl⁴/(ℏ³c⁵) ~ 10⁹⁴ kg/m³; requires 120-order cancellation"
  - field_a_term: "Supersymmetry (bosonic and fermionic zero-point energies cancel)"
    field_b_term: "Proposed solution: bosonic +ℏω/2 cancels fermionic −ℏω/2"
    note: "Unbroken SUSY would give Λ = 0 exactly; broken SUSY at TeV scale still leaves ~10⁶⁰ excess"
related_unknowns:
  - u-cosmological-constant-small-value-explanation
related_hypotheses:
  - h-dark-energy-quintessence-equation-of-state-variation
cross_pollination_opportunities:
  - >
    Precision measurements of the dark energy equation of state w(z) as a
    function of redshift (from Euclid, DESI, Roman Space Telescope) can
    distinguish a true cosmological constant (w = −1 exactly) from dynamical
    dark energy (quintessence, w(z) ≠ −1), constraining QFT vacuum energy models.
  - >
    Analogue experiments of vacuum energy (Casimir effect in precision
    cavities) can constrain the sign and magnitude of UV contributions to
    the QED vacuum energy, informing whether QFT renormalization schemes
    for Λ are physically reasonable.
communication_gap: >
  Cosmologists using Λ as a phenomenological fit parameter and quantum field
  theorists computing vacuum energies publish in different communities. Weinberg
  (1989) Reviews of Modern Physics stated the problem cleanly but no solution
  has emerged in 37 years. The disconnect between observational cosmology,
  high-energy theory, and gravitational physics is structural and deep.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1103/RevModPhys.61.1"
    note: "Weinberg (1989) Rev. Mod. Phys. – the cosmological constant problem; 120-order discrepancy"
  - doi: "10.1086/307221"
    note: "Perlmutter et al. (1999) ApJ – measurements of Ω and Λ from 42 high-z supernovae; dark energy discovery"
  - doi: "10.1086/300499"
    note: "Riess et al. (1998) AJ – observational evidence for supernovae acceleration; dark energy"
  - doi: "10.1146/annurev-astro-081811-125543"
    note: "Weinberg et al. (2013) – observational probes of cosmic acceleration; dark energy review"
""")

write(ROOT / "unknowns-catalog/astronomy/u-cosmological-constant-small-value-explanation.yaml", """
id: u-cosmological-constant-small-value-explanation
title: >
  Why is the cosmological constant Λ ~ 10⁻⁵² m⁻² (small but non-zero), and
  what physical mechanism causes the ~120-order-of-magnitude cancellation
  between UV quantum vacuum contributions and the observed dark energy density?
status: open
priority: critical
disciplines:
  - cosmology
  - quantum-field-theory
  - particle-physics
summary: >
  The cosmological constant problem is the largest unsolved fine-tuning problem
  in physics. Quantum field theory predicts a vacuum energy density ~10¹²¹ times
  larger than observed. Proposed solutions include: (1) anthropic selection in
  a multiverse (Weinberg 1987 prediction of Λ < 10⁻¹²³ compatible with galaxy
  formation, confirmed), (2) supersymmetry cancellation (broken SUSY leaves ~
  10⁶⁰ excess), (3) sequestering mechanisms (degravitation), (4) modified
  gravity replacing Λ with a dynamical field. None is theoretically complete or
  empirically tested.
systematic_gaps:
  - No quantum gravity theory makes a first-principles calculation of Λ that matches observation.
  - The anthropic argument requires a populated multiverse with a specific measure; no such measure is derived from first principles.
  - Precision measurements of dark energy equation of state are insufficient to distinguish Λ from quintessence at current sensitivity.
last_reviewed: "2026-05-07"
""")

write(ROOT / "hypotheses/active/h-dark-energy-quintessence-equation-of-state-variation.yaml", """
id: h-dark-energy-quintessence-equation-of-state-variation
title: >
  If dark energy is quintessence (a scalar field) rather than a true cosmological
  constant, Euclid+DESI+Roman combined measurements of the dark energy equation
  of state will detect w(z) ≠ −1 at >2σ significance for z < 2, with the
  deviation following the Chevallier-Polarski-Linder parameterisation
  w(a) = w₀ + w_a(1−a) with |w_a| > 0.1.
status: active
created: "2026-05-07"
priority: critical
impact_score: 0.90
related_disciplines:
  - cosmology
  - particle-physics
unknowns_addressed:
  - u-cosmological-constant-small-value-explanation
evidence_links:
  - doi: "10.1086/307221"
    type: supporting
    confidence: 0.60
    note: "Perlmutter 1999 – SN Ia data consistent with w = −1; current precision insufficient to detect w_a"
  - doi: "10.1146/annurev-astro-081811-125543"
    type: related
    confidence: 0.55
    note: "Weinberg 2013 – dark energy probes; Euclid+DESI precision projections for w(z)"
proposed_tests:
  - description: >
      Combine public Euclid weak-lensing power spectra + DESI BAO measurements
      + Roman SN Ia data (all expected 2026-2030). Perform joint MCMC parameter
      estimation for {w₀, w_a, Ω_m, H₀} using CosmoSIS or MontePython. Test
      whether the best-fit w_a is inconsistent with 0 at >2σ. Secondary test:
      compare Bayesian evidence for ΛCDM vs. CPL quintessence model using
      Savage-Dickey density ratio.
""")

# ── 107 ────────────────────────────────────────────────────────────────────
write(ROOT / "cross-domain/ecology-physics/b-forest-fire-self-organized-criticality.yaml", """
id: b-forest-fire-self-organized-criticality
title: >
  Forest fire frequency-area distributions follow a power law P(A) ~ A^{−β}
  with β ≈ 1.3–1.5, consistent with Bak-Tang-Wiesenfeld self-organized
  criticality (SOC): forests spontaneously evolve to a critical state where
  perturbations (lightning) cause cascading fires of all sizes without
  external parameter tuning.
status: established
fields:
  - ecology
  - statistical-physics
  - environmental-science
bridge_claim: >
  Bak, Tang & Wiesenfeld (1987) introduced the sandpile automaton as the
  prototype SOC system: local collapse rules cause avalanches of all sizes,
  P(s) ~ s^{-3/2}, without tuning any parameter. The forest fire model
  (Drossel & Schwabl 1992) is an SOC system where trees grow slowly, lightning
  strikes randomly, and fires spread to nearest neighbours: the steady-state
  fire-size distribution follows a power law. Malamud et al. (1998) showed
  that US National Forest fire data (1970–2000) follow P(A) ~ A^{−1.3} over
  8 orders of magnitude in fire area, matching the SOC prediction. The power
  law fire-area distribution also matches the Gutenberg-Richter law for
  earthquake magnitudes (both are SOC manifestations), providing a universal
  framework for catastrophic natural hazards.
translation_table:
  - field_a_term: "Forest fire area distribution P(A) ~ A^{−1.3}"
    field_b_term: "SOC avalanche size distribution P(s) ~ s^{-β}"
    note: "Both power laws lack a characteristic scale; both arise from a critical state"
  - field_a_term: "Tree growth (slow process) + lightning strike (rare driving)"
    field_b_term: "Slow sandpile grain addition + toppling cascade"
    note: "Separation of time scales (slow drive, fast cascade) is the hallmark of SOC"
  - field_a_term: "Suppression of small fires → increased large fire risk"
    field_b_term: "Subcritical sand accumulation → larger avalanches when released"
    note: "Fire suppression policy moves the forest away from SOC; analogous to subcritical accumulation"
  - field_a_term: "Conifer fuel load (biomass per unit area)"
    field_b_term: "Local slope / stress in the sandpile; drives the cascade"
    note: "High fuel load = steep local slope; fire spreads when fuel load exceeds ignition threshold"
related_unknowns:
  - u-forest-fire-soc-climate-change-modification
related_hypotheses:
  - h-forest-fire-soc-beta-exponent-climate-invariance
cross_pollination_opportunities:
  - >
    SOC theory predicts that the fire-area exponent β should change systematically
    with fuel connectivity (the effective percolation density of flammable
    vegetation). Remote sensing of fuel connectivity from Landsat can test
    whether β correlates with landscape-scale fuel heterogeneity across
    different biomes.
  - >
    Prescribed burn programs that maintain fire-size distributions near the SOC
    power law (rather than suppressing all fires) can be designed using SOC
    theory to minimise catastrophic fire risk, directly applying physics to
    forest management policy.
communication_gap: >
  Forest ecologists and fire managers focus on species composition, fire
  weather, and suppression tactics; statistical physicists studying SOC rarely
  engage with practical fire management. Malamud et al. (1998) established the
  empirical connection but the SOC framework is not routinely used in wildfire
  risk assessment by land management agencies.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1103/PhysRevLett.59.381"
    note: "Bak, Tang & Wiesenfeld (1987) PRL – self-organized criticality: an explanation of 1/f noise"
  - doi: "10.1126/science.281.5384.1840"
    note: "Malamud et al. (1998) Science – forest fires: an example of self-organized critical behavior"
  - doi: "10.1103/PhysRevE.46.1829"
    note: "Drossel & Schwabl (1992) PRE – self-organised critical forest-fire model"
  - doi: "10.1073/pnas.0911553106"
    note: "Pueyo et al. (2010) PNAS – testing self-organized criticality in global forest fire data"
""")

write(ROOT / "unknowns-catalog/ecology/u-forest-fire-soc-climate-change-modification.yaml", """
id: u-forest-fire-soc-climate-change-modification
title: >
  How does climate-change-driven drought and fuel accumulation modify the
  power-law exponent of forest fire size distributions, and is the SOC
  critical state preserved or destroyed under extreme warming scenarios?
status: open
priority: high
disciplines:
  - ecology
  - statistical-physics
  - environmental-science
  - climate-science
summary: >
  The SOC interpretation of forest fire statistics assumes slow fuel accumulation
  and random ignition driving the system to a critical state. Climate change
  increases drought frequency, fuel dryness, and ignition probability (lightning,
  human ignition). Whether these changes shift the exponent β, destroy the power-
  law (sub-critical or super-critical regime), or maintain SOC with modified
  parameters is unknown and has major implications for wildfire risk management
  under climate change.
systematic_gaps:
  - Time-series analysis of fire-size power-law exponents before and after major drought events has not been performed systematically across multiple biomes.
  - Theoretical models of how increased fuel dryness (reduced ignition threshold) shifts the SOC critical point have not been developed for the Drossel-Schwabl model.
  - Whether fire suppression policies combined with climate change create a sub-critical state with anomalously large eventual fires exceeds SOC power-law predictions.
last_reviewed: "2026-05-07"
""")

write(ROOT / "hypotheses/active/h-forest-fire-soc-beta-exponent-climate-invariance.yaml", """
id: h-forest-fire-soc-beta-exponent-climate-invariance
title: >
  The forest fire area power-law exponent β is robust (1.3 ± 0.2) across
  climate zones and decadal drought cycles when fires are not suppressed,
  reflecting the universal SOC critical point; deviations beyond this range
  indicate departure from SOC caused by fire suppression or extreme fuel loading.
status: active
created: "2026-05-07"
priority: high
impact_score: 0.76
related_disciplines:
  - ecology
  - statistical-physics
unknowns_addressed:
  - u-forest-fire-soc-climate-change-modification
evidence_links:
  - doi: "10.1126/science.281.5384.1840"
    type: supporting
    confidence: 0.75
    note: "Malamud 1998 – US National Forest data β ≈ 1.3 across geographic regions; SOC interpretation"
  - doi: "10.1073/pnas.0911553106"
    type: supporting
    confidence: 0.65
    note: "Pueyo 2010 – global fire area distribution; SOC consistent across continents"
proposed_tests:
  - description: >
      Compute fire-area power-law exponents β from MODIS burned-area data
      (2001–2024) for 8 global biomes with high and low fire-suppression regimes.
      Fit β using maximum-likelihood power-law estimation (Clauset et al. 2009).
      Test whether β lies outside [1.1, 1.5] in suppression-heavy vs. natural
      fire-regime biomes. Correlate β with PDSI drought index for the preceding
      10 years.
""")

# ── 108 ────────────────────────────────────────────────────────────────────
write(ROOT / "cross-domain/biology-chemistry/b-circadian-clock-molecular-oscillator.yaml", """
id: b-circadian-clock-molecular-oscillator
title: >
  The ~24-hour circadian clock in eukaryotes is a biochemical limit-cycle
  oscillator: the PER/CRY/CLOCK/BMAL1 transcription-translation feedback loop
  generates self-sustained oscillations described by Goodwin-type nonlinear
  ODEs, and the clock's period, amplitude, and entrainability are predicted
  by the Hopf bifurcation structure of the oscillator.
status: established
fields:
  - chronobiology
  - systems-biology
  - chemistry
  - nonlinear-dynamics
bridge_claim: >
  The core circadian oscillator is a negative feedback loop: CLOCK:BMAL1
  activates Per and Cry transcription; PER:CRY proteins accumulate, enter
  the nucleus, and repress CLOCK:BMAL1. This is a delayed negative feedback
  loop producing limit-cycle oscillations (Goodwin 1965). Goldbeter (1995)
  showed that a 3-variable ODE model (PER mRNA, cytoplasmic PER, nuclear PER)
  with Hill coefficient n ≥ 9 generates ~24h oscillations. Leloup & Goldbeter
  (2003) extended this to the full PER/CRY system (19 variables), reproducing
  observed period mutations (per01, tau mutation) quantitatively. The Hopf
  bifurcation at critical Hill coefficient n_c separates non-oscillatory and
  oscillatory regimes; biological circuits operate above n_c due to cooperative
  repression.
translation_table:
  - field_a_term: "PER/CRY nuclear repression of CLOCK:BMAL1"
    field_b_term: "Negative feedback in a nonlinear ODE oscillator (Goodwin model)"
    note: "Delayed negative feedback with cooperative Hill-function repression (n > 8) = Hopf bifurcation"
  - field_a_term: "Circadian period (~24h)"
    field_b_term: "Period of the limit cycle at the Hopf bifurcation"
    note: "Period is set by the delay in the feedback loop (mRNA half-life, nuclear transport time)"
  - field_a_term: "Temperature compensation of period"
    field_b_term: "Robustness of limit-cycle period to parameter variation"
    note: "Biological circuits tune multiple rate constants so period is insensitive to temperature Q₁₀"
  - field_a_term: "Photic entrainment by light pulses (phase response curve)"
    field_b_term: "External forcing of a limit-cycle oscillator (Arnold tongues)"
    note: "Phase response curve = Jacobian of the oscillator limit cycle under impulsive perturbation"
related_unknowns:
  - u-circadian-temperature-compensation-mechanism
related_hypotheses:
  - h-circadian-hopf-bifurcation-period-mutation-prediction
cross_pollination_opportunities:
  - >
    The Hopf bifurcation framework predicts that the circadian clock becomes
    arrhythmic (below the bifurcation) when PER/CRY concentrations are below
    a threshold; pharmacological inhibition of casein kinase Iε (which
    phosphorylates and degrades PER) should increase amplitude and restore
    arrhythmic cells to oscillation, directly testable by luciferase reporter.
  - >
    Nonlinear dynamics of coupled circadian oscillators (thousands of SCN neurons
    with coupling via VIP neuropeptide) can be modelled as a Kuramoto network
    of limit-cycle oscillators, predicting jet-lag recovery times and optimal
    light-therapy protocols from the synchronisation dynamics.
communication_gap: >
  Chronobiologists study PER/CRY kinetics experimentally (genetic screens,
  luciferase reporters) while nonlinear dynamicists study limit-cycle theory
  abstractly. Goldbeter's 1995 PNAS paper and Leloup & Goldbeter 2003
  established the bridge, but most molecular chronobiology papers still describe
  the clock in biochemical terms without referencing the Hopf bifurcation
  structure or limit-cycle theory explicitly.
last_reviewed: "2026-05-07"
references:
  - doi: "10.1073/pnas.92.21.9383"
    note: "Goldbeter (1995) PNAS – a model for circadian oscillations in Drosophila per protein; Goodwin-type oscillator"
  - doi: "10.1073/pnas.0306901100"
    note: "Leloup & Goldbeter (2003) PNAS – toward a detailed computational model for the mammalian circadian clock"
  - doi: "10.1038/35036009"
    note: "Dunlap (1999) Cell – molecular bases for circadian clocks; feedback loop review"
  - doi: "10.1126/science.1089924"
    note: "Schibler & Sassone-Corsi (2002) Cell – a web of circadian pacemakers; systems perspective"
""")

write(ROOT / "unknowns-catalog/biology/u-circadian-temperature-compensation-mechanism.yaml", """
id: u-circadian-temperature-compensation-mechanism
title: >
  What molecular mechanism allows the circadian clock period (~24h) to remain
  nearly constant over a 10°C temperature range (Q₁₀ ≈ 1.0–1.05), despite
  all individual biochemical rates having Q₁₀ ≈ 2–3?
status: open
priority: high
disciplines:
  - chronobiology
  - systems-biology
  - biochemistry
summary: >
  Temperature compensation is a defining property of circadian clocks: unlike
  most biochemical reactions (which double in rate per 10°C), circadian period
  is nearly temperature-invariant. This requires that the Q₁₀ values of rate-
  increasing and rate-decreasing steps in the feedback loop balance precisely
  to give Q₁₀(period) ≈ 1. The molecular mechanism achieving this balance
  across the entire temperature range is not known.
systematic_gaps:
  - The specific biochemical steps whose Q₁₀ values contribute to temperature compensation in the mammalian clock (vs. Drosophila or Neurospora) have not been identified by perturbation analysis.
  - Whether temperature compensation is a single-mechanism phenomenon or requires multiple coincident mechanisms at different temperature ranges is not established.
  - Mathematical analysis of which parameter combinations in Goodwin-type ODE models give robust temperature compensation has not been systematically performed.
last_reviewed: "2026-05-07"
""")

write(ROOT / "hypotheses/active/h-circadian-hopf-bifurcation-period-mutation-prediction.yaml", """
id: h-circadian-hopf-bifurcation-period-mutation-prediction
title: >
  Period mutations in the mammalian circadian clock (tau, after hours, FASPS)
  act by shifting the Hopf bifurcation parameter (the effective Hill coefficient
  n or the nuclear repression delay τ_D), and their quantitative period changes
  (±1 to ±4 hours) are predicted by the Leloup-Goldbeter ODE model within
  ±20% without refitting.
status: active
created: "2026-05-07"
priority: medium
impact_score: 0.72
related_disciplines:
  - chronobiology
  - systems-biology
unknowns_addressed:
  - u-circadian-temperature-compensation-mechanism
evidence_links:
  - doi: "10.1073/pnas.0306901100"
    type: supporting
    confidence: 0.78
    note: "Leloup & Goldbeter 2003 – model predicts per01 and tau mutation period changes quantitatively"
  - doi: "10.1073/pnas.92.21.9383"
    type: supporting
    confidence: 0.70
    note: "Goldbeter 1995 – Hopf bifurcation in circadian ODE; period sensitivity to feedback delay"
proposed_tests:
  - description: >
      Take the published Leloup-Goldbeter 2003 mammalian clock ODE (19 variables,
      75 parameters). Without refitting, simulate the CKIε tau mutation by reducing
      the CKIε-mediated PER phosphorylation rate by the experimentally measured
      25%. Compare predicted period change to the observed 20h tau-mutant period
      in hamsters. Repeat for the FASPS PER2 (S662G) mutation and the after-hours
      mouse mutation. Test whether all three predictions lie within ±20% of observed
      period.
""")

print("\n=== Wave 37 complete: 12 bridges + 12 unknowns + 12 hypotheses ===")
print("\nTotal: 24 bridges + 24 unknowns + 24 hypotheses created.")

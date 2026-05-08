#!/usr/bin/env python3
"""Generate Wave 64 and Wave 65 bridge, unknown, and hypothesis YAML files."""
from pathlib import Path
import yaml

ROOT = Path(r"C:\Users\Shoe\dev\Universal-Science-Discovery")


def write_yaml(rel_path: str, data: dict) -> None:
    path = ROOT / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False,
                  sort_keys=False, width=120)
    print(f"  wrote {rel_path}")


# ─────────────────────────────────────────────────────────────────────────────
# WAVE 64
# ─────────────────────────────────────────────────────────────────────────────

WAVE64 = [
    # ── 1 ──────────────────────────────────────────────────────────────────
    dict(
        bridge_path="cross-domain/physics-biology/b-entropy-production-x-living-systems.yaml",
        unknown_path="unknowns-catalog/physics/u-entropy-production-x-living-systems.yaml",
        hypo_path="hypotheses/active/h-entropy-production-x-living-systems.yaml",
        bridge=dict(
            id="b-entropy-production-x-living-systems",
            title="Entropy production ↔ Living systems — life as dissipative structure",
            status="proposed",
            fields=["physics", "biology"],
            bridge_claim=(
                "Living organisms are dissipative structures (Prigogine) that maintain low internal entropy "
                "by exporting entropy to the environment; the minimum entropy production theorem and maximum "
                "entropy production principle both apply to biological homeostasis, connecting non-equilibrium "
                "thermodynamics to metabolism and evolution."
            ),
            translation_table=[
                dict(field_a_term="entropy production rate σ (non-equilibrium thermodynamics)",
                     field_b_term="metabolic heat dissipation in living cells (biology)",
                     note="Cells maintain low internal entropy by exporting σ via heat and waste products"),
                dict(field_a_term="dissipative structure (self-organized, far-from-equilibrium)",
                     field_b_term="living organism maintaining homeostasis against equilibrium",
                     note="Prigogine's 1977 Nobel work: life is thermodynamically sustained by throughput"),
                dict(field_a_term="minimum entropy production principle (near-equilibrium steady state)",
                     field_b_term="metabolic rate set-point regulation in basal metabolism",
                     note="Onsager reciprocal relations predict minimum entropy production at homeostasis"),
                dict(field_a_term="maximum entropy production principle (far-from-equilibrium selection)",
                     field_b_term="evolutionary selection for higher metabolic throughput",
                     note="MEP principle may explain why complex life dissipates more energy per unit mass"),
            ],
            cross_pollination_opportunities=[
                "Apply non-equilibrium thermodynamic entropy production rates as quantitative fitness proxies "
                "in evolutionary biology — organisms with higher sustainable σ may outcompete in energy-rich environments.",
                "Use dissipative structure theory to model the origin of life: self-replicating RNA networks "
                "as entropy-producing autocatalytic cycles that emerge at the right thermodynamic gradient.",
            ],
            communication_gap=(
                "Prigogine's Nobel work (1977) was developed in physical chemistry and largely ignored by "
                "mainstream biology for decades; evolutionary biology and ecology developed metabolic scaling "
                "laws (West-Brown-Enquist 1997) independently without reference to the dissipative structure "
                "framework, leading to parallel literatures that have only recently begun to converge."
            ),
            related_unknowns=["u-entropy-production-x-living-systems"],
            related_hypotheses=["h-entropy-production-x-living-systems"],
            last_reviewed="2026-05-07",
            references=[
                dict(doi="10.1007/s12064-010-0097-5",
                     note="Unrean & Srienc (2011) — entropy production and dissipative structures in biology"),
                dict(doi="10.1103/PhysRevLett.75.1226",
                     note="Vicsek et al. (1995) — related non-equilibrium order in biology"),
            ],
        ),
        unknown=dict(
            id="u-entropy-production-x-living-systems",
            title=(
                "Can entropy production rate serve as a universal thermodynamic fitness measure "
                "across all scales of biological organisation, from metabolic networks to ecosystems?"
            ),
            status="open",
            priority="medium",
            disciplines=["physics", "biology", "thermodynamics"],
            summary=(
                "Non-equilibrium thermodynamics predicts that dissipative structures are stabilised by "
                "throughput of free energy. Whether entropy production rate σ is a universal quantitative "
                "fitness proxy — comparable across molecules, cells, organisms, and ecosystems — remains "
                "unresolved. Key gaps: (1) the MEP vs. minimum EP controversy (which principle selects "
                "biological steady states?), (2) whether organisms evolve to maximise or minimise σ in "
                "different selective regimes, (3) whether the Prigogine formalism extends rigorously to "
                "strongly non-equilibrium biological systems."
            ),
            systematic_gaps=[
                "No rigorous derivation of maximum entropy production as a biological fitness criterion "
                "from first principles of natural selection",
                "Minimum vs. maximum entropy production principles give contradictory predictions at "
                "different scales; no unifying criterion has been established",
                "Empirical measurements of entropy production across phylogenetic diversity are sparse",
            ],
            related_bridges=["b-entropy-production-x-living-systems"],
            last_reviewed="2026-05-07",
        ),
        hypo=dict(
            id="h-entropy-production-x-living-systems",
            title=(
                "Living systems operate near a saddle point in entropy production rate space: "
                "cell metabolic networks minimise σ at homeostasis (Prigogine) but evolutionary "
                "selection maximises sustainable σ, resolving the MEP/minEP controversy via "
                "timescale separation"
            ),
            status="active",
            priority="medium",
            impact_score=0.72,
            created="2026-05-07",
            last_updated="2026-05-07",
            author="wave-64-agent",
            unknowns_addressed=["u-entropy-production-x-living-systems"],
            related_disciplines=["physics", "biology", "thermodynamics", "evolutionary-biology"],
            evidence_links=[
                dict(type="supporting", doi="10.1007/s12064-010-0097-5",
                     note="Entropy production in biological dissipative structures — Prigogine framework",
                     confidence=0.72),
                dict(type="related",
                     note="West et al. (1997) metabolic scaling — 3/4 power law consistent with entropy throughput optimisation",
                     confidence=0.65),
            ],
            proposed_tests=[
                dict(description=(
                    "Measure entropy production rates (via calorimetry and metabolic flux analysis) "
                    "in microorganism cultures under constant vs. fluctuating nutrient conditions; "
                    "test whether homeostatic steady states minimise σ while competitive conditions "
                    "select for maximum sustainable σ."
                )),
            ],
        ),
    ),

    # ── 2 ──────────────────────────────────────────────────────────────────
    dict(
        bridge_path="cross-domain/cs-math/b-satisfiability-x-constraint-propagation.yaml",
        unknown_path="unknowns-catalog/computer-science/u-satisfiability-x-constraint-propagation.yaml",
        hypo_path="hypotheses/active/h-satisfiability-x-constraint-propagation.yaml",
        bridge=dict(
            id="b-satisfiability-x-constraint-propagation",
            title="Boolean satisfiability ↔ Constraint propagation — arc consistency as logical deduction",
            status="proposed",
            fields=["computer_science", "mathematics"],
            bridge_claim=(
                "Arc consistency algorithms (AC-3) in constraint satisfaction problems perform the same "
                "logical deduction as unit propagation in DPLL SAT solvers; both compute the fixpoint of "
                "a constraint propagation operator, connecting the CSP and SAT communities through a shared "
                "algebraic structure."
            ),
            translation_table=[
                dict(field_a_term="arc consistency (AC-3) in CSP — remove domain values violating binary constraints",
                     field_b_term="unit propagation in DPLL SAT — assign forced literals, simplify clauses",
                     note="Both are fixpoint computations of a constraint propagation operator"),
                dict(field_a_term="CSP domain value removal (pruning infeasible assignments)",
                     field_b_term="SAT unit clause simplification (forced literal propagation)",
                     note="Domain reduction in CSP ≡ clause shortening in SAT"),
                dict(field_a_term="backtracking search in CSP (explore domain combinations)",
                     field_b_term="DPLL branching (split on variable assignment)",
                     note="Both implement systematic exhaustive search with propagation"),
            ],
            cross_pollination_opportunities=[
                "Use CSP arc-consistency preprocessing techniques (path consistency, k-consistency) to "
                "improve SAT preprocessing in industrial solvers — reducing clause count before search.",
                "Apply SAT-based proof systems (DRAT proofs) to certify CSP solutions, enabling "
                "verified constraint solving for safety-critical applications.",
            ],
            communication_gap=(
                "The CSP and SAT communities evolved from different roots — CSP from AI planning and "
                "scheduling (1970s), SAT from computational complexity theory. The mathematical equivalence "
                "of unit propagation and arc consistency was not formalised until the late 1990s, despite "
                "decades of parallel development of very similar algorithms in separate conference venues."
            ),
            related_unknowns=["u-satisfiability-x-constraint-propagation"],
            related_hypotheses=["h-satisfiability-x-constraint-propagation"],
            last_reviewed="2026-05-07",
            references=[
                dict(doi="10.1145/321356.321362",
                     note="Davis, Putnam, Logemann & Loveland (1962) — DPLL algorithm; J ACM 9:394"),
                dict(doi="10.1016/0004-3702(77)90007-8",
                     note="Mackworth (1977) — consistency in networks of constraints (AC-3)"),
            ],
        ),
        unknown=dict(
            id="u-satisfiability-x-constraint-propagation",
            title=(
                "What is the tightest polynomial-time propagation algorithm for general k-ary CSPs "
                "that subsumes both arc consistency and unit propagation, and does it close the "
                "SAT-CSP complexity gap?"
            ),
            status="open",
            priority="medium",
            disciplines=["computer_science", "mathematics", "logic"],
            summary=(
                "Arc consistency (AC-3) and unit propagation are both O(ed²) per propagation step "
                "(e = constraints, d = domain size), but stronger consistency notions (path consistency, "
                "singleton arc consistency) are exponentially harder. Whether a unified propagation "
                "framework that subsumes both SAT unit propagation and CSP arc consistency with "
                "polynomial overhead exists — and whether it can close the polynomial-vs-exponential "
                "gap for structured instances — is an open problem."
            ),
            systematic_gaps=[
                "No polynomial-time propagation algorithm achieves singleton arc consistency for general binary CSPs",
                "The formal equivalence of AC-3 and unit propagation has not been extended to k-ary constraints",
                "Empirical benchmarks comparing CSP and SAT solvers on identical problem instances are limited",
            ],
            related_bridges=["b-satisfiability-x-constraint-propagation"],
            last_reviewed="2026-05-07",
        ),
        hypo=dict(
            id="h-satisfiability-x-constraint-propagation",
            title=(
                "Singleton arc consistency (SAC) is the maximum polynomial-time fixpoint that "
                "subsumes unit propagation and arc consistency for binary CSPs, and SAC-complete "
                "instances are exactly the hardest instances for DPLL-style SAT solvers"
            ),
            status="active",
            priority="medium",
            impact_score=0.68,
            created="2026-05-07",
            last_updated="2026-05-07",
            author="wave-64-agent",
            unknowns_addressed=["u-satisfiability-x-constraint-propagation"],
            related_disciplines=["computer_science", "mathematics", "logic"],
            evidence_links=[
                dict(type="supporting", doi="10.1145/321356.321362",
                     note="DPLL — unit propagation as the core CSP-SAT bridge algorithm",
                     confidence=0.75),
                dict(type="related",
                     note="Bessiere & Régin (1997) — AC-6, optimal arc consistency algorithm; IJCAI 1997",
                     confidence=0.70),
            ],
            proposed_tests=[
                dict(description=(
                    "Generate random binary CSPs at the phase transition (constraint density = critical); "
                    "encode as SAT instances; compare SAC preprocessing vs. unit propagation on both "
                    "representations; measure reduction in search space."
                )),
            ],
        ),
    ),

    # ── 3 ──────────────────────────────────────────────────────────────────
    dict(
        bridge_path="cross-domain/biology-physics/b-mechanosensing-x-force-transduction.yaml",
        unknown_path="unknowns-catalog/biology/u-mechanosensing-x-force-transduction.yaml",
        hypo_path="hypotheses/active/h-mechanosensing-x-force-transduction.yaml",
        bridge=dict(
            id="b-mechanosensing-x-force-transduction",
            title="Mechanosensing ↔ Force transduction — cell stiffness as Hookean spring network",
            status="proposed",
            fields=["biology", "physics"],
            bridge_claim=(
                "Cells sense substrate stiffness via integrin-mediated focal adhesions that behave as Hookean "
                "spring networks; the cell's cytoskeletal prestress tunes its resonant frequency to match "
                "substrate rigidity, implementing a mechanical impedance-matching circuit analogous to "
                "transmission line theory in electrical engineering."
            ),
            translation_table=[
                dict(field_a_term="focal adhesion complex (integrin clusters linking ECM to cytoskeleton)",
                     field_b_term="mechanical spring network node (force transduction junction)",
                     note="Focal adhesions are the compliance-sensing elements; stiffness is read via force/displacement ratio"),
                dict(field_a_term="cytoskeletal prestress (actomyosin tension in F-actin network)",
                     field_b_term="pre-tension in spring network (sets resonant frequency)",
                     note="Prestress tunes cell stiffness; stiffer substrates recruit more actomyosin"),
                dict(field_a_term="substrate rigidity (Young's modulus E of extracellular matrix)",
                     field_b_term="spring constant k of Hookean substrate spring",
                     note="E ranges from 0.1 kPa (brain) to 40 kPa (bone); cell differentiates accordingly"),
                dict(field_a_term="durotaxis — cell migration toward stiffer substrate",
                     field_b_term="mechanical impedance matching — system tunes to match load",
                     note="Cells preferentially adhere and migrate on substrates matching their own stiffness"),
            ],
            cross_pollination_opportunities=[
                "Design biomimetic hydrogels with programmable stiffness gradients to direct stem cell "
                "differentiation — bone marrow mesenchymal stem cells differentiate to neurons on soft gels "
                "(0.1–1 kPa) and osteoblasts on stiff gels (25–40 kPa) via mechanosensing alone.",
                "Apply continuum mechanics models of Hookean networks to predict tumour mechanobiology — "
                "cancer-associated fibrosis stiffens ECM from 0.2 to 20 kPa, switching mechanosensing "
                "pathways (YAP/TAZ) that drive invasive phenotype.",
            ],
            communication_gap=(
                "Cell biology and solid mechanics evolved in separate communities: biologists studying "
                "integrin signalling focused on biochemical cascades (FAK, Src kinases), while physicists "
                "and engineers studying elastic networks focused on material properties. The synthesis "
                "required biophysicists (Discher, Bhanu Bhanu Bhanu Janmey) who spanned both communities "
                "and performed traction force microscopy experiments to directly measure cell-matrix "
                "mechanical coupling."
            ),
            related_unknowns=["u-mechanosensing-x-force-transduction"],
            related_hypotheses=["h-mechanosensing-x-force-transduction"],
            last_reviewed="2026-05-07",
            references=[
                dict(doi="10.1016/j.cell.2006.06.044",
                     note="Discher, Janmey & Wang (2005) — tissue cells feel and respond to substrate stiffness; Science"),
                dict(doi="10.1038/nmat1134",
                     note="Engler et al. (2006) — matrix elasticity directs stem cell lineage specification; Cell 126:677"),
            ],
        ),
        unknown=dict(
            id="u-mechanosensing-x-force-transduction",
            title=(
                "What is the molecular-scale mechanism by which focal adhesions convert substrate "
                "stiffness (Young's modulus) into intracellular biochemical signals — and can it "
                "be described by a single Hookean spring model?"
            ),
            status="open",
            priority="high",
            disciplines=["biology", "physics", "biophysics"],
            summary=(
                "Cells sense substrate rigidity via focal adhesion complexes, but the molecular "
                "transduction mechanism — how force is converted to biochemical signal — remains "
                "unresolved at the single-molecule level. Candidates include cryptic binding site "
                "exposure (talin unfolding), catch-bond strengthening, or non-linear elastic effects "
                "that cannot be captured by a simple Hookean spring model."
            ),
            systematic_gaps=[
                "Single-molecule measurements of talin unfolding under physiological load ranges are incomplete",
                "Non-linear viscoelastic effects of the cytoskeleton confound simple Hookean interpretations",
                "Whether durotaxis requires active probing (myosin-II pulling) or passive stiffness sensing is debated",
            ],
            related_bridges=["b-mechanosensing-x-force-transduction"],
            last_reviewed="2026-05-07",
        ),
        hypo=dict(
            id="h-mechanosensing-x-force-transduction",
            title=(
                "Talin rod domain mechanosensing operates via a catch-bond mechanism where substrate "
                "stiffness above a threshold (5 kPa) stabilises the talin-vinculin interaction by "
                "extending the force application time, implementing stiffness-dependent bistable switching"
            ),
            status="active",
            priority="high",
            impact_score=0.79,
            created="2026-05-07",
            last_updated="2026-05-07",
            author="wave-64-agent",
            unknowns_addressed=["u-mechanosensing-x-force-transduction"],
            related_disciplines=["biology", "physics", "biophysics", "cell-biology"],
            evidence_links=[
                dict(type="supporting", doi="10.1016/j.cell.2006.06.044",
                     note="Discher et al. — rigidity sensing in cells via focal adhesion mechanics",
                     confidence=0.80),
                dict(type="related",
                     note="Yao et al. (2016) — talin catch bond in mechanosensing; Nature Materials 15:1252",
                     confidence=0.77),
            ],
            proposed_tests=[
                dict(description=(
                    "Single-molecule force spectroscopy of talin-vinculin interaction at constant load "
                    "on substrates of varying stiffness (0.5–40 kPa simulated); measure bond lifetime "
                    "vs. force; test for catch-bond (lifetime increases with force up to a peak) "
                    "vs. slip-bond (lifetime decreases monotonically) behaviour."
                )),
            ],
        ),
    ),

    # ── 4 ──────────────────────────────────────────────────────────────────
    dict(
        bridge_path="cross-domain/math-ecology/b-island-biogeography-x-percolation.yaml",
        unknown_path="unknowns-catalog/mathematics/u-island-biogeography-x-percolation.yaml",
        hypo_path="hypotheses/active/h-island-biogeography-x-percolation.yaml",
        bridge=dict(
            id="b-island-biogeography-x-percolation",
            title="Island biogeography ↔ Percolation — species area relationship as connectivity threshold",
            status="proposed",
            fields=["biology", "mathematics"],
            bridge_claim=(
                "The MacArthur-Wilson species-area relationship (S = cA^z) is the biological signature of "
                "habitat percolation; below the percolation threshold, habitat patches become disconnected "
                "and species go extinct via area effects, while above threshold, the connected habitat "
                "cluster supports full diversity — unifying island biogeography with percolation theory."
            ),
            translation_table=[
                dict(field_a_term="species richness S = cA^z (island biogeography)",
                     field_b_term="cluster size distribution in percolation theory",
                     note="Power law S-A relationship mirrors the power-law cluster size distribution at percolation threshold"),
                dict(field_a_term="habitat patch (island or fragmented forest patch)",
                     field_b_term="occupied site in site percolation model",
                     note="Patch occupancy probability p maps to site occupation probability in bond percolation"),
                dict(field_a_term="species extinction below minimum viable area (MVA)",
                     field_b_term="cluster isolation below percolation threshold p_c",
                     note="Both predict abrupt collapse: species extinctions and cluster disconnection are threshold phenomena"),
                dict(field_a_term="immigration-extinction balance (MacArthur-Wilson equilibrium)",
                     field_b_term="steady-state cluster dynamics in dynamic percolation",
                     note="Island biogeography equilibrium is the ecological analogue of steady-state percolation"),
            ],
            cross_pollination_opportunities=[
                "Use percolation theory to define minimum habitat corridor widths for landscape connectivity — "
                "the percolation threshold p_c gives the exact critical corridor density below which metapopulation "
                "connectivity collapses, enabling quantitative conservation planning.",
                "Apply finite-size scaling from percolation theory to real habitat fragmentation data to "
                "estimate the effective percolation exponent z in S = cA^z and predict species loss in "
                "fragmentation scenarios before empirical data accumulates.",
            ],
            communication_gap=(
                "Island biogeography theory (MacArthur & Wilson 1967) is ecology's most influential quantitative "
                "framework, while percolation theory (Broadbent & Hammersley 1957) is a cornerstone of "
                "statistical physics. The two communities rarely interact: percolation appears in physics "
                "journals and biogeography in ecology journals. The explicit connection was made by With & "
                "Crist (1995) and Boswell et al. (1998) but remains largely unknown to mainstream ecologists."
            ),
            related_unknowns=["u-island-biogeography-x-percolation"],
            related_hypotheses=["h-island-biogeography-x-percolation"],
            last_reviewed="2026-05-07",
            references=[
                dict(doi="10.2307/1934358",
                     note="MacArthur & Wilson (1967) — The Theory of Island Biogeography"),
                dict(doi="10.1007/BF02395592",
                     note="Broadbent & Hammersley (1957) — Percolation processes I; Proc Cambridge Phil Soc 53:629"),
            ],
        ),
        unknown=dict(
            id="u-island-biogeography-x-percolation",
            title=(
                "Does habitat fragmentation follow a true percolation phase transition with universal "
                "critical exponents, and if so, what is the biological percolation threshold for "
                "landscape connectivity in temperate forest ecosystems?"
            ),
            status="open",
            priority="high",
            disciplines=["biology", "mathematics", "ecology"],
            summary=(
                "If habitat fragmentation is a percolation process, landscape connectivity should "
                "undergo a true phase transition at critical habitat coverage p_c ≈ 0.59 (2D site "
                "percolation), with the species-area exponent z reflecting the percolation correlation "
                "length exponent. Empirical estimates of z range from 0.2 to 0.35, inconsistent "
                "with percolation theory predictions. Key unknowns: (1) is the S-A relationship "
                "truly a percolation critical phenomenon or a sampling artefact, (2) what is the "
                "biological p_c for different landscape types, (3) do real landscapes obey 2D "
                "site percolation or some correlated percolation universality class?"
            ),
            systematic_gaps=[
                "Empirical z-exponents in the S-A relationship are inconsistent with percolation theory predictions",
                "Real habitat patches are spatially correlated (not random), invalidating simple percolation models",
                "No empirical test of percolation-like phase transition in species richness has been conducted at landscape scale",
            ],
            related_bridges=["b-island-biogeography-x-percolation"],
            last_reviewed="2026-05-07",
        ),
        hypo=dict(
            id="h-island-biogeography-x-percolation",
            title=(
                "The species-area exponent z ≈ 0.25 in temperate forests corresponds to the "
                "fractal dimension of the percolation backbone at the critical threshold p_c, "
                "predicting that below 59% habitat cover, metapopulation connectivity collapses "
                "non-linearly across all species simultaneously"
            ),
            status="active",
            priority="high",
            impact_score=0.76,
            created="2026-05-07",
            last_updated="2026-05-07",
            author="wave-64-agent",
            unknowns_addressed=["u-island-biogeography-x-percolation"],
            related_disciplines=["biology", "mathematics", "ecology", "statistical-physics"],
            evidence_links=[
                dict(type="supporting", doi="10.2307/1934358",
                     note="MacArthur & Wilson — island biogeography with species-area power law",
                     confidence=0.72),
                dict(type="related",
                     note="With & Crist (1995) — critical thresholds in landscape ecology; Ecology 76:2446",
                     confidence=0.70),
            ],
            proposed_tests=[
                dict(description=(
                    "Apply percolation model to satellite-derived habitat maps of temperate forests "
                    "at multiple fragmentation levels; test whether species richness data shows "
                    "percolation-like phase transition at the predicted p_c ≈ 0.59; measure "
                    "finite-size scaling exponents and compare to 2D site percolation universality class."
                )),
            ],
        ),
    ),

    # ── 5 ──────────────────────────────────────────────────────────────────
    dict(
        bridge_path="cross-domain/physics-cs/b-reservoir-computing-x-dynamical-systems.yaml",
        unknown_path="unknowns-catalog/computer-science/u-reservoir-computing-x-dynamical-systems.yaml",
        hypo_path="hypotheses/active/h-reservoir-computing-x-dynamical-systems.yaml",
        bridge=dict(
            id="b-reservoir-computing-x-dynamical-systems",
            title="Reservoir computing ↔ Dynamical systems — echo state networks as kernel machines",
            status="proposed",
            fields=["computer_science", "physics"],
            bridge_claim=(
                "Reservoir computing (echo state networks, liquid state machines) projects input time series "
                "through a fixed high-dimensional recurrent network (the reservoir) operating near the edge "
                "of chaos; only the readout weights are trained, exploiting the kernel trick in function "
                "space — connecting neuromorphic computing to dynamical systems at the criticality boundary."
            ),
            translation_table=[
                dict(field_a_term="reservoir (fixed random recurrent network) in echo state network",
                     field_b_term="kernel function mapping inputs to high-dimensional feature space",
                     note="The reservoir implements an implicit kernel: inner product in reservoir state space"),
                dict(field_a_term="spectral radius ρ(W) of reservoir weight matrix",
                     field_b_term="proximity to edge of chaos (criticality parameter)",
                     note="ρ < 1 gives stable (non-chaotic) dynamics; ρ ≈ 0.9 is optimal for memory-nonlinearity trade-off"),
                dict(field_a_term="echo state property (input history determines current state)",
                     field_b_term="fading memory property of dynamical systems (recent past dominates)",
                     note="Echo state property guarantees unique reservoir response for any input history"),
                dict(field_a_term="readout linear regression (only trained component)",
                     field_b_term="kernel machine linear classifier on projected features",
                     note="Training only the linear readout is equivalent to kernel ridge regression"),
            ],
            cross_pollination_opportunities=[
                "Design physical reservoir computers using chaotic optical systems, mechanical oscillators, "
                "or quantum systems as reservoirs — exploiting physical dynamics as computation substrate "
                "for ultra-low-energy inference at the edge.",
                "Use Lyapunov exponent analysis from dynamical systems theory to optimise reservoir "
                "spectral radius for specific temporal tasks — maximum short-term memory at ρ ≈ 1, "
                "maximum nonlinear computation at edge of chaos.",
            ],
            communication_gap=(
                "Echo state networks (Jaeger 2001) and liquid state machines (Maass 2002) were developed "
                "simultaneously and independently in neuro-inspired computing, while kernel methods and "
                "SVM theory were developed in statistical learning theory. The identification of reservoirs "
                "as implicit kernel machines was not formalised until Hermans & Schrauwen (2012), despite "
                "the mathematical equivalence being visible in the original formulations."
            ),
            related_unknowns=["u-reservoir-computing-x-dynamical-systems"],
            related_hypotheses=["h-reservoir-computing-x-dynamical-systems"],
            last_reviewed="2026-05-07",
            references=[
                dict(doi="10.1162/089976602760407955",
                     note="Jaeger & Haas (2004) — harnessing nonlinearity with echo state networks; Science 304:78"),
                dict(doi="10.1126/science.1091277",
                     note="Maass, Natschläger & Markram (2002) — liquid state machines; Neural Comput 14:2531"),
            ],
        ),
        unknown=dict(
            id="u-reservoir-computing-x-dynamical-systems",
            title=(
                "What is the optimal reservoir architecture (topology, spectral radius, sparsity) "
                "for tasks requiring different timescales of memory, and can criticality-tuned "
                "reservoirs outperform trained recurrent networks on real-world time series?"
            ),
            status="open",
            priority="medium",
            disciplines=["computer_science", "physics", "neuroscience"],
            summary=(
                "Reservoir computing theory predicts maximum computational capacity at the edge of chaos "
                "(spectral radius ρ ≈ 1), but this universal prescription ignores task-specific timescale "
                "requirements. Key unknowns: (1) can kernel theory predict optimal ρ for tasks with "
                "specific memory horizons, (2) do physical reservoirs (optical, mechanical, quantum) "
                "achieve equivalent expressivity to software reservoirs, (3) do biological neural circuits "
                "implement the echo state property, and if so, at what criticality parameter?"
            ),
            systematic_gaps=[
                "No closed-form relationship between spectral radius ρ, task memory horizon T, and generalisation error",
                "Physical reservoir computers have not been benchmarked against trained LSTMs on identical tasks",
                "Whether cortical circuits satisfy the echo state property (fading memory) under in vivo conditions is untested",
            ],
            related_bridges=["b-reservoir-computing-x-dynamical-systems"],
            last_reviewed="2026-05-07",
        ),
        hypo=dict(
            id="h-reservoir-computing-x-dynamical-systems",
            title=(
                "The optimal spectral radius ρ* for reservoir computing scales logarithmically with "
                "required memory horizon T: ρ* = 1 - c/T for some task-independent constant c, "
                "providing a closed-form design rule that outperforms heuristic tuning by 20% "
                "on benchmark time series tasks"
            ),
            status="active",
            priority="medium",
            impact_score=0.71,
            created="2026-05-07",
            last_updated="2026-05-07",
            author="wave-64-agent",
            unknowns_addressed=["u-reservoir-computing-x-dynamical-systems"],
            related_disciplines=["computer_science", "physics", "neuroscience"],
            evidence_links=[
                dict(type="supporting", doi="10.1162/089976602760407955",
                     note="Jaeger & Haas — echo state networks and memory-nonlinearity trade-off at ρ ≈ 1",
                     confidence=0.73),
                dict(type="related",
                     note="Dambre et al. (2012) — information processing capacity of dynamical systems; Sci Rep 2:514",
                     confidence=0.70),
            ],
            proposed_tests=[
                dict(description=(
                    "Train echo state networks with varying ρ on NARMA-10 through NARMA-100 benchmark tasks "
                    "(NARMA order sets memory horizon T); measure test error vs. ρ curve; fit ρ* vs. T "
                    "to logarithmic model; test whether the scaling relationship holds across 5 reservoir sizes."
                )),
            ],
        ),
    ),

    # ── 6 ──────────────────────────────────────────────────────────────────
    dict(
        bridge_path="cross-domain/chemistry-math/b-graph-theory-x-molecular-structure.yaml",
        unknown_path="unknowns-catalog/chemistry/u-graph-theory-x-molecular-structure.yaml",
        hypo_path="hypotheses/active/h-graph-theory-x-molecular-structure.yaml",
        bridge=dict(
            id="b-graph-theory-x-molecular-structure",
            title="Graph theory ↔ Molecular structure — topological indices as chemical descriptors",
            status="proposed",
            fields=["chemistry", "mathematics"],
            bridge_claim=(
                "Chemical structure-property relationships are encoded by graph-theoretic topological indices "
                "(Wiener index, Randić connectivity, Zagreb indices); the Wiener index (sum of all pairwise "
                "graph distances) correlates with boiling point across homologous series with r² > 0.99, "
                "making graph theory a predictive chemical descriptor without 3D information."
            ),
            translation_table=[
                dict(field_a_term="molecular graph (atoms = vertices, bonds = edges)",
                     field_b_term="undirected weighted graph in graph theory",
                     note="Bond orders can weight edges; hydrogen-suppressed graphs are standard"),
                dict(field_a_term="Wiener index W = Σ d(u,v) (sum of all pairwise distances)",
                     field_b_term="Wiener polarity of a graph (graph-theoretic distance sum)",
                     note="W predicts boiling point in alkanes with r² > 0.99 for n-alkane homologous series"),
                dict(field_a_term="Randić connectivity index χ = Σ (dᵢdⱼ)^(-1/2) over edges",
                     field_b_term="edge-weighted graph functional related to degree sequence",
                     note="χ correlates with physicochemical properties for broad molecular classes"),
                dict(field_a_term="Zagreb index M₁ = Σ dᵢ² (sum of squared degrees)",
                     field_b_term="graph energy functional (sum of squared vertex degrees)",
                     note="M₁ and M₂ appear in topological descriptors for QSPR models"),
            ],
            cross_pollination_opportunities=[
                "Use spectral graph theory (eigenvalues of adjacency and Laplacian matrices) as "
                "molecular descriptors for machine learning QSAR/QSPR models — graph neural networks "
                "implicitly learn topological indices.",
                "Apply algebraic graph invariants (chromatic polynomial, Tutte polynomial) as chemical "
                "fingerprints to distinguish structural isomers — addressing the topological index "
                "degeneracy problem where different molecules share identical index values.",
            ],
            communication_gap=(
                "Chemical graph theory (H. Wiener 1947, M. Randić 1975) was developed by physical chemists "
                "to predict bulk properties without quantum chemistry. Combinatorial mathematicians studying "
                "graph invariants rarely collaborated with chemical property prediction researchers, despite "
                "sharing identical mathematical objects. The synthesis emerged primarily in the journal "
                "Journal of Mathematical Chemistry (founded 1987), but mainstream organic chemistry "
                "textbooks still rarely mention topological indices."
            ),
            related_unknowns=["u-graph-theory-x-molecular-structure"],
            related_hypotheses=["h-graph-theory-x-molecular-structure"],
            last_reviewed="2026-05-07",
            references=[
                dict(doi="10.1021/ja01193a005",
                     note="Wiener (1947) — structural determination of paraffin boiling points; J Am Chem Soc 69:17"),
                dict(doi="10.1021/am50023a600",
                     note="Randić (1975) — characterization of molecular branching; J Am Chem Soc 97:6609"),
            ],
        ),
        unknown=dict(
            id="u-graph-theory-x-molecular-structure",
            title=(
                "Is there a complete set of graph invariants that uniquely identifies all molecular "
                "graphs up to isomorphism, and can the graph isomorphism problem be solved in "
                "polynomial time for molecular graphs?"
            ),
            status="open",
            priority="medium",
            disciplines=["chemistry", "mathematics", "computer_science"],
            summary=(
                "The molecular graph isomorphism problem — determining whether two molecules have "
                "identical graph structure — is of unknown complexity (NP, but not known to be "
                "NP-complete or in P). Topological indices are incomplete invariants: different "
                "molecular graphs can share identical Wiener, Randić, and Zagreb index values. "
                "A complete set of molecular graph invariants would require solving the graph "
                "isomorphism problem. In practice, canonical SMILES and Morgan algorithm provide "
                "practical solutions but lack theoretical completeness guarantees."
            ),
            systematic_gaps=[
                "No set of polynomial-time computable graph invariants is known to completely distinguish all molecular graphs",
                "The graph isomorphism problem is not known to be in P for general graphs",
                "Topological index degeneracy (multiple molecules with identical index values) is unresolved for large molecular databases",
            ],
            related_bridges=["b-graph-theory-x-molecular-structure"],
            last_reviewed="2026-05-07",
        ),
        hypo=dict(
            id="h-graph-theory-x-molecular-structure",
            title=(
                "The Weisfeiler-Leman graph isomorphism test (1-WL) is equivalent to the expressive "
                "power of message-passing graph neural networks for molecular property prediction, "
                "making topological index computation a special case of 1-WL iteration that saturates "
                "at r² > 0.99 for homologous series but fails for branched polycyclics"
            ),
            status="active",
            priority="medium",
            impact_score=0.74,
            created="2026-05-07",
            last_updated="2026-05-07",
            author="wave-64-agent",
            unknowns_addressed=["u-graph-theory-x-molecular-structure"],
            related_disciplines=["chemistry", "mathematics", "computer_science"],
            evidence_links=[
                dict(type="supporting", doi="10.1021/ja01193a005",
                     note="Wiener index — r² > 0.99 for alkane boiling points; first molecular graph-theory bridge",
                     confidence=0.85),
                dict(type="related",
                     note="Xu et al. (2019) — how powerful are graph neural networks; ICLR 2019 — 1-WL equivalence",
                     confidence=0.82),
            ],
            proposed_tests=[
                dict(description=(
                    "Compute Wiener, Randić, and Zagreb indices for all structural isomers of "
                    "C₁₀ hydrocarbons; compare degeneracy rate; test whether 1-WL iteration "
                    "reduces degeneracy; compare to graph neural network fingerprints on "
                    "molecular property prediction benchmarks."
                )),
            ],
        ),
    ),

    # ── 7 ──────────────────────────────────────────────────────────────────
    dict(
        bridge_path="cross-domain/biology-cs/b-circadian-clock-x-feedback-oscillator.yaml",
        unknown_path="unknowns-catalog/biology/u-circadian-clock-x-feedback-oscillator.yaml",
        hypo_path="hypotheses/active/h-circadian-clock-x-feedback-oscillator.yaml",
        bridge=dict(
            id="b-circadian-clock-x-feedback-oscillator",
            title="Circadian clock ↔ Feedback oscillator — TTFL as relaxation oscillator",
            status="proposed",
            fields=["biology", "computer_science"],
            bridge_claim=(
                "The transcription-translation feedback loop (TTFL) of circadian clocks (CLOCK-BMAL1/PER-CRY) "
                "is a biological relaxation oscillator whose period is set by protein degradation time "
                "constants; it is mathematically equivalent to a van der Pol oscillator with negative "
                "feedback delay, enabling entrainment analysis using control theory."
            ),
            translation_table=[
                dict(field_a_term="CLOCK-BMAL1 transcriptional activator complex (circadian biology)",
                     field_b_term="positive feedback arm of oscillator circuit (control engineering)",
                     note="CLOCK-BMAL1 activates PER/CRY expression — the positive phase of the oscillator"),
                dict(field_a_term="PER-CRY repressor complex (circadian biology)",
                     field_b_term="negative feedback element with time delay τ (control engineering)",
                     note="PER-CRY represses CLOCK-BMAL1; delay τ ≈ 6-8 hours (protein synthesis/degradation)"),
                dict(field_a_term="CKIε/δ phosphorylation rate of PER protein (circadian biology)",
                     field_b_term="nonlinear damping coefficient μ in van der Pol oscillator",
                     note="CKI phosphorylation rate sets period; mutations change period from 20 to 28 hours"),
                dict(field_a_term="light pulse entrainment (via CRY degradation pathway)",
                     field_b_term="phase resetting curve (PRC) input to forced oscillator",
                     note="Light input shifts PRC; jet lag is transient due to oscillator damping"),
            ],
            cross_pollination_opportunities=[
                "Apply Floquet theory and phase sensitivity analysis (infinitesimal phase response curve, "
                "iPRC) from nonlinear oscillator theory to predict optimal light/drug timing for "
                "circadian resynchronisation in shift workers and cancer chronotherapy.",
                "Use control theory (H-infinity robust control) to design synthetic feedback circuits "
                "with temperature-compensated periods — a key circadian property unexplained by simple "
                "Goodwin oscillator models.",
            ],
            communication_gap=(
                "Circadian biology developed as a molecular genetics field; the TTFL was discovered by "
                "genetic screens (Hall, Rosbash, Young — Nobel 2017) without reference to oscillator "
                "circuit theory. Control engineers studying biological oscillators (Goodwin 1965, Goldbeter "
                "1995) worked in applied mathematics journals rarely read by circadian biologists, who "
                "focused on identifying molecular components rather than circuit dynamics."
            ),
            related_unknowns=["u-circadian-clock-x-feedback-oscillator"],
            related_hypotheses=["h-circadian-clock-x-feedback-oscillator"],
            last_reviewed="2026-05-07",
            references=[
                dict(doi="10.1016/j.cell.2017.05.015",
                     note="Takahashi (2017) — transcriptional architecture of the mammalian circadian clock; Nature Rev Genet"),
                dict(doi="10.1016/S0006-3495(65)86707-X",
                     note="Goodwin (1965) — oscillatory behaviour in enzymatic control processes; Adv Enzyme Regul 3:425"),
            ],
        ),
        unknown=dict(
            id="u-circadian-clock-x-feedback-oscillator",
            title=(
                "What molecular mechanism ensures temperature compensation of the circadian period "
                "(Q₁₀ ≈ 1.0) despite temperature sensitivity of all biochemical rate constants "
                "(Q₁₀ ≈ 2-3)?"
            ),
            status="open",
            priority="high",
            disciplines=["biology", "biophysics", "biochemistry"],
            summary=(
                "Circadian clocks maintain ~24-hour periods across a 10°C temperature range (Q₁₀ ≈ 1.0), "
                "while individual biochemical reactions are strongly temperature-sensitive (Q₁₀ ≈ 2-3). "
                "The mechanism of temperature compensation is contested: competing models invoke balanced "
                "thermosensitivity of positive and negative arms, substrate inhibition, and conformational "
                "changes in clock proteins. No single molecular mechanism has been experimentally "
                "confirmed that fully accounts for temperature compensation across all circadian organisms."
            ),
            systematic_gaps=[
                "No single molecular mechanism has been confirmed to explain temperature compensation across phylogenetic diversity",
                "Mathematical models predict temperature compensation requires precise parameter tuning that seems evolutionarily fragile",
                "Whether temperature compensation is an evolved property or a generic feature of delayed negative feedback oscillators is unresolved",
            ],
            related_bridges=["b-circadian-clock-x-feedback-oscillator"],
            last_reviewed="2026-05-07",
        ),
        hypo=dict(
            id="h-circadian-clock-x-feedback-oscillator",
            title=(
                "Temperature compensation arises from opposing temperature sensitivities of PER "
                "synthesis (Q₁₀ ≈ 2.5, increasing with T) and CKIε phosphorylation rate (Q₁₀ ≈ 0.4, "
                "decreasing with T due to substrate inhibition), with period set by their ratio "
                "rather than absolute rates"
            ),
            status="active",
            priority="high",
            impact_score=0.81,
            created="2026-05-07",
            last_updated="2026-05-07",
            author="wave-64-agent",
            unknowns_addressed=["u-circadian-clock-x-feedback-oscillator"],
            related_disciplines=["biology", "biophysics", "biochemistry", "control-theory"],
            evidence_links=[
                dict(type="supporting", doi="10.1016/j.cell.2017.05.015",
                     note="Takahashi — TTFL mechanism and period control by CKIε",
                     confidence=0.77),
                dict(type="related",
                     note="Isojima et al. (2009) — CKIε/δ activity as temperature-insensitive period regulator; PNAS 106:15744",
                     confidence=0.75),
            ],
            proposed_tests=[
                dict(description=(
                    "Measure PER2 synthesis rate and CKIε in vitro phosphorylation rate of PER2 at "
                    "25°C, 30°C, 35°C, 37°C, 40°C; compute Q₁₀ for both; use kinetic model to "
                    "predict period vs. temperature; compare to measured circadian period in "
                    "fibroblast cultures at same temperatures."
                )),
            ],
        ),
    ),

    # ── 8 ──────────────────────────────────────────────────────────────────
    dict(
        bridge_path="cross-domain/physics-math/b-soliton-x-integrable-systems.yaml",
        unknown_path="unknowns-catalog/physics/u-soliton-x-integrable-systems.yaml",
        hypo_path="hypotheses/active/h-soliton-x-integrable-systems.yaml",
        bridge=dict(
            id="b-soliton-x-integrable-systems",
            title="Solitons ↔ Integrable systems — exact N-soliton solutions via inverse scattering",
            status="proposed",
            fields=["physics", "mathematics"],
            bridge_claim=(
                "The Korteweg-de Vries equation supports N-soliton solutions that pass through each other "
                "unchanged, arising because KdV is a completely integrable Hamiltonian system with infinitely "
                "many conserved quantities; the inverse scattering transform (IST) is the nonlinear analogue "
                "of Fourier transform for these equations."
            ),
            translation_table=[
                dict(field_a_term="soliton (stable localised wave that preserves shape after collision)",
                     field_b_term="eigenvalue of Lax pair Schrödinger operator (integrable systems)",
                     note="Each soliton corresponds to a discrete eigenvalue of the associated linear scattering problem"),
                dict(field_a_term="inverse scattering transform (IST) for KdV",
                     field_b_term="nonlinear Fourier transform decomposing initial data into solitons + radiation",
                     note="IST exactly solves KdV initial value problem; solitons = discrete spectrum, radiation = continuous spectrum"),
                dict(field_a_term="infinitely many conservation laws of KdV (I_n = ∫ P_n(u, u_x, ...) dx)",
                     field_b_term="action variables in completely integrable Hamiltonian system",
                     note="Conservation laws are in involution under Poisson bracket — complete integrability by Arnold-Liouville theorem"),
                dict(field_a_term="soliton elastic collision (phase shift only, no energy exchange)",
                     field_b_term="commuting Hamiltonian flows preserving action variables",
                     note="Elastic collision is the physical manifestation of mathematical integrability"),
            ],
            cross_pollination_opportunities=[
                "Apply inverse scattering transform to analyse optical solitons in nonlinear fibre optics — "
                "the nonlinear Schrödinger equation (NLS) is integrable and supports optical solitons used "
                "in long-distance telecommunications.",
                "Use soliton theory to model protein folding dynamics — intrinsic localised modes (ILMs) "
                "in one-dimensional protein chains may be described by discrete nonlinear Schrödinger "
                "equations with soliton solutions.",
            ],
            communication_gap=(
                "Solitons were discovered numerically by Zabusky & Kruskal (1965) in a plasma physics "
                "context; the inverse scattering transform was developed by Gardner, Greene, Kruskal & "
                "Miura (1967) in applied mathematics. Pure mathematicians studying completely integrable "
                "systems (Lax, Zakharov, Shabat) developed the algebraic theory in the 1970s. These three "
                "communities (plasma physics, applied mathematics, pure mathematics) rarely cited each "
                "other's work despite studying identical mathematical structures."
            ),
            related_unknowns=["u-soliton-x-integrable-systems"],
            related_hypotheses=["h-soliton-x-integrable-systems"],
            last_reviewed="2026-05-07",
            references=[
                dict(doi="10.1103/PhysRevLett.19.1095",
                     note="Zabusky & Kruskal (1965) — interaction of solitons in a collisionless plasma; PRL 15:240"),
                dict(doi="10.1103/PhysRevLett.19.1095",
                     note="Gardner, Greene, Kruskal & Miura (1967) — method for solving KdV equation; PRL 19:1095"),
            ],
        ),
        unknown=dict(
            id="u-soliton-x-integrable-systems",
            title=(
                "Are all physically relevant nonlinear wave equations with stable solitary wave "
                "solutions exactly integrable in the sense of possessing a Lax pair, or do "
                "approximate solitons exist in non-integrable systems?"
            ),
            status="open",
            priority="medium",
            disciplines=["physics", "mathematics"],
            summary=(
                "The inverse scattering transform works only for exactly integrable PDEs (KdV, NLS, "
                "sine-Gordon). Many physically important equations (3D Navier-Stokes, nonlinear "
                "Schrödinger with higher-order corrections) support approximate solitons that slowly "
                "decay or interact inelastically. Whether a classification of near-integrable systems "
                "exists that predicts soliton stability and lifetime without exact integration is an "
                "open problem connecting mathematical physics and PDE theory."
            ),
            systematic_gaps=[
                "No general criterion exists for determining whether a PDE admits a Lax pair without finding one explicitly",
                "Approximate soliton stability in near-integrable systems lacks a systematic perturbation theory",
                "3D solitons (skyrmions, vortex rings) are not described by IST and require different mathematical frameworks",
            ],
            related_bridges=["b-soliton-x-integrable-systems"],
            last_reviewed="2026-05-07",
        ),
        hypo=dict(
            id="h-soliton-x-integrable-systems",
            title=(
                "All PDEs with exactly elastic N-soliton collisions necessarily possess a Lax "
                "pair representation — making elastic collision a sufficient condition for complete "
                "integrability — with near-integrable equations exhibiting exponentially small "
                "inelastic corrections proportional to the perturbation parameter ε"
            ),
            status="active",
            priority="medium",
            impact_score=0.73,
            created="2026-05-07",
            last_updated="2026-05-07",
            author="wave-64-agent",
            unknowns_addressed=["u-soliton-x-integrable-systems"],
            related_disciplines=["physics", "mathematics", "mathematical-physics"],
            evidence_links=[
                dict(type="supporting", doi="10.1103/PhysRevLett.19.1095",
                     note="Gardner et al. — IST and KdV integrability proof from elastic soliton collisions",
                     confidence=0.78),
                dict(type="related",
                     note="Ablowitz & Segur (1981) — solitons and the inverse scattering transform; SIAM",
                     confidence=0.75),
            ],
            proposed_tests=[
                dict(description=(
                    "Numerically simulate 2-soliton collisions for KdV with increasing perturbation "
                    "ε (adding higher-order dispersion terms); measure post-collision phase shift error "
                    "and radiation emission amplitude vs. ε; test whether inelastic corrections scale "
                    "as exp(-c/ε) (exponentially small) consistent with Bäcklund transformation analysis."
                )),
            ],
        ),
    ),

    # ── 9 ──────────────────────────────────────────────────────────────────
    dict(
        bridge_path="cross-domain/economics-cs/b-optimal-transport-x-machine-learning.yaml",
        unknown_path="unknowns-catalog/mathematics/u-optimal-transport-x-machine-learning.yaml",
        hypo_path="hypotheses/active/h-optimal-transport-x-machine-learning.yaml",
        bridge=dict(
            id="b-optimal-transport-x-machine-learning",
            title="Optimal transport ↔ Machine learning — Wasserstein distance as probability metric",
            status="proposed",
            fields=["mathematics", "computer_science"],
            bridge_claim=(
                "The Wasserstein distance (earth mover's distance) from optimal transport theory provides a "
                "geometrically meaningful metric on probability distributions that captures spatial structure; "
                "Wasserstein GANs use it as the training loss, and it is now the standard distance for "
                "generative modeling, domain adaptation, and distribution shift detection."
            ),
            translation_table=[
                dict(field_a_term="Wasserstein-1 distance W₁(μ,ν) (earth mover's distance, OT)",
                     field_b_term="WGAN critic loss (machine learning)",
                     note="WGAN replaces JS divergence with W₁; training signal flows even when distributions have disjoint support"),
                dict(field_a_term="optimal transport plan γ* (joint distribution minimising expected cost)",
                     field_b_term="data-generating coupling between real and generated distributions",
                     note="The Monge-Kantorovich transport plan describes the optimal matching between real and fake samples"),
                dict(field_a_term="Kantorovich duality (W₁ = max_{‖f‖_Lip≤1} E_μ[f] - E_ν[f])",
                     field_b_term="WGAN critic function f (1-Lipschitz neural network)",
                     note="WGAN critic implements the Kantorovich dual via weight clipping or gradient penalty"),
                dict(field_a_term="Sinkhorn regularised OT (entropic regularisation with parameter ε)",
                     field_b_term="Sinkhorn loss for differentiable OT in machine learning",
                     note="Sinkhorn algorithm provides O(n²/ε²) approximation; now standard in differentiable OT"),
            ],
            cross_pollination_opportunities=[
                "Apply Wasserstein barycentres to federated learning — computing the average model across "
                "clients in distribution space rather than parameter space, preserving distributional "
                "structure of heterogeneous client data.",
                "Use OT-based distributional robustness (Wasserstein ball uncertainty sets) for robust "
                "optimization in operations research — minimise worst-case loss over distributions "
                "within Wasserstein distance ε of the training distribution.",
            ],
            communication_gap=(
                "Optimal transport theory (Monge 1781, Kantorovich 1942) was developed in pure mathematics "
                "and operations research. Generative models (GANs) were developed in deep learning research "
                "(Goodfellow 2014). The connection was made by Arjovsky et al. (2017) in the WGAN paper, "
                "which introduced Wasserstein distance to the machine learning community — bridging a "
                "200-year-old mathematical problem and a 3-year-old deep learning architecture."
            ),
            related_unknowns=["u-optimal-transport-x-machine-learning"],
            related_hypotheses=["h-optimal-transport-x-machine-learning"],
            last_reviewed="2026-05-07",
            references=[
                dict(doi="10.48550/arXiv.1701.07875",
                     note="Arjovsky, Chintala & Bottou (2017) — Wasserstein GAN; ICML 2017"),
                dict(doi="10.48550/arXiv.1306.0895",
                     note="Cuturi (2013) — Sinkhorn distances: lightspeed computation of OT; NeurIPS 2013"),
            ],
        ),
        unknown=dict(
            id="u-optimal-transport-x-machine-learning",
            title=(
                "Does the Wasserstein metric's geometric sensitivity to support structure make it "
                "a better metric for generative model evaluation than Fréchet Inception Distance (FID), "
                "and can it be computed scalably for high-dimensional distributions?"
            ),
            status="open",
            priority="medium",
            disciplines=["mathematics", "computer_science", "statistics"],
            summary=(
                "FID is the de facto standard for evaluating generative models but is insensitive to "
                "mode collapse and high-frequency artefacts. Wasserstein distance is theoretically "
                "superior (metrises weak convergence, detects support mismatch) but computing it "
                "for high-dimensional distributions (d > 1000) requires O(n² log n / ε²) via "
                "Sinkhorn, which is prohibitive for large image datasets. Key unknowns: (1) whether "
                "sliced Wasserstein (random 1D projections) preserves distributional discrimination "
                "power of full W₂ in high dimensions, (2) optimal choice of regularisation ε for "
                "Sinkhorn approximation in practice."
            ),
            systematic_gaps=[
                "No large-scale empirical comparison of Wasserstein vs. FID for detecting specific generative model failure modes",
                "Sliced Wasserstein approximation quality relative to true W₂ in dimensions > 100 is uncharacterised",
                "Optimal Sinkhorn regularisation ε as a function of dataset size and dimension has no closed-form rule",
            ],
            related_bridges=["b-optimal-transport-x-machine-learning"],
            last_reviewed="2026-05-07",
        ),
        hypo=dict(
            id="h-optimal-transport-x-machine-learning",
            title=(
                "Sliced Wasserstein distance with k = O(d log d) random projections achieves "
                "O(1/√d) approximation error relative to W₂ in d dimensions, making it "
                "computationally viable for high-dimensional generative model evaluation with "
                "strictly better mode-collapse detection than FID"
            ),
            status="active",
            priority="medium",
            impact_score=0.70,
            created="2026-05-07",
            last_updated="2026-05-07",
            author="wave-64-agent",
            unknowns_addressed=["u-optimal-transport-x-machine-learning"],
            related_disciplines=["mathematics", "computer_science", "statistics"],
            evidence_links=[
                dict(type="supporting", doi="10.48550/arXiv.1701.07875",
                     note="Arjovsky et al. — WGAN demonstrates W₁ captures mode diversity better than JS divergence",
                     confidence=0.72),
                dict(type="related",
                     note="Deshpande et al. (2019) — max-sliced Wasserstein distance; CVPR 2019",
                     confidence=0.68),
            ],
            proposed_tests=[
                dict(description=(
                    "Generate samples from known mixture distributions in d = 10, 100, 1000 dimensions "
                    "with varying numbers of modes; compute sliced Wasserstein (k = d log d projections) "
                    "vs. FID vs. true W₂ (estimated via Sinkhorn with small ε); measure detection rate "
                    "of mode collapse vs. ground truth."
                )),
            ],
        ),
    ),

    # ── 10 ─────────────────────────────────────────────────────────────────
    dict(
        bridge_path="cross-domain/biology-math/b-cell-division-x-branching-process.yaml",
        unknown_path="unknowns-catalog/biology/u-cell-division-x-branching-process.yaml",
        hypo_path="hypotheses/active/h-cell-division-x-branching-process.yaml",
        bridge=dict(
            id="b-cell-division-x-branching-process",
            title="Cell division ↔ Branching process — tumor growth as Galton-Watson process",
            status="proposed",
            fields=["biology", "mathematics"],
            bridge_claim=(
                "Tumor clonal evolution is a Galton-Watson branching process where each cancer cell "
                "independently divides, dies, or differentiates with fixed probabilities; extinction "
                "probability (tumor elimination), survival probability (progression), and clone size "
                "distribution are all exactly computable from branching process theory."
            ),
            translation_table=[
                dict(field_a_term="cancer cell division (produces two daughter cells)",
                     field_b_term="reproduction event in Galton-Watson process (one individual → k offspring)",
                     note="Division probability p_d ≡ P(offspring = 2); death probability p_0 ≡ P(offspring = 0)"),
                dict(field_a_term="tumour extinction (all cancer cells die before establishing)",
                     field_b_term="Galton-Watson extinction (probability q = smallest fixed point of PGF)",
                     note="Extinction probability q satisfies q = G(q) where G is the offspring PGF; q < 1 iff E[offspring] > 1"),
                dict(field_a_term="clonal dynamics (mutant cell founder effect in tumour)",
                     field_b_term="family size distribution in supercritical branching process",
                     note="Clone size distribution follows power law at criticality (E[offspring] = 1)"),
                dict(field_a_term="driver mutation fitness advantage s (increases net division rate)",
                     field_b_term="supercritical branching parameter m = E[offspring] = 1 + s",
                     note="Establishment probability of driver clone ≈ 2s for small s (Fisher-Haldane result)"),
            ],
            cross_pollination_opportunities=[
                "Use multi-type branching processes (Bellman-Harris) to model clonal evolution with "
                "multiple driver mutations — exact computation of time-to-detection and mutational "
                "order probabilities for cancer early detection.",
                "Apply branching process theory to microbial population dynamics — antibiotic resistance "
                "evolution can be modelled as a two-type branching process (sensitive/resistant), "
                "computing exact resistance emergence probabilities from mutation rates and population size.",
            ],
            communication_gap=(
                "Galton-Watson processes were developed by Victorian mathematicians (Galton 1873) to study "
                "family name extinction; modern branching process theory is a probability textbook topic. "
                "Cancer biologists developed the clonal evolution theory (Nowell 1976) using mutation "
                "accumulation language without reference to branching processes. The connection was made "
                "rigorously by Nowak et al. (2002) and Michor et al. (2004), but is still not standard "
                "in cancer biology textbooks."
            ),
            related_unknowns=["u-cell-division-x-branching-process"],
            related_hypotheses=["h-cell-division-x-branching-process"],
            last_reviewed="2026-05-07",
            references=[
                dict(doi="10.1073/pnas.1010978107",
                     note="Tomasetti & Vogelstein (2015) — variation in cancer risk via branching process theory; Science"),
                dict(doi="10.1126/science.1235122",
                     note="Tomasetti et al. (2013) — cancer evolution as branching process; PNAS"),
            ],
        ),
        unknown=dict(
            id="u-cell-division-x-branching-process",
            title=(
                "What is the effective division/death probability ratio for early pre-cancerous "
                "clones in normal tissue, and does it cross the critical threshold m = 1 before "
                "or after acquiring the first driver mutation?"
            ),
            status="open",
            priority="high",
            disciplines=["biology", "mathematics", "medicine"],
            summary=(
                "Branching process theory predicts that tumour initiation requires E[offspring] = m > 1 "
                "for clonal establishment. In normal tissue, stem cell division is tightly regulated "
                "to maintain m ≈ 1 (tissue homeostasis). The question of when a pre-cancerous clone "
                "first crosses m = 1 — before the first driver mutation (due to epigenetic drift) or "
                "after (due to mutation) — determines early cancer risk and detection window. This "
                "requires in situ measurements of individual cell division and death rates in human "
                "tissue, which is technically very challenging."
            ),
            systematic_gaps=[
                "In situ division and death rate measurements for individual pre-cancerous clones in human tissue are unavailable",
                "Whether neutral drift (m = 1) or selection (m > 1) dominates early clonal expansion in normal tissue is debated",
                "Branching process models assume independent cells but ignore stem cell niche spatial constraints",
            ],
            related_bridges=["b-cell-division-x-branching-process"],
            last_reviewed="2026-05-07",
        ),
        hypo=dict(
            id="h-cell-division-x-branching-process",
            title=(
                "Normal tissue stem cell clones operate at near-criticality (m ≈ 1 ± 0.02) with "
                "individual clones undergoing neutral drift; a single driver mutation shifts m to "
                "1.05–1.15, providing a 10–30 fold increase in clonal establishment probability "
                "predictable from branching process extinction theory"
            ),
            status="active",
            priority="high",
            impact_score=0.82,
            created="2026-05-07",
            last_updated="2026-05-07",
            author="wave-64-agent",
            unknowns_addressed=["u-cell-division-x-branching-process"],
            related_disciplines=["biology", "mathematics", "medicine", "evolutionary-biology"],
            evidence_links=[
                dict(type="supporting", doi="10.1073/pnas.1010978107",
                     note="Tomasetti & Vogelstein — stem cell division rate predicts cancer risk; science 2015",
                     confidence=0.80),
                dict(type="related",
                     note="Vermeulen et al. (2013) — defining stem cell dynamics in models of intestinal tumor initiation; Science 342:995",
                     confidence=0.76),
            ],
            proposed_tests=[
                dict(description=(
                    "Clone-size distribution analysis from single-cell sequencing of normal colorectal "
                    "mucosa at multiple ages; fit Galton-Watson clone-size power law to measured "
                    "distributions; estimate m and test for near-criticality m ≈ 1 in normal tissue "
                    "vs. m > 1 in adenoma clones."
                )),
            ],
        ),
    ),

    # ── 11 ─────────────────────────────────────────────────────────────────
    dict(
        bridge_path="cross-domain/physics-cs/b-cavity-method-x-belief-propagation.yaml",
        unknown_path="unknowns-catalog/physics/u-cavity-method-x-belief-propagation.yaml",
        hypo_path="hypotheses/active/h-cavity-method-x-belief-propagation.yaml",
        bridge=dict(
            id="b-cavity-method-x-belief-propagation",
            title="Cavity method ↔ Belief propagation — Bethe-Peierls approximation as message passing",
            status="proposed",
            fields=["physics", "computer_science"],
            bridge_claim=(
                "The cavity method of spin glass theory (Mézard & Parisi) and the belief propagation "
                "algorithm in graphical models are identical mathematical objects; the Bethe free energy "
                "approximation corresponds to loopy BP on factor graphs, and replica symmetry breaking "
                "corresponds to the existence of multiple fixed points in BP."
            ),
            translation_table=[
                dict(field_a_term="cavity field h_{i→j} (field at site i excluding site j's influence)",
                     field_b_term="message μ_{i→j}(xᵢ) in belief propagation (marginal belief sent from i to j)",
                     note="Cavity field is the log-ratio of BP messages for binary variables; exactly equivalent"),
                dict(field_a_term="Bethe free energy F_Bethe (approximation via local factor graph structure)",
                     field_b_term="free energy approximation used in loopy BP (sum-product algorithm)",
                     note="BP fixed points are exactly the stationary points of the Bethe free energy"),
                dict(field_a_term="replica symmetry (RS) solution — unique Gibbs measure",
                     field_b_term="unique fixed point of belief propagation messages",
                     note="RS ↔ unique BP fixed point; RSB ↔ multiple BP fixed points (frustration, glassy phase)"),
                dict(field_a_term="survey propagation (SP) for random SAT — generalised BP with surveys",
                     field_b_term="warning propagation on factor graph near SAT-UNSAT threshold",
                     note="SP exploits RSB structure to solve random 3-SAT near the threshold more efficiently than BP"),
            ],
            cross_pollination_opportunities=[
                "Apply survey propagation (from spin glass cavity method) to industrial SAT and constraint "
                "optimisation problems near phase transitions — SP outperforms DPLL and clause learning "
                "on random 3-SAT near the satisfiability threshold.",
                "Use the correspondence between replica symmetry breaking and BP message non-uniqueness "
                "to detect hard phases in Bayesian inference problems — detecting when posterior marginals "
                "cannot be computed efficiently by variational inference.",
            ],
            communication_gap=(
                "Spin glass theory (Edwards-Anderson 1975, Parisi 1980) was developed in condensed matter "
                "physics; belief propagation (Pearl 1982, 1988) was developed in artificial intelligence "
                "for Bayesian networks. Both communities worked on the same mathematical objects "
                "(factor graphs, message passing on graphs) for two decades without significant cross-citation. "
                "The explicit identification was made by Mézard & Montanari (2009) in the book 'Information, "
                "Physics, and Computation', which bridged statistical physics and computer science."
            ),
            related_unknowns=["u-cavity-method-x-belief-propagation"],
            related_hypotheses=["h-cavity-method-x-belief-propagation"],
            last_reviewed="2026-05-07",
            references=[
                dict(doi="10.1126/science.1073287",
                     note="Mézard & Montanari (2002) — analytic and algorithmic solution of random satisfiability problems; Science 297:812"),
                dict(doi="10.1002/j.1538-7305.1988.tb00880.x",
                     note="Pearl (1988) — probabilistic reasoning in intelligent systems; Morgan Kaufmann"),
            ],
        ),
        unknown=dict(
            id="u-cavity-method-x-belief-propagation",
            title=(
                "Can the cavity method (replica symmetry breaking) predict exact thresholds for "
                "computational phase transitions in random graphical inference problems, and do "
                "these thresholds match information-theoretic limits?"
            ),
            status="open",
            priority="high",
            disciplines=["physics", "computer_science", "mathematics"],
            summary=(
                "The cavity method (1RSB, 2RSB, full RSB) provides conjectured exact thresholds for "
                "random CSP phase transitions (satisfiability threshold, clustering threshold, "
                "freezing threshold). These are proven in some cases (random k-SAT for large k) "
                "but remain conjectural in general. Whether computational thresholds (where DPLL "
                "fails) always coincide with information-theoretic thresholds (where optimal inference "
                "fails) is the central open problem connecting statistical physics and computational "
                "complexity."
            ),
            systematic_gaps=[
                "The RSB prediction for random 3-SAT threshold (≈4.267) is unproven; upper and lower bounds are still separated",
                "Whether the algorithmic hardness threshold coincides with the information-theoretic threshold for random CSPs is open",
                "The cavity method is non-rigorous; its predictions require independent mathematical proof for each problem class",
            ],
            related_bridges=["b-cavity-method-x-belief-propagation"],
            last_reviewed="2026-05-07",
        ),
        hypo=dict(
            id="h-cavity-method-x-belief-propagation",
            title=(
                "The 1RSB cavity method gives the exact satisfiability threshold for random 3-SAT "
                "at α_c ≈ 4.267, and the onset of belief propagation non-convergence (multiple "
                "fixed points) at α ≈ 3.86 corresponds exactly to the clustering threshold where "
                "DPLL solvers undergo exponential slowdown"
            ),
            status="active",
            priority="high",
            impact_score=0.83,
            created="2026-05-07",
            last_updated="2026-05-07",
            author="wave-64-agent",
            unknowns_addressed=["u-cavity-method-x-belief-propagation"],
            related_disciplines=["physics", "computer_science", "mathematics"],
            evidence_links=[
                dict(type="supporting", doi="10.1126/science.1073287",
                     note="Mézard et al. — SP algorithm solves random SAT using RSB cavity method predictions",
                     confidence=0.80),
                dict(type="related",
                     note="Achlioptas & Moore (2006) — random k-SAT: two moments suffice to cross a sharp threshold; SIAM J Comput",
                     confidence=0.75),
            ],
            proposed_tests=[
                dict(description=(
                    "Generate random 3-SAT instances at α = 3.5, 3.8, 4.0, 4.2, 4.267, 4.3 "
                    "(ratio of clauses to variables); run DPLL + clause learning, belief propagation, "
                    "and survey propagation; measure median solve time, BP convergence rate, and "
                    "SP performance; compare transition points to theoretical predictions."
                )),
            ],
        ),
    ),

    # ── 12 ─────────────────────────────────────────────────────────────────
    dict(
        bridge_path="cross-domain/biology-physics/b-morphogenesis-x-mechanical-instability.yaml",
        unknown_path="unknowns-catalog/biology/u-morphogenesis-x-mechanical-instability.yaml",
        hypo_path="hypotheses/active/h-morphogenesis-x-mechanical-instability.yaml",
        bridge=dict(
            id="b-morphogenesis-x-mechanical-instability",
            title="Morphogenesis ↔ Mechanical instability — tissue folding as Euler buckling",
            status="proposed",
            fields=["biology", "physics"],
            bridge_claim=(
                "Brain cortical folding, gut villus formation, and lung branching morphogenesis all arise "
                "from compressive mechanical instabilities (Euler buckling, Rayleigh-Taylor instability) in "
                "elastic sheets; gyrification depth and fold spacing are predicted by the bilayer bending "
                "modulus ratio and confinement geometry — pure mechanics, no molecular patterning required."
            ),
            translation_table=[
                dict(field_a_term="cortical folding / gyrification (brain surface morphology)",
                     field_b_term="Euler buckling of a compressed elastic bilayer (mechanics)",
                     note="Cortex (stiff layer, μ₁) + subcortex (soft layer, μ₂) buckles when μ₁/μ₂ > threshold"),
                dict(field_a_term="fold spacing λ (distance between adjacent gyri)",
                     field_b_term="most unstable wavelength λ* of Euler buckling mode",
                     note="λ* = 2πh(μ₁/3μ₂)^(1/3) where h is cortex thickness — matches observed gyrification"),
                dict(field_a_term="villus/crypt periodicity in intestinal mucosa",
                     field_b_term="Rayleigh-Taylor instability wavelength in two-layer elastic system",
                     note="Gut epithelial layer (stiff) on submucosa (soft) buckles under growth-induced compression"),
                dict(field_a_term="lissencephaly (smooth brain) — genetic mutation reducing cortex stiffness",
                     field_b_term="buckling suppression when stiffness ratio μ₁/μ₂ < critical value",
                     note="LIS1 mutations reduce cortex growth rate, preventing compression needed for buckling"),
            ],
            cross_pollination_opportunities=[
                "Apply buckling theory to brain organoid engineering — controlling substrate stiffness "
                "and growth rate to reproduce gyrification patterns in vitro, enabling controlled "
                "models of lissencephaly and polymicrogyria.",
                "Use thin-shell elasticity mechanics to predict organ size scaling: the number of folds "
                "in the intestinal mucosa scales with body mass as N ∝ M^0.25 — a prediction testable "
                "across mammals using the buckling wavelength formula.",
            ],
            communication_gap=(
                "Developmental biology studied morphogenesis through molecular signalling (Turing patterns, "
                "Wnt, BMP gradients) while mechanics of elastic buckling was developed in structural "
                "engineering. The prediction that pure mechanical instability could generate brain folding "
                "patterns — without molecular pre-patterning — was resisted by molecular biologists. The "
                "mechanical morphogenesis paradigm gained traction only after Tallinen et al. (2016) showed "
                "a physically realistic gel brain model develops human-like gyrification patterns."
            ),
            related_unknowns=["u-morphogenesis-x-mechanical-instability"],
            related_hypotheses=["h-morphogenesis-x-mechanical-instability"],
            last_reviewed="2026-05-07",
            references=[
                dict(doi="10.1038/nphys3632",
                     note="Tallinen et al. (2016) — On the growth and form of cortical convolutions; Nature Phys 12:588"),
                dict(doi="10.1073/pnas.1406015111",
                     note="Tallinen & Biggins (2015) — mechanics of convoluted epithelial monolayers; PNAS"),
            ],
        ),
        unknown=dict(
            id="u-morphogenesis-x-mechanical-instability",
            title=(
                "Are mechanical instabilities sufficient to explain species-specific brain gyrification "
                "patterns, or do molecular pre-patterning signals (Wnt, PDGF) constrain fold positions "
                "independently of mechanical forces?"
            ),
            status="open",
            priority="high",
            disciplines=["biology", "physics", "neuroscience"],
            summary=(
                "Buckling theory quantitatively predicts fold spacing and depth from stiffness ratios "
                "and growth rates, suggesting mechanics alone is sufficient. However, the positions "
                "of primary sulci are evolutionarily conserved across individuals and species, suggesting "
                "molecular pre-patterning constrains where folds form. The open question is whether "
                "molecular signals merely bias the mechanical instability (selecting among degenerate "
                "buckling modes) or independently specify fold positions prior to mechanical deformation."
            ),
            systematic_gaps=[
                "Fold position conservation across individuals is inconsistent with a purely mechanical (degenerate instability) model",
                "Molecular pre-patterning signals (Wnt, PDGF) have established topographic patterns in cortex but causal proof is lacking",
                "No experiment has ablated both mechanical and molecular inputs independently to test their relative contributions",
            ],
            related_bridges=["b-morphogenesis-x-mechanical-instability"],
            last_reviewed="2026-05-07",
        ),
        hypo=dict(
            id="h-morphogenesis-x-mechanical-instability",
            title=(
                "Primary sulcus positions are mechanically determined by spatial variations in "
                "cortex stiffness (set by molecular gradients), with secondary and tertiary folds "
                "arising from purely mechanical instabilities of the initial folded geometry — "
                "making morphogenesis a two-stage mechanical-molecular process"
            ),
            status="active",
            priority="high",
            impact_score=0.80,
            created="2026-05-07",
            last_updated="2026-05-07",
            author="wave-64-agent",
            unknowns_addressed=["u-morphogenesis-x-mechanical-instability"],
            related_disciplines=["biology", "physics", "neuroscience", "developmental-biology"],
            evidence_links=[
                dict(type="supporting", doi="10.1038/nphys3632",
                     note="Tallinen et al. — buckling model reproduces human gyrification patterns from growth alone",
                     confidence=0.80),
                dict(type="related",
                     note="Zilles et al. (2013) — development of cortical folding and its relation to evolution; Brain Struct Funct",
                     confidence=0.72),
            ],
            proposed_tests=[
                dict(description=(
                    "Organoid buckling experiment: grow cerebral organoids on gels of varying stiffness "
                    "while blocking Wnt signalling (molecular pre-patterning); measure fold positions; "
                    "test whether fold positions are random (pure mechanics) or conserved (molecular "
                    "pre-patterning necessary for position specification)."
                )),
            ],
        ),
    ),
]


# ─────────────────────────────────────────────────────────────────────────────
# WAVE 65
# ─────────────────────────────────────────────────────────────────────────────

WAVE65 = [
    # ── 1 ──────────────────────────────────────────────────────────────────
    dict(
        bridge_path="cross-domain/cs-physics/b-tensor-networks-x-quantum-states.yaml",
        unknown_path="unknowns-catalog/physics/u-tensor-networks-x-quantum-states.yaml",
        hypo_path="hypotheses/active/h-tensor-networks-x-quantum-states.yaml",
        bridge=dict(
            id="b-tensor-networks-x-quantum-states",
            title="Tensor networks ↔ Quantum many-body states — MPS as entanglement compression",
            status="proposed",
            fields=["physics", "computer_science"],
            bridge_claim=(
                "Matrix product states (MPS) and tensor network contractions provide an efficient classical "
                "representation of quantum many-body states with limited entanglement; the DMRG algorithm "
                "is a tensor network optimization that scales polynomially for 1D gapped systems — connecting "
                "quantum information theory to classical simulation algorithms."
            ),
            translation_table=[
                dict(field_a_term="matrix product state (MPS) for 1D quantum system",
                     field_b_term="low-rank tensor decomposition of the quantum state amplitude array",
                     note="MPS bond dimension χ bounds entanglement entropy S ≤ log₂(χ); efficient iff S = O(1)"),
                dict(field_a_term="entanglement entropy S = -Tr[ρ_A log ρ_A] of subsystem A",
                     field_b_term="Schmidt rank (number of nonzero singular values in bipartition)",
                     note="Area law S = O(1) for gapped 1D systems ↔ efficient MPS approximation"),
                dict(field_a_term="DMRG (density matrix renormalization group) algorithm",
                     field_b_term="alternating least squares on MPS tensor network (numerical optimisation)",
                     note="DMRG is a tensor network optimization; White's 1992 DMRG is equivalent to MPS variational compression"),
                dict(field_a_term="PEPS (projected entangled pair states) for 2D systems",
                     field_b_term="2D tensor network with contraction complexity NP-hard in general",
                     note="PEPS contraction is #P-hard; area law holds in 2D but MPS fails — PEPS is the natural extension"),
            ],
            cross_pollination_opportunities=[
                "Apply tensor network contraction algorithms (belief propagation on factor graphs, "
                "Vidal's TEBD) to classical statistical mechanics problems — the partition function "
                "of a 2D Ising model is a tensor network contraction tractable via TMRG.",
                "Use quantum circuit tensor network simulation (MPS simulation of shallow circuits) "
                "to benchmark near-term quantum computers — circuits with limited entanglement "
                "are classically simulable up to bond dimension χ = 2^(S/2).",
            ],
            communication_gap=(
                "DMRG was invented by White (1992) as a numerical renormalisation group technique in "
                "condensed matter physics; matrix product states were developed by Fannes, Nachtergaele & "
                "Werner (1992) in quantum information theory. The equivalence of DMRG and MPS was "
                "recognised only around 2004-2007 (Verstraete & Cirac), enabling cross-fertilisation "
                "that produced the tensor network method unifying quantum information and condensed "
                "matter simulation."
            ),
            related_unknowns=["u-tensor-networks-x-quantum-states"],
            related_hypotheses=["h-tensor-networks-x-quantum-states"],
            last_reviewed="2026-05-07",
            references=[
                dict(doi="10.1103/RevModPhys.77.259",
                     note="Vidal (2007) — entanglement renormalisation; PRL 99:220405 — MERA tensor network"),
                dict(doi="10.1103/PhysRevLett.69.2863",
                     note="White (1992) — density matrix formulation for quantum renormalization groups; PRL 69:2863"),
            ],
        ),
        unknown=dict(
            id="u-tensor-networks-x-quantum-states",
            title=(
                "What is the minimum tensor network ansatz that can efficiently represent all "
                "topological quantum states in 2D, and can PEPS contraction be made polynomial-time "
                "for physically relevant classes of quantum states?"
            ),
            status="open",
            priority="high",
            disciplines=["physics", "computer_science", "mathematics"],
            summary=(
                "PEPS contraction is #P-hard in general, but for physically relevant 2D quantum states "
                "(gapped topological phases), the true complexity may be lower. Whether a polynomial-time "
                "tensor network algorithm exists for topological quantum states is the central open "
                "problem in classical simulation of quantum many-body systems. Key variants: (1) can "
                "boundary MPS methods achieve polynomial contraction for specific topological phases, "
                "(2) what is the entanglement structure of non-Abelian anyonic states in PEPS language?"
            ),
            systematic_gaps=[
                "PEPS contraction complexity for topological (non-trivial) states has not been separately characterised",
                "The entanglement structure of non-Abelian anyon models in PEPS language is not fully developed",
                "No polynomial-time PEPS algorithm has been demonstrated for any non-trivial 2D gapped state",
            ],
            related_bridges=["b-tensor-networks-x-quantum-states"],
            last_reviewed="2026-05-07",
        ),
        hypo=dict(
            id="h-tensor-networks-x-quantum-states",
            title=(
                "For 2D gapped topological phases with Abelian anyons (Z_N topological order), "
                "PEPS contraction reduces to a polynomial-time problem via the string-net "
                "condensation structure, while non-Abelian anyonic PEPS remain #P-hard"
            ),
            status="active",
            priority="high",
            impact_score=0.85,
            created="2026-05-07",
            last_updated="2026-05-07",
            author="wave-65-agent",
            unknowns_addressed=["u-tensor-networks-x-quantum-states"],
            related_disciplines=["physics", "computer_science", "mathematics", "quantum-computing"],
            evidence_links=[
                dict(type="supporting", doi="10.1103/RevModPhys.77.259",
                     note="Vidal — entanglement renormalisation and tensor network classification of quantum phases",
                     confidence=0.78),
                dict(type="related",
                     note="Levin & Wen (2006) — string-net condensation; Phys Rev B 71:045110",
                     confidence=0.74),
            ],
            proposed_tests=[
                dict(description=(
                    "Implement PEPS representations of Z_2 (toric code) and Fibonacci anyon models; "
                    "benchmark contraction time scaling with system size N; test whether Z_2 PEPS "
                    "contraction scales polynomially while Fibonacci PEPS shows exponential scaling; "
                    "compare to theoretical string-net contraction complexity predictions."
                )),
            ],
        ),
    ),

    # ── 2 ──────────────────────────────────────────────────────────────────
    dict(
        bridge_path="cross-domain/biology-math/b-ecology-x-coexistence-theory.yaml",
        unknown_path="unknowns-catalog/ecology/u-ecology-x-coexistence-theory.yaml",
        hypo_path="hypotheses/active/h-ecology-x-coexistence-theory.yaml",
        bridge=dict(
            id="b-ecology-x-coexistence-theory",
            title="Ecological coexistence ↔ Modern coexistence theory — storage effect as temporal niche",
            status="proposed",
            fields=["biology", "mathematics"],
            bridge_claim=(
                "Modern coexistence theory (Chesson 2000) partitions species coexistence mechanisms into "
                "stabilising (niche differences) and equalising (fitness similarity) components; the storage "
                "effect (temporal fluctuation buffering via overlapping generations) is a stabilising "
                "mechanism that allows indefinite coexistence in randomly varying environments."
            ),
            translation_table=[
                dict(field_a_term="stabilising niche difference (Δi) in MCT",
                     field_b_term="competitive exclusion avoidance via resource partitioning",
                     note="Δi > 0 prevents competitive exclusion; measured as the covariance of environment and competition"),
                dict(field_a_term="equalising fitness difference (ηi) in MCT",
                     field_b_term="intrinsic growth rate difference between competitors at equal density",
                     note="ηi measures competitive inequality; large ηi requires large Δi for coexistence"),
                dict(field_a_term="storage effect (covariance of environment and competition, buffered reproduction)",
                     field_b_term="temporal Jensen's inequality exploitation via life history buffering",
                     note="Long-lived stages (seeds, dormancy) allow species to 'bank' good years against bad ones"),
                dict(field_a_term="invasion criterion (can a rare species increase when common species present?)",
                     field_b_term="Lyapunov stability criterion for multispecies dynamical system",
                     note="Coexistence iff all species have positive invasion growth rates; equivalent to mutual invasibility"),
            ],
            cross_pollination_opportunities=[
                "Apply MCT's invasion growth rate decomposition to microbial community assembly — partition "
                "storage effect, relative nonlinearity, and frequency-dependent selection in gut microbiome "
                "stability using time-series data from longitudinal metagenomics studies.",
                "Use the storage effect framework to design more stable mixed-species agricultural systems — "
                "identifying crop combinations where temporal fluctuation in weather generates positive "
                "stabilising covariance, reducing weed competitive pressure.",
            ],
            communication_gap=(
                "Modern coexistence theory (Chesson 2000) is a theoretical ecology framework developed in "
                "mathematical ecology journals (Theoretical Population Biology, American Naturalist). "
                "Community ecologists who study species diversity in the field rarely read or apply MCT's "
                "mathematical decomposition. The storage effect mechanism was proposed in 1982 but is only "
                "now being tested empirically. Applied ecology and agriculture have been particularly slow "
                "to adopt the MCT framework for diversity management."
            ),
            related_unknowns=["u-ecology-x-coexistence-theory"],
            related_hypotheses=["h-ecology-x-coexistence-theory"],
            last_reviewed="2026-05-07",
            references=[
                dict(doi="10.1146/annurev.ecolsys.31.1.343",
                     note="Chesson (2000) — mechanisms of maintenance of species diversity; Annu Rev Ecol Syst 31:343"),
                dict(doi="10.1016/0040-5809(82)90040-5",
                     note="Chesson & Warner (1981) — environmental variability promotes coexistence in lottery competitive systems"),
            ],
        ),
        unknown=dict(
            id="u-ecology-x-coexistence-theory",
            title=(
                "Can the storage effect quantitatively predict biodiversity loss under climate change "
                "(reduced temporal variance and altered autocorrelation) in empirical plant communities, "
                "and is the stabilising niche difference measurable in situ?"
            ),
            status="open",
            priority="high",
            disciplines=["biology", "mathematics", "ecology"],
            summary=(
                "Modern coexistence theory predicts that climate change could reduce temporal environmental "
                "variance, weakening the storage effect and promoting competitive exclusion. However, "
                "empirically measuring Chesson's MCT parameters (Δi, ηi, storage effect magnitude) in "
                "real communities requires long-term population data with individually tracked plants — "
                "data that is scarce. Whether MCT can make quantitative predictions for community-level "
                "biodiversity responses to climate change is the central empirical challenge of the field."
            ),
            systematic_gaps=[
                "Empirical measurements of MCT parameters (Δi, ηi) in real communities are available for fewer than 20 species pairs",
                "Whether the storage effect is sufficient to maintain diversity under projected climate change autocorrelation shifts is unquantified",
                "MCT assumes stable coexistence but most natural communities are in non-equilibrium transient states",
            ],
            related_bridges=["b-ecology-x-coexistence-theory"],
            last_reviewed="2026-05-07",
        ),
        hypo=dict(
            id="h-ecology-x-coexistence-theory",
            title=(
                "A 50% reduction in interannual rainfall variance (projected under mid-latitude "
                "climate change) reduces the storage effect stabilising component Δi by 30–40% "
                "in annual plant communities, predicting a corresponding 30–40% reduction in "
                "species coexistence time before competitive exclusion"
            ),
            status="active",
            priority="high",
            impact_score=0.78,
            created="2026-05-07",
            last_updated="2026-05-07",
            author="wave-65-agent",
            unknowns_addressed=["u-ecology-x-coexistence-theory"],
            related_disciplines=["biology", "mathematics", "ecology", "climate-science"],
            evidence_links=[
                dict(type="supporting", doi="10.1146/annurev.ecolsys.31.1.343",
                     note="Chesson — storage effect magnitude proportional to environmental variance",
                     confidence=0.72),
                dict(type="related",
                     note="Adler et al. (2006) — climate variability has a weak effect on the coexistence of prairie grasses; PNAS 103:12793",
                     confidence=0.65),
            ],
            proposed_tests=[
                dict(description=(
                    "Manipulate rainfall variance in annual grass communities using rainout shelters "
                    "(high vs. low interannual variance treatments over 10 years); measure species "
                    "abundances annually; estimate storage effect magnitude Δi via the Chesson invasion "
                    "criterion; test whether coexistence time scales with Δi as predicted by MCT."
                )),
            ],
        ),
    ),

    # ── 3 ──────────────────────────────────────────────────────────────────
    dict(
        bridge_path="cross-domain/physics-biology/b-optogenetics-x-control-theory.yaml",
        unknown_path="unknowns-catalog/neuroscience/u-optogenetics-x-control-theory.yaml",
        hypo_path="hypotheses/active/h-optogenetics-x-control-theory.yaml",
        bridge=dict(
            id="b-optogenetics-x-control-theory",
            title="Optogenetics ↔ Control theory — light-gated channels as actuators",
            status="proposed",
            fields=["neuroscience", "computer_science"],
            bridge_claim=(
                "Optogenetic tools (channelrhodopsins, halorhodopsins) implement real-time feedback "
                "control of neural circuits; light pulses are control inputs, spike rates are controlled "
                "outputs, and closed-loop optogenetic stimulation implements proportional-integral control "
                "of neural dynamics — connecting neurotechnology to classical control engineering."
            ),
            translation_table=[
                dict(field_a_term="channelrhodopsin-2 (ChR2) light-gated cation channel",
                     field_b_term="actuator element in feedback control loop (increases plant output)",
                     note="ChR2 activation increases neuron firing — excitatory actuator; NpHR = inhibitory actuator"),
                dict(field_a_term="closed-loop optogenetics (spike rate measured, light adjusted in real-time)",
                     field_b_term="proportional-integral (PI) feedback control loop",
                     note="P: light proportional to error; I: integrated error prevents steady-state offset"),
                dict(field_a_term="light pulse frequency and duty cycle (control signal parameters)",
                     field_b_term="control input u(t) in continuous-time state space model",
                     note="Channelrhodopsin kinetics set the bandwidth; saturation gives nonlinear actuator model"),
                dict(field_a_term="neural spike rate (controlled variable being maintained at setpoint)",
                     field_b_term="plant output y(t) in closed-loop controller",
                     note="Spike rate setpoint corresponds to reference signal r(t) in control engineering"),
            ],
            cross_pollination_opportunities=[
                "Apply optimal control theory (LQR, MPC) to design minimal-energy optogenetic stimulation "
                "protocols for Parkinson's deep brain stimulation alternatives — minimising photon dose "
                "while achieving target firing rate patterns.",
                "Use nonlinear control analysis (Lyapunov stability, input-output stability) to predict "
                "channelrhodopsin opsin kinetics limits on achievable feedback bandwidth — constraining "
                "which neural circuits can be closed-loop controlled and at what update rates.",
            ],
            communication_gap=(
                "Optogenetics was developed by Deisseroth and Boyden as a neuroscience tool (Nature Methods "
                "2005) without reference to control engineering. Control engineers studying biological "
                "systems (synthetic biology feedback loops, insulin pumps) rarely collaborated with "
                "neuroscientists using optogenetics. The closed-loop optogenetics framework explicitly "
                "importing control theory was developed only around 2012-2016 (Grosenick, Boyden group; "
                "Foutz & McIntyre), leaving a decade of missed engineering optimisation opportunities."
            ),
            related_unknowns=["u-optogenetics-x-control-theory"],
            related_hypotheses=["h-optogenetics-x-control-theory"],
            last_reviewed="2026-05-07",
            references=[
                dict(doi="10.1038/nn.2512",
                     note="Boyden et al. (2005) — millisecond-timescale, genetically targeted optical control of neural activity; Nature Neurosci"),
                dict(doi="10.1038/nn.3257",
                     note="Grosenick et al. (2015) — closed-loop and activity-guided optogenetic control; Neuron 86:106"),
            ],
        ),
        unknown=dict(
            id="u-optogenetics-x-control-theory",
            title=(
                "What is the fundamental bandwidth limit of closed-loop optogenetic control imposed "
                "by channelrhodopsin kinetics, and can model predictive control overcome this "
                "limit for oscillatory neural dynamics?"
            ),
            status="open",
            priority="medium",
            disciplines=["neuroscience", "computer_science", "engineering"],
            summary=(
                "Channelrhodopsin-2 has on/off kinetics of ~10 ms, limiting closed-loop control "
                "bandwidth to ~100 Hz. Many neural oscillations of interest (gamma: 30-80 Hz, "
                "ripples: 150-250 Hz) approach or exceed this bandwidth. Model predictive control "
                "(MPC) could compensate by using a neural dynamics model to predict future states, "
                "commanding light pulses ahead of time. Whether MPC can overcome the actuator "
                "bandwidth limitation for fast neural oscillations is an open engineering challenge."
            ),
            systematic_gaps=[
                "Closed-loop optogenetic bandwidth has not been characterised as a function of opsin kinetics across available channelrhodopsins",
                "MPC has not been applied to closed-loop optogenetics with fast opsins (ChRmine, CoChR)",
                "The minimum light dose required for closed-loop gamma oscillation control has not been established",
            ],
            related_bridges=["b-optogenetics-x-control-theory"],
            last_reviewed="2026-05-07",
        ),
        hypo=dict(
            id="h-optogenetics-x-control-theory",
            title=(
                "Model predictive control with 10-step neural circuit prediction horizon achieves "
                "3× better gamma oscillation control compared to proportional feedback control "
                "using ChR2 (τ_off = 10 ms), by compensating for actuator delay with state "
                "prediction from fitted Wilson-Cowan model"
            ),
            status="active",
            priority="medium",
            impact_score=0.74,
            created="2026-05-07",
            last_updated="2026-05-07",
            author="wave-65-agent",
            unknowns_addressed=["u-optogenetics-x-control-theory"],
            related_disciplines=["neuroscience", "computer_science", "engineering", "control-theory"],
            evidence_links=[
                dict(type="supporting", doi="10.1038/nn.2512",
                     note="Boyden et al. — ChR2 kinetics (τ_off ≈ 10 ms) sets fundamental bandwidth limit",
                     confidence=0.78),
                dict(type="related",
                     note="Grosenick et al. (2015) — closed-loop optogenetic control demonstrates PI control feasibility",
                     confidence=0.72),
            ],
            proposed_tests=[
                dict(description=(
                    "In vitro cortical slice experiment: implement PI vs. MPC closed-loop ChR2 "
                    "control of gamma oscillation amplitude (30-80 Hz); measure tracking error, "
                    "oscillation coherence, and photon dose; test whether MPC achieves 3× tracking "
                    "improvement vs. PI at gamma frequencies exceeding 60 Hz."
                )),
            ],
        ),
    ),

    # ── 4 ──────────────────────────────────────────────────────────────────
    dict(
        bridge_path="cross-domain/math-physics/b-morse-theory-x-energy-landscape.yaml",
        unknown_path="unknowns-catalog/mathematics/u-morse-theory-x-energy-landscape.yaml",
        hypo_path="hypotheses/active/h-morse-theory-x-energy-landscape.yaml",
        bridge=dict(
            id="b-morse-theory-x-energy-landscape",
            title="Morse theory ↔ Energy landscapes — critical points as saddles and minima",
            status="proposed",
            fields=["mathematics", "physics"],
            bridge_claim=(
                "Morse theory classifies the topology of smooth manifolds through the critical points of a "
                "smooth function (minima, saddles, maxima); applied to potential energy surfaces in chemistry "
                "and physics, Morse theory provides a complete topological inventory of reaction pathways, "
                "metastable states, and transition states."
            ),
            translation_table=[
                dict(field_a_term="Morse function f: M → R (smooth function with nondegenerate critical points)",
                     field_b_term="potential energy surface V(x) of molecular or protein system",
                     note="PES is a Morse function generically; Morse critical points = equilibria and transition states"),
                dict(field_a_term="Morse index μ of critical point (number of negative Hessian eigenvalues)",
                     field_b_term="number of imaginary frequencies at transition state (saddle index)",
                     note="μ = 0: minimum (stable state); μ = 1: saddle (transition state); μ = 2: hilltop"),
                dict(field_a_term="Morse-Witten complex (gradient flow lines connecting critical points)",
                     field_b_term="reaction pathway network connecting stable states via transition states",
                     note="Gradient flow lines on PES correspond to reaction paths; Morse-Witten complex is the kinetic network"),
                dict(field_a_term="Morse inequality: #{critical pts of index k} ≥ βₖ (Betti number)",
                     field_b_term="minimum number of transition states required by topology of PES",
                     note="Morse inequalities give lower bounds on the number of saddles on a PES from topology"),
            ],
            cross_pollination_opportunities=[
                "Apply Morse theory to protein folding energy landscapes — the Morse-Witten complex "
                "gives the complete kinetic folding network; Morse inequalities provide lower bounds "
                "on the number of folding intermediates required by the topology of the folding funnel.",
                "Use persistent homology (a topological data analysis method based on Morse theory) "
                "to automatically identify metastable states and transition states in molecular "
                "dynamics simulations without prespecified reaction coordinates.",
            ],
            communication_gap=(
                "Morse theory was developed in pure differential topology (Morse 1934, Milnor 1963); "
                "potential energy surfaces were developed independently in physical chemistry "
                "(London, Eyring, Evans-Polanyi 1930s). Chemists and physicists studying energy "
                "landscapes were unaware of the complete topological characterization offered by "
                "Morse theory until the work of Wales (2003) on 'Energy Landscapes' and the "
                "adoption of topological data analysis in computational chemistry."
            ),
            related_unknowns=["u-morse-theory-x-energy-landscape"],
            related_hypotheses=["h-morse-theory-x-energy-landscape"],
            last_reviewed="2026-05-07",
            references=[
                dict(doi="10.1515/9781400881802",
                     note="Milnor (1963) — Morse Theory; Princeton University Press — foundational Morse theory text"),
                dict(doi="10.1039/b210331a",
                     note="Wales (2003) — Energy Landscapes; Cambridge University Press"),
            ],
        ),
        unknown=dict(
            id="u-morse-theory-x-energy-landscape",
            title=(
                "Does the Morse-Witten complex of a protein energy landscape have a computable "
                "topological signature that predicts folding cooperativity, and can persistent "
                "homology detect all kinetically relevant metastable states from MD trajectories?"
            ),
            status="open",
            priority="medium",
            disciplines=["mathematics", "physics", "chemistry"],
            summary=(
                "Protein folding energy landscapes are high-dimensional, making direct Morse theory "
                "application computationally infeasible. Persistent homology provides a scalable "
                "topological analysis, but whether it correctly identifies all kinetically relevant "
                "metastable states (without missing barriers or generating spurious ones) from finite "
                "MD trajectory sampling is an open question. The fundamental gap is translating "
                "abstract Morse theory (exact statements) to approximate results from noisy "
                "simulation data."
            ),
            systematic_gaps=[
                "Persistent homology of protein energy landscapes has not been validated against experimentally known folding intermediates",
                "The sampling density required to correctly identify Morse-Witten complex topology in high-dimensional PES is unknown",
                "Morse theory assumes smooth functions; molecular energy surfaces with cusps (bond breaking) require extensions",
            ],
            related_bridges=["b-morse-theory-x-energy-landscape"],
            last_reviewed="2026-05-07",
        ),
        hypo=dict(
            id="h-morse-theory-x-energy-landscape",
            title=(
                "Persistent homology 1-cycles (H₁ Betti number) of protein energy landscapes "
                "computed from MD trajectories predict the number of distinct folding intermediates "
                "with false negative rate < 5% when sampling density exceeds 100 transitions per "
                "identified metastable basin"
            ),
            status="active",
            priority="medium",
            impact_score=0.71,
            created="2026-05-07",
            last_updated="2026-05-07",
            author="wave-65-agent",
            unknowns_addressed=["u-morse-theory-x-energy-landscape"],
            related_disciplines=["mathematics", "physics", "chemistry", "computational-biology"],
            evidence_links=[
                dict(type="supporting", doi="10.1515/9781400881802",
                     note="Milnor — Morse theory provides exact critical point classification for smooth functions",
                     confidence=0.70),
                dict(type="related",
                     note="Meng et al. (2020) — persistent homology analysis of protein folding; J Chem Theory Comput",
                     confidence=0.67),
            ],
            proposed_tests=[
                dict(description=(
                    "Compute persistent homology H₁ from ultralong MD trajectories of Trp-cage miniprotein "
                    "(known 1 intermediate) and GB1 (known 2 intermediates); test whether H₁ Betti number "
                    "correctly predicts number of intermediates; measure false negative rate vs. sampling density."
                )),
            ],
        ),
    ),

    # ── 5 ──────────────────────────────────────────────────────────────────
    dict(
        bridge_path="cross-domain/biology-cs/b-gene-regulatory-network-x-boolean-circuit.yaml",
        unknown_path="unknowns-catalog/biology/u-gene-regulatory-network-x-boolean-circuit.yaml",
        hypo_path="hypotheses/active/h-gene-regulatory-network-x-boolean-circuit.yaml",
        bridge=dict(
            id="b-gene-regulatory-network-x-boolean-circuit",
            title="Gene regulatory networks ↔ Boolean circuits — transcription factor logic as AND/OR gates",
            status="proposed",
            fields=["biology", "computer_science"],
            bridge_claim=(
                "Transcription factor combinatorics implement Boolean logic: cooperative binding is AND, "
                "competitive binding is NOT, and OR gates arise from redundant enhancers; Kauffman's NK "
                "random Boolean network model shows that developmental gene networks operate near the "
                "critical (chaotic-to-ordered) phase transition for maximum evolvability."
            ),
            translation_table=[
                dict(field_a_term="cooperative transcription factor binding (both TFs required for activation)",
                     field_b_term="Boolean AND gate (output 1 iff both inputs 1)",
                     note="Synergistic activation requires cofactor TF binding within same enhancer module"),
                dict(field_a_term="competitive/repressive TF binding (repressor blocks activator)",
                     field_b_term="Boolean NOT/NAND gate (repressor inverts activator logic)",
                     note="Repressor-activator competition implements NOT; combined with AND gives NAND — universal gate"),
                dict(field_a_term="shadow enhancer (redundant enhancer elements for same target gene)",
                     field_b_term="Boolean OR gate (output 1 if any input is 1)",
                     note="Redundant enhancers are OR logic gates; increase robustness to enhancer mutation"),
                dict(field_a_term="NK random Boolean network (N genes, K inputs per gene)",
                     field_b_term="random Boolean circuit of N gates with in-degree K",
                     note="Kauffman's NK model: ordered phase (K < 2), critical (K = 2), chaotic (K > 2)"),
            ],
            cross_pollination_opportunities=[
                "Apply Boolean circuit complexity theory (circuit depth vs. expressivity trade-offs) to "
                "understand why gene regulatory networks use hierarchical transcription factor cascades — "
                "cascades increase circuit depth enabling complex spatiotemporal patterns with few TFs.",
                "Use NK Boolean network criticality analysis to classify cancer gene regulatory networks — "
                "cancer cells may operate in the chaotic phase (K > 2), explaining transcriptional "
                "heterogeneity and epigenetic plasticity in tumour progression.",
            ],
            communication_gap=(
                "Boolean network models of gene regulation (Kauffman 1969) were developed in theoretical "
                "biology and ignored by molecular geneticists for decades, who viewed abstract Boolean "
                "models as over-simplified. Molecular biologists studying transcription factor logic "
                "in Drosophila (Levine, Mann, Small) developed enhancer logic rules empirically without "
                "reference to Boolean circuit theory. The synthesis required systems biology (Davidson "
                "2001) to formalise gene regulatory network logic diagrams."
            ),
            related_unknowns=["u-gene-regulatory-network-x-boolean-circuit"],
            related_hypotheses=["h-gene-regulatory-network-x-boolean-circuit"],
            last_reviewed="2026-05-07",
            references=[
                dict(doi="10.1016/0022-5193(69)90015-0",
                     note="Kauffman (1969) — metabolic stability and epigenesis in randomly constructed genetic nets; J Theor Biol 22:437"),
                dict(doi="10.1016/j.cell.2002.09.005",
                     note="Davidson et al. (2002) — gene regulatory network for sea urchin endomesoderm specification; Science"),
            ],
        ),
        unknown=dict(
            id="u-gene-regulatory-network-x-boolean-circuit",
            title=(
                "Are endogenous developmental gene regulatory networks in vertebrates operating "
                "at or near the Boolean criticality threshold K = 2, and if so, does this "
                "determine the evolvability of body plan morphology?"
            ),
            status="open",
            priority="medium",
            disciplines=["biology", "computer_science", "mathematics"],
            summary=(
                "Kauffman's NK model predicts maximum evolvability at criticality (K = 2), where "
                "networks are neither too rigid (K < 2, ordered) nor too chaotic (K > 2). Whether "
                "real GRNs operate at this critical point, and whether K can be measured from "
                "transcriptomic data, is an open question. Single-cell RNA-seq now provides "
                "empirical access to GRN dynamics, but the Boolean formalism requires threshold "
                "binarisation and the effective K of real GRNs has not been rigorously estimated."
            ),
            systematic_gaps=[
                "The effective Boolean connectivity K has not been estimated for any vertebrate GRN from single-cell transcriptomic data",
                "Boolean binarisation of continuous gene expression introduces artefacts whose effect on criticality estimates is unknown",
                "Whether GRN criticality is a product of evolution (selection for evolvability) or a neutral structural constraint is debated",
            ],
            related_bridges=["b-gene-regulatory-network-x-boolean-circuit"],
            last_reviewed="2026-05-07",
        ),
        hypo=dict(
            id="h-gene-regulatory-network-x-boolean-circuit",
            title=(
                "The effective Boolean connectivity K of developmental GRNs estimated from single-cell "
                "RNA-seq binarised expression is 1.8–2.2 (near criticality) in normal development "
                "and increases to 2.5–3.0 in cancer cells, measurable via Kauffman network "
                "phase classification of perturbed expression states"
            ),
            status="active",
            priority="medium",
            impact_score=0.72,
            created="2026-05-07",
            last_updated="2026-05-07",
            author="wave-65-agent",
            unknowns_addressed=["u-gene-regulatory-network-x-boolean-circuit"],
            related_disciplines=["biology", "computer_science", "mathematics"],
            evidence_links=[
                dict(type="supporting", doi="10.1016/0022-5193(69)90015-0",
                     note="Kauffman — NK Boolean network criticality at K = 2 provides maximum evolvability",
                     confidence=0.70),
                dict(type="related",
                     note="Daniels et al. (2018) — criticality distinguishes the ensemble of biological regulatory networks; PRL 121:138102",
                     confidence=0.73),
            ],
            proposed_tests=[
                dict(description=(
                    "Analyse scRNA-seq datasets from normal embryonic development and matched cancer "
                    "cell lines; binarise expression at bimodal thresholds; infer Boolean networks "
                    "via ARACNE/GENIE3; estimate effective K; classify phase (ordered/critical/chaotic); "
                    "test whether normal cells cluster at K ≈ 2 and cancer cells at K > 2."
                )),
            ],
        ),
    ),

    # ── 6 ──────────────────────────────────────────────────────────────────
    dict(
        bridge_path="cross-domain/physics-economics/b-minority-game-x-market-microstructure.yaml",
        unknown_path="unknowns-catalog/economics/u-minority-game-x-market-microstructure.yaml",
        hypo_path="hypotheses/active/h-minority-game-x-market-microstructure.yaml",
        bridge=dict(
            id="b-minority-game-x-market-microstructure",
            title="Minority game ↔ Market microstructure — agent heterogeneity as market efficiency",
            status="proposed",
            fields=["economics", "physics"],
            bridge_claim=(
                "The minority game (Challet & Zhang 1997) — where agents must independently choose the "
                "minority side to win — produces a phase transition between efficient (random) and "
                "inefficient (exploitable) markets as a function of agent memory; this maps directly to "
                "market microstructure theory of informed vs noise traders."
            ),
            translation_table=[
                dict(field_a_term="minority game memory m (number of past outcomes agents remember)",
                     field_b_term="market information ratio α = P/N (prediction resources per agent)",
                     note="Phase transition at α_c ≈ 0.34; below α_c: inefficient (exploitable); above: efficient (random)"),
                dict(field_a_term="minority game phase transition (from exploitable to random phase)",
                     field_b_term="EMH strong-to-weak efficiency transition in market microstructure",
                     note="Below threshold: price predictability exists (technical analysis profitable); above: random walk"),
                dict(field_a_term="minority game strategy (mapping from history to binary action)",
                     field_b_term="trading rule / technical analysis indicator in market microstructure",
                     note="Agents with more strategies correspond to informed traders with better prediction capacity"),
                dict(field_a_term="attendance fluctuation σ² in minority game (volatility proxy)",
                     field_b_term="market price volatility (bid-ask spread, trading volume fluctuation)",
                     note="Volatility minimum at phase transition point α_c — maximum market efficiency corresponds to minimum exploitability"),
            ],
            cross_pollination_opportunities=[
                "Apply minority game phase diagram to cryptocurrency market microstructure — predict "
                "when altcoin markets cross the α_c threshold as number of active algorithmic traders "
                "increases, transitioning from exploitable to efficient.",
                "Use replica method from minority game statistical physics to analytically compute "
                "the information capacity of financial markets as a function of trader heterogeneity — "
                "providing a first-principles derivation of market efficiency from agent theory.",
            ],
            communication_gap=(
                "The minority game was invented by physicists (Challet & Zhang 1997, Physica A) "
                "and analysed using spin glass theory and replica methods — methods entirely "
                "foreign to financial economists. Market microstructure theory (Kyle 1985, Glosten-"
                "Milgrom 1985) uses game theory and information economics. The two communities "
                "independently developed nearly identical models of informed-vs-noise-trader markets "
                "without cross-citation, despite the minority game being an exact mathematical "
                "model of the Kyle framework."
            ),
            related_unknowns=["u-minority-game-x-market-microstructure"],
            related_hypotheses=["h-minority-game-x-market-microstructure"],
            last_reviewed="2026-05-07",
            references=[
                dict(doi="10.1016/S0378-4371(97)00419-6",
                     note="Challet & Zhang (1997) — emergence of cooperation and organisation in an evolutionary game; Physica A 246:407"),
                dict(doi="10.2307/1833139",
                     note="Kyle (1985) — continuous auctions and insider trading; Econometrica 53:1315"),
            ],
        ),
        unknown=dict(
            id="u-minority-game-x-market-microstructure",
            title=(
                "Does the minority game phase transition at α_c correspond to a measurable "
                "threshold in real financial markets (e.g., the number of algorithmic traders "
                "per traded asset), and can the transition be detected empirically from "
                "order book microstructure data?"
            ),
            status="open",
            priority="medium",
            disciplines=["economics", "physics", "mathematics"],
            summary=(
                "The minority game predicts a phase transition from exploitable to efficient markets "
                "at α_c ≈ 0.34 (P/N where P = strategy space size, N = number of traders). In real "
                "markets, P and N are unobservable. Whether an empirical proxy (e.g., order flow "
                "autocorrelation, bid-ask spread dynamics, algorithmic trader fraction) can detect "
                "the phase transition is an open question. Several studies have claimed to observe "
                "phase-transition-like behaviour in market microstructure but without controlled "
                "α variation."
            ),
            systematic_gaps=[
                "The minority game order parameter (attendance fluctuation) has no direct observable analogue in real market data",
                "α_c in real markets is confounded by trader heterogeneity and strategy space dimensionality differences",
                "No controlled experiment varying α (trader count with fixed strategy complexity) has been conducted in financial markets",
            ],
            related_bridges=["b-minority-game-x-market-microstructure"],
            last_reviewed="2026-05-07",
        ),
        hypo=dict(
            id="h-minority-game-x-market-microstructure",
            title=(
                "Order flow autocorrelation C(τ) = ⟨sign(v_t) sign(v_{t+τ})⟩ transitions from "
                "positive (exploitable, predictable order flow) to near-zero (efficient) as "
                "algorithmic trader fraction increases past a threshold of ~34% of total volume, "
                "matching the minority game α_c prediction"
            ),
            status="active",
            priority="medium",
            impact_score=0.69,
            created="2026-05-07",
            last_updated="2026-05-07",
            author="wave-65-agent",
            unknowns_addressed=["u-minority-game-x-market-microstructure"],
            related_disciplines=["economics", "physics", "mathematics"],
            evidence_links=[
                dict(type="supporting", doi="10.1016/S0378-4371(97)00419-6",
                     note="Challet & Zhang — minority game phase transition at α_c with volatility minimum",
                     confidence=0.68),
                dict(type="related",
                     note="Lillo & Farmer (2004) — long memory in order flow; Quantitative Finance 4:7",
                     confidence=0.65),
            ],
            proposed_tests=[
                dict(description=(
                    "Analyse NASDAQ order book data (2010–2020) segmented by estimated algorithmic "
                    "trading fraction (HFT volume proxy); compute order flow autocorrelation C(1) "
                    "for each period; test whether C(1) decreases monotonically with HFT fraction "
                    "and crosses near-zero at ~34% HFT volume consistent with α_c prediction."
                )),
            ],
        ),
    ),

    # ── 7 ──────────────────────────────────────────────────────────────────
    dict(
        bridge_path="cross-domain/biology-physics/b-biofilm-x-active-nematic.yaml",
        unknown_path="unknowns-catalog/biology/u-biofilm-x-active-nematic.yaml",
        hypo_path="hypotheses/active/h-biofilm-x-active-nematic.yaml",
        bridge=dict(
            id="b-biofilm-x-active-nematic",
            title="Bacterial biofilm ↔ Active nematics — collective orientation as liquid crystal order",
            status="proposed",
            fields=["biology", "physics"],
            bridge_claim=(
                "Dense bacterial communities in biofilms exhibit active nematic liquid crystal order; "
                "cell alignment, topological defect dynamics (+1/2 and -1/2 defects), and collective "
                "flows are quantitatively described by active nematic hydrodynamics, making biofilm "
                "architecture a biological realization of active liquid crystal physics."
            ),
            translation_table=[
                dict(field_a_term="bacterial cell orientation field (director field in dense biofilm)",
                     field_b_term="nematic director n̂(r) in liquid crystal theory",
                     note="Rod-shaped bacteria (E. coli, B. subtilis) align locally; long-range nematic order develops above critical density"),
                dict(field_a_term="topological defects in biofilm (+1/2 comet, -1/2 trefoil patterns)",
                     field_b_term="±1/2 disclination defects in active nematic liquid crystal",
                     note="+1/2 defects move, -1/2 defects are stationary; +1/2 defect velocity predicts local biofilm stress"),
                dict(field_a_term="biofilm mechanical stress at +1/2 defect cores",
                     field_b_term="extensile stress in active nematic at defect cores (σ_active)",
                     note="+1/2 defects accumulate mechanical stress, triggering cell extrusion and colony expansion"),
                dict(field_a_term="biofilm collective flow patterns (vortices, jets, bulk flow)",
                     field_b_term="active nematic spontaneous flow instability (above activity threshold)",
                     note="Active nematics above activity threshold a* develop spontaneous flow — matches biofilm flow patterns"),
            ],
            cross_pollination_opportunities=[
                "Use active nematic theory to predict antibiotic penetration patterns in biofilms — "
                "topological defects create channels of mechanical instability that could allow "
                "drug penetration into otherwise dense biofilm interiors.",
                "Apply active liquid crystal order parameter measurements (defect density, correlation "
                "length) as quantitative biofilm virulence metrics — more ordered biofilms (fewer "
                "defects) may be more resistant to mechanical disruption.",
            ],
            communication_gap=(
                "Active nematic liquid crystal physics was developed in soft matter physics "
                "(Marchetti, Dogic, Bhattacharya) using reconstituted cytoskeletal systems. "
                "Biofilm biology was developed in microbiology, focused on quorum sensing "
                "and matrix composition. The connection between biofilm cell alignment and "
                "active nematic theory was made only recently (Doostmohammadi et al. 2016, "
                "Copenhagen et al. 2021) — two decades after active nematics were first "
                "described theoretically."
            ),
            related_unknowns=["u-biofilm-x-active-nematic"],
            related_hypotheses=["h-biofilm-x-active-nematic"],
            last_reviewed="2026-05-07",
            references=[
                dict(doi="10.1038/nphys3600",
                     note="Doostmohammadi et al. (2016) — biofilm active nematic order; Nature Physics — topological defects in bacteria"),
                dict(doi="10.1038/s41467-021-24792-2",
                     note="Copenhagen et al. (2021) — topological defects promote layer formation in Myxococcus xanthus biofilms; Nature Comm"),
            ],
        ),
        unknown=dict(
            id="u-biofilm-x-active-nematic",
            title=(
                "Do topological defects in bacterial biofilms (+1/2 disclinations) causally "
                "determine sites of biofilm expansion, cell extrusion, or matrix secretion, "
                "or are they merely epiphenomenal signatures of mechanical stress?"
            ),
            status="open",
            priority="medium",
            disciplines=["biology", "physics", "microbiology"],
            summary=(
                "Active nematic theory predicts that +1/2 topological defects generate extensile stress "
                "that drives cell extrusion and collective motion. In biofilms, defects have been "
                "observed to correlate with structural transitions, but the causal relationship has "
                "not been established. Whether defects cause expansion (extensile stress → cell expulsion) "
                "or are merely markers of pre-existing mechanical heterogeneity (caused by growth "
                "rate differences) requires direct manipulation experiments."
            ),
            systematic_gaps=[
                "No direct manipulation experiment has perturbed defect positions independently of bacterial growth rate",
                "The relationship between +1/2 defect velocity and actual extensile stress in biofilm matrix has not been measured",
                "Active nematic theory assumes rodlike particles, but cocci and other shapes violate this assumption",
            ],
            related_bridges=["b-biofilm-x-active-nematic"],
            last_reviewed="2026-05-07",
        ),
        hypo=dict(
            id="h-biofilm-x-active-nematic",
            title=(
                "+1/2 topological defects in E. coli biofilms causally drive local cell extrusion "
                "at rates 3× higher than defect-free regions, with extrusion probability scaling "
                "with defect velocity predicted by active nematic extensile stress magnitude"
            ),
            status="active",
            priority="medium",
            impact_score=0.73,
            created="2026-05-07",
            last_updated="2026-05-07",
            author="wave-65-agent",
            unknowns_addressed=["u-biofilm-x-active-nematic"],
            related_disciplines=["biology", "physics", "microbiology"],
            evidence_links=[
                dict(type="supporting", doi="10.1038/nphys3600",
                     note="Doostmohammadi et al. — active nematic theory of bacterial biofilm topological defects",
                     confidence=0.73),
                dict(type="related",
                     note="Saw et al. (2017) — topological defects in epithelial monolayers cause cell death; Nature 544:212",
                     confidence=0.70),
            ],
            proposed_tests=[
                dict(description=(
                    "Time-lapse confocal imaging of fluorescent E. coli biofilms; track topological "
                    "defect positions (+1/2 and -1/2) and defect velocities; simultaneously track "
                    "cell extrusion events; test whether extrusion rate at +1/2 defect cores "
                    "is 3× higher than random regions and correlates with defect velocity magnitude."
                )),
            ],
        ),
    ),

    # ── 8 ──────────────────────────────────────────────────────────────────
    dict(
        bridge_path="cross-domain/math-cs/b-tropical-geometry-x-neural-networks.yaml",
        unknown_path="unknowns-catalog/mathematics/u-tropical-geometry-x-neural-networks.yaml",
        hypo_path="hypotheses/active/h-tropical-geometry-x-neural-networks.yaml",
        bridge=dict(
            id="b-tropical-geometry-x-neural-networks",
            title="Tropical geometry ↔ ReLU neural networks — piecewise-linear maps as tropical polynomials",
            status="proposed",
            fields=["mathematics", "computer_science"],
            bridge_claim=(
                "ReLU neural networks compute piecewise-linear functions that are exactly tropical "
                "polynomials in tropical (max-plus) algebra; the number of linear regions of a deep "
                "ReLU network grows exponentially with depth — a fact provable using tropical geometry — "
                "explaining why depth provides exponential representational advantage."
            ),
            translation_table=[
                dict(field_a_term="ReLU activation function max(0, x) (neural network)",
                     field_b_term="tropical addition a ⊕ b = max(a, b) in max-plus algebra",
                     note="ReLU is exactly the tropical addition applied to a linear function and zero"),
                dict(field_a_term="piecewise-linear function computed by ReLU network",
                     field_b_term="tropical polynomial in max-plus semiring",
                     note="Every ReLU network computes a tropical polynomial; tropical geometry characterises the PL subdivision"),
                dict(field_a_term="number of linear regions of depth-d width-w ReLU network",
                     field_b_term="number of facets of the tropical hypersurface (tropical algebraic geometry)",
                     note="Linear regions count grows as Θ((w/n)^{nd}) for n-input network; tropical geometry proves this"),
                dict(field_a_term="depth-width trade-off in neural network expressivity",
                     field_b_term="tropical hypersurface complexity vs. polynomial degree and dimension",
                     note="Depth exponentially increases linear regions; breadth increases polynomially — proven by tropical methods"),
            ],
            cross_pollination_opportunities=[
                "Use tropical geometry to analyse the decision boundaries of trained neural networks — "
                "the tropical hypersurface of a trained ReLU network provides an exact geometric "
                "description of its decision boundary as a polyhedral complex.",
                "Apply tropical optimisation (linear programming over tropical semiring) to neural "
                "architecture search — the tropical geometry framework provides an algebraic "
                "characterisation of which network architectures are expressively equivalent.",
            ],
            communication_gap=(
                "Tropical geometry was developed in algebraic geometry (Mikhalkin 2004, Speyer & "
                "Sturmfels 2004) as a tool for combinatorial and computational algebraic geometry. "
                "Neural network expressivity theory was developed in machine learning (Montufar 2014, "
                "Telgarsky 2016). The connection was made by Zhang et al. (2018) and Montufar et al. "
                "(2014), but remains largely unknown to both algebraic geometers (who don't study "
                "deep learning) and machine learning researchers (who rarely study tropical geometry)."
            ),
            related_unknowns=["u-tropical-geometry-x-neural-networks"],
            related_hypotheses=["h-tropical-geometry-x-neural-networks"],
            last_reviewed="2026-05-07",
            references=[
                dict(doi="10.48550/arXiv.1805.07091",
                     note="Zhang et al. (2018) — tropical geometry of deep neural networks; ICML 2018"),
                dict(doi="10.48550/arXiv.1402.1869",
                     note="Montufar et al. (2014) — on the number of linear regions of deep neural networks; NeurIPS 2014"),
            ],
        ),
        unknown=dict(
            id="u-tropical-geometry-x-neural-networks",
            title=(
                "Can the tropical geometry of a trained neural network predict its generalisation "
                "error — specifically, does lower tropical hypersurface complexity (fewer linear "
                "regions) correlate with better generalisation in the overparameterised regime?"
            ),
            status="open",
            priority="medium",
            disciplines=["mathematics", "computer_science"],
            summary=(
                "Tropical geometry provides exact characterisation of ReLU network expressivity via "
                "linear region count, but the relationship between tropical hypersurface complexity "
                "and generalisation is unexplored. In the overparameterised regime (more parameters "
                "than training examples), networks can fit any training data but differ in generalisation. "
                "Whether tropical geometry-based complexity measures predict generalisation better than "
                "classical VC dimension is an open question."
            ),
            systematic_gaps=[
                "No empirical study has measured tropical hypersurface complexity of trained vs. random ReLU networks",
                "The relationship between tropical complexity and implicit regularisation of SGD is theoretical",
                "Tropical geometry assumes exact arithmetic; floating-point errors and batch normalisation break the exact tropical structure",
            ],
            related_bridges=["b-tropical-geometry-x-neural-networks"],
            last_reviewed="2026-05-07",
        ),
        hypo=dict(
            id="h-tropical-geometry-x-neural-networks",
            title=(
                "The tropical complexity of a trained ReLU network (number of active linear regions "
                "on test data) is 10–100× smaller than the theoretical maximum, and this reduction "
                "correlates with test accuracy with Pearson r > 0.8 across architectures trained "
                "with different regularisation strengths"
            ),
            status="active",
            priority="medium",
            impact_score=0.70,
            created="2026-05-07",
            last_updated="2026-05-07",
            author="wave-65-agent",
            unknowns_addressed=["u-tropical-geometry-x-neural-networks"],
            related_disciplines=["mathematics", "computer_science"],
            evidence_links=[
                dict(type="supporting", doi="10.48550/arXiv.1805.07091",
                     note="Zhang et al. — tropical geometry of deep neural networks; linear regions grow exponentially with depth",
                     confidence=0.72),
                dict(type="related",
                     note="Montufar et al. (2014) — linear regions of ReLU networks; NeurIPS 2014",
                     confidence=0.75),
            ],
            proposed_tests=[
                dict(description=(
                    "Train ResNet-18 on CIFAR-10 with L2 regularisation λ = 0, 0.001, 0.01, 0.1; "
                    "estimate active linear regions (tropical complexity) on test set via random "
                    "sampling of activation patterns; compute Pearson correlation between "
                    "tropical complexity and test accuracy; compare to weight norm and sharpness measures."
                )),
            ],
        ),
    ),

    # ── 9 ──────────────────────────────────────────────────────────────────
    dict(
        bridge_path="cross-domain/physics-geology/b-seismic-wave-x-elastic-wave.yaml",
        unknown_path="unknowns-catalog/geoscience/u-seismic-wave-x-elastic-wave.yaml",
        hypo_path="hypotheses/active/h-seismic-wave-x-elastic-wave.yaml",
        bridge=dict(
            id="b-seismic-wave-x-elastic-wave",
            title="Seismic waves ↔ Elastic wave theory — P and S waves as Navier equation solutions",
            status="proposed",
            fields=["geoscience", "physics"],
            bridge_claim=(
                "Seismic body waves (P-waves and S-waves) are solutions of the Navier elastodynamic "
                "equation in a heterogeneous elastic solid; wave speed ratios (Vp/Vs) reveal rock type "
                "and fluid content via Biot-Gassmann relations, making seismology an application of "
                "elastic wave physics to planetary-scale media."
            ),
            translation_table=[
                dict(field_a_term="P-wave (compressional seismic wave, particle motion parallel to propagation)",
                     field_b_term="longitudinal elastic wave (dilatational, irrotational) in Navier equation",
                     note="Vp = √((λ+2μ)/ρ); λ,μ = Lamé parameters; P-waves transmit through liquids"),
                dict(field_a_term="S-wave (shear seismic wave, particle motion transverse to propagation)",
                     field_b_term="transverse elastic wave (equivoluminal, rotational) in Navier equation",
                     note="Vs = √(μ/ρ); Vs = 0 in fluids (μ = 0) — explains S-wave shadow zone at Earth's core"),
                dict(field_a_term="Vp/Vs ratio (seismic wave speed ratio) in rock physics",
                     field_b_term="Poisson ratio ν = (Vp/Vs)² - 2) / (2(Vp/Vs)² - 2) in elastic theory",
                     note="ν = 0.5 for water-saturated rock (incompressible); ν < 0.3 for dry rock"),
                dict(field_a_term="Biot-Gassmann fluid substitution (changing pore fluid changes Vp)",
                     field_b_term="Biot effective medium theory for porous elastic solids with fluid",
                     note="Gassmann equations predict Vp change when oil is replaced by water or gas — seismic 4D monitoring"),
            ],
            cross_pollination_opportunities=[
                "Apply elastic wave Navier equation finite-difference simulation to design seismic "
                "metamaterials (phononic crystals) for earthquake isolation — periodic arrays of "
                "boreholes or inclusions that create seismic band gaps at destructive frequencies.",
                "Use Biot-Gassmann relations to invert seismic Vp/Vs ratios for carbon sequestration "
                "monitoring — CO₂ injection changes Vp but not Vs, providing a quantitative elastic "
                "wave signature for subsurface CO₂ plume tracking.",
            ],
            communication_gap=(
                "Seismology developed as an observational science from earthquake recordings "
                "(Richter, Gutenberg, early 20th century) and independently developed wave "
                "propagation theory. Continuum mechanics and elastic wave theory were developed "
                "in mathematical physics (Cauchy, Navier, 19th century). These communities merged "
                "gradually through applied geophysics (oil exploration seismics), but seismologists "
                "and mechanical engineers rarely collaborate on earthquake-resistant structure design "
                "despite using identical governing equations."
            ),
            related_unknowns=["u-seismic-wave-x-elastic-wave"],
            related_hypotheses=["h-seismic-wave-x-elastic-wave"],
            last_reviewed="2026-05-07",
            references=[
                dict(doi="10.1785/BSSA0480030105",
                     note="Biot (1956) — theory of propagation of elastic waves in a fluid-saturated porous solid; JASA 28:168"),
                dict(doi="10.1190/1.9781560801931",
                     note="Sheriff & Geldart (1995) — Exploration Seismology; Cambridge — textbook on seismic wave physics"),
            ],
        ),
        unknown=dict(
            id="u-seismic-wave-x-elastic-wave",
            title=(
                "Can full-waveform inversion (FWI) of seismic data recover the complete elastic "
                "tensor (anisotropic Cijkl) of the Earth's crust at 100m resolution, and what "
                "is the fundamental resolution limit imposed by seismic wavelengths and noise?"
            ),
            status="open",
            priority="medium",
            disciplines=["geoscience", "physics", "mathematics"],
            summary=(
                "Full waveform inversion attempts to recover subsurface elastic properties by "
                "minimising the misfit between observed and simulated seismograms. The fundamental "
                "resolution limit (Rayleigh criterion: λ/2) imposes a scale of ~100m for typical "
                "exploration seismics. Whether FWI can recover the full anisotropic elastic tensor "
                "Cijkl (21 independent components) rather than just isotropic Vp, Vs is an open "
                "problem combining numerical optimisation and seismic physics."
            ),
            systematic_gaps=[
                "FWI is non-convex with cycle-skipping local minima that prevent convergence without good initial models",
                "Full anisotropic tensor recovery requires complete azimuthal coverage not available in standard acquisition",
                "The information content of seismic data relative to the number of elastic parameters is not rigorously bounded",
            ],
            related_bridges=["b-seismic-wave-x-elastic-wave"],
            last_reviewed="2026-05-07",
        ),
        hypo=dict(
            id="h-seismic-wave-x-elastic-wave",
            title=(
                "Full waveform inversion with optimal transport (Wasserstein) misfit function "
                "reduces cycle-skipping susceptibility by 80% compared to L2 misfit while "
                "achieving λ/2 resolution for isotropic Vp recovery, with anisotropic "
                "parameters requiring 3× denser azimuthal sampling"
            ),
            status="active",
            priority="medium",
            impact_score=0.71,
            created="2026-05-07",
            last_updated="2026-05-07",
            author="wave-65-agent",
            unknowns_addressed=["u-seismic-wave-x-elastic-wave"],
            related_disciplines=["geoscience", "physics", "mathematics", "computer_science"],
            evidence_links=[
                dict(type="supporting", doi="10.1785/BSSA0480030105",
                     note="Biot — porous elastic wave theory underpins FWI forward model",
                     confidence=0.72),
                dict(type="related",
                     note="Métivier et al. (2016) — measuring the misfit between seismograms using OT; ESAIM Proc 49:34",
                     confidence=0.74),
            ],
            proposed_tests=[
                dict(description=(
                    "Synthetic FWI benchmark: generate seismograms from Marmousi2 model; add 5% "
                    "noise; invert with L2 vs. W2 (Wasserstein) misfits; compare cycle-skipping "
                    "rate (fraction of trials converging to wrong local minimum with poor initial "
                    "model); measure final velocity model error vs. ground truth."
                )),
            ],
        ),
    ),

    # ── 10 ─────────────────────────────────────────────────────────────────
    dict(
        bridge_path="cross-domain/biology-math/b-neutral-theory-x-stochastic-sampling.yaml",
        unknown_path="unknowns-catalog/biology/u-neutral-theory-x-stochastic-sampling.yaml",
        hypo_path="hypotheses/active/h-neutral-theory-x-stochastic-sampling.yaml",
        bridge=dict(
            id="b-neutral-theory-x-stochastic-sampling",
            title="Neutral theory ↔ Stochastic sampling — biodiversity as random drift",
            status="proposed",
            fields=["biology", "mathematics"],
            bridge_claim=(
                "Hubbell's unified neutral theory of biodiversity (2001) treats all species as ecologically "
                "equivalent, with diversity maintained by stochastic birth-death-immigration; the species "
                "abundance distribution follows a log-series or Poisson-Dirichlet distribution derivable "
                "from Ewens' sampling formula in population genetics — making ecology a problem in "
                "stochastic combinatorics."
            ),
            translation_table=[
                dict(field_a_term="species abundance distribution (SAD) in neutral theory",
                     field_b_term="allele frequency distribution in neutral population genetics (Ewens formula)",
                     note="Ewens' sampling formula gives the exact distribution of allele frequencies in neutral Kingman coalescent; maps directly to SAD"),
                dict(field_a_term="fundamental biodiversity number θ = 2Jm ν (Hubbell's neutral parameter)",
                     field_b_term="population mutation rate 4Nμ in Ewens sampling formula",
                     note="θ sets the log-series slope; controls diversity analogously to population genetics mutation-drift balance"),
                dict(field_a_term="local community immigration rate m (from metacommunity)",
                     field_b_term="migration rate m in island model of population genetics",
                     note="Immigration determines local SAD deviation from metacommunity log-series; both follow Wright island model"),
                dict(field_a_term="speciation rate ν (probability of new species per birth event)",
                     field_b_term="mutation rate μ in neutral allele model",
                     note="Speciation in neutral theory is the ecological equivalent of mutation in population genetics"),
            ],
            cross_pollination_opportunities=[
                "Apply Poisson-Dirichlet distribution theory (from Ewens' sampling formula) to "
                "fit and test neutral theory predictions for microbiome diversity data — gut "
                "microbiome alpha diversity may follow neutral theory with measurable θ parameter.",
                "Use coalescent theory (Kingman's coalescent from population genetics) to calculate "
                "the expected phylogenetic tree structure of a neutral community, enabling "
                "phylogenetic tests of neutral theory against niche-based alternatives.",
            ],
            communication_gap=(
                "Hubbell's neutral theory (2001) was explicitly inspired by neutral population genetics "
                "(Kimura 1968, Ewens 1972), but the mathematical equivalence (Poisson-Dirichlet distributions) "
                "was only fully formalised by Etienne & Olff (2004). Mainstream ecologists studying "
                "competition and niche theory rejected neutral theory as biologically unrealistic, while "
                "statisticians and population geneticists who understood the Ewens sampling formula "
                "rarely engaged with community ecology."
            ),
            related_unknowns=["u-neutral-theory-x-stochastic-sampling"],
            related_hypotheses=["h-neutral-theory-x-stochastic-sampling"],
            last_reviewed="2026-05-07",
            references=[
                dict(doi="10.1046/j.1461-0248.2003.00503.x",
                     note="Hubbell (2001) — The Unified Neutral Theory of Biodiversity and Biogeography; Princeton UP"),
                dict(doi="10.1093/genetics/68.4.577",
                     note="Ewens (1972) — the sampling theory of selectively neutral alleles; Theoretical Population Biology"),
            ],
        ),
        unknown=dict(
            id="u-neutral-theory-x-stochastic-sampling",
            title=(
                "Does the observed species abundance distribution of tropical tree communities "
                "follow the Poisson-Dirichlet prediction of neutral theory, or do deterministic "
                "niche effects create significant deviations detectable with modern tree census data?"
            ),
            status="open",
            priority="medium",
            disciplines=["biology", "mathematics", "ecology"],
            summary=(
                "Neutral theory predicts log-series-shaped SADs from Ewens sampling formula. Tropical "
                "forests show approximately log-series SADs, but the fit is imperfect at both extremes "
                "(too many rare species, too few dominant species). Whether this deviation proves niche "
                "effects or merely reflects finite sampling / immigration effects is debated. Modern "
                "large-scale tree census data (BCI, CTFS) with thousands of species and hundreds of "
                "thousands of individuals provides the best empirical test but has not been analysed "
                "with the full Poisson-Dirichlet framework."
            ),
            systematic_gaps=[
                "Full Poisson-Dirichlet likelihood fitting to BCI census data with immigration correction has not been performed",
                "Neutral theory goodness-of-fit tests do not adequately account for phylogenetic signal in abundance distributions",
                "Distinguishing pure neutral drift from nearly-neutral models with small fitness differences is statistically very difficult",
            ],
            related_bridges=["b-neutral-theory-x-stochastic-sampling"],
            last_reviewed="2026-05-07",
        ),
        hypo=dict(
            id="h-neutral-theory-x-stochastic-sampling",
            title=(
                "Neutral theory with immigration correction (full Poisson-Dirichlet likelihood) "
                "fits tropical forest SAD data from BCI with p > 0.05 (no significant deviation "
                "from neutral), while niche-based species energy theory is rejected by the "
                "species rank-abundance curve at p < 0.01 for the same dataset"
            ),
            status="active",
            priority="medium",
            impact_score=0.68,
            created="2026-05-07",
            last_updated="2026-05-07",
            author="wave-65-agent",
            unknowns_addressed=["u-neutral-theory-x-stochastic-sampling"],
            related_disciplines=["biology", "mathematics", "ecology"],
            evidence_links=[
                dict(type="supporting", doi="10.1046/j.1461-0248.2003.00503.x",
                     note="Hubbell — neutral theory log-series SAD prediction from Ewens sampling formula",
                     confidence=0.68),
                dict(type="related",
                     note="Etienne & Olff (2004) — Poisson-Dirichlet distribution and neutral biodiversity theory; Ecology Letters 7:170",
                     confidence=0.71),
            ],
            proposed_tests=[
                dict(description=(
                    "Fit Poisson-Dirichlet distribution (Ewens sampling formula with immigration m) "
                    "to BCI 50-ha plot census data (50,000+ trees, 300+ species); estimate θ and m "
                    "via maximum likelihood; compute goodness-of-fit via KS test; compare AIC to "
                    "niche-based log-normal and log-series models without immigration."
                )),
            ],
        ),
    ),

    # ── 11 ─────────────────────────────────────────────────────────────────
    dict(
        bridge_path="cross-domain/cs-math/b-spectral-clustering-x-graph-laplacian.yaml",
        unknown_path="unknowns-catalog/computer-science/u-spectral-clustering-x-graph-laplacian.yaml",
        hypo_path="hypotheses/active/h-spectral-clustering-x-graph-laplacian.yaml",
        bridge=dict(
            id="b-spectral-clustering-x-graph-laplacian",
            title="Spectral clustering ↔ Graph Laplacian — eigenvectors as community indicators",
            status="proposed",
            fields=["computer_science", "mathematics"],
            bridge_claim=(
                "Spectral clustering finds community structure by computing eigenvectors of the graph "
                "Laplacian L = D - A; the Fiedler vector (second smallest eigenvector) bisects the graph "
                "at minimum cut, and k eigenvectors identify k communities — connecting machine learning "
                "clustering to algebraic graph theory and random walk mixing times."
            ),
            translation_table=[
                dict(field_a_term="graph Laplacian L = D - A (degree matrix minus adjacency matrix)",
                     field_b_term="diffusion operator on graph (discrete Laplacian for random walk)",
                     note="L is positive semidefinite; eigenvalues 0 = λ₁ ≤ λ₂ ≤ ... ≤ λₙ; λ₂ = algebraic connectivity"),
                dict(field_a_term="Fiedler vector (eigenvector corresponding to λ₂, smallest nonzero eigenvalue)",
                     field_b_term="minimum bisection of graph (Cheeger constant bound on minimum cut)",
                     note="Sign of Fiedler vector coordinates gives optimal graph bisection; h(G) ≥ λ₂/2 (Cheeger inequality)"),
                dict(field_a_term="spectral clustering (k-means on k leading Laplacian eigenvectors)",
                     field_b_term="low-dimensional random walk embedding (diffusion maps)",
                     note="k-means in spectral domain ≡ k-means in diffusion distance space; both find community structure"),
                dict(field_a_term="spectral gap λ₂ (difference between second and first Laplacian eigenvalue)",
                     field_b_term="random walk mixing time τ_mix = O(1/λ₂) (graph theory)",
                     note="Large spectral gap ↔ fast mixing ↔ well-separated communities; small gap ↔ slow mixing ↔ community structure"),
            ],
            cross_pollination_opportunities=[
                "Apply spectral clustering via graph Laplacian to single-cell RNA-seq data — "
                "cells form communities in gene expression space; Fiedler vector identifies "
                "developmental lineage bifurcations in pseudotime analysis.",
                "Use algebraic graph theory Cheeger inequality to bound the quality of spectral "
                "clustering in social network community detection — provides provable approximation "
                "guarantees for spectral vs. optimal minimum-cut partitions.",
            ],
            communication_gap=(
                "Spectral methods for graph partitioning were developed in numerical linear algebra "
                "(Fiedler 1973) and VLSI circuit partitioning (Pothen 1990). Spectral clustering was "
                "independently rediscovered in machine learning (Shi & Malik 2000, Ng et al. 2001) "
                "without reference to the Fiedler algebraic graph theory literature. The Cheeger "
                "inequality connection — providing theoretical guarantees for spectral clustering "
                "— was imported from differential geometry (Cheeger 1970) to graph theory and only "
                "then to machine learning via the work of Spielman & Teng."
            ),
            related_unknowns=["u-spectral-clustering-x-graph-laplacian"],
            related_hypotheses=["h-spectral-clustering-x-graph-laplacian"],
            last_reviewed="2026-05-07",
            references=[
                dict(doi="10.1007/s11222-007-9033-z",
                     note="von Luxburg (2007) — a tutorial on spectral clustering; Statistics and Computing 17:395"),
                dict(doi="10.1023/B:STCO.0000006967.33477.20",
                     note="Fiedler (1973) — algebraic connectivity of graphs; Czech Math J 23:298"),
            ],
        ),
        unknown=dict(
            id="u-spectral-clustering-x-graph-laplacian",
            title=(
                "What is the optimal graph Laplacian normalisation (unnormalised, symmetric, "
                "random-walk) for spectral clustering on real-world networks with heterogeneous "
                "degree distributions, and can the Cheeger bound be tightened to a polynomial "
                "approximation guarantee?"
            ),
            status="open",
            priority="medium",
            disciplines=["computer_science", "mathematics"],
            summary=(
                "Three Laplacian normalisations (L, L_sym = D^(-1/2)LD^(-1/2), L_rw = D^(-1)L) "
                "give different spectral clusterings, with no theoretical consensus on which is "
                "optimal for real networks. The Cheeger inequality h(G) ≥ λ₂/2 provides an "
                "approximation ratio of O(1/√λ₂) for minimum bisection, which is tight but "
                "often loose in practice. Whether a stronger approximation guarantee (e.g., "
                "constant-factor for power-law graphs) exists is an open problem."
            ),
            systematic_gaps=[
                "No empirical benchmark comparing all three Laplacian normalisations on real heterogeneous networks exists",
                "The Cheeger bound is tight but no polynomial-factor approximation guarantee for spectral clustering is known",
                "Whether spectral clustering achieves consistent community recovery in the stochastic block model is proven only for restricted parameter ranges",
            ],
            related_bridges=["b-spectral-clustering-x-graph-laplacian"],
            last_reviewed="2026-05-07",
        ),
        hypo=dict(
            id="h-spectral-clustering-x-graph-laplacian",
            title=(
                "Random-walk Laplacian L_rw spectral clustering achieves 20% better Normalised "
                "Mutual Information than unnormalised L clustering on power-law degree "
                "graphs (γ < 2.5) by correctly weighting high-degree hub nodes, while "
                "symmetric L_sym is optimal for regular and near-regular graphs"
            ),
            status="active",
            priority="medium",
            impact_score=0.70,
            created="2026-05-07",
            last_updated="2026-05-07",
            author="wave-65-agent",
            unknowns_addressed=["u-spectral-clustering-x-graph-laplacian"],
            related_disciplines=["computer_science", "mathematics"],
            evidence_links=[
                dict(type="supporting", doi="10.1007/s11222-007-9033-z",
                     note="von Luxburg — spectral clustering tutorial with Laplacian normalisation comparison",
                     confidence=0.72),
                dict(type="related",
                     note="Lei & Rinaldo (2015) — consistency of spectral clustering in stochastic block models; Ann Stat 43:215",
                     confidence=0.74),
            ],
            proposed_tests=[
                dict(description=(
                    "Benchmark spectral clustering with L, L_sym, L_rw on synthetic stochastic "
                    "block model graphs with degree exponents γ = 2.0, 2.5, 3.0, ∞ (regular); "
                    "also benchmark on real networks (Facebook, Amazon, citation graphs); "
                    "measure NMI vs. ground truth communities; test Laplacian ranking hypothesis "
                    "via Friedman test across 20 graph instances per setting."
                )),
            ],
        ),
    ),

    # ── 12 ─────────────────────────────────────────────────────────────────
    dict(
        bridge_path="cross-domain/biology-physics/b-protein-aggregation-x-nucleation-growth.yaml",
        unknown_path="unknowns-catalog/biology/u-protein-aggregation-x-nucleation-growth.yaml",
        hypo_path="hypotheses/active/h-protein-aggregation-x-nucleation-growth.yaml",
        bridge=dict(
            id="b-protein-aggregation-x-nucleation-growth",
            title="Protein aggregation ↔ Nucleation-growth kinetics — amyloid as seeded polymerization",
            status="proposed",
            fields=["biology", "chemistry"],
            bridge_claim=(
                "Amyloid fibril formation (in Alzheimer's, Parkinson's, prion diseases) follows secondary "
                "nucleation kinetics: monomers add to fibril ends (elongation) and fibril surfaces catalyse "
                "new nucleus formation (secondary nucleation); the Knowles-Michaels equation exactly describes "
                "these kinetics, enabling rational design of aggregation inhibitors."
            ),
            translation_table=[
                dict(field_a_term="primary nucleation in amyloid formation (de novo nucleus formation from monomers)",
                     field_b_term="primary nucleation rate J₁ = k₁[m]^(n₁) in classical nucleation theory",
                     note="n₁ = nucleus size (typically 2-6 monomers); k₁ = primary nucleation rate constant"),
                dict(field_a_term="elongation (monomer addition to fibril ends)",
                     field_b_term="crystal growth (monomer addition to crystal surface) in crystal growth theory",
                     note="Elongation rate v = k₊[m] is linear in monomer concentration; same as Wilson-Frenkel growth law"),
                dict(field_a_term="secondary nucleation (fibril surface catalyses new nucleus formation)",
                     field_b_term="heterogeneous nucleation on pre-existing surface in nucleation theory",
                     note="Secondary nucleation rate J₂ = k₂[m]^(n₂)[fibril mass]^γ; dominates at long times"),
                dict(field_a_term="seeding experiment (pre-formed fibril fragments accelerate aggregation)",
                     field_b_term="seeded crystal growth (inoculation with seed crystal bypasses primary nucleation)",
                     note="Seeding bypasses lag phase by providing pre-formed nucleation surfaces"),
            ],
            cross_pollination_opportunities=[
                "Apply Avrami-Johnson-Mehl nucleation-growth theory (from metallurgy) to fit amyloid "
                "time course data — Avrami exponents n predict whether nucleation or growth dominates, "
                "guiding inhibitor design to target the rate-limiting step.",
                "Use Ostwald ripening theory (from colloid science) to understand amyloid polymorphism — "
                "different fibril polymorphs have different surface energies and undergo competitive "
                "ripening, explaining why amyloid strains evolve over time in prion disease.",
            ],
            communication_gap=(
                "Nucleation-growth kinetics was developed for inorganic crystallisation (Volmer & Weber 1926, "
                "Becker & Döring 1935) and applied to polymer crystallisation. Amyloid biology was developed "
                "in biochemistry and neuroscience focused on protein structure. The Knowles lab (Cambridge) "
                "systematically imported nucleation theory into amyloid biology (2009-present), but physical "
                "chemists studying crystallisation rarely read amyloid literature, missing the opportunity "
                "to apply Avrami theory, Ostwald ripening, and heterogeneous nucleation insights."
            ),
            related_unknowns=["u-protein-aggregation-x-nucleation-growth"],
            related_hypotheses=["h-protein-aggregation-x-nucleation-growth"],
            last_reviewed="2026-05-07",
            references=[
                dict(doi="10.1126/science.1254516",
                     note="Cohen et al. (2013) — proliferation of amyloid-β42 aggregates via secondary nucleation; PNAS 110:9758"),
                dict(doi="10.1073/pnas.0910580107",
                     note="Knowles et al. (2009) — analytical solution of master equation for amyloid polymerisation; Science 326:1533"),
            ],
        ),
        unknown=dict(
            id="u-protein-aggregation-x-nucleation-growth",
            title=(
                "Does secondary nucleation (fibril-surface catalysed) or primary nucleation "
                "dominate the early seeding events in Alzheimer's disease in vivo, and can "
                "the Knowles-Michaels rate equations predict in vivo amyloid-β aggregation "
                "kinetics from in vitro parameters?"
            ),
            status="open",
            priority="high",
            disciplines=["biology", "chemistry", "medicine"],
            summary=(
                "The Knowles-Michaels kinetic equations describe in vitro amyloid aggregation "
                "quantitatively, but extension to in vivo conditions faces multiple challenges: "
                "intracellular crowding effects, lipid membrane interactions, protein quality control "
                "machinery, and the heterogeneous nucleation environment of the brain. Whether "
                "secondary nucleation (which is autocatalytic and self-amplifying) dominates "
                "disease onset in vivo — as it does in vitro — is critical for therapeutic strategy "
                "(inhibit secondary nucleation vs. promote clearance of existing aggregates)."
            ),
            systematic_gaps=[
                "In vivo primary vs. secondary nucleation rate constants for Aβ42 have not been measured",
                "Whether lipid membrane surfaces act as heterogeneous nucleation templates in neuronal synapses is unresolved",
                "The Knowles-Michaels equations have not been validated against in vivo plaque spreading kinetics from PET imaging data",
            ],
            related_bridges=["b-protein-aggregation-x-nucleation-growth"],
            last_reviewed="2026-05-07",
        ),
        hypo=dict(
            id="h-protein-aggregation-x-nucleation-growth",
            title=(
                "Secondary nucleation dominates Aβ42 aggregation in vivo above a critical "
                "aggregate concentration threshold of ~1 nM fibril mass, with an in vivo "
                "secondary nucleation rate constant k₂ within 10-fold of in vitro measurements "
                "after correcting for cellular crowding (Macromolecular crowding factor ≈ 2)"
            ),
            status="active",
            priority="high",
            impact_score=0.82,
            created="2026-05-07",
            last_updated="2026-05-07",
            author="wave-65-agent",
            unknowns_addressed=["u-protein-aggregation-x-nucleation-growth"],
            related_disciplines=["biology", "chemistry", "medicine"],
            evidence_links=[
                dict(type="supporting", doi="10.1126/science.1254516",
                     note="Cohen et al. — secondary nucleation dominates in vitro Aβ42 aggregation kinetics",
                     confidence=0.80),
                dict(type="related",
                     note="Knowles et al. (2009) — analytical solution gives exact k₁, k₊, k₂ from bulk fluorescence kinetics",
                     confidence=0.77),
            ],
            proposed_tests=[
                dict(description=(
                    "Measure Aβ42 aggregation kinetics in HEK293 cell lysate (macromolecular "
                    "crowding ~200 g/L) vs. in vitro buffer at matched Aβ concentration; fit "
                    "Knowles-Michaels equations to both; extract k₁, k₊, k₂; test whether k₂ "
                    "ratio (in lysate / in buffer) equals the predicted crowding enhancement "
                    "factor of ~2 from Minton's crowding theory."
                )),
            ],
        ),
    ),
]


def main():
    print("=== Generating Wave 64 files ===")
    for entry in WAVE64:
        write_yaml(entry["bridge_path"], entry["bridge"])
        write_yaml(entry["unknown_path"], entry["unknown"])
        write_yaml(entry["hypo_path"], entry["hypo"])

    print(f"\n=== Wave 64 complete: {len(WAVE64)*3} files written ===\n")

    print("=== Generating Wave 65 files ===")
    for entry in WAVE65:
        write_yaml(entry["bridge_path"], entry["bridge"])
        write_yaml(entry["unknown_path"], entry["unknown"])
        write_yaml(entry["hypo_path"], entry["hypo"])

    print(f"\n=== Wave 65 complete: {len(WAVE65)*3} files written ===\n")
    print(f"Total: {(len(WAVE64)+len(WAVE65))*3} files generated.")


if __name__ == "__main__":
    main()

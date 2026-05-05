"""Extra unknowns + hypotheses + bridges for Phase 0 500+ target."""
import os

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  Created: {os.path.basename(path)}')

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ────────────────────────────────────────────────────────────────
# EXTRA UNKNOWNS (4 more to guarantee 500+ total)
# ────────────────────────────────────────────────────────────────
extras = {
    os.path.join(BASE, 'unknowns-catalog', 'linguistics', 'u-language-contact-convergence-limit.yaml'):
        "id: u-language-contact-convergence-limit\ntitle: What is the maximum degree of structural convergence possible between unrelated contact languages, and what constraints prevent full convergence?\nstatus: open\npriority: medium\ndisciplines:\n  - linguistics\n  - contact-linguistics\n  - linguistic-typology\nsummary: >\n  Language contact produces structural convergence in addition to lexical borrowing.\n  The Balkan Sprachbund and South Asian linguistic area show unrelated languages can\n  converge on shared structural features. Whether there are universal limits on\n  structural convergence is debated.\nsystematic_gaps:\n  - A typologically complete borrowability hierarchy for all structural features has not been established.\n  - The social conditions that facilitate versus resist structural borrowing are not generalised.\n  - Timescales required for structural convergence in different feature domains are not estimated.\nlast_reviewed: '2026-05-05'\n",

    os.path.join(BASE, 'unknowns-catalog', 'social-science', 'u-collective-memory-formation.yaml'):
        "id: u-collective-memory-formation\ntitle: How do collective memories of historical events form, persist, and distort across generations, and what factors determine their cultural salience?\nstatus: open\npriority: medium\ndisciplines:\n  - social-science\n  - sociology\n  - history\nsummary: >\n  Collective memory shapes national identity, inter-group conflict, and political\n  behaviour. Studies show that collective memories are selectively constructed,\n  politically managed, and transmitted through education and ritual. What determines\n  which events become collectively memorable and which are forgotten is not well theorised.\nsystematic_gaps:\n  - The mechanisms by which collective memory is transmitted across generational boundaries are not well characterised.\n  - The relationship between individual autobiographical memory and collective memory involves unknown aggregation processes.\n  - State memory management (censorship, commemoration) has heterogeneous effects not captured by current models.\nlast_reviewed: '2026-05-05'\n",

    os.path.join(BASE, 'unknowns-catalog', 'economics', 'u-market-microstructure-price-formation.yaml'):
        "id: u-market-microstructure-price-formation\ntitle: What determines the speed and efficiency of price discovery in financial markets, and how does high-frequency trading affect market quality?\nstatus: open\npriority: medium\ndisciplines:\n  - economics\n  - financial-economics\n  - market-microstructure\nsummary: >\n  High-frequency trading accounts for 50-60 percent of US equity volume. Whether HFT\n  improves market quality (narrower spreads, faster price discovery) or degrades it\n  (arms race costs, flash crashes, adverse selection for slower traders) is empirically\n  contested.\nsystematic_gaps:\n  - The welfare effects of HFT on institutional and retail investors require counterfactual markets that do not exist.\n  - The relationship between HFT and market fragility (flash crashes) is not causally established.\n  - Cross-market contagion through HFT arbitrage strategies is theoretically predicted but empirically difficult to measure.\nlast_reviewed: '2026-05-05'\n",

    os.path.join(BASE, 'unknowns-catalog', 'economics', 'u-creative-economy-measurement.yaml'):
        "id: u-creative-economy-measurement\ntitle: How should the creative economy be measured in national accounts, and does it drive innovation spillovers to other sectors?\nstatus: open\npriority: low\ndisciplines:\n  - economics\n  - cultural-economics\n  - innovation-studies\nsummary: >\n  Creative industries contribute 3-10 percent of GDP in high-income countries depending\n  on definition. National accounts poorly capture creative value: digital goods are\n  often underpriced, intangible assets are not fully included, and spillover effects\n  to other industries are not measured.\nsystematic_gaps:\n  - No consistent international definition of the creative economy enables cross-country comparison.\n  - The economic spillovers from creative clusters to other industries are estimated with inconsistent methods.\n  - Digital disruption of creative industries has changed value creation in ways not reflected in national accounts.\nlast_reviewed: '2026-05-05'\n",
}

print("Creating 4 extra unknowns...")
for path, content in extras.items():
    write(path, content)

# ────────────────────────────────────────────────────────────────
# HYPOTHESES (8 new)
# ────────────────────────────────────────────────────────────────
HYP_DIR = os.path.join(BASE, 'hypotheses', 'active')
os.makedirs(HYP_DIR, exist_ok=True)

hypotheses = {
    'h-quantum-advantage-noise-threshold.yaml':
        "id: h-quantum-advantage-noise-threshold\ntitle: Quantum processors achieve practical advantage over classical algorithms only when two-qubit gate fidelity exceeds 99.9 percent across all qubits simultaneously\nstatus: active\ncreated: '2026-05-05'\npriority: high\nimpact_score: 9\nevidence_links: []\nrelated_unknowns:\n  - u-quantum-advantage-classical-boundary\n  - u-topological-qc-fault-tolerance-threshold\n",

    'h-polarisation-ising-phase-transition.yaml':
        "id: h-polarisation-ising-phase-transition\ntitle: Political polarisation dynamics undergo a genuine phase transition at a critical partisan homophily threshold, analogous to the Ising ferromagnetic transition\nstatus: active\ncreated: '2026-05-05'\npriority: high\nimpact_score: 8\nevidence_links: []\nrelated_unknowns:\n  - u-political-polarisation-dynamics\n  - u-social-contagion-vs-homophily\n",

    'h-linguistic-relativity-neural-boundary.yaml':
        "id: h-linguistic-relativity-neural-boundary\ntitle: Linguistic relativity effects on color perception are mediated exclusively by left-hemisphere language areas and disappear when verbal processing is suppressed by concurrent verbal shadowing\nstatus: active\ncreated: '2026-05-05'\npriority: medium\nimpact_score: 7\nevidence_links: []\nrelated_unknowns:\n  - u-linguistic-relativity-cognition\n  - u-linguistic-relativity-color-perception\n",

    'h-carbon-price-optimal-100.yaml':
        "id: h-carbon-price-optimal-100\ntitle: The social cost of carbon, corrected for distribution weights and risk aversion, exceeds 200 USD per tonne CO2 in 2026 under any plausible discount rate below 3 percent\nstatus: active\ncreated: '2026-05-05'\npriority: high\nimpact_score: 9\nevidence_links: []\nrelated_unknowns:\n  - u-carbon-price-optimal-level\n",

    'h-neuroinflammation-depression-biomarker.yaml':
        "id: h-neuroinflammation-depression-biomarker\ntitle: CRP level above 3 mg/L identifies a biologically distinct depression subtype that responds to anti-inflammatory treatment but not to SSRIs, with effect size at least 0.5\nstatus: active\ncreated: '2026-05-05'\npriority: high\nimpact_score: 9\nevidence_links: []\nrelated_unknowns:\n  - u-neuroinflammation-depression-causality\n",

    'h-soil-microbiome-carbon-enhancement.yaml':
        "id: h-soil-microbiome-carbon-enhancement\ntitle: Inoculating agricultural soils with high-carbon-use-efficiency microbial consortia increases soil organic carbon sequestration by at least 20 percent over 5 years without reducing crop yields\nstatus: active\ncreated: '2026-05-05'\npriority: medium\nimpact_score: 8\nevidence_links: []\nrelated_unknowns:\n  - u-soil-microbiome-carbon-cycling\n",

    'h-llm-scaling-emergence-artifact.yaml':
        "id: h-llm-scaling-emergence-artifact\ntitle: All reported emergent capabilities in large language models are metric artifacts of nonlinear evaluation functions and disappear when measured on continuous scales\nstatus: active\ncreated: '2026-05-05'\npriority: high\nimpact_score: 8\nevidence_links: []\nrelated_unknowns:\n  - u-emergent-capabilities-llm-prediction\n  - u-transformer-scaling-law-limits\n",

    'h-rewilding-trophic-cascade-predictability.yaml':
        "id: h-rewilding-trophic-cascade-predictability\ntitle: The magnitude of trophic cascades following large predator reintroduction is predictable from prey biomass, prey behavioral plasticity, and landscape connectivity with R-squared greater than 0.6\nstatus: active\ncreated: '2026-05-05'\npriority: medium\nimpact_score: 7\nevidence_links: []\nrelated_unknowns:\n  - u-rewilding-ecosystem-outcomes\n",
}

print("\nCreating 8 hypotheses...")
for filename, content in hypotheses.items():
    write(os.path.join(HYP_DIR, filename), content)

# ────────────────────────────────────────────────────────────────
# BRIDGES (2 new — bridges 39 and 40)
# ────────────────────────────────────────────────────────────────
# Find existing bridge directories and create new ones
bridge_39_dir = os.path.join(BASE, 'cross-domain', 'linguistics-physics')
bridge_40_dir = os.path.join(BASE, 'cross-domain', 'social-physics')

b39 = """id: b-linguistic-relativity-quantum-basis
title: >
  Linguistic relativity (Sapir-Whorf) and quantum measurement basis choice both reveal
  how the observer's representational framework determines what aspects of an
  underdetermined reality become definite.
status: proposed
fields:
  - linguistics
  - quantum-mechanics
  - philosophy-of-mind
  - cognitive-science
bridge_claim: >
  Linguistic relativity holds that the language one speaks shapes what aspects of
  perceptual reality are discriminated and categorised. Quantum measurement theory
  holds that the choice of measurement basis determines which quantum property becomes
  definite upon measurement. In both cases, an observer's representational apparatus
  (lexical categories vs measurement operators) acts as a filter that creates rather
  than merely records a slice of an otherwise indeterminate reality. The parallel is
  not merely metaphorical: both effects have formal structure (Wigner's friend in QM;
  categorical perception in linguistics) and both reveal observer-dependence of
  apparent facts about the world. Neither field has engaged the other's literature.
translation_table:
  - field_a_term: lexical category boundary (e.g., blue/green distinction)
    field_b_term: measurement basis (e.g., x-spin vs z-spin)
    note: The representational choice that determines what contrast becomes perceptible/definite
  - field_a_term: categorical perception effect
    field_b_term: projection postulate (state collapses to eigenstate)
    note: The act of applying a category sharpens the representation of what was diffuse
  - field_a_term: linguistic relativity effect size
    field_b_term: basis rotation angle (degree of incompatible measurement)
    note: How different the two frameworks are determines how different the induced realities are
  - field_a_term: cross-linguistic universals (color focal points)
    field_b_term: preferred measurement bases (eigenstates of Hamiltonian)
    note: Some representations are more natural/stable than others regardless of observer choice
cross_pollination_opportunities:
  - Apply quantum contextuality formalisms to model how linguistic context determines
    interpretation of ambiguous expressions — context-dependent meaning as quantum contextuality.
  - Use categorical perception paradigms to test whether quantum-like probability updating
    (order effects in judgment) follow the same pattern as cross-categorical discrimination.
  - Develop formal linguistic relativity measures analogous to quantum entanglement measures
    to quantify how much a language shapes perception across domains.
communication_gap: >
  Linguists studying Sapir-Whorf work in cognitive science and anthropology journals;
  quantum foundations researchers publish in physics and philosophy of physics. Neither
  reads the other. The connection has been noted informally but never formalised.
last_reviewed: "2026-05-05"
related_unknowns:
  - u-linguistic-relativity-cognition
  - u-many-worlds-copenhagen-experimental
  - u-quantum-darwinism-evidence
"""

b40 = """id: b-social-ising-polarisation
title: >
  Political polarisation dynamics in networked populations are mathematically equivalent
  to the Ising model ferromagnetic phase transition, with partisan identity as spin,
  echo chambers as ferromagnetic domains, and social influence strength as inverse
  temperature.
status: proposed
fields:
  - political-science
  - statistical-physics
  - network-science
  - social-science
bridge_claim: >
  The Ising model describes how local alignment interactions between magnetic spins
  produce global ordered phases (ferromagnetism) or disordered phases (paramagnetism)
  depending on temperature. Political polarisation shows strikingly similar dynamics:
  individuals align their views with social neighbours (local influence), partisan
  sorting produces large-scale ideological clusters (ferromagnetic domains), and
  critical transitions from pluralist to polarised states resemble phase transitions.
  Quantitative analogies include the susceptibility peak near the critical point
  (maximum persuadability as partisan identity hardens), the diverging correlation
  length (viewpoints becoming correlated across longer network distances), and
  spontaneous symmetry breaking (arbitrary advantage of one side snowballing into
  dominance). Statistical physics has rigorous tools for these phenomena; political
  science has the empirical data and domain understanding.
translation_table:
  - field_a_term: spin (up or down)
    field_b_term: partisan identity (Democrat or Republican)
    note: The binary state variable; extensions to Potts model can handle multi-party systems
  - field_a_term: exchange coupling J
    field_b_term: social influence strength (peer pressure, media consumption homophily)
    note: The tendency to align with neighbours; heterogeneous J maps to variable influence susceptibility
  - field_a_term: temperature T
    field_b_term: inverse of social conformity pressure (openness to persuasion)
    note: High T = disordered opinions; low T = locked-in partisan alignment
  - field_a_term: ferromagnetic phase transition at T_c
    field_b_term: polarisation tipping point (sudden shift from pluralist to sorted society)
    note: Below T_c, spontaneous magnetisation appears — below the political threshold, partisan sorting locks in
  - field_a_term: external magnetic field H
    field_b_term: elite messaging / media framing (directional push on population opinion)
    note: H breaks symmetry and can trigger or prevent magnetisation in one direction
  - field_a_term: domain walls
    field_b_term: geographical and social boundaries between partisan communities
    note: Domain walls are costly (frustration) in the Ising model; partisan boundaries involve costly cross-cutting ties
cross_pollination_opportunities:
  - Use renormalisation group analysis to identify which social variables are relevant versus
    irrelevant near the polarisation critical point, clarifying which interventions can shift
    the transition temperature.
  - Map survey data on partisan identity strength and cross-partisan tie frequency to Ising model
    parameters; test whether the susceptibility peak (maximum persuadability) coincides with the
    historical period of lowest polarisation.
  - Apply finite-size scaling to predict how polarisation dynamics differ in small versus large
    democracies, or in countries with different social network structures.
  - Design depolarisation interventions analogous to annealing protocols: gradually increasing
    the social temperature (cross-partisan exposure) to allow reordering without sudden phase
    transitions.
communication_gap: >
  Political scientists rarely engage statistical physics literature; physicists studying
  opinion dynamics rarely engage the substantive political science literature on polarisation
  mechanisms. Sociophysics models of opinion dynamics exist but are not integrated with
  empirical political science data. The Ising-polarisation analogy is qualitatively known
  in sociophysics but has not been operationalised with real partisan identity survey data
  and tested against the renormalisation group predictions.
last_reviewed: "2026-05-05"
related_unknowns:
  - u-political-polarisation-dynamics
  - u-social-norm-cascade-tipping-points
  - u-social-ising-universality
related_hypotheses:
  - h-polarisation-ising-phase-transition
"""

print("\nCreating 2 bridges...")
write(os.path.join(bridge_39_dir, 'b-linguistic-relativity-quantum-basis.yaml'), b39)
write(os.path.join(bridge_40_dir, 'b-social-ising-polarisation.yaml'), b40)

print("\n=== Summary ===")
print(f"Extra unknowns: {len(extras)}")
print(f"Hypotheses: {len(hypotheses)}")
print(f"Bridges: 2")

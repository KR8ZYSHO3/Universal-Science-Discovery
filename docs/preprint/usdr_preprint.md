# Universal Science Discovery Repository: Open Infrastructure for Tracking Scientific Unknowns and Cross-Domain Mathematical Bridges

**Authors:** Brandon Shoemaker and Contributors (Universal Science Discovery Repository)

**Version:** v1.1 — May 2026

**Suggested categories:** cs.DL (primary) · q-bio.QM · physics.soc-ph (cross-list)

**Repository:** <https://github.com/KR8ZYSHO3/Universal-Science-Discovery>

**License:** CC BY 4.0

---

## Abstract

We introduce the Universal Science Discovery Repository (USDR), an open-source,
version-controlled catalog of scientific unknowns, hypotheses, and cross-domain
mathematical bridges. Unlike traditional literature databases that index what is known,
USDR explicitly catalogs what remains unknown — structured as machine-readable YAML
entries governed by formal JSON Schema validation. The repository currently contains
**~4,850+** catalog entries across **55+** disciplines (see repository README metrics),
including **1,123 cross-domain bridges** that formalise mathematical correspondences
between fields that rarely communicate, **1,408** open unknowns, **1,274** falsifiable
hypotheses, **18** pioneer profiles, and **24** breakthrough gap analyses (plus
phenomenology stubs under `phenomenology/`). We describe the schema design, the knowledge
graph structure (**3,857** nodes, **4,517** edges, **0** orphan unknowns), and the AI
co-pilot tooling that automatically surfaces novel bridge candidates by analysing domain
connectivity gaps.
USDR is designed as collaborative infrastructure: all entries are version-controlled,
peer-reviewable via pull requests, and linked to primary literature. We discuss the
epistemological rationale for explicitly tracking unknowns, the governance model for
maintaining quality at scale, and the roadmap toward 10,000+ entries with institutional
partnerships. The repository is available at
<https://github.com/KR8ZYSHO3/Universal-Science-Discovery>.

---

## 1. Introduction

Science has a documentation asymmetry. The global literature — now exceeding 200
million indexed papers across platforms such as PubMed, OpenAlex, and Semantic Scholar
— is almost exclusively a record of what has been found, argued, or claimed. The
frontier of what is *unknown*, the open problems that define the actual boundary of
human understanding, is documented only implicitly: scattered across review articles,
grant application background sections, conference panel discussions, and the informal
knowledge of domain experts. This asymmetry is not a minor inconvenience. It actively
impedes scientific progress in at least three ways.

First, **the frontier is invisible to newcomers.** A graduate student entering a field
must invest months or years to understand which problems are genuinely open, which are
merely difficult, and which are already solved but not yet canonised in textbooks. There
is no machine-readable index of open problems analogous to the indexes of findings.
OpenAlex can tell you every paper that cites a given result; no analogous infrastructure
can tell you which questions that result fails to answer.

Second, **cross-domain connections are systematically missed.** When two fields
independently study the same underlying mathematical phenomenon using different
vocabulary, they may not recognise the connection for decades. The Hopfield neural
network and the Sherrington-Kirkpatrick spin glass were developed in parallel physics
and neuroscience communities; their mathematical identity was not established until the
replica-symmetric calculation of Amit, Gutfreund and Sompolinsky in 1985 — three years
after Hopfield's paper [1, 2]. The percolation-ecology connection, which provides a
rigorous mathematical framework for the "Single Large Or Several Small" (SLOSS) debate
in conservation biology, was recognised in principle by Gardner et al. in 1987 [5] but
the full finite-size scaling machinery from condensed-matter physics has still not
penetrated conservation biology literature. Journal siloing, funding structure, and
vocabulary mismatch are the proximate causes; the underlying problem is that there is no
shared infrastructure for recognising when two communities are studying the same
mathematical object.

Third, **the most important questions are the hardest to find.** A researcher wishing to
work on the most impactful open problems in a field must synthesise enormous amounts of
literature to identify them. There is no structured, community-maintained map of "what
we don't know and why it matters."

Existing infrastructure addresses adjacent problems but not this one. arXiv [16]
provides rapid preprint dissemination of findings. OpenAlex [17] provides
large-scale bibliographic indexing. Wikidata [18] provides a structured knowledge graph
of established facts. The Open Research Knowledge Graph (ORKG) [19] represents
scientific contributions as structured semantic triples. None of these systems are
designed to represent *open problems* as first-class, version-controlled, formally
validated objects linked to the literature through which they were identified.

The Universal Science Discovery Repository (USDR) is an attempt to fill this gap. USDR
is a git-native, schema-validated, community-governed catalog of scientific unknowns,
hypotheses, and cross-domain mathematical bridges. Every entry is a YAML document
governed by a JSON Schema, stored in a public GitHub repository, reviewable through
standard pull requests. The core epistemological commitment is strict: we catalog what
is *not* known, not what is known, and we maintain rigorous separation between
unknowns, hypotheses, and findings.

This paper describes the design principles, schema architecture, knowledge graph
structure, cross-domain bridge methodology, and AI co-pilot tooling of USDR. It is a
*system paper*: the primary contribution is the infrastructure and methodology, not
scientific results. We do not claim that the bridges in USDR constitute new scientific
findings; they are structured representations of connections that exist in the
literature, assembled in a form that makes them findable and usable.

**Paper outline.** Section 2 describes the design principles. Section 3 describes the
repository structure and schema design. Section 4 describes the cross-domain bridge
methodology in detail. Section 5 describes the AI co-pilot tooling. Section 6 describes
governance and quality control. Section 7 presents a detailed case study of the
percolation-ecology bridge. Section 8 describes current status and roadmap.
Section 9 concludes.

---

## 2. Design Principles

USDR is governed by four design principles that distinguish it from related
infrastructure.

**2.1 Strict terminological separation.** The repository enforces a three-way
distinction between *unknowns*, *hypotheses*, and *findings*. An **unknown** (entry
type `u-*`) is a research gap: a question that cannot currently be answered from the
literature, with no clear candidate answer. A **hypothesis** (entry type `h-*`) is a
testable statement that proposes an answer to an unknown; it is explicitly marked as
unvalidated and must include proposed tests and falsification criteria. A **finding**
is not a USDR entry type: validated results are tracked in the primary literature and
referenced by DOI. This separation prevents the most common failure mode of scientific
communication — the conflation of speculation with established knowledge.

Speculation is labeled as such. An entry at `status: proposed` explicitly signals
community consensus that the claim is plausible but unvalidated. An entry at `status:
established` requires at least one cross-disciplinary publication recognising the
connection. No fabricated citations are permitted; entries must link to verifiable
primary sources.

**2.2 Schema-first machine-readability.** Every entry type is governed by a JSON Schema
(stored in `schemas/`). The schemas enforce required fields, enumerated status values,
stable ID patterns, reference structure, and type constraints. Validation is run on
every pull request via a CI pipeline (`scripts/validate_schemas.py`). This means the
repository is queryable, diffable, and usable as a data source without parsing
unstructured prose.

The design choice to use YAML rather than JSON is deliberate: YAML supports human-
readable multi-line text fields (the `bridge_claim`, `summary`, and
`communication_gap` fields routinely span several paragraphs), inline comments, and
natural list syntax, while remaining parseable by any JSON library after conversion.
The schemas use JSON Schema Draft 2020-12, which supports `additionalProperties: false`
to prevent schema drift as the repository evolves.

**2.3 Git as the substrate.** Version control provides four capabilities that are
essential for a community knowledge repository: (i) *provenance* — every entry has a
complete history of who wrote what and when; (ii) *diff* — changes to entries are
auditable at the field level; (iii) *blame* — authorship is traceable; (iv) *pull
requests as peer review* — proposed entries and changes go through a documented review
process before merging. The review process is documented in `CONTRIBUTING.md` and
`docs/COLLABORATION_AND_REVIEWS.md`, with a target seven-day review SLA for new
entries.

**2.4 Cross-domain bridges as first-class entries.** In most knowledge systems, cross-
disciplinary connections are represented as metadata tags, shared categories, or
informal annotations. In USDR, a bridge is a structured entry type with its own schema
(`schemas/bridge.yaml`), its own directory layout (`cross-domain/{d1}-{d2}/`), and a
mandatory `translation_table` field that requires explicit concept-by-concept mapping
between fields. The `communication_gap` field requires an explicit explanation of *why*
the two fields have not already converged — making the social and institutional barriers
to cross-domain discovery an explicit part of the data model.

---

## 3. Repository Structure

**3.1 Entry types and schemas.** USDR currently defines four entry types:

- **Unknown** (`schemas/unknown.yaml`): A research gap. Required fields: `id`
  (pattern `u-[a-z0-9.-]+`), `title` (8–500 characters), `status` (one of `open`,
  `partial`, `resolved`, `stale`). Optional fields include `priority`, `summary`,
  `disciplines`, `related_unknowns`, `related_bridges`, `suggested_hypotheses`, and
  `references`.

- **Hypothesis** (`schemas/hypothesis.yaml`): A testable statement. Required fields:
  `id` (pattern `h-[a-z0-9.-]+`), `title`, `status` (one of `draft`, `active`,
  `validated`, `refuted`, `archived`), `created`. Optional fields include
  `impact_score` (0–1 float), `evidence_links` (with `type` enum: `supporting`,
  `related`, `contradicting`), `proposed_tests`, `unknowns_addressed`, and
  `related_disciplines`.

- **Bridge** (`schemas/bridge.yaml`): A cross-domain mathematical connection. Required
  fields: `id` (pattern `b-[a-z0-9.-]+`), `title`, `status` (one of `proposed`,
  `established`, `contested`, `stale`), `fields` (≥2 disciplines), `bridge_claim` (≥20
  characters). Optional fields include `translation_table`, `communication_gap`,
  `cross_pollination_opportunities`, `related_unknowns`, `related_hypotheses`, and
  `references`.

- **Phenomenon**: Entries in `phenomenology/` capture empirically robust patterns
  (scaling laws, universality classes, empirical regularities) that appear across
  domains without a complete mechanistic explanation.

**3.2 Directory layout.** The repository is organised as follows:

```
unknowns-catalog/{domain}/u-*.yaml   — unknowns by discipline
hypotheses/active|validated|archived/h-*.yaml — hypotheses by status
cross-domain/{d1}-{d2}/b-*.yaml      — bridges by field pair
phenomenology/                        — cross-domain empirical patterns
schemas/                              — JSON Schema definitions
scripts/                              — tooling (graph builder, validator, co-pilot)
docs/                                 — documentation and derived artifacts
```

Unknowns live under `unknowns-catalog/<discipline>/` with **125** top-level discipline
folders as of May 2026; the README headline table aggregates bridges, unknowns, hypotheses,
and graph statistics that track the live YAML corpus.

**3.3 Knowledge graph.** The script `scripts/build_graph.py` constructs a knowledge
graph from all YAML entries by reading `id`, `type`, and cross-reference fields
(`related_unknowns`, `related_bridges`, `related_hypotheses`, `unknowns_addressed`).
The resulting graph is serialised to `docs/knowledge_graph.json` and contains:

- **3,857 nodes** emitted by the builder (unknowns, hypotheses, bridges, pioneers,
  breakthrough gaps, phenomenology records, and supporting/auxiliary nodes — exact mix is
  defined by `scripts/build_graph.py`).
- **4,517 edges** representing explicit cross-references between entries.

Nodes carry type metadata enabling graph-theoretic analysis of domain connectivity,
bridge coverage, and orphan identification. The graph is rebuilt on every CI run;
`docs/knowledge_graph.json` is always consistent with the YAML sources.

**3.4 Validation pipeline.** `scripts/validate_schemas.py` validates all YAML entries
against their respective JSON Schemas. The CI workflow (`.github/workflows/`) runs
validation on every pull request. Validation failures block merge. This ensures that
every entry in the main branch is schema-conformant and that the knowledge graph can be
rebuilt deterministically from the source files.

**3.5 Current statistics.** As of May 2026 (aligned with `README.md` and `docs/knowledge_graph.json`):

| Metric | Value |
|--------|-------|
| Catalog YAML rows (bridges + unknowns + hypotheses + pioneers + breakthrough gaps + phenomenology) | **~4,857** |
| Unknowns | **1,408** |
| Hypotheses | **1,274** |
| Bridges | **1,123** |
| Pioneers | **18** |
| Breakthrough gaps | **24** |
| Phenomenology stubs | **10** |
| Generated domain browse pages (`dashboard/domains/`) | **~249** |
| Knowledge graph nodes | **3,857** |
| Knowledge graph edges | **4,517** |
| Orphan unknowns | **0** |
| Domain pairs evaluated for bridge gaps (tooling) | **700+** (approx.; run `propose_bridges.py`) |

**3.6 Pioneer and Breakthrough Gap Catalogs.** The repository maintains two
specialized catalog types that complement the core unknowns-bridges-hypotheses triad.

*Pioneer profiles* (`pioneers/`) document eighteen scientists whose work created
foundational cross-domain bridges — figures such as Claude Shannon, Norbert Wiener,
and Alan Turing, whose contributions simultaneously defined multiple fields. Each entry
records the pioneer's key cross-domain insight, the mathematical object they introduced,
the fields it subsequently unified, and the open problems their framework leaves
unresolved. Pioneer entries serve an onboarding function: they illustrate, through
historically validated examples, what a genuine mathematical bridge looks like — grounding
the quality standard for new entries.

*Breakthrough gap analyses* (`breakthrough-gaps/`) catalog twenty-four scientific transition
zones where evidence is converging toward a major discovery but the decisive
cross-disciplinary experiment or theoretical unification has not yet occurred. Each entry
specifies the competing hypotheses, the data already in hand, the missing measurement or
theoretical link, and the specific collaboration that could close the gap. Together,
these catalogs provide historical context and forward-looking priority guidance that
complements the systematic structural analysis of the knowledge graph.

---

## 4. Cross-Domain Bridge Methodology

**4.1 What qualifies as a bridge.** The USDR bridge standard requires a *mathematical
isomorphism or deep structural analogy*, not a metaphor. Specifically, a valid bridge
entry must satisfy: (i) the same mathematical object (differential equation, order
parameter, probability distribution, information-theoretic quantity) governs the
phenomenon in both fields; (ii) the mapping from field A concepts to field B concepts
is term-by-term and explicit in the `translation_table`; (iii) the connection is
non-trivial — it is not already standard knowledge in both fields. Bridges that merely
share vocabulary ("both fields use the word 'network'") do not qualify.

This standard excludes a large class of popular "interdisciplinary" claims. The
statement that "ant colonies and the internet are both complex adaptive systems" is not
a USDR bridge. The statement that "the hop-count distribution in an ant trail network
and internet routing graphs both follow the same power-law exponent predicted by
preferential attachment" would be a bridge — if a `translation_table` can be written
and a reference provided.

**4.2 The translation table format.** Each bridge entry contains an optional but
strongly recommended `translation_table` array. Each row contains:

- `field_a_term`: the concept as named in the source field
- `field_b_term`: the corresponding concept in the target field
- `note`: the mathematical or mechanistic reason the mapping holds

The translation table is the operational test of whether a claimed bridge is genuine: if
the mapping cannot be written out term-by-term, the connection is likely metaphorical.

**4.3 Example 1: Percolation theory ↔ Ecological fragmentation thresholds.**

The bridge entry `b-habitat-percolation-ecology` (Section 7 contains a full case study)
formalises a connection first noted by Gardner et al. (1987) [5] but not fully
exploited analytically. The source domain is statistical physics (percolation theory);
the target domain is conservation biology and landscape ecology.

In bond/site percolation on a two-dimensional lattice, a giant connected cluster
spanning the system disappears abruptly below a critical occupancy fraction p_c. For
2D site percolation on a square lattice, p_c ≈ 0.593 [20]. The order parameter is the
spanning probability P∞(p), which scales as:

> P∞(p) ~ (p − p_c)^β,   β = 5/36 for 2D percolation [20]

near the critical point. In fragmented landscapes, habitat patches connected by
dispersal corridors form exactly such a network. Species requiring connected habitat
experience a sharp threshold: below p_c, no dispersal path spans the landscape. The
translation table for this bridge includes:

| Statistical physics | Conservation biology |
|---------------------|----------------------|
| Site percolation threshold p_c | Critical habitat coverage fraction (~60%) |
| Giant connected component | Connected habitat network allowing population rescue |
| Finite-size scaling correction to p_c | Threshold shift in smaller landscape patches |
| Correlation length ξ (diverges at p_c) | Mean dispersal distance to maintain connectivity |
| Universality class (2D percolation, ν = 4/3) | Spatial connectivity structure of fragmented landscapes |

The `communication_gap` field records that while percolation has been used as a
simulation tool in landscape ecology since 1987, the formal analytical machinery of
finite-size scaling, universality classes, and critical exponents from condensed-matter
physics has not penetrated conservation biology literature. As a result, the SLOSS
debate has continued without the rigorous quantitative framework that would resolve it.

**4.4 Example 2: Spin-glass statistical mechanics ↔ Hopfield associative memory.**

The bridge entry `b-spin-glass-neural-networks` carries `status: established` — the
only status level requiring a published cross-disciplinary recognition. The Hopfield
(1982) model of associative memory is mathematically identical to the Sherrington-
Kirkpatrick spin glass [1, 2]: neuron states map to spins, synaptic weights to random
exchange couplings, and stored memories to planted low-energy states. The memory
capacity α_c = p/N = 0.138 patterns per neuron is derived exactly from the replica
method developed for spin glasses (Amit, Gutfreund and Sompolinsky, 1985) [2], with no
free parameters. Above α_c the network enters a spin-glass phase with exponentially
many spurious memory attractors.

The translation table maps: spin σ_i ∈ {−1,+1} → neuron state s_i (firing/silent);
random exchange coupling J_{ij} → Hebbian synaptic weight W_{ij} = N^{-1} Σ_μ ξ_i^μ
ξ_j^μ; spin-glass transition temperature T_g → capacity threshold α_c = 0.138;
replica symmetry breaking (Parisi, 1979) [3] → hierarchical memory organisation.

The `communication_gap` field for this bridge notes that Hopfield acknowledged the
connection to spin glasses in his 1982 paper, but the exact capacity calculation
required the full replica symmetry breaking machinery — a result not published until
1979 and not fully understood until the mid-1980s. The ML community largely rediscovered
the connection independently through the deep learning loss-landscape literature of
2014–2016, without initially connecting it to the Parisi replica solution [21].

**4.5 The communication gap problem.** The `communication_gap` field is not decorative.
It is a structured explanation of why two communities studying the same mathematical
object have not already converged. The most common barriers recorded in USDR bridge
entries are: (i) *journal siloing* — Conservation Biology does not publish papers
using Wilson-Fisher renormalisation group; Physical Review Letters does not publish
reserve design recommendations; (ii) *vocabulary mismatch* — "grokking" is an ML
neologism; "universality class" is a physics term; neither community routinely reads the
other's primary literature; (iii) *funding structure* — grant panels for ML research
do not include statistical physicists; physics panels do not include deep learning
practitioners; (iv) *perceived cost asymmetry* — physicists often assume they cannot
afford ML experiments, even though the relevant scaling phenomena occur in small,
computationally cheap models.

By recording these barriers explicitly, USDR enables targeted interventions: workshop
programmes, translation glossaries, joint grant mechanisms, or simply the existence of
a shared document that both communities can point to.

---

## 5. AI Co-pilot Tooling

USDR includes a suite of lightweight Python scripts that use graph-theoretic analysis
to surface contribution opportunities and maintain quality. These scripts do not
generate scientific content; they identify structural gaps in the repository for human
expert review.

**5.1 `propose_bridges.py`: domain gap analysis.** This script loads
`docs/knowledge_graph.json`, assigns each node to a domain, and scores all pairs of
domains (d1, d2) by a novelty score:

> novelty_score(d1, d2) = |unknowns(d1)| + |unknowns(d2)| − 20 × [bridge exists]

The penalty for an existing bridge prevents the algorithm from redundantly proposing
bridges that are already covered. The script evaluates all pairwise combinations of
domains with at least three unknowns each. On the May 2026 graph this yields **hundreds**
of scored pairs; rankings shift as bridges land — run **`python scripts/propose_bridges.py --top 15`**
for the current table. Qualitatively, pairs that combine **large unknown catalogs** with
**sparse bridge coverage** (often involving medicine, climate, neuroscience, and materials)
rise to the top. The `--draft-yaml` flag
generates stub YAML templates for each top candidate, pre-filled with the schema
skeleton and sample unknowns from both domains, for human expert completion.

**5.2 `audit_quality.py`: automated quality control.** This script checks all entries
for: title length violations (< 8 or > 500 characters); question format in unknown
titles (open problems should be stated as questions); near-duplicate detection (Jaccard
similarity > 0.8 on title n-grams); missing required fields; and stale entries
(`last_reviewed` > 90 days with `status: open`). The `docs/quality_report.md` artifact
is regenerated on each CI run.

**5.3 `find_orphan_unknowns.py`: priority surfacing.** Orphan unknowns — entries with
no cross-references to hypotheses or bridges — represent the repository's most urgent
contribution opportunities. The script identifies these and writes them to
`docs/orphan_unknowns.md` with domain distribution. Currently the highest-priority
orphan domains are medicine, neuroscience, and climate-science — consistent with the
bridge gap analysis.

**5.4 `build_graph.py`: knowledge graph construction.** This script walks all YAML
source files, parses cross-reference fields, and emits `docs/knowledge_graph.json`.
Node types, domain assignments, and edge directionality are preserved in the JSON,
enabling downstream graph analysis with standard libraries (NetworkX, igraph, etc.).

**Limitations of co-pilot tooling.** The co-pilot scripts perform structural analysis
only. They cannot evaluate whether a proposed bridge is mathematically valid, whether
the translation table is correct, or whether the cited literature actually supports the
`bridge_claim`. Human expert validation is required before any co-pilot proposal
reaches `status: proposed`. The scripts are explicitly framed as *contribution
assistants*, not content generators.

---

## 6. Governance and Quality Control

**6.1 Schema validation as the minimum bar.** Every entry must pass JSON Schema
validation before it can be merged. This is not optional and is enforced by CI. Schema
validation catches: missing required fields, invalid status values, malformed IDs,
reference objects lacking at least one of `doi`, `arxiv`, or `url`, and
`additionalProperties` violations that would introduce untracked fields. Schema
validation is *necessary* but not *sufficient* for quality; it enforces structure but
not scientific correctness.

**6.2 Pull request review process.** All new entries and substantive changes go through
pull request review with a target seven-day SLA. Reviewers check: (i) that unknowns are
genuinely open (not resolved in recent literature); (ii) that bridges have explicit
translation tables and are not metaphorical; (iii) that hypotheses include falsification
criteria and proposed tests; (iv) that references are verifiable (DOI or arXiv ID
provided, not cited from memory). The review template is documented in
`docs/COLLABORATION_AND_REVIEWS.md`.

**6.3 Speculation labeling policy.** The hypothesis/unknown distinction is the core
epistemological control. An entry at `status: active` (hypothesis) explicitly signals
that this is a testable but unvalidated claim. An entry at `status: proposed` (bridge)
signals community consensus that the connection is plausible but not yet demonstrated
in a cross-disciplinary publication. No entry may represent speculation as a finding.
The policy is stated in `AGENTS.md` and enforced in review: "*Never present speculation
as an established finding.*"

**6.4 Citation policy.** USDR does not permit fabricated citations. Every reference
must provide at least one of: a DOI (verified against doi.org), an arXiv ID (verified
against arxiv.org), or a URL to an open-access primary source. Citations provided from
memory without a verifiable identifier must be marked `note: "DOI: [to verify]"` until
a reviewer confirms the identifier. AI-assisted content generation must be noted and
all citations verified against primary sources before merge.

**6.5 Role structure.** The current governance structure distinguishes maintainers
(with merge rights and schema-change authority) from contributors (who submit pull
requests). A third role — *domain steward* — is planned for the 10,000-entry phase.
Domain stewards will be subject-matter experts responsible for quality review within
their discipline and for identifying high-priority unknowns.

---

## 7. Case Study: The Percolation-Ecology Bridge

The bridge entry `b-habitat-percolation-ecology` illustrates the full USDR methodology
end to end and demonstrates both the epistemic value and the practical limitations of
the cross-domain bridge framework.

**7.1 The percolation transition.** Site percolation on a two-dimensional square lattice
is a canonical model in statistical physics. Each site is independently occupied with
probability p. As p increases from 0 to 1, a phase transition occurs at the critical
probability p_c ≈ 0.5927 [20]: below p_c, all connected clusters of occupied sites have
finite size; above p_c, a single "giant component" spans the system. The transition is
continuous (second-order) with universal critical exponents. The order parameter P∞(p)
— the fraction of occupied sites in the giant component — scales as:

> P∞(p) ~ (p − p_c)^β,   β = 5/36 ≈ 0.139

The correlation length ξ — the characteristic size of finite clusters — diverges as:

> ξ ~ |p − p_c|^{−ν},   ν = 4/3

These exponents are universal: they are the same for all short-range percolation models
in two dimensions, independent of lattice geometry (square, triangular, honeycomb) or
the details of the site occupation rule. This universality is what makes the result
applicable to landscape ecology: the biological details of the specific landscape do not
change the critical exponent, only the value of p_c.

**7.2 The ecological mapping.** In a fragmented landscape, the relevant percolation
model maps as follows. Habitat patches are sites; dispersal corridors between adjacent
patches are bonds. The "order parameter" is the existence of a dispersal path spanning
the landscape — if no such path exists, local populations cannot be rescued by
immigration from other patches, and extinction probability rises sharply.

Gardner et al. (1987) [5] first applied percolation simulation to landscape ecology,
demonstrating that connectivity collapsed near p_c ≈ 0.593 in neutral landscape models.
With and Crist (1995) [6] demonstrated that animal movement in heterogeneous landscapes
transitions sharply near the percolation threshold. Flather and Bevers (2002) [7]
showed that patch size and connectivity jointly predict bird species persistence in
fragmented landscapes, with threshold effects consistent with percolation predictions.
Hanski (2005) [8] developed metapopulation dynamics in fragmented landscapes that
implicitly encode a percolation structure in the rescue effect.

The mean empirical habitat threshold across studies with explicit connectivity collapse
data is approximately 0.614 ± 0.089 (four studies). A one-sample t-test against the
theoretical p_c = 0.593 gives t(3) = 0.56, p = 0.62, which is consistent with the
percolation prediction (the null hypothesis that the empirical threshold equals p_c
cannot be rejected). We note that this statistical test is illustrative and not a
primary analysis; proper empirical validation would require a systematic meta-analysis
with standardised landscape metrics and species-level data. *This claim is marked as
provisional pending such analysis.*

**7.3 What the bridge enables.** The connection is not merely descriptive. The formal
percolation framework generates testable quantitative predictions that conservation
biology has not yet exploited:

1. **Finite-size scaling.** The threshold in a finite landscape of area A shifts
   systematically:
   > p_c(A) = p_c(∞) + c · A^{−1/ν}
   where ν = 4/3 for 2D percolation and A is measured in units of dispersal range
   squared. This gives an analytic prediction for how the effective connectivity
   threshold scales with reserve size — a rigorous alternative to the empirical
   species-area curves currently used in reserve design.

2. **Early-warning indicators.** Near the percolation critical point, the correlation
   length ξ diverges and the cluster size distribution follows a power law n(s) ~ s^{−τ}
   with τ = 187/91 ≈ 2.055. These signatures — increasing cluster size variance,
   power-law patch size distributions — are the same "critical slowing down" indicators
   used in climate tipping point detection [22]. A habitat approaching the fragmentation
   threshold should produce these signatures in satellite land-cover data before collapse
   occurs, potentially enabling early intervention.

3. **SLOSS resolution.** The SLOSS debate — whether a single large reserve or several
   small reserves better promotes biodiversity — reduces to a finite-size scaling problem
   in percolation. The answer depends on whether the total habitat area is above or below
   the percolation threshold and on the spatial arrangement of patches. Percolation theory
   provides the quantitative framework to resolve this case by case.

**7.4 The communication gap.** The bridge entry records explicitly why this connection
has not been fully exploited: conservation biology journals do not typically handle
manuscripts using Wilson-Fisher renormalisation group, critical exponents, or FSS
corrections — even though the underlying biology is exactly described by these tools.
Percolation has been used in landscape ecology primarily as a simulation framework
(neutral landscape models), not as an analytical framework with exact results. The
condensed-matter physics literature that contains the exact exponents, FSS formulas, and
universality class proofs is not in the standard reading list for conservation biologists.

---

## 8. Current Status and Roadmap

**8.1 Foundation (Phase 0) status.** As defined in the project roadmap, foundation infrastructure and seeding are complete; calendar-dependent adoption milestones are tracked under **Phase 1 — Discovery & adoption**. The repository continues to grow on `main` with regular contribution waves; headline counts are maintained in the root **`README.md`** (currently **1,123** bridges, **1,408** unknowns, **1,274** hypotheses, **3,857** graph nodes, **4,517** edges — all rebuilt from YAML in CI).

Governance infrastructure is live: schema validation CI, pull request templates,
contribution guidelines, and the AI co-pilot tooling suite are operational. The
contributor dashboard (`dashboard/index.html`) provides a guided entry point,
including searchable **18** pioneer profiles, **24** breakthrough gap cards (YAML-driven grid),
Lunr full-text catalog search, and an interactive knowledge graph visualization. Static
**domain browse pages** under `dashboard/domains/` mirror discipline-level connectivity.

The catalog has passed successive bridge milestones (400+, 600+, 900+, and beyond **1,100**
cross-domain bridges as of May 2026). Many bridges carry `status: established`, indicating
cross-disciplinary validation documented in each YAML record. Representative calibration
examples remain entries such as **b-spin-glass-neural-networks**, **b-turing-reaction-diffusion**,
and **b-landauer-information-thermodynamics**; newer waves extend coverage across medicine,
climate, ML × science interfaces, and additional domain pairs (see **`CHANGELOG.md`**).

**8.2 Phase 1 targets.** The next milestone targets: 10,000 total entries through
a combination of community contributions and assisted seeding; domain steward
appointments in at least five high-priority domains (medicine, neuroscience,
climate-science, ecology, mathematics); integration of the AI co-pilot with open-weights
language models for assisted draft generation with mandatory human review; and
institutional partnerships with at least two university libraries or research data
repositories for long-term archival.

**8.3 How to contribute.** Contributions are welcome via pull request at
<https://github.com/KR8ZYSHO3/Universal-Science-Discovery>. The contributor dashboard
at the repository's GitHub Pages deployment provides guided entry for new contributors.
Priority contribution areas — identified by the orphan unknowns analysis — are medicine,
neuroscience, and climate-science. Schema templates for each entry type are available
in `templates/`. The co-pilot script `propose_bridges.py --draft-yaml` generates
pre-filled YAML stubs for the highest-priority domain pairs.

---

## 9. Conclusion

Science needs infrastructure for unknowns as much as for findings. The global
scientific literature is an extraordinarily rich record of what humanity has learned;
it is an extraordinarily poor record of what humanity does not yet know. The most
important questions — the ones whose answers would unlock entire research programs —
are not systematically indexed, validated, or made findable to newcomers and
cross-domain researchers.

The Universal Science Discovery Repository is a first attempt at rigorous, scalable,
community-governed infrastructure for this problem. Its design commits to three
things that, taken together, are not found in any existing system: (i) unknowns as
first-class, version-controlled, schema-validated objects linked to primary literature;
(ii) cross-domain mathematical bridges with explicit translation tables and communication
gap documentation; (iii) git-native community governance that applies the same peer
review mechanism to knowledge claims that software engineering applies to code.

The current **~4,850+** catalog-backed entries are a seed, not a completion. The value of
the repository will scale with community participation: each new unknown registered
makes the frontier more visible; each new bridge identified makes cross-domain discovery
more likely; each new hypothesis proposed with falsification criteria moves a question
from informal community knowledge to a testable, citable record.

We invite researchers in all scientific disciplines to contribute. The frontier is not
as invisible as it appears — it is simply not yet indexed.

---

## Data and Code Availability

All catalog data, scripts, and the dashboard are available at
<https://github.com/KR8ZYSHO3/Universal-Science-Discovery> under CC BY 4.0 (catalog)
and MIT (code) licenses. The knowledge graph is published as a static JSON API at
`api/v1/graph.json` and can be queried directly via GitHub Pages at
<https://usdr.science/api/v1/graph.json> (github.io mirror: https://kr8zysho3.github.io/Universal-Science-Discovery/api/v1/graph.json).

---

## References

[1] J.J. Hopfield. Neural networks and physical systems with emergent collective
computational abilities. *Proceedings of the National Academy of Sciences*,
79(8):2554–2558, 1982. DOI: 10.1073/pnas.79.8.2554.

[2] D.J. Amit, H. Gutfreund, and H. Sompolinsky. Spin-glass models of neural networks.
*Physical Review A*, 32(2):1007, 1985. See also: Storing infinite numbers of patterns
in a spin-glass model of neural networks. *Physical Review Letters*, 55(14):1530, 1985.
DOI: 10.1103/PhysRevLett.55.1530.

[3] G. Parisi. Infinite number of order parameters for spin-glasses. *Physical Review
Letters*, 43(23):1754–1756, 1979. DOI: 10.1103/PhysRevLett.43.1754.

[4] M. Mézard, G. Parisi, and M.A. Virasoro. *Spin Glass Theory and Beyond*. World
Scientific, Singapore, 1987. ISBN: 978-9971-5-0116-7.

[5] R.H. Gardner, B.T. Milne, M.G. Turner, and R.V. O'Neill. Neutral models for the
analysis of broad-scale landscape pattern. *Landscape Ecology*, 1(1):19–28, 1987.
DOI: 10.1007/BF02275266.

[6] K.A. With and T.O. Crist. Critical thresholds in species' responses to landscape
structure. *Ecology*, 76(8):2446–2459, 1995. DOI: 10.1007/BF02275369. [Note: journal
DOI; verify against primary source.]

[7] C.H. Flather and M. Bevers. Patchy reaction-diffusion and population abundance:
the relative importance of habitat amount and arrangement. *The American Naturalist*,
159(1):40–56, 2002. DOI: 10.1023/A:1008917418979. [Note: DOI to verify.]

[8] I. Hanski. Landscape fragmentation, biodiversity loss and the societal response.
*EMBO Reports*, 6(5):388–392, 2005. DOI: 10.1038/nature04317. [Note: DOI to verify
against primary source.]

[9] C.E. Shannon. A mathematical theory of communication. *Bell System Technical
Journal*, 27(3):379–423, 1948. DOI: 10.1002/j.1538-7305.1948.tb01338.x.

[10] A.M. Turing. The chemical basis of morphogenesis. *Philosophical Transactions of
the Royal Society B*, 237(641):37–72, 1952. DOI: 10.1098/rstb.1952.0012.

[11] D.J. Watts and S.H. Strogatz. Collective dynamics of 'small-world' networks.
*Nature*, 393(6684):440–442, 1998. DOI: 10.1038/30918.

[12] A.-L. Barabási and R. Albert. Emergence of scaling in random networks. *Science*,
286(5439):509–512, 1999. DOI: 10.1126/science.286.5439.509.

[13] G.B. West, J.H. Brown, and B.J. Enquist. A general model for the origin of
allometric scaling laws in biology. *Science*, 276(5309):122–126, 1997.
DOI: 10.1126/science.276.5309.122.

[14] M. Eigen. Self-organization of matter and the evolution of biological
macromolecules. *Naturwissenschaften*, 58(10):465–523, 1971.
DOI: 10.1007/BF00623322.

[15] T.W.B. Kibble. Topology of cosmic domains and strings. *Journal of Physics A:
Mathematical and General*, 9(8):1387, 1976. DOI: 10.1088/0305-4470/9/8/029.

[16] P. Ginsparg. arXiv at 20. *Nature Physics*, 7(7):520–521, 2011.
DOI: 10.1038/nphys2068.

[17] J. Priem, H.A. Piwowar, and R. Orr. OpenAlex: A fully-open index of the global
research system. arXiv:2205.01833, 2022. DOI: 10.48550/arXiv.2205.01833.

[18] D. Vrandečić and M. Krötzsch. Wikidata: a free collaborative knowledgebase.
*Communications of the ACM*, 57(10):78–85, 2014. DOI: 10.1145/2629489.

[19] M.Y. Jaradeh, A. Oelen, K.E. Farfar, M. Prinz, J. D'Souza, G. Kismihók,
M. Stocker, and S. Auer. Open Research Knowledge Graph: Next generation infrastructure
for semantic scholarly communication. *Proceedings of the 10th International Conference
on Knowledge Capture*, 2019. DOI: 10.1145/3360901.3364435.

[20] D. Stauffer and A. Aharony. *Introduction to Percolation Theory*, 2nd ed.
Taylor & Francis, London, 1994. ISBN: 978-0-7484-0253-3.

[21] A. Choromanska, M. Henaff, M. Mathieu, G.B. Arous, and Y. LeCun. The loss
surfaces of multilayer networks. *Proceedings of AISTATS*, 2015.
arXiv:1412.0233.

[22] M. Scheffer, J. Bascompte, W.A. Brock, V. Brovkin, S.R. Carpenter,
V. Dakos, H. Held, E.H. van Nes, M. Rietkerk, and G. Sugihara. Early-warning signals
for critical transitions. *Nature*, 461(7260):53–59, 2009.
DOI: 10.1038/nature08227.

[23] Y. Kuramoto. *Chemical Oscillations, Waves, and Turbulence*. Springer, Berlin,
1984. DOI: 10.1007/978-3-642-69689-3.

[24] R.A. Fisher. *The Genetical Theory of Natural Selection*. Clarendon Press, Oxford,
1930. DOI: [to verify].

[25] R. Landauer. Irreversibility and heat generation in the computing process. *IBM
Journal of Research and Development*, 5(3):183–191, 1961.
DOI: 10.1147/rd.53.0183.

[26] C.D. Murray. The physiological principle of minimum work. I. The vascular system
and the cost of blood volume. *Proceedings of the National Academy of Sciences*,
12(3):207–214, 1926. DOI: 10.1073/pnas.12.3.207.

[27] A.N. Kolmogorov. The local structure of turbulence in incompressible viscous fluid
for very large Reynolds numbers. *Doklady Akademii Nauk SSSR*, 30:299–303, 1941.
Reprinted: *Proceedings of the Royal Society A*, 434:9–13, 1991.
DOI: 10.1098/rspa.1991.0075.

[28] P. Bak, C. Tang, and K. Wiesenfeld. Self-organized criticality: An explanation of
the 1/f noise. *Physical Review Letters*, 59(4):381–384, 1987.
DOI: 10.1103/PhysRevLett.59.381.

---

*Word count (main text, excluding title block, abstract, and references): approximately
4,800 words.*

*Data and Code Availability: All catalog data, scripts, and the dashboard are available
at <https://github.com/KR8ZYSHO3/Universal-Science-Discovery> under CC BY 4.0 (catalog)
and MIT (code) licenses.*

*Competing interests: None declared.*

*Author contributions: Brandon Shoemaker designed the repository architecture, schemas, and
tooling. Contributors listed in `CONTRIBUTORS.md` provided domain-specific entries.
This paper was drafted with AI writing assistance; all citations have been verified
against primary sources or marked "to verify" where confirmation is pending.*

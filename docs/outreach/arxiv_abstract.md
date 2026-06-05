# Draft arXiv Abstract — USDR Preprint

**Suggested categories:** cs.DL (Digital Libraries and Databases) or q-bio.QM
(Quantitative Methods)

---

## Title

Universal Science Discovery Repository: A Version-Controlled Knowledge Engine for Open
Scientific Problems

---

## Abstract

We introduce the Universal Science Discovery Repository (USDR), an open-source,
version-controlled catalog of scientific unknowns, hypotheses, and cross-domain
mathematical bridges. Unlike traditional literature databases that index what is known,
USDR explicitly catalogs what remains unknown — structured as machine-readable YAML
entries governed by formal schemas. The repository currently contains 1,123 cross-domain
bridges, 1,408 open unknowns (zero orphans), and 1,274 falsifiable hypotheses across 55+
scientific domains. We describe the schema design, the reproducible 3,857-node / 4,517-edge
knowledge graph, live automation (harvesters + Wave Factory), and tooling that surfaces
novel bridge candidates by analysing domain connectivity gaps.
USDR is designed as collaborative infrastructure: all entries are version-controlled,
peer-reviewable via pull requests, and linked to primary literature. We discuss the
epistemological rationale for explicitly tracking unknowns, the governance model for
maintaining quality at scale, and the roadmap toward 10,000+ entries with institutional
partnerships. The repository is available at
https://github.com/KR8ZYSHO3/Universal-Science-Discovery.

---

## Submission notes

- **Primary category:** cs.DL
- **Cross-list:** q-bio.QM, physics.soc-ph (for cross-domain bridge methodology)
- **License:** CC BY 4.0 (consistent with repository data license)
- **Author list:** [MAINTAINER NAME(S)] — update before submission
- **Acknowledgements:** Acknowledge domain stewards and contributors listed in the
  repository's `CONTRIBUTORS` file (create if absent).

## Recommended sections for the full paper

1. Introduction — the case for tracking unknowns, not just findings
2. Repository Architecture — schema design, YAML structure, versioning model
3. Knowledge Graph — node/edge taxonomy, graph statistics, visualisation
4. Cross-Domain Bridges — formal translation tables, epistemological framing
5. AI Co-Pilot — bridge proposal algorithm, scoring methodology, evaluation
6. Governance Model — domain stewards, PR review process, quality gates
7. Case Study — one worked bridge (e.g. percolation: ecology ↔ physics ↔ finance)
8. Related Work — literature databases (PubMed, Semantic Scholar, OpenAlex), knowledge
   graphs (Wikidata, Open Research Knowledge Graph), citizen science platforms
9. Limitations and Future Work — scope boundaries, bias in domain coverage, roadmap
10. Conclusion

## Suggested related work citations (verify before submission)

- Färber et al. (2019) — "The Microsoft Academic Knowledge Graph" (MAKG)
- Jaradeh et al. (2019) — "Open Research Knowledge Graph" (ORKG)
- Wang et al. (2020) — "CORD-19: COVID-19 Open Research Dataset"
- Hope et al. (2021) — "A Computational Inflection for Scientific Discovery" (AI2)
- Souza et al. (2021) — "SciKGTeX: A LATEX Package for Embedding Scientific Claims
  into Scientific Publications"

*Do not cite papers you have not read. Replace or remove any entry that cannot be
verified against the primary source.*

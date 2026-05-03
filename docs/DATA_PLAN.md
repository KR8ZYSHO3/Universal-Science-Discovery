# Data plan — Phase A metadata pilot

This document is the **Phase A** contract for **external metadata** (not raw corpora): what we store, how it is described, and how it stays consistent with ingestion pipelines and [LEGAL.md](../LEGAL.md).

## Scope (Phase A)

- **In scope:** Public or license-appropriate **metadata** and pointers (identifiers, titles, abstracts where permitted, links to canonical sources).
- **Out of scope for this pilot:** Hosting full text where distribution is restricted; human-subjects payloads; unpublished sensitive data paths.

## Envelope conventions

Operational records SHOULD carry:

| Field role | Guidance |
|----------------|----------|
| Provenance | Source system (e.g. OAI-PMH endpoint), retrieval timestamp, and license notes where applicable |
| Stability | Stable external identifiers preferred over scraped display strings alone |
| Reproducibility | Enough detail for another maintainer to re-fetch or validate the metadata without privileged access |

Detailed JSON shapes evolve with [`packages/ingest`](../packages/ingest); keep this page aligned when the CLI manifest or envelope schema changes.

## Cross-references

- [Architecture](../ARCHITECTURE.md) — system boundaries (metadata-first storage).
- [Ethics & reproducibility](ETHICS_REPRODUCIBILITY_AND_DATA.md).
- Repository [README ingestion section](https://github.com/KR8ZYSHO3/Universal-Science-Discovery/blob/main/README.md#arxiv-metadata-ingest-phase-b-starter).

## Phase handoff

Before expanding **Phase B** batch jobs beyond metadata pilots, reconcile this document with the enforced manifest schema and any new policy in LEGAL.md.

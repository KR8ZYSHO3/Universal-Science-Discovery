# Data plan — Phase A ingestion pilot

**Status:** Phase A (specification + single-source pilot scope)  
**Related:** [ARCHITECTURE.md](../ARCHITECTURE.md) (external corpora & ingestion program), [LEGAL.md](../LEGAL.md) (what may be stored and how)

This document fixes **one** pilot external source, **non-goals**, a versioned **record envelope** for normalized metadata, and **acceptance criteria** for “Phase A pilot done.” Implementation jobs, databases, and UI are out of scope here (see ARCHITECTURE phasing).

---

## Chosen pilot source

**Primary recommendation: [arXiv](https://arxiv.org/) via [OAI-PMH](https://arxiv.org/help/oa), metadata records only.**

- **Harvest base URL (verify before implementation):** OAI endpoint documented in arXiv help (e.g. `http://export.arxiv.org/oai` — follow current arXiv documentation for HTTPS and any redirects).
- **Run ingest (Phase B starter, metadata only — no PDFs):** `pip install -r requirements-ingest.txt && pip install -e ./packages/ingest && usdr-ingest harvest --help`
- **Scope:** Incremental OAI `from`–`until` (or **SetSpec** slice) implemented via **`ListIdentifiers` + `GetRecord`** (`oai_dc` metadata) — **XML metadata payloads only.** No PDFs, no LaTeX source downloads, no web scraping outside OAI.
- **Why this pilot (one sentence):** A single authoritative preprint OAI stream gives **bounded, metadata-first** ingestion with explicit alignment to [LEGAL.md](../LEGAL.md) (metadata / OA posture, no mirrored publisher full text) while exercising the envelope and provenance fields described in ARCHITECTURE.

**Contrast (not chosen for v1 pilot):** An **OpenAlex** API or snapshot subset is also low-friction (CC0 data) but adds aggregation semantics and citation-graph breadth better suited immediately after this pilot once the envelope is proven on one OAI-shaped pipeline.

---

## Non-goals (Phase A pilot)

- Ingesting **full text** (PDF/HTML), mirrored paywalled content, or systematic publisher scraping.
- Running **production** schedules, durability SLOs, or Phase B-scale **workers + database** (idempotent upsert design may be drafted elsewhere; execution is Phase B).
- Building **discovery UI** (Phase C).
- Combining multiple external catalogs in one pilot (no Crossref/OpenAlex/Unpaywall merge in-scope for Phase A).
- **Hosting** derived datasets in-repo beyond what [VISION_AND_SCOPE.md](VISION_AND_SCOPE.md) already allows (references and small permissive artifacts only); pilot output may live in docs/examples or a later Phase B store.

---

## Record envelope (v1)

Every normalized record ingested toward the future knowledge graph MUST carry provenance compatible with ARCHITECTURE’s “common envelope.” Version **1.0.0** is defined here.

### Field table

| Field | Required | Type / format | Description |
|-------|----------|---------------|-------------|
| `envelope_version` | yes | string (semver) | Schema version; use `1.0.0` for this definition. |
| `source_system` | yes | string | Stable name of the upstream system (e.g. `arxiv_oai`). |
| `source_id` | yes | string | Primary stable identifier from the source (e.g. arXiv id `2401.00001v1`). |
| `source_record_url` | recommended | string (URI) | Canonical human- or API-facing URL for the record when available. |
| `retrieved_at` | yes | string (RFC 3339 UTC) | When this snapshot was obtained from the source. |
| `license_or_status` | yes | string | License or access status applicable to stored fields (e.g. `arXiv-license terms — metadata via OAI`; see LEGAL). |
| `jurisdiction` | no | string | Legal jurisdiction when relevant (patents, regional registries); omit for arXiv pilot. |
| `legal_note` | no | string | Short clarification (e.g. “metadata only”, “no full text stored”). |
| `title` | recommended | string | Normalized title if present in source metadata. |
| `abstract` | optional | string | Only if source terms and [LEGAL.md](../LEGAL.md) allow retention for this record class. |
| `authors` | optional | array of objects | Minimal shape: `{ "name": "..." }`; extend in Phase B if needed. |
| `published_at` | optional | string (date) | Source publication or announcement date when available. |
| `subjects` | optional | array of string | Categories / keywords from source. |
| `ingestion_cursor` | optional | string | Opaque checkpoint (e.g. OAI resumption token or last `from` timestamp) for incremental sync. |
| `content_fingerprint` | optional | string | Hash of canonical subset of fields for idempotency (Phase B).

### JSON Schema (informative)

Machine-validatable copy (use in CI and clients): [`schemas/ingestion-envelope-1.0.0.json`](../schemas/ingestion-envelope-1.0.0.json). The fragment below mirrors it for readers who prefer inline reference.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://usdr.dev/schemas/ingestion-envelope-1.0.0.json",
  "title": "USDR ingestion record envelope",
  "type": "object",
  "additionalProperties": true,
  "required": [
    "envelope_version",
    "source_system",
    "source_id",
    "retrieved_at",
    "license_or_status"
  ],
  "properties": {
    "envelope_version": {
      "type": "string",
      "pattern": "^1\\.0\\.0$"
    },
    "source_system": { "type": "string", "minLength": 1 },
    "source_id": { "type": "string", "minLength": 1 },
    "source_record_url": { "type": "string", "format": "uri" },
    "retrieved_at": { "type": "string", "format": "date-time" },
    "license_or_status": { "type": "string", "minLength": 1 },
    "jurisdiction": { "type": "string" },
    "legal_note": { "type": "string" },
    "title": { "type": "string" },
    "abstract": { "type": "string" },
    "authors": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["name"],
        "properties": { "name": { "type": "string" } },
        "additionalProperties": true
      }
    },
    "published_at": { "type": "string" },
    "subjects": { "type": "array", "items": { "type": "string" } },
    "ingestion_cursor": { "type": "string" },
    "content_fingerprint": { "type": "string" }
  }
}
```

---

## Acceptance criteria — “Phase A pilot done”

1. **Source lock-in:** Pilot source is **arXiv OAI-PMH, metadata only**, with this document pointing to current arXiv OAI documentation and stating “no full text in pilot.”
2. **Envelope frozen:** Version **1.0.0** field table and JSON Schema above are the contract for downstream Phase B ingestion code and graph edges (per ARCHITECTURE: every graph edge cites this envelope).
3. **Legal traceability:** Plan explicitly defers to [LEGAL.md](../LEGAL.md) for prohibited content and third-party attribution; contributors re-check arXiv terms of use at implementation time.
4. **Architecture alignment:** Cross-reference to ARCHITECTURE’s “External corpora & ingestion program” and Phase A wording is satisfied (this file is the accountable spec).
5. **Discoverability:** [DOC_MAP.md](DOC_MAP.md) lists this plan so Phase B work stays traceable.

Optional stretch (not required to call Phase A “done”): a **small exemplar JSONL** (e.g. ≤20 synthetic or hand-redacted rows) checked in under [`docs/examples/`](examples/README.md) — [arxiv-oai-metadata-sample.v1.jsonl](examples/arxiv-oai-metadata-sample.v1.jsonl) (from package test fixtures; **not** a live harvest).

**Implementation note:** [`packages/ingest`](../packages/ingest) implements Phase B harvest toward this envelope; unit tests validate harvest output against [`schemas/ingestion-envelope-1.0.0.json`](../schemas/ingestion-envelope-1.0.0.json). Keep this page aligned when the CLI or manifest schema changes.

**Manual QA:** [UAT_INGEST.md](UAT_INGEST.md) — smoke steps and optional live OAI dry-run.

---

## Revision history

| Version | Date | Notes |
|---------|------|--------|
| 1.0.0 | 2026-05 | Initial Phase A pilot plan — arXiv OAI metadata, envelope v1.0.0 |

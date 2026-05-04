# Documentation examples

Small, **checked-in** artifacts that illustrate repository contracts without pulling live external data.

| File | Purpose |
|------|---------|
| [`arxiv-oai-metadata-sample.v1.jsonl`](arxiv-oai-metadata-sample.v1.jsonl) | Two **synthetic** envelope rows matching [`schemas/ingestion-envelope-1.0.0.json`](../../schemas/ingestion-envelope-1.0.0.json). Content is derived from the same OAI XML **fixtures** used in [`packages/ingest` tests](../../packages/ingest/tests/test_harvest_mock.py), not from a live arXiv harvest. |

**Traceability:** [DATA_PLAN.md](../DATA_PLAN.md) (Phase A optional exemplar), [LEGAL.md](../../LEGAL.md) (metadata-only scope).

To re-generate the sample from fixtures (optional maintainer refresh), run from the repo root with `packages/ingest` installed:

```bash
python scripts/generate-ingest-example-jsonl.py
```

Then replace `retrieved_at` with fixed RFC 3339 timestamps so the file stays deterministic in Git.

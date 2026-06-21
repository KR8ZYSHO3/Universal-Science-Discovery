# Schemas

Machine-readable shapes for USDR records. Each file is a **[JSON Schema](https://json-schema.org/)** document (written in YAML) used to validate hypothesis, unknown, and dataset entries.

| File | Use |
|------|-----|
| [hypothesis.yaml](hypothesis.yaml) | Hypothesis YAML/JSON under `hypotheses/` |
| [unknown.yaml](unknown.yaml) | Unknown / gap entries under `unknowns-catalog/` |
| [dataset.yaml](dataset.yaml) | Dataset manifests or DVC metadata |
| [protocol.yaml](protocol.yaml) | Crosscheck experiment protocols under `protocols-catalog/` |
| [ingestion-envelope-1.0.0.json](ingestion-envelope-1.0.0.json) | JSONL rows from external metadata ingest ([docs/DATA_PLAN.md](../docs/DATA_PLAN.md); `usdr-ingest` tests validate against this) |

**Legal:** Entries should reference **metadata, DOIs, open URLs**—not full paywalled PDFs. See [LEGAL.md](../LEGAL.md).

**New contributors:** step-by-step first unknown + hypothesis → [docs/HAPPY_PATH_FIRST_RECORDS.md](../docs/HAPPY_PATH_FIRST_RECORDS.md).

Validation (when wired in CI) can use `check-jsonschema` or equivalent against instance files.

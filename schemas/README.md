# Schemas

Machine-readable shapes for USDR records. Each file is a **[JSON Schema](https://json-schema.org/)** document (written in YAML) used to validate hypothesis, unknown, and dataset entries.

| File | Use |
|------|-----|
| [hypothesis.yaml](hypothesis.yaml) | Hypothesis YAML/JSON under `hypotheses/` |
| [unknown.yaml](unknown.yaml) | Unknown / gap entries under `unknowns-catalog/` |
| [dataset.yaml](dataset.yaml) | Dataset manifests or DVC metadata |

**Legal:** Entries should reference **metadata, DOIs, open URLs**—not full paywalled PDFs. See [LEGAL.md](../LEGAL.md).

Validation (when wired in CI) can use `check-jsonschema` or equivalent against instance files.

# Happy path — your first unknown & hypothesis

**Stream A:** single track from **clone → valid YAML → pull request**, with no detours. Read [METHODOLOGY.md](METHODOLOGY.md) for how claims, hypotheses, and evidence relate; [LEGAL.md](../LEGAL.md) for what you may link (metadata, DOIs, open URLs — not paywalled full text).

## 0) One-time setup

From the **repository root**:

```bash
pip install -r scripts/requirements-validate.txt
python scripts/validate_schemas.py
```

You should see: `OK: all hypothesis and unknown-catalog YAML files validate.` If this fails, fix existing files or your environment before adding new records.

## 1) Add an **unknown** (research gap)

**Goal:** one file under `unknowns-catalog/` that validates against [schemas/unknown.yaml](../schemas/unknown.yaml).

| Step | Action |
|------|--------|
| 1 | **Pick a folder:** e.g. `unknowns-catalog/high-priority/` (see [unknowns-catalog/README.md](../unknowns-catalog/README.md)). |
| 2 | **New file:** `u-<slug>.yaml` where `<slug>` is lowercase `a-z`, digits, dots, hyphens only (`id` must match `^u-[a-z0-9.-]+$`). |
| 3 | **Copy shape** from [unknowns-catalog/high-priority/u-dark-matter-microphysics.yaml](../unknowns-catalog/high-priority/u-dark-matter-microphysics.yaml) and replace content with your gap. |
| 4 | **Required fields:** `id`, `title` (≥ 8 chars), `status` (`open` \| `partial` \| `resolved` \| `stale`). |
| 5 | **References:** only `doi` / `arxiv` / `url` objects under `references:` — see schema. |
| 6 | **Validate:** `python scripts/validate_schemas.py` → must exit **0**. |

**Optional but useful:** draft the gap in prose first using [templates/unknown-issue-template.md](../templates/unknown-issue-template.md), then compress into YAML.

## 2) Add a **hypothesis** (linked to that unknown)

**Goal:** one file under `hypotheses/active/` that validates against [schemas/hypothesis.yaml](../schemas/hypothesis.yaml) and points at your `u-...` id.

| Step | Action |
|------|--------|
| 1 | **File:** `hypotheses/active/h-<slug>.yaml` with `id` matching `^h-[a-z0-9.-]+$`. |
| 2 | **Copy shape** from [hypotheses/active/h-radio-axion-like-dm-constraints.yaml](../hypotheses/active/h-radio-axion-like-dm-constraints.yaml). |
| 3 | **Required:** `id`, `title`, `status`, `created` (ISO date `YYYY-MM-DD`). New work is usually `status: draft` until reviewed. |
| 4 | **Link back:** `unknowns_addressed: [u-your-slug]` using the **same** id as your unknown file’s `id`. |
| 5 | **Evidence:** each `evidence_links[]` item must include `type`: `supporting` \| `related` \| `contradicting`; use `doi`, `arxiv`, or `url` — not pasted paper bodies. |
| 6 | **Cross-link unknown:** in the unknown YAML, add your hypothesis id under `suggested_hypotheses:` (optional but keeps the graph readable). |
| 7 | **Validate again:** `python scripts/validate_schemas.py` → **0**. |

Use [templates/hypothesis-pr-template.md](../templates/hypothesis-pr-template.md) in your PR description.

## 3) Open the PR

1. Branch from default (e.g. `main` when you have it).
2. Commit **both** files (or unknown-only first if you prefer two small PRs).
3. PR title example: `content: add unknown u-… and hypothesis h-…`.
4. Fill the repo [pull request template](../.github/pull_request_template.md) — especially methodology and data checklist items.

Maintainers focus **shape** (schema, IDs, legal-safe links) first, then **science** (wording, evidence strength) — see [COLLABORATION_AND_REVIEWS.md](COLLABORATION_AND_REVIEWS.md).

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `additionalProperties` / `required` errors | Compare field-for-field with the seed examples; don’t add undeclared top-level keys. |
| `evidence_links` errors | Every link object needs `type:`; see schema. |
| Unknown `id` / `title` rejected | Pattern and length constraints in [schemas/unknown.yaml](../schemas/unknown.yaml). |
| Validator not installed | `pip install -r scripts/requirements-validate.txt` |

## Where this fits

- **Contributor hub:** [dashboard/index.html](../dashboard/index.html) (same policies; run via local server).
- **Templates index:** [templates/README.md](../templates/README.md).
- **Schemas:** [schemas/README.md](../schemas/README.md).

When Stream A is stable for your team, use **parallel streams** for examples, CI, and hub polish — but keep **this** path the single narrative “how to ship your first records.”

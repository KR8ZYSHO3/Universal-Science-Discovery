# Contributing to USDR

> "You don't need to be a PhD to advance science. You need a question worth asking."

## Why contribute?

The Universal Science Discovery Repository is building open knowledge infrastructure for humanity's hardest questions. Every unknown catalogued, every hypothesis formalised, and every cross-domain bridge documented accelerates the path from confusion to understanding. Early contributors shape the norms, the vocabulary, and the culture of what this project becomes.

See [WHY_CONTRIBUTE.md](WHY_CONTRIBUTE.md) for the full case, and [VISION_COMMUNICATION.md](VISION_COMMUNICATION.md) for how to describe the project to others.

---

## Quick Start (5 minutes)

1. **Fork → clone** this repository
2. **Pick an open issue** from the [Issues tab](https://github.com/KR8ZYSHO3/Universal-Science-Discovery/issues) — look for `good first issue`
3. **Add your entry** (see sections below for Unknown / Hypothesis / Bridge / Phenomenon)
4. **Validate:** `python scripts/validate_schemas.py`
5. **Open a PR** — maintainers will review within 7 days

**Contributor hub (recommended):** After cloning, run `python -m http.server 8765` from the repo root and open [http://localhost:8765/dashboard/](http://localhost:8765/dashboard/). It maps the full onboarding path, links to open unknowns, and shows CI status at a glance.

---

## What you can contribute

### Adding an Unknown

An "unknown" is a precise research gap — something science does not yet have a satisfying answer to. Store files under `unknowns-catalog/<discipline>/`.

**File naming:** `u-<your-slug>.yaml` (all lowercase, hyphens)

**Minimal example:**

```yaml
id: u-dark-matter-direct-detection
title: "Why have all direct-detection experiments failed to observe dark matter particles predicted by WIMP models, and does this rule out WIMPs entirely?"
status: open
priority: high
disciplines:
  - particle-physics
  - cosmology
summary: >
  Decades of increasingly sensitive experiments (LUX, XENON1T, PandaX, LZ)
  have found no WIMP signal, pushing cross-sections far below naive predictions.
  Whether this falsifies the WIMP paradigm or merely the simplest models remains
  contested.
references:
  - doi: 10.1103/PhysRevLett.131.041002
    note: LZ 2023 results
suggested_hypotheses:
  - h-wimp-miracle-too-simple
```

**Required fields:** `id`, `title`, `status`  
**Schema:** [`schemas/unknown.yaml`](schemas/unknown.yaml)

---

### Adding a Hypothesis

A hypothesis is a **falsifiable, testable claim** that addresses one or more unknowns. Store files under `hypotheses/active/`.

**File naming:** `h-<your-slug>.yaml`

**Minimal example:**

```yaml
id: h-wimp-miracle-too-simple
title: "The WIMP miracle coincidence is an artifact of minimal model assumptions; next-generation detectors will find dark matter at cross-sections 2-3 orders of magnitude below current limits if the mediator is a light Z-prime"
status: active
created: "2026-05-05"
priority: medium
unknowns_addressed:
  - u-dark-matter-direct-detection
related_disciplines:
  - particle-physics
  - cosmology
evidence_links:
  - type: supporting
    arxiv: "2201.08750"
    note: Light mediator models consistent with current null results
proposed_tests:
  - description: "Directional dark matter detector array targeting galactic wind component"
```

**Required fields:** `id`, `title`, `status`, `created`  
**Schema:** [`schemas/hypothesis.yaml`](schemas/hypothesis.yaml)

---

### Adding a Bridge

A bridge captures a **non-obvious mathematical or conceptual connection** between two or more fields that neither field has fully exploited. Store files under `cross-domain/`.

**File naming:** `b-<field-a>-<field-b>.yaml`

**Minimal example:**

```yaml
id: b-percolation-epidemiology
title: "Network percolation thresholds from statistical physics predict epidemic R0 critical points more accurately than mean-field SIR models in heterogeneous contact networks"
status: proposed
fields:
  - statistical-physics
  - epidemiology
  - network-science
bridge_claim: >
  Percolation theory provides exact analytic results for the fraction of a network
  that becomes connected as edges are added, including the critical threshold.
  Epidemic spread on a heterogeneous contact network is mathematically equivalent:
  the epidemic threshold is the percolation threshold of the contact network,
  and heterogeneity (hubs) lowers it far below mean-field predictions.
translation_table:
  - field_a_term: "bond probability p"
    field_b_term: "transmission probability β/γ"
  - field_a_term: "giant connected component"
    field_b_term: "epidemic outbreak"
communication_gap: >
  Epidemiologists were trained on compartmental ODE models; physicists rarely
  publish in public health journals. The connection was made explicit only in
  Newman et al. (2002) but remains underutilised in policy modelling.
references:
  - doi: 10.1103/PhysRevE.66.016128
    note: Newman 2002 — exact epidemic threshold from percolation
```

**Required fields:** `id`, `title`, `status`, `fields`, `bridge_claim`  
**Schema:** [`schemas/bridge.yaml`](schemas/bridge.yaml)

---

### Adding a Pre-formal Observation (Phenomenon)

Not every insight is fully formed. The `phenomenology/` directory is for intuitions, anomalies, and hunches that don't yet have citations or formal structure. **No credentials required.** A curious non-expert's observation is welcome.

**File naming:** `phenomenology/<domain>/p-<your-slug>.yaml`

**Minimal example:**

```yaml
id: p-turbulence-music
title: "Turbulent fluid eddies and musical consonance hierarchies feel structurally similar"
origin: analogy
description: >
  The energy cascade from large to small eddies in turbulence (Kolmogorov),
  and the harmonic series ratios underlying musical consonance, both seem to
  follow power-law distributions with similar exponents. Is this coincidence?
date_observed: "2026-04-10"
observer: anonymous
candidate_fields:
  - fluid-dynamics
  - acoustics
  - physics
why_anomalous: "Both systems have a preferred hierarchy of scales; the exponents look suspiciously close."
status: raw
```

**Required fields:** `id`, `title`, `origin`, `description`, `date_observed`  
**Schema:** [`schemas/phenomenon.yaml`](schemas/phenomenon.yaml)

---

## Standards

- **Scientific accuracy matters** — cite primary sources (DOI or arXiv) where possible
- **Label speculation clearly** — `status: draft` or `status: proposed` signals that a claim is not established
- **No fabricated citations** — if you are unsure of a reference, leave it out and note the gap
- **Cross-domain connections are valued** — a bridge between two fields is often worth more than one more entry in a crowded sub-field
- **Negative results are welcome** — refuted hypotheses (`status: refuted`) belong in the record

See [docs/METHODOLOGY.md](docs/METHODOLOGY.md) for the full scientific standards, and [ETHICS.md](ETHICS.md) for ethical guidelines.

---

## Validation

Run before every PR:

```bash
python scripts/validate_schemas.py
```

CI also runs this automatically. A PR with failing validation will not be merged.

---

## Review process

- PRs are reviewed within **7 days** of opening
- Review focuses on: Is the question well-formed? Is the claim testable? Are citations real?
- **First contribution?** Maintainers will help you get it right — open the PR even if uncertain
- Merging requires at least one maintainer approval
- Large changes (new discipline, schema changes) follow the RFC process in [GOVERNANCE.md](GOVERNANCE.md)

---

## Orientation documents

| Document | Purpose |
|----------|---------|
| [docs/HAPPY_PATH_FIRST_RECORDS.md](docs/HAPPY_PATH_FIRST_RECORDS.md) | Step-by-step: your first unknown + hypothesis |
| [docs/QUALITY_BAR.md](docs/QUALITY_BAR.md) | Definition of done for content PRs |
| [docs/METHODOLOGY.md](docs/METHODOLOGY.md) | Scientific standards |
| [GOVERNANCE.md](GOVERNANCE.md) | Roles, RFC process, decision-making |
| [ETHICS.md](ETHICS.md) | Ethical guardrails |
| [LEGAL.md](LEGAL.md) | Copyright, licensing, no-full-papers policy |

**AI use:** If you use AI tools to draft entries, follow [cursorrules](cursorrules) and human-validate citations and factual claims before submitting.

---

## Community

GitHub Issues and Discussions are the primary coordination channel while the project is in Phase 0. Discord/forum will be announced when ready.

---

## Recognition

All contributors whose PRs are merged are listed in [CONTRIBUTORS.md](CONTRIBUTORS.md). Maintainers add contributors manually during Phase 0; Phase 1 will automate this via a GitHub Action.

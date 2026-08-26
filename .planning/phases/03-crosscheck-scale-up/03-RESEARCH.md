# Phase 3: Crosscheck scale-up - Research

**Researched:** 2026-08-26
**Domain:** Git-native Crosscheck pipeline (bridge YAML → generator drafts → human-promoted catalog → stdlib repro → static hub + CI honesty)
**Confidence:** HIGH (pipeline, CI, hub, gitignore, schema); MEDIUM (which new bridge to lock — ranked with evidence)

<user_constraints>
## User Constraints (from CONTEXT.md)

**CRITICAL:** If CONTEXT.md exists from /gsd-discuss-phase, copy locked decisions here verbatim. These MUST be honored by the planner.

### Locked Decisions

- **D-01 (CROSS-06 generate):** Run `python scripts/generate_crosscheck.py --bridge <id> --write` for **≥1 bridge that currently has zero files in `protocols-catalog/`**. Document the exact command and output paths in `docs/CROSSCHECK.md`. Do not use `--all` as the documented happy path (too noisy). Habitat already has two seed protocols — it does not count as the "new bridge."
- **D-02 (CROSS-06 promote):** Promote **≥1** generated draft into `protocols-catalog/` after filling every TODO (`null_hypothesis`, `statistical_analysis_plan`, honest `experimental_design`). Human review remains the merge gate — do not auto-promote. Status may be `draft` or `ready`. **Do not set `status: confirmed` unless a real local run printed `RESULT: CONFIRMED`.** Prefer `ready` or `executed`.
- **D-03 (repro path):** The phase goal requires the path through a **repro bundle**. Add `repro/<protocol-id>/` with README + runnable script (stdlib preferred). Script must print a `RESULT:` line and **exit 0 always** (Phase 2 contract). If the science is not yet a precision pass, print `INCONCLUSIVE` honestly. Do **not** add a fifth `grep RESULT: CONFIRMED` job — that is Phase 4 TRUST-02.
- **D-04 (no trophy hunt):** Do not start another FSS / exponent precision campaign. Do not copy epidemic's 90-minute Monte Carlo sweep. If the new protocol cannot be a small stdlib demo, ship promoted YAML + a documented local runner, still without claiming CONFIRMED.
- **D-05 (CROSS-07 parity):** Add a parity matrix covering **all four seed protocols** (habitat FSS, cluster exponent, Ising EWI, epidemic FSS). Columns at minimum: protocol id, Python canonical script, browser JS (yes/no + filename), Colab notebook (yes/no), CI grep CONFIRMED (yes/no), RESULT contract (`exit 0`, stdout token). Epidemic is Colab-only (no JS). Habitat/cluster/Ising have JS with lighter demo budgets than Python. State explicitly that **Python is canonical**; browser/Colab are demo tier.
- **D-06 (hub):** Surface the parity matrix from the existing Crosscheck hub section and/or `docs/CROSSCHECK.md` (linked from the hub). Do not redesign the dashboard (Phase 5). After protocol YAML / hub HTML changes: `python scripts/build_crosscheck.py --apply` then `--check`.
- **D-07 (epidemic freeze):** Do not change `epidemic_percolation_fss.py` constants, freeze vector, or `NU_THEORY = 3.0`. Do not shop a prettier R².
- **D-08 (schemas):** New/moved protocol YAML must pass `python scripts/validate_schemas.py`. Generator drafts that stay in `drafts/crosscheck/` are gitignored or committed only if `.gitignore` allows — check before planning; do not fight Wave Factory gitignore patterns.
- **D-09:** No marketing, DNS, arXiv, or new catalog waves. No JS runner for networkx protocols.

### Claude's Discretion

- Which new bridge to generate from (must satisfy D-01). Prefer a desktop-tier opportunity that can share percolation/Ising patterns already in `repro/`.
- Whether the promoted protocol is `draft` vs `ready`.
- Whether the new repro is a thin stdlib demo or README-only plus a `python -c` smoke that the generator output validates.
- Exact filename/location of the parity matrix (`docs/CROSSCHECK.md` section vs `docs/CROSSCHECK_PARITY.md`).
- Whether to add `generate_crosscheck.py` to `tests/repo_smoke` (nice-to-have; TRUST-03 is Phase 4 — only add a **fast** dry-run smoke if it stays <30s and needs no networkx).

### Deferred Ideas (OUT OF SCOPE)

- Feeding execution results YAML back into hypothesis validation (`docs/CROSSCHECK.md` internal "Phase 3")
- Unified percolation toolkit across ecology/epidemiology/oncology (`docs/CROSSCHECK.md` internal "Phase 4")
- TRUST-02 / TRUST-03 CI expansion
- HUB-01 smart recommendations
- In-browser JS for epidemic FSS
- Raising epidemic freeze R²
</user_constraints>

<phase_requirements>
## Phase Requirements

| ID | Text | Phase | Status | Planning implication |
|----|------|-------|--------|----------------------|
| **CROSS-06** | Second-bridge protocol drafts promoted or generated via `generate_crosscheck.py` | 3 | Pending | Happy path is `--bridge <id> --write` (not `--all`), then **human** promote of ≥1 draft with TODOs filled, plus a repro bundle. Habitat is not a "second bridge." |
| **CROSS-07** | Browser runner outputs documented vs Python canonical (parity matrix) | 3 | Pending | Document all **four existing seeds**. Python = canonical; JS/Colab = demo. Do not add epidemic JS (D-09). |

Traceability: `.planning/REQUIREMENTS.md` (v1.1). Success criteria from `.planning/ROADMAP.md`: (1) generator run documented for ≥1 new bridge; (2) parity doc: Python vs browser outcome tiers per protocol. ROADMAP plans: **03-01** Generate + promote; **03-02** Browser/Colab parity matrix + hub updates.
</phase_requirements>

<architectural_responsibility_map>
## Architectural Responsibility Map

This is a **git-native static pipeline**, not a multi-tier web app. Capabilities still have owners — do not invent an API/backend for Crosscheck.

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| Draft generation (`generate_crosscheck.py`) | Local CLI / git working tree | — | Reads `cross-domain/**/b-*.yaml`, writes `drafts/crosscheck/<rel>/<id>.yaml`. No network. |
| Human promote | Git + PR (storage) | Schema CI | Manual copy into `protocols-catalog/`. `validate_schemas.py` is the merge gate. No promote script. |
| Canonical experiment | Local Python (stdlib preferred) | GitHub Actions (existing 4 greps only) | Python scripts under `repro/<id>/` are source of truth. New protocol must **not** get a 5th CONFIRMED grep. |
| Browser demo | Static Pages / Browser | — | Only if stdlib JS exists **and** is listed in `scripts/crosscheck_browser.py` `BROWSER_RUNNERS`. D-09: no JS for networkx. |
| Colab demo | External notebook host | Local `run_crosscheck.ipynb` | Epidemic only today. New protocol should not require Colab unless it needs networkx (prefer stdlib so Colab is unnecessary). |
| Hub Crosscheck grid | Static HTML (GitHub Pages) | `render_crosscheck_hub.py` | Cards injected between `<!-- @hub-crosscheck-grid-begin/end -->` in `dashboard/index.html`. Not a redesign. |
| Drift gate | CI / Frontend Server (Actions) | Local `--check` | `build_crosscheck.py --check` snapshots hub-grid block, explainer HTML, and `repro/*/index.html`. |
| Integrity / claims | Documentation + catalog YAML | LEGAL / METHODOLOGY | Status enum and `RESULT:` stdout — never auto-`confirmed`. |

**Single-product note:** All Crosscheck "runtime" is files in git. The hub is a static site. Planning should not add servers, APIs, or smart-recommendations (HUB-01 / Phase 5).
</architectural_responsibility_map>

<research_summary>
## Summary

Phase 3 is a **pipeline + honesty** phase: prove that a *new* bridge (zero files in `protocols-catalog/` today) can go `generate_crosscheck.py --write` → `drafts/crosscheck/` → human-edited `protocols-catalog/` → `repro/<id>/` → hub card, **without** a fifth CONFIRMED trophy or a dashboard redesign.

The generator is a local PyYAML CLI. It is **not** a promoter. There is **no** `promote_crosscheck.py` (Wave Factory's `promote_wave_factory_batch.py` is a different catalog). Drafts skip if the output path exists. Generated YAML is schema-shaped but scientifically incomplete: `null_hypothesis` and `statistical_analysis_plan` are TODO strings; `experimental_design` is five generic steps; `last_reviewed` is hardcoded `2026-06-21`; titles still say `[DRAFT]`. `validate_schemas.py` only walks `protocols-catalog/`, so drafts are invisible to CI until promoted.

**Primary recommendation:** Generate from **`b-percolation-oncology`**, promote **opportunity 1** (giant-component fraction) as a **thin stdlib lattice demo** that prints `RESULT: INCONCLUSIVE` and exits 0. Put the CROSS-07 parity matrix in `docs/CROSSCHECK.md` (new section, linked from the existing hub manifesto sentence). Do not add JS. Do not grep CONFIRMED. After YAML/hub changes: `build_crosscheck.py --apply` then `--check`.

Do **not** confuse GSD Phase 3 with the numbered "Phase 3 / Phase 4" table inside `docs/CROSSCHECK.md` (those are deferred: results-YAML feedback and unified toolkit).
</research_summary>

<standard_stack>
## Standard Stack

The established libraries/tools for **this** domain (repo Crosscheck loop). Do not add a new framework.

### Core
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| CPython | 3.11 (CI in `crosscheck-repro.yml`, `validate.yml`) | Canonical repro + generator | Already the Actions runtime |
| PyYAML | repo-local (`import yaml`; `safe_load` / `dump`) | Bridge + protocol YAML | Generator and every catalog script |
| jsonschema Draft 2020-12 | `scripts/validate_schemas.py` | Protocol schema gate | `schemas/protocol.yaml` `$schema` is draft/2020-12 |
| Python stdlib (`random`, `math`) | 3.11 | Lattice percolation / Ising | Habitat FSS, cluster, Ising are stdlib-only |

### Supporting
| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| networkx | CI `pip install networkx` only | ER bond percolation | **Epidemic seed only.** D-09 / D-04: do not pick a new bridge that needs it. |
| pytest | `tests/repo_smoke/` | `--check` + freeze-fit regression | Do not add live MC here. Optional **fast** `generate_crosscheck --dry-run` only if <30s. |
| GitHub Actions | `crosscheck-repro.yml`, `validate.yml` | CONFIRMED greps + schema | Do not add a 5th CONFIRMED job. Path filter `repro/**` **will still re-run the existing four** when a new bundle is added. |

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| Thin stdlib lattice demo | README-only + `python -c` schema smoke | Allowed by discretion, weaker CROSS-06 "repro path" story. D-03 wants a runnable script that prints `RESULT:`. |
| `b-percolation-oncology` | `b-percolation-threshold-x-polymer-gelation` | Polymer is `established` and 2D **bond** `p_c = 1/2` is exact — slightly easier physics, weaker manifesto-toolkit story. |
| Manual promote (copy YAML) | New `promote_crosscheck.py` | Wave Factory already has a promote script; Crosscheck docs say human PR. Building a promoter is out of scope and risks auto-promote (D-02). |
| New `docs/CROSSCHECK_PARITY.md` | Section in `docs/CROSSCHECK.md` | Extra file is fine; hub already links the manifesto. Prefer one page unless the matrix is huge. |
| JS runner for the new protocol | Python-only | D-09 forbids JS for networkx; even for stdlib, Phase 3 is not a fifth in-browser trophy. |

**Installation (no new packages expected):**
```bash
# already required for generator + schema
pip install pyyaml jsonschema
# epidemic CI only — do not add to the new protocol
# pip install networkx
```
</standard_stack>

<architecture_patterns>
## Architecture Patterns

### System Architecture Diagram

```text
cross-domain/**/b-<id>.yaml
        |  cross_pollination_opportunities[i]
        v
python scripts/generate_crosscheck.py --bridge <id> --write
        |  skip if dest exists
        v
drafts/crosscheck/<rel-parent>/<p-b-...>.yaml     [NOT validated; NOT gitignored today]
        |  HUMAN: fill TODOs, honest design, rename id?, set status draft|ready
        |  copy/move into protocols-catalog/<rel-parent>/
        |  add repro_bundle: repro/<protocol-id>/
        v
protocols-catalog/**/p-b-*.yaml                   [validate_schemas.py]
        |
        +--> repro/<protocol-id>/{README.md, script.py, requirements.txt}
        |         stdout: "RESULT: INCONCLUSIVE|CONFIRMED"
        |         process exit: 0 always (D-03)
        |
        +--> python scripts/build_crosscheck.py --apply
                 |-- generate_repro_index_pages.py  --> repro/<id>/index.html
                 |-- render_crosscheck_hub.py --apply --> dashboard/index.html  (@hub-crosscheck-grid)
                 |-- generate_explainers.py <bridge-ids> --> dashboard/explainers/<bridge>.html
                 v
             python scripts/build_crosscheck.py --check   [CI + repo_smoke]
```

Hub **run-mode** branch (`scripts/crosscheck_browser.py` `run_mode`):

```text
if proto_id in BROWSER_RUNNERS and JS file exists -> "browser" ("Run in browser")
else if run_crosscheck.ipynb exists               -> "colab"   ("Open in Colab")
else                                               -> "local"   ("Run repro")
```

New protocol with stdlib Python only → **local** card. That is correct; do not add JS to force a browser badge.

### Recommended Project Structure

```
drafts/crosscheck/physics-oncology/          # generator output (local; see D-08)
  p-b-percolation-oncology-….yaml

protocols-catalog/physics-oncology/          # NEW dir, mirrors cross-domain/ physics-oncology/
  p-b-percolation-oncology-gcc.yaml          # human id (recommended rename)

repro/p-b-percolation-oncology-gcc/
  README.md
  requirements.txt                           # empty/comment: stdlib
  giant_component_fraction.py                # RESULT: INCONCLUSIVE; exit 0
  index.html                                 # generated — do not hand-edit

docs/CROSSCHECK.md                           # generate/promote commands + parity matrix
dashboard/index.html                         # grid regenerated; static manifesto link + optional #parity
```

Mirror existing seeds: `protocols-catalog/physics-ecology/`, `physics-epidemiology/`, `physics-social/`.

### Pattern 1: Generate then skip-if-exists
**What:** `--write` creates parent dirs and writes YAML only when the destination file is missing.
**When to use:** First generation of a bridge. Re-running `--write` after a partial edit will **not** refresh TODOs.
**Example:**
```python
# Source: scripts/generate_crosscheck.py (write branch)
out_path.parent.mkdir(parents=True, exist_ok=True)
if out_path.exists():
    print(f"      skip (exists): {out_path.relative_to(ROOT)}")
else:
    out_path.write_text(
        yaml.dump(protocol, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )
```

### Pattern 2: Human promote (no script)
**What:** Copy the draft to `protocols-catalog/<same rel-parent as the bridge>/`, then rewrite science fields. Same governance as Wave Factory: automation proposes, humans merge.
**When to use:** Always. There is no Crosscheck promote CLI.
**Example:**
```bash
# Documented happy path (D-01) — example; lock bridge in plan
python scripts/generate_crosscheck.py --bridge b-percolation-oncology --write
# Output: drafts/crosscheck/physics-oncology/p-b-percolation-oncology-*.yaml

# Promote (manual). Rename id to a short human slug before schema/hub.
# Fill null_hypothesis, statistical_analysis_plan, experimental_design.
# Set status: ready  (not confirmed)
# Set repro_bundle: repro/p-b-percolation-oncology-gcc/
python scripts/validate_schemas.py
python scripts/build_crosscheck.py --apply
python scripts/build_crosscheck.py --check
```

### Pattern 3: RESULT token + exit 0
**What:** Phase 2 contract — stdout carries the scientific outcome; process exit is always 0 so CI `grep` is the gate, not the exit code.
**When to use:** Every new repro script (D-03). If not a precision pass, print `INCONCLUSIVE`.
**Example:**
```python
# Source: repro/p-b-percolation-epidemiology-fss/epidemic_percolation_fss.py
print(
    f"RESULT: {'CONFIRMED' if passed else 'INCONCLUSIVE (increase SEEDS_PER_N for higher precision)'}"
)
return 0
```

### Pattern 4: Hub injection, not redesign
**What:** `render_crosscheck_hub.py` replaces only the marked grid. The section title, manifesto `<a href="../docs/CROSSCHECK.md">`, and surrounding layout are static.
**When to use:** 03-02. Link the parity matrix by adding an anchor in `docs/CROSSCHECK.md` and (optionally) a clause in the existing `section-desc` paragraph. Do not add a new hub section, cards layout, or recommendation engine.

### Anti-Patterns to Avoid
- **`--all --write` as the docs happy path:** noisy; D-01 forbids it.
- **Auto-promote / Wave Factory-style `--apply` promoter for protocols:** D-02 human gate.
- **`status: confirmed` because the YAML looks complete:** only if a real run printed `RESULT: CONFIRMED` (D-02). Prefer `ready` or `executed`.
- **Fifth `grep RESULT: CONFIRMED` job:** Phase 4 TRUST-02 (D-03).
- **Copying epidemic Monte Carlo or habitat 350-trial FSS:** D-04 trophy hunt.
- **JS runner for networkx (or for the new protocol):** D-09; Phase 3 is pipeline, not a fifth browser demo.
- **Hand-editing `repro/*/index.html` or explainer HTML:** 02-03 established `--apply` as the only writer.
- **Implementing `docs/CROSSCHECK.md` internal Phase 3/4:** deferred (results YAML; unified toolkit).
- **Fighting `drafts/wave_factory/` gitignore:** D-08. Adding `drafts/crosscheck/` is *analogous*, not a fight; un-ignoring wave_factory is the fight.
</architecture_patterns>

<dont_hand_roll>
## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Promoting drafts | `promote_crosscheck.py` with `--apply` | Manual copy + PR (documented in `docs/CROSSCHECK.md`) | Human merge gate is the product. Wave Factory already has the only promote script. |
| YAML validation | Ad-hoc required-key checks | `python scripts/validate_schemas.py` + `schemas/protocol.yaml` | `additionalProperties: false`; CI already runs it. |
| Hub card HTML | Hand-written 5th card | `render_crosscheck_hub.py` via `build_crosscheck.py --apply` | Drift gate will fail `--check` if you hand-edit the marked block. |
| Explainer for the new bridge | Hand HTML in `dashboard/explainers/` | `generate_explainers.py` (called by `--apply`; union of `DEFAULT_BRIDGES` + every `source_bridge`) | Same drift snapshot. |
| Lattice percolation / union-find | New physics library | Copy patterns from `repro/p-b-habitat-percolation-ecology-cluster-exponent/cluster_size_exponent.py` | Already stdlib; D-04 wants thin reuse, not a new engine. |
| Run-mode detection | Duplicate browser/colab ifs in hub | `scripts/crosscheck_browser.py` | Single registry `BROWSER_RUNNERS` + `run_crosscheck.ipynb`. |
| Schema for drafts | Validating `drafts/crosscheck/` in CI | Validate only after promote | `validate_schemas.py` deliberately scopes to `protocols-catalog/`. |
| CONFIRMED CI for the new protocol | 5th grep job | Honest `INCONCLUSIVE` + document in parity matrix as CI grep = no | TRUST-02 is Phase 4. |

**Key insight:** The missing piece is not code generation quality — it is a **repeatable human loop** and an **honest run-mode matrix**. Experts in this repo already solved lattice percolation, hub injection, and RESULT tokens. Phase 3 should reuse those, not invent a promoter or a precision campaign.
</dont_hand_roll>

<common_pitfalls>
## Common Pitfalls

### Pitfall 1: Treating generator YAML as catalog-ready
**What goes wrong:** Promoted file still has `TODO:` strings, `[DRAFT]` title, generic five-step design, `last_reviewed: "2026-06-21"`.
**Why it happens:** `null_hypothesis` and `statistical_analysis_plan` are **optional** in `schemas/protocol.yaml` (`required` is only id, title, status, source_bridge, falsifiable_prediction, experimental_design, feasibility_tier). TODOs still **pass** schema.
**How to avoid:** D-02 checklist before `validate_schemas.py`: rewrite those three science fields; drop `[DRAFT]`; set today's `last_reviewed`; add `repro_bundle`.
**Warning signs:** `TODO:` grep hits in `protocols-catalog/`; title starts with `[DRAFT]`.

### Pitfall 2: Generator `feasibility_tier` over-labels desktop
**What goes wrong:** Oncology opportunity 0 (DCE-MRI imaging) is tagged `desktop` because the text contains "percolation **models**" (`DESKTOP_KEYWORDS` includes `"model"`). Island biogeography opp 0 is `field` because of `"landscape"`.
**Why it happens:** Keyword heuristic in `infer_feasibility()`, not a human feasibility review.
**How to avoid:** Promote the opportunity that is actually a laptop experiment (oncology **index 1**, giant-component metrics). Override `feasibility_tier` if the heuristic is wrong.
**Warning signs:** Protocol claims desktop but experimental_design starts with clinical imaging or satellite land-cover.

### Pitfall 3: Long, truncated protocol ids
**What goes wrong:** Generator ids are `p-{bridge_id}-{slugify(opportunity)[:40]}` — e.g. `p-b-percolation-oncology-percolation-derived-metrics-giant-compon`. Ugly hub titles and Windows-long paths.
**Why it happens:** Slug is first sentence, max 40 chars, no vocabulary of `fss` / `gcc` / `ewi`.
**How to avoid:** On promote, rename to a short id matching seed style (`p-b-habitat-percolation-ecology-fss`). Schema pattern is `^p-b-[a-z0-9.-]+$` (no length cap). Repro folder must match `repro_bundle`.
**Warning signs:** Hub card truncates the `[DRAFT] Crosscheck <bridge> — opportunity N` title.

### Pitfall 4: `status: confirmed` or a 5th CI grep
**What goes wrong:** Catalog lies, or Phase 4 work is pulled forward.
**Why it happens:** All four seeds already grep CONFIRMED; adding a bundle feels like "the same CI job."
**How to avoid:** D-02/D-03/D-04. Print `INCONCLUSIVE`. Status `ready` (or `executed` only if a local run happened). No new grep.
**Warning signs:** PR adds a 5th `grep -q "RESULT: CONFIRMED"` step; YAML `status: confirmed` without a logged stdout.

### Pitfall 5: Generated `index.html` still claims exit code 1
**What goes wrong:** `generate_repro_index_pages.py` hardcodes "Exit code `0` = prediction within tolerance; `1` = falsified". Habitat FSS README still says the same, but the Python **returns 0 always**. 02-03 deferred fixing the generator sentence.
**Why it happens:** Shared template predates the Phase 2 exit-0 contract.
**How to avoid:** Parity matrix states the **code** contract. Planner should treat a one-line generator fix as 03-02 honesty (not a dashboard redesign). If left unfixed, `--apply` will stamp the lie onto the **new** protocol's `index.html` too.
**Warning signs:** New `repro/<id>/index.html` contradicts D-03.

### Pitfall 6: Adding a new `repro/` directory retriggers all four CONFIRMED jobs
**What goes wrong:** PR runtime includes habitat FSS (minutes) + epidemic ~90s even though the new protocol is INCONCLUSIVE.
**Why it happens:** `crosscheck-repro.yml` paths include `repro/**` and `protocols-catalog/**`.
**How to avoid:** Expected. Do not disable those jobs. Do not add a 5th. Budget wall-clock for the PR.
**Warning signs:** Someone "simplifies" CI by removing seed greps — that is a regression of CROSS-01–04.

### Pitfall 7: Numbering collision with `docs/CROSSCHECK.md` roadmap
**What goes wrong:** Planner implements "execution results YAML" or "unified percolation toolkit" thinking that is GSD Phase 3/4.
**Why it happens:** Manifesto table uses Phase 3/4 for different work. CONTEXT deferred those.
**How to avoid:** GSD Phase 3 = CROSS-06 + CROSS-07 only. Mention the collision in the manifesto when editing it.
**Warning signs:** New `results.yaml` schema; shared toolkit package across ecology/epidemiology/oncology.

### Pitfall 8: Committing raw drafts vs fighting gitignore
**What goes wrong:** Unreviewed TODO YAML lands on `main`, or someone deletes `drafts/wave_factory/` from `.gitignore`.
**Why it happens:** `drafts/crosscheck/` is **not** ignored today; only `drafts/wave_factory/` is.
**How to avoid:** Prefer generate locally → promote the filled file → leave drafts untracked. Optionally add `drafts/crosscheck/` to `.gitignore` (parallel to wave_factory — allowed). Do not un-ignore wave_factory (D-08).
**Warning signs:** `git status` shows dozens of `p-b-*.yaml` under drafts after an accidental `--all --write`.
</common_pitfalls>

<code_examples>
## Code Examples

Verified from this repository (not third-party docs).

### Generator CLI (D-01 happy path)
```bash
# Source: scripts/generate_crosscheck.py docstring + argparse
python scripts/generate_crosscheck.py --bridge b-percolation-oncology --dry-run
python scripts/generate_crosscheck.py --bridge b-percolation-oncology --write
# Do not document as happy path:
# python scripts/generate_crosscheck.py --all --write
```

`--bridge` XOR `--all` required. `--dry-run` XOR `--write`. Neither write flag: still lists ids, then prints `Hint: add --dry-run or --write`.

### Fields the generator emits (schema gaps)
```python
# Source: scripts/generate_crosscheck.py build_protocol()
return {
    "id": protocol_id,                          # p-{bridge_id}-{slug[:40]}
    "title": f"[DRAFT] Crosscheck {bridge_id} — opportunity {index + 1}",
    "status": "draft",
    "source_bridge": bridge_id,
    "source_hypothesis": related_h,             # FIRST related_hypotheses only
    "source_unknown": related_u,                # FIRST related_unknowns only
    "pollination_index": index,
    "falsifiable_prediction": opportunity.strip(),
    "null_hypothesis": "TODO: state what outcome would refute the bridge mapping",
    "translation_mapping": translation,         # from bridge translation_table
    "experimental_design": [                    # generic; not honest
        f"Load bridge {bridge_id} ...",
        "...",
        "Compare result to prediction; record confirmed or falsified.",
    ],
    "statistical_analysis_plan": "TODO: specify test statistic and acceptance criteria",
    "feasibility_tier": infer_feasibility(opportunity),
    "last_reviewed": "2026-06-21",              # hardcoded
    # missing: repro_bundle, estimated_runtime, references
}
```

Draft dest path = `drafts/crosscheck/` + bridge path relative to `cross-domain/`. Example: `cross-domain/physics-oncology/b-percolation-oncology.yaml` → `drafts/crosscheck/physics-oncology/p-b-….yaml`.

### Protocol schema: required vs TODO-optional
```yaml
# Source: schemas/protocol.yaml
required:
  - id
  - title
  - status
  - source_bridge
  - falsifiable_prediction
  - experimental_design
  - feasibility_tier
# optional but D-02 requires filling before promote:
# null_hypothesis, statistical_analysis_plan, repro_bundle, estimated_runtime
additionalProperties: false
status.enum: [draft, ready, executed, confirmed, falsified]
id.pattern: "^p-b-[a-z0-9.-]+$"
```

`validate_schemas.py` iterates `protocols-catalog/**/p-b-*.yaml` only and checks `source_bridge` exists in `cross-domain/`.

### Four-seed run-mode registry
```python
# Source: scripts/crosscheck_browser.py
BROWSER_RUNNERS = {
    "p-b-habitat-percolation-ecology-fss": "simulate_percolation_fss.js",
    "p-b-habitat-percolation-ecology-cluster-exponent": "cluster_size_exponent.js",
    "p-b-ising-social-dynamics-ewi": "ising_critical_slowing.js",
}
COLAB_NOTEBOOK = "run_crosscheck.ipynb"
# epidemic: no BROWSER_RUNNERS entry; has run_crosscheck.ipynb → run_mode "colab"
```

### Hub markers (do not redesign)
```html
<!-- Source: dashboard/index.html around the Crosscheck section -->
<section id="crosscheck">
  ...
  <a href="../docs/CROSSCHECK.md">Crosscheck manifesto</a>
  ...
  <!-- @hub-crosscheck-grid-begin -->
  ... four seed cards ...
  <!-- @hub-crosscheck-grid-end -->
</section>
```

`build_crosscheck.py --check` snapshots **only** the marked grid (`@hub-crosscheck-grid`), plus explainer HTML and `repro/*/index.html`. Edits to the static manifesto sentence are **outside** the snapshot (safe) but still need `mkdocs build --strict` if `docs/` changes.

### Seed RESULT / exit facts (for the parity matrix)
```python
# habitat FSS: return 0 always
print(f"RESULT: {'CONFIRMED' if passed else 'INCONCLUSIVE (increase TRIALS_PER_P for higher precision)'}")
return 0

# cluster: can return 1 if too few clusters or NaN fit — then no RESULT line
if len(pooled_sizes) < 3:
    print("ERROR: insufficient clusters for fit")
    return 1

# ising / epidemic: return 0 always + RESULT token
```
</code_examples>

<validation_architecture>
## Validation Architecture

| Gate | Command / workflow | What it proves | Phase 3 use |
|------|--------------------|----------------|-------------|
| Schema | `python scripts/validate_schemas.py` | Promoted YAML matches `schemas/protocol.yaml`; `source_bridge` exists | **Required** after promote (D-08). Drafts in `drafts/crosscheck/` are **not** scanned. |
| Catalog smoke | `pytest tests/repo_smoke/test_catalog_regression.py` | Schema + domain pages + hub counts + orphans | Must stay green. New protocol YAML is included automatically. |
| Crosscheck drift | `python scripts/build_crosscheck.py --check` (also `tests/repo_smoke/test_crosscheck_artifacts.py`) | Hub grid, explainers, repro index match catalog | **Required** after `--apply` (D-06). |
| Freeze fits | `tests/repo_smoke/test_crosscheck_repro_regression.py` | Habitat/Ising/cluster/epidemic **fixed-input** fits | Do not add live MC. Optional: do **not** add a freeze test for the new INCONCLUSIVE demo. |
| CONFIRMED greps | `.github/workflows/crosscheck-repro.yml` | Four seed scripts print `RESULT: CONFIRMED` | Will **re-run** on `repro/**` or `protocols-catalog/**` PRs. **Do not add a 5th job.** |
| Catalog validate workflow | `.github/workflows/validate.yml` | `validate_schemas.py` + `audit_quality.py` | Paths already include `protocols-catalog/**`, `repro/**`, `scripts/generate_crosscheck.py`. Does **not** execute the generator. |
| MkDocs | `mkdocs build --strict` | `docs/CROSSCHECK.md` nav (`mkdocs.yml` "Prove the bridge") | Required when manifesto / parity section changes (documentation-and-dashboard rule). |
| Optional generator smoke | `python scripts/generate_crosscheck.py --bridge <id> --dry-run` | CLI + YAML dump | Discretion: add to `repo_smoke` only if <30s and no networkx (TRUST-03 is Phase 4). |

**Honesty checks (manual / plan acceptance, not CI):**
- Promoted YAML has no `TODO:`
- `status` is not `confirmed` unless stdout was `RESULT: CONFIRMED`
- New script prints `RESULT:` and exits 0
- Parity matrix lists all four seeds with Python-canonical vs demo-tier budgets
- Epidemic constants untouched (D-07)

**What "done" is not:** a fifth CONFIRMED, a JS runner, a promoter script, or hub visual redesign.
</validation_architecture>

<security_domain>
## Security Domain

**Threat model:** Maintainer-run local CLI that reads **committed bridge YAML** and writes **YAML drafts**. No untrusted web input, no authn, no user-uploaded files, no secrets.

| ASVS / class | Applicable? | Notes |
|--------------|-------------|-------|
| V2 Authn / V3 Session / V4 Access | N/A | No Crosscheck service. |
| V5 Input validation | Low | `yaml.safe_load` on git-tracked files only. Do not switch to `yaml.load`. Schema `additionalProperties: false` on promote. |
| V5 Injection (XSS) | Low | Hub/explainer generators use `html.escape` on titles. New protocol titles must stay escaped via `--apply`, not hand HTML. |
| V6 Crypto | N/A | |
| V7 Error handling | N/A | |
| V8 Data protection | Integrity, not confidentiality | Do not commit identifiable imaging (oncology DCE-MRI is **not** the repro). Thin lattice demo uses synthetic occupancy only. Follow `docs/ETHICS_REPRODUCIBILITY_AND_DATA.md`. |
| V10 Malicious code | N/A | Generator does not interpolate opportunity text into Python — only YAML strings. Still do not `eval` opportunity prose. |
| V14 Config | Low | `.gitignore`: `drafts/wave_factory/` ignored; `drafts/crosscheck/` **not** ignored. |

**Integrity rules (the real "security" of this phase):**
1. Do **not** claim `CONFIRMED` in YAML or hub copy without `RESULT: CONFIRMED` stdout.
2. Do **not** auto-promote drafts.
3. Do **not** treat GSD artifacts as scientific evidence (`PROJECT.md` / METHODOLOGY).
4. Generator is not a web scraper; do not wire it to untrusted URLs.

LEGAL.md: no paywalled PDFs, no PII. Oncology protocol must not imply clinical data in-repo.
</security_domain>

<sota_updates>
## State of the Art (this repo, 2026-08)

Not a fast-moving JS framework. Relevant "current approach" is **this repository after Phase 2**.

| Old approach (pre-Crosscheck / Phase 1 READMEs) | Current approach (Phase 2 contract) | When changed | Impact on Phase 3 |
|-------------------------------------------------|-------------------------------------|--------------|-------------------|
| Exit code 1 = falsified | Exit 0 always; `RESULT:` token on stdout | Epidemic 02-01/02-03; Ising already exit 0 | New script **must** exit 0. Generator `index.html` sentence is stale. |
| Habitat README "0 = pass, 1 = falsified" | Code returns 0 always | Drift | CROSS-07 matrix must cite **code**, not stale README. Optional README fix in 03-02. |
| 3 seed protocols in `docs/CROSSCHECK.md` table | 4 seeds; Ising missing from manifesto table | Phase 1 Ising + Phase 2 epidemic | 03-02 should list all four + the new protocol. |
| Manifesto "Phase 3" = results YAML into hypotheses | GSD Phase 3 = generate/promote + parity | GSD v1.1 2026-06-23 | Do not implement manifesto Phase 3. |
| Wave Factory promote CLI | Crosscheck: manual PR only | Wave Factory vs Crosscheck split | Do not copy `promote_wave_factory_batch.py`. |

**New tools/patterns to consider:**
- **`--apply` / `--check` pair:** already the Crosscheck equivalent of a build system. Always run both after catalog/hub edits.
- **`run_mode()` registry:** extending `BROWSER_RUNNERS` is how a future JS demo would appear — out of scope for the new protocol.

**Deprecated/outdated:**
- Documenting `--all --write` as the contributor happy path.
- Using generated `[DRAFT]` YAML as a finding.
- Fifth in-browser runner as a substitute for a documented pipeline.
</sota_updates>

<bridge_candidates>
## New-bridge ranking (CROSS-06 / D-01)

**Constraint:** zero files in `protocols-catalog/` for that `source_bridge`. Existing catalog is **only**:

| Protocol | `source_bridge` | Dir |
|----------|-----------------|-----|
| `p-b-habitat-percolation-ecology-fss` | `b-habitat-percolation-ecology` | `protocols-catalog/physics-ecology/` |
| `p-b-habitat-percolation-ecology-cluster-exponent` | same | same |
| `p-b-percolation-epidemiology-fss` | `b-percolation-epidemiology` | `protocols-catalog/physics-epidemiology/` |
| `p-b-ising-social-dynamics-ewi` | `b-ising-social-dynamics` | `protocols-catalog/physics-social/` |

Habitat is **disqualified** as the "new bridge" (D-01), even though it still has unused opportunities (unified toolkit, climate EWI).

Verified via `python scripts/generate_crosscheck.py --bridge <id> --dry-run` on 2026-08-26. Linked hypothesis/unknown YAML exist for the top two.

### Rank 1 (recommended): `b-percolation-oncology`

| Field | Evidence |
|-------|----------|
| Path | [VERIFIED: `cross-domain/physics-oncology/b-percolation-oncology.yaml`] |
| Catalog files | **Zero** [VERIFIED: `protocols-catalog/` listing] |
| Opportunities | **3** (generator indices 0–2), all tagged `desktop` by heuristic |
| Stdlib vs networkx | **Stdlib lattice** — same giant-component / union-find as cluster exponent; translation table is bond occupancy ↔ vessel patency, GCC ↔ viable vascular core |
| Thin repro without precision pass | **Yes.** Occupancy sweep → giant-component fraction S(p) on L×L site percolation; print `RESULT: INCONCLUSIVE` (not a clinical biomarker, not FSS ν). Do **not** hunt CONFIRMED. |
| Why first | Habitat opportunity 3 already names this bridge as the third leg of a future toolkit (`docs/CROSSCHECK.md` internal Phase 4 — **do not build the toolkit**, do use the named target). New domain (oncology), not a fifth ecology protocol. |
| Promote which opp | **Index 1** — "Percolation-derived metrics (giant-component fraction) as a real-time treatment-response biomarker." Operationalize as a **synthetic lattice**, not DCE-MRI. |
| Skip | Index 0 is imaging/clinical (heuristic-mislabeled desktop). Index 2 is adaptive dosing / control — not a thin demo. |
| Linked records | `h-adaptive-therapy-percolation-threshold`, `u-tumor-containment-percolation` [VERIFIED] |
| Generator ids (raw) | `p-b-percolation-oncology-oncologists-provide-longitudinal-imaging`; `…-percolation-derived-metrics-giant-compon`; `…-adaptive-dosing-protocols-derived-from-o` |
| Suggested promote id | `p-b-percolation-oncology-gcc` (human rename) |
| JS | **No** (D-09 not triggered; still skip JS to keep the phase a pipeline demo) |

### Rank 2: `b-percolation-threshold-x-polymer-gelation`

| Field | Evidence |
|-------|----------|
| Path | [VERIFIED: `cross-domain/chemistry-physics/b-percolation-threshold-x-polymer-gelation.yaml`] |
| Catalog files | Zero |
| Opportunities | **2**, both generator-`desktop` |
| Stdlib vs networkx | **Stdlib.** 2D square **bond** percolation has exact `p_c = 1/2`; Flory–Stockmayer is mean-field. Cluster/habitat union-find ports cleanly. |
| Thin repro | **Yes**, even easier physics than oncology. Risk: a spanning-above-0.5 check is so easy it could print `CONFIRMED` by accident — D-04 still says do not claim CONFIRMED; keep acceptance criteria honest (e.g. document INCONCLUSIVE unless a precision pass is explicitly in scope — it is not). |
| Why second | Status `established`. Opp 1 is literally "hybrid simulations coupling reaction kinetics with bond-percolation." Opp 0 wants microrheology **datasets** (not in-repo). |
| Linked records | `h-percolation-threshold-x-polymer-gelation`, `u-percolation-mapping-quantitative-gel-chemistry` [VERIFIED] |
| Cost | Very long generated ids; promote dir would be `protocols-catalog/chemistry-physics/`. |

### Rank 3: `b-island-biogeography-percolation` (weak)

| Field | Evidence |
|-------|----------|
| Path | [VERIFIED: `cross-domain/ecology-physics/b-island-biogeography-percolation.yaml`] |
| Opportunities | **2** — opp 0 `field` (landscape/satellite), opp 1 `desktop` (climate + "model") |
| Stdlib | Yes (same 2D habitat lattice) |
| Why third | **Too close to habitat** (With & Crist 1995 even appears on the habitat cluster protocol). Satisfies D-01 literally but fails the "new bridge" spirit. |

### Rejected for this phase

| Bridge | Why not |
|--------|---------|
| `b-percolation-rumor-spreading` | 3 desktop opps, but SIR/bond mapping **duplicates epidemic**; scale-free `p_c → 0` wants networkx (D-09). |
| `b-percolation-network-robustness` | Scale-free dismantling / networkx. |
| `b-percolation-epidemiology` / habitat / Ising | Already have catalog files. |
| `b-climate-tipping-percolation` | Conceptual; EWI reuse would look like a second Ising trophy. |
| `b-supply-chain-network-x-bond-percolation-disruption` | Wants industrial datasets, not a stdlib demo. |
| `b-grokking-criticality` | Needs ML training; not a thin percolation/Ising port. |

**Planner default if orchestrator does not relock:** Rank 1, promote opp 1, stdlib GCC demo, `status: ready`, `RESULT: INCONCLUSIVE`, no JS, no CONFIRMED grep.
</bridge_candidates>

<parity_matrix_facts>
## CROSS-07 — seed run-mode facts (do not invent)

Python is **canonical**. Browser/Colab are **demo tier** with lighter budgets.

| Protocol id | Python canonical | Browser JS | Colab | CI grep `RESULT: CONFIRMED` | RESULT contract |
|-------------|------------------|------------|-------|-----------------------------|-----------------|
| `p-b-habitat-percolation-ecology-fss` | `simulate_percolation_fss.py` — L∈{16,32,64,128}, `TRIALS_PER_P=350`, `P_GRID=32` | **Yes** `simulate_percolation_fss.js` — same L, `TRIALS_PER_P=120`, `P_GRID=30` | No | **Yes** (`crosscheck-repro.yml` habitat job) | Prints `RESULT: CONFIRMED\|INCONCLUSIVE`; **code `return 0`**. README still says "exit 1 = falsified" (**stale**). |
| `p-b-habitat-percolation-ecology-cluster-exponent` | `cluster_size_exponent.py` — `P=0.59`, `L=256`, `SEEDS=20` | **Yes** `cluster_size_exponent.js` — `P=0.592`, `L=128`, `SEEDS=20` | No | **Yes** | Prints `RESULT:` on success; **can `return 1`** if too few clusters / NaN fit (no RESULT line). |
| `p-b-ising-social-dynamics-ewi` | `ising_critical_slowing.py` — `LATTICE_SIZE=48`, `EQ_SWEEPS_BASE=1200`, `EQ_SWEEPS_NEAR_TC=6000`, `SAMPLES=400` | **Yes** `ising_critical_slowing.js` — `L=32`, EQ 400/1600, `SAMPLES=120` | No | **Yes** | `RESULT:` + **exit 0 always**. README matches. |
| `p-b-percolation-epidemiology-fss` | `epidemic_percolation_fss.py` — networkx, N∈{200,…,5000}, `SEEDS_PER_N=20` (D-07 freeze — do not change) | **No** (not in `BROWSER_RUNNERS`; D-09) | **Yes** `run_crosscheck.ipynb` (clone-and-run of the `.py`) | **Yes** | `RESULT:` + **exit 0 always**. README matches. Catalog `status: confirmed`. |

Hub labels today [VERIFIED: `dashboard/index.html` cards]: cluster/habitat FSS/Ising → "Run in browser"; epidemic → "Open in Colab".

`docs/CROSSCHECK.md` protocol table currently lists **three** seeds and **omits Ising** — 03-02 should fix that when adding the matrix.

**Suggested matrix location:** new `## Run-mode parity` section in `docs/CROSSCHECK.md` with an explicit sentence "Python is canonical; browser and Colab are demo tier." Hub: keep the existing manifesto link; optionally append "Parity matrix" pointing at `#run-mode-parity`. A separate `docs/CROSSCHECK_PARITY.md` is allowed by discretion but splits the only Crosscheck doc the hub already cites.

**New protocol row (if Rank 1):** JS no, Colab no, CI grep no, RESULT `INCONCLUSIVE` + exit 0, hub label "Run repro".
</parity_matrix_facts>

<gitignore_and_promote>
## Drafts, gitignore, promote

| Question | Answer | Provenance |
|----------|--------|------------|
| Is `drafts/crosscheck/` gitignored? | **No.** Only `drafts/wave_factory/` is. | [VERIFIED: `.gitignore` line 43] |
| Does `drafts/crosscheck/` exist in tree? | **No** (not listed under `drafts/`). Generator creates it on `--write`. | [VERIFIED: `drafts/` listing] |
| Promote script? | **None** for Crosscheck. Wave Factory: `scripts/harvesters/promote_wave_factory_batch.py`. Manifesto: "drafts stay in `drafts/crosscheck/` until a human promotes them … via PR." | [VERIFIED: repo-wide promote grep + `docs/CROSSCHECK.md`] |
| Schema scan of drafts? | **No.** `validate_schemas.py` only `protocols-catalog/**/p-b-*.yaml`. | [VERIFIED] |
| D-08 planning choice | Generate locally; promote filled YAML; **do not commit TODO drafts**. Optionally add `drafts/crosscheck/` to `.gitignore` (parallel to wave_factory — not a fight). Do not touch `drafts/wave_factory/` ignore. | [ASSUMED recommendation] |

`docs/CROSSCHECK.md` "Contributing" currently says promote after filling `experimental_design` and `falsifiable_prediction` — **incomplete vs D-02** (also `null_hypothesis`, `statistical_analysis_plan`, honest design). 03-01 should update that paragraph with the exact `--bridge` command and output path.
</gitignore_and_promote>

<open_questions>
## Open Questions (RESOLVED)

Locked into `03-CONTEXT.md` D-10–D-17 on 2026-08-26 by the plan-phase orchestrator.

Resolved in this research:

1. **Does a Crosscheck promote script exist?** No. Manual copy + PR.
2. **Is `drafts/crosscheck/` gitignored?** No.
3. **Does the generator skip existing files?** Yes, by destination path.
4. **Will schema reject TODO drafts?** No — TODOs are in optional fields. Human filling is a process gate, not a schema gate.
5. **Where is the hub Crosscheck section rendered?** Static `#crosscheck` section in `dashboard/index.html`; cards between `@hub-crosscheck-grid-*` via `render_crosscheck_hub.py`. Manifesto link already present.
6. **ASVS?** Mostly N/A. Integrity = no false CONFIRMED, no auto-promote, no clinical data in git.

Remaining items locked D-10–D-17:

1. **Which new bridge?** RESOLVED D-10: `b-percolation-oncology` opp 1 → `p-b-percolation-oncology-gcc`.
2. **Generator id vs rename?** RESOLVED D-10: rename on promote; `pollination_index: 1`.
3. **Parity file?** RESOLVED D-11: section in `docs/CROSSCHECK.md`.
4. **Exit-code honesty in index generator?** RESOLVED D-15: yes, one-line fix + habitat FSS README.
5. **Gitignore drafts/crosscheck?** RESOLVED D-12: yes.
6. **Promoted status?** RESOLVED D-13: `ready`; never `confirmed`.
7. **Thin stdlib vs README-only?** RESOLVED D-14: stdlib `RESULT: INCONCLUSIVE`, exit 0.
8. **repo_smoke for generator?** RESOLVED D-16: skip this phase.
</open_questions>

<sources>
## Sources

### Primary (HIGH confidence)
- [VERIFIED: `scripts/generate_crosscheck.py`] — CLI, `DRAFTS_DIR`, skip-if-exists, `build_protocol` TODOs, `infer_feasibility` keywords
- [VERIFIED: `schemas/protocol.yaml`] — required fields, status enum, `additionalProperties: false`
- [VERIFIED: `scripts/validate_schemas.py`] — catalog glob only
- [VERIFIED: `scripts/build_crosscheck.py`] — `--apply` / `--check`, hub-grid snapshot, explainer union
- [VERIFIED: `scripts/render_crosscheck_hub.py`] — markers, `run_mode` links
- [VERIFIED: `scripts/crosscheck_browser.py`] — `BROWSER_RUNNERS`, Colab notebook name
- [VERIFIED: `scripts/generate_repro_index_pages.py`] — stale exit-code 1 sentence
- [VERIFIED: `.github/workflows/crosscheck-repro.yml`] — four CONFIRMED greps; path filters
- [VERIFIED: `.gitignore`] — `drafts/wave_factory/` only
- [VERIFIED: `docs/CROSSCHECK.md`] — generate/promote loop; internal Phase 3/4 numbering
- [VERIFIED: `protocols-catalog/`] — four seed YAML only
- [VERIFIED: four `repro/*/`] scripts, JS, README, epidemic notebook
- [VERIFIED: `dashboard/index.html` `#crosscheck` + markers]
- [VERIFIED: dry-run generator on oncology, polymer, island biogeography, rumor]
- [VERIFIED: `.planning/REQUIREMENTS.md` CROSS-06/07; `ROADMAP.md` 03-01/03-02; `03-CONTEXT.md` D-01–D-09]
- [VERIFIED: `.planning/phases/02-epidemic-fss-precision/02-03-SUMMARY.md`] — YAML honesty, Colab clone-and-run, `--apply`, habitat/cluster/Ising left `executed`

### Secondary (MEDIUM confidence)
- [VERIFIED: habitat `b-habitat-percolation-ecology.yaml` opportunity 3 names oncology + epidemiology toolkit] — supports Rank 1 without implementing manifesto Phase 4
- [ASSUMED: human-renamed protocol id is acceptable] — schema allows any `p-b-[a-z0-9.-]+`; seeds already diverge from generator slugs (those four were never generator leftovers in catalog)

### Tertiary (LOW confidence — needs validation during implement)
- Exact wall-clock of a tiny oncology GCC demo (keep L small; must not become an FSS campaign)
- Whether `audit_quality.py` flags `[DRAFT]` titles if someone promotes without renaming (run it)
</sources>

<metadata>
## Metadata

**Research scope:**
- Core technology: USDR Crosscheck generator + catalog + static hub + repro RESULT contract
- Ecosystem: PyYAML, jsonschema, stdlib percolation, GitHub Actions greps, MkDocs
- Patterns: skip-if-exists drafts, human promote, `--apply/--check`, Python-canonical vs demo tier
- Pitfalls: TODO-optional schema, feasibility heuristic, stale exit-code docs, CI path retrigger, manifesto numbering collision

**Confidence breakdown:**
- Standard stack: HIGH — already in repo; no new libraries
- Architecture: HIGH — read full generator, build, hub, CI, schema
- Pitfalls: HIGH — verified skip-if-exists, schema optionality, gitignore, stale README/index
- Bridge ranking: MEDIUM — three candidates verified; owner may prefer polymer's exact p_c
- Code examples: HIGH — copied from in-repo sources

**Research date:** 2026-08-26
**Valid until:** 2026-09-25 (30 days — repo-local pipeline; re-verify if catalog or generator changes)

**Cursor rules in scope (do not implement in research, planner must honor):**
- `.cursor/rules/documentation-and-dashboard.mdc` — CHANGELOG Unreleased, `docs/CROSSCHECK.md`, hub link, `mkdocs build --strict`, optional consultant handoff
- `.cursor/rules/science-discovery-core.mdc` — no fabricated claims/DOIs
- `.cursor/rules/agent-execution.mdc` — run generator/validate in-environment during implement
- `.cursor/rules/usdr-key-documents.mdc` — stale vs GSD v1.1 (discovery/marketing); **GSD `PROJECT.md` Ship Bar and CONTEXT D-09 win** (no marketing)
</metadata>

---

*Phase: 03-crosscheck-scale-up*
*Research completed: 2026-08-26*
*Ready for planning: yes*

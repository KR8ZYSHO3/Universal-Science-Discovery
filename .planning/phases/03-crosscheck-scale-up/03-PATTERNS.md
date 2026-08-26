# Phase 3 Pattern Map

Repeat the **existing** Crosscheck pipeline for a **non-seed** bridge. Do not invent a fifth CONFIRMED trophy, a promote CLI, or a JS runner for networkx.

Canonical generate path: `scripts/generate_crosscheck.py` → `drafts/crosscheck/` → human-edited YAML in `protocols-catalog/` → `repro/<protocol-id>/`. Canonical catalog analog: `protocols-catalog/physics-ecology/p-b-habitat-percolation-ecology-fss.yaml` (schema-complete, TODOs filled). Canonical RESULT/README analog: `repro/p-b-ising-social-dynamics-ewi/` (exit 0 always). Canonical demo-tier analog: `scripts/crosscheck_browser.py` + epidemic Colab (no JS). Artifact regen: `scripts/build_crosscheck.py --apply` then `--check`.

Habitat already has two protocols — it does **not** count as the new bridge (D-01). Epidemic freeze (`NU_THEORY = 3.0`, constants) is frozen (D-07). A fifth `grep RESULT: CONFIRMED` job is Phase 4 TRUST-02, not this phase (D-03).

---

## File Classification

| Target file | Role | Analog file | What to copy |
|---|---|---|---|
| `docs/CROSSCHECK.md` | Manifesto + happy-path docs (D-01, D-05, D-06) | Same file (Quick start / Protocol catalog / Contributing) | Document **exact** `python scripts/generate_crosscheck.py --bridge <new-id> --write` and output path under `drafts/crosscheck/<domain-pair>/`. Do **not** document `--all` as the happy path. Add a **parity matrix** covering all **four seeds** plus the new protocol. Add Ising to the catalog table (today lists 3 of 4 seeds). Link Python-as-canonical vs browser/Colab demo. |
| `docs/CROSSCHECK_PARITY.md` (optional; Claude discretion) | Dedicated parity table if `CROSSCHECK.md` would get too long | No existing parity file — closest is the catalog table in `docs/CROSSCHECK.md` plus hub cards | Same columns as D-05. If created, link from `docs/CROSSCHECK.md` and from the hub `section-desc` (one extra `<a>`). Prefer a section in `CROSSCHECK.md` unless the table is large. |
| `scripts/generate_crosscheck.py` | Draft generator — **likely docs-only this phase** | Already the pipeline | Run `--bridge <id> --write` for a bridge with **zero** `protocols-catalog/` files. Do not change skip-if-exists, `--all` behavior, or auto-write to `protocols-catalog/`. Optional: tiny `--dry-run` smoke in pytest (discretion; <30s, no networkx). |
| `drafts/crosscheck/<domain-pair>/p-b-<bridge>-<slug>.yaml` | Generator output (staging) | Path formula in `output_path_for()` | Mirrors `cross-domain/` relative parent. **Not** gitignored (only `drafts/wave_factory/` is). Commit only if human wants the draft in git; promotion copy lives in `protocols-catalog/`. |
| `protocols-catalog/<domain-pair>/p-b-<new-id>.yaml` | Promoted protocol (D-02, D-08) | `protocols-catalog/physics-ecology/p-b-habitat-percolation-ecology-fss.yaml` (field set) + epidemic YAML (honesty of design vs script) | Required schema keys + filled `null_hypothesis` / `statistical_analysis_plan` / honest `experimental_design`. `status: draft` or `ready` (prefer `ready` if design is complete). **Never** `confirmed` unless a local run printed `RESULT: CONFIRMED`. Set `repro_bundle: repro/<id>/`. Directory name should match the bridge’s `cross-domain/` parent (same as generator). |
| `protocols-catalog/README.md` | Status enum for humans | Same file | Status table is already correct. Optionally mention the new protocol; do not add an auto-promote command. |
| `repro/<protocol-id>/` | Runnable bundle (D-03, D-04) | Habitat FSS (stdlib layout) or Ising (README honesty). **Do not** copy epidemic’s 90s networkx sweep | `README.md` + `requirements.txt` + `*.py` that prints `RESULT:` and **`return 0` always**. If science is not a precision pass, print `INCONCLUSIVE` honestly. Stdlib preferred. No JS unless the new protocol is a small lattice demo (D-09: no JS for networkx). |
| `repro/<protocol-id>/README.md` | Human run + honesty | **Ising** README, not habitat FSS README | Bridge relative link; one run command; **“Exit code 0 always; inspect stdout for CONFIRMED vs INCONCLUSIVE.”** Habitat FSS README still claims exit 1 on falsify — **do not copy that lie**. |
| `repro/<protocol-id>/<script>.py` | Canonical Python (source of truth) | Habitat/cluster/Ising `main()` RESULT contract | Header print of protocol id; per-point lines; `RESULT: CONFIRMED` or `RESULT: INCONCLUSIVE (...)`; `return 0`. Do not add this path to `crosscheck-repro.yml` grep unless it actually prints CONFIRMED (out of scope anyway). |
| `repro/<protocol-id>/index.html` | Generated Pages landing | Produced by `scripts/generate_repro_index_pages.py` | **Do not hand-edit.** After YAML + bundle exist: `python scripts/build_crosscheck.py --apply`. Generator currently still says exit 1 = falsified in the HTML — do not “fix” that generator unless in scope; README is the honesty surface for the new bundle. |
| `scripts/crosscheck_browser.py` | Demo-tier registry | Same file `BROWSER_RUNNERS` / `COLAB_NOTEBOOK` | **Do not** add epidemic to JS. Add a JS filename **only** if the new repro ships a stdlib `.js` next to Python. Colab is detected by presence of `run_crosscheck.ipynb` (epidemic pattern). Default `run_mode` without JS/notebook is `"local"`. |
| `scripts/render_crosscheck_hub.py` | Hub grid injection | Same file; markers in `dashboard/index.html` | Cards auto-include any catalog YAML with `repro_bundle`. After new protocol: `--apply` via `build_crosscheck.py`. Do **not** redesign the dashboard (D-06 / Phase 5). Optional: one manifesto/parity link in the **static** `section-desc` (outside the marker block). |
| `dashboard/index.html` Crosscheck `<section id="crosscheck">` | Human surface | Existing section + `@hub-crosscheck-grid-*` markers | Grid body is generated. Static intro already links `docs/CROSSCHECK.md`. If parity lives only in docs, that link is enough; do not add a new hub widget. |
| `scripts/build_crosscheck.py` | Regen + drift gate (D-06) | Same file `--apply` / `--check` | Order: `generate_repro_index_pages.py` → `render_crosscheck_hub.py --apply` → `generate_explainers.py <bridge-ids>`. Globs `protocols-catalog/**/p-b-*.yaml`. `--check` snapshots repro `index.html`, explainers, and hub marker block, then restores on drift. **Does not read `RESULT:`.** |
| `scripts/generate_explainers.py` | Bridge explainer `#crosscheck` cards | `load_protocols_by_bridge()` / `format_crosscheck_protocols()` | Auto-picks up new YAML via `source_bridge`. `build_crosscheck.py` already adds every catalog `source_bridge` to explainer IDs. No hand-edit of `dashboard/explainers/*.html`. |
| `tests/repo_smoke/test_crosscheck_artifacts.py` | Drift gate in pytest | Same file | Unchanged: subprocess `build_crosscheck.py --check`. After `--apply`, this stays green. |
| `tests/repo_smoke/test_crosscheck_repro_regression.py` | Frozen-input fit pins | Habitat/Ising/epidemic tests in that file | **Do not** add a live Monte Carlo. Optional pin only if the new script has a pure `fit_*` on fixed arrays. Cluster’s live `collect_pooled_sizes()` is the anti-pattern for a “fast” smoke. |
| `tests/repo_smoke/test_generate_crosscheck.py` (maybe) | Fast CLI dry-run (discretion) | **No analog** — closest is subprocess style of `test_crosscheck_artifacts.py` | `python scripts/generate_crosscheck.py --bridge <seed-or-new> --dry-run`; assert exit 0 and a `p-b-` id on stdout. Must be <30s, no networkx, no `--write` into the worktree (or write then delete). TRUST-03 is Phase 4. |
| `.github/workflows/crosscheck-repro.yml` | CI CONFIRMED greps | Four existing seed jobs | **Do not add a fifth CONFIRMED grep** (D-03). Path filters already include `repro/**` and `protocols-catalog/**`. New bundle may run locally only. |
| `schemas/protocol.yaml` | Required/optional fields | Same schema | Do not extend schema this phase. New YAML must pass `python scripts/validate_schemas.py` (`p-b-*.yaml` + `source_bridge` must exist in `cross-domain/`). |
| `CHANGELOG.md` / `README.md` / `.planning/STATE.md` | Docs deliverable | Existing Crosscheck mentions in README / `docs/CROSSCHECK.md` | After merge-worthy work: Unreleased changelog, catalog table, STATE. Not a new generator. |

---

## Analog excerpts

### 1. Seed protocol YAML — required schema vs generator TODOs

**Schema required** (`schemas/protocol.yaml`): `id`, `title`, `status`, `source_bridge`, `falsifiable_prediction`, `experimental_design` (≥3 steps), `feasibility_tier`.

**Optional but expected on promote (D-02):** `null_hypothesis`, `statistical_analysis_plan`, `repro_bundle`, `pollination_index`, `translation_mapping`, `source_hypothesis` / `source_unknown`, `estimated_runtime`, `last_reviewed`, `references`.

Generator `build_protocol()` already emits a schema-shaped draft with TODOs:

```python
# scripts/generate_crosscheck.py — do not auto-promote this object
"status": "draft",
"falsifiable_prediction": opportunity.strip(),
"null_hypothesis": "TODO: state what outcome would refute the bridge mapping",
"experimental_design": default_experimental_design(...),  # 5 generic steps
"statistical_analysis_plan": "TODO: specify test statistic and acceptance criteria",
"feasibility_tier": infer_feasibility(opportunity),
"last_reviewed": "2026-06-21",
```

Happy path (D-01): **single bridge**, not `--all`:

```bash
python scripts/generate_crosscheck.py --bridge b-habitat-percolation-ecology --dry-run
python scripts/generate_crosscheck.py --bridge <NEW_BRIDGE_ID> --write
```

Writes `drafts/crosscheck/<cross-domain-parent>/<protocol_id>.yaml`; skips if the file exists. `--write` never touches `protocols-catalog/`.

**Copy this field layout** from habitat FSS (promoted, TODOs gone). Status is `executed` even though CI greps CONFIRMED — Phase 2 left habitat/cluster/Ising at `executed` and only epidemic at `confirmed` after a real stdout CONFIRMED.

```yaml
# protocols-catalog/physics-ecology/p-b-habitat-percolation-ecology-fss.yaml
id: p-b-habitat-percolation-ecology-fss
status: executed
source_bridge: b-habitat-percolation-ecology
source_hypothesis: h-habitat-percolation-critical-density
source_unknown: u-habitat-fragmentation-threshold
pollination_index: 0
falsifiable_prediction: >
  Monte Carlo estimates of the site percolation threshold ...
null_hypothesis: >
  Threshold estimates are independent of lattice size ...
experimental_design:
  - Run site percolation Monte Carlo on L×L square lattices ...
statistical_analysis_plan: >
  Log-linear fit of (p_c(L) - p_c_inf) vs L with fixed p_c_inf = 0.59274621;
feasibility_tier: desktop
repro_bundle: repro/p-b-habitat-percolation-ecology-fss/
```

Epidemic YAML is the **honesty** analog when a script exists: `experimental_design` / runtime / RESULT contract must match the Python, including `Exit code is always 0`. Copy that discipline, not `status: confirmed`.

Catalog README status enum (do not invent new statuses):

| Status | Meaning |
|--------|---------|
| `draft` | Auto-generated or incomplete — not yet promoted |
| `ready` | Human-reviewed, runnable |
| `executed` | Repro bundle has been run |
| `confirmed` | Results support the falsifiable prediction |
| `falsified` | Results refute the falsifiable prediction |

---

### 2. RESULT print contract (stdout token; exit 0)

Python is canonical. CI greps the **substring** `RESULT: CONFIRMED` (not anchored). New Phase 3 scripts must still print a `RESULT:` line even if the token is `INCONCLUSIVE`.

Habitat FSS (`simulate_percolation_fss.py`) — copy this shape:

```python
    print(f"RESULT: {'CONFIRMED' if passed else 'INCONCLUSIVE (increase TRIALS_PER_P for higher precision)'}")
    return 0
```

Cluster (`cluster_size_exponent.py`) — same token; `return 0` on the success path (error paths still `return 1` if the fit cannot run at all — prefer habitat/Ising “always 0” for a thin demo):

```python
    print(f"RESULT: {'CONFIRMED' if passed else 'INCONCLUSIVE (adjust P or L for clearer scaling)'}")
    return 0
```

Ising (`ising_critical_slowing.py`):

```python
    print(f"RESULT: {result}")  # CONFIRMED or INCONCLUSIVE (...)
    return 0
```

Epidemic (`epidemic_percolation_fss.py`) — **do not copy the Monte Carlo**; copy the token + always-0:

```python
    print(
        f"RESULT: {'CONFIRMED' if passed else 'INCONCLUSIVE (increase SEEDS_PER_N for higher precision)'}"
    )
    return 0
```

Do **not** add a new job to `.github/workflows/crosscheck-repro.yml`. Existing four jobs stay as-is (including epidemic freeze).

---

### 3. `BROWSER_RUNNERS` dict vs Colab vs local

File: `scripts/crosscheck_browser.py`

```python
BROWSER_RUNNERS: dict[str, str] = {
    "p-b-habitat-percolation-ecology-fss": "simulate_percolation_fss.js",
    "p-b-habitat-percolation-ecology-cluster-exponent": "cluster_size_exponent.js",
    "p-b-ising-social-dynamics-ewi": "ising_critical_slowing.js",
}
COLAB_NOTEBOOK = "run_crosscheck.ipynb"
```

Epidemic is **intentionally absent** from `BROWSER_RUNNERS`. Colab is inferred if `repro/.../run_crosscheck.ipynb` exists. `run_mode()`: browser → colab → `"local"`.

JS files are **demo budget**, not canonical (D-05):

- Habitat FSS JS: `TRIALS_PER_P = 120` vs Python `350`
- Cluster JS: `L = 128` vs Python `256`
- Ising JS: `LATTICE_SIZE = 32` vs Python `48`

Hub + explainer + repro `index.html` all call this registry. After any YAML/`BROWSER_RUNNERS` change: `python scripts/build_crosscheck.py --apply`.

Parity matrix columns (D-05) — **does not exist yet**; populate from this inventory:

| protocol id | Python canonical | browser JS | Colab | CI grep CONFIRMED | RESULT contract |
|---|---|---|---|---|---|
| `p-b-habitat-percolation-ecology-fss` | `simulate_percolation_fss.py` | yes, `simulate_percolation_fss.js` (lighter) | no | yes | `RESULT:` + Python `return 0` (README currently lies about exit 1) |
| `p-b-habitat-percolation-ecology-cluster-exponent` | `cluster_size_exponent.py` | yes, `cluster_size_exponent.js` (lighter) | no | yes | `RESULT:` + `return 0` on fit path |
| `p-b-ising-social-dynamics-ewi` | `ising_critical_slowing.py` | yes, `ising_critical_slowing.js` (lighter) | no | yes | `RESULT:` + `return 0` always |
| `p-b-percolation-epidemiology-fss` | `epidemic_percolation_fss.py` | **no** | yes, `run_crosscheck.ipynb` | yes | `RESULT:` + `return 0` always |
| *(new protocol)* | new `.py` | no unless stdlib JS | no unless notebook | **no** (Phase 4) | `RESULT:` + `return 0` always |

State explicitly: **Python is canonical; browser/Colab are demo tier.**

---

### 4. `--apply` / `--check` (hub + landings + explainers)

`scripts/build_crosscheck.py` is the only regen entry point to copy:

```python
steps = [
    [py, str(SCRIPTS / "generate_repro_index_pages.py")],
    [py, str(SCRIPTS / "render_crosscheck_hub.py"), "--apply"],
    [py, str(SCRIPTS / "generate_explainers.py"), *bridge_ids],
]
```

Catalog glob (new YAML must match):

```python
for path in sorted(CATALOG.rglob("p-b-*.yaml")):
    ...
    bundle = str(data.get("repro_bundle", "")).strip().rstrip("/")
```

Protocols **without** `repro_bundle` do **not** appear in hub cards or repro `index.html`. Promote + bundle together (D-03).

`--check` diffs those artifacts and the marker block:

```html
        <!-- @hub-crosscheck-grid-begin -->
        ...cards...
        <!-- @hub-crosscheck-grid-end -->
```

Usage after YAML/hub edits:

```bash
python scripts/build_crosscheck.py --apply
python scripts/build_crosscheck.py --check
python scripts/validate_schemas.py
```

Pytest analog (do not rewrite):

```python
# tests/repo_smoke/test_crosscheck_artifacts.py
cmd = [sys.executable, str(REPO_ROOT / "scripts" / "build_crosscheck.py"), "--check"]
```

`render_crosscheck_hub.py` without `--apply` is dry-run (prints count, no write). `build_crosscheck.py` always passes `--apply` to the hub renderer even in `--check` (snapshot/restore).

Do not hand-edit `dashboard/explainers/*.html` or `repro/*/index.html`.

---

### 5. README honesty (exit 0 always)

**Copy Ising / epidemic, not habitat FSS README.**

Ising (`repro/p-b-ising-social-dynamics-ewi/README.md`):

```markdown
```bash
python ising_critical_slowing.py
```

Exit code 0 always; inspect stdout for CONFIRMED vs INCONCLUSIVE.
```

Epidemic (`repro/p-b-percolation-epidemiology-fss/README.md`):

```markdown
Exit code 0 always; inspect stdout for CONFIRMED vs INCONCLUSIVE.

Demo tier is Google Colab (`run_crosscheck.ipynb`) ... There is no in-browser JS runner.
```

**Anti-pattern** — habitat FSS README (Python still `return 0`):

```markdown
Exit code 0 = falsifiable prediction within tolerance; 1 = falsified.
```

Cluster README has **no** exit-code sentence — incomplete analog.

Repro layout to copy (stdlib):

```
repro/p-b-your-protocol-id/
├── README.md
├── requirements.txt    # habitat: "# No external dependencies — stdlib only"
└── your_script.py
```

`docs/CROSSCHECK.md` Contributing section already documents this tree and `repro_bundle: repro/p-b-your-protocol-id/`.

Thin demo vs epidemic: D-04 forbids copying epidemic’s ~90s `SEEDS_PER_N=20` / N up to 5000 networkx sweep. Prefer a short stdlib script or YAML + documented `python -c` smoke.

---

### 6. Human promote (no Crosscheck promote CLI)

Manifesto loop (`docs/CROSSCHECK.md`):

```
Bridge → generate_crosscheck.py → drafts/crosscheck → human PR review → protocols-catalog → repro bundle
```

> Same governance as Wave Factory: automation proposes, humans merge.

Promote is **copy + fill TODOs + PR**, not a script. Wave Factory `scripts/harvesters/promote_wave_factory_batch.py --apply` is **not** an analog to reuse: it moves harvest triples into `cross-domain/` / `unknowns-catalog/` / `hypotheses/` and has no protocol schema.

`.gitignore` gitignores `drafts/wave_factory/` only. `drafts/crosscheck/` is currently **absent** on disk and **not** gitignored — generator creates it on `--write`. Do not fight Wave Factory ignore patterns (D-08).

---

## Shared Patterns

- **Python is canonical.** Browser JS (lighter trial/L) and Colab (`run_crosscheck.ipynb` clones and runs the same `.py`) are demo tier. Document that in the parity matrix (D-05).
- **Human promote gate.** Generator writes `drafts/crosscheck/` with `status: draft` and TODOs. Humans fill `null_hypothesis` / `statistical_analysis_plan` / real `experimental_design` and merge into `protocols-catalog/`. No auto-move into the catalog.
- **No auto-confirmed.** Schema allows `confirmed`, but D-02: do not set it unless a real local run printed `RESULT: CONFIRMED`. Prefer `ready` or `executed`. Epidemic is the only catalog `confirmed` today; habitat/cluster/Ising remain `executed` despite CI greps.
- **`RESULT:` stdout + exit 0.** Decision lives in the printed token. Do not use process exit as confirmed/falsified. Do not add a fifth CI grep this phase.
- **Hub is generated.** Any promoted YAML with `repro_bundle` appears in hub cards, explainer `#crosscheck`, and Pages landing after `build_crosscheck.py --apply`. `--check` is the drift gate (`CROSS-05` already shipped).
- **Schema validation** on `protocols-catalog/**/p-b-*.yaml` only (not drafts). `source_bridge` must exist in `cross-domain/`.
- **Stdlib first.** Habitat/cluster/Ising: `# No external dependencies`. Epidemic `networkx>=3.0` is the exception, frozen, no JS (D-09).
- **Docs honesty:** YAML design, README, and script must agree (Phase 2 02-03 pattern). Do not claim CONFIRMED or exit-1-on-falsify if the script always returns 0 / prints INCONCLUSIVE.
- **Not a trophy hunt.** New bridge may ship `INCONCLUSIVE` honestly. Do not start another FSS/exponent precision campaign.

---

## No Analog Found

| Gap | Notes for planning |
|---|---|
| **Crosscheck promote CLI** | Missing. Promote is a documented human copy/PR. Do **not** build `promote_crosscheck.py` this phase (would blur the human gate). Closest existing CLI (`promote_wave_factory_batch.py`) is a different catalog and must not be wired to protocols. |
| **Parity matrix** | Missing as a first-class doc. Four seeds are only implied by hub cards + `BROWSER_RUNNERS` + CI YAML. Phase 3 must **author** the table (D-05) in `docs/CROSSCHECK.md` and/or `docs/CROSSCHECK_PARITY.md`, covering habitat FSS, cluster exponent, Ising EWI, epidemic FSS, then the new protocol. Surface from hub via existing manifesto link (optional extra sentence). Do not invent a dashboard widget. |
| **`generate_crosscheck.py` smoke test** | No `tests/` reference. Discretion: a **fast** `--dry-run` subprocess (<30s, no networkx) is nice-to-have; TRUST-03 is Phase 4. Do not run `--all`. |
| **`drafts/crosscheck/` tree** | Not in repo yet. First `--write` creates it. Decide in plan whether to commit the draft YAML or only the promoted catalog copy. |
| **Ising row in `docs/CROSSCHECK.md` catalog table** | Hub has four cards; manifesto table lists three. Parity work should include Ising. |
| **Habitat FSS README / generated `index.html` exit-code lie** | Known honesty bug. Out of scope unless touching those files; **do not copy**. New README uses Ising wording. Generated landings still say exit 1 = falsified (`generate_repro_index_pages.py`) — fixing the generator is optional and not required for CROSS-06/07. |
| **JS runner for the new protocol** | Only exists for three stdlib lattice repros. No analog for a local-only or networkx protocol except epidemic Colab. Default: omit JS. |

---

## Pipeline recap (copy this order in 03-01 / 03-02)

1. Pick a bridge **other than** habitat / epidemic / Ising seeds that currently has **zero** `protocols-catalog/` files (prefer desktop-tier percolation/Ising-like opportunity — Claude discretion).
2. `python scripts/generate_crosscheck.py --bridge <id> --write`
3. Human-edit TODOs; copy into `protocols-catalog/<domain-pair>/`; `status: ready` (or `draft`); never auto-`confirmed`.
4. Add `repro/<protocol-id>/` with RESULT printer, exit 0, honest README.
5. `python scripts/validate_schemas.py`
6. `python scripts/build_crosscheck.py --apply` && `--check`
7. Author parity matrix for **all four seeds** + new protocol; link from `docs/CROSSCHECK.md` / hub manifesto line.
8. Do not touch epidemic freeze constants; do not add CI CONFIRMED grep; do not redesign the dashboard.

---

## PATTERN MAPPING COMPLETE

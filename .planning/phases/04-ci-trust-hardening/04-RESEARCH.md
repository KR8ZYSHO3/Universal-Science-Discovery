# Phase 4: CI & trust hardening - Research

**Researched:** 2026-08-26
**Domain:** GitHub Actions CONFIRMED gates + pytest repo_smoke for Crosscheck entry points
**Confidence:** HIGH

<user_constraints>
## User Constraints (from CONTEXT.md)

**CRITICAL:** If CONTEXT.md exists from /gsd-discuss-phase, copy locked decisions here verbatim. These MUST be honored by the planner.

### Locked Decisions

- **D-01 (TRUST-02 gate token):** Gate **stdout** `RESULT: CONFIRMED`, not YAML `status: confirmed`. Today habitat FSS, cluster exponent, and Ising YAML remain `status: executed` while their Python prints `RESULT: CONFIRMED`. Epidemic YAML is `confirmed`. Oncology GCC YAML is `ready` and prints `INCONCLUSIVE`. Do **not** mass-edit YAML status as a unification stunt.
- **D-02 (keep the four greps):** `crosscheck-repro.yml` already tees+greps `RESULT: CONFIRMED` for habitat FSS, cluster exponent, epidemic FSS, and Ising EWI. Keep all four. Do not drop epidemic. Do not replace live CI runs of those four with pytest-only pins.
- **D-03 (no fake fifth CONFIRMED):** `repro/p-b-percolation-oncology-gcc/giant_component_fraction.py` always prints `RESULT: INCONCLUSIVE` and exits 0. **Never** add `grep -q "RESULT: CONFIRMED"` for GCC. If GCC is run in CI or pytest, assert `RESULT: INCONCLUSIVE` and exit code 0.
- **D-04 (unified means inventory, not a trophy):** TRUST-02 “unified CONFIRMED gates” means a **maintainable mapping** so a future CONFIRMED protocol cannot silently skip CI. Researcher/planner pick the mechanism (workflow matrix from a checked-in list, a small Python inventory check in repo_smoke that diffs catalog/repro vs the workflow YAML, or both). The inventory must treat **expected stdout token** as the source of truth, not YAML `status`.
- **D-05 (epidemic freeze):** Do not change `epidemic_percolation_fss.py` constants, freeze `mean_pcs` in `test_epidemic_fss_fit_confirmed_on_reference_pcs`, or `NU_THEORY = 3.0`. No live NetworkX / ER Monte Carlo in pytest. Do not shop a prettier R².
- **D-06 (TRUST-03 epidemic):** Epidemic freeze pytest **already exists** in `tests/repo_smoke/test_crosscheck_repro_regression.py`. Do not duplicate it. TRUST-03 “covers epidemic” is closed by keeping that test and asserting `NU_THEORY == 3.0` still holds.
- **D-07 (TRUST-03 generate_crosscheck):** Add a **fast** repo_smoke for `scripts/generate_crosscheck.py`. Happy path: `--bridge b-percolation-oncology --dry-run` (or another existing bridge). Assert exit 0 and a `p-b-` id on stdout. **No `--write`** (must not dirty the worktree). No networkx. Must stay well under 30s.
- **D-08 (TRUST-03 GCC entry point):** Add repo_smoke for `giant_component_fraction.py`. Prefer actually running the stdlib script (L=32, TRIALS=8 is cheap) and asserting `RESULT: INCONCLUSIVE` plus exit 0. Do not add a fake freeze-fit of CONFIRMED numbers. Do not copy cluster’s live `collect_pooled_sizes()` anti-pattern into new tests.
- **D-09 (where tests run):** New pytest lives in `tests/repo_smoke/` and is picked up automatically by `.github/workflows/validate-schemas.yml` (`python -m pytest tests/repo_smoke -v`). Do **not** duplicate the pytest bundle inside `crosscheck-repro.yml`.
- **D-10 (workflow path filters):** `crosscheck-repro.yml` currently triggers on `repro/**`, `protocols-catalog/**`, and Crosscheck build scripts — **not** `tests/repo_smoke/**`. That is OK for CONFIRMED greps. If 04-01 adds a helper script used by the workflow, include that script in the workflow `paths:` list. Do not add `generate_crosscheck.py` as a fifth CONFIRMED job.
- **D-11 (honesty docs):** Update `docs/CROSSCHECK.md` (parity / CI column) so it states CONFIRMED-only grep policy: four seeds grepped CONFIRMED; GCC is INCONCLUSIVE and must not be grepped CONFIRMED. After any hub HTML change: `python scripts/build_crosscheck.py --apply` then `--check`. Prefer docs-only if the hub already links the manifesto.
- **D-12:** No marketing, DNS, arXiv, catalog waves, JS runners, promote CLI, or Phase 5 recommendations.
- **D-13:** No fabricated `RESULT: CONFIRMED`. GSD artifacts are process metadata, not scientific evidence.
- **D-14:** ROADMAP plan split: **04-01** unified CONFIRMED gates in CI (TRUST-02); **04-02** repo_smoke expansion (TRUST-03). They may run as independent waves if they do not share files; if both edit `docs/CROSSCHECK.md`, serialize that file to one plan or one trailing docs task.

### Claude's Discretion

- Exact TRUST-02 inventory mechanism (matrix job vs pytest that parses `.github/workflows/crosscheck-repro.yml` vs a tiny `scripts/` helper). Prefer the smallest change that fails CI when a CONFIRMED stdout protocol is missing from the workflow.
- Whether GCC also runs as a named step in `crosscheck-repro.yml` (INCONCLUSIVE grep) **in addition to** pytest, or pytest-only.
- Which `--bridge` id the generate dry-run uses.
- Whether 04-01 and 04-02 are parallel Wave 1 or sequential.

### Deferred Ideas (OUT OF SCOPE)

- Feeding execution results YAML back into hypothesis validation (`docs/CROSSCHECK.md` internal “Phase 3”)
- Unified percolation toolkit (`docs/CROSSCHECK.md` internal “Phase 4”)
- HUB-01 smart recommendations (GSD Phase 5)
- In-browser JS for epidemic FSS
- Raising epidemic freeze R² / retuning `SEEDS_PER_N`
- Changing habitat / cluster / Ising YAML `status` from `executed` to `confirmed`
</user_constraints>

## Project Constraints (from .cursor/rules/)

Treat these with the same authority as locked decisions. Do not plan work that contradicts them.

- **Claims vs process:** Do not fabricate citations or `RESULT: CONFIRMED`. Label speculation. GSD artifacts are not scientific evidence. [VERIFIED: `.cursor/rules/science-discovery-core.mdc`, CONTEXT D-13]
- **Docs with the change:** Merge-worthy CI/workflow work updates `CHANGELOG.md` Unreleased and the honesty surface in `docs/CROSSCHECK.md` (D-11). Update `README.md` / `docs/DOC_MAP.md` / `docs/REPOSITORY_MANIFEST.md` only if paths or user-visible commands change. [VERIFIED: `.cursor/rules/documentation-and-dashboard.mdc`]
- **Hub:** Prefer docs-only. Hub already links the manifesto and `#run-mode-parity`. If `dashboard/index.html` is untouched, do **not** run `build_crosscheck.py --apply`. If hub HTML *is* edited: `--apply` then `--check`. [VERIFIED: `dashboard/index.html` lines 1883–1884; CONTEXT D-11]
- **MkDocs:** Any `docs/` or `mkdocs.yml` edit requires `mkdocs build --strict`. [VERIFIED: `.cursor/rules/documentation-and-dashboard.mdc`, `CONTRIBUTING.md`]
- **Run checks in-environment:** `python -m pytest tests/repo_smoke` and `python scripts/validate_schemas.py`; do not hand the user a runbook instead of executing. [VERIFIED: `.cursor/rules/agent-execution.mdc`, `CONTRIBUTING.md`]
- **Stale rule conflict:** `.cursor/rules/usdr-key-documents.mdc` “Current focus (2026-05-09)” still lists arXiv/outreach. That is **v1.2 Launch**, parked. Honor CONTEXT D-12 / GSD ROADMAP, not that stale marketing block.

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| **TRUST-02** | All CONFIRMED protocols gated in `crosscheck-repro.yml` | Four live `tee`+`grep -q "RESULT: CONFIRMED"` steps already exist. Close the requirement with a **repo_smoke inventory** that diffs CONFIRMED-capable `repro/**/*.py` (stdout-token heuristic, **not** YAML `status`) against those steps so a fifth CONFIRMED script cannot skip CI. Do not rewrite the workflow into a matrix. Do not grep GCC CONFIRMED. |
| **TRUST-03** | Additional repo_smoke tests for epidemic + script entry points | Epidemic freeze already exists (`test_epidemic_fss_fit_confirmed_on_reference_pcs`, `NU_THEORY == 3.0`) — keep, do not duplicate. Add `--dry-run` smoke for `generate_crosscheck.py` (`--bridge b-percolation-oncology`) and a live stdlib run of `giant_component_fraction.py` asserting `RESULT: INCONCLUSIVE` + exit 0. New tests live only in `tests/repo_smoke/` (picked up by `validate-schemas.yml`). |

ROADMAP success criteria: (1) all CONFIRMED protocols gated in the crosscheck-repro workflow; (2) repo_smoke covers epidemic + any new script entry points. Plans: **04-01** Unified CONFIRMED gates in CI; **04-02** repo_smoke expansion. [VERIFIED: `.planning/REQUIREMENTS.md`, `.planning/ROADMAP.md`]
</phase_requirements>

<research_summary>
## Summary

Phase 4 is a **fail-closed mapping + smoke** phase, not a fifth CONFIRMED trophy and not a catalog-status cleanup. Today the four seed scripts are already grepped live in `.github/workflows/crosscheck-repro.yml`. Habitat / cluster / Ising YAML is still `status: executed` while those scripts can print `RESULT: CONFIRMED`; epidemic YAML is `confirmed`; oncology GCC is `ready` and always prints `INCONCLUSIVE`. Any inventory that keys off YAML `status` would **drop three of four seeds** and is forbidden (D-01).

The smallest change that fails CI when a future CONFIRMED-stdout protocol is missing from the workflow is a **new pytest in `tests/repo_smoke/`** that (1) discovers CONFIRMED-capable `repro/**/*.py` via source markers, (2) requires each discovered script path to appear in `crosscheck-repro.yml` in a step that also contains `grep -q "RESULT: CONFIRMED"`, and (3) requires the CONFIRMED-grep count to equal the discovered count. Parse the workflow as **text**, not `yaml.safe_load` — PyYAML 1.1 turns the top-level `on:` key into `True`. Do **not** convert the four jobs to an Actions matrix, do **not** add a `scripts/` helper, and do **not** add GCC as a fifth CONFIRMED grep. GCC belongs in **pytest-only** (`validate-schemas.yml` already runs the whole `tests/repo_smoke` bundle on every PR to `main`).

**Primary recommendation:** 04-01 = text-parse inventory pytest + CROSSCHECK.md CONFIRMED-only grep policy (docs-only; no hub `--apply`). 04-02 = generate `--bridge b-percolation-oncology --dry-run` smoke + live GCC INCONCLUSIVE/exit-0 smoke in a new test file; keep the existing epidemic freeze test. Sequential waves because both touch `CHANGELOG.md`; `docs/CROSSCHECK.md` is 04-01-only.
</research_summary>

<architectural_responsibility_map>
## Architectural Responsibility Map

This is a **CI + local pytest** phase. There is no Browser/API/CDN work. Do not invent a backend, a promote CLI, or a hub widget.

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| Live CONFIRMED gates (four seeds) | CI (`crosscheck-repro.yml` `run:` + `grep -q`) | Local Python repro | D-02: keep live Monte Carlo / Ising / FSS runs. Pytest freeze pins are **not** a substitute. [VERIFIED: `.github/workflows/crosscheck-repro.yml`] |
| TRUST-02 inventory (fail if a CONFIRMED-capable script is ungated) | `tests/repo_smoke/` (pytest) | `validate-schemas.yml` (always-on) | Smallest fail-closed mapping. Runs on every PR because `validate-schemas.yml` has **no** path filter. [VERIFIED: `.github/workflows/validate-schemas.yml`] |
| Epidemic TRUST-03 | Existing freeze pytest | Live CI grep (already shipped) | D-05/D-06: keep `NU_THEORY == 3.0`; no live NetworkX in pytest. [VERIFIED: `tests/repo_smoke/test_crosscheck_repro_regression.py`] |
| generate_crosscheck entry point | Local CLI smoke via pytest subprocess | `validate.yml` path filter already lists the script | `--dry-run` only; no `--write`. PyYAML already installed in `validate-schemas.yml`. [VERIFIED: `scripts/generate_crosscheck.py`, `validate.yml`] |
| GCC entry point | pytest subprocess of stdlib script | — | D-03/D-08: assert `INCONCLUSIVE` + exit 0. Not a `crosscheck-repro.yml` CONFIRMED job. [VERIFIED: `repro/p-b-percolation-oncology-gcc/giant_component_fraction.py`] |
| Honesty / parity CI column | Docs (`docs/CROSSCHECK.md`) | Static hub link (already present) | D-11: docs-only unless hub HTML changes. [VERIFIED: `dashboard/index.html`] |

**Single-product note:** All “runtime” is files in git plus GitHub-hosted runners. Planning must not add servers, reusable-workflow abstraction, or smart-recommendations (HUB-01).
</architectural_responsibility_map>

<standard_stack>
## Standard Stack

Do not add a package, linter, or Actions plugin. Use what CI already installs.

### Core

| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| CPython | 3.11 in `crosscheck-repro.yml`; 3.12 in `validate-schemas.yml` (local 3.12.6) | Repro + pytest | Already the two Actions runtimes. Do not unify versions this phase. [VERIFIED: workflow YAML; `python --version`] |
| pytest | 8.4.2 local; CI `pip install pytest` unpinned | `tests/repo_smoke/` | `pyproject.toml` `[tool.pytest.ini_options] testpaths` already includes `tests/repo_smoke`. [VERIFIED: `pyproject.toml`; `python -m pytest --version`] |
| PyYAML | 6.0.3 local; CI `pip install pyyaml` | `generate_crosscheck.py` import | Generator fails with exit 2 if missing. Already in `validate-schemas.yml`. **Do not** `yaml.safe_load` the workflow file. [VERIFIED: local `yaml.__version__`; PyYAML 1.1 `on:` → `True`] |
| GNU `grep` / `tee` | Ubuntu runner | Live CONFIRMED gate | Existing four steps. Keep verbatim. [VERIFIED: `.github/workflows/crosscheck-repro.yml`] |

### Supporting

| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| jsonschema | `>=4.20` in CI (local 4.23.0) | Catalog validation (already in repo_smoke) | Do not add protocol-status unification. [VERIFIED: `validate-schemas.yml`] |
| networkx | CI `pip install networkx` in `crosscheck-repro.yml` only | Epidemic live Monte Carlo | **Pytest must not import it** (D-05). [VERIFIED: workflow + `test_crosscheck_repro_regression.py`] |
| actions/checkout | `@v7` | Both workflows | Do not drive-by pin SHAs or bump. [VERIFIED: workflow YAML] |
| actions/setup-python | `@v5` in crosscheck-repro; `@v6` in validate-schemas | Python toolchain | Do not unify this phase. [VERIFIED: workflow YAML] |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| **Pytest text inventory (recommended)** | GitHub Actions `strategy.matrix` of `{script, token}` | Matrix would auto-run a new row, but D-02 forbids replacing the four hardcoded greps; rewriting them is larger than one test file; `${{ matrix.script }}` inside `run:` is an extra injection surface. [CITED: docs.github.com script-injections] |
| Pytest text inventory | `scripts/check_crosscheck_gates.py` helper also called from the workflow | Extra CLI + D-10 path-filter chore. Pytest is already the merge gate. |
| Pytest text inventory | `yaml.safe_load(crosscheck-repro.yml)` then walk `jobs.smoke.steps` | **Broken:** PyYAML 1.1 loads `on:` as boolean `True`, so the trigger block is not under `"on"`. Verified this session. |
| Pytest-only GCC | Extra `crosscheck-repro.yml` step grepping `RESULT: INCONCLUSIVE` | Cheap (~0.06s) but duplicates pytest, muddles the workflow’s CONFIRMED-only job, and is not TRUST-02. |
| `--bridge b-percolation-oncology` | `--bridge b-habitat-percolation-ecology` | Habitat is the docs “any bridge” preview. Oncology is the Phase 3 happy path TRUST-03 must cover. |
| `--dry-run` | `--all --dry-run` | Noisy / slower; D-07 wants one bridge. |
| New test files | Append to `test_catalog_regression.py` / `test_crosscheck_repro_regression.py` | Catalog file’s `_run_script` ignores stdout; regression file is freeze-fits. New files keep 04-01/04-02 from colliding. |

**Installation (no new packages):**

```bash
pip install pyyaml "jsonschema>=4.20" pytest
# epidemic live CI only — do not add to new pytest:
# pip install networkx
```

**Version verification:** pytest 8.4.2, PyYAML 6.0.3, jsonschema 4.23.0, CPython 3.12.6 probed this session. CI versions are unpinned except `jsonschema>=4.20`. [VERIFIED: local `python -c` / workflow YAML]
</standard_stack>

<architecture_patterns>
## Architecture Patterns

### System Architecture Diagram

```text
PR / push to main
        |
        +-- validate-schemas.yml  [NO path filter; every PR]
        |         pip: pyyaml jsonschema pytest
        |         python -m pytest tests/repo_smoke -v
        |              |
        |              +-- existing: validate_schemas / domain pages / dashboard / orphans / --check
        |              +-- existing: freeze fits (habitat, Ising, cluster live pooled, epidemic NU_THEORY=3.0)
        |              +-- NEW 04-01: scan repro/**/*.py CONFIRMED markers
        |              |              vs text of .github/workflows/crosscheck-repro.yml
        |              |              FAIL if a CONFIRMED-capable script has no CONFIRMED grep step
        |              |              FAIL if GCC (INCONCLUSIVE-only) is grepped CONFIRMED
        |              +-- NEW 04-02: generate_crosscheck.py --bridge b-percolation-oncology --dry-run
        |              |              assert exit 0 and "p-b-" on stdout; no --write
        |              +-- NEW 04-02: python giant_component_fraction.py
        |                             assert exit 0 and RESULT: INCONCLUSIVE
        |
        +-- crosscheck-repro.yml  [paths: repro/**, protocols-catalog/**, Crosscheck build scripts]
                  pip: networkx
                  Habitat FSS     --> tee /tmp/fss.out      --> grep -q "RESULT: CONFIRMED"
                  Cluster tau     --> tee /tmp/cluster.out  --> grep -q "RESULT: CONFIRMED"
                  Epidemic FSS    --> tee /tmp/epidemic.out --> grep -q "RESULT: CONFIRMED"
                  Ising EWI       --> tee /tmp/ising.out    --> grep -q "RESULT: CONFIRMED"
                  [do not add GCC CONFIRMED grep]
                  [do not add pytest here — D-09]
                  [do not add generate_crosscheck.py as a job — D-10]
```

Decision point: a new `repro/p-b-*/something.py` that contains a CONFIRMED RESULT marker **must** get a fifth live grep step **and** will fail 04-01 inventory until that step exists. A new INCONCLUSIVE-only script (like GCC) must **not** get a CONFIRMED grep; pytest covers the entry point.

### Recommended Project Structure

```
.github/workflows/
  crosscheck-repro.yml          # KEEP four tee+grep steps; no matrix; no GCC CONFIRMED
  validate-schemas.yml          # unchanged; already pytest tests/repo_smoke -v

tests/repo_smoke/
  test_crosscheck_repro_regression.py   # KEEP epidemic freeze; do not duplicate
  test_crosscheck_artifacts.py          # KEEP --check
  test_catalog_regression.py            # KEEP; do not overload _run_script
  test_crosscheck_confirmed_gates.py    # NEW 04-01 inventory
  test_crosscheck_entry_points.py       # NEW 04-02 generate dry-run + GCC subprocess

docs/CROSSCHECK.md              # 04-01 only: CONFIRMED-only grep policy; GCC CI column stays no
CHANGELOG.md                    # Unreleased bullets per plan
```

Do not add `scripts/check_crosscheck_gates.py`. Do not add `repro/CONFIRMED_GATES.yml`.

### Pattern 1: TRUST-02 inventory (text diff, stdout-token source of truth)

**What:** Discover CONFIRMED-capable repro scripts from **source markers**, then require each to be invoked in `crosscheck-repro.yml` in a step that greps `RESULT: CONFIRMED`.
**When to use:** 04-01. This is the whole TRUST-02 mechanism.
**Markers (use these; do not use YAML `status`):**

A `repro/**/*.py` file (skip `__pycache__`) is CONFIRMED-capable if its UTF-8 text contains any of:

- `'CONFIRMED' if` or `"CONFIRMED" if` (habitat / cluster / epidemic f-string)
- `result = "CONFIRMED"` or `result = 'CONFIRMED'` (Ising)
- literal `RESULT: CONFIRMED`

GCC currently matches **none** of these (only `RESULT: INCONCLUSIVE`). [VERIFIED: five repro `*.py` files]

**Pairing rule:** Split the workflow text on step headers (`- name:`). For each discovered script, the relative POSIX path (`repro/p-b-.../file.py`) must appear in a step whose body also contains `grep -q "RESULT: CONFIRMED"`. Assert `workflow.count('grep -q "RESULT: CONFIRMED"') == len(discovered)`. For every repro `*.py` that is **not** CONFIRMED-capable, no step may contain both that script path and a CONFIRMED grep.

**Example (gate to keep, not rewrite):**

```yaml
# Source: .github/workflows/crosscheck-repro.yml
- name: Epidemic percolation FSS (expect CONFIRMED)
  run: |
    python repro/p-b-percolation-epidemiology-fss/epidemic_percolation_fss.py | tee /tmp/epidemic.out
    grep -q "RESULT: CONFIRMED" /tmp/epidemic.out
```

### Pattern 2: TRUST-03 subprocess smokes (list argv, capture stdout)

**What:** Mirror `test_crosscheck_artifacts.py`: `subprocess.run([...], cwd=REPO_ROOT, capture_output=True, text=True, check=False)` then assert returncode and stdout tokens.
**When to use:** generate dry-run and GCC. Do **not** use `test_catalog_regression._run_script` (it throws away stdout). Do **not** `importlib` + `collect_pooled_sizes()`.

```python
# Source: tests/repo_smoke/test_crosscheck_artifacts.py
proc = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True, check=False)
if proc.returncode != 0:
    out = (proc.stdout or "") + (proc.stderr or "")
    raise AssertionError(f"build_crosscheck.py --check failed:\n{out}")
```

Generate command **must** be:

```bash
python scripts/generate_crosscheck.py --bridge b-percolation-oncology --dry-run
```

Assert `returncode == 0` and `"p-b-"` in stdout (this session: three `p-b-percolation-oncology-…` ids; promoted catalog id `p-b-percolation-oncology-gcc` will **not** appear — do not assert that). Never pass `--write`. Never `--all`. [VERIFIED: live `--dry-run` this session]

GCC command:

```bash
python repro/p-b-percolation-oncology-gcc/giant_component_fraction.py
```

Assert `returncode == 0`, `"RESULT: INCONCLUSIVE" in stdout`, and `"RESULT: CONFIRMED" not in stdout`. Timed **0.058s** this session. [VERIFIED]

### Pattern 3: Keep freeze-fits and live greps as two layers

**What:** pytest pins **fit functions** on frozen vectors; CI greps **full script stdout**. Epidemic already has both (02-02).
**When to use:** Always. TRUST-03 epidemic is closed by **not deleting** `test_epidemic_fss_fit_confirmed_on_reference_pcs` and its `assert mod.NU_THEORY == 3.0`.

```python
# Source: tests/repo_smoke/test_crosscheck_repro_regression.py
assert mod.NU_THEORY == 3.0
assert mod.PC_INF == 1.0 / mod.MEAN_DEGREE
nu, r2, sign_ok = mod.fit_nu(mod.SIZES, pcs)
```

### Pattern 4: Docs-only honesty for the CI column

**What:** Edit `docs/CROSSCHECK.md` Run-mode parity so the GCC CI cell is **no** (CONFIRMED-only grep policy), not “no (Phase 4 TRUST-02)” which currently reads like Phase 4 might add a CONFIRMED grep. State explicitly: four seeds grepped CONFIRMED; GCC must not be grepped CONFIRMED.
**When to use:** 04-01. Hub already links `#run-mode-parity` — skip `--apply`. Then `mkdocs build --strict`.

### Anti-Patterns to Avoid

- **YAML `status: confirmed` as the inventory key:** would miss habitat/cluster/Ising (`executed`) and still miss GCC (`ready`). [VERIFIED: five protocol YAML files]
- **Replacing live greps with pytest-only pins:** D-02.
- **`grep -q "RESULT: CONFIRMED"` on GCC:** D-03; script cannot print it.
- **`yaml.safe_load` on GitHub workflow files:** `on:` → `True`. [VERIFIED: this session]
- **Copying `collect_pooled_sizes()` into a new test:** live L=256×20 Monte Carlo; D-08 forbids it for GCC.
- **`--write` in pytest:** dirties `drafts/crosscheck/` (gitignored, still a worktree side effect). D-07.
- **Duplicating epidemic freeze** in 04-02. D-06.
- **Duplicating `pytest tests/repo_smoke` inside `crosscheck-repro.yml`.** D-09.
- **Adding `generate_crosscheck.py` as a fifth CONFIRMED job.** D-10.
- **Hub `--apply` for a docs-only CROSSCHECK.md edit.** D-11.
- **TDD red-green on tests that already pass against current main:** the inventory/smokes are the product and will be green on first write if markers/commands are correct. Use standard (non-TDD) plans.
</architecture_patterns>

<dont_hand_roll>
## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| “Are all CONFIRMED scripts in CI?” | Actions matrix, extra YAML allowlist, or `scripts/` helper | One pytest text inventory in `tests/repo_smoke/` | Smallest fail-closed check; already executed by `validate-schemas.yml`; avoids `on:` parse and `${{ matrix.* }}` in `run:` |
| Parse GitHub workflow YAML | Custom YAML 1.2 loader / `ruamel.yaml` / `yamlcore` | `Path.read_text` + string/`- name:` split | PyYAML 1.1 bool-coerces `on`/`yes`/`off`; do not add a YAML 1.2 dep for one test |
| GCC CONFIRMED pin | Fake freeze-fit numbers | Subprocess the real script; assert INCONCLUSIVE + 0 | D-03/D-08; script is 0.06s stdlib |
| generate smoke | Import `main()` and inspect dicts | Subprocess CLI `--dry-run` | Matches the documented entry point; argparse is the contract |
| Epidemic coverage | Second freeze test or live NetworkX | Existing `test_epidemic_fss_fit_confirmed_on_reference_pcs` | D-05/D-06 |
| Workflow injection hardening | New composite action / `pull_request_target` | Keep `run:` blocks as **static** strings (already true) | GitHub: never interpolate untrusted context into `run:` [CITED: docs.github.com script-injections] |
| Status unification | Flip habitat/cluster/Ising to `confirmed` | Leave YAML alone; document stdout vs status | D-01 deferred |

**Key insight:** TRUST-02 is a **coverage invariant**, not a new experiment. Experts gate scientific stdout with `grep` and gate process invariants with pytest. Mixing those layers (pytest-only CONFIRMED, or YAML-status CI) is how this repo would silently lie.
</dont_hand_roll>

<common_pitfalls>
## Common Pitfalls

### Pitfall 1: Inventory keyed on catalog YAML `status`
**What goes wrong:** Only epidemic (`confirmed`) looks “CONFIRMED”; habitat/cluster/Ising (`executed`) look ungated; GCC (`ready`) is irrelevant either way.
**Why it happens:** Schema enum `draft\|ready\|executed\|confirmed\|falsified` is a human catalog field, not the CI token. [VERIFIED: `schemas/protocol.yaml`, five protocol files]
**How to avoid:** Source markers in `repro/**/*.py` plus workflow text. Never `status == confirmed`.
**Warning signs:** Test reads `protocols-catalog/**/*.yaml`; assertion count is 1 instead of 4.

### Pitfall 2: `yaml.safe_load` on `crosscheck-repro.yml`
**What goes wrong:** `data.keys() == ['name', True, 'jobs']`; looking up `data["on"]` raises or misses triggers; a “parsed” inventory silently walks the wrong tree.
**Why it happens:** PyYAML 1.1 (PyYAML 6.0.3 still) coerces `on`/`yes`/`off`/`true` to booleans. [VERIFIED: this session]
**How to avoid:** Text parse. Do not add ruamel just to parse one file.
**Warning signs:** Test imports `yaml` to load `.github/workflows/*.yml`.

### Pitfall 3: Fifth CONFIRMED grep for GCC (or generate)
**What goes wrong:** GCC cannot print `RESULT: CONFIRMED`; `grep -q` fails the job or, worse, someone “fixes” the script to print CONFIRMED (D-13).
**Why it happens:** CROSSCHECK.md currently says GCC CI grep is “**no** (Phase 4 TRUST-02)”, which looks like a TODO.
**How to avoid:** Rewrite that cell to CONFIRMED-only policy. Pytest-only for GCC. Never add generate as a CONFIRMED job.
**Warning signs:** `giant_component_fraction.py` or `generate_crosscheck.py` next to `grep -q "RESULT: CONFIRMED"`.

### Pitfall 4: Copying cluster’s live `collect_pooled_sizes()` 
**What goes wrong:** New GCC test imports the module and re-runs lattice work as a “unit” test, or worse copies L=256 pooled collection. Cluster’s existing freeze test **already** calls `collect_pooled_sizes()` live (anti-pattern to not spread).
**Why it happens:** `test_cluster_exponent_fit_confirmed_on_reference_pcs` is the nearest example in the same file.
**How to avoid:** Subprocess `giant_component_fraction.py`. Do not call GCC helpers from pytest. Do not “fix” the cluster test in this phase.
**Warning signs:** `importlib.util.spec_from_file_location` pointing at `giant_component_fraction.py`.

### Pitfall 5: `--write` or `--all` in pytest
**What goes wrong:** `--write` creates gitignored YAML under `drafts/crosscheck/` (skip-if-exists, still a side effect). `--all` walks every bridge with opportunities — slow and noisy.
**Why it happens:** CROSSCHECK.md documents `--write` as the human happy path.
**How to avoid:** Hard-code argv `["--bridge", "b-percolation-oncology", "--dry-run"]`. Assert `"p-b-"` in stdout.
**Warning signs:** Test argv contains `--write` or `--all`.

### Pitfall 6: Interpolating GitHub context into `run:`
**What goes wrong:** `run: python ${{ matrix.script }}` or PR title in a shell string is workflow script injection.
**Why it happens:** Matrix rewrite looks tidy.
**How to avoid:** Do not introduce a matrix. Keep static `run:` blocks. Inventory is pytest. [CITED: https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions]
**Warning signs:** `${{` inside a `run:` string that includes paths or titles.

### Pitfall 7: Drive-by epidemic retune or YAML status flips
**What goes wrong:** Phase 4 “unification” edits `NU_THEORY` or flips `executed` → `confirmed`.
**Why it happens:** Ship-bar pressure to make catalog match stdout.
**How to avoid:** D-01/D-05/deferred list. Do not open those files except to read.
**Warning signs:** Diff in `epidemic_percolation_fss.py` or habitat/cluster/Ising YAML `status:`.
</common_pitfalls>

<code_examples>
## Code Examples

Verified patterns from **this repo** (not invented). Planner task actions should copy these.

### Live CONFIRMED grep (keep all four)

```yaml
# Source: .github/workflows/crosscheck-repro.yml
- name: Habitat percolation FSS (expect CONFIRMED)
  run: |
    python repro/p-b-habitat-percolation-ecology-fss/simulate_percolation_fss.py | tee /tmp/fss.out
    grep -q "RESULT: CONFIRMED" /tmp/fss.out
```

Same shape for cluster (`/tmp/cluster.out`), epidemic (`/tmp/epidemic.out`), Ising (`/tmp/ising.out`). [VERIFIED]

### CONFIRMED stdout markers in seed scripts

```python
# Source: repro/p-b-habitat-percolation-ecology-fss/simulate_percolation_fss.py
print(f"RESULT: {'CONFIRMED' if passed else 'INCONCLUSIVE (increase TRIALS_PER_P for higher precision)'}")
return 0
```

```python
# Source: repro/p-b-ising-social-dynamics-ewi/ising_critical_slowing.py
if passed:
    result = "CONFIRMED"
# ...
print(f"RESULT: {result}")
return 0
```

### GCC honesty (never CONFIRMED)

```python
# Source: repro/p-b-percolation-oncology-gcc/giant_component_fraction.py
print(
    "RESULT: INCONCLUSIVE (thin synthetic lattice; not a clinical "
    "biomarker; not an FSS precision pass)"
)
return 0
```

### Epidemic freeze to keep (do not duplicate)

```python
# Source: tests/repo_smoke/test_crosscheck_repro_regression.py
assert list(mod.SIZES) == [200, 500, 1000, 2000, 5000]
assert mod.NU_THEORY == 3.0
pcs = [
    0.16796109080314636,
    0.16996005177497864,
    0.16739705204963684,
    0.1681748926639557,
    0.16720572113990784,
]
```

Those five floats are the 02-01 CONFIRMED_FREEZE vector — do not invent replacements. [VERIFIED: `02-02-SUMMARY.md`]

### Cluster anti-pattern (do not copy)

```python
# Source: tests/repo_smoke/test_crosscheck_repro_regression.py
sizes = mod.collect_pooled_sizes()  # live L=256, SEEDS=20 — D-08: not for new tests
```

### generate_crosscheck CLI contract

```python
# Source: scripts/generate_crosscheck.py
parser.add_argument("--bridge", type=str, help="Single bridge ID (b-...)")
parser.add_argument("--dry-run", action="store_true", help="Print drafts without writing files")
parser.add_argument("--write", action="store_true", help="Write drafts to drafts/crosscheck/")
# mutually exclusive: parser.error("Use either --dry-run or --write, not both")
```

Dry-run stdout this session includes lines like `[1] p-b-percolation-oncology-percolation-derived-metrics-giant-compon` and `Total protocols: 3`. [VERIFIED]

### pytest pickup (do not duplicate in crosscheck-repro.yml)

```yaml
# Source: .github/workflows/validate-schemas.yml
- name: Catalog YAML + domain pages + dashboard consistency + orphan report
  run: python -m pytest tests/repo_smoke -v --tb=short
```

```toml
# Source: pyproject.toml
[tool.pytest.ini_options]
testpaths = ["packages/ingest/tests", "tests/repo_smoke"]
addopts = "-ra"
```
</code_examples>

<sota_updates>
## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| Assume PyYAML round-trips GitHub workflow YAML | Treat Actions YAML as **text** for invariants; GitHub’s runner is the YAML 1.1 consumer | PyYAML still 1.1-bool in 6.x | 04-01 must not `safe_load` `on:` |
| Actions matrix as the default “unify the jobs” move | Static `run:` steps + a coverage test | GitHub script-injection guidance | Matrix in `run: python ${{ matrix.script }}` is extra risk for zero gain here |
| ASVS 4.x V5 “input validation” chapter numbers | ASVS 5.0.0 (May 2025) remaps validation to V2; injection to V1 | May 2025 | Use outcomes (argv lists, no shell interpolation), not a fake web-app ASVS spreadsheet |
| Pin Actions to moving tags casually | Prefer SHA pins for third-party actions; this repo already uses `actions/checkout@v7` | GitHub secure-use | Do **not** expand Phase 4 into a pin-SHA campaign |

**New tools/patterns to consider (and reject for this phase):**
- **actionlint / zizmor:** useful later; not needed to close TRUST-02/03.
- **Reusable workflows:** extra indirection; four steps stay in one file.
- **yamlcore / ruamel.yaml:** would fix `on:` if we parsed YAML; text parse needs neither.

**Deprecated/outdated:**
- Treating YAML `status: confirmed` as the CI source of truth (never was, in this repo).
- CROSSCHECK.md wording that GCC CI grep is a Phase 4 TRUST-02 TODO — TRUST-02 is CONFIRMED-only.
</sota_updates>

## Environment Availability

Step 2.6: probed this session. No missing blocking tools.

| Dependency | Required By | Available | Version | Fallback |
|------------|------------|-----------|---------|----------|
| CPython | pytest, generate, GCC | ✓ | 3.12.6 local; CI 3.11/3.12 | — |
| pytest | TRUST-02/03 tests | ✓ | 8.4.2 | CI installs unpinned `pytest` |
| PyYAML | `generate_crosscheck.py` | ✓ | 6.0.3 | CI `pip install pyyaml` |
| jsonschema | existing repo_smoke | ✓ | 4.23.0 | CI `jsonschema>=4.20` |
| networkx | epidemic **live** CI only | CI-only | unpinned | **Do not** require it for new tests |
| mkdocs | D-11 docs edit | not probed | — | Required only after `docs/` change; `mkdocs-build.yml` is CI backup |

**Missing dependencies with no fallback:** none.

**Missing dependencies with fallback:** none for the phase itself. `mkdocs` is a docs-gate, not a test-gate.

## Validation Architecture

`.planning/config.json` is absent → treat `workflow.nyquist_validation` as **enabled**.

### Test Framework

| Property | Value |
|----------|-------|
| Framework | pytest 8.4.2 (CI unpinned `pytest`) |
| Config file | `pyproject.toml` `[tool.pytest.ini_options]` |
| Quick run command | `python -m pytest tests/repo_smoke/test_crosscheck_confirmed_gates.py tests/repo_smoke/test_crosscheck_entry_points.py tests/repo_smoke/test_crosscheck_repro_regression.py::test_epidemic_fss_fit_confirmed_on_reference_pcs -x` |
| Full suite command | `python -m pytest tests/repo_smoke -v --tb=short` (same as `validate-schemas.yml`) |

Also run after docs: `mkdocs build --strict`. Do not require `packages/ingest/tests` for this phase.

### Phase Requirements → Test Map

| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| TRUST-02 | Every CONFIRMED-capable `repro/**/*.py` is grepped CONFIRMED in `crosscheck-repro.yml` | unit (inventory) | `python -m pytest tests/repo_smoke/test_crosscheck_confirmed_gates.py -x` | ❌ Wave 0 |
| TRUST-02 | GCC / INCONCLUSIVE-only scripts are **not** grepped CONFIRMED | unit (negative) | same file | ❌ Wave 0 |
| TRUST-02 | Four live tee+grep steps still present (D-02) | implied by inventory equality | same file + do not delete workflow steps | ✅ workflow; ❌ assertion |
| TRUST-03 | Epidemic freeze `NU_THEORY == 3.0` | unit (keep) | `python -m pytest tests/repo_smoke/test_crosscheck_repro_regression.py::test_epidemic_fss_fit_confirmed_on_reference_pcs -x` | ✅ |
| TRUST-03 | `generate_crosscheck.py --bridge b-percolation-oncology --dry-run` exit 0 + `p-b-` stdout | smoke | `python -m pytest tests/repo_smoke/test_crosscheck_entry_points.py -x` | ❌ Wave 0 |
| TRUST-03 | `giant_component_fraction.py` INCONCLUSIVE + exit 0 | smoke | same file | ❌ Wave 0 |

### Sampling Rate

- **Per task commit:** quick run command above (<30s; generate + GCC + inventory are near-instant; epidemic freeze is 0.02s; **full `tests/repo_smoke` includes live cluster `collect_pooled_sizes()`** — still the merge bundle).
- **Per wave merge:** `python -m pytest tests/repo_smoke -v --tb=short`
- **Phase gate:** full repo_smoke green + `mkdocs build --strict` if `docs/` changed. Do not require a live `crosscheck-repro.yml` run locally (needs networkx + minutes of Monte Carlo). Inventory pytest is the local stand-in for TRUST-02.

### Wave 0 Gaps

- [ ] `tests/repo_smoke/test_crosscheck_confirmed_gates.py` — TRUST-02 inventory + negative GCC assertion
- [ ] `tests/repo_smoke/test_crosscheck_entry_points.py` — TRUST-03 generate dry-run + GCC subprocess
- [ ] `docs/CROSSCHECK.md` CI-column honesty (not a test file; 04-01 docs task)
- [ ] Framework install: none — pytest + PyYAML already in `validate-schemas.yml`

Existing infrastructure covers epidemic TRUST-03. Cluster live pooled test is a pre-existing slow/anti-pattern — **do not “fix” it here**.

## Security Domain

`security_enforcement` is absent in config → **enabled**. This phase is CI YAML + pytest, not an application. Keep ASVS honest and small.

### Applicable ASVS Categories

ASVS 5.0.0 (May 2025) remapped chapters; the table below uses the GSD template’s 4.x labels and maps the **outcome**. [CITED: OWASP ASVS 5.0 V2 Validation; V1 Encoding/Injection]

| ASVS Category | Applies | Standard Control |
|---------------|---------|-----------------|
| V2 Authentication | no | No logins, tokens, or `GITHUB_TOKEN` permission changes |
| V3 Session Management | no | No sessions |
| V4 Access Control | no | Do not add `pull_request_target` or write permissions. Existing workflows stay `pull_request` + `ubuntu-latest` |
| V5 Input Validation | yes (narrow) | Subprocess **list argv** (no `shell=True`). Inventory reads committed files, not PR titles. Generate `--bridge` is a test constant |
| V6 Cryptography | no | No secrets, JWTs, or hashing |

### Known Threat Patterns for GitHub Actions + pytest

| Pattern | STRIDE | Standard Mitigation |
|---------|--------|---------------------|
| Workflow script injection via `${{ github.event.pull_request.title }}` (or matrix path) in `run:` | Tampering | Keep `run:` **static**. Do not introduce `strategy.matrix` into `run: python ${{ matrix.script }}`. [CITED: https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions] |
| `yaml.load` / unexpected `safe_load` of workflow | Tampering | Do not deserialize workflow YAML. Text parse only. |
| `shell=True` pytest subprocess | Tampering | `subprocess.run([sys.executable, script, ...], cwd=REPO_ROOT)` like `test_crosscheck_artifacts.py` |
| `pull_request_target` + untrusted checkout | Elevation of privilege | Do not add this trigger. [CITED: GitHub “Mitigating the risks of untrusted code checkout”] |
| Fabricated `RESULT: CONFIRMED` to make grep pass | Repudiation / Integrity | D-13; GCC must assert INCONCLUSIVE |
| `--write` in CI mutating the runner worktree | Tampering (low) | `--dry-run` only |

Do not expand this phase into SHA-pinning all Actions, CODEOWNERS, or Scorecard. Those are real GitHub hardening items and **out of TRUST-02/03 scope**.

<assumptions_log>
## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| — | *(none)* | — | All material claims are `[VERIFIED]` against this repo or `[CITED]` official docs. |

**If this table is empty:** All claims in this research were verified or cited — no user confirmation needed.

Discretion items below have **recommended answers** so the planner can lock them without a discuss-phase.
</assumptions_log>

<open_questions>
## Open Questions

1. **TRUST-02 inventory mechanism (Discretion)**
   - What we know: Four live greps already exist. YAML `status` is not the token. PyYAML cannot round-trip this workflow. D-04 allows matrix, pytest, or helper.
   - What's unclear: nothing blocking — smallest fail-closed option is clear.
   - **Recommendation:** Pytest text inventory in `tests/repo_smoke/test_crosscheck_confirmed_gates.py`. No matrix. No `scripts/` helper. No workflow rewrite unless a future protocol is added (out of this phase).

2. **Does GCC belong in `crosscheck-repro.yml` as an INCONCLUSIVE step? (Discretion)**
   - What we know: D-03 allows CI **or** pytest if the assertion is INCONCLUSIVE + exit 0. D-09 says new pytest lives in repo_smoke. D-11 wants CONFIRMED-only grep policy. GCC ran in 0.058s locally.
   - What's unclear: maintainer taste for seeing GCC in the CONFIRMED workflow log.
   - **Recommendation:** **pytest-only.** Do not add an INCONCLUSIVE step to `crosscheck-repro.yml`. Negative inventory assertion: `giant_component_fraction.py` must not share a step with `grep -q "RESULT: CONFIRMED"`.

3. **Which `--bridge` for generate dry-run? (Discretion)**
   - What we know: D-07 allows any existing bridge. Oncology is the Phase 3 happy path; habitat is the manifesto “preview any one bridge” example. Dry-run prints three `p-b-percolation-oncology-*` ids in well under 30s.
   - **Recommendation:** `--bridge b-percolation-oncology --dry-run`. Assert `"p-b-"` in stdout (do **not** assert the human-promoted id `p-b-percolation-oncology-gcc`).

4. **04-01 vs 04-02 parallel or sequential? (Discretion / D-14)**
   - What we know: Implementation files do not overlap if 04-01 owns `test_crosscheck_confirmed_gates.py` + `docs/CROSSCHECK.md` and 04-02 owns `test_crosscheck_entry_points.py`. Both would edit `CHANGELOG.md` Unreleased.
   - **Recommendation:** **Sequential 04-01 then 04-02.** Serialize `CHANGELOG.md`. `docs/CROSSCHECK.md` is 04-01-only so D-14 is satisfied. If the planner insists on parallel Wave 1, freeze CHANGELOG to 04-02 (or a trailing docs task) and keep CROSSCHECK.md on 04-01.

5. **Should 04-02 touch `test_crosscheck_repro_regression.py`?**
   - What we know: Epidemic freeze already asserts `NU_THEORY == 3.0`. D-06 says do not duplicate.
   - **Recommendation:** Do not edit that file. 04-02 verification command **re-runs** the existing test; that is enough to prove TRUST-03 “covers epidemic.”
</open_questions>

<sources>
## Sources

### Primary (HIGH confidence)

- `.github/workflows/crosscheck-repro.yml` — four `tee` + `grep -q "RESULT: CONFIRMED"` steps; path filters; `pip install networkx`; Python 3.11
- `.github/workflows/validate-schemas.yml` — `python -m pytest tests/repo_smoke -v --tb=short` on every PR/push to `main`; PyYAML + pytest; Python 3.12
- `.github/workflows/validate.yml` — path-filtered schema job; already lists `scripts/generate_crosscheck.py`; does **not** run pytest
- `tests/repo_smoke/test_crosscheck_repro_regression.py` — freeze fits; epidemic `NU_THEORY == 3.0`; cluster `collect_pooled_sizes()` live
- `tests/repo_smoke/test_crosscheck_artifacts.py` — subprocess list-argv pattern
- `tests/repo_smoke/test_catalog_regression.py` — `_run_script` (stdout discarded)
- `scripts/generate_crosscheck.py` — `--dry-run` / `--write` / `--bridge` contract
- `repro/p-b-*/**.py` — RESULT markers; GCC INCONCLUSIVE
- `protocols-catalog/**/p-b-*.yaml` — status `executed` ×3, `confirmed` ×1, `ready` ×1
- `docs/CROSSCHECK.md` — Run-mode parity CI column
- `pyproject.toml` — pytest `testpaths`
- `.planning/{REQUIREMENTS,ROADMAP,PROJECT,STATE}.md` + `04-CONTEXT.md` + `02-02-SUMMARY.md` + `03-01-SUMMARY.md` + `03-02-SUMMARY.md`
- Local probes: `python --version`, `pytest --version`, `yaml.__version__`, generate `--dry-run`, GCC 0.058s, `yaml.safe_load` `on:` → `True`
- GitHub Docs: [Workflow syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions); [Security hardening / script injections](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions)
- OWASP ASVS 5.0 V2 Validation and Business Logic — https://github.com/OWASP/ASVS/blob/v5.0.0/5.0/en/0x11-V2-Validation-and-Business-Logic.md

### Secondary (MEDIUM confidence)

- PyYAML YAML 1.1 boolean-key coercion (`on`/`yes`/`off`) — Stack Overflow consensus, **confirmed locally** against this workflow

### Tertiary (LOW confidence)

- None used as planning authority
</sources>

<metadata>
## Metadata

**Research scope:**
- Core technology: GitHub Actions stdout greps + pytest repo_smoke
- Ecosystem: pytest 8.4, PyYAML 6.0, existing USDR Crosscheck CI
- Patterns: text inventory vs matrix; subprocess smokes; CONFIRMED vs INCONCLUSIVE tokens
- Pitfalls: YAML status, `on:` parse, fifth CONFIRMED grep, cluster live MC copy, `--write`

**Confidence breakdown:**
- Standard stack: HIGH — versions probed; no new libraries
- Architecture: HIGH — all paths read in this repo; inventory mechanism exercised as a design against real files
- Pitfalls: HIGH — `on:` gotcha reproduced; GCC/generate commands run; protocol statuses grepped
- Code examples: HIGH — copied from this repo

**Research date:** 2026-08-26
**Valid until:** 2026-09-25 (30 days — CI YAML and pytest 8 are stable; re-check if a fifth CONFIRMED script is merged first)
</metadata>

---

*Phase: 04-ci-trust-hardening*
*Research completed: 2026-08-26*
*Ready for planning: yes*

# Phase 4: CI & trust hardening - Pattern Map

**Mapped:** 2026-08-26
**Files analyzed:** 4 (2 new tests, 2 docs edits)
**Analogs found:** 4 / 4

Phase 4 is **fail-closed mapping + smoke**, not a fifth CONFIRMED trophy. Copy pytest/subprocess/docs patterns from existing `tests/repo_smoke/` and honesty docs. Do **not** rewrite `.github/workflows/crosscheck-repro.yml` into a matrix, do **not** add a GCC CONFIRMED grep, do **not** add a `scripts/` helper, do **not** duplicate the epidemic freeze test, do **not** `yaml.safe_load` the workflow.

Primary assignment:

- **04-01:** `tests/repo_smoke/test_crosscheck_confirmed_gates.py` + `docs/CROSSCHECK.md` (CONFIRMED-only grep policy; docs-only, no hub `--apply`)
- **04-02:** `tests/repo_smoke/test_crosscheck_entry_points.py` (`generate_crosscheck.py --bridge b-percolation-oncology --dry-run` + live GCC `RESULT: INCONCLUSIVE` / exit 0)
- **CHANGELOG.md** Unreleased: sequential (04-01 then 04-02) so both plans do not collide on that file

---

## File Classification

| New/Modified File | Role | Data Flow | Closest Analog | Match Quality |
|-------------------|------|-----------|----------------|---------------|
| `tests/repo_smoke/test_crosscheck_confirmed_gates.py` | test | file-I/O | `tests/repo_smoke/test_catalog_regression.py` (`REPO_ROOT`, `Path.read_text`) + `scripts/build_crosscheck.py` (`rglob` + UTF-8 text; **not** `yaml.safe_load`) | role-match (inventory algorithm is new) |
| `docs/CROSSCHECK.md` | config | file-I/O | Same file, `## Run-mode parity` table CI column (lines 77–88) | exact |
| `tests/repo_smoke/test_crosscheck_entry_points.py` | test | request-response | `tests/repo_smoke/test_crosscheck_artifacts.py` list-argv `subprocess.run` **with stdout capture** | exact |
| `CHANGELOG.md` | config | file-I/O | Same file, `## [Unreleased]` Added bullets (lines 10–16) | exact |

**Do not create/modify (keep as analog / freeze):**

| File | Why it is off-limits |
|------|----------------------|
| `.github/workflows/crosscheck-repro.yml` | Keep four static `tee` + `grep -q "RESULT: CONFIRMED"` steps. No matrix. No GCC step. No pytest job. |
| `.github/workflows/validate-schemas.yml` | Already runs `python -m pytest tests/repo_smoke -v --tb=short` with no path filter. New tests are picked up automatically. |
| `tests/repo_smoke/test_crosscheck_repro_regression.py` | Epidemic freeze already closes TRUST-03 “covers epidemic”. Do not duplicate. Do not copy `collect_pooled_sizes()`. |
| `tests/repo_smoke/test_catalog_regression.py` | Do not overload `_run_script` (it discards stdout). |
| `scripts/generate_crosscheck.py` | CLI contract analog only. Do not edit. |
| `repro/p-b-percolation-oncology-gcc/giant_component_fraction.py` | Always `RESULT: INCONCLUSIVE`, exit 0. Do not add CONFIRMED. |
| `dashboard/index.html` | Already links `#run-mode-parity`. Docs-only CROSSCHECK.md edit → **no** `build_crosscheck.py --apply`. |
| `scripts/check_crosscheck_gates.py` / `repro/CONFIRMED_GATES.yml` | **Do not add.** Inventory lives in pytest. |

---

## Pattern Assignments

### `tests/repo_smoke/test_crosscheck_confirmed_gates.py` (test, file-I/O)

**Analog (boilerplate):** `tests/repo_smoke/test_catalog_regression.py` + `tests/repo_smoke/test_crosscheck_artifacts.py`

**Analog (scan committed files as UTF-8 text):** `scripts/build_crosscheck.py` `snapshot_artifacts` / `rglob` — copy **text read**, never `yaml.safe_load` on the workflow.

**Analog (CONFIRMED grep steps to pair against):** `.github/workflows/crosscheck-repro.yml` (keep, do not rewrite)

**Analog (negative case):** `repro/p-b-percolation-oncology-gcc/giant_component_fraction.py`

**Imports / repo-root pattern** (`tests/repo_smoke/test_crosscheck_artifacts.py` lines 1–9; same in catalog regression lines 12–19):

```python
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
```

For the inventory file, drop `subprocess`/`sys` unless a helper needs them. Keep `from __future__ import annotations` and `REPO_ROOT`. Add no PyYAML import.

**UTF-8 text read + relative POSIX path** (`scripts/build_crosscheck.py` lines 84–88) — copy this I/O, not YAML load:

```python
snap[str(path.relative_to(ROOT))] = path.read_text(encoding="utf-8")
```

**Glob analog** (`scripts/build_crosscheck.py` lines 48–49 / `scripts/generate_crosscheck.py` line 129) — adapt to `repro/**/*.py`, skip `__pycache__`:

```python
for path in sorted(CATALOG.rglob("p-b-*.yaml")):
```

Inventory glob to implement:

```python
REPRO_ROOT = REPO_ROOT / "repro"
WORKFLOW = REPO_ROOT / ".github" / "workflows" / "crosscheck-repro.yml"

def _repro_py_files() -> list[Path]:
    return [
        p
        for p in sorted(REPRO_ROOT.rglob("*.py"))
        if "__pycache__" not in p.parts
    ]
```

**CONFIRMED-capable markers (source of truth — not YAML `status`):**

A `repro/**/*.py` file is CONFIRMED-capable if its UTF-8 text contains **any** of:

- `'CONFIRMED' if` or `"CONFIRMED" if`
- `result = "CONFIRMED"` or `result = 'CONFIRMED'`
- literal `RESULT: CONFIRMED`

Verified markers in current seeds:

```python
# repro/p-b-habitat-percolation-ecology-fss/simulate_percolation_fss.py line 115
print(f"RESULT: {'CONFIRMED' if passed else 'INCONCLUSIVE (increase TRIALS_PER_P for higher precision)'}")

# repro/p-b-habitat-percolation-ecology-cluster-exponent/cluster_size_exponent.py line 132
print(f"RESULT: {'CONFIRMED' if passed else 'INCONCLUSIVE (adjust P or L for clearer scaling)'}")

# repro/p-b-percolation-epidemiology-fss/epidemic_percolation_fss.py lines 161-163
print(
    f"RESULT: {'CONFIRMED' if passed else 'INCONCLUSIVE (increase SEEDS_PER_N for higher precision)'}"
)

# repro/p-b-ising-social-dynamics-ewi/ising_critical_slowing.py lines 187-193
if passed:
    result = "CONFIRMED"
# ...
print(f"RESULT: {result}")
```

GCC currently matches **none** of these:

```python
# repro/p-b-percolation-oncology-gcc/giant_component_fraction.py lines 122-126
print(
    "RESULT: INCONCLUSIVE (thin synthetic lattice; not a clinical "
    "biomarker; not an FSS precision pass)"
)
return 0
```

**Workflow pairing (parse as TEXT, not YAML):**

```yaml
# .github/workflows/crosscheck-repro.yml lines 29-46 — keep verbatim; inventory must find these
- name: Habitat percolation FSS (expect CONFIRMED)
  run: |
    python repro/p-b-habitat-percolation-ecology-fss/simulate_percolation_fss.py | tee /tmp/fss.out
    grep -q "RESULT: CONFIRMED" /tmp/fss.out

- name: Cluster size exponent (expect CONFIRMED)
  run: |
    python repro/p-b-habitat-percolation-ecology-cluster-exponent/cluster_size_exponent.py | tee /tmp/cluster.out
    grep -q "RESULT: CONFIRMED" /tmp/cluster.out

- name: Epidemic percolation FSS (expect CONFIRMED)
  run: |
    python repro/p-b-percolation-epidemiology-fss/epidemic_percolation_fss.py | tee /tmp/epidemic.out
    grep -q "RESULT: CONFIRMED" /tmp/epidemic.out

- name: Ising social dynamics EWI (expect CONFIRMED)
  run: |
    python repro/p-b-ising-social-dynamics-ewi/ising_critical_slowing.py | tee /tmp/ising.out
    grep -q "RESULT: CONFIRMED" /tmp/ising.out
```

**Core inventory algorithm (new; no existing test analog — implement from RESEARCH Pattern 1):**

1. `workflow = WORKFLOW.read_text(encoding="utf-8")` — **never** `yaml.safe_load` (PyYAML 1.1 turns top-level `on:` into `True`).
2. Split on step headers (`- name:`) so each step body can be inspected independently.
3. For each CONFIRMED-capable script, the relative POSIX path (`repro/p-b-.../file.py`) must appear in a step whose body also contains `grep -q "RESULT: CONFIRMED"`.
4. Assert `workflow.count('grep -q "RESULT: CONFIRMED"') == len(discovered)`.
5. **Negative:** for every repro `*.py` that is **not** CONFIRMED-capable (today: `giant_component_fraction.py`), no step may contain both that script path and a CONFIRMED grep.

Suggested assertion names (non-TDD; green on first write against current main):

```python
def test_confirmed_capable_repro_scripts_are_grepped_in_crosscheck_repro_workflow() -> None:
    ...

def test_inconclusive_only_scripts_are_not_grepped_confirmed() -> None:
    # giant_component_fraction.py must NOT share a CONFIRMED grep step
    ...
```

**Error handling:** pytest `assert` with the missing POSIX path and the discovered vs grep counts in the message. Do not wrap in try/except. Do not `shell=True`.

**Validation:** no JSON/YAML schema. Source markers + workflow text only. Never read `protocols-catalog/**/*.yaml` `status:`.

**Anti-patterns for this file:**

- `import yaml` / `yaml.safe_load(WORKFLOW.read_text(...))`
- GitHub Actions `strategy.matrix`
- A fifth workflow step grepping GCC CONFIRMED
- New `scripts/check_crosscheck_gates.py`
- `importlib` / live Monte Carlo

**Pickup (do not duplicate pytest in `crosscheck-repro.yml`):**

```yaml
# .github/workflows/validate-schemas.yml lines 19-23
- name: Install validators + pytest
  run: pip install pyyaml "jsonschema>=4.20" pytest

- name: Catalog YAML + domain pages + dashboard consistency + orphan report
  run: python -m pytest tests/repo_smoke -v --tb=short
```

```toml
# pyproject.toml lines 2-5
[tool.pytest.ini_options]
testpaths = ["packages/ingest/tests", "tests/repo_smoke"]
addopts = "-ra"
```

---

### `docs/CROSSCHECK.md` (config, file-I/O)

**Analog:** same file, `## Run-mode parity` (lines 77–88)

**Core pattern — rewrite the GCC CI cell**, not the whole manifesto. Hub already links this heading:

```html
<!-- dashboard/index.html line 1884 — already present; do not edit hub for this docs-only change -->
· <a href="../docs/CROSSCHECK.md#run-mode-parity">Run-mode parity</a>
```

Current table (line 80 header + line 88 GCC row is the honesty bug):

```markdown
## Run-mode parity

Python is canonical; browser and Colab are demo tier.

| protocol id | Python canonical | browser JS | Colab | CI grep CONFIRMED | RESULT contract |
|-------------|--------------|------------|-------|-------------------|-----------------|
| `p-b-habitat-percolation-ecology-fss` | ... | yes, ... | no | yes | stdout `RESULT:` token; Python `return 0` always |
| `p-b-habitat-percolation-ecology-cluster-exponent` | ... | yes, ... | no | yes | ... |
| `p-b-ising-social-dynamics-ewi` | ... | yes, ... | no | yes | stdout `RESULT:` token; Python `return 0` always |
| `p-b-percolation-epidemiology-fss` | ... | **no** | yes, `run_crosscheck.ipynb` | yes | stdout `RESULT:` token; Python `return 0` always |
| `p-b-percolation-oncology-gcc` | `giant_component_fraction.py` (`L=32`, `TRIALS=8`) | **no** | **no** | **no** (Phase 4 TRUST-02) | stdout `RESULT: INCONCLUSIVE`; Python `return 0` always |
```

**Replace** the GCC CI cell `**no** (Phase 4 TRUST-02)` (reads like a TODO that might add a CONFIRMED grep) with **CONFIRMED-only grep policy**. Keep the four seed CI cells as `yes`. GCC CI cell stays **no**.

Policy sentence to add next to the table (04-01 owns this file; 04-02 does not edit it):

- Four seed scripts are grepped `RESULT: CONFIRMED` in `.github/workflows/crosscheck-repro.yml`.
- GCC always prints `RESULT: INCONCLUSIVE` and **must not** be grepped CONFIRMED.
- Pytest covers the GCC entry point (`tests/repo_smoke/`); `validate-schemas.yml` runs that bundle on every PR.

**Do not** run `python scripts/build_crosscheck.py --apply` after a docs-only edit. After the edit: `mkdocs build --strict`.

**Do not** change the internal Roadmap Phase 3/4 rows (lines 125–134) — those are Crosscheck product phases, not GSD.

---

### `tests/repo_smoke/test_crosscheck_entry_points.py` (test, request-response)

**Analog (copy this, including stdout capture):** `tests/repo_smoke/test_crosscheck_artifacts.py`

**Anti-analog (do not copy as-is):** `tests/repo_smoke/test_catalog_regression.py` `_run_script` — it throws away stdout, which 04-02 must assert.

**Anti-analog (do not copy):** `test_cluster_exponent_fit_confirmed_on_pooled_reference` live `collect_pooled_sizes()`.

**Do not edit / do not duplicate:** `test_epidemic_fss_fit_confirmed_on_reference_pcs` in `test_crosscheck_repro_regression.py`. TRUST-03 epidemic is closed by **re-running** that existing test in the 04-02 verification command.

**Imports pattern** (`tests/repo_smoke/test_crosscheck_artifacts.py` lines 1–17):

```python
"""Crosscheck codegen drift gate (see scripts/build_crosscheck.py)."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


def test_crosscheck_artifacts_up_to_date() -> None:
    cmd = [sys.executable, str(REPO_ROOT / "scripts" / "build_crosscheck.py"), "--check"]
    proc = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True, check=False)
    if proc.returncode != 0:
        out = (proc.stdout or "") + (proc.stderr or "")
        raise AssertionError(f"build_crosscheck.py --check failed:\n{out}")
```

Copy: `from __future__`, list argv, `cwd=REPO_ROOT`, `capture_output=True`, `text=True`, `check=False`, combine stdout+stderr on failure. Adapt docstring and assertion text. Use `assert proc.returncode == 0` **and** inspect `proc.stdout` (artifacts test only checks returncode).

**List-argv shape also in** `tests/repo_smoke/test_catalog_regression.py` lines 22–27 — copy the subprocess call, **not** the helper that ignores stdout:

```python
def _run_script(name: str, *extra_args: str) -> None:
    cmd = [sys.executable, str(REPO_ROOT / "scripts" / name), *extra_args]
    proc = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True, check=False)
    if proc.returncode != 0:
        out = (proc.stdout or "") + (proc.stderr or "")
        raise AssertionError(f"{name} exited {proc.returncode}:\n{out}")
```

**Generate CLI contract** (`scripts/generate_crosscheck.py` lines 136–147, 152–165):

```python
parser.add_argument("--bridge", type=str, help="Single bridge ID (b-...)")
parser.add_argument("--all", action="store_true", help="All bridges with cross_pollination_opportunities")
parser.add_argument("--dry-run", action="store_true", help="Print drafts without writing files")
parser.add_argument("--write", action="store_true", help="Write drafts to drafts/crosscheck/")
# mutually exclusive: parser.error("Use either --dry-run or --write, not both")
```

```python
print(f"  [{i}] {protocol['id']}  tier={protocol['feasibility_tier']}")
if args.dry_run:
    print(yaml.dump(protocol, allow_unicode=True, sort_keys=False, default_flow_style=False)[:400] + "...")
```

Happy-path argv **must** be (D-07; oncology Phase 3 path):

```python
cmd = [
    sys.executable,
    str(REPO_ROOT / "scripts" / "generate_crosscheck.py"),
    "--bridge",
    "b-percolation-oncology",
    "--dry-run",
]
proc = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True, check=False)
assert proc.returncode == 0, (proc.stdout or "") + (proc.stderr or "")
assert "p-b-" in (proc.stdout or "")
assert "--write" not in cmd
```

Do **not** pass `--write` or `--all`. Do **not** assert the human-promoted id `p-b-percolation-oncology-gcc` (dry-run prints generator ids like `p-b-percolation-oncology-percolation-derived-metrics-giant-compon`). No networkx. Must stay well under 30s.

**GCC live stdlib subprocess** — run the real script; do not import helpers:

```python
cmd = [
    sys.executable,
    str(REPO_ROOT / "repro" / "p-b-percolation-oncology-gcc" / "giant_component_fraction.py"),
]
proc = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True, check=False)
assert proc.returncode == 0
assert "RESULT: INCONCLUSIVE" in (proc.stdout or "")
assert "RESULT: CONFIRMED" not in (proc.stdout or "")
```

Script contract (`giant_component_fraction.py` lines 100–130): header `Crosscheck: p-b-percolation-oncology-gcc`, always prints INCONCLUSIVE, `return 0`, `raise SystemExit(main())`. L=32 / TRIALS=8 is already cheap (~0.06s); do not retune.

**Epidemic freeze to keep (do not copy into the new file):**

```python
# tests/repo_smoke/test_crosscheck_repro_regression.py lines 75-96
def test_epidemic_fss_fit_confirmed_on_reference_pcs() -> None:
    ...
    pcs = [
        0.16796109080314636,
        0.16996005177497864,
        0.16739705204963684,
        0.1681748926639557,
        0.16720572113990784,
    ]
    assert list(mod.SIZES) == [200, 500, 1000, 2000, 5000]
    assert mod.NU_THEORY == 3.0
    assert mod.PC_INF == 1.0 / mod.MEAN_DEGREE
    nu, r2, sign_ok = mod.fit_nu(mod.SIZES, pcs)
```

04-02 verification command **re-runs** that test. Do not invent a second freeze vector.

**Cluster anti-pattern (do not copy):**

```python
# tests/repo_smoke/test_crosscheck_repro_regression.py lines 59-67
def test_cluster_exponent_fit_confirmed_on_pooled_reference() -> None:
    ...
    sizes = mod.collect_pooled_sizes()  # live L=256, SEEDS=20 — not for GCC
```

Do not `importlib.util.spec_from_file_location` pointing at `giant_component_fraction.py`.

**Error handling:** same as artifacts — `check=False` then `AssertionError` / `assert` with combined stdout+stderr. Never `shell=True`.

---

### `CHANGELOG.md` (config, file-I/O)

**Analog:** same file, Unreleased header (lines 10–16)

```markdown
## [Unreleased]

### Added — Crosscheck generate/promote path and run-mode parity
- **`docs/CROSSCHECK.md`:** Happy-path generate is `python scripts/generate_crosscheck.py --bridge b-percolation-oncology --write` ...
```

**Copy:** Keep a Changelog `### Added` / `### Changed` bullets under `## [Unreleased]`. Name paths. Do not invent scientific claims.

- **04-01 bullet:** inventory pytest + CROSSCHECK.md CONFIRMED-only grep policy (four seeds grepped CONFIRMED; GCC must not be).
- **04-02 bullet:** `test_crosscheck_entry_points.py` generate `--dry-run` + GCC INCONCLUSIVE/exit-0 smoke.

Serialize this file (04-01 then 04-02). Do not touch `README.md` / `docs/DOC_MAP.md` / `docs/REPOSITORY_MANIFEST.md` unless user-visible commands change (they do not: pytest pickup is already `tests/repo_smoke`).

---

## Shared Patterns

### Repo-root pytest module header
**Source:** `tests/repo_smoke/test_crosscheck_artifacts.py` lines 1–9; `test_catalog_regression.py` lines 12–19
**Apply to:** both new test files

```python
from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
```

Entry-points test also imports `subprocess` and `sys`. Inventory test does not need subprocess.

### List-argv subprocess (no shell interpolation)
**Source:** `tests/repo_smoke/test_crosscheck_artifacts.py` lines 12–17
**Apply to:** `test_crosscheck_entry_points.py` only (generate + GCC)

```python
cmd = [sys.executable, str(REPO_ROOT / "scripts" / "..."), ...]
proc = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True, check=False)
```

Never `shell=True`. Never interpolate GitHub `${{ }}` into workflow `run:` (and do not introduce a matrix).

### Stdout `RESULT:` token vs catalog YAML `status`
**Source:** four seed `main()` printers + `giant_component_fraction.py` lines 122–126 + D-01
**Apply to:** inventory markers, GCC assertions, CROSSCHECK.md CI column

CI gates **stdout**. Habitat/cluster/Ising YAML remain `status: executed`; epidemic YAML is `confirmed`; GCC YAML is `ready`. Inventory must **not** key off `status:`.

### Two-layer CONFIRMED coverage (keep both)
**Source:** `test_crosscheck_repro_regression.py` freeze fits + `crosscheck-repro.yml` live greps
**Apply to:** do not collapse either layer

- Pytest pins **fit functions** on frozen vectors (epidemic `NU_THEORY == 3.0` already exists).
- CI greps **full script stdout** for the four seeds.
- Inventory pytest asserts the **mapping** between CONFIRMED-capable scripts and those greps.
- GCC is pytest-only INCONCLUSIVE; not a fifth live CONFIRMED grep.

### Docs-only honesty (no hub regen)
**Source:** `docs/CROSSCHECK.md` `#run-mode-parity`; `dashboard/index.html` line 1884
**Apply to:** 04-01 docs task

Edit CROSSCHECK.md. Skip `build_crosscheck.py --apply`. Run `mkdocs build --strict`.

### Pickup path (do not duplicate the bundle)
**Source:** `.github/workflows/validate-schemas.yml` lines 19–23; `pyproject.toml` `testpaths`
**Apply to:** both new tests

New files under `tests/repo_smoke/` are collected automatically. Do **not** add `python -m pytest tests/repo_smoke` to `crosscheck-repro.yml`. Do **not** add `generate_crosscheck.py` as a CONFIRMED job.

### CHANGELOG Unreleased bullets
**Source:** `CHANGELOG.md` lines 10–16
**Apply to:** both plans, sequential so 04-02 appends after 04-01

---

## No Analog Found

| File / concern | Role | Data Flow | Reason |
|----------------|------|-----------|--------|
| TRUST-02 inventory algorithm (marker scan + `- name:` split + grep-count equality) | test | file-I/O | No existing test parses `.github/workflows/*.yml` as text. Implement from RESEARCH Pattern 1; copy only `REPO_ROOT` / `read_text` / `rglob` boilerplate. |
| PyYAML `on:` boolean-key pitfall | — | — | No repo test documents this. Encode as a comment + “do not `import yaml`” in the inventory file. |
| GCC live subprocess smoke | test | request-response | Closest is artifacts `--check`; GCC has no freeze-fit analog and must not copy cluster `collect_pooled_sizes()`. Subprocess the real stdlib script. |

Planner should use RESEARCH.md Pattern 1–2 for those algorithms, not invent a matrix, helper script, or YAML 1.2 dependency.

---

## Do not copy

| Anti-pattern | Source | Why |
|--------------|--------|-----|
| `_run_script` discarding stdout | `test_catalog_regression.py` lines 22–27 | 04-02 must assert `p-b-` / `RESULT: INCONCLUSIVE` on stdout |
| `collect_pooled_sizes()` in pytest | `test_crosscheck_repro_regression.py` line 66 | Live L=256×20 MC; D-08 forbids spreading it to GCC |
| `importlib` load of GCC | same file `_load_module` | Freeze-fit style; GCC has no CONFIRMED fit to pin |
| `yaml.safe_load` on workflows | RESEARCH pitfall 2 | `on:` → `True` |
| `--write` / `--all` in pytest | `generate_crosscheck.py` | Dirties `drafts/crosscheck/` or is noisy/slow |
| Duplicate epidemic freeze | D-06 | `test_epidemic_fss_fit_confirmed_on_reference_pcs` already exists |
| Fifth `grep -q "RESULT: CONFIRMED"` | D-03 | GCC cannot print it; do not “fix” the script |
| Actions `strategy.matrix` in `run:` | GitHub script-injection guidance | Keep static `run:` strings |
| Hub `--apply` for docs-only | D-11 | `#run-mode-parity` link already exists |
| YAML `status: confirmed` inventory key | D-01 | Would drop habitat/cluster/Ising (`executed`) |

---

## Metadata

**Analog search scope:** `tests/repo_smoke/`, `.github/workflows/`, `scripts/generate_crosscheck.py`, `scripts/build_crosscheck.py`, `repro/p-b-*/**/*.py`, `docs/CROSSCHECK.md`, `CHANGELOG.md`, `pyproject.toml`, `dashboard/index.html` (hub link only)
**Files scanned:** 14 analog/source files (3 existing smokes, 2 workflows, generator, GCC + 4 CONFIRMED printers, CROSSCHECK.md, CHANGELOG.md, pyproject.toml, build_crosscheck.py glob/read_text)
**Pattern extraction date:** 2026-08-26

**Planner constraints (from this map):**

1. 04-01 owns `test_crosscheck_confirmed_gates.py` + `docs/CROSSCHECK.md` + first CHANGELOG bullet.
2. 04-02 owns `test_crosscheck_entry_points.py` + second CHANGELOG bullet. Does not edit CROSSCHECK.md or the epidemic freeze file.
3. Sequential waves (CHANGELOG collision). Standard (non-TDD) plans — tests are the product and should be green on first write.
4. Verification: `python -m pytest tests/repo_smoke/test_crosscheck_confirmed_gates.py tests/repo_smoke/test_crosscheck_entry_points.py tests/repo_smoke/test_crosscheck_repro_regression.py::test_epidemic_fss_fit_confirmed_on_reference_pcs -x` then full `python -m pytest tests/repo_smoke -v --tb=short`; `mkdocs build --strict` after docs.

---

## PATTERN MAPPING COMPLETE

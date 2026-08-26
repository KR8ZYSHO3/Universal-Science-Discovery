# Phase 2 Pattern Map

Copy existing Crosscheck CONFIRMED patterns. Do not invent a new result protocol, CI gate, or regression style.

Canonical CONFIRMED analog for FSS ν-fit: `repro/p-b-habitat-percolation-ecology-fss/simulate_percolation_fss.py` (Phase 1 PR #298). Supporting analogs: cluster exponent (RESULT + CI grep; pooled seeds), Ising EWI (RESULT print + README exit-code honesty).

`scripts/build_crosscheck.py --check` does **not** read `RESULT: CONFIRMED`. It only diffs generated hub/index/explainer artifacts against `protocols-catalog/`. CONFIRMED is a **stdout contract** grepped by `.github/workflows/crosscheck-repro.yml`.

---

## File Classification

| Target file | Role | Analog file | What to copy |
|---|---|---|---|
| `C:\Projects\Universal-Science-Discovery-git\repro\p-b-percolation-epidemiology-fss\epidemic_percolation_fss.py` | Canonical Python repro (source of truth) | `repro/p-b-habitat-percolation-ecology-fss/simulate_percolation_fss.py` | Module constants (`PC_INF` analog, `NU_THEORY`, `NU_TOLERANCE`); **signed** `fit_nu` returning `(nu, r2, sign_ok)`; `passed = sign_ok and rel_err <= NU_TOLERANCE`; stdout header + per-size line + `RESULT: CONFIRMED` / `INCONCLUSIVE (...)`; `return 0` always; `random.Random(seed)` per instance |
| same | RESULT line wording | `cluster_size_exponent.py` `main()` / `ising_critical_slowing.py` `main()` | Exact `print(f"RESULT: {'CONFIRMED' if passed else 'INCONCLUSIVE (...hint...)'}")` so CI `grep -q "RESULT: CONFIRMED"` works |
| `C:\Projects\Universal-Science-Discovery-git\tests\repo_smoke\test_crosscheck_repro_regression.py` | Fast decision-logic pin | `test_percolation_fss_fit_confirmed_on_reference_pcs` in that file | `_load_module` from repro path; **fixed** `pcs` vector from a documented CONFIRMED run; call `fit_nu`; assert `sign_ok`, `rel_err <= NU_TOLERANCE`, `r2 > 0`. Do **not** copy cluster’s live `collect_pooled_sizes()` (full MC in pytest) |
| same | Optional extra pin | `test_ising_ewi_fit_confirmed_on_reference_variances` | Same load-module + frozen numeric inputs if epidemic adds extra gates (monotonicity of mean p_c vs N) |
| `.github/workflows/crosscheck-repro.yml` | CI CONFIRMED grep | Same file, habitat / cluster / Ising jobs | Change epidemic step from bare `python ...` to `tee` + `grep -q "RESULT: CONFIRMED"`. `networkx` already installed |
| `protocols-catalog/physics-epidemiology/p-b-percolation-epidemiology-fss.yaml` | Catalog fields that drive hub/explainers | `protocols-catalog/physics-ecology/p-b-habitat-percolation-ecology-fss.yaml` + `schemas/protocol.yaml` | Keep required schema keys; **rewrite `experimental_design` / `statistical_analysis_plan` / `null_hypothesis` / `estimated_runtime` to match the actual signed log-log + theoretical p_c(∞)** (habitat honesty). Bump `last_reviewed`. Optional: `status: confirmed` (schema allows it; Phase 1 left CONFIRMED protocols at `executed`) |
| `repro/p-b-percolation-epidemiology-fss/run_crosscheck.ipynb` | Demo tier (Colab) | Already the epidemic demo; generator analog is `scripts/crosscheck_browser.py` `COLAB_NOTEBOOK` + `colab_section()` in `generate_repro_index_pages.py` | Keep 3-cell clone → `pip -r` → `python epidemic_percolation_fss.py`. Do **not** add a JS browser runner (epidemic needs networkx). After YAML edits, `python scripts/build_crosscheck.py --apply` so `index.html` Colab note stays aligned |
| `repro/p-b-percolation-epidemiology-fss/README.md` | Human run instructions | Ising README (exit-code honesty) + habitat README (bridge link + one command) | Bridge relative link; `pip install -r` + `python epidemic_percolation_fss.py`; **“Exit code 0 always; inspect stdout for CONFIRMED vs INCONCLUSIVE”** (habitat README claims exit 1 on falsify but Python always returns 0 — do not copy that lie) |
| `repro/p-b-percolation-epidemiology-fss/index.html` | Generated Pages landing | Habitat `index.html` is **browser**; epidemic is **Colab** — both produced by `generate_repro_index_pages.py` | Do not hand-edit. After protocol YAML changes: `python scripts/build_crosscheck.py --apply`. `--check` fails if landing/hub/explainer drift |
| `scripts/build_crosscheck.py` | Artifact regen / drift gate | n/a (already exists) | After YAML/title/prediction/status edits: `--apply`. CI/pytest `test_crosscheck_artifacts_up_to_date` runs `--check`. **No CONFIRMED interaction** |
| `repro/p-b-percolation-epidemiology-fss/requirements.txt` | Declared deps | already `networkx>=3.0` | Keep. Habitat analog is `# No external dependencies` — not applicable |

---

## Analog excerpts

### 1. Habitat signed-delta `fit_nu` (copy this shape)

File: `C:\Projects\Universal-Science-Discovery-git\repro\p-b-habitat-percolation-ecology-fss\simulate_percolation_fss.py`

Constants + theoretical p_c(∞) (epidemic should add `PC_INF = 1 / (MEAN_DEGREE - 1)` instead of using `pcs[-1]`):

```python
PC_INF = 0.59274621
NU_THEORY = 4 / 3
NU_TOLERANCE = 0.15
SIZES = [16, 32, 64, 128]
TRIALS_PER_P = 350
```

Signed log-log fit (the Phase 1 precision pass). Epidemic currently returns only `(nu, r2)` and uses last-N as p_c(∞) — replace with this pattern, swapping `L` for `N`:

```python
def fit_nu(sizes: List[int], pcs: List[float]) -> Tuple[float, float, bool]:
    """Fit p_c(inf) - p_c(L) ~ L^(-1/nu) via log-log linear regression."""
    import math

    deltas = [PC_INF - pc for pc in pcs]
    sign_ok = all(d > 0 for d in deltas)
    xs = [math.log(L) for L in sizes]
    ys = [
        math.log(d if sign_ok else abs(pc - PC_INF) + 1e-9)
        for d, pc in zip(deltas, pcs)
    ]
    n = len(xs)
    x_mean = sum(xs) / n
    y_mean = sum(ys) / n
    num = sum((x - x_mean) * (y - y_mean) for x, y in zip(xs, ys))
    den = sum((x - x_mean) ** 2 for x in xs)
    slope = num / den if den else 0.0
    nu = -1 / slope if slope else float("inf")
    ss_res = sum((y - (y_mean + slope * (x - x_mean))) ** 2 for x, y in zip(xs, ys))
    ss_tot = sum((y - y_mean) ** 2 for y in ys)
    r2 = 1 - ss_res / ss_tot if ss_tot else 0.0
    return nu, r2, sign_ok
```

Decision + print (copy; swap theory numbers and the INCONCLUSIVE hint to `SEEDS_PER_N`):

```python
    nu, r2, sign_ok = fit_nu(SIZES, pcs)
    rel_err = abs(nu - NU_THEORY) / NU_THEORY
    passed = sign_ok and rel_err <= NU_TOLERANCE

    print()
    if not sign_ok:
        print("Sign check: p_c estimates crossed p_c(inf) — increase TRIALS_PER_P")
    print(f"Fitted nu = {nu:.4f}  (R² = {r2:.4f})")
    print(f"Relative error vs 4/3 = {100 * rel_err:.1f}%  (tolerance {100 * NU_TOLERANCE:.0f}%)")
    print(f"RESULT: {'CONFIRMED' if passed else 'INCONCLUSIVE (increase TRIALS_PER_P for higher precision)'}")
    return 0
```

Seeding analog (per-size, not a global RNG):

```python
        pc = estimate_pc(L, TRIALS_PER_P, seed=42 + i * 1000)
```

Habitat JS demo (`simulate_percolation_fss.js` `fitNu`) mirrors the same signed deltas; **do not port to epidemic** — demo tier is Colab.

**Sign-direction note for epidemic:** habitat 2D site p_c(L) is expected **below** p_c(∞) (`PC_INF - pc > 0`). Mean-field ER bond p_c(N) vs 1/(⟨k⟩−1) may sit consistently **above** or **below** depending on the 50% giant-fraction estimator. If all deltas have the same sign but opposite habitat’s, copy the **gate** (`all same sign`) not the **literal** `PC_INF - pc > 0`. A one-line generalization: `sign_ok = all(d > 0 for d in deltas) or all(d < 0 for d in deltas)` then `ys = log(|d|)`. Do not invent a new fitter (still OLS log-log, ν = −1/slope).

**Do not keep** current epidemic `fit_nu`:

```python
    pc_inf = pcs[-1]
    ys = [math.log(abs(pc - pc_inf) + 1e-9) for pc in pcs]
    return nu, r2
```

Using the largest N as p_c(∞) zeros the last residual and is the likely reason baseline ν = 0.239 / 76.1% error in `02-CONTEXT.md`.

---

### 2. `RESULT: CONFIRMED` print format (CI contract)

All CONFIRMED repros print a single line containing the exact substring `RESULT: CONFIRMED` (grep is not anchored). Pattern:

Habitat FSS:

```python
    print(f"RESULT: {'CONFIRMED' if passed else 'INCONCLUSIVE (increase TRIALS_PER_P for higher precision)'}")
```

Cluster exponent:

```python
    print(f"RESULT: {'CONFIRMED' if passed else 'INCONCLUSIVE (adjust P or L for clearer scaling)'}")
```

Ising EWI (same substring; slightly more branching):

```python
    if passed:
        result = "CONFIRMED"
    elif gamma_ok or ewi_mono:
        result = "INCONCLUSIVE (increase EQ_SWEEPS_NEAR_TC for higher precision)"
    else:
        result = "INCONCLUSIVE (increase EQ_SWEEPS_NEAR_TC for higher precision)"
    print(f"RESULT: {result}")
```

Epidemic **already** prints this shape (`increase SEEDS_PER_N for stability`) — keep the token `RESULT: CONFIRMED` after the fit actually passes. Exit code stays 0 either way.

---

### 3. CI grep job YAML block

File: `C:\Projects\Universal-Science-Discovery-git\.github\workflows\crosscheck-repro.yml`

Install analog (already present — do not add a second pip):

```yaml
      - name: Install dependencies
        run: pip install networkx
```

CONFIRMED jobs to clone (habitat + cluster + ising). Epidemic job today is ungated:

```yaml
      - name: Habitat percolation FSS (expect CONFIRMED)
        run: |
          python repro/p-b-habitat-percolation-ecology-fss/simulate_percolation_fss.py | tee /tmp/fss.out
          grep -q "RESULT: CONFIRMED" /tmp/fss.out

      - name: Cluster size exponent (expect CONFIRMED)
        run: |
          python repro/p-b-habitat-percolation-ecology-cluster-exponent/cluster_size_exponent.py | tee /tmp/cluster.out
          grep -q "RESULT: CONFIRMED" /tmp/cluster.out

      - name: Epidemic percolation FSS
        run: python repro/p-b-percolation-epidemiology-fss/epidemic_percolation_fss.py

      - name: Ising social dynamics EWI (expect CONFIRMED)
        run: |
          python repro/p-b-ising-social-dynamics-ewi/ising_critical_slowing.py | tee /tmp/ising.out
          grep -q "RESULT: CONFIRMED" /tmp/ising.out
```

Replace the epidemic step with the same `tee` + `grep -q` pattern:

```yaml
      - name: Epidemic percolation FSS (expect CONFIRMED)
        run: |
          python repro/p-b-percolation-epidemiology-fss/epidemic_percolation_fss.py | tee /tmp/epidemic.out
          grep -q "RESULT: CONFIRMED" /tmp/epidemic.out
```

Only add this **after** a documented local run prints `RESULT: CONFIRMED`. Path filters already include `repro/**`.

---

### 4. Regression test: signature and how it pins a known input

File: `C:\Projects\Universal-Science-Discovery-git\tests\repo_smoke\test_crosscheck_repro_regression.py`

Shared loader (reuse; do not duplicate):

```python
def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod
```

**Copy this test, not the cluster one.** Habitat pins frozen p_c estimates from a dated CONFIRMED run — pytest does not re-run Monte Carlo:

```python
def test_percolation_fss_fit_confirmed_on_reference_pcs() -> None:
    mod = _load_module(
        "simulate_percolation_fss",
        REPO_ROOT / "repro/p-b-habitat-percolation-ecology-fss/simulate_percolation_fss.py",
    )
    # Reference p_c estimates at TRIALS_PER_P=350, seed=42 (2026-06-22 CONFIRMED run).
    pcs = [0.59080, 0.59059, 0.59268, 0.59179]
    nu, r2, sign_ok = mod.fit_nu(mod.SIZES, pcs)
    rel_err = abs(nu - mod.NU_THEORY) / mod.NU_THEORY
    assert sign_ok, "expected all p_c below p_c(inf) for signed FSS fit"
    assert rel_err <= mod.NU_TOLERANCE, f"nu={nu:.4f} err={100 * rel_err:.1f}%"
    assert r2 > 0.0
```

Epidemic analog to add (names only — numbers come from a real CONFIRMED run):

```python
def test_epidemic_fss_fit_confirmed_on_reference_pcs() -> None:
    mod = _load_module(
        "epidemic_percolation_fss",
        REPO_ROOT / "repro/p-b-percolation-epidemiology-fss/epidemic_percolation_fss.py",
    )
    # Reference mean p_c(N) at documented SEEDS_PER_N / SIZES / seed recipe (YYYY-MM-DD CONFIRMED run).
    pcs = [...]  # freeze mean_pcs printed by that run
    nu, r2, sign_ok = mod.fit_nu(mod.SIZES, pcs)
    rel_err = abs(nu - mod.NU_THEORY) / mod.NU_THEORY
    assert sign_ok
    assert rel_err <= mod.NU_TOLERANCE
    assert r2 > 0.0
```

**Do not copy** cluster’s live re-sim (too slow for ER N=5000 in repo_smoke):

```python
def test_cluster_exponent_fit_confirmed_on_pooled_reference() -> None:
    ...
    sizes = mod.collect_pooled_sizes()  # re-runs 20 × 256²
    tau, r2 = mod.fit_tau(sizes)
```

Ising analog (frozen series, not live MC) if extra gates are needed:

```python
def test_ising_ewi_fit_confirmed_on_reference_variances() -> None:
    ...
    temps = [2.65, 2.55, 2.45, 2.38, 2.33]
    variances = [0.011354, 0.022608, 0.038065, 0.074723, 0.150698]
    ...
    gamma, r2 = mod.fit_gamma(temps, scale_chi)
```

---

### 5. Protocol YAML fields that record outcome

Schema (`C:\Projects\Universal-Science-Discovery-git\schemas\protocol.yaml`): `status` enum is `[draft, ready, executed, confirmed, falsified]`. There is **no** `last_result` / `outcome` field. Outcome is:

1. stdout `RESULT: CONFIRMED` (CI)
2. optional `status: confirmed` (hub badge via `render_crosscheck_hub.py` `status_style`)
3. `experimental_design` / `statistical_analysis_plan` / `null_hypothesis` / `estimated_runtime` / `last_reviewed` describing the **actual** decision rule

Phase 1 CONFIRMED protocols still use `status: executed`. Copy that unless product wants the hub badge upgraded (then `--apply`).

Habitat FSS fields to mirror (decision-rule honesty):

```yaml
id: p-b-habitat-percolation-ecology-fss
status: executed
falsifiable_prediction: >
  ... nu within 15% of the 2D percolation value 4/3.
null_hypothesis: >
  ... or the fitted exponent differs from 4/3 by more than 15%.
experimental_design:
  - Run site percolation Monte Carlo on L×L square lattices for L ∈ {16, 32, 64, 128}.
  - For each L, estimate p_c using the crossing probability method (50% spanning threshold).
  - Record (L, p_c_estimate) pairs and fit p_c(L) = p_c_inf + c * L^(-1/nu) via log-linear regression.
  - Compare fitted nu to theoretical 4/3; accept if relative error ≤ 15%.
  - Document random seed, trial count, and confidence intervals in repro output.
statistical_analysis_plan: >
  Log-linear fit of (p_c(L) - p_c_inf) vs L with fixed p_c_inf = 0.59274621;
  report slope, R², and 95% CI on nu = -1/slope_exponent.
feasibility_tier: desktop
repro_bundle: repro/p-b-habitat-percolation-ecology-fss/
estimated_runtime: 4–8 minutes on a modern laptop (350 trials/p by default)
last_reviewed: "2026-06-21"
```

Epidemic YAML **today** still says bootstrap 10 seeds and nonlinear least squares; the script is OLS log-log with `SEEDS_PER_N = 5`. After precision pass, rewrite those bullets to match habitat: **fixed theoretical p_c(∞) = 1/(⟨k⟩−1)**, log-linear ν, accept if relative error ≤ documented tolerance, record seeds per N.

Hub/explainer **do** render `status`. Changing it (or title/prediction) without `--apply` fails `--check`:

```python
# scripts/build_crosscheck.py
# --check snapshots repro/*/index.html, dashboard/explainers, hub grid;
# regenerates; diffs; restores on failure. Does not run repro scripts.
```

```python
# tests/repo_smoke/test_crosscheck_artifacts.py
def test_crosscheck_artifacts_up_to_date() -> None:
    cmd = [sys.executable, str(REPO_ROOT / "scripts" / "build_crosscheck.py"), "--check"]
```

---

### 6. Colab notebook (demo tier — already exists)

`C:\Projects\Universal-Science-Discovery-git\repro\p-b-percolation-epidemiology-fss\run_crosscheck.ipynb`

```python
# cell 0 markdown: protocol id + “Canonical repro: epidemic_percolation_fss.py”
# cell 1:
!git clone --depth 1 https://github.com/KR8ZYSHO3/Universal-Science-Discovery.git
%cd Universal-Science-Discovery/repro/p-b-percolation-epidemiology-fss
# cell 2:
!pip install -q -r requirements.txt
!python epidemic_percolation_fss.py
```

Registry (`scripts/crosscheck_browser.py`): epidemic is **not** in `BROWSER_RUNNERS`; Colab is detected if `run_crosscheck.ipynb` exists. Habitat/cluster/ising are JS. Keep that split.

Generator note for Colab-only pages:

```python
    if has_colab:
        return """  <div class=\"note\">
    <strong>Open in Colab below</strong> for a one-click cloud run (requires networkx), or clone this
    folder for the canonical Python repro.
  </div>"""
```

---

### 7. README analog (copy Ising honesty)

Ising (`repro/p-b-ising-social-dynamics-ewi/README.md`):

```markdown
# p-b-ising-social-dynamics-ewi

Crosschecks [`b-ising-social-dynamics`](...) via 2D Ising critical slowing down near T_c.

```bash
python ising_critical_slowing.py
```

Exit code 0 always; inspect stdout for CONFIRMED vs INCONCLUSIVE.
```

Epidemic README already has pip + script; add the exit-code sentence. Habitat’s “exit 1 = falsified” is **not** what the Python does.

---

## Shared Patterns

### Python canonical vs browser/Colab demo

- **Canonical:** `*.py` in `repro/p-b-.../`. CI and citations run this.
- **Demo:** stdlib protocols get a JS port (`BROWSER_RUNNERS`) with a **reduced** trial budget (`TRIALS_PER_P = 120` vs 350). Epidemic **cannot** follow that (networkx). Demo = Colab notebook calling the same `.py`.
- Do not add a new runner framework. Shared UI is already `repro/_shared/crosscheck-runner.js` (unused for epidemic).

### RNG seeding

- Habitat FSS: `random.Random(seed)` inside `crossing_probability`; `estimate_pc(..., seed=42 + i * 1000)`; bisection steps use `seed + _`.
- Epidemic already: `er_graph(..., seed=N * 100 + s)` and `estimate_pc(g, seed=N * 100 + s + 7)`; `random.Random(seed)` inside bisection. Keep deterministic integer seeds. Increasing `SEEDS_PER_N` should extend `range(SEEDS_PER_N)` with the same formula so old instances remain comparable.
- Cluster: `random.Random(seed)` for `seed in range(SEEDS)`.
- Ising: single `SEED = 42` stream.
- No numpy RNG. No global `random.seed` without a `Random` instance.

### RESULT line grepped by CI

- Exact substring `RESULT: CONFIRMED`.
- Workflow: `python ... | tee /tmp/foo.out` then `grep -q "RESULT: CONFIRMED"`.
- `--check` / `build_crosscheck.py` never greps this.
- Schema `status: confirmed` is independent and currently unused by CONFIRMED seeds.

### No new frameworks

- Stdlib `math` OLS, not scipy/numpy curve_fit (despite epidemic YAML saying “nonlinear least squares”).
- `networkx` is the only extra dep (already in workflow + `requirements.txt`).
- Tests: `importlib.util.spec_from_file_location`, no pytest plugins.
- Do not add a results YAML sidecar; Phase 3 of `docs/CROSSCHECK.md` is not this work.

### Precision-pass recipe (from Phase 1 habitat/cluster)

1. Raise ensemble size (`TRIALS_PER_P` / `SEEDS` analog → `SEEDS_PER_N` and/or more graph instances).
2. Fit against **theoretical** infinite-size constant, not the largest simulated point.
3. Signed (consistent-direction) log-log; fail CONFIRMED if signs cross.
4. Document one local CONFIRMED stdout (ν, R², % error, params).
5. Freeze those mean p_c values in `test_*_fit_confirmed_on_reference_pcs`.
6. Add CI grep.
7. Align protocol YAML design/runtime with the new defaults; `--apply` if generated pages change.

---

## No Analog Found

Things epidemic FSS needs that **habitat lattice FSS does not have** (keep/extend existing epidemic code; do not invent a second stack):

| Need | Habitat analog? | Where it already lives / what to do |
|---|---|---|
| Erdős–Rényi graphs | No (square lattice site occupation) | Keep `er_graph()` → `nx.erdos_renyi_graph(n, p_edge, seed=seed)` with `p_edge = mean_k / (n - 1)` |
| `networkx` | No (`requirements.txt` is stdlib-only) | Keep `networkx>=3.0`; CI `pip install networkx`; ImportError → exit 2 |
| Theoretical p_c = 1/(⟨k⟩−1) | Different constant (`PC_INF = 0.59274621` 2D site) | **Copy the role of `PC_INF`**, not the number. For `MEAN_DEGREE = 6`, `PC_INF = 1/5 = 0.2` (Newman 2002 transmissibility / bond threshold on ER). Protocol already cites `doi: 10.1103/PhysRevE.66.016128` |
| Mean over **graph instances** | Habitat means over **occupation trials** on one lattice geometry (`TRIALS_PER_P`) | Epidemic already: `SEEDS_PER_N` graphs per N, `mean_pc = sum(estimates)/len(estimates)`. Raise this (context baseline is 5). Cluster analog for pooling is `SEEDS = 20` independent lattices, not graphs |
| Bond percolation on a fixed graph | Habitat is **site** percolation / spanning cluster | Keep `giant_fraction` (keep edge w.p. p, giant component / N, bisection to 50%) |
| Mean-field ν = 1 | Habitat ν = 4/3 | Already `NU_THEORY = 1.0`; tolerance 0.25 in YAML/null. Tighten only if a sweep supports it |
| Colab demo (no JS) | Habitat has in-browser JS | Already `run_crosscheck.ipynb` + generated Colab button. No analog JS giant-component runner |
| Bisection on giant fraction vs crossing probability | Different estimator, same **binary-search p_c** shape | Copy habitat’s outer FSS loop, not `spans()` |
| Print `delta=` vs theory | Habitat prints `delta={pc - PC_INF:+.5f}` | Epidemic prints seeds only. Add `delta=` vs `PC_INF` so sign problems are visible in CI logs |

**Not missing:** RESULT print, CI workflow file, Colab notebook, `SEEDS_PER_N` loop, `grep` job *slot* (only the grep is missing).

---

## Planner constraints (from this map)

- Change `fit_nu` to habitat signed + theoretical `PC_INF` before raising seeds blindly; current last-N `pc_inf` is structurally biased.
- Sweep `SEEDS_PER_N` / N grid under the existing runtime budget (largest N=5000) **before** committing defaults and CI grep.
- Pin regression inputs from a real CONFIRMED stdout; do not re-simulate ER graphs in pytest.
- After YAML edits: `python scripts/build_crosscheck.py --apply` then `--check`.
- Do not add scipy, numpy, JS, or a new outcome schema field.

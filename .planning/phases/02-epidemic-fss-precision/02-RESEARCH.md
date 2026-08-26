# Phase 2: Epidemic FSS precision - Research

**Researched:** 2026-08-26
**Domain:** Mean-field bond percolation finite-size scaling on Erdős–Rényi graphs (Crosscheck protocol `p-b-percolation-epidemiology-fss`)
**Confidence:** HIGH

<user_constraints>
## User Constraints (from CONTEXT.md)

**CRITICAL:** If CONTEXT.md exists from /gsd-discuss-phase, copy locked decisions here verbatim. These MUST be honored by the planner.

Verbatim from `.planning/phases/02-epidemic-fss-precision/02-CONTEXT.md`:

### Goal

Fourth seed Crosscheck protocol CONFIRMED — bond percolation FSS on Erdős–Rényi graphs (ν ≈ 1 mean-field).

### Baseline (default settings)

```
SEEDS_PER_N=5, SIZES=[200,500,1000,2000,5000], MEAN_DEGREE=6
Fitted nu = 0.239, R² = 0.62, error vs 1.0 = 76.1%
RESULT: INCONCLUSIVE
```

### Prior art in repo

Habitat FSS pass (#298): `TRIALS_PER_P=350`, signed `fit_nu()` when all p_c < p_c(∞). Same pattern likely applies:
- Increase `SEEDS_PER_N` and/or graph instances per N
- Signed log-log fit on p_c(∞) − p_c(N) ~ N^(−1/ν)
- Fixed-input regression test once stable

### Files

- `repro/p-b-percolation-epidemiology-fss/epidemic_percolation_fss.py`
- `protocols-catalog/.../p-b-percolation-epidemiology-fss.yaml`
- Colab path (networkx) — verify after Python CONFIRMED

### Constraints

- `networkx` required — CI already installs it in crosscheck-repro.yml
- Runtime budget: largest N=5000; sweep before committing heavy defaults
- Browser demo may not exist — Colab is demo tier

### Success

- `RESULT: CONFIRMED` at documented tolerance
- Regression test in `test_crosscheck_repro_regression.py`
- CI grep in `crosscheck-repro.yml`

### Locked Decisions
- Python is canonical; browser/Colab is demo tier. [VERIFIED: `.planning/PROJECT.md`, `02-CONTEXT.md`]
- Do not add an in-browser JS runner for this protocol (networkx is not stdlib). Colab already exists. [VERIFIED: `scripts/crosscheck_browser.py` — epidemic is absent from `BROWSER_RUNNERS`]
- Keep `SIZES` including N=5000 unless a sweep proves a cheaper set still confirms. Sweep before committing heavy `SEEDS_PER_N`. [VERIFIED: `02-CONTEXT.md`]
- CROSS-04 is in scope for Phase 2 even though PROJECT.md WORK-01 says epidemic CONFIRMED should unblock the Crosscheck full loop — ROADMAP still requires CROSS-04 here. Do not defer the protocol. [VERIFIED: `.planning/ROADMAP.md`, `.planning/PROJECT.md`]
- No marketing, DNS, arXiv, or catalog waves in this phase. [VERIFIED: `02-CONTEXT.md` phase prompt / `.planning/ROADMAP.md` Deferred]

### Claude's Discretion
- Exact `SEEDS_PER_N` / trials-per-mid after a timed sweep
- Whether `NU_TOLERANCE` stays 0.25 or tightens toward habitat's 0.15 once the estimator is correct
- Critical-point estimator details (order-parameter threshold vs susceptibility peak) provided the fit is signed, uses theoretical p_c(∞), and is documented
- Whether protocol YAML `status` becomes `confirmed` in this phase (schema allows it; all four seeds are still `executed`)
- Pin vs floating `networkx` in CI (`pip install networkx` is currently unpinned)

### Deferred Ideas (OUT OF SCOPE)
- Marketing, DNS, `usdr.science`, arXiv [VERIFIED: `.planning/ROADMAP.md`]
- Catalog waves / generate-and-promote new bridges (Phase 3 CROSS-06)
- Browser/JS parity matrix (Phase 3 CROSS-07)
- Unified CONFIRMED gates for *all* protocols and repo_smoke expansion for new entry points (Phase 4 TRUST-02/03) — *except* the epidemic grep + epidemic regression test required by this phase's success criteria
- Closing WORK-01 (outcome → catalog/hub status for every seed) as a full loop; a YAML `status:` bump for epidemic only is optional if the protocol file is already being edited
</user_constraints>

<phase_requirements>
## Phase Requirements

| ID | Requirement | How this phase addresses it | Priority |
|----|-------------|------------------------------|----------|
| **CROSS-04** | Epidemic FSS CONFIRMED | `epidemic_percolation_fss.py` prints `RESULT: CONFIRMED`; fixed-input ν regression test; `crosscheck-repro.yml` greps CONFIRMED for epidemic | Must |
| ROADMAP-2.1 | Parameter sweep + precision pass | Signed `fit_nu`, theoretical p_c(∞), seed/size sweep under CI runtime budget | Must |
| ROADMAP-2.2 | Regression test + CI CONFIRMED gate | Mirror habitat/Ising/cluster tests in `tests/repo_smoke/test_crosscheck_repro_regression.py` | Must |
| ROADMAP-2.3 | Colab/notebook path | Verify `run_crosscheck.ipynb` still runs the canonical Python script; no new JS runner | Must (verify, not rewrite) |

Traceability: `.planning/REQUIREMENTS.md` lists CROSS-04 as the sole Phase 2 requirement. [VERIFIED]
</phase_requirements>

<architectural_responsibility_map>
## Architectural Responsibility Map

This is a **single-tier scientific CLI simulation** with a static demo face. It is not a web application. Do not assign capabilities to Browser/API/CDN tiers that do not own the decision.

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| Graph generation + bond percolation + ν fit + `RESULT:` line | CLI / Python (canonical) | — | CI and researchers run `epidemic_percolation_fss.py`; Python is source of truth [VERIFIED: `PROJECT.md` Key Decisions] |
| CONFIRMED gate | CI (`crosscheck-repro.yml` grep) | Local pytest for *fit logic* | Habitat/cluster/Ising already use stdout grep; epidemic currently runs without grep [VERIFIED: `.github/workflows/crosscheck-repro.yml`] |
| Fixed-input fit regression | `tests/repo_smoke/` (pytest) | — | Does **not** re-simulate graphs; loads `fit_nu` with frozen p_c vector [VERIFIED: `tests/repo_smoke/test_crosscheck_repro_regression.py`] |
| Protocol metadata / hub landing page | Catalog YAML → generated static HTML | GitHub Pages | `build_crosscheck.py` regenerates `repro/.../index.html` from YAML; not a runtime server [VERIFIED: `scripts/build_crosscheck.py`, `scripts/generate_repro_index_pages.py`] |
| One-click demo | Colab notebook | Static `index.html` | Epidemic has Colab, not a browser runner [VERIFIED: `scripts/crosscheck_browser.py`, `run_crosscheck.ipynb`] |
| Artifact drift check | `build_crosscheck.py --check` | `validate.yml` / `build-graph.yml` | Already shipped in Phase 1 (CROSS-05). Touching protocol YAML requires `--apply` | [VERIFIED: `scripts/build_crosscheck.py`] |

**Single-tier application — scientific decision logic resides in the Python repro.** Hub/Colab are discovery surfaces, not alternate physics engines.
</architectural_responsibility_map>

<research_summary>
## Summary

Phase 2 is not “turn up `SEEDS_PER_N` until ν luckily hits 1.” The current `INCONCLUSIVE` (ν = 0.239, 76% error) is **reproduced by a fit bug even on exact ν = 1 synthetic data**. `fit_nu` sets `pc_inf = pcs[-1]`, so the last size contributes `log(1e-9) ≈ −20.7` and the slope is garbage. Habitat already solved this class of bug: **fixed theoretical p_c(∞)** + **signed log-log fit**. [VERIFIED: local Python 3.12.6 + networkx 3.6 diagnostic, 2026-08-26; `simulate_percolation_fss.py` `fit_nu`]

A second, larger issue: the epidemic script’s operational threshold is **giant-component fraction ≥ 0.5**. For Poisson ER that is **not** p_c. Infinite-N giant fraction S = 0.5 occurs at remaining mean degree λ\* = 2 ln 2 ≈ 1.386, i.e. p\* = 2 ln 2 / ⟨k⟩ ≈ 0.231 for ⟨k⟩ = 6 — well above the percolation threshold 1/⟨k⟩ ≈ 0.167. Local Monte Carlo (20 seeds, N ∈ {200,500,1000,2000}) found p_{S=0.5}(N) already pinned at ≈ 0.231 with **no measurable FSS** (mixed signs vs p\*, R² = 0.013). More seeds cannot confirm ν = 1 with this estimator. [VERIFIED: same local diagnostic]

The scientifically valid analog of habitat FSS is a **critical-point** estimator. Using bisection until S ≥ N^{−1/3} (mean-field order parameter at p_c: β/ν̄ = 1/3) produced p_c(N) ↓ toward 1/6 from above, fitted ν̄ = 2.68, R² = 0.93, vs theoretical **ν̄ = 3** (10.8% error — inside a 15–25% band). Literature: ER critical window ~ N^{−1/3} (Bollobás 1984); mean-field ν_lattice = 1/2, d_u = 6 ⇒ ν̄ = d_u ν = 3. Catalog/protocol ν = 1 is the **chemical-distance / Bethe** exponent, incorrectly inserted into |Δp| ~ N^{−1/ν}. [VERIFIED: local diagnostic; CITED: Bollobás 1984 via Borgs et al.; Newman 2002 T_c formula]

**Primary recommendation:** Treat this as a **methodology pass** (precedent: cluster-exponent 01-03), not a trophy hunt. (1) `fast_gnp_random_graph` + more averaging. (2) Theoretical `PC_INF = 1/⟨k⟩` for Poisson ER. (3) Critical estimator (recommend S ≥ N^{−1/3}). (4) Signed `fit_nu` matching habitat’s `(nu, r2, sign_ok)` contract. (5) Set `NU_THEORY = 3.0` (volume FSS ν̄) and document that catalog ν = 1 is a different exponent — do **not** confirm ν = 1 by hiding the estimator. Then freeze a reference p_c vector, add the pytest, and grep CONFIRMED in CI.
</research_summary>

<standard_stack>
## Standard Stack

The established libraries/tools for this domain (this repo + NetworkX ecosystem):

### Core
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| CPython | 3.11 in `crosscheck-repro.yml`; 3.12 in `validate-schemas.yml`; local 3.12.6 | Run repro + pytest | CI already locked to 3.11 for the smoke job [VERIFIED: `.github/workflows/crosscheck-repro.yml`] |
| networkx | `>=3.0` in bundle `requirements.txt`; locally 3.6; CI `pip install networkx` **unpinned** | ER graphs + connected components | Protocol requires it; do not hand-roll G(n,p) [VERIFIED: `repro/p-b-percolation-epidemiology-fss/requirements.txt`] |
| pytest | unpinned in `validate-schemas.yml` | Repo smoke including Crosscheck fit regressions | Already how habitat/Ising/cluster fits are locked [VERIFIED: `.github/workflows/validate-schemas.yml`] |
| stdlib `random` / `math` | — | Seeds + log-log OLS | Habitat/Ising/cluster do **not** use numpy for the fit [VERIFIED: `simulate_percolation_fss.py`] |

### Supporting
| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| PyYAML | CI validate/build | Protocol YAML | Only if protocol metadata changes; then `build_crosscheck.py --apply` |
| Google Colab (hosted) | n/a | Demo tier | After Python CONFIRMED; notebook already `!python epidemic_percolation_fss.py` [VERIFIED: `run_crosscheck.ipynb`] |

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| `nx.erdos_renyi_graph` (current) | `nx.fast_gnp_random_graph` | **Use the latter.** Docs: `erdos_renyi_graph` is O(n²); sparse k=6, n=5000 is 25× slower (0.51 s vs 0.021 s) [VERIFIED: local timing; CITED: NetworkX 3.6.1 docs] |
| Poisson ER G(n,p) | Random regular / configuration model | Regular graphs have T_c = 1/(k−1) = 0.2; ER Poisson has T_c = 1/⟨k⟩. Prompt’s “1/(k−1) for ER” is the regular-graph formula. **Keep ER** (protocol says Erdős–Rényi) and use 1/⟨k⟩ [CITED: Newman 2002 Eq. (23)] |
| Log-log OLS (habitat) | `scipy.optimize.curve_fit` NLS | Protocol YAML *says* NLS; habitat *does* log-linear. Stay with habitat log-linear; fix the YAML to match. Do not add scipy. |
| `nx.connected_components` | Hand-rolled Union-Find | Habitat cluster-exponent already has Union-Find for lattices; for graphs, NetworkX BFS CC is O(n+m) and documented. Don’t hand-roll. [CITED: NetworkX `connected_components` notes] |
| In-browser JS | Canonical Python | No NetworkX in JS; Phase 3 owns parity. |

**Installation (repro bundle):**
```bash
pip install -r repro/p-b-percolation-epidemiology-fss/requirements.txt
python repro/p-b-percolation-epidemiology-fss/epidemic_percolation_fss.py
```

**CI (already):**
```yaml
pip install networkx   # recommend: pip install "networkx>=3.0"
```
</standard_stack>

<architecture_patterns>
## Architecture Patterns

### System Architecture Diagram

```
                    seeds, SIZES, MEAN_DEGREE (module constants)
                                    |
                                    v
                    +--------------------------------+
                    | er_graph(N, k, seed)           |
                    | nx.fast_gnp_random_graph       |
                    +----------------+---------------+
                                    |
                                    v
                    +--------------------------------+
                    | estimate_pc(N): bisection      |
                    |   mid → mean giant fraction    |
                    |   until S >= S_thresh(N)       |---- NetworkX connected_components
                    +----------------+---------------+
                                    |
                                    v
                    p_c_hat(N) averaged over SEEDS_PER_N
                                    |
                                    v
                    +--------------------------------+
                    | fit_nu(sizes, pcs)             |
                    | signed log-log vs PC_INF       |
                    | nu = -1/slope; R²; sign_ok     |
                    +----------------+---------------+
                                    |
                    +-------+-------+--------+
                    | sign_ok AND |nu-nu_th| <= tol ?
                    | yes → RESULT: CONFIRMED
                    | no  → RESULT: INCONCLUSIVE
                    +-------+-------+--------+
                                    |
                    CI grep "RESULT: CONFIRMED"
                    pytest fit_nu(frozen pcs)
                    (optional) protocol YAML status: confirmed
                                    |
                    if YAML/title/runtime changed:
                      python scripts/build_crosscheck.py --apply
```

### Recommended Project Structure

Do **not** create a new package. Stay inside the existing repro bundle + one test module:

```
repro/p-b-percolation-epidemiology-fss/
├── epidemic_percolation_fss.py   # canonical (edit)
├── requirements.txt              # networkx>=3.0 (keep)
├── run_crosscheck.ipynb          # Colab; verify after Python CONFIRMED
├── index.html                    # GENERATED — do not hand-edit if YAML changes
└── README.md
protocols-catalog/physics-epidemiology/p-b-percolation-epidemiology-fss.yaml
tests/repo_smoke/test_crosscheck_repro_regression.py   # add epidemic test
.github/workflows/crosscheck-repro.yml                 # grep CONFIRMED
```

### Pattern 1: Habitat-style signed FSS fit (copy this contract)

**What:** Fit |p_c(∞) − p_c(L)| ~ L^{−1/ν} with **fixed theoretical p_c(∞)**. Fail the sign check rather than taking `abs()`.
**When to use:** Always for CROSS-04. Current epidemic `pcs[-1]` substitution is the primary numerical bug.
**Example:** habitat `fit_nu` [VERIFIED: `repro/p-b-habitat-percolation-ecology-fss/simulate_percolation_fss.py`]

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
    # ... OLS slope → nu = -1/slope, r2 ...
    return nu, r2, sign_ok
```

Epidemic should **generalize the sign**, not copy `PC_INF - pc` blindly: local data for the critical estimator has **all p_c(N) > 1/⟨k⟩** (approaching from above). Habitat 2D wrapping typically sits slightly *below* 0.5927. Recommend:

```python
deltas = [pc - PC_INF for pc in pcs]   # ER pseudocritical from above
sign_ok = all(d > 0 for d in deltas)
```

If signs mix → `RESULT: INCONCLUSIVE` (increase seeds), same message pattern as habitat’s “increase TRIALS_PER_P”.

### Pattern 2: Average, then bisect (habitat crossing probability)

**What:** Habitat does not bisect a single noisy spanning event. It averages `TRIALS_PER_P=350` occupancy realizations at each mid, then bisects the **mean** crossing probability (nearly monotone).
**When to use:** Epidemic currently bisects **one** bond sample on **one** graph per mid (24 noisy non-monotone queries). That is biased.
**Fix:** Generate `SEEDS_PER_N` graphs once per N; at each mid, average giant fraction across those graphs (and optionally multiple bond samples). Bisect the mean.

### Pattern 3: Critical-window estimator, not S = 0.5

**What:** At p_c, mean-field order parameter S ~ N^{−β/ν̄} = N^{−1/3}. Bisect until S ≥ N^{−1/3} tracks p_c(N) → 1/⟨k⟩ with ν̄ ≈ 3.
**When to use:** Default recommendation for CROSS-04. S = 0.5 is a supercritical isosurface with no FSS in N = 200–5000.
**Do not** silently keep S = 0.5 and change only pc_inf — that confirms nothing.

### Anti-Patterns to Avoid
- **`pc_inf = pcs[-1]`:** Last point is log(1e-9); synthetic ν=1 data yields ν ≈ 0.23 — matches the locked baseline 0.239. [VERIFIED: local diagnostic]
- **`abs()` hiding sign errors:** Habitat still has an abs fallback for the log, but `passed` requires `sign_ok`. Epidemic currently has no sign check at all.
- **Trophy-hunting ν = 1** with a supercritical estimator or a changed target that is not written down.
- **Adding numpy/scipy** for one OLS fit.
- **Hand-editing generated `index.html`** instead of `build_crosscheck.py --apply`.
- **Exit-code CONFIRMED:** index.html claims exit 0/1; the script always returns 0. CI greps **stdout**. Keep that contract. [VERIFIED: `epidemic_percolation_fss.py` `return 0`; `index.html` lines 65–66]
</architecture_patterns>

<dont_hand_roll>
## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| G(n,p) ER graph | Nested Python loops over n² pairs | `nx.fast_gnp_random_graph(n, p, seed=...)` | O(n+m) sparse algorithm; `erdos_renyi_graph` is O(n²) alias of `gnp_random_graph` [CITED: NetworkX 3.6.1 `erdos_renyi_graph` notes] |
| Giant component | Custom BFS/DFS | `max(nx.connected_components(G), key=len)` | Documented O(n+m); habitat already hand-rolls DFS only because it is a lattice without NetworkX |
| Log-log ν fit | New fitting library | Copy habitat OLS (stdlib) | Same decision rule as CROSS-01; pytest loads the function |
| Bond percolation | NetworkX `subgraph` copies + extra deps | Keep current “new Graph, add edges with prob p” **or** Union-Find on occupied edges if timing requires it | Current CC is ~10 ms at N=5000 [VERIFIED: local timing]. Sweep first; only micro-optimize if CI budget fails |
| Theoretical T_c | Guess 1/(k−1) for ER | Newman generating-function T_c = ⟨k⟩ / ⟨k(k−1)⟩ → **1/⟨k⟩ for Poisson** | Prompt’s 1/(k−1) is random-regular [CITED: Newman 2002 Eq. (23)] |
| Browser demo | Port NetworkX to JS | Existing Colab notebook | `BROWSER_RUNNERS` intentionally omits epidemic [VERIFIED: `scripts/crosscheck_browser.py`] |

**Key insight:** This repo already has a working FSS Crosscheck (habitat). The job is to **port that pattern** onto NetworkX ER graphs with the correct mean-field volume exponent — not to invent a percolation library.
</dont_hand_roll>

<common_pitfalls>
## Common Pitfalls

### Pitfall 1: Substituting last finite size for p_c(∞)
**What goes wrong:** `ys[-1] = log(1e-9) ≈ −20.7` dominates OLS; fitted ν ≈ 0.23 on *perfect* ν=1 data (baseline 0.239 / 76.1% error).
**Why it happens:** No closed-form p_c was coded; “largest N is close enough” is not close enough in log space.
**How to avoid:** Constant `PC_INF` like habitat’s `0.59274621`. For Poisson ER bond percolation, `PC_INF = 1/MEAN_DEGREE` if the estimator tracks true p_c; `2*math.log(2)/MEAN_DEGREE` only if keeping S = 0.5 (not recommended).
**Warning signs:** Last printed `p_c_hat` used as theory; ν insensitive to `SEEDS_PER_N`.

### Pitfall 2: S = 0.5 is not p_c on ER graphs
**What goes wrong:** Infinite-N S(p_c) = 0. S = 0.5 sits at p\* ≈ 0.231, O(1) above criticality. FSS of the *critical point* is invisible; p_{0.5}(N) is already flat by N = 200.
**Why it happens:** Habitat’s 50% **wrapping** probability is a valid 2D p_c estimator (universal O(1) spanning probability at p_c). That analogy does not transfer to giant fraction on ER.
**How to avoid:** Threshold at S_c(N) ~ N^{−1/3}, or susceptibility peak. Document the choice in protocol YAML `experimental_design`.
**Warning signs:** All `p_c_hat` ≈ 0.23 independent of N; mixed signs vs 1/6 and vs 0.2.

### Pitfall 3: Catalog ν = 1 vs volume FSS ν̄ = 3
**What goes wrong:** Fitting |p_c(N) − p_c| ~ N^{−1/ν} against ν = 1 expects 1/N shift. ER critical window is N^{−1/3} (ν̄ = 3). Honest critical estimator will “fail” 25% vs 1 and pass vs 3.
**Why it happens:** Mixing Bethe-lattice chemical-distance ν = 1 with the formula that habitat uses for *linear* size L. Unknown YAML writes `N^{-1/nu}` with `nu=1` as a shorthand.
**How to avoid:** Methodology note in script docstring + protocol YAML: this Crosscheck tests **ν̄ = 3** for |Δp| ~ N^{−1/ν̄}. Do not relabel 3 as 1.
**Warning signs:** Pressure to loosen tolerance or drop N=200 to force ν ≈ 1.

### Pitfall 4: Bisection on a single noisy sample
**What goes wrong:** Each mid draws independent bonds; giant fraction is not monotone in p for one draw. Bisection is biased.
**Why it happens:** `estimate_pc` uses `trials = 1` unlike habitat’s 350.
**How to avoid:** Average across graph realizations at each mid (Pattern 2). Optionally raise bond samples per mid after a sweep.
**Warning signs:** Huge seed-to-seed SD (local: sd ≈ 0.023 at N=200 with one sample).

### Pitfall 5: Using `erdos_renyi_graph` at N=5000
**What goes wrong:** 0.51 s/graph vs 0.021 s for `fast_gnp_random_graph`. Heavy `SEEDS_PER_N` then blows the “sweep before heavy defaults” budget.
**Why it happens:** NetworkX alias is the familiar name; docs warn it is O(n²).
**How to avoid:** Sparse generator; keep N=5000.
**Warning signs:** CI step minutes grow linearly with seeds while CC time is still ~10 ms.

### Pitfall 6: Protocol YAML / generated HTML drift
**What goes wrong:** YAML still says “NLS + 10 seeds per N”; script is log-log + 5 seeds. `index.html` is generated. Hand-edits get reverted by `--check`.
**Why it happens:** Phase 1 CONFIRMED habitat/cluster/Ising **without** flipping YAML `status` off `executed`.
**How to avoid:** If experimental_design / statistical_analysis_plan / estimated_runtime change, update YAML and run `python scripts/build_crosscheck.py --apply`. Optionally set `status: confirmed` (schema enum includes it) [VERIFIED: `schemas/protocol.yaml`].
**Warning signs:** `build_crosscheck.py --check` red on the PR.

### Pitfall 7: Confirming via CI grep only, skipping pytest
**What goes wrong:** Full Monte Carlo is slow and RNG-fragile; without a frozen-vector test, a later one-line fit change silently breaks the decision rule.
**How to avoid:** Habitat pattern: record p_c from the CONFIRMED run in a comment + assert `rel_err <= NU_TOLERANCE` and `sign_ok`.
**Warning signs:** Test re-runs NetworkX at N=5000 (too slow for `tests/repo_smoke`).
</common_pitfalls>

<code_examples>
## Code Examples

Verified patterns from **this repo** and NetworkX docs.

### Habitat signed fit + pass rule (copy contract)

```python
# Source: repro/p-b-habitat-percolation-ecology-fss/simulate_percolation_fss.py
nu, r2, sign_ok = fit_nu(SIZES, pcs)
rel_err = abs(nu - NU_THEORY) / NU_THEORY
passed = sign_ok and rel_err <= NU_TOLERANCE
print(f"RESULT: {'CONFIRMED' if passed else 'INCONCLUSIVE (increase TRIALS_PER_P for higher precision)'}")
```

### Proposed epidemic constants + signed fit (planning target)

```python
# Proposed for epidemic_percolation_fss.py — analog of habitat, not current file
MEAN_DEGREE = 6
SIZES = [200, 500, 1000, 2000, 5000]
SEEDS_PER_N = 20          # sweep; do not jump to 350
NU_THEORY = 3.0           # volume FSS ν̄; document vs catalog chemical ν=1
NU_TOLERANCE = 0.25       # keep until sweep; tighten to 0.15 if stable
PC_INF = 1.0 / MEAN_DEGREE  # Poisson ER / Newman T_c, NOT 1/(k-1)

def fit_nu(sizes, pcs):
    import math
    deltas = [pc - PC_INF for pc in pcs]  # local data: approach from above
    sign_ok = all(d > 0 for d in deltas)
    xs = [math.log(N) for N in sizes]
    ys = [math.log(d if sign_ok else abs(d) + 1e-9) for d in deltas]
    # OLS identical to habitat ...
    return nu, r2, sign_ok
```

### NetworkX sparse ER + giant component

```python
# Source: https://networkx.org/documentation/stable/reference/generated/networkx.generators.random_graphs.erdos_renyi_graph.html
# Notes: erdos_renyi_graph is O(n^2); use fast_gnp_random_graph for sparse p.
p_edge = mean_k / (n - 1) if n > 1 else 0.0
g = nx.fast_gnp_random_graph(n, p_edge, seed=seed)

# Source: https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.components.connected_components.html
largest_cc = max(nx.connected_components(kept), key=len)
frac = len(largest_cc) / n
```

### Critical threshold analog (order parameter at p_c)

```python
# Mean-field: S(p_c) ~ N^{-β/ν̄} = N^{-1/3}
# Local 20-seed run: ν̄=2.68, R²=0.93 vs 3. [VERIFIED: 2026-08-26 diagnostic]
def order_parameter_threshold(n: int) -> float:
    return n ** (-1.0 / 3.0)
```

### Habitat regression test (copy structure)

```python
# Source: tests/repo_smoke/test_crosscheck_repro_regression.py
def test_percolation_fss_fit_confirmed_on_reference_pcs() -> None:
    mod = _load_module(
        "simulate_percolation_fss",
        REPO_ROOT / "repro/p-b-habitat-percolation-ecology-fss/simulate_percolation_fss.py",
    )
    pcs = [0.59080, 0.59059, 0.59268, 0.59179]  # frozen CONFIRMED run
    nu, r2, sign_ok = mod.fit_nu(mod.SIZES, pcs)
    rel_err = abs(nu - mod.NU_THEORY) / mod.NU_THEORY
    assert sign_ok
    assert rel_err <= mod.NU_TOLERANCE
    assert r2 > 0.0
```

Proposed epidemic test (after a CONFIRMED run freezes real numbers — **do not invent pcs in the plan**):

```python
def test_epidemic_fss_fit_confirmed_on_reference_pcs() -> None:
    mod = _load_module(
        "epidemic_percolation_fss",
        REPO_ROOT / "repro/p-b-percolation-epidemiology-fss/epidemic_percolation_fss.py",
    )
    pcs = [...]  # paste from CONFIRMED stdout; comment seed + SEEDS_PER_N + date
    nu, r2, sign_ok = mod.fit_nu(mod.SIZES, pcs)
    rel_err = abs(nu - mod.NU_THEORY) / mod.NU_THEORY
    assert sign_ok
    assert rel_err <= mod.NU_TOLERANCE
    assert r2 > 0.0
```

### CI grep pattern (Ising / habitat — epidemic currently missing grep)

```yaml
# Source: .github/workflows/crosscheck-repro.yml (habitat step)
# Epidemic step today: `python .../epidemic_percolation_fss.py` with no grep.
- name: Epidemic percolation FSS (expect CONFIRMED)
  run: |
    python repro/p-b-percolation-epidemiology-fss/epidemic_percolation_fss.py | tee /tmp/epidemic.out
    grep -q "RESULT: CONFIRMED" /tmp/epidemic.out
```
</code_examples>

<validation_architecture>
## Validation Architecture

| Layer | What it proves | Where | Speed |
|-------|----------------|-------|-------|
| **Unit / fit regression** | Decision rule (signed ν, tolerance) on frozen p_c | `tests/repo_smoke/test_crosscheck_repro_regression.py` | milliseconds |
| **Repo smoke CI** | That test file on every PR | `.github/workflows/validate-schemas.yml` → `python -m pytest tests/repo_smoke` | already on all PRs [VERIFIED] |
| **Full Monte Carlo CI** | End-to-end `RESULT: CONFIRMED` with real RNG | `.github/workflows/crosscheck-repro.yml` path filter `repro/**` | seconds–minutes; grep gate |
| **Artifact drift** | YAML ↔ generated `index.html` / hub | `scripts/build_crosscheck.py --check` (CROSS-05, already shipped) | seconds |
| **Colab** | Demo still calls canonical script | Manual after Python CONFIRMED (ROADMAP 02-03) | human |

**Gating today [VERIFIED: `crosscheck-repro.yml`]:**
- Habitat: run + `grep -q "RESULT: CONFIRMED"`
- Cluster: run + grep
- **Epidemic: run only (no grep)** ← Phase 2 must add grep
- Ising: run + grep

**pytest is in CI** via `validate-schemas.yml` (Python 3.12), not via `crosscheck-repro.yml` (Python 3.11). Both must stay green. Do not put a 5-minute NetworkX sweep inside `tests/repo_smoke`.

**Sweep protocol (before committing defaults):**
1. Switch generator to `fast_gnp_random_graph` (no physics change).
2. Time `SEEDS_PER_N ∈ {10, 20, 40}` at full `SIZES` including 5000.
3. Compare estimators: S ≥ 0.5 (expect fail) vs S ≥ N^{−1/3} (expect ν̄ ~ 3).
4. Commit the smallest seed count that is `sign_ok` and within tolerance **on more than one seed batch**.
5. Freeze that stdout p_c vector into the regression test.

**Runtime budget:** GitHub-hosted job default timeout is **360 minutes**; this workflow has **no** `timeout-minutes` set. [CITED: GitHub Actions `jobs.<job_id>.timeout-minutes` default 360]. Practical budget: habitat (L=128, 350 trials) + cluster (L=256, 20 seeds) + Ising already share the job. Local: 4 sizes × 20 seeds × 2 estimators ≈ **5.9 s** with `fast_gnp`; N=5000 CC ≈ **10 ms**, graph gen ≈ **21 ms**. Even `SEEDS_PER_N=50` should stay well under a minute for epidemic alone. Do **not** copy habitat’s 350 without a timed need. [VERIFIED: local timings]
</validation_architecture>

<security_domain>
## Security Domain

This phase is a **deterministic scientific simulation** (seeded RNG, no network listeners, no user accounts). OWASP ASVS application categories mostly **do not apply**. Pretending they do would pad the plan.

| ASVS category | Applies? | Notes |
|---------------|----------|-------|
| V1 Architecture | N/A | No application tiers beyond CLI + static Pages |
| V2 Authentication | N/A | No users |
| V3 Session | N/A | |
| V4 Access control | N/A | |
| V5 Input validation | Minimal | No untrusted input. Constants and CLI-less `main()`. Do not add argparse that reads files from argv unless needed |
| V6 Cryptography | N/A | `random.Random(seed)` is **scientific** RNG, not CSPRNG — do not “upgrade” to `secrets` |
| V7 Error handling | Low | Print `ERROR: networkx required` and exit 2 already [VERIFIED: script] |
| V8 Data protection | N/A | Synthetic graphs only; no human/outbreak microdata in this protocol (catalog *mentions* nursing homes as a future test — **do not commit such data**) [VERIFIED: `docs/ETHICS_REPRODUCIBILITY_AND_DATA.md`] |
| V9 Communications | N/A | Colab clones the **public** GitHub repo; no secrets |
| V10 Malicious clients | N/A | |
| V11 Business logic | Scientific integrity, not ASVS | Do not confirm a false exponent; label methodology changes |
| V12 Files | N/A | No uploads |
| V13 API | N/A | |
| V14 Configuration | Low | Pin `networkx>=3.0` in the bundle; CI install is unpinned — optional harden |

**Integrity controls that *do* apply (reproducibility, not ASVS):**
- Record seeds (`N * 100 + s` today) and print them or keep them as constants.
- Frozen p_c vector in pytest so the pass rule cannot drift independently of Monte Carlo noise.
- No fabricated DOIs; Newman 2002 is already in `docs/citation_index.md` and the protocol YAML. [VERIFIED]
</security_domain>

<environment_availability>
## Environment Availability

| Tool | Local (this research) | CI smoke | CI pytest | Colab |
|------|----------------------|----------|-----------|-------|
| Python | 3.12.6 [VERIFIED] | 3.11 [VERIFIED: crosscheck-repro.yml] | 3.12 [VERIFIED: validate-schemas.yml] | Colab default (notebook metadata claims 3.10) |
| networkx | 3.6 [VERIFIED] | `pip install networkx` unpinned | **not installed** (fit test must not import nx at module level if avoidable; `import networkx` currently runs at import and would fail pytest **unless** networkx is added to the pytest job or import is lazy) | `pip install -r requirements.txt` |
| pytest | used via CONTRIBUTING | not in this workflow | yes | n/a |

**Blocker to flag for the planner:** `epidemic_percolation_fss.py` does `import networkx` at module top. `_load_module` in the regression test **executes the module**. `validate-schemas.yml` installs `pyyaml jsonschema pytest` only — **not networkx**. Habitat/Ising/cluster tests work because those modules are stdlib.

**Fix (pick one, prefer the first):**
1. Lazy-import networkx inside `er_graph` / `giant_fraction` (keep `fit_nu` import-safe), **or**
2. Add `pip install networkx` to `validate-schemas.yml`.

Option 1 matches “pytest tests the fit, not the Monte Carlo” and avoids slowing schema CI.
</environment_availability>

<sota_updates>
## State of the Art (theory relevant to this protocol)

| Old / catalog shorthand | Current standard | When established | Impact on Phase 2 |
|-------------------------|------------------|------------------|-------------------|
| ν = 1 in \|Δp\| ~ N^{−1/ν} for random graphs | Volume FSS exponent ν̄ = 3; window ~ N^{−1/3} | Bollobás 1984; mean-field d_u=6, ν=1/2 | Target for a *critical* estimator is ν̄ = 3, not 1 |
| T_c = 1/(k−1) “for ER” | T_c = ⟨k⟩/⟨k(k−1)⟩ = 1/⟨k⟩ for Poisson; 1/(k−1) for k-regular | Newman 2002; Callaway et al. 2000 | Keep ER; `PC_INF = 1/6` |
| 50% giant = p_c | S(p_c)=0; S=1/2 at λ=2 ln 2 | ER / branching process (textbook) | Must change estimator to confirm a critical exponent |
| `nx.erdos_renyi_graph` as default | `fast_gnp_random_graph` for sparse p | NetworkX docs (current 3.6.1) | Easy CI win |

**Deprecated/outdated for this phase:**
- Using the largest simulated N as p_c(∞).
- Treating CONFIRMED as a YAML-free stdout trophy while `status: executed` (acceptable to leave for Phase 4, but do not *worsen* YAML/script mismatch).
</sota_updates>

<open_questions>
## Open Questions (RESOLVED)

Locked into `02-CONTEXT.md` Decisions D-01–D-08 on 2026-08-26 by the plan-phase orchestrator.

1. **Lock ν̄ = 3 vs keep protocol ν = 1** — RESOLVED: D-03 `NU_THEORY = 3.0`; rewrite YAML; do not confirm ν = 1.
2. **Critical estimator** — RESOLVED: D-02 ship `S ≥ N^{-1/3}`; susceptibility only if N=5000 sign-check fails.
3. **Poisson 1/⟨k⟩ vs regular 1/(k−1)** — RESOLVED: D-01 `PC_INF = 1/MEAN_DEGREE`.
4. **SEEDS_PER_N final value** — RESOLVED as a 02-01 sweep task: D-06 start 20, try 40 if mixed, never 350.
5. **Protocol YAML `status: confirmed`** — RESOLVED: D-08 update wrong YAML fields; flip epidemic `status` in the same PR if Python CONFIRMED.
6. **networkx import vs pytest job** — RESOLVED: D-05 lazy-import.
</open_questions>

<assumptions_log>
## Assumptions Log

| ID | Assumption | Basis | Risk if wrong |
|----|------------|-------|---------------|
| A1 | Planner will accept ν̄=3 as the CROSS-04 target | Literature + local fit; 01-03 methodology-pass precedent | If owner insists on ν=1 *and* S=0.5, CROSS-04 cannot be honestly CONFIRMED |
| A2 | `fast_gnp_random_graph` is distributionally equivalent to `erdos_renyi_graph` for G(n,p) | NetworkX docs (same model, different algorithm) | Seed-level bit disagreement only; averages must still match theory |
| A3 | CI epidemic step can grow from ~seconds to ~1 minute | Local timings; 360 min default timeout | If Ubuntu runner is much slower, drop SEEDS not N=5000 |
| A4 | Colab notebook needs no cell rewrite if the .py API stays `python epidemic_percolation_fss.py` | Notebook content [VERIFIED] | If constants become CLI flags, notebook must pass them |
| A5 | Not committing protocol YAML is OK only if experimental_design is unchanged | Drift gate CROSS-05 | Changing estimator without YAML would lie about the experiment |
| A6 | Prompt’s pc_inf=1/(k−1) was a regular-graph slip, not a decision to switch topology | Protocol text “Erdős–Rényi graphs G(N, p)” | If owner wanted k-regular, T_c=0.2 and generator changes |
</assumptions_log>

<sources>
## Sources

### Primary (HIGH confidence)
- `repro/p-b-percolation-epidemiology-fss/epidemic_percolation_fss.py` — current fit, seeds, S=0.5 bisection
- `repro/p-b-habitat-percolation-ecology-fss/simulate_percolation_fss.py` — signed `fit_nu`, TRIALS_PER_P=350, PC_INF
- `tests/repo_smoke/test_crosscheck_repro_regression.py` — frozen-vector pattern
- `.github/workflows/crosscheck-repro.yml` — CONFIRMED greps; epidemic ungated
- `.github/workflows/validate-schemas.yml` — pytest smoke (no networkx)
- `scripts/build_crosscheck.py` — artifact regen, **not** a CONFIRMED gate
- `scripts/crosscheck_browser.py` — no epidemic JS runner; Colab helper
- `protocols-catalog/physics-epidemiology/p-b-percolation-epidemiology-fss.yaml`
- Local commands, 2026-08-26: Python 3.12.6, networkx 3.6; synthetic fit_nu bug; N=5000 timings; 20-seed estimator comparison
- NetworkX 3.6.1 docs: `erdos_renyi_graph`, `connected_components` — https://networkx.org/documentation/stable/

### Secondary (MEDIUM confidence — cited literature)
- Newman, M. E. J. (2002). Spread of epidemic disease on networks. *Phys. Rev. E* **66**, 016128. DOI 10.1103/PhysRevE.66.016128. T_c = ⟨k⟩ / ⟨k(k−1)⟩. [CITED: https://arxiv.org/abs/cond-mat/0205009 HTML Eq. (23); also `docs/citation_index.md`]
- Callaway, Newman, Strogatz, Watts (2000). Network robustness and fragility. *Phys. Rev. Lett.* **85**, 5468. [CITED: https://arxiv.org/abs/cond-mat/0007300]
- Bollobás (1984) / Borgs–Chayes–Kesten–Spencer: ER critical window p = (1/N)(1 + λ N^{−1/3}). [CITED: https://arxiv.org/pdf/math/0006135 (tr-98-27 / CMP paper discussion)]
- Hong, Ha, Park (2007). Finite-size scaling in complex networks. *Phys. Rev. Lett.* **98**, 258701. FSS exponent ν̄ on networks. [CITED: https://arxiv.org/abs/cond-mat/0701516]
- GitHub Actions `timeout-minutes` default 360. [CITED: https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions]

### Tertiary (LOW confidence)
- Protocol YAML reference `arxiv: cond-mat/9212004` “Finite-size scaling toolkit” — not re-fetched; do not invent a title in implementation docs; keep the existing YAML note if the file is edited for other reasons.
</sources>

<metadata>
## Metadata

**Research scope:**
- Core technology: NetworkX ER bond percolation + log-log FSS fit
- Ecosystem: existing USDR Crosscheck (habitat FSS, cluster τ, Ising γ), GitHub Actions, pytest smoke, Colab
- Patterns: signed theoretical-pc fit; average-then-bisect; critical-window order-parameter threshold
- Pitfalls: pc_inf substitution, S=0.5, ν vs ν̄, noisy bisection, O(n²) generator, pytest import of networkx

**Confidence breakdown:**
- Standard stack: HIGH — files + installed networkx 3.6 + NetworkX docs
- Architecture: HIGH — copy habitat/CI patterns already in-tree
- Pitfalls: HIGH — synthetic reproduction of ν=0.239; Monte Carlo of both estimators
- Code examples: HIGH — copied from this repo / official NetworkX docs
- Exponent recommendation (ν̄=3): HIGH on theory; MEDIUM-HIGH on “20 seeds is enough at N=5000” (sweep still required)

**Research date:** 2026-08-26
**Valid until:** 2026-09-25 (30 days — NetworkX 3.x and this protocol are stable; the Monte Carlo defaults are the perishable part)
</metadata>

---

*Phase: 02-epidemic-fss-precision*
*Research completed: 2026-08-26*
*Ready for planning: yes*

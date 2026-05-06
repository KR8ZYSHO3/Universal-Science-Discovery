# USDR Python Scripts — Code Audit

**Audit date:** 2026-05-06  
**Auditor:** engineering agent (comprehensive audit sprint)  
**Scope:** all primary scripts in `scripts/`

---

## Summary

| Script | HIGH | MEDIUM | LOW | Status |
|--------|------|--------|-----|--------|
| `validate_schemas.py` | 0 | 1 | 1 | Clean |
| `build_graph.py` | 0 | 0 | 2 | Clean |
| `generate_api.py` | 1 | 1 | 2 | **Fixed** |
| `update_dashboard_stats.py` | 0 | 1 | 1 | Clean |
| `generate_domain_pages.py` | 0 | 1 | 2 | Clean |
| `generate_explainers.py` | 0 | 1 | 2 | Clean |
| `propose_bridges.py` | 1 | 1 | 2 | **Fixed** |
| `find_orphan_unknowns.py` | 2 | 0 | 1 | **Fixed** |
| `audit_quality.py` | 0 | 1 | 1 | Clean |
| `build_citation_index.py` | 1 | 1 | 1 | **Fixed** |

**HIGH issues found:** 5  
**HIGH issues fixed:** 5 (all)  
**Schema validation:** PASS — all 1,000+ YAML records valid  
**Quality audit:** 0 ERRORS, 0 WARNINGS, 18 INFO items  
**Orphan unknowns:** 300 of 619 unknowns have no graph connections (expected — high contribution opportunity)

---

## Detailed Findings

---

### `scripts/validate_schemas.py`

**Purpose:** Validates all catalog YAML (unknowns, hypotheses, bridges, phenomenology, pioneers, breakthrough-gaps) against JSON Schema.

#### Issues

| Severity | Issue | Location |
|----------|-------|----------|
| MEDIUM | `load_yaml` at the top level (used for schema loading) has no try/except — if a schema file is corrupt, the script crashes with an unhandled exception rather than a clear error message. | Line 12–19 |
| LOW | No `--help` / argparse description. Script behavior (exit code) is well-documented in the module docstring, but there is no `--dry-run` or `--paths` flag for partial validation. | Global |

**Action:** No fix applied (MEDIUM/LOW); schema loading crashes are acceptable since schema files are tightly controlled. The module docstring is clear.

---

### `scripts/build_graph.py`

**Purpose:** Builds `docs/knowledge_graph.json` from all catalog YAML entries.

#### Issues

| Severity | Issue | Location |
|----------|-------|----------|
| LOW | No argparse / `--help` interface. | Global |
| LOW | `OUTPUT` path is hardcoded as a module-level constant (`docs/knowledge_graph.json`). Fine for CI use; no `--output` flag for custom paths. | Line 21 |

**Action:** No fix needed. Script is well-structured with proper exception handling in `load_yaml`, orphan-edge filtering, and per-file warnings.

---

### `scripts/generate_api.py`

**Purpose:** Generates static JSON API endpoints under `api/v1/`.

#### Issues

| Severity | Issue | Location | Fix Applied |
|----------|-------|----------|-------------|
| **HIGH** | Bare `except:` in `load_yaml` catches `SystemExit` and `KeyboardInterrupt`, masking critical failures and preventing Ctrl-C from working correctly. | Line 26–27 | ✅ Changed to `except Exception as exc` with stderr warning |
| MEDIUM | Silent failure mode: when `load_yaml` fails it returns `{}` with no per-file log (pre-fix). Now emits a WARNING to stderr. | Line 26–27 | ✅ Fixed alongside HIGH fix |
| LOW | No argparse / `--help`. | Global | Noted |
| LOW | `import shutil` inside function body (lines 138, 144, 150) — minor style issue, should be at module top. | Lines 138, 144, 150 | Noted |

---

### `scripts/update_dashboard_stats.py`

**Purpose:** Reads actual catalog file counts and patches `dashboard/index.html` stat counters.

#### Issues

| Severity | Issue | Location |
|----------|-------|----------|
| MEDIUM | Uses `sys.argv` check instead of argparse — `--apply` flag is functional but not documented by `--help`. | Line 62 |
| LOW | `sys.exit(1)` is called when dashboard file is missing, but the script has `-> None` return type annotation. Consistent behavior, but exit code isn't documented. | Line 79 |

**Action:** No fix applied. The `--apply` pattern is clear and intentional (safe dry-run default).

---

### `scripts/generate_domain_pages.py`

**Purpose:** Generates per-domain HTML landing pages under `dashboard/domains/`.

#### Issues

| Severity | Issue | Location |
|----------|-------|----------|
| MEDIUM | `get_domain_hypotheses` uses `str(data)` (the YAML dict stringified) to find hypothesis linkage to unknowns. This crude string match can produce false positives when unknown IDs appear in unrelated fields. | Line 91–92 |
| LOW | Bare `except Exception: return {}` in `load_yaml` silently discards parse errors. | Line 46–47 |
| LOW | `DOMAIN_META` dictionary has 20 entries but the repo has domains outside this list — unknown domains fall back to generic icon/color with no warning. | Line 20–41 |

**Action:** No fix applied. The hypothesis-linkage heuristic is a display feature, not a data integrity issue. False positives result in showing slightly more hypotheses (acceptable). Capped at 10 per page.

---

### `scripts/generate_explainers.py`

**Purpose:** Generates rich HTML explainer pages for individual bridges.

#### Issues

| Severity | Issue | Location |
|----------|-------|----------|
| MEDIUM | In `find_bridge_yaml`, the fallback loop opens every YAML file in `cross-domain/` with a bare `except Exception: pass` — parse errors are silently dropped. | Line 44–49 |
| LOW | Uses `sys.argv[1:]` directly instead of argparse — no `--help`. | Line 576 |
| LOW | `DEFAULT_BRIDGES` is hardcoded — if those bridge IDs are renamed, the script silently generates 0 explainers without error. The per-bridge try/except does catch this and reports errors, so it degrades gracefully. | Line 27–33 |

**Action:** No fix applied. Errors are caught and reported per bridge; the script does not crash.

---

### `scripts/propose_bridges.py`

**Purpose:** Proposes novel cross-domain bridge candidates from pioneer seeds, breakthrough gaps, and domain-gap analysis.

#### Issues

| Severity | Issue | Location | Fix Applied |
|----------|-------|----------|-------------|
| **HIGH** | `_breakthrough_gap_proposals` returns `gaps_dir` (a `Path` object) instead of `proposals` (an empty list) when the directory doesn't exist. This causes `TypeError: 'PosixPath' object is not iterable` downstream. | Line 97 | ✅ Changed `return gaps_dir` to `return proposals` |
| MEDIUM | Output JSON contains `"generated": "2026-05-06"` hardcoded string instead of `date.today().isoformat()`. | Line 306 | Noted for future fix |
| LOW | No argparse description for `--draft-yaml` flag behavior (what directory it writes to). | Line 244 | Noted |
| LOW | `_yaml_load` fallback (when PyYAML is unavailable) returns `{}` silently — callers won't know the file wasn't parsed. | Line 34–37 | Noted |

---

### `scripts/find_orphan_unknowns.py`

**Purpose:** Identifies unknowns with no graph connections — priority contribution targets.

#### Issues

| Severity | Issue | Location | Fix Applied |
|----------|-------|----------|-------------|
| **HIGH** | `UnicodeEncodeError` when printing the `≥` character on Windows terminals using cp1252 encoding. Confirmed crash in test run. | Line 38 | ✅ Added `io.TextIOWrapper` stdout override when encoding is not UTF-8 |
| **HIGH** | No try/except around `knowledge_graph.json` read. If the file is missing (e.g., before first `build_graph.py` run), the script crashes with an unhandled `FileNotFoundError`. | Line 18–20 | ✅ Added existence check and `json.JSONDecodeError` / `OSError` handling with `sys.exit(1)` |
| LOW | No argparse / `--help`. | Global | Noted |

---

### `scripts/audit_quality.py`

**Purpose:** Audits unknowns catalog for quality issues (short titles, missing metadata, duplicates).

#### Issues

| Severity | Issue | Location |
|----------|-------|----------|
| MEDIUM | Only audits `unknowns-catalog/` — bridges and hypotheses are not quality-checked. Adding similar checks for bridges (translation table presence, real DOIs) would improve coverage. | Lines 33–78 |
| LOW | Duplicate-detection uses normalized title match (`re.sub(r"\W+", " ", title.lower())`). Very short titles (≤3 words) can produce spurious duplicate warnings. | Line 64 |

**Action:** No fix applied. Scope expansion (bridges/hypotheses) is a feature request, not a bug.

---

### `scripts/build_citation_index.py`

**Purpose:** Extracts DOIs/references from all catalog entries and identifies cross-domain influential papers.

#### Issues

| Severity | Issue | Location | Fix Applied |
|----------|-------|----------|-------------|
| **HIGH** | Bare `except:` in `load_yaml` catches `SystemExit` and `KeyboardInterrupt`. | Line 17 | ✅ Changed to `except Exception as exc` with stderr warning |
| MEDIUM | `"generated": str(Path(__file__).stat().st_mtime)` uses the script's filesystem modification timestamp (a float like `1746460892.123`) instead of today's date. This is misleading in the output JSON. | Line 106 | ✅ Changed to `date.today().isoformat()` |
| LOW | No argparse / `--help`. | Global | Noted |

---

## Quality Audit Results (2026-05-06)

From `python scripts/audit_quality.py`:

```
ERRORS:   0
WARNINGS: 0
INFO:     18
```

All 18 INFO items are low-priority style notes (titles not phrased as questions). No data integrity issues. Full report: `docs/quality_report.md`.

---

## Schema Validation Results (2026-05-06)

From `python scripts/validate_schemas.py`:

```
OK: all hypothesis, unknown-catalog, cross-domain bridge, phenomenology, pioneer, and
breakthrough-gap YAML files validate. (4 phenomenology entries, 13 pioneer entries,
11 breakthrough-gap entries)
```

All records pass. No schema fixes needed.

---

## Orphan Unknowns (2026-05-06)

From `python scripts/find_orphan_unknowns.py`:

```
Total unknowns in graph:                    619
Connected to ≥1 bridge or hypothesis edge:  319
Orphan unknowns (no connections):           300
```

300 orphans (48%) is expected at this stage — the content build sprint added unknowns faster than bridges can connect them. These are the **highest-priority contribution targets**. Full list: `docs/orphan_unknowns.md`.

---

## Recommendations for Future Work

| Priority | Recommendation |
|----------|---------------|
| MEDIUM | Add `--output` flag to `build_graph.py` for custom graph paths (CI flexibility) |
| MEDIUM | Replace hardcoded `"generated"` date in `propose_bridges.py` with `date.today().isoformat()` |
| MEDIUM | Expand `audit_quality.py` to check bridges (translation table ≥3 rows, real DOIs, status field set) |
| LOW | Add `argparse` with `--help` to all scripts lacking it (`build_graph.py`, `find_orphan_unknowns.py`, `generate_explainers.py`, `build_citation_index.py`) |
| LOW | Move `import shutil` to module level in `generate_api.py` |
| LOW | Add a `--domain-meta-fallback-warn` flag to `generate_domain_pages.py` to log when a domain has no icon/color in `DOMAIN_META` |

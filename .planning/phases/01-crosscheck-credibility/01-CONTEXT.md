# Phase 1 Context: Crosscheck credibility

**Gathered:** 2026-06-23 (retroactive from merged PRs)

## Problem

Seed Crosscheck protocols were INCONCLUSIVE at default settings. Outreach copy (`READY_TO_POST.md`) promised runnable demos but outcomes were weak. No CI drift gate for Crosscheck artifacts.

## Approach

Precision passes per protocol (increase trials, fix fit methodology, pooled histograms). Core pipeline: `build_crosscheck.py`, regression tests, bot PR regen. Mirror JS demos with lighter budgets.

## Outcomes (shipped)

| PR | Deliverable |
|----|-------------|
| #297 | Ising EWI CONFIRMED |
| #298 | Habitat FSS CONFIRMED |
| #299–#301 | `build_crosscheck.py`, drift gate, graph bot integration |
| #300 | Stale graph removed, repro regression tests |
| #302 | Cluster exponent CONFIRMED (pooled, p=0.59, L=256) |

## Scorecard

3/4 CONFIRMED: FSS ν, Ising γ, cluster τ. Epidemic FSS deferred to Phase 5.

## Next phase handoff

Outreach copy must be updated before Reddit/arXiv push. Lead with "3 CONFIRMED Crosscheck demos."
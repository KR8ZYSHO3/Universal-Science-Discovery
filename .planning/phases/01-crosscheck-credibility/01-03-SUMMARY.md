# 01-03 Summary: Cluster exponent precision pass

**Completed:** 2026-06-23 (PR #302)

## One-liner

Cluster size distribution τ reaches CONFIRMED via pooled histogram, p=0.59, L=256, scaling s∈[8,L/4].

## Shipped

- `cluster_size_exponent.py` + JS demo (128² @ p=0.592)
- Protocol YAML updated
- CI CONFIRMED grep + regression test for pooled fit
- Pooled τ=1.954 (4.9% off 187/91)

## Verification

- `python repro/.../cluster_size_exponent.py` → CONFIRMED
- `test_cluster_exponent_fit_confirmed_on_pooled_reference` passes
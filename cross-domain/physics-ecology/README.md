# Statistical Physics ↔ Conservation Ecology

## The bridge in one sentence

The ~60% habitat threshold at which forest-interior species collapse is the 2D site
percolation threshold (p_c = 0.593), and 50 years of percolation finite-size scaling
gives conservation biology a rigorous, quantitative framework that the SLOSS debate
has never had.

## The percolation trilogy

This bridge completes a trio of fields united by the same mathematics:

| Bridge | Field | Application |
|--------|-------|-------------|
| `b-percolation-oncology` | Oncology | Tumour vascular network fragmentation |
| `b-percolation-epidemiology` | Epidemiology | Outbreak threshold in finite populations |
| **`b-habitat-percolation-ecology`** | **Conservation ecology** | **Species extinction in fragmented landscapes** |

The numerical algorithms for computing the percolation order parameter, correlation
length, and FSS corrections are *identical* across all three. A single open-source
percolation toolkit would serve tumour biologists, public health agencies, and
conservation planners simultaneously.

## The SLOSS resolution

SLOSS (Single Large Or Several Small reserves?) has been debated since the 1970s.
Percolation theory answers it: for a fixed total habitat area H, the connectivity
of the landscape (the percolation order parameter) depends on the spatial arrangement
of patches, not just the total area. Near the percolation threshold, a single large
reserve is always better for connectivity — a rigorous result, not an approximation.

## Bridge entries

- [`b-habitat-percolation-ecology`](b-habitat-percolation-ecology.yaml)

## Unknowns seeded here

- [`u-habitat-fragmentation-threshold`](../../unknowns-catalog/biology/u-habitat-fragmentation-threshold.yaml)

## Hypotheses to test

- [`h-habitat-percolation-critical-density`](../../hypotheses/active/h-habitat-percolation-critical-density.yaml)

## Next contributor action

1. Download Sentinel-2 land-cover data for 20 fragmented forest landscapes
2. Compute percolation order parameter and cluster-size distribution
3. Test whether cluster-size exponent matches tau=187/91 (2D percolation)
4. Open a PR against `h-habitat-percolation-critical-density.yaml`

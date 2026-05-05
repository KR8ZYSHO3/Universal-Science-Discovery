# Statistical Physics ↔ Climate Science

## The bridge in one sentence

Climate tipping points are formal phase transitions — the IPCC's qualitative
"tipping elements" each correspond to a specific bifurcation class (fold, Hopf,
second-order), and condensed-matter physics provides universal early-warning
indicators and exact scaling exponents that climate science has measured
empirically but never matched to theory.

## The tipping elements and their bifurcation classes

| Tipping element | Bifurcation class | Universal EWI |
|----------------|-------------------|---------------|
| Amazon forest/savanna | Fold (bistability) | AR1 ~ 1 - c*(mu_c-mu)^(1/2) |
| Arctic sea ice | Near-second-order | Variance ~ (mu_c-mu)^(-1) |
| AMOC collapse | Subcritical fold (hysteresis) | Rising AR1 + variance + 1/f spectral shift |
| Permafrost carbon | First-order (nucleation) | Waiting-time distribution for nucleation events |
| West Antarctic Ice Sheet | Fold (marine ice instability) | Spatial correlation length divergence |

## The data exists; the physics test has not been done

- Boers (2021) detected rising AR1 in AMOC fingerprint data, 1870-2020.
- Boulton et al. (2022) detected rising AR1 in Amazon NDVI, 2000-2020.
- Neither paper fit the fold-bifurcation scaling exponent 1/2 or estimated the remaining warming budget to tipping.

## Connection to other bridges

- [`b-habitat-percolation-ecology`](../physics-ecology/b-habitat-percolation-ecology.yaml) — Amazon deforestation triggers *both* a percolation threshold (connectivity loss) and a fold bifurcation (precipitation feedback). Two-threshold system.
- [`b-kibble-zurek-morphogenesis`](../cosmology-biology/b-kibble-zurek-morphogenesis.yaml) — KZ mechanism and AMOC quench-rate physics share the same quench-rate universality.
- [`b-ising-social-dynamics`](../physics-social/b-ising-social-dynamics.yaml) — Social climate action tipping coupled to physical climate tipping.

## Bridge entries

- [`b-tipping-points-phase-transitions`](b-tipping-points-phase-transitions.yaml)

## Hypotheses to test

- [`h-amoc-fold-bifurcation-ew`](../../hypotheses/active/h-amoc-fold-bifurcation-ew.yaml)

## Next contributor action

1. Get Boers (2021) AMOC AR1 time series (data available in paper supplement)
2. Fit AR1(t) = 1 - c*(T_c - T)^(1/2) using global mean temperature as forcing proxy
3. Extract T_c — the critical warming threshold for AMOC collapse
4. Open a PR against `h-amoc-fold-bifurcation-ew.yaml`

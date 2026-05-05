# Cross-domain bridges: physics (fluid dynamics) ↔ finance

## Active bridges

### b-turbulence-financial-markets — Kolmogorov cascade ↔ multifractal market volatility

Lewis Richardson (1922) described turbulent energy transfer as:
> *"Big whirls have little whirls that feed on their velocity,*
> *and little whirls have lesser whirls and so on to viscosity."*

Kolmogorov (1941) made this precise: energy injected at the large scale L cascades
down to the dissipation scale η with a universal power-law spectrum E(k) ~ k^{-5/3}.
At every intermediate scale, the velocity fluctuations are self-similar.

**Benoit Mandelbrot noticed something in 1963:** cotton price changes had the same
statistical fingerprint — heavy tails, self-similarity across timescales, long-range
dependence. Mainstream finance ignored him and built everything on Gaussian Brownian
motion instead. Then came 2008.

The quantitative connection is the **multifractal cascade**:
- In turbulence: energy multiplied by a log-normal random factor at each scale
- In finance: volatility multiplied by a log-normal random factor at each timescale

Same mathematics. The intermittency parameter λ² — which measures how "bursty" the
cascade is — has been measured in both systems. In S&P 500 returns: λ² ≈ 0.03.
In high-Reynolds turbulence: λ² ≈ 0.025. Close enough to be suspicious.

**What's missing:** turbulence has the Reynolds number — a single dimensionless
parameter that predicts when flow goes turbulent. Finance has no equivalent.
Finding the financial Reynolds number could predict when markets transition from
stable to crash-like dynamics. That's the open unknown this bridge seeds.

---

## Related bridges

- `b-tipping-points-phase-transitions` — financial crashes as bifurcations
- `b-ising-social-dynamics` — opinion cascade driving market herding
- `b-percolation-epidemiology` — systemic risk as network percolation

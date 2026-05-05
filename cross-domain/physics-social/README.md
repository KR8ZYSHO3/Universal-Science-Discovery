# Statistical Physics ↔ Social Science

## The bridge in one sentence

The Ising model of ferromagnetism describes opinion dynamics, norm cascades, and
political polarisation — social tipping points are phase transitions with
measurable early-warning indicators, and echo chamber formation follows the
Allen-Cahn coarsening dynamics of ferromagnetic domains.

## The same-sex marriage case

US support for same-sex marriage: 27% (1996) → 53% (2012) → 67% (2018).
The inflection near 50% in 2011-2012 is the social T_c — the Curie temperature
of American opinion on this issue. The Ising EWI (rising AR1 and variance before
T_c) should be visible in Gallup state-level data. Nobody has computed it.

## The polarisation prediction

Echo chambers are ferromagnetic Ising domains. Domain coarsening under Allen-Cahn
dynamics grows domain size as t^(1/2). With algorithmic recommendation acting as
an effective ferromagnetic coupling (spins prefer to align with their network
neighbourhood), coarsening is accelerated. This gives a *specific, quantitative*
prediction for political polarisation growth rate — falsifiable against ANES data.

## Connection to climate

The social and physical tipping bridges are coupled: climate action spreading
(Ising social transition) can push the physical climate system past its fold
bifurcation before the physical forcing alone would. Neither bridge alone captures
this interaction — both are needed simultaneously.

## Bridge entries

- [`b-ising-social-dynamics`](b-ising-social-dynamics.yaml)

## Unknowns seeded here

- [`u-social-ising-universality`](../../unknowns-catalog/physics/u-social-ising-universality.yaml)

## Hypotheses to test

- [`h-norm-cascade-ising-ew`](../../hypotheses/active/h-norm-cascade-ising-ew.yaml)

## Next contributor action

1. Download Gallup state-level same-sex marriage support data (public, 2003-2012)
2. Compute rolling AR1 and variance for each state
3. Fit Ising fold scaling: AR1(t) = 1 - c*(t_c - t)^(1/2)
4. Compare AIC to logistic null model
5. Open a PR against `h-norm-cascade-ising-ew.yaml`

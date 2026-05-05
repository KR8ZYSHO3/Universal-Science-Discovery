# Statistical Physics ↔ Epidemiology

## The bridge in one sentence

The epidemic threshold R_0=1 is a percolation phase transition, and 50 years
of finite-size scaling from condensed-matter physics could quantitatively improve
outbreak risk estimates in hospitals, schools, and island communities — where
standard mean-field R_0 estimates are systematically biased.

## Why this matters right now

During COVID-19, hundreds of nursing home and hospital outbreaks provided natural
experiments in populations of N=50 to N=500. Standard R_0 estimates (from early
exponential growth) don't have population-size uncertainty bands. Percolation
finite-size scaling gives a rigorous formula for those bands — and the data to
test it already exists in CDC MMWR reports, ECDC bulletins, and UK PHE analyses.

## The math in 30 seconds

In bond percolation: giant component appears at p_c.  
In SIR epidemics: major outbreak occurs at R_0 = 1.  
These are the same condition. The FSS correction to p_c in a finite network of N nodes is:

```
p_c(N) = p_c(∞) + c · N^(-1/ν)
```

For random-graph contact networks, ν=1. For 2D spatially structured populations, ν=4/3.  
Nobody has measured ν from real outbreak data.

## Bridge entries

- [`b-percolation-epidemiology`](b-percolation-epidemiology.yaml)

## Unknowns seeded here

- [`u-percolation-epidemic-fss`](../../unknowns-catalog/biology/u-percolation-epidemic-fss.yaml)

## Hypotheses to test

- [`h-percolation-outbreak-threshold`](../../hypotheses/active/h-percolation-outbreak-threshold.yaml)

## Related bridges

- [`b-percolation-oncology`](../physics-oncology/b-percolation-oncology.yaml) — same percolation mathematics applied to tumour vasculature

## Next contributor action

1. Pull 50+ COVID-19 nursing home outbreak reports from CDC MMWR (all public domain)
2. Fit R_0 vs N^(-1) and measure the FSS exponent ν
3. Compare to theoretical prediction ν=1
4. Open a PR against `h-percolation-outbreak-threshold.yaml`

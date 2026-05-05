# Cross-domain bridges: physics ↔ ecology

## Active bridges

### b-turing-patterns-ecosystem-tipping — Turing patterns as early-warning signals for ecosystem collapse

In the 1990s, ecologists noticed that drought-stressed vegetation in the Sahel,
the Negev, and Namibia forms strikingly regular spatial patterns: stripes on
slopes, hexagonal patches on flat terrain, leopard-spots of bare soil surrounded
by vegetation rings. These were beautiful, but their *function* was unclear.

In 1999, ecologist Mark Klausmeier wrote down the simplest model: vegetation
absorbs water (activator), and dense vegetation locally depletes water
(inhibitor). The diffusion rates differ: water flows fast, vegetation spreads
slowly. That is exactly the Turing condition. The characteristic patch spacing
follows directly from the Turing wavelength formula.

In 2004, a *Science* paper changed everything: **the progression of pattern types
is an early-warning signal for ecosystem collapse.** As rainfall decreases:

```
Uniform green → Labyrinthine → Stripes → Spots → Bare soil
(healthy)                                          (collapsed)
```

Each transition is a Turing bifurcation. The final transition — spots to bare
soil — is catastrophic and hysteretic: once the system collapses, increasing
rainfall does *not* immediately restore vegetation.

**The 2026 extension** (from our arXiv harvest): the pattern can either *buffer*
or *accelerate* collapse depending on whether the spot pattern remains above the
percolation threshold (p_c = 0.5927). If the vegetated fraction exceeds p_c,
connectivity is maintained and the ecosystem is resilient. Below p_c, it tips.

This bridges three pillars of the project:
- **Turing reaction-diffusion** (`b-turing-reaction-diffusion`)
- **Percolation theory** (`b-percolation-ecology`)
- **Self-organised criticality** (`b-self-organized-criticality`)

### Practical implication
Satellite time-series of vegetation patterns can be analysed using Fourier
spectroscopy. A narrowing and shifting Turing peak in the power spectrum is a
quantitative early-warning signal — *years before collapse* — that requires no
ground-truth data.

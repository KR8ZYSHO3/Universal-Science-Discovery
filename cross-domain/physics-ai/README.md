# Cross-domain bridges: physics ↔ artificial intelligence

## Active bridges

### b-phase-transitions-ml-grokking — Statistical physics phase transitions ↔ grokking, double descent, and scaling laws

Deep learning is full of phenomena that physicists recognise immediately and
ML engineers name from scratch:

| ML phenomenon | Physics equivalent |
|---------------|-------------------|
| Grokking | First- or second-order phase transition |
| Double descent curve | Non-monotonic susceptibility near a critical point |
| Interpolation threshold | Critical capacity α_c (Hopfield spin glass) |
| Loss landscape | Free energy landscape of an SK spin glass |
| Neural scaling laws L ~ N^{-α} | Power laws at criticality |
| Flat minima generalise | Low-temperature ordered phase |
| Catastrophic forgetting | Spin-glass metastable states / replica symmetry breaking |

**The grokking example in detail:**

In 2022, OpenAI researchers noticed that a small transformer trained on modular
arithmetic achieves 100% training accuracy very quickly, then — after thousands
of additional epochs — suddenly generalises to the test set. This "grokking"
was reported without reference to phase transitions.

A 2026 arXiv paper (from our harvest: "Dimensional Criticality at Grokking
Across MLPs and Transformers") measured the *intrinsic dimension* of the hidden
representation throughout training. At the grokking point, the intrinsic
dimension of the representation drops by half — the signature of a symmetry-
breaking phase transition, where the ordered phase has lower effective
dimensionality than the disordered phase.

**Open question:** what universality class does grokking belong to? If it is
the 2D Ising universality class, then finite-size scaling with β = 1/8, ν = 1
should collapse all grokking curves onto a single function. This would be one
of the most concrete predictions of cross-domain physics/ML connection.

## Related bridges

- `b-spin-glass-neural-networks` — the foundational spin-glass/ML bridge (Hopfield, SK model)
- `b-self-organized-criticality` — SOC and brain criticality
- `b-landauer-information-thermodynamics` — thermodynamic cost of computation

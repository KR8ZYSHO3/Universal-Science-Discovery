# Cross-domain bridges

Explicit connections between scientific fields that are studying the same underlying
phenomenon with different language, methods, or tools — and with little awareness of
each other.

Each subfolder contains one or more `b-*.yaml` bridge entries validated against
`schemas/bridge.yaml`. See `docs/CROSS_DOMAIN_BRIDGES.md` for the full overview and
contributing guide, and `docs/prompts/bridge_discovery.md` for the prompt to find
new bridges while reading any paper.

---

## Active bridges

| ID | Fields | Status | Unknowns | Hypotheses |
|----|--------|--------|----------|-----------|
| [b-percolation-oncology](physics-oncology/b-percolation-oncology.yaml) | statistical-physics ↔ oncology | proposed | u-tumor-containment-percolation, u-active-matter-percolation | h-adaptive-therapy-percolation-threshold, h-active-matter-percolation-oncology |
| [b-criticality-neuroscience](physics-neuroscience/b-criticality-neuroscience.yaml) | condensed-matter ↔ neuroscience | proposed | u-brain-criticality-function, u-cardiac-criticality-synchronization | h-criticality-conscious-integration, h-cardiac-arrhythmia-phase-transition |
| [b-glymphatic-aging](biology-medicine/b-glymphatic-aging.yaml) | sleep-medicine ↔ neurology ↔ geroscience | proposed | u-amyloid-progression-trajectory | h-glymphatic-amyloid-clearance-rate |
| [b-lichen-astrobiology](biology-astrobiology/b-lichen-astrobiology.yaml) | synthetic-biology ↔ astrobiology | proposed | u-synthetic-lichen-biofabrication | h-lichen-consortium-metabolic-coupling |
| [b-topology-morphogenesis](mathematics-biology/b-topology-morphogenesis.yaml) | mathematics/topology ↔ developmental-biology | proposed | u-topological-morphogenesis, u-cortical-folding-topology | h-topological-defect-morphogenesis, h-cortical-sulcal-topological-conservation |
| [b-grokking-criticality](ai-physics/b-grokking-criticality.yaml) | AI/machine-learning ↔ statistical-physics | proposed | u-grokking-phase-transition | h-grokking-criticality-universality |
| [b-quantum-biology-navigation](quantum-biology/b-quantum-biology-navigation.yaml) | quantum-mechanics ↔ sensory-biology | **established** | u-quantum-biology-decoherence | h-quantum-compass-precision |
| [b-kibble-zurek-morphogenesis](cosmology-biology/b-kibble-zurek-morphogenesis.yaml) | cosmology ↔ developmental-biology | proposed | u-kibble-zurek-embryo, u-topological-morphogenesis | h-kibble-zurek-polarity-scaling |
| [b-renormalization-biological-scaling](mathematics-biology/b-renormalization-biological-scaling.yaml) | mathematical-physics ↔ comparative-physiology | proposed | u-renormalization-allometric, u-kleiber-pulsatile-waves | h-allometric-rg-fixed-point, h-kleiber-wave-physics |
| [b-percolation-epidemiology](physics-epidemiology/b-percolation-epidemiology.yaml) | statistical-physics ↔ epidemiology | proposed | u-percolation-epidemic-fss | h-percolation-outbreak-threshold |
| [b-habitat-percolation-ecology](physics-ecology/b-habitat-percolation-ecology.yaml) | statistical-physics ↔ conservation-ecology | proposed | u-habitat-fragmentation-threshold | h-habitat-percolation-critical-density |
| [b-error-threshold-information](information-evolution/b-error-threshold-information.yaml) | information-theory ↔ molecular-evolution | proposed | u-error-threshold-genome-size | h-viral-proofreading-shannon-optimality |
| [b-kuramoto-synchronization](physics-engineering-neuroscience/b-kuramoto-synchronization.yaml) | statistical-physics ↔ neuroscience ↔ cardiology ↔ engineering | proposed | u-brain-criticality-function, u-cardiac-criticality-synchronization | h-kuramoto-af-spectral-gap, h-cardiac-arrhythmia-phase-transition |
| [b-fisher-information-evolution](statistics-evolution/b-fisher-information-evolution.yaml) | statistics ↔ evolutionary-biology ↔ machine-learning | proposed | u-fisher-natural-gradient-evolution | h-fisher-speed-limit-selection |
| [b-tipping-points-phase-transitions](physics-climate/b-tipping-points-phase-transitions.yaml) | statistical-physics ↔ climate-science | proposed | u-climate-ew-indicator-universality | h-amoc-fold-bifurcation-ew |
| [b-ising-social-dynamics](physics-social/b-ising-social-dynamics.yaml) | statistical-physics ↔ social-science | proposed | u-social-ising-universality | h-norm-cascade-ising-ew |

---

## Subdirectories

| Folder | Bridge |
|--------|--------|
| `physics-oncology/` | Percolation threshold ↔ tumour vascular fragmentation |
| `physics-neuroscience/` | Phase transitions ↔ neural avalanches |
| `biology-medicine/` | Glymphatic system ↔ sleep / amyloid / aging |
| `biology-astrobiology/` | Synthetic lichen consortia ↔ space ISRU |
| `mathematics-biology/` | Topological defects + RG fixed-point ↔ embryonic morphogenesis + biological scaling |
| `ai-physics/` | Grokking transition ↔ second-order phase transitions |
| `quantum-biology/` | Radical-pair compass ↔ quantum Fisher-information sensing |
| `cosmology-biology/` | Kibble-Zurek mechanism ↔ embryonic symmetry breaking |
| `physics-epidemiology/` | Network percolation ↔ epidemic threshold + finite-size scaling |
| `physics-ecology/` | Percolation ↔ habitat fragmentation threshold (SLOSS resolution) |
| `information-evolution/` | Shannon channel capacity ↔ Eigen error threshold (Darwin meets Shannon) |
| `physics-engineering-neuroscience/` | Kuramoto model ↔ neural gamma / cardiac AF / power grid / laser arrays |
| `statistics-evolution/` | Fisher information ↔ fundamental theorem of natural selection ↔ natural gradient (ML) |
| `physics-climate/` | Phase transitions + EWIs ↔ climate tipping points (AMOC, Amazon, Arctic) |
| `physics-social/` | Ising model ↔ opinion dynamics ↔ social tipping points ↔ echo chambers |

---

## How to add a bridge

1. Use `docs/prompts/bridge_discovery.md` while reading any paper.
2. Create a new subfolder `cross-domain/<field-a>-<field-b>/`.
3. Write `b-<short-name>.yaml` following `schemas/bridge.yaml`.
4. Run `python scripts/validate_schemas.py` — exits 0 if valid.
5. Open a PR; CI validates the schema automatically.

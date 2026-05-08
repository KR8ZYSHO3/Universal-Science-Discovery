"""Patch Wave 42 bridge files to match actual repo schema."""
import os, re, glob

ROOT = r"C:\Users\Shoe\dev\Universal-Science-Discovery"

BRIDGE_FILES = [
    r"cross-domain\neuroscience-physics\b-neuroplasticity-stdp.yaml",
    r"cross-domain\ecology-thermodynamics\b-ecosystem-metabolic-scaling.yaml",
    r"cross-domain\physics-computer-science\b-spin-glass-replica-optimization.yaml",
    r"cross-domain\ecology-chemistry\b-redfield-ratio-ocean-stoichiometry.yaml",
    r"cross-domain\ecology-mathematics\b-predator-prey-hopf-bifurcation.yaml",
    r"cross-domain\neuroscience-physics\b-hodgkin-huxley-conductance.yaml",
    r"cross-domain\materials-science-physics\b-classical-nucleation-theory.yaml",
    r"cross-domain\physics-biology\b-vicsek-active-matter-flocking.yaml",
    r"cross-domain\computer-science-mathematics\b-legal-argumentation-formal-logic.yaml",
    r"cross-domain\quantum-physics-information\b-quantum-decoherence-einselection.yaml",
    r"cross-domain\biology-mathematics\b-morphogen-turing-patterning.yaml",
    r"cross-domain\materials-science-mathematics\b-preisach-hysteresis-model.yaml",
]

def patch_file(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # domains: [x, y] -> fields:\n  - x\n  - y
    def replace_domains(m):
        items = [i.strip() for i in m.group(1).split(",")]
        lines = "fields:\n" + "".join(f"  - {i}\n" for i in items)
        return lines
    text = re.sub(r"domains:\s*\[([^\]]+)\]", replace_domains, text)

    # source: -> field_a_term:
    text = text.replace("  - source:", "  - field_a_term:")
    # target: -> field_b_term:  (only within translation_table context, all occurrences)
    text = re.sub(r"^    target:", "    field_b_term:", text, flags=re.MULTILINE)
    # notes: -> note:
    text = re.sub(r"^    notes:", "    note:", text, flags=re.MULTILINE)

    # Remove confidence line
    text = re.sub(r"^confidence:.*\n", "", text, flags=re.MULTILINE)

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Patched: {os.path.basename(path)}")

for rel in BRIDGE_FILES:
    patch_file(os.path.join(ROOT, rel))

print("All Wave 42 bridge files patched.")

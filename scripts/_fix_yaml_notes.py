"""Fix unquoted colon-in-value YAML errors in untracked bridge files."""
import re

files = [
    'cross-domain/biology-chemistry/b-rna-world-origin-of-life.yaml',
    'cross-domain/biology-engineering/b-tissue-engineering-regenerative-medicine.yaml',
    'cross-domain/ecology-physics/b-nutrient-cycling-stoichiometry.yaml',
    'cross-domain/engineering-mathematics/b-graph-algorithms-network-optimization.yaml',
    'cross-domain/mathematics-computer-science/b-cryptography-number-theory.yaml',
    'cross-domain/mathematics-physics/b-chaos-theory-strange-attractors.yaml',
    'cross-domain/mathematics-physics/b-measure-theory-probability.yaml',
    'cross-domain/neuroscience-physics/b-sensory-adaptation-weber-fechner.yaml',
    'cross-domain/physics-chemistry/b-electrochemical-energy-storage-conversion.yaml',
    'cross-domain/social-science-biology/b-stress-biology-social-determinants.yaml',
    'cross-domain/social-science-engineering/b-hci-cognitive-load.yaml',
]

SCALAR_FIELDS = {
    'note', 'field_a_term', 'field_b_term', 'title', 'bridge_claim',
    'communication_gap', 'summary', 'description', 'label',
}

line_pat = re.compile(r'^(\s+(?:' + '|'.join(SCALAR_FIELDS) + r'):\s)([^"\'|>].*)$')


def needs_quoting(val):
    stripped = val.strip()
    if not stripped:
        return False
    if ':' not in stripped:
        return False
    if stripped.startswith('"') or stripped.startswith("'"):
        return False
    return True


for fpath in files:
    try:
        with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
            lines = f.readlines()
    except Exception as e:
        print(f'Error reading {fpath}: {e}')
        continue

    changed = False
    new_lines = []
    for line in lines:
        m = line_pat.match(line.rstrip('\n'))
        if m:
            prefix, val = m.group(1), m.group(2)
            if needs_quoting(val):
                escaped = val.replace('"', '\\"')
                new_line = prefix + '"' + escaped + '"' + '\n'
                new_lines.append(new_line)
                changed = True
                continue
        new_lines.append(line)

    if changed:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f'Fixed: {fpath}')
    else:
        print(f'No change needed: {fpath}')

print('Done.')

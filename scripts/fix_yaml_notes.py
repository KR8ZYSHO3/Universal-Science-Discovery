import re

def fix_yaml_note_fields(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    lines = content.split("\n")
    fixed_lines = []
    for line in lines:
        m = re.match(r"^(\s+)(field_a_term|field_b_term|note|title):\s+(.+)$", line)
        if m:
            indent, key, value = m.group(1), m.group(2), m.group(3)
            if ":" in value and not value.startswith(">") and not value.startswith("|") and not value.startswith('"'):
                value_escaped = value.replace('"', '\\"')
                line = indent + key + ": \"" + value_escaped + "\""
        fixed_lines.append(line)
    
    fixed = "\n".join(fixed_lines)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(fixed)
    print("Fixed: " + filepath)

files = [
    "cross-domain/biology-physics/b-circadian-clocks-nonlinear-oscillators.yaml",
    "cross-domain/neuroscience-control-theory/b-motor-control-internal-models.yaml",
    "cross-domain/physics-biology/b-cochlear-mechanics-hearing.yaml",
    "cross-domain/social-science-physics/b-traffic-flow-fluid-dynamics.yaml",
]
for f in files:
    fix_yaml_note_fields(f)

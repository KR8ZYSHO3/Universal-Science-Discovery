import re, glob, yaml

def fix_yaml_note_fields(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    lines = content.split("\n")
    fixed_lines = []
    for line in lines:
        # Match any key: value where value contains unquoted colon
        # Keys to check: title, note, field_a_term, field_b_term, description
        m = re.match(r"^(\s*(?:- )?(field_a_term|field_b_term|note|title|description)):\s+(.+)$", line)
        if m:
            prefix, key, value = m.group(1), m.group(2), m.group(3)
            if ":" in value and not value.startswith(">") and not value.startswith("|") and not value.startswith('"'):
                # Escape any existing quotes
                value_escaped = value.replace('"', '\\"')
                # Reconstruct line preserving whether it had "- " prefix
                if "- " in prefix:
                    indent = prefix.replace("- " + key, "")
                    line = indent + "- " + key + ": \"" + value_escaped + "\""
                else:
                    line = prefix + ": \"" + value_escaped + "\""
        fixed_lines.append(line)
    
    fixed = "\n".join(fixed_lines)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(fixed)

files_to_fix = [
    "hypotheses/active/h-langlands-physics-electric-magnetic-duality.yaml",
    "hypotheses/active/h-pain-sex-difference-microglia-spinal-cord.yaml",
    "hypotheses/active/h-placebo-endogenous-opioid-dlpfc.yaml",
    "cross-domain/neuroscience-control-theory/b-motor-control-internal-models.yaml",
]

for f in files_to_fix:
    fix_yaml_note_fields(f)
    print("Fixed: " + f)

# Verify
errors = []
all_files = []
all_files += glob.glob("hypotheses/**/*.yaml", recursive=True)
all_files += glob.glob("cross-domain/**/*.yaml", recursive=True)
all_files += glob.glob("unknowns-catalog/**/*.yaml", recursive=True)

for fpath in all_files:
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            yaml.safe_load(f.read())
    except Exception as e:
        errors.append(fpath + ": " + str(e)[:60])

print("Remaining errors: " + str(len(errors)))
for e in errors:
    print("  " + e)

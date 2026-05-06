import re, glob, yaml

def fix_yaml_note_fields(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    lines = content.split("\n")
    fixed_lines = []
    for line in lines:
        # Match title/note/field_a_term/field_b_term values with unquoted colons
        m = re.match(r"^(\s*)(field_a_term|field_b_term|note|title):\s+(.+)$", line)
        if m:
            indent, key, value = m.group(1), m.group(2), m.group(3)
            if ":" in value and not value.startswith(">") and not value.startswith("|") and not value.startswith('"'):
                value_escaped = value.replace('"', '\\"')
                line = indent + key + ": \"" + value_escaped + "\""
        fixed_lines.append(line)
    
    fixed = "\n".join(fixed_lines)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(fixed)

# Collect all yaml files
files = []
files += glob.glob("hypotheses/**/*.yaml", recursive=True)
files += glob.glob("cross-domain/**/*.yaml", recursive=True)
files += glob.glob("unknowns-catalog/**/*.yaml", recursive=True)

fixed_count = 0
for fpath in files:
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            yaml.safe_load(f.read())
    except Exception:
        fix_yaml_note_fields(fpath)
        fixed_count += 1

print("Fixed " + str(fixed_count) + " files")

# Re-check
errors = []
for fpath in files:
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            yaml.safe_load(f.read())
    except Exception as e:
        errors.append((fpath, str(e)[:80]))

print("Remaining errors: " + str(len(errors)))
for f, e in errors:
    print("  " + f + ": " + e)

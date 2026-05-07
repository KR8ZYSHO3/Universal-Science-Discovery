"""Fix note: fields that contain colons (need quoting) in YAML files."""
import os
import re
import glob
import yaml


def quote_note_values(text):
    """
    For any line matching '  - note: TEXT' or '    note: TEXT' where TEXT
    contains a colon and is not already quoted, wrap TEXT in double quotes.
    Also handle colons in standalone note values inside reference blocks.
    """
    def replacer(m):
        indent = m.group(1)
        value = m.group(2).strip()
        # Already quoted
        if value.startswith('"') or value.startswith("'"):
            return m.group(0)
        # Contains colon and is not a block scalar
        if ':' in value:
            # Escape any existing double quotes
            value = value.replace('"', '\\"')
            return f'{indent}note: "{value}"'
        return m.group(0)

    text = re.sub(r'^([ \t]+note: )([^\n]+)$', replacer, text, flags=re.MULTILINE)
    return text


files = (
    glob.glob("cross-domain/**/*.yaml", recursive=True)
    + glob.glob("unknowns-catalog/**/*.yaml", recursive=True)
    + glob.glob("hypotheses/**/*.yaml", recursive=True)
    + glob.glob("pioneers/**/*.yaml", recursive=True)
)

fixed = 0
skipped = 0
for f in files:
    # First check if the file already parses cleanly
    try:
        with open(f, 'r', encoding='utf-8') as fh:
            orig = fh.read()
        yaml.safe_load(orig)
        # Already valid, skip
        skipped += 1
        continue
    except yaml.YAMLError:
        pass

    # Fix note: values with colons
    try:
        with open(f, 'r', encoding='utf-8') as fh:
            orig = fh.read()
        new = quote_note_values(orig)
        try:
            yaml.safe_load(new)
            if new != orig:
                with open(f, 'w', encoding='utf-8') as fh:
                    fh.write(new)
                print(f"Fixed: {f}")
                fixed += 1
        except yaml.YAMLError as e2:
            print(f"STILL BROKEN after fix: {f}")
            print(f"  Error: {e2}")
    except Exception as e:
        print(f"ERROR {f}: {e}")

print(f"Fixed: {fixed}, already valid: {skipped}")

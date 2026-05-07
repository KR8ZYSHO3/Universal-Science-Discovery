#!/usr/bin/env python3
"""Fix unquoted YAML values containing ': ' that cause parse errors."""
import re
from pathlib import Path

def fix_note_with_colon(filepath):
    content = Path(filepath).read_text(encoding="utf-8")
    lines = content.split("\n")
    changed = False
    for i, line in enumerate(lines):
        m = re.match(r'^(\s+)(note|field_b_term|field_a_term):\s+(.+)$', line)
        if m:
            indent = m.group(1)
            key = m.group(2)
            val = m.group(3)
            if ": " in val and not val.startswith('"') and not val.startswith("'"):
                escaped = val.replace('"', '\\"')
                lines[i] = f'{indent}{key}: "{escaped}"'
                changed = True
    if changed:
        Path(filepath).write_text("\n".join(lines), encoding="utf-8")
        print(f"Fixed: {filepath}")
    return changed

fix_note_with_colon("cross-domain/chemistry-biology/b-protein-post-translational-modifications.yaml")
fix_note_with_colon("cross-domain/engineering-physics/b-optical-fiber-nonlinear-optics.yaml")

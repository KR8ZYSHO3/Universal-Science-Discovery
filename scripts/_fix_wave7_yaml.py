"""Fix schema violations in wave-7 YAML files."""
import os
import re
import glob


def fix_citations(text):
    """Replace 'citation:' key with 'note:' in reference blocks."""
    # With note on next line: '  - citation: X\n    note: Y' -> '  - note: X -- Y'
    def merge_replacer(m):
        cit = m.group(1).strip().strip('"').strip("'")
        note = m.group(2).strip()
        return f"  - note: {cit} -- {note}"

    text = re.sub(r"  - citation: ([^\n]+)\n    note: ([^\n]+)", merge_replacer, text)

    # Without note
    def solo_replacer(m):
        cit = m.group(1).strip().strip('"').strip("'")
        return f"  - note: {cit}"

    text = re.sub(r"  - citation: ([^\n]+)", solo_replacer, text)
    return text


def fix_cross_pollination_colons(text):
    """
    cross_pollination_opportunities items that contain a colon get parsed as
    YAML mappings. Wrap the entire item value in a block scalar or quote it.
    Pattern: '  - Bridge X: description' -> '  - >-\n    Bridge X -- description'
    """
    def replacer(m):
        full = m.group(1)
        # Replace the colon that's being parsed as a mapping key
        # The item looks like: '  - Some text: rest of text'
        # We want: '  - Some text -- rest of text'
        fixed = full.replace(": ", " -- ", 1)
        return f"  - {fixed}"

    # Match list items that have 'Word...: rest' (not '- doi:' or '- note:' etc.)
    text = re.sub(
        r"^  - ((?!doi:|note:|arxiv:|url:|field_|type:|confidence:|summarize:|Apply |Use |Design |Investigate |Bridge |Map |Connect |Sequence)[A-Z][^:\n]+:[^\n]+)$",
        replacer,
        text,
        flags=re.MULTILINE,
    )
    return text


def fix_systematic_gaps_colons(text):
    """Same fix for systematic_gaps items."""
    return fix_cross_pollination_colons(text)


def fix_pioneer_status(text):
    """Fix current_status: established -> open_question in pioneer files."""
    text = re.sub(r"current_status: established", "current_status: open_question", text)
    return text


files = (
    glob.glob("cross-domain/**/*.yaml", recursive=True)
    + glob.glob("unknowns-catalog/**/*.yaml", recursive=True)
    + glob.glob("hypotheses/**/*.yaml", recursive=True)
    + glob.glob("pioneers/**/*.yaml", recursive=True)
)

fixed = 0
for f in files:
    try:
        with open(f, "r", encoding="utf-8") as fh:
            orig = fh.read()
        new = orig
        new = fix_citations(new)
        new = fix_cross_pollination_colons(new)
        new = fix_pioneer_status(new)
        if new != orig:
            with open(f, "w", encoding="utf-8") as fh:
                fh.write(new)
            print(f"Fixed: {f}")
            fixed += 1
    except Exception as e:
        print(f"ERROR {f}: {e}")

print(f"Total fixed: {fixed}")

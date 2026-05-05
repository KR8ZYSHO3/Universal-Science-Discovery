#!/usr/bin/env python3
"""Validate USDR record YAML under hypotheses/, unknowns-catalog/, cross-domain/, and phenomenology/."""
from __future__ import annotations

import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


def load_yaml(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if data is None:
        raise ValueError(f"{path}: empty or non-document YAML")
    if not isinstance(data, dict):
        raise ValueError(f"{path}: root must be a mapping (object)")
    return data


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    schemas = root / "schemas"
    hypothesis_schema  = load_yaml(schemas / "hypothesis.yaml")
    unknown_schema     = load_yaml(schemas / "unknown.yaml")
    bridge_schema      = load_yaml(schemas / "bridge.yaml")
    phenomenon_schema  = load_yaml(schemas / "phenomenon.yaml")
    hypo_validator     = Draft202012Validator(hypothesis_schema)
    unk_validator      = Draft202012Validator(unknown_schema)
    bridge_validator   = Draft202012Validator(bridge_schema)
    phenom_validator   = Draft202012Validator(phenomenon_schema)

    errors: list[str] = []

    for path in sorted((root / "hypotheses").rglob("*.yaml")):
        inst = load_yaml(path)
        for err in hypo_validator.iter_errors(inst):
            loc = "/".join(str(p) for p in err.absolute_path) or "(root)"
            errors.append(f"{path.relative_to(root)} [{loc}]: {err.message}")

    for path in sorted((root / "unknowns-catalog").rglob("*.yaml")):
        inst = load_yaml(path)
        for err in unk_validator.iter_errors(inst):
            loc = "/".join(str(p) for p in err.absolute_path) or "(root)"
            errors.append(f"{path.relative_to(root)} [{loc}]: {err.message}")

    for path in sorted((root / "cross-domain").rglob("b-*.yaml")):
        inst = load_yaml(path)
        for err in bridge_validator.iter_errors(inst):
            loc = "/".join(str(p) for p in err.absolute_path) or "(root)"
            errors.append(f"{path.relative_to(root)} [{loc}]: {err.message}")

    phenom_dir = root / "phenomenology"
    if phenom_dir.exists():
        for path in sorted(phenom_dir.rglob("p-*.yaml")):
            inst = load_yaml(path)
            for err in phenom_validator.iter_errors(inst):
                loc = "/".join(str(p) for p in err.absolute_path) or "(root)"
                errors.append(f"{path.relative_to(root)} [{loc}]: {err.message}")

    if errors:
        print("Schema validation failed:\n", file=sys.stderr)
        for line in errors:
            print(line, file=sys.stderr)
        return 1

    phenom_count = len(list(phenom_dir.rglob("p-*.yaml"))) if phenom_dir.exists() else 0
    print(
        f"OK: all hypothesis, unknown-catalog, cross-domain bridge, "
        f"and phenomenology YAML files validate. "
        f"({phenom_count} phenomenology entr{'y' if phenom_count == 1 else 'ies'})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

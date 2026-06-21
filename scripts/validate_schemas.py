#!/usr/bin/env python3
"""Validate USDR record YAML under hypotheses/, unknowns-catalog/, cross-domain/, protocols-catalog/, phenomenology/, pioneers, and breakthrough-gaps/."""
from __future__ import annotations

import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, Draft7Validator


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
    hypothesis_schema     = load_yaml(schemas / "hypothesis.yaml")
    unknown_schema        = load_yaml(schemas / "unknown.yaml")
    bridge_schema         = load_yaml(schemas / "bridge.yaml")
    phenomenon_schema     = load_yaml(schemas / "phenomenon.yaml")
    pioneer_schema        = load_yaml(schemas / "pioneer.yaml")
    breakthrough_schema   = load_yaml(schemas / "breakthrough_gap.yaml")
    protocol_schema       = load_yaml(schemas / "protocol.yaml")

    hypo_validator        = Draft202012Validator(hypothesis_schema)
    unk_validator         = Draft202012Validator(unknown_schema)
    bridge_validator      = Draft202012Validator(bridge_schema)
    phenom_validator      = Draft202012Validator(phenomenon_schema)
    # pioneer and breakthrough_gap schemas use draft-07 ($schema declaration)
    pioneer_validator     = Draft7Validator(pioneer_schema)
    breakthrough_validator = Draft7Validator(breakthrough_schema)
    protocol_validator    = Draft202012Validator(protocol_schema)

    errors: list[str] = []
    bridge_ids: set[str] = set()

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
        if inst.get("id"):
            bridge_ids.add(inst["id"])
        for err in bridge_validator.iter_errors(inst):
            loc = "/".join(str(p) for p in err.absolute_path) or "(root)"
            errors.append(f"{path.relative_to(root)} [{loc}]: {err.message}")

    protocol_dir = root / "protocols-catalog"
    protocol_count = 0
    if protocol_dir.exists():
        for path in sorted(protocol_dir.rglob("p-b-*.yaml")):
            inst = load_yaml(path)
            protocol_count += 1
            for err in protocol_validator.iter_errors(inst):
                loc = "/".join(str(p) for p in err.absolute_path) or "(root)"
                errors.append(f"{path.relative_to(root)} [{loc}]: {err.message}")
            src = inst.get("source_bridge")
            if src and src not in bridge_ids:
                errors.append(
                    f"{path.relative_to(root)} [source_bridge]: unknown bridge id {src!r}"
                )

    phenom_dir = root / "phenomenology"
    if phenom_dir.exists():
        for path in sorted(phenom_dir.rglob("p-*.yaml")):
            inst = load_yaml(path)
            for err in phenom_validator.iter_errors(inst):
                loc = "/".join(str(p) for p in err.absolute_path) or "(root)"
                errors.append(f"{path.relative_to(root)} [{loc}]: {err.message}")

    pioneer_dir = root / "pioneers"
    if pioneer_dir.exists():
        for path in sorted(pioneer_dir.glob("pioneer-*.yaml")):
            inst = load_yaml(path)
            for err in pioneer_validator.iter_errors(inst):
                loc = "/".join(str(p) for p in err.absolute_path) or "(root)"
                errors.append(f"{path.relative_to(root)} [{loc}]: {err.message}")

    bg_dir = root / "breakthrough-gaps"
    if bg_dir.exists():
        for path in sorted(bg_dir.glob("bg-*.yaml")):
            inst = load_yaml(path)
            for err in breakthrough_validator.iter_errors(inst):
                loc = "/".join(str(p) for p in err.absolute_path) or "(root)"
                errors.append(f"{path.relative_to(root)} [{loc}]: {err.message}")

    if errors:
        print("Schema validation failed:\n", file=sys.stderr)
        for line in errors:
            print(line, file=sys.stderr)
        return 1

    phenom_count   = len(list(phenom_dir.rglob("p-*.yaml"))) if phenom_dir.exists() else 0
    pioneer_count  = len(list(pioneer_dir.glob("pioneer-*.yaml"))) if pioneer_dir.exists() else 0
    bg_count       = len(list(bg_dir.glob("bg-*.yaml"))) if bg_dir.exists() else 0
    print(
        f"OK: all hypothesis, unknown-catalog, cross-domain bridge, crosscheck protocol, "
        f"phenomenology, pioneer, and breakthrough-gap YAML files validate. "
        f"({protocol_count} crosscheck protocol{'s' if protocol_count != 1 else ''}, "
        f"{phenom_count} phenomenology entr{'y' if phenom_count == 1 else 'ies'}, "
        f"{pioneer_count} pioneer entr{'y' if pioneer_count == 1 else 'ies'}, "
        f"{bg_count} breakthrough-gap entr{'y' if bg_count == 1 else 'ies'})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

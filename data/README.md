# Data

This directory is for **non-sensitive** data that the repository is allowed to version.

- **Do not** commit raw identifiable human data, secrets, or unlicensed third-party dumps. See [docs/ETHICS_REPRODUCIBILITY_AND_DATA.md](../docs/ETHICS_REPRODUCIBILITY_AND_DATA.md).
- Prefer **small** derived tables or manifest files that point to externally hosted datasets with licenses and access procedures.
- Document how each file was produced (script path, date, upstream version).

`data/raw/` is gitignored by default; use approved institutional storage for sensitive raw inputs.

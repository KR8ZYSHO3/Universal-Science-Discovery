# Operate this catalog

One ordered list. Stop when the step’s skip condition is true.

This is **not** science. It does not confirm bridges. It does not add records. Night Crew already lands harvested open questions (`u-gap-*`) on GitHub; you do not run YAML for that.

Visitor path stays [USE.md](USE.md). Longer ops appendix: [DEV_DASHBOARD.md](DEV_DASHBOARD.md). **Adding a record:** [CATALOG_BATCH.md](CATALOG_BATCH.md). Harvested waves: [PATH_TO_SUCCESS.md](PATH_TO_SUCCESS.md).

## 1. Get a copy

**Skip if** you already have the project folder.

```bash
git clone https://github.com/KR8ZYSHO3/Universal-Science-Discovery.git
cd Universal-Science-Discovery
```

Need: Python 3.11 or 3.12, and `pip install pyyaml jsonschema networkx` once.

## 2. Open the hub locally

**Skip if** you only need to check files, not the site.

```bash
python -m http.server 8765
```

Open [http://localhost:8765/dashboard/](http://localhost:8765/dashboard/). You should see **USDR · Map · Search · Add · More**. Hosted copy: [the live hub](https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/). Map is full screen.

## 3. Check the catalog

**Skip if** CI on the change already passed this script.

```bash
python scripts/validate_schemas.py
```

Must exit 0.

## 4. Check hub numbers match the files

**Skip if** you did not touch catalog YAML or `dashboard/index.html` snapshot counts.

```bash
python scripts/verify_dashboard_consistency.py
```

Must exit 0.

## 5. After you change catalog records

**Skip if** you did not add or edit unknowns, hypotheses, bridges, or phenomenology.

Follow [CATALOG_BATCH.md](CATALOG_BATCH.md) (validate → map → hub numbers → one review). Do not push generated map files as a silent second commit.

## 6. After you run a test (Crosscheck)

**Skip if** you did not run a protocol.

Capture stdout, then:

```bash
python scripts/apply_crosscheck_result.py --protocol <id> --from-stdout run.txt --apply --refresh-hub
```

This writes `last_run_result` onto the protocol file and the hub card. It does **not** set `status: confirmed`. Honest INCONCLUSIVE stays visible.

## Do not

- Market, register DNS, or submit arXiv from this list
- Auto-promote Wave Factory bridges
- Treat INCONCLUSIVE as a pass or a fail of the science
- Run `promote_unknowns.py --apply` by hand unless you are debugging; Night Crew already lands `u-gap-*`

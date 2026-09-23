# Catalog batch — one local run

One ordered list for **adding or editing catalog records** (open questions, testable ideas, claimed links). Stop when a skip is true.

This is not a second strategy. Visitor path: [USE.md](USE.md). How to *write* a first record: [HAPPY_PATH_FIRST_RECORDS.md](HAPPY_PATH_FIRST_RECORDS.md). Site checks without adding records: [OPERATE.md](OPERATE.md). Harvested drafts and Wave Factory stay in [PATH_TO_SUCCESS.md](PATH_TO_SUCCESS.md).

A person still reads the change before it joins `main`. Do not push straight to `main`. Do not auto-promote bridges.

## 0. Scope

**Skip the rest of this page if** you did not add or edit a catalog file.

One change is one review. Prefer one record, or a small set that belongs together. Do not mix a catalog edit with a hub redesign.

## 1. Write the record

Copy a similar file. Change the title, summary, and references. Do not paste a paper.

| Kind | Where | Id |
|------|--------|----|
| Open question | `unknowns-catalog/<folder>/u-<slug>.yaml` | `u-…` |
| Testable idea | `hypotheses/active/h-<slug>.yaml` | `h-…` |
| Claimed link | `cross-domain/<pair>/b-<slug>.yaml` | `b-…` |

Field-by-field: [HAPPY_PATH_FIRST_RECORDS.md](HAPPY_PATH_FIRST_RECORDS.md). New claims stay `status: proposed` or `draft` until a person promotes them. Never set `status: confirmed` from this list.

## 2. Check the files

```bash
python scripts/validate_schemas.py
```

Must exit 0. **Skip if** the review’s checks already passed this script and you have not edited again.

## 3. Rebuild the map

**Skip if** you only changed docs, not catalog files.

```bash
python -X utf8 scripts/build_graph.py
python scripts/update_dashboard_stats.py --apply
```

## 4. Check the hub numbers

```bash
python scripts/verify_dashboard_consistency.py
```

Must exit 0. If it fails, the snapshot on the hub does not match the files. Fix that in this same change. Do not open a second dump later and merge it silently.

## 5. Send one review

Commit the record **and** the generated map/count files from steps 3–4, if those files changed.

- Branch from `main`. Example title: `content: add u-…`
- Fill the review checklist. A person reads shape first, then the science.
- Do not merge your own science without that read.

If GitHub later opens a **graph rebuild** follow-up, merge that when its checks pass. That follow-up is generated files only, not a second scientific claim.

## Do not

- Auto-promote Wave Factory or night-crew bridges. Those steps stay in [PATH_TO_SUCCESS.md](PATH_TO_SUCCESS.md).
- Land harvested `u-gap-*` by hand. Night Crew already does that.
- Treat INCONCLUSIVE as confirmed.
- Market, register DNS, or submit arXiv from this list.

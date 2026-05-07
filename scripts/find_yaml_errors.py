import glob, yaml

errors = []
for f in glob.glob("hypotheses/**/*.yaml", recursive=True) + glob.glob("cross-domain/**/*.yaml", recursive=True) + glob.glob("unknowns-catalog/**/*.yaml", recursive=True):
    try:
        with open(f, "r", encoding="utf-8") as fp:
            yaml.safe_load(fp.read())
    except Exception as e:
        errors.append((f, str(e)[:120]))

print("Total YAML errors: " + str(len(errors)))
for f, e in errors:
    print("  " + f)

"""Fix Wave 43 schema issues."""
import re, os

ROOT = r"C:\Users\Shoe\dev\Universal-Science-Discovery"

def rf(rel):
    p = os.path.join(ROOT, rel)
    with open(p, "r", encoding="utf-8") as f:
        return f.read()

def wf(rel, t):
    p = os.path.join(ROOT, rel)
    with open(p, "w", encoding="utf-8") as f:
        f.write(t)

# 1. Remove confidence from radiocarbon bridge root
t = rf(r"cross-domain\physics-mathematics\b-radiocarbon-dating-exponential-decay.yaml")
t = re.sub(r"^confidence:.*\n", "", t, flags=re.MULTILINE)
wf(r"cross-domain\physics-mathematics\b-radiocarbon-dating-exponential-decay.yaml", t)
print("Fixed radiocarbon confidence field")

# 2. Fix cav hypothesis - add type to Stern reference
t = rf(r"hypotheses\active\h-cav-phantom-jam-suppression-1percent.yaml")
t = t.replace(
    '  - doi: "10.1038/s41598-018-26668-6"\n    note: ',
    '  - doi: "10.1038/s41598-018-26668-6"\n    type: supporting\n    confidence: 0.75\n    note: '
)
wf(r"hypotheses\active\h-cav-phantom-jam-suppression-1percent.yaml", t)
print("Fixed cav hypothesis evidence type")

# 3. Fix senolytic hypothesis - add type to Baker 2016 reference
t = rf(r"hypotheses\active\h-senolytic-therapy-reduces-cancer-risk-aged-tissue.yaml")
t = t.replace(
    '  - doi: "10.1038/nature16932"\n    note:',
    '  - doi: "10.1038/nature16932"\n    type: supporting\n    confidence: 0.78\n    note:'
)
wf(r"hypotheses\active\h-senolytic-therapy-reduces-cancer-risk-aged-tissue.yaml", t)
print("Fixed senolytic hypothesis evidence type")

print("All Wave 43 fixes applied.")

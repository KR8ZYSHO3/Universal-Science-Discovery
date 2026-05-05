"""Update dashboard stat counts to reflect new totals."""
with open('dashboard/index.html', encoding='utf-8') as f:
    content = f.read()

replacements = [
    ('38 cross-domain bridges', '40 cross-domain bridges'),
    ('266 unknowns', '401 unknowns'),
    ('52 hypotheses', '60 hypotheses'),
    ('id="stat-hyp">52<', 'id="stat-hyp">60<'),
    ('id="stat-unk">266<', 'id="stat-unk">401<'),
    ('id="stat-bridges">38<', 'id="stat-bridges">40<'),
    ('all 357 nodes', 'all 502 nodes'),
    ('<span id="kg-node-count">138<', '<span id="kg-node-count">502<'),
    ('357 nodes', '502 nodes'),
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        print(f'Replaced: {old[:50]}')
    else:
        print(f'NOT FOUND: {old[:50]}')

with open('dashboard/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Dashboard updated.')

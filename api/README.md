# USDR Static JSON API

Base URL: `https://usdr.science/api/v1/`

## Endpoints

| Endpoint | Description |
|----------|-------------|
| `meta.json` | Catalog statistics, counts, and metadata |
| `unknowns.json` | All open unknowns with domain, status, and file path |
| `bridges.json` | All cross-domain bridges with translation tables and references |
| `hypotheses.json` | All active hypotheses with priority and evidence links |
| `domains.json` | Per-domain summary statistics |
| `graph.json` | Full knowledge graph (nodes + edges) |
| `bridge_proposals.json` | AI co-pilot bridge proposals (novelty scores) |

## Example Usage

```javascript
// Fetch all bridges
const res = await fetch('https://usdr.science/api/v1/bridges.json');
const { count, items } = await res.json();
console.log(`${count} bridges loaded`);

// Find bridges connecting two domains
const physicsBiology = items.filter(b =>
  (b.source_domain === 'physics' && b.target_domain === 'biology') ||
  (b.source_domain === 'biology' && b.target_domain === 'physics')
);
```

```python
import requests
data = requests.get('https://usdr.science/api/v1/unknowns.json').json()
astronomy_unknowns = [u for u in data['items'] if u['domain'] == 'astronomy']
```

## Rate Limits

This is a static API served via GitHub Pages — no rate limits, no authentication required.

## License

All data is CC-BY-4.0. Please cite the USDR repository when using this data.

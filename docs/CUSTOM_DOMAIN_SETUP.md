# Custom Domain Setup

## Status
CNAME file committed to repo root — points to `usdr.science`.

## To complete setup:
1. Register `usdr.science` at Namecheap, Cloudflare, or Google Domains (~$12-15/year)
2. Add DNS records at your registrar:
   - Type: CNAME | Name: www | Value: kr8zysho3.github.io
   - Type: A | Name: @ | Value: 185.199.108.153
   - Type: A | Name: @ | Value: 185.199.109.153
   - Type: A | Name: @ | Value: 185.199.110.153
   - Type: A | Name: @ | Value: 185.199.111.153
3. In GitHub repo Settings → Pages → Custom domain → enter `usdr.science`
4. Check "Enforce HTTPS"
5. Wait 10-30 minutes for DNS propagation

## After setup, update these files:
- README.md — dashboard link
- docs/preprint/usdr_preprint.md — repo URL
- docs/outreach/*.md — all links
- dashboard/index.html — og:url meta tag
- api/v1/meta.json — base_url field

# arXiv Submission Guide

## Step 1: Create an arXiv account
- Go to https://arxiv.org/user/register
- Use an institutional email if possible (faster endorsement)
- Request endorsement in cs.DL category if needed

## Step 2: Convert the Markdown preprint to PDF
The preprint is at `docs/preprint/usdr_preprint.md`.

### Option A: Pandoc (recommended)
```bash
# Install pandoc + LaTeX
pip install pandoc
# or: sudo apt-get install pandoc texlive-full

# Convert to PDF
pandoc docs/preprint/usdr_preprint.md \
  -o docs/preprint/usdr_preprint.pdf \
  --pdf-engine=pdflatex \
  --variable geometry:margin=1in \
  --variable fontsize=11pt \
  --bibliography=docs/preprint/references.bib \
  --citeproc
```

### Option B: Use Overleaf (online LaTeX editor)
1. Go to overleaf.com and create a free account
2. New Project → Upload → paste the markdown content
3. Convert headings and formatting to LaTeX manually
4. Download PDF

### Option C: Use a Markdown-to-PDF online converter
- https://www.markdowntopdf.com/
- Upload the file, download PDF
- Quick but lower quality formatting

## Step 3: Submit to arXiv
1. Log into arxiv.org
2. Click "Submit" → "New Submission"
3. Select primary category: **cs.DL** (Digital Libraries and Repositories)
4. Cross-list categories: **q-bio.QM**, **physics.soc-ph**, **cs.IR**
5. Upload PDF
6. Fill in metadata:
   - Title: "Universal Science Discovery Repository: An Open Infrastructure for Cross-Domain Mathematical Bridge Mapping"
   - Authors: Brandon Shoemaker
   - Abstract: [copy from preprint]
7. Submit — paper goes live within 1-2 business days

## Step 4: After submission
- Share arXiv link on X.com, LinkedIn, GitHub
- Add arXiv badge to README
- Contact labs@arxiv.org about arXiv Labs listing
- Update all outreach materials with arXiv DOI

## Step 5: Register `usdr.science` domain
- Namecheap.com or Cloudflare Registrar
- Search for `usdr.science` (~$12-15/year)
- After purchase, follow `docs/CUSTOM_DOMAIN_SETUP.md`

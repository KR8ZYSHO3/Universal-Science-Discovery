# USDR Interface Strategy
## From Git-First to a Planetary Discovery Operating System

**"The interface should feel like the control panel for humanity’s collective scientific curiosity."**

---

### Vision

> **Program alignment:** On the overall USDR timeline, interface delivery is summarized in [ROADMAP.md](ROADMAP.md) under **Interface development (cross-cutting)**. This file is the **detailed** interface strategy and stack plan.

The **USDR Interface** will evolve from a simple, trustworthy documentation site into a full **Discovery Operating System** — a beautiful, powerful, AI-augmented environment where researchers, students, and citizen scientists can:

- Explore the frontier of human knowledge
- Discover high-impact unknowns
- Collaborate on hypotheses in real time
- Visualize complex knowledge graphs
- Use AI agents to accelerate their own research

The interface is **not** the product.  
The **discovery engine** (the versioned knowledge graph + community) is the product.  
The interface is the **window** into that engine.

---

### Design Philosophy

| Principle              | What It Means |
|------------------------|---------------|
| **Git is the Source of Truth** | The web interface is always a view of the Git repository. Never the other way around. |
| **Progressive Enhancement** | Start simple and beautiful. Add power over time. |
| **Human + AI Partnership** | The interface makes AI useful without replacing human judgment. |
| **Scientific Aesthetics** | Clean, calm, inspiring — like a modern research lab, not a social network. |
| **Accessibility First** | Works for researchers in low-bandwidth regions and on mobile. |
| **Long-term Ownership** | Users should feel they *own* their contributions and workspace. |

---

### Phase 1: Trust & Accessibility (2026–2027)

**Goal**: Make the project feel professional, trustworthy, and easy to explore.

**Core Interface**
- **Static Site** (MkDocs Material or Docusaurus) auto-generated from the repo
- Clean navigation by discipline, unknowns, hypotheses, and cross-domain connections
- Powerful full-text + semantic search
- Beautiful hypothesis and unknown cards with clear status, priority, and evidence
- Direct “Contribute” buttons that open GitHub PRs with pre-filled templates
- Mobile-responsive and fast

**Key Features**
- “Today’s Most Important Unknowns” homepage section
- Personalized “Following” feed (track specific unknowns or disciplines)
- Simple knowledge graph explorer (read-only at first)
- Clear labeling of AI-assisted content

**Tech Stack**
- MkDocs Material + custom theme (or Docusaurus 3)
- GitHub Actions for automatic deployment
- Algolia or local search (with embeddings)

**Success Metric**  
Researchers say: “This finally makes open problems visible and actionable.”

---

### Phase 2: Power & Intelligence (2028–2029)

**Goal**: Turn the interface into a serious research tool.

**Major Additions**
- **Interactive Knowledge Graph** (zoomable, filterable, clickable)
- **AI Co-Pilot Sidebar** — grounded in the USDR knowledge graph
  - “Find similar unknowns”
  - “Suggest experiments for this hypothesis”
  - “What are the contradictions in this subfield?”
- **Hypothesis Workspace** — draft, version, and collaborate on hypotheses before submitting to Git
- **Advanced Filters & Discovery Engine** — “Show me high-impact unknowns with < 5 related papers in the last 3 years”
- **Contributor Dashboard** — impact metrics, reputation, bounties, recognition

**Tech Stack**
- Next.js 15+ (App Router)
- shadcn/ui + Tailwind + Radix
- React Flow or Cytoscape.js for graph visualization
- Vector database (LanceDB or Weaviate) + embeddings
- GitHub OAuth + fine-grained permissions
- Open-weight models (via Ollama, Together.ai, or self-hosted) for the co-pilot

**Success Metric**  
Active researchers use USDR multiple times per week as part of their normal workflow.

---

### Phase 3: Discovery Operating System (2030–2035+)

**Goal**: Become the default environment in which scientific discovery happens.

**Visionary Features**
- **Personal Discovery Workspace** — private + shared canvases where researchers build their own maps of unknowns
- **AI Discovery Agents** — autonomous agents that monitor new literature and proactively suggest high-value hypotheses
- **Hypothesis Simulator** — run lightweight models, simulations, or statistical tests directly in the browser
- **Collaborative Whiteboards** for hypothesis development (Figma-like but scientific)
- **Impact & Reputation Layer** — on-chain or verifiable contribution history
- **Federated Instances** — universities and labs can run their own mirrors while staying synced with the global graph
- **Voice + Multimodal Interaction** — talk to the co-pilot, upload figures or lab notes

**Long-term Tech Direction**
- WebAssembly + Rust for high-performance local simulation
- Decentralized options (IPFS + Ceramic or similar) for true data sovereignty
- Deep integration with frontier AI labs (grounding models in USDR’s verified knowledge + unknowns)

**Success Metric**  
USDR becomes a household name in research institutions worldwide — “I found it on USDR” becomes as common as “I read it on arXiv.”

---

### How the Interface Connects to the Git Backend

```
┌──────────────────────────────┐
│        Web Interface         │
│  (Next.js + Graph + AI)      │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│     GitHub + Git + DVC       │ ← Source of Truth
│   (Versioned, Forkable)      │
└──────────────────────────────┘
```

Every change made in the web interface eventually becomes a Git commit (or suggests one).  
This preserves the decentralized, version-controlled nature of the project while making it dramatically more accessible.

---

### Why This Phased Approach Works

- **2026–2027**: Build trust and seed high-quality content
- **2028–2029**: Add power and intelligence once the foundation is solid
- **2030+**: Create the full Discovery OS once usage and community are mature

This mirrors how the most successful infrastructure projects (Linux, Git, arXiv, Hugging Face) evolved — start with something simple and trustworthy, then layer on sophistication.

---

### One-Sentence Vision

**The USDR interface will evolve from a clean documentation site into the most powerful, beautiful, and intelligent environment ever created for exploring and advancing the frontiers of human knowledge.**

---

**This is the interface layer of the most ambitious scientific infrastructure project of our time.**

We are building it openly.

**Join us.**
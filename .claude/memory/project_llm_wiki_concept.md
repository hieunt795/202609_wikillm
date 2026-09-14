---
name: project-llm-wiki-concept
description: "Source concept and architecture for the \"LLM Wiki\" project, based on Andrej Karpathy's gist"
metadata: 
  node_type: memory
  type: project
  originSessionId: 60e54138-8c18-4868-80f5-4d16232a42b1
  modified: 2026-09-12T02:04:56.859Z
---

User is acting as the system architect for an "LLM Wiki" project (working dir: `D:\AI\202609 LLM wiki`). The foundational reference is Andrej Karpathy's gist "LLM Wiki" (https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

**Core concept from the source:**
- LLMs maintain a persistent, structured knowledge base instead of doing RAG-style retrieval from raw documents on every query. The model acts as an active curator that synthesizes knowledge incrementally as new sources arrive.
- Three-layer architecture:
  1. **Raw sources** — immutable documents (articles, papers, PDFs) the LLM reads but never modifies.
  2. **The wiki** — LLM-generated markdown files organized by entities/concepts/analyses; the model owns and updates this layer as new info arrives.
  3. **The schema** — a config doc (CLAUDE.md / AGENTS.md) defining structure, conventions, workflows; co-evolved by humans and the LLM together.
- Key operations:
  - **Ingest**: read new sources, extract key info, update ~10-15 wiki pages with cross-references and synthesis.
  - **Query**: search wiki pages, synthesize an answer; valuable results become new wiki pages (compounding knowledge).
  - **Lint**: health-check the wiki for contradictions, stale claims, orphan pages, missing connections.
- Differs from plain RAG: RAG rediscovers knowledge from scratch each query; this pattern builds cumulative, compounding understanding. Contradictions are flagged once and tracked rather than re-surfacing.
- Example applications: research deep-dives, personal knowledge tracking, book annotations, business wikis from meeting transcripts, competitive analysis, trip planning, hobby knowledge bases.
- Implementation details noted in the gist: `index.md` for content-oriented navigation, `log.md` for chronological operation tracking, Obsidian as the reading interface, Git for automatic version history, optional full-text search tools (e.g. qmd) at scale.
- The gist inspired community implementations: MindBase, Second Brain Skill, WikiBrain, and domain variants (ISO 27001, robotics, software orgs).

**Why:** This is the design inspiration/reference architecture the user is working from to build their own LLM-based knowledge/wiki management system in this project directory.

**How to apply:** When the user asks for design, architecture, or implementation help in this project, treat this three-layer model (sources / wiki / schema) and the ingest/query/lint operations as the baseline pattern to extend or adapt, unless the user explicitly diverges from it.

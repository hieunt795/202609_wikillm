---
name: project-evergreen-notes-concept
description: "Source concept \"Evergreen Notes\" by Andy Matuschak — second reference architecture for the LLM Wiki project"
metadata: 
  node_type: memory
  type: project
  originSessionId: 60e54138-8c18-4868-80f5-4d16232a42b1
  modified: 2026-09-12T12:16:36.415Z
---

Second source reference for the "LLM Wiki" project (see [[project-llm-wiki-concept]]): Andy Matuschak's "Evergreen notes" (https://notes.andymatuschak.org/z5E5QawiXCMbtNtupvxeoEX).

**Core concept:**
Evergreen notes are written and organized to evolve, accumulate, and contribute across projects over time — optimized for "better thinking," not just recording information (contrast with transient/disposable notes).

**Five principles:**
1. **Atomic** — each note focuses on one individual concept.
2. **Concept-oriented** — organized around ideas, not around sources (a note is not "my notes on article X," it's "the idea itself").
3. **Densely linked** — extensively cross-connected to related notes.
4. **Associative ontologies** — prefer networked/associative relationships over rigid hierarchies/folders.
5. **Personal writing** — written for oneself, not for an external audience (affects tone/completeness).

**Supporting practices mentioned:**
- Writing about texts read, to deepen understanding.
- Categorizing notes by type.
- A "reading inbox" to capture references before processing.
- A "writing inbox" for preliminary/unprocessed thoughts.
- "Executable writing" strategies.

**Historical roots:** draws heavily on the **Zettelkasten** (slip-box) method of Niklas Luhmann; Matuschak documents both similarities and differences vs. classic Zettelkasten. Referenced: Ahrens — scattered notes across many locations burden memory; Luhmann's slip-box work outlines a systematic approach to knowledge management.

**Verbatim outline of the entry note (its 16 outbound links, in order — these titles *are* the source's structure):**
1. About these notes
2. Most people take only transient notes
3. "Better note-taking" misses the point; what matters is "better thinking"
4. Evergreen note-writing as fundamental unit of knowledge work
5. Evergreen notes should be atomic
6. Evergreen notes should be concept-oriented
7. Evergreen notes should be densely linked
8. Prefer associative ontologies to hierarchical taxonomies
9. Write notes for yourself by default, disregarding audience
10. Zettelkasten
11. Similarities and differences between evergreen note-writing and Zettelkasten
12. Write about what you read to internalize texts deeply
13. Taxonomy of note types
14. A reading inbox to capture possibly-useful references
15. A writing inbox for transient and incomplete notes
16. Executable strategy for writing

(Note itself is ~3 short paragraphs; nearly all substance lives in the linked sub-notes — itself a demonstration of the "atomic + densely linked" principles. Stable URL also resolves at /Evergreen_notes.)

**Deeper findings (from reading the linked sub-notes, not just the entry note):**
- *Atomic* is a balance, not maximal splitting: "one subject, covered comprehensively" — too-broad notes hide connections, too-fragmented notes dilute the link network. Metaphor: a good note is like a good API.
- *Titles are like APIs* — the title is the interface other notes "call"; must be precise and reusable outside any source context.
- *Tags are described as ineffective* for association; fine-grained `[[links]]` are the real connective tissue. (Tension with this project's token-efficiency design, which uses frontmatter `tags` as a cheap filter index — resolution: tags = performance index only, never a substitute for links.)
- *Stub links*: link freely to notes that don't exist yet / are incomplete — don't wait to finish a note before linking to it.
- Associative-ontology heuristic: ask **"in what context will I want to encounter this again?"** instead of "which category does this belong to?"
- *Taxonomy of note types* (developmental ladder): ephemeral scratchings → writing-inbox notes → evergreen notes, where evergreen itself has substages: **stub → simple definition → bridge note (narrowly connects 2 adjacent concepts) → declarative note (complete-phrase/assertion title) → question-framed note (when evidence is inconclusive) → higher-level API note → abstract note (synthesizes many notes)**. Outside the ladder: literature notes (titled after one work — equivalent to this project's `01_sources/`), person/business notes, log notes.
- *Title rules* (from "Prefer note titles with complete phrases…" + "Prefer positive note titles…"): default to **complete declarative phrases** (a sharp title creates pressure to actually support the claim); **questions** are valid titles when evidence is inconclusive but are a temporary state to be refactored into declaratives; **noun phrases are the exception**, reserved for core terms other notes orbit around (this is why `gdp`, `absorption` etc. stay nouns in this project); prefer **positive** over negative framing ("Metacognitive supports require dynamic environments" beats "Passive environments can't offer metacognitive support"); being unable to write a sharp title signals muddy thinking or an atomicity violation.
- A note should be small enough to finish in one sitting (Matuschak: under ~30 minutes).
- Accumulation mechanism: "Knowledge work should **accrete**" — transient notes leave "a pile of dissociated notes" that "won't have added up to anything." Two pathways: insight accumulation + reading accumulation. Searching for links while writing a new note acts as **informal spaced repetition** over old notes.

**Why relevant to this project:** This is explicitly being gathered (alongside Karpathy's LLM Wiki gist) as a second foundational reference for designing the project's own LLM-based wiki system. Likely tension/complement to track: Karpathy's model is LLM-as-curator with ingest/query/lint operations over markdown; Evergreen Notes is a human-authored-note philosophy (atomicity, concept-orientation, dense linking, associative structure, personal voice) — the project may want to adapt evergreen-note principles (esp. atomic + concept-oriented + densely linked) into the `02_wiki/` page design (see taxonomy in `00_schema.md`: entity/concept/analysis).

**How to apply:** When advising on wiki page granularity, linking strategy, or note-writing style for this project, draw on these 5 principles as a second design lens alongside the Karpathy 3-layer/ingest-query-lint architecture already adopted in the project structure (00_schema.md, agents.md, 01_sources/, 02_wiki/, log.md).

---
name: portfolio-pdlc-wire
description: Stand up a portfolio-pdlc workspace from whatever an organization already has — folders of decks and docs, a Jira/Align export, a spreadsheet of initiatives, or a blank page. Use when wiring the portfolio PDLC for the first time, onboarding an engagement's existing initiative material into the operating system, or re-wiring after a major re-scoping. Produces the charter, workflow definition, initiative cards, and first generated board. Part of the portfolio-pdlc family.
metadata:
  tags: flow-agile, product-strategy
  version: 1.0.0
---

# Portfolio PDLC — Wire

## Outcome

A folder that satisfies the portfolio workspace contract: charter, workflow definition,
one card per significant investment with honest (not aspirational) frontmatter, and a first
generated board that already tells leadership something true. Start with what exists —
**map, don't invent**.

## Inputs

Point me at the material: a folder tree, exports (CSV/Jira/Align), decks, meeting notes —
or name the initiatives conversationally. Also useful: who sponsors the portfolio, and any
existing workflow/stage language the org already uses.

## Workflow

1. **Inventory before structure.** Sweep the provided material and list candidate
   initiatives with whatever stage/owner/size evidence exists. Present the inventory before
   creating anything — merging duplicates and spotting "one initiative wearing three names"
   happens here.
2. **Instantiate the workspace** from `skills/portfolio-pdlc/templates/` (charter, pdlc,
   topology, AGENTS.md). Keep the default lifecycle stages unless the org has real stage
   language — then map theirs onto the default in the pdlc.md table (the narrative aliases
   column exists for exactly this).
3. **Have the two wiring dialogues** (with the human, or record explicit defaults if
   running headless and flag them in the charter):
   - **Flow boundaries**: where does tracking start (idea? business ask?) and end (outcome
     measured → operational roadmap)?
   - **Altitude**: scale-up scoring rule (size + strategic + collaboration, 1–3 each) or
     enterprise rule (Baseline Gate + 2-of-4 constraint tests)? Score every candidate;
     3–4 → Tier-2 awareness lane, 5–6 → flag for conversation, 7–9 → Tier-1.
4. **Create the cards.** One `initiatives/<slug>/initiative.md` per investment from the
   template. Honesty rules:
   - `stage` = where the evidence says it is, not where anyone wishes; note doubts inline.
   - `stage_entered` = best evidence (doc dates, commit history, "roughly March" → first of
     month, noted as approximate).
   - `orientation: mixed` unless the source material genuinely steers on outcomes — the
     assess skill upgrades it, never the wire.
   - Leave gaps visible (no `outcome_hypothesis` yet is a finding, not an embarrassment).
5. **Backfill history if it exists.** Prior stage transitions worth having (from status
   reports or tracker history) may be seeded into `flow-log.csv` — this is the ONE
   sanctioned hand-touch of that file, done chronologically, before the first board run.
6. **Generate the first board**: `python3 <this-repo>/skills/portfolio-pdlc/scripts/portfolio_board.py <ws>`.
7. **Write the wiring brief** (`reviews/YYYY-MM-DD-wiring-brief.md`): what got mapped, what
   got merged, altitude calls made, the board's first-read headlines (busy board? risk
   balance? oldest items?), and the open questions for the sponsors.

## Rules

- Map, don't invent: every card traces to source material or a named human statement.
  Fabricated detail poisons every later assess.
- Don't fix while wiring. Activity-framed titles, missing hypotheses, stale stages — record
  them as they are; improving cards is `portfolio-pdlc-compound`'s job on later cycles.
- Tiering is a proposal until a sponsor confirms it; say so in the wiring brief.
- A busy first board is information, not failure — the minibook's three causes (too much in
  flight / over-centralized / factions) go in the brief as hypotheses, not accusations.

## Quality Gates

- Workspace passes the board script with zero contract violations.
- Every card names its source material.
- Flow boundaries and the altitude rule are written into the charter (or flagged as
  defaulted-pending-sponsor).
- The wiring brief states the board's first three headlines in sponsor language.

## References

- `skills/portfolio-pdlc/references/workspace-contract.md`, `templates/`
- Umbrella: `portfolio-pdlc` (operating loop starts after wiring)

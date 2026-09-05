---
name: sniff-test-portfolio
description: Add-on to the sniff-test skill that looks across many initiatives on a portfolio Kanban for board-level patterns — duplicate/shadowing initiatives, WIP clustering, stale-status sweeps, experiment scope creep, and portfolio risk balance (Explore/Discovery vs. Build & Deliver split). Use when reviewing a whole board or portfolio, prepping a sponsor/ELT portfolio review, or deciding where the portfolio is over- or under-invested. For sniffing a single initiative, use sniff-test.
metadata:
  tags: flow-agile, product-strategy
  version: 1.0.0
---

# Sniff Test — Portfolio Add-On

## Outcome

Across a set of initiatives (a portfolio Kanban or any backlog), surface the **board-level** patterns a single-initiative sniff can't see — so leadership can rebalance risk, kill duplication, and find hidden WIP. Per-initiative clarity reads come from the base `sniff-test` skill; this add-on is about the relationships *between* items.

## When To Use

- Reviewing a whole portfolio Kanban or backlog, not one item.
- Prepping a sponsor / ELT portfolio review or a "where are we over-invested?" conversation.
- After running single-initiative sniffs on several items and wanting the cross-cutting story.
- Checking whether the portfolio's risk exposure is intentional.

## Prerequisite

Run (or assume) base `sniff-test` reads on the individual items first — verified stage + clarity-by-dimension per initiative. This add-on consumes those reads; it does not replace them.

## How to Run Me — What to Feed Me

Point me at the **portfolio's system of record**: the portfolio Kanban (Tier-1 board), the Jira project/board, the Confluence portfolio space, or the folder where initiative canvases and roadmaps live. The more of each initiative's Lean Product Canvas, Outcome-Oriented Roadmap, and recent sponsor update I can reach, the more reliable the stale-status sweep and risk-balance split become. With thin input I'll work from whatever board snapshot you give me and flag low coverage — board-level findings degrade fast when the per-initiative evidence isn't reachable.

## Scan Approaches — pick deliberately

| Approach | What it is | When to use |
|---|---|---|
| **Full-board baseline** | Sniff every initiative as a baseline | A dedicated session or major portfolio-review agenda item. Establishes the baseline you compare actuals against later. |
| **Random sample** | Sniff a random selection across stages | Building the muscle; spot-checking board health. |
| **Stage debrief** | Sniff all items that just passed a stage | e.g., everything newly committed into Execute/Build. |
| **Cadence** | Sniff on a rhythm | After a planning interval; as part of the Strategic Portfolio Review. |

State the chosen approach and the altitude (Tier-1 enterprise only, or including Tier-2 domain/team work) in one line.

## Portfolio Patterns To Detect

1. **Duplicate / shadowing initiatives.** Two+ items covering substantially the same problem, or one quietly subsuming another. Smell: fuzzy boundaries between a parent initiative and its "refinement." Move: merge, make one a sub-issue, or sharpen the distinct bet each represents.
2. **WIP clustering / hidden imbalance.** Many initiatives piled in one domain or one stage while others starve. Smell: every "top priority" pointing the same way; lots of work stuck just before a commitment point. Move: surface the real tradeoff for a leadership capacity decision.
3. **Portfolio risk balance (Explore/Discovery vs. Build & Deliver).** What share of capacity sits in **Explore / Discovery** (uncertain, exploratory, smaller bets) vs. **Execute/Build + Rollout** (committed, known ROI trajectory)? The framework frames this like a financial portfolio — leadership should see the split and manage it intentionally (a common practitioner reference point is ~20% in de-risking / ~80% in build-and-deliver). Smell: ~100% committed work (no exploration → future surprises) or runaway exploration that never commits.
4. **Stale-status sweep.** Board-wide version of the single-item check: which status labels disagree with the evidence (shipped output, downstream artifacts, go-live state, git history)? Stale labels distort the whole portfolio picture. Move: correct the stages, then re-read the balance.
5. **Experiment scope creep.** Items framed as small Explore/Discovery experiments that have ballooned into full builds. Smell: an "experiment" with a delivery-sized footprint and no proceed/stop decision. Move: re-cut to the riskiest assumption, or graduate it honestly to a committed Execute/Build.
6. **Watermelon clustering.** A pattern of initiatives that were green throughout and turned out misplaced — points at a systemic gap in how the portfolio reads its own confidence, not just one bad bet.

## Rules

- **Patterns, not re-grading.** Don't re-sniff each item in depth; consume the base reads and report the relationships.
- **Correct stages before reading balance.** A stale-status sweep comes before any Explore/Discovery-vs-Build&Deliver split, or the split is fiction.
- **Make tradeoffs visible; don't resolve them silently.** The output of WIP/balance findings is a leadership decision surfaced, not a reshuffle done unilaterally.
- **Speak portfolio risk in financial-portfolio terms** and in maturity/confidence language, not "phase gates."
- **Keep altitude honest.** Only Tier-1 enterprise bets belong on the portfolio Kanban; flag Tier-2 domain/team work that's been escalated without meeting the criteria, and vice versa.

## Output Modes

- `portfolio scan` (default): a compact table of initiatives × verified stage × clarity summary × pattern flags, plus a short narrative of the 2–4 cross-cutting findings and the risk-balance split.
- `risk-balance view`: just the Explore/Discovery vs. Build & Deliver split with the rebalancing conversation.
- `review brief`: a sponsor/ELT-ready summary — what's duplicated, where WIP is hidden, whether risk exposure is intentional, and the decisions requested.

## Quality Gates

- A stale-status sweep is done before any risk-balance claim.
- At least the duplication, WIP-clustering, and risk-balance patterns are explicitly checked.
- Each pattern flag names a specific leadership conversation or decision, not a vague observation.
- The risk-balance split is stated, with whether it looks intentional.
- Altitude (what belongs on the portfolio board) is assessed.

## References

- Base skill: `sniff-test.md` and its references for per-initiative clarity dimensions, the lifecycle rubric, and the Risk/Derisking Matrix.

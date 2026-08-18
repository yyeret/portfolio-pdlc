---
name: portfolio-pdlc-assess
description: The sensing pass of the portfolio-pdlc operating system. Use when asking "where is everything really, and is it outcome-oriented or activity-oriented?" — full portfolio reads, review/investment-council prep, stale-status sweeps, or restoring board integrity after contract violations. Verifies stages against evidence, classifies every card on the input→impact ladder, reads flow and risk balance, and outputs a review brief with ranked candidate moves. Composes the sniff-test and sniff-test-portfolio skills included in this repo.
metadata:
  tags: flow-agile, product-strategy
  version: 1.0.0
---

# Portfolio PDLC — Assess

## Outcome

An evidence-verified read of the whole portfolio: corrected stages, an
outcome-vs-activity classification per card, flow and risk-balance findings, and a ranked
list of candidate moves — packaged as a review brief a sponsor can decide from. Assessment
changes `orientation` fields and fixes contract violations; it never advances stages or
rewrites cards (that's advance/strengthen work on later cycles).

## Modes

- `full` (default): everything below, board-wide.
- `sweep`: steps 1–2 only — restore board integrity and correct stale statuses.
- `review-prep`: full assess rendered as the investment-council brief
  (`templates/review.md`), decisions-first, with 1–2 sparring-pit nominations.

## Workflow

1. **Regenerate the board** (script). Fix contract violations first — a board that can't
   build lies about everything else.
2. **Stale-status sweep — verify stages against evidence.** For each in-flow card, corroborate
   the claimed stage against reality: artifacts present, decision-log entries, shipped
   output, tracker/git history, dates. Correct `stage`/`stage_entered` where evidence
   disagrees (note the correction in the card's Evidence log). Stage labels are claims;
   this step is why the rest of the read can be trusted. **Do this before any balance or
   flow claim.**
3. **Classify orientation on the input→impact ladder.** For each Tier-1 card, read title +
   hypothesis + indicators and place what the card actually steers on:
   input → activity → output → outcome → impact.
   - Steers on outcomes/impact with plausible leading indicators → `orientation: outcome`
   - Names outcomes but steers on outputs/activities (or indicators are activity counts) → `mixed`
   - Solution/activity-first, no outcome in sight → `activity`
   Write the field; cite the tell (one line) in the Evidence log. This is the portfolio's
   "outcome-oriented vs activity-oriented" x-ray.
4. **Clarity-vs-stage reads.** Where depth is warranted (decision imminent, big money,
   suspicion), run `sniff-test` (this repo) per initiative — clarity relative to stage
   across Desirability/Viability/Feasibility, evidence vs opinion, derisking fit. The core
   rubric, inline: early stages may be uncertain (healthy);
   committed stages carrying opinion-tagged riskiest assumptions are the smell
   (watermelon risk; rubber-stamp commits).
5. **Board-level patterns.** Run `sniff-test-portfolio` (this repo) for duplicates/
   shadowing, WIP clustering, and experiment scope creep; at minimum check:
   duplicated problem space across cards, one team's name dominating `dependencies:`,
   "experiments" with delivery-sized footprints, and the Explore+Discovery vs committed
   split (state whether it looks intentional; ~20/80 is a common practitioner reference point — an
   anchor for conversation, not a law).
6. **Write the brief** to `reviews/` (review-prep mode uses the council template):
   corrected stages (what moved and why), orientation counts and worst offenders, flow
   findings, risk balance, and **ranked candidate moves** phrased in the umbrella skill's
   leverage-table terms — so the next loop cycles have a queue.

## Rules

- Correct stages before reading balance — the sweep precedes every other claim.
- Evidence beats opinion; unevidenced confidence is a question mark and gets said plainly.
- Assess doesn't fix. Findings become candidate moves, improvement cards, or brief lines —
  never in-place rewrites during the assessment.
- Confidence language for sponsors; no gates, no compliance tone. Findings name the
  conversation they should trigger.
- Note coverage honestly: cards whose evidence was unreachable get "unverified," not a guess.

## Quality Gates

- Board regenerated before and after; zero contract violations at exit.
- Every Tier-1 card has a current, cited `orientation` value.
- Stage corrections logged in the affected cards' Evidence logs.
- Risk-balance split stated with an intentionality judgment.
- The brief's candidate moves map to leverage-table rows (so the loop can consume them).

## References

- Ladder + derisking rubric: `skills/sniff-test/references/derisking-and-indicators.md`
  (this repo).
- Templates: `skills/portfolio-pdlc/templates/review.md`

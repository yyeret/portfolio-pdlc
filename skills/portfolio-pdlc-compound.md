---
name: portfolio-pdlc-compound
description: Improve the quality, outcome orientation, and derisking of ONE initiative's artifacts in the portfolio PDLC — rewrite activity-framed cards into outcome hypotheses with leading indicators, sharpen riskiest assumptions with evidence/opinion tags, fix derisking-approach mismatches, and capture at most one durable learning. Use on cards flagged activity-oriented, thin on evidence, missing indicators, or carrying committed money with open risks. The loop-2 skill of the portfolio-pdlc family.
metadata:
  tags: flow-agile, product-strategy
  version: 1.0.0
---

# Portfolio PDLC — Compound

## Outcome

One card upgraded from status-report material to steering instrument: outcome-framed,
carrying leading indicators a sponsor can actually steer by, riskiest assumptions tagged
and matched with a proportionate derisking plan — plus, when the work taught something
durable, exactly one learning captured for the operating system.

## Pick-one rule

One card per invocation. Committed money outranks ideas: given a choice, strengthen the
execute/rollout card before the explore card (the umbrella leverage table encodes this).

## Workflow

1. **Read the card cold.** Title, hypothesis, indicators, assumptions, evidence log — plus
   its source material if reachable. Where on the input→impact ladder does it actually
   steer? (input → activity → output → outcome → impact.)
2. **Rewrite for outcome orientation** (an OKR-rewriting skill composes here if you have
   one; the rules below suffice on their own):
   - Title says what becomes true for whom — not the solution being built. Lightweight
     first move when a full rewrite is premature: fix the name.
   - `outcome_hypothesis` in testable form: *if [user/stakeholder] attains [benefit] via
     [change], we expect [business impact]*.
   - Card-format alternatives are legitimate (OKR card, A3, Lean Canvas, DIBB bet) — match
     the org's language; the invariant is outcome + evidence, not the template.
3. **Leading indicators — Goldilocks or nothing.** Each indicator must give feedback in
   reasonable time AND plausibly correlate to the outcome. Replace activity counters
   ("12 features shipped") with sense-and-respond signals. One Metric That Matters for the
   current riskiest assumption beats five vanity numbers. Include current values or `n/a`
   honestly.
4. **Sharpen the riskiest assumptions.** Tag every claim **evidence** or **opinion** across
   Desirability / Viability / Feasibility. Confident-but-unevidenced items move to the top
   of the discovery agenda. Name watermelon risk plainly where clarity is asserted deep in
   the lifecycle without evidence.
5. **Fix the derisking fit.** Match approach to risk: low → just-do-it; medium → ship &
   measure; high → discovery/testing or seek-alpha (deliberately attack the scariest
   unknown). Both mismatch directions are smells — heavyweight discovery on the certain,
   "just build it" on the speculative. Update `risk_level` / `derisking_approach` and the
   Derisking plan section; note in the card if the mismatch implies a stage conversation
   (that's an advance move, not yours).
6. **Record.** Evidence log entry (what changed and why), `orientation` updated only if the
   card now genuinely steers on outcomes, board regenerated.
7. **Compound — at most one learning.** If this rewrite exposed something durable (a
   recurring anti-pattern, a template gap, a language fix that landed), write ONE
   `learnings/<slug>.md` (contract format). If it implies changing the operating model,
   also capture an `improvements/` card — the learning holds the evidence, the card holds
   the bet. Zero learnings is a fine outcome; forced learnings are noise.

## Rules

- Improve the card, not the initiative's plan of record — scope/commitment changes are
  decisions for humans, prepared via advance.
- Preserve the author's voice and the org's vocabulary; this is sharpening, not
  ghostwriting a consulting artifact.
- Never upgrade `orientation` as a courtesy. The field follows the words, not the intent.
- Indicators without current values are flagged `n/a`, not invented.
- One card, at most one learning, board regenerated — the compound loop stays small on
  purpose.

## Quality Gates

- The card's title + hypothesis pass the ladder test at outcome level (or the brief says
  why not yet, and what's missing).
- Every riskiest assumption carries an evidence/opinion tag.
- Derisking approach matches risk level, or the mismatch is escalated as a candidate move.
- ≤1 learning captured, in contract format, only if it changes future behavior.

## References

- Ladder + Goldilocks/OMTM: `skills/sniff-test/references/derisking-and-indicators.md`
  (this repo).

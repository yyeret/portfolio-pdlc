# Probe Library — Improving the PDLC and the Portfolio Construction

Derived from the Portfolio Agility Trailmap (the minibook behind
`scaling-product-organizations-with-portfolio-agility`) plus enterprise portfolio operating experience.
Used by `portfolio-pdlc-improve`. Each probe is something to **sense in the workspace data**,
the **question it forces**, and the **typical move** — which, when warranted, becomes an
improvement card, never an on-the-spot change.

Format per probe: **Signal** (computable or readable from board/flow-log/cards) →
**Question** → **Typical move**.

## Family A — Process probes (the PDLC itself)

**A1. Flow boundaries start too late.**
Signal: cards first appear at Plan/Commit or Execute; `flow-log.csv` shows few or no
Explore/Discovery entries. Question: where do initiatives actually get intercepted — and how
much speed/impact opportunity dies before we see them? Move: shift the start boundary
earlier; add idea intake to Explore.

**A2. Altitude drift.**
Signal: Tier-1 cards with `portfolio_score` ≤ 4, or Tier-2 cards scoring 7–9; review notes
that read tactical. Question: are portfolio conversations at cruising altitude — engaging,
steering, right-level — or too low (tactical, leaders disengage) / too high (real strategy
handled in side channels)? Move: re-score the board, move cards across tiers, restate the
threshold in PORTFOLIO.md.

**A3. Busy board.**
Signal: WIP well above limits (or no limits), many stages crowded, ages long across the
board. Question: which of the three causes dominates — too many things in flight, too much
centralization (managing work that belongs to teams), or factions running parallel agendas?
Move: differs by cause — WIP freeze / re-tier to awareness lane / merge factional boards.

**A4. No right-to-left habit.**
Signal: loop-log and reviews consistently discuss new/Explore items before aging Execute
items; throughput flat while intake grows. Question: are we finishing before starting?
Move: encode right-to-left review order in pdlc.md policies; "no new work" period.

**A5. Missing explicit discovery-vs-skip decision.**
Signal: cards jump explore → plan-commit with `risk_level: high` and no Discovery entry in
flow-log; Decision logs silent on why discovery was skipped. Question: who decided to skip
discovery, and was that a risk-based call or a habit? Move: add the explicit fork to
pdlc.md ("go through discovery, or skip it — decided, not defaulted"); template prompt in
the card.

**A6. Rubber-stamp commits.**
Signal: Plan/Commit entries whose riskiest assumptions are all tagged *opinion*; commit
decisions dated the same day the card entered plan-commit. Question: is the investment
decision real — could the answer have been "no"? Move: "what would make us say no" prompt
in the decision brief; minimum evidence expectations per risk level.

**A7. No measure-and-learn tail.**
Signal: cards go execute → done with no BAU period, no indicator readings in the Evidence
log after rollout. Question: did the outcome hypothesis actually land? Are we seeing
diminishing returns? Is this still a business constraint? Move: add the four
measure-and-learn questions to the BAU policy; keep cards in BAU until indicators are read.

**A8. No SLE / expectation management.**
Signal: enough flow-log history to compute stage cycle times, but no Service Level
Expectation stated in pdlc.md; sponsors surprised by durations. Question: what can we
honestly promise about time-through-stage today? Move: publish SLE from percentiles;
review breaches.

**A9. Recurring stale statuses.**
Signal: assess sweeps keep re-flagging the same cards/owners for stage-vs-evidence
mismatch. Question: what makes honesty expensive here? Move: reduce status theater —
smaller stages, evidence-based board regeneration cadence, sponsor language shift.

**A10. Watermelon retros missing.**
Signal: `learnings/` has no `watermelon` entries though initiatives have completed; no
baseline-confidence-vs-actual comparison anywhere. Question: where were we confidently
wrong, and what does that say about how we read our own confidence? Move: add a BAU-exit
retro comparing lifecycle clarity claims to results; log watermelons as learnings.

**A11. Risk-balance drift.**
Signal: board's Explore+Discovery share of Tier-1 WIP near 0% (all-in on committed builds)
or persistently huge (exploration that never commits). A common practitioner reference point:
roughly ~20% de-risking / ~80% build-and-deliver — a conversation anchor, not a law.
Question: is our risk exposure intentional? Move: state a target split in PORTFOLIO.md;
rebalance intake.

## Family B — Topology / portfolio-construction probes

**B1. Dependency concentration (the 80/20 team).**
Signal: one name dominates `dependencies:` across cards (count them); that team appears in
most Execute-stage delays. Question: which constraint would, if relieved, localize the most
work? Move: improvement card exploring platform extraction, T-shaping into that skill, or
intake protection for that team.

**B2. Platform extraction candidate.**
Signal: the same capability (billing, auth, data access, publishing) named as a dependency
by 3+ initiatives across different products. Question: would a self-service platform melt
this iron spaghetti — and what's the smallest slice that proves it? Move: improvement card
(`improvement-topology`), Discovery via `portfolio-pdlc-simulate` (dependency-tax scenario)
plus one real tracer initiative.

**B3. Oversized initiative hogging the lane.**
Signal: one card's age and dependency list dwarf everything in its stage; other items queue
behind it. Question: can it split into independently valuable investments, each worth
finishing on its own? Move: split proposal as a decision brief; don't split unilaterally.

**B4. Factional structure.**
Signal: initiative sources/owners cluster into camps that never share dependencies or
reviews; duplicate/shadowing cards (see `sniff-test-portfolio`). Question: is the org
coordinating one portfolio or several competing ones? Move: merge boards; make redundancy
visible on one board and let leadership choose.

**B5. Outcome-team candidate.**
Signal: a strategic outcome repeatedly needs the same 3–4 teams' collaboration
(`dependencies` co-occurrence). Question: would a stable broader-perspective team — or a
transient strategically-focused one — own this outcome with fewer handoffs? Move:
improvement card comparing team-topology options.

**B6. T-shaping candidate.**
Signal: a narrow skill (one team, even one person) appears on the critical path of multiple
cards' Derisking plans or delays. Question: what would it take for adjacent teams to
self-serve 80% of this? Move: improvement card for deliberate cross-skilling; measure
dependency count as the leading indicator.

**B7. Option comparison discipline.**
Not a detector — the rubric every topology bet must pass before Plan/Commit. Compare each
design option **including the current state** on: (1) % of portfolio work localized (aim
for a strong majority — 80% is better); (2) size of change from today (change is hard);
(3) product/technology/people risk (e.g., moving a core capability to people with limited
know-how); (4) future-proofness against strategy and horizon. Evolve the chosen option like
a product: outcomes, leading indicators, discovery, increments.

## Using the library

- A probe run reads data first (board, flow-log, cards, reviews); a probe with no signal is
  reported as "checked, quiet" — that's information too.
- Every fired probe yields either an improvement card or an explicit "not worth a card
  because…" line in the review brief. No free-floating advice.
- Probes never change `pdlc.md`, `topology.md`, or tiers directly — those are Plan/Commit
  decisions on improvement cards.

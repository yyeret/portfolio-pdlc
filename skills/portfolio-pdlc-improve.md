---
name: portfolio-pdlc-improve
description: Probe the portfolio operating system itself — both the PDLC process (flow boundaries, altitude, WIP, discovery discipline, measure-and-learn) and the portfolio construction/topology (dependency concentration, platform extraction, team-around-outcome options) — and capture improvement ideas as spec-driven bets in the improvements/ backlog instead of implementing them on the spot. Use when the board is healthy enough to earn self-improvement, after recurring findings, or on an improvement cadence. Loops 3+4 of the portfolio-pdlc family; focus:process, focus:topology, or focus:auto.
metadata:
  tags: flow-agile, product-strategy
  version: 1.0.0
---

# Portfolio PDLC — Improve

## Outcome

The operating system gets treated as a product: probes run against real workspace data,
each fired probe becomes either an improvement card (benefit hypothesis, leading
indicators, success/kill criteria, discovery approach) or an explicit "checked, quiet"
line — and **nothing gets changed on the spot**. The improvement backlog is where
compounding lives; impulse edits to pdlc.md are how operating models rot.

## Focus argument

- `focus:process` — Family A probes (the PDLC itself)
- `focus:topology` — Family B probes (portfolio construction: dependencies, platforms, team shapes)
- `focus:auto` (default) — read the board and recent briefs, run the 3–5 probes the data
  is already pointing at across both families

## Workflow

1. **Load the probe library**: `skills/portfolio-pdlc/references/probe-library.md`
   (Family A: flow boundaries, altitude drift, busy board, right-to-left habit, explicit
   discovery-vs-skip, rubber-stamp commits, measure-and-learn tail, SLE, recurring stale
   statuses, watermelon retros, risk-balance drift. Family B: dependency concentration,
   platform extraction, oversized initiatives, factions, outcome-team candidates,
   T-shaping, option-comparison discipline).
2. **Gather the data first**: current `board.md`, `flow-log.csv`, recent `reviews/`,
   `learnings/`, `topology.md`, and the cards' `dependencies:` fields (count name
   frequency — the 80/20 read). Probes read data; they don't free-associate.
3. **Run the selected probes.** For each: signal present? cite the data. No signal? one
   "checked, quiet" line. Recurring learnings in `learnings/` count as signal (three
   similar `card-quality` learnings = a template/process probe firing).
4. **Capture bets, not fixes.** Each fired probe worth acting on becomes
   `improvements/<slug>/improvement.md` (template): benefit hypothesis, leading indicators,
   success/kill criteria, and the cheapest discovery — a data probe, a one-review pilot, a
   single-initiative tracer, or a `portfolio-pdlc-simulate` scenario (name the scenario in
   the card). Topology bets MUST include the option-comparison table (B7): each option vs
   current state on % work localized / change size / risk / future-proofness.
5. **Right-size the ceremony.** A bet big enough to reorganize teams or change funding
   deserves full spec treatment — compose your spec-writing skills on its card if you run
   a larger library; otherwise the improvement template's sections are the lightweight spec. A policy tweak (right-to-left review order) needs no ceremony at all.
6. **Report.** Append findings to the current review brief (or write
   `reviews/YYYY-MM-DD-improve-probe.md`): probes run, fired/quiet, cards created, and
   which existing improvement bets this evidence strengthens or kills.

## Rules

- **Capture, never implement.** Changes to `pdlc.md`, `topology.md`, tiers, or WIP limits
  happen only when their improvement card passes plan-commit with a human decision — walk
  the talk; the operating model rides its own lifecycle.
- Every bet gets kill criteria at birth. An improvement we can't revert or falsify is a
  mandate, not a bet — say which it is and who mandated it.
- Probes cite data or stay silent. "The org should consider…" without a signal is
  consulting prose; delete it.
- Respect improvement WIP: if `improvements/` already holds more open bets than the org
  digests, strengthen/kill existing ones before minting new cards.
- Simulation results are discovery evidence for a bet — never a substitute for the human
  decision to adopt it.

## Quality Gates

- Every probe run is accounted for: fired-with-citation or checked-quiet.
- Every new card has hypothesis, indicators, success/kill criteria, and a named, timeboxed
  discovery approach.
- Topology cards include the option-comparison table with current state as an option.
- Zero direct edits to pdlc.md / topology.md / tiers in this invocation.

## References

- `skills/portfolio-pdlc/references/probe-library.md` — the probe families (source: the
  Portfolio Agility Trailmap minibook + enterprise portfolio practice).
- `portfolio-pdlc-simulate` — the discovery engine for flow/topology what-ifs.

---
name: sniff-test
description: Run a lightweight, evidence-based "sniff test" on a single initiative (epic, project, or Tier-1 bet) to find where its clarity is insufficient for its stage in the Portfolio PDLC lifecycle, so you can drive the right investment/commit and derisking conversations. Best run pointed at where the initiative is managed (its folder/workspace, Confluence space, or Jira epic) or given its Lean Product Canvas plus a recent sponsor update; with little input it asks for context first. Use when pressure-testing an initiative before a Plan/Commit decision or Execute/Build commitment, checking whether a Lean Product Canvas and Discovery plan match the real risks, or coaching on leading indicators and risk-appropriate derisking. For multi-initiative board patterns, use the sniff-test-portfolio add-on.
metadata:
  tags: flow-agile, product-strategy
  version: 1.0.0
---

# Sniff Test

## Outcome

For one initiative, surface where clarity is insufficient *for where it sits in the lifecycle* — fast, with low ceremony — so the right go/no-go and derisking conversations happen *before* money is committed. The deliverable is not a grade; it is the specific conversation, evidence, or derisking activity to run next.

This is the diagnostic backbone of the Portfolio PDLC operating system: it makes initiative confidence legible, supports an honest investment/commit decision, and builds the evidence record that guards against the **rubber-stamp anti-pattern** (a business decision arriving at software's door expecting a ceremonial handoff). The framework's core principle is **"common language, not gates"** — confidence grows through the lifecycle; the sniff test reads whether it has grown *enough for the stage*.

## Core Idea

For the initiative, ask two questions:

1. **Do we have enough clarity for this stage?** Read across the Lean Product Canvas framing (Problem, Users, Outcomes, Hypotheses) and the risk lens — **Desirability, Viability, Feasibility** (plus architecture / data / security assumptions where relevant).
2. **Is our derisking approach appropriate for the risk level?** Just Do It vs. Ship & Measure vs. Discovery/Testing (or Seek Alpha) — matched to actual uncertainty, not habit.

Clarity that is *expected to be low* early (in Explore / Discovery) is healthy — that is the whole point of pre-commitment derisking. The smell is a **mismatch**: an initiative deep in the lifecycle carrying question marks it should have resolved, a Discovery plan aimed at what's already understood, a "skip to Execute/Build" with open desirability, or clarity that is confident opinion with no evidence behind it (a **watermelon** — green outside, red inside).

## Stage Is a Required, Verified Input

The clarity read only means something *relative to the stage*, so the stage must be established first — and **not trusted on its label alone**.

1. **Get the stage.** Take it from the user, or extract the claimed stage from the materials (board status, spec status field, Kanban column).
2. **Verify it against evidence before rating.** A status label is frequently stale. Corroborate the claimed stage against what actually exists: downstream artifacts, shipped code/output, go-live state, git history, decision records. If the evidence says the work is further along (or further behind) than the label, **flag the stage mismatch first** — it can invalidate the entire clarity-vs-stage comparison and is often the single highest-signal finding.
3. **Map to the lifecycle stages.** Explore → Discovery *(optional)* → Plan/Commit → Execute/Build → Rollout/Last Mile *(optional)* → Business as Usual (see `references/lifecycle-clarity-rubric.md` for per-stage detail). If the initiative is Tier-2 (domain/team-centered) rather than Tier-1 (enterprise), note that it runs under the framework as lightweight guardrails rather than on the enterprise portfolio Kanban.

## When To Use

- Pressure-testing one initiative before a Plan/Commit decision or the Plan/Commit → Execute/Build "point of last return."
- Checking whether an initiative's Lean Product Canvas, assumption set, or Discovery plan points at its real risks.
- Reviewing a single Kanban item during Explore, Discovery, or a readiness conversation.
- Coaching an initiative owner or sponsor on leading indicators, growing confidence, or risk-appropriate derisking.

## How to Run Me — What to Feed Me

The cleanest way to run me: **point me at where this initiative is actually managed** and name the initiative. Tell me the stage you think it's in if you know it — I'll verify it against the evidence either way. In rough order of value, what helps most:

1. **The team's system of record (best).** Run me in the folder/workspace/repo where the initiative lives, or point me at its Confluence space, Jira epic + child tickets, or shared drive. I'll ingest what's there — canvas, roadmap, tickets, docs, decisions — and corroborate the stage against real evidence instead of a status label. Just tell me which tool holds the source of truth and how to reach it.
2. **A Lean Product Canvas (the core artifact).** The primary thing I read — ideally tagged with the current lifecycle stage. It carries the problem, users, outcomes, hypotheses, and assumptions I rate clarity against. (One of the framework's two foundation artifacts.)
3. **A recent sponsor update (useful).** What's being claimed about status, confidence, and risk to leadership — prime material for spotting watermelons and stale-status mismatches.
4. **The feature list / Outcome-Oriented Roadmap (useful).** The features and where each one stands, so I can check whether delivery progress actually matches the claimed stage and confidence. (the framework's other foundation artifact.)

Beyond the artifacts, I'll establish two things: the initiative's **tier** (Tier-1 enterprise vs. Tier-2 domain/team), and **what "you can count on being true" at this stage** (the stage's executive contract if one is defined; otherwise I use the default rubric and say so). The single most important and most-skipped input is **evidence behind any claimed clarity** — I treat confident-but-unevidenced conviction as a question mark, because that's what separates a real commit decision from a rubber stamp.

**If you give me little or no input:** I'll still run, but I'll **ask you for context first** — what the initiative is, where it's managed, and what stage you think it's in. Expect a longer, noisier flag list: with sparse information much of it reads as "unknown / unevidenced," which is itself a finding (the clarity isn't written down anywhere I can check). The more you point me at the real sources, the shorter and sharper the flags get.

## Core Workflow

0. **Ingest the inputs (or ask for them).** Gather what's available from the system of record / canvas / sponsor update / roadmap (see "How to Run Me"). If there's little or nothing to read, ask for context before sniffing — name the initiative, where it's managed, and the suspected stage — and warn that a thin-input run will produce many "unknown/unevidenced" flags.
1. **Establish and verify the stage** (see above). Flag any stage-vs-evidence mismatch before anything else.
2. **Rate clarity per dimension.** Mark each Lean Product Canvas / risk dimension: clear / partial / question mark — and tag each as evidence-backed or opinion. Use `references/clarity-dimensions.md`.
3. **Compare to the stage expectation.** Score clarity *against where the initiative sits*, not in the absolute. Flag mismatches using `references/lifecycle-clarity-rubric.md`.
4. **Check the derisking fit.** Is the discovery/assumption-burn-down plan aimed at the biggest uncertainties? Is the development approach proportionate to the risk? Use `references/derisking-and-indicators.md`.
5. **Name the smells.** Call out specific smells and watermelon risk plainly; don't soften them.
6. **Drive the conversation.** For each flag, state the next conversation or derisking activity — small and specific. Note what it means for the go/no-go.

## Rules

- **Steer, don't grade.** The deliverable is the right next conversation/experiment, not a scorecard. If a rating doesn't change a conversation or a go/no-go, don't belabor it.
- **Verify the stage before trusting it.** A stale status label is itself a smell and can invalidate the whole read.
- **Low clarity early is healthy; mismatch is the smell.** Don't flag an Explore / Discovery initiative for being uncertain. Do flag an Execute/Build or Rollout initiative carrying open question marks.
- **Demand evidence, not opinion.** Mark confident-but-unevidenced claims as question marks. Hunt watermelons. This is what makes the commit decision a real one rather than a rubber stamp.
- **Make the derisking plan align with the gaps.** A feasibility prototype when the open question is "do customers want this?" is a smell, not progress.
- **Prefer leading indicators.** Lagging totals confirm the past; they can't steer under uncertainty. Push toward sense-and-respond indicators that give timely feedback *and* plausibly correlate to the outcome.
- **Match the approach to the risk.** Just Do It for low uncertainty; Ship & Measure or Discovery/Testing (Seek Alpha) as uncertainty rises. Over-discovering the certain and under-discovering the risky are both smells.
- **Keep it lightweight, and watch the language.** A very light review has high value. The framework is "common language, **not gates**" — in sponsor/leadership framing avoid "phase gates" and "exit criteria"; speak in **confidence and what you can rely on**.
- **Stay single-initiative.** Cross-item patterns (shadowing, WIP clustering, portfolio risk balance) belong to the `sniff-test-portfolio` add-on.
- **Separate what you heard from what you inferred.** When you fill a rating from your own reading, say so and invite correction.

## Output Modes

- `single-initiative sniff` (default): verified stage, per-dimension clarity ratings with evidence/opinion tags, stage-mismatch flags, derisking-fit check, and the one next conversation or experiment with its go/no-go implication.
- `readiness check`: focused read for a specific decision point (Plan/Commit investment decision, Plan/Commit → Execute/Build commitment) — what we can rely on, what's still open, what evidence is missing.
- `coaching`: explain or pressure-test a specific concept (leading vs. lagging indicators, risk-appropriate derisking, watermelons, rubber-stamp risk) against the initiative.

## Quality Gates

- Available inputs (system of record / canvas / sponsor update / roadmap) are ingested; if input was thin, context was requested before sniffing and the resulting flag noise was called out as a coverage gap.
- The stage is established and **verified against evidence**; any stage-vs-label mismatch is flagged.
- Every flag is tied to a *stage mismatch*, not just a low score.
- Each claimed clarity is tagged evidence-backed or opinion.
- At least one smell or watermelon risk is named where the initiative warrants it.
- Each flag carries a specific, small next conversation or derisking activity — not "do more discovery."
- The derisking approach is assessed for fit to the actual risk level, with leading indicators preferred.
- The "what you can count on" standard is stated explicitly (including when a default was used).
- Sponsor-facing output uses confidence / "what you can rely on" language ("common language, not gates"), not gate/exit-criteria language.
- The output reads like a portfolio facilitator steering with evidence, not a compliance audit.

## References

- `references/clarity-dimensions.md` — Lean Product Canvas framing + the Desirability/Viability/Feasibility risk lens, with the diagnostic question per dimension.
- `references/lifecycle-clarity-rubric.md` — lifecycle stages and Kanban states, expected clarity / "what you can count on" / smells / watermelon risk by stage.
- `references/derisking-and-indicators.md` — the Risk/Derisking Matrix (Just Do It / Ship & Measure / Discovery-Testing / Seek Alpha), leading indicators and sense-and-respond, the input→impact ladder, and Goldilocks/OMTM.
- `references/facilitation-and-visual-management.md` — when to run a sniff, single-initiative session format, visual management (cards/dots), who to involve, and how to handle resistance.

## Related Skills

- `sniff-test-portfolio` — the multi-initiative add-on: shadowing/duplicate detection, WIP clustering, portfolio risk balance (Explore/Discovery vs. Build & Deliver split), and board-wide stale-status sweeps.
- `lean-product-canvas-coach` — to build or strengthen the canvas this skill reads.

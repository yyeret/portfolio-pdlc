---
title: A blocking finding gets fixed and re-reviewed instead of spending a human
type: improvement-process
stage: watching
owner: Yuval
opened: 2026-08-21
benefit_hypothesis: "If blocking findings are fixed and re-reviewed automatically up to twice, humans are spent only on judgement calls — because most first-round blocks are defects the author can fix in minutes, not decisions anyone needs to make"
measures: [rounds-to-clean, human-round-trips-per-change, notes-carried]
baseline: "Under the one-shot gate, PR #2's first BLOCK included a one-line typo fix that still cost a full human round-trip"
kill_criteria: "If the median change needs all three rounds, the bar is miscalibrated rather than the authors — revisit the bar's wording, do NOT raise the round cap. A loop that always runs to its limit is not converging."
probe: "PR #3 is the first run; read rounds-to-clean across the next five PRs"
---

# A blocking finding gets fixed and re-reviewed instead of spending a human

## The signal

The gate adopted in `agent-merge-authority` was one-shot: any BLOCK went to a human. PR #2's
block bundled a genuine judgement call (should a policy granting merge authority be its own
first customer?) with a typo — a quoted exit code of 0 where the real value is 4. The typo
did not need a human. Under a one-shot gate it got one anyway, because it travelled with
something that did.

## Benefit hypothesis

If the loop fixes blocking findings and re-reviews, up to twice, then
human-round-trips-per-change falls to only the §4 escalation cases, **because** the two
categories are separable: a defect has a correct fix the author can make, a judgement call
has no fix at all.

## Options considered

| Option | What changes | Effort | Risk | Reversible? |
|---|---|---|---|---|
| do nothing | — | — | humans spend attention on typos | — |
| unbounded fix-and-re-review | loop until clean | s | converges on plausibility, not truth — the failure this repo warns about in every inner graph | yes |
| bounded loop, 3 reviews / 2 fixes | `docs/quality-bar.md` §6 | s | a real problem could survive to the cap and get handed back late | yes |
| let the author decide what is worth a human | judgement | none | the author is the one party who cannot judge that | — |

## Probe

PR #3 itself. Watch specifically for the failure the bound exists to prevent: a reviewer
that reshapes its objection each round rather than converging. The convergence guard is
supposed to catch that — this probe tests whether it fires when it should, and stays quiet
when it should not.

## Probe result — PR #3, all three rounds

The loop ran its full bound on the change that introduces it and **ended in a hand-back**,
not a merge. Three rounds, three BLOCKs, four blocking findings:

| Round | Finding | Fix |
|---|---|---|
| 1 | §6 sent §4.1 — a failed check — straight to a human, defeating the loop it was introducing | `db5db77`, one paragraph + two lines |
| 1 | the pseudocode dispatched `PASS -> merge` before the escalation branch, inverting §4's stated precedence | `db5db77`, one line moved |
| 2 | that fix reached `docs/quality-bar.md` and not `AGENTS.md`, the file every session loads | `367d03f`, one sentence |
| 3 | the bar's opening paragraph still states the single-pass rule the change replaces | `06ceb3e`, applied on a human's call after the loop had ended |

Every one was real, and every one was a sentence or a line to fix. A one-shot gate would
have caught round 1's two and shipped the other two.

**The bound was not the binding constraint — the reviewer's question was.** Three of the
four findings are the same defect at different sites: this repo states its review
disposition in five places, and rounds 1 and 2 each fixed the site in front of them without
asking where else it was written. Round 2 counted the sites and reported four. Round 3 asked
the question properly, found the fifth, and tripped the convergence guard doing it.

The fourth — round 1's precedence inversion — is the counter-example, and it belongs in the
record: an ordering bug in the new pseudocode, caught on the first read, nothing to do with
where else anything was written. One finding in four was what a single pass would have been
enough for.

So the loop spent three rounds on one defect and still did not finish it. That is a finding
about what the reviewer is asked, not about the number of rounds — and it is the first
evidence for the kill criterion, which says a bar that always runs to its limit is
miscalibrated in its wording rather than short of rounds.

## Adoption

**Adopted on a human decision, not on a clean verdict.** The loop graded its own
introducing change and declined to merge it — three rounds, three BLOCKs. Yuval read the
open finding and called it: apply the fix, merge. That is the routing working rather than
failing; what the loop is for is putting a decision in front of a human with the evidence
attached, and the alternative — merging on the author's own say-so after the gate said no —
is the thing the gate exists to prevent.

Worth remembering when reading the measures below: the change is live, and it has never
once produced the clean verdict it defines.

## Watch

| Date | Measure | Value | Read |
|---|---|---|---|
| 2026-08-21 | rounds-to-clean | never clean (3 of 3) | ran to the bound; hand-back, not merge |
| 2026-08-21 | human-round-trips-per-change | 1 | vs. 1 under the one-shot gate — no saving on this change, because the loop never converged |
| 2026-08-21 | blocking findings that were real | 4 of 4 | none were reviewer noise; each named a file, a line, and a fix of a sentence or less |
| 2026-08-21 | notes-carried | 8 | recorded across three rounds, none fixed, none re-raised as blocking by a later round |
| 2026-08-21 | merged on | human decision | the loop's own verdict on the change was BLOCK; `06ceb3e` carries round 3's fix and is the merge |

## Decision log

| Date | Decision | Who | Basis |
|---|---|---|---|
| 2026-08-21 | Build it: review becomes a bounded loop | Yuval | "subagent review, fix should be a loop until clean review and then merge" |
| 2026-08-21 | Apply round 3's finding and merge #3 despite the BLOCK | Yuval | handed back with one open finding and a one-sentence fix; called it rather than spending a fourth round |

# PDLC readiness — validation record

**Date:** 2026-10-05. **Method:** author-run manual calibration against local source files, plus packaging and rendered-output checks. No independent agent evaluation or measured leader usability study was performed.

## Real-source calibration

### Framework: customized Spec Kit

Snapshot: `cb644d4ed8fb1555761c366f4d3646e90c743bb6`, clean local checkout. Content inspection was read-only. The user subsequently authorized preserving this snapshot on `spec-kit-yuval-pdlc` and refreshing the primary checkout to clean upstream; that repository reorganization was performed separately from the assessment. Core specify/plan/tasks/analyze/implement/validate path, spec/plan templates, and relevant local history inspected.

Result: **PDLC-aware, loop incomplete.** Intent, risk-dependent discovery planning, and delivery verification receive credit; leading-indicator contracts, human decision ownership, and review routing are partial; adoption responsibility is absent from the inspected core path. The separate validation command is substantial counterevidence against a blanket “SDLC only” label.

Full paired report: [executive HTML](2026-10-05-spec-kit-pdlc-readiness.html) and [canonical Markdown](2026-10-05-spec-kit-pdlc-readiness.md).

### Artifact: GitHub Spec Kit Demo Application

Source: Spec Kit `temp_spec.md` at the same snapshot, read in full. The artifact declares Draft, created 2025-11-23. Assessment is of this single-file draft, not of the current framework or a shipped product. No claim that the current customized workflow generated it.

Result: **SDLC-focused for the inspected artifact**, with useful user-capability and comprehension criteria. Its observable boundary is a functioning demo meeting acceptance scenarios. Its user stories explain why setup and reset matter, and SC-007 (a five-minute walkthrough), SC-009 (navigation comprehension), and SC-010 (audience understanding) go beyond raw output counts. SC-010's 90% target is already in the source; it is not an assessor recommendation.

| Dimension | Read | Rationale / source |
|---|---|---|
| Intent and outcome | Supported | User Stories 1–3 name presenter/audience value; Success Criteria include comprehension. |
| Assumptions and discovery | Partial | Assumptions mostly select implementation defaults; no evidence-based probe of presenter or audience uncertainty. |
| Leading indicators | Partial | SC-009/010 could inform learning; sampling, measurement method, baseline, owner, and decision use are unspecified. |
| Commitment and decisions | Gap within this file | Draft status and feature branch are present; no human investment/continue/stop contract appears. |
| Delivery and verification | Supported for a draft spec | Prioritized scenarios, independent tests, edge cases, and acceptance criteria define the intended result. This does not establish tests passed. |
| Adoption and operation | Partial | Launch/reset/offline requirements support presenter use; no pilot owner or ongoing support handoff is assigned. |
| Outcome review and adaptation | Gap within this file | “More can be added post-launch based on feedback” in Assumptions lacks a review trigger, owner, evidence threshold, and recorded decision. |

Lifecycle: Explore Supported; Discover Partial; Commit Gap; Deliver Supported as a draft contract; Adopt Partial; Review outcomes Gap; Adapt/operate Partial because feedback is mentioned without a loop. Confidence is medium for this file; surrounding product governance is unassessed.

Priority repair: use the existing comprehension criterion in a small presenter/audience trial before expanding custom scenarios. Proposed owner: demo product owner. Agree how understanding is observed, sample adequacy, and a review event that can alter scope. Impact: reduce the risk of polishing an engaging simulation that leaves the audience unable to explain the workflow. Do not add a revenue goal, infer that failed outcomes occurred, or demand production evidence from a draft. A linked existing pilot/review contract would change this read.

### Reference cross-check: Compound Engineering

Snapshot: `4927d7a12a805351745e69c532f8d30f2bae3d8e`, clean. Focused calibration, **not a complete framework verdict**. Inspected the `ce-brainstorm` section contract, `ce-plan` section contract and relevant workflow instructions, `ce-work` shipping workflow, and `ce-compound` purpose/behavior.

- The plan contract carries a Problem Frame, traceable requirements, implementation units, verification, and Definition of Done. These are substantial intent preservation and delivery strengths.
- The shipping workflow, Phase 3 step 6, requires operational monitoring signals, failure/rollback triggers, a validation window, and an owner. Phase 4 carries that plan into the PR. It would be wrong to report “no post-deploy responsibility.”
- These instructions do not, by themselves, establish a product-adoption or business-outcome review. The operational contract deserves credit; product steering remains unestablished in this inspected slice.
- Capturing solved engineering problems through `ce-compound` is useful engineering learning. It is not evidence that customer-value assumptions were tested.

## Adversarial desk checks

Walked the rubric through the cases in the skill's `references/tests.md`:

- An unavailable linked review remains Unknown and can make the verdict Insufficient evidence.
- An explicit parent-process handoff can satisfy PDLC coverage even when the coding step ends at a PR.
- Build latency can be a product outcome for a developer platform when tied to a representative baseline, pilot, review owner, and response.
- Early-stage uncertainty and justified low-risk exceptions do not automatically lower readiness.
- A fully connected hypothetical bundle meets the PDLC-ready rule; green delivery alone cannot offset missing product review.

These are reasoning checks, not a scored benchmark or proof of repeated model reliability.

## Packaging and presentation

- Repository plugin validator: 20 discoverable skills; four manifests agree.
- Skill-creator validator: valid frontmatter and skill structure.
- Markdown links within the new skill resolve; both sample views use the same source content.
- Native browser inspection covered desktop (1280 requested) and narrow (390 requested; effective layout 416) views. The initial narrow table wrapped labels poorly; changed it to stacked rows and rechecked. No horizontal overflow in the final narrow view. Evidence anchor navigation works.
- Cross-harness delivery: plain Markdown and a self-contained HTML asset; no runtime, external service, or harness-specific execution dependency. No Windows or alternate-harness execution was performed.

## Follow-up evidence

The remaining validation is whether a real adoption leader can identify the first intervention from the brief in two minutes, and whether another assessor applies the rubric consistently. Those are user/repeat-run outcomes, not claims this author review can establish.

Skill-library friction observed: the shared skill-creator workflow still prescribes flat entry files and an index builder specific to that repository, while its own constitution and this repo require folders with SKILL.md. Proposed source edit: in the shared skill creator's “Choose structure” workflow, replace the fixed flat-path instruction with “Use the target repo's validated install contract; use a folder with SKILL.md where native plugin discovery requires it. Run that repo's index/packaging checks.” This proposal was not applied to the shared library.

## Expanded comparison calibration

Five public frameworks and the custom fork were inspected using pinned sources (Kiro: dated official docs), with optional Spec Kit Assess and Compound Strategy/Product Pulse configurations separated. The comparison uses a fresh Compound upstream snapshot; the earlier local-checkout monitoring observation above remains tied to its older revision.

Calibration correction: BMAD's researched product brief and PRD earn upstream band 2 and Partial discovery, because those artifacts do not themselves require an evidence-backed go/no-go or learning/delivery decision. This prevents template richness from being mistaken for investment discipline. The chart band definitions were added to the reusable skill.

### Final artifact checks

- Eight configurations share the same seven-dimension profile and anchored ordinal chart method. The comparison explicitly distinguishes engineering measures from leading product signals.
- All 21 pinned repository citation paths resolve in the assessed snapshots. An encoded GitHub source URL returned HTTP 200; Kiro uses the inspected official documentation pages.
- The three-slide PowerPoint passed package, geometry, font-policy and reimport checks with no findings or warnings. Both quadrant diagrams use native editable shapes; the eight-row summary is a native table. Every finalized slide was rendered and visually inspected. No native PowerPoint or Google Slides execution was performed.
- The comparison HTML embeds both diagram previews and uses horizontally scrollable tables at narrow widths. Browser inspection verified image loading, normal-view diagram and summary rendering, direct section anchors and no document-width overflow at the tested narrow width. The CUA click helper did not reliably follow distant fragment links, so direct fragment navigation was used for visual inspection.
- Final Git check: primary Spec Kit is clean main at b1463da; preserved augmented worktree is cb644d4 on spec-kit-yuval-pdlc. Original Compound and Portfolio PDLC primary checkouts remain clean on main.

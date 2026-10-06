# PDLC readiness — Spec Kit · latest upstream

**SDLC-focused default; optional product discovery**

The default path carries a specification through implementation and convergence, then recommends review or a PR. It explicitly excludes post-launch business outcomes from convergence. A first-party assessment bundle adds pre-build discovery and human review when deliberately selected. [E4, E5, E7, E9]

Framework assessment · 2026-10-05 · upstream main b1463da8 · freshly fetched, clean checkout · high confidence in the documented default boundary; organizational practice unassessed. Ratings below cover core SDD, with optional capabilities identified separately.

## Lifecycle coverage

Explore: **Supported** | Discover: **Partial** | Commit: **Partial** | Deliver: **Supported** | Adopt: **Gap** | Review outcomes: **Gap** | Adapt & operate: **Gap**

Adaptation should return evidence to Explore or Discover. Supported means an explicit contract; Partial an incomplete connection; Gap missing in inspected scope; Unknown unavailable evidence; Not needed a justified exception.

## Keep what works

- Core specification requires user value, prioritized journeys, and measurable success criteria. It is not merely a coding task list. [E1, E2]

- Convergence verifies actual implementation against requirements and appends traceable corrective work. Completion claims alone are not enough. [E4]

- The optional first-party assess bundle includes problem framing, evidence against the idea, concept choices, and human approval of its verdict before a manual SDD handoff. [E7–E10]

## First move

Keep the delivery loop. Make a product owner responsible for carrying one success signal through adoption and a timed outcome review; decide explicitly when the existing assess bundle is warranted before commitment. [E4, E7, E9]

## What you can rely on

| Dimension | Evidence state | Read and rationale |
|---|---|---|
| Intent and outcome | Supported | Core specify requires user value and measurable outcomes; the optional assess path adds a stronger problem frame and cost-of-inaction baseline. [E1, E2, E8] |
| Assumptions and discovery | Partial | Core captures assumptions and technical research; it does not condition delivery on product uncertainty. Optional assess has substantive evidence and concept checks, but is an independent entry point. [E1, E3, E7, E10] |
| Leading indicators | Partial | Success metrics are requested, but core does not require an early decision-linked measurement contract. Optional define adds a baseline or unknown marker, not an owned recurring review. [E1, E8] |
| Commitment and decisions | Partial | Users review core steps, but those reviews do not establish an investment policy. Optional assess workflow explicitly adds human approval of a pre-build verdict; it does not govern the full continue/pivot/stop lifecycle. [E5, E9, E10] |
| Delivery and verification | Supported | Implement checks tasks and tests; converge inspects the code against intent and loops unresolved obligations back into tasks. [E4, E6] |
| Adoption and operation | Gap | No accountable adoption or ongoing-operation handoff appears in the inspected core completion path. Neither the optional pre-build assessment nor generic extension hooks establish one. [E4, E6, E7] |
| Outcome review and adaptation | Gap | Core convergence excludes post-launch outcomes and ends with review/PR readiness. Optional assess ends before SDD; neither inspected path assigns post-launch product-evidence review and adaptation. [E4, E7, E9] |

## Where the gaps affect decisions

### 1 · Software conformance is the final default feedback loop

Converge checks whether the implementation satisfies the agreed artifacts; its inventory excludes post-launch outcome metrics. [E4]

**Impact:** Leaders can know that the requested software was built without knowing whether the original investment should expand, change, or stop.

**Smallest repair:** Add a product review handoff after delivery: primary signal, cohort, evidence window, owner, and recorded next-investment decision. Keep convergence as the engineering completion check.

**Owner and evidence:** Product or initiative owner. Proof: one shipped slice produces a real outcome review and an explicit next action.

### 2 · Discovery is available but has to be selected

The first-party assess workflow is deliberately separate from default SDD. Its bundle adds human review, but no mandatory uncertainty-based routing selects it. [E5, E7, E9]

**Impact:** A high-uncertainty idea can enter delivery directly even though useful discovery support already exists.

**Smallest repair:** Define a lightweight entry policy: which uncertainties require the assess route, and what evidence justifies direct delivery. Use the existing bundle before inventing more assessment documents.

**Owner and evidence:** Product and engineering leadership. Proof: the next uncertain initiative takes the discovery route or records why existing evidence is sufficient.

### 3 · Success measures have no default route into user adoption

Core lists measurable outcomes and the optional define command asks for baselines; neither binds those measures to a rollout owner and follow-up event. [E1, E8, E4]

**Impact:** A success criterion can remain a sentence in the spec while release, support, and evidence collection happen independently.

**Smallest repair:** Turn one existing criterion into an adoption experiment: define intended users, measurement method, baseline plan, review timing, and a proportionate operational guardrail.

**Owner and evidence:** Product owner and rollout lead. Proof: observed use by the intended cohort reaches the person responsible for the outcome decision.

## Are the indicators useful?

Task completion time and first-attempt success in the core template can be useful leading capability signals. Concurrency is a quality/capacity measure; support-ticket reduction may be a later outcome. The template alone does not establish which is decision-relevant. [E1]

The optional define command is stronger on problem framing and asks for a metric baseline, allowing unknown. It still does not prescribe a measurement owner, observation window, or response to the result. [E8]

Illustrative repair: for a pilot onboarding change, measure successful first-task completion in the intended cohort before the expansion decision. Agree the baseline, threshold, and time window with the owner; watch support demand as a guardrail. This is a proposed contract, not an approved target.

## Evidence and limits

Snapshot: github/spec-kit main b1463da80bdba3cf6b019118ed499888758233d2, fetched 2026-10-05. Inspected core specify/plan/implement/converge instructions and templates, README default path, first-party assess extension and its define/decide contracts, workflow and bundle wiring, and catalog entries. Discovery and commitment are Partial in the default profile; the explicitly selected assess route provides stronger pre-build support. Community catalog descriptions were not treated as implemented behavior and their external repositories were not audited. No installation was configured or workflow executed. A configured external product process could close the documented core gaps.

- **E1** — `templates/spec-template.md` — User Scenarios & Testing; Success Criteria; Assumptions. Source: Spec Kit local snapshot above.

- **E2** — `templates/commands/specify.md` — Specification Quality Validation; Success Criteria Guidelines. Source: Spec Kit local snapshot above.

- **E3** — `templates/commands/plan.md` — Phase 0 research; Phase 1 quickstart validation guide. Source: Spec Kit local snapshot above.

- **E4** — `templates/commands/converge.md` — Goal; step 2 outcome exclusions; steps 4–8 evidence checks and PR handoff. Source: Spec Kit local snapshot above.

- **E5** — `README.md` — Independent entry points; Spec-Driven Development; Idea assessment. Source: Spec Kit local snapshot above.

- **E6** — `templates/commands/implement.md` — Completion validation; Mandatory Post-Execution Hooks; Done When. Source: Spec Kit local snapshot above.

- **E7** — `extensions/assess/README.md` — Handoff; Installation; Guardrails. Source: Spec Kit local snapshot above.

- **E8** — `extensions/assess/commands/speckit.assess.define.md` — Execution; Success Metrics template. Source: Spec Kit local snapshot above.

- **E9** — `workflows/assess/workflow.yml` — review-verdict human approval; manual specify handoff. Source: Spec Kit local snapshot above.

- **E10** — `extensions/assess/commands/speckit.assess.decide.md` — Evidence strength and concept requirements; go/clarify/kill; handoff. Source: Spec Kit local snapshot above.

## Next decision

Use this core for software delivery, and assign the product loop explicitly. For one upcoming initiative, decide whether to select the existing assess bundle; agree who owns adoption evidence and the post-launch continue/change/stop review. Reassess the resulting configured workflow, not just the source distribution.

Assessment of documented support, not certification or proof of achieved outcomes.

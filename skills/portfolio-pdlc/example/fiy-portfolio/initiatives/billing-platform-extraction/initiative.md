---
title: Product teams self-serve pricing and plan changes
type: platform
tier: 1
stage: explore
stage_entered: 2026-08-05
owner: Noa
sponsor: Jim
outcome_hypothesis: "If billing becomes a self-service platform, most pricing/plan work localizes to product teams and portfolio cycle time drops"
leading_indicators: []
risk_level: high
derisking_approach: discovery
orientation: mixed
portfolio_score: 8
dependencies: []
next_decision: "2026-09-10 — invest in extraction discovery? (Jim + eng lead)"
---

# Product teams self-serve pricing and plan changes

## Problem / Opportunity

Payments & Billing sits in the critical path of 3 of 7 Tier-1 cards and most team-level
work involving money. Every plan change is a ticket; the queue is the real roadmap.

## Riskiest assumptions

- 80% of billing requests fit a self-service golden path — **opinion** (needs request-log
  analysis).
- Extraction can proceed without freezing in-flight billing work — **opinion**.

## Derisking plan

Discovery: analyze six months of billing tickets for pattern coverage; simulate the
dependency-tax reduction (`portfolio-pdlc-simulate`, scenario `extract-billing-platform`);
tracer: one product team ships one plan change via a prototype API.

## Decision log

(pre-investment)

## Evidence log

- 2026-08-05 — dependency count from board: payments-billing named by 3 Tier-1 cards.

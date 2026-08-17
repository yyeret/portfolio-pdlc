# Topology — FlowImpact Yoga

## Teams & groups

| Team/Group | Owns | Size | Notes |
|---|---|---|---|
| Studio Web | scheduling, studio portal | 4 teams | core product, oldest code |
| Mobile | member & instructor apps | 2 teams | mid-rewrite (see `mobile-app-rewrite`) |
| Payments & Billing | billing engine, payouts, invoicing | 1 team | **in everything's critical path** |
| Data & Analytics | warehouse, studio insights | 1 team | shared service, ticket queue |
| Platform Services | auth, notifications, integrations | 1 team | absorbing SSO work |

## Shared capabilities & platforms

Billing is a ticket queue, not self-service — every pricing, payout, or plan change lands
on the Payments & Billing team. Auth/SSO heading the same way via Platform Services.

## Known dependency hotspots

`payments-billing` appears in the dependency list of 3 of 7 Tier-1 cards (latest board
count). Data & Analytics second at 3, but its requests are smaller and queue faster.

## Candidate topology options

1. **Current state** — keep Payments & Billing as owning team; coordination via tickets.
2. **Billing self-service platform** — extract APIs + golden paths so product teams
   self-serve plan/pricing changes (see `initiatives/billing-platform-extraction`).
3. **Embed billing engineers** in the two heaviest product teams for two quarters
   (T-shaping play).

Compare on: % work localized / change size / risk / future-proofness — when option 2 or 3
graduates, it gets an improvement or platform card, not a hallway decision.

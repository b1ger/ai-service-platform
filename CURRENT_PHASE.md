# CURRENT_PHASE

## Phase
Phase 0 — Discovery & demo-driven scoping.

## Phase objective
Build a focused demo (call it Spike-0) that proves the core architectural insight (composite-first / brand-asset preservation), then use that demo on a 25–30 minute voice call with the first design partner to lock MVP scope.

## Scope right now (in)
- Continue Telegram discovery with Kateryna (Shower Pack)
- **Build demo spike** — one narrow vertical slice (see `DEMO_SCOPE.md`), throwaway code allowed
- Schedule and conduct voice call with demo in hand
- Translate observed failure modes into MVP feature spec, informed by what worked/failed in the demo
- Choose production technical stack (separate from demo stack, can differ)
- Draft 1-page Design Partner Agreement
- Document everything in this repo

## Scope right now (out)
- Production-quality code (auth, billing, multi-tenant infra)
- Full MVP (only the narrow demo spike)
- Frontend / UI polish beyond Gradio defaults
- Outreach to additional brands
- Pricing, billing, marketing
- Anything from the archived service-business framing

## Note on the demo spike
Demo code is explicitly throwaway. It exists to prove the architecture and impress the design partner on the call. Production MVP code will be a fresh start with proper structure (`server/`, `app/`). Do not over-invest in demo polish.

## Required outputs in this phase
- Filled `DESIGN_PARTNER_LOG.md` with all discovery to date
- `MVP_SCOPE_V0.md` (will be created after voice call) — 5–7 pages, buildable spec
- `TECH_STACK.md` (will be created after voice call) — concrete model and infra choices
- Signed (or at least verbally agreed) Design Partner Agreement
- Updated `NEXT_STEPS.md` reflecting the path to first prototype

## Success criteria for exiting Phase 0
All of the following must be true:
- Design partner has confirmed enthusiasm for the proposed product (not lukewarm)
- MVP scope is concrete enough that a developer with Claude Code could begin implementation
- Technical stack is chosen for at least the first prototype iteration
- Time budget for first prototype is set (target: 4–6 weeks at 10–15 hrs/week)
- Partner has provided real assets to test against (product photos, packaging, examples)

## Gate to next phase
Move to Phase 1 (Build first prototype) only when all Phase 0 success criteria are met. Do not start coding before this.

## Current execution rule
Bias toward decision-quality over decision-speed. We have 6 months of runway and 10–15 hours/week. The cost of building the wrong thing is far higher than the cost of one extra week of clarification.

## Honest acknowledgement
Operator is currently "willing to try" rather than "fully convicted" on this product direction. That is acceptable for Phase 0 — conviction should grow (or fail to grow) as discovery and prototyping reveal whether this can become a real product. Do not pretend conviction we don't have. Decision gates exist for a reason.

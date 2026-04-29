# START HERE

## Purpose
Entry point for the operator (you) and for Claude Code working in this repo.

## What this repo is now
A working repository for building **Composer** — a vertical AI image tool for Ukrainian DTC manufacturers that generates SEO-optimized product photography for e-commerce galleries while preserving brand assets exactly.

Earlier iteration framed this as a service business (consulting / automation). That direction was discarded on 2026-04-29 — git history retains the old files if anything needs to be referenced.

## What phase we are in
**Phase 0 — Discovery & MVP scoping.**
See `CURRENT_PHASE.md` for explicit scope.

## Read these files first, in order
1. `CURRENT_PHASE.md` — what we're doing right now
2. `PRODUCT_HYPOTHESIS.md` — what we believe and why
3. `FAILURE_MODES_OBSERVED.md` — the technical brief, derived from real user data
4. `DESIGN_PARTNER_LOG.md` — current state of discovery
5. `NEXT_STEPS.md` — concrete near-term actions
6. `CLAUDE.md` — operating rules for Claude Code

## What to work on now
The single highest-priority outcome right now is:
**Lock MVP scope after voice call with the design partner (Kateryna at Shower Pack).**

Subordinate tasks supporting that outcome are listed in `NEXT_STEPS.md`.

## What NOT to work on now
- Full UI design / production frontend
- Backend infrastructure beyond a local prototype
- Pricing pages, marketing site, billing
- Outreach to additional brands beyond the design partner
- Anything from the archived service-business framing

## Operating principles
- One design partner at a time until first MVP is shipped
- Real data over assumptions: every product decision must trace back to a verbatim quote or observed failure
- Constrained scope: prefer a narrow tool that nails one workflow over a broad tool that does everything mediocrely
- Composite-first, generate-second: brand assets are sacred and never regenerated
- Validate via the partner's actual usage, not by feature count

## Decision gates
- Gate 1: Lock MVP scope (after voice call). Gate criterion: 5–7 page document any developer could pick up and build.
- Gate 2: Ship first usable prototype to design partner (target: 4–6 weeks of focused work after Gate 1).
- Gate 3: Partner uses prototype on at least 5 real product cards. Gate criterion: documented time savings vs. their ChatGPT workflow.
- Gate 4: Decide whether to scale to additional brands or kill / pivot. Gate criterion: partner is willing to pay AND introduces ≥2 similar brands.

## When in doubt
Re-read `PRODUCT_HYPOTHESIS.md` and `FAILURE_MODES_OBSERVED.md`. If the work in front of you doesn't move us toward Gate 1 or 2, it's not the right work.

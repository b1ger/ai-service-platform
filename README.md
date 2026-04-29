# Composer (working name)

Vertical AI image tool for Ukrainian DTC manufacturers — generates SEO-optimized product photography for e-commerce galleries (Horoshop, Prom, Rozetka) without losing brand assets.

## Why this exists
Small Ukrainian e-commerce brands manually rewrite product cards using ChatGPT — and consistently fail when it comes to product photography. Existing AI tools either regenerate brand assets (destroying packaging, logos, product details) or require Photoshop-level skill. Composer sits in the middle: simpler than Photoshop, more reliable than ChatGPT, narrower than Midjourney.

## Current phase
**Phase 0 — Discovery & MVP scoping with first design partner.**
See `CURRENT_PHASE.md` for what's in scope right now.

## Design partner
Shower Pack (`showerpack.com.ua`) — Ukrainian manufacturer of dry hygiene kits. Owner Kateryna spends ~15–20 hours/week rewriting product cards on Horoshop with ChatGPT. Image editing is the documented top pain.

## Repo structure (current)
- `README.md` — this file
- `START_HERE.md` — entry point for any operator working in this repo
- `CURRENT_PHASE.md` — what we are doing right now
- `PRODUCT_HYPOTHESIS.md` — what we are building and for whom
- `FAILURE_MODES_OBSERVED.md` — concrete failure patterns from real user data
- `DESIGN_PARTNER_LOG.md` — discovery notes and verbatim quotes
- `DEMO_SCOPE.md` — what the Spike-0 demo proves
- `NEXT_STEPS.md` — short ordered list of what to do next
- `CLAUDE.md` — operating instructions for Claude Code in this repo
- `code/spike-0/` — throwaway demo prototype for the design partner call

The previous iteration of this repo framed the project as a service / consulting business. That direction was abandoned on 2026-04-29 in favour of a product-first approach. The earlier files were deleted (not archived) — git history retains them if needed.

## Status snapshot
- Hypothesis: validated by first round of discovery
- Design partner: engaged via Telegram, voice call pending
- MVP scope: drafted (see `PRODUCT_HYPOTHESIS.md`)
- Code: not yet started
- Decision gate: full MVP scope locked after voice call with design partner

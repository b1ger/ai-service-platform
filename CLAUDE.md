# CLAUDE.md — operating instructions for Claude Code in this repo

## Context
This repo holds the working materials for **Composer**, a vertical AI image tool for Ukrainian DTC manufacturers. The operator is a Java developer building this part-time (10–15 hrs/week) using Claude Code. Currently in Phase 0 (Discovery & MVP scoping). No code yet.

## Read these first when entering this repo
1. `START_HERE.md`
2. `CURRENT_PHASE.md`
3. `PRODUCT_HYPOTHESIS.md`
4. `FAILURE_MODES_OBSERVED.md`
5. `DESIGN_PARTNER_LOG.md`
6. `NEXT_STEPS.md`

## What this repo is for, right now
Discovery documentation, product specs, and (eventually) a thin code prototype. It is not yet a software project. Until Gate 1 in `NEXT_STEPS.md` is reached, do not create code, scaffolding, or build configuration.

## How to behave
- Default to writing markdown documents that capture decisions and observations, not code.
- When generating any artifact (script, KP, message, prompt), trace it back to a quote or observation in `DESIGN_PARTNER_LOG.md` or `FAILURE_MODES_OBSERVED.md`. Do not invent customer needs.
- Do not propose features that are not in `PRODUCT_HYPOTHESIS.md`. If a new feature seems necessary, propose it as an amendment with reasoning, do not silently expand scope.
- Keep changes tightly scoped. One concern per file. One idea per commit.
- Push back if asked to do work that contradicts `CURRENT_PHASE.md` § "Scope right now (out)". State the conflict, suggest alternatives.

## Tone in generated content
- Direct, plain Ukrainian or English depending on file purpose
- No corporate fluff, no buzzwords, no "synergize" / "leverage" / "unlock potential"
- Short sentences over long ones
- Concrete examples over abstractions

## File conventions
- All planning docs in repo root, in UPPER_CASE.md if they are top-level state files
- Drafts and work-in-progress in `_drafts/`
- Throwaway demo / spike code in `code/spike-N/`
- Production code (when scope is locked) goes in `app/` (frontend) and `server/` (backend)
- An earlier service-business iteration was discarded — its files are retrievable from git history but do not resurrect them without explicit operator instruction

## Decision protocol
When facing an ambiguous decision:
1. Re-read `PRODUCT_HYPOTHESIS.md` § "What we believe" and § "What we explicitly do not believe"
2. Check `CURRENT_PHASE.md` for current scope
3. Check `DESIGN_PARTNER_LOG.md` for relevant partner data
4. If still ambiguous, surface the question to the operator rather than choosing arbitrarily

## What success looks like in this phase
The exit criterion for Phase 0 is in `CURRENT_PHASE.md`. Until those criteria are all met, the answer to "should we start coding now?" is no.

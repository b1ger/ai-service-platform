# Failure Modes Observed (from real user data)

## Source
Direct evidence: four ChatGPT image-editing conversations from Kateryna (Shower Pack), shared via Telegram on 2026-04-29. These conversations span product-card image generation tasks: bundle photos (10 items + gift), product introduction, use-case shots in field/trench/vehicle, and component substitution (changing a towel material in an existing photo).

This document encodes the technical brief for Composer based on these observed failures. Every product feature should trace back to one or more failure modes here.

## Failure mode 1 — Brand asset regeneration

**What happens.** When asked to edit an image containing the user's actual product (mitt, packaging, etc.), ChatGPT regenerates a new "imagined" version of the product instead of preserving the real one. The regenerated version has different texture, color, proportions.

**User quote.** *"А навіщо ти створила новий продукт?"* (when given two real product photos to combine, ChatGPT generated a fictional bundle). *"Тобі НЕ треба генерити рукавицю взагалі — у тебе вже є ідеальний асет."*

**Why this happens.** Diffusion models do not have a notion of "this asset is locked, do not regenerate". Every generation re-encodes the entire image and decodes a new variant. Without explicit reference-image conditioning + masking, brand assets drift on every iteration.

**What Composer must do.** Treat brand assets as first-class locked layers. Composite real product photos onto generated scenes, never re-render the products themselves.

---

## Failure mode 2 — Spatial reasoning failures

**What happens.** User describes an item by spatial position ("the towel between the water sachet on top and the foam mitt on the bottom"). The model identifies the wrong object, edits the wrong layer, or claims to understand and then edits incorrectly.

**User quote.** Three rounds of clarification: *"де рушник на сёму фото?"* → wrong identification → *"Ні, рушник біленький між водою та пінною рукавицею"* → wrong again → *"Ні, ти знов помилилась. Ще раз, де рушник на моєму фото?"*

**Why this happens.** Text descriptions of spatial relationships are ambiguous to vision-language models, especially when objects look similar. The model cannot reliably resolve "between A and B" without grounded mask input.

**What Composer must do.** Visual region selection (point-and-click or mask drawing) for any "edit only X" operation. Never rely on text alone to specify which object to modify.

---

## Failure mode 3 — Counting failures

**What happens.** User requests "10 items + 1 gift" in a bundle composition. Model produces 4 items, then 5 after correction, then 6 after another correction. Often never lands on the exact count.

**User quote.** *"Все чудово, тільки шість пар шкарпеток має бути, а ти зробила чотири"* → next attempt → *"ти зробила 5 тепер, а треба 6"*.

**Why this happens.** Diffusion models lack explicit count grounding. Bundle compositions with specific numbers are well-known weak point of free-form image generation.

**What Composer must do.** For any "X items in a row / grid / bundle" composition, use programmatic placement of pre-rendered or composited single-item assets. Never rely on the diffusion model to count.

---

## Failure mode 4 — Composition intent ignored

**What happens.** User specifies a precise interaction ("hold the mitt between both hands, in front of face"). Model defaults to the statistically common pattern from training data ("wear the mitt on the hand like a glove"). Repeated correction does not converge.

**User quote.** Five rounds of: *"не вдягай йому рукавицю на руку. Треба покласти піну в руки, всередину. Ззовні руки не має бути нічого."*

**Why this happens.** When user intent contradicts training-data priors, the model regresses to priors.

**What Composer must do.** For complex character + product interactions, provide reference pose images / scene templates rather than requiring the user to describe interactions in text. Curated template library beats free-form prompting.

---

## Failure mode 5 — Typography / packaging text corruption

**What happens.** Any edit to an image containing packaging causes the text on the packaging to become distorted, blurry, or misspelled.

**User quote.** *"ти зіпсувала щойно упаковку, подивись уважно, там букви вже попили"*.

**Why this happens.** Diffusion models render text glyph-by-glyph during generation; any re-encoding of the image risks degrading text. This is a well-known failure mode.

**What Composer must do.** Never let the diffusion model touch packaging containing text. Keep packaging as a separate locked layer (PNG with alpha) composited on top of the generated scene. Text is preserved pixel-perfect because it was never regenerated.

---

## Failure mode 6 — High iteration friction

**What happens.** Even when the model gets close to the desired result, every correction produces a new full re-generation that drifts on aspects the user previously approved. The user is constantly chasing regressions.

**User quote.** Implicit throughout — every conversation has 5–15+ rounds of corrections, with the user explaining the same constraint multiple times.

**Why this happens.** No persistent canvas state. Every prompt is effectively starting from scratch with light reference conditioning at best.

**What Composer must do.** Persistent project state. Once a layer is approved, it is locked. Subsequent edits operate only on unlocked layers. User can iterate without losing prior progress.

---

## Failure mode 7 — No structured output for downstream platforms

**What happens.** Even when an image turns out well, the user still has to manually crop / resize / format for Horoshop's specific requirements, then upload one by one. The image work is not the end of the workflow; the platform integration is.

**User quote.** Implicit — Kateryna's workflow includes "вношу на сайт" as a separate step ("ОК but adds time").

**Why this happens.** ChatGPT is a generic chat tool. It has no concept of target platform.

**What Composer must do.** Output stage produces a Horoshop-ready (and later Prom-, Rozetka-ready) gallery pack: correct dimensions, ordered for best gallery performance, optionally pushed via API.

---

## Implications for technical stack

Based on these failure modes, the Composer architecture must include:

- **Layered project model**: each image is a stack of locked + unlocked layers, not a flat pixel array
- **Reference-image conditioning**: brand assets enter as image inputs, not as prompt text
- **Mask-based regional editing**: SAM2 / equivalent for selecting edit regions, with strict pixel preservation outside the mask
- **Composite-first pipeline**: scene generation and asset placement are separate steps with separate models if needed
- **Programmatic placement for counts**: bundle / grid compositions use code-based layout, not diffusion
- **Typography as locked PNG overlay**: packaging never enters the diffusion pass
- **Project state persistence**: approved layers stay approved across iterations
- **Platform-aware output**: format-pack generation per target marketplace

Specific model candidates (to be evaluated in tech-stack doc after voice call):
- Flux.1 Kontext for reference-conditioned generation and inpainting
- SAM2 for mask generation
- rembg or BiRefNet for clean background removal
- nano-banana / Gemini 2.5 Image for fast scene drafts
- ComfyUI as orchestration layer (or custom Python if simpler)

## What is explicitly NOT a problem to solve
- The quality of free-form image generation itself. Modern models are good enough; the issue is that they are the wrong tool for asset-preserving edits.
- The quality of text descriptions. We are not building a "better prompt assistant" — we are building a different paradigm where text is replaced by visual selection.

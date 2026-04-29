# Next Steps

Short, ordered, actionable. If a task is not on this list, it is not the priority right now.

## Strategy update (2026-04-29)
Pivoted from "build mockups for the call" to "build a working demo (Spike-0) for the call". Demo code is throwaway — see `DEMO_SCOPE.md` for what's in scope and what's not.

## Today / next 24 hours

### Set up the demo environment (operator, ~30 min)
1. Get a Replicate API token at https://replicate.com/account/api-tokens
2. `cd code/spike-0 && python -m venv .venv && source .venv/bin/activate`
3. `pip install -r requirements.txt`
4. `cp .env.example .env` and paste the token into `.env`
5. Download 2–3 public product photos from `showerpack.com.ua` into `code/spike-0/assets/inputs/`:
   - `foam_mitt.jpg` — clean shot of the foam mitt
   - `packaging_combat.jpg` — green Combat packaging
   - `packaging_water.jpg` — turquoise "with water" version
6. Run `python app.py` — Gradio should open at http://localhost:7860

### First test run (operator, ~10 min)
7. Upload `foam_mitt.jpg`, choose "Окоп / польові умови", click Generate
8. Watch the three intermediate images: product without background → generated scene → final composite
9. Repeat with the packaging photo and a different scene

If the result is convincing → Spike-0 is operational, move to polish.
If the result is weak → see the iteration plan below.

## Iteration plan if first results are weak
The most likely failure modes and quick fixes:

- **Background removal poor** (jagged edges, halo): swap rembg for BiRefNet via Replicate. Update `background_removal.py`.
- **Scene has products / people in it** despite negative prompts: tighten scene prompts in `scenes.py`, or switch model to `imagen-4-fast` or `recraft-v3`.
- **Product looks pasted-on** (lighting wrong): add a Flux Kontext post-pass in `pipeline.py` — feed final composite as reference, prompt "harmonize lighting and color, do not change product details". Optional.
- **Shadow looks fake**: reduce shadow opacity in `compositor.py` from 110 to 60–80, increase blur radius.

## Before the voice call (after demo works)

### Prepare the demo run (~1 hour)
10. Pick 3 strongest examples that work reliably with the same scene preset. Save them in `assets/outputs/demo/` so you can show them quickly without waiting.
11. Take 2–3 of Kateryna's ChatGPT failure screenshots (the ones she shared) and save them next to your demo outputs for side-by-side comparison.
12. Practice the demo flow once. From "let me show you" to "and here's the result" — should be under 5 minutes.

### Prepare the rest of the call (~2 hours)
13. **PITCH_SCRIPT.md** (new file) — 7-minute script. Cover: (a) why ChatGPT keeps failing for her, in plain language, (b) the architectural insight (composite vs regenerate), (c) the demo, (d) the offer (free 6-month design partnership), (e) the ask.
14. **DESIGN_PARTNER_AGREEMENT.md** (new file) — 1 page, plain language. Use principles from `DESIGN_PARTNER_LOG.md`.
15. Compile 8–10 concrete technical questions for the call (what's her real asset library size, can we get Horoshop API access, etc.).

### Send Telegram inviting to the call
16. Once demo runs reliably + script ready, send Kateryna a short message:
    > Катю, я підготував маленьке демо того, що я хочу зробити для вирішення твоєї проблеми з фото. Хочу за 25–30 хв голосом показати екраном що це + обговорити один формат партнерства, який, думаю, буде вигідний нам обом. Коли тобі зручно: завтра ввечері, післязавтра?

## During the voice call (25–30 min)
- Open: thank her, recap her ChatGPT struggles in 1 sentence (2 min)
- Diagnose: why those tools fail her — 1 specific technical reason in plain words (3 min)
- Demo: live screen-share showing one of her photo types in 2 different scenes (5 min)
- Listen: her reactions, questions, objections (10 min)
- Offer: design partnership (3 min)
- Close: agree on next concrete step + timeline (2 min)

## After the voice call (within 24 hours)
17. Send written summary to Kateryna.
18. Update `DESIGN_PARTNER_LOG.md` with verbatim quotes and decisions.
19. Lock production MVP scope in `MVP_SCOPE_V1.md` (new file). Different from Spike-0 — this is for real.
20. Lock production technical stack in `TECH_STACK.md`.

## After scope is locked
21. Create `app/` (frontend) and `server/` (backend) directories
22. Begin implementation of production MVP (separate from `code/spike-0/`)

## Decision gates
Do not proceed past each gate without meeting its criterion.
- **Gate 0 (current)**: Spike-0 produces a convincing composite for at least 1 product × 2 scenes
- **Gate 1**: voice call complete, design partner enthusiastic, MVP scope locked → start production build
- **Gate 2**: production MVP ships, partner uses it on ≥5 real products → measure time savings vs ChatGPT
- **Gate 3**: partner is willing to pay AND introduces ≥2 similar brands → expand
- **Failure path**: at any gate, pause and reassess if the criterion fails. Stopping costs less than building unwanted product.

## What's NOT on this list (deliberately)
- Outreach to additional brands
- Production MVP code (Spike-0 is throwaway, separate code)
- Marketing site, landing page, social media
- Pricing page, billing integration
- Anything from the archived service-business framing

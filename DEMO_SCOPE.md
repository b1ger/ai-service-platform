# Demo Scope (Spike-0)

## Purpose
A single, focused demonstration to bring to the voice call with Kateryna (Shower Pack). The demo must prove the core Composer insight (composite-first architecture preserves brand assets) in a way that is visually obvious to a non-technical viewer.

This is **throwaway code**, not the foundation of the product. Production MVP will be a fresh start.

## What the demo does
A web page (Gradio app) where the operator can:

1. Upload a real product photo (Kateryna's foam mitt, packaging, or similar)
2. Pick a target scene from a small dropdown (e.g., "military trench / soldier washing face", "vehicle interior", "field daylight")
3. Click "Generate"
4. See three outputs side-by-side:
   - **Input** — the uploaded real product
   - **ChatGPT-style result** — what naive free-form AI generation produces (we can show a real screenshot Kateryna already shared, or run the same prompt through a basic Flux generation to demonstrate the failure)
   - **Composer result** — the same product composited into the generated scene with brand assets preserved exactly

## Why this specific demo
This demo lands the architectural insight in a single screen. Failure modes 1 (asset regeneration), 5 (typography corruption), and parts of 6 (iteration friction) become visible in one comparison. This is the most powerful single thing we can demonstrate in 5 minutes during a voice call.

## What's in the pipeline (technical)

Step 1: **Background removal**
Input: user-uploaded product photo
Tool: `rembg` (open source) or `BiRefNet` for higher quality
Output: transparent PNG of the product

Step 2: **Scene generation**
Input: scene description (from dropdown, prompt-engineered presets)
Tool: Flux Schnell via Replicate API (fast, cheap) or Imagen for cleaner results
Output: 1024×1024 background image, no products in it

Step 3: **Composition**
Input: transparent product PNG + generated scene
Tool: PIL for placement + simple shadow synthesis OR Flux Fill / Kontext for AI-assisted compositing
Output: final image with product placed in scene

Step 4: **Comparison view**
Display all three (input / "ChatGPT" / Composer) on the Gradio UI

## Stack for the demo
- **Language**: Python 3.11+
- **UI**: Gradio (single-file web app)
- **Image AI**: Replicate API (Flux Schnell, Flux Kontext, BiRefNet)
- **Image manipulation**: Pillow, NumPy
- **Local infra**: just runs on operator's machine, no deployment needed
- **API key**: one Replicate API token in `.env`

Estimated cost per demo run: $0.01–0.03

## Time budget
- Total: 8–14 hours of focused work
- Day 1 (4–6 hrs): pipeline working end-to-end with one scene preset, ugly UI but functional
- Day 2 (2–4 hrs): 2–3 scene presets, side-by-side comparison view, basic styling
- Day 3 (2–4 hrs): polish for demo, prepare 2–3 example product photos to demo with, dry run

## Test assets
Public Shower Pack product photos available on `showerpack.com.ua` can be used as input. Operator should download 2–3 representative shots:
- the foam mitt close-up
- the green "Combat" packaging
- the bundle "10 + sushkar gift" (to attempt the counting demo separately)

If specific assets are needed that aren't on the public site, request them from Kateryna with a one-line message ("щоб не вгадувати — кинь будь-ласка 3–5 ваших чистих фото продукту"). She has already implicitly offered.

## What is explicitly OUT of demo scope
- Login, accounts, multi-tenant
- Persistence (no DB, results regenerated each session)
- Asset library with tagging
- Region editor / mask drawing
- Batch generation
- Horoshop API integration
- Counting engine for bundles (one demo at a time — defer this if first comparison demo works)
- Multiple template categories (start with one)
- Cost tracking
- Error handling beyond basic try/except
- Logging beyond `print()`

## Success criterion
The demo is "done" when the operator can:
1. Show the Gradio UI to Kateryna over screen share
2. Upload one of her real photos
3. Generate the composite within ~30 seconds
4. Visually demonstrate that the product is preserved while the scene is generated

If Kateryna says "о, це саме те, що мені треба" — demo did its job. If she says "цікаво, але..." — we listen carefully and adjust scope.

## Failure path
If after 8 hours of focused work the pipeline is not producing convincing composites, pause and reassess. Possibilities: bad model choice, need better masking, need different compositing approach. Do not push past 14 hours of demo work — instead, prepare static mockups (Figma / hand-drawn) for the call as a fallback.

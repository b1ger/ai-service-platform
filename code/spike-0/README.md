# Composer — Spike-0 demo

Throwaway prototype to demonstrate the composite-first architecture during the voice call with Kateryna (Shower Pack).

**This is not production code.** See `../../DEMO_SCOPE.md` for what this is and isn't.

## What it does
Takes a real product photo + scene description → produces a composite where the product is preserved exactly while the scene is AI-generated.

Pipeline:
1. Background removal from input product photo (`rembg`)
2. Scene generation matching the chosen template (`Flux Schnell` via Replicate)
3. Composition: transparent product PNG over generated scene with simple shadow synthesis
4. Optional: light-matching pass via `Flux Kontext` (reference-conditioned)

## Setup

Requires Python 3.11+.

```bash
cd code/spike-0
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Get a Replicate API token (https://replicate.com/account/api-tokens) and create a `.env` file in `code/spike-0/`:

```
REPLICATE_API_TOKEN=r8_xxxxx
```

## Run

```bash
python app.py
```

Opens a Gradio UI on http://localhost:7860.

## Repo layout

```
code/spike-0/
├── README.md                     # this file
├── requirements.txt
├── .env.example
├── app.py                        # Gradio entry point
├── composer/
│   ├── __init__.py
│   ├── background_removal.py     # rembg wrapper
│   ├── scene_generator.py        # Flux Schnell wrapper
│   ├── compositor.py             # PIL-based placement + shadow
│   ├── pipeline.py               # orchestrates the full flow
│   └── scenes.py                 # preset scene prompts
└── assets/
    ├── inputs/                   # test product photos go here
    └── outputs/                  # generated results saved here
```

## Test inputs to download

Save 2–3 product photos from showerpack.com.ua into `assets/inputs/`:
- `foam_mitt.jpg` — close-up of the foam mitt
- `packaging_combat.jpg` — green Combat packaging shot
- `packaging_water.jpg` — turquoise "with water" version

These are public product photos and fine to use for prototype testing.

## Cost

Each generation costs roughly $0.01–0.03 in Replicate API charges. Budget $5–10 for the entire demo development.

## Known limitations of the spike

- One scene template at a time (no batch)
- No mask-based region editing
- No counting engine for bundles
- No persistence between sessions
- No auth, no users
- Crude shadow synthesis (good enough for demo, not for production)
- Hard-coded scene presets, no custom prompting in UI

These are intentional. Production MVP will address them.

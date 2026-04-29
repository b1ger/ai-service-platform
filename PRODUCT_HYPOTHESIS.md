# Product Hypothesis

## One-line summary
Composer is a vertical AI image tool that generates SEO-optimized product photography for Ukrainian DTC e-commerce brands while preserving brand assets (packaging, logos, product details) exactly.

## Problem we are solving
Small Ukrainian e-commerce brand owners (Horoshop / Prom / Rozetka sellers) spend many hours per week manually preparing product cards using ChatGPT. The most painful task is image work:
- Editing existing product photos (changing backgrounds, lighting, components)
- Generating use-case scenarios (product in context: field, car, backpack, etc.)
- Generating bundle compositions (e.g., "10 items + bonus")

ChatGPT and similar generative tools fail systematically at this work because they regenerate brand assets each iteration, distort packaging text, miscount items, and ignore explicit "don't change X" instructions. The owner ends up doing 5–10 iterations per image and often has to revert to manual editing.

## Who this is for (ICP)

### Primary: small Ukrainian DTC manufacturers
- Sells own products direct to consumer through their own e-commerce site (Horoshop / Prom / Rozetka) plus social channels
- Owner or small team handles SEO and content themselves (no dedicated marketer)
- Has existing real product photography (studio shots, packaging, components) but needs to produce many more variants for SEO and marketplace listings
- Already pays for ChatGPT or similar tools and is comfortable with AI-assisted workflows
- Estimated 500–2000 such brands in Ukraine

### Concrete first design partner
**Shower Pack** (`showerpack.com.ua`) — Ukrainian manufacturer of dry hygiene kits for military and field use. Founded 2017, family-run, Ukrainian Business Awards 2023 winner. Owner Kateryna spends 3–4 hours per workday rewriting product cards with ChatGPT and has 30 products + 10–20 general pages remaining. Has named image generation as her topmost pain.

## What we believe
1. Brand asset preservation is the core unmet need, not image generation quality.
2. The right architecture is **composite-first**: real product photos are sacred assets that get placed into AI-generated scenes, never regenerated.
3. Mask-based / regional editing is required — full-image regeneration always breaks something the user said not to touch.
4. A narrow tool with 5–7 standard e-com photo templates beats a general image editor for this audience.
5. Ukrainian / regional integrations (Horoshop API, Cyrillic-aware UI, local payment) are a real moat against US-built generic tools.
6. Owners will pay 500–2000 UAH/month for a tool that demonstrably saves 5+ hours of their personal time per week.

## What we explicitly do not believe
- We do not believe we can or should compete with Midjourney / Flux / general AI image tools on quality of free-form generation.
- We do not believe this becomes a billion-dollar SaaS. Realistic ceiling: 10–50 paying brands in year 1, 100–300 in year 2, low-to-mid tens of thousands UAH/month MRR. This is a profitable side-business, not a venture-scale company.
- We do not believe service / consulting work is the right business model for the operator. Product-first.

## MVP product description (V0 draft — to be finalized after voice call)

### Core concept
A web app where a brand owner uploads their product asset library once, then generates galleries of product photos by selecting composition templates and use-case scenes. Brand assets are never regenerated; they are composited into AI-generated backgrounds.

### Core layers

1. **Asset Library**
   - Owner uploads real product photos (packaging from multiple angles, components, textures)
   - Each asset is tagged "locked — never regenerate"
   - Stored with metadata: product name, SKU, asset type

2. **Scene Generator**
   - Generates background scenes only, without products
   - Pre-built scene categories: field/trench, vehicle interior, backpack, kitchen, hospital, white background, lifestyle
   - User can describe custom scenes via short prompt + reference image

3. **Compositor**
   - Places real product asset onto generated scene
   - Auto-matches lighting, shadow direction, perspective, scale
   - Preserves all packaging text, logos, and product details pixel-perfect

4. **Templates (7 standard e-commerce photo types)**
   - Hero shot (white / clean background)
   - Use case in context (with character interaction)
   - Bundle / components breakdown
   - Compactness / scale (in pocket, hand, backpack)
   - Comparison (vs alternatives)
   - Result / outcome shot
   - Lifestyle scenario series

5. **Counting Engine** (for bundles)
   - "X items + Y gift" compositions handled programmatically
   - Layout grid, not generation, so counts are always exact

6. **Region Editor**
   - Mask-based local edits ("change only this area")
   - All un-masked pixels guaranteed unchanged
   - Critical for "don't touch packaging / typography" cases

7. **Output**
   - Pack of files in correct dimensions for target platform (start: Horoshop)
   - Optional direct upload via Horoshop API
   - Recommended ordering for the gallery (per established e-com best practice)

## What we are NOT building (MVP)
- Free-form image generation
- Video
- Text generation (the design partner already uses ChatGPT for this and is satisfied)
- Multi-user collaboration
- Auto-translation of product descriptions
- Mobile app
- Anything for follow-up messaging, CRM, or non-image workflows

## Pricing hypothesis (to validate)
- Free tier: 5 generations/month, watermarked
- Paid tier: 500–1500 UAH/month for unlimited generations
- Design partner gets 6 months free in exchange for partnership

## Defensibility / moat
- Vertical focus on Ukrainian DTC e-commerce (US tools won't tune for this)
- Horoshop / Prom / Rozetka native integrations
- Composite-first architecture (most generic tools won't pivot to this; it's a different product philosophy)
- Cyrillic-aware UX, local payment (Fondy / LiqPay in v2)
- Real customer co-design from day one

## Risks we are aware of
- Image AI improves rapidly; what is hard today (asset preservation) may be a default ChatGPT feature in 12 months. Counter: product depth in workflow / templates / Ukrainian e-com integrations, not just model quality.
- Small TAM: 500–2000 brands × low single-digit conversion = small business. Counter: this is acceptable; not aiming for venture-scale.
- One-design-partner risk: building for a sample of one. Counter: explicit Phase 0 → Phase 1 gate to validate with at least 2–3 more brands before scaling.
- Operator capacity: 10–15 hrs/week is tight. Counter: aggressive scoping, Claude Code as force multiplier, no service-side distractions.

## Conviction level (operator)
"Willing to try, no better options yet visible." This is honest and acceptable for Phase 0. Conviction is not a prerequisite; it's an outcome of validation. Decision gates exist precisely because we don't have to be sure today.

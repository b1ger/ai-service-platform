"""Scene generation via Replicate (Flux Schnell).

We deliberately use Flux Schnell because:
- it's fast (~2-3s per image)
- it's cheap (~$0.003 / image)
- the scenes we want are simple environments without products,
  which Flux handles well without aggressive prompting

For production we may switch to Imagen or self-hosted Flux Pro.
"""

import os
from io import BytesIO
from typing import Optional

import replicate
import requests
from dotenv import load_dotenv
from PIL import Image

from .scenes import ScenePreset

load_dotenv()


FLUX_SCHNELL_VERSION = "black-forest-labs/flux-schnell"


def generate_scene(preset: ScenePreset, seed: Optional[int] = None) -> Image.Image:
    """Generate a background scene image (no product, no people, no text).

    Returns a PIL Image at 1024x1024.
    """
    if not os.getenv("REPLICATE_API_TOKEN"):
        raise RuntimeError(
            "REPLICATE_API_TOKEN not set. Copy .env.example to .env and fill it in."
        )

    inputs = {
        "prompt": preset.prompt,
        "aspect_ratio": "1:1",
        "output_format": "png",
        "num_outputs": 1,
        "num_inference_steps": 4,  # schnell is optimized for 4 steps
        "go_fast": True,
        "megapixels": "1",
    }
    if seed is not None:
        inputs["seed"] = seed

    output = replicate.run(FLUX_SCHNELL_VERSION, input=inputs)

    # replicate.run returns either a list of URLs (older client) or
    # a list of FileOutput objects (newer client). Handle both.
    item = output[0] if isinstance(output, list) else output

    if hasattr(item, "read"):
        # FileOutput-style: stream the bytes directly
        return Image.open(BytesIO(item.read())).convert("RGB")

    # Treat as URL
    url = str(item)
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    return Image.open(BytesIO(response.content)).convert("RGB")

"""Background removal for the input product photo.

Uses rembg locally (no API call). For better quality we could swap to a
Replicate-hosted BiRefNet, but rembg is fast, free, and good enough for the demo.
"""

from io import BytesIO
from pathlib import Path

from PIL import Image
from rembg import remove


def remove_background(image: Image.Image) -> Image.Image:
    """Return a transparent PNG of the product, background removed.

    Input: PIL Image (any mode)
    Output: PIL Image, RGBA, with the product foregrounded on transparency
    """
    # rembg.remove accepts bytes; convert PIL → bytes → bytes → PIL
    buf_in = BytesIO()
    image.convert("RGBA").save(buf_in, format="PNG")
    buf_in.seek(0)

    output_bytes = remove(buf_in.read())

    return Image.open(BytesIO(output_bytes)).convert("RGBA")


def remove_background_from_path(path: Path | str) -> Image.Image:
    return remove_background(Image.open(path))

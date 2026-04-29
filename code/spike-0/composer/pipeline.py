"""End-to-end pipeline: product photo + scene key → composited image."""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from PIL import Image

from .background_removal import remove_background
from .compositor import composite_product_into_scene
from .scene_generator import generate_scene
from .scenes import SCENE_PRESETS, get_scene


@dataclass
class CompositeResult:
    input_image: Image.Image
    product_no_bg: Image.Image
    generated_scene: Image.Image
    final_composite: Image.Image


def generate_composite(
    product_image: Image.Image,
    scene_key: str,
    seed: Optional[int] = None,
    save_dir: Optional[Path] = None,
) -> CompositeResult:
    """Run the full pipeline.

    1. Remove background from product photo
    2. Generate target scene (no products in it)
    3. Composite product into scene with shadow

    Args:
        product_image: PIL Image of the product
        scene_key: one of SCENE_PRESETS keys
        seed: optional seed for reproducible scene generation
        save_dir: if set, save intermediates and final to this dir

    Returns:
        CompositeResult with all four images for display.
    """
    preset = get_scene(scene_key)

    # Step 1: background removal
    product_no_bg = remove_background(product_image)

    # Step 2: generate scene
    scene = generate_scene(preset, seed=seed)

    # Step 3: composite
    final = composite_product_into_scene(
        product_rgba=product_no_bg,
        scene_rgb=scene,
        target_position=preset.target_position,
        add_shadow=True,
    )

    if save_dir is not None:
        save_dir = Path(save_dir)
        save_dir.mkdir(parents=True, exist_ok=True)
        product_no_bg.save(save_dir / "01_product_no_bg.png")
        scene.save(save_dir / "02_scene.png")
        final.save(save_dir / "03_final.png")

    return CompositeResult(
        input_image=product_image,
        product_no_bg=product_no_bg,
        generated_scene=scene,
        final_composite=final,
    )

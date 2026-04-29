"""Composite a transparent product PNG onto a generated background.

This is the heart of the composite-first architecture. Key principle:
the product pixels are NEVER regenerated. We resize and place the
real product image on top of the AI-generated scene, with simple
shadow synthesis underneath.

For the demo this PIL-based approach is enough. Production will likely
add: light direction estimation, color harmonization, AI-assisted
edge blending via Flux Fill, etc.
"""

from PIL import Image, ImageDraw, ImageFilter


def composite_product_into_scene(
    product_rgba: Image.Image,
    scene_rgb: Image.Image,
    target_position: tuple[float, float, float],
    add_shadow: bool = True,
) -> Image.Image:
    """Place product onto scene at the target position.

    Args:
        product_rgba: transparent PNG of the product (RGBA)
        scene_rgb: AI-generated background scene (RGB)
        target_position: (x_frac, y_frac, scale_frac) where:
            x_frac, y_frac — center of placement, fractions of scene dimensions (0-1)
            scale_frac — height of product as fraction of scene height (0-1)
        add_shadow: whether to render a soft drop shadow under the product

    Returns:
        Composited PIL Image (RGB)
    """
    scene = scene_rgb.convert("RGBA").copy()
    scene_w, scene_h = scene.size

    x_frac, y_frac, scale_frac = target_position

    # Resize the product to occupy scale_frac of scene height
    target_height = int(scene_h * scale_frac)
    aspect = product_rgba.width / product_rgba.height
    target_width = int(target_height * aspect)

    product_resized = product_rgba.resize(
        (target_width, target_height), Image.LANCZOS
    )

    # Compute top-left placement
    cx = int(scene_w * x_frac)
    cy = int(scene_h * y_frac)
    px = cx - target_width // 2
    py = cy - target_height // 2

    if add_shadow:
        scene = _draw_shadow(scene, product_resized, (px, py))

    scene.alpha_composite(product_resized, (px, py))
    return scene.convert("RGB")


def _draw_shadow(
    scene: Image.Image,
    product: Image.Image,
    placement: tuple[int, int],
) -> Image.Image:
    """Synthesise a soft drop shadow under the product.

    Crude but visually convincing for the demo:
    - extract the alpha mask of the product
    - downscale slightly, fill with semi-transparent black
    - blur it
    - paste it offset down-and-right from the product
    """
    px, py = placement
    alpha = product.split()[-1]

    # Slightly squashed shadow (foreshortening)
    shadow_w = int(alpha.width * 1.0)
    shadow_h = int(alpha.height * 0.4)
    shadow_alpha = alpha.resize((shadow_w, shadow_h), Image.LANCZOS)

    shadow = Image.new("RGBA", (shadow_w, shadow_h), (0, 0, 0, 0))
    fill = Image.new("RGBA", (shadow_w, shadow_h), (0, 0, 0, 110))
    shadow.paste(fill, (0, 0), shadow_alpha)

    # Heavy blur for softness
    shadow = shadow.filter(ImageFilter.GaussianBlur(radius=12))

    # Position shadow at the product's "feet"
    shadow_x = px + int(alpha.width * 0.05)
    shadow_y = py + alpha.height - int(shadow_h * 0.6)

    scene.alpha_composite(shadow, (shadow_x, shadow_y))
    return scene

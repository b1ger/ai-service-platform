"""Hardcoded scene presets for the demo.

Each preset includes a Flux-friendly prompt that produces a clean background
scene with a clearly-defined "empty zone" where the product will be composited.

For the spike we keep these few and well-tested. Production will expand.
"""

from dataclasses import dataclass


@dataclass
class ScenePreset:
    key: str
    label: str
    prompt: str
    negative_prompt: str
    # Where (roughly) the product should land. (x_frac, y_frac, scale_frac)
    target_position: tuple[float, float, float]


SCENE_PRESETS: dict[str, ScenePreset] = {
    "trench_field": ScenePreset(
        key="trench_field",
        label="Окоп / польові умови",
        prompt=(
            "Cinematic photograph of a muddy military trench at golden hour. "
            "Sandbags, dirt walls, scattered gear, soft afternoon light. "
            "Empty foreground in the center-bottom of the frame, ready for an object to be placed there. "
            "No people, no products, no text, no logos. "
            "Realistic, documentary style, shallow depth of field, 50mm lens look."
        ),
        negative_prompt="people, soldier, product, packaging, text, logos, watermark, cartoon",
        target_position=(0.50, 0.72, 0.28),
    ),
    "vehicle_interior": ScenePreset(
        key="vehicle_interior",
        label="Інтер'єр авто",
        prompt=(
            "Realistic photograph of a vehicle's center console and front passenger seat, "
            "warm afternoon light through the windshield, leather seat texture, "
            "an empty area on the seat in the foreground. "
            "Documentary style, no people, no products, no text, no logos."
        ),
        negative_prompt="people, driver, product, packaging, text, logos, watermark",
        target_position=(0.55, 0.65, 0.22),
    ),
    "backpack_pocket": ScenePreset(
        key="backpack_pocket",
        label="Кишеня рюкзака / спорядження",
        prompt=(
            "Realistic close-up photograph of an open military-style backpack pocket, "
            "tactical fabric, daylight, the pocket is empty in the center of the frame. "
            "No products, no people, no text, no logos."
        ),
        negative_prompt="people, product, packaging, text, logos, watermark",
        target_position=(0.50, 0.55, 0.30),
    ),
    "field_hike": ScenePreset(
        key="field_hike",
        label="Похід / природа",
        prompt=(
            "Realistic photograph of a forest clearing or grassy field on a sunny day, "
            "a flat surface in the foreground (a log, a rock, or grass) "
            "where an object could be placed. Natural daylight, no people, no products, no text."
        ),
        negative_prompt="people, hiker, product, packaging, text, logos, watermark",
        target_position=(0.50, 0.70, 0.25),
    ),
    "white_studio": ScenePreset(
        key="white_studio",
        label="Студія / білий фон",
        prompt=(
            "Clean white studio background, soft even lighting, slight floor reflection, "
            "minimalist product photography setting. No products, no text, no logos."
        ),
        negative_prompt="background clutter, text, logos, watermark, people",
        target_position=(0.50, 0.60, 0.40),
    ),
}


def get_scene(key: str) -> ScenePreset:
    if key not in SCENE_PRESETS:
        raise KeyError(f"Unknown scene: {key}. Available: {list(SCENE_PRESETS)}")
    return SCENE_PRESETS[key]

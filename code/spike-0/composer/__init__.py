"""Composer Spike-0 — throwaway demo pipeline.

See ../../DEMO_SCOPE.md for context. Not production code.
"""

from .pipeline import generate_composite
from .scenes import SCENE_PRESETS

__all__ = ["generate_composite", "SCENE_PRESETS"]

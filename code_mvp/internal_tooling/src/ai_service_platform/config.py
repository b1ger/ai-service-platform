import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent.parent
SRC_DIR = BASE_DIR / "src"
EXAMPLES_DIR = BASE_DIR / "examples"

# Artifact storage
OUTPUT_DIR = EXAMPLES_DIR / "outputs"
INPUT_DIR = EXAMPLES_DIR / "inputs"

def ensure_dirs():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(INPUT_DIR, exist_ok=True)

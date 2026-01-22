import os
from dataclasses import dataclass

from . import __version__ as GENERATOR_VERSION

# Short git commit from GitHub Actions
GIT_COMMIT = os.getenv("GITHUB_SHA", "dev")[:7]

# IMPORTANT: set as GitHub Actions secret
GLOBAL_SALT = os.getenv("GLOBAL_SALT", "CHANGE_ME")

@dataclass(frozen=True)
class DifficultySpec:
    name: str
    rows: int
    cols: int
    active_cells: int
    cards: int
    regions: int

# Fixed sizes per difficulty
SPECS = {
    "easy":   DifficultySpec("easy",   4, 4, 12,  6,  4),
    "medium": DifficultySpec("medium", 6, 6, 30, 15, 10),
    "hard":   DifficultySpec("hard",   8, 8, 48, 24, 16),
}

# Fence colors are per-card, hint-only (NOT used in region rules)
FENCE_COLORS = ["white", "brown", "black"]

# Animal roster (8) — snail is a full animal with 0 legs.
ANIMALS = [
    ("Chicken", 2),
    ("Cow", 4),
    ("Horse", 4),
    ("Dog", 4),
    ("Cat", 4),
    ("Bee", 6),
    ("Spider", 8),
    ("Snail", 0),
]

"""Top-level package exports for the template package.

Overview:
- Purpose: Define what the package exposes as public API.
- Used by: Python import system and downstream users.
- Adds: Stable import paths and cleaner user-facing package surface.
- Learn more: https://docs.python.org/3/tutorial/modules.html#packages
"""

from mypackage.example import clip_and_scale, power_self

__all__ = ["power_self", "clip_and_scale"]

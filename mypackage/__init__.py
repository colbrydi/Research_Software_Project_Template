"""Top-level package exports for the template package.

Overview:
- Purpose: Define what the package exposes as public API.
- Used by: Python import system and downstream users.
- Adds: Stable import paths and cleaner user-facing package surface.
- Learn more: https://docs.python.org/3/tutorial/modules.html#packages
"""

from importlib.metadata import PackageNotFoundError, version

from mypackage.example import clip_and_scale, power_self

__all__ = ["power_self", "clip_and_scale"]

# Optional: expose package version from installed metadata.
# When running directly from source, metadata may not exist yet.
try:
	__version__ = version("mypackage")
except PackageNotFoundError:
	__version__ = "0.0.0"

# ---------------------------------------------------------------------------
# Scaffold examples for future package growth
# ---------------------------------------------------------------------------
# 1) Grouped imports from multiple modules:
# Learn more: https://realpython.com/python-modules-packages/
# from mypackage.algebra import solve_linear
# from mypackage.stats import mean_center
# __all__.extend(["solve_linear", "mean_center"])

# 2) Re-export everything from selected submodules using a loop:
# Learn more: https://docs.python.org/3/reference/import.html
# from mypackage import algebra as _algebra
# from mypackage import stats as _stats
#
# for _module in (_algebra, _stats):
#     __all__.extend(getattr(_module, "__all__", []))

# 3) Optional lazy imports for heavy dependencies:
# Learn more: https://peps.python.org/pep-0562/
# def __getattr__(name: str):
#     if name == "slow_model":
#         from mypackage.models import slow_model
#         return slow_model
#     raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

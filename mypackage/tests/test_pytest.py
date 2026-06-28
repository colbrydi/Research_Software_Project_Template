"""Basic tests for the template package.

Overview:
- Purpose: Verify example behavior and error handling.
- Used by: `pytest` via `make test` and CI.
- Adds: Confidence that core functionality works after changes.
- Learn more: https://docs.pytest.org/en/stable/getting-started.html

How to adapt this file to your own function:
1. Import your function at the top of the file.
2. Update one "known values" test with 3-5 concrete input/output examples.
3. Add at least one edge case (for example: empty input, zero, or one).
4. Add at least one invalid-input test using ``pytest.raises``.
5. Keep one regression test per bug you fix in the future.

Additional tutorials:
- Pytest examples: https://docs.pytest.org/en/stable/example/index.html
- Good test structure: https://docs.pytest.org/en/stable/explanation/goodpractices.html
- Python testing intro (Real Python): https://realpython.com/python-testing/
"""

import pytest

from mypackage import clip_and_scale, power_self


# Pattern 1: import/smoke test
#
# Use this to catch setup problems early. If this fails, the package import path
# or environment is usually the first thing to check.
def test_imports() -> None:
    """Sanity-check import path for the package."""
    import mypackage

    assert hasattr(mypackage, "power_self")


# Pattern 2: fixture
#
# Fixtures are reusable setup data. Students can replace this with sample data,
# model objects, temporary files, etc.
@pytest.fixture
def small_inputs() -> list[int]:
    """Reusable sample inputs for tests."""
    return [0, 1, 2, 3]


# Pattern 3: parameterized test
#
# Parameterization lets one test function check many input/output pairs.
@pytest.mark.parametrize(
    ("x", "expected"),
    [
        (0, 1),
        (1, 1),
        (2, 4),
        (3, 27),
    ],
)
def test_power_self_known_values(x: int, expected: int) -> None:
    """Validate known values with a compact table of examples."""
    assert power_self(x) == expected


# Pattern 4: property-style test over small data
#
# This checks a simple rule across many values instead of one example.
def test_power_self_outputs_are_positive(small_inputs: list[int]) -> None:
    """All outputs for non-negative inputs should be positive."""
    for x in small_inputs:
        assert power_self(x) >= 1


# Pattern 5: exception test
#
# Use pytest.raises to verify invalid inputs fail in the expected way.
def test_power_self_type_error() -> None:
    """Non-integers should raise a clear type error."""
    with pytest.raises(TypeError):
        power_self("Hello world")  # type: ignore[arg-type]


def test_power_self_value_error() -> None:
    """Negative integers are rejected."""
    with pytest.raises(ValueError):
        power_self(-1)


# Pattern 6: regression test template
#
# Keep one test per bug that was fixed before. Replace this with a short,
# real bug example from your project when one appears.
def test_regression_example_zero_is_one() -> None:
    """Regression example: zero input should stay mapped to one."""
    assert power_self(0) == 1


# Pattern 7: multi-argument function tests
#
# This template shows tests for functions with keyword arguments and range checks.
@pytest.mark.parametrize(
    ("value", "minimum", "maximum", "expected"),
    [
        (0.25, 0.0, 1.0, 0.25),
        (-3.0, 0.0, 1.0, 0.0),
        (3.0, 0.0, 1.0, 1.0),
        (12.0, 10.0, 20.0, 0.2),
    ],
)
def test_clip_and_scale_values(value: float, minimum: float, maximum: float, expected: float) -> None:
    """Clip-and-scale should produce expected normalized values."""
    assert clip_and_scale(value, min_value=minimum, max_value=maximum) == pytest.approx(expected)


def test_clip_and_scale_type_error() -> None:
    """Non-numeric values should raise a clear type error."""
    with pytest.raises(TypeError):
        clip_and_scale("bad")  # type: ignore[arg-type]


def test_clip_and_scale_range_error() -> None:
    """Invalid ranges should raise a clear value error."""
    with pytest.raises(ValueError):
        clip_and_scale(0.5, min_value=2.0, max_value=2.0)


# Pattern 7: template students can copy/paste
#
# Replace `your_function_name` and the input/output values with your own code.
# Keep this block as a starter until your team has enough project-specific tests.
@pytest.mark.parametrize(
    ("x", "expected"),
    [
        (1, 1),
        (2, 4),
    ],
)
def test_template_replace_with_your_function(x: int, expected: int) -> None:
    """Template: replace this with tests for your own function."""
    assert power_self(x) == expected


"""Example module for template projects.

Overview:
- Purpose: Show a small, testable function with input validation.
- Used by: Import statements in user code and unit tests.
- Adds: A clear starting example for writing robust functions.
- Learn more: https://docs.python.org/3/tutorial/controlflow.html#defining-functions

Docstring features demonstrated in this file:

- Argument and return type descriptions
- Raised exceptions
- Copy-paste examples
- Notes and cross-references for readers

These sections render nicely in pdoc-generated pages.
"""


def power_self(x: int) -> int:
    """Return x raised to itself.

    Args:
        x: A non-negative integer.

    Returns:
        The value of x**x.

    Raises:
        TypeError: If ``x`` is not an integer.
        ValueError: If ``x`` is negative.

    Examples:
        >>> power_self(3)
        27
        >>> power_self(0)
        1

    Notes:
        This function is intentionally simple and easy to test.
        It is a good first example for students learning unit testing.

    See Also:
        clip_and_scale: Example with multiple parameters and keyword-only args.
    """
    if not isinstance(x, int):
        raise TypeError("x must be an integer")
    if x < 0:
        raise ValueError("x must be non-negative")
    return int(x**x)


def clip_and_scale(value: float, *, min_value: float = 0.0, max_value: float = 1.0) -> float:
    """Clip a number to a range, then scale to [0, 1].

    Args:
        value: Input value to transform.
        min_value: Lower bound for clipping.
        max_value: Upper bound for clipping.

    Returns:
        Value clipped to ``[min_value, max_value]`` and scaled into ``[0, 1]``.

    Raises:
        TypeError: If ``value`` is not numeric.
        ValueError: If ``max_value <= min_value``.

    Examples:
        >>> clip_and_scale(0.25)
        0.25
        >>> clip_and_scale(-2.0)
        0.0
        >>> clip_and_scale(12.0, min_value=10.0, max_value=20.0)
        0.2

    Notes:
        This pattern (validate -> transform -> return) is common in scientific code.
        The function is small on purpose so students can practice writing tests.
    """
    if not isinstance(value, (int, float)):
        raise TypeError("value must be numeric")
    if max_value <= min_value:
        raise ValueError("max_value must be greater than min_value")

    clipped = min(max(float(value), min_value), max_value)
    return (clipped - min_value) / (max_value - min_value)



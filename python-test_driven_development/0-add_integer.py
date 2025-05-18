#!/usr/bin/python3
"""
This module provides a function to add two integers.
"""


def add_integer(a, b=98):
    """
    Returns the sum of a and b as integers.

    >>> add_integer(2, 3)
    5
    >>> add_integer(100, -2)
    98
    >>> add_integer(100.3, -2)
    98
    >>> add_integer(4, "School")
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    >>> add_integer(None)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    >>> add_integer(float('inf'), 1)
    Traceback (most recent call last):
        ...
    ValueError: cannot convert float NaN to integer
    >>> add_integer(float('nan'), 1)
    Traceback (most recent call last):
        ...
    ValueError: cannot convert float NaN to integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float) and (a != a or a == float('inf') or a == float('-inf')):
        raise ValueError("cannot convert float NaN to integer")
    if isinstance(b, float) and (b != b or b == float('inf') or b == float('-inf')):
        raise ValueError("cannot convert float NaN to integer")
    return int(a) + int(b)


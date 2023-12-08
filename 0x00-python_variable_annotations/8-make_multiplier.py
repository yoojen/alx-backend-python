#!/usr/bin/env python3
"""Python basic variables annotation"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function with multiplied inputs"""
    def inner_function(inner_float: float) -> float:
        return inner_float * multiplier
    return inner_function

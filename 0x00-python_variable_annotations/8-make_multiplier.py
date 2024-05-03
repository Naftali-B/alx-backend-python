#!/usr/bin/env python3
"""
    type-annotated function make_multiplier
    takes a float multiplier
    returns a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        Args:
            a float multiplier

        Return:
            a function that multiplies a float by multiplier
    """

    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function

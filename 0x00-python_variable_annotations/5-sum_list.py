#!/usr/bin/env python3
"""
    type-annotated function sum_list
    takes a list input_list of floats
    and returns their sum as a float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
        Args:
            input_list: float numbers

        Return:
            Sum of input_list as float
    """

    return sum(input_list)

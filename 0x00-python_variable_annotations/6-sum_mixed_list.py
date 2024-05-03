#!/usr/bin/env python3
"""
    type-annotated function sum_mixed_list
    takes a list mxd_lst of integers and floats
    returns their sum as a float
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        Args:
            mxd_lst: list of integers and floats

        Return:
            their sum as a float
    """

    return sum(mxd_lst)

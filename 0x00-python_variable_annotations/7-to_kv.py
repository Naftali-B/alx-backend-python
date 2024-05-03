#!/usr/bin/env python3
"""
    type-annotated function to_kv that takes a string k and an int OR float v
    returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        Args:
            k: String
            v: Union: int or float

        Return:
            A tuple with string and int or float
    """

    return (k, float(v ** 2))

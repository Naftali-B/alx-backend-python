#!/usr/bin/env python3
"""
    duck-typed annotations
"""
from typing import Union, Any, Sequence



def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
        Args:
            lst: Any data type

        Return:
            lst[0] or None
    """
    if lst:
        return lst[0]
    else:
        return None

#!/usr/bin/env python3
""" a measure_time function """

import time
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


def measure_time(max_delay: int = 10, n: int = 0) -> float:
    """
        Args:
            n: int
            max_delay int: max wait

        Return:
            total_time / n : float
    """
    first_time = time.perf_counter()
    asyncio.run(wait_n(max_delay, n))
    elapsed = time.perf_counter() - first_time
    total_time = elapsed / n

    return total_time

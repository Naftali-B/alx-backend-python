#!/usr/bin/env python3
""" async routine, wait_n """
import asyncio
import random
from typing import List


from basic_async_syntax import wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
        Args:
            n: spawn function
            max_delay: max wait

        Return:
            return the list of all the delays (float values)
    """
    delays: List[float] = []
    tasks: List = []

    for _ in range(n):
        tasks.append(wait_random(max_delay))

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays

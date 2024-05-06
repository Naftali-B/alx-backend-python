#!/usr/bin/env python3
""" Execute wait_random coroutine n times concurrently. """

import asyncio
import random
from typing import List


task_wait_random = __import__('3-tasks').wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
        Args:
            n (int): Number of times to execute wait_random coroutine.
            max_delay (int): Maximum delay for each wait_random coroutine.

        Return:
            List[float]: List of delays returned by wait_random coroutines.
    """
    delays: List[float] = []
    tasks: List[asyncio.Task] = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays

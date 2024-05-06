#!/usr/bin/env python3
""" asynchronous coroutine """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
        Args:
            max_delay, with a default value of 10

        Return:
            delay: random floating-point number
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay

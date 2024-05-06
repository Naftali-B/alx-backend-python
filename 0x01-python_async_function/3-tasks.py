#!/usr/bin/env python3
""" task_wait_random """

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
        Args:
            max_delay (int): Maximum delay for the wait_random coroutine.

        Return:
            Task: Task object for the wait_random coroutine.
    """
    task = asyncio.create_task(wait_random(max_delay))

    return task

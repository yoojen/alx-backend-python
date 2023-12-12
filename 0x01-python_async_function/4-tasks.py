#!/usr/bin/env python3

"""async routine called wait_n that takes in 2 int arguments"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """process task returned with Task obj in task 3 and return list"""
    delay_tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(delay_tasks)]

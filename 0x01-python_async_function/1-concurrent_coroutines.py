#!/usr/bin/env python3

"""async routine called wait_n that takes in 2 int arguments"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """get result from async function"""
    delay_tasks = [asyncio.create_task(
        wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(delay_tasks)]

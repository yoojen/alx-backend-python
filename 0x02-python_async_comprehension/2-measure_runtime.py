#!/usr/bin/env python3
"""await for async to finish and calculate time elapsed"""

import asyncio
from time import perf_counter
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """measure run time of async_comperation function from other file"""
    start = perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end = perf_counter()

    return (end - start)

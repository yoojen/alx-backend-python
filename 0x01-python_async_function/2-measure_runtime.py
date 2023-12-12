#!/usr/bin/env python3

"""function with integers n and max_delay as arguments"""

import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    function measure time elapssed

    Keyword arguments:
    n -- number of times
    max_delay -- total time that function can delay while executing
    Return: total time / n
    """

    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    time_elapsed = time.perf_counter() - start
    return time_elapsed / n

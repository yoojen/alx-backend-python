#!/usr/bin/env python3

"""asynchronous coroutine that takes in an integer argument"""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    asynchronous coroutine that takes in an integer argument
    wait_random that waits for a random delay between 0 and max_delay

    Keyword arguments:
    max_delay -- a default value of 10 - included and float value.
    Return: returns the random number
    """

    random_number = random.uniform(0, max_delay + 1)
    await asyncio.sleep(random_number)
    return random_number

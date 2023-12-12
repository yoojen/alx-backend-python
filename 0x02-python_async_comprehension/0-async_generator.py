#!/usr/bin/env python3

"""pythhn generators - async basic syntax"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """creates geneerator and yields one for each iteration"""
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)

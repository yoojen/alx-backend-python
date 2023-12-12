#!/usr/bin/env python3

"""async comprehension implementation"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List:
    """async comprehension to make easy readable syntax"""
    results = [result async for result in async_generator()]
    return results

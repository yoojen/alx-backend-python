#!/usr/bin/env python3
"""create task and return Task object"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """return the task object of wait random async function"""
    return asyncio.create_task(wait_random(max_delay))

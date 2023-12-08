#!/usr/bin/env python3
"""Python basic variables annotation"""

from typing import List


def sum_list(input_list: List[float]) -> float:
        """return summation of list form input of function"""
        sum: float = 0.0
        for number in input_list:
            sum = sum + number
        return sum

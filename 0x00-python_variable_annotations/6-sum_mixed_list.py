#!/usr/bin/env python3
"""Python basic variables annotation"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
        """return summation of list form input of function"""
        sum = 0.0
        for number in mxd_lst:
            sum = sum + number
        return sum

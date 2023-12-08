#!/usr/bin/env python3
"""Python basic variables annotation"""

from typing import List, Sequence, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return types of typing module classes"""
    return [(i, len(i)) for i in lst]

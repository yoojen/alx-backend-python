#!/usr/bin/env python3

import unittest
from parameterized import parameterized
access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """test utils.access_nested_map possible edge cases"""

    @parameterized.expand([
            ({"a": 1}, "a", 1),
            ({"a": {"b": 2}}, "a", {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
            ])
    def test_access_nested_map(self, nested_map, sequence, expected_output):
        """check if all output are right"""
        res = access_nested_map(nested_map, sequence)
        self.assertEqual(res, expected_output)

    @parameterized.expand([
            ({}, ['a'], KeyError),
            ({"a": 1}, ['a', 'b'], KeyError)
            ])
    def test_access_nested_map_exception(self, nested_map, sequence, exc):
        """check if the function raises an exception"""
        with self.assertRaises(exc, msg="KeyError Exception occured"):
            access_nested_map(nested_map, sequence)

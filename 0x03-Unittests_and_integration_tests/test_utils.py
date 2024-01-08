#!/usr/bin/env python3

import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import (access_nested_map, get_json)


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


class TestGetJson(unittest.TestCase):
    """implement mock testing for api request"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io",  {"payload": False})
        ])
    def test_get_json(self, test_url, test_payload):
        """check if utils.get_json returned expected results using mock"""
        configs = {'return_value.json.return_value': test_payload}
        patcher = patch('requests.get', **configs)
        mock = patcher.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()
        patcher.stop()

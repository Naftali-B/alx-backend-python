#!/usr/bin/env python3
"""Test utilities"""
import unittest
from unittest.mock import patch
import requests
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized, parameterized_class


class TestAccessNestedMap(unittest.TestCase):
    """Tests for access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map returns correct result"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map raises KeyError for invalid path"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), str(KeyError(path)))


class TestGetJson(unittest.TestCase):
    """Tests for get_json function"""

    @parameterized.expand([
        ("http://tack.plus", {"payload": True}),
        ("http://tack.plus", {"payload": False})
    ])
    def test_get_json(self, url, expected_payload):
        """Test get_json returns correct JSON response"""
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = expected_payload
            self.assertEqual(get_json(url), expected_payload)


class TestMemoize(unittest.TestCase):
    """Tests for memoize decorator"""

    def test_memoize(self):
        """Test memoize decorator caches result"""
        class TestClass:
            """Test class with a method and memoized property"""

            def a_method(self):
                """Simple method returning a fixed value"""
                return 42

            @memoize
            def a_property(self):
                """Memoized property"""
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            test_instance = TestClass()
            self.assertEqual(test_instance.a_property, 42)
            self.assertEqual(test_instance.a_property, 42)
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()


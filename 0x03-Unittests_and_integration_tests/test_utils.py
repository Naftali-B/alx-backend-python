#!/usr/bin/env python3
"""
Test utils
"""
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
        """Test that access_nested_map returns the expected result"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that access_nested_map raises KeyError for invalid paths"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), repr(context.exception))


class TestGetJson(unittest.TestCase):
    """Tests for get_json function"""

    @parameterized.expand([
        ("http://tack.plus", {"payload": True}),
        ("http://tack.plus", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Test that get_json returns the expected JSON response"""
        with patch('requests.get') as mock_request:
            mock_request.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)
            mock_request.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Tests for memoize decorator"""

    def test_memoize(self):
        """Test that memoize caches the result of the method"""

        class TestClass:
            """Test class with memoized method"""

            def a_method(self):
                """Method that returns 42"""
                return 42

            @memoize
            def a_property(self):
                """Memoized property"""
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            test_instance = TestClass()
            self.assertEqual(test_instance.a_property(), 42)
            self.assertEqual(test_instance.a_property(), 42)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()


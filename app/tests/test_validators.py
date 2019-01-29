#StackOverflow-lite/app/tests/test_validators.py
"""Tests for validators run with pytest"""
import unittest
from app.api.validators import validate_string   


class ValidatorsTestCase(unittest.TestCase):


    def test_for_strings(self):
        with self.assertRaises(ValueError):
            validate_string("@##$$Hello")

    
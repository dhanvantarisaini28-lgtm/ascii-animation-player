"""
test_validation.py
-------------------
Unit tests for the menu input-validation logic in main.py.

Run with:
    python -m unittest test_validation.py -v

(These tests also work with pytest if you have it installed: `pytest`.)
"""

import unittest

from main import parse_choice

MAX_OPTION = 12  # same as len(MENU_OPTIONS) in main.py


class TestParseChoice(unittest.TestCase):

    def test_valid_choice_in_range(self):
        self.assertEqual(parse_choice("1", MAX_OPTION), 1)
        self.assertEqual(parse_choice("12", MAX_OPTION), 12)

    def test_valid_quit_choice(self):
        self.assertEqual(parse_choice("0", MAX_OPTION), 0)

    def test_non_numeric_input_is_rejected(self):
        self.assertIsNone(parse_choice("abc", MAX_OPTION))
        self.assertIsNone(parse_choice("", MAX_OPTION))
        self.assertIsNone(parse_choice("5.5", MAX_OPTION))

    def test_out_of_range_input_is_rejected(self):
        self.assertIsNone(parse_choice("13", MAX_OPTION))
        self.assertIsNone(parse_choice("99", MAX_OPTION))

    def test_negative_input_is_rejected(self):
        # str.isdigit() is False for a leading '-', so this should
        # already be rejected before the range check even runs.
        self.assertIsNone(parse_choice("-1", MAX_OPTION))

    def test_whitespace_input_is_rejected(self):
        self.assertIsNone(parse_choice("  ", MAX_OPTION))
        self.assertIsNone(parse_choice(" 5", MAX_OPTION))


if __name__ == "__main__":
    unittest.main()

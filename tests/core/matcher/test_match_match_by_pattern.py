import unittest
from src.core import match_by_pattern


class TestCoreMatcherMatchByPattern(unittest.TestCase):
    def test_is_defined(self):
        self.assertTrue(match_by_pattern)

    def test_matches_by_pattern(self):
        expected = "1st"
        matches = match_by_pattern("persons", "I")
        (person, span) = matches[0]
        self.assertEqual(person, expected)

    def test_true_negative(self):
        not_expected = "2nd"
        matches = match_by_pattern("persons", "I")
        (person, span) = matches[0]
        self.assertNotEqual(person, not_expected)

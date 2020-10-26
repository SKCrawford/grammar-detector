import unittest
from src.core import match_by_pattern


class TestCoreMatcherMatchByPattern(unittest.IsolatedAsyncioTestCase):
    def test_is_defined(self):
        self.assertTrue(match_by_pattern)

    async def test_matches_by_pattern(self):
        expected = "1st"
        matches = await match_by_pattern("persons", "I")
        (person, span) = matches[0]
        self.assertEqual(person, expected)

    async def test_true_negative(self):
        not_expected = "2nd"
        matches = await match_by_pattern("persons", "I")
        (person, span) = matches[0]
        self.assertNotEqual(person, not_expected)

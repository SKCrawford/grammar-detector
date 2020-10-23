import unittest
from src.core import match_by_pattern


class TestPatternMatcher(unittest.TestCase):
    def test_is_defined(self):
        self.assertTrue(match_by_pattern)

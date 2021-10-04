import unittest
from src.core.matcher.parse import parse_match


class TestCoreMatcherParseMatch(unittest.TestCase):
    def test_is_defined(self):
        self.assertTrue(parse_match)

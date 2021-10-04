import unittest
from src.core.matcher.match import run_matcher


class TestCoreMatcherRunMatcher(unittest.TestCase):
    def test_is_defined(self):
        self.assertTrue(run_matcher)

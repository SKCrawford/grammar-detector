import unittest
from src.core.pattern import load_patterns


class TestPatternLoader(unittest.TestCase):
    def test_is_defined(self):
        self.assertTrue(load_patterns)

    # TODO

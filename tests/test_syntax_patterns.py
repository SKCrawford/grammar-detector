import unittest
from src.SyntaxPatterns import SyntaxPatterns


class TestSyntaxPatternsSingleton(unittest.TestCase):
    def test_is_defined(self):
        self.assertTrue(SyntaxPatterns)

    def test_is_constructable(self):
        self.assertTrue(SyntaxPatterns())

    def test_loads_patterns(self):
        self.assertTrue(SyntaxPatterns().patterns)

    def test_is_singleton(self):
        instance1 = SyntaxPatterns()
        instance2 = SyntaxPatterns()
        self.assertIs(instance1, instance2)

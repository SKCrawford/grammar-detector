import unittest
from src.nlp import nlp


class TestGlobalNlpTokenizer(unittest.TestCase):
    def test_is_defined(self):
        self.assertTrue(nlp)

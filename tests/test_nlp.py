import unittest
from grammardetector.Nlp import Nlp


class TestGlobalNlpTokenizer(unittest.TestCase):
    def test_is_defined(self):
        nlp = Nlp()
        self.assertTrue(nlp)
        self.assertTrue(nlp._nlp)

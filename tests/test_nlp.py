import unittest
from spacy.lang.en import English
from src.nlp import nlp


class TestGlobalNlpTokenizer(unittest.TestCase):
    def test_is_defined(self):
        self.assertTrue(nlp)
        self.assertIsInstance(nlp, English)

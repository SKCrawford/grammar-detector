import unittest
from src.core import extract_span_features


class TestPhraseFeatureParser(unittest.TestCase):
    def test_is_defined(self):
        self.assertTrue(extract_span_features)

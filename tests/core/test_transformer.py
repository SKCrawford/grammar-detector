import unittest
from src.core import parse_phrase_features_from_chunk


class TestPhraseFeatureParser(unittest.TestCase):
    def test_is_defined(self):
        self.assertTrue(parse_phrase_features_from_chunk)

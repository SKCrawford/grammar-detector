import unittest
from src.features.noun_set.detector import detect_noun_features
from src.features.noun_set.model import NounFeatureSet


class TestNounFeatureSetDetector(unittest.TestCase):
    def test_is_defined(self):
        self.assertTrue(detect_noun_features)

    def test_true_positive(self):
        result = detect_noun_features("I am a test.")
        self.assertTrue(result)
        self.assertIsInstance(result, NounFeatureSet)
        self.assertIsInstance(result.nouns, list)
        self.assertIsInstance(result.person, str)

    def test_true_negative(self):
        self.assertRaises(TypeError, detect_noun_features, 100)
        self.assertRaises(TypeError, detect_noun_features, True)
        self.assertRaises(TypeError, detect_noun_features, ["test string"])
        self.assertRaises(TypeError, detect_noun_features, None)

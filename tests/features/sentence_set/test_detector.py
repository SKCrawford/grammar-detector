import unittest
from src.features.sentence_set.detector import detect_sentence_features
from src.features.sentence_set.model import SentenceFeatureSet


class TestSentenceFeatureSetDetector(unittest.TestCase):
    def test_is_defined(self):
        self.assertTrue(detect_sentence_features)

    def test_true_positive(self):
        features = detect_sentence_features("I am running.")
        self.assertIsInstance(features, SentenceFeatureSet)
        self.assertTrue(features)
        self.assertIsInstance(features.sentence, str)
        self.assertEqual(features.sentence, "I am running.")

    def test_true_negative(self):
        self.assertRaises(TypeError, detect_sentence_features, 100)
        self.assertRaises(TypeError, detect_sentence_features, True)
        self.assertRaises(TypeError, detect_sentence_features, ["I am running."])
        self.assertRaises(TypeError, detect_sentence_features, None)

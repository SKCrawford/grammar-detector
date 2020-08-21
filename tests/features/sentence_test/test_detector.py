import unittest
from src.features.sentence_set.detector import detect_sentence_features
from src.features.sentence_set.model import SentenceFeatureSet
from src.features.verb_set.model import VerbFeatureSet


class TestSentenceFeatureSetDetector(unittest.TestCase):
    def test_is_defined(self):
        self.assertTrue(detect_sentence_features)

    def test_detect_sentence_feature_set(self):
        result = detect_sentence_features("I am a test.")
        self.assertIsInstance(result, SentenceFeatureSet)
        self.assertTrue(result)

    def test_detect_sentence_feature_set_sentence(self):
        result = detect_sentence_features("I am a test.")
        self.assertIsInstance(result.sentence, str)
        self.assertEqual(result.sentence, "I am a test.")

    def test_detect_sentence_feature_set_verb_feature_set(self):
        result = detect_sentence_features("I am a test.")
        self.assertIsInstance(result.verb_features, VerbFeatureSet)
        self.assertTrue(result)

    def test_rejects_int_argument(self):
        self.assertRaises(TypeError, detect_sentence_features, 100)

    def test_rejects_bool_argument(self):
        self.assertRaises(TypeError, detect_sentence_features, True)

    def test_rejects_list_argument(self):
        self.assertRaises(TypeError, detect_sentence_features, ["I am a test."])

    def test_rejects_none_argument(self):
        self.assertRaises(TypeError, detect_sentence_features, None)

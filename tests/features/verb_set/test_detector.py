import unittest
from src.features.verb_set.detector import detect_verb_features
from src.features.verb_set.model import VerbFeatureSet


class TestVerbFeatureSetDetector(unittest.TestCase):
    def test_is_defined(self):
        self.assertTrue(detect_verb_features)

    def test_detect_verb_feature_set(self):
        result = detect_verb_features("I am a test.")
        self.assertTrue(result)
        self.assertIsInstance(result, VerbFeatureSet)

    def test_detect_verb_feature_set_verb(self):
        result = detect_verb_features("I am a test.")
        self.assertIsInstance(result.verb.root, str)
        self.assertEqual(result.verb.root, "am")

    def test_detect_verb_feature_set_tense(self):
        result = detect_verb_features("I am a test.")
        self.assertIsInstance(result.tense, str)
        self.assertEqual(result.tense, "present")

    def test_detect_verb_feature_set_aspect(self):
        result = detect_verb_features("I am a test.")
        self.assertIsInstance(result.aspect, str)
        self.assertEqual(result.aspect, "simple")

    def test_rejects_int_argument(self):
        self.assertRaises(TypeError, detect_verb_features, 100)

    def test_rejects_bool_argument(self):
        self.assertRaises(TypeError, detect_verb_features, True)

    def test_rejects_list_argument(self):
        self.assertRaises(TypeError, detect_verb_features, ["test string"])

    def test_rejects_none_argument(self):
        self.assertRaises(TypeError, detect_verb_features, None)

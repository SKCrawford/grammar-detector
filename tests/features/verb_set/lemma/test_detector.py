import unittest
from src.features.verb_set.lemma.detector import detect_verb_lemmas


class TestVerbLemmasDetector(unittest.TestCase):
    def assertLemmas_(self, value, expected_lemmas):
        result = detect_verb_lemmas(value)
        self.assertEqual(result, expected_lemmas)

    def test_is_defined(self):
        self.assertTrue(detect_verb_lemmas)

    def test_returns_a_string(self):
        lemmas = detect_verb_lemmas("I have been running.")
        self.assertIsInstance(lemmas, str)

    def test_true_positive(self):
        self.assertLemmas_("I have been running.", "have be run")

    def test_true_negative(self):
        self.assertRaises(TypeError, detect_verb_lemmas, 100)
        self.assertRaises(TypeError, detect_verb_lemmas, True)
        self.assertRaises(TypeError, detect_verb_lemmas, ["I have been running."])
        self.assertRaises(TypeError, detect_verb_lemmas, None)
        self.assertRaises(ValueError, detect_verb_lemmas, "")

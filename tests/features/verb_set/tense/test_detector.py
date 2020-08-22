import unittest
from src.features.verb_set.tense.detector import detect_verb_tense


class TestVerbFeatureSetDetector(unittest.TestCase):
    def assertTense_(self, value, expected):
        result = detect_verb_tense(value)
        self.assertEqual(result, expected)

    def test_is_defined(self):
        self.assertTrue(detect_verb_tense)

    def test_returns_a_string(self):
        result = detect_verb_tense("I am a test.")
        self.assertIsInstance(result, str)

    def test_true_positive(self):
        self.assertTense_("I run.", "present")
        self.assertTense_("I have run.", "present")
        self.assertTense_("I am running.", "present")
        self.assertTense_("I have been running.", "present")

        self.assertTense_("I ran.", "past")
        self.assertTense_("I had run.", "past")
        self.assertTense_("I was running.", "past")
        self.assertTense_("I had been running.", "past")

        self.assertTense_("I will run.", "future")
        self.assertTense_("I am going to run.", "future")
        self.assertTense_("I will have run.", "future")
        self.assertTense_("I will be running.", "future")
        self.assertTense_("I will have been running.", "future")

    def test_true_negative(self):
        self.assertRaises(TypeError, detect_verb_tense, 100)
        self.assertRaises(TypeError, detect_verb_tense, True)
        self.assertRaises(TypeError, detect_verb_tense, ["I run."])
        self.assertRaises(TypeError, detect_verb_tense, None)

    def test_false_positive(self):
        self.assertRaises(ValueError, detect_verb_tense, "")

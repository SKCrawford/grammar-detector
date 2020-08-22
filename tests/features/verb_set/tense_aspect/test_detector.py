import unittest
from src.features.verb_set.tense_aspect.detector import detect_verb_tense_aspect


class TestVerbTenseAspectDetector(unittest.TestCase):
    def assertTenseAspect_(self, value, expected_tense, expected_aspect):
        result = detect_verb_tense_aspect(value)
        self.assertEqual(result, (expected_tense, expected_aspect))

    def test_is_defined(self):
        self.assertTrue(detect_verb_tense_aspect)

    def test_returns_a_tuple_of_strings(self):
        (tense, aspect) = detect_verb_tense_aspect("I am a test.")
        self.assertIsInstance(tense, str)
        self.assertIsInstance(aspect, str)

    def test_true_positive(self):
        self.assertTenseAspect_("I run.", "present", "simple")
        self.assertTenseAspect_("I ran.", "past", "simple")
        self.assertTenseAspect_("I will run.", "future", "simple")
        self.assertTenseAspect_("I am going to run.", "future", "simple")

        self.assertTenseAspect_("I have run.", "present", "perfect")
        self.assertTenseAspect_("I had run.", "past", "perfect")
        self.assertTenseAspect_("I will have run.", "future", "perfect")

        self.assertTenseAspect_("I am running.", "present", "continuous")
        self.assertTenseAspect_("I was running.", "past", "continuous")
        self.assertTenseAspect_("I will be running.", "future", "continuous")

        self.assertTenseAspect_("I have been running.", "present", "perfect continuous")
        self.assertTenseAspect_("I had been running.", "past", "perfect continuous")
        self.assertTenseAspect_("I will have been running.", "future", "perfect continuous")

    def test_true_negative(self):
        self.assertRaises(TypeError, detect_verb_tense_aspect, 100)
        self.assertRaises(TypeError, detect_verb_tense_aspect, True)
        self.assertRaises(TypeError, detect_verb_tense_aspect, ["test string"])
        self.assertRaises(TypeError, detect_verb_tense_aspect, None)

    def test_false_positive(self):
        self.assertRaises(ValueError, detect_verb_tense_aspect, "")

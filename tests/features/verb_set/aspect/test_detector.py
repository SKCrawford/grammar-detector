import unittest
from src.features.verb_set.aspect.detector import detect_verb_aspect


class TestVerbFeatureSetDetector(unittest.TestCase):
    def assertAspect_(self, value, expected):
        result = detect_verb_aspect(value)
        self.assertEqual(result, expected)

    def test_is_defined(self):
        self.assertTrue(detect_verb_aspect)

    def test_returns_a_string(self):
        result = detect_verb_aspect("I am a test.")
        self.assertIsInstance(result, str)

    def test_true_positive(self):
        self.assertAspect_("I run.", "simple")
        self.assertAspect_("I ran.", "simple")
        self.assertAspect_("I will run.", "simple")
        self.assertAspect_("I am going to run.", "simple")

        self.assertAspect_("I have run.", "perfect")
        self.assertAspect_("I had run.", "perfect")
        self.assertAspect_("I will have run.", "perfect")

        self.assertAspect_("I am running.", "continuous")
        self.assertAspect_("I was running.", "continuous")
        self.assertAspect_("I will be running.", "continuous")

        self.assertAspect_("I have been running.", "perfect continuous")
        self.assertAspect_("I had been running.", "perfect continuous")
        self.assertAspect_("I will have been running.", "perfect continuous")

    def test_true_negative(self):
        self.assertRaises(TypeError, detect_verb_aspect, 100)
        self.assertRaises(TypeError, detect_verb_aspect, True)
        self.assertRaises(TypeError, detect_verb_aspect, ["test string"])
        self.assertRaises(TypeError, detect_verb_aspect, None)

    def test_false_positive(self):
        self.assertRaises(ValueError, detect_verb_aspect, "")

import unittest
from src.features.verb_set.verb.detector import detect_verb


class TestVerbVerbDetector(unittest.TestCase):
    def assertVerb_(self, value, expected):
        result = detect_verb(value)
        self.assertEqual(result, expected)

    def test_is_defined(self):
        self.assertTrue(detect_verb)

    def test_returns_a_string(self):
        result = detect_verb("I am a test.")
        self.assertIsInstance(result, str)

    def test_true_positive(self):
        self.assertVerb_("I run.", "run")
        self.assertVerb_("I have run.", "have run")
        self.assertVerb_("I am running.", "am running")
        self.assertVerb_("I have been running.", "have been running")

        self.assertVerb_("I ran.", "ran")
        self.assertVerb_("I had run.", "had run")
        self.assertVerb_("I was running.", "was running")
        self.assertVerb_("I had been running.", "had been running")

        self.assertVerb_("I will run.", "will run")
        self.assertVerb_("I am going to run.", "am going to run")
        self.assertVerb_("I will have run.", "will have run")
        self.assertVerb_("I will be running.", "will be running")
        self.assertVerb_("I will have been running.", "will have been running")

    def test_true_negative(self):
        self.assertRaises(TypeError, detect_verb, 100)
        self.assertRaises(TypeError, detect_verb, True)
        self.assertRaises(TypeError, detect_verb, ["I run."])
        self.assertRaises(TypeError, detect_verb, None)

    def test_false_positive(self):
        self.assertRaises(ValueError, detect_verb, "")

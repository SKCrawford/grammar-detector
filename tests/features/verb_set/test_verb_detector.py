import unittest
from src.features.verb_set import detect_verbs
from src.util.serializable import Serializable


class TestVerbVerbDetector(unittest.TestCase):
    def assertVerb_(self, sentence, expected):
        verb = detect_verbs(sentence)[0]
        self.assertEqual(verb.phrase, expected)

    def test_is_defined(self):
        self.assertTrue(detect_verbs)

    def test_returns_a_list_of_serializable_objects(self):
        result = detect_verbs("I run.")
        self.assertIsInstance(result, list)
        [self.assertIsInstance(verb, Serializable) for verb in result]

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
        self.assertRaises(TypeError, detect_verbs, 100)
        self.assertRaises(TypeError, detect_verbs, True)
        self.assertRaises(TypeError, detect_verbs, ["I run."])
        self.assertRaises(TypeError, detect_verbs, None)

    def test_false_positive(self):
        self.assertRaises(ValueError, detect_verbs, "")

import unittest
from src.features.verb_set import detect_verb_features


class TestVerbFeaturesDetector(unittest.TestCase):
    def assertVerbText_(self, value, expected_texts):
        result = detect_verb_features(value)
        count = 0
        for expected_text in expected_texts:
            verb = result[count]
            result_text = verb.phrase
            self.assertEqual(result_text, expected_text)
            count += 1

    def test_is_defined(self):
        self.assertTrue(detect_verb_features)

    def test_returns_a_list_of_serializable_objects(self):
        result = detect_verb_features("I ran to the beach.")
        self.assertIsInstance(result, list)
        [self.assertIsInstance(verb, dict) for verb in result]

    def test_true_positive(self):
        self.assertVerbText_("I run.", ["run"])
        self.assertVerbText_("I have run.", ["have run"])
        self.assertVerbText_("I am running.", ["am running"])
        self.assertVerbText_("I have been running.", ["have been running"])

        self.assertVerbText_("I ran.", ["ran"])
        self.assertVerbText_("I had run.", ["had run"])
        self.assertVerbText_("I was running.", ["was running"])
        self.assertVerbText_("I had been running.", ["had been running"])

        self.assertVerbText_("I will run.", ["will run"])
        self.assertVerbText_("I am going to run.", ["am going to run"])
        self.assertVerbText_("I will have run.", ["will have run"])
        self.assertVerbText_("I will be running.", ["will be running"])
        self.assertVerbText_("I will have been running.", ["will have been running"])

    def test_true_negative(self):
        self.assertRaises(TypeError, detect_verb_features, 100)
        self.assertRaises(TypeError, detect_verb_features, True)
        self.assertRaises(TypeError, detect_verb_features, ["I ran to the beach."])
        self.assertRaises(TypeError, detect_verb_features, None)
        self.assertRaises(ValueError, detect_verb_features, "")

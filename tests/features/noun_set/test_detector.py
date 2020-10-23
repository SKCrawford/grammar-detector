import unittest
from src.features.noun_set import detect_noun_features
from src.util.serializable import Serializable


class TestNounFeaturesDetector(unittest.TestCase):
    def assertNounText_(self, value, expected_texts):
        result = detect_noun_features(value)
        count = 0
        for expected_text in expected_texts:
            noun = result[count]
            result_text = noun.phrase
            self.assertEqual(result_text, expected_text)
            count += 1

    def test_is_defined(self):
        self.assertTrue(detect_noun_features)

    def test_returns_a_list_of_serializable_objects(self):
        result = detect_noun_features("I ran to the beach.")
        self.assertIsInstance(result, list)
        [self.assertIsInstance(noun, Serializable) for noun in result]

    def test_true_positive(self):
        self.assertNounText_("I ran to you.", ["I", "you"])
        self.assertNounText_("You ran to her.", ["You", "her"])
        self.assertNounText_("She ran to him.", ["She", "him"])
        self.assertNounText_("He ran to me.", ["He", "me"])
        value = "The pretty, little girl played with her extravagant dollhouse that her mother bought the day before."
        expected = ["The pretty, little girl", "her extravagant dollhouse", "her mother", "the day"]
        self.assertNounText_(value, expected) 

    def test_true_negative(self):
        self.assertRaises(TypeError, detect_noun_features, 100)
        self.assertRaises(TypeError, detect_noun_features, True)
        self.assertRaises(TypeError, detect_noun_features, ["I ran to the beach."])
        self.assertRaises(TypeError, detect_noun_features, None)
        self.assertRaises(ValueError, detect_noun_features, "")

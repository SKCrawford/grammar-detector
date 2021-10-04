import unittest
from src.features.verb_set.verb import is_verb


class TestVerbVerbValidator(unittest.TestCase):
    def test_are_validators_defined(self):
        self.assertTrue(is_verb)

    def test_verb_validator_true_positive(self):
        verb = {}
        verb["pos"] = "VERB"
        verb["text"] = "run"
        verb["lemmas"] = "run"
        verb["root_lemma"] = "run"
        is_verb(verb)

    def test_verb_validator_true_negative(self):
        self.assertRaises(TypeError, is_verb, 100)
        self.assertRaises(TypeError, is_verb, True)
        self.assertRaises(TypeError, is_verb, ["run"])
        self.assertRaises(TypeError, is_verb, "")
        noun = { "pos": "NOUN" }
        self.assertRaises(ValueError, is_verb, noun)

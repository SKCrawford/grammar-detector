import unittest
from src.features.verb_set.verb import is_verb
from src.util.serializable import Serializable


class TestVerbVerbValidator(unittest.TestCase):
    def test_are_validators_defined(self):
        self.assertTrue(is_verb)

    def test_verb_validator_true_positive(self):
        verb = Serializable()           \
            .set("pos", "VERB")         \
            .set("text", "run")         \
            .set("lemmas", "run")       \
            .set("root_lemma", "run")
        is_verb(verb)

    def test_verb_validator_true_negative(self):
        self.assertRaises(TypeError, is_verb, 100)
        self.assertRaises(TypeError, is_verb, True)
        self.assertRaises(TypeError, is_verb, ["run"])
        self.assertRaises(TypeError, is_verb, "")
        noun = Serializable().set("pos", "NOUN")
        self.assertRaises(ValueError, is_verb, noun)

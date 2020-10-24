import unittest
from src.features.verb_set.transitivity import is_verb_transitivity, is_verb_valency


class TestVerbTransitivityValidator(unittest.TestCase):
    def test_are_validators_defined(self):
        self.assertTrue(is_verb_transitivity)
        self.assertTrue(is_verb_valency)

    def test_transitivity_validator_true_positive(self):
        is_verb_transitivity("impersonal")
        is_verb_transitivity("intransitive")
        is_verb_transitivity("transitive")
        is_verb_transitivity("ditransitive")

        is_verb_valency(0)
        is_verb_valency(1)
        is_verb_valency(2)
        is_verb_valency(3)

    def test_transitivity_validator_true_negative(self):
        self.assertRaises(TypeError, is_verb_transitivity, 100)
        self.assertRaises(TypeError, is_verb_transitivity, True)
        self.assertRaises(TypeError, is_verb_transitivity, ["intransitive"])
        self.assertRaises(ValueError, is_verb_transitivity, "")
        self.assertRaises(ValueError, is_verb_transitivity, "run")

        self.assertRaises(TypeError, is_verb_valency, "0")
        self.assertRaises(TypeError, is_verb_valency, "1")
        self.assertRaises(TypeError, is_verb_valency, "2")
        self.assertRaises(TypeError, is_verb_valency, "3")
        self.assertRaises(TypeError, is_verb_valency, True)
        self.assertRaises(TypeError, is_verb_valency, False)
        self.assertRaises(TypeError, is_verb_valency, [0])
        self.assertRaises(ValueError, is_verb_valency, -1)
        self.assertRaises(ValueError, is_verb_valency, 4)

    def test_transitivity_validator_false_positive(self):
        self.assertRaises(ValueError, is_verb_transitivity, "intransitive".upper())
        self.assertRaises(ValueError, is_verb_transitivity, "intransitive".title())

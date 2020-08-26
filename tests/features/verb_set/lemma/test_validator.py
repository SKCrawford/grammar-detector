import unittest
from src.features.verb_set.lemmas.validator import validate_lemmas


class TestVerbLemmasValidator(unittest.TestCase):
    def test_are_validators_defined(self):
        self.assertTrue(validate_lemmas)

    def test_lemmas_validator_true_positive(self):
        validate_lemmas("have be run")

    def test_lemmas_validator_true_negative(self):
        self.assertRaises(TypeError, validate_lemmas, 100)
        self.assertRaises(TypeError, validate_lemmas, True)
        self.assertRaises(TypeError, validate_lemmas, ["have be run"])
        self.assertRaises(ValueError, validate_lemmas, "")

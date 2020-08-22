import unittest
from src.features.verb_set.verb.validator import validate_verb


class TestVerbVerbValidator(unittest.TestCase):
    def test_are_validators_defined(self):
        self.assertTrue(validate_verb)

    def test_verb_validator_true_positive(self):
        validate_verb("run")
        validate_verb("run away")

    def test_verb_validator_true_negative(self):
        self.assertRaises(TypeError, validate_verb, 100)
        self.assertRaises(TypeError, validate_verb, True)
        self.assertRaises(TypeError, validate_verb, ["run"])
        self.assertRaises(ValueError, validate_verb, "")

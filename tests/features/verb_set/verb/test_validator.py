import unittest
from src.features.verb_set.verb import validator


class TestVerbVerbValidator(unittest.TestCase):
    def test_are_validators_defined(self):
        self.assertTrue(validator.validate_verb_feature)
        self.assertTrue(validator._validate_verb_text)

    def test_verb_validator_true_positive(self):
        validator._validate_verb_text("run")
        validator._validate_verb_text("run away")

    def test_verb_validator_true_negative(self):
        self.assertRaises(TypeError, validator._validate_verb_text, 100)
        self.assertRaises(TypeError, validator._validate_verb_text, True)
        self.assertRaises(TypeError, validator._validate_verb_text, ["run"])
        self.assertRaises(ValueError, validator._validate_verb_text, "")

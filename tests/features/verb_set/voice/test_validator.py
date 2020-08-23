import unittest
from src.features.verb_set.voice.validator import validate_voice


class TestVerbgValidator(unittest.TestCase):
    def test_are_validators_defined(self):
        self.assertTrue(validate_voice)

    def test_voice_validator_true_positive(self):
        validate_voice("passive")
        validate_voice("active")

    def test_voice_validator_true_negative(self):
        self.assertRaises(TypeError, validate_voice, 100)
        self.assertRaises(TypeError, validate_voice, True)
        self.assertRaises(TypeError, validate_voice, ["present"])
        self.assertRaises(ValueError, validate_voice, "")
        self.assertRaises(ValueError, validate_voice, "run")

    def test_voice_validator_false_positive(self):
        self.assertRaises(ValueError, validate_voice, "passive".upper())
        self.assertRaises(ValueError, validate_voice, "passive".title())
        self.assertRaises(ValueError, validate_voice, "pass")
        self.assertRaises(ValueError, validate_voice, "act")

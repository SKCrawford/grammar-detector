import unittest
from src.features.verb_set.voice import is_verb_voice


class TestVerbVoiceValidator(unittest.TestCase):
    def test_are_validators_defined(self):
        self.assertTrue(is_verb_voice)
        self.assertTrue(is_verb_voice)

    def test_voice_validator_true_positive(self):
        is_verb_voice("passive")
        is_verb_voice("active")

    def test_voice_validator_true_negative(self):
        self.assertRaises(TypeError, is_verb_voice, 100)
        self.assertRaises(TypeError, is_verb_voice, True)
        self.assertRaises(TypeError, is_verb_voice, ["present"])
        self.assertRaises(ValueError, is_verb_voice, "")
        self.assertRaises(ValueError, is_verb_voice, "run")

    def test_voice_validator_false_positive(self):
        self.assertRaises(ValueError, is_verb_voice, "passive".upper())
        self.assertRaises(ValueError, is_verb_voice, "passive".title())
        self.assertRaises(ValueError, is_verb_voice, "pass")
        self.assertRaises(ValueError, is_verb_voice, "act")

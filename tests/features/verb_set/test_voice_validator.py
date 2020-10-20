import unittest


@unittest.skip("TODO needs major updates")
class TestVerbVoiceValidator(unittest.TestCase):
    def test_are_validators_defined(self):
        self.assertTrue(validator._validate_voice)
        self.assertTrue(validator._validate_voice)

    def test_voice_validator_true_positive(self):
        validator._validate_voice("passive")
        validator._validate_voice("active")

    def test_voice_validator_true_negative(self):
        self.assertRaises(TypeError, validator._validate_voice, 100)
        self.assertRaises(TypeError, validator._validate_voice, True)
        self.assertRaises(TypeError, validator._validate_voice, ["present"])
        self.assertRaises(ValueError, validator._validate_voice, "")
        self.assertRaises(ValueError, validator._validate_voice, "run")

    def test_voice_validator_false_positive(self):
        self.assertRaises(ValueError, validator._validate_voice, "passive".upper())
        self.assertRaises(ValueError, validator._validate_voice, "passive".title())
        self.assertRaises(ValueError, validator._validate_voice, "pass")
        self.assertRaises(ValueError, validator._validate_voice, "act")

import unittest
from src.features.verb_set.validator import validate_verb_feature_set


class TestVerbFeatureSetValidator(unittest.TestCase):
    def test_are_validators_defined(self):
        self.assertTrue(validator._validate_verb)
        self.assertTrue(validator._validate_tense)
        self.assertTrue(validator._validate_aspect)

    def test_verb_validator_true_positive(self):
        validator._validate_verb("run")
        validator._validate_verb("run away")

    def test_verb_validator_true_negative(self):
        self.assertRaises(TypeError, validator._validate_verb, 100)
        self.assertRaises(TypeError, validator._validate_verb, True)
        self.assertRaises(TypeError, validator._validate_verb, ["run"])
        self.assertRaises(ValueError, validator._validate_verb, "")

    def test_tense_validator_true_positive(self):
        validator._validate_tense("present")
        validator._validate_tense("past")
        validator._validate_tense("future")

    def test_tense_validator_false_positive(self):
        self.assertRaises(ValueError, validator._validate_tense, "present".upper())
        self.assertRaises(ValueError, validator._validate_tense, "present".title())
        self.assertRaises(ValueError, validator._validate_tense, "pst")
        self.assertRaises(ValueError, validator._validate_tense, "pres")
        self.assertRaises(ValueError, validator._validate_tense, "fut")

    def test_tense_validator_true_negative(self):
        self.assertRaises(TypeError, validator._validate_tense, 100)
        self.assertRaises(TypeError, validator._validate_tense, True)
        self.assertRaises(TypeError, validator._validate_tense, ["run"])
        self.assertRaises(ValueError, validator._validate_tense, "")
        self.assertRaises(ValueError, validator._validate_tense, "run")

    def test_aspect_validator_true_positive(self):
        validator._validate_aspect("simple")
        validator._validate_aspect("perfect")
        validator._validate_aspect("continuous")
        validator._validate_aspect("perfect continuous")

    def test_aspect_validator_true_negative(self):
        self.assertRaises(TypeError, validator._validate_aspect, 100)
        self.assertRaises(TypeError, validator._validate_aspect, True)
        self.assertRaises(TypeError, validator._validate_aspect, ["run"])
        self.assertRaises(ValueError, validator._validate_aspect, "")
        self.assertRaises(ValueError, validator._validate_aspect, "run")

    def test_aspect_validator_false_positive(self):
        self.assertRaises(ValueError, validator._validate_aspect, "simple".upper())
        self.assertRaises(ValueError, validator._validate_aspect, "simple".title())
        self.assertRaises(ValueError, validator._validate_aspect, "simp")
        self.assertRaises(ValueError, validator._validate_aspect, "perf")
        self.assertRaises(ValueError, validator._validate_aspect, "cont")
        self.assertRaises(ValueError, validator._validate_aspect, "perf cont")

import unittest
from src.features.verb_set.tense_aspect.validator import validate_aspect, validate_tense


class TestVerbTenseAspectValidator(unittest.TestCase):
    def test_are_validators_defined(self):
        self.assertTrue(validate_aspect)
        self.assertTrue(validate_tense)

    def test_tense_validator_true_positive(self):
        validate_tense("present")
        validate_tense("past")
        validate_tense("future")

    def test_tense_validator_true_negative(self):
        self.assertRaises(TypeError, validate_tense, 100)
        self.assertRaises(TypeError, validate_tense, True)
        self.assertRaises(TypeError, validate_tense, ["present"])
        self.assertRaises(ValueError, validate_tense, "")
        self.assertRaises(ValueError, validate_tense, "run")

    def test_tense_validator_false_positive(self):
        self.assertRaises(ValueError, validate_tense, "present".upper())
        self.assertRaises(ValueError, validate_tense, "present".title())
        self.assertRaises(ValueError, validate_tense, "pst")
        self.assertRaises(ValueError, validate_tense, "pres")
        self.assertRaises(ValueError, validate_tense, "fut")

    def test_aspect_validator_true_positive(self):
        validate_aspect("simple")
        validate_aspect("perfect")
        validate_aspect("continuous")
        validate_aspect("perfect continuous")

    def test_aspect_validator_true_negative(self):
        self.assertRaises(TypeError, validate_aspect, 100)
        self.assertRaises(TypeError, validate_aspect, True)
        self.assertRaises(TypeError, validate_aspect, ["run"])
        self.assertRaises(ValueError, validate_aspect, "")
        self.assertRaises(ValueError, validate_aspect, "run")

    def test_aspect_validator_false_positive(self):
        self.assertRaises(ValueError, validate_aspect, "simple".upper())
        self.assertRaises(ValueError, validate_aspect, "simple".title())
        self.assertRaises(ValueError, validate_aspect, "simp")
        self.assertRaises(ValueError, validate_aspect, "perf")
        self.assertRaises(ValueError, validate_aspect, "cont")
        self.assertRaises(ValueError, validate_aspect, "perf cont")

import unittest
from src.features.verb_set.tense_aspect import is_verb_aspect, is_verb_tense


class TestVerbTenseAspectValidator(unittest.TestCase):
    def test_are_validators_defined(self):
        self.assertTrue(is_verb_aspect)
        self.assertTrue(is_verb_tense)

    def test_tense_validator_true_positive(self):
        is_verb_tense("present")
        is_verb_tense("past")
        is_verb_tense("future")

    def test_tense_validator_true_negative(self):
        self.assertRaises(TypeError, is_verb_tense, 100)
        self.assertRaises(TypeError, is_verb_tense, True)
        self.assertRaises(TypeError, is_verb_tense, ["present"])
        self.assertRaises(ValueError, is_verb_tense, "")
        self.assertRaises(ValueError, is_verb_tense, "run")

    def test_tense_validator_false_positive(self):
        self.assertRaises(ValueError, is_verb_tense, "present".upper())
        self.assertRaises(ValueError, is_verb_tense, "present".title())
        self.assertRaises(ValueError, is_verb_tense, "pst")
        self.assertRaises(ValueError, is_verb_tense, "pres")
        self.assertRaises(ValueError, is_verb_tense, "fut")

    def test_aspect_validator_true_positive(self):
        is_verb_aspect("simple")
        is_verb_aspect("perfect")
        is_verb_aspect("continuous")
        is_verb_aspect("perfect continuous")

    def test_aspect_validator_true_negative(self):
        self.assertRaises(TypeError, is_verb_aspect, 100)
        self.assertRaises(TypeError, is_verb_aspect, True)
        self.assertRaises(TypeError, is_verb_aspect, ["run"])
        self.assertRaises(ValueError, is_verb_aspect, "")
        self.assertRaises(ValueError, is_verb_aspect, "run")

    def test_aspect_validator_false_positive(self):
        self.assertRaises(ValueError, is_verb_aspect, "simple".upper())
        self.assertRaises(ValueError, is_verb_aspect, "simple".title())
        self.assertRaises(ValueError, is_verb_aspect, "simp")
        self.assertRaises(ValueError, is_verb_aspect, "perf")
        self.assertRaises(ValueError, is_verb_aspect, "cont")
        self.assertRaises(ValueError, is_verb_aspect, "perf cont")

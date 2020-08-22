import unittest
from src.features.verb_set.validator import validate_verb_feature_set
from src.features.verb_set.model import VerbFeatureSet


class TestVerbFeatureSetValidator(unittest.TestCase):
    def test_are_validators_defined(self):
        self.assertTrue(validate_verb_feature_set)

    def test_verb_validator_true_positive(self):
        f_set = VerbFeatureSet()
        validate_verb_feature_set(f_set)
        f_set.verb = "had been running"
        f_set.tense = "past"
        f_set.aspect = "perfect continuous"
        validate_verb_feature_set(f_set)

    def test_verb_validator_true_negative(self):
        self.assertRaises(TypeError, validate_verb_feature_set, "run")
        self.assertRaises(TypeError, validate_verb_feature_set, 100)
        self.assertRaises(TypeError, validate_verb_feature_set, True)
        self.assertRaises(TypeError, validate_verb_feature_set, ["run"])

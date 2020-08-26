import unittest
from src.features.noun_set.model import NounFeatureSet
from src.features.noun_set.validator import validate_noun_feature_set


class TestNounFeatureSetValidator(unittest.TestCase):
    def test_are_validators_defined(self):
        self.assertTrue(validate_noun_feature_set)

    def test_noun_validator_true_positive(self):
        f_set = NounFeatureSet()
        validate_noun_feature_set(f_set)

    def test_noun_validator_true_negative(self):
        self.assertRaises(TypeError, validate_noun_feature_set, "run")
        self.assertRaises(TypeError, validate_noun_feature_set, 100)
        self.assertRaises(TypeError, validate_noun_feature_set, True)
        self.assertRaises(TypeError, validate_noun_feature_set, ["run"])

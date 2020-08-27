import unittest
from src.features.noun_set.model import NounFeatureSet
from src.features.noun_set import validator


class TestNounFeatureSetValidator(unittest.TestCase):
    def test_are_validators_defined(self):
        self.assertTrue(validator.validate_noun_feature_set)

    def test_noun_validator_true_positive(self):
        f_set = NounFeatureSet()
        validator.validate_noun_feature_set(f_set)

    def test_noun_validator_true_negative(self):
        self.assertRaises(TypeError, validator.validate_noun_feature_set, "run")
        self.assertRaises(TypeError, validator.validate_noun_feature_set, 100)
        self.assertRaises(TypeError, validator.validate_noun_feature_set, True)
        self.assertRaises(TypeError, validator.validate_noun_feature_set, ["run"])

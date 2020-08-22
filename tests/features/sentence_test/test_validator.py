import unittest
from src.features.sentence_set import validator
from src.features.sentence_set.model import SentenceFeatureSet
from src.features.verb_set.model import VerbFeatureSet


class TestSentenceFeatureSetValidator(unittest.TestCase):
    def test_are_validators_defined(self):
        self.assertTrue(validator.validate_sentence_feature_set)
        self.assertTrue(validator._validate_feature_set)
        self.assertTrue(validator._validate_sentence)

    def test_feature_set_validator_true_positive(self):
        f_set = SentenceFeatureSet()
        self.assertIsInstance(f_set, SentenceFeatureSet)
        self.assertTrue(f_set)

    def test_feature_set_validator_true_negative(self):
        self.assertRaises(TypeError, validator._validate_feature_set, "run")
        self.assertRaises(TypeError, validator._validate_feature_set, 100)
        self.assertRaises(TypeError, validator._validate_feature_set, True)
        self.assertRaises(TypeError, validator._validate_feature_set, ["run"])

    def test_sentence_validator_true_positive(self):
        validator._validate_sentence("I am a test.")
        validator._validate_sentence("Zounds!")

    def test_sentence_validator_true_negative(self):
        self.assertRaises(TypeError, validator._validate_sentence, 100)
        self.assertRaises(TypeError, validator._validate_sentence, True)
        self.assertRaises(TypeError, validator._validate_sentence, ["run"])

    def test_sentence_validator_false_positive(self):
        self.assertRaises(ValueError, validator._validate_sentence, "")

import unittest
from src.features.verb_set.lemma.validator import validate_lemma_phrase


class TestVerbLemmaPhraseValidator(unittest.TestCase):
    def test_are_validators_defined(self):
        self.assertTrue(validate_lemma_phrase)

    def test_lemmas_phrase_validator_true_positive(self):
        validate_lemma_phrase("have be run")

    def test_lemmas_phrase_validator_true_negative(self):
        self.assertRaises(TypeError, validate_lemma_phrase, 100)
        self.assertRaises(TypeError, validate_lemma_phrase, True)
        self.assertRaises(TypeError, validate_lemma_phrase, ["have be run"])
        self.assertRaises(ValueError, validate_lemma_phrase, "")

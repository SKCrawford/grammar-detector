import unittest
from src.features.noun_set.noun.validator import validate_noun
from src.features.noun_set.noun.model import NounFeature


class TestNounValidator(unittest.TestCase):
    def test_are_validators_defined(self):
        self.assertTrue(validate_noun)

    def test_noun_validator_true_positive(self):
        noun = NounFeature()
        noun.text = "the books"
        noun.lemmas = "the book"
        noun.root_lemma = "book"
        validate_noun(noun)

    def test_noun_validator_true_negative(self):
        self.assertRaises(TypeError, validate_noun, "book")
        self.assertRaises(TypeError, validate_noun, 100)
        self.assertRaises(TypeError, validate_noun, True)
        self.assertRaises(TypeError, validate_noun, [NounFeature()])

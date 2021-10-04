import unittest
from src.features.noun_set.noun import is_noun


class TestNounValidator(unittest.TestCase):
    def test_are_validators_defined(self):
        self.assertTrue(is_noun)

    def test_noun_validator_true_positive(self):
        noun = {}
        noun["pos"] = "NOUN"
        noun["text"] = "the books"
        noun["lemmas"] = "the book"
        noun["root_lemma"] = "book"
        is_noun(noun)

    def test_noun_validator_true_negative(self):
        self.assertRaises(TypeError, is_noun, "book")
        self.assertRaises(TypeError, is_noun, 100)
        self.assertRaises(TypeError, is_noun, True)
        self.assertRaises(TypeError, is_noun, [{}])

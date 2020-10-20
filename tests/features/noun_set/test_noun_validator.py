import unittest


@unittest.skip("TODO needs major updates")
class TestNounValidator(unittest.TestCase):
    def test_are_validators_defined(self):
        self.assertTrue(validator.validate_noun_feature)

    def test_noun_validator_true_positive(self):
        noun = NounFeature()
        noun.text = "the books"
        noun.lemmas = "the book"
        noun.root_lemma = "book"
        validator.validate_noun_feature(noun)

    def test_noun_validator_true_negative(self):
        self.assertRaises(TypeError, validator.validate_noun_feature, "book")
        self.assertRaises(TypeError, validator.validate_noun_feature, 100)
        self.assertRaises(TypeError, validator.validate_noun_feature, True)
        self.assertRaises(TypeError, validator.validate_noun_feature, [NounFeature()])

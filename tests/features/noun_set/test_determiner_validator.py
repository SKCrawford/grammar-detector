import unittest


def is_noun_determiner(determiner):
    pass


def is_noun_determiner_type(determiner_type):
    pass


class TestNounPersonValidator(unittest.TestCase):
    def test_are_validators_defined(self):
        self.assertTrue(is_noun_determiner)
        self.assertTrue(is_noun_determiner_type)

    def test_person_validator_true_positive(self):
        is_noun_determiner("a")
        is_noun_determiner("an")
        is_noun_determiner("the")
        is_noun_determiner(None)

        is_noun_determiner_type("indefinite")
        is_noun_determiner_type("definite")
        is_noun_determiner_type("other")
        is_noun_determiner_type("none")

    def test_person_validator_true_negative(self):
        self.assertRaises(TypeError, is_noun_determiner, 100)
        self.assertRaises(TypeError, is_noun_determiner, True)
        self.assertRaises(TypeError, is_noun_determiner, ["the"])
        self.assertRaises(ValueError, is_noun_determiner, "")
        self.assertRaises(ValueError, is_noun_determiner, "run")

        self.assertRaises(TypeError, is_noun_determiner_type, 100)
        self.assertRaises(TypeError, is_noun_determiner_type, True)
        self.assertRaises(TypeError, is_noun_determiner_type, ["definite"])
        self.assertRaises(ValueError, is_noun_determiner_type, "")
        self.assertRaises(ValueError, is_noun_determiner_type, "run")

    def test_person_validator_false_positive(self):
        self.assertRaises(ValueError, is_noun_determiner, "the".upper())
        self.assertRaises(ValueError, is_noun_determiner, "the".title())

        self.assertRaises(ValueError, is_noun_determiner_type, "definite".upper())
        self.assertRaises(ValueError, is_noun_determiner_type, "definite".title())

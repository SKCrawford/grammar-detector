import unittest
from src.features.noun_set.person import is_noun_person


class TestNounPersonValidator(unittest.TestCase):
    def test_are_validators_defined(self):
        self.assertTrue(is_noun_person)

    def test_person_validator_true_positive(self):
        is_noun_person("1st")
        is_noun_person("2nd")
        is_noun_person("3rd")

    def test_person_validator_true_negative(self):
        self.assertRaises(TypeError, is_noun_person, 100)
        self.assertRaises(TypeError, is_noun_person, True)
        self.assertRaises(TypeError, is_noun_person, ["3rd"])
        self.assertRaises(ValueError, is_noun_person, "")
        self.assertRaises(ValueError, is_noun_person, "run")

    def test_person_validator_false_positive(self):
        self.assertRaises(ValueError, is_noun_person, "3rd".upper())
        self.assertRaises(ValueError, is_noun_person, "3rd".title())
        self.assertRaises(ValueError, is_noun_person, "third".lower())
        self.assertRaises(ValueError, is_noun_person, "third".upper())
        self.assertRaises(ValueError, is_noun_person, "third".title())

import unittest
from src.features.noun_set.person.validator import validate_person


class TestNounPersonValidator(unittest.TestCase):
    def test_are_validators_defined(self):
        self.assertTrue(validate_person)

    def test_person_validator_true_positive(self):
        validate_person("1st")
        validate_person("2nd")
        validate_person("3rd")

    def test_person_validator_true_negative(self):
        self.assertRaises(TypeError, validate_person, 100)
        self.assertRaises(TypeError, validate_person, True)
        self.assertRaises(TypeError, validate_person, ["3rd"])
        self.assertRaises(ValueError, validate_person, "")
        self.assertRaises(ValueError, validate_person, "run")

    def test_person_validator_false_positive(self):
        self.assertRaises(ValueError, validate_person, "3rd".upper())
        self.assertRaises(ValueError, validate_person, "3rd".title())
        self.assertRaises(ValueError, validate_person, "third".lower())
        self.assertRaises(ValueError, validate_person, "third".upper())
        self.assertRaises(ValueError, validate_person, "third".title())

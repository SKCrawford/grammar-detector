import unittest


@unittest.skip("TODO needs major updates")
class TestNounPersonValidator(unittest.TestCase):
    def test_are_validators_defined(self):
        self.assertTrue(validator.validate_person_feature)
        self.assertTrue(validator._validate_person)

    def test_person_validator_true_positive(self):
        validator._validate_person("1st")
        validator._validate_person("2nd")
        validator._validate_person("3rd")

    def test_person_validator_true_negative(self):
        self.assertRaises(TypeError, validator._validate_person, 100)
        self.assertRaises(TypeError, validator._validate_person, True)
        self.assertRaises(TypeError, validator._validate_person, ["3rd"])
        self.assertRaises(ValueError, validator._validate_person, "")
        self.assertRaises(ValueError, validator._validate_person, "run")

    def test_person_validator_false_positive(self):
        self.assertRaises(ValueError, validator._validate_person, "3rd".upper())
        self.assertRaises(ValueError, validator._validate_person, "3rd".title())
        self.assertRaises(ValueError, validator._validate_person, "third".lower())
        self.assertRaises(ValueError, validator._validate_person, "third".upper())
        self.assertRaises(ValueError, validator._validate_person, "third".title())

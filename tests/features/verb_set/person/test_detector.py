import unittest
from src.features.verb_set.person.detector import detect_verb_person


class TestVerbPersonDetector(unittest.TestCase):
    def assertPerson_(self, value, expected_person):
        result = detect_verb_person(value)
        self.assertEqual(result, expected_person)

    def test_is_defined(self):
        self.assertTrue(detect_verb_person)

    def test_returns_a_string(self):
        person = detect_verb_person("She is running for President.")
        self.assertIsInstance(person, str)

    def test_true_positive(self):
        self.assertPerson_("I am running for President.", "1st")
        self.assertPerson_("We are running for President.", "1st")
        self.assertPerson_("You are running for President.", "2nd")
        self.assertPerson_("She is running for President.", "3rd")
        self.assertPerson_("They are running for President.", "3rd")
        self.assertPerson_("Amy is running for President.", "3rd")
        self.assertPerson_("Biden and Harris are running for President.", "3rd")


    def test_true_negative(self):
        self.assertRaises(TypeError, detect_verb_person, 100)
        self.assertRaises(TypeError, detect_verb_person, True)
        self.assertRaises(TypeError, detect_verb_person, ["She is running for President."])
        self.assertRaises(TypeError, detect_verb_person, None)
        self.assertRaises(ValueError, detect_verb_person, "")
import unittest
from src.features.verb_set.tense_aspect import extract_tense_aspect


class TestTenseAspectExtractor(unittest.TestCase):
    def test_true_positive(self):
        (tense, aspect) = extract_tense_aspect("present simple")
        self.assertEqual(tense, "present")
        self.assertEqual(aspect, "simple")

        (tense, aspect) = extract_tense_aspect("past simple")
        self.assertEqual(tense, "past")
        self.assertEqual(aspect, "simple")

        (tense, aspect) = extract_tense_aspect("future simple will")
        self.assertEqual(tense, "future")
        self.assertEqual(aspect, "simple")

        (tense, aspect) = extract_tense_aspect("future simple be-going-to")
        self.assertEqual(tense, "future")
        self.assertEqual(aspect, "simple")

        (tense, aspect) = extract_tense_aspect("present perfect")
        self.assertEqual(tense, "present")
        self.assertEqual(aspect, "perfect")

        (tense, aspect) = extract_tense_aspect("present continuous")
        self.assertEqual(tense, "present")
        self.assertEqual(aspect, "continuous")

        (tense, aspect) = extract_tense_aspect("present perfect continuous")
        self.assertEqual(tense, "present")
        self.assertEqual(aspect, "perfect continuous")

        (tense, aspect) = extract_tense_aspect("present perfect continuous 3rd")
        self.assertEqual(tense, "present")
        self.assertEqual(aspect, "perfect continuous")

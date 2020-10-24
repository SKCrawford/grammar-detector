import unittest
from src.features.noun_set import detect_noun_determiner


class TestNounDeterminerDetector(unittest.TestCase):
    def assertDeterminer_(self, value, expected_determiner, expected_type):
        (result_determiner, result_type) = detect_noun_determiner(value)
        self.assertEqual(result_determiner, expected_determiner)
        self.assertEqual(result_type, expected_type)

    def test_is_defined(self):
        self.assertTrue(detect_noun_determiner)

    def test_returns_a_tuple_of_strings(self):
        (determiner, determiner_type) = detect_noun_determiner("the book")
        self.assertIsInstance(determiner, str)
        self.assertIsInstance(determiner_type, str)

    def test_true_positive(self):
        self.assertDeterminer_("the book", "the", "definite")
        self.assertDeterminer_("the green book", "the", "definite")
        self.assertDeterminer_("the incredibly green book", "the", "definite")
        self.assertDeterminer_("the book that was on a shelf", "the", "definite")

        self.assertDeterminer_("a book", "a", "indefinite")
        self.assertDeterminer_("a green book", "a", "indefinite")
        self.assertDeterminer_("a hideously green book", "a", "indefinite")
        self.assertDeterminer_("a book that was on a shelf", "a", "indefinite")

        self.assertDeterminer_("an apple", "an", "indefinite")
        self.assertDeterminer_("an ugly apple", "an", "indefinite")
        self.assertDeterminer_("an incredibly green apple", "an", "indefinite")
        self.assertDeterminer_("an apple that was on a shelf", "an", "indefinite")

        self.assertDeterminer_("apple", None, "none")
        self.assertDeterminer_("ugly apple", None, "none")
        self.assertDeterminer_("incredibly green apple", None, "none")
        self.assertDeterminer_("apple that was on a shelf", None, "none")

    def test_true_negative(self):
        self.assertRaises(TypeError, detect_noun_determiner, 100)
        self.assertRaises(TypeError, detect_noun_determiner, True)
        self.assertRaises(TypeError, detect_noun_determiner, ["the book"])
        self.assertRaises(TypeError, detect_noun_determiner, None)
        self.assertRaises(ValueError, detect_noun_determiner, "")

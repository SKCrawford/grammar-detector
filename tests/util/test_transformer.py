import unittest
from src.util.transformer import remove_ordinals, split_words_into_first_and_rest


class TestRemoveCardinalsTransformer(unittest.TestCase):
    def test_is_defined(self):
        self.assertTrue(remove_ordinals)

    def test_alphanumeric_lower(self):
        result = remove_ordinals("present continuous 3rd".lower())
        expected = "present continuous".lower()
        self.assertEqual(result, expected)

    def test_alphanumeric_upper(self):
        result = remove_ordinals("present continuous 3rd".upper())
        expected = "present continuous".upper()
        self.assertEqual(result, expected)

    def test_alphanumeric_title(self):
        result = remove_ordinals("present continuous 3rd".title())
        expected = "present continuous".title()
        self.assertEqual(result, expected)

    def test_alpha_lower(self):
        result = remove_ordinals("present continuous third".lower())
        expected = "present continuous".lower()
        self.assertEqual(result, expected)

    def test_alpha_upper(self):
        result = remove_ordinals("present continuous third".upper())
        expected = "present continuous".upper()
        self.assertEqual(result, expected)

    def test_alpha_title(self):
        result = remove_ordinals("present continuous third".title())
        expected = "present continuous".title()
        self.assertEqual(result, expected)

    def test_name(self):
        result = remove_ordinals("Lupin the Third")
        expected = "Lupin the"
        self.assertEqual(result, expected)

    def test_identical(self):
        result = remove_ordinals("present continuous")
        expected = "present continuous"
        self.assertEqual(result, expected)

    def test_reject_int(self):
        self.assertRaises(TypeError, split_words_into_first_and_rest, 100)

    def test_reject_bool(self):
        self.assertRaises(TypeError, split_words_into_first_and_rest, True)

    def test_reject_list(self):
        self.assertRaises(TypeError, split_words_into_first_and_rest, ["present continuous 3rd"])

    def test_reject_none(self):
        self.assertRaises(TypeError, split_words_into_first_and_rest, None)

class TestSplitWordsIntoFirstAndRestTransformer(unittest.TestCase):
    def test_is_defined(self):
        self.assertTrue(split_words_into_first_and_rest)

    def test_alphanumeric_lower(self):
        result = split_words_into_first_and_rest("present continuous 3rd".lower())
        expected = ("present".lower(), "continuous 3rd".lower())
        self.assertEqual(result, expected)

    def test_alphanumeric_upper(self):
        result = split_words_into_first_and_rest("present continuous 3rd".upper())
        expected = ("present".upper(), "continuous 3rd".upper())
        self.assertEqual(result, expected)

    def test_alphanumeric_title(self):
        result = split_words_into_first_and_rest("present continuous 3rd".title())
        expected = ("present".title(), "continuous 3rd".title())
        self.assertEqual(result, expected)

    def test_alpha_lower(self):
        result = split_words_into_first_and_rest("present continuous third".lower())
        expected = ("present".lower(), "continuous third".lower())
        self.assertEqual(result, expected)

    def test_alpha_upper(self):
        result = split_words_into_first_and_rest("present continuous third".upper())
        expected = ("present".upper(), "continuous third".upper())
        self.assertEqual(result, expected)

    def test_alpha_title(self):
        result = split_words_into_first_and_rest("present continuous third".title())
        expected = ("present".title(), "continuous third".title())
        self.assertEqual(result, expected)

    def test_name(self):
        result = split_words_into_first_and_rest("Lupin the Third")
        expected = ("Lupin", "the Third")
        self.assertEqual(result, expected)

    def test_reject_int(self):
        self.assertRaises(TypeError, split_words_into_first_and_rest, 100)

    def test_reject_bool(self):
        self.assertRaises(TypeError, split_words_into_first_and_rest, True)

    def test_reject_list(self):
        self.assertRaises(TypeError, split_words_into_first_and_rest, ["present continuous 3rd"])

    def test_reject_none(self):
        self.assertRaises(TypeError, split_words_into_first_and_rest, None)

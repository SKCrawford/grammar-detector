import unittest
from src.core.pattern.model import Pattern, PatternSet


class TestPatternModel(unittest.TestCase):
    def test_is_defined(self):
        self.assertTrue(Pattern)

    def test_is_constructable(self):
        name = "test pattern"
        tokens = [{ "TAG": "VB" }]
        self.assertTrue(Pattern(name, tokens))

    def test_has_name(self):
        name = "custom pattern name"
        tokens = [{ "TAG": "VB" }]
        pattern = Pattern(name, tokens)
        self.assertIsInstance(pattern.name, str)
        self.assertEqual(pattern.name, name)

    def test_has_default_name(self):
        name = None
        tokens = [{ "TAG": "VB" }]
        pattern = Pattern(name, tokens)
        self.assertIsInstance(pattern.name, str)
        self.assertTrue(pattern.name)

        name = ""
        tokens = [{ "TAG": "VB" }]
        pattern = Pattern(name, tokens)
        self.assertIsInstance(pattern.name, str)
        self.assertTrue(pattern.name)

    def test_has_tokens(self):
        name = "custom pattern name"
        tokens = [{ "TAG": "VB" }]
        pattern = Pattern(name, tokens)
        self.assertIsInstance(pattern.tokens, list)
        self.assertEqual(pattern.tokens, tokens)



class TestPatternSetModel(unittest.TestCase):
    test_pattern_set = None

    def _create_testing_pattern_set(self):
        pattern_1_name = "pattern 1"
        pattern_1_tokens = [{ "POS": "NOUN" }, { "POS": "VERB", "DEP": "ROOT" }]
        pattern_2_name = "pattern 2"
        pattern_2_tokens = [{ "POS": "ADJ" }, { "POS": "NOUN" }]
        pattern_3_name = "pattern 3"
        pattern_3_tokens = [{ "POS": "ADV" }, { "POS": "VERB" }]
        pattern_set = PatternSet("phrases")
        pattern_set.create(pattern_1_name, pattern_1_tokens)
        pattern_set.create(pattern_2_name, pattern_2_tokens)
        pattern_set.create(pattern_3_name, pattern_3_tokens)
        return pattern_set

    def setUp(self):
        self.test_pattern_set = self._create_testing_pattern_set()

    def test_is_defined(self):
        self.assertTrue(PatternSet)

    def test_is_constructable(self):
        name = "test pattern set name"
        self.assertTrue(PatternSet(name))

    def test_has_name(self):
        name = "phrases"
        pattern_set = PatternSet(name)
        self.assertIsInstance(pattern_set.name, str)
        self.assertEqual(pattern_set.name, name)

    def test_has_default_name(self):
        name = None
        pattern_set = PatternSet(name)
        self.assertIsInstance(pattern_set.name, str)
        self.assertTrue(pattern_set.name)

        name = ""
        pattern_set = PatternSet(name)
        self.assertIsInstance(pattern_set.name, str)
        self.assertTrue(pattern_set.name)

    def test_creates_patterns(self):
        result = len(self.test_pattern_set._patterns)
        expected = 3
        self.assertEqual(result, expected)

    def test_finds_a_pattern(self):
        result = self.test_pattern_set.find("pattern 2").name
        expected = "pattern 2"
        self.assertEqual(result, expected)

    def test_finds_all_patterns(self):
        result = [pattern.name for pattern in self.test_pattern_set.find_all()]
        expected = ["pattern 1", "pattern 2", "pattern 3"]
        self.assertListEqual(result, expected)

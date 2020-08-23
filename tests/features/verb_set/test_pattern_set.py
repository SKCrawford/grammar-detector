import unittest
from src.core.pattern.model import PatternSet
from src.features.verb_set.pattern_set import create_verb_feature_set_pattern_set


class TestVerbFeatureSetPatternSet(unittest.TestCase):
    pattern_set = None

    def setUp(self):
        self.pattern_set = create_verb_feature_set_pattern_set()

    def test_is_defined(self):
        self.assertTrue(create_verb_feature_set_pattern_set)

    def test_is_the_right_type(self):
        self.assertIsInstance(self.pattern_set, PatternSet)
        self.assertTrue(self.pattern_set)

    def test_has_at_least_1_pattern(self):
        result = len(self.pattern_set.find_all())
        self.assertGreater(result, 0)

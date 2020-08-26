import unittest
from src.core.pattern.matcher import PatternSetMatcher
from src.features.verb_set.tense_aspect.matcher import create_verb_tense_aspect_matcher


class TestVerbTenseAspectMatcher(unittest.TestCase):
    def test_is_matcher_creator_defined(self):
        self.assertTrue(create_verb_tense_aspect_matcher)

    def test_is_matcher_constructed(self):
        self.assertIsInstance(create_verb_tense_aspect_matcher(), PatternSetMatcher)

    def test_constructs_new_instances(self):
        matcher1 = create_verb_tense_aspect_matcher()
        matcher2 = create_verb_tense_aspect_matcher()
        self.assertIsNot(matcher1, matcher2)
        self.assertNotEqual(hex(id(matcher1)), hex(id(matcher2)))
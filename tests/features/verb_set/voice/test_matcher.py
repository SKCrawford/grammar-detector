import unittest
from src.core.pattern.matcher import PatternSetMatcher
from src.features.verb_set.voice.matcher import create_verb_voice_matcher


class TestVerbVoiceMatcher(unittest.TestCase):
    def test_is_matcher_creator_defined(self):
        self.assertTrue(create_verb_voice_matcher)

    def test_is_matcher_constructed(self):
        self.assertIsInstance(create_verb_voice_matcher(), PatternSetMatcher)

    def test_constructs_new_instances(self):
        matcher1 = create_verb_voice_matcher()
        matcher2 = create_verb_voice_matcher()
        self.assertIsNot(matcher1, matcher2)
        self.assertNotEqual(hex(id(matcher1)), hex(id(matcher2)))

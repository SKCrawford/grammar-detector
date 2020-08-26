import unittest
from src.core.pattern.matcher import PatternSetMatcher
from src.features.noun_set.person.matcher import create_noun_person_matcher


class TestNounPersonMatcher(unittest.TestCase):
    def test_is_matcher_creator_defined(self):
        self.assertTrue(create_noun_person_matcher)

    def test_is_matcher_constructed(self):
        self.assertIsInstance(create_noun_person_matcher(), PatternSetMatcher)

    def test_constructs_new_instances(self):
        matcher1 = create_noun_person_matcher()
        matcher2 = create_noun_person_matcher()
        self.assertIsNot(matcher1, matcher2)
        self.assertNotEqual(hex(id(matcher1)), hex(id(matcher2)))

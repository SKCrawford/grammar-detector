import unittest
from src.core.pattern.model import PatternSet
from src.features.noun_set.person.pattern_set import create_noun_person_pattern_set


class TestNounPersonPatternSet(unittest.TestCase):
    def test_is_pattern_set_creator_defined(self):
        self.assertTrue(create_noun_person_pattern_set)

    def test_is_pattern_set_constructed(self):
        self.assertIsInstance(create_noun_person_pattern_set(), PatternSet)

    def test_constructs_new_instances(self):
        pattern_set1 = create_noun_person_pattern_set()
        pattern_set2 = create_noun_person_pattern_set()
        self.assertIsNot(pattern_set1, pattern_set2)
        self.assertNotEqual(hex(id(pattern_set1)), hex(id(pattern_set2)))

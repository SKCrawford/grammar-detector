import unittest
from spacy import load
from spacy.matcher import Matcher
from src.core.pattern.model import PatternSet
from src.core.pattern.matcher import PatternSetMatcher
from src.nlp import nlp


def create_testing_pattern_set():
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


class TestPatternSetMatcher(unittest.TestCase):
    def test_is_defined(self):
        self.assertTrue(PatternSetMatcher)

    def test_accepts_pattern_set_in_constructor(self):
        p_set = create_testing_pattern_set()
        p_set_matcher = PatternSetMatcher(p_set)
        self.assertTrue(p_set_matcher._pattern_set)
        self.assertIsInstance(p_set_matcher._pattern_set, PatternSet)

    def test_rejects_nlp_in_constructor(self):
        nlp = load("en_core_web_sm")
        self.assertRaises(TypeError, PatternSetMatcher, nlp)

    def test_has_base_matcher_instance(self):
        p_set = create_testing_pattern_set()
        p_set_matcher = PatternSetMatcher(p_set)
        p_set_matcher._load()
        self.assertIsInstance(p_set_matcher._matcher, Matcher)

    def test_creates_a_new_matcher_on_each_construction(self):
        p_set = create_testing_pattern_set()
        p_set_matcher1 = PatternSetMatcher(p_set)
        p_set_matcher2 = PatternSetMatcher(p_set)
        p_set_matcher1._load()
        p_set_matcher2._load()
        self.assertIsNot(p_set_matcher1._matcher, p_set_matcher2._matcher)
        self.assertNotEqual(hex(id(p_set_matcher1._matcher)), hex(id(p_set_matcher2._matcher)))

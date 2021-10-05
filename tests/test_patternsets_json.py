import logging
import unittest
from src.patterns import load_pattern_set, PatternSet
from src.Matcher import Matcher
from settings import PATTERN_SETS_NAMES
from src.extractors import get_doc


logger = logging.getLogger(__name__)


class TestPatternSetJsonTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.pattern_sets = {}
        self.matchers = {}

        for pset_name in PATTERN_SETS_NAMES:
            pattern_set = PatternSet(pset_name)
            self.pattern_sets[pset_name] = pattern_set
            self.matchers[pset_name] = Matcher(pattern_set)

    def test_pattern_set_json_tests(self):
        for pset_key in self.pattern_sets:
            pset = self.pattern_sets[pset_key]
            matcher = self.matchers[pset_key]

            if pset.tests:
                with self.subTest(pset.name):
                    for t in pset.tests:
                        input = get_doc(t["input"])
                        expected_rulenames = t["rulenames"] if "rulenames" in t else []
                        expected_spans = t["spans"] if "spans" in t else []

                        if not expected_rulenames and not expected_spans:
                            err_msg = "The test entry must have at least one of these keys: rulenames, spans"
                            raise KeyError(err_msg)

                        input_type = type(input)
                        if input_type != str:
                            err_msg = f"Expected a string but got a {input_type}"
                            raise TypeError(err_msg)

                        has_many_rulenames = bool(len(expected_rulenames) > 1)
                        has_many_spans = bool(len(expected_spans) > 1)
                        if has_many_rulenames or has_many_spans:
                            if pset.how_many_matches == "ONE":
                                err_msg = f"The pattern set expects only one match, but the test contains multiple rulenames and/or spans"
                                raise ValueError(err_msg)

                        rulenames = []
                        spans = []
                        for (rulename, span, features) in matcher.match(input):
                            rulenames.append(rulename)
                            spans.append(str(span))

                        if expected_rulenames:
                            self.assertListEqual(rulenames, expected_rulenames)
                        if expected_spans:
                            self.assertListEqual(spans, expected_spans)

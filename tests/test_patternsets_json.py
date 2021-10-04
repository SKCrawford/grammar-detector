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
                for test in pset.tests:
                    input = get_doc(test["input"])
                    expected_rulename = test["rulename"] if "rulename" in test else None
                    expected_span = test["span"] if "span" in test else None

                    if not expected_rulename and not expected_span:
                        err_msg = "The test entry must have at least one of these keys: expected_rulename and/or expected_span"
                        raise KeyError(err_msg)

                    (rulename, _, features) = matcher.match(input)
                    span = str(features["span"])

                    if expected_rulename:
                        err_msg = f"'{input}': expected rulename '{expected_rulename}' but got '{rulename}'"
                        self.assertEqual(rulename, expected_rulename, err_msg)

                    if expected_span:
                        err_msg = f"'{input}': expected span '{expected_span}' but got '{span}'"
                        self.assertEqual(span, expected_span, err_msg)

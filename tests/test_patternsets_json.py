import logging
import unittest
from src.patterns import load_pattern_set, PatternSet
from src.Matcher import Matcher
from settings import PATTERN_SETS_NAMES, SettingKeys, SettingValues
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

    # Refactor this horrid mess!!
    def test_pattern_set_json_tests(self):
        for pset_key in self.pattern_sets:
            pset = self.pattern_sets[pset_key]
            matcher = self.matchers[pset_key]

            if pset.tests:
                with self.subTest(pset.name):
                    for t in pset.tests:
                        should_skip = None
                        skip_reason = None
                        try:
                            key = SettingKeys.PSET_TESTS_SKIP.value
                            should_skip = bool(t[key])
                            key = SettingKeys.PSET_TESTS_SKIP_REASON.value
                            skip_reason = str(t[key])
                        except KeyError:
                            should_skip = False
                        except Exception as e:
                            raise e

                        if not should_skip:  # Early exit is impossible
                            input = get_doc(t[SettingKeys.PSET_TESTS_INPUT.value])

                            key = SettingKeys.PSET_TESTS_RULENAMES.value
                            expected_rulenames = t[key] if key in t else []

                            key = SettingKeys.PSET_TESTS_SPANS.value
                            expected_spans = t[key] if key in t else []

                            if not expected_rulenames and not expected_spans:
                                valid_keys = [
                                    SettingKeys.PSET_TESTS_RULENAMES.value,
                                    SettingKeys.PSET_TESTS_SPANS.value,
                                ]
                                err_msg = f"The test entry must have at least one of these keys: {valid_keys}"
                                raise KeyError(err_msg)

                            has_many_rulenames = bool(len(expected_rulenames) > 1)
                            has_many_spans = bool(len(expected_spans) > 1)
                            if has_many_rulenames or has_many_spans:
                                if (
                                    pset.how_many_matches
                                    == SettingValues.HOW_MANY_MATCHES_ONE_MATCH.value
                                ):
                                    err_msg = f"The pattern set expects only one match, but the test contains multiple rulenames and/or spans"
                                    raise ValueError(err_msg)

                            with self.subTest(f"{pset.name}:{input}"):
                                rulenames = []
                                spans = []
                                for (rulename, span, features) in matcher.match(input):
                                    rulenames.append(rulename)
                                    spans.append(str(span))

                                if expected_rulenames:
                                    self.assertListEqual(rulenames, expected_rulenames)
                                if expected_spans:
                                    self.assertListEqual(spans, expected_spans)
                        else:
                            msg = f"Skipping {pset.name} test '{input}': {skip_reason}"
                            print(msg)
                            logger.debug(msg)

import logging
import unittest
from src.patterns import PatternSetLoader
from src.Matcher import Matcher
from settings import PATTERN_SETS_NAMES, SettingKeys, SettingValues
from src.extractors import get_doc


logger = logging.getLogger(__name__)


class TestPatternSetJsonTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.pattern_sets = {}
        self.matchers = {}
        loader = PatternSetLoader()

        for pset_name in PATTERN_SETS_NAMES:
            pattern_set = loader.load(pset_name)
            self.pattern_sets[pset_name] = pattern_set
            self.matchers[pset_name] = Matcher(pattern_set)

    def should_skip_pset(self, pset):
        should_skip = None
        skip_reason = None

        try:
            key = SettingKeys.PSET_META_SKIP.value
            skip_setting = pset.meta[key]
            if type(skip_setting) == bool:
                should_skip = skip_setting
                skip_reason = ""
            elif type(skip_setting) == str:
                should_skip = bool(len(skip_setting))
                skip_reason = skip_setting
            else:
                msg = f"Expected a bool or str but got '{type(skip_setting)}'"
                logger.error(msg)
                raise TypeError(msg)
        except KeyError:
            should_skip = False
            skip_reason = ""
        except Exception as e:
            logger.error(e)
            raise e
        finally:
            return (should_skip, skip_reason)

    def should_skip_test(self, test):
        should_skip = None
        skip_reason = None

        try:
            skip_setting = test[SettingKeys.PSET_TESTS_SKIP.value]
            if type(skip_setting) == bool:
                should_skip = skip_setting
                skip_reason = ""
            elif type(skip_setting) == str:
                should_skip = bool(len(skip_setting))
                skip_reason = skip_setting
            else:
                msg = f"Expected a bool or str but got '{type(skip_setting)}'"
                logger.error(msg)
                raise TypeError(msg)
            return (should_skip, skip_reason)
        except KeyError:
            should_skip = False
            skip_reason = ""
        except Exception as e:
            logger.error(e)
            raise e
        finally:
            return (should_skip, skip_reason)

    def get_input(self, test):
        return get_doc(test[SettingKeys.PSET_TESTS_INPUT.value])

    def get_expected_results(self, test, pset):
        rulenames_key = SettingKeys.PSET_TESTS_RULENAMES.value
        spans_key = SettingKeys.PSET_TESTS_SPANS.value
        expected_rulenames = test[rulenames_key] if rulenames_key in test else []
        expected_spans = test[spans_key] if spans_key in test else []

        # Validate the presence of at least one key containing expected results
        if not expected_rulenames and not expected_spans:
            valid_keys = [rulenames_key, spans_key]
            err_msg = f"The test must have at least one of these keys: {valid_keys}"
            logger.error(err_msg)
            raise KeyError(err_msg)

        # Validate the length of expected results in relation to the expected number of matches
        expects_many_rulenames = bool(len(expected_rulenames) > 1)
        expects_many_spans = bool(len(expected_spans) > 1)
        if expects_many_rulenames or expects_many_spans:
            key = SettingKeys.PSET_META_HOW_MANY_MATCHES.value
            how_many_matches = pset.meta[key]
            one_match = SettingValues.HOW_MANY_MATCHES_ONE_MATCH.value
            if how_many_matches.upper() == one_match.upper():
                err_msg = "The pattern set expects only one match, but the test expects multiple matches"
                logger.error(err_msg)
                raise ValueError(err_msg)
        return (expected_rulenames, expected_spans)

    def run_test(self, test, matcher, pset):
        input = self.get_input(test)

        (should_skip, skip_reason) = self.should_skip_test(test)
        if should_skip:
            msg = f"Skipping patternset '{pset.name}': '{input}'"
            if bool(len(skip_reason)):
                msg = msg + f"({skip_reason})"
                print(msg)
                logger.debug(msg)
            return

        with self.subTest(f"{pset.name}:{input}"):
            (expected_rulenames, expected_spans) = self.get_expected_results(test, pset)

            rulenames = []
            spans = []
            for (rulename, span, features) in matcher.match(input):
                rulenames.append(rulename)
                spans.append(str(span))

            if expected_rulenames:
                self.assertListEqual(rulenames, expected_rulenames)
            if expected_spans:
                self.assertListEqual(spans, expected_spans)

    def run_pset(self, pset, matcher):
        (should_skip, skip_reason) = self.should_skip_pset(pset)
        if should_skip:
            msg = f"Skipping patternset '{pset.name}'"
            if bool(len(skip_reason)):
                msg = msg + f": {skip_reason}"
                print(msg)
                logger.debug(msg)
            return

        if pset.tests:
            with self.subTest(pset.name):
                [self.run_test(test, matcher, pset) for test in pset.tests]

    def test_pattern_set_json_tests(self):
        for pset_key in self.pattern_sets:
            pset = self.pattern_sets[pset_key]
            matcher = self.matchers[pset_key]
            self.run_pset(pset, matcher)

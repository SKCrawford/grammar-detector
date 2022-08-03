import unittest
from logging import getLogger
from settings import pattern_set_config
from src.detectors import detect_feature
from src.loaders import YamlLoader
from src.matchers import PatternSetMatcher
from src.patterns import PatternSet, PatternSetRepository
from src.utils import get_doc


logger = getLogger(__name__)


class TestDetectorTests(unittest.TestCase):
    """The test suite for the YAML patternset configuration files. When running this suite via `$ python -m unittest`, the tests in the YAML patternset configuration files will be run. This allows for the patterns to be tested by running the specified input then comparing the expected/actual matching rulenames and text spans. This information can then be used to make improvements to, expand upon, and battle harden the YAML patternset configuration files. As a general rule, when patternsets do not behave as expected, the solution is to improve the patterns or add new variations of existing patterns. The solution is rarely to add new features via code, so fixing errors in the patterns themselves should be the first step."""

    @classmethod
    def setUpClass(self):
        """Load the patternset configuration files to extract the tests."""
        self.pattern_sets: dict[str, PatternSet] = {}
        file_loader = YamlLoader(pattern_set_config.host_dir_path)
        repo = PatternSetRepository()

        for pset_name in pattern_set_config.names:
            pset_data = file_loader(pset_name)
            pattern_set: PatternSet = repo.create(pset_name, pset_data)
            self.pattern_sets[pattern_set.name] = pattern_set

    def should_skip_pset(self, pset):
        """Determine if the patternset's tests should be skipped. This operates at the patternset level."""
        should_skip = None
        skip_reason = None

        try:
            skip_key = pattern_set_config.keys.prop_str("SKIP_TESTS")
            skip_setting = pset.meta[skip_key]
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

        return (should_skip, skip_reason)

    def should_skip_test(self, test):
        """Determine if the patternset's tests should be skipped. This operates at the test level."""
        should_skip = None
        skip_reason = None

        try:
            skip_key = pattern_set_config.keys.prop_str("TESTS_SKIP")
            skip_setting = test[skip_key]
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

        return (should_skip, skip_reason)

    def get_input(self, test):
        """Extract the input from the test entry."""
        return test[pattern_set_config.keys.prop_str("TESTS_INPUT")]

    def get_expected_results(self, test, pset):
        """Extract the expected rulenames and text spans from the test entry."""
        rulenames_key = pattern_set_config.keys.prop_str("TESTS_RULENAMES")
        spans_key = pattern_set_config.keys.prop_str("TESTS_SPANS")
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
            how_many_key = pattern_set_config.keys.prop_str("HOW_MANY_MATCHES")
            how_many_matches = pset.meta[how_many_key]
            one_match_setting = pattern_set_config.values.prop_str("ONE_MATCH")
            if how_many_matches.upper() == one_match_setting.upper():
                err_msg = "The pattern set expects only one match, but the test expects multiple matches"
                logger.error(err_msg)
                raise ValueError(err_msg)
        return (expected_rulenames, expected_spans)

    def run_test(self, test, pset):
        """The main entrypoint to run an individual test."""
        input = self.get_input(test)

        # Determine if the test should be skipped
        (should_skip, skip_reason) = self.should_skip_test(test)
        if should_skip:
            msg = f"Skipping patternset '{pset.name}': '{input}'"
            if bool(len(skip_reason)):
                msg = msg + f" ({skip_reason})"
                print(msg)
                logger.debug(msg)
            return

        # Extract expected results, run matcher, and compare to actual results
        # Separate each test in a pset using subTest to prevent failures from stopping other tests
        with self.subTest(f"{pset.name}:{input}"):
            (expected_rulenames, expected_spans) = self.get_expected_results(test, pset)
            rulenames = []
            spans = []

            match_sets = detect_feature(input, pset.name)
            for mset in match_sets:
                rulenames.append(mset.best.rulename)
                spans.append(str(mset.best.span))

            if expected_rulenames:
                self.assertListEqual(rulenames, expected_rulenames)
            if expected_spans:
                self.assertListEqual(spans, expected_spans)

    def run_pset(self, pset):
        """The main entrypoint to run all of the tests in a patternset."""
        (should_skip, skip_reason) = self.should_skip_pset(pset)
        if should_skip:
            msg = f"Skipping patternset '{pset.name}'"
            if bool(len(skip_reason)):
                msg = msg + f": {skip_reason}"
                print(msg)
                logger.debug(msg)
            return

        # Separate each pset using subTest to prevent failures from stopping the run
        if pset.tests:
            with self.subTest(pset.name):
                [self.run_test(test, pset) for test in pset.tests]

    def test_pattern_set_json_tests(self):
        """The main entrypoint for the unittest package."""
        for pset_key in self.pattern_sets:
            pset = self.pattern_sets[pset_key]
            self.run_pset(pset)

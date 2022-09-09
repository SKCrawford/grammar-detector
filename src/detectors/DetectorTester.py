from logging import getLogger
from typing import Optional
from unittest import TestCase
from .Detector import Detector
from ..patterns import PatternSet


logger = getLogger(__name__)


class DetectorTester(TestCase):
    def _should_skip_pset(self, pattern_set: PatternSet) -> tuple[bool, str]:
        """Determine if the patternset's tests should be skipped. This operates at the patternset level."""
        should_skip: Optional[bool] = None
        skip_reason: Optional[str] = None

        try:
            skip_setting: str = pattern_set.skip_tests
            should_skip = bool(len(skip_setting))
            skip_reason = skip_setting
        except KeyError:
            should_skip = False
            skip_reason = ""
        except Exception as e:
            raise e

        return (should_skip, skip_reason)

    def _should_skip_test(self, test) -> tuple[bool, str]:
        """Determine if the patternset's tests should be skipped. This operates at the test level."""
        should_skip: Optional[bool] = None
        skip_reason: Optional[str] = None

        try:
            skip_setting: str = test["skip"]
            should_skip = bool(len(skip_setting))
            skip_reason = skip_setting
        except KeyError:
            should_skip = False
            skip_reason = ""
        except Exception as e:
            raise e

        return (should_skip, skip_reason)

    def _get_input(self, test) -> str:
        """Extract the input from the test entry."""
        return test["input"]

    def _get_expected_results(self, test, pattern_set: PatternSet) -> tuple[list[str], list[str]]:
        """Extract the expected rulenames and text spans from the test entry."""
        expected_rulenames = test["rulenames"] if "rulenames" in test else []
        expected_spans = test["spans"] if "spans" in test else []

        # Validate the presence of at least one key containing expected results
        if not expected_rulenames and not expected_spans:
            valid_keys = ["rulenames", "spans"]
            err_msg = f"The test must have at least one of these keys: {valid_keys}"
            raise KeyError(err_msg)

        # TODO refine and re-enable this
        # Validate the length of expected results in relation to the expected number of matches
        # expects_many_rulenames = bool(len(expected_rulenames) > 1)
        # expects_many_spans = bool(len(expected_spans) > 1)
        # if expects_many_rulenames or expects_many_spans:
        #     how_many_matches = pattern_set.meta["how_many_matches"]
        #     one_match_setting = Config().prop_str("PATTERN_SET_ONE_MATCH")

        #     if how_many_matches.upper() == one_match_setting.upper():
        #         err_msg = "The patternset expects only one match, but the test expects multiple matches"
        #         raise ValueError(err_msg)
        return (expected_rulenames, expected_spans)

    def _run_test(self, test, detector: Detector) -> None:
        """The main entrypoint to run an individual test."""
        input: str = self._get_input(test)

        # Determine if the test should be skipped
        (should_skip, skip_reason) = self._should_skip_test(test)
        if should_skip:
            msg = f"Skipping patternset '{detector.pattern_set.name}': '{input}'"
            if bool(len(skip_reason)):
                msg = msg + f" ({skip_reason})"
                print(msg)
            return

        # Extract expected results, run matcher, and compare to actual results
        # Separate each test using subTest to prevent failures from stopping other tests
        with self.subTest(f"{detector.pattern_set.name}:{input}"):
            (expected_rulenames, expected_spans) = self._get_expected_results(test, detector.pattern_set)
            rulenames: list[str] = []
            spans: list[str] = []

            for match in detector(input):
                rulenames.append(match.rulename)
                spans.append(str(match.span))

            if expected_rulenames:
                self.assertListEqual(rulenames, expected_rulenames)
            if expected_spans:
                self.assertListEqual(spans, expected_spans)

    def run_tests(self, detector: Detector) -> Optional[tuple[str, int, int]]:
        """The main entrypoint to run all of the tests in a patternset."""
        pattern_set: PatternSet = detector.pattern_set
        (should_skip, skip_reason) = self._should_skip_pset(pattern_set)
        if should_skip:
            msg = f"Skipping patternset '{pattern_set.name}'"
            if bool(len(skip_reason)):
                msg = msg + f": {skip_reason}"
                print(msg)
            return None

        # Separate using subTest to prevent failures from stopping the run
        num_pass = 0
        num_fail = 0
        if pattern_set.tests:
            with self.subTest(pattern_set.name):
                for test in pattern_set.tests:
                    try:
                        self._run_test(test, detector)
                        num_pass += 1
                    except Exception as e:
                        input: str = self._get_input(test)
                        print("======================================================================")
                        print(f"FAIL: [{pattern_set.name}: {input}]")
                        print("----------------------------------------------------------------------")
                        print("ACTUAL vs EXPECTED\n")
                        print(e)
                        print("----------------------------------------------------------------------\n")
                        num_fail += 1
        return (pattern_set.name, num_pass, num_fail)

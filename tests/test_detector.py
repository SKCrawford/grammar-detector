from unittest import TestCase
from settings import Filepath, pattern_set_config
from src.detectors import DetectorRepository


class TestDetectorTests(TestCase):
    """The test suite for the YAML patternset configuration files. When running this suite via `$ python -m unittest`, the tests in the YAML patternset configuration files will be run. This allows for the patterns to be tested by running the specified input then comparing the expected/actual matching rulenames and text spans. This information can then be used to make improvements to, expand upon, and battle harden the YAML patternset configuration files. As a general rule, when patternsets do not behave as expected, the solution is to improve the patterns or add new variations of existing patterns. The solution is rarely to add new features via code, so fixing errors in the patterns themselves should be the first step."""

    @classmethod
    def setUpClass(self):
        """Load the patternset configuration files to extract the tests."""
        self.repo = DetectorRepository()
        for fpath in pattern_set_config.internal_patternset_filepaths:
            fp = Filepath(fpath)
            self.repo.create(fp.filepath)

    def should_skip_pset(self, pset):
        """Determine if the patternset's tests should be skipped. This operates at the patternset level."""
        should_skip = None
        skip_reason = None

        try:
            skip_setting = pset.meta["skip_tests"]
            if type(skip_setting) == bool:
                should_skip = skip_setting
                skip_reason = ""
            elif type(skip_setting) == str:
                should_skip = bool(len(skip_setting))
                skip_reason = skip_setting
            else:
                msg = f"Expected a bool or str but got '{type(skip_setting)}'"
                raise TypeError(msg)
        except KeyError:
            should_skip = False
            skip_reason = ""
        except Exception as e:
            raise e

        return (should_skip, skip_reason)

    def should_skip_test(self, test):
        """Determine if the patternset's tests should be skipped. This operates at the test level."""
        should_skip = None
        skip_reason = None

        try:
            skip_setting = test["skip"]
            if type(skip_setting) == bool:
                should_skip = skip_setting
                skip_reason = ""
            elif type(skip_setting) == str:
                should_skip = bool(len(skip_setting))
                skip_reason = skip_setting
            else:
                msg = f"Expected a bool or str but got '{type(skip_setting)}'"
                raise TypeError(msg)
            return (should_skip, skip_reason)
        except KeyError:
            should_skip = False
            skip_reason = ""
        except Exception as e:
            raise e

        return (should_skip, skip_reason)

    def get_input(self, test):
        """Extract the input from the test entry."""
        return test["input"]

    def get_expected_results(self, test, pset):
        """Extract the expected rulenames and text spans from the test entry."""
        expected_rulenames = test["rulenames"] if "rulenames" in test else []
        expected_spans = test["spans"] if "spans" in test else []

        # Validate the presence of at least one key containing expected results
        if not expected_rulenames and not expected_spans:
            valid_keys = [rulenames_key, spans_key]
            err_msg = f"The test must have at least one of these keys: {valid_keys}"
            raise KeyError(err_msg)

        # Validate the length of expected results in relation to the expected number of matches
        expects_many_rulenames = bool(len(expected_rulenames) > 1)
        expects_many_spans = bool(len(expected_spans) > 1)
        if expects_many_rulenames or expects_many_spans:
            how_many_matches = pset.meta["how_many_matches"]
            one_match_setting = pattern_set_config.prop_str("ONE_MATCH")

            if how_many_matches.upper() == one_match_setting.upper():
                err_msg = "The patternset expects only one match, but the test expects multiple matches"
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
            return

        # Extract expected results, run matcher, and compare to actual results
        # Separate each test using subTest to prevent failures from stopping other tests
        with self.subTest(f"{pset.name}:{input}"):
            (expected_rulenames, expected_spans) = self.get_expected_results(test, pset)
            rulenames = []
            spans = []

            detector = self.repo.get_one(pset.name)
            for match in detector(input):
                rulenames.append(match.rulename)
                spans.append(str(match.span))

            if expected_rulenames:
                self.assertListEqual(rulenames, expected_rulenames)
            if expected_spans:
                self.assertListEqual(spans, expected_spans)

    def run_detector(self, detector):
        """The main entrypoint to run all of the tests in a patternset."""
        pset = detector.pattern_set
        (should_skip, skip_reason) = self.should_skip_pset(pset)
        if should_skip:
            msg = f"Skipping patternset '{pset.name}'"
            if bool(len(skip_reason)):
                msg = msg + f": {skip_reason}"
                print(msg)
            return

        # Separate using subTest to prevent failures from stopping the run
        if pset.tests:
            with self.subTest(pset.name):
                for test in pset.tests:
                    self.run_test(test, pset)

    def test_pattern_set_json_tests(self):
        """The main entrypoint for the unittest package."""
        [self.run_detector(detector) for detector in self.repo.get_all()]

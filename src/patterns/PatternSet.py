from logging import getLogger
from typing import Union
from settings import pattern_set_config_keys
from .Pattern import Pattern, PatternData


Name = str
MetaSetting = Union[str, bool]
Meta = dict[str, MetaSetting]

TestInput = str
TestExpectedRulenames = list[str]
TestExpectedSpans = list[str]
Test = dict[str, Union[TestInput, TestExpectedRulenames, TestExpectedSpans]]

PatternSetData = dict[str, Union[Meta, list[PatternData], list[Test]]]
ExtractedPatternSetData = tuple[Meta, list[PatternData], list[Test]]


logger = getLogger(__name__)


def extract_pattern_set_data(data: PatternSetData) -> ExtractedPatternSetData:
    """Extract and return the patterns, meta config, and tests from the loaded PatternSetData."""
    # Extract the patterns
    patterns_key: str = pattern_set_config_keys.prop_str("PATTERNS")
    pattern_data_list: list[PatternData] = data[patterns_key]

    # Extract the meta config
    meta: Meta = {}
    meta_key: str = pattern_set_config_keys.prop_str("META")
    if meta_key in data:
        meta = data[meta_key]

    # Extract the tests
    tests: list[Test] = []
    tests_key: str = pattern_set_config_keys.prop_str("TESTS")
    if tests_key in data:
        tests = data[tests_key]

    return (pattern_data_list, meta, tests)


class PatternSet:
    def __init__(self, name: Name) -> None:
        self.name: Name = name
        self.patterns: dict[str, Pattern] = {}
        self.meta: Meta = {}
        self.tests: Tests = []

    def add_pattern(self, pattern: Pattern) -> None:
        self.patterns[pattern.rulename] = pattern

    def get_all_patterns(self) -> list[Pattern]:
        return [self.patterns[k] for k in self.patterns]

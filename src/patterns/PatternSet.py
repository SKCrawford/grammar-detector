from logging import getLogger
from typing import Literal, Union
from settings import pattern_set_config
from .Pattern import Pattern, PatternData


Name = str
MetaSettingKeys = Literal["extract_noun_chunks", "how_many_matches", "skip_tests"]
MetaSettingValues = Union[str, bool]
Meta = dict[MetaSettingKeys, MetaSettingValues]

TestKeys = Literal["input", "rulenames", "spans", "skip"]
TestInput = str
TestExpectedRulenames = list[str]
TestExpectedSpans = list[str]
Test = dict[TestKeys, Union[TestInput, TestExpectedRulenames, TestExpectedSpans]]

PatternSetData = dict[str, Union[list[PatternData], Meta, list[Test]]]
ExtractedPatternSetData = tuple[list[PatternData], Meta, list[Test]]


logger = getLogger(__name__)


class PatternSet:
    def __init__(self, name: Name, data: PatternSetData) -> None:
        logger.debug(f"Constructing the '{name}' PatternSet")
        (pattern_data_list, meta, tests) = self._extract_data(data)

        self.patterns: dict[str, Pattern] = {}
        self.name: Name = name
        self.meta: Meta = meta
        self.tests: list[Test] = tests

        for pattern_data in pattern_data_list:
            pattern = Pattern(pattern_data)
            self.add_pattern(pattern)

    @property
    def how_many_matches(self) -> str:
        try:
            return str(self.meta["how_many_matches"])
        except:
            return pattern_set_config.prop_str("ONE_MATCH")

    @property
    def should_extract_noun_chunks(self) -> bool:
        try:
            return bool(self.meta["extract_noun_chunks"])
        except:
            return False

    def _extract_data(self, data: PatternSetData) -> ExtractedPatternSetData:
        """Extract and return the patterns, meta config, and tests from the loaded PatternSetData."""
        logger.info("Extracting the PatternSet data")

        logger.debug("Extracting the patterns")
        pattern_data_list: list[PatternData] = data["patterns"]

        logger.debug("Extracting the meta config")
        meta: Meta = data["meta"] if "meta" in data else {}

        logger.debug("Extracting the tests")
        tests: list[Test] = data["tests"] if "tests" in data else []

        return (pattern_data_list, meta, tests)

    def add_pattern(self, pattern: Pattern) -> None:
        logger.info(
            f"Adding the '{pattern.rulename}' Pattern to the '{self.name}' PatternSet"
        )
        self.patterns[pattern.rulename] = pattern

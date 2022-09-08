from logging import getLogger
from typing import Literal, Union
from ..Config import Config
from .Pattern import Pattern, PatternData


MetaSettingKeys = Literal[
    "best_match",
    "extract_noun_chunks",
    "how_many_matches",
    "skip_tests",
]
MetaSettingValues = Union[str, bool]
Meta = dict[MetaSettingKeys, MetaSettingValues]

TestKeys = Literal[
    "input",
    "rulenames",
    "skip",
    "spans",
]
TestInput = str
TestExpectedRulenames = list[str]
TestExpectedSpans = list[str]
Test = dict[TestKeys, Union[TestInput, TestExpectedRulenames, TestExpectedSpans]]

PatternSetData = dict[str, Union[list[PatternData], Meta, list[Test]]]


logger = getLogger(__name__)


class PatternSet:
    def __init__(self, name: str, data: PatternSetData) -> None:
        logger.debug(f"Constructing the '{name}' PatternSet")
        self.name: str = name

        self.patterns: dict[str, Pattern] = {}
        for p_data in data["patterns"]:
            pattern = Pattern(p_data)
            logger.info(f"Adding '{pattern.rulename}' to '{self.name}'")
            self.patterns[pattern.rulename] = pattern

        self.meta: Meta = data["meta"] if "meta" in data else {}
        for meta_key in self.meta:
            logger.debug(f"Found '{self.meta[meta_key]}' for meta '{meta_key}'")

        self.tests: list[Test] = data["tests"] if "tests" in data else []
        for test in self.tests:
            logger.debug(f"Found test: {test['input']}")

    @property
    def best_match(self) -> str:
        try:
            return str(self.meta["best_match"])
        except:
            return Config().prop_str("PATTERN_SET_DEFAULT_BEST_MATCH")

    @property
    def how_many_matches(self) -> str:
        try:
            return str(self.meta["how_many_matches"])
        except:
            return Config().prop_str("PATTERN_SET_DEFAULT_HOW_MANY_MATCHES")

    @property
    def should_extract_noun_chunks(self) -> bool:
        try:
            return bool(self.meta["extract_noun_chunks"])
        except:
            return False

    @property
    def skip_tests(self) -> str:
        try:
            return str(self.meta["skip_tests"])
        except:
            return ""

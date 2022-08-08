from logging import getLogger
from typing import Literal, Union
from settings import pattern_set_config
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

        logger.debug("Loading the meta settings")
        self.meta: Meta = data["meta"] if "meta" in data else {}

        logger.debug("Loading the tests")
        self.tests: list[Test] = data["tests"] if "tests" in data else []

    @property
    def best_match(self) -> str:
        try:
            return str(self.meta["best_match"])
        except:
            return pattern_set_config.prop_str("DEFAULT_BEST_MATCH")

    @property
    def how_many_matches(self) -> str:
        try:
            return str(self.meta["how_many_matches"])
        except:
            return pattern_set_config.prop_str("DEFAULT_HOW_MANY_MATCHES")

    @property
    def should_extract_noun_chunks(self) -> bool:
        try:
            return bool(self.meta["extract_noun_chunks"])
        except:
            return False

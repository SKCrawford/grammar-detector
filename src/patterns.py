from logging import getLogger
from spacy.tokens import Token
from typing import Any, Union
from settings import SettingKeys


MetaSetting = Union[str, bool]
MetaDict = dict[str, MetaSetting]
Test = dict[str, Union[str, list[str]]]


logger = getLogger(__name__)


class Pattern:
    def __init__(self, pattern_data: dict[str, Any]):
        self.rulename: str = pattern_data[SettingKeys.PSET_PATTERNS_RULENAME.value]
        self.tokens: list[Token] = pattern_data[SettingKeys.PSET_PATTERNS_TOKENS.value]


class PatternSet:
    def __init__(self, name: str, pset_data: dict[str, Any]):
        self.name: str = name
        self.patterns: dict[str, Pattern] = {}

        meta_key: str = SettingKeys.PSET_META.value
        self.meta: MetaDict = pset_data[meta_key] if meta_key in pset_data else {}

        tests_key: str = SettingKeys.PSET_TESTS.value
        self.tests: list[Test] = pset_data[tests_key] if tests_key in pset_data else []

        patterns_key: str = SettingKeys.PSET_PATTERNS.value
        for pattern_data in pset_data[patterns_key]:
            self._add_pattern(pattern_data)

    def get_all_patterns(self) -> list[Pattern]:
        return [self.patterns[k] for k in self.patterns]

    def _add_pattern(self, pattern_data: dict[str, Any]) -> None:
        pattern = Pattern(pattern_data)
        self.patterns[pattern.rulename] = pattern

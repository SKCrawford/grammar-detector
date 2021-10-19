from logging import getLogger
from spacy.tokens import Token
from typing import Any, Union

# from settings import PatternSetConfigKeys
from settings import pattern_set_config_keys


MetaSetting = Union[str, bool]
MetaDict = dict[str, MetaSetting]
Test = dict[str, Union[str, list[str]]]


logger = getLogger(__name__)


class Pattern:
    def __init__(self, pattern_data: dict[str, Any]):
        # rulename_key: str = PatternSetConfigKeys.PATTERNS_RULENAME.value
        rulename_key: str = pattern_set_config_keys.prop("RULENAME")
        self.rulename: str = pattern_data[rulename_key]

        # tokens_key: str = PatternSetConfigKeys.PATTERNS_TOKENS.value
        tokens_key: str = pattern_set_config_keys.prop("TOKENS")
        self.tokens: list[Token] = pattern_data[tokens_key]


class PatternSet:
    def __init__(self, name: str, pset_data: dict[str, Any]):
        self.name: str = name
        self.patterns: dict[str, Pattern] = {}

        # meta_key: str = PatternSetConfigKeys.META.value
        meta_key: str = pattern_set_config_keys.prop("META")
        self.meta: MetaDict = pset_data[meta_key] if meta_key in pset_data else {}

        # tests_key: str = PatternSetConfigKeys.TESTS.value
        tests_key: str = pattern_set_config_keys.prop("TESTS")
        self.tests: list[Test] = pset_data[tests_key] if tests_key in pset_data else []

        # patterns_key: str = PatternSetConfigKeys.PATTERNS.value
        patterns_key: str = pattern_set_config_keys.prop("PATTERNS")
        for pattern_data in pset_data[patterns_key]:
            self._add_pattern(pattern_data)

    def get_all_patterns(self) -> list[Pattern]:
        return [self.patterns[k] for k in self.patterns]

    def _add_pattern(self, pattern_data: dict[str, Any]) -> None:
        pattern = Pattern(pattern_data)
        self.patterns[pattern.rulename] = pattern

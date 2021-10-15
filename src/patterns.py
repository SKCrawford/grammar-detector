from json import load as load_json
from logging import getLogger
from os.path import join
from spacy.tokens import Token
from typing import Any, Union
from yaml import FullLoader, load as load_yaml
from settings import PATTERNS_DIR_FILE_EXTENSION, PATTERNS_DIR_PATH, SettingKeys


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


class PatternSetLoader:
    def __init__(self) -> None:
        self.file_ext: str = PATTERNS_DIR_FILE_EXTENSION
        self.dir_path: str = PATTERNS_DIR_PATH
        self.pattern_sets: dict[str, PatternSet] = {}

    def load(self, pset_name: str) -> PatternSet:
        if pset_name in self.pattern_sets:
            return self.pattern_sets[pset_name]

        pset_data: dict[str, Any] = {}
        filepath = self._get_path(pset_name)
        logger.debug(f"Reading file at '{filepath}'")
        with open(filepath, "r") as f:
            logger.debug(f"Loading '{filepath}' as a {self.file_ext} file")
            pset_data = self._load_file(f)

        pset = PatternSet(pset_name, pset_data)
        self.pattern_sets[pset.name] = pset
        return pset

    def _load_file(self, file):
        if self.file_ext == "yaml" or self.file_ext == "yml":
            return load_yaml(file, Loader=FullLoader)
        elif self.file_ext == "json":
            return load_json(file)
        else:
            raise ValueError(f"Invalid file extension '{self.file_ext}'")

    def _get_path(self, pset_name: str) -> str:
        filename = f"{pset_name}.{self.file_ext}"
        return join(self.dir_path, filename)

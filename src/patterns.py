from logging import getLogger
from json import load
from os.path import join
from settings import PATTERNS_DIR_FILE_EXTENSION, PATTERNS_DIR_PATH, SettingKeys


logger = getLogger(__name__)


class Pattern:
    def __init__(self, pattern_data: dict):
        self.rulename = pattern_data[SettingKeys.PSET_PATTERNS_RULENAME.value]
        self.tokens = pattern_data[SettingKeys.PSET_PATTERNS_TOKENS.value]


class PatternSet:
    def __init__(self, name: str, pset_data: dict, **kwargs):
        self.name: str = name
        self.patterns: dict = {}

        meta_key: str = SettingKeys.PSET_META.value
        self.meta: dict = pset_data[meta_key] if meta_key in pset_data else {}

        tests_key: str = SettingKeys.PSET_TESTS.value
        self.tests: list = pset_data[tests_key] if tests_key in pset_data else []

        patterns_key: str = SettingKeys.PSET_PATTERNS.value
        for pattern_data in pset_data[patterns_key]:
            self._add_pattern(pattern_data)

    def get_all_patterns(self) -> list[Pattern]:
        return [self.patterns[k] for k in self.patterns]

    def _add_pattern(self, pattern_data: dict) -> None:
        pattern: Pattern = Pattern(pattern_data)
        self.patterns[pattern.rulename]: Pattern = pattern


class PatternSetLoader:
    def __init__(self):
        self.file_ext: str = PATTERNS_DIR_FILE_EXTENSION
        self.dir_path: str = PATTERNS_DIR_PATH
        self.pattern_sets: dict = {}

    def load(self, pset_name: str) -> PatternSet:
        """Given a str, return a PatternSet instance."""
        if pset_name in self.pattern_sets:
            return self.pattern_sets[pset_name]

        pset_data: dict = None
        with open(self._get_path(pset_name), "r") as f:
            pset_data = load(f)

        pset = PatternSet(pset_name, pset_data)
        self.pattern_sets[pset.name]: PatternSet = pset
        return pset

    def _get_path(self, pset_name: str) -> str:
        filename = f"{pset_name}.{self.file_ext}"
        return join(self.dir_path, filename)

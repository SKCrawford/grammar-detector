import os
from logging import DEBUG
from enum import Enum


class Config:
    """A class containing the configuration settings for the app. This class should not be directly imported; import the premade instance `config` instead."""

    def __init__(self):
        # Configurable
        self.pattern_set_dir = "patterns"
        self.pattern_set_file_ext = "yaml"
        self.spacy_dataset = "en_core_web_lg"

        # Do not configure (caches for getters)
        self._root_dir_path = None
        self._pattern_set_dir_path = None
        self._pattern_set_names = None
        self._pattern_set_paths = None

    @property
    def root_dir_path(self) -> str:
        """Return the full path of the project's root directory."""
        if self._root_dir_path:
            return self._root_dir_path
        path = os.path.dirname(os.path.abspath(__file__))
        self._root_dir_path = path
        return path

    @property
    def pattern_set_dir_path(self) -> str:
        """Return the full path of the directory containing the patternsets."""
        if self._pattern_set_dir_path:
            return self._pattern_set_dir_path
        path = os.path.join(self.root_dir_path, self.pattern_set_dir)
        self._pattern_set_dir_path = path
        return path

    @property
    def pattern_set_names(self) -> list[str]:
        """Return a list of the existing patternsets. This is tantamount to the patternsets' filenames without the file extension."""
        if self._pattern_set_names:
            return self._pattern_set_names

        names = []
        for path in self.pattern_set_paths:
            name = path.replace(f".{self.pattern_set_file_ext}", "")
            names.append(name)
        self._pattern_set_names = names
        return names

    @property
    def pattern_set_paths(self) -> list[str]:
        """Return a list of the existing patternsets. This is tantamount to the patternsets' filenames with the file extension."""
        if self._pattern_set_paths:
            return self._pattern_set_paths

        filepaths = []
        for f in os.listdir(self.pattern_set_dir_path):
            if f.endswith(self.pattern_set_file_ext) and not f.startswith("."):
                filepaths.append(f)
        self._pattern_set_paths = filepaths
        return filepaths


class LoggerConfig(Enum):
    """Project-wide logging configuration settings."""

    DIR = ".logs"
    FILE_DEBUG = "debug.log"
    FILE_LAST = "last.log"
    FILE_TEST = "test.log"
    FORMAT = (
        "[%(asctime)s][%(module)s:%(funcName)s:%(lineno)d][%(levelname)s] %(message)s"
    )
    LEVEL = DEBUG


class PatternSetConfigKeys(Enum):
    """Acceptable keys for the PatternSet's configuration settings. Changes to the keys in the YAML file should be reflected here and vice-versa."""

    META = "meta"
    META_BEST_MATCH = "best_match"
    META_EXTRACT_NOUN_CHUNKS = "extract_noun_chunks"
    META_HOW_MANY_MATCHES = "how_many_matches"
    META_SKIP = "skip"  # TODO change to "skip_tests" for clarity
    PATTERNS = "patterns"
    PATTERNS_RULENAME = "rulename"
    PATTERNS_TOKENS = "tokens"
    TESTS = "tests"
    TESTS_INPUT = "input"
    TESTS_RULENAMES = "rulenames"
    TESTS_SKIP = "skip"
    TESTS_SPANS = "spans"


class PatternSetConfigValues(Enum):
    """Acceptable values for the PatternSet's configuration settings."""

    BEST_MATCH_FIRST = "FIRST"  # NYI
    BEST_MATCH_LAST = "LAST"  # NYI
    BEST_MATCH_LONGEST = "LONGEST"  # Not the spaCy matcher setting
    BEST_MATCH_SHORTEST = "SHORTEST"  # NYI
    HOW_MANY_MATCHES_ALL_MATCHES = "ALL"
    HOW_MANY_MATCHES_ONE_MATCH = "ONE"


class PatternSetConfigDefaults(Enum):
    """Default values for the PatternSet's configuration settings."""

    BEST_MATCH = PatternSetConfigValues.BEST_MATCH_LONGEST.value
    HOW_MANY_MATCHES = PatternSetConfigValues.HOW_MANY_MATCHES_ONE_MATCH.value
    SHOULD_EXTRACT_NOUN_CHUNKS = False


config = Config()

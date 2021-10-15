import os
import logging
from enum import Enum


class SettingValues(Enum):
    BEST_MATCH_FIRST = "FIRST"  # NYI
    BEST_MATCH_LAST = "LAST"  # NYI
    BEST_MATCH_LONGEST = "LONGEST"  # Not the spaCy matcher setting
    BEST_MATCH_SHORTEST = "SHORTEST"  # NYI
    HOW_MANY_MATCHES_ALL_MATCHES = "ALL"
    HOW_MANY_MATCHES_MANY_MATCHES = "MANY"  # NYI
    HOW_MANY_MATCHES_ONE_MATCH = "ONE"


class SettingKeys(Enum):
    PSET_META = "meta"
    PSET_META_BEST_MATCH = "best_match"
    PSET_META_EXTRACT_NOUN_CHUNKS = "extract_noun_chunks"
    PSET_META_HOW_MANY_MATCHES = "how_many_matches"
    PSET_META_SKIP = "skip"
    PSET_PATTERNS = "patterns"
    PSET_PATTERNS_RULENAME = "rulename"
    PSET_PATTERNS_TOKENS = "tokens"
    PSET_TESTS = "tests"
    PSET_TESTS_SKIP = "skip"
    PSET_TESTS_SKIP_REASON = "skip_reason"
    PSET_TESTS_INPUT = "input"
    PSET_TESTS_RULENAMES = "rulenames"
    PSET_TESTS_SPANS = "spans"


class Defaults(Enum):
    BEST_MATCH = SettingValues.BEST_MATCH_LONGEST
    HOW_MANY_MATCHES = SettingValues.HOW_MANY_MATCHES_ONE_MATCH
    SHOULD_EXTRACT_NOUN_CHUNKS = False


ROOT_DIR_PATH: str = os.path.dirname(os.path.abspath(__file__))

LOG_FORMAT: str = (
    "[%(asctime)s][%(module)s:%(funcName)s:%(lineno)d][%(levelname)s] %(message)s"
)

LOG_LEVEL: int = logging.DEBUG

LOG_FILE_DEBUG: str = "debug.log"

LOG_FILE_LAST: str = "last.log"

LOG_FILE_TEST: str = "test.log"

PATTERNS_DIR_FILE_EXTENSION: str = "yaml"

PATTERNS_DIR_NAME: str = "patterns/"

PATTERNS_DIR_PATH: str = os.path.join(ROOT_DIR_PATH, PATTERNS_DIR_NAME)

PATTERN_SETS_PATHS: list[str] = [
    f
    for f in os.listdir(PATTERNS_DIR_PATH)
    if not f.startswith(".") and f.endswith(PATTERNS_DIR_FILE_EXTENSION)
]

PATTERN_SETS_NAMES: list[str] = [
    p.replace(f".{PATTERNS_DIR_FILE_EXTENSION}", "") for p in PATTERN_SETS_PATHS
]

SPACY_DATASET: str = "en_core_web_lg"

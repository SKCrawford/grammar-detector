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
    PATTERN_SET_FILE_META_BEST_MATCH = "best_match"
    PATTERN_SET_FILE_META_EXTRACT_NOUN_CHUNKS = "extract_noun_chunks"
    PATTERN_SET_FILE_META_HOW_MANY_MATCHES = "how_many_matches"
    PATTERN_SET_FILE_META = "meta"
    PATTERN_SET_FILE_PATTERNS = "patterns"
    PATTERN_SET_FILE_PATTERNS_RULENAME = "rulename"
    PATTERN_SET_FILE_PATTERNS_TOKENS = "tokens"
    PATTERN_SET_FILE_TESTS_INPUT = "input"
    PATTERN_SET_FILE_TESTS = "tests"
    PATTERN_SET_FILE_TESTS_RULENAMES = "rulenames"
    PATTERN_SET_FILE_TESTS_SPANS = "spans"


class Defaults(Enum):
    BEST_MATCH = SettingValues.BEST_MATCH_LONGEST
    HOW_MANY_MATCHES = SettingValues.HOW_MANY_MATCHES_ONE_MATCH
    SHOULD_EXTRACT_NOUN_CHUNKS = False


ROOT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))

LOG_FORMAT = (
    "[%(asctime)s][%(module)s:%(funcName)s:%(lineno)d][%(levelname)s] %(message)s"
)

LOG_LEVEL = logging.DEBUG

LOG_FILE_DEBUG = "debug.log"

LOG_FILE_LAST = "last.log"

LOG_FILE_TEST = "test.log"

PATTERNS_DIR_FILE_EXTENSION = "json"

PATTERNS_DIR_NAME = "patterns/"

PATTERNS_DIR_PATH = os.path.join(ROOT_DIR_PATH, PATTERNS_DIR_NAME)

PATTERN_SETS_PATHS = [f for f in os.listdir(PATTERNS_DIR_PATH) if not f.startswith(".")]

PATTERN_SETS_NAMES = [
    p.replace(f".{PATTERNS_DIR_FILE_EXTENSION}", "") for p in PATTERN_SETS_PATHS
]

SPACY_DATASET = "en_core_web_lg"

import logging
from json import load
from os.path import join
from settings import (
    Defaults,
    SettingKeys,
    PATTERNS_DIR_PATH,
    PATTERNS_DIR_FILE_EXTENSION,
)


logger = logging.getLogger(__name__)


def load_pattern_set(pattern_set_filename):
    """Given a filepath ending with .json,"""
    pattern_set_path = join(
        PATTERNS_DIR_PATH, f"{pattern_set_filename}.{PATTERNS_DIR_FILE_EXTENSION}"
    )
    logger.debug(f"Started loading {pattern_set_path}")

    try:
        with open(pattern_set_path, "r") as f:
            result = load(f)
            logger.debug(f"Finished loading {pattern_set_path}")
            return result
    except FileNotFoundError as e:
        logger.error(f"Couldn't find {pattern_set_path}")
        raise e
    except Exception as e:
        logger.error(f"Unknown error occurred while loading {pattern_set_path}")
        raise e


class Pattern:
    def __init__(self, rulename, tokens):
        self.rulename = rulename
        self.tokens = tokens


class PatternSet:
    def __init__(self, pattern_set_name):
        self.name = pattern_set_name
        self.patterns = {}
        data = load_pattern_set(self.name)

        key = SettingKeys.PSET_META.value
        self.meta = data[key] if key in data else None

        key = SettingKeys.PSET_TESTS.value
        self.tests = data[key] if key in data else []

        for pattern_entry in data[SettingKeys.PSET_PATTERNS.value]:
            rulename = pattern_entry[SettingKeys.PSET_PATTERNS_RULENAME.value]
            tokens = pattern_entry[SettingKeys.PSET_PATTERNS_TOKENS.value]
            self.patterns[rulename] = Pattern(rulename, tokens)

    def get_all_patterns(self):
        return [self.patterns[k] for k in self.patterns]

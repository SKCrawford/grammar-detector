import logging
from json import load
from os.path import join
from settings import PATTERNS_DIR


logger = logging.getLogger(__name__)


def load_pattern_set(pattern_set_filename):
    """Given a filepath ending with .json,"""
    pattern_set_path = join(PATTERNS_DIR, f"{pattern_set_filename}.json")
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
        self.meta = data["meta"] if "meta" in data else None
        self.tests = data["tests"] if "tests" in data else []

        for pattern_entry in data["patterns"]:
            rulename = pattern_entry["rulename"]
            tokens = pattern_entry["tokens"]
            self.patterns[rulename] = Pattern(rulename, tokens)

    @property
    def how_many_matches(self):
        key = "how_many_matches"
        setting = self.meta[key] if key in self.meta else "one"
        assert type(setting) == str, f"Expected a str but got {type(setting)}"
        return setting.upper()

    @property
    def should_extract_noun_chunks(self):
        key = "should_extract_noun_chunks"
        setting = self.meta[key] if key in self.meta else False
        assert type(setting) == bool, f"Expected a bool but got {type(setting)}"
        return setting

    def get_all_patterns(self):
        return [self.patterns[k] for k in self.patterns]

    def get_pattern(self, rulename):
        return self.patterns[rulename]

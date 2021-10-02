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
        self.meta = None
        self.patterns = {}

        data = load_pattern_set(self.name)
        self.meta = data["meta"]
        for pattern_entry in data["patterns"]:
            rulename = pattern_entry["rulename"]
            tokens = pattern_entry["tokens"]
            self.patterns[rulename] = Pattern(rulename, tokens)

    @property
    def how_many_matches(self):
        setting = None
        try:
            setting = self.meta["how_many_matches"]
        except KeyError:
            setting = "one"  # TODO refactor
        assert type(setting) == str
        return setting.upper()

    @property
    def should_extract_noun_chunks(self):
        setting = None
        try:
            setting = self.meta["extract_noun_chunks"]
        except KeyError:
            setting = False  # TODO refactor
        assert type(setting) == bool
        return setting

    def get_all_patterns(self):
        return [self.patterns[k] for k in self.patterns]

    def get_pattern(self, rulename):
        return self.patterns[rulename]

import logging
from settings import SettingKeys
from .load import load_pattern_set
from .Pattern import Pattern


logger = logging.getLogger(__name__)


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

    def get_meta(self, meta_key):
        if meta_key not in self.meta:
            msg = f"Key '{meta_key}' does not exist in meta"
            logger.error(msg)
            raise KeyError(msg)
        return self.meta[meta_key]

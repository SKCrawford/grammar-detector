from logging import getLogger
from .BaseMatcher import BaseMatcher
from .LongestMatcher import LongestMatcher
from settings import pattern_set_config_values


logger = getLogger(__name__)


class SoloMatcher(LongestMatcher):
    def __init__(self):
        self.best_match = pattern_set_config_values.prop_str("LONGEST_MATCH")

    def match_one(self, doclike: Union[Doc, Span]) -> Match:
        """Run the matcher and return the best match. The matcher method is determined by the `best_match` attribute."""
        longest_match_setting_val = pattern_set_config_values.prop_str("LONGEST_MATCH")

        if self.best_match.upper() == longest_match_setting_val.upper():
            return self.match_longest(doclike)

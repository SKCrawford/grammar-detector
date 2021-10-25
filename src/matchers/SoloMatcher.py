from logging import getLogger
from spacy.tokens import Doc
from settings import pattern_set_config_values
from .LongestMatcher import LongestMatcher
from .Match import Match
from .Matcher import Matcher


logger = getLogger(__name__)


class SoloMatcher(LongestMatcher):
    """A callable Matcher for getting the best match for a given Doc, which is determined by the `best_match` attribute. For compatibility, the singular result is returned in a list."""

    def __init__(self) -> None:
        super().__init__()
        self.best_match = pattern_set_config_values.prop_str("LONGEST_MATCH")

    def __call__(self, doc: Doc) -> Match:
        """The entrypoint for this Matcher."""
        return self.match_one(doc)

    def match_one(self, doc: Doc) -> Match:
        """Get the best match for a given Doc, which is determined by the `best_match` attribute. For compatibility, the singular result is returned in a list."""
        longest_match_setting = pattern_set_config_values.prop_str("LONGEST_MATCH")

        if self.best_match.upper() == longest_match_setting.upper():
            return self.match_longest(doc)

from logging import getLogger
from spacy.tokens import Doc
from settings import pattern_set_config_values
from .Match import Match, RawMatch


logger = getLogger(__name__)


class MatchSet:
    def __init__(self, raw_matches: list[RawMatch], doc: Doc) -> None:
        self.matches = [Match(raw_match, doc) for raw_match in raw_matches]
        self.doc: Doc = doc
        self.best_match = pattern_set_config_values.prop_str("LONGEST_MATCH")

    def __repr__(self):
        return f"<MatchSet ({len(self.all)}): {[repr(m) for m in self.all]}"

    @property
    def all(self):
        logger.info(f"Getting all {len(self.matches)} matches")
        return self.matches

    @property
    def best(self):
        logger.info(f"Getting the best match of these: {matches}")
        longest_match_setting = pattern_set_config_values.prop_str("LONGEST_MATCH")
        if self.best_match.upper() == longest_match_setting.upper():
            return self.match_longest(doc)

    @property
    def longest(self):
        logger.info(f"Getting the longest match of these: {matches}")
        distances: list[int] = [match.end - match.start for match in self.matches]
        largest_distance_i: int = distances.index(max(distances))
        longest_match: Match = self.matches[largest_distance_i]
        logger.info(f"Got the longest match: {longest_match}")
        return longest_match

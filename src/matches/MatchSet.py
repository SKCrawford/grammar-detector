from logging import getLogger
from spacy.tokens import Doc
from settings import pattern_set_config
from .Match import Match, RawMatch


logger = getLogger(__name__)


class MatchSet:
    def __init__(self, raw_matches: list[RawMatch], doc: Doc) -> None:
        logger.info(f"Constructing the MatchSet for '{doc.text}'")
        self.matches: list[Match] = [Match(raw_match, doc) for raw_match in raw_matches]
        self.doc: Doc = doc
        # TODO refactor setting the default
        self.best_match: str = pattern_set_config.prop_str("LONGEST_MATCH")

    def __repr__(self):
        return f"<MatchSet ({len(self.all)}): {[repr(m) for m in self.all]}"

    @property
    def all(self) -> list[Match]:
        logger.debug(f"Getting all {len(self.matches)} matches")
        return self.matches

    @property
    def best(self) -> Match:
        logger.info(
            f"Getting the best match of these {len(self.matches)}: {self.matches}"
        )
        longest_match_setting = pattern_set_config.prop_str("LONGEST_MATCH")

        if self.best_match.upper() == longest_match_setting.upper():
            return self.longest
        else:
            msg = f"The best match was either not provided or not supported: {self.best_match}"
            logger.error(msg)
            raise ValueError(msg)

    @property
    def longest(self) -> Match:
        logger.info(
            f"Getting the longest match of these {len(self.matches)}: {self.matches}"
        )
        distances: list[int] = [match.end - match.start for match in self.matches]
        largest_distance_i: int = distances.index(max(distances))
        longest_match: Match = self.matches[largest_distance_i]
        logger.info(f"Got the longest match: {longest_match}")
        return longest_match

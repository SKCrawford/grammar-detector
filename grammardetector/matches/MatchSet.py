from logging import getLogger
from spacy.tokens import Doc
from ..Config import Config
from .Match import Match, RawMatch


PATTERN_SET_ALL_MATCHES: str = "all"
PATTERN_SET_ONE_MATCH: str = "one"
PATTERN_SET_LONGEST_MATCH: str = "longest"


logger = getLogger(__name__)


class MatchSet:
    def __init__(
        self,
        raw_matches: list[RawMatch],
        doc: Doc,
        best_match: str = "",
        how_many_matches: str = "",
    ) -> None:
        logger.debug(f"Constructing the MatchSet for '{doc.text}'")
        self.matches: list[Match] = [Match(raw_match, doc) for raw_match in raw_matches]
        self.doc: Doc = doc
        self.best_match: str = best_match
        self.how_many_matches: str = how_many_matches

    def __repr__(self):
        return f"<MatchSet ({len(self.all)}): {[repr(m) for m in self.all]}"

    @property
    def result(self) -> list[Match]:
        if not self.matches:
            return []

        if self.how_many_matches == PATTERN_SET_ONE_MATCH:
            return [self.best]
        elif self.how_many_matches == PATTERN_SET_ALL_MATCHES:
            return self.all
        else:
            msg = f"Invalid value for 'how_many_matches': {self.how_many_matches}"
            logger.error(msg)
            raise ValueError(msg)

    @property
    def all(self) -> list[Match]:
        logger.debug(f"Getting all {len(self.matches)} matches")
        return self.matches

    @property
    def best(self) -> Match:
        logger.info(
            f"Getting the best match of these {len(self.matches)}: {self.matches}"
        )
        longest_match_setting = PATTERN_SET_LONGEST_MATCH

        if self.best_match.upper() == longest_match_setting.upper():
            return self.longest
        else:
            msg = f"Invalid value for 'best_match': {self.best_match}"
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

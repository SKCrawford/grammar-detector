from logging import getLogger
from spacy.tokens import Doc
from ..matches import Match
from .Matcher import Matcher


logger = getLogger(__name__)


class LongestMatcher(Matcher):
    """A callable Matcher for getting the longest match for a given Doc, which is the match with the greatest distance between its start and end values. For compatibility, the singular result is returned in a list."""

    def __call__(self, doc: Doc) -> list[Match]:
        """The entrypoint for this Matcher."""
        return self.match_longest(doc)

    def match_longest(self, doc: Doc) -> list[Match]:
        """Get the longest match for a given Doc, which is the match with the greatest distance between its start and end values. For compatibility, the singular result is returned in a list."""
        matches: list[Match] = self.match_all(doc)

        logger.debug(f"Getting the longest match of these: {matches}")
        distances: list[int] = [match.end - match.start for match in matches]
        largest_distance_i: int = distances.index(max(distances))
        longest_match: Match = matches[largest_distance_i]

        logger.debug(f"Got the longest match: {longest_match}")
        return [longest_match]

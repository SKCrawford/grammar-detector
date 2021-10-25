from logging import getLogger
from spacy.tokens import Doc, Span
from .BaseMatcher import BaseMatcher
from .Match import Match


logger = getLogger(__name__)


class LongestMatcher(BaseMatcher):
    def match_longest(self, doclike: Union[Doc, Span]) -> Match:
        """Run the matcher and return the longest match, which is the match with the greatest distance between its start and end values."""
        matches: list[Match] = self.match_all(doclike)

        logger.debug(f"Getting the longest match of these: {matches}")
        distances: list[int] = [match.end - match.start for match in matches]
        largest_distance_i: int = distances.index(max(distances))
        longest_match: Match = matches[largest_distance_i]

        logger.debug(f"Got the longest match: {longest_match}")
        return longest_match

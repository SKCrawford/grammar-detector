from logging import getLogger
from ..inputs import Input
from ..matchers import PatternSetMatcher
from ..matches import MatchSet
from ..patterns import PatternSet


logger = getLogger(__name__)


class Detector:
    def __init__(self, pattern_set: PatternSet) -> None:
        logger.debug("Constructing the Detector")
        self.pattern_set = pattern_set
        self.name = self.pattern_set.name

        logger.debug(f"Creating the '{self.pattern_set.name}' PatternSetMatcher")
        self.matcher = self._load_matcher(self.pattern_set)

    def __call__(self, raw: str) -> list[MatchSet]:
        """The entrypoint for the Detector."""
        logger.debug(f"Detecting for '{self.name}' feature in '{raw}'")
        input = Input(raw)
        input.extract_noun_chunks = bool(self.pattern_set.should_extract_noun_chunks)
        match_sets: list[MatchSet] = [self.matcher(frag) for frag in input.fragments]

        logger.debug(f"Found {len(match_sets)} '{self.name}' MatchSets: {match_sets}")
        return match_sets

    def _load_matcher(self, pattern_set: PatternSet) -> PatternSetMatcher:
        return PatternSetMatcher(self.pattern_set)

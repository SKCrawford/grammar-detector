from logging import getLogger
from ..Input import Input
from ..matchers import PatternSetMatcher
from ..matches import Match, MatchSet
from ..patterns import PatternSet
from ..utils import flatten, Timeable


logger = getLogger(__name__)


class Detector(Timeable):
    def __init__(self, pattern_set: PatternSet) -> None:
        super().__init__()
        stop_timer = self.tk.start(f"Init the '{pattern_set.name}' Detector")

        logger.debug(f"Constructing the '{pattern_set.name}' Detector")
        self.pattern_set = pattern_set
        self.name = self.pattern_set.name

        logger.debug(f"Creating the '{self.pattern_set.name}' PatternSetMatcher")
        self.matcher = PatternSetMatcher(self.pattern_set)
        stop_timer()

    def __call__(self, raw: str) -> list[Match]:
        """The entrypoint for the Detector."""
        logger.info(f"Detecting '{self.name}'")
        input = Input(raw)
        input.extract_noun_chunks = bool(self.pattern_set.should_extract_noun_chunks)

        matches: list[list[Match]] = []
        for frag in input.fragments:
            match_set: MatchSet = self.matcher(frag)
            matches.append(match_set.result)
        return flatten(matches)

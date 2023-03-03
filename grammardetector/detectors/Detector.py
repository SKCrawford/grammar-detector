from logging import getLogger
from typing import Union
from ..Input import Input
from ..matchers import PatternSetMatcher
from ..matches import Match, MatchSet
from ..patterns import PatternSet
from ..utils import flatten


logger = getLogger(__name__)


class Detector:
    def __init__(self, pattern_set: PatternSet) -> None:
        logger.debug(f"Constructing the '{pattern_set.name}' Detector")
        self.pattern_set = pattern_set
        self.name = self.pattern_set.name

        logger.debug(f"Creating the '{self.pattern_set.name}' PatternSetMatcher")
        self.matcher = PatternSetMatcher(self.pattern_set)

    def __call__(self, text: Union[str, Input]) -> list[Match]:
        """The entrypoint for the Detector."""
        logger.info(f"Detecting '{self.name}'")
        input: Input
        if isinstance(text, str):
            input = Input(text)
        elif isinstance(text, Input):
            input = text
        else:
            raise TypeError(f"Expected input to be a str or Input but got {type(input)}")

        input.extract_noun_chunks = bool(self.pattern_set.should_extract_noun_chunks)

        matches: list[list[Match]] = []
        for frag in input.fragments:
            match_set: MatchSet = self.matcher(frag)
            matches.append(match_set.result)
        return flatten(matches)

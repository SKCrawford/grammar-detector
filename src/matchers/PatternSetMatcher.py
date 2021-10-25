import asyncio
from logging import getLogger
from spacy.matcher import Matcher as SpacyMatcher
from spacy.tokens import Doc, Span, Token
from typing import Callable, Union
from settings import pattern_set_config_values
from ..extractors import extract_span_features
from ..inputs import Input
from ..nlp import nlp
from ..patterns import PatternSet, Rulename
from ..utils import flatten
from .Match import Match
from .SoloMatcher import SoloMatcher


CallableManyMatches = Callable[[Input], list[Match]]


logger = getLogger(__name__)


class PatternSetMatcher(SoloMatcher):
    """A callable Matcher that adds the Patterns of the given PatternSet to the underlying matcher and modifies its Match/list[Match] output based on the meta configuration of the PatternSet."""

    def __init__(self, pattern_set: PatternSet):
        super().__init__()
        self.pattern_set: PatternSet = pattern_set

        logger.debug(
            f"Adding the {self.pattern_set.name} PatternSet's Patterns to the internal matcher"
        )
        for pattern in self.pattern_set.get_all_patterns():
            spacy_config: dict[str, str] = {"greedy": "LONGEST"}
            logger.debug(f"Adding the Pattern '{pattern.rulename}'")
            self._matcher.add(pattern.rulename, [pattern.tokens], **spacy_config)

    def __call__(self, input: Input) -> list[Match]:
        """The entry point for running the matcher. Using the PatternSet provided during construction, the appropriate matcher method will be called. All usable matcher methods should be included here."""
        return self.match_pattern_set(input)

    def match_pattern_set(self, input: Input) -> list[Match]:
        """Fragment the input, run the appropriate matcher, and modify the outgoing Matches based on the PatternSet's configuration."""
        logger.debug("Fragmenting the Input")
        fragments: list[Doc] = input.fragments

        logger.debug("Getting the match function")
        match: CallableManyMatches = self.get_match_fn()

        logger.debug(f"Running the match function on the fragments: {fragments}")
        matches = [match(item) for item in fragments]

        logger.debug(f"Flattening the matches: {matches}")
        matches: list[Match] = flatten(matches)

        logger.debug(f"Returning the matches: {matches}")
        return matches

    def get_match_fn(self) -> CallableManyMatches:
        """Determine the appropriate match function to use based on the PatternSet's settings."""
        one_match_setting: str = pattern_set_config_values.prop_str("ONE_MATCH")
        all_matches_setting: str = pattern_set_config_values.prop_str("ALL_MATCHES")
        how_many_matches: str = self.pattern_set.how_many_matches

        if how_many_matches.upper() == one_match_setting.upper():
            logger.debug("Getting the match function for one result per fragment")
            return self.match_one

        elif how_many_matches.upper() == all_matches_setting.upper():
            logger.debug("Getting the match function for all results per fragment")
            return self.match_all

        else:
            msg = f"Invalid how_many_matches setting: {how_many_matches} ({type(how_many_matches)})"
            logger.error(msg)
            raise ValueError(msg)

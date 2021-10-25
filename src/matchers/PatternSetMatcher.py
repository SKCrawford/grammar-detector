import asyncio
from logging import getLogger
from spacy.matcher import Matcher as SpacyMatcher
from spacy.tokens import Doc, Span, Token
from settings import pattern_set_config
from ..extractors import extract_span_features
from ..inputs import Input
from ..nlp import nlp
from ..patterns import PatternSet, Rulename
from ..utils import flatten
from .SoloMatcher import SoloMatcher


logger = getLogger(__name__)


class PatternSetMatcher(SoloMatcher):
    def __init__(self, pattern_set: PatternSet):
        self.pattern_set: PatternSet = pattern_set

        logger.debug("Adding the {self.pattern_set.name} PatternSet's Patterns to the internal matcher")
        for pattern in self.pattern_set.get_all_patterns():
            spacy_config: dict[str, str] = {"greedy": "LONGEST"}
            logger.debug(f"Adding the Pattern '{pattern.rulename}'")
            self._matcher.add(pattern.rulename, [pattern.tokens], **spacy_config)

    def __call__(self, input: Input) -> list[Match]:
        """The entry point for running the matcher. Using the pattern set provided during construction, the appropriate matcher method will be called. All usable matcher methods should be included here."""
        one_match_setting_val: str = pattern_set_config.values.prop_str("ONE_MATCH")
        all_matches_setting_val: str = pattern_set_config.values.prop_str("ALL_MATCHES")

        if self.how_many_matches.upper() == one_match_setting_val.upper():
            return self._match_one(input)
        elif self.how_many_matches.upper() == all_matches_setting_val.upper():
            return self._match_all(input)
        else:
            raise ValueError(f"Invalid how_many_matches setting: {how_many_matches}")

    def _fragment(self, input: Input) -> Union[list[Doc], list[Span]]:
        logger.debug(f"Fragmenting the input '{input.raw}'")
        fragments: Union[list[Doc], list[Span]] = []

        if self.pattern_set.should_extract_noun_chunks:
            logger.debug(f"Extracting the noun chunks")
            fragments = input.noun_chunks
            fragments = cast(list[Span], fragments)
        else:
            fragments = input.docs
            fragments = cast(list[Doc], fragments)
        logger.debug(f"Fragmented the input '{input.raw}' into {len(fragments)} fragment(s).")
        return fragments

    def _match_one(self, input: Input) -> list[Match]:
        logger.debug("Matching for one result")

        logger.debug("Fragmenting the input")
        fragments = self._fragment(input)

        logger.debug(f"Running the matcher against these fragments: {fragments}")
        matches = [self.match_one(item) for item in fragments]
        matches = flatten(matches)

        logger.debug(f"Returning the parsed matches: {matches}")
        return matches

2    def _match_all(self, input: Input) -> list[Match]:
        logger.debug("Matching for all results")

        logger.debug("Fragmenting the input")
        fragments = self._fragment(input)

        matches = [self.match_all(item) for item in fragments]
        matches = flatten(matches)

        logger.debug(f"Returning all matches: {matches}")
        return matches

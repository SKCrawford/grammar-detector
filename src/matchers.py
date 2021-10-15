import asyncio
from logging import getLogger
from spacy.matcher import Matcher as SpacyMatcher
from spacy.tokens import Doc, Span, Token
from typing import Any
from settings import Defaults, SettingKeys, SettingValues
from .extractors import extract_span_features
from .nlp import nlp
from .patterns import PatternSet


Match = tuple[int, int, int]
ParsedMatch = tuple[str, Span, dict[str, str]]


logger = getLogger(__name__)


class PatternSetMatcher:
    def __init__(self, pattern_set: PatternSet):
        self.pattern_set: PatternSet = pattern_set

        logger.debug("Constructing the internal spaCy matcher")
        self._inner_matcher = SpacyMatcher(nlp.vocab, validate=True)

        logger.debug("Adding the patterns to the internal matcher")
        for pattern in self.pattern_set.get_all_patterns():
            rulename: str = pattern.rulename
            tokens: list[Token] = pattern.tokens
            config: dict[str, Any] = {
                "greedy": "LONGEST",  # Not the same as the settings.py value
                "on_match": self._on_match,
            }
            logger.debug(f"Adding the pattern '{rulename}' to the internal matcher")
            self._inner_matcher.add(rulename, [tokens], **config)

    def match(self, doc: Doc) -> list[ParsedMatch]:
        """The entry point for running the matcher. Using the pattern set provided
        during construction, the appropriate matcher method will be returned.
        All usable matcher methods should be included here."""
        # Maybe handle default in PatternSet
        how_many_matches: str = str(Defaults.HOW_MANY_MATCHES.value).upper()
        key: str = SettingKeys.PSET_META_HOW_MANY_MATCHES.value
        if key in self.pattern_set.meta:
            how_many_matches = str(self.pattern_set.meta[key]).upper()

        logger.debug(f"Running the matcher method for '{how_many_matches}' result(s)")
        one_match: str = SettingValues.HOW_MANY_MATCHES_ONE_MATCH.value.upper()
        all_matches: str = SettingValues.HOW_MANY_MATCHES_ALL_MATCHES.value.upper()
        if how_many_matches == one_match:
            return self._match_one(doc)
        elif how_many_matches == all_matches:
            return self._match_all(doc)
        else:
            raise ValueError(f"Invalid how_many_matches setting: {how_many_matches}")

    def _match_one(self, doc: Doc) -> list[ParsedMatch]:
        logger.debug("Matching for one result")
        logger.debug("Running the internal matcher")
        all_matches = self._inner_matcher(doc)
        logger.debug(f"Found {len(all_matches)} match(es)")

        logger.debug("Determining the best match")
        best_match = self._get_best_match(all_matches)

        logger.debug(f"Parsing the best match: {best_match}")
        parsed_match = self._parse_match(best_match, doc)

        logger.debug(f"Parsed the best match: {parsed_match}")
        return [parsed_match]

    def _match_all(self, doc: Doc) -> list[ParsedMatch]:
        logger.debug("Matching for all results")
        logger.debug("Running the internal matcher")
        all_matches: list[Match] = self._inner_matcher(doc)
        logger.debug(f"Found {len(all_matches)} match(es)")

        logger.debug(f"Parsing many matches: {all_matches}")
        parsed: list[ParsedMatch] = [self._parse_match(m, doc) for m in all_matches]

        logger.debug(f"Parsed many matches: {parsed}")
        return parsed

    def _on_match(
        self, matcher: SpacyMatcher, doc: Doc, i: int, matches: list[Match]
    ) -> None:
        # logger.debug(f"MATCH #{i}")
        # logger.debug("Running the on_match callback")
        # logger.debug(f"External matcher: {self}")
        # logger.debug(f"Internal matcher: {matcher}")
        # logger.debug(f"Doc: {doc}")
        # logger.debug(f"Matches: {matches}")
        return

    def _parse_match(self, match: Match, doc: Doc) -> ParsedMatch:
        (match_id, start, end) = match
        rulename = nlp.vocab.strings[match_id]
        span = doc[start:end]
        logger.debug(f"Parsed ('{rulename}', '{span}') from match '{match}'")
        return (rulename, span, extract_span_features(span))

    def _get_best_match(self, matches: list[Match]) -> Match:
        # TODO
        logger.debug(f"Getting the best match from {matches}")
        return self._get_longest_match(matches)

    def _get_longest_match(self, matches: list[Match]) -> Match:
        logger.debug(f"Getting the longest match from {matches}")
        distances: list[int] = [end - start for (_, start, end) in matches]
        largest_distance_i: int = distances.index(max(distances))
        return matches[largest_distance_i]

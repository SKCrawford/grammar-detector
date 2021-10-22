import asyncio
from logging import getLogger
from spacy.matcher import Matcher as SpacyMatcher
from spacy.tokens import Doc, Span, Token
from settings import pattern_set_config
from .extractors import extract_span_features
from .nlp import nlp
from .patterns import PatternSet, Rulename


MatchId = int
Start = int
End = int
Match = tuple[MatchId, Start, End]

SpanFeatures = dict[str, str]
ParsedMatch = tuple[Rulename, Span, SpanFeatures]


logger = getLogger(__name__)


class PatternSetMatcher:
    def __init__(self, pattern_set: PatternSet):
        self.pattern_set: PatternSet = pattern_set

        logger.debug("Constructing the internal spaCy Matcher")
        self._inner_matcher = SpacyMatcher(nlp.vocab, validate=True)

        logger.debug("Adding the Patterns to the internal matcher")
        for pattern in self.pattern_set.get_all_patterns():
            spacy_config: dict[str, str] = {"greedy": "LONGEST"}
            logger.debug(f"Adding the Pattern '{pattern.rulename}'")
            self._inner_matcher.add(pattern.rulename, [pattern.tokens], **spacy_config)

    def __call__(self, doc: Doc) -> list[ParsedMatch]:
        """The entry point for running the matcher. Using the pattern set provided during construction, the appropriate matcher method will be called. All usable matcher methods should be included here."""
        one_match_setting_val: str = pattern_set_config.values.prop("ONE_MATCH")
        all_matches_setting_val: str = pattern_set_config.values.prop("ALL_MATCHES")

        how_many_matches: str = one_match_setting_val  # Defaults to one match
        how_many_key: str = pattern_set_config.keys.prop("HOW_MANY_MATCHES")
        if how_many_key in self.pattern_set.meta:
            how_many_matches = str(self.pattern_set.meta[how_many_key])

        logger.debug(f"Running the matcher method for '{how_many_matches}' result(s)")
        if how_many_matches.upper() == one_match_setting_val.upper():
            return [self._match_one(doc)]
        elif how_many_matches.upper() == all_matches_setting_val.upper():
            return self._match_all(doc)
        else:
            raise ValueError(f"Invalid how_many_matches setting: {how_many_matches}")

    def _match_one(self, doc: Doc) -> ParsedMatch:
        logger.debug("Matching for one result")
        logger.debug("Running the internal matcher")
        all_matches = self._inner_matcher(doc)
        logger.debug(f"Found {len(all_matches)} match(es)")

        logger.debug("Determining the best match")
        best_match = self._get_best_match(all_matches)

        logger.debug(f"Parsing the best match: {best_match}")
        parsed_match = self._parse_match(best_match, doc)

        logger.debug(f"Parsed the best match: {parsed_match}")
        return parsed_match

    def _match_all(self, doc: Doc) -> list[ParsedMatch]:
        logger.debug("Matching for all results")
        logger.debug("Running the internal matcher")
        all_matches: list[Match] = self._inner_matcher(doc)
        logger.debug(f"Found {len(all_matches)} match(es)")

        logger.debug(f"Parsing many matches: {all_matches}")
        parsed: list[ParsedMatch] = [self._parse_match(m, doc) for m in all_matches]

        logger.debug(f"Parsed many matches: {parsed}")
        return parsed

    def _parse_match(self, match: Match, doc: Doc) -> ParsedMatch:
        (match_id, start, end) = match
        rulename: Rulename = nlp.vocab.strings[match_id]
        span: Span = doc[start:end]
        span_features: SpanFeatures = extract_span_features(span)
        logger.debug(f"Parsed ('{rulename}', '{span}') from match '{match}'")
        return (rulename, span, span_features)

    def _get_best_match(self, matches: list[Match]) -> Match:
        # TODO
        logger.debug(f"Getting the best match from {matches}")
        return self._get_longest_match(matches)

    def _get_longest_match(self, matches: list[Match]) -> Match:
        logger.debug(f"Getting the longest match from {matches}")
        distances: list[int] = [end - start for (_, start, end) in matches]
        largest_distance_i: int = distances.index(max(distances))
        return matches[largest_distance_i]

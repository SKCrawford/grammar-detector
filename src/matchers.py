import asyncio
from logging import getLogger
from spacy.matcher import Matcher as SpacyMatcher
from spacy.tokens import Doc, Span, Token
from settings import pattern_set_config
from .extractors import extract_span_features
from .inputs import Input
from .nlp import nlp
from .patterns import PatternSet, Rulename
from .utils import flatten


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

    def __call__(self, input: Input) -> list[ParsedMatch]:
        """The entry point for running the matcher. Using the pattern set provided during construction, the appropriate matcher method will be called. All usable matcher methods should be included here."""
        return self._match(input)

    @property
    def how_many_matches(self) -> str:
        try:
            key: str = pattern_set_config.keys.prop_str("HOW_MANY_MATCHES")
            return str(self._pattern_set.meta[key])
        except:
            return pattern_set_config.values.prop_str("ONE_MATCH")

    @property
    def should_extract_noun_chunks(self) -> bool:
        try:
            key: str = pattern_set_config.keys.prop_str("SHOULD_EXTRACT_NOUN_CHUNKS")
            return bool(self._pattern_set.meta[key])
        except:
            return False

    def _fragment_input(self, input: Input) -> Union[list[Doc], list[Span]]:
        fragmented_input: Union[list[Doc], list[Span]] = []
        if self.should_extract_noun_chunks:
            fragmented_input = input.noun_chunks
            fragmented_input = cast(list[Span], fragmented_input)
        else:
            fragmented_input = input.docs
            fragmented_input = cast(list[Doc], fragmented_input)
        return fragmented_input

    def _match(self, input: Input):
        one_match_setting_val: str = pattern_set_config.values.prop_str("ONE_MATCH")
        all_matches_setting_val: str = pattern_set_config.values.prop_str("ALL_MATCHES")

        if self.how_many_matches.upper() == one_match_setting_val.upper():
            return self._match_one(input)
        elif self.how_many_matches.upper() == all_matches_setting_val.upper():
            return self._match_all(input)
        else:
            raise ValueError(f"Invalid how_many_matches setting: {how_many_matches}")

    def _match_one(self, input: Input) -> list[ParsedMatch]:
        logger.debug("Matching for one result")

        logger.debug("Fragmenting the input")
        fragments = self._fragment_input(input)

        logger.debug(f"Running the matcher against these fragments: {fragments}")
        matches = [self._match_one_fragment(item) for item in fragments]

        logger.debug(f"Returning the parsed matches: {matches}")
        return flatten(matches)

    def _match_one_fragment(self, item: Union[Doc, Span]) -> ParsedMatch:
        logger.debug(f"Running the matcher against '{item}'")
        matches: list[Match] = self._inner_matcher(item)
        logger.debug(f"Found {len(matches)} match(es)")

        logger.debug(f"Getting the best match of these: {matches}")
        best_match: Match = self._get_best_match(matches)

        logger.debug(f"Parsing the best match: {best_match}")
        parsed: ParsedMatch = self._parse_match(best_match)

        logger.debug(f"Parsed the best match: {parsed}")
        return parsed

    def _match_all(self, input: Input) -> list[ParsedMatch]:
        logger.debug("Matching for all results")

        logger.debug("Fragmenting the input")
        fragments = self._fragment_input(input)

        matches_list = [self._match_all_fragment(item) for item in fragments]

        logger.debug(f"Returning all matches: {matches_list}")
        return flatten(matches_list)

    def _match_all_fragment(self, item: Union[Doc, Span]) -> list[ParsedMatch]:
        logger.debug(f"Running the internal matcher against '{item}'")
        matches: list[Match] = self._inner_matcher(item)
        logger.debug(f"Found {len(matches)} match(es)")

        logger.debug(f"Parsing the matches: {matches}")
        parsed: list[ParsedMatch] = [self._parse_match(match) for match in matches]

        logger.debug(f"Parsed the matches: {parsed_matches}")
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

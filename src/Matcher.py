import asyncio
import logging
from spacy.matcher import Matcher as SpacyMatcher
from . import validators
from .extractors import extract_span_features
from .nlp import nlp


logger = logging.getLogger(__name__)


class Matcher:
    def __init__(self):
        self._inner_matcher = None
        self._pattern_set = None

    def match_one(self, pattern_set, doc):
        logger.debug("Preparing to run the external matcher")
        self._pre_match(pattern_set)

        logger.debug("Running the external matcher")
        all_matches = self._run_matcher(doc)
        logger.debug(f"Found '{len(all_matches)}' match(es)")

        logger.debug("Determining the best match")
        best_match = self._get_best_match(all_matches)

        logger.debug(f"Parsing the best match: {best_match}")
        parsed_match = self._parse_match(best_match, doc)

        logger.debug(f"Parsed one match: {parsed_match}")
        return parsed_match

    def match_many(self, pattern_set, doc):
        logger.debug("Preparing to run the external matcher")
        self._pre_match(pattern_set)

        logger.debug("Running the external matcher")
        all_matches = self._run_matcher(doc)
        logger.debug(f"Found '{len(all_matches)}' match(es)")

        logger.debug(f"Parsing many matches: {all_matches}")
        parsed_matches = [self._parse_match(m, doc) for m in all_matches]

        logger.debug(f"Parsed many matches: {parsed_matches}")
        return parsed_matches

    def _pre_match(self, pattern_set):
        logger.debug(f"Creating the internal spaCy matcher")
        self._inner_matcher = self._create_matcher(pattern_set)

    def _on_match(self, matcher, doc, i, matches):
        logger.debug(f"MATCH #{i}")
        logger.debug("Running the on_match callback")
        logger.debug(f"External matcher: {self}")
        logger.debug(f"Internal matcher: {matcher}")
        logger.debug(f"Doc: {doc}")
        logger.debug(f"Matches: {matches}")

    def _create_matcher(self, pattern_set):
        logger.debug("Creating the internal spaCy matcher")
        matcher = SpacyMatcher(nlp.vocab, validate=True)

        logger.debug("Adding the patterns to the internal matcher")
        for p in pattern_set["patterns"]:
            rulename = p["rulename"]
            tokens = p["tokens"]
            config = {
                "greedy": "LONGEST",
                "on_match": self._on_match,
            }
            logger.debug(f"Adding pattern '{rulename}' to the internal matcher")
            matcher.add(rulename, [tokens], **config)
        return matcher

    def _run_matcher(self, doc):
        logger.debug(f"Running the internal matcher on doc '{doc}'")
        return self._inner_matcher(doc)

    def _parse_match(self, match, doc):
        logger.debug(f"Parsing match '{match}'")
        (match_id, start, end) = match
        rulename = nlp.vocab.strings[match_id]
        span = doc[start:end]
        logger.debug(f"Parsed ('{rulename}', '{span}') from match '{match}'")
        return (rulename, span, extract_span_features(span))

    def _get_best_match(self, matches):
        try:
            return matches[-1]
        except IndexError:
            msg = f"No matches were found"
            logger.error(msg)
            raise Exception(msg)

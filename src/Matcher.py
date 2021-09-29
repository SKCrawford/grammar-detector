import asyncio
import logging
from spacy.matcher import Matcher as SpacyMatcher
from . import validators
from .extractors import get_doc
from .nlp import nlp
from .patterns import load_pattern_set


logger = logging.getLogger(__name__)


class Matcher:
    def __init__(self):
        self._inner_matcher = None
        self._pattern_set = None
        self._doc = None

    def match_by_pattern(self, pattern_set_name, maybe_tokenized):
        """Deprecated."""
        return self.match_one(pattern_set_name, maybe_tokenized)

    def match_one(self, pattern_set_name, maybe_tokenized):
        logger.debug("Preparing to run matcher")
        self._pre_match(pattern_set_name, maybe_tokenized)

        logger.debug("Running matcher")
        all_matches = self._run_matcher(self._doc)
        best_match = all_matches[-1]

        logger.debug(f"Parsing one match '{best_match}'")
        return self._parse_match(best_match, self._doc)

    def match_many(self, pattern_set_name, maybe_tokenized):
        logger.debug("Preparing to run matcher")
        self._pre_match(pattern_set_name, maybe_tokenized)

        logger.debug("Running matcher")
        all_matches = self._run_matcher(self._doc)

        logger.debug(f"Parsing many matches '{all_matches}'")
        return [self._parse_match(m) for m in all_matches]

    def _pre_match(self, pattern_set_name, maybe_tokenized):
        logger.debug(f"Loading pattern set '{pattern_set_name}'")
        pattern_set = load_pattern_set(pattern_set_name)

        logger.debug(f"Creating the internal spaCy matcher")
        self._inner_matcher = self._create_matcher(pattern_set)

        logger.debug(f"Tokenizing `{maybe_tokenized}`")
        self._doc = get_doc(maybe_tokenized)

    def _on_match(self, matcher, doc, i, matches):
        logger.debug(f"MATCH #{i}")
        logger.debug("Running on_match callback")
        logger.debug(f"Matcher: '{matcher}'")
        logger.debug(f"Doc: '{doc}'")
        logger.debug(f"Matches: '{matches}'")
        parsed_matches = [self._parse_match(m, doc) for m in matches]
        logger.debug(f"Parsed: '{parsed_matches}'")

    def _create_matcher(self, pattern_set):
        logger.debug("Creating the spaCy matcher")
        matcher = SpacyMatcher(nlp.vocab, validate=True)

        logger.debug("Adding patterns to the spaCy matcher")
        for p in pattern_set:
            match_value = p["rulename"]
            config = {
                "greedy": "LONGEST",
                "on_match": self._on_match,
            }
            matcher.add(match_value, [p["tokens"]], **config)
        return matcher

    def _run_matcher(self, tokenized):
        logger.debug(f"Running the spaCy matcher on tokenized '{tokenized}'")
        return self._inner_matcher(tokenized)

    def _parse_match(self, match, doc):
        logger.debug(f"Parsing match `{match}`")
        (match_id, start, end) = match
        rulename = nlp.vocab.strings[match_id]
        span = doc[start:end]
        return (rulename, span)

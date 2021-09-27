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
        self._instance = None
        self.all_matches = []  # Output of Spacy's matcher (List<(int, int, int)>)
        self.match = None  # Preparsed (Tuple<string, Span>)

    def match_by_pattern(self, pattern_set_filename, maybe_tokenized):
        pattern_set = load_pattern_set(pattern_set_filename)
        self._instance = self._create_matcher(pattern_set)
        self.all_matches = self._run_matcher(maybe_tokenized)
        # <-- On-match callback has already been executed by now
        return self.match

    def _on_match(self, matcher, doc, i, matches):
        """Because Spacy's Matcher on-match callback returns void, an outer class is
        required. Given a Matcher, a Doc, an int, and a List<MatchTuple>, return void.
        """
        # Temporary fix until upgrading to Spacy v3.0
        self.match = self._parse_match(matches[-1], doc)

    def _create_matcher(self, pattern_set):
        logger.debug("Creating the Spacy matcher")
        matcher = SpacyMatcher(nlp.vocab, validate=True)
        logger.debug("Adding patterns to the Spacy matcher")
        [
            matcher.add(p["rulename"], [p["tokens"]], on_match=self._on_match)
            for p in pattern_set
        ]
        return matcher

    def _run_matcher(self, maybe_tokenized):
        logger.debug(f"Tokenizing `{maybe_tokenized}`")
        doc = get_doc(maybe_tokenized)
        logger.debug("Running matcher on tokens")
        # On-match callback happens while calling matcher instance
        return self._instance(doc)

    def _parse_match(self, match, doc):
        logger.debug(f"Parsing match `{match}`")
        (match_id, start, end) = match
        rulename = nlp.vocab.strings[match_id]
        span = doc[start:end]
        return (rulename, span)

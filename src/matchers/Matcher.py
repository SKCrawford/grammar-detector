from logging import getLogger
from spacy.matcher import Matcher as SpacyMatcher
from spacy.tokens import Doc, Span
from typing import Union
from ..nlp import nlp
from ..matches import Match, RawMatch


logger = getLogger(__name__)


class Matcher:
    """A callable Matcher for getting all Matches for the given Doc."""

    def __init__(self):
        self._matcher = SpacyMatcher(nlp.vocab, validate=True)

    def __call__(self, doc: Doc) -> list[Match]:
        """The entrypoint for this Matcher."""
        return self.match_all(doc)

    def match_all(self, doc: Doc) -> list[Match]:
        """Get all Matches for the given Doc."""
        logger.debug(f"Running the Matcher against '{doc}'")
        spacy_matches: list[SpacyMatch] = self._matcher(doc)
        logger.debug(f"Found {len(spacy_matches)} matches: {spacy_matches}")

        matches: list[Match] = [Match(sp_match, doc) for sp_match in spacy_matches]
        logger.debug(f"Created {len(matches)} Matches: {matches}")
        return matches

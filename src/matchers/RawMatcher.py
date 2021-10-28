from logging import getLogger
from spacy.matcher import Matcher as SpacyMatcher
from spacy.tokens import Doc, Span
from typing import Union
from ..nlp import nlp
from ..matches import Match, RawMatch


logger = getLogger(__name__)


class RawMatcher:
    """A callable Matcher for getting all Matches for the given Doc."""

    def __init__(self) -> None:
        logger.debug("Constructing the RawMatcher")
        self._matcher = SpacyMatcher(nlp.vocab, validate=True)

    def __call__(self, doc: Doc) -> list[RawMatch]:
        """Get all matches for the given `Doc`."""
        logger.debug(f"Calling the RawMatcher on '{doc}'")
        raw_matches: list[RawMatch] = self._matcher(doc)
        logger.debug(f"Found {len(raw_matches)} raw matches: {raw_matches}")
        return raw_matches

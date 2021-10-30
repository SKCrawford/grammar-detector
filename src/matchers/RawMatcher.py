from logging import getLogger
from spacy.matcher import Matcher as SpacyMatcher
from spacy.tokens import Doc
from typing import Union
from ..matches import Match, RawMatch
from ..nlp import nlp


logger = getLogger(__name__)


class RawMatcher:
    """A callable Matcher for getting all Matches for the given Doc."""

    def __init__(self) -> None:
        logger.info("Constructing the RawMatcher")
        self._matcher = SpacyMatcher(nlp.vocab, validate=True)

    def __call__(self, doc: Doc) -> list[RawMatch]:
        """Get all matches for the given `Doc`."""
        logger.info(f"Calling the RawMatcher on '{doc}'")
        raw_matches: list[RawMatch] = self._matcher(doc)
        logger.info(f"Found {len(raw_matches)} raw matches: {raw_matches}")
        return raw_matches

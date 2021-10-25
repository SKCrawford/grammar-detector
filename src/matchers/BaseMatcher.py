from logging import getLogger
from spacy.matcher import Matcher as SpacyMatcher
from spacy.tokens import Doc, Span
from typing import Union
from ..nlp import nlp
from .Match import Match, SpacyMatch


logger = getLogger(__name__)


class BaseMatcher:
    def __init__(self):
        self._matcher = SpacyMatcher(nlp.vocab, validate=True)

    def match_all(self, doclike: Union[Doc, Span]) -> list[Match]:
        """Get all Matches for the item."""
        logger.debug(f"Running the matcher against '{doclike}' ({type(doclike)})")
        spacy_matches: list[SpacyMatch] = self._matcher(doclike)
        logger.debug(f"Found {len(spacy_matches)} match(es): {spacy_matches}")

        matches: list[Match] = [Match(sp_match, doclike) for sp_match in spacy_matches]
        logger.debug(f"Created {len(matches)} Match(es): {matches}")
        return matches

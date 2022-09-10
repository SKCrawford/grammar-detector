from logging import getLogger
from spacy.matcher import Matcher as SpacyMatcher
from spacy.tokens import Doc
from ..matches import RawMatch
from ..Nlp import Nlp


logger = getLogger(__name__)


class RawMatcher:
    """A callable Matcher for getting all Matches for the given Doc."""

    def __init__(self) -> None:
        logger.debug("Constructing the RawMatcher")
        self._matcher = SpacyMatcher(Nlp()._nlp.vocab, validate=True)

    def __call__(self, doc: Doc) -> list[RawMatch]:
        """Get all matches for the given `Doc`."""
        raw_matches: list[RawMatch] = self._matcher(doc)
        logger.info(f"Found {len(raw_matches)} raw matches: {raw_matches}")
        return raw_matches

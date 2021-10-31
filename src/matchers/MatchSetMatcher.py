from logging import getLogger
from spacy.tokens import Doc
from .RawMatcher import RawMatcher
from ..matches import MatchSet, RawMatch


logger = getLogger(__name__)


class MatchSetMatcher(RawMatcher):
    def __init__(self) -> None:
        logger.debug("Constructing the MatchSetMatcher")
        super().__init__()

    def __call__(self, doc: Doc) -> MatchSet:
        logger.debug(f"Calling the MatchSetMatcher on '{doc}'")
        raw_matches: list[RawMatch] = super().__call__(doc)
        return MatchSet(raw_matches, doc)

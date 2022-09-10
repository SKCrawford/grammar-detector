from logging import getLogger
from spacy.tokens import Doc
from ..Config import Config
from ..matches import MatchSet, RawMatch
from .RawMatcher import RawMatcher
from ..patterns import PATTERN_SET_DEFAULT_BEST_MATCH, PATTERN_SET_DEFAULT_HOW_MANY_MATCHES


logger = getLogger(__name__)


class MatchSetMatcher(RawMatcher):
    def __init__(
        self,
        best_match: str = PATTERN_SET_DEFAULT_BEST_MATCH,
        how_many_matches: str = PATTERN_SET_DEFAULT_HOW_MANY_MATCHES,
    ) -> None:
        logger.debug("Constructing the MatchSetMatcher")
        super().__init__()
        self.best_match = best_match
        self.how_many_matches = how_many_matches

    def __call__(self, doc: Doc) -> MatchSet:
        logger.debug(f"Calling the MatchSetMatcher on '{doc}'")
        raw_matches: list[RawMatch] = super().__call__(doc)
        return MatchSet(
            raw_matches,
            doc,
            best_match=self.best_match,
            how_many_matches=self.how_many_matches,
        )

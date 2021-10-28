import asyncio
from logging import getLogger
from spacy.matcher import Matcher as SpacyMatcher
from spacy.tokens import Doc, Span, Token
from typing import Callable, Union
from settings import pattern_set_config_values
from ..extractors import extract_span_features
from ..inputs import Input
from ..matches import Match, MatchSet
from ..nlp import nlp
from ..patterns import PatternSet, Rulename
from ..utils import flatten
from .MatchSetMatcher import MatchSetMatcher


CallableManyMatches = Callable[[Input], list[Match]]


logger = getLogger(__name__)


class PatternSetMatcher(MatchSetMatcher):
    """A callable `Matcher` that adds the `Pattern`s of the given `PatternSet` to the underlying matcher."""

    def __init__(self, pattern_set: PatternSet) -> None:
        logger.debug("Constructing the PatternSetMatcher")
        super().__init__()
        self.pattern_set: PatternSet = pattern_set

        logger.debug(
            f"Registering the '{self.pattern_set.name}' PatternSet's Patterns to the internal matcher"
        )
        for pattern in self.pattern_set.get_all_patterns():
            spacy_config: dict[str, str] = {"greedy": "LONGEST"}
            logger.debug(f"Adding the Pattern '{pattern.rulename}'")
            self._matcher.add(pattern.rulename, [pattern.tokens], **spacy_config)

from logging import getLogger
from ..patterns import PatternSet
from .MatchSetMatcher import MatchSetMatcher


logger = getLogger(__name__)


class PatternSetMatcher(MatchSetMatcher):
    """A callable `Matcher` that adds the `Pattern`s of the given `PatternSet` to the underlying matcher."""

    def __init__(self, pattern_set: PatternSet) -> None:
        logger.info("Constructing the PatternSetMatcher")
        super().__init__()
        self.pattern_set: PatternSet = pattern_set

        logger.info(f"Registering the '{self.pattern_set.name}' PatternSet's Patterns")
        for pattern in self.pattern_set.get_all_patterns():
            spacy_config: dict[str, str] = {"greedy": "LONGEST"}
            logger.debug(f"Registering the '{pattern.rulename}' Pattern")
            self._matcher.add(pattern.rulename, [pattern.tokens], **spacy_config)

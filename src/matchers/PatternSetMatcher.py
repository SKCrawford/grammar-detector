from logging import getLogger
from ..patterns import Pattern, PatternSet
from .MatchSetMatcher import MatchSetMatcher


logger = getLogger(__name__)


class PatternSetMatcher(MatchSetMatcher):
    """A callable `Matcher` that adds the `Pattern`s of the given `PatternSet` to the underlying matcher."""

    def __init__(self, pattern_set: PatternSet) -> None:
        logger.info("Constructing the PatternSetMatcher")
        super().__init__()
        self.pset: PatternSet = pattern_set

        logger.info(f"Registering the Patterns for the '{self.pset.name}' PatternSet")
        for pattern_key in self.pset.patterns:
            pattern: Pattern = self.pset.patterns[pattern_key]
            spacy_config: dict[str, str] = {"greedy": "LONGEST"}
            logger.debug(f"Registering the '{pattern.rulename}' Pattern")
            self._matcher.add(pattern.rulename, [pattern.tokens], **spacy_config)

from logging import getLogger
from ..patterns import Pattern, PatternSet
from .MatchSetMatcher import MatchSetMatcher


logger = getLogger(__name__)


class PatternSetMatcher(MatchSetMatcher):
    """A callable `Matcher` that adds the `Pattern`s of the given `PatternSet` to the underlying matcher."""

    def __init__(self, pattern_set: PatternSet) -> None:
        logger.debug("Constructing the PatternSetMatcher")
        super().__init__(
            best_match=pattern_set.best_match,
            how_many_matches=pattern_set.how_many_matches,
        )
        self.pset: PatternSet = pattern_set

        logger.info(
            f"Adding {len(self.pset.patterns)} Patterns to '{self.pset.name}' PatternSetMatcher"
        )
        for pattern_key in self.pset.patterns:
            pattern: Pattern = self.pset.patterns[pattern_key]
            spacy_config: dict[str, str] = {"greedy": "LONGEST"}
            logger.debug(f"Adding the '{pattern.rulename}' Pattern")
            self._matcher.add(pattern.rulename, [pattern.tokens], **spacy_config)

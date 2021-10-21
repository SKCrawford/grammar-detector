from logging import getLogger
from typing import Optional
from settings import pattern_set_config_keys
from ..cache import Cacheable
from .Pattern import Pattern
from .PatternSet import MetaDict, PatternSet, Test


logger = getLogger(__name__)


# TODO fix the terrible typings
class PatternSetRepository(Cacheable):
    """The class for creating, caching, and retrieving PatternSet instances."""

    def create(self, name: str, pattern_set_data: dict[str, Any]) -> PatternSet:
        """Create a new PatternSet instance, cache it, and return it."""
        if self.is_key_in_cache(name):
            return self.get_one_from_cache(name)

        # Extract the pattern data
        patterns_key: str = pattern_set_config_keys.prop("PATTERNS")
        patterns_data = pattern_set_data[patterns_key]

        # Extract the meta config
        meta_key: str = pattern_set_config_keys.prop("META")
        meta: MetaDict = {}
        if meta_key in pattern_set_data:
            meta = pattern_set_data[meta_key]

        # Extract the tests
        tests_key: str = pattern_set_config_keys.prop("TESTS")
        tests: list[Test] = []
        if tests_key in pattern_set_data:
            tests = pattern_set_data[tests_key]

        # Create and add patterns to the patternset
        pattern_set = PatternSet(name)
        for pattern_data in patterns_data:
            self.register_pattern(pattern_data, pattern_set)

        pattern_set.meta = meta
        pattern_set.tests = tests

        self.save_to_cache(pattern_set.name, pattern_set)
        return pattern_set

    def get_all(self) -> list[PatternSet]:
        """Return all cached PatternSet instances."""
        return self.retrieve_all_from_cache()

    def get_one(self, name: str) -> PatternSet:
        """Return one cached PatternSet instance."""
        if not self.is_key_in_cache(name):
            msg = f"PatternSet '{name}' is not in the repository."
            logger.error(msg)
            raise KeyError(msg)
        return self.retrieve_one_from_cache(name)

    def register_pattern(
        self,
        pattern_data: dict[str, Any],
        pattern_set: PatternSet,
    ) -> None:
        """Extract the components of the raw pattern data, create a Pattern, and add it to the PatternSet."""
        rulename_key: str = pattern_set_config_keys.prop("RULENAME")
        rulename: str = pattern_data[rulename_key]

        tokens_key: str = pattern_set_config_keys.prop("TOKENS")
        tokens: list[Token] = pattern_data[tokens_key]

        pattern = Pattern(rulename, tokens)
        pattern_set.patterns[pattern.name] = pattern

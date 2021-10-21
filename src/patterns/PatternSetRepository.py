from logging import getLogger
from spacy.tokens import Token
from typing import Optional
from settings import pattern_set_config_keys
from ..cache import Cacheable
from .Pattern import extract_pattern_data, Pattern, PatternData
from .PatternSet import extract_pattern_set_data, Meta, PatternSet, PatternSetData, 
from .PatternSet import Name as PatternSetName


logger = getLogger(__name__)


class PatternSetRepository(Cacheable):
    """The class for creating, caching, and retrieving PatternSet instances."""

    def create(self, name: PatternSetName, data: PatternSetData) -> PatternSet:
        """Create a new PatternSet instance, cache it, and return it. If a PatternSet with the same name has already been created, the cached instance will be returned."""
        if self.cache.has_key(name):
            return self.cache.get_one(name)

        (pattern_data_list, meta, tests) = extract_pattern_set_data(data)
        pattern_set = PatternSet(name)
        pattern_set.meta = meta
        pattern_set.tests = tests
        for pattern_data in pattern_data_list:
            self.register_pattern(pattern_data, pattern_set)

        self.cache.save(pattern_set.name, pattern_set)
        return pattern_set

    def get_all(self) -> list[PatternSet]:
        """Return all cached PatternSet instances."""
        return self.cache.get_all()

    def get_one(self, name: PatternSetName) -> PatternSet:
        """Return one cached PatternSet instance."""
        if not self.cache.has_key(name):
            msg = f"PatternSet '{name}' is not in the repository."
            logger.error(msg)
            raise KeyError(msg)
        return self.cache.get_one(name)

    def register_pattern(self, data: PatternData, pattern_set: PatternSet) -> None:
        """Extract the components of the raw pattern data, create a Pattern, and add it to the PatternSet."""
        (rulename, tokens) = extract_pattern_data(data)
        pattern_set.add_pattern(Pattern(rulename, tokens))

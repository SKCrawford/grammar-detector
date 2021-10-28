from logging import getLogger
from typing import cast
from ..repositories import BeforeSaveCallback, CacheKeyCallback, Repository
from ..utils import singleton
from .Pattern import extract_pattern_data, Pattern, PatternData
from .PatternSet import extract_pattern_set_data, Name, PatternSet, PatternSetData


logger = getLogger(__name__)


@singleton
class PatternSetRepository(Repository):
    def __init__(self):
        make_cache_key: CacheKeyCallback = lambda pset: pset.name  # Callable[[T], str]
        super().__init__(PatternSet, cache_key=make_cache_key)

    def create(self, name: Name, data: PatternSetData) -> PatternSet:
        """Create a new `PatternSet`, cache it, and return it. If a `PatternSet` with the same name has already been created, the cached instance will be returned."""
        if self.cache.has_key(name):
            return self.get_one(name)

        # Callable[[T], T]
        before_save: BeforeSaveCallback = lambda pset: self._before_save(pset, data)
        return super().create(name, before_save=before_save)

    def _before_save(self, pset: PatternSet, data: PatternSetData) -> PatternSet:
        (pattern_data_list, meta, tests) = extract_pattern_set_data(data)
        logger.debug(
            f"Loading {len(meta.keys())} meta options for the '{pset.name}' PatternSet"
        )
        pset.meta = meta

        logger.debug(f"Loading {len(tests)} tests for the '{pset.name}' PatternSet")
        pset.tests = tests

        logger.debug(
            f"Loading {len(pattern_data_list)} patterns for the '{pset.name}' PatternSet"
        )
        [self._register_pattern(p_data, pset) for p_data in pattern_data_list]
        return pset

    def _register_pattern(self, data: PatternData, pattern_set: PatternSet) -> None:
        """Extract the components of the raw PatternData, create a Pattern, and add it to the PatternSet."""
        (rulename, tokens) = extract_pattern_data(data)
        logger.debug(f"Registering the '{rulename}' Pattern")
        pattern_set.add_pattern(Pattern(rulename, tokens))

from logging import getLogger
from typing import cast
from ..repositories import Repository
from ..utils import singleton
from .Pattern import PatternData
from .PatternSet import Name, PatternSet, PatternSetData


logger = getLogger(__name__)


@singleton
class PatternSetRepository(Repository):
    def __init__(self):
        logger.debug("Constructing the PatternSetRepository")
        super().__init__(PatternSet, cache_key=lambda pset: pset.name)

    def create(self, *args, **kwargs) -> PatternSet:
        """Create a new `PatternSet`, cache it, and return it. If a `PatternSet` with the same name has already been created, the cached instance will be returned."""
        # TODO move this logic to Repository
        name = args[0]
        if self.cache.has_key(name):
            logger.info(f"Getting an existing '{name}' PatternSet")
            return self.get_one(name)

        # Callable[[T], T]
        logger.info(f"Creating a new '{name}' PatternSet")
        return super().create(*args, **kwargs)

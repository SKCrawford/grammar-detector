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
        super().__init__(PatternSet)

    def cache_key(self, *args: str, **kwargs: str) -> str:
        name: str = args[0]
        return name

    def create(self, *args: str, **kwargs: str) -> PatternSet:
        """Create a new `PatternSet`, cache it, and return it. If a `PatternSet` with the same name has already been created, the cached instance will be returned."""
        name: str = self.cache_key(*args, **kwargs)
        logger.info(f"Creating or retrieving the '{name}' PatternSet")
        return super().create(*args, **kwargs)

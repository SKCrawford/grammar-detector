from logging import getLogger
from typing import cast, Union
from settings import pattern_set_config
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

    def cache_key(self, name: Name, data: PatternSetData) -> str:
        return name

    def create(self, name: Name, data: PatternSetData) -> PatternSet:
        """Create a new `PatternSet`, cache it, and return it. If a `PatternSet` with the same name has already been created, the cached instance will be returned."""
        logger.info(f"Creating or retrieving the '{name}' PatternSet")
        return super().create(name, data)

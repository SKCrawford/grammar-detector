import asyncio
from logging import getLogger
from ..Repository import Repository
from ..utils import singleton
from .PatternSet import PatternSet, PatternSetData


logger = getLogger(__name__)


@singleton
class PatternSetRepository(Repository):
    def __init__(self):
        logger.debug("Constructing the PatternSetRepository")
        super().__init__(PatternSet)

    def cache_key(self, name: str, data: PatternSetData) -> str:
        return name

    async def create(self, name: str, data: PatternSetData) -> PatternSet:
        """Create a new `PatternSet`, cache it, and return it. If a `PatternSet` with the same name has already been created, the cached instance will be returned."""
        logger.info(f"Creating or retrieving the '{name}' PatternSet")
        stop_timer = self.tk.start(f"Create the '{name}' PatternSet")
        pattern_set: PatternSet = await super().create(name, data)
        stop_timer()
        return pattern_set

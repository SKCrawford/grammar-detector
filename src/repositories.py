from logging import getLogger
from typing import Callable, Generic, TypeVar
from .cache import Cache


T = TypeVar("T")


logger = getLogger(__name__)


class Repository(Generic[T]):
    def __init__(self, klass: T) -> None:
        """Create a repository for the specified `klass`."""
        logger.info(f"Constructing the Repository[{klass}]")
        self._klass: T = klass
        self.cache: Cache = Cache()

    def cache_key(self, *args, **kwargs) -> str:
        msg = "make_cache_key method was not overridden"
        logger.error(msg)
        raise NotImplementedError(msg)

    def create(self, *args: str, **kwargs: str) -> T:
        """When saving the instance to the cache, its key is created by the overriden `make_cache_key` method."""
        logger.debug("Making the cache key")
        cache_key: str = self.cache_key(*args, **kwargs)

        logger.debug(f"Checking the cache for key '{cache_key}'")
        if self.cache.has_key(cache_key):
            return self.get_one(cache_key)

        logger.debug(f"Constructing the {self._klass}")
        instance: T = self._klass(*args, **kwargs)

        logger.debug(f"Caching {self._klass} instance to key '{cache_key}'")
        self.cache.save(cache_key, instance)
        return self.get_one(cache_key)

    def get_all(self) -> list[T]:
        logger.debug(f"Getting all instances of {self._klass}")
        return self.cache.get_all()

    def get_one(self, cache_key: str) -> T:
        logger.debug(f"Getting the '{cache_key}' {self._klass}")
        return self.cache.get_one(str(cache_key))

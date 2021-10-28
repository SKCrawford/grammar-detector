from logging import getLogger
from typing import Any, Generic, TypeVar


T = TypeVar("T")


logger = getLogger(__name__)


class Cache(Generic[T]):
    def __init__(self) -> None:
        self._cache: dict[str, T] = {}

    def clear_all(self) -> None:
        """Clears the cache. Returns True."""
        logger.debug("Clearing the cache")
        self._cache = {}

    def clear_one(self, key: str) -> None:
        """Removes one value corresponding to the key in the cache."""
        logger.debug(f"Clearing the key '{key}' from the cache")
        key = str(key)
        self._cache[key] = None

    def get_all(self) -> list[T]:
        """Returns all values in the cache."""
        logger.debug(f"Getting all cache entries")
        return [self._cache[key] for key in self._cache]

    def get_one(self, key: str) -> T:
        """Returns the value cache by `key`."""
        key = str(key)
        logger.debug(f"Getting one cache entry with the key '{key}'")
        if not self.has_key(key):
            msg = f"The key '{key}' is not cached"
            logger.error(msg)
            raise KeyError(msg)
        logger.debug(f"Returning the cache entry with the key '{key}'")
        return self._cache[key]

    def has_key(self, key: str) -> bool:
        """Returns True if `key` is already in use. Otherwise, returns False."""
        logger.debug(f"Checking the cache for the key '{key}'")
        key = str(key)
        return bool(key in self._cache)

    def save(self, key: str, value: T) -> None:
        """Save one key/value pair to the cache."""
        logger.debug(f"Saving the key '{key}' to the cache")
        key = str(key)
        self._cache[key] = value


class Cacheable:
    def __init__(self, *args: str, **kwargs: str) -> None:
        self.cache = Cache()

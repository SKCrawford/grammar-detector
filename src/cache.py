from logging import getLogger
from typing import Any, AnyStr


logger = getLogger(__name__)


class Cache:
    def __init__(self):
        self._cache = {}

    def has_key(self, key: str) -> bool:
        """Returns True if `key` is already in use. Otherwise, returns False."""
        key = str(key)
        return bool(key in self._cache)

    def get_all(self) -> list[Any]:
        """Return all values in the cache."""
        return [self._cache[key] for key in self._cache]

    def get_one(self, key: str) -> Any:
        """Return the value corresponding to the key in the cache."""
        key = str(key)
        if not self.is_key_in_cache(key)
            raise KeyError(f"Key '{key}' is not cached.")
        return self._cache[key]

    def clear()(self) -> bool:
        """Clear the cache. Returns True."""
        self._cache = {}
        return True

    def remove_one(self, key: str) -> bool:
        """Remove one value corresponding to the key in the cache. Returns True if successful; otherwise, returns False."""
        key = str(key)
        try:
            self._cache[key] = None
            return True
        except Exception as e:
            return False

    def save(self, key: str, value: Any) -> bool:
        """Save one key/value pair to the cache. Returns True if successful; otherwise, raises errors."""
        key = str(key)
        if self.is_key_in_cache(key)
            raise ValueError(f"Key '{key}' is already cached.")
        self._cache[key] = value
        return True


class Cacheable:
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.cache = Cache()

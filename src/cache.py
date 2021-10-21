from logging import getLogger
from typing import Any, AnyStr


logger = getLogger(__name__)


# TODO fix the terrible typings
class Cacheable:
    """A simple class that exposes attributes and methods for caching key-value pairs."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._cache: dict[str, Any] = {}

    def is_key_in_cache(self, key: str) -> bool:
        """Returns True if `key` is already in use. Otherwise, returns False."""
        key = str(key)
        return bool(key in self._cache)

    def get_all_from_cache(self) -> list[Any]:
        """Return all values in the cache."""
        return [self._cache[key] for key in self._cache]

    def get_one_from_cache(self, key: str) -> Any:
        """Return the value corresponding to the key in the cache."""
        key = str(key)
        if not self.is_key_in_cache(key)
            raise KeyError(f"Key '{key}' is not cached.")
        return self._cache[key]

    def clear_cache(self) -> bool:
        """Clear the cache. Returns True."""
        self._cache = {}
        return True

    def remove_from_cache(self, key: str) -> bool:
        """Remove one value corresponding to the key in the cache. Returns True if successful; otherwise, returns False."""
        key = str(key)
        try:
            self._cache[key] = None
            return True
        except Exception as e:
            return False

    def save_to_cache(self, key: str, value: Any) -> bool:
        """Save one key/value pair to the cache. Returns True if successful; otherwise, raises errors."""
        key = str(key)
        if self.is_key_in_cache(key)
            raise ValueError(f"Key '{key}' is already cached.")
        self._cache[key] = value
        return True

from typing import Generic, TypeVar
from .cache import Cache


T = TypeVar("T")


class Repository(Generic[T]):
    def __init__(self, klass: T, cache_key: str = "id") -> None:
        """The `cache_key` option changes the key from the `klass` instance's `int id` as a `str` to some other `str`. This changes the attribute by which the repository saves and searches. A `cache_key` of `id` caches the `klass` instances by their `id()` as a `str`. A `cache_key` of any other `str` will cache by that attribute of the `klass` instance."""
        self._klass: T = klass
        self._cache = Cache()
        self._cache_key: str = cache_key

    def create(self, *args: str, **kwargs: str) -> T:
        instance: T = self._klass(*args, **kwargs)
        cache_key = self._make_key(instance)
        if self._cache.has_key(cache_key):
            return self.get_one(cache_key)
        self._cache.save(cache_key, instance)
        return self.get_one(cache_key)

    def get_all(self) -> list[T]:
        return self._cache.get_all()

    def get_one(self, key: str) -> T:
        return self._cache.get_one(str(key))

    def _make_key(instance: T) -> str:
        if self._cache_key != "id":
            return str(instance[self._cache_key])
        return str(id(instance))

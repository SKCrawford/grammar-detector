from typing import Generic, TypeVar
from .cache import Cache


T = TypeVar("T")


class Repository(Generic[T]):
    def __init__(self, klass: T) -> None:
        self._klass = klass
        self._cache = Cache()

    def create(self, *args, **kwargs) -> T:
        instance = self._klass(*args, **kwargs)
        self._cache.save(id(instance), instance)
        return instance

    def get_all(self) -> list[T]:
        return self._cache.get_all()

    def get_one(self, id: int) -> T:
        id = int(id)
        return self._cache.get_one(id)

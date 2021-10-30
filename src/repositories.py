from logging import getLogger
from typing import Callable, Generic, TypeVar
from .cache import Cache


T = TypeVar("T")
BeforeSaveCallback = Callable[[T], T]
CacheKeyCallback = Callable[[T], str]


logger = getLogger(__name__)


def get_object_id(t: T) -> str:
    return str(id(t))


def noop(t: T) -> T:
    return t


class Repository(Generic[T]):
    def __init__(self, klass: T, cache_key: CacheKeyCallback = get_object_id) -> None:
        """Create a repository for the specified `klass`. The `cache_key` callback takes a `klass` instance and returns a `str` to be used as the cache key, defaulting to the instance's `id` as a `str`."""
        # logger.debug(f"Constructing the Repository[{klass}]")
        logger.info(f"Constructing the Repository[{klass}]")
        self._klass: T = klass
        self.cache = Cache()
        self.make_cache_key: CacheKeyCallback = cache_key

    def create(
        self,
        *args: str,
        before_save: BeforeSaveCallback = noop,
        **kwargs: str,
    ) -> T:
        """Run the `before_save` callback after creating the `klass` instance but before saving it to the cache, permitting changes to be made pre-save. When saving the instance to the cache, its key is created by the `cache_key` callback that was provided to the Repository's constructor."""
        # logger.debug(f"Constructing the {self._klass}")
        logger.info(f"Constructing the {self._klass}")
        instance: T = self._klass(*args, **kwargs)

        logger.debug("Running the before_save callback")
        instance = before_save(instance)

        logger.debug("Running the cache_key callback")
        cache_key: str = self.make_cache_key(instance)

        logger.info(f"Saving the '{cache_key}' {self._klass} instance")
        self.cache.save(cache_key, instance)
        return self.get_one(cache_key)

    def get_all(self) -> list[T]:
        logger.debug(f"Getting all instances of {self._klass}")
        return self.cache.get_all()

    def get_one(self, cache_key: str) -> T:
        logger.debug(f"Getting the '{cache_key}' {self._klass}")
        return self.cache.get_one(str(cache_key))

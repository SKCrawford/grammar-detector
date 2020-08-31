import logging
from functools import wraps
from . import validator


logger = logging.getLogger(__name__)


def is_in_enum(enum):
    """A decorator wrapping the is_in_enum validator.

    Given an Enum, return a function decorator.
    """
    def decorator(fn):
        @wraps(fn)
        def wrapper(*w_args, **w_kwargs):
            value = w_args[0]
            validator.is_in_enum(value, enum)
            return fn(*w_args, **w_kwargs)
        return wrapper
    return decorator


def is_truthy(fn):
    """A decorator wrapping the is_truthy validator. Does not accept arguments."""
    @wraps(fn)
    def wrapper(*w_args, **w_kwargs):
        value = w_args[0]
        validator.is_truthy(value)
        return fn(*w_args, **w_kwargs)
    return wrapper


def is_type(type_):
    """A decorator wrapping the is_in_enum validator.

    Given a type, return a function decorator.
    """
    def decorator(fn):
        @wraps(fn)
        def wrapper(*w_args, **w_kwargs):
            value = w_args[0]
            validator.is_type(value, type_)
            return fn(*w_args, **w_kwargs)
        return wrapper
    return decorator


# source: https://riptutorial.com/python/example/10954/create-singleton-class-with-a-decorator
def singleton(klass):
    """A class decorator adding singleton functionality."""
    instances = [None]
    def wrapper(*args, **kwargs):
        logger.debug(f"Looking for a pre-existing instance of `{klass}`")
        instance = instances[0]
        if instance is None:
            logger.debug("Didn't find a pre-existing instance")
            logger.debug("Creating a new instance")
            instance = klass(*args, **kwargs)
            instances[0] = instance
        logger.debug(f"Returning the instance `{instance}`")
        return instance
    return wrapper

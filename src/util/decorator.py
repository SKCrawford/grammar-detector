from functools import wraps
from .validator import is_in_enum as is_in_enum_validate
from .validator import is_truthy as is_truthy_validate
from .validator import is_type as is_type_validate


def is_in_enum(enum):
    """A decorator wrapping the is_in_enum validator.

    Given an Enum, return a function decorator.
    """
    def decorator(fn):
        @wraps(fn)
        def wrapper(*w_args, **w_kwargs):
            value = w_args[0]
            is_in_enum_validate(value, enum)
            return fn(*w_args, **w_kwargs)
        return wrapper
    return decorator


def is_truthy(fn):
    """A decorator wrapping the is_truthy validator. Does not accept arguments."""
    @wraps(fn)
    def wrapper(*w_args, **w_kwargs):
        value = w_args[0]
        is_truthy_validate(value)
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
            is_type_validate(value, type_)
            return fn(*w_args, **w_kwargs)
        return wrapper
    return decorator


# source: https://riptutorial.com/python/example/10954/create-singleton-class-with-a-decorator
def singleton(klass):
    """A class decorator adding singleton functionality."""
    instances = [None]
    def wrapper(*args, **kwargs):
        if instances[0] is None:
            instances[0] = klass(*args, **kwargs)
        return instances[0]
    return wrapper

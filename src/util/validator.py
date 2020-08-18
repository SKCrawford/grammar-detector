def is_in_enum(value, enum):
    """Return True if a value matches one of the values in an enum. Otherwise,
    return False.

    Given a string and an Enum class, return a boolean.
    """
    was_found = False
    for name, member in enum.__members__.items():
        if value == member.value:
            was_found = True
    if not was_found:
        raise ValueError(f"expected an enum {enum} value but got {value}")
    return value


def is_truthy(value):
    """Raise a ValueError if the value is not truthy.

    Given an object, return void.
    """
    if not bool(value):
        raise ValueError(f"expected a truthy value but got {value}")
    return value


def is_type(value, type_):
    """Raise a TypeError if the value is not of the specified type.
    
    Given an object and a type, return void.
    """
    if not isinstance(value, type_):
        raise TypeError(f"expected a {type_} but got {type(value)}")
    return value

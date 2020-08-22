def is_in_enum(value, enum):
    """Raise a ValueError if the value is not in the enum.

    Given a string and an Enum class, return a boolean.
    """
    was_found = False
    for name, member in enum.__members__.items():
        if value == member.value:
            was_found = True
    if not was_found:
        raise ValueError(f"expected an {enum} value but got {value}")


def is_not_type(value, type_):
    """Raise a TypeError if the value is of the specified type.

    Given an object and a type, return void.
    """
    if isinstance(value, type_):
        raise TypeError(f"expected a value not of type {type_}")


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

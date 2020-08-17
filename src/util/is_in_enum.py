def is_in_enum(value, enum):
    """Return True if a value matches one of the values in an enum. Otherwise,
    return False.

    Given a string and an Enum class, return a boolean.
    """

    for name, member in enum.__members__.items():
        if value == member.value:
            return True
    return False

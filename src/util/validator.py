import logging


def is_in_enum(value, enum):
    """Raise a ValueError if the value is not in the enum.

    Given a string and an Enum class, return a boolean.
    """
    logger = logging.getLogger(is_in_enum.__name__)
    logger.debug(f"Validating value `{value}` for enum `{enum}`")
    was_found = False
    for name, member in enum.__members__.items():
        if value == member.value:
            was_found = True
    if not was_found:
        err_msg = "Invalid"
        logger.error(err_msg)
        raise ValueError(err_msg)
    logger.debug("Valid")


def is_not_type(value, type_):
    """Raise a TypeError if the value is of the specified type.

    Given an object and a type, return void.
    """
    logger = logging.getLogger(is_not_type.__name__)
    logger.debug(f"Validating value `{value}` is not of type `{type_}`")
    if isinstance(value, type_):
        err_msg = "Invalid"
        logger.error(err_msg)
        raise TypeError(err_msg)
    logger.debug(f"Valid: value is of type `{type(value)}`")


def is_truthy(value):
    """Raise a ValueError if the value is not truthy.

    Given an object, return void.
    """
    logger = logging.getLogger(is_truthy.__name__)
    logger.debug(f"Validating value `{value}`")
    if not bool(value):
        err_msg = "Invalid"
        logger.error(err_msg)
        raise ValueError(err_msg)
    logger.debug(f"Valid")

def is_type(value, type_):
    """Raise a TypeError if the value is not of the specified type.

    Given an object and a type, return void.
    """
    logger = logging.getLogger(is_type.__name__)
    logger.debug(f"Validating value `{value}` is of type `{type_}`")
    if not isinstance(value, type_):
        err_msg = "Invalid: value is of type `{type(value)}`"
        logger.error(err_msg)
        raise ValueError(err_msg)
    logger.debug("Valid")

import logging


def is_in_enum(value, enum):
    """Raise a ValueError if the value is not in the enum.

    Given a string and an Enum class, return a boolean.
    """
    logger = logging.getLogger(is_in_enum.__name__)
    logger.debug(f"Validating value `{value}` is in enum `{enum}`")
    was_found = False
    for name, member in enum.__members__.items():
        if value == member.value:
            was_found = True
    if not was_found:
        err_msg = f"Value `{value}` is not in enum `{enum}`"
        logger.error(err_msg)
        raise ValueError(err_msg)
    logger.debug(f"Value `{value}` is in enum `{enum}`")


def is_not_type(value, type_):
    """Raise a TypeError if the value is of the specified type.

    Given an object and a type, return void.
    """
    logger = logging.getLogger(is_not_type.__name__)
    logger.debug(f"Validating value `{value}` is not of type `{type_}`")
    if isinstance(value, type_):
        err_msg = f"Value `{value}` is of type `{type_}`"
        logger.error(err_msg)
        raise TypeError(err_msg)
    logger.debug(f"Value `{value}` is not of type `{type_}`")


def is_truthy(value):
    """Raise a ValueError if the value is not truthy.

    Given an object, return void.
    """
    logger = logging.getLogger(is_truthy.__name__)
    logger.debug(f"Validating value `{value}` is truthy")
    if not bool(value):
        err_msg = f"Value `{value}` is not truthy"
        logger.error(err_msg)
        raise ValueError(err_msg)
    logger.debug(f"Value `{value}` is truthy")

def is_type(value, type_):
    """Raise a TypeError if the value is not of the specified type.

    Given an object and a type, return void.
    """
    logger = logging.getLogger(is_type.__name__)
    logger.debug(f"Validating value `{value}` is of type `{type_}`")
    if not isinstance(value, type_):
        raise TypeError(f"expected a `{type_} but got {type(value)}`")
        err_msg = f"Value `{value}` is not of type `{type_} but of type {type(value)}`"
        logger.error(err_msg)
        raise ValueError(err_msg)
    logger.debug(f"Value `{value}` is of type `{type_}`")

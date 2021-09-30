import logging
from spacy.tokens import Doc, Span
from .nlp import nlp  # TODO make nlp an arg for dep inj


logger = logging.getLogger(__name__)


def is_in_enum(value, enum):
    """Raise a ValueError if the value is not in the enum.

    Given a string and an Enum class, return a boolean.
    """
    logger.debug(f"Validating '{value}' for enum '{enum}'")
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
    logger.debug(f"Validating '{value}' is not of type '{type_}'")
    if isinstance(value, type_):
        err_msg = "Invalid"
        logger.error(err_msg)
        raise TypeError(err_msg)
    logger.debug(f"Valid: type is '{type(value)}'")


def is_tokenized(maybe_tokenized):
    """Given any type, return a boolean."""
    logger.debug(f"Validating '{maybe_tokenized}'")
    is_not_type(maybe_tokenized, type(None))
    is_truthy(maybe_tokenized)

    logger.debug("Determining if input is already tokenized")
    if isinstance(maybe_tokenized, str):
        logger.debug("Not tokenized")
        return False
    elif isinstance(maybe_tokenized, Doc) or isinstance(maybe_tokenized, Span):
        logger.debug("Already tokenized")
        return True

    err_msg = f"Expected a string, Doc, or Span but got '{type(maybe_tokenized)}'"
    logger.error(err_msg)
    raise TypeError(err_msg)


def is_truthy(value):
    """Raise a ValueError if the value is not truthy.

    Given an object, return void.
    """
    logger.debug(f"Validating '{value}'")
    if not bool(value):
        err_msg = "Invalid"
        logger.error(err_msg)
        raise ValueError(err_msg)
    logger.debug("Valid")


def is_type(value, type_):
    """Raise a TypeError if the value is not of the specified type.

    Given an object and a type, return void.
    """
    logger.debug(f"Validating '{value}' is of type '{type_}'")
    if not isinstance(value, type_):
        err_msg = f"Invalid: type is '{type(value)}'"
        logger.error(err_msg)
        raise TypeError(err_msg)
    logger.debug("Valid")

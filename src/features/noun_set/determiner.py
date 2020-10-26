import logging
from enum import Enum
from src.core import match_by_pattern
from src.core.matcher.parse import parse_match
from src.util.decorator import is_in_enum, is_not_type, is_truthy, is_type


logger = logging.getLogger(__name__)


class Determiner(Enum):
    """All possible English determiners."""

    DEFINITE = "definite"
    INDEFINITE = "indefinite"
    OTHER = "other"
    NONE = "none"


@is_type((str, type(None)))
def is_noun_determiner(determiner):
    if type(determiner) is str and determiner == "":
        raise ValueError(f"Invalid: determiner is an empty string")


@is_type(str)
@is_truthy
@is_in_enum(Determiner)
def is_noun_determiner_type(determiner_type):
    pass


def detect_noun_determiner(maybe_tokenized):
    logger.debug("Started detecting")
    matches = match_by_pattern("determiners", maybe_tokenized)
    (determiner_type, span) = matches[0]
    is_noun_determiner_type(determiner_type)

    determiner = None
    if determiner_type != Determiner.NONE.value:
        determiner = span[0].text
    is_noun_determiner(determiner) 
    return (determiner, determiner_type)

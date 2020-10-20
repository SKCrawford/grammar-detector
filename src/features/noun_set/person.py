import logging
from enum import Enum
from src.core import match_by_pattern


logger = logging.getLogger(__name__)


class Person(Enum):
    """All possible English sentence persons."""

    FIRST = "1st"
    SECOND = "2nd"
    THIRD = "3rd"


def detect_noun_person(maybe_tokenized):
    logger.debug("Started detecting")
    matches = match_by_pattern("persons", maybe_tokenized)
    (person, span) = matches[0]
    return person

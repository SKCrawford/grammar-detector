import asyncio
import logging
from enum import Enum
from src.core import match_by_pattern
from src.util.validator import is_in_enum, is_truthy, is_type


logger = logging.getLogger(__name__)


class Person(Enum):
    """All possible English sentence persons."""

    FIRST = "1st"
    SECOND = "2nd"
    THIRD = "3rd"


def is_noun_person(person):
    is_type(person, str)
    is_truthy(person)
    is_in_enum(person, Person)


async def detect_noun_person(maybe_tokenized):
    logger.debug("Started detecting")
    matches = await match_by_pattern("persons", maybe_tokenized)
    (person, span) = matches[0]
    is_noun_person(person)
    return person

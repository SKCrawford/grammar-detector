import logging
from enum import Enum
from src.core import match_by_pattern
from src.util.validator import is_in_enum, is_truthy, is_type


logger = logging.getLogger(__name__)


class Voice(Enum):
    """All possible English sentence voices."""

    ACTIVE = "active"
    PASSIVE = "passive"
    UNKNOWN = "???"


def is_verb_voice(voice):
    is_type(voice, str)
    is_truthy(voice)
    is_in_enum(voice, Voice)


def detect_verb_voice(maybe_tokenized):
    logger.debug("Started detecting")
    matches = match_by_pattern("voices", maybe_tokenized)
    (voice, span) = matches[0]
    is_verb_voice(voice)
    return voice

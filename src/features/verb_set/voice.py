import logging
from enum import Enum
from src.core import match_by_pattern


logger = logging.getLogger(__name__)


class Voice(Enum):
    """All possible English sentence voices."""

    ACTIVE = "active"
    PASSIVE = "passive"
    UNKNOWN = "???"


def detect_verb_voice(maybe_tokenized):
    logger.debug("Started detecting")
    matches = match_by_pattern("voices", maybe_tokenized)
    (voice, span) = matches[0]
    return voice

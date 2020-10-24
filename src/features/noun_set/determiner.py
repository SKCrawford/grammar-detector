import logging
from enum import Enum
from src.core import match_by_pattern
from src.core.matcher.parse import parse_match
from src.util.spacy import make_doc


logger = logging.getLogger(__name__)


class Determiner(Enum):
    """All possible determiners."""

    DEFINITE = "DEFINITE"
    INDEFINITE = "INDEFINITE"
    OTHER = "OTHER"
    NONE = "NONE"


def detect_determiner(maybe_tokenized):
    logger.debug("Started detecting")
    matches = match_by_pattern("determiners", maybe_tokenized)

    (determiner_type, span) = matches[0]
    determiner = None
    # enum doesn't work (yet)
    # if determiner_type != Determiner.NONE:
    if determiner_type != "NONE": 
        determiner = span[0].text.lower()
    return (determiner, determiner_type.lower())

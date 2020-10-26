import asyncio
import logging
from spacy.tokens.span import Span
from enum import Enum
from src.core import extract_span_features
from src.util.spacy import get_doc
from src.util.validator import is_in_enum, is_truthy, is_type
from .person import detect_noun_person
from .determiner import detect_noun_determiner


logger = logging.getLogger(__name__)


class Nominal(Enum):
    """All possible nominal parts of speech. Numerals are not nominal."""

    NOUN = "NOUN"
    PRONOUN = "PRON"
    PROPER_NOUN = "PROPN"


def is_noun(noun):
    is_truthy(noun)
    is_in_enum(noun["pos"], Nominal)


async def detect_nouns(maybe_tokenized):
    logger.debug("Started detecting")
    doc = get_doc(maybe_tokenized)
    nouns = []
    for noun_chunk in doc.noun_chunks:
        person, (determiner, determiner_type) = await asyncio.gather(
            detect_noun_person(noun_chunk),
            detect_noun_determiner(noun_chunk),
        )

        noun = extract_span_features(noun_chunk)
        noun["person"] = person
        noun["determiner"] = determiner
        noun["determiner_type"] = determiner_type
        is_noun(noun)
        nouns.append(noun)
    return nouns

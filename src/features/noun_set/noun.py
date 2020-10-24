import logging
from enum import Enum
from src.core import parse_phrase_features_from_chunk
from src.util.serializable import Serializable
from src.util.spacy import make_doc
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
    is_type(noun, Serializable)
    is_truthy(noun)
    is_in_enum(noun.pos, Nominal)


def detect_nouns(maybe_tokenized):
    logger.debug("Started detecting")
    doc = make_doc(maybe_tokenized)
    nouns = []
    for noun_chunk in doc.noun_chunks:
        person = detect_noun_person(noun_chunk)
        (determiner, determiner_type) = detect_noun_determiner(noun_chunk)
        phrase_features = parse_phrase_features_from_chunk(noun_chunk)

        noun = Serializable()                           \
            .copy_dict(phrase_features)                 \
            .set("person", person)                      \
            .set("determiner", determiner)              \
            .set("determiner_type", determiner_type)
        is_noun(noun)
        nouns.append(noun)
    return nouns

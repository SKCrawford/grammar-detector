import logging
from src.core import parse_phrase_features_from_chunk
from src.util.serializable import Serializable
from src.util.spacy import make_doc
from .person import detect_noun_person


logger = logging.getLogger(__name__)


def detect_nouns(maybe_tokenized):
    logger.debug("Started detecting")
    doc = make_doc(maybe_tokenized)
    nouns = []
    for noun_chunk in doc.noun_chunks:
        person = detect_noun_person(noun_chunk)
        phrase_features = parse_phrase_features_from_chunk(noun_chunk)

        noun = Serializable()           \
            .copy_dict(phrase_features) \
            .set("person", person)
        nouns.append(noun)
    return nouns

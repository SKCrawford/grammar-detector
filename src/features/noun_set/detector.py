import logging
from src.util.spacy import make_doc
from .noun.detector import detect_nouns


logger = logging.getLogger(__name__)


def detect_noun_features(maybe_tokenized):
    logger.debug("Started detecting")
    doc = make_doc(maybe_tokenized)
    noun_features = detect_nouns(doc)
    return noun_features

import logging
from .verb.detector import detect_verbs


logger = logging.getLogger(__name__)


def detect_verb_features(maybe_tokenized):
    logger.debug("Started detecting")
    verb_features = detect_verbs(maybe_tokenized)
    return verb_features

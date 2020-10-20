import logging
from .verb import detect_verbs


logger = logging.getLogger(__name__)


def detect_verb_features(maybe_tokenized):
    logger.debug("Started detecting")
    return detect_verbs(maybe_tokenized)

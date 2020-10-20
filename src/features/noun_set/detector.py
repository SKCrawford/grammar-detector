import logging
from .noun import detect_nouns


logger = logging.getLogger(__name__)


def detect_noun_features(maybe_tokenized):
    logger.debug("Started detecting")
    return detect_nouns(maybe_tokenized)

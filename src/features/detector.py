import logging
from .noun_set import detect_noun_features
from .verb_set import detect_verb_features


logger = logging.getLogger(__name__)


def detect_features(sentence):
    """The main entry point for the feature detector."""

    logger.debug("Started detecting")
    nouns = detect_noun_features(sentence)
    verbs = detect_verb_features(sentence)

    feature_set = {}
    feature_set["sentence"] = sentence
    feature_set["nouns"] = nouns
    feature_set["verbs"] = verbs
    return feature_set

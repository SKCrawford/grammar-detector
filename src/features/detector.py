import logging
from src.util.spacy import make_doc
from .noun_set.detector import detect_noun_features
from .verb_set.detector import detect_verb_features
from .model import FeatureSet


logger = logging.getLogger(__name__)


def detect_features(sentence):
    """The main entry point for the feature detector."""

    logger.debug("Started detecting")
    doc = make_doc(sentence)
    verbs = detect_verb_features(doc)
    nouns = detect_noun_features(doc)

    feature_set = FeatureSet()
    feature_set.sentence = sentence
    feature_set.verbs = verbs
    feature_set.nouns = nouns
    return feature_set

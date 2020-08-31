import logging
from src.util.builder import Builder
from src.util.spacy import make_doc
from ..noun_set import detect_nouns
from ..verb_set import detect_verbs
from .model import SentenceFeatureSet
from .validator import validate_sentence_feature_set


logger = logging.getLogger(__name__)


def detect_sentence_features(sentence):
    """Determine the linguistic features of a sentence.

    Given a string, return a SentenceFeatureSet instance.
    """
    logger.debug("Started detecting")
    doc = make_doc(sentence)
    verbs = detect_verbs(doc)
    nouns = detect_nouns(doc)

    sent_f_set = Builder(SentenceFeatureSet)    \
        .set_attr("sentence", sentence)         \
        .set_attr("verbs", verbs)               \
        .set_attr("nouns", nouns)               \
        .build()                                    
    validate_sentence_feature_set(sent_f_set)
    logger.debug(f"Finished detecting: `{sent_f_set}`")
    return sent_f_set

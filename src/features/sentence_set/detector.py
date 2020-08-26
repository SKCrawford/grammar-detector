from src.util.spacy import make_doc
from ..noun_set.detector import detect_noun_features
from ..verb_set.detector import detect_verb_features
from .builder import SentenceFeatureSetBuilder
from .validator import validate_sentence_feature_set


def detect_sentence_features(sentence):
    """Determine the linguistic features of a sentence.

    Given a string, return a SentenceFeatureSet instance.
    """
    doc = make_doc(sentence)
    verb_f_set = detect_verb_features(doc)
    noun_f_set = detect_noun_features(doc)

    sent_f_set = SentenceFeatureSetBuilder()    \
        .spawn()                                \
        .set_sentence(sentence)                 \
        .set_verb_feature_set(verb_f_set)       \
        .set_noun_feature_set(noun_f_set)       \
        .build()                                    

    validate_sentence_feature_set(sent_f_set)
    return sent_f_set

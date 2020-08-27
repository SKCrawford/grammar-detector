from src.util.builder import Builder
from src.util.spacy import make_doc
from .tense_aspect.detector import detect_verb_tense_aspect
from .verb.detector import detect_verbs
from .voice.detector import detect_verb_voice
from .model import VerbFeatureSet
from .validator import validate_verb_feature_set


def detect_verb_features(maybe_tokenized):
    """Detect the features of a sentence's verb. Currently detects tense,
    aspect, and voice.

    Given a string, return a VerbFeatureSet instance.
    """
    doc = make_doc(maybe_tokenized)
    verbs = detect_verbs(doc)
    (tense, aspect) = detect_verb_tense_aspect(doc)
    voice = detect_verb_voice(doc)

    verb_f_set = Builder(VerbFeatureSet)    \
        .set_attr('verbs', verbs)           \
        .set_attr('tense', tense)           \
        .set_attr('aspect', aspect)         \
        .set_attr('voice', voice)           \
        .build()
    validate_verb_feature_set(verb_f_set)
    return verb_f_set

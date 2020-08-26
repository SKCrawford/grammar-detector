from src.util.builder import Builder
from src.util.spacy import make_doc
from .lemma.detector import detect_verb_lemmas
from .tense_aspect.detector import detect_verb_tense_aspect
from .verb.detector import detect_verb
from .voice.detector import detect_verb_voice
from .model import VerbFeatureSet
from .validator import validate_verb_feature_set


def detect_verb_features(sentence_or_doc):
    """Detect the features of a sentence's verb. Currently detects tense,
    aspect, and voice.

    Given a string, return a VerbFeatureSet instance.
    """
    doc = make_doc(sentence_or_doc)
    verb = detect_verb(doc)
    (tense, aspect) = detect_verb_tense_aspect(doc)
    voice = detect_verb_voice(doc)
    lemmas = detect_verb_lemmas(doc)

    verb_f_set = Builder(VerbFeatureSet)    \
        .set_attr('verb', verb)             \
        .set_attr('tense', tense)           \
        .set_attr('aspect', aspect)         \
        .set_attr('voice', voice)           \
        .set_attr('lemmas', lemmas)         \
        .build()
    validate_verb_feature_set(verb_f_set)
    return verb_f_set

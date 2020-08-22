from spacy.tokens.doc import Doc
from src.core.pattern.matcher import PatternSetMatcher
from src.nlp import nlp
from src.util.transformer import make_doc
from .aspect.detector import detect_verb_aspect
from .tense.detector import detect_verb_tense
from .verb.detector import detect_verb
from .builder import VerbFeatureSetBuilder
from .validator import validate_verb_feature_set


def detect_verb_features(sentence_or_doc):
    """Detect the features of a sentence's verb. Currently detects tense and aspect.

    Given a string, return a VerbFeatureSet instance.
    """
    doc = make_doc(sentence_or_doc)

    verb = detect_verb(doc)
    aspect = detect_verb_aspect(doc)
    tense = detect_verb_tense(doc)

    builder = VerbFeatureSetBuilder()
    verb_f_set = builder.spawn()    \
        .set_verb(verb)             \
        .set_tense(tense)           \
        .set_aspect(aspect)         \
        .build()
    validate_verb_feature_set(verb_f_set)
    return verb_f_set

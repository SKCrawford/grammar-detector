from src.util.transformer import make_doc
from .tense_aspect.detector import detect_verb_tense_aspect
from .person.detector import detect_verb_person
from .verb.detector import detect_verb
from .voice.detector import detect_verb_voice
from .builder import VerbFeatureSetBuilder
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
    person = detect_verb_person(doc)

    verb_f_set = VerbFeatureSetBuilder()    \
        .spawn()                            \
        .set_verb(verb)                     \
        .set_tense(tense)                   \
        .set_aspect(aspect)                 \
        .set_voice(voice)                   \
        .set_person(person)                 \
        .build()
    validate_verb_feature_set(verb_f_set)
    return verb_f_set

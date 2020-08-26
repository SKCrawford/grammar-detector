from src.util.transformer import make_doc
from .person.detector import detect_noun_person
from .noun.detector import detect_nouns
from .builder import NounFeatureSetBuilder
from .validator import validate_noun_feature_set


def detect_noun_features(sentence_or_doc):
    """Detect the features of a sentence's noun.

    Given a string, return a NounFeatureSet instance.
    """
    doc = make_doc(sentence_or_doc)

    noun = detect_nouns(doc)
    person = detect_noun_persons(doc)

    noun_f_set = NounFeatureSetBuilder()    \
        .spawn()                            \
        .set_attr('nouns', nouns)           \
        .set_attr('person', person)         \
        .build()
    validate_noun_feature_set(noun_f_set)
    return noun_f_set

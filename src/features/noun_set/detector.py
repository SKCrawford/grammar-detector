from src.util.builder import Builder
from src.util.spacy import make_doc
from .person.detector import detect_noun_person
from .noun.detector import detect_nouns
from .model import NounFeatureSet
from .validator import validate_noun_feature_set


def detect_noun_features(maybe_tokenized):
    """Detect the features of a sentence's noun.

    Given a string, return a NounFeatureSet instance.
    """
    doc = make_doc(maybe_tokenized)
    nouns = detect_nouns(doc)
    person = detect_noun_person(doc)

    noun_f_set = Builder(NounFeatureSet)    \
        .set_attr('nouns', nouns)           \
        .set_attr('person', person)         \
        .build()
    validate_noun_feature_set(noun_f_set)
    return noun_f_set

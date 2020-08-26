from src.util.matcher import run_matcher
from src.util.transformer import make_doc
from .matcher import create_noun_person_matcher
from .model import PersonFeature
from .validator import validate_person


def detect_noun_person(sentence_or_doc):
    doc = make_doc(sentence_or_doc)
    matcher = create_noun_person_matcher()
    match = run_matcher(matcher, doc)

    if not match:
        return ""

    (person, noun_span) = match
    validate_person(person)
    person_feature = PersonFeature()
    person_feature.value = person
    return person_feature

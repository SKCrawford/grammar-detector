from src.core.feature.detector import PhraseFeatureDetector
from src.util.spacy import make_doc
from ..person.detector import detect_noun_person
from .model import NounFeature
from .validator import validate_noun_feature


def detect_nouns(maybe_tokenized):
    doc = make_doc(maybe_tokenized)
    detector = PhraseFeatureDetector(NounFeature, None)
    nouns = []
    for noun_chunk in doc.noun_chunks:
        noun = detector.detect_one(noun_chunk)
        noun.person = detect_noun_person(noun_chunk).value
        validate_noun_feature(noun)
        nouns.append(noun)
    return nouns

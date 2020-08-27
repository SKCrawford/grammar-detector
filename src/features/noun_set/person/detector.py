from src.core.feature.detector import SimpleFeatureDetector
from src.util.spacy import run_matcher
from .matcher import create_noun_person_matcher
from .model import PersonFeature
from .validator import validate_person


def detect_noun_person(sentence_or_doc):
    feature = PersonFeature()
    feature.name = "person"
    matcher = create_noun_person_matcher()
    detector = SimpleFeatureDetector(feature, matcher, validate_person)
    return detector.detect(sentence_or_doc)

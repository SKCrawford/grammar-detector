from src.core.feature.detector import SimpleFeatureDetector
from src.util.spacy import run_matcher
from .matcher import create_noun_person_matcher
from .model import PersonFeature
from .validator import validate_person_feature


def detect_noun_person(maybe_tokenized):
    matcher = create_noun_person_matcher()
    detector = SimpleFeatureDetector(PersonFeature, matcher)
    return detector.detect(maybe_tokenized)[0]

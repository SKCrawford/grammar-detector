from src.core.feature.detector import PhraseFeatureDetector
from .matcher import create_verb_matcher
from .model import VerbFeature
from .validator import validate_verb_feature


def detect_verbs(maybe_tokenized):
    matcher = create_verb_matcher()
    detector = PhraseFeatureDetector(VerbFeature, matcher)
    verbs = detector.detect(maybe_tokenized)
    [validate_verb_feature(verb) for verb in verbs]
    return verbs

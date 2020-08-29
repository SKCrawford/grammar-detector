from src.core.feature.detector import SimpleFeatureDetector
from .matcher import create_verb_voice_matcher
from .model import VoiceFeature
from .validator import validate_voice_feature


def detect_verb_voice(maybe_tokenized):
    matcher = create_verb_voice_matcher()
    detector = SimpleFeatureDetector(VoiceFeature, matcher)
    feature = detector.detect(maybe_tokenized)[0]
    validate_voice_feature(feature)
    return feature

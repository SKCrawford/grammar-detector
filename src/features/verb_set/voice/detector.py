from src.core.feature.detector import SimpleFeatureDetector
from src.util.spacy import run_matcher
from .matcher import create_verb_voice_matcher
from .model import VoiceFeature
from .validator import validate_voice_feature


def detect_verb_voice(maybe_tokenized):
    matcher = create_verb_voice_matcher()
    detector = SimpleFeatureDetector(VoiceFeature, matcher)
    return detector.detect(maybe_tokenized)[0]

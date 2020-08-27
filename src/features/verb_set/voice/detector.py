from src.core.feature.detector import SimpleFeatureDetector
from src.util.spacy import run_matcher
from .matcher import create_verb_voice_matcher
from .model import VoiceFeature
from .validator import validate_voice


def detect_verb_voice(sentence_or_doc):
    feature = VoiceFeature()
    matcher = create_verb_voice_matcher()
    detector = SimpleFeatureDetector(feature, matcher, validate_voice)
    return detector.detect(sentence_or_doc)

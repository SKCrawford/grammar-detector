from src.core.feature.detector import SimpleFeatureDetector
from src.util.spacy import run_matcher
from .matcher import create_verb_tense_aspect_matcher
from .model import TenseAspectFeature
from .transformer import extract_tense_aspect
from .validator import validate_tense_aspect_feature


class TenseAspectFeatureDetector(SimpleFeatureDetector):
    def determine_features(self, verb_tense, span):
        (tense, aspect) = extract_tense_aspect(verb_tense)
        return {
            "value": { 
                "tense": tense,
                "aspect": aspect,
            }
        }
    


def detect_verb_tense_aspect(maybe_tokenized):
    matcher = create_verb_tense_aspect_matcher()
    detector = TenseAspectFeatureDetector(TenseAspectFeature, matcher)
    feature = detector.detect_one(maybe_tokenized)
    return feature

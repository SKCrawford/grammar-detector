import logging
from src.core.feature.detector import PhraseFeatureDetector
from ..tense_aspect.detector import detect_verb_tense_aspect
from ..voice.detector import detect_verb_voice
from .matcher import create_verb_matcher
from .model import VerbFeature
from .validator import validate_verb_feature


logger = logging.getLogger(__name__)


def detect_verbs(maybe_tokenized):
    logger.debug("Started detecting")
    matcher = create_verb_matcher()
    detector = PhraseFeatureDetector(VerbFeature, matcher)

    verbs = detector.detect_many(maybe_tokenized)
    for verb in verbs:
        verb.voice = detect_verb_voice(maybe_tokenized).value
        verb.tense_aspect = detect_verb_tense_aspect(maybe_tokenized).value

    [validate_verb_feature(verb) for verb in verbs]
    logger.debug(f"Finished detecting: `{verbs}`")
    return verbs

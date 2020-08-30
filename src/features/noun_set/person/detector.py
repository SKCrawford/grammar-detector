import logging
from src.core.feature.detector import SimpleFeatureDetector
from .matcher import create_noun_person_matcher
from .model import PersonFeature
from .validator import validate_person_feature


logger = logging.getLogger(__name__)


def detect_noun_person(maybe_tokenized):
    logger.debug("Started detecting")
    matcher = create_noun_person_matcher()
    detector = SimpleFeatureDetector(PersonFeature, matcher)
    feature = detector.detect_one(maybe_tokenized)
    validate_person_feature(feature)
    logger.debug(f"Finished detecting: `{feature}`")
    return feature

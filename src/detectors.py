import asyncio
import logging
import os
from json import load
from settings import PATTERNS_DIR
from .Matcher import Matcher


logger = logging.getLogger(__name__)


async def detect_features(sentence, pattern_sets):
    """The main entry point for the feature detector."""
    logger.debug("Started detecting features")

    feature_set = {}
    matcher = Matcher()
    for pattern_set in pattern_sets:
        logger.debug(f"Started detecting '{pattern_set}'")
        feature_set[pattern_set] = matcher.match_by_pattern(pattern_set, sentence)
        logger.debug(f"Finished detecting '{pattern_set}'")

    logger.debug("Finished detecting features")
    return feature_set

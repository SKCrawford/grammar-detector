import asyncio
import logging
import os
from json import load
from settings import PATTERNS_DIR
from .Matcher import Matcher
from .patterns import load_pattern_set


logger = logging.getLogger(__name__)


DEFAULT_HOW_MANY_MATCHES = "one"


async def detect_features(sentence, pattern_set_names):
    """The main entry point for the feature detector."""
    logger.debug(f"Started detecting for the features '{pattern_set_names}'")

    feature_set = {}
    matcher = Matcher()
    for pattern_set_name in pattern_set_names:
        logger.debug(f"Detecting for the feature '{pattern_set_name}'")
        logger.debug(f"Loading the pattern set '{pattern_set_name}'")
        pattern_set = load_pattern_set(pattern_set_name)

        logger.debug(f"Determining how many matches should be returned")
        how_many_matches = None
        try:
            how_many_matches = pattern_set["meta"]["how_many_matches"].upper()
        except Exception:
            how_many_matches = DEFAULT_HOW_MANY_MATCHES

        logger.debug(
            f"Determining the detector function for '{how_many_matches}' result(s)."
        )
        result = None
        if how_many_matches == "ONE":
            logger.debug(f"Matching one")
            result = matcher.match_one(pattern_set, sentence)
        elif how_many_matches == "MANY":
            logger.debug(f"Matching many")
            result = matcher.match_many(pattern_set, sentence)
        else:  # Search for one or many by default
            logger.debug(f"Matching with default '{DEFAULT_HOW_MANY_MATCHES}'")
            result = matcher.match_one(pattern_set, sentence)

        logger.debug(
            f"Setting the result to the feature set's '{pattern_set_name}' key"
        )
        feature_set[pattern_set_name] = result

        logger.debug(f"Finished detecting for the feature '{pattern_set_name}'")

    logger.debug(f"Finished detecting for the features '{pattern_set_names}'")
    return feature_set

import asyncio
import logging
import os
from json import load
from settings import PATTERNS_DIR
from .extractors import get_doc
from .Matcher import Matcher
from .patterns import load_pattern_set


logger = logging.getLogger(__name__)


DEFAULT_HOW_MANY_MATCHES = "one"


async def detect_features(sentence, pattern_set_names):
    """The main entry point for the feature detector."""
    logger.debug(f"Started detecting for the features '{pattern_set_names}'")

    feature_set = {}
    matcher = Matcher()

    logger.debug(f"Tokenizing '{sentence}'")
    doc = get_doc(sentence)

    for pattern_set_name in pattern_set_names:
        logger.debug(f"Detecting for the feature '{pattern_set_name}'")
        logger.debug(f"Loading the pattern set '{pattern_set_name}'")
        pattern_set = load_pattern_set(pattern_set_name)

        # Noun chunks
        logger.debug("Determining if the noun chunks should be extracted")
        should_extract_noun_chunks = False
        try:
            should_extract_noun_chunks = pattern_set["meta"]["extract_noun_chunks"]
        except KeyError:
            should_extract_noun_chunks = False

        logger.debug(f"Extracting the noun chunks: {should_extract_noun_chunks}")
        inputs = doc.noun_chunks if should_extract_noun_chunks else [doc]

        # Deciding the appropriate matcher function
        logger.debug(f"Determining how many matches should be returned")
        how_many_matches = None
        try:
            how_many_matches = pattern_set["meta"]["how_many_matches"].upper()
        except Exception:
            how_many_matches = DEFAULT_HOW_MANY_MATCHES

        logger.debug(
            f"Determining the detector function for '{how_many_matches}' result(s)."
        )
        results = []
        for input in inputs:
            result = None
            if how_many_matches == "ONE":
                logger.debug(f"Matching one")
                result = matcher.match_one(pattern_set, input)
            elif how_many_matches == "MANY":
                logger.debug(f"Matching many")
                result = matcher.match_many(pattern_set, input)
            else:  # Search for one or many by default
                logger.debug(f"Matching with default '{DEFAULT_HOW_MANY_MATCHES}'")
                result = matcher.match_one(pattern_set, input)
            results.append(result)

        logger.debug(
            f"Setting the results to the feature set's '{pattern_set_name}' key"
        )
        feature_set[pattern_set_name] = results

        logger.debug(f"Finished detecting for the feature '{pattern_set_name}'")

    logger.debug(f"Finished detecting for the features '{pattern_set_names}'")
    return feature_set

import asyncio
import logging
import os
from json import load
from settings import PATTERNS_DIR
from .extractors import get_doc
from .Matcher import Matcher
from .patterns import load_pattern_set, PatternSet


logger = logging.getLogger(__name__)


DEFAULT_HOW_MANY_MATCHES = "one"


async def detect_features(sentence, pattern_set_names):
    """The main entry point for the feature detector."""
    logger.debug(f"Started detecting for the features '{pattern_set_names}'")
    feature_set = {}

    logger.debug(f"Tokenizing '{sentence}'")
    doc = get_doc(sentence)

    for pattern_set_name in pattern_set_names:
        logger.debug(f"Detecting for the feature '{pattern_set_name}'")
        logger.debug(f"Loading the pattern set '{pattern_set_name}'")
        pattern_set = PatternSet(pattern_set_name)

        logger.debug("Constructing the external matcher")
        matcher = Matcher(pattern_set)

        # Noun chunks
        logger.debug("Determining if the noun chunks should be extracted from the doc")
        should_extract_noun_chunks = pattern_set.should_extract_noun_chunks
        logger.debug(f"Extracting the noun chunks: {should_extract_noun_chunks}")
        inputs = doc.noun_chunks if should_extract_noun_chunks else [doc]

        # Deciding the appropriate matcher function
        logger.debug(f"Running the external matcher")
        feature_set[pattern_set_name] = [matcher.match(input) for input in inputs]
        logger.debug(f"Finished detecting for the feature '{pattern_set_name}'")

    logger.debug(f"Finished detecting for the features '{pattern_set_names}'")
    return feature_set

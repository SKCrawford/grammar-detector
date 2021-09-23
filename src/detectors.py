import asyncio
import logging
import os
from json import load
from settings import PATTERNS_DIR
from .matchers import match_by_pattern


logger = logging.getLogger(__name__)


async def detect_features(sentence):
    """The main entry point for the feature detector."""
    logger.debug("Started detecting")

    featureset = await match_by_pattern("voices", sentence)
    return featureset

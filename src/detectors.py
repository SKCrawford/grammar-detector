import asyncio
import logging
import os
from json import load
from settings import PATTERNS_DIR


logger = logging.getLogger(__name__)


async def detect_features(sentence):
    """The main entry point for the feature detector."""
    logger.debug("Started detecting")

    feature_set = {}
    return feature_set

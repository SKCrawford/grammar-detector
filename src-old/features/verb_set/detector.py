import asyncio
import logging
from .verb import detect_verbs


logger = logging.getLogger(__name__)


async def detect_verb_features(maybe_tokenized):
    logger.debug("Started detecting")
    return await detect_verbs(maybe_tokenized)

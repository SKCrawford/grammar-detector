import asyncio
import logging
from .noun import detect_nouns


logger = logging.getLogger(__name__)


async def detect_noun_features(maybe_tokenized):
    logger.debug("Started detecting")
    return await detect_nouns(maybe_tokenized)

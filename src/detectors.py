import asyncio
from logging import getLogger
from spacy.tokens import Doc
from settings import SettingKeys
from .extractors import get_doc
from .matchers import PatternSetMatcher as Matcher
from .patterns import PatternSetLoader


logger = getLogger(__name__)


async def detect_features(sentence: str, pattern_set_names: list[str]) -> dict:
    """The main entry point for the feature detector."""
    logger.debug(f"Started detecting for the features '{pattern_set_names}'")
    feature_set = {}

    logger.debug("Creating the PatternSetLoader instance")
    loader = PatternSetLoader()

    logger.debug(f"Tokenizing '{sentence}'")
    doc: Doc = get_doc(sentence)

    for pattern_set_name in pattern_set_names:
        logger.debug(f"Detecting for the feature '{pattern_set_name}'")
        logger.debug(f"Loading the pattern set '{pattern_set_name}'")
        pattern_set: PatternSet = loader.load(pattern_set_name)

        logger.debug("Constructing the external matcher")
        matcher = Matcher(pattern_set)

        # Noun chunks
        logger.debug("Determining if the noun chunks should be extracted from the doc")
        key: str = SettingKeys.PSET_META_EXTRACT_NOUN_CHUNKS.value
        should_extract_noun_chunks: bool = pattern_set.meta[key]

        logger.debug(f"Extracting the noun chunks: {should_extract_noun_chunks}")
        inputs = doc.noun_chunks if should_extract_noun_chunks else [doc]

        logger.debug(f"Running the external matcher")
        feature_set[pattern_set_name] = [matcher.match(input) for input in inputs]
        logger.debug(f"Finished detecting for the feature '{pattern_set_name}'")

    logger.debug(f"Finished detecting for the features '{pattern_set_names}'")
    return feature_set

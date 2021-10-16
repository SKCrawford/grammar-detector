import asyncio
from logging import getLogger
from spacy.tokens import Doc, Span
from typing import Any, Union
from settings import PATTERNS_DIR_PATH, SettingKeys
from .extractors import get_doc
from .matchers import ParsedMatch, PatternSetMatcher as Matcher
from .patterns import PatternSet
from .loaders import PatternSetLoader, YamlLoader


logger = getLogger(__name__)


async def detect_features(
    sentence: str, pattern_set_names: list[str]
) -> dict[str, Any]:
    """The main entry point for the feature detector."""
    logger.debug(f"Started detecting for the features '{pattern_set_names}'")
    feature_set = {}

    logger.debug("Creating the PatternSetLoader instance")
    pattern_sets_dir_path = PATTERNS_DIR_PATH
    file_loader = YamlLoader(pattern_sets_dir_path)
    pset_loader = PatternSetLoader(file_loader)

    logger.debug(f"Tokenizing '{sentence}'")
    doc: Doc = get_doc(sentence)

    for pattern_set_name in pattern_set_names:
        logger.debug(f"Detecting for the feature '{pattern_set_name}'")
        logger.debug(f"Loading the pattern set '{pattern_set_name}'")
        pattern_set: PatternSet = pset_loader(pattern_set_name)

        logger.debug("Constructing the external matcher")
        matcher = Matcher(pattern_set)

        # Noun chunks
        logger.debug("Determining if the noun chunks should be extracted from the doc")
        key: str = SettingKeys.PSET_META_EXTRACT_NOUN_CHUNKS.value
        should_extract_noun_chunks: bool = bool(pattern_set.meta[key])

        inputs: list[Union[Doc, Span]] = []
        if should_extract_noun_chunks:
            logger.debug("Extracting the noun chunks")
            inputs = doc.noun_chunks
        else:
            inputs = [doc]

        logger.debug(f"Running the external matcher")
        matches: list[list[ParsedMatch]] = [matcher.match(input) for input in inputs]
        feature_set[pattern_set_name] = matches
        logger.debug(f"Finished detecting for the feature '{pattern_set_name}'")

    logger.debug(f"Finished detecting for the features '{pattern_set_names}'")
    return feature_set

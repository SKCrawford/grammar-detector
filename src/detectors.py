import asyncio
from logging import getLogger
from settings import PATTERNS_DIR_PATH, SettingKeys
from spacy.tokens import Doc, Span
from typing import Any, Union
from .extractors import get_doc
from .loaders import PatternSetLoader, YamlLoader
from .matchers import ParsedMatch, PatternSetMatcher
from .patterns import PatternSet


logger = getLogger(__name__)


async def detect_feature(doc: Doc, pattern_set_name: str) -> dict[str, Any]:
    logger.debug(f"Started detecting for the feature '{pattern_set_name}'")
    logger.debug(f"Loading the patternset '{pattern_set_name}'")
    pattern_set: PatternSet = pset_loader(pattern_set_name)

    logger.debug("Constructing the PatternSetMatcher")
    matcher = PatternSetMatcher(pattern_set)

    logger.debug("Determining if the noun chunks should be extracted from the doc")
    key: str = SettingKeys.PSET_META_EXTRACT_NOUN_CHUNKS.value
    should_extract_noun_chunks: bool = bool(pattern_set.meta[key])

    inputs: list[Union[Doc, Span]] = []
    if should_extract_noun_chunks:
        logger.debug("Extracting the noun chunks from the doc")
        inputs = doc.noun_chunks
    else:
        inputs = [doc]

    logger.debug("Running the PatternSetMatcher")
    matches: list[list[ParsedMatch]] = [matcher(input) for input in inputs]
    logger.debug(f"Finished detecting for the feature '{pattern_set_name}'")
    return matches


async def detect_features(
    sentence: str, pattern_set_names: list[str]
) -> dict[str, Any]:
    """The main entry point for the feature detector."""
    logger.debug(f"Started detecting for the features '{pattern_set_names}'")
    feature_set = {}

    logger.debug("Creating the PatternSetLoader instance")
    pattern_sets_dir_path: str = PATTERNS_DIR_PATH
    file_loader = YamlLoader(pattern_sets_dir_path)
    pset_loader = PatternSetLoader(file_loader)

    logger.debug(f"Tokenizing '{sentence}'")
    doc: Doc = get_doc(sentence)

    for pset_name in pattern_set_names:
        feature_set[pset_name] = await detect_feature(doc, pset_name)

    logger.debug(f"Finished detecting for the features '{pattern_set_names}'")
    return feature_set

import asyncio
from logging import getLogger
from spacy.tokens import Doc, Span
from typing import Any, Union
from settings import pattern_set_config
from .extractors import get_doc
from .loaders import PatternSetLoader, YamlLoader
from .matchers import ParsedMatch, PatternSetMatcher
from .patterns import PatternSet


logger = getLogger(__name__)


async def detect_feature(doc: Doc, pattern_set: PatternSet) -> dict[str, Any]:
    logger.debug(f"Started detecting for the feature '{pattern_set.name}'")
    logger.debug("Constructing the PatternSetMatcher")
    matcher = PatternSetMatcher(pattern_set)

    logger.debug("Determining if the noun chunks should be extracted from the doc")
    key: str = pattern_set_config.keys.prop("SHOULD_EXTRACT_NOUN_CHUNKS")
    should_extract_noun_chunks: bool = pattern_set.meta[key]

    inputs: list[Union[Doc, Span]] = []
    if should_extract_noun_chunks:
        logger.debug("Extracting the noun chunks from the doc")
        inputs = doc.noun_chunks
    else:
        inputs = [doc]

    logger.debug("Running the PatternSetMatcher")
    matches: list[list[ParsedMatch]] = [matcher(input) for input in inputs]
    logger.debug(f"Finished detecting for the feature '{pattern_set.name}'")
    return matches


async def detect_features(
    sentence: str, pattern_set_names: list[str]
) -> dict[str, Any]:  # TODO fix typing
    """The main entry point for the feature detector."""
    logger.debug(f"Started detecting for the features '{pattern_set_names}'")
    feature_set = {}

    logger.debug(f"Tokenizing '{sentence}'")
    doc: Doc = get_doc(sentence)

    logger.debug("Constructing the PatternSetLoader")
    file_loader = YamlLoader(pattern_set_config.host_dir_path)
    pattern_set_loader = PatternSetLoader(file_loader)

    for pattern_set_name in pattern_set_names:
        logger.debug(f"Loading the patternset '{pattern_set_name}'")
        pattern_set = pattern_set_loader(pattern_set_name)
        feature_set[pattern_set.name] = await detect_feature(doc, pattern_set)

    logger.debug(f"Finished detecting for the features '{pattern_set_names}'")
    return feature_set

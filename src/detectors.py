from __future__ import annotations
import asyncio
from logging import getLogger
from spacy.tokens import Doc, Span
from typing import Any, cast, Union
from settings import pattern_set_config
from .extractors import get_doc
from .loaders import FileLoader, YamlLoader
from .matchers import ParsedMatch, PatternSetMatcher
from .patterns import PatternSet, PatternSetRepository

# from .loaders import YamlLoader


logger = getLogger(__name__)


class SyntaxFeatureDetector:
    def __init__(self, file_loader: YamlLoader, pattern_set_repo: PatternSetRepository):
        self.file_loader: YamlLoader = file_loader
        self.pset_repo: PatternSetRepository = pattern_set_repo
        self.features: list[str] = []
        self.matchers: list[PatternSetMatcher] = []
        self.inputs: Union[list[Doc], list[Span]] = []

    def load_pattern_sets(self, features: list[str]) -> SyntaxFeatureDetector:
        for feature in self.features:
            pset_data: PatternSetData = file_loader(feature)
            self.pset_repo.create(feature, pset_data)
        return self

    def load_matchers(self) -> SyntaxFeatureDetector:
        for pattern_set in self.pset_repo.get_all():
            self.matchers[pattern_set.name] = PatternSetMatcher(pattern_set)
        return self

    def process_input(self, input: str) -> SyntaxFeatureDetector:
        # logger.debug("Determining if the noun chunks should be extracted from the doc")
        key: str = pattern_set_config.keys.prop_str("SHOULD_EXTRACT_NOUN_CHUNKS")
        should_extract_noun_chunks: bool = bool(pattern_set.meta[key])

        if should_extract_noun_chunks:
            # logger.debug("Extracting the noun chunks from the doc")
            inputs = doc.noun_chunks
            cast(list[Span], inputs)
            self.inputs = inputs
        else:
            inputs = [doc]
            cast(list[Doc], inputs)
            self.inputs = inputs
        return self

    def __call__(self, input: str, features: list[str]) -> dict[str, Any]:
        self.load_pattern_sets(features).load_matchers().process_input(input)

        feature_set = {}
        for feature_name in self.matchers:
            matcher = self.matcher[feature_name]
            matches: list[list[ParsedMatch]] = [matcher(input) for input in self.inputs]
            feature_set[feature_name] = matches
        return feature_set


async def detect_feature(doc: Doc, pattern_set: PatternSet) -> list[list[ParsedMatch]]:
    logger.debug(f"Started detecting for the feature '{pattern_set.name}'")
    logger.debug("Constructing the PatternSetMatcher")
    matcher = PatternSetMatcher(pattern_set)

    logger.debug("Determining if the noun chunks should be extracted from the doc")
    key: str = pattern_set_config.keys.prop_str("SHOULD_EXTRACT_NOUN_CHUNKS")
    should_extract_noun_chunks: bool = bool(pattern_set.meta[key])

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

    logger.debug("Creating the FileLoader")
    file_loader = YamlLoader(pattern_set_config.host_dir_path)

    logger.debug("Creating the PatternSetRepository")
    repo = PatternSetRepository()

    logger.debug("Creating the SyntaxFeatureDetector")
    detector = SyntaxFeatureDetector(file_loader, repo)

    matches = detector(sentence, pattern_set_names)

    # logger.debug("Creating and caching the PatternSets")
    # for pset_name in pattern_set_names:
    #     logger.debug(f"Loading PatternSet data '{pset_name}'")
    #     pset_data = file_loader(pset_name)

    #     logger.debug(f"Creating and caching the PatternSet '{pset_name}'")
    #     repo.create(pset_name, pset_data)

    # # TODO fix async
    # for pattern_set in repo.get_all():
    #     logger.debug(f"Loading the PatternSet '{pattern_set.name}'")
    #     feature_set[pattern_set.name] = await detect_feature(doc, pattern_set)

    logger.debug(f"Finished detecting for the features '{pattern_set_names}'")
    return feature_set

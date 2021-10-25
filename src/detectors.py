from __future__ import annotations
import asyncio
from logging import getLogger
from spacy.tokens import Doc, Span
from typing import Any, cast, Union
from settings import pattern_set_config
from .extractors import get_doc
from .inputs import Input
from .loaders import YamlLoader
from .matchers import Match, PatternSetMatcher
from .patterns import PatternSet, PatternSetRepository


logger = getLogger(__name__)


class Detector:
    def __init__(self, pattern_set: PatternSet) -> None:
        self.pattern_set: PatternSet = pattern_set
        self.matcher = PatternSetMatcher(self.pattern_set)

    def __call__(self, raw: str):
        """The entrypoint for the Detector."""
        return self.detect(raw)

    def detect(self, raw: str) -> list[Match]:
        input = Input(raw)
        input.extract_noun_chunks = self.pattern_set.should_extract_noun_chunks
        return self.matcher(input)


def detect_feature(input: str, feature: str):
    logger.debug("Creating the FileLoader")
    file_loader = YamlLoader(pattern_set_config.host_dir_path)

    logger.debug("Creating the PatternSetRepository")
    pset_repo = PatternSetRepository()

    logger.debug("Loading the PatternSetRepository")
    for pset_name in pattern_set_config.names:
        pset_data = file_loader(pset_name)
        pset_repo.create(pset_name, pset_data)

    logger.debug(f"Getting the PatternSet for '{feature}'")
    pattern_set = pset_repo.get_one(feature)

    logger.debug("Creating the Detector")
    detector = Detector(pattern_set)

    logger.debug(f"Running the Detector on str '{input}'")
    matches = detector(input)

    logger.debug(f"Found {len(matches)} Match(es): {matches}")
    return matches

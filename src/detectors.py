from __future__ import annotations
import asyncio
from logging import getLogger
from spacy.tokens import Doc, Span
from typing import Any, cast, Union
from settings import pattern_set_config
from .extractors import get_doc
from .inputs import Input
from .loaders import YamlLoader
from .matches import Match, MatchSet
from .matchers import PatternSetMatcher
from .patterns import PatternSet, PatternSetRepository


logger = getLogger(__name__)


class Detector:
    def __init__(self, pattern_set: PatternSet) -> None:
        logger.debug(
            f"Constructing the Detector with the '{pattern_set.name}' PatternSet"
        )
        self.pattern_set: PatternSet = pattern_set
        self.matcher = PatternSetMatcher(self.pattern_set)

    def __call__(self, raw: str):
        """The entrypoint for the Detector."""
        logger.debug(f"Calling the '{self.pattern_set.name}' Detector on: '{raw}'")
        return self.detect(raw)

    def detect(self, raw: str) -> list[MatchSet]:
        input = Input(raw)
        input.extract_noun_chunks = bool(self.pattern_set.should_extract_noun_chunks)
        return [self.matcher(fragment) for fragment in input.fragments]


def detect_feature(input: str, feature: str):
    logger.debug("Creating the FileLoader")
    file_loader = YamlLoader(pattern_set_config.host_dir_path)

    logger.debug("Creating the PatternSetRepository")
    pset_repo = PatternSetRepository()

    logger.debug("Loading the PatternSetRepository")
    for pset_name in pattern_set_config.names:
        pset_data: PatternSetData = file_loader(pset_name)
        pset_repo.create(pset_name, pset_data)

    logger.debug(f"Getting the '{feature}' PatternSet")
    pattern_set: PatternSet = pset_repo.get_one(feature)

    logger.debug("Creating the Detector")
    detector = Detector(pattern_set)

    logger.debug(f"Running the Detector on str '{input}'")
    match_sets: list[MatchSet] = detector(input)

    logger.debug(f"Found {len(match_sets)} '{feature}' MatchSets: {match_sets}")
    return match_sets

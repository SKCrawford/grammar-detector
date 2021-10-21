from logging import getLogger
from typing import Union
from .Pattern import Pattern


MetaSetting = Union[str, bool]
MetaDict = dict[str, MetaSetting]
Test = dict[str, Union[str, list[str]]]


logger = getLogger(__name__)


class PatternSet:
    def __init__(self, name: str):
        self.name: str = name
        self.patterns: dict[str, Pattern] = {}
        self.meta: MetaDict = {}
        self.tests: list[Test] = []

    def get_all_patterns(self) -> list[Pattern]:
        return [self.patterns[k] for k in self.patterns]

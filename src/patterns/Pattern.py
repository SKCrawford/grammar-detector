from logging import getLogger
from spacy.tokens import Token
from typing import Union


Rulename = str
Tokens = list[Token]
PatternData = dict[str, Union[Rulename, Tokens]]
ExtractedPatternData = tuple[Rulename, Tokens]


logger = getLogger(__name__)


class Pattern:
    def __init__(self, data: PatternData):
        (rulename, tokens) = self._extract_data(data)

        logger.debug(f"Constructing the '{rulename}' Pattern")
        self.rulename: Rulename = rulename
        self.tokens: Tokens = tokens

    def _extract_data(self, data: PatternData) -> ExtractedPatternData:
        rulename: Rulename = data["rulename"]
        tokens: Tokens = data["tokens"]
        return (rulename, tokens)

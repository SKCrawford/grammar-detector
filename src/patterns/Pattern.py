from logging import getLogger
from spacy.tokens import Token
from typing import Union


Rulename = str
Tokens = list[Token]
PatternData = dict[str, Union[Rulename, Tokens]]
ExtractedPatternData = tuple[Rulename, Tokens]


logger = getLogger(__name__)


def extract_pattern_data(data: PatternData) -> ExtractedPatternData:
    rulename: Rulename = data["rulename"]
    tokens: Tokens = data["tokens"]
    return (rulename, tokens)


class Pattern:
    def __init__(self, rulename: Rulename, tokens: Tokens):
        logger.debug(f"Constructing the '{rulename}' Pattern")
        self.rulename: Rulename = rulename
        self.tokens: Tokens = tokens

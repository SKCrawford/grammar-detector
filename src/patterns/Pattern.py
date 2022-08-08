from logging import getLogger
from spacy.tokens import Token
from typing import Union


PatternData = dict[str, Union[str, list[Token]]]


logger = getLogger(__name__)


class Pattern:
    def __init__(self, data: PatternData):
        self.rulename: str = data["rulename"]
        logger.debug(f"Constructing the '{self.rulename}' Pattern")
        self.tokens: list[Token] = data["tokens"]

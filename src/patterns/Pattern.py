from logging import getLogger
from spacy.tokens import Token


logger = getLogger(__name__)


class Pattern:
    def __init__(self, rulename: str, tokens: list[Token]):
        self.rulename: str = rulename
        self.tokens: list[Token] = tokens

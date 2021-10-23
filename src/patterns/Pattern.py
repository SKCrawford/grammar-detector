from logging import getLogger
from spacy.tokens import Token
from typing import Union
from settings import pattern_set_config_keys


Rulename = str
Tokens = list[Token]
PatternData = dict[str, Union[Rulename, Tokens]]
ExtractedPatternData = tuple[Rulename, Tokens]


logger = getLogger(__name__)


def extract_pattern_data(data: PatternData) -> ExtractedPatternData:
    rulename: Rulename = data[pattern_set_config_keys.prop_str("RULENAME")]
    tokens: Tokens = data[pattern_set_config_keys._prop("TOKENS", Tokens)]  # type: ignore # TODO
    return (rulename, tokens)


class Pattern:
    def __init__(self, rulename: Rulename, tokens: Tokens):
        self.rulename: Rulename = rulename
        self.tokens: Tokens = tokens

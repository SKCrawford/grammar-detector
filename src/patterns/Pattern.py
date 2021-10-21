from logging import getLogger
from spacy.tokens import Token
from typing import Any
from settings import pattern_set_config_keys


logger = getLogger(__name__)


class Pattern:
    def __init__(self, pattern_data: dict[str, Any]):
        rulename_key: str = pattern_set_config_keys.prop("RULENAME")
        self.rulename: str = pattern_data[rulename_key]

        tokens_key: str = pattern_set_config_keys.prop("TOKENS")
        self.tokens: list[Token] = pattern_data[tokens_key]

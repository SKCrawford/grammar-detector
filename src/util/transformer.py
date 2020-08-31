import logging
import re
from spacy.tokens.doc import Doc
from src.nlp import nlp
from .validator import is_not_type, is_truthy, is_type


def remove_ordinals(string):
    """Remove alphanumeric ordinal values, such as third or 3rd.

    Given a string, return a string.
    """
    logger = logging.getLogger(remove_ordinals.__name__)
    logger.debug(f"Started validating string `{string}`")
    is_type(string, str)
    is_truthy(string)
    logger.debug("Finished validating string")

    logger.debug("Started removing ordinals")
    ordinal_reg = r"\b(\w+)(?:st|nd|rd|th)"
    stripped = re.sub(ordinal_reg, "", string, flags=re.IGNORECASE).strip()
    logger.debug(f"Finished removing ordinals: `{stripped}`")
    return stripped


def split_words_into_first_and_rest(string):
    """Split a multi-word string into the first word and the rest of the words.

    Given a string, return a tuple of (string, string).
    """
    logger = logging.getLogger(split_words_into_first_and_rest.__name__)
    logger.debug(f"Started validating string `{string}`")
    is_type(string, str)
    is_truthy(string)
    logger.debug("Finished validating string`")

    logger.debug("Started splitting string")
    first_word_and_rest_of_words_reg = r"(\w+)\s([\w\s]*)"
    match = re.search(first_word_and_rest_of_words_reg, string)

    first_word = ""
    rest_of_words = ""
    if match:
        first_word = match.group(1).strip()
        rest_of_words = match.group(2).strip()
    logger.debug(f"Finished splitting string: ('{first_word}`, `{rest_of_words}`)")
    return (first_word, rest_of_words)

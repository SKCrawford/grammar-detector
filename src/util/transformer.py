import re
from .validator import is_truthy, is_type


def remove_cardinals(string):
    """Remove alphanumeric cardinal values, such as third or 3rd.

    Given a string, return a string.
    """
    is_type(string, str)
    is_truthy(string)
    cardinal_reg = r"\b(?:1st|2nd|3rd|first|second|third)"
    return re.sub(cardinal_reg, "", string).strip()


def split_words_into_first_and_rest(string):
    """Split a multi-word string into the first word and the rest of the words.

    Given a string, return a tuple of (string, string).
    """
    first_word_and_rest_of_words_reg = r"(\w+)\s([\w\s]*)"
    match = re.search(first_word_and_rest_of_words_reg, string)

    first_word = ""
    rest_of_words = ""
    if match:
        first_word = match.group(1).strip()
        rest_of_words = match.group(2).strip()
    return (first_word, rest_of_words)

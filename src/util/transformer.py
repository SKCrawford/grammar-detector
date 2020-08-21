import re
from .validator import is_truthy, is_type


def remove_ordinals(string):
    """Remove alphanumeric ordinal values, such as third or 3rd.

    Given a string, return a string.
    """
    is_type(string, str)
    is_truthy(string)
    ordinal_reg = r"\b(\w+)(?:st|nd|rd|th)"
    return re.sub(ordinal_reg, "", string, flags=re.IGNORECASE).strip()


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

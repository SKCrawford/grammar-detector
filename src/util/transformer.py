import re
from spacy.tokens.doc import Doc
from src.nlp import nlp
from .validator import is_not_type, is_truthy, is_type


def make_doc(sentence_or_doc):
    """Given a string or a Doc instance, return a Doc instance."""
    is_not_type(sentence_or_doc, type(None))
    is_truthy(sentence_or_doc)

    if isinstance(sentence_or_doc, str):
        return nlp(sentence_or_doc)
    elif isinstance(sentence_or_doc, Doc):
        return sentence_or_doc
    else:
        raise TypeError(f"expected a string or Doc instance but got {type(sentence_or_doc)}")


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
    is_type(string, str)
    is_truthy(string)
    first_word_and_rest_of_words_reg = r"(\w+)\s([\w\s]*)"
    match = re.search(first_word_and_rest_of_words_reg, string)

    first_word = ""
    rest_of_words = ""
    if match:
        first_word = match.group(1).strip()
        rest_of_words = match.group(2).strip()
    return (first_word, rest_of_words)

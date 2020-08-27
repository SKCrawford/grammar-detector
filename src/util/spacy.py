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


def run_matcher(matcher, sentence_or_doc):
    """Given a Matcher and a string or a Doc, return a tuple of (string, Span)."""
    is_not_type(matcher, type(None))
    is_truthy(matcher)

    doc = make_doc(sentence_or_doc)
    matches = matcher(doc)
    if not matches:
        return None

    (match_id, start, end) = find_best_match(matches, doc)
    pattern_name = nlp.vocab.strings[match_id]
    matching_span = doc[start:end]
    return (pattern_name, matching_span)


def find_best_match(matches, doc):
    """Determine the best match out of a list of matches by 
    the start and end values.

    Given a list of Matches and a Doc, return a tuple of (int, int, int).
    """
    is_type(doc, Doc)
    is_type(matches, list)
    is_truthy(matches)

    lowest_start = 100000
    highest_end = -1
    for (match_id, start, end) in matches:
        if start < lowest_start:
            lowest_start = start
        if end > highest_end:
            highest_end = end
    return (match_id, lowest_start, highest_end)

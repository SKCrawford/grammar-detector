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

    match = _find_best_match(matches, doc)
    (pattern_name, matching_span) = match
    return (pattern_name, matching_span)


def _find_best_match(matches, doc):
    """Determine the best match out of a list of matches.

    The best match is determined by the length of the matches' `span`s.
    Some verb tenses will be flagged for multiple matches. For example,
    'I will have been doing that' will be flagged for both:
        * present perfect continuous 'have been doing'
        * future perfect continuous 'will have been doing'
    The length of 'will have been doing' is longer than 'have been doing',
    so the best match will be the longer span. This method should
    not be necessary if the patterns are well-made.

    Given a list of Match instances and a Doc instance, return a tuple of (string, string).
    """
    is_type(doc, Doc)
    is_type(matches, list)
    is_truthy(matches)

    best_match_rulename = ""
    best_match_span = ""

    for (match_id, start, end) in matches:
        rulename = nlp.vocab.strings[match_id]
        span = doc[start:end]

        if len(best_match_span) < len(span):
            best_match_rulename = rulename
            best_match_span = span

    return (best_match_rulename, best_match_span)

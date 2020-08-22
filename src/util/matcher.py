from spacy.tokens.doc import Doc
from src.nlp import nlp
from .validator import is_truthy, is_type


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


def run_matcher(matcher, doc):
    is_truthy(matcher)
    is_type(doc, Doc)

    matches = matcher(doc)
    if not matches:
        return None
    return _find_best_match(matches, doc)

from spacy.tokens.doc import Doc
from spacy.tokens.span import Span
from src.util.spacy import get_span, make_doc


def detect_similarity(base_word, target_words):
    """Given a Span and a list of Spans, return a float."""
    similarities = []
    base_span = get_span(base_word)
    for target_word in target_words:
        target_span = get_span(target_word)
        similarity = base_span.similarity(target_span)
        entry = (similarity, target_span, base_span)
        similarities.append(entry)
    return similarities

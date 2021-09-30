import logging
from spacy import explain
from .nlp import nlp


logger = logging.getLogger(__name__)


def get_doc(phrase):
    """Given a str, a Doc, or a Span, return a Doc."""
    logger.debug(f"Getting the Doc of '{phrase}' ({type(phrase)})")
    doc = None
    if type(phrase) == str:
        doc = nlp(phrase)
    elif type(phrase) == Doc:
        doc = phrase
    elif type(phrase) == Span:
        doc = phrase.doc
    else:
        msg = f"Cannot get the Doc of '{phrase}' ({type(phrase)})"
        logger.error(msg)
        raise TypeError(msg)
    return doc


def get_span(phrase):
    """Given a str, a Doc, or a Span, return a Span."""
    logger.debug(f"Getting the Span of '{phrase}' ({type(phrase)})")
    span = None
    if type(phrase) == str:
        span = get_doc(phrase)[:]
    elif type(phrase) == Doc:
        span = phrase[:]
    elif type(phrase) == Span:
        span = phrase
    else:
        msg = f"Cannot get the Span of '{phrase}' ({type(phrase)})"
        logger.error(msg)
        raise TypeError(msg)
    return span


def extract_span_features(match_span):
    """Given a Span, return a dictionary."""
    logging.getLogger(__name__).info(f"Parsing Span '{match_span}'")
    return {
        "span": match_span,
        "phrase": match_span.text,
        "root": match_span.root.text,
        "root_head": match_span.root.head.text,
        "pos": match_span.root.pos_,
        "tag": match_span.root.tag_,
        "dep": match_span.root.dep_,
        "phrase_lemma": match_span.lemma_,
        "root_lemma": match_span.root.lemma_,
        "pos_desc": explain(match_span.root.pos_),
        "tag_desc": explain(match_span.root.tag_),
        "dep_desc": explain(match_span.root.dep_),
    }

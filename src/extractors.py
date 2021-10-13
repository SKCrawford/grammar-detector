from logging import getLogger
from spacy import explain
from spacy.tokens import Doc, Span
from .nlp import nlp


logger = getLogger(__name__)


def get_doc(phrase: any) -> Doc:
    """Given a str, a Doc, or a Span, return a Doc."""
    logger.debug(f"Getting the Doc of '{phrase}' ({type(phrase)})")
    doc: Doc = None
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


def extract_span_features(match_span: Span) -> dict:
    """Given a Span, return a dictionary."""
    logger.debug(f"Parsing Span '{match_span}'")
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

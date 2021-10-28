from logging import getLogger
from spacy import explain
from spacy.tokens import Doc, Span
from typing import Any, cast, Union
from .nlp import nlp


SpanFeatures = dict[str, str]


logger = getLogger(__name__)


def get_doc(phrase: Union[str, Doc, Span]) -> Doc:
    logger.debug(f"Getting the Doc of '{phrase}' ({type(phrase)})")
    doc: Doc = None
    phrase_type = type(phrase)
    if phrase_type == str:
        phrase = cast(str, phrase)
        doc = nlp(phrase)
    elif phrase_type == Doc:
        phrase = cast(Doc, phrase)
        doc = phrase
    elif phrase_type == Span:
        phrase = cast(Span, phrase)
        doc = phrase
    else:
        msg = f"Cannot get the Doc of '{phrase}' ({phrase_type})"
        logger.error(msg)
        raise TypeError(msg)
    return doc


def extract_span_features(match_span: Span) -> SpanFeatures:
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
        "pos_desc": explain(match_span.root.pos_),  # type: ignore # explain is untyped
        "tag_desc": explain(match_span.root.tag_),  # type: ignore # explain is untyped
        "dep_desc": explain(match_span.root.dep_),  # type: ignore # explain is untyped
    }

from logging import getLogger
from spacy import explain
from spacy.tokens import Doc, Span
from typing import Any, Union
from .nlp import nlp


SpanFeatures = dict[str, str]


logger = getLogger(__name__)


def get_doc(text: Union[str, Doc, Span]) -> Doc:
    text_type = type(text)

    logger.debug(f"Getting the Doc for '{text}' (text_type)")
    if isinstance(text_type, Doc):
        logger.debug("Skipping tokenizing")
        return text
    elif isinstance(text_type, Span):
        logger.debug("Converting the Span to a Doc")
        return text.as_doc()
    elif isinstance(text_type, str):
        logger.debug("Tokenizing the raw str")
        return nlp(text)
    else:
        msg = f"Cannot get the Doc for '{text}' ({text_type})"
        logger.error(msg)
        raise TypeError(msg)


def extract_span_features(match_span: Span) -> SpanFeatures:
    logger.debug(f"Parsing the '{match_span}' Span")
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

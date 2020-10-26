import logging
from spacy.tokens import Doc, Span
from src.nlp import nlp # TODO make nlp an arg for dep inj
from .validator import is_not_type, is_truthy, is_type


logger = logging.getLogger(__name__)


def is_tokenized(maybe_tokenized):
    """Given any type, return a boolean."""
    logger.debug(f"Validating `{maybe_tokenized}`")
    is_not_type(maybe_tokenized, type(None))
    is_truthy(maybe_tokenized)

    logger.debug("Determining if input is already tokenized")
    if isinstance(maybe_tokenized, str):
        logger.debug("Not tokenized")
        return False
    elif isinstance(maybe_tokenized, Doc) or isinstance(maybe_tokenized, Span):
        logger.debug("Already tokenized")
        return True

    err_msg = f"Expected a string, Doc, or Span but got `{type(maybe_tokenized)}`"
    logger.error(err_msg)
    raise TypeError(err_msg)


def make_doc(maybe_tokenized):
    """Given a string, Doc, or Span, return a Doc."""
    logger.debug(f"Tokenizing `{maybe_tokenized}`")
    return nlp(maybe_tokenized) if not is_tokenized(maybe_tokenized) else maybe_tokenized


def get_span(phrase):
    """Given a str, a Span, or a Doc, return a Span."""
    span = None
    if type(phrase) == str:
        span = make_doc(phrase)[:]
    elif type(phrase) == Doc:
        span = phrase[:]
    elif type(phrase) == Span:
        span = phrase
    else:
        msg = f"Cannot get span of {type(phrase)}"
        logger.error(msg)
        raise TypeError(msg)
    return span

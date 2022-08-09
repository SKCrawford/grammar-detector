from logging import getLogger
from typing import Union
from spacy.tokens import Doc, Span
from ..nlp import nlp


logger = getLogger(__name__)


def get_doc(text: Union[str, Doc, Span]) -> Doc:
    """Coerce a `str`, `Doc`, or `Span` into a `Doc`. Raises a `TypeError` when `text` is none of these classes."""
    logger.info(f"Getting the Doc for '{text}' (text_type)")
    if isinstance(text, Doc):
        logger.debug("Skipping tokenizing")
        return text
    elif isinstance(text, Span):
        logger.debug("Converting the Span to a Doc")
        return text.as_doc()
    elif isinstance(text, str):
        logger.debug("Tokenizing")
        return nlp(text)
    else:
        msg = f"Cannot get the Doc for '{text}' ({type(text)})"
        logger.error(msg)
        raise TypeError(msg)

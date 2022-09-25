from logging import getLogger
from spacy import load as spacy_load
from spacy.language import Language
from spacy.tokens import Doc, Span
from typing import Union
from .defaults import LANGUAGE_MODEL
from .utils import singleton


logger = getLogger(__name__)


@singleton
class Nlp:
    def __init__(self, language_model: str = LANGUAGE_MODEL):
        self.label: str = language_model
        self._nlp: Language = spacy_load(self.label)

    def __call__(self, *args, **kwargs):
        return self._nlp(*args, **kwargs)


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
        return Nlp()(text)
    else:
        msg = f"Cannot get the Doc for '{text}' ({type(text)})"
        logger.error(msg)
        raise TypeError(msg)

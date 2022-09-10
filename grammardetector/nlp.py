from logging import getLogger
from spacy import load as spacy_load
from spacy.language import Language
from spacy.tokens import Doc, Span
from typing import Union
from .Config import Config


logger = getLogger(__name__)
dataset = Config().prop_str("DATASET")
logger.info(f"Started loading the spaCy model with the dataset '{dataset}'")

# Don't forget to run (with the appropriate dataset):
# $ python -m download en_core_web_lg
nlp: Language = spacy_load(dataset)
logger.info("Finished loading the spaCy model")


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

import logging
import spacy


logger = logging.getLogger(__name__)
logger.info("Started loading the spaCy model")

nlp = spacy.load("en_core_web_sm")

logger.info("Finished loading the spaCy model")

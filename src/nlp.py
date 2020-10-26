import logging
import spacy


logging.getLogger(__name__).info("Loading the spaCy model")
nlp = spacy.load("en_core_web_lg")

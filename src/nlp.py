import logging
import spacy


data = "en_core_web_lg"

logging.getLogger(__name__).info(f"Started loading the spaCy model with data '{data}'")
nlp = spacy.load(data)
logging.getLogger(__name__).info("Finished loading the spaCy model")

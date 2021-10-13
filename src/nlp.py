import logging
import spacy
from settings import SPACY_DATASET


logging.getLogger(__name__).info(
    f"Started loading the spaCy model with the dataset '{SPACY_DATASET}'"
)
# Don't forget to run (with the appropriate dataset):
# $ python -m download en_core_web_lg
nlp = spacy.load(SPACY_DATASET)
logging.getLogger(__name__).info("Finished loading the spaCy model")

from logging import getLogger
from spacy import load as spacy_load
import spacy
from settings import SPACY_DATASET


logger = getLogger(__name__)
logger.info(f"Started loading the spaCy model with the dataset '{SPACY_DATASET}'")

# Don't forget to run (with the appropriate dataset):
# $ python -m download en_core_web_lg
nlp = spacy.load(SPACY_DATASET)
logger.info("Finished loading the spaCy model")

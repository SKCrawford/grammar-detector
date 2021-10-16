from logging import getLogger
from spacy import load as spacy_load
from spacy.language import Language
from settings import config


logger = getLogger(__name__)
logger.info(
    f"Started loading the spaCy model with the dataset '{config.spacy_dataset}'"
)

# Don't forget to run (with the appropriate dataset):
# $ python -m download en_core_web_lg
nlp: Language = spacy_load(config.spacy_dataset)
logger.info("Finished loading the spaCy model")

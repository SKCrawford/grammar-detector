from logging import getLogger
from spacy import load as spacy_load
from spacy.language import Language
from settings import data_config


logger = getLogger(__name__)
logger.info(
    f"Started loading the spaCy model with the dataset {data_config.prop('DATASET')}"
)

# Don't forget to run (with the appropriate dataset):
# $ python -m download en_core_web_lg
nlp: Language = spacy_load(data_config.prop("DATASET"))
logger.info("Finished loading the spaCy model")

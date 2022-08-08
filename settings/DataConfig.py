import src.logger
from logging import getLogger
from .Config import Config


logger = getLogger(__name__)


class DataConfig(Config):
    """A class containing the configuration settings for the spaCy language model."""

    def __init__(self, config_file_path: str) -> None:
        logger.debug("Constructing the DataConfig")
        super().__init__(config_file_path)
        self.prefix = "DATA"

from logging import getLogger
from os.path import join
from .Config import Config


logger = getLogger(__name__)


class LoggerConfig(Config):
    """A class containing the configuration settings for the logger."""

    def __init__(self, config_file_path: str) -> None:
        logger.info("Constructing the LoggerConfig")
        super().__init__(config_file_path)
        self.prefix = "LOGGER"

    @property
    def host_dir_path(self):
        logger.debug(f"Getting the path for the logs dir")
        return join(self.project_root_path, self.prop_str("DIR"))

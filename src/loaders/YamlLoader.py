from logging import getLogger
from typing import Any, TextIO
from yaml import FullLoader as FullYamlLoader, load as load_yaml
from ..utils import singleton
from .FileLoader import FileLoader


logger = getLogger(__name__)


@singleton
class YamlLoader(FileLoader):
    def load(self, file: TextIO) -> Any:
        logger.debug(f"Loading the YAML file: {file}")
        return load_yaml(file, Loader=FullYamlLoader)

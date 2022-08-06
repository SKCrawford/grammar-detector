from logging import getLogger
from typing import Any, TextIO
from yaml import FullLoader as FullYamlLoader, load as load_yaml
from .utils import singleton


logger = getLogger(__name__)


# @singleton  # the parent inherits the child's singleton decorator
class FileLoader:
    def __call__(self, filepath: str) -> dict[str, Any]:
        with open(filepath, "r") as file:
            return self.load(file)

    def load(self, file: TextIO) -> dict[str, Any]:
        msg = f"load(file) was not implemented"
        logger.error(msg)
        raise NotImplementedError(msg)


@singleton
class YamlLoader(FileLoader):
    def load(self, file: TextIO) -> Any:
        logger.debug(f"Loading the YAML file: {file}")
        return load_yaml(file, Loader=FullYamlLoader)

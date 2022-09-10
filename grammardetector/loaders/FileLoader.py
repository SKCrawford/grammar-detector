from logging import getLogger
from typing import Any, TextIO


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

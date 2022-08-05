from logging import getLogger
from functools import cached_property
from os.path import split


logger = getLogger(__name__)


class Filepath:
    """A helper class for working with filepaths, especially with extracting a filepath's components."""

    def __init__(self, filepath: str) -> None:
        self._filepath: str = ""
        self.dir_path: str = ""
        self.filename: str = ""
        self.name: str = ""
        self.extension: str = ""

        self._filepath = str(filepath)
        [self.dir_path, self.filename] = split(self._filepath)
        [self.name, self.extension] = self.filename.split(".")

    @property
    def filepath(self) -> str:
        """The full filepath, including the directories, name, and extension."""
        return self._filepath

    @filepath.setter
    def filepath(self, _: str) -> None:
        msg = f"The internal filepath attribute cannot be modified"
        logger.error(msg)
        raise AttributeError(msg)

    @cached_property
    def is_hidden(self) -> bool:
        """Returns True if the file is a hidden file. Otherwise, returns False."""
        return bool(self.filename.startswith("."))

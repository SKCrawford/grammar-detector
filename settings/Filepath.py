import src.logger
from logging import getLogger
from functools import cached_property
from os.path import split


logger = getLogger(__name__)


class Filepath:
    """A helper class for working with filepaths, especially with extracting a filepath's components."""

    def __init__(self, filepath: str) -> None:
        self._filepath: str = str(filepath)
        self.dir_path: str = ""
        self.filename: str = ""
        self.name: str = ""
        self.extension: str = ""

        (self.dir_path, self.filename) = split(self._filepath)
        fname_splits = self.filename.split(".")
        # Use -2 instead of 0 because hidden files's 0 is an empty string
        self.name = fname_splits[-2]
        self.extension = fname_splits[-1]

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

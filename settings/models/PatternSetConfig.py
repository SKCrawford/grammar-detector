from logging import getLogger
from os import listdir
from os.path import join
from .Config import Config


logger = getLogger(__name__)


def has_extension(expected_extension: str, filename: str) -> bool:
    """Returns True if a file's filename ends with the expected extension. Otherwise, returns False."""
    return bool(str(filename).endswith(expected_extension))


def is_hidden_file(filename: str) -> bool:
    """Returns True if a file's filename indicates whether it is a hidden filename. Otherwise, returns False."""
    return bool(str(filename).startswith("."))


def trim_extension(extension: str, filename: str) -> str:
    return filename.replace(extension, "")


class PatternSetConfig(Config):
    """A class containing the configuration settings for the patternset directory and files."""

    def __init__(self, config_file_path: str) -> None:
        logger.info("Constructing the PatternSetConfig")
        super().__init__(config_file_path)
        self.prefix = "PATTERN_SET"

    def _validate_filename(self, filename: str) -> bool:
        """Returns True if the filename is valid for patternset file. Otherwise, returns False."""
        logger.debug(f"Validating patternset filename '{filename}'")
        is_hidden: bool = is_hidden_file(filename)
        expected_extension: str = self.prop_str("FILE_EXTENSION")
        has_correct_extension: bool = has_extension(expected_extension, filename)
        return bool(not is_hidden and has_correct_extension)

    @property
    def host_dir_path(self) -> str:
        """Return the full path of the directory containing the patternsets."""
        logger.debug(f"Getting the filepath for the patternsets dir")
        dir_path_override = self.prop_str("HOST_DIR_PATH")
        if dir_path_override:
            return dir_path_override
        return join(self.project_root_path, self.prop_str("HOST_DIR"))

    @property
    def paths(self) -> list[str]:
        """Returns a list of the existing patternsets with the file extension."""
        logger.debug("Getting the list of patternsets filepaths in the patternsets dir")
        filenames: list[str] = listdir(self.host_dir_path)
        logger.info("Validating PatternSet filenames")
        return [fn for fn in filenames if self._validate_filename(fn)]

    @property
    def names(self) -> list[str]:
        """Returns a list of the existing patternsets without the file extension."""
        logger.info("Getting the list of patternsets in the patternsets dir")
        extension: str = "." + self.prop_str("FILE_EXTENSION")
        return [trim_extension(extension, path) for path in self.paths]

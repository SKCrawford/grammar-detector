from logging import getLogger
from os import listdir
from os.path import join
from .Config import Config
from .Filepath import Filepath


logger = getLogger(__name__)


class PatternSetConfig(Config):
    """A class containing the configuration settings for the patternset directory and files."""

    def __init__(self, config_file_path: str) -> None:
        logger.debug("Constructing the PatternSetConfig")
        self.config_fp: Filepath = Filepath(config_file_path)
        super().__init__(self.config_fp.filepath)
        self.prefix = "PATTERN_SET"

    @property
    def internal_patternset_dirpath(self) -> str:
        return join(self.project_root_path, self.prop_str("HOST_DIR"))

    @property
    def internal_patternset_filenames(self):
        filenames: list[str] = listdir(self.internal_patternset_dirpath)
        return [fname for fname in filenames if self.is_valid_filename(fname)]

    @property
    def internal_patternset_filepaths(self):
        filepaths = []
        for fname in self.internal_patternset_filenames:
            fpath = join(self.internal_patternset_dirpath, fname)
            filepaths.append(fpath)
        return filepaths

    def is_valid_filename(self, filename: str) -> bool:
        """Returns True if the filename is valid for patternset file. Otherwise, returns False."""
        logger.debug(f"Validating patternset filename '{filename}'")
        pset_fp: Filepath = Filepath(filename)
        has_extension: bool = bool(pset_fp.extension == self.prop_str("FILE_EXTENSION"))
        return bool(not pset_fp.is_hidden and has_extension)

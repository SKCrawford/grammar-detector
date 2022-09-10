from logging import getLogger
from os import listdir
from os.path import abspath, join
from pathlib import Path
from typing import Any
from yaml import FullLoader, load as load_yaml
from .utils import Filepath, singleton


PATTERN_SET_FILE_EXTENSION: str = "yaml"
PATTERN_SET_HOST_DIR: str = "patternsets"


logger = getLogger(__name__)


@singleton
class Config:
    """A class for managing configuration settings."""
    @property
    def project_root_path(self) -> str:
        """Returns the full path of the project's root directory."""
        p = abspath(__file__)
        return str(Path(p).parents[1])

    @property
    def internal_patternset_dirpath(self) -> str:
        """Returns the filepath to the directory containing the internal patternsets."""
        return join(self.project_root_path, PATTERN_SET_HOST_DIR)

    @property
    def internal_patternset_filenames(self) -> list[str]:
        """Returns a list of the internal patternsets' filenames with the extension."""
        filenames: list[str] = listdir(self.internal_patternset_dirpath)
        return [fn for fn in filenames if self.is_valid_patternset_filename(fn)]

    @property
    def internal_patternset_filepaths(self) -> list[str]:
        """Returns a list of the internal patternsets' filepaths."""
        filepaths = []
        for fname in self.internal_patternset_filenames:
            fpath = join(self.internal_patternset_dirpath, fname)
            filepaths.append(fpath)
        return filepaths

    def is_valid_patternset_filename(self, filename: str) -> bool:
        """Returns True if the filename is valid for patternset file. Otherwise, returns False."""
        logger.debug(f"Validating patternset filename '{filename}'")
        fp: Filepath = Filepath(filename)
        has_ext = bool(fp.extension == PATTERN_SET_FILE_EXTENSION)
        return bool(not fp.is_hidden and has_ext)

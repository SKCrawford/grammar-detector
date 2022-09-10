from logging import getLogger
from os import listdir
from os.path import abspath, join
from pathlib import Path
from typing import Any
from yaml import FullLoader, load as load_yaml
from .utils import Filepath, singleton


logger = getLogger(__name__)


@singleton
class Config:
    """A class for managing configuration settings."""

    def __init__(self, config_file_path: str = "settings/settings.yaml") -> None:
        with open(config_file_path, "r") as f:
            self._settings = load_yaml(f, Loader=FullLoader)

    def _prop(self, property_name: str) -> Any:
        """Returns the config setting for `property_name`. Fails loudly."""
        property_name = property_name.upper()
        setting: Any = self._settings[property_name]
        logger.debug(f"Found '{setting}' for config setting '{property_name}'")
        return setting

    def prop_str(self, property_name: str) -> str:
        """Coerces the settings property to guarantee type safety."""
        return str(self._prop(property_name))

    def prop_bool(self, property_name: str) -> bool:
        """Coerces the settings property to guarantee type safety."""
        return bool(self._prop(property_name))

    def prop_int(self, property_name: str) -> int:
        """Coerces the settings property to guarantee type safety."""
        return int(self._prop(property_name))

    def prop_float(self, property_name: str) -> float:
        """Coerces the settings property to guarantee type safety."""
        return float(self._prop(property_name))

    @property
    def project_root_path(self) -> str:
        """Returns the full path of the project's root directory."""
        p = abspath(__file__)
        return str(Path(p).parents[1])

    @property
    def internal_patternset_dirpath(self) -> str:
        """Returns the filepath to the directory containing the internal patternsets."""
        return join(self.project_root_path, self.prop_str("PATTERN_SET_HOST_DIR"))

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
        has_ext = bool(fp.extension == self.prop_str("PATTERN_SET_FILE_EXTENSION"))
        return bool(not fp.is_hidden and has_ext)

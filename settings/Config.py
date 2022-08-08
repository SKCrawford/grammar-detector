from logging import getLogger
from os.path import abspath
from pathlib import Path
from typing import Any
from yaml import FullLoader, load as load_yaml


logger = getLogger(__name__)


class Config:
    """A class for managing configuration settings. When extending `Config`, set the `prefix` attribute in the constructor."""

    def __init__(self, config_file_path: str) -> None:
        logger.info("Constructing the Config")
        self.prefix: str = ""

        logger.info(f"Loading the config file at {config_file_path}")
        self.config_file_path = config_file_path
        with open(config_file_path, "r") as f:
            self._settings = load_yaml(f, Loader=FullLoader)

    def _prop(self, property_name: str) -> Any:
        """Returns the config setting for `property_name`. Fails loudly."""
        if self.prefix:
            property_name = f"{self.prefix}_{property_name}"
        property_name = property_name.upper()
        value = self._settings[property_name]
        logger.debug(f"Found '{value}' for config setting '{property_name}'")
        return self._settings[property_name]

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

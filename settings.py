from __future__ import annotations  # Required for typing ConfigFactory
from logging import DEBUG, getLogger
from os import listdir, path
from typing import Any, cast, Optional, TextIO, TypeVar, Union
from yaml import FullLoader, load as load_yaml


# Adopted from: https://www.hackerearth.com/practice/notes/samarthbhargav/a-design-pattern-for-configuration-management-in-python/


ConfigSetting = Union[str, bool, int, float]
ConfigDict = dict[str, ConfigSetting]
T = TypeVar("T", bound="Config")


logger = getLogger(__name__)


# TODO refactor this out
config_file_path: str = "settings.yaml"


def has_extension(expected_extension: str, filename: str) -> bool:
    """Returns True if a file's filename ends with the expected extension. Otherwise, returns False."""
    return bool(str(filename).endswith(expected_extension))


def is_hidden_file(filename: str) -> bool:
    """Returns True if a file's filename indicates whether it is a hidden filename. Otherwise, returns False."""
    return bool(str(filename).startswith("."))


def trim_extension(extension: str, filename: str) -> str:
    return filename.replace(extension, "")


# The values are easily configurable whereas the keys themselves are not configurable.
class Config:
    """A class for managing configuration settings. To create one, either use the `ConfigFactory` class or extend `Config`. When using the `ConfigFactory` class, specify the prefix in the `create` method. When extending `Config`, set the `prefix` attribute in the constructor."""

    def __init__(self, config_dict: ConfigDict) -> None:
        logger.info("Constructing the Config")
        self._settings = config_dict
        self.prefix: str = ""

    def _prop(self, property_name: str) -> Any:
        """Returns the config setting for `property_name`. Fails loudly."""
        if self.prefix:
            property_name = f"{self.prefix}_{property_name}"
        logger.debug(f"Getting the config setting '{property_name}'")
        property_name = property_name.upper()
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
        return path.dirname(path.abspath(__file__))


class PatternSetConfig(Config):
    """A class containing the configuration settings for the patternset directory and files."""

    def __init__(self, config_dict: ConfigDict) -> None:
        logger.info("Constructing the PatternSetConfig")
        super().__init__(config_dict)
        self.prefix = "PATTERN_SET"
        self.keys: Config = Config({})  # Shortcut dummy for PatternSetConfigKeys
        self.values: Config = Config({})  # Shortcut dummy for PatternSetConfigValues

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
        return path.join(self.project_root_path, self.prop_str("HOST_DIR"))

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


class ConfigFactory:
    """A helper class for creating instances of the `Config` class. Load the YAML settings file using the `load()` method, then construct new `Config` instances using the `create()` method."""

    def __init__(self) -> None:
        logger.info("Constructing the ConfigFactory")
        self._cache: dict[str, Config] = {}
        self.settings: ConfigDict = {}

    # def load(self, config_file_path: str) -> ConfigFactory:
    def load(self, config_file_path: str):
        """Load a YAML file containing the configuration settings to the attribute `settings`. Returns the ConfigFactory instance."""
        logger.info(f"Loading the config file at {config_file_path}")
        self.config_file_path = config_file_path
        with open(config_file_path, "r") as f:
            self.settings = load_yaml(f, Loader=FullLoader)
        return self

    def create(self, prefix: str) -> Config:
        """Constructs a new Config instance and sets its prefix to the `prefix` attribute. The `load()` method must be called prior to this method."""
        logger.info(f"Creating a new Config with the '{prefix}' prefix")

        # Check call order
        if not self.settings:
            msg = "The config file has not yet been loaded. Load it using the `load()` method."
            logger.error(msg)
            raise Exception(msg)

        # Search cache
        prefix = prefix.upper()
        if prefix in self._cache:
            return self._cache[prefix]

        # Create then cache
        instance = Config(self.settings)
        instance.prefix = prefix
        self._cache[instance.prefix] = instance
        return instance


config_factory = ConfigFactory().load(config_file_path)
data_config = config_factory.create("DATA")
logger_config = config_factory.create("LOGGER")

pattern_set_config = PatternSetConfig(config_factory.settings)
pattern_set_config_keys = config_factory.create("PATTERN_SET_KEY")
pattern_set_config_values = config_factory.create("PATTERN_SET_VAL")

pattern_set_config.keys = pattern_set_config_keys  # For convenience
pattern_set_config.values = pattern_set_config_values  # For convenience

from logging import DEBUG
from os import listdir, path
from typing import Optional, TextIO, Union
from yaml import FullLoader, load as load_yaml


# Adopted from: https://www.hackerearth.com/practice/notes/samarthbhargav/a-design-pattern-for-configuration-management-in-python/


ConfigSetting = Union[str, bool, int, float]
ConfigDict = dict[str, ConfigSetting]


# TODO refactor this out
config_file_path: str = "settings.yaml"


# The values are easily configurable whereas the keys themselves are not configurable.
class Config:
    """A class for managing configuration settings. To create one, either use the `ConfigFactory` class or extend `Config`. When using the `ConfigFactory` class, specify the prefix in the `create` method. When extending `Config`, set the `prefix` attribute in the constructor."""

    def __init__(self, config_dict: ConfigDict) -> None:
        self._settings = config_dict
        self.prefix = None  # Set the prefix in the constructor of extending classes

    def prop(self, property_name: str) -> ConfigSetting:
        """Return a configuration setting matching the pattern `{prefix}_{property_name}`. Fails loudly via KeyError."""
        if self.prefix:
            property_name = f"{self.prefix}_{property_name}"
        property_name = property_name.upper()
        return self._settings[property_name]

    @property
    def project_root_path(self) -> str:
        """Return the full path of the project's root directory."""
        return path.dirname(path.abspath(__file__))


class PatternSetConfig(Config):
    """A class containing the configuration settings for the patternset directory and files."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prefix = "PATTERN_SET"
        self.keys = None  # Shortcut for PatternSetConfigKeys
        self.values = None  # Shortcut for PatternSetConfigValues

    def _validate_pattern_set_file(self, file: TextIO) -> bool:
        """Return True if the file is a valid patternset file. Otherwise, return False."""
        is_hidden_file = lambda f: bool(f.startswith("."))
        is_correct_extension = lambda f: bool(f.endswith(self.prop("FILE_EXTENSION")))
        return bool(not is_hidden_file(file) and is_correct_extension(file))

    @property
    def host_dir_path(self) -> str:
        """Return the full path of the directory containing the patternsets."""
        if self.prop("HOST_DIR_PATH"):  # Set manually
            return self.prop("HOST_DIR_PATH")
        return path.join(self.project_root_path, self.prop("HOST_DIR"))

    @property
    def paths(self) -> list[str]:
        """Return a list of the existing patternsets with the file extension."""
        if self.prop("PATHS"):  # Set manually
            return self.prop("PATHS")
        pset_files = listdir(self.host_dir_path)
        return [str(f) for f in pset_files if self._validate_pattern_set_file(f)]

    @property
    def names(self) -> list[str]:
        """Return a list of the existing patternsets without the file extension."""
        if self.prop("NAMES"):  # Set manually
            return self.prop("NAMES")
        file_extension = "." + self.prop("FILE_EXTENSION")
        trim_extension = lambda p: p.replace(file_extension, "")
        return [trim_extension(path) for path in self.paths]


class ConfigFactory:
    """A helper class for creating instances of the `Config` class. Load the YAML settings file using the `load` method, then construct new `Config` instances using the `create` method."""

    def __init__(self):
        self._cache: dict[str, Config] = {}
        self.settings: ConfigDict = {}

    def load(self, config_file_path: str):  # -> ConfigFactory
        """Load a YAML file containing the configuration settings to the attribute `settings`. Returns the ConfigFactory instance."""
        self.config_file_path = config_file_path
        with open(config_file_path, "r") as f:
            self.settings = load_yaml(f, Loader=FullLoader)
        return self

    def create(self, prefix: str) -> Config:
        """Construct a new Config instance and set its prefix to the attribute `prefix`. The method `load()` must be called prior to this method."""
        # Check call order
        if not self.settings:
            msg = "The config file has not yet been loaded. Load it using the `load` method."
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

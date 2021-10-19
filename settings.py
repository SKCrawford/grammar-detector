from logging import DEBUG
from os import listdir, path
from typing import TextIO, Union


# source: https://www.hackerearth.com/practice/notes/samarthbhargav/a-design-pattern-for-configuration-management-in-python/


ConfigDict = dict[str, Union[str, bool, int, float]]


# The values are easily configurable whereas the keys themselves are not configurable.
_config_dict: ConfigDict = {
    # # Configurations for the language data
    "DATA_DATASET": "en_core_web_lg",
    # #
    # # Configurations for the logger
    "LOGGER_DIR": ".logs",
    "LOGGER_FILE_DEBUG": "debug.log",
    "LOGGER_FILE_LAST": "last.log",
    "LOGGER_FILE_TEST": "test.log",
    "LOGGER_FORMAT": "[%(asctime)s][%(module)s:%(funcName)s:%(lineno)d][%(levelname)s] %(message)s",
    "LOGGER_LEVEL": DEBUG,
    # #
    # # Base configurations for the pattern sets outside of the patternset file
    "PATTERN_SET_FILE_EXTENSION": "yaml",
    "PATTERN_SET_HOST_DIR": "patterns",
    # "PATTERN_SET_HOST_DIR_PATH": manually override the setting for pset_config.host_dir_path
    # "PATTERN_SET_NAMES": manually override the setting for pset_config.names
    # "PATTERN_SET_PATHS": manually override the setting for pset_config.paths
    # #
    # # Acceptable keys for configuring patternset files (see the template for the structure)
    "PATTERN_SET_KEY_BEST_MATCH": "best_match",
    "PATTERN_SET_KEY_HOW_MANY_MATCHES": "how_many_matches",
    "PATTERN_SET_KEY_META": "meta",
    "PATTERN_SET_KEY_PATTERNS": "patterns",
    "PATTERN_SET_KEY_RULENAME": "rulename",
    "PATTERN_SET_KEY_SHOULD_EXTRACT_NOUN_CHUNKS": "extract_noun_chunks",
    "PATTERN_SET_KEY_SKIP_TESTS": "skip_tests",
    "PATTERN_SET_KEY_TESTS": "tests",
    "PATTERN_SET_KEY_TESTS_INPUT": "input",
    "PATTERN_SET_KEY_TESTS_RULENAMES": "rulenames",
    "PATTERN_SET_KEY_TESTS_SKIP": "skip",
    "PATTERN_SET_KEY_TESTS_SPANS": "spans",
    "PATTERN_SET_KEY_TOKENS": "tokens",
    # #
    # # Acceptable values for configuring patternset files
    "PATTERN_SET_VAL_ALL_MATCHES": "all",
    "PATTERN_SET_VAL_FIRST_MATCH": "last",  # NYI
    "PATTERN_SET_VAL_LAST_MATCH": "first",  # NYI
    "PATTERN_SET_VAL_LONGEST_MATCH": "longest",  # Currently the only choice
    "PATTERN_SET_VAL_ONE_MATCH": "one",
    "PATTERN_SET_VAL_SHORTEST_MATCH": "shortest",  # NYI
}


class _ConfigBase:
    """The base class from which config classes are derived. This class is not intended for direct use."""

    def __init__(self, config_dict: ConfigDict):
        self._config = config_dict or {}

    def prop(self, property_name: str):
        """Return a configuration setting. Fails loudly via KeyError."""
        property_name = property_name.upper()
        if property_name not in self._config:
            return None
        return self._config[property_name]

    @property
    def project_root_path(self) -> str:
        """Return the full path of the project's root directory."""
        return path.dirname(path.abspath(__file__))


class DataConfig(_ConfigBase):
    """A class containing the configuration settings for the language data."""

    def prop(self, property_name: str) -> str:
        """Return a language data configuration setting."""
        return super().prop(f"DATA_{property_name}")


class LoggerConfig(_ConfigBase):
    """A class containing the configuration settings for the logger."""

    def prop(self, property_name: str) -> str:
        """Return a logger configuration setting."""
        return super().prop(f"LOGGER_{property_name}")


class PatternSetConfig(_ConfigBase):
    """A class containing the configuration settings for the patternset dir and files."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.keys = None  # Shortcut for PatternSetConfigKeys
        self.values = None  # Shortcut for PatternSetConfigValues

    def _validate_pattern_set_file(self, file: TextIO) -> bool:
        """Return True if the file is a valid patternset file. Otherwise, return False."""
        is_hidden_file = lambda f: bool(f.startswith("."))
        is_correct_extension = lambda f: bool(f.endswith(self.prop("FILE_EXTENSION")))
        return bool(not is_hidden_file(file) and is_correct_extension(file))

    def prop(self, property_name: str) -> str:
        """Return a patternset configuration setting."""
        return super().prop(f"PATTERN_SET_{property_name}")

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


class PatternSetConfigKeys(_ConfigBase):
    """A class containing the valid keys for patternset file configuration."""

    def prop(self, property_name: str) -> str:
        """Return a patternset configuration key."""
        return super().prop(f"PATTERN_SET_KEY_{property_name}")


class PatternSetConfigValues(_ConfigBase):
    """A class containing the valid values for patternset file configuration."""

    def prop(self, property_name: str) -> str:
        """Return a patternset configuration value."""
        return super().prop(f"PATTERN_SET_VAL_{property_name}")


data_config = DataConfig(_config_dict)

logger_config = LoggerConfig(_config_dict)

pattern_set_config = PatternSetConfig(_config_dict)

pattern_set_config_keys = PatternSetConfigKeys(_config_dict)

pattern_set_config_values = PatternSetConfigValues(_config_dict)

pattern_set_config.keys = pattern_set_config_keys  # For convenience
pattern_set_config.values = pattern_set_config_values  # For convenience

from os.path import join
from .models import DataConfig, LoggerConfig, PatternSetConfig


def settings_path(filename: str) -> str:
    dir_path = "settings/"
    filetype = "yaml"
    return join(dir_path, f"{filename}.{filetype}")


data_config = DataConfig(settings_path("data"))
logger_config = LoggerConfig(settings_path("logger"))
pattern_set_config = PatternSetConfig(settings_path("patternsets"))

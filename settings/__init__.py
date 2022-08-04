from os.path import join
from .DataConfig import DataConfig
from .LoggerConfig import LoggerConfig
from .PatternSetConfig import PatternSetConfig


settings_filepath = "settings.yaml"

data_config = DataConfig(settings_filepath)
logger_config = LoggerConfig(settings_filepath)
pattern_set_config = PatternSetConfig(settings_filepath)

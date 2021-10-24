import logging
from os.path import join
from settings import logger_config


last_filepath = join(logger_config.prop_str("DIR"), logger_config.prop_str("FILE_LAST"))
last_filehandler = logging.FileHandler(last_filepath, mode="w+")

debug_filepath = join(
    logger_config.prop_str("DIR"), logger_config.prop_str("FILE_DEBUG")
)
debug_filehandler = logging.FileHandler(debug_filepath, mode="a+")

logging.basicConfig(
    format=logger_config.prop_str("FORMAT"),
    level=logger_config.prop_int("LEVEL"),
    handlers=[last_filehandler, debug_filehandler],
)

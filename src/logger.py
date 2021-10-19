import logging
from os.path import join
from settings import logger_config


last_filepath = join(logger_config.prop("DIR"), logger_config.prop("FILE_LAST"))
last_filehandler = logging.FileHandler(last_filepath, mode="w+")

debug_filepath = join(logger_config.prop("DIR"), logger_config.prop("FILE_DEBUG"))
debug_filehandler = logging.FileHandler(debug_filepath, mode="a+")

logging.basicConfig(
    format=logger_config.prop("FORMAT"),
    level=logger_config.prop("LEVEL"),
    handlers=[last_filehandler, debug_filehandler],
)

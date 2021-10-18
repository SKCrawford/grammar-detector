import logging
from os.path import join
from settings import LoggerConfig


last_filepath = join(LoggerConfig.DIR.value, LoggerConfig.FILE_LAST.value)
last_filehandler = logging.FileHandler(last_filepath, mode="w+")

debug_filepath = join(LoggerConfig.DIR.value, LoggerConfig.FILE_DEBUG.value)
debug_filehandler = logging.FileHandler(debug_filepath, mode="a+")

logging.basicConfig(
    format=LoggerConfig.FORMAT.value,
    level=LoggerConfig.LEVEL.value,
    handlers=[last_filehandler, debug_filehandler],
)

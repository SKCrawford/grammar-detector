import logging
from settings import LoggerConfig


last_filehandler = logging.FileHandler(LoggerConfig.FILE_LAST.value, mode="w")
debug_filehandler = logging.FileHandler(LoggerConfig.FILE_DEBUG.value)

logging.basicConfig(
    format=LoggerConfig.FORMAT.value,
    level=LoggerConfig.LEVEL.value,
    handlers=[last_filehandler, debug_filehandler],
)

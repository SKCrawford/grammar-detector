import logging
from settings import LOG_FILE_DEBUG, LOG_FILE_LAST, LOG_FORMAT, LOG_LEVEL


last_filehandler = logging.FileHandler(LOG_FILE_LAST, mode="w")
debug_filehandler = logging.FileHandler(LOG_FILE_DEBUG)

logging.basicConfig(
    format=LOG_FORMAT, level=LOG_LEVEL, handlers=[last_filehandler, debug_filehandler]
)

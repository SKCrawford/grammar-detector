import logging
from logging import basicConfig, Formatter, StreamHandler
import sys
from settings import logger_config


basic_formatter = Formatter(fmt=logger_config.prop_str("FORMAT_BASIC"))
detailed_formatter = Formatter(fmt=logger_config.prop_str("FORMAT_DETAILED"))

handler = StreamHandler(sys.stdout)
level: int = logger_config.prop_int("LEVEL")
formatter: Formatter = basic_formatter if level == logging.INFO else detailed_formatter
handler.setFormatter(formatter)

error_handler = StreamHandler(sys.stderr)
error_handler.setLevel(logging.WARNING)
error_handler.setFormatter(detailed_formatter)

basicConfig(
    level=level,
    handlers=[handler, error_handler],
)

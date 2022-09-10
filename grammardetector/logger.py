from logging import basicConfig, Formatter, INFO, StreamHandler, WARNING
from sys import stderr, stdout
from .Config import Config


def configure_logger(config: Config, log_level: int):
    basic_formatter = Formatter(fmt=config.prop_str("LOGGER_FORMAT_BASIC"))
    detailed_formatter = Formatter(fmt=config.prop_str("LOGGER_FORMAT_DETAILED"))

    handler = StreamHandler(stdout)
    formatter: Formatter = basic_formatter if log_level == INFO else detailed_formatter
    handler.setFormatter(formatter)

    error_handler = StreamHandler(stderr)
    error_handler.setLevel(WARNING)
    error_handler.setFormatter(detailed_formatter)

    basicConfig(level=log_level, handlers=[handler, error_handler])

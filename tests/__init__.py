from logging import basicConfig
from settings import LoggerConfig


basicConfig(
    filename=LoggerConfig.FILE_TEST.value,
    filemode="w",
    format=LoggerConfig.FORMAT.value,
    level=LoggerConfig.LEVEL.value,
)

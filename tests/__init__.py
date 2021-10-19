from logging import basicConfig
from os.path import join
from settings import logger_config


log_file_path = join(
    logger_config.project_root_path,
    logger_config.prop("DIR"),
    logger_config.prop("FILE_TEST"),
)


basicConfig(
    filename=logger_config.prop("FILE_TEST"),
    filemode="w+",
    format=logger_config.prop("FORMAT"),
    level=logger_config.prop("LEVEL"),
)

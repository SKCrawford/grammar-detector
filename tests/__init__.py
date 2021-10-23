from logging import basicConfig
from os.path import join
from settings import logger_config


log_file_path = join(
    logger_config.project_root_path,
    logger_config.prop_str("DIR"),
    logger_config.prop_str("FILE_TEST"),
)


basicConfig(
    filename=log_file_path,
    filemode="w+",
    format=logger_config.prop_str("FORMAT"),
    level=logger_config.prop_int("LEVEL"),
)

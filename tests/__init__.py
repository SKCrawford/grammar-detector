import logging
from settings import LOG_FILE_TEST


logging.basicConfig(
    filename=LOG_FILE_TEST,
    filemode="w",
    format="[%(asctime)s][%(module)s:%(funcName)s:%(lineno)d][%(levelname)s] %(message)s",
    level=logging.DEBUG,
)

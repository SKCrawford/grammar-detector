import logging


logging.basicConfig(
    filename="info.log",
    format="[%(asctime)s][%(module)s:%(funcName)s:%(lineno)d][%(levelname)s] %(message)s",
    level=logging.DEBUG,
)

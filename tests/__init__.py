import logging


logging.basicConfig(
    filename="test.log",
    filemode="w",
    format="[%(asctime)s][%(module)s:%(funcName)s:%(lineno)d][%(levelname)s] %(message)s",
    level=logging.DEBUG,
)

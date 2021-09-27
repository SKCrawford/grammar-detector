import logging


FORMAT = "[%(asctime)s][%(module)s:%(funcName)s:%(lineno)d][%(levelname)s] %(message)s"
LEVEL = logging.DEBUG

last_filehandler = logging.FileHandler("last.log", mode="w")
debug_filehandler = logging.FileHandler("debug.log")

logging.basicConfig(
    format=FORMAT, level=LEVEL, handlers=[last_filehandler, debug_filehandler]
)

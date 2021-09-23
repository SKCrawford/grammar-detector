import logging
from json import load
from os.path import join
from settings import PATTERNS_DIR


logger = logging.getLogger(__name__)


def load_patternset(patternset_filename):
    """Given a filepath ending with .json, """
    patternset_path = join(PATTERNS_DIR, f"{patternset_filename}.json")
    logger.debug(f"Loading {patternset_path}")
    with open(patternset_path, "r") as f:
        try:
            return load(f)
        except FileNotFoundError as e:
            logger.error(f"Couldn't find {patternset_path}")
            raise e
        except Exception as e:
            logger.error(f"Unknown error occurred while loading {patternset_path}")
            raise e

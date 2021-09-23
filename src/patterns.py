import logging
from json import load
from os.path import join
from settings import PATTERNS_DIR


logger = logging.getLogger(__name__)


def load_patternset(pattern_filename):
    """Given a filepath ending with .json, """
    pattern_path = join(PATTERNS_DIR, f"{pattern_filename}.json")
    logger.debug(f"Loading {pattern_path}")
    with open(pattern_path, "r") as f:
        try:
            return load(f)
        except FileNotFoundError as e:
            logger.error(f"Couldn't find {pattern_path}")
            raise e
        except Exception as e:
            logger.error(f"Unknown error occurred while loading {pattern_path}")
            raise e

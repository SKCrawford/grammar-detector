import logging
from json import load
from os.path import join
from settings import PATTERNS_DIR_PATH, PATTERNS_DIR_FILE_EXTENSION


logger = logging.getLogger(__name__)


def load_pattern_set(pattern_set_filename):
    """Given a filepath ending with .json, return loaded JSON data."""
    pattern_set_path = join(
        PATTERNS_DIR_PATH, f"{pattern_set_filename}.{PATTERNS_DIR_FILE_EXTENSION}"
    )
    logger.debug(f"Started loading {pattern_set_path}")

    try:
        with open(pattern_set_path, "r") as f:
            result = load(f)
            logger.debug(f"Finished loading {pattern_set_path}")
            return result
    except FileNotFoundError as e:
        logger.error(f"Couldn't find {pattern_set_path}")
        raise e
    except Exception as e:
        logger.error(f"Unknown error occurred while loading {pattern_set_path}")
        raise e

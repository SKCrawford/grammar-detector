import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

PATTERNS_DIR = os.path.join(ROOT_DIR, "patterns/")

PATTERN_SETS_PATHS = os.listdir(PATTERNS_DIR)

PATTERN_SETS_NAMES = [psp.replace(".json", "") for psp in PATTERN_SETS_PATHS]

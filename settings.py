import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

PATTERNS_DIR = os.path.join(ROOT_DIR, "patterns/")

PATTERN_SETS_PATHS = [f for f in os.listdir(PATTERNS_DIR) if not f.startswith(".")]

PATTERN_SETS_NAMES = [psp.replace(".json", "") for psp in PATTERN_SETS_PATHS]

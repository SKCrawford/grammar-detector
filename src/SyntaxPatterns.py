import json
import logging
import os
from src.util.decorator import singleton


logger = logging.getLogger(__name__)
patterns_json_path = f"{os.path.dirname(__file__)}/../patterns.json"


@singleton
class SyntaxPatterns:
    """The master record of syntax patterns. Loads the patterns.json in
    the root of the repo on construction. The same instance is always returned
    because the patterns do not change at runtime.
    """

    def __init__(self):
        logger.debug(f"Loading syntax patterns from the JSON file at `{patterns_json_path}`")
        self.patterns = self._load_syntax_patterns()

    def _load_syntax_patterns(self):
        with open(patterns_json_path, "r") as f:
            return json.load(f)

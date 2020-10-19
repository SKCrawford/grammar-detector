from src.SyntaxPatterns import SyntaxPatterns
from .model import PatternSet


class PatternSetFactory:
    """A convenience class for building PatternSet instances."""

    def __init__(self):
        self._pattern_set = None

    def set_json_key(self, json_key):
        self._json_key = json_key
        return self

    def set_name(self, name):
        self._name = name
        return self

    def build(self):
        self._pattern_set = PatternSet(self._name)
        patterns = SyntaxPatterns().patterns[self._json_key]
        for name in patterns:
            tokens = patterns[name]
            self._pattern_set.create(name, tokens)
        return self._pattern_set

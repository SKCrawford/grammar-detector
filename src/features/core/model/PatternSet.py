from .Pattern import Pattern
from .PatternValidator import PatternValidator


class PatternSet:
    """A named collection of patterns."""

    name = "untitled pattern set"
    _patterns = {}
    _validator = PatternValidator()

    def __init__(self, name):
        self.name = name

    def create(self, name, tokens):
        """Create and save a pattern.

        Given a string and a list of tokens, return None.
        """
        self._validator.validate_name(name)
        self._validator.validate_tokens(tokens)
        self._patterns[name] = Pattern(name, tokens)

    def find(self, name):
        """Find a pattern by name.

        Given a string, return a pattern.
        """
        self._validator.validate_name(name)
        return self._patterns[name]

    def find_all(self):
        """Find all patterns.

        Given no args, returns a list of patterns.
        """
        if not len(self._patterns):
            return []
        return [self.find(key) for key in self._patterns]

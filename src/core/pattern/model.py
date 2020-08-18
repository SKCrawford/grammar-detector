from .validator import validate_pattern


default_pattern_name = "untitled pattern"
default_pattern_set_name = "untitled pattern set"


class Pattern:
    """A named list of tokens.

    Usage: `matcher.add(pattern.name, [pattern.tokens])`
    """

    name = default_pattern_name
    tokens = []

    def __init__(self, name, tokens):
        if not name: 
            name = default_pattern_name
        self.name = name
        self.tokens = tokens


class PatternSet:
    """A named collection of patterns."""

    name = ""
    _patterns = {}

    def __init__(self, name):
        if not name: 
            name = default_pattern_set_name
        self.name = name


    def create(self, name, tokens):
        """Create and save a pattern.

        Given a string and a list of tokens, return void.
        """
        validate_pattern(name, tokens)
        self._patterns[name] = Pattern(name, tokens)

    def find(self, name):
        """Find a pattern by name.

        Given a string, return a Pattern instance.
        """
        return self._patterns[name]

    def find_all(self):
        """Find all patterns.

        Given void, returns a list<Pattern>.
        """
        if not len(self._patterns):
            return []
        return [self.find(key) for key in self._patterns]

class Pattern:
    def __init__(self, rulename, value, tokens, *args, **kwargs):
        """Accepts a string, a primitive, and a list of spaCy tokens."""
        self.rulename = rulename
        self.value = value
        self.tokens = tokens


class PatternSet:
    def __init__(self, name, patterns):
        """Accepts a string, a primitive, and a list of spaCy tokens."""
        self.name = name
        self.patterns = patterns


class PatternLoader:
    def __init__(self, TODO, *args, **kwargs):
        super().__init__(*args, **kwargs)

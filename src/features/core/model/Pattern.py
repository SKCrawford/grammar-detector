class Pattern:
    """A named list of tokens.

    Usage: `matcher.add(pattern.name, [pattern.tokens])`
    """

    name = "untitled pattern"
    tokens = []

    def __init__(self, name, tokens):
        self.name = name
        self.tokens = tokens

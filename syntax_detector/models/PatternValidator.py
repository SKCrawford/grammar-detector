class PatternValidator:
    """Validate attributes of a potential pattern."""

    def validate_name(self, name):
        if not isinstance(name, str):
            raise TypeError(f"expects a string but received {type(name)}")
        if not name:
            raise ValueError(f"expects a non-empty string but received {name}")

    def validate_tokens(self, tokens):
        if not isinstance(tokens, list):
            raise TypeError(f"expects a list but received {type(tokens)}")
        if not tokens:
            raise ValueError(f"expects a non-empty list but received {tokens}")

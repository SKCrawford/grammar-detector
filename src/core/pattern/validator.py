from src.util.decorator import is_truthy, is_type


def validate_pattern(name, tokens):
    """Validate attributes of a potential pattern.

    Given a string and a list<token>, return void.
    """
    _validate_name(name)
    _validate_tokens(tokens)


@is_type(str)
@is_truthy
def _validate_name(name):
    pass


@is_type(list)
@is_truthy
def _validate_tokens(tokens):
    pass

from src.util.decorator import is_truthy, is_type


@is_type(str)
@is_truthy
def validate_verb(verb):
    pass

from src.util.decorator import is_in_enum, is_truthy, is_type
from .enum import Voice


@is_type(str)
@is_truthy
@is_in_enum(Voice)
def validate_voice(verb):
    pass

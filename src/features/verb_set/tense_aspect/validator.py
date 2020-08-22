from src.util.decorator import is_in_enum, is_truthy, is_type
from .enum import Aspect, Tense


@is_type(str)
@is_truthy
@is_in_enum(Aspect)
def validate_aspect(aspect):
    pass


@is_type(str)
@is_truthy
@is_in_enum(Tense)
def validate_tense(tense):
    pass

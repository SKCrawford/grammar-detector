from src.util.decorator import is_truthy, is_type
from .model import NounFeature


@is_type(NounFeature)
@is_truthy
def validate_noun(value):
    pass

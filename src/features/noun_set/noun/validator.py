from src.util.decorator import is_truthy, is_type
from .model import Noun


@is_type(Noun)
@is_truthy
def validate_noun(noun):
    pass

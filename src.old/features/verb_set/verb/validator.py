from src.util.decorator import is_truthy, is_type
from .model import VerbFeature


@is_type(VerbFeature)
@is_truthy
def validate_verb_feature(feature):
    _validate_verb_text(feature.phrase)


@is_type(str)
@is_truthy
def _validate_verb_text(value):
    pass

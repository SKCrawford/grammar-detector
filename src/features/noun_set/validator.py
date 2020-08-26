from src.util.decorator import is_truthy, is_type
from .model import NounFeatureSet


@is_type(NounFeatureSet)
@is_truthy
def validate_noun_feature_set(feature_set):
    """Validate a NounFeatureSet instance.

    Given a NounFeatureSet instance, return void.
    """
    pass

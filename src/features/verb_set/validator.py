from src.util.decorator import is_truthy, is_type
from .model import VerbFeatureSet


@is_type(VerbFeatureSet)
@is_truthy
def validate_verb_feature_set(feature_set):
    """Validate a VerbFeatureSet instance.

    Given a VerbFeatureSet instance, return void.
    """
    pass

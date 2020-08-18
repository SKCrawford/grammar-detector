from src.util.decorator import is_in_enum, is_truthy, is_type
from .enum.Aspect import Aspect
from .enum.Tense import Tense


def validate_verb_feature_set(feature_set):
    """Validate a VerbFeatureSet instance.
    
    Given a VerbFeatureSet instance, return void.
    """
    _validate_verb(feature_set.verb)
    _validate_tense(feature_set.tense)
    _validate_aspect(feature_set.aspect)


@is_type(str)
@is_truthy
def _validate_verb(verb):
    pass


@is_type(str)
@is_truthy
@is_in_enum(Tense)
def _validate_tense(tense):
    pass


@is_type(str)
@is_truthy
@is_in_enum(Aspect)
def _validate_aspect(aspect):
    pass

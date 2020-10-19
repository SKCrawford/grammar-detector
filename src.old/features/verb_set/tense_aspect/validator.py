from src.util.decorator import is_in_enum, is_truthy, is_type
from .enum import Aspect, Tense
from .model import TenseAspectFeature


@is_type(TenseAspectFeature)
@is_truthy
def validate_tense_aspect_feature(feature):
    validate_tense(feature.value["tense"])
    validate_aspect(feature.value["aspect"])


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

from src.util.decorator import is_in_enum, is_truthy, is_type
from .enum import Person
from .model import PersonFeature


@is_type(PersonFeature)
@is_truthy
def validate_person_feature(feature):
    _validate_person(feature.value)


@is_type(str)
@is_truthy
@is_in_enum(Person)
def _validate_person(value):
    pass

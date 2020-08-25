from src.util.decorator import is_in_enum, is_truthy, is_type
from .enum import Person


@is_type(str)
@is_truthy
@is_in_enum(Person)
def validate_person(verb):
    pass

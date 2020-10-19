from enum import Enum


class Person(Enum):
    """All possible English persons, as in the first person, the second
    person, and the third person."""

    FIRST = "first"
    SECOND = "second"
    THIRD = "third"
    UNKNOWN = "???"

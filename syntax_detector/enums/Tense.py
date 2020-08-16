from enum import Enum


class Tense(Enum):
    """All possible English verb tenses (without the aspect)."""

    PAST = "past"
    PRESENT = "present"
    FUTURE = "future"

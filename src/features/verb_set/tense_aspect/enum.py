from enum import Enum


class Aspect(Enum):
    """All possible English verb aspects."""

    SIMPLE = "simple"
    PERF = "perfect"
    CONT = "continuous"
    PERF_CONT = "perfect continuous"
    UNKNOWN = "???"


class Tense(Enum):
    """All possible English verb tenses (without the aspect)."""

    PAST = "past"
    PRESENT = "present"
    FUTURE = "future"
    UNKNOWN = "???"

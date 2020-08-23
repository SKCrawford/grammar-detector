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


class TenseAspect(Enum):
    """All possible English verb tenses and aspects."""

    PRESENT_SIMPLE = "present simple"
    PRESENT_SIMPLE_3 = "present simple 3rd"
    PAST_SIMPLE = "past simple"
    FUTURE_SIMPLE = "future simple"
    FUTURE_SIMPLE_WILL = "future simple will"
    FUTURE_SIMPLE_BE_GOING_TO = "future simple be-going-to"
    FUTURE_SIMPLE_BE_GOING_TO_3 = "future simple be-going-to 3rd"
    PRESENT_CONT = "present continuous"
    PRESENT_CONT_3 = "present continuous 3rd"
    PAST_CONT = "past continuous"
    FUTURE_CONT = "future continuous"
    PRESENT_PERF = "present perfect"
    PRESENT_PERF_3 = "present perfect 3rd"
    PAST_PERF = "past perfect"
    FUTURE_PERF = "future perfect"
    PRESENT_PERF_CONT = "present perfect continuous"
    PRESENT_PERF_CONT_3 = "present perfect continuous 3rd"
    PAST_PERF_CONT = "past perfect continuous"
    FUTURE_PERF_CONT = "future perfect continuous"
    UNKNOWN = "???"

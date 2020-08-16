from enum import Enum


class Aspect(Enum):
    """All possible English verb aspects."""

    SIMPLE = "simple"
    PERF = "perfect"
    CONT = "continuous"
    PERF_CONT = "perfect continuous"

import logging
from enum import Enum, IntEnum
from src.core import match_by_pattern


logger = logging.getLogger(__name__)


class Transitivity(Enum):
    """All possible English verb transitivity categories."""

    IMPERSONAL = "impersonal"
    INTRANSITIVE = "intransitive"
    TRANSITIVE = "transitive"
    DITRANSITIVE = "ditransitive"


class Valency(IntEnum):
    """All possible English verb valencies of the transitivity categories."""

    IMPERSONAL = 0
    INTRANSITIVE = 1
    TRANSITIVE = 2
    DITRANSITIVE = 3


def determine_valency(transitivity):
    """Given a string, return a non-negative int."""
    logger.debug(f"Determining the valency of a(n) `{transitivity}` verb")
    if transitivity == Transitivity.IMPERSONAL.value:
        return Valency.IMPERSONAL.value
    elif transitivity == Transitivity.INTRANSITIVE.value:
        return Valency.INTRANSITIVE.value
    elif transitivity == Transitivity.TRANSITIVE.value:
        return Valency.TRANSITIVE.value
    elif transitivity == Transitivity.DITRANSITIVE.value:
        return Valency.DITRANSITIVE.value
    else:
        msg = f"Could not determine the valency of a(n) `{transitivity}` verb"
        logger.error(msg)
        raise ValueError(msg)


def detect_verb_transitivity(maybe_tokenized):
    """Detect a verb's transitivity and valency. This detector cannot yet
    distinguish between [dobj] [*] [pobj] and [dobj] [prep] [pobj]. This means that
    these verbs are identified as ditransitive:
    * Correct: She played a round with him. ([dobj] [prep "with"] [pobj])
    * Incorrect: She played a long game of basketball. ([dobj] [prep "of"] [pobj])

    Given a string, Doc, or Span, return a tuple of (string, int).
    """
    logger.debug("Started detecting")
    matches = match_by_pattern("transitivity", maybe_tokenized)

    transitivity = None
    valency = None
    if matches:
        (transitivity, span) = matches[-1]
    if transitivity is not None:
        valency = determine_valency(transitivity)
    return (transitivity, valency)

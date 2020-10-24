import logging
import re
from enum import Enum
from src.core import match_by_pattern
from src.util.validator import is_in_enum, is_truthy, is_type


logger = logging.getLogger(__name__)


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

    # Active voice
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

    # Passive voice
    PRESENT_SIMPLE_PASSIVE = "present simple passive"
    PRESENT_SIMPLE_3_PASSIVE = "present simple 3rd passive"
    PAST_SIMPLE_PASSIVE = "past simple passive"
    FUTURE_SIMPLE_PASSIVE = "future simple passive"
    FUTURE_SIMPLE_WILL_PASSIVE = "future simple will passive"
    FUTURE_SIMPLE_BE_GOING_TO_PASSIVE = "future simple be-going-to passive"
    FUTURE_SIMPLE_BE_GOING_TO_3_PASSIVE = "future simple be-going-to 3rd passive"
    PRESENT_CONT_PASSIVE = "present continuous passive"
    PRESENT_CONT_3_PASSIVE = "present continuous 3rd passive"
    PAST_CONT_PASSIVE = "past continuous passive"
    FUTURE_CONT_PASSIVE = "future continuous passive"
    PRESENT_PERF_PASSIVE = "present perfect passive"
    PRESENT_PERF_3_PASSIVE = "present perfect 3rd passive"
    PAST_PERF_PASSIVE = "past perfect passive"
    FUTURE_PERF_PASSIVE = "future perfect passive"
    PRESENT_PERF_CONT_PASSIVE = "present perfect continuous passive"
    PRESENT_PERF_CONT_3_PASSIVE = "present perfect continuous 3rd passive"
    PAST_PERF_CONT_PASSIVE = "past perfect continuous passive"
    FUTURE_PERF_CONT_PASSIVE = "future perfect continuous passive"
    UNKNOWN = "???"


def is_verb_tense_aspect(tense_aspect):
    is_type(tense_aspect, str)
    is_truthy(tense_aspect)
    is_in_enum(tense_aspect, TenseAspect)


def is_verb_tense(tense):
    is_type(tense, str)
    is_truthy(tense)
    is_in_enum(tense, Tense)


def is_verb_aspect(aspect):
    is_type(aspect, str)
    is_truthy(aspect)
    is_in_enum(aspect, Aspect)


def extract_tense_aspect(verb_tense):
    """Determine the tense and aspect of a verb tense phrase. For example
    'future perfect continuous' should return ('future', 'perfect continuous').
    Irrelevant features, such as person or descriptors, are removed. For example,
    'future simple be-going-to' should return ('future', 'simple').

    Given a string, return a tuple of (string, string).
    """
    tense = ""
    aspect = ""
    reg = r"(present|past|future)\s(simple|perfect continuous|perfect|continuous)"
    match = re.match(reg, verb_tense)
    if match:
        tense = match.group(1).strip()
        aspect = match.group(2).strip()
    return (tense, aspect)


def detect_verb_tense_aspect(maybe_tokenized):
    logger.debug("Started detecting")
    matches = match_by_pattern("tense_aspects", maybe_tokenized)
    (tense_aspect, span) = matches[0]
    is_verb_tense_aspect(tense_aspect)

    (tense, aspect) = extract_tense_aspect(tense_aspect)
    is_verb_tense(tense)
    is_verb_aspect(aspect)
    return (tense, aspect)
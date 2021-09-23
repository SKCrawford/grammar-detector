import asyncio
import logging
from enum import Enum
from src.core import extract_span_features, match_by_pattern
from src.util.validator import is_in_enum, is_truthy, is_type
from .tense_aspect import detect_verb_tense_aspect
from .transitivity import detect_verb_transitivity
from .voice import detect_verb_voice


logger = logging.getLogger(__name__)


class Verbial(Enum):
    """All possible verbial parts of speech."""

    AUX = "AUX" # POS "AUX" can be DEP "ROOT"
    VERB = "VERB"


def is_verb(verb):
    is_truthy(verb)
    is_in_enum(verb["pos"], Verbial)


async def detect_verbs(maybe_tokenized):
    logger.debug("Started detecting")
    matches = await match_by_pattern("tense_aspects", maybe_tokenized)
    verbs = []
    for (_, match_span) in matches:
        (tense, aspect), (transitivity, valency), voice = await asyncio.gather(
            detect_verb_tense_aspect(match_span),
            detect_verb_transitivity(maybe_tokenized),
            detect_verb_voice(match_span),
        )

        verb = extract_span_features(match_span)
        verb["tense"] = tense
        verb["aspect"] = aspect
        verb["voice"] = voice
        verb["transitivity"] = transitivity
        verb["valency"] = valency
        is_verb(verb)
        verbs.append(verb)
    return verbs

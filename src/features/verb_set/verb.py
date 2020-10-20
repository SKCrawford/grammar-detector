import logging
from src.core import match_by_pattern, parse_phrase_features_from_chunk
from src.util.serializable import Serializable
from .tense_aspect import detect_verb_tense_aspect
from .voice import detect_verb_voice


logger = logging.getLogger(__name__)


def detect_verbs(maybe_tokenized):
    logger.debug("Started detecting")
    matches = match_by_pattern("tense_aspects", maybe_tokenized)
    verbs = []
    for (tense_aspect, span) in matches:
        (tense, aspect) = detect_verb_tense_aspect(span)
        voice = detect_verb_voice(span)
        phrase_features = parse_phrase_features_from_chunk(span)

        verb = Serializable()           \
            .copy_dict(phrase_features) \
            .set("tense", tense)        \
            .set("aspect", aspect)      \
            .set("voice", voice)
        verbs.append(verb)
    return verbs

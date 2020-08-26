from src.util.spacy import run_matcher
from .matcher import create_verb_voice_matcher
from .validator import validate_voice


def detect_verb_voice(sentence_or_doc):
    matcher = create_verb_voice_matcher()
    match = run_matcher(matcher, sentence_or_doc)

    if not match:
        return ""
    (voice, verb_span) = match
    validate_voice(voice)
    return voice

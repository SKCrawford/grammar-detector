from src.util.matcher import run_matcher
from src.util.transformer import make_doc
from .matcher import create_verb_voice_matcher
from .validator import validate_voice


def detect_verb_voice(sentence_or_doc):
    doc = make_doc(sentence_or_doc)
    matcher = create_verb_voice_matcher()
    match = run_matcher(matcher, doc)

    if not match:
        return ""
    (voice, verb_span) = match
    validate_voice(voice)
    return voice

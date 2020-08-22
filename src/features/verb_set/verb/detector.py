from src.util.matcher import run_matcher
from src.util.transformer import make_doc
from ..matcher import create_verb_tense_matcher
from .validator import validate_verb


def detect_verb(sentence_or_doc):
    doc = make_doc(sentence_or_doc)
    matcher = create_verb_tense_matcher()
    match = run_matcher(matcher, doc)

    (rulename, verb_span) = match
    verb = verb_span.text
    validate_verb(verb)
    return verb_span.text

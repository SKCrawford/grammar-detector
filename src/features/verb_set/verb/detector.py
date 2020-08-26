from src.util.spacy import run_matcher
from .matcher import create_verb_matcher
from .validator import validate_verb


def detect_verb(sentence_or_doc):
    matcher = create_verb_matcher()
    match = run_matcher(matcher, sentence_or_doc)

    if not match:
        return ""
    (rulename, verb_span) = match
    verb = verb_span.text
    validate_verb(verb)
    return verb_span.text

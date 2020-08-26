from src.util.spacy import run_matcher
from .matcher import create_verb_tense_aspect_matcher
from .transformer import extract_tense_aspect
from .validator import validate_aspect, validate_tense


def detect_verb_tense_aspect(sentence_or_doc):
    matcher = create_verb_tense_aspect_matcher()
    match = run_matcher(matcher, sentence_or_doc)

    if not match:
        return ("", "")
    (verb_tense, verb_span) = match
    (tense, aspect) = extract_tense_aspect(verb_tense)

    validate_tense(tense)
    validate_aspect(aspect)
    return (tense, aspect)

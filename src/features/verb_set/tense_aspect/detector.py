from src.util.spacy import run_matcher
from .matcher import create_verb_tense_aspect_matcher
from .transformer import extract_tense_aspect
from .validator import validate_aspect, validate_tense


def detect_verb_tense_aspect(maybe_tokenized):
    matcher = create_verb_tense_aspect_matcher()
    match = run_matcher(matcher, maybe_tokenized)

    # TODO fix match vs matches b/c of run_matcher refactor
    if not match:
        return ("", "")
    (verb_tense, verb_span) = match[0]
    (tense, aspect) = extract_tense_aspect(verb_tense)

    validate_tense(tense)
    validate_aspect(aspect)
    return (tense, aspect)

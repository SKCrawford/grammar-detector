from src.util.matcher import run_matcher
from src.util.transformer import make_doc, split_words_into_first_and_rest
from ..matcher import create_verb_tense_matcher
from .validator import validate_tense


def detect_verb_tense(sentence_or_doc):
    doc = make_doc(sentence_or_doc)
    matcher = create_verb_tense_matcher()
    match = run_matcher(matcher, doc)

    (verb_tense, verb_span) = match
    (tense, aspect) = split_words_into_first_and_rest(verb_tense)
    validate_tense(tense)
    return tense

from src.util.matcher import run_matcher
from src.util.transformer import make_doc
from .matcher import create_noun_matcher
from .validator import validate_noun


def detect_nouns(sentence_or_doc):
    doc = make_doc(sentence_or_doc)
    matcher = create_noun_matcher()
    match = run_matcher(matcher, doc)
    print(match)

    if not match:
        return ""
    (rulename, noun_span) = match
    noun = noun_span.text
    validate_noun(noun)
    return noun

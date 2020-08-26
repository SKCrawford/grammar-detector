from src.util.matcher import run_matcher
from src.util.transformer import make_doc
from .matcher import create_verb_lemma_matcher
from .validator import validate_lemma_phrase


def detect_verb_lemmas(sentence_or_doc):
    doc = make_doc(sentence_or_doc)
    matcher = create_verb_lemma_matcher()
    match = run_matcher(matcher, doc)

    if not match:
        return ""
    (verb_tense, verb_span) = match
    lemmas = [word.lemma_ for word in verb_span]
    lemma_phrase = " ".join(lemmas)
    validate_lemma_phrase(lemma_phrase)
    return lemma_phrase

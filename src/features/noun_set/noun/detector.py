from src.util.transformer import make_doc
from .transformer import extract_features_from_noun_chunk
from .validator import validate_noun


def detect_nouns(sentence_or_doc):
    doc = make_doc(sentence_or_doc)
    nouns = []
    for noun_chunk in doc.noun_chunks:
        noun = extract_features_from_noun_chunk(noun_chunk)
        validate_noun(noun)
        nouns.append(noun)
    return nouns

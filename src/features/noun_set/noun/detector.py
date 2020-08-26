from spacy import explain
from src.util.transformer import make_doc
from .model import Noun
from .transformer import extract_features_from_noun_chunk
from .validator import validate_noun


def detect_nouns(sentence_or_doc):
    doc = make_doc(sentence_or_doc)
    nouns = []
    for noun_chunk in doc.noun_chunks:
        noun = Noun()
        features = extract_features_from_noun_chunk(noun_chunk)

        for feature_name in features:
            setattr(noun, feature_name, features[feature_name])
        validate_noun(noun)
        nouns.append(noun)
    return nouns

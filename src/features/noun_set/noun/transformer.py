from spacy import explain
from .model import Noun


def extract_features_from_noun_chunk(noun_chunk):
    features = {}
    features["text"] = noun_chunk.text
    features["root_text"] = noun_chunk.root.text
    features["root_head_text"]= noun_chunk.root.head.text
    features["pos"] = noun_chunk.root.pos_
    features["tag"] = noun_chunk.root.tag_
    features["dep"] = noun_chunk.root.dep_
    features["lemmas"] = noun_chunk.lemma_
    features["root_lemma"] = noun_chunk.root.lemma_
    features["pos_desc"] = explain(noun_chunk.root.pos_)
    features["tag_desc"] = explain(noun_chunk.root.tag_)
    features["dep_desc"] = explain(noun_chunk.root.dep_)

    test_noun = Noun()
    for key in features:
        if not hasattr(test_noun, key):
            raise ValueError(f"feature got invalid attribute {key}")
    return features

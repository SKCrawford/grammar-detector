from spacy import explain


def parse_phrase_features_from_chunk(chunk):
    features = {}
    features["phrase"] = chunk.text
    features["root"] = chunk.root.text
    features["root_head"] = chunk.root.head.text
    features["pos"] = chunk.root.pos_
    features["tag"] = chunk.root.tag_
    features["dep"] = chunk.root.dep_
    features["phrase_lemma"] = chunk.lemma_
    features["root_lemma"] = chunk.root.lemma_
    features["pos_desc"] = explain(chunk.root.pos_)
    features["tag_desc"] = explain(chunk.root.tag_)
    features["dep_desc"] = explain(chunk.root.dep_)
    return features

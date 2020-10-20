import logging
from spacy import explain


def parse_phrase_features_from_chunk(chunk):
    logger = logging.getLogger(parse_phrase_features_from_chunk.__name__)
    logger.info(f"Parsing `{chunk}`")
    return {
        "phrase": chunk.text,
        "root": chunk.root.text,
        "root_head": chunk.root.head.text,
        "pos": chunk.root.pos_,
        "tag": chunk.root.tag_,
        "dep": chunk.root.dep_,
        "phrase_lemma": chunk.lemma_,
        "root_lemma": chunk.root.lemma_,
        "pos_desc": explain(chunk.root.pos_),
        "tag_desc": explain(chunk.root.tag_),
        "dep_desc": explain(chunk.root.dep_),
    }

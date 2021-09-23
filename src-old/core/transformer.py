import logging
from spacy import explain


def extract_span_features(match_span):
    logging.getLogger(__name__).info(f"Parsing `{match_span}`")
    return {
        "span": match_span,
        "phrase": match_span.text,
        "root": match_span.root.text,
        "root_head": match_span.root.head.text,
        "pos": match_span.root.pos_,
        "tag": match_span.root.tag_,
        "dep": match_span.root.dep_,
        "phrase_lemma": match_span.lemma_,
        "root_lemma": match_span.root.lemma_,
        "pos_desc": explain(match_span.root.pos_),
        "tag_desc": explain(match_span.root.tag_),
        "dep_desc": explain(match_span.root.dep_),
    }

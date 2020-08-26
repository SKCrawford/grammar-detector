from spacy import explain
from .model import NounFeature


def extract_features_from_noun_chunk(noun_chunk):
    noun = NounFeature()
    noun.phrase = noun_chunk.text
    noun.root = noun_chunk.root.text
    noun.root_head = noun_chunk.root.head.text
    noun.pos = noun_chunk.root.pos_
    noun.tag = noun_chunk.root.tag_
    noun.dep = noun_chunk.root.dep_
    noun.phrase_lemma = noun_chunk.lemma_
    noun.root_lemma = noun_chunk.root.lemma_
    noun.pos_desc = explain(noun_chunk.root.pos_)
    noun.tag_desc = explain(noun_chunk.root.tag_)
    noun.dep_desc = explain(noun_chunk.root.dep_)
    return noun

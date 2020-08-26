from spacy import explain
from src.util.builder import Builder
from .model import NounFeature


def extract_features_from_noun_chunk(noun_chunk):
    return Builder(NounFeature)                                 \
        .set_attr("phrase", noun_chunk.text)                    \
        .set_attr("root", noun_chunk.root.text)                 \
        .set_attr("root_head", noun_chunk.root.head.text)       \
        .set_attr("pos", noun_chunk.root.pos_)                  \
        .set_attr("tag", noun_chunk.root.tag_)                  \
        .set_attr("dep", noun_chunk.root.dep_)                  \
        .set_attr("phrase_lemma", noun_chunk.lemma_)            \
        .set_attr("root_lemma", noun_chunk.root.lemma_)         \
        .set_attr("pos_desc", explain(noun_chunk.root.pos_))    \
        .set_attr("tag_desc", explain(noun_chunk.root.tag_))    \
        .set_attr("dep_desc", explain(noun_chunk.root.dep_))    \
        .build()

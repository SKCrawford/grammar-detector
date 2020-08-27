from src.core.pattern.factory import PatternSetFactory


def create_verb_tense_aspect_pattern_set():
    return PatternSetFactory()          \
        .set_json_key("tense_aspects")  \
        .set_name("verb tenses")        \
        .build()                        \

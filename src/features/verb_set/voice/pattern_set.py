from src.core.pattern.factory import PatternSetFactory


def create_verb_voice_pattern_set():
    """ Return a pattern set related to verb voices.

    Given void, return a PatternSet instance.
    """
    return PatternSetFactory()      \
        .set_json_key("voices")     \
        .set_name("voice")          \
        .build()

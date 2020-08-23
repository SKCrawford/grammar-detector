from src.core.pattern.model import PatternSet
from src.SyntaxPatterns import SyntaxPatterns


def create_verb_voice_pattern_set():
    """ Return a pattern set related to verb voices.

    Given void, return a PatternSet instance.
    """
    voice_patterns = SyntaxPatterns().patterns["voices"]
    p_set = PatternSet("voice")
    for name in voice_patterns:
        tokens = voice_patterns[name]
        p_set.create(name, tokens)
    return p_set

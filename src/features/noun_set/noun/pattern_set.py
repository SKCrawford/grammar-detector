from src.core.pattern.model import PatternSet
from src.SyntaxPatterns import SyntaxPatterns


def create_noun_pattern_set():
    """ Return a pattern set related to nouns.

    Given void, return a PatternSet instance.
    """
    person_patterns = SyntaxPatterns().patterns[""]
    p_set = PatternSet("")
    for name in person_patterns:
        tokens = person_patterns[name]
        p_set.create(name, tokens)
    return p_set

from src.core.pattern.model import PatternSet
from src.SyntaxPatterns import SyntaxPatterns


def create_verb_person_pattern_set():
    """ Return a pattern set related to verb persons.

    Given void, return a PatternSet instance.
    """
    person_patterns = SyntaxPatterns().patterns["persons"]
    p_set = PatternSet("person")
    for name in person_patterns:
        tokens = person_patterns[name]
        p_set.create(name, tokens)
    return p_set

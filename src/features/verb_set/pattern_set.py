from src.core.pattern.model import PatternSet
from src.SyntaxPatterns import SyntaxPatterns


def create_verb_tense_pattern_set():
    """ Return a pattern set related to verb tenses.

    Given void, return a PatternSet instance.
    """
    tense_aspects = SyntaxPatterns().patterns["tense_aspects"]
    p_set = PatternSet("verb tenses")
    for name in tense_aspects:
        tokens = tense_aspects[name]
        p_set.create(name, tokens)
    return p_set

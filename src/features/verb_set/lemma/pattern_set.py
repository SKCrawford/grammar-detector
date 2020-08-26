from src.core.pattern.model import PatternSet
from src.SyntaxPatterns import SyntaxPatterns
from ..pattern_set import create_verb_feature_set_pattern_set


def create_verb_lemma_pattern_set():
    """ Return a pattern set related to verb lemmas.

    Given void, return a PatternSet instance.
    """
    return create_verb_feature_set_pattern_set()

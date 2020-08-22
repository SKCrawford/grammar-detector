from src.core.pattern.matcher import PatternSetMatcher
from .pattern_set import create_verb_tense_pattern_set


def create_verb_tense_matcher():
    """Create the matcher pre-formatted for detecting verb features.

    Given void, return the PatternSetMatcher instance.
    """
    return PatternSetMatcher(create_verb_tense_pattern_set())

from src.core.pattern.matcher import PatternSetMatcher
from .pattern_set import create_noun_person_pattern_set


def create_noun_person_matcher():
    """Create the matcher pre-formatted for detecting noun person.

    Given void, return the PatternSetMatcher instance.
    """
    return PatternSetMatcher(create_noun_person_pattern_set())

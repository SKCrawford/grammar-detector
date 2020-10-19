from src.core.pattern.matcher import PatternSetMatcher
from .pattern_set import create_verb_voice_pattern_set


def create_verb_voice_matcher():
    """Create the matcher pre-formatted for detecting verb voice.

    Given void, return the PatternSetMatcher instance.
    """
    return PatternSetMatcher(create_verb_voice_pattern_set())

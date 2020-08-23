from src.core.pattern.matcher import PatternSetMatcher
from .pattern_set import create_verb_tense_aspect_pattern_set


def create_verb_tense_aspect_matcher():
    return PatternSetMatcher(create_verb_tense_aspect_pattern_set())

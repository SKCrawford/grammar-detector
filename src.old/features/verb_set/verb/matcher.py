from src.core.pattern.matcher import PatternSetMatcher
from .pattern_set import create_verb_pattern_set


def create_verb_matcher():
    return PatternSetMatcher(create_verb_pattern_set())

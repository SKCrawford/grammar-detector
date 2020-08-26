from src.core.pattern.matcher import PatternSetMatcher
from .pattern_set import create_noun_pattern_set


def create_noun_matcher():
    return PatternSetMatcher(create_noun_pattern_set())

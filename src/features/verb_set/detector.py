from src.core.pattern.matcher import PatternSetMatcher
from src.nlp import nlp
from src.util.validator import is_truthy, is_type
from .factory import VerbFeatureSetFactory
from .pattern_set import create_verb_tense_pattern_set
from .validator import validate_verb_feature_set


def detect_verb_features(sentence):
    """Detect the features of a sentence's verb. Currently detects tense and aspect.

    Given a string, return a VerbFeatureSet instance.
    """
    is_type(sentence, str)
    is_truthy(sentence)

    doc = nlp(sentence)
    matcher = PatternSetMatcher(create_verb_tense_pattern_set())
    matches = matcher(doc)
    if not matches:
        return None
    match = matcher.best_match(doc, matches)

    verb_f_set = VerbFeatureSetFactory(match).build()
    validate_verb_feature_set(verb_f_set)
    return verb_f_set

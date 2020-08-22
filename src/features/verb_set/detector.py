from src.core.pattern.matcher import PatternSetMatcher
from src.nlp import nlp
from src.util.validator import is_truthy, is_type
from .builder import VerbFeatureSetBuilder
from .pattern_set import create_verb_tense_pattern_set
from .validator import validate_verb_feature_set


def _extract_verb_and_tense_from_match(match):
    """Returns a tuple of (verb, verb_tense). Note the difference between
    verb_tense, tense, and aspect. Here's an example:
        verb_tense = "future perfect continuous"
        tense = "future"
        aspect = "perfect continuous"

    Given a Match instance, returns a tuple of (string, string).
    """
    verb = ""
    (verb_tense, verb_span) = match
    if verb_span and verb_span.text:
        verb = verb_span.text
    return (verb, verb_tense)


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

    (verb, verb_tense) = _extract_verb_and_tense_from_match(match)
    builder = VerbFeatureSetBuilder()
    verb_f_set = builder.spawn()                \
        .set_verb(verb)                         \
        .derive_tense_and_aspect(verb_tense)    \
        .build()
    validate_verb_feature_set(verb_f_set)
    return verb_f_set

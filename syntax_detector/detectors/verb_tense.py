from ..models.PatternSetMatcher import PatternSetMatcher
from ..nlp import nlp
from ..pattern_sets.verb_tense import verb_tense_pattern_set


def detect_verb_tense(sentence):
    """Return a sentence's verb and its tense.

    Given a string, return a tuple of (rulename, span).
    """
    if not isinstance(sentence, str):
        raise TypeError("arg[0] is not a string")

    if not bool(sentence):
        raise ValueError("arg[0] is not truthy")

    doc = nlp(sentence)
    matcher = PatternSetMatcher(verb_tense_pattern_set)
    matches = matcher(doc)

    if not matches:
        return None

    (rulename, span) = matcher.best_match(doc, matches)
    return (rulename, span)

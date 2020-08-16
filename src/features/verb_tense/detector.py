import re
from src.nlp import nlp
from ..core.model.PatternSetMatcher import PatternSetMatcher
from .pattern_set import verb_tense_pattern_set


# Words with simple only
segment_verb_tense_pattern = r"^([\w]+)\s([\w]+)\s([\w]+)"


#  segment_verb_tense_pattern = r"^(\w+)\s(\w+)[\s(\w+)]$"
#  segment_verb_tense_pattern = r"^(\w+)\s(\w+)$"


def segment_verb_tense(verb_tense):
    tense = "???"
    aspect = "???"
    person = "???"

    match = re.search(segment_verb_tense_pattern, verb_tense)
    print("Match found:", bool(match))
    if match:
        tense = match.group(1)
        aspect = match.group(2)
        person = match.group(3)

    return (tense, aspect, person)


def detect_verb_features(sentence):
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

    (verb_tense, verb_span) = matcher.best_match(doc, matches)
    (tense, aspect, is_third_person) = segment_verb_tense(verb_tense)
    verb = verb_span.text
    return (tense, aspect, is_third_person, verb)
